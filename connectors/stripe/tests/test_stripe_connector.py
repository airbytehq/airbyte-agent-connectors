"""
Tests for Stripe blessed connector.
"""

from airbyte_ai_stripe import StripeConnector


def test_connector_creation():
    """Test creating StripeConnector instance with Authentication."""
    connector = StripeConnector.create(auth_config={"token": "test_token"})
    assert connector.connector_name == "stripe"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert StripeConnector.connector_name == "stripe"
    assert hasattr(StripeConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = StripeConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
