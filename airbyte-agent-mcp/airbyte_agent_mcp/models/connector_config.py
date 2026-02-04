"""Connector configuration models."""

import os
import re
from enum import Enum
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field

_ENV_PATTERN = re.compile(r"\$\{env\.([^}]+)\}")


def resolve_env_vars(value: str) -> str:
    """Replace ${env.VAR_NAME} placeholders with actual environment variable values.

    Args:
        value: String that may contain ${env.VAR_NAME} placeholders.

    Returns:
        String with placeholders replaced by environment variable values.

    Raises:
        ValueError: If an environment variable is not set.
    """

    def replace_env(match: re.Match) -> str:
        var_name = match.group(1)
        env_value = os.environ.get(var_name)
        if env_value is None:
            raise ValueError(f"Environment variable '{var_name}' is not set")
        return env_value

    return _ENV_PATTERN.sub(replace_env, value)


def resolve_credentials(credentials: dict[str, str]) -> dict[str, str]:
    """Resolve environment variables in all credential values.

    Args:
        credentials: Dict with potentially templated values.

    Returns:
        Dict with all environment variable placeholders resolved.

    Raises:
        ValueError: If any environment variable is not set.
    """
    return {key: resolve_env_vars(value) for key, value in credentials.items()}


class SourceType(str, Enum):
    """Type of connector source."""

    PACKAGE = "package"
    CLOUD = "cloud"


class PackageSource(BaseModel):
    """Package connector source configuration.

    The ``package`` field accepts anything ``pip install`` understands:
    - A PyPI name: ``airbyte-agent-gong``
    - A local path (contains ``/``): ``/path/to/connector`` or ``./rel/path``
    - A git URL: ``git+https://github.com/org/repo.git@branch``
    """

    type: Literal[SourceType.PACKAGE] = SourceType.PACKAGE
    package: str
    version: str | None = None  # None means latest (PyPI only)


class CloudSource(BaseModel):
    """Airbyte Cloud connector source configuration."""

    type: Literal[SourceType.CLOUD] = SourceType.CLOUD
    connector_id: str


Source = PackageSource | CloudSource


def auth_config_to_env_template(auth_config_type: type[BaseModel], connector_name: str) -> dict[str, str]:
    """Convert an auth config type to a dict with environment variable placeholders.

    Args:
        auth_config_type: A Pydantic model class for auth configuration.
        connector_name: Name of the connector, used as env var prefix (e.g., "gong").

    Returns:
        Dict mapping field names to environment variable placeholders.
        E.g., {"access_key": "${env.GONG_ACCESS_KEY}", "access_key_secret": "${env.GONG_ACCESS_KEY_SECRET}"}
    """
    prefix = connector_name.upper().replace("-", "_").replace(" ", "_")
    return {field_name: f"${{env.{prefix}_{field_name.upper()}}}" for field_name in auth_config_type.model_fields}


def connector_params_to_template(params: list) -> dict[str, str]:
    """Convert a list of ConnectorParam to a dict with placeholder values.

    Args:
        params: List of ConnectorParam from get_additional_connector_params().

    Returns:
        Dict mapping param names to placeholder values.
        E.g., {"subdomain": "# TODO: your-subdomain"}
    """
    return {p.name: f"# TODO: {p.name}" for p in params}


class ConnectorConfig(BaseModel):
    """Configuration for a single connector."""

    connector: Source
    credentials: dict[str, str] = Field(default_factory=dict)
    config: dict[str, str] = Field(default_factory=dict)

    @classmethod
    def load(cls, config_path: Path) -> "ConnectorConfig":
        """Load connector configuration from file.

        Args:
            config_path: Path to config file.

        Returns:
            ConnectorConfig object with loaded configuration.

        Raises:
            FileNotFoundError: If config file doesn't exist.
        """
        if not config_path.exists():
            raise FileNotFoundError(f"Connector config file not found: {config_path}")

        with open(config_path) as f:
            data = yaml.safe_load(f) or {}
            return cls(**data)

    def to_dict(self) -> dict:
        """Convert to dict, excluding None values and empty dicts.

        Returns:
            Dict representation with empty values removed.
        """
        data = self.model_dump(mode="json", exclude_none=True)
        # Remove empty dicts
        return {k: v for k, v in data.items() if v != {}}

    def save(self, config_path: Path) -> None:
        """Save connector configuration to file.

        Args:
            config_path: Path to config file.
        """
        # Ensure parent directory exists
        config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(config_path, "w") as f:
            yaml.safe_dump(self.to_dict(), f, default_flow_style=False, sort_keys=False)
