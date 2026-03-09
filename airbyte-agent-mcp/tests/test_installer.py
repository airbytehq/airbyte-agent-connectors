"""Tests for installer module."""

import importlib.metadata
import json
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from airbyte_agent_mcp.installer import (
    ConnectorInstallError,
    _find_package_by_source_url,
    _get_pip_command,
    get_package_name,
    install_package,
    is_git_url,
    is_local_path,
    is_package_installed,
    uninstall_package,
)


class TestIsLocalPath:
    def test_absolute_path(self):
        assert is_local_path("/path/to/connector") is True

    def test_relative_path_dot_slash(self):
        assert is_local_path("./my/connector") is True

    def test_relative_path_no_dot(self):
        assert is_local_path("myconnectors/gong") is True

    def test_home_path(self):
        assert is_local_path("~/connectors/gong") is True

    def test_parent_path(self):
        assert is_local_path("../other/connector") is True

    def test_pypi_name_not_path(self):
        assert is_local_path("airbyte-agent-gong") is False

    def test_pypi_name_with_version_not_path(self):
        assert is_local_path("airbyte-agent-gong==1.0.0") is False

    def test_git_url_not_path(self):
        assert is_local_path("git+https://github.com/org/repo.git") is False


class TestIsGitUrl:
    def test_git_https(self):
        assert is_git_url("git+https://github.com/org/repo.git") is True

    def test_git_with_branch(self):
        assert is_git_url("git+https://github.com/org/repo.git@main") is True

    def test_git_with_subdirectory(self):
        assert is_git_url("git+https://github.com/org/repo.git#subdirectory=pkg") is True

    def test_pypi_name_not_git(self):
        assert is_git_url("airbyte-agent-gong") is False

    def test_local_path_not_git(self):
        assert is_git_url("/path/to/connector") is False

    def test_https_url_without_git_prefix(self):
        assert is_git_url("https://github.com/org/repo.git") is False


class TestGetPipCommand:
    @patch("airbyte_agent_mcp.installer.is_executable_available", return_value=True)
    def test_uses_uv_when_available(self, _mock):
        assert _get_pip_command() == ["uv", "pip"]

    @patch("airbyte_agent_mcp.installer.is_executable_available", return_value=False)
    def test_falls_back_to_python_pip(self, _mock):
        cmd = _get_pip_command()
        assert cmd[1:] == ["-m", "pip"]


class TestGetPackageName:
    def test_pypi_name(self):
        assert get_package_name("airbyte-agent-gong") == "airbyte-agent-gong"

    def test_pypi_name_with_version(self):
        assert get_package_name("airbyte-agent-gong==1.0.0") == "airbyte-agent-gong"

    def test_local_path(self, tmp_path):
        pyproject = tmp_path / "pyproject.toml"
        pyproject.write_text('[project]\nname = "my-connector"\n')
        assert get_package_name(str(tmp_path)) == "my-connector"

    def test_local_path_missing_pyproject(self, tmp_path):
        with pytest.raises(ConnectorInstallError, match="pyproject.toml not found"):
            get_package_name(str(tmp_path / "nonexistent"))

    def test_git_url_found(self):
        mock_dist = MagicMock()
        mock_dist.read_text.return_value = json.dumps({"url": "https://github.com/org/repo.git"})
        mock_dist.metadata = {"Name": "my-connector"}

        with patch.object(importlib.metadata, "distributions", return_value=[mock_dist]):
            assert get_package_name("git+https://github.com/org/repo.git") == "my-connector"

    def test_git_url_not_found(self):
        with patch.object(importlib.metadata, "distributions", return_value=[]):
            with pytest.raises(ConnectorInstallError, match="Could not determine package name"):
                get_package_name("git+https://github.com/org/repo.git")


