"""Hosted executor for proxying operations through the backend API."""

from __future__ import annotations

import os
import httpx

from .models import (
    ExecutionConfig,
    ExecutionResult,
)


class HostedExecutor:
    """Executor that proxies execution through the Sonar backend API.

    This is the "hosted mode" executor that makes HTTP calls to the backend API
    instead of directly calling external services. The backend handles all
    connector logic, secrets management, and execution.

    The API URL is configured at initialization via the api_url parameter,
    which defaults to the AIRBYTE_CONNECTOR_API_URL environment variable.

    Implements ExecutorProtocol.

    Example:
        executor = HostedExecutor(
            connector_id="stripe-prod-123",
            airbyte_client_id="client_abc123",
            airbyte_client_secret="secret_xyz789"
        )

        config = ExecutionConfig(
            resource="customers",
            verb="list"
        )

        result = await executor.execute(config)
        if result.success:
            print(f"Data: {result.data}")
        else:
            print(f"Error: {result.error}")
    """

    def __init__(
        self,
        connector_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        api_url: str | None = None,
    ):
        """Initialize hosted executor.

        Args:
            connector_id: ID of the connector to execute (e.g., "stripe-prod-123")
            airbyte_client_id: Airbyte client ID for authentication
            airbyte_client_secret: Airbyte client secret for authentication
            api_url: API URL for the hosted executor backend. Defaults to
                AIRBYTE_CONNECTOR_API_URL environment variable or "http://localhost:8001"

        Example:
            executor = HostedExecutor(
                connector_id="my-connector-id",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Or with custom API URL:
            executor = HostedExecutor(
                connector_id="my-connector-id",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                api_url="https://api.production.com"
            )
        """
        self.connector_id = connector_id
        self.airbyte_client_id = airbyte_client_id
        self.airbyte_client_secret = airbyte_client_secret
        self.api_url = api_url or os.getenv(
            "AIRBYTE_CONNECTOR_API_URL", "http://localhost:8001"
        )

        # Create synchronous HTTP client
        # We use sync client even though execute() is async for simplicity
        # The async wrapper allows it to work with the protocol
        self.client = httpx.Client(
            timeout=httpx.Timeout(300.0),  # 5 minute timeout
            follow_redirects=True,
        )

    async def execute(self, config: ExecutionConfig) -> ExecutionResult:
        """Execute connector via backend API (ExecutorProtocol implementation).

        Makes an HTTP POST request to /connectors/{connector_id}/execute with
        OAuth authentication and the configuration in the request body.

        Args:
            config: Execution configuration (resource, verb, params)

        Returns:
            ExecutionResult with success/failure status

        Raises:
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            config = ExecutionConfig(
                resource="customers",
                verb="list"
            )
            result = await executor.execute(config)
        """
        # Build API URL from instance api_url
        url = f"{self.api_url}/connectors/{self.connector_id}/execute"

        # Build request body matching ExecutionRequest model
        # Extract resource, verb, and params from config attributes
        request_body = {
            "resource": config.resource,
            "verb": config.verb,
            "params": config.params,
        }

        try:
            # Make synchronous HTTP request
            # (wrapped in async method for protocol compatibility)
            response = self.client.post(url, json=request_body)

            # Raise exception for 4xx/5xx status codes
            response.raise_for_status()

            # Parse JSON response
            result_data = response.json()

            # Return success result
            return ExecutionResult(success=True, data=result_data, error=None)

        except httpx.HTTPStatusError:
            # HTTP error (4xx, 5xx) - re-raise as infrastructure error
            # Let the caller handle this
            raise

        except httpx.RequestError:
            # Network error (connection failed, timeout, etc.) - re-raise
            raise

    def close(self):
        """Close the HTTP client.

        Call this when you're done using the executor to clean up resources.

        Example:
            executor = HostedExecutor(
                workspace_id="workspace-123",
                connector_id="my-connector"
            )
            try:
                result = await executor.execute(config)
            finally:
                executor.close()
        """
        self.client.close()
