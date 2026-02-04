"""Tests for register_commands helper functions."""

from unittest.mock import MagicMock, patch

import pytest

from airbyte_agent_mcp.cli.register_commands import _get_claude_desktop_config_path, _get_server_name


class TestGetClaudeDesktopConfigPath:
    def test_returns_a_path(self):
        path = _get_claude_desktop_config_path()
        assert path.name == "claude_desktop_config.json"
        assert "Claude" in str(path)


class TestGetServerName:
    def test_uses_explicit_name(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        assert _get_server_name(config_file, "custom-name") == "custom-name"

    @patch("airbyte_agent_mcp.cli.register_commands.ConnectorConfig.load")
    @patch("airbyte_agent_mcp.cli.register_commands.load_connector")
    def test_derives_from_connector(self, mock_load, mock_cfg_load, tmp_path):
        mock_connector = MagicMock()
        mock_connector.connector_name = "gong"
        mock_load.return_value = mock_connector
        config_file = tmp_path / "config.yaml"
        config_file.touch()
        assert _get_server_name(config_file, None) == "airbyte-gong"

    @patch("airbyte_agent_mcp.cli.register_commands.ConnectorConfig.load")
    @patch("airbyte_agent_mcp.cli.register_commands.load_connector")
    def test_derives_from_cloud_source(self, mock_load, mock_cfg_load, tmp_path):
        mock_connector = MagicMock()
        mock_connector.connector_name = "hubspot"
        mock_load.return_value = mock_connector
        config_file = tmp_path / "config.yaml"
        config_file.touch()
        assert _get_server_name(config_file, None) == "airbyte-hubspot"

    def test_raises_on_missing_config(self, tmp_path):
        config_file = tmp_path / "missing.yaml"
        with pytest.raises(FileNotFoundError, match="Config file not found"):
            _get_server_name(config_file, None)

    @patch("airbyte_agent_mcp.cli.register_commands.ConnectorConfig.load", side_effect=Exception("fail"))
    def test_raises_on_load_error(self, mock_cfg_load, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.touch()
        with pytest.raises(Exception, match="fail"):
            _get_server_name(config_file, None)

    @patch("airbyte_agent_mcp.cli.register_commands.ConnectorConfig.load")
    @patch("airbyte_agent_mcp.cli.register_commands.load_connector")
    def test_derives_from_local_path(self, mock_load, mock_cfg_load, tmp_path):
        mock_connector = MagicMock()
        mock_connector.connector_name = "zendesk-support"
        mock_load.return_value = mock_connector
        config_file = tmp_path / "config.yaml"
        config_file.touch()
        assert _get_server_name(config_file, None) == "airbyte-zendesk-support"
