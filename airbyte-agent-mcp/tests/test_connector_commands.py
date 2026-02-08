"""Tests for connector CLI commands."""

from unittest.mock import patch

from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli
from airbyte_agent_mcp.cli.connector_commands import _connector_name_from_package, _parse_git_url

runner = CliRunner()


class TestConnectorNameFromPackage:
    def test_strips_airbyte_agent_prefix_hyphen(self):
        assert _connector_name_from_package("airbyte-agent-gong") == "gong"

    def test_strips_airbyte_agent_prefix_underscore(self):
        assert _connector_name_from_package("airbyte_agent_gong") == "gong"

    def test_preserves_name_without_prefix(self):
        assert _connector_name_from_package("custom-connector") == "custom-connector"

    def test_case_insensitive_prefix(self):
        assert _connector_name_from_package("Airbyte-Agent-Gong") == "Gong"

    def test_preserves_compound_name(self):
        assert _connector_name_from_package("airbyte-agent-zendesk-support") == "zendesk-support"


class TestParseGitUrl:
    def test_simple_url(self):
        result = _parse_git_url("git+https://github.com/org/repo.git")
        assert result == {"git": "https://github.com/org/repo.git"}

    def test_url_with_ref(self):
        result = _parse_git_url("git+https://github.com/org/repo.git@v1.0")
        assert result == {"git": "https://github.com/org/repo.git", "ref": "v1.0"}

    def test_url_with_subdirectory(self):
        result = _parse_git_url("git+https://github.com/org/repo.git#subdirectory=pkg")
        assert result == {"git": "https://github.com/org/repo.git", "subdirectory": "pkg"}

    def test_url_with_ref_and_subdirectory(self):
        result = _parse_git_url("git+https://github.com/org/repo.git@main#subdirectory=connectors/gong")
        assert result == {
            "git": "https://github.com/org/repo.git",
            "ref": "main",
            "subdirectory": "connectors/gong",
        }


class TestListOss:
    @patch("airbyte_agent_mcp.cli.connector_commands.fetch_registry")
    def test_lists_connectors(self, mock_fetch):
        mock_fetch.return_value = [
            {"connector_name": "gong", "latest_version": "0.1.0", "connector_definition_id": "abc"},
            {"connector_name": "stripe", "latest_version": "0.2.0", "connector_definition_id": "def"},
        ]
        result = runner.invoke(cli, ["connectors", "list-oss"])
        assert result.exit_code == 0
        assert "gong" in result.output
        assert "stripe" in result.output

    @patch("airbyte_agent_mcp.cli.connector_commands.fetch_registry")
    def test_filters_by_pattern(self, mock_fetch):
        mock_fetch.return_value = [
            {"connector_name": "gong", "latest_version": "0.1.0", "connector_definition_id": "abc"},
            {"connector_name": "stripe", "latest_version": "0.2.0", "connector_definition_id": "def"},
        ]
        result = runner.invoke(cli, ["connectors", "list-oss", "--pattern", "gong"])
        assert result.exit_code == 0
        assert "gong" in result.output
        assert "stripe" not in result.output

    @patch("airbyte_agent_mcp.cli.connector_commands.fetch_registry")
    def test_empty_results(self, mock_fetch):
        mock_fetch.return_value = []
        result = runner.invoke(cli, ["connectors", "list-oss"])
        assert result.exit_code == 0
        assert "No connectors found" in result.output

    @patch("airbyte_agent_mcp.cli.connector_commands.fetch_registry")
    def test_pattern_no_match(self, mock_fetch):
        mock_fetch.return_value = [
            {"connector_name": "gong", "latest_version": "0.1.0", "connector_definition_id": "abc"},
        ]
        result = runner.invoke(cli, ["connectors", "list-oss", "-p", "nonexistent"])
        assert result.exit_code == 0
        assert "No connectors found" in result.output


