"""Tests for MCP CLI commands."""

from unittest.mock import ANY, MagicMock, patch

import typer
from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli

runner = CliRunner()


class TestMcpServe:
    def test_missing_config_file(self):
        result = runner.invoke(cli, ["mcp", "serve", "nonexistent.yaml"])
        assert result.exit_code == 1
        assert "Error" in result.output

    @patch("airbyte_agent_mcp.cli.mcp_commands.create_mcp_server")
    @patch("airbyte_agent_mcp.cli.mcp_commands.register_connectors")
    @patch("airbyte_agent_mcp.cli.mcp_commands.load_connectors")
    def test_serve_stdio(self, mock_load_connectors, mock_register_connectors, mock_create_mcp_server, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_connector.connector_version = "1.0.0"
        mock_load_connectors.return_value = [mock_connector]
        mock_mcp = MagicMock()
        mock_create_mcp_server.return_value = mock_mcp

        result = runner.invoke(cli, ["mcp", "serve", str(config_file)])
        assert result.exit_code == 0
        mock_register_connectors.assert_called_once_with(mock_mcp, [mock_connector], ANY)
        mock_mcp.run.assert_called_once_with(transport="stdio")

    @patch("airbyte_agent_mcp.cli.mcp_commands.create_mcp_server")
    @patch("airbyte_agent_mcp.cli.mcp_commands.register_connectors")
    @patch("airbyte_agent_mcp.cli.mcp_commands.load_connectors")
    def test_serve_http(self, mock_load_connectors, mock_register_connectors, mock_create_mcp_server, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_connector.connector_version = "1.0.0"
        mock_load_connectors.return_value = [mock_connector]
        mock_mcp = MagicMock()
        mock_create_mcp_server.return_value = mock_mcp

        result = runner.invoke(cli, ["mcp", "serve", str(config_file), "--transport", "http", "--port", "9000"])
        assert result.exit_code == 0
        mock_register_connectors.assert_called_once_with(mock_mcp, [mock_connector], ANY)
        mock_mcp.run.assert_called_once_with(transport="http", host="127.0.0.1", port=9000)

    @patch("airbyte_agent_mcp.cli.mcp_commands.load_connectors")
    def test_connector_load_error(self, mock_load_connectors, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_load_connectors.side_effect = typer.Exit(1)

        result = runner.invoke(cli, ["mcp", "serve", str(config_file)])
        assert result.exit_code == 1

    @patch("airbyte_agent_mcp.cli.mcp_commands.create_mcp_server")
    @patch("airbyte_agent_mcp.cli.mcp_commands.register_connectors")
    @patch("airbyte_agent_mcp.cli.mcp_commands.load_connectors")
    def test_serve_aggregate_registers_namespaced_tools(
        self,
        mock_load_connectors,
        mock_register_connectors,
        mock_create_mcp_server,
        tmp_path,
    ):
        config_file = tmp_path / "aggregate.yaml"
        config_file.write_text("configs:\n  - gong.yaml\n  - salesforce.yaml\n")

        gong = MagicMock()
        gong.connector_name = "gong"
        gong.connector_version = "1.0.0"

        salesforce = MagicMock()
        salesforce.connector_name = "salesforce"
        salesforce.connector_version = "1.0.0"

        mock_load_connectors.return_value = [gong, salesforce]
        mock_mcp = MagicMock()
        mock_create_mcp_server.return_value = mock_mcp

        result = runner.invoke(cli, ["mcp", "serve", str(config_file)])
        assert result.exit_code == 0
        mock_register_connectors.assert_called_once_with(mock_mcp, [gong, salesforce], ANY)
        mock_mcp.run.assert_called_once_with(transport="stdio")

    def test_shows_help(self):
        result = runner.invoke(cli, ["mcp", "--help"])
        assert result.exit_code == 0
        assert "serve" in result.output
