"""AirbyteCloudClient for Airbyte Platform API integration."""

from __future__ import annotations

import os
from datetime import datetime, timedelta
from typing import Any

import httpx

from airbyte_agent_sdk.http.exceptions import (
    AuthenticationError,
    ConnectorValidationError,
    HTTPStatusError,
    RateLimitError,
)


def _raise_with_body(response: httpx.Response) -> None:
    """Raise the appropriate SDK exception for an httpx error response.

    Unlike httpx's raise_for_status(), this includes the response body in the
    error message so that API validation errors are visible to the caller, and
    maps status codes to the SDK exception hierarchy so framework adapters can
    translate them into retryable tool errors.

    Status code mapping:
    - 401/403 -> AuthenticationError
    - 429     -> RateLimitError (parses Retry-After header when present)
    - 400/422 -> ConnectorValidationError
    - other ≥400 -> HTTPStatusError
    """
    if response.is_success:
        return

    # Try to get the response body for a more informative error. Prefer
    # structured JSON error details when available (mirrors the httpx adapter).
    body_text: str
    try:
        body_text = response.text
    except Exception:
        body_text = "<unable to read response body>"

    detail_message: str | None = None
    try:
        error_data = response.json()
        if isinstance(error_data, dict):
            errors_list = error_data.get("errors")
            if isinstance(errors_list, list) and errors_list:

                def _extract_error(e: object) -> str:
                    if isinstance(e, dict):
                        return str(e.get("userPresentableMessage") or e.get("message") or e.get("error") or e)
                    return str(e)

                detail_message = ", ".join(_extract_error(e) for e in errors_list)
            else:
                detail_message = error_data.get("message") or error_data.get("error")
    except Exception:
        detail_message = None

    detail = detail_message if detail_message else body_text
    message = f"HTTP {response.status_code} error for {response.request.method} {response.url}: {detail}"

    status_code = response.status_code

    if status_code in (401, 403):
        raise AuthenticationError(message=message, status_code=status_code)

    if status_code == 429:
        retry_after: int | None = None
        retry_after_header = response.headers.get("retry-after")
        if retry_after_header is not None:
            try:
                retry_after = int(retry_after_header)
            except ValueError:
                retry_after = None
        raise RateLimitError(message=message, retry_after=retry_after)

    if status_code in (400, 422):
        raise ConnectorValidationError(message=message, status_code=status_code)

    raise HTTPStatusError(status_code=status_code, message=message)


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

        # Get a connector ID (workspace_name maps to customer_name on the wire)
        connector_id = await client.get_connector_id(
            workspace_name="my-workspace",
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

    DEFAULT_API_BASE_URL = "https://api.airbyte.ai"
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

        # Allow developers to redirect all SDK traffic to a local backend via
        # SDK_DEV_ADP_API_HOST (e.g. "http://localhost:8000").  This is NOT
        # intended for end-user SDKs — only for local development and testing.
        self.API_BASE_URL = os.environ.get("SDK_DEV_ADP_API_HOST", "").rstrip("/") or self.DEFAULT_API_BASE_URL

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
        workspace_name: str,
        connector_definition_id: str,
    ) -> str:
        """Get connector ID for a workspace.

        Looks up the connector that belongs to the specified workspace
        and connector definition. Validates that exactly one connector exists.

        Args:
            workspace_name: Workspace name in the Airbyte system
            connector_definition_id: UUID of the connector definition

        Returns:
            Connector ID (UUID string)

        Raises:
            ValueError: If 0 or more than 1 connector is found
            httpx.HTTPStatusError: If API returns 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            connector_id = await client.get_connector_id(
                workspace_name="user-123",
                connector_definition_id="550e8400-e29b-41d4-a716-446655440000"
            )
        """

        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors"
        params = {
            "workspace_name": workspace_name,
            "definition_id": connector_definition_id,
        }

        headers = self._build_headers(token=token)
        response = await self._http_client.get(url, params=params, headers=headers)
        _raise_with_body(response)

        data = response.json()
        connectors = data["data"]

        if len(connectors) == 0:
            raise ValueError(f"No connector found for workspace_name '{workspace_name}' and connector definition '{connector_definition_id}'")

        if len(connectors) > 1:
            raise ValueError(
                f"Multiple connectors found for workspace_name '{workspace_name}' "
                f"and connector definition '{connector_definition_id}'. Expected exactly 1, "
                f"found {len(connectors)}"
            )

        connector_id = connectors[0]["id"]
        return connector_id

    async def initiate_oauth(
        self,
        definition_id: str,
        workspace_name: str,
        redirect_url: str,
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
        environment: dict[str, Any] | None = None,
    ) -> str:
        """Initiate a server-side OAuth flow with auto-source creation.

        Starts the OAuth flow for a connector. Returns a consent URL where the
        end user should be redirected to grant access. After completing consent,
        the source is automatically created and the user is redirected to your
        redirect_url with a `connector_id` query parameter.

        Args:
            definition_id: Connector definition UUID
            workspace_name: Workspace name identifier
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + workspace_name.
            replication_config: Optional replication settings (e.g., start_date).
                Merged with OAuth credentials during source creation.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.
            environment: Optional environment configuration (e.g., subdomain).
                Required for connectors whose OAuth URLs contain environment
                variables (e.g., Zendesk uses subdomain in OAuth URLs).

        Returns:
            The OAuth consent URL

        Raises:
            httpx.HTTPStatusError: If the request fails

        Example:
            consent_url = await client.initiate_oauth(
                definition_id="d8313939-3782-41b0-be29-b3ca20d8dd3a",
                workspace_name="my-workspace",
                redirect_url="https://myapp.com/oauth/callback",
                name="My HubSpot Source",
                replication_config={"start_date": "2024-01-01"},
                environment={"subdomain": "my-company"},
            )
            # Redirect user to: consent_url
            # After consent: https://myapp.com/oauth/callback?connector_id=...
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors/oauth/initiate"
        headers = self._build_headers(token=token)
        request_body: dict[str, Any] = {
            "workspace_name": workspace_name,
            "definition_id": definition_id,
            "redirect_url": redirect_url,
        }

        if name is not None:
            request_body["name"] = name
        if replication_config is not None:
            request_body["replication_config"] = replication_config
        if source_template_id is not None:
            request_body["source_template_id"] = source_template_id
        if environment is not None:
            request_body["environment"] = environment

        response = await self._http_client.post(url, json=request_body, headers=headers)
        _raise_with_body(response)
        return response.json()["consent_url"]

    async def create_source(
        self,
        name: str,
        connector_definition_id: str,
        workspace_name: str,
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
            workspace_name: Workspace name identifier
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
                workspace_name="my-workspace",
                credentials={"access_token": "..."},
                replication_config={"start_date": "2024-01-01T00:00:00Z"}
            )

            # With server-side OAuth:
            source_id = await client.create_source(
                name="My Intercom Source",
                connector_definition_id="d8313939-3782-41b0-be29-b3ca20d8dd3a",
                workspace_name="my-workspace",
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config={"start_date": "2024-01-01T00:00:00Z"}
            )
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors"
        headers = self._build_headers(token=token)

        request_body: dict[str, Any] = {
            "name": name,
            "definition_id": connector_definition_id,
            "workspace_name": workspace_name,
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
            AuthenticationError: If API returns 401/403
            RateLimitError: If API returns 429
            ConnectorValidationError: If API returns 400/422
            HTTPStatusError: If API returns any other 4xx/5xx status code

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
            AuthenticationError: If API returns 401/403
            RateLimitError: If API returns 429
            ConnectorValidationError: If API returns 400/422 (retryable by LLM)
            HTTPStatusError: If API returns any other 4xx/5xx status code
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

    async def list_workspace_connectors(self, customer_name: str) -> list[dict[str, Any]]:
        """List connector instances for a workspace.

        Raises:
            AuthenticationError: If API returns 401/403
            RateLimitError: If API returns 429
            ConnectorValidationError: If API returns 400/422
            HTTPStatusError: If API returns any other 4xx/5xx status code
            httpx.RequestError: If network request fails
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors"
        headers = self._build_headers(token=token)
        response = await self._http_client.get(
            url,
            params={"customer_name": customer_name},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()["data"]

    async def delete_connector(self, connector_id: str) -> None:
        """Delete a connector (async, returns 202)."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/integrations/connectors/{connector_id}"
        headers = self._build_headers(token=token)
        response = await self._http_client.delete(url, headers=headers)
        _raise_with_body(response)

    # ---- Workspace resolution ------------------------------------------------

    async def resolve_workspace_id(self, workspace_name: str) -> str:
        """Resolve a workspace name to its UUID.

        Calls the workspaces list API with a name filter and selects the exact
        match.  Raises ValueError when zero or multiple workspaces match.
        """
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/workspaces"
        headers = self._build_headers(token=token)
        response = await self._http_client.get(
            url,
            params={"name_contains": workspace_name},
            headers=headers,
        )
        _raise_with_body(response)
        workspaces = [w for w in response.json()["data"] if w["name"] == workspace_name]
        if len(workspaces) == 0:
            raise ValueError(f"No workspace found with name '{workspace_name}'")
        if len(workspaces) > 1:
            raise ValueError(f"Multiple workspaces found with name '{workspace_name}'")
        return str(workspaces[0]["id"])

    # ---- Workflow CRUD -------------------------------------------------------

    async def list_workflows(self, workspace_id: str) -> list[dict[str, Any]]:
        """List workflows for a workspace."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows"
        headers = self._build_headers(token=token)
        response = await self._http_client.get(
            url,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()["data"]

    async def create_workflow(
        self,
        workspace_id: str,
        name: str,
        tasks: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Create a workflow.  workspace_id goes in the body only."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows"
        headers = self._build_headers(token=token)
        request_body: dict[str, Any] = {"workspace_id": workspace_id, "name": name}
        if tasks is not None:
            request_body["tasks"] = tasks
        response = await self._http_client.post(url, json=request_body, headers=headers)
        _raise_with_body(response)
        return response.json()

    async def get_workflow(self, workflow_id: str, workspace_id: str) -> dict[str, Any]:
        """Get a single workflow."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}"
        headers = self._build_headers(token=token)
        response = await self._http_client.get(
            url,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()

    async def update_workflow(
        self,
        workflow_id: str,
        workspace_id: str,
        *,
        name: str | None = None,
    ) -> dict[str, Any]:
        """Update a workflow (PATCH)."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}"
        headers = self._build_headers(token=token)
        request_body: dict[str, Any] = {}
        if name is not None:
            request_body["name"] = name
        response = await self._http_client.patch(
            url,
            json=request_body,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()

    async def delete_workflow(self, workflow_id: str, workspace_id: str) -> None:
        """Delete a workflow."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}"
        headers = self._build_headers(token=token)
        response = await self._http_client.delete(
            url,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)

    # ---- Automation CRUD -----------------------------------------------------

    async def create_automation(
        self,
        workflow_id: str,
        workspace_id: str,
        *,
        trigger_type: str = "schedule",
        enabled: bool = True,
        cron_expression: str | None = None,
        timezone: str | None = None,
        completion_webhook_url: str | None = None,
    ) -> dict[str, Any]:
        """Create an automation on a workflow."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}/automations"
        headers = self._build_headers(token=token)
        request_body: dict[str, Any] = {
            "workspace_id": workspace_id,
            "trigger_type": trigger_type,
            "enabled": enabled,
        }
        if cron_expression is not None:
            request_body["cron_expression"] = cron_expression
        if timezone is not None:
            request_body["timezone"] = timezone
        if completion_webhook_url is not None:
            request_body["completion_webhook_url"] = completion_webhook_url
        response = await self._http_client.post(
            url,
            json=request_body,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()

    async def list_automations(
        self,
        workflow_id: str,
        workspace_id: str,
    ) -> list[dict[str, Any]]:
        """List automations for a workflow."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}/automations"
        headers = self._build_headers(token=token)
        response = await self._http_client.get(
            url,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()["data"]

    async def get_automation(
        self,
        workflow_id: str,
        automation_id: str,
        workspace_id: str,
    ) -> dict[str, Any]:
        """Get a single automation."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}/automations/{automation_id}"
        headers = self._build_headers(token=token)
        response = await self._http_client.get(
            url,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()

    async def update_automation(
        self,
        workflow_id: str,
        automation_id: str,
        workspace_id: str,
        *,
        enabled: bool | None = None,
        trigger_type: str | None = None,
        cron_expression: str | None = None,
        timezone: str | None = None,
        completion_webhook_url: str | None = None,
    ) -> dict[str, Any]:
        """Update an automation (PATCH)."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}/automations/{automation_id}"
        headers = self._build_headers(token=token)
        request_body: dict[str, Any] = {}
        if enabled is not None:
            request_body["enabled"] = enabled
        if trigger_type is not None:
            request_body["trigger_type"] = trigger_type
        if cron_expression is not None:
            request_body["cron_expression"] = cron_expression
        if timezone is not None:
            request_body["timezone"] = timezone
        if completion_webhook_url is not None:
            request_body["completion_webhook_url"] = completion_webhook_url
        response = await self._http_client.patch(
            url,
            json=request_body,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)
        return response.json()

    async def delete_automation(
        self,
        workflow_id: str,
        automation_id: str,
        workspace_id: str,
    ) -> None:
        """Delete an automation."""
        token = await self.get_bearer_token()
        url = f"{self.API_BASE_URL}/api/v1/internal/workflows/{workflow_id}/automations/{automation_id}"
        headers = self._build_headers(token=token)
        response = await self._http_client.delete(
            url,
            params={"workspace_id": workspace_id},
            headers=headers,
        )
        _raise_with_body(response)

    async def close(self):
        """Close the HTTP client.

        Call this when you're done using the client to clean up resources.
        """
        await self._http_client.aclose()