class TestInstallPackage:
    @patch("airbyte_agent_mcp.installer.subprocess.run")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    def test_installs_pypi_package(self, _pip, mock_run):
        install_package("airbyte-agent-gong")
        args = mock_run.call_args[0][0]
        assert args == ["uv", "pip", "install", "airbyte-agent-gong"]

    @patch("airbyte_agent_mcp.installer.subprocess.run")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    def test_installs_with_version(self, _pip, mock_run):
        install_package("airbyte-agent-gong==1.0.0")
        args = mock_run.call_args[0][0]
        assert args == ["uv", "pip", "install", "airbyte-agent-gong==1.0.0"]

    @patch("airbyte_agent_mcp.installer.subprocess.run")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    def test_installs_git_url(self, _pip, mock_run):
        install_package("git+https://github.com/org/repo.git@main")
        args = mock_run.call_args[0][0]
        assert args == ["uv", "pip", "install", "git+https://github.com/org/repo.git@main"]

    @patch("airbyte_agent_mcp.installer.subprocess.run")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    def test_installs_local_path_as_editable(self, _pip, mock_run, tmp_path):
        local_dir = tmp_path / "connector"
        local_dir.mkdir()
        install_package(str(local_dir))
        args = mock_run.call_args[0][0]
        assert "-e" in args
        assert str(local_dir) in args

    def test_raises_for_missing_local_path(self):
        with pytest.raises(ConnectorInstallError, match="does not exist"):
            install_package("/nonexistent/path")

    def test_raises_for_file_path(self, tmp_path):
        f = tmp_path / "file.txt"
        f.write_text("hi")
        with pytest.raises(ConnectorInstallError, match="not a directory"):
            install_package(str(f))

    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    @patch("airbyte_agent_mcp.installer.subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd", stderr="err"))
    def test_raises_on_failure(self, _run, _pip):
        with pytest.raises(ConnectorInstallError, match="Failed to install"):
            install_package("bad-package")

    @patch("site.main")
    @patch("importlib.invalidate_caches")
    @patch("airbyte_agent_mcp.installer.subprocess.run")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    def test_refreshes_import_caches_after_install(self, _pip, _run, mock_invalidate, mock_site_main):
        install_package("airbyte-agent-gong")
        mock_invalidate.assert_called_once()
        mock_site_main.assert_called_once()

    @patch("site.main")
    @patch("importlib.invalidate_caches")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    @patch("airbyte_agent_mcp.installer.subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd", stderr="err"))
    def test_does_not_refresh_caches_on_failure(self, _run, _pip, mock_invalidate, mock_site_main):
        with pytest.raises(ConnectorInstallError):
            install_package("bad-package")
        mock_invalidate.assert_not_called()
        mock_site_main.assert_not_called()


class TestFindPackageBySourceUrl:
    def test_finds_matching_package(self):
        mock_dist = MagicMock()
        mock_dist.read_text.return_value = json.dumps({"url": "https://github.com/org/repo.git", "vcs_info": {"vcs": "git"}})
        mock_dist.metadata = {"Name": "my-connector"}

        with patch.object(importlib.metadata, "distributions", return_value=[mock_dist]):
            result = _find_package_by_source_url("git+https://github.com/org/repo.git")
            assert result == "my-connector"

    def test_returns_none_when_no_match(self):
        mock_dist = MagicMock()
        mock_dist.read_text.return_value = json.dumps({"url": "https://other.com/pkg", "vcs_info": {"vcs": "git"}})
        mock_dist.metadata = {"Name": "other-package"}

        with patch.object(importlib.metadata, "distributions", return_value=[mock_dist]):
            result = _find_package_by_source_url("git+https://github.com/org/repo.git")
            assert result is None

    def test_returns_none_when_no_direct_url(self):
        mock_dist = MagicMock()
        mock_dist.read_text.return_value = None

        with patch.object(importlib.metadata, "distributions", return_value=[mock_dist]):
            result = _find_package_by_source_url("git+https://github.com/org/repo.git")
            assert result is None

    def test_returns_none_when_no_distributions(self):
        with patch.object(importlib.metadata, "distributions", return_value=[]):
            result = _find_package_by_source_url("git+https://github.com/org/repo.git")
            assert result is None

    def test_strips_git_plus_prefix_for_matching(self):
        mock_dist = MagicMock()
        mock_dist.read_text.return_value = json.dumps({"url": "https://github.com/org/repo.git"})
        mock_dist.metadata = {"Name": "my-connector"}

        with patch.object(importlib.metadata, "distributions", return_value=[mock_dist]):
            result = _find_package_by_source_url("git+https://github.com/org/repo.git@v1.0")
            assert result == "my-connector"


class TestUninstallPackage:
    @patch("airbyte_agent_mcp.installer.subprocess.run")
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    def test_uninstalls(self, _pip, mock_run):
        uninstall_package("airbyte-agent-gong")
        args = mock_run.call_args[0][0]
        assert args == ["uv", "pip", "uninstall", "-y", "airbyte-agent-gong"]

    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    @patch("airbyte_agent_mcp.installer.subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd", stderr="err"))
    def test_raises_on_failure(self, _run, _pip):
        with pytest.raises(ConnectorInstallError, match="Failed to uninstall"):
            uninstall_package("bad-package")


class TestIsPackageInstalled:
    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    @patch("airbyte_agent_mcp.installer.subprocess.run")
    def test_returns_true_when_installed(self, mock_run, _pip):
        mock_run.return_value.returncode = 0
        assert is_package_installed("airbyte-agent-gong") is True

    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    @patch("airbyte_agent_mcp.installer.subprocess.run")
    def test_returns_false_when_not_installed(self, mock_run, _pip):
        mock_run.return_value.returncode = 1
        assert is_package_installed("nonexistent") is False

    @patch("airbyte_agent_mcp.installer._get_pip_command", return_value=["uv", "pip"])
    @patch("airbyte_agent_mcp.installer.subprocess.run", side_effect=Exception("boom"))
    def test_returns_false_on_exception(self, _run, _pip):
        assert is_package_installed("anything") is False
