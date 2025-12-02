"""
Tests for Zendesk-Support blessed connector.
"""

from airbyte_ai_zendesk_support import ZendeskSupportConnector


def test_connector_creation():
    """Test creating ZendeskSupportConnector instance with Authentication."""
    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_access_token", "refresh_token": "test_refresh_token", "client_id": "test_client_id", "client_secret": "test_client_secret"})
    assert connector.connector_name == "zendesk-support"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert ZendeskSupportConnector.connector_name == "zendesk-support"
    assert hasattr(ZendeskSupportConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = ZendeskSupportConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
