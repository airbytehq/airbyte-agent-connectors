"""Tests for login CLI command."""

from unittest.mock import patch

from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli

runner = CliRunner()


def _invoke_login(tmp_path, org_id="my-org", input_text="my-id\nmy-secret\n"):
    with (
        patch("airbyte_agent_mcp.cli.login_commands.get_org_env_path", return_value=tmp_path / "orgs" / org_id / ".env"),
        patch("airbyte_agent_mcp.cli.login_commands.Config") as mock_config_cls,
    ):
        mock_config = mock_config_cls.load.return_value
        result = runner.invoke(cli, ["login", org_id], input=input_text)
    return result, mock_config


class TestLogin:
    def test_writes_env_file_to_org_dir(self, tmp_path):
        result, _ = _invoke_login(tmp_path)

        assert result.exit_code == 0
        env_file = tmp_path / "orgs" / "my-org" / ".env"
        assert env_file.exists()

        content = env_file.read_text()
        assert "AIRBYTE_CLIENT_ID=my-id" in content
        assert "AIRBYTE_CLIENT_SECRET=my-secret" in content
        assert "AIRBYTE_ORGANIZATION_ID=my-org" in content

    def test_sets_default_organization(self, tmp_path):
        _, mock_config = _invoke_login(tmp_path)

        assert mock_config.default_organization_id == "my-org"
        mock_config.save.assert_called_once()

    def test_prints_confirmation(self, tmp_path):
        result, _ = _invoke_login(tmp_path)

        assert result.exit_code == 0
        assert "Credentials saved" in result.output

    def test_prints_default_org_message(self, tmp_path):
        result, _ = _invoke_login(tmp_path)

        assert result.exit_code == 0
        assert "set as default" in result.output

    def test_shows_credentials_url(self, tmp_path):
        result, _ = _invoke_login(tmp_path, org_id="org-abc")

        assert result.exit_code == 0
        assert "https://app.airbyte.ai/organizations/org-abc/authentication-module" in result.output

    def test_overwrites_existing_file(self, tmp_path):
        org_dir = tmp_path / "orgs" / "my-org"
        org_dir.mkdir(parents=True)
        env_file = org_dir / ".env"
        env_file.write_text("AIRBYTE_CLIENT_ID=old-id\n")

        result, _ = _invoke_login(tmp_path, input_text="new-id\nnew-secret\n")

        assert result.exit_code == 0
        content = env_file.read_text()
        assert "AIRBYTE_CLIENT_ID=new-id" in content
        assert "old-id" not in content

    def test_creates_org_directory(self, tmp_path):
        nested = tmp_path / "sub" / "dir"
        with (
            patch("airbyte_agent_mcp.cli.login_commands.get_org_env_path", return_value=nested / "orgs" / "org-1" / ".env"),
            patch("airbyte_agent_mcp.cli.login_commands.Config"),
        ):
            result = runner.invoke(cli, ["login", "org-1"], input="id\nsecret\n")

        assert result.exit_code == 0
        assert (nested / "orgs" / "org-1" / ".env").exists()
