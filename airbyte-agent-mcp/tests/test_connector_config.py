"""Tests for connector_config models and helpers."""

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import BaseModel, ValidationError

from airbyte_agent_mcp.models.connector_config import (
    ConnectorConfig,
    ConnectorConfigList,
    ConnectorSource,
    auth_config_to_env_template,
    connector_params_to_template,
    resolve_aggregate_name,
    resolve_connector_config,
    resolve_credentials,
    resolve_env_vars,
)


class TestConnectorSource:
    def test_package_only(self):
        src = ConnectorSource(package="airbyte-agent-gong")
        assert src.package == "airbyte-agent-gong"
        assert src.version is None
        assert src.path is None
        assert src.git is None
        assert src.connector_id is None

    def test_package_with_version(self):
        src = ConnectorSource(package="airbyte-agent-gong", version="1.0.0")
        assert src.package == "airbyte-agent-gong"
        assert src.version == "1.0.0"

    def test_path_only(self):
        src = ConnectorSource(path="/path/to/connector")
        assert src.path == "/path/to/connector"
        assert src.package is None

    def test_relative_path(self):
        src = ConnectorSource(path="./my/connector")
        assert src.path == "./my/connector"

    def test_git_only(self):
        src = ConnectorSource(git="https://github.com/org/repo.git")
        assert src.git == "https://github.com/org/repo.git"

    def test_git_with_ref_and_subdirectory(self):
        src = ConnectorSource(git="https://github.com/org/repo.git", ref="main", subdirectory="gong")
        assert src.ref == "main"
        assert src.subdirectory == "gong"

    def test_connector_id_only(self):
        src = ConnectorSource(connector_id="abc-123-def-456")
        assert src.connector_id == "abc-123-def-456"
        assert src.is_cloud
        assert not src.has_package_source

    def test_connector_id_with_package(self):
        src = ConnectorSource(connector_id="abc-123", package="airbyte-agent-gong", version="2.0")
        assert src.is_cloud
        assert src.has_package_source
        assert src.package == "airbyte-agent-gong"
        assert src.version == "2.0"

    def test_connector_id_with_path(self):
        src = ConnectorSource(connector_id="abc-123", path="../integrations/gong/.generated")
        assert src.is_cloud
        assert src.has_package_source

    def test_mutual_exclusion_package_and_path(self):
        with pytest.raises(ValidationError, match="At most one"):
            ConnectorSource(package="airbyte-agent-gong", path="/some/path")

    def test_mutual_exclusion_package_and_git(self):
        with pytest.raises(ValidationError, match="At most one"):
            ConnectorSource(package="airbyte-agent-gong", git="https://github.com/org/repo.git")

    def test_mutual_exclusion_path_and_git(self):
        with pytest.raises(ValidationError, match="At most one"):
            ConnectorSource(path="/some/path", git="https://github.com/org/repo.git")

    def test_no_source_at_all(self):
        with pytest.raises(ValidationError, match="At least one"):
            ConnectorSource()

    def test_version_without_package(self):
        with pytest.raises(ValidationError, match="'version' can only be used with 'package'"):
            ConnectorSource(path="/some/path", version="1.0")

    def test_ref_without_git(self):
        with pytest.raises(ValidationError, match="'ref' can only be used with 'git'"):
            ConnectorSource(package="airbyte-agent-gong", ref="main")

    def test_subdirectory_without_git(self):
        with pytest.raises(ValidationError, match="'subdirectory' can only be used with 'git'"):
            ConnectorSource(package="airbyte-agent-gong", subdirectory="gong")


class TestConnectorSourceProperties:
    def test_is_cloud_true(self):
        assert ConnectorSource(connector_id="abc").is_cloud is True

    def test_is_cloud_false(self):
        assert ConnectorSource(package="pkg").is_cloud is False

    def test_has_package_source_package(self):
        assert ConnectorSource(package="pkg").has_package_source is True

    def test_has_package_source_path(self):
        assert ConnectorSource(path="/p").has_package_source is True

    def test_has_package_source_git(self):
        assert ConnectorSource(git="https://example.com/repo.git").has_package_source is True

    def test_has_package_source_cloud_only(self):
        assert ConnectorSource(connector_id="abc").has_package_source is False


class TestConnectorSourceToInstallSpec:
    def test_package_spec(self):
        assert ConnectorSource(package="airbyte-agent-gong").to_install_spec() == "airbyte-agent-gong"

    def test_package_with_version_spec(self):
        assert ConnectorSource(package="airbyte-agent-gong", version="1.0").to_install_spec() == "airbyte-agent-gong==1.0"

    def test_path_spec(self):
        assert ConnectorSource(path="/path/to/connector").to_install_spec() == "/path/to/connector"

    def test_git_spec(self):
        assert ConnectorSource(git="https://github.com/org/repo.git").to_install_spec() == "git+https://github.com/org/repo.git"

    def test_git_with_ref_spec(self):
        src = ConnectorSource(git="https://github.com/org/repo.git", ref="main")
        assert src.to_install_spec() == "git+https://github.com/org/repo.git@main"

    def test_git_with_subdirectory_spec(self):
        src = ConnectorSource(git="https://github.com/org/repo.git", subdirectory="gong")
        assert src.to_install_spec() == "git+https://github.com/org/repo.git#subdirectory=gong"

    def test_git_with_ref_and_subdirectory_spec(self):
        src = ConnectorSource(git="https://github.com/org/repo.git", ref="main", subdirectory="gong")
        assert src.to_install_spec() == "git+https://github.com/org/repo.git@main#subdirectory=gong"

    def test_cloud_only_returns_none(self):
        assert ConnectorSource(connector_id="abc").to_install_spec() is None

    def test_cloud_with_package_returns_package_spec(self):
        src = ConnectorSource(connector_id="abc", package="airbyte-agent-gong", version="2.0")
        assert src.to_install_spec() == "airbyte-agent-gong==2.0"


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


class TestConnectorConfigStringShorthand:
    def test_string_shorthand_auto_prefixes(self):
        cfg = ConnectorConfig.model_validate({"connector": "gong", "credentials": {}})
        assert cfg.connector.package == "airbyte-agent-gong"

    def test_string_shorthand_already_prefixed(self):
        cfg = ConnectorConfig.model_validate({"connector": "airbyte-agent-gong", "credentials": {}})
        assert cfg.connector.package == "airbyte-agent-gong"

    def test_string_shorthand_with_credentials(self):
        cfg = ConnectorConfig.model_validate({"connector": "gong", "credentials": {"key": "val"}})
        assert cfg.connector.package == "airbyte-agent-gong"
        assert cfg.credentials == {"key": "val"}


class TestConnectorConfigToDict:
    def test_excludes_none_and_empty(self):
        cfg = ConnectorConfig(connector=ConnectorSource(package="airbyte-agent-gong"))
        d = cfg.to_dict()
        assert "credentials" not in d
        assert "config" not in d
        assert d["connector"]["package"] == "airbyte-agent-gong"

    def test_includes_non_empty_credentials(self):
        cfg = ConnectorConfig(
            connector=ConnectorSource(connector_id="gong"),
            credentials={"key": "value"},
        )
        d = cfg.to_dict()
        assert d["credentials"] == {"key": "value"}

    def test_cloud_with_path_to_dict(self):
        cfg = ConnectorConfig(
            connector=ConnectorSource(connector_id="abc-123", path="../integrations/gong/.generated"),
        )
        d = cfg.to_dict()
        assert d["connector"]["connector_id"] == "abc-123"
        assert d["connector"]["path"] == "../integrations/gong/.generated"


class TestConnectorConfigLoadSave:
    def test_load_package_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector:\n  package: airbyte-agent-gong\ncredentials:\n  api_key: test\n")
        cfg = ConnectorConfig.load(config_file)
        assert cfg.connector.package == "airbyte-agent-gong"
        assert cfg.credentials == {"api_key": "test"}

    def test_load_path_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector:\n  path: /path/to/connector\ncredentials:\n  api_key: test\n")
        cfg = ConnectorConfig.load(config_file)
        assert cfg.connector.path == "/path/to/connector"
        assert cfg.connector.package is None

    def test_load_cloud_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector:\n  connector_id: abc-123\ncredentials:\n  key: val\n")
        cfg = ConnectorConfig.load(config_file)
        assert cfg.connector.connector_id == "abc-123"
        assert cfg.connector.is_cloud
        assert not cfg.connector.has_package_source

    def test_load_cloud_with_path_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector:\n  connector_id: abc-123\n  path: ../integrations/gong/.generated\n")
        cfg = ConnectorConfig.load(config_file)
        assert cfg.connector.connector_id == "abc-123"
        assert cfg.connector.path == "../integrations/gong/.generated"

    def test_load_string_shorthand_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: gong\ncredentials:\n  api_key: test\n")
        cfg = ConnectorConfig.load(config_file)
        assert cfg.connector.package == "airbyte-agent-gong"

    def test_load_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            ConnectorConfig.load(tmp_path / "nonexistent.yaml")

    def test_save_and_reload(self, tmp_path):
        cfg = ConnectorConfig(
            connector=ConnectorSource(package="airbyte-agent-gong", version="1.0"),
            credentials={"key": "val"},
        )
        path = tmp_path / "out.yaml"
        cfg.save(path)
        assert path.exists()

        reloaded = ConnectorConfig.load(path)
        assert reloaded.connector.package == "airbyte-agent-gong"
        assert reloaded.connector.version == "1.0"
        assert reloaded.credentials == {"key": "val"}

    def test_save_and_reload_path(self, tmp_path):
        cfg = ConnectorConfig(
            connector=ConnectorSource(path="./my/connector"),
            credentials={"key": "val"},
        )
        path = tmp_path / "out.yaml"
        cfg.save(path)
        reloaded = ConnectorConfig.load(path)
        assert reloaded.connector.path == "./my/connector"

    def test_save_and_reload_cloud_with_package(self, tmp_path):
        cfg = ConnectorConfig(
            connector=ConnectorSource(connector_id="abc-123", package="airbyte-agent-gong", version="2.0"),
        )
        path = tmp_path / "out.yaml"
        cfg.save(path)
        reloaded = ConnectorConfig.load(path)
        assert reloaded.connector.connector_id == "abc-123"
        assert reloaded.connector.package == "airbyte-agent-gong"
        assert reloaded.connector.version == "2.0"

    def test_save_creates_parent_dirs(self, tmp_path):
        cfg = ConnectorConfig(connector=ConnectorSource(connector_id="gong"))
        path = tmp_path / "a" / "b" / "config.yaml"
        cfg.save(path)
        assert path.exists()


