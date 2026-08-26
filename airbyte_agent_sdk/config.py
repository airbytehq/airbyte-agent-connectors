"""Global SDK configuration for Airbyte credentials."""

from __future__ import annotations

import os
import threading
from dataclasses import dataclass
from typing import Literal, cast


@dataclass(frozen=True)
class SDKConfig:
    client_id: str
    client_secret: str
    organization_id: str | None = None
    workspace_name: str = "default"


_lock = threading.Lock()
_config: SDKConfig | None = None


def configure(
    *,
    client_id: str,
    client_secret: str,
    organization_id: str | None = None,
    workspace_name: str = "default",
) -> None:
    """Set global SDK credentials. These are used as defaults by connect() and Workspace.

    Calling configure() again overwrites the previous configuration.
    Explicit kwargs passed to connect()/Workspace() always take priority.
    """
    global _config
    with _lock:
        _config = SDKConfig(
            client_id=client_id,
            client_secret=client_secret,
            organization_id=organization_id,
            workspace_name=workspace_name,
        )


def get_config() -> SDKConfig | None:
    return _config


def _reset_config() -> None:
    """Reset global config. For testing only."""
    global _config
    with _lock:
        _config = None


def resolve_credentials(
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    organization_id: str | None = None,
    workspace_name: str | None = None,
) -> tuple[str, str, str | None, str]:
    """Resolve credentials: explicit arg -> global config -> env var.

    Returns (client_id, client_secret, organization_id, workspace_name).
    Raises ValueError if client_id or client_secret cannot be resolved.
    """
    cfg = _config
    resolved_id = client_id or (cfg.client_id if cfg else None) or os.environ.get("AIRBYTE_CLIENT_ID")
    resolved_secret = client_secret or (cfg.client_secret if cfg else None) or os.environ.get("AIRBYTE_CLIENT_SECRET")
    resolved_org = organization_id or (cfg.organization_id if cfg else None) or os.environ.get("AIRBYTE_ORGANIZATION_ID")
    resolved_ws = workspace_name or (cfg.workspace_name if cfg else None) or "default"
    if not resolved_id or not resolved_secret:
        raise ValueError(
            "client_id and client_secret are required. "
            "Use configure(), pass them as arguments, "
            "or set AIRBYTE_CLIENT_ID/AIRBYTE_CLIENT_SECRET environment variables."
        )
    return resolved_id, resolved_secret, resolved_org, resolved_ws


@dataclass(frozen=True)
class AWSDataPlaneCredentials:
    """AWS credentials for the customer's data plane.

    Consulted only on the local hydration path, which is enabled by
    ``SECRETS_CONFIGURED_FROM_ENVIRONMENT=true``. Any field may be ``None``:
    when explicit keys are absent, boto3 falls back to its default provider
    chain (e.g. an implicit IAM role).
    """

    access_key_id: str | None = None
    secret_access_key: str | None = None
    session_token: str | None = None
    region_name: str | None = None

    @property
    def has_explicit_keys(self) -> bool:
        return bool(self.access_key_id and self.secret_access_key)


def resolve_aws_credentials(
    *,
    access_key_id: str | None = None,
    secret_access_key: str | None = None,
    session_token: str | None = None,
    region_name: str | None = None,
) -> AWSDataPlaneCredentials:
    """Resolve AWS data-plane credentials: explicit arg -> env var.

    Prefer the enterprise-flex secret-manager convention, then fall back to the
    standard AWS SDK environment variables. When no explicit keys are resolved,
    the returned credentials allow boto3 to source an implicit IAM role. Only
    consulted when ``SECRETS_CONFIGURED_FROM_ENVIRONMENT=true``.
    """
    resolved_access_key_id = access_key_id or os.environ.get("AWS_SECRET_MANAGER_ACCESS_KEY_ID") or os.environ.get("AWS_ACCESS_KEY_ID")
    resolved_secret_access_key = (
        secret_access_key or os.environ.get("AWS_SECRET_MANAGER_SECRET_ACCESS_KEY") or os.environ.get("AWS_SECRET_ACCESS_KEY")
    )
    resolved_session_token = session_token or os.environ.get("AWS_SECRET_MANAGER_SESSION_TOKEN") or os.environ.get("AWS_SESSION_TOKEN")
    if bool(resolved_access_key_id) != bool(resolved_secret_access_key):
        raise ValueError(
            "AWS_SECRET_MANAGER_ACCESS_KEY_ID and AWS_SECRET_MANAGER_SECRET_ACCESS_KEY must be configured together "
            "for local executable-bundle secret hydration. If you want to use the AWS default provider chain, omit both."
        )
    if resolved_session_token and not (resolved_access_key_id and resolved_secret_access_key):
        raise ValueError(
            "AWS_SECRET_MANAGER_SESSION_TOKEN requires AWS_SECRET_MANAGER_ACCESS_KEY_ID and "
            "AWS_SECRET_MANAGER_SECRET_ACCESS_KEY for local executable-bundle secret hydration."
        )
    return AWSDataPlaneCredentials(
        access_key_id=resolved_access_key_id,
        secret_access_key=resolved_secret_access_key,
        session_token=resolved_session_token,
        region_name=region_name
        or os.environ.get("AWS_SECRET_MANAGER_REGION")
        or os.environ.get("AWS_REGION")
        or os.environ.get("AWS_DEFAULT_REGION"),
    )


SecretManagerProvider = Literal["aws", "gcp"]


@dataclass(frozen=True)
class GCPDataPlaneCredentials:
    """GCP credentials for the customer's data plane.

    Consulted only on the local hydration path, which is enabled by
    ``SECRETS_CONFIGURED_FROM_ENVIRONMENT=true``. If explicit credentials are
    absent, the Google client library falls back to Application Default
    Credentials.
    """

    project_id: str | None = None
    credentials_json: str | None = None
    credentials_path: str | None = None
    secret_version: str = "latest"


def resolve_secret_manager_provider(provider: str | None = None) -> SecretManagerProvider:
    """Resolve which customer-owned secret manager should hydrate bundles."""
    resolved_provider = (provider or os.environ.get("SECRET_MANAGER_PROVIDER") or "").strip().lower()
    if resolved_provider:
        if resolved_provider not in {"aws", "gcp"}:
            raise ValueError("SECRET_MANAGER_PROVIDER must be either 'aws' or 'gcp' for local executable-bundle secret hydration.")
        return cast(SecretManagerProvider, resolved_provider)

    has_gcp_config = any(
        os.environ.get(name)
        for name in (
            "GCP_SECRET_MANAGER_PROJECT_ID",
            "GCP_SECRET_MANAGER_CREDENTIALS_JSON",
            "GCP_SECRET_MANAGER_CREDENTIALS_PATH",
        )
    )
    if has_gcp_config:
        return "gcp"
    return "aws"


def resolve_gcp_credentials(
    *,
    project_id: str | None = None,
    credentials_json: str | None = None,
    credentials_path: str | None = None,
    secret_version: str | None = None,
) -> GCPDataPlaneCredentials:
    """Resolve GCP Secret Manager credentials: explicit arg -> env var."""
    resolved_credentials_json = credentials_json or os.environ.get("GCP_SECRET_MANAGER_CREDENTIALS_JSON")
    resolved_credentials_path = (
        credentials_path or os.environ.get("GCP_SECRET_MANAGER_CREDENTIALS_PATH") or os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    )
    if resolved_credentials_json and resolved_credentials_path:
        raise ValueError(
            "GCP_SECRET_MANAGER_CREDENTIALS_JSON and GCP_SECRET_MANAGER_CREDENTIALS_PATH/GOOGLE_APPLICATION_CREDENTIALS "
            "cannot both be configured for local executable-bundle secret hydration."
        )
    return GCPDataPlaneCredentials(
        project_id=project_id
        or os.environ.get("GCP_SECRET_MANAGER_PROJECT_ID")
        or os.environ.get("GOOGLE_CLOUD_PROJECT")
        or os.environ.get("GCLOUD_PROJECT"),
        credentials_json=resolved_credentials_json,
        credentials_path=resolved_credentials_path,
        secret_version=secret_version or os.environ.get("GCP_SECRET_MANAGER_SECRET_VERSION") or "latest",
    )
