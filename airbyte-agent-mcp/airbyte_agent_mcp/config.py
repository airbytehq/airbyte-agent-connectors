"""Configuration loading and validation."""

import logging
from pathlib import Path

import yaml

from airbyte_agent_mcp.models import Config, ConnectorType

logger = logging.getLogger(__name__)


def load_connector_config(config_path: str = "configured_connectors.yaml") -> Config:
    """Load and validate configuration from YAML file.

    Args:
        config_path: Path to configured_connectors.yaml file

    Returns:
        Validated Config object

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config is invalid
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}\nCreate a configured_connectors.yaml file with your connector definitions."
        )

    logger.info(f"Loading configuration from {config_path}")

    with open(path) as f:
        data = yaml.safe_load(f)

    if not data:
        raise ValueError(f"Configuration file is empty: {config_path}")

    try:
        config = Config(**data)
    except Exception as e:
        raise ValueError(f"Invalid configuration: {e}") from e

    logger.info(f"Loaded {len(config.connectors)} connector(s): {', '.join(c.id for c in config.connectors)}")

    return config


def validate_connectors(config: Config) -> list[str]:
    """Validate that connectors are available.

    For LOCAL connectors with path: Check if connector.yaml exists
    For LOCAL connectors with connector_name: Skip validation (validated lazily on first use)
    For HOSTED connectors: Not implemented

    Args:
        config: Configuration to validate

    Returns:
        List of error messages (empty if all valid)
    """
    errors = []

    for connector in config.connectors:
        logger.debug(f"Validating connector: {connector.id}")

        if connector.type == ConnectorType.LOCAL:
            if connector.path:
                # Check if connector.yaml exists
                connector_path = Path(connector.path)
                if not connector_path.exists():
                    error = f"LOCAL connector '{connector.id}': File not found: {connector.path}"
                    errors.append(error)
                    logger.error(error)
                else:
                    logger.debug(f"LOCAL connector '{connector.id}' file found")
            elif connector.connector_name:
                # Registry-based connector: validation happens lazily on first use
                logger.debug(
                    f"LOCAL connector '{connector.id}' uses registry (connector_name={connector.connector_name}), skipping startup validation"
                )
        elif connector.type == ConnectorType.HOSTED:
            # HOSTED connectors are not implemented yet
            error = f"HOSTED connector '{connector.id}' - not implemented"
            errors.append(error)
            logger.error(error)
        else:
            error = f"Unknown connector type '{connector.type}' found"
            errors.append(error)
            logger.error(error)

    if not errors:
        logger.info("All connectors validated successfully")

    return errors