class TestConnectorConfigList:
    def test_load_aggregate_file(self, tmp_path):
        aggregate_file = tmp_path / "aggregate.yaml"
        aggregate_file.write_text("name: acme-data-hub\nconfigs:\n  - gong.yaml\n  - salesforce.yaml\n")

        aggregate = ConnectorConfigList.load(aggregate_file)
        assert aggregate.name == "acme-data-hub"
        assert aggregate.configs == [tmp_path / "gong.yaml", tmp_path / "salesforce.yaml"]

    def test_load_resolves_config_paths_relative_to_aggregate_file(self, tmp_path):
        aggregate_file = tmp_path / "aggregate.yaml"
        aggregate_file.write_text("name: acme-data-hub\nconfigs:\n  - connectors/gong.yaml\n")

        aggregate = ConnectorConfigList.load(aggregate_file)
        assert aggregate.configs == [tmp_path / "connectors" / "gong.yaml"]

    def test_rejects_empty_configs(self):
        with pytest.raises(ValidationError, match="must contain at least one"):
            ConnectorConfigList(name="acme-data-hub", configs=[])

    def test_accepts_name(self):
        cfg = ConnectorConfigList(name="acme-data-hub", configs=[Path("gong.yaml")])
        assert cfg.name == "acme-data-hub"

    def test_rejects_missing_name(self):
        with pytest.raises(ValidationError):
            ConnectorConfigList.model_validate({"configs": ["gong.yaml"]})

    def test_rejects_blank_name(self):
        with pytest.raises(ValidationError, match="'name' cannot be empty"):
            ConnectorConfigList(name="   ", configs=[Path("gong.yaml")])


class TestResolveConnectorConfigPaths:
    def test_single_config_returns_original_path(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: gong\n")

        paths = resolve_connector_config(config_file)
        assert paths == [config_file]

    def test_aggregate_config_returns_resolved_paths(self, tmp_path):
        config_a = tmp_path / "a.yaml"
        config_b = tmp_path / "subdir" / "b.yaml"
        config_b.parent.mkdir(parents=True, exist_ok=True)
        config_a.write_text("connector: gong\n")
        config_b.write_text("connector: salesforce\n")

        aggregate = tmp_path / "aggregate.yaml"
        aggregate.write_text("name: acme-data-hub\nconfigs:\n  - a.yaml\n  - subdir/b.yaml\n")

        paths = resolve_connector_config(aggregate)
        assert paths == [config_a, config_b]

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            resolve_connector_config(tmp_path / "missing.yaml")

    def test_rejects_ambiguous_single_and_list_config(self, tmp_path):
        config_file = tmp_path / "ambiguous.yaml"
        config_file.write_text("connector: gong\nconfigs:\n  - other.yaml\n")

        with pytest.raises(ValueError, match="both 'connector' and 'configs'"):
            resolve_connector_config(config_file)


class TestResolveAggregateName:
    def test_returns_none_for_single_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: gong\n")

        assert resolve_aggregate_name(config_file) is None

    def test_returns_none_for_aggregate_without_name(self, tmp_path):
        config_file = tmp_path / "aggregate.yaml"
        config_file.write_text("configs:\n  - gong.yaml\n")

        with pytest.raises(ValidationError):
            resolve_aggregate_name(config_file)

    def test_returns_name_for_aggregate_with_name(self, tmp_path):
        config_file = tmp_path / "aggregate.yaml"
        config_file.write_text("name: acme-data-hub\nconfigs:\n  - gong.yaml\n")

        assert resolve_aggregate_name(config_file) == "acme-data-hub"
