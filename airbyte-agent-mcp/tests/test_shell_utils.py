"""Tests for shell_utils module."""

from unittest.mock import patch

from airbyte_agent_mcp.shell_utils import find_executable, is_executable_available


class TestFindExecutable:
    @patch("airbyte_agent_mcp.shell_utils.shutil.which", return_value="/usr/bin/uv")
    def test_returns_path_when_found(self, _mock):
        assert find_executable("uv") == "/usr/bin/uv"

    @patch("airbyte_agent_mcp.shell_utils.shutil.which", return_value=None)
    def test_returns_none_when_not_found(self, _mock):
        assert find_executable("nonexistent") is None


class TestIsExecutableAvailable:
    @patch("airbyte_agent_mcp.shell_utils.find_executable", return_value="/usr/bin/uv")
    def test_true_when_found(self, _mock):
        assert is_executable_available("uv") is True

    @patch("airbyte_agent_mcp.shell_utils.find_executable", return_value=None)
    def test_false_when_not_found(self, _mock):
        assert is_executable_available("nonexistent") is False
