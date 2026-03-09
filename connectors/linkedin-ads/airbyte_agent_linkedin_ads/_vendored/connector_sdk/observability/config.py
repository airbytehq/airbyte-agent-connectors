"""Unified configuration for connector-sdk."""

import logging
import os
import tempfile
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

# New config location
CONFIG_DIR = Path.home() / ".airbyte" / "connector-sdk"
CONFIG_PATH = CONFIG_DIR / "config.yaml"

# Legacy file locations (for migration)
LEGACY_USER_ID_PATH = Path.home() / ".airbyte" / "ai_sdk_user_id"
LEGACY_INTERNAL_MARKER_PATH = Path.home() / ".airbyte" / "internal_user"


@dataclass
class SDKConfig:
    """Connector SDK configuration."""

    user_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_internal_user: bool = False

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for YAML serialization."""
        return {
            "user_id": self.user_id,
            "is_internal_user": self.is_internal_user,
        }


def _delete_legacy_files() -> None:
    """
    Delete legacy config files after successful migration.

    Removes:
    - ~/.airbyte/ai_sdk_user_id
    - ~/.airbyte/internal_user
    """
    for legacy_path in [LEGACY_USER_ID_PATH, LEGACY_INTERNAL_MARKER_PATH]:
        try:
            if legacy_path.exists():
                legacy_path.unlink()
                logger.debug(f"Deleted legacy config file: {legacy_path}")
        except Exception as e:
            logger.debug(f"Could not delete legacy file {legacy_path}: {e}")


def _migrate_legacy_config() -> SDKConfig | None:
    """
    Migrate from legacy file-based config to new YAML format.

    Reads from:
    - ~/.airbyte/ai_sdk_user_id (user_id)
    - ~/.airbyte/internal_user (is_internal_user marker)

    Returns SDKConfig if migration was successful, None otherwise.
    """
    user_id = None
    is_internal = False

    # Try to read legacy user_id
    try:
        if LEGACY_USER_ID_PATH.exists():
            user_id = LEGACY_USER_ID_PATH.read_text().strip()
            if not user_id:
                user_id = None
    except Exception:
        pass

    # Check legacy internal_user marker
    try:
        is_internal = LEGACY_INTERNAL_MARKER_PATH.exists()
    except Exception:
        pass

    if user_id or is_internal:
        return SDKConfig(
            user_id=user_id or str(uuid.uuid4()),
            is_internal_user=is_internal,
        )

    return None


def load_config() -> SDKConfig:
    """
    Load SDK configuration from config file.

    Checks (in order):
    1. New config file at ~/.airbyte/connector-sdk/config.yaml
    2. Legacy files at ~/.airbyte/ai_sdk_user_id and ~/.airbyte/internal_user
    3. Creates new config with generated user_id if nothing exists

    Environment variable AIRBYTE_INTERNAL_USER can override is_internal_user.

    Returns:
        SDKConfig with user_id and is_internal_user
    """
    config = None

    # Try to load from new config file
    try:
        if CONFIG_PATH.exists():
            content = CONFIG_PATH.read_text()
            data = yaml.safe_load(content) or {}
            config = SDKConfig(
                user_id=data.get("user_id", str(uuid.uuid4())),
                is_internal_user=data.get("is_internal_user", False),
            )
            # Always clean up legacy files if they exist (even if new config exists)
            _delete_legacy_files()
    except Exception as e:
        logger.debug(f"Could not load config from {CONFIG_PATH}: {e}")

    # Try to migrate from legacy files if new config doesn't exist
    if config is None:
        config = _migrate_legacy_config()
        if config:
            # Save migrated config to new location
            try:
                save_config(config)
                logger.debug("Migrated legacy config to new location")
                # Delete legacy files after successful migration
                _delete_legacy_files()
            except Exception as e:
                logger.debug(f"Could not save migrated config: {e}")

    # Create new config if nothing exists
    if config is None:
        config = SDKConfig()
        try:
            save_config(config)
        except Exception as e:
            logger.debug(f"Could not save new config: {e}")

    # Environment variable override for is_internal_user
    env_value = os.getenv("AIRBYTE_INTERNAL_USER", "").lower()
    if env_value in ("true", "1", "yes"):
        config.is_internal_user = True
    elif env_value:
        # Any other non-empty value (including "false", "0", "no") defaults to False
        config.is_internal_user = False

    return config


def save_config(config: SDKConfig) -> None:
    """
    Save SDK configuration to config file.

    Creates the config directory if it doesn't exist.
    Uses atomic writes to prevent corruption from concurrent access.

    Args:
        config: SDKConfig to save
    """
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    # Use atomic write: write to temp file then rename (atomic on POSIX)
    fd, temp_path = tempfile.mkstemp(dir=CONFIG_DIR, suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            yaml.dump(config.to_dict(), f, default_flow_style=False)
        os.rename(temp_path, CONFIG_PATH)
    except Exception:
        # Clean up temp file on failure
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise
