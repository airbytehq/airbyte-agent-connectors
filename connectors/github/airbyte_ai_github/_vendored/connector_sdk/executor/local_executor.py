"""Local executor for direct HTTP execution of connector operations."""

from __future__ import annotations

import asyncio
import inspect
import os
import re
import time
from typing import Any, AsyncIterator, Protocol
from urllib.parse import quote

from opentelemetry import trace

from ..constants import (
    DEFAULT_MAX_CONNECTIONS,
    DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
)
from ..secrets import SecretStr
from ..http_client import HTTPClient, TokenRefreshCallback
from ..config_loader import load_connector_config
from ..logging import NullLogger, RequestLogger
from ..observability import ObservabilitySession
from ..auth_template import apply_auth_mapping
from ..telemetry import SegmentTracker
from ..types import ConnectorConfig, EntityDefinition, Action

from .models import (
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    EntityNotFoundError,
    ActionNotSupportedError,
    MissingParameterError,
    InvalidParameterError,
)


class _OperationContext:
    """Shared context for operation handlers."""

    def __init__(self, executor: "LocalExecutor"):
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
        self.build_request_body = executor._build_request_body
        self.determine_request_format = executor._determine_request_format
        self.validate_required_body_fields = executor._validate_required_body_fields


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
    ) -> dict[str, Any] | AsyncIterator[bytes]:
        """Execute the operation and return result."""
        ...


