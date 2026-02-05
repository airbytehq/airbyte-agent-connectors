"""Tests for org CLI commands."""

from unittest.mock import patch

from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli
from airbyte_agent_mcp.models.cli_config import Config

runner = CliRunner()


def _setup_org(tmp_path, org_id):
    """Create an org directory with a .env file."""
    org_dir = tmp_path / "orgs" / org_id
    org_dir.mkdir(parents=True)
    (org_dir / ".env").write_text(f"AIRBYTE_ORGANIZATION_ID={org_id}\n")


def _setup_config(tmp_path, default_org=None):
    """Create a config.yaml with optional default org."""
    cfg = Config()
    cfg.default_organization_id = default_org
    cfg.save(tmp_path)


class TestOrgsList:
    def test_lists_logged_in_orgs(self, tmp_path):
        _setup_config(tmp_path, default_org="org-abc")
        _setup_org(tmp_path, "org-abc")
        _setup_org(tmp_path, "org-xyz")

        with patch("airbyte_agent_mcp.cli.org_commands.get_config_dir", return_value=tmp_path):
            with patch("airbyte_agent_mcp.cli.org_commands.Config.load", return_value=Config.load(tmp_path)):
                result = runner.invoke(cli, ["orgs", "list"])

        assert result.exit_code == 0
        assert "org-abc" in result.output
        assert "org-xyz" in result.output
        assert "\u2713" in result.output

    def test_empty_when_no_orgs(self, tmp_path):
        _setup_config(tmp_path)

        with patch("airbyte_agent_mcp.cli.org_commands.get_config_dir", return_value=tmp_path):
            result = runner.invoke(cli, ["orgs", "list"])

        assert result.exit_code == 0
        assert "No organizations logged in" in result.output

    def test_empty_when_orgs_dir_missing(self, tmp_path):
        _setup_config(tmp_path)

        with patch("airbyte_agent_mcp.cli.org_commands.get_config_dir", return_value=tmp_path):
            result = runner.invoke(cli, ["orgs", "list"])

        assert result.exit_code == 0
        assert "No organizations logged in" in result.output


class TestOrgsDefault:
    def test_shows_current_default(self, tmp_path):
        _setup_config(tmp_path, default_org="org-abc")

        with patch("airbyte_agent_mcp.cli.org_commands.Config.load", return_value=Config.load(tmp_path)):
            result = runner.invoke(cli, ["orgs", "default"])

        assert result.exit_code == 0
        assert "org-abc" in result.output

    def test_shows_message_when_no_default(self, tmp_path):
        _setup_config(tmp_path)

        with patch("airbyte_agent_mcp.cli.org_commands.Config.load", return_value=Config.load(tmp_path)):
            result = runner.invoke(cli, ["orgs", "default"])

        assert result.exit_code == 0
        assert "No default organization set" in result.output

    def test_sets_default(self, tmp_path):
        _setup_config(tmp_path)
        _setup_org(tmp_path, "org-abc")

        with (
            patch("airbyte_agent_mcp.cli.org_commands.get_config_dir", return_value=tmp_path),
            patch("airbyte_agent_mcp.cli.org_commands.Config.load", return_value=Config.load(tmp_path)),
            patch("airbyte_agent_mcp.cli.org_commands.Config.save"),
        ):
            result = runner.invoke(cli, ["orgs", "default", "org-abc"])

        assert result.exit_code == 0
        assert "Default organization set to org-abc" in result.output

    def test_rejects_unknown_org(self, tmp_path):
        _setup_config(tmp_path)

        with (
            patch("airbyte_agent_mcp.cli.org_commands.get_config_dir", return_value=tmp_path),
            patch("airbyte_agent_mcp.cli.org_commands.Config.load", return_value=Config.load(tmp_path)),
        ):
            result = runner.invoke(cli, ["orgs", "default", "org-unknown"])

        assert result.exit_code == 1
        assert "not found" in result.output
