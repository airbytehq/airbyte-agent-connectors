"""Global SDK configuration for Airbyte credentials."""

from __future__ import annotations

import os
import threading
from dataclasses import dataclass


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
