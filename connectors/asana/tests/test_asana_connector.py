"""
Tests for Asana blessed connector.
"""

from airbyte_ai_asana import AsanaConnector


def test_connector_creation():
    """Test creating AsanaConnector instance with Authentication.
    """
    connector = AsanaConnector(auth_config={"token": "test_token"})
    assert connector.connector_name == "asana"
    assert connector.connector_version

def test_connector_metadata():
    """Test connector metadata."""
    assert AsanaConnector.connector_name == "asana"
    assert hasattr(AsanaConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = AsanaConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"