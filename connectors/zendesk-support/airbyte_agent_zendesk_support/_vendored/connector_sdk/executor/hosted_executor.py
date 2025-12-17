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

    The executor takes an external_user_id and uses the AirbyteCloudClient to:
    1. Authenticate with the Airbyte Platform (bearer token with caching)
    2. Look up the user's connector instance
    3. Execute the connector operation via the cloud API

    Implements ExecutorProtocol.

    Example:
        # Create executor with user ID, credentials, and connector definition ID
        executor = HostedExecutor(
            external_user_id="user-123",
            airbyte_client_id="client_abc123",
            airbyte_client_secret="secret_xyz789",
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
        external_user_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        connector_definition_id: str,
    ):
        """Initialize hosted executor.

        Args:
            external_user_id: User identifier in the Airbyte system
            airbyte_client_id: Airbyte client ID for authentication
            airbyte_client_secret: Airbyte client secret for authentication
            connector_definition_id: Connector definition ID used to look up
                the user's connector instance.

        Example:
            executor = HostedExecutor(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_definition_id="abc123-def456-ghi789",
            )
        """
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
        1. Get connector id from connector model
        2. Look up the user's connector instance ID
        3. Execute the connector operation via the cloud API
        4. Parse the response into ExecutionResult

        Args:
            config: Execution configuration (entity, action, params)

        Returns:
            ExecutionResult with success/failure status

        Raises:
            ValueError: If no instance or multiple instances found for user
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
            span.set_attribute("connector.definition_id", self._connector_definition_id)
            span.set_attribute("connector.entity", config.entity)
            span.set_attribute("connector.action", config.action)
            span.set_attribute("user.external_id", self._external_user_id)
            if config.params:
                # Only add non-sensitive param keys
                span.set_attribute("connector.param_keys", list(config.params.keys()))

            try:
                # Step 1: Get connector definition id
                connector_definition_id = self._connector_definition_id

                # Step 2: Get the connector instance ID for this user
                instance_id = await self._cloud_client.get_connector_instance_id(
                    external_user_id=self._external_user_id,
                    connector_definition_id=connector_definition_id,
                )

                span.set_attribute("connector.instance_id", instance_id)

                # Step 3: Execute the connector via the cloud API
                response = await self._cloud_client.execute_connector(
                    instance_id=instance_id,
                    entity=config.entity,
                    action=config.action,
                    params=config.params,
                )

                # Step 4: Parse the response into ExecutionResult
                # The response_data is a dict from the API
                result = self._parse_execution_result(response)

                # Mark span as successful
                span.set_attribute("connector.success", result.success)

                return result

            except ValueError as e:
                # Instance lookup validation error (0 or >1 instances)
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
