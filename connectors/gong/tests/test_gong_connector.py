"""
Tests for Gong blessed connector.
"""

from airbyte_ai_gong import GongConnector


def test_connector_creation():
    """Test creating GongConnector instance with Access Key Authentication."""
    connector = GongConnector.create(auth_config={"access_key": "test_access_key", "access_key_secret": "test_access_key_secret"})
    assert connector.connector_name == "gong"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert GongConnector.connector_name == "gong"
    assert hasattr(GongConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = GongConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
