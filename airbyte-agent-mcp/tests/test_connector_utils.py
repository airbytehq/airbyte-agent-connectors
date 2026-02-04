"""Tests for connector_utils helpers."""

from pydantic import BaseModel

from airbyte_agent_mcp.connector_utils import (
    AirbyteCloudAuthConfig,
    ConnectorLoadError,
    ConnectorParam,
    _package_to_module_name,
    get_cloud_auth_config_type,
)


class TestConnectorParam:
    def test_create(self):
        p = ConnectorParam(name="subdomain", annotation="str", required=True)
        assert p.name == "subdomain"
        assert p.annotation == "str"
        assert p.required is True

    def test_optional_annotation(self):
        p = ConnectorParam(name="region", annotation=None, required=False)
        assert p.annotation is None
        assert p.required is False


class TestPackageToModuleName:
    def test_replaces_hyphens(self):
        assert _package_to_module_name("airbyte-agent-gong") == "airbyte_agent_gong"

    def test_no_hyphens(self):
        assert _package_to_module_name("mypackage") == "mypackage"

    def test_multiple_hyphens(self):
        assert _package_to_module_name("a-b-c-d") == "a_b_c_d"


class TestGetCloudAuthConfigType:
    def test_returns_airbyte_cloud_auth_config(self):
        result = get_cloud_auth_config_type()
        assert result is AirbyteCloudAuthConfig
        assert issubclass(result, BaseModel)


class TestAirbyteCloudAuthConfig:
    def test_create(self):
        cfg = AirbyteCloudAuthConfig(
            airbyte_external_user_id="user1",
            airbyte_client_id="client1",
            airbyte_client_secret="secret1",
        )
        assert cfg.airbyte_external_user_id == "user1"
        assert cfg.airbyte_client_id == "client1"
        assert cfg.airbyte_client_secret == "secret1"

    def test_fields_present(self):
        fields = AirbyteCloudAuthConfig.model_fields
        assert "airbyte_external_user_id" in fields
        assert "airbyte_client_id" in fields
        assert "airbyte_client_secret" in fields


class TestConnectorLoadError:
    def test_is_exception(self):
        err = ConnectorLoadError("something broke")
        assert isinstance(err, Exception)
        assert str(err) == "something broke"
