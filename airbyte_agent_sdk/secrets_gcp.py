"""GCP Secret Manager hydration for executable bundles (opt-in `secrets-gcp` extra).

This module is only reached on the opt-in local execution path -- when
`SECRETS_CONFIGURED_FROM_ENVIRONMENT=true`, the SDK calls
`POST /connectors/{id}/execute/prepare` and resolves the returned bundle's
unhydrated `secret_coordinate::` values against the customer's own GCP Secret
Manager in their data plane. `google-cloud-secret-manager` is imported lazily
inside `hydrate_source_config` so the base install (without the
`secrets-gcp` extra) never imports it on the hosted path.

Provider selection lives in
`airbyte_agent_sdk.config.resolve_secret_manager_provider`: set
`SECRET_MANAGER_PROVIDER=gcp` to select this module explicitly. Absent that
variable, GCP is inferred when any of `GCP_SECRET_MANAGER_PROJECT_ID`,
`GCP_SECRET_MANAGER_CREDENTIALS_JSON`, or
`GCP_SECRET_MANAGER_CREDENTIALS_PATH` is set; otherwise AWS remains the
default.

Coordinate forms accepted after the `secret_coordinate::` prefix:

- A full resource name, `projects/<project>/secrets/<id>`, optionally already
  carrying `/versions/<version>`. Used as given; the configured version is
  appended when absent.
- A bare secret id such as `organization_<org_id>__source_config__<uuid>`,
  expanded to `projects/<project>/secrets/<id>/versions/<version>` using the
  resolved project. Legacy coordinates containing `/` are rewritten to `__`,
  since GCP Secret Manager secret ids cannot contain a slash.

Credentials come from `airbyte_agent_sdk.config.resolve_gcp_credentials`, which
reads those same `GCP_SECRET_MANAGER_*` variables and falls back to Application
Default Credentials; when no project is configured explicitly, the project
discovered alongside the credentials is used. Each distinct coordinate is
fetched once per hydration call, and hydration fails closed -- a credential or
fetch failure raises rather than falling back to hosted execution.

Stored values must be plaintext UTF-8 scalars; a JSON object or array payload is
rejected rather than injected into the connector config, matching
`airbyte_agent_sdk.secrets_aws`.
"""

from __future__ import annotations

import json
from dataclasses import replace
from typing import Any

from airbyte_agent_sdk.config import GCPDataPlaneCredentials, resolve_gcp_credentials

_SECRET_COORDINATE_PREFIX = "secret_coordinate::"

_INSTALL_HINT = "Install it with: pip install airbyte-agent-sdk[secrets-gcp]"
_GCP_HINT = (
    "Verify your GCP secret store configuration "
    "(SECRET_MANAGER_PROVIDER=gcp, GCP_SECRET_MANAGER_PROJECT_ID or GOOGLE_CLOUD_PROJECT for short coordinates, "
    "optional GCP_SECRET_MANAGER_CREDENTIALS_JSON or GOOGLE_APPLICATION_CREDENTIALS, and optional "
    "GCP_SECRET_MANAGER_SECRET_VERSION). AWS and GCP secret hydration are currently implemented. "
    "Execution was NOT sent to Airbyte Cloud."
)


def _is_secret_coordinate(value: Any) -> bool:
    return isinstance(value, str) and value.startswith(_SECRET_COORDINATE_PREFIX)


def _coordinate_secret_name(value: str, credentials: GCPDataPlaneCredentials) -> str:
    """Turn a `secret_coordinate::` value into a GCP Secret Manager resource name."""
    secret_id = value.split("::", 1)[1]
    if secret_id.startswith("projects/"):
        if "/versions/" in secret_id:
            return secret_id
        return f"{secret_id}/versions/{credentials.secret_version}"
    if "/" in secret_id:
        secret_id = secret_id.replace("/", "__")
    if not credentials.project_id:
        raise ValueError(f"Secret coordinate '{secret_id}' is not a full GCP Secret Manager resource name and no project was configured. {_GCP_HINT}")
    return f"projects/{credentials.project_id}/secrets/{secret_id}/versions/{credentials.secret_version}"


