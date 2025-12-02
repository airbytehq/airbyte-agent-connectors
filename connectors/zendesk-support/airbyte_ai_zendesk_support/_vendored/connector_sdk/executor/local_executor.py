"""Local executor for direct HTTP execution of connector operations."""

from __future__ import annotations

import asyncio
import os
import re
import time
from typing import Any
from urllib.parse import quote

from ..constants import (
    DEFAULT_MAX_CONNECTIONS,
    DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
)
from ..secrets import SecretStr
from ..http_client import HTTPClient
from ..config_loader import load_connector_config
from ..logging import NullLogger, RequestLogger
from ..observability import ObservabilitySession
from ..telemetry import SegmentTracker
from ..types import ConnectorConfig, ResourceDefinition, Verb

from .models import (
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    ResourceNotFoundError,
    VerbNotSupportedError,
    MissingParameterError,
    InvalidParameterError,
)


class LocalExecutor:
    """Async executor for Resource×Verb operations with direct HTTP execution.

    This is the "local mode" executor that makes direct HTTP calls to external APIs.
    It performs local resource/verb lookups, validation, and request building.

    Implements ExecutorProtocol.
    """

    def __init__(
        self,
        config_path: str,
        secrets: dict[str, SecretStr],
        enable_logging: bool = False,
        log_file: str | None = None,
        execution_context: str | None = None,
        max_connections: int = DEFAULT_MAX_CONNECTIONS,
        max_keepalive_connections: int = DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
        max_logs: int | None = 10000,
    ):
        """Initialize async executor.

        Args:
            config_path: Path to connector.yaml
            secrets: Secret credentials for authentication (e.g., {"token": SecretStr("sk_...")})
            enable_logging: Enable request/response logging
            log_file: Path to log file (if enable_logging=True)
            execution_context: Execution context (mcp, direct, blessed, agent)
            max_connections: Maximum number of concurrent connections
            max_keepalive_connections: Maximum number of keepalive connections
            max_logs: Maximum number of logs to keep in memory before rotation.
                Set to None for unlimited (not recommended for production).
                Defaults to 10000.
        """
        self.config: ConnectorConfig = load_connector_config(config_path)
        self.secrets = secrets

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
            secrets=secrets,
            logger=self.logger,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
        )

        # Build O(1) lookup indexes
        self._resource_index: dict[str, ResourceDefinition] = {
            resource.name: resource for resource in self.config.resources
        }

        # Build O(1) operation index: (resource, verb) -> endpoint
        self._operation_index: dict[tuple[str, Verb], Any] = {}
        for resource in self.config.resources:
            for verb in resource.verbs:
                endpoint = resource.endpoints.get(verb)
                if endpoint:
                    self._operation_index[(resource.name, verb)] = endpoint

    async def execute(self, config: ExecutionConfig) -> ExecutionResult:
        """Execute connector with given configuration (ExecutorProtocol implementation).

        This method implements the ExecutorProtocol interface. It wraps the internal
        _execute_operation() method to provide a consistent interface with HostedExecutor.

        Args:
            config: Execution configuration (resource, verb, params)

        Returns:
            ExecutionResult with success/failure status

        Raises:
            Infrastructure exceptions: Network errors, auth failures, etc.

        Example:
            config = ExecutionConfig(
                resource="customers",
                verb="list",
                params={"limit": 10}
            )
            result = await executor.execute(config)
            if result.success:
                print(result.data)
        """
        try:
            # Call the internal execute method
            response_data = await self._execute_operation(
                resource=config.resource, verb=config.verb, params=config.params
            )

            # Wrap successful response in ExecutionResult
            return ExecutionResult(success=True, data=response_data, error=None)

        except (
            ResourceNotFoundError,
            VerbNotSupportedError,
            MissingParameterError,
            InvalidParameterError,
        ) as e:
            # These are "expected" execution errors - return them in ExecutionResult
            return ExecutionResult(success=False, data={}, error=str(e))

        # All other exceptions (network errors, auth failures) are raised as-is
        # This includes HTTP errors from the http_client

    async def _execute_operation(
        self,
        resource: str,
        verb: str | Verb,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Internal method: Execute a verb on a resource asynchronously.

        This is the internal implementation used by execute().
        External code should use execute(config) instead.

        Args:
            resource: Resource name (e.g., "Customer")
            verb: Verb to execute (e.g., "get" or Verb.GET)
            params: Parameters for the operation
                - For GET: {"id": "cus_123"} for path params
                - For LIST: {"limit": 10} for query params
                - For CREATE/UPDATE: {"email": "...", "name": "..."} for body

        Returns:
            API response as dictionary

        Raises:
            ValueError: If resource or verb not found
            HTTPClientError: If API request fails
        """
        params = params or {}
        verb = Verb(verb) if isinstance(verb, str) else verb

        # Increment operation counter
        self.session.increment_operations()

        # Track operation timing and status
        start_time = time.time()
        error_type = None
        status_code = None

        try:
            # O(1) resource lookup
            resource_def = self._resource_index.get(resource)
            if not resource_def:
                available_resources = list(self._resource_index.keys())
                raise ResourceNotFoundError(
                    f"Resource '{resource}' not found in connector. "
                    f"Available resources: {available_resources}"
                )

            # Check if verb is supported
            if verb not in resource_def.verbs:
                supported_verbs = [v.value for v in resource_def.verbs]
                raise VerbNotSupportedError(
                    f"Verb '{verb.value}' not supported for resource '{resource}'. "
                    f"Supported verbs: {supported_verbs}"
                )

            # O(1) operation lookup
            endpoint = self._operation_index.get((resource, verb))
            if not endpoint:
                raise ExecutorError(
                    f"No endpoint defined for {resource}.{verb.value}. "
                    f"This is a configuration error."
                )

            # Validate required body fields for CREATE/UPDATE operations
            self._validate_required_body_fields(endpoint, params, verb, resource)

            # Build request parameters
            # Use path_override if available, otherwise use the OpenAPI path
            actual_path = (
                endpoint.path_override.path if endpoint.path_override else endpoint.path
            )
            path = self._build_path(actual_path, params)
            query_params = self._extract_query_params(endpoint.query_params, params)

            # Build request body (GraphQL or standard)
            body = self._build_request_body(endpoint, params)

            # Determine request format (json/data parameters)
            request_kwargs = self._determine_request_format(endpoint, body)

            # Execute async HTTP request
            response = await self.http_client.request(
                method=endpoint.method,
                path=path,
                params=query_params if query_params else None,
                json=request_kwargs.get("json"),
                data=request_kwargs.get("data"),
            )

            # Assume success with 200 status code if no exception raised
            status_code = 200
            return response

        except Exception as e:
            # Capture error details
            error_type = type(e).__name__

            # Try to get status code from HTTP errors
            if hasattr(e, "response") and hasattr(e.response, "status_code"):
                status_code = e.response.status_code

            raise

        finally:
            # Always track operation (success or failure)
            timing_ms = (time.time() - start_time) * 1000
            self.tracker.track_operation(
                resource=resource,
                verb=verb.value if isinstance(verb, Verb) else verb,
                status_code=status_code,
                timing_ms=timing_ms,
                error_type=error_type,
            )

    async def execute_batch(
        self, operations: list[tuple[str, str | Verb, dict[str, Any] | None]]
    ) -> list[dict[str, Any]]:
        """Execute multiple operations concurrently.

        Args:
            operations: List of (resource, verb, params) tuples

        Returns:
            List of responses in the same order as operations

        Raises:
            ValueError: If any resource or verb not found
            HTTPClientError: If any API request fails

        Example:
            results = await executor.execute_batch([
                ("Customer", "list", {"limit": 10}),
                ("Customer", "get", {"id": "cus_123"}),
                ("Customer", "get", {"id": "cus_456"}),
            ])
        """
        # Create tasks for all operations
        tasks = [
            self._execute_operation(resource, verb, params)
            for resource, verb, params in operations
        ]

        # Execute all tasks concurrently using asyncio.gather
        results = await asyncio.gather(*tasks)
        return results

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
        self, endpoint: Any, params: dict[str, Any], verb: Verb, resource: str
    ) -> None:
        """Validate that required body fields are present for CREATE/UPDATE operations.

        Args:
            endpoint: Endpoint definition
            params: Parameters provided
            verb: Operation verb
            resource: Resource name

        Raises:
            MissingParameterError: If required body fields are missing
        """
        # Only validate for operations that typically have required body fields
        if verb not in (Verb.CREATE, Verb.UPDATE):
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
                f"Missing required body fields for {resource}.{verb.value}: {missing_fields}. "
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
