"""Test data models."""

import pytest
from pydantic import ValidationError

from airbyte_agent_mcp.models import (
    ConnectorConfig,
    ConnectorType,
)


def test_local_connector_requires_path_or_connector_name():
    """Test LOCAL connector requires either path or connector_name."""
    with pytest.raises(ValidationError):
        ConnectorConfig(
            id="test",
            type=ConnectorType.LOCAL,
            # Missing both path and connector_name!
        )


def test_local_connector_with_path():
    """Test LOCAL connector with path is valid."""
    connector = ConnectorConfig(
        id="test",
        type=ConnectorType.LOCAL,
        path="/path/to/connector.yaml",
    )
    assert connector.id == "test"
    assert connector.type == ConnectorType.LOCAL
    assert connector.path == "/path/to/connector.yaml"
    assert connector.connector_name is None


def test_local_connector_with_connector_name():
    """Test LOCAL connector with connector_name is valid."""
    connector = ConnectorConfig(
        id="test",
        type=ConnectorType.LOCAL,
        connector_name="stripe",
    )
    assert connector.id == "test"
    assert connector.type == ConnectorType.LOCAL
    assert connector.path is None
    assert connector.connector_name == "stripe"


def test_local_connector_with_connector_name_and_version():
    """Test LOCAL connector with connector_name and version is valid."""
    connector = ConnectorConfig(
        id="test",
        type=ConnectorType.LOCAL,
        connector_name="stripe",
        version="1.2.0",
    )
    assert connector.id == "test"
    assert connector.connector_name == "stripe"
    assert connector.version == "1.2.0"


def test_local_connector_with_path_and_version_fails():
    """Test LOCAL connector with path and version is invalid.

    Version pinning is only supported for registry-based connectors.
    """
    with pytest.raises(ValidationError, match="Version pinning is only supported for registry-based connectors"):
        ConnectorConfig(
            id="test",
            type=ConnectorType.LOCAL,
            path="/path/to/connector.yaml",
            version="1.0.0",
        )


def test_hosted_connector_valid():
    """Test HOSTED connector validation."""
    # HOSTED connectors don't require path
    connector = ConnectorConfig(id="test", type=ConnectorType.HOSTED, description="Test hosted connector")
    assert connector.id == "test"
    assert connector.type == ConnectorType.HOSTED