def hydrate_source_config(
    source_config: dict[str, Any],
    *,
    credentials: GCPDataPlaneCredentials | None = None,
) -> dict[str, Any]:
    """Resolve `secret_coordinate::` values in *source_config* via GCP Secret Manager.

    Walks nested dicts/lists and returns a fully hydrated copy of the config.

    Raises:
        ImportError: If google-cloud-secret-manager is not installed (missing
            `secrets-gcp` extra).
        ValueError: If credentials are misconfigured, no project can be resolved
            for a bare coordinate, or a coordinate does not resolve to a
            plaintext UTF-8 value.
    """
    credentials = credentials or resolve_gcp_credentials()
    client, adc_project_id = _build_secret_manager_client(credentials)
    if not credentials.project_id and adc_project_id:
        credentials = replace(credentials, project_id=adc_project_id)
    resolved_cache: dict[str, str] = {}

    def _resolve(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: _resolve(inner) for key, inner in value.items()}
        if isinstance(value, list):
            return [_resolve(item) for item in value]
        if _is_secret_coordinate(value):
            secret_name = _coordinate_secret_name(value, credentials)
            if secret_name not in resolved_cache:
                resolved_cache[secret_name] = _fetch_secret(client, secret_name)
            return resolved_cache[secret_name]
        return value

    return _resolve(source_config)


def _build_secret_manager_client(credentials: GCPDataPlaneCredentials) -> tuple[Any, str | None]:
    # google-cloud-secret-manager is an opt-in dependency needed only on the
    # local hydration path, so it is imported lazily here.
    try:
        from google.auth import default, load_credentials_from_dict, load_credentials_from_file
        from google.cloud import secretmanager
    except ImportError as exc:
        raise ImportError(f"google-cloud-secret-manager is required to hydrate executable bundles from GCP Secret Manager. {_INSTALL_HINT}") from exc

    if credentials.credentials_json:
        try:
            credentials_info = json.loads(credentials.credentials_json)
        except json.JSONDecodeError as exc:
            raise ValueError("GCP_SECRET_MANAGER_CREDENTIALS_JSON must contain valid Google credentials JSON.") from exc
        google_credentials, project_id = load_credentials_from_dict(credentials_info)
        return secretmanager.SecretManagerServiceClient(credentials=google_credentials), project_id
    if credentials.credentials_path:
        google_credentials, project_id = load_credentials_from_file(credentials.credentials_path)
        return secretmanager.SecretManagerServiceClient(credentials=google_credentials), project_id
    google_credentials, project_id = default()
    return secretmanager.SecretManagerServiceClient(credentials=google_credentials), project_id


def _fetch_secret(client: Any, secret_name: str) -> str:
    # google-api-core is part of the opt-in GCP extra and is only needed while
    # executing the GCP hydration path.
    from google.api_core.exceptions import GoogleAPICallError, RetryError

    try:
        response = client.access_secret_version(request={"name": secret_name})
    except (GoogleAPICallError, RetryError) as exc:
        raise ValueError(f"Failed to resolve secret coordinate '{secret_name}' from GCP Secret Manager. {_GCP_HINT} Details: {exc}") from exc

    payload = getattr(response, "payload", None)
    data = getattr(payload, "data", None)
    if data is None:
        raise ValueError(f"Secret coordinate '{secret_name}' resolved to an empty GCP Secret Manager payload. Store a plaintext UTF-8 value.")
    try:
        secret_string = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(
            f"Secret coordinate '{secret_name}' resolved to a non-UTF-8 GCP Secret Manager value. Store a plaintext UTF-8 value."
        ) from exc

    try:
        parsed = json.loads(secret_string)
    except json.JSONDecodeError:
        return secret_string

    if isinstance(parsed, dict | list):
        raise ValueError(
            f"Secret coordinate '{secret_name}' resolved to a JSON GCP Secret Manager value. "
            "Store the connector credential as a plaintext value, not a JSON object."
        )
    return secret_string
