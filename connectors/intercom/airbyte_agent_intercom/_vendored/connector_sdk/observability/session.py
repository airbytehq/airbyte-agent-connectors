"""Shared session context for both logging and telemetry."""

import logging
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


def get_persistent_user_id() -> str:
    """
    Get or create an anonymous user ID stored in the home directory.

    The ID is stored in ~/.airbyte/ai_sdk_user_id and persists across all sessions.
    If the file doesn't exist, a new UUID is generated and saved.

    Returns:
        An anonymous UUID string that uniquely identifies this user across sessions.
    """
    try:
        # Create .airbyte directory in home folder if it doesn't exist
        airbyte_dir = Path.home() / ".airbyte"
        airbyte_dir.mkdir(exist_ok=True)

        # Path to user ID file
        user_id_file = airbyte_dir / "ai_sdk_user_id"

        # Try to read existing user ID
        if user_id_file.exists():
            user_id = user_id_file.read_text().strip()
            if user_id:  # Validate it's not empty
                return user_id

        # Generate new user ID if file doesn't exist or is empty
        user_id = str(uuid.uuid4())
        user_id_file.write_text(user_id)
        logger.debug(f"Generated new anonymous user ID: {user_id}")

        return user_id
    except Exception as e:
        # If we can't read/write the file, generate a session-only ID
        logger.debug(f"Could not access anonymous user ID file: {e}")
        return str(uuid.uuid4())


def get_public_ip() -> Optional[str]:
    """
    Fetch the public IP address of the user.

    Returns None if unable to fetch (network issues, etc).
    Uses httpx for a robust HTTP request to a public IP service.
    """
    try:
        import httpx

        # Use a short timeout to avoid blocking
        with httpx.Client(timeout=2.0) as client:
            response = client.get("https://api.ipify.org?format=text")
            response.raise_for_status()
            return response.text.strip()
    except Exception:
        # Never fail - just return None
        return None


class ObservabilitySession:
    """Shared session context for both logging and telemetry."""

    def __init__(
        self,
        connector_name: str,
        connector_version: Optional[str] = None,
        execution_context: str = "direct",
        session_id: Optional[str] = None,
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

    def increment_operations(self):
        """Increment the operation counter."""
        self.operation_count += 1

    def duration_seconds(self) -> float:
        """Calculate session duration in seconds."""
        return (datetime.now(UTC) - self.started_at).total_seconds()
