"""Configuration model for Airbyte Agent MCP."""

import uuid
from pathlib import Path

import yaml
from pydantic import BaseModel, Field

# Default config directory in user's home
DEFAULT_CONFIG_DIR = Path.home() / ".airbyte_agent_mcp"

# Global config directory - can be overridden
_config_dir: Path = DEFAULT_CONFIG_DIR


def set_config_dir(config_dir: Path) -> None:
    """Set the global config directory.

    Args:
        config_dir: Path to the config directory.
    """
    global _config_dir
    _config_dir = config_dir


def get_config_dir() -> Path:
    """Get the current config directory.

    Returns:
        Path to the config directory.
    """
    return _config_dir


class Config(BaseModel):
    """Configuration model for Airbyte Agent MCP."""

    installation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    @classmethod
    def load(cls, config_dir: Path | None = None) -> "Config":
        """Load configuration from file, or create default if it doesn't exist.

        Args:
            config_dir: Optional config directory path. If None, uses global config dir.

        Returns:
            Config object with loaded or default configuration.
        """
        dir_path = config_dir or _config_dir
        dir_path.mkdir(parents=True, exist_ok=True)
        config_file = dir_path / "config.yaml"

        if config_file.exists():
            with open(config_file) as f:
                data = yaml.safe_load(f) or {}
                return cls(**data)
        else:
            # Create default config
            config = cls()
            config.save(config_dir)
            return config

    def save(self, config_dir: Path | None = None) -> None:
        """Save configuration to file.

        Args:
            config_dir: Optional config directory path. If None, uses global config dir.
        """
        dir_path = config_dir or _config_dir
        dir_path.mkdir(parents=True, exist_ok=True)
        config_file = dir_path / "config.yaml"

        with open(config_file, "w") as f:
            yaml.safe_dump(self.model_dump(), f, default_flow_style=False)

    @classmethod
    def get(cls, config_dir: Path | None = None) -> "Config":
        """Get the current configuration.

        Args:
            config_dir: Optional config directory path. If None, uses global config dir.

        Returns:
            Config object with current configuration.
        """
        return cls.load(config_dir)
