"""Tests for connector_config models and helpers."""

import os
from unittest.mock import patch

import pytest
from pydantic import BaseModel

from airbyte_agent_mcp.models.connector_config import (
    CloudSource,
    ConnectorConfig,
    PackageSource,
    SourceType,
    auth_config_to_env_template,
    connector_params_to_template,
    resolve_credentials,
    resolve_env_vars,
)


class TestSourceType:
    def test_values(self):
        assert SourceType.PACKAGE == "package"
        assert SourceType.CLOUD == "cloud"


class TestPackageSource:
    def test_create_with_version(self):
        src = PackageSource(package="airbyte-agent-gong", version="1.0.0")
        assert src.package == "airbyte-agent-gong"
        assert src.version == "1.0.0"

    def test_create_without_version(self):
        src = PackageSource(package="airbyte-agent-gong")
        assert src.version is None

    def test_create_with_local_path(self):
        src = PackageSource(package="/path/to/connector")
        assert src.type == SourceType.PACKAGE
        assert src.package == "/path/to/connector"

    def test_create_with_relative_path(self):
        src = PackageSource(package="./my/connector")
        assert src.package == "./my/connector"

    def test_create_with_git_url(self):
        src = PackageSource(package="git+https://github.com/org/repo.git@main")
        assert src.package == "git+https://github.com/org/repo.git@main"


class TestCloudSource:
    def test_create(self):
        src = CloudSource(connector_id="abc-123-def-456")
        assert src.type == SourceType.CLOUD
        assert src.connector_id == "abc-123-def-456"


class TestResolveEnvVars:
    def test_replaces_env_var(self):
        with patch.dict(os.environ, {"MY_KEY": "secret123"}):
            assert resolve_env_vars("${env.MY_KEY}") == "secret123"

    def test_replaces_multiple_vars(self):
        with patch.dict(os.environ, {"A": "hello", "B": "world"}):
            assert resolve_env_vars("${env.A} ${env.B}") == "hello world"

    def test_no_placeholders(self):
        assert resolve_env_vars("plain text") == "plain text"

    def test_missing_env_var_raises(self):
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="MISSING_VAR"):
                resolve_env_vars("${env.MISSING_VAR}")


class TestResolveCredentials:
    def test_resolves_all_values(self):
        with patch.dict(os.environ, {"KEY": "val1", "SECRET": "val2"}):
            result = resolve_credentials({"api_key": "${env.KEY}", "api_secret": "${env.SECRET}"})
            assert result == {"api_key": "val1", "api_secret": "val2"}

    def test_plain_values_unchanged(self):
        result = resolve_credentials({"key": "literal_value"})
        assert result == {"key": "literal_value"}


class TestAuthConfigToEnvTemplate:
    def test_generates_template_with_connector_prefix(self):
        class MyAuth(BaseModel):
            access_key: str
            access_key_secret: str

        result = auth_config_to_env_template(MyAuth, "gong")
        assert result == {
            "access_key": "${env.GONG_ACCESS_KEY}",
            "access_key_secret": "${env.GONG_ACCESS_KEY_SECRET}",
        }

    def test_hyphenated_connector_name(self):
        class MyAuth(BaseModel):
            api_key: str

        result = auth_config_to_env_template(MyAuth, "zendesk-support")
        assert result == {
            "api_key": "${env.ZENDESK_SUPPORT_API_KEY}",
        }

    def test_empty_model(self):
        class Empty(BaseModel):
            pass

        assert auth_config_to_env_template(Empty, "gong") == {}


class TestConnectorParamsToTemplate:
    def test_generates_template(self):
        from airbyte_agent_mcp.connector_utils import ConnectorParam

        params = [ConnectorParam("subdomain", "str", True), ConnectorParam("region", "str", False)]
        result = connector_params_to_template(params)
        assert result == {"subdomain": "# TODO: subdomain", "region": "# TODO: region"}

    def test_empty_list(self):
        assert connector_params_to_template([]) == {}


class TestConnectorConfigToDict:
    def test_excludes_none_and_empty(self):
        cfg = ConnectorConfig(connector=PackageSource(package="airbyte-agent-gong"))
        d = cfg.to_dict()
        assert "credentials" not in d
        assert "config" not in d
        assert d["connector"]["package"] == "airbyte-agent-gong"

    def test_includes_non_empty_credentials(self):
        cfg = ConnectorConfig(
            connector=CloudSource(connector_id="gong"),
            credentials={"key": "value"},
        )
        d = cfg.to_dict()
        assert d["credentials"] == {"key": "value"}


class TestConnectorConfigLoadSave:
    def test_load_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector:\n  type: package\n  package: airbyte-agent-gong\ncredentials:\n  api_key: test\n")
        cfg = ConnectorConfig.load(config_file)
        assert isinstance(cfg.connector, PackageSource)
        assert cfg.credentials == {"api_key": "test"}

    def test_load_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            ConnectorConfig.load(tmp_path / "nonexistent.yaml")

    def test_save_and_reload(self, tmp_path):
        cfg = ConnectorConfig(
            connector=PackageSource(package="airbyte-agent-gong", version="1.0"),
            credentials={"key": "val"},
        )
        path = tmp_path / "out.yaml"
        cfg.save(path)
        assert path.exists()

        reloaded = ConnectorConfig.load(path)
        assert isinstance(reloaded.connector, PackageSource)
        assert reloaded.connector.package == "airbyte-agent-gong"
        assert reloaded.credentials == {"key": "val"}

    def test_save_creates_parent_dirs(self, tmp_path):
        cfg = ConnectorConfig(connector=CloudSource(connector_id="gong"))
        path = tmp_path / "a" / "b" / "config.yaml"
        cfg.save(path)
        assert path.exists()

    def test_load_local_path_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector:\n  type: package\n  package: /path/to/connector\ncredentials:\n  api_key: test\n")
        cfg = ConnectorConfig.load(config_file)
        assert isinstance(cfg.connector, PackageSource)
        assert cfg.connector.package == "/path/to/connector"

    def test_save_and_reload_local_path(self, tmp_path):
        cfg = ConnectorConfig(
            connector=PackageSource(package="./my/connector"),
            credentials={"key": "val"},
        )
        path = tmp_path / "out.yaml"
        cfg.save(path)
        reloaded = ConnectorConfig.load(path)
        assert isinstance(reloaded.connector, PackageSource)
        assert reloaded.connector.package == "./my/connector"
