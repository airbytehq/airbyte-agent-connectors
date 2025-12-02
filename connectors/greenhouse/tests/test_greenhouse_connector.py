"""
Tests for Greenhouse blessed connector.
"""

from airbyte_ai_greenhouse import GreenhouseConnector


def test_connector_creation():
    """Test creating GreenhouseConnector instance with Harvest API Key Authentication."""
    connector = GreenhouseConnector.create(auth_config={"api_key": "test_api_key"})
    assert connector.connector_name == "greenhouse"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert GreenhouseConnector.connector_name == "greenhouse"
    assert hasattr(GreenhouseConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = GreenhouseConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