class LocalExecutor:
    """Async executor for Entity×Action operations with direct HTTP execution.

    This is the "local mode" executor that makes direct HTTP calls to external APIs.
    It performs local entity/action lookups, validation, and request building.

    Implements ExecutorProtocol.
    """

    def __init__(
        self,
        config_path: str,
        secrets: dict[str, SecretStr] | None = None,
        auth_config: dict[str, SecretStr] | None = None,
        enable_logging: bool = False,
        log_file: str | None = None,
        execution_context: str | None = None,
        max_connections: int = DEFAULT_MAX_CONNECTIONS,
        max_keepalive_connections: int = DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
        max_logs: int | None = 10000,
        config_values: dict[str, str] | None = None,
        on_token_refresh: TokenRefreshCallback = None,
    ):
        """Initialize async executor.

        Args:
            config_path: Path to connector.yaml
            secrets: (Legacy) Auth parameters that bypass x-airbyte-auth-config mapping.
                Directly passed to auth strategies (e.g., {"username": "...", "password": "..."}).
                Cannot be used together with auth_config.
            auth_config: User-facing auth configuration following x-airbyte-auth-config spec.
                Will be transformed via auth_mapping to produce auth parameters.
                Cannot be used together with secrets.
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
        """
        # Validate mutual exclusivity
        if secrets is not None and auth_config is not None:
            raise ValueError(
                "Cannot provide both 'secrets' and 'auth_config' parameters. "
                "Use 'auth_config' for user-facing credentials (recommended), "
                "or 'secrets' for direct auth parameters (legacy)."
            )

        self.config: ConnectorConfig = load_connector_config(config_path)
        self.on_token_refresh = on_token_refresh

        # Determine which credentials to use and whether to apply mapping
        if auth_config is not None:
            # Apply auth config mapping (user-facing → auth parameters)
            self.secrets = self._apply_auth_config_mapping(auth_config)
        elif secrets is not None:
            # Use secrets directly (bypass mapping - legacy behavior)
            self.secrets = secrets
        else:
            # No credentials provided
            self.secrets = None

        self.config_values = config_values or {}

        # Create shared observability session
        self.session = ObservabilitySession(
            connector_name=self.config.name,
            connector_version=getattr(self.config, "version", None),
            execution_context=(
                execution_context or os.getenv("AIRBYTE_EXECUTION_CONTEXT", "direct")
            ),
        )

        # Initialize telemetry tracker
        self.tracker = SegmentTracker(self.session)
        self.tracker.track_connector_init(
            connector_version=getattr(self.config, "version", None)
        )

        # Initialize logger
        if enable_logging:
            self.logger = RequestLogger(
                log_file=log_file,
                connector_name=self.config.name,
                max_logs=max_logs,
            )
        else:
            self.logger = NullLogger()

        # Initialize async HTTP client with connection pooling
        self.http_client = HTTPClient(
            base_url=self.config.base_url,
            auth_config=self.config.auth,
            secrets=self.secrets,
            config_values=self.config_values,
            logger=self.logger,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            on_token_refresh=on_token_refresh,
        )

        # Build O(1) lookup indexes
        self._entity_index: dict[str, EntityDefinition] = {
            entity.name: entity for entity in self.config.entities
        }

        # Build O(1) operation index: (entity, action) -> endpoint
        self._operation_index: dict[tuple[str, Action], Any] = {}
        for entity in self.config.entities:
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

    def _apply_auth_config_mapping(
        self, user_secrets: dict[str, SecretStr]
    ) -> dict[str, SecretStr]:
        """Apply auth_mapping from x-airbyte-auth-config to transform user secrets.

        This method takes user-provided secrets (e.g., {"api_token": "abc123"}) and
        transforms them into the auth scheme format (e.g., {"username": "abc123", "password": "api_token"})
        using the template mappings defined in x-airbyte-auth-config.

        Args:
            user_secrets: User-provided secrets from config

        Returns:
            Transformed secrets matching the auth scheme requirements
        """
        if not self.config.auth.user_config_spec:
            # No x-airbyte-auth-config defined, use secrets as-is
            return user_secrets

        user_config_spec = self.config.auth.user_config_spec
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

        # Convert SecretStr values to plain strings for template processing
        user_config_values = {
            key: (
                value.get_secret_value()
                if hasattr(value, "get_secret_value")
                else str(value)
            )
            for key, value in user_secrets.items()
        }

        # Apply the auth_mapping templates, passing required_fields so optional
        # fields that are not provided can be skipped
        mapped_values = apply_auth_mapping(
            auth_mapping, user_config_values, required_fields=required_fields
        )

        # Convert back to SecretStr
        mapped_secrets = {key: SecretStr(value) for key, value in mapped_values.items()}

        return mapped_secrets

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
            # Convert config to internal format
            action = (
                Action(config.action)
                if isinstance(config.action, str)
                else config.action
            )
            params = config.params or {}

            # Dispatch to handler (handlers handle telemetry internally)
            handler = next(
                (h for h in self._operation_handlers if h.can_handle(action)), None
            )
            if not handler:
                raise ExecutorError(
                    f"No handler registered for action '{action.value}'."
                )

            # Execute handler
            result = handler.execute_operation(config.entity, action, params)

            # Handle AsyncIterator (download) vs dict (standard)
            if inspect.isasyncgen(result):
                # Download: return stream in ExecutionResult
                return ExecutionResult(success=True, data=result, error=None)

            # Standard: await coroutine and return
            response_data = await result
            return ExecutionResult(success=True, data=response_data, error=None)

        except (
            EntityNotFoundError,
            ActionNotSupportedError,
            MissingParameterError,
            InvalidParameterError,
        ) as e:
            # These are "expected" execution errors - return them in ExecutionResult
            return ExecutionResult(success=False, data={}, error=str(e))

    async def _execute_operation(
        self,
        entity: str,
        action: str | Action,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Internal method: Execute an action on an entity asynchronously.

        This method now delegates to the appropriate handler.
        External code should use execute(config) instead.

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
        handler = next(
            (h for h in self._operation_handlers if h.can_handle(action)), None
        )
        if not handler:
            raise ExecutorError(f"No handler registered for action '{action.value}'.")

        return await handler.execute_operation(entity, action, params)

    async def execute_batch(
        self, operations: list[tuple[str, str | Action, dict[str, Any] | None]]
    ) -> list[dict[str, Any] | AsyncIterator[bytes]]:
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
            handler = next(
                (h for h in self._operation_handlers if h.can_handle(action)), None
            )
            if not handler:
                raise ExecutorError(
                    f"No handler registered for action '{action.value}'."
                )

            # Call handler directly (exceptions propagate naturally)
            tasks.append(handler.execute_operation(entity, action, params))

        # Execute all tasks concurrently - exceptions propagate via asyncio.gather
        return await asyncio.gather(*tasks)

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
                    f"Missing required path parameter '{placeholder}' for path '{path_template}'. "
                    f"Provided parameters: {list(params.keys())}"
                )

            # Validate parameter value is not None or empty string
            value = params[placeholder]
            if value is None or (isinstance(value, str) and value.strip() == ""):
                raise InvalidParameterError(
                    f"Path parameter '{placeholder}' cannot be None or empty string"
                )

            encoded_value = quote(str(value), safe="")
            path = path.replace(f"{{{placeholder}}}", encoded_value)

        return path

    def _extract_query_params(
        self, allowed_params: list[str], params: dict[str, Any]
    ) -> dict[str, Any]:
        """Extract query parameters from params.

        Args:
            allowed_params: List of allowed query parameter names
            params: All parameters

        Returns:
            Dictionary of query parameters
        """
        return {key: value for key, value in params.items() if key in allowed_params}

    def _extract_body(
        self, allowed_fields: list[str], params: dict[str, Any]
    ) -> dict[str, Any]:
        """Extract body fields from params.

        Args:
            allowed_fields: List of allowed body field names
            params: All parameters

        Returns:
            Dictionary of body fields
        """
        return {key: value for key, value in params.items() if key in allowed_fields}

    @staticmethod
    def _extract_download_url(
        response: dict[str, Any],
        file_field: str,
        entity: str,
    ) -> str:
        """Extract download URL from metadata response using x-airbyte-file-url.

        Args:
            response: Metadata response containing file reference
            file_field: JSON path to file URL field (from x-airbyte-file-url)
            entity: Entity name (for error messages)

        Returns:
            Extracted file URL

        Raises:
            ExecutorError: If file field not found or invalid
        """
        # Navigate nested path (e.g., "article_attachment.content_url")
        parts = file_field.split(".")
        current = response

        for i, part in enumerate(parts):
            if not isinstance(current, dict):
                raise ExecutorError(
                    f"Cannot extract download URL for {entity}: "
                    f"Expected dict at '{'.'.join(parts[:i])}', got {type(current).__name__}"
                )

            if part not in current:
                raise ExecutorError(
                    f"Cannot extract download URL for {entity}: "
                    f"Field '{part}' not found in response. Available fields: {list(current.keys())}"
                )

            current = current[part]

        if not isinstance(current, str):
            raise ExecutorError(
                f"Cannot extract download URL for {entity}: "
                f"Expected string at '{file_field}', got {type(current).__name__}"
            )

        return current

    def _build_request_body(
        self, endpoint: Any, params: dict[str, Any]
    ) -> dict[str, Any] | None:
        """Build request body (GraphQL or standard).

        Args:
            endpoint: Endpoint definition
            params: Parameters from execute() call

        Returns:
            Request body dict or None if no body needed
        """
        if endpoint.graphql_body:
            return self._build_graphql_body(endpoint.graphql_body, params)
        elif endpoint.body_fields:
            return self._extract_body(endpoint.body_fields, params)
        return None

    def _determine_request_format(
        self, endpoint: Any, body: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Determine json/data parameters for HTTP request.

        GraphQL always uses JSON, regardless of content_type setting.

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
            return {"data": body}

        return {}

    def _process_graphql_fields(
        self, query: str, graphql_config: dict[str, Any], params: dict[str, Any]
    ) -> str:
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
        self, graphql_config: dict[str, Any], params: dict[str, Any]
    ) -> dict[str, Any]:
        """Build GraphQL request body with variable substitution and field selection.

        Args:
            graphql_config: GraphQL configuration from x-airbyte-body-type extension
            params: Parameters from execute() call

        Returns:
            GraphQL request body: {"query": "...", "variables": {...}}
        """
        query = graphql_config["query"]

        # Process field selection (dynamic fields or default fields)
        query = self._process_graphql_fields(query, graphql_config, params)

        body = {"query": query}

        # Substitute variables from params
        if "variables" in graphql_config and graphql_config["variables"]:
            body["variables"] = self._interpolate_variables(
                graphql_config["variables"], params
            )

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
        graphql_fields = [
            self._convert_nested_field_to_graphql(field) for field in fields
        ]

        # Replace placeholder with field list
        fields_str = " ".join(graphql_fields)
        return query.replace("{{ fields }}", fields_str)

    def _interpolate_variables(
        self, variables: dict[str, Any], params: dict[str, Any]
    ) -> dict[str, Any]:
        """Recursively interpolate variables using params.

        Preserves types (doesn't stringify everything).

        Supports:
        - Direct replacement: "{{ owner }}" → params["owner"] (preserves type)
        - Nested objects: {"input": {"name": "{{ name }}"}}
        - Arrays: [{"id": "{{ id }}"}]

        Args:
            variables: Variables dict with template placeholders
            params: Parameters to substitute

        Returns:
            Interpolated variables dict with types preserved
        """

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
                return value
            elif isinstance(value, dict):
                return {k: interpolate_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [interpolate_value(item) for item in value]
            else:
                return value

        return interpolate_value(variables)

    def _validate_required_body_fields(
        self, endpoint: Any, params: dict[str, Any], action: Action, entity: str
    ) -> None:
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

        # Check if endpoint has body fields defined
        if not endpoint.body_fields:
            return

        # For now, we treat all body_fields as potentially required for CREATE/UPDATE
        # In a more advanced implementation, we could parse the request schema
        # to identify truly required fields
        missing_fields = []
        for field in endpoint.body_fields:
            if field not in params:
                missing_fields.append(field)

        if missing_fields:
            raise MissingParameterError(
                f"Missing required body fields for {entity}.{action.value}: {missing_fields}. "
                f"Provided parameters: {list(params.keys())}"
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
    """Handler for standard REST operations (GET, LIST, CREATE, UPDATE, DELETE, SEARCH, AUTHORIZE)."""

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
            Action.SEARCH,
            Action.AUTHORIZE,
        }

    async def execute_operation(
        self, entity: str, action: Action, params: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute standard REST operation with full telemetry and error handling."""
        tracer = trace.get_tracer("airbyte.connector-sdk.executor.local")

        with tracer.start_as_current_span("local_executor.execute_operation") as span:
            # Add span attributes
            span.set_attribute("connector.name", self.ctx.executor.config.name)
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
                    raise EntityNotFoundError(
                        f"Entity '{entity}' not found in connector. "
                        f"Available entities: {available_entities}"
                    )

                # Check if action is supported
                if action not in entity_def.actions:
                    supported_actions = [a.value for a in entity_def.actions]
                    raise ActionNotSupportedError(
                        f"Action '{action.value}' not supported for entity '{entity}'. "
                        f"Supported actions: {supported_actions}"
                    )

                # O(1) operation lookup
                endpoint = self.ctx.operation_index.get((entity, action))
                if not endpoint:
                    raise ExecutorError(
                        f"No endpoint defined for {entity}.{action.value}. "
                        f"This is a configuration error."
                    )

                # Validate required body fields for CREATE/UPDATE operations
                self.ctx.validate_required_body_fields(endpoint, params, action, entity)

                # Build request parameters
                # Use path_override if available, otherwise use the OpenAPI path
                actual_path = (
                    endpoint.path_override.path
                    if endpoint.path_override
                    else endpoint.path
                )
                path = self.ctx.build_path(actual_path, params)
                query_params = self.ctx.extract_query_params(
                    endpoint.query_params, params
                )

                # Build request body (GraphQL or standard)
                body = self.ctx.build_request_body(endpoint, params)

                # Determine request format (json/data parameters)
                request_kwargs = self.ctx.determine_request_format(endpoint, body)

                # Execute async HTTP request
                response = await self.ctx.http_client.request(
                    method=endpoint.method,
                    path=path,
                    params=query_params if query_params else None,
                    json=request_kwargs.get("json"),
                    data=request_kwargs.get("data"),
                )

                # Assume success with 200 status code if no exception raised
                status_code = 200

                # Mark span as successful
                span.set_attribute("connector.success", True)
                span.set_attribute("http.status_code", status_code)

                return response

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

    async def execute_operation(
        self, entity: str, action: Action, params: dict[str, Any]
    ) -> AsyncIterator[bytes]:
        """Execute download operation (one-step or two-step) with full telemetry."""
        tracer = trace.get_tracer("airbyte.connector-sdk.executor.local")

        with tracer.start_as_current_span("local_executor.execute_operation") as span:
            # Add span attributes
            span.set_attribute("connector.name", self.ctx.executor.config.name)
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
                    raise EntityNotFoundError(
                        f"Entity '{entity}' not found in connector. "
                        f"Available entities: {list(self.ctx.entity_index.keys())}"
                    )

                # Look up operation
                operation = self.ctx.operation_index.get((entity, action))
                if not operation:
                    raise ActionNotSupportedError(
                        f"Action '{action.value}' not supported for entity '{entity}'. "
                        f"Supported actions: {[a.value for a in entity_def.actions]}"
                    )

                # Common setup for both download modes
                actual_path = (
                    operation.path_override.path
                    if operation.path_override
                    else operation.path
                )
                path = self.ctx.build_path(actual_path, params)
                query_params = self.ctx.extract_query_params(
                    operation.query_params, params
                )

                # Prepare headers (with optional Range support)
                range_header = params.get("range_header")
                headers = {"Accept": "*/*"}
                if range_header is not None:
                    headers["Range"] = range_header

                # Check download mode: two-step (with file_field) or one-step (without)
                file_field = operation.file_field

                if file_field:
                    # Two-step download: metadata → extract URL → stream file
                    # Step 1: Get metadata (standard request)
                    request_body = self.ctx.build_request_body(
                        endpoint=operation,
                        params=params,
                    )
                    request_format = self.ctx.determine_request_format(
                        operation, request_body
                    )
                    self.ctx.validate_required_body_fields(
                        operation, params, action, entity
                    )

                    metadata_response = await self.ctx.http_client.request(
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
                    file_response = await self.ctx.http_client.request(
                        method="GET",
                        path=file_url,
                        headers=headers,
                        stream=True,
                    )
                else:
                    # One-step direct download: stream file directly from endpoint
                    file_response = await self.ctx.http_client.request(
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
                async for chunk in file_response.original_response.aiter_bytes(
                    chunk_size=default_chunk_size
                ):
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
