"""AirbyteCloudClient for Airbyte Platform API integration."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import httpx


class AirbyteCloudClient:
    """Client for interacting with Airbyte Platform APIs.

    Handles authentication, token caching, and API calls to:
    - Get bearer tokens for authentication
    - Look up connectors for users
    - Execute connectors via the cloud API

    Example:
        client = AirbyteCloudClient(
            client_id="your-client-id",
            client_secret="your-client-secret"
        )

        # Get a connector ID
        connector_id = await client.get_connector_id(
            external_user_id="user-123",
            connector_definition_id="550e8400-e29b-41d4-a716-446655440000"
        )

        # Execute the connector
        result = await client.execute_connector(
            connector_id=connector_id,
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

    async def get_connector_id(
        self,
        external_user_id: str,
        connector_definition_id: str,
    ) -> str:
        """Get connector ID for a user.

        Looks up the connector that belongs to the specified user
        and connector definition. Validates that exactly one connector exists.

        Args:
            external_user_id: User identifier in the Airbyte system
            connector_definition_id: UUID of the connector definition

        Returns:
            Connector ID (UUID string)

        Raises:
            ValueError: If 0 or more than 1 connector is found
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            connector_id = await client.get_connector_id(
                external_user_id="user-123",
                connector_definition_id="550e8400-e29b-41d4-a716-446655440000"
            )
        """

        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/connectors/connectors_for_user"
        params = {
            "external_user_id": external_user_id,
            "definition_id": connector_definition_id,
        }

        headers = {"Authorization": f"Bearer {token}"}
        response = await self._http_client.get(url, params=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        connectors = data["connectors"]

        if len(connectors) == 0:
            raise ValueError(f"No connector found for user '{external_user_id}' and connector definition '{connector_definition_id}'")

        if len(connectors) > 1:
            raise ValueError(
                f"Multiple connectors found for user '{external_user_id}' "
                f"and connector definition '{connector_definition_id}'. Expected exactly 1, "
                f"found {len(connectors)}"
            )

        connector_id = connectors[0]["id"]
        return connector_id

    async def create_source(
        self,
        name: str,
        connector_definition_id: str,
        external_user_id: str,
        credentials: dict[str, Any],
        replication_config: dict[str, Any] | None = None,
    ) -> str:
        """Create a new source on Airbyte Agent Platform.

        Args:
            name: Source name
            connector_definition_id: UUID of the connector definition
            external_user_id: User identifier
            credentials: Connector auth config dict
            replication_config: Optional replication settings (e.g., start_date for
                connectors with x-airbyte-replication-config). Required for REPLICATION
                mode sources like Intercom.

        Returns:
            The created source ID (UUID string)

        Raises:
            httpx.HTTPStatusError: If creation fails

        Example:
            source_id = await client.create_source(
                name="My Gong Source",
                connector_definition_id="32382e40-3b49-4b99-9c5c-4076501914e7",
                external_user_id="my-workspace",
                credentials={"access_key": "...", "access_key_secret": "..."}
            )

            # For REPLICATION mode sources (e.g., Intercom):
            source_id = await client.create_source(
                name="My Intercom Source",
                connector_definition_id="d8313939-3782-41b0-be29-b3ca20d8dd3a",
                external_user_id="my-workspace",
                credentials={"access_token": "..."},
                replication_config={"start_date": "2024-01-01T00:00:00Z"}
            )
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/v1/integrations/connectors"
        headers = {"Authorization": f"Bearer {token}"}

        request_body: dict[str, Any] = {
            "name": name,
            "definition_id": connector_definition_id,
            "external_user_id": external_user_id,
            "credentials": credentials,
        }

        if replication_config is not None:
            request_body["replication_config"] = replication_config

        response = await self._http_client.post(url, json=request_body, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data["id"]

    async def execute_connector(
        self,
        connector_id: str,
        entity: str,
        action: str,
        params: dict[str, Any] | None,
    ) -> dict[str, Any]:
        """Execute a connector operation.

        Args:
            connector_id: Connector UUID (source ID)
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
                connector_id="550e8400-e29b-41d4-a716-446655440000",
                entity="customers",
                action="list",
                params={"limit": 10}
            )
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/connectors/sources/{connector_id}/execute"
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
