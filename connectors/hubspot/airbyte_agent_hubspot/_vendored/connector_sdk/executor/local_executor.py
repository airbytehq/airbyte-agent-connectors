"""Local executor for direct HTTP execution of connector operations."""

from __future__ import annotations

import asyncio
import inspect
import logging
import os
import re
import time
from collections.abc import AsyncIterator
from typing import Any, Protocol
from urllib.parse import quote

from jinja2 import Environment, StrictUndefined
from jsonpath_ng import parse as parse_jsonpath
from opentelemetry import trace

from ..auth_template import apply_auth_mapping
from ..connector_model_loader import load_connector_model
from ..constants import (
    DEFAULT_MAX_CONNECTIONS,
    DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
)
from ..http_client import HTTPClient, TokenRefreshCallback
from ..logging import NullLogger, RequestLogger
from ..observability import ObservabilitySession
from ..schema.extensions import RetryConfig
from ..secrets import SecretStr
from ..telemetry import SegmentTracker
from ..types import (
    Action,
    AuthConfig,
    AuthOption,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)

from .models import (
    ActionNotSupportedError,
    EntityNotFoundError,
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    InvalidParameterError,
    MissingParameterError,
    StandardExecuteResult,
)


class _OperationContext:
    """Shared context for operation handlers."""

    def __init__(self, executor: LocalExecutor):
        self.executor = executor
        self.http_client = executor.http_client
        self.tracker = executor.tracker
        self.session = executor.session
        self.logger = executor.logger
        self.entity_index = executor._entity_index
        self.operation_index = executor._operation_index
        # Bind helper methods
        self.build_path = executor._build_path
        self.extract_query_params = executor._extract_query_params
        self.extract_body = executor._extract_body
        self.extract_header_params = executor._extract_header_params
        self.build_request_body = executor._build_request_body
        self.determine_request_format = executor._determine_request_format
        self.validate_required_body_fields = executor._validate_required_body_fields
        self.extract_records = executor._extract_records

    @property
    def standard_handler(self) -> _StandardOperationHandler | None:
        """Return the standard operation handler, or None if not registered."""
        for h in self.executor._operation_handlers:
            if isinstance(h, _StandardOperationHandler):
                return h
        return None


class _OperationHandler(Protocol):
    """Protocol for operation handlers."""

    def can_handle(self, action: Action) -> bool:
        """Check if this handler can handle the given action."""
        ...

    async def execute_operation(
        self,
        entity: str,
        action: Action,
        params: dict[str, Any],
    ) -> StandardExecuteResult | AsyncIterator[bytes]:
        """Execute the operation and return result.

        Returns:
            StandardExecuteResult for standard operations (GET, LIST, CREATE, etc.)
            AsyncIterator[bytes] for download operations
        """
        ...


