"""AirbyteCloudClient for Airbyte Platform API integration."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import httpx


class AirbyteCloudClient:
    """Client for interacting with Airbyte Platform APIs.

    Handles authentication, token caching, and API calls to:
    - Get bearer tokens for authentication
    - Look up connector instances for users
    - Execute connectors via the cloud API

    Example:
        client = AirbyteCloudClient(
            client_id="your-client-id",
            client_secret="your-client-secret"
        )

        # Get a connector instance
        instance_id = await client.get_connector_instance_id(
            external_user_id="user-123",
            connector_definition_id="stripe-def-456"
        )

        # Execute the connector
        result = await client.execute_connector(
            instance_id=instance_id,
            entity="customers",
            action="list",
            params={"limit": 10}
        )
    """

    AUTH_BASE_URL = "https://cloud.airbyte.com"  # For token endpoint
    API_BASE_URL = "https://api.airbyte.ai"  # For instance lookup & execution

    def __init__(self, client_id: str, client_secret: str):
        """Initialize AirbyteCloudClient.

        Args:
            client_id: Airbyte client ID for authentication
            client_secret: Airbyte client secret for authentication
        """
        self._client_id = client_id
        self._client_secret = client_secret

        # Token cache (instance-level)
        self._cached_token: str | None = None
        self._token_expires_at: datetime | None = None
        self._http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(300.0),  # 5 minute timeout
            follow_redirects=True,
        )

    async def get_bearer_token(self) -> str:
        """Get bearer token for API authentication.

        Caches the token and only requests a new one when the cached token
        is expired or missing. Adds a 60-second buffer before expiration
        to avoid edge cases.

        Returns:
            Bearer token string

        Raises:
            httpx.HTTPStatusError: If the token request fails with 4xx/5xx
            httpx.RequestError: If the network request fails

        Example:
            token = await client.get_bearer_token()
            # Use token in Authorization header: f"Bearer {token}"
        """
        # Check if we have a cached token that hasn't expired
        if self._cached_token and self._token_expires_at:
            # Add 60 second buffer before expiration to avoid edge cases
            now = datetime.now()
            if now < self._token_expires_at:
                # Token is still valid, return cached version
                return self._cached_token

        # Token is missing or expired, fetch a new one
        url = f"{self.AUTH_BASE_URL}/api/v1/applications/token"
        request_body = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }

        response = await self._http_client.post(url, json=request_body)
        response.raise_for_status()

        data = response.json()
        access_token = data["access_token"]
        expires_in = 15 * 60  # default 15 min expiry time * 60 seconds

        # Calculate expiration time with 60 second buffer
        expires_at = datetime.now() + timedelta(seconds=expires_in - 60)
        self._cached_token = access_token
        self._token_expires_at = expires_at

        return access_token

    async def get_connector_instance_id(
        self,
        external_user_id: str,
        connector_definition_id: str,
    ) -> str:
        """Get connector instance ID for a user.

        Looks up the connector instance that belongs to the specified user
        and connector definition. Validates that exactly one instance exists.

        Args:
            external_user_id: User identifier in the Airbyte system
            connector_definition_id: UUID of the connector definition

        Returns:
            Connector instance ID (UUID string)

        Raises:
            ValueError: If 0 or more than 1 instance is found
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            instance_id = await client.get_connector_instance_id(
                external_user_id="user-123",
                connector_definition_id="550e8400-e29b-41d4-a716-446655440000"
            )
        """

        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/connectors/instances_for_user"
        params = {
            "external_user_id": external_user_id,
            "definition_id": connector_definition_id,
        }

        headers = {"Authorization": f"Bearer {token}"}
        response = await self._http_client.get(url, params=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        instances = data["instances"]

        if len(instances) == 0:
            raise ValueError(f"No connector instance found for user '{external_user_id}' " f"and connector '{connector_definition_id}'")

        if len(instances) > 1:
            raise ValueError(
                f"Multiple connector instances found for user '{external_user_id}' "
                f"and connector '{connector_definition_id}'. Expected exactly 1, "
                f"found {len(instances)}"
            )

        instance_id = instances[0]["id"]
        return instance_id

    async def execute_connector(
        self,
        instance_id: str,
        entity: str,
        action: str,
        params: dict[str, Any] | None,
    ) -> dict[str, Any]:
        """Execute a connector operation.

        Args:
            instance_id: Connector instance UUID
            entity: Entity name (e.g., "customers", "invoices")
            action: Operation action (e.g., "list", "get", "create")
            params: Optional parameters for the operation

        Returns:
            Raw JSON response dict from the API

        Raises:
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            result = await client.execute_connector(
                instance_id="inst-123",
                entity="customers",
                action="list",
                params={"limit": 10}
            )
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/connectors/instances/{instance_id}/execute"
        headers = {"Authorization": f"Bearer {token}"}
        request_body = {
            "entity": entity,
            "action": action,
            "params": params,
        }

        response = await self._http_client.post(url, json=request_body, headers=headers)
        response.raise_for_status()

        return response.json()

    async def close(self):
        """Close the HTTP client.

        Call this when you're done using the client to clean up resources.
        """
        await self._http_client.aclose()
