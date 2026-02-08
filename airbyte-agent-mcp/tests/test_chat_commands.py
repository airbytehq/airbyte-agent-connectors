"""Tests for chat CLI commands."""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli

runner = CliRunner()


class TestChat:
    def test_missing_config_file(self):
        result = runner.invoke(cli, ["chat", "nonexistent.yaml"])
        assert result.exit_code == 1
        assert "Error" in result.output

    @patch("airbyte_agent_mcp.cli.helpers.load_connector")
    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    @patch("airbyte_agent_mcp.cli.chat_commands.asyncio")
    def test_oneshot_mode(self, mock_asyncio, mock_config_load, mock_load_connector, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_connector.connector_version = "1.0.0"
        mock_load_connector.return_value = mock_connector

        result = runner.invoke(cli, ["chat", str(config_file), "What calls happened?"])
        assert result.exit_code == 0
        mock_asyncio.run.assert_called_once()

    @patch("airbyte_agent_mcp.cli.helpers.load_connector")
    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    @patch("airbyte_agent_mcp.cli.chat_commands.asyncio")
    def test_interactive_mode(self, mock_asyncio, mock_config_load, mock_load_connector, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_connector.connector_version = "1.0.0"
        mock_load_connector.return_value = mock_connector

        result = runner.invoke(cli, ["chat", str(config_file)])
        assert result.exit_code == 0
        mock_asyncio.run.assert_called_once()

    @patch("airbyte_agent_mcp.cli.helpers.load_connector")
    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    def test_connector_load_error(self, mock_config_load, mock_load_connector, tmp_path):
        from airbyte_agent_mcp.connector_utils import ConnectorLoadError

        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_load_connector.side_effect = ConnectorLoadError("Package not found")

        result = runner.invoke(cli, ["chat", str(config_file)])
        assert result.exit_code == 1
        assert "Connector load error" in result.output

    @patch("airbyte_agent_mcp.cli.helpers.ConnectorConfig.load")
    def test_config_value_error(self, mock_config_load, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("connector: test\n")

        mock_config_load.side_effect = ValueError("Invalid config format")

        result = runner.invoke(cli, ["chat", str(config_file)])
        assert result.exit_code == 1
        assert "Configuration error" in result.output
