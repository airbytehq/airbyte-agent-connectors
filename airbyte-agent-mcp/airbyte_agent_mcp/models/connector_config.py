"""Connector configuration models."""

import os
import re
from pathlib import Path

import yaml
from pydantic import BaseModel, Field, model_validator

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


class ConnectorSource(BaseModel):
    """Connector source configuration.

    Supports three mutually exclusive package source types:
    - ``package``: A PyPI package name (e.g., ``airbyte-agent-gong``)
    - ``path``: A local filesystem path (e.g., ``../integrations/gong/.generated``)
    - ``git``: A git repository URL (e.g., ``https://github.com/org/repo.git``)

    Additionally, ``connector_id`` is orthogonal and can be combined with any
    package source, or used alone (auto-resolves the package from the registry).
    """

    package: str | None = None
    version: str | None = None
    path: str | None = None
    git: str | None = None
    ref: str | None = None
    subdirectory: str | None = None
    connector_id: str | None = None

    @model_validator(mode="after")
    def validate_source(self) -> "ConnectorSource":
        sources = [s for s in (self.package, self.path, self.git) if s is not None]
        if len(sources) > 1:
            raise ValueError("At most one of 'package', 'path', 'git' may be specified")
        if len(sources) == 0 and self.connector_id is None:
            raise ValueError("At least one of 'package', 'path', 'git', or 'connector_id' must be specified")
        if self.version is not None and self.package is None:
            raise ValueError("'version' can only be used with 'package'")
        if self.ref is not None and self.git is None:
            raise ValueError("'ref' can only be used with 'git'")
        if self.subdirectory is not None and self.git is None:
            raise ValueError("'subdirectory' can only be used with 'git'")
        return self

    @property
    def is_cloud(self) -> bool:
        return self.connector_id is not None

    @property
    def has_package_source(self) -> bool:
        return self.package is not None or self.path is not None or self.git is not None

    def to_install_spec(self) -> str | None:
        """Return a pip-installable spec string, or None if cloud-only."""
        if self.path is not None:
            return self.path
        if self.git is not None:
            spec = f"git+{self.git}"
            if self.ref:
                spec += f"@{self.ref}"
            if self.subdirectory:
                spec += f"#subdirectory={self.subdirectory}"
            return spec
        if self.package is not None:
            if self.version:
                return f"{self.package}=={self.version}"
            return self.package
        return None


def auth_config_to_env_template(auth_config_type: type[BaseModel], connector_name: str | None = None) -> dict[str, str]:
    """Convert an auth config type to a dict with environment variable placeholders.

    Args:
        auth_config_type: A Pydantic model class for auth configuration.
        connector_name: Optional connector name used as env var prefix (e.g., "gong").
            When None, field names are used directly (e.g., ``airbyte_client_id`` -> ``AIRBYTE_CLIENT_ID``).

    Returns:
        Dict mapping field names to environment variable placeholders.
    """
    if connector_name:
        prefix = connector_name.upper().replace("-", "_").replace(" ", "_")
        return {field_name: f"${{env.{prefix}_{field_name.upper()}}}" for field_name in auth_config_type.model_fields}
    return {field_name: f"${{env.{field_name.upper()}}}" for field_name in auth_config_type.model_fields}


def connector_params_to_template(params: list) -> dict[str, str]:
    """Convert a list of ConnectorParam to a dict with placeholder values.

    Args:
        params: List of ConnectorParam from get_additional_connector_params().

    Returns:
        Dict mapping param names to placeholder values.
        E.g., {"subdomain": "# TODO: your-subdomain"}
    """
    return {p.name: f"# TODO: {p.name}" for p in params}


_PACKAGE_PREFIX = "airbyte-agent-"


def _load_yaml(config_path: Path) -> dict:
    if not config_path.exists():
        raise FileNotFoundError(f"Connector config file not found: {config_path}")
    with open(config_path) as f:
        return yaml.safe_load(f) or {}


class ConnectorConfig(BaseModel):
    """Configuration for a single connector."""

    connector: ConnectorSource
    credentials: dict[str, str] = Field(default_factory=dict)
    config: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def _normalize_connector(cls, data: dict) -> dict:
        if not isinstance(data, dict) or "connector" not in data:
            return data
        value = data["connector"]
        if isinstance(value, str):
            name = value if value.startswith(_PACKAGE_PREFIX) else f"{_PACKAGE_PREFIX}{value}"
            data["connector"] = {"package": name}
        return data

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
        return cls(**_load_yaml(config_path))

    def to_dict(self) -> dict:
        """Convert to dict, excluding None values and empty dicts.

        Returns:
            Dict representation with empty values removed.
        """
        data = self.model_dump(mode="json", exclude_none=True)
        return {k: v for k, v in data.items() if v != {}}

    def save(self, config_path: Path) -> None:
        """Save connector configuration to file.

        Args:
            config_path: Path to config file.
        """
        config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(config_path, "w") as f:
            yaml.safe_dump(self.to_dict(), f, default_flow_style=False, sort_keys=False)


class ConnectorConfigList(BaseModel):
    """Configuration that references multiple connector config files."""

    name: str
    configs: list[Path]

    @model_validator(mode="after")
    def validate_configs(self) -> "ConnectorConfigList":
        if not self.configs:
            raise ValueError("'configs' must contain at least one config file path")
        if not self.name.strip():
            raise ValueError("'name' cannot be empty")
        return self

    @classmethod
    def load(cls, config_path: Path) -> "ConnectorConfigList":
        """Load aggregate connector configuration from file."""
        aggregate = cls(**_load_yaml(config_path))

        base_dir = config_path.parent
        resolved_configs = [p if p.is_absolute() else base_dir / p for p in aggregate.configs]
        return cls(name=aggregate.name, configs=resolved_configs)


def resolve_connector_config(config_path: Path) -> list[Path]:
    """Resolve config path(s) from a single or aggregate config file."""
    data = _load_yaml(config_path)
    has_connector = "connector" in data
    has_configs = "configs" in data

    if has_connector and has_configs:
        raise ValueError("Config cannot contain both 'connector' and 'configs'")

    if has_configs:
        return ConnectorConfigList.load(config_path).configs

    ConnectorConfig.load(config_path)
    return [config_path]


def resolve_aggregate_name(config_path: Path) -> str | None:
    """Resolve aggregate config name if present, otherwise return None."""
    data = _load_yaml(config_path)
    has_connector = "connector" in data
    has_configs = "configs" in data

    if has_connector and has_configs:
        raise ValueError("Config cannot contain both 'connector' and 'configs'")

    if not has_configs:
        return None

    aggregate = ConnectorConfigList.load(config_path)
    return aggregate.name
