"""Hosted executor for proxying operations through the cloud API."""

from __future__ import annotations

from opentelemetry import trace

from ..cloud_utils import AirbyteCloudClient

from .models import (
    ExecutionConfig,
    ExecutionResult,
)


class HostedExecutor:
    """Executor that proxies execution through the Airbyte Cloud API.

    This is the "hosted mode" executor that makes HTTP calls to the cloud API
    instead of directly calling external services. The cloud API handles all
    connector logic, secrets management, and execution.

    The executor uses the AirbyteCloudClient to:
    1. Authenticate with the Airbyte Platform (bearer token with caching)
    2. Look up the user's connector (if connector_id not provided)
    3. Execute the connector operation via the cloud API

    Implements ExecutorProtocol.

    Example:
        # Create executor with explicit connector_id (no lookup needed)
        executor = HostedExecutor(
            airbyte_client_id="client_abc123",
            airbyte_client_secret="secret_xyz789",
            connector_id="existing-source-uuid",
        )

        # Or create executor with user ID for lookup
        executor = HostedExecutor(
            airbyte_client_id="client_abc123",
            airbyte_client_secret="secret_xyz789",
            external_user_id="user-123",
            connector_definition_id="abc123-def456-ghi789",
        )

        # Execute an operation
        execution_config = ExecutionConfig(
            entity="customers",
            action="list",
            params={"limit": 10}
        )

        result = await executor.execute(execution_config)
        if result.success:
            print(f"Data: {result.data}")
        else:
            print(f"Error: {result.error}")
    """

    def __init__(
        self,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        connector_id: str | None = None,
        external_user_id: str | None = None,
        connector_definition_id: str | None = None,
    ):
        """Initialize hosted executor.

        Either provide connector_id directly OR (external_user_id + connector_definition_id)
        for lookup.

        Args:
            airbyte_client_id: Airbyte client ID for authentication
            airbyte_client_secret: Airbyte client secret for authentication
            connector_id: Direct connector/source ID (skips lookup if provided)
            external_user_id: User identifier in the Airbyte system (for lookup)
            connector_definition_id: Connector definition ID (for lookup)

        Raises:
            ValueError: If neither connector_id nor (external_user_id + connector_definition_id) provided

        Example:
            # With explicit connector_id (no lookup)
            executor = HostedExecutor(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid",
            )

            # With lookup by user + definition
            executor = HostedExecutor(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                external_user_id="user-123",
                connector_definition_id="abc123-def456-ghi789",
            )
        """
        # Validate: either connector_id OR (external_user_id + connector_definition_id) required
        if not connector_id and not (external_user_id and connector_definition_id):
            raise ValueError("Either connector_id OR (external_user_id + connector_definition_id) must be provided")

        self._connector_id = connector_id
        self._external_user_id = external_user_id
        self._connector_definition_id = connector_definition_id

        # Create AirbyteCloudClient for API interactions
        self._cloud_client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
        )

    async def execute(self, config: ExecutionConfig) -> ExecutionResult:
        """Execute connector via cloud API (ExecutorProtocol implementation).

        Flow:
        1. Use provided connector_id or look up from external_user_id + definition_id
        2. Execute the connector operation via the cloud API
        3. Parse the response into ExecutionResult

        Args:
            config: Execution configuration (entity, action, params)

        Returns:
            ExecutionResult with success/failure status

        Raises:
            ValueError: If no connector or multiple connectors found for user (when doing lookup)
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            config = ExecutionConfig(
                entity="customers",
                action="list",
                params={"limit": 10}
            )
            result = await executor.execute(config)
        """
        tracer = trace.get_tracer("airbyte.connector-sdk.executor.hosted")

        with tracer.start_as_current_span("airbyte.hosted_executor.execute") as span:
            # Add span attributes for observability
            if self._connector_definition_id:
                span.set_attribute("connector.definition_id", self._connector_definition_id)
            span.set_attribute("connector.entity", config.entity)
            span.set_attribute("connector.action", config.action)
            if self._external_user_id:
                span.set_attribute("user.external_id", self._external_user_id)
            if config.params:
                # Only add non-sensitive param keys
                span.set_attribute("connector.param_keys", list(config.params.keys()))

            try:
                # Use provided connector_id or look it up
                if self._connector_id:
                    connector_id = self._connector_id
                else:
                    # Look up connector by external_user_id + definition_id
                    connector_id = await self._cloud_client.get_connector_id(
                        external_user_id=self._external_user_id,  # type: ignore[arg-type]
                        connector_definition_id=self._connector_definition_id,  # type: ignore[arg-type]
                    )

                span.set_attribute("connector.connector_id", connector_id)

                # Step 3: Execute the connector via the cloud API
                response = await self._cloud_client.execute_connector(
                    connector_id=connector_id,
                    entity=config.entity,
                    action=config.action,
                    params=config.params,
                )

                # Step 4: Parse the response into ExecutionResult
                result = self._parse_execution_result(response)

                # Mark span as successful
                span.set_attribute("connector.success", result.success)

                return result

            except ValueError as e:
                # Connector lookup validation error (0 or >1 connectors)
                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", "ValueError")
                span.record_exception(e)
                raise

            except Exception as e:
                # HTTP errors and other exceptions
                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", type(e).__name__)
                span.record_exception(e)
                raise

    async def check(self) -> ExecutionResult:
        """Perform a health check via the cloud API."""
        config = ExecutionConfig(entity="*", action="check", params={})
        return await self.execute(config)

    def _parse_execution_result(self, response: dict) -> ExecutionResult:
        """Parse API response into ExecutionResult.

        Args:
            response_data: Raw JSON response from the cloud API

        Returns:
            ExecutionResult with parsed data
        """

        return ExecutionResult(
            success=True,
            data=response["result"],
            meta=response.get("connector_metadata"),
            error=None,
        )

    async def close(self):
        """Close the cloud client and cleanup resources.

        Call this when you're done using the executor to clean up HTTP connections.

        Example:
            executor = HostedExecutor(...)
            try:
                result = await executor.execute(config)
            finally:
                await executor.close()
        """
        await self._cloud_client.close()