class LocalExecutor:
    """Async executor for Entity×Action operations with direct HTTP execution.

    This is the "local mode" executor that makes direct HTTP calls to external APIs.
    It performs local entity/action lookups, validation, and request building.

    Implements ExecutorProtocol.
    """

    def __init__(
        self,
        config_path: str | None = None,
        model: ConnectorModel | None = None,
        secrets: dict[str, SecretStr] | None = None,
        auth_config: dict[str, SecretStr] | None = None,
        auth_scheme: str | None = None,
        enable_logging: bool = False,
        log_file: str | None = None,
        execution_context: str | None = None,
        max_connections: int = DEFAULT_MAX_CONNECTIONS,
        max_keepalive_connections: int = DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
        max_logs: int | None = 10000,
        config_values: dict[str, str] | None = None,
        on_token_refresh: TokenRefreshCallback = None,
        retry_config: RetryConfig | None = None,
    ):
        """Initialize async executor.

        Args:
            config_path: Path to connector.yaml.
                If neither config_path nor model is provided, an error will be raised.
            model: ConnectorModel object to execute.
            secrets: (Legacy) Auth parameters that bypass x-airbyte-auth-config mapping.
                Directly passed to auth strategies (e.g., {"username": "...", "password": "..."}).
                Cannot be used together with auth_config.
            auth_config: User-facing auth configuration following x-airbyte-auth-config spec.
                Will be transformed via auth_mapping to produce auth parameters.
                Cannot be used together with secrets.
            auth_scheme: (Multi-auth only) Explicit security scheme name to use.
                If None, SDK will auto-select based on provided credentials.
                Example: auth_scheme="githubOAuth"
            enable_logging: Enable request/response logging
            log_file: Path to log file (if enable_logging=True)
            execution_context: Execution context (mcp, direct, blessed, agent)
            max_connections: Maximum number of concurrent connections
            max_keepalive_connections: Maximum number of keepalive connections
            max_logs: Maximum number of logs to keep in memory before rotation.
                Set to None for unlimited (not recommended for production).
                Defaults to 10000.
            config_values: Optional dict of config values for server variable substitution
                (e.g., {"subdomain": "acme"} for URLs like https://{subdomain}.api.example.com).
            on_token_refresh: Optional callback function(new_tokens: dict) called when
                OAuth2 tokens are refreshed. Use this to persist updated tokens.
                Can be sync or async. Example: lambda tokens: save_to_db(tokens)
            retry_config: Optional retry configuration override. If provided, overrides
                the connector.yaml x-airbyte-retry-config. If None, uses connector.yaml
                config or SDK defaults.
        """
        # Validate mutual exclusivity of secrets and auth_config
        if secrets is not None and auth_config is not None:
            raise ValueError(
                "Cannot provide both 'secrets' and 'auth_config' parameters. "
                "Use 'auth_config' for user-facing credentials (recommended), "
                "or 'secrets' for direct auth parameters (legacy)."
            )

        # Validate mutual exclusivity of config_path and model
        if config_path is not None and model is not None:
            raise ValueError("Cannot provide both 'config_path' and 'model' parameters.")

        if config_path is None and model is None:
            raise ValueError("Must provide either 'config_path' or 'model' parameter.")

        # Load model from path or use provided model
        if config_path is not None:
            self.model: ConnectorModel = load_connector_model(config_path)
        else:
            self.model: ConnectorModel = model

        self.on_token_refresh = on_token_refresh
        self.config_values = config_values or {}

        # Handle auth selection for multi-auth or single-auth connectors
        user_credentials = auth_config if auth_config is not None else secrets
        selected_auth_config, self.secrets = self._initialize_auth(user_credentials, auth_scheme)

        # Create shared observability session
        self.session = ObservabilitySession(
            connector_name=self.model.name,
            connector_version=getattr(self.model, "version", None),
            execution_context=(execution_context or os.getenv("AIRBYTE_EXECUTION_CONTEXT", "direct")),
        )

        # Initialize telemetry tracker
        self.tracker = SegmentTracker(self.session)
        self.tracker.track_connector_init(connector_version=getattr(self.model, "version", None))

        # Initialize logger
        if enable_logging:
            self.logger = RequestLogger(
                log_file=log_file,
                connector_name=self.model.name,
                max_logs=max_logs,
            )
        else:
            self.logger = NullLogger()

        # Initialize async HTTP client with connection pooling
        self.http_client = HTTPClient(
            base_url=self.model.base_url,
            auth_config=selected_auth_config,
            secrets=self.secrets,
            config_values=self.config_values,
            logger=self.logger,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            on_token_refresh=on_token_refresh,
            retry_config=retry_config or self.model.retry_config,
        )

        # Build O(1) lookup indexes
        self._entity_index: dict[str, EntityDefinition] = {entity.name: entity for entity in self.model.entities}

        # Build O(1) operation index: (entity, action) -> endpoint
        self._operation_index: dict[tuple[str, Action], Any] = {}
        for entity in self.model.entities:
            for action in entity.actions:
                endpoint = entity.endpoints.get(action)
                if endpoint:
                    self._operation_index[(entity.name, action)] = endpoint

        # Register operation handlers (order matters for can_handle priority)
        op_context = _OperationContext(self)
        self._operation_handlers: list[_OperationHandler] = [
            _DownloadOperationHandler(op_context),
            _StandardOperationHandler(op_context),
        ]

    def _apply_auth_config_mapping(self, user_secrets: dict[str, SecretStr]) -> dict[str, SecretStr]:
        """Apply auth_mapping from x-airbyte-auth-config to transform user secrets.

        This method takes user-provided secrets (e.g., {"api_token": "abc123"}) and
        transforms them into the auth scheme format (e.g., {"username": "abc123", "password": "api_token"})
        using the template mappings defined in x-airbyte-auth-config.

        Args:
            user_secrets: User-provided secrets from config

        Returns:
            Transformed secrets matching the auth scheme requirements
        """
        if not self.model.auth.user_config_spec:
            # No x-airbyte-auth-config defined, use secrets as-is
            return user_secrets

        user_config_spec = self.model.auth.user_config_spec
        auth_mapping = None
        required_fields: list[str] | None = None

        # Check for single option (direct auth_mapping)
        if user_config_spec.auth_mapping:
            auth_mapping = user_config_spec.auth_mapping
            required_fields = user_config_spec.required
        # Check for oneOf (multiple auth options)
        elif user_config_spec.one_of:
            # Find the matching option based on which required fields are present
            for option in user_config_spec.one_of:
                option_required = option.required or []
                if all(field in user_secrets for field in option_required):
                    auth_mapping = option.auth_mapping
                    required_fields = option_required
                    break

        if not auth_mapping:
            # No matching auth_mapping found, use secrets as-is
            return user_secrets

        # If required fields are missing and user provided no credentials,
        # return as-is (allows empty auth for testing or optional auth)
        if required_fields and not user_secrets:
            return user_secrets

        # Convert SecretStr values to plain strings for template processing
        user_config_values = {
            key: (value.get_secret_value() if hasattr(value, "get_secret_value") else str(value)) for key, value in user_secrets.items()
        }

        # Apply the auth_mapping templates, passing required_fields so optional
        # fields that are not provided can be skipped
        mapped_values = apply_auth_mapping(auth_mapping, user_config_values, required_fields=required_fields)

        # Convert back to SecretStr
        mapped_secrets = {key: SecretStr(value) for key, value in mapped_values.items()}

        return mapped_secrets

    def _initialize_auth(
        self,
        user_credentials: dict[str, SecretStr] | None,
        explicit_scheme: str | None,
    ) -> tuple[AuthConfig, dict[str, SecretStr] | None]:
        """Initialize authentication for single or multi-auth connectors.

        Handles both legacy single-auth and new multi-auth connectors.
        For multi-auth, the auth scheme can be explicitly provided or inferred
        from the provided credentials by matching against each scheme's required fields.

        Args:
            user_credentials: User-provided credentials (auth_config or secrets)
            explicit_scheme: Explicit scheme name for multi-auth (optional, will be
                inferred from credentials if not provided)

        Returns:
            Tuple of (selected AuthConfig for HTTPClient, transformed secrets)

        Raises:
            ValueError: If multi-auth connector can't determine which scheme to use
        """
        # Multi-auth: explicit scheme selection or inference from credentials
        if self.model.auth.is_multi_auth():
            if not user_credentials:
                available_schemes = [opt.scheme_name for opt in self.model.auth.options]
                raise ValueError(f"Multi-auth connector requires credentials. Available schemes: {available_schemes}")

            # If explicit scheme provided, use it directly
            if explicit_scheme:
                selected_option, transformed_secrets = self._select_auth_option(user_credentials, explicit_scheme)
            else:
                # Infer auth scheme from provided credentials
                selected_option, transformed_secrets = self._infer_auth_scheme(user_credentials)

            # Convert AuthOption to single-auth AuthConfig for HTTPClient
            selected_auth_config = AuthConfig(
                type=selected_option.type,
                config=selected_option.config,
                user_config_spec=None,  # Not needed by HTTPClient
            )

            return (selected_auth_config, transformed_secrets)

        # Single-auth: use existing logic
        if user_credentials is not None:
            # Apply mapping if this is auth_config (not legacy secrets)
            transformed_secrets = self._apply_auth_config_mapping(user_credentials)
        else:
            transformed_secrets = None

        return (self.model.auth, transformed_secrets)

    def _infer_auth_scheme(
        self,
        user_credentials: dict[str, SecretStr],
    ) -> tuple[AuthOption, dict[str, SecretStr]]:
        """Infer authentication scheme from provided credentials.

        Matches user credentials against each auth option's required fields
        to determine which scheme to use.

        Args:
            user_credentials: User-provided credentials

        Returns:
            Tuple of (inferred AuthOption, transformed secrets)

        Raises:
            ValueError: If no scheme matches, or multiple schemes match
        """
        options = self.model.auth.options
        if not options:
            raise ValueError("No auth options available in multi-auth config")

        # Get the credential keys provided by the user
        provided_keys = set(user_credentials.keys())

        # Find all options where all required fields are present
        matching_options: list[AuthOption] = []
        for option in options:
            if option.user_config_spec and option.user_config_spec.required:
                required_fields = set(option.user_config_spec.required)
                if required_fields.issubset(provided_keys):
                    matching_options.append(option)
            elif not option.user_config_spec or not option.user_config_spec.required:
                # Option has no required fields - it matches any credentials
                matching_options.append(option)

        # Handle matching results
        if len(matching_options) == 0:
            # No matches - provide helpful error message
            scheme_requirements = []
            for opt in options:
                required = opt.user_config_spec.required if opt.user_config_spec and opt.user_config_spec.required else []
                scheme_requirements.append(f"  - {opt.scheme_name}: requires {required}")
            raise ValueError(
                f"Could not infer auth scheme from provided credentials. "
                f"Provided keys: {list(provided_keys)}. "
                f"Available schemes and their required fields:\n" + "\n".join(scheme_requirements)
            )

        if len(matching_options) > 1:
            # Multiple matches - need explicit scheme
            matching_names = [opt.scheme_name for opt in matching_options]
            raise ValueError(
                f"Multiple auth schemes match the provided credentials: {matching_names}. Please specify 'auth_scheme' explicitly to disambiguate."
            )

        # Exactly one match - use it
        selected_option = matching_options[0]
        transformed_secrets = self._apply_auth_mapping_for_option(user_credentials, selected_option)
        return (selected_option, transformed_secrets)

    def _select_auth_option(
        self,
        user_credentials: dict[str, SecretStr],
        scheme_name: str,
    ) -> tuple[AuthOption, dict[str, SecretStr]]:
        """Select authentication option by explicit scheme name.

        Args:
            user_credentials: User-provided credentials
            scheme_name: Explicit scheme name (e.g., "githubOAuth")

        Returns:
            Tuple of (selected AuthOption, transformed secrets)

        Raises:
            ValueError: If scheme not found
        """
        options = self.model.auth.options
        if not options:
            raise ValueError("No auth options available in multi-auth config")

        # Find matching scheme
        for option in options:
            if option.scheme_name == scheme_name:
                transformed_secrets = self._apply_auth_mapping_for_option(user_credentials, option)
                return (option, transformed_secrets)

        # Scheme not found
        available = [opt.scheme_name for opt in options]
        raise ValueError(f"Auth scheme '{scheme_name}' not found. Available schemes: {available}")

    def _apply_auth_mapping_for_option(
        self,
        user_credentials: dict[str, SecretStr],
        option: AuthOption,
    ) -> dict[str, SecretStr]:
        """Apply auth mapping for a specific auth option.

        Transforms user credentials using the option's auth_mapping templates.

        Args:
            user_credentials: User-provided credentials
            option: AuthOption to apply

        Returns:
            Transformed secrets after applying auth_mapping

        Raises:
            ValueError: If required fields are missing or mapping fails
        """
        if not option.user_config_spec:
            # No mapping defined, use credentials as-is
            return user_credentials

        # Extract auth_mapping and required fields
        user_config_spec = option.user_config_spec
        auth_mapping = user_config_spec.auth_mapping
        required_fields = user_config_spec.required

        if not auth_mapping:
            raise ValueError(f"No auth_mapping found for scheme '{option.scheme_name}'")

        # Convert SecretStr to plain strings for template processing
        user_config_values = {
            key: (value.get_secret_value() if hasattr(value, "get_secret_value") else str(value)) for key, value in user_credentials.items()
        }

        # Apply the auth_mapping templates
        mapped_values = apply_auth_mapping(auth_mapping, user_config_values, required_fields=required_fields)

        # Convert back to SecretStr
        return {key: SecretStr(value) for key, value in mapped_values.items()}

    async def execute(self, config: ExecutionConfig) -> ExecutionResult:
        """Execute connector operation using handler pattern.

        Args:
            config: Execution configuration (entity, action, params)

        Returns:
            ExecutionResult with success/failure status and data

        Example:
            config = ExecutionConfig(
                entity="customers",
                action="list",
                params={"limit": 10}
            )
            result = await executor.execute(config)
            if result.success:
                print(result.data)
        """
        try:
            # Check for hosted-only actions before converting to Action enum
            if config.action == "search":
                raise NotImplementedError(
                    "search is only available in hosted execution mode. "
                    "Initialize the connector with external_user_id, airbyte_client_id, "
                    "and airbyte_client_secret to use this feature."
                )

            # Convert config to internal format
            action = Action(config.action) if isinstance(config.action, str) else config.action
            params = config.params or {}

            # Dispatch to handler (handlers handle telemetry internally)
            handler = next((h for h in self._operation_handlers if h.can_handle(action)), None)
            if not handler:
                raise ExecutorError(f"No handler registered for action '{action.value}'.")

            # Execute handler
            result = handler.execute_operation(config.entity, action, params)

            # Check if it's an async generator (download) or awaitable (standard)
            if inspect.isasyncgen(result):
                # Download operation: return generator directly
                return ExecutionResult(
                    success=True,
                    data=result,
                    error=None,
                    meta=None,
                )
            else:
                # Standard operation: await and extract data and metadata
                handler_result = await result
                return ExecutionResult(
                    success=True,
                    data=handler_result.data,
                    error=None,
                    meta=handler_result.metadata,
                )

        except (
            EntityNotFoundError,
            ActionNotSupportedError,
            MissingParameterError,
            InvalidParameterError,
        ) as e:
            # These are "expected" execution errors - return them in ExecutionResult
            return ExecutionResult(success=False, data={}, error=str(e))

    async def check(self) -> ExecutionResult:
        """Perform a health check by running a lightweight list operation.

        Finds the operation marked with preferred_for_check=True, or falls back
        to the first list operation. Executes it with limit=1 to verify
        connectivity and credentials.

        Returns:
            ExecutionResult with data containing status, error, and checked operation details.
        """
        check_entity = None
        check_endpoint = None

        # Look for preferred check operation
        for (ent_name, op_action), endpoint in self._operation_index.items():
            if getattr(endpoint, "preferred_for_check", False):
                check_entity = ent_name
                check_endpoint = endpoint
                break

        # Fallback to first list operation
        if check_endpoint is None:
            for (ent_name, op_action), endpoint in self._operation_index.items():
                if op_action == Action.LIST:
                    check_entity = ent_name
                    check_endpoint = endpoint
                    break

        if check_endpoint is None or check_entity is None:
            return ExecutionResult(
                success=True,
                data={
                    "status": "skipped",
                    "error": "No list operation available for health check",
                },
            )

        # Find the standard handler to execute the list operation
        standard_handler = next(
            (h for h in self._operation_handlers if isinstance(h, _StandardOperationHandler)),
            None,
        )

        if standard_handler is None:
            return ExecutionResult(
                success=True,
                data={
                    "status": "skipped",
                    "error": "No standard handler available",
                },
            )

        try:
            await standard_handler.execute_operation(check_entity, Action.LIST, {"limit": 1})
            return ExecutionResult(
                success=True,
                data={
                    "status": "healthy",
                    "checked_entity": check_entity,
                    "checked_action": "list",
                },
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                data={
                    "status": "unhealthy",
                    "error": str(e),
                    "checked_entity": check_entity,
                    "checked_action": "list",
                },
                error=str(e),
            )

    async def _execute_operation(
        self,
        entity: str,
        action: str | Action,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Internal method: Execute an action on an entity asynchronously.

        This method now delegates to the appropriate handler and extracts just the data.
        External code should use execute(config) instead for full ExecutionResult with metadata.

        Args:
            entity: Entity name (e.g., "Customer")
            action: Action to execute (e.g., "get" or Action.GET)
            params: Parameters for the operation
                - For GET: {"id": "cus_123"} for path params
                - For LIST: {"limit": 10} for query params
                - For CREATE/UPDATE: {"email": "...", "name": "..."} for body

        Returns:
            API response as dictionary

        Raises:
            ValueError: If entity or action not found
            HTTPClientError: If API request fails
        """
        params = params or {}
        action = Action(action) if isinstance(action, str) else action

        # Delegate to the appropriate handler
        handler = next((h for h in self._operation_handlers if h.can_handle(action)), None)
        if not handler:
            raise ExecutorError(f"No handler registered for action '{action.value}'.")

        # Execute handler and extract just the data for backward compatibility
        result = await handler.execute_operation(entity, action, params)
        if isinstance(result, StandardExecuteResult):
            return result.data
        else:
            # Download operation returns AsyncIterator directly
            return result

    async def execute_batch(self, operations: list[tuple[str, str | Action, dict[str, Any] | None]]) -> list[dict[str, Any] | AsyncIterator[bytes]]:
        """Execute multiple operations concurrently (supports all action types including download).

        Args:
            operations: List of (entity, action, params) tuples

        Returns:
            List of responses in the same order as operations.
            Standard operations return dict[str, Any].
            Download operations return AsyncIterator[bytes].

        Raises:
            ValueError: If any entity or action not found
            HTTPClientError: If any API request fails

        Example:
            results = await executor.execute_batch([
                ("Customer", "list", {"limit": 10}),
                ("Customer", "get", {"id": "cus_123"}),
                ("attachments", "download", {"id": "att_456"}),
            ])
        """
        # Build tasks by dispatching directly to handlers
        tasks = []
        for entity, action, params in operations:
            # Convert action to Action enum if needed
            action = Action(action) if isinstance(action, str) else action
            params = params or {}

            # Find appropriate handler
            handler = next((h for h in self._operation_handlers if h.can_handle(action)), None)
            if not handler:
                raise ExecutorError(f"No handler registered for action '{action.value}'.")

            # Call handler directly (exceptions propagate naturally)
            tasks.append(handler.execute_operation(entity, action, params))

        # Execute all tasks concurrently - exceptions propagate via asyncio.gather
        results = await asyncio.gather(*tasks)

        # Extract data from results
        extracted_results = []
        for result in results:
            if isinstance(result, StandardExecuteResult):
                # Standard operation: extract data
                extracted_results.append(result.data)
            else:
                # Download operation: return iterator as-is
                extracted_results.append(result)

        return extracted_results

    def _build_path(self, path_template: str, params: dict[str, Any]) -> str:
        """Build path by replacing {param} placeholders with URL-encoded values.

        Args:
            path_template: Path with placeholders (e.g., /v1/customers/{id})
            params: Parameters containing values for placeholders

        Returns:
            Completed path with URL-encoded values (e.g., /v1/customers/cus_123)

        Raises:
            MissingParameterError: If required path parameter is missing
        """
        placeholders = re.findall(r"\{(\w+)\}", path_template)

        path = path_template
        for placeholder in placeholders:
            if placeholder not in params:
                raise MissingParameterError(
                    f"Missing required path parameter '{placeholder}' for path '{path_template}'. Provided parameters: {list(params.keys())}"
                )

            # Validate parameter value is not None or empty string
            value = params[placeholder]
            if value is None or (isinstance(value, str) and value.strip() == ""):
                raise InvalidParameterError(f"Path parameter '{placeholder}' cannot be None or empty string")

            encoded_value = quote(str(value), safe="")
            path = path.replace(f"{{{placeholder}}}", encoded_value)

        return path

    def _extract_query_params(self, allowed_params: list[str], params: dict[str, Any]) -> dict[str, Any]:
        """Extract query parameters from params.

        Args:
            allowed_params: List of allowed query parameter names
            params: All parameters

        Returns:
            Dictionary of query parameters
        """
        return {key: value for key, value in params.items() if key in allowed_params}

    def _extract_body(self, allowed_fields: list[str], params: dict[str, Any]) -> dict[str, Any]:
        """Extract body fields from params, filtering out None values.

        Args:
            allowed_fields: List of allowed body field names
            params: All parameters

        Returns:
            Dictionary of body fields with None values filtered out
        """
        return {key: value for key, value in params.items() if key in allowed_fields and value is not None}

    def _extract_header_params(self, endpoint: EndpointDefinition, params: dict[str, Any], body: dict[str, Any] | None = None) -> dict[str, str]:
        """Extract header parameters from params and schema defaults.

        Also adds Content-Type header when there's a request body (unless already specified
        as a header parameter in the OpenAPI spec).

        Args:
            endpoint: Endpoint definition with header_params and header_params_schema
            params: All parameters
            body: Request body (if any) - used to determine if Content-Type should be added

        Returns:
            Dictionary of header name -> value
        """
        headers: dict[str, str] = {}

        for header_name in endpoint.header_params:
            # Check if value is provided in params
            if header_name in params and params[header_name] is not None:
                headers[header_name] = str(params[header_name])
            # Otherwise, use default from schema if available
            elif header_name in endpoint.header_params_schema:
                default_value = endpoint.header_params_schema[header_name].get("default")
                if default_value is not None:
                    headers[header_name] = str(default_value)

        # Add Content-Type header when there's a request body, but only if not already
        # specified as a header parameter (which allows custom content types like
        # application/vnd.spCampaign.v3+json)
        if body is not None and endpoint.content_type and "Content-Type" not in headers:
            headers["Content-Type"] = endpoint.content_type.value

        return headers

    def _serialize_deep_object_params(self, params: dict[str, Any], deep_object_param_names: list[str]) -> dict[str, Any]:
        """Serialize deepObject parameters to bracket notation format.

        Converts nested dict parameters to the deepObject format expected by APIs
        like Stripe. For example:
        - Input: {'created': {'gte': 123, 'lte': 456}}
        - Output: {'created[gte]': 123, 'created[lte]': 456}

        Args:
            params: Query parameters dict (may contain nested dicts)
            deep_object_param_names: List of parameter names that use deepObject style

        Returns:
            Dictionary with deepObject params serialized to bracket notation
        """
        serialized = {}

        for key, value in params.items():
            if key in deep_object_param_names and isinstance(value, dict):
                # Serialize nested dict to bracket notation
                for subkey, subvalue in value.items():
                    if subvalue is not None:  # Skip None values
                        serialized[f"{key}[{subkey}]"] = subvalue
            else:
                # Keep non-deepObject params as-is (already validated by _extract_query_params)
                serialized[key] = value

        return serialized

    @staticmethod
    def _extract_download_url(
        response: dict[str, Any],
        file_field: str,
        entity: str,
    ) -> str:
        """Extract download URL from metadata response using x-airbyte-file-url.

        Supports both simple dot notation (e.g., "article.content_url") and array
        indexing with bracket notation (e.g., "calls[0].media.audioUrl").

        Args:
            response: Metadata response containing file reference
            file_field: JSON path to file URL field (from x-airbyte-file-url)
            entity: Entity name (for error messages)

        Returns:
            Extracted file URL

        Raises:
            ExecutorError: If file field not found or invalid
        """
        # Navigate nested path (e.g., "article_attachment.content_url" or "calls[0].media.audioUrl")
        parts = file_field.split(".")
        current = response

        for i, part in enumerate(parts):
            # Check if part has array indexing (e.g., "calls[0]")
            array_match = re.match(r"^(\w+)\[(\d+)\]$", part)

            if array_match:
                field_name = array_match.group(1)
                index = int(array_match.group(2))

                # Navigate to the field
                if not isinstance(current, dict):
                    raise ExecutorError(
                        f"Cannot extract download URL for {entity}: Expected dict at '{'.'.join(parts[:i])}', got {type(current).__name__}"
                    )

                if field_name not in current:
                    raise ExecutorError(
                        f"Cannot extract download URL for {entity}: "
                        f"Field '{field_name}' not found in response. Available fields: {list(current.keys())}"
                    )

                # Get the array
                array_value = current[field_name]
                if not isinstance(array_value, list):
                    raise ExecutorError(
                        f"Cannot extract download URL for {entity}: Expected list at '{field_name}', got {type(array_value).__name__}"
                    )

                # Check index bounds
                if index >= len(array_value):
                    raise ExecutorError(
                        f"Cannot extract download URL for {entity}: Index {index} out of bounds for '{field_name}' (length: {len(array_value)})"
                    )

                current = array_value[index]
            else:
                # Regular dict navigation
                if not isinstance(current, dict):
                    raise ExecutorError(
                        f"Cannot extract download URL for {entity}: Expected dict at '{'.'.join(parts[:i])}', got {type(current).__name__}"
                    )

                if part not in current:
                    raise ExecutorError(
                        f"Cannot extract download URL for {entity}: Field '{part}' not found in response. Available fields: {list(current.keys())}"
                    )

                current = current[part]

        if not isinstance(current, str):
            raise ExecutorError(f"Cannot extract download URL for {entity}: Expected string at '{file_field}', got {type(current).__name__}")

        return current

    @staticmethod
    def _substitute_file_field_params(
        file_field: str,
        params: dict[str, Any],
    ) -> str:
        """Substitute template variables in file_field with parameter values.

        Uses Jinja2 with custom delimiters to support OpenAPI-style syntax like
        "attachments[{index}].url" where {index} is replaced with params["index"].

        Args:
            file_field: File field path with optional template variables
            params: Parameters from execute() call

        Returns:
            File field with template variables substituted

        Example:
            >>> _substitute_file_field_params("attachments[{attachment_index}].url", {"attachment_index": 0})
            "attachments[0].url"
        """

        # Use custom delimiters to match OpenAPI path parameter syntax {var}
        # StrictUndefined raises clear error if a template variable is missing
        env = Environment(
            variable_start_string="{",
            variable_end_string="}",
            undefined=StrictUndefined,
        )
        template = env.from_string(file_field)
        return template.render(params)

    def _build_request_body(self, endpoint: EndpointDefinition, params: dict[str, Any]) -> dict[str, Any] | None:
        """Build request body (GraphQL or standard).

        Args:
            endpoint: Endpoint definition
            params: Parameters from execute() call

        Returns:
            Request body dict or None if no body needed
        """
        if endpoint.graphql_body:
            # Extract defaults from query_params_schema for GraphQL variable interpolation
            param_defaults = {name: schema.get("default") for name, schema in endpoint.query_params_schema.items() if "default" in schema}
            return self._build_graphql_body(endpoint.graphql_body, params, param_defaults)
        elif endpoint.body_fields:
            # Start with defaults from request body schema
            body = dict(endpoint.request_body_defaults)
            # Override with user-provided params (filtering out None values)
            user_body = self._extract_body(endpoint.body_fields, params)
            body.update(user_body)
            return body if body else None
        elif endpoint.request_body_defaults:
            # If no body_fields but we have defaults, return the defaults
            return dict(endpoint.request_body_defaults)
        return None

    def _flatten_form_data(self, data: dict[str, Any], parent_key: str = "") -> dict[str, Any]:
        """Flatten nested dict/list structures into bracket notation for form encoding.

        Stripe and similar APIs require nested arrays/objects to be encoded using bracket
        notation when using application/x-www-form-urlencoded content type.

        Args:
            data: Nested dict with arrays/objects to flatten
            parent_key: Parent key for nested structures (used in recursion)

        Returns:
            Flattened dict with bracket notation keys

        Examples:
            >>> _flatten_form_data({"items": [{"price": "p1", "qty": 1}]})
            {"items[0][price]": "p1", "items[0][qty]": 1}

            >>> _flatten_form_data({"customer": "cus_123", "metadata": {"key": "value"}})
            {"customer": "cus_123", "metadata[key]": "value"}
        """
        flattened = {}

        for key, value in data.items():
            new_key = f"{parent_key}[{key}]" if parent_key else key

            if isinstance(value, dict):
                # Recursively flatten nested dicts
                flattened.update(self._flatten_form_data(value, new_key))
            elif isinstance(value, list):
                # Flatten arrays with indexed bracket notation
                for i, item in enumerate(value):
                    indexed_key = f"{new_key}[{i}]"
                    if isinstance(item, dict):
                        # Nested dict in array - recurse
                        flattened.update(self._flatten_form_data(item, indexed_key))
                    elif isinstance(item, list):
                        # Nested list in array - recurse
                        flattened.update(self._flatten_form_data({str(i): item}, new_key))
                    else:
                        # Primitive value in array
                        flattened[indexed_key] = item
            else:
                # Primitive value - add directly
                flattened[new_key] = value

        return flattened

    def _determine_request_format(self, endpoint: EndpointDefinition, body: dict[str, Any] | None) -> dict[str, Any]:
        """Determine json/data parameters for HTTP request.

        GraphQL always uses JSON, regardless of content_type setting.
        For form-encoded requests, nested structures are flattened into bracket notation.

        Args:
            endpoint: Endpoint definition
            body: Request body dict or None

        Returns:
            Dict with 'json' and/or 'data' keys for http_client.request()
        """
        if not body:
            return {}

        is_graphql = endpoint.graphql_body is not None

        if is_graphql or endpoint.content_type.value == "application/json":
            return {"json": body}
        elif endpoint.content_type.value == "application/x-www-form-urlencoded":
            # Flatten nested structures for form encoding
            flattened_body = self._flatten_form_data(body)
            return {"data": flattened_body}

        return {}

    def _process_graphql_fields(self, query: str, graphql_config: dict[str, Any], params: dict[str, Any]) -> str:
        """Process GraphQL query field selection.

        Handles:
        - Dynamic fields from params['fields']
        - Default fields from config
        - String vs list format for default_fields

        Args:
            query: GraphQL query string (may contain {{ fields }} placeholder)
            graphql_config: GraphQL configuration dict
            params: Parameters from execute() call

        Returns:
            Processed query string with fields injected
        """
        if "{{ fields }}" not in query:
            return query

        # Check for explicit fields parameter
        if "fields" in params and params["fields"]:
            return self._inject_graphql_fields(query, params["fields"])

        # Use default fields if available
        if "default_fields" not in graphql_config:
            return query  # Placeholder remains (could raise error in the future)

        default_fields = graphql_config["default_fields"]
        if isinstance(default_fields, str):
            # Already in GraphQL format - direct replacement
            return query.replace("{{ fields }}", default_fields)
        elif isinstance(default_fields, list):
            # List format - convert to GraphQL
            return self._inject_graphql_fields(query, default_fields)

        return query

    def _build_graphql_body(
        self,
        graphql_config: dict[str, Any],
        params: dict[str, Any],
        param_defaults: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build GraphQL request body with variable substitution and field selection.

        Args:
            graphql_config: GraphQL configuration from x-airbyte-body-type extension
            params: Parameters from execute() call
            param_defaults: Default values for params from query_params_schema

        Returns:
            GraphQL request body: {"query": "...", "variables": {...}}
        """
        query = graphql_config["query"]

        # Process field selection (dynamic fields or default fields)
        query = self._process_graphql_fields(query, graphql_config, params)

        body = {"query": query}

        # Substitute variables from params
        if "variables" in graphql_config and graphql_config["variables"]:
            variables = self._interpolate_variables(graphql_config["variables"], params, param_defaults)
            # Filter out None values (optional fields not provided) - matches REST _extract_body() behavior
            # But preserve None for variables explicitly marked as nullable (e.g., to unassign a user)
            nullable_vars = set(graphql_config.get("x-airbyte-nullable-variables") or [])
            body["variables"] = {k: v for k, v in variables.items() if v is not None or k in nullable_vars}

        # Add operation name if specified
        if "operationName" in graphql_config:
            body["operationName"] = graphql_config["operationName"]

        return body

    def _convert_nested_field_to_graphql(self, field: str) -> str:
        """Convert dot-notation field to GraphQL field selection.

        Example: "primaryLanguage.name" -> "primaryLanguage { name }"

        Args:
            field: Field name in dot notation (e.g., "primaryLanguage.name")

        Returns:
            GraphQL field selection string
        """
        if "." not in field:
            return field

        parts = field.split(".")
        result = parts[0]
        for part in parts[1:]:
            result += f" {{ {part}"
        result += " }" * (len(parts) - 1)
        return result

    def _inject_graphql_fields(self, query: str, fields: list[str]) -> str:
        """Inject field selection into GraphQL query.

        Replaces field selection placeholders ({{ fields }}) with actual field list.
        Supports nested fields using dot notation (e.g., "primaryLanguage.name").

        Args:
            query: GraphQL query string (may contain {{ fields }} placeholder)
            fields: List of fields to select (e.g., ["id", "name", "primaryLanguage.name"])

        Returns:
            GraphQL query with fields injected

        Example:
            Input query: "query { repository { {{ fields }} } }"
            Fields: ["id", "name", "primaryLanguage { name }"]
            Output: "query { repository { id name primaryLanguage { name } } }"
        """
        # Check if query has field placeholder
        if "{{ fields }}" not in query:
            # No placeholder - return query as-is (backward compatible)
            return query

        # Convert field list to GraphQL field selection
        graphql_fields = [self._convert_nested_field_to_graphql(field) for field in fields]

        # Replace placeholder with field list
        fields_str = " ".join(graphql_fields)
        return query.replace("{{ fields }}", fields_str)

    def _interpolate_variables(
        self,
        variables: dict[str, Any],
        params: dict[str, Any],
        param_defaults: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Recursively interpolate variables using params.

        Preserves types (doesn't stringify everything).

        Supports:
        - Direct replacement: "{{ owner }}" → params["owner"] (preserves type)
        - Nested objects: {"input": {"name": "{{ name }}"}}
        - Arrays: [{"id": "{{ id }}"}]
        - Default values: "{{ per_page }}" → param_defaults["per_page"] if not in params
        - Unsubstituted placeholders: "{{ states }}" → None (for optional params without defaults)

        Args:
            variables: Variables dict with template placeholders
            params: Parameters to substitute
            param_defaults: Default values for params from query_params_schema

        Returns:
            Interpolated variables dict with types preserved
        """
        defaults = param_defaults or {}

        def interpolate_value(value: Any) -> Any:
            if isinstance(value, str):
                # Check for exact template match (preserve type)
                for key, param_value in params.items():
                    placeholder = f"{{{{ {key} }}}}"
                    if value == placeholder:
                        return param_value  # Return actual value (int, list, etc.)
                    elif placeholder in value:
                        # Partial match - do string replacement
                        value = value.replace(placeholder, str(param_value))

                # Check if any unsubstituted placeholders remain
                if re.search(r"\{\{\s*\w+\s*\}\}", value):
                    # Extract placeholder name and check for default value
                    match = re.search(r"\{\{\s*(\w+)\s*\}\}", value)
                    if match:
                        param_name = match.group(1)
                        if param_name in defaults:
                            # Use default value (preserves type)
                            return defaults[param_name]
                    # No default found - return None (for optional params)
                    return None

                return value
            elif isinstance(value, dict):
                return {k: interpolate_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [interpolate_value(item) for item in value]
            else:
                return value

        return interpolate_value(variables)

    def _wrap_primitives(self, data: Any) -> dict[str, Any] | list[dict[str, Any]] | None:
        """Wrap primitive values in dict format for consistent response structure.

        Transforms primitive API responses into dict format so downstream code
        can always expect dict-based data structures.

        Args:
            data: Response data (could be primitive, list, dict, or None)

        Returns:
            - If data is a primitive (str, int, float, bool): {"value": data}
            - If data is a list: wraps all non-dict elements as {"value": item}
            - If data is already a dict or list of dicts: unchanged
            - If data is None: None

        Examples:
            >>> executor._wrap_primitives(42)
            {"value": 42}
            >>> executor._wrap_primitives([1, 2, 3])
            [{"value": 1}, {"value": 2}, {"value": 3}]
            >>> executor._wrap_primitives([1, {"id": 2}, 3])
            [{"value": 1}, {"id": 2}, {"value": 3}]
            >>> executor._wrap_primitives([[1, 2], 3])
            [{"value": [1, 2]}, {"value": 3}]
            >>> executor._wrap_primitives({"id": 1})
            {"id": 1}  # unchanged
        """
        if data is None:
            return None

        # Handle primitive scalars
        if isinstance(data, (bool, str, int, float)):
            return {"value": data}

        # Handle lists - wrap non-dict elements
        if isinstance(data, list):
            if not data:
                return []  # Empty list unchanged

            wrapped = []
            for item in data:
                if isinstance(item, dict):
                    wrapped.append(item)
                else:
                    wrapped.append({"value": item})
            return wrapped

        # Dict - return unchanged
        if isinstance(data, dict):
            return data

        # Unknown type - wrap for safety
        return {"value": data}

    def _extract_records(
        self,
        response_data: Any,
        endpoint: EndpointDefinition,
    ) -> dict[str, Any] | list[dict[str, Any]] | None:
        """Extract records from response using record extractor.

        Type inference based on action:
        - list, search: Returns array ([] if not found)
        - get, create, update, delete: Returns single record (None if not found)

        Automatically wraps primitive values (int, str, float, bool) in {"value": primitive}
        format to ensure consistent dict-based responses for downstream code.

        Args:
            response_data: Full API response (can be dict, list, primitive, or None)
            endpoint: Endpoint with optional record extractor and action

        Returns:
            - Extracted data if extractor configured and path found
            - [] or None if path not found (based on action)
            - Original response if no extractor configured or on error
            - Primitives are wrapped as {"value": primitive}
        """
        # Check if endpoint has record extractor
        extractor = endpoint.record_extractor
        if not extractor:
            return self._wrap_primitives(response_data)

        # Determine if this action returns array or single record
        action = endpoint.action
        if not action:
            return self._wrap_primitives(response_data)

        is_array_action = action in (Action.LIST, Action.API_SEARCH)

        try:
            # Parse and apply JSONPath expression
            jsonpath_expr = parse_jsonpath(extractor)
            matches = [match.value for match in jsonpath_expr.find(response_data)]

            if not matches:
                # Path not found - return empty based on action
                return [] if is_array_action else None

            # Return extracted data with primitive wrapping
            if is_array_action:
                # For array actions, return the array (or list of matches)
                result = matches[0] if len(matches) == 1 else matches
            else:
                # For single record actions, return first match
                result = matches[0]

            return self._wrap_primitives(result)

        except Exception as e:
            logging.warning(f"Failed to apply record extractor '{extractor}': {e}. Returning original response.")
            return self._wrap_primitives(response_data)

    def _extract_metadata(
        self,
        response_data: dict[str, Any],
        response_headers: dict[str, str],
        endpoint: EndpointDefinition,
    ) -> dict[str, Any] | None:
        """Extract metadata from response using meta extractor.

        Each field in meta_extractor dict is independently extracted using JSONPath
        for body extraction, or special prefixes for header extraction:
        - @link.{rel}: Extract URL from RFC 5988 Link header by rel type
        - @header.{name}: Extract raw header value by header name
        - Otherwise: JSONPath expression for body extraction

        Missing or invalid paths result in None for that field (no crash).

        Args:
            response_data: Full API response (before record extraction)
            response_headers: HTTP response headers
            endpoint: Endpoint with optional meta extractor configuration

        Returns:
            - Dict of extracted metadata if extractor configured
            - None if no extractor configured
            - Dict with None values for failed extractions

        Example:
            meta_extractor = {
                "pagination": "$.records",
                "request_id": "$.requestId",
                "next_page_url": "@link.next",
                "rate_limit": "@header.X-RateLimit-Remaining"
            }
            Returns: {
                "pagination": {"cursor": "abc", "total": 100},
                "request_id": "xyz123",
                "next_page_url": "https://api.example.com/data?cursor=abc",
                "rate_limit": "99"
            }
        """
        # Check if endpoint has meta extractor
        if endpoint.meta_extractor is None:
            return None

        extracted_meta: dict[str, Any] = {}

        # Extract each field independently
        for field_name, extractor_expr in endpoint.meta_extractor.items():
            try:
                if extractor_expr.startswith("@link."):
                    # RFC 5988 Link header extraction
                    rel = extractor_expr[6:]
                    extracted_meta[field_name] = self._extract_link_url(response_headers, rel)
                elif extractor_expr.startswith("@header."):
                    # Raw header value extraction (case-insensitive lookup)
                    header_name = extractor_expr[8:]
                    extracted_meta[field_name] = self._get_header_value(response_headers, header_name)
                else:
                    # JSONPath body extraction
                    jsonpath_expr = parse_jsonpath(extractor_expr)
                    matches = [match.value for match in jsonpath_expr.find(response_data)]

                    if matches:
                        # Return first match (most common case)
                        extracted_meta[field_name] = matches[0]
                    else:
                        # Path not found - set to None
                        extracted_meta[field_name] = None

            except Exception as e:
                # Log error but continue with other fields
                logging.warning(f"Failed to apply meta extractor for field '{field_name}' with expression '{extractor_expr}': {e}. Setting to None.")
                extracted_meta[field_name] = None

        return extracted_meta

    @staticmethod
    def _extract_link_url(headers: dict[str, str], rel: str) -> str | None:
        """Extract URL from RFC 5988 Link header by rel type.

        Parses Link header format: <url>; param1="value1"; rel="next"; param2="value2"

        Supports:
        - Multiple parameters per link in any order
        - Both quoted and unquoted rel values
        - Multiple links separated by commas

        Args:
            headers: Response headers dict
            rel: The rel type to extract (e.g., "next", "prev", "first", "last")

        Returns:
            The URL for the specified rel type, or None if not found
        """
        link_header = headers.get("Link") or headers.get("link", "")
        if not link_header:
            return None

        for link_segment in re.split(r",(?=\s*<)", link_header):
            link_segment = link_segment.strip()

            url_match = re.match(r"<([^>]+)>", link_segment)
            if not url_match:
                continue

            url = url_match.group(1)
            params_str = link_segment[url_match.end() :]

            rel_match = re.search(r';\s*rel="?([^";,]+)"?', params_str, re.IGNORECASE)
            if rel_match and rel_match.group(1).strip() == rel:
                return url

        return None

    @staticmethod
    def _get_header_value(headers: dict[str, str], header_name: str) -> str | None:
        """Get header value with case-insensitive lookup.

        Args:
            headers: Response headers dict
            header_name: Header name to look up

        Returns:
            Header value or None if not found
        """
        # Try exact match first
        if header_name in headers:
            return headers[header_name]

        # Case-insensitive lookup
        header_name_lower = header_name.lower()
        for key, value in headers.items():
            if key.lower() == header_name_lower:
                return value

        return None

    def _validate_required_body_fields(self, endpoint: Any, params: dict[str, Any], action: Action, entity: str) -> None:
        """Validate that required body fields are present for CREATE/UPDATE operations.

        Args:
            endpoint: Endpoint definition
            params: Parameters provided
            action: Operation action
            entity: Entity name

        Raises:
            MissingParameterError: If required body fields are missing
        """
        # Only validate for operations that typically have required body fields
        if action not in (Action.CREATE, Action.UPDATE):
            return

        # Get the request schema to find truly required fields
        request_schema = endpoint.request_schema
        if not request_schema:
            return

        # Only validate fields explicitly marked as required in the schema
        required_fields = request_schema.get("required", [])
        missing_fields = [field for field in required_fields if field not in params]

        if missing_fields:
            raise MissingParameterError(
                f"Missing required body fields for {entity}.{action.value}: {missing_fields}. Provided parameters: {list(params.keys())}"
            )

    async def close(self):
        """Close async HTTP client and logger."""
        self.tracker.track_session_end()
        await self.http_client.close()
        self.logger.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()


# =============================================================================
# Operation Handlers
# =============================================================================


class _StandardOperationHandler:
    """Handler for standard REST operations (GET, LIST, CREATE, UPDATE, DELETE, API_SEARCH, AUTHORIZE)."""

    def __init__(self, context: _OperationContext):
        self.ctx = context

    def can_handle(self, action: Action) -> bool:
        """Check if this handler can handle the given action."""
        return action in {
            Action.GET,
            Action.LIST,
            Action.CREATE,
            Action.UPDATE,
            Action.DELETE,
            Action.API_SEARCH,
            Action.AUTHORIZE,
        }

    async def execute_operation(self, entity: str, action: Action, params: dict[str, Any]) -> StandardExecuteResult:
        """Execute standard REST operation with full telemetry and error handling."""
        tracer = trace.get_tracer("airbyte.connector-sdk.executor.local")

        with tracer.start_as_current_span("airbyte.local_executor.execute_operation") as span:
            # Add span attributes
            span.set_attribute("connector.name", self.ctx.executor.model.name)
            span.set_attribute("connector.entity", entity)
            span.set_attribute("connector.action", action.value)
            if params:
                span.set_attribute("connector.param_keys", list(params.keys()))

            # Increment operation counter
            self.ctx.session.increment_operations()

            # Track operation timing and status
            start_time = time.time()
            error_type = None
            status_code = None

            try:
                # O(1) entity lookup
                entity_def = self.ctx.entity_index.get(entity)
                if not entity_def:
                    available_entities = list(self.ctx.entity_index.keys())
                    raise EntityNotFoundError(f"Entity '{entity}' not found in connector. Available entities: {available_entities}")

                # Check if action is supported
                if action not in entity_def.actions:
                    supported_actions = [a.value for a in entity_def.actions]
                    raise ActionNotSupportedError(
                        f"Action '{action.value}' not supported for entity '{entity}'. Supported actions: {supported_actions}"
                    )

                # O(1) operation lookup
                endpoint = self.ctx.operation_index.get((entity, action))
                if not endpoint:
                    raise ExecutorError(f"No endpoint defined for {entity}.{action.value}. This is a configuration error.")

                # Validate required body fields for CREATE/UPDATE operations
                self.ctx.validate_required_body_fields(endpoint, params, action, entity)

                # Build request parameters
                # Use path_override if available, otherwise use the OpenAPI path
                actual_path = endpoint.path_override.path if endpoint.path_override else endpoint.path
                path = self.ctx.build_path(actual_path, params)
                query_params = self.ctx.extract_query_params(endpoint.query_params, params)

                # Serialize deepObject parameters to bracket notation
                if endpoint.deep_object_params:
                    query_params = self.ctx.executor._serialize_deep_object_params(query_params, endpoint.deep_object_params)

                # Build request body (GraphQL or standard)
                body = self.ctx.build_request_body(endpoint, params)

                # Determine request format (json/data parameters)
                request_kwargs = self.ctx.determine_request_format(endpoint, body)

                # Extract header parameters from OpenAPI operation (pass body to add Content-Type)
                header_params = self.ctx.extract_header_params(endpoint, params, body)

                # Execute async HTTP request
                response_data, response_headers = await self.ctx.http_client.request(
                    method=endpoint.method,
                    path=path,
                    params=query_params if query_params else None,
                    json=request_kwargs.get("json"),
                    data=request_kwargs.get("data"),
                    headers=header_params if header_params else None,
                )

                # Extract metadata from original response (before record extraction)
                metadata = self.ctx.executor._extract_metadata(response_data, response_headers, endpoint)

                # Extract records if extractor configured
                response = self.ctx.extract_records(response_data, endpoint)

                # Assume success with 200 status code if no exception raised
                status_code = 200

                # Mark span as successful
                span.set_attribute("connector.success", True)
                span.set_attribute("http.status_code", status_code)

                # Return StandardExecuteResult with data and metadata
                return StandardExecuteResult(data=response, metadata=metadata)

            except (EntityNotFoundError, ActionNotSupportedError) as e:
                # Validation errors - record in span
                error_type = type(e).__name__
                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", error_type)
                span.record_exception(e)
                raise

            except Exception as e:
                # Capture error details
                error_type = type(e).__name__

                # Try to get status code from HTTP errors
                if hasattr(e, "response") and hasattr(e.response, "status_code"):
                    status_code = e.response.status_code
                    span.set_attribute("http.status_code", status_code)

                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", error_type)
                span.record_exception(e)
                raise

            finally:
                # Always track operation (success or failure)
                timing_ms = (time.time() - start_time) * 1000
                self.ctx.tracker.track_operation(
                    entity=entity,
                    action=action.value if isinstance(action, Action) else action,
                    status_code=status_code,
                    timing_ms=timing_ms,
                    error_type=error_type,
                )


class _DownloadOperationHandler:
    """Handler for download operations.

    Supports two modes:
    - Two-step (with x-airbyte-file-url): metadata request → extract URL → stream file
    - One-step (without x-airbyte-file-url): stream file directly from endpoint
    """

    def __init__(self, context: _OperationContext):
        self.ctx = context

    def can_handle(self, action: Action) -> bool:
        """Check if this handler can handle the given action."""
        return action == Action.DOWNLOAD

    async def execute_operation(self, entity: str, action: Action, params: dict[str, Any]) -> AsyncIterator[bytes]:
        """Execute download operation (one-step or two-step) with full telemetry."""
        tracer = trace.get_tracer("airbyte.connector-sdk.executor.local")

        with tracer.start_as_current_span("airbyte.local_executor.execute_operation") as span:
            # Add span attributes
            span.set_attribute("connector.name", self.ctx.executor.model.name)
            span.set_attribute("connector.entity", entity)
            span.set_attribute("connector.action", action.value)
            if params:
                span.set_attribute("connector.param_keys", list(params.keys()))

            # Increment operation counter
            self.ctx.session.increment_operations()

            # Track operation timing and status
            start_time = time.time()
            error_type = None
            status_code = None

            try:
                # Look up entity
                entity_def = self.ctx.entity_index.get(entity)
                if not entity_def:
                    raise EntityNotFoundError(f"Entity '{entity}' not found in connector. Available entities: {list(self.ctx.entity_index.keys())}")

                # Look up operation
                operation = self.ctx.operation_index.get((entity, action))
                if not operation:
                    raise ActionNotSupportedError(
                        f"Action '{action.value}' not supported for entity '{entity}'. Supported actions: {[a.value for a in entity_def.actions]}"
                    )

                # Common setup for both download modes
                actual_path = operation.path_override.path if operation.path_override else operation.path
                path = self.ctx.build_path(actual_path, params)
                query_params = self.ctx.extract_query_params(operation.query_params, params)

                # Serialize deepObject parameters to bracket notation
                if operation.deep_object_params:
                    query_params = self.ctx.executor._serialize_deep_object_params(query_params, operation.deep_object_params)

                # Prepare headers (with optional Range support)
                range_header = params.get("range_header")
                headers = {"Accept": "*/*"}
                if range_header is not None:
                    headers["Range"] = range_header

                # Check download mode: two-step (with file_field) or one-step (without)
                file_field = operation.file_field

                if file_field:
                    # Substitute template variables in file_field (e.g., "attachments[{index}].url")
                    file_field = LocalExecutor._substitute_file_field_params(file_field, params)

                if file_field:
                    # Two-step download: metadata → extract URL → stream file
                    # Step 1: Get metadata (standard request)
                    request_body = self.ctx.build_request_body(
                        endpoint=operation,
                        params=params,
                    )
                    request_format = self.ctx.determine_request_format(operation, request_body)
                    self.ctx.validate_required_body_fields(operation, params, action, entity)

                    metadata_response, _ = await self.ctx.http_client.request(
                        method=operation.method,
                        path=path,
                        params=query_params,
                        **request_format,
                    )

                    # Step 2: Extract file URL from metadata
                    file_url = LocalExecutor._extract_download_url(
                        response=metadata_response,
                        file_field=file_field,
                        entity=entity,
                    )

                    # Step 3: Stream file from extracted URL
                    file_response, _ = await self.ctx.http_client.request(
                        method="GET",
                        path=file_url,
                        headers=headers,
                        stream=True,
                    )
                else:
                    # One-step direct download: stream file directly from endpoint
                    file_response, _ = await self.ctx.http_client.request(
                        method=operation.method,
                        path=path,
                        params=query_params,
                        headers=headers,
                        stream=True,
                    )

                # Assume success once we start streaming
                status_code = 200

                # Mark span as successful
                span.set_attribute("connector.success", True)
                span.set_attribute("http.status_code", status_code)

                # Stream file chunks
                default_chunk_size = 8 * 1024 * 1024  # 8 MB
                async for chunk in file_response.original_response.aiter_bytes(chunk_size=default_chunk_size):
                    # Log each chunk for cassette recording
                    self.ctx.logger.log_chunk_fetch(chunk)
                    yield chunk

            except (EntityNotFoundError, ActionNotSupportedError) as e:
                # Validation errors - record in span
                error_type = type(e).__name__
                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", error_type)
                span.record_exception(e)

                # Track the failed operation before re-raising
                timing_ms = (time.time() - start_time) * 1000
                self.ctx.tracker.track_operation(
                    entity=entity,
                    action=action.value,
                    status_code=status_code,
                    timing_ms=timing_ms,
                    error_type=error_type,
                )
                raise

            except Exception as e:
                # Capture error details
                error_type = type(e).__name__

                # Try to get status code from HTTP errors
                if hasattr(e, "response") and hasattr(e.response, "status_code"):
                    status_code = e.response.status_code
                    span.set_attribute("http.status_code", status_code)

                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", error_type)
                span.record_exception(e)

                # Track the failed operation before re-raising
                timing_ms = (time.time() - start_time) * 1000
                self.ctx.tracker.track_operation(
                    entity=entity,
                    action=action.value,
                    status_code=status_code,
                    timing_ms=timing_ms,
                    error_type=error_type,
                )
                raise

            finally:
                # Track successful operation (if no exception was raised)
                # Note: For generators, this runs after all chunks are yielded
                if error_type is None:
                    timing_ms = (time.time() - start_time) * 1000
                    self.ctx.tracker.track_operation(
                        entity=entity,
                        action=action.value,
                        status_code=status_code,
                        timing_ms=timing_ms,
                        error_type=None,
                    )
