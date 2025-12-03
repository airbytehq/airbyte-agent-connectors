"""
Tests for Hubspot blessed connector.
"""

from airbyte_ai_hubspot import HubspotConnector


def test_connector_creation():
    """Test creating HubspotConnector instance with Access Token Authentication."""
    connector = HubspotConnector(auth_config={"access_token": "test_access_token"})
    assert connector.connector_name == "hubspot"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert HubspotConnector.connector_name == "hubspot"
    assert hasattr(HubspotConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = HubspotConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
