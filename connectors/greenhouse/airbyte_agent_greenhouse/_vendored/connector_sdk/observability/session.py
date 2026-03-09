"""Shared session context for both logging and telemetry."""

import logging
import uuid
from datetime import UTC, datetime
from typing import Any, Dict

from .config import SDKConfig, load_config

logger = logging.getLogger(__name__)

# Cache the config at module level to avoid repeated reads
_cached_config: SDKConfig | None = None


def _get_config() -> SDKConfig:
    """Get cached SDK config or load from file."""
    global _cached_config
    if _cached_config is None:
        _cached_config = load_config()
    return _cached_config


def _clear_config_cache() -> None:
    """Clear the cached config. Used for testing."""
    global _cached_config
    _cached_config = None


def get_persistent_user_id() -> str:
    """
    Get the persistent anonymous user ID.

    Now reads from ~/.airbyte/connector-sdk/config.yaml

    Returns:
        An anonymous UUID string that uniquely identifies this user across sessions.
    """
    return _get_config().user_id


def get_public_ip() -> str | None:
    """
    Fetch the public IP address of the user.

    Returns None if unable to fetch (network issues, etc).
    Uses httpx for a robust HTTP request to a public IP service.
    """
    try:
        # NOTE: Import here intentionally - this is a non-critical network call
        # that may fail. Importing at module level would make httpx a hard dependency.
        import httpx

        # Use a short timeout to avoid blocking
        with httpx.Client(timeout=2.0) as client:
            response = client.get("https://api.ipify.org?format=text")
            response.raise_for_status()
            return response.text.strip()
    except Exception:
        # Never fail - just return None
        return None


def get_is_internal_user() -> bool:
    """
    Check if the current user is an internal Airbyte user.

    Now reads from ~/.airbyte/connector-sdk/config.yaml
    Environment variable AIRBYTE_INTERNAL_USER can override.

    Returns False if not set or on any error.
    """
    return _get_config().is_internal_user


class ObservabilitySession:
    """Shared session context for both logging and telemetry."""

    def __init__(
        self,
        connector_name: str,
        connector_version: str | None = None,
        execution_context: str = "direct",
        session_id: str | None = None,
    ):
        self.session_id = session_id or str(uuid.uuid4())
        self.user_id = get_persistent_user_id()
        self.connector_name = connector_name
        self.connector_version = connector_version
        self.execution_context = execution_context
        self.started_at = datetime.now(UTC)
        self.operation_count = 0
        self.metadata: Dict[str, Any] = {}
        self.public_ip = get_public_ip()
        self.is_internal_user = get_is_internal_user()

    def increment_operations(self):
        """Increment the operation counter."""
        self.operation_count += 1

    def duration_seconds(self) -> float:
        """Calculate session duration in seconds."""
        return (datetime.now(UTC) - self.started_at).total_seconds()
