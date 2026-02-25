"""AirbyteCloudClient for Airbyte Platform API integration."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import httpx


def _raise_with_body(response: httpx.Response) -> None:
    """Raise HTTPStatusError with response body included in the message.

    Unlike httpx's raise_for_status(), this includes the response body in the
    error message so that API validation errors are visible to the caller.
    """
    if response.is_success:
        return

    # Try to get the response body for a more informative error
    try:
        body = response.text
    except Exception:
        body = "<unable to read response body>"

    message = f"HTTP {response.status_code} error for {response.request.method} {response.url}: {body}"
    raise httpx.HTTPStatusError(message=message, request=response.request, response=response)


class AirbyteCloudClient:
    """Client for interacting with Airbyte Platform APIs.

    Handles authentication, token caching, and API calls to:
    - Get bearer tokens for authentication
    - Look up connectors for users
    - Execute connectors via the cloud API

    Example:
        client = AirbyteCloudClient(
            client_id="your-client-id",
            client_secret="your-client-secret",
            organization_id="00000000-0000-0000-0000-000000000123",
        )

        # Get a connector ID
        connector_id = await client.get_connector_id(
            customer_name="user-123",
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

    API_BASE_URL = "https://api.airbyte.ai"  # For all API calls including token endpoint
    AUTHORIZATION_HEADER = "Authorization"
    ORGANIZATION_ID_HEADER = "X-Organization-Id"

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        organization_id: str | None = None,
    ):
        """Initialize AirbyteCloudClient.

        Args:
            client_id: Airbyte client ID for authentication
            client_secret: Airbyte client secret for authentication
            organization_id: Optional Airbyte organization ID for multi-org request routing
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._organization_id = organization_id

        # Token cache (instance-level)
        self._cached_token: str | None = None
        self._token_expires_at: datetime | None = None
        self._http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(300.0),  # 5 minute timeout
            follow_redirects=True,
        )

    def _build_headers(self, token: str | None = None) -> dict[str, str]:
        """Build request headers for Airbyte API calls."""
        headers: dict[str, str] = {}
        if token is not None:
            headers[self.AUTHORIZATION_HEADER] = f"Bearer {token}"
        if self._organization_id:
            headers[self.ORGANIZATION_ID_HEADER] = self._organization_id
        return headers

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
        url = f"{self.API_BASE_URL}/api/v1/account/applications/token"
        request_body = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }

        request_kwargs: dict[str, Any] = {"json": request_body}
        headers = self._build_headers()
        if headers:
            request_kwargs["headers"] = headers

        response = await self._http_client.post(url, **request_kwargs)
        _raise_with_body(response)

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
        customer_name: str,
        connector_definition_id: str,
    ) -> str:
        """Get connector ID for a customer.

        Looks up the connector that belongs to the specified customer
        and connector definition. Validates that exactly one connector exists.

        Args:
            customer_name: Customer name in the Airbyte system
            connector_definition_id: UUID of the connector definition

        Returns:
            Connector ID (UUID string)

        Raises:
            ValueError: If 0 or more than 1 connector is found
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            connector_id = await client.get_connector_id(
                customer_name="user-123",
                connector_definition_id="550e8400-e29b-41d4-a716-446655440000"
            )
        """

        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors"
        params = {
            "customer_name": customer_name,
            "definition_id": connector_definition_id,
        }

        headers = self._build_headers(token=token)
        response = await self._http_client.get(url, params=params, headers=headers)
        _raise_with_body(response)

        data = response.json()
        connectors = data["data"]

        if len(connectors) == 0:
            raise ValueError(f"No connector found for customer_name '{customer_name}' and connector definition '{connector_definition_id}'")

        if len(connectors) > 1:
            raise ValueError(
                f"Multiple connectors found for customer_name '{customer_name}' "
                f"and connector definition '{connector_definition_id}'. Expected exactly 1, "
                f"found {len(connectors)}"
            )

        connector_id = connectors[0]["id"]
        return connector_id

    async def initiate_oauth(
        self,
        definition_id: str,
        customer_name: str,
        redirect_url: str,
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """Initiate a server-side OAuth flow with auto-source creation.

        Starts the OAuth flow for a connector. Returns a consent URL where the
        end user should be redirected to grant access. After completing consent,
        the source is automatically created and the user is redirected to your
        redirect_url with a `connector_id` query parameter.

        Args:
            definition_id: Connector definition UUID
            customer_name: Customer name identifier
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + customer_name.
            replication_config: Optional replication settings (e.g., start_date).
                Merged with OAuth credentials during source creation.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Raises:
            httpx.HTTPStatusError: If the request fails

        Example:
            consent_url = await client.initiate_oauth(
                definition_id="d8313939-3782-41b0-be29-b3ca20d8dd3a",
                customer_name="my-workspace",
                redirect_url="https://myapp.com/oauth/callback",
                name="My HubSpot Source",
                replication_config={"start_date": "2024-01-01"},
            )
            # Redirect user to: consent_url
            # After consent: https://myapp.com/oauth/callback?connector_id=...
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors/oauth/initiate"
        headers = self._build_headers(token=token)
        request_body: dict[str, Any] = {
            "customer_name": customer_name,
            "definition_id": definition_id,
            "redirect_url": redirect_url,
        }

        if name is not None:
            request_body["name"] = name
        if replication_config is not None:
            request_body["replication_config"] = replication_config
        if source_template_id is not None:
            request_body["source_template_id"] = source_template_id

        response = await self._http_client.post(url, json=request_body, headers=headers)
        _raise_with_body(response)
        return response.json()["consent_url"]

    async def create_source(
        self,
        name: str,
        connector_definition_id: str,
        customer_name: str,
        credentials: dict[str, Any] | None = None,
        replication_config: dict[str, Any] | None = None,
        server_side_oauth_secret_id: str | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """Create a new source on Airbyte Cloud.

        Supports two authentication modes:
        1. Direct credentials: Provide `credentials` dict
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            name: Source name
            connector_definition_id: UUID of the connector definition
            customer_name: Customer name identifier
            credentials: Connector auth config dict. Required unless using OAuth.
            replication_config: Optional replication settings (e.g., start_date for
                connectors with x-airbyte-replication-config). Required for REPLICATION
                mode sources like Intercom.
            server_side_oauth_secret_id: OAuth secret ID from initiate_oauth redirect.
                When provided, credentials are not required.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The created source ID (UUID string)

        Raises:
            httpx.HTTPStatusError: If creation fails

        Example:
            # With direct credentials:
            source_id = await client.create_source(
                name="My Intercom Source",
                connector_definition_id="d8313939-3782-41b0-be29-b3ca20d8dd3a",
                customer_name="my-workspace",
                credentials={"access_token": "..."},
                replication_config={"start_date": "2024-01-01T00:00:00Z"}
            )

            # With server-side OAuth:
            source_id = await client.create_source(
                name="My Intercom Source",
                connector_definition_id="d8313939-3782-41b0-be29-b3ca20d8dd3a",
                customer_name="my-workspace",
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config={"start_date": "2024-01-01T00:00:00Z"}
            )
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/v1/integrations/connectors"
        headers = self._build_headers(token=token)

        request_body: dict[str, Any] = {
            "name": name,
            "definition_id": connector_definition_id,
            "customer_name": customer_name,
        }

        if credentials is not None:
            request_body["credentials"] = credentials
        if replication_config is not None:
            request_body["replication_config"] = replication_config
        if server_side_oauth_secret_id is not None:
            request_body["server_side_oauth_secret_id"] = server_side_oauth_secret_id
        if source_template_id is not None:
            request_body["source_template_id"] = source_template_id

        response = await self._http_client.post(url, json=request_body, headers=headers)
        _raise_with_body(response)

        data = response.json()
        return data["id"]

    async def configure_oauth_app_parameters(
        self,
        connector_type: str,
        credentials: dict[str, Any] | None,
    ) -> None:
        """Configure or remove OAuth app credentials for the authenticated organization.

        When credentials are provided, sends flat key/value pairs
        (e.g., {"client_id": "...", "client_secret": "..."}) to the Sonar API,
        which handles expansion to the nested format required by the downstream
        Airbyte platform.

        When credentials are None, removes any existing override so the
        organization reverts to the default Airbyte-managed OAuth app.

        Args:
            connector_type: Connector type identifier (e.g., "hubspot")
            credentials: Flat OAuth app credentials dict, or None to remove the override

        Raises:
            httpx.HTTPStatusError: If the request fails

        Example:
            await client.configure_oauth_app_parameters(
                connector_type="hubspot",
                credentials={"client_id": "my-id", "client_secret": "my-secret"},
            )

            await client.configure_oauth_app_parameters(
                connector_type="hubspot",
                credentials=None,
            )
        """
        token = await self.get_bearer_token()
        headers = {"Authorization": f"Bearer {token}"}

        if credentials is None:
            url = f"{self.API_BASE_URL}/api/v1/oauth/credentials/connector_type/{connector_type}"
            response = await self._http_client.delete(url, headers=headers)
        else:
            url = f"{self.API_BASE_URL}/api/v1/oauth/credentials"
            request_body: dict[str, Any] = {
                "connector_type": connector_type,
                "configuration": credentials,
            }
            response = await self._http_client.put(url, json=request_body, headers=headers)

        _raise_with_body(response)

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
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors/{connector_id}/execute"
        headers = self._build_headers(token=token)
        request_body = {
            "entity": entity,
            "action": action,
            "params": params,
        }

        response = await self._http_client.post(url, json=request_body, headers=headers)
        _raise_with_body(response)

        return response.json()

    async def close(self):
        """Close the HTTP client.

        Call this when you're done using the client to clean up resources.
        """
        await self._http_client.aclose()