class TestConfigure:
    def test_requires_connector_id_or_package(self):
        result = runner.invoke(cli, ["connectors", "configure"])
        assert result.exit_code == 1
        assert "Must provide at least one" in result.output

    def test_version_requires_package(self):
        result = runner.invoke(cli, ["connectors", "configure", "--connector-id", "abc", "--version", "1.0.0"])
        assert result.exit_code == 1
        assert "--version can only be used with --package" in result.output

    @patch("airbyte_agent_mcp.cli.connector_commands.install_package")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_package_name")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_auth_config_types")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_additional_connector_params")
    def test_package_mode_generates_config(self, mock_params, mock_auth, mock_pkg_name, mock_install, tmp_path):
        from pydantic import BaseModel, Field

        class TestAuth(BaseModel):
            api_key: str = Field(description="API key")

        mock_pkg_name.return_value = "airbyte-agent-gong"
        mock_auth.return_value = [TestAuth]
        mock_params.return_value = []

        output = tmp_path / "connector-gong-package.yaml"
        result = runner.invoke(cli, ["connectors", "configure", "--package", "airbyte-agent-gong", "-f", str(output)])
        assert result.exit_code == 0
        assert output.exists()
        content = output.read_text()
        assert "connector" in content

    @patch("airbyte_agent_mcp.cli.connector_commands.install_package")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_package_name")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_auth_config_types")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_additional_connector_params")
    def test_overwrite_flag(self, mock_params, mock_auth, mock_pkg_name, mock_install, tmp_path):
        from pydantic import BaseModel, Field

        class TestAuth(BaseModel):
            api_key: str = Field(description="API key")

        mock_pkg_name.return_value = "airbyte-agent-gong"
        mock_auth.return_value = [TestAuth]
        mock_params.return_value = []

        output = tmp_path / "config.yaml"
        output.write_text("old content")

        result = runner.invoke(cli, ["connectors", "configure", "--package", "airbyte-agent-gong", "-f", str(output)])
        assert result.exit_code == 1
        assert "already exists" in result.output

        result = runner.invoke(cli, ["connectors", "configure", "--package", "airbyte-agent-gong", "-f", str(output), "--overwrite"])
        assert result.exit_code == 0

    @patch("airbyte_agent_mcp.cli.connector_commands.install_package")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_package_name")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_auth_config_types")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_additional_connector_params")
    def test_auto_generated_filename(self, mock_params, mock_auth, mock_pkg_name, mock_install, tmp_path, monkeypatch):
        from pydantic import BaseModel, Field

        class TestAuth(BaseModel):
            api_key: str = Field(description="API key")

        mock_pkg_name.return_value = "airbyte-agent-gong"
        mock_auth.return_value = [TestAuth]
        mock_params.return_value = []

        monkeypatch.chdir(tmp_path)

        result = runner.invoke(cli, ["connectors", "configure", "--package", "airbyte-agent-gong"])
        assert result.exit_code == 0
        assert (tmp_path / "connector-gong-package.yaml").exists()

    @patch("airbyte_agent_mcp.cli.connector_commands.get_api")
    @patch("airbyte_agent_mcp.cli.connector_commands.registry_lookup")
    @patch("airbyte_agent_mcp.cli.connector_commands.get_cloud_auth_config_type")
    def test_cloud_mode(self, mock_cloud_auth, mock_registry, mock_api, tmp_path, monkeypatch):
        from pydantic import BaseModel, Field

        class CloudAuth(BaseModel):
            airbyte_client_id: str = Field(description="Client ID")
            airbyte_client_secret: str = Field(description="Client secret")

        mock_cloud_auth.return_value = CloudAuth
        mock_api.return_value.get_connector.return_value = {
            "source_template": {"source_definition_id": "abc-123"},
        }
        mock_registry.return_value = {
            "abc-123": {"connector_name": "gong"},
        }

        monkeypatch.chdir(tmp_path)

        result = runner.invoke(cli, ["connectors", "configure", "-c", "some-connector-id"])
        assert result.exit_code == 0
        assert (tmp_path / "connector-gong-cloud.yaml").exists()
