"""
Tests for Zendesk-Support blessed connector.
"""

from airbyte_ai_zendesk_support import ZendeskSupportConnector


def test_connector_creation():
    """Test creating ZendeskSupportConnector instance."""
    connector = ZendeskSupportConnector.create(secrets={"api_key": "test_key"})
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
