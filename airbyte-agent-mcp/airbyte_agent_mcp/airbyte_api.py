"""Client for the Airbyte ADP API."""

from __future__ import annotations

import os
import time
from typing import Any

import httpx

BASE_URL = "https://api.airbyte.ai/api/v1"
REGISTRY_URL = "https://connectors.airbyte.ai/registry.json"


class AirbyteAuthError(Exception):
    """Raised when Airbyte API authentication fails."""


_registry_cache: list[dict[str, Any]] | None = None


def fetch_registry() -> list[dict[str, Any]]:
    """Fetch the connector registry (cached after first successful call).

    Returns:
        List of connector dicts with keys: connector_id, connector_name,
        docs_url, latest_version, latest_url, versions.
    """
    global _registry_cache
    if _registry_cache is not None:
        return _registry_cache
    resp = httpx.get(REGISTRY_URL, timeout=30.0)
    resp.raise_for_status()
    _registry_cache = resp.json()["connectors"]
    return _registry_cache


class AirbyteApi:
    """Thin HTTP client for the Airbyte ADP API.

    Authenticates via client credentials and caches the token until expiry.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._http = httpx.Client(base_url=BASE_URL, timeout=30.0)
        self._token: str | None = None
        self._token_expires_at: float = 0.0

    def close(self) -> None:
        """Close the underlying HTTP client and release connections."""
        self._http.close()

    def __enter__(self) -> AirbyteApi:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def _ensure_token(self) -> str:
        """Authenticate and return a valid bearer token, refreshing if expired."""
        if self._token and time.monotonic() < self._token_expires_at:
            return self._token

        resp = self._http.post(
            "/account/applications/token",
            json={"client_id": self._client_id, "client_secret": self._client_secret},
        )
        # Temporary 500 since the API doesn't properly return
        if resp.status_code in (401, 403, 500):
            raise AirbyteAuthError(f"Authentication failed ({resp.status_code}).")
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        # Refresh 60s before actual expiry to avoid edge-case failures
        self._token_expires_at = time.monotonic() + data["expires_in"] - 60
        return self._token

    def _auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._ensure_token()}"}

    def list_customers(self) -> list[dict[str, Any]]:
        """List customers.

        Returns:
            List of customer dicts.
        """
        resp = self._http.get("/workspaces", headers=self._auth_headers())
        resp.raise_for_status()
        return resp.json()["data"]

    def get_connector(self, connector_id: str) -> dict[str, Any]:
        """Get a connector source by ID.

        Args:
            connector_id: UUID of the connector source.

        Returns:
            Connector source dict with keys: id, name, source_template,
            replication_config, created_at, updated_at.
        """
        resp = self._http.get(f"/integrations/connectors/{connector_id}", headers=self._auth_headers())
        resp.raise_for_status()
        return resp.json()

    def list_connector_sources(self, customer_id: str) -> list[dict[str, Any]]:
        """List connector sources for a customer.

        Args:
            customer_id: UUID of the customer.

        Returns:
            List of connector source dicts with keys: id, name,
            summarized_source_template, created_at, updated_at.
        """
        resp = self._http.get(
            "/integrations/connectors",
            params={"workspace_id": customer_id},
            headers=self._auth_headers(),
        )
        resp.raise_for_status()
        return resp.json()["data"]


def get_api() -> AirbyteApi:
    """Create an AirbyteApi client from environment variables.

    Raises:
        AirbyteAuthError: If AIRBYTE_CLIENT_ID or AIRBYTE_CLIENT_SECRET are not set.
    """
    client_id = os.environ.get("AIRBYTE_CLIENT_ID")
    client_secret = os.environ.get("AIRBYTE_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise AirbyteAuthError("Airbyte credentials not configured.")

    return AirbyteApi(client_id=client_id, client_secret=client_secret)


def registry_lookup() -> dict[str, dict[str, str]]:
    """Build a lookup from source_definition_id to registry entry."""
    try:
        entries = fetch_registry()
    except Exception:
        return {}
    return {e["connector_definition_id"]: e for e in entries if "connector_definition_id" in e}
