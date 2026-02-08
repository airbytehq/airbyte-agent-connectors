"""Tests for MCP CLI commands."""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli

runner = CliRunner()


class TestMcpServe:
    def test_missing_config_file(self):
        result = runner.invoke(cli, ["mcp", "serve", "nonexistent.yaml"])
        assert result.exit_code == 1
        assert "Error" in result.output

    @patch("airbyte_agent_mcp.cli.mcp_commands.mcp")
    @patch("airbyte_agent_mcp.cli.mcp_commands.register_connector_tools")
    @patch("airbyte_agent_mcp.cli.helpers.load_connector")
    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    def test_serve_stdio(self, mock_config_load, mock_load_connector, mock_register, mock_mcp, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_connector.connector_version = "1.0.0"
        mock_load_connector.return_value = mock_connector

        result = runner.invoke(cli, ["mcp", "serve", str(config_file)])
        assert result.exit_code == 0
        mock_register.assert_called_once_with(mock_connector)
        mock_mcp.run.assert_called_once_with(transport="stdio")

    @patch("airbyte_agent_mcp.cli.mcp_commands.mcp")
    @patch("airbyte_agent_mcp.cli.mcp_commands.register_connector_tools")
    @patch("airbyte_agent_mcp.cli.helpers.load_connector")
    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    def test_serve_http(self, mock_config_load, mock_load_connector, mock_register, mock_mcp, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_connector.connector_version = "1.0.0"
        mock_load_connector.return_value = mock_connector

        result = runner.invoke(cli, ["mcp", "serve", str(config_file), "--transport", "http", "--port", "9000"])
        assert result.exit_code == 0
        mock_mcp.run.assert_called_once_with(transport="http", host="127.0.0.1", port=9000)

    @patch("airbyte_agent_mcp.cli.helpers.load_connector")
    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    def test_connector_load_error(self, mock_config_load, mock_load_connector, tmp_path):
        from airbyte_agent_mcp.connector_utils import ConnectorLoadError

        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_load_connector.side_effect = ConnectorLoadError("Package not found")

        result = runner.invoke(cli, ["mcp", "serve", str(config_file)])
        assert result.exit_code == 1
        assert "Connector load error" in result.output

    def test_shows_help(self):
        result = runner.invoke(cli, ["mcp", "--help"])
        assert result.exit_code == 0
        assert "serve" in result.output
