"""
Tests for Linear blessed connector.
"""

from airbyte_ai_linear import LinearConnector


def test_connector_creation():
    """Test creating LinearConnector instance."""
    connector = LinearConnector.create(secrets={"api_key": "test_key"})
    assert connector.connector_name == "linear"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert LinearConnector.connector_name == "linear"
    assert hasattr(LinearConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = LinearConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
