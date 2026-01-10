"""
Tests for Commonroom blessed connector.
"""

from airbyte_agent_commonroom import CommonroomConnector
from airbyte_agent_commonroom.models import CommonroomAuthConfig

def test_connector_creation():
    """Test creating CommonroomConnector instance with API Token Authentication.
    """
    connector = CommonroomConnector(auth_config=CommonroomAuthConfig(api_token="test_api_token"))
    assert connector.connector_name == "commonroom"
    assert connector.connector_version

def test_connector_metadata():
    """Test connector metadata."""
    assert CommonroomConnector.connector_name == "commonroom"
    assert hasattr(CommonroomConnector, "connector_version")


def test_embedded_connector_model():
    """Test embedded model can be loaded."""
    from airbyte_agent_commonroom.connector_model import CommonroomConnectorModel

    assert CommonroomConnectorModel is not None
    assert CommonroomConnectorModel.name == "commonroom"
    assert len(CommonroomConnectorModel.entities) > 0