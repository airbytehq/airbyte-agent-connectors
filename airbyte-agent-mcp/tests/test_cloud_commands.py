"""Tests for cloud CLI commands."""

from unittest.mock import MagicMock, patch

import httpx
import pytest
from typer.testing import CliRunner

from airbyte_agent_mcp.cli.cloud_commands import cloud_app

runner = CliRunner()

_REGISTRY = [
    {"connector_definition_id": "def-gong", "connector_name": "gong", "latest_version": "0.1.14"},
    {"connector_definition_id": "def-sf", "connector_name": "salesforce", "latest_version": "0.2.0"},
]


@pytest.fixture(autouse=True)
def _env_vars(monkeypatch):
    """Set required env vars for all tests."""
    monkeypatch.setenv("AIRBYTE_CLIENT_ID", "test-id")
    monkeypatch.setenv("AIRBYTE_CLIENT_SECRET", "test-secret")


def _token_response():
    return {"access_token": "tok", "token_type": "bearer", "expires_in": 3600}


class TestListCustomers:
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_lists_customers(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(
            json=lambda: {"data": [{"id": "ws-1", "name": "Dev"}, {"id": "ws-2", "name": "Prod"}]},
            raise_for_status=lambda: None,
        )

        result = runner.invoke(cloud_app, ["customers", "list"])
        assert result.exit_code == 0
        assert "Dev" in result.output
        assert "Prod" in result.output
        assert "2 customers" in result.output

    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_empty_customers(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(
            json=lambda: {"data": []},
            raise_for_status=lambda: None,
        )

        result = runner.invoke(cloud_app, ["customers", "list"])
        assert result.exit_code == 0
        assert "No customers found" in result.output

    def test_missing_credentials(self, monkeypatch):
        monkeypatch.delenv("AIRBYTE_CLIENT_ID", raising=False)
        monkeypatch.delenv("AIRBYTE_CLIENT_SECRET", raising=False)

        result = runner.invoke(cloud_app, ["customers", "list"])
        assert result.exit_code == 1


class TestListCloudConnectors:
    @patch("airbyte_agent_mcp.cli.cloud_commands.registry_lookup", return_value={e["connector_definition_id"]: e for e in _REGISTRY})
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_lists_connectors(self, mock_get, mock_post, _mock_reg):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(
            json=lambda: {
                "data": [
                    {
                        "id": "c1",
                        "name": "My Gong",
                        "summarized_source_template": {"actor_definition_id": "def-gong"},
                        "created_at": "2024-01-01",
                    },
                    {
                        "id": "c2",
                        "name": "My Salesforce",
                        "summarized_source_template": {"actor_definition_id": "def-sf"},
                        "created_at": "2024-02-01",
                    },
                ]
            },
            raise_for_status=lambda: None,
        )

        result = runner.invoke(cloud_app, ["connectors", "list", "--customer-id", "ws-123"])
        assert result.exit_code == 0
        assert "My Gong" in result.output
        assert "My Salesforce" in result.output
        assert "gong" in result.output
        assert "airbyte-agent-gong" in result.output
        assert "salesforce" in result.output
        assert "airbyte-agent-salesforce" in result.output
        assert "2 connectors" in result.output

    @patch("airbyte_agent_mcp.cli.cloud_commands.registry_lookup", return_value={e["connector_definition_id"]: e for e in _REGISTRY})
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_empty_list(self, mock_get, mock_post, _mock_reg):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(
            json=lambda: {"data": []},
            raise_for_status=lambda: None,
        )

        result = runner.invoke(cloud_app, ["connectors", "list", "--customer-id", "ws-123"])
        assert result.exit_code == 0
        assert "No cloud connectors found" in result.output

    def test_missing_customer_id(self):
        result = runner.invoke(cloud_app, ["connectors", "list"])
        assert result.exit_code != 0

    @patch("airbyte_agent_mcp.cli.cloud_commands.registry_lookup", return_value={})
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_passes_customer_id_param(self, mock_get, mock_post, _mock_reg):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(
            json=lambda: {"data": []},
            raise_for_status=lambda: None,
        )

        runner.invoke(cloud_app, ["connectors", "list", "--customer-id", "ws-abc"])
        assert mock_get.call_args[1]["params"] == {"workspace_id": "ws-abc"}


class TestGetCloudConnector:
    @patch("airbyte_agent_mcp.cli.cloud_commands.registry_lookup", return_value={e["connector_definition_id"]: e for e in _REGISTRY})
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_gets_connector(self, mock_get, mock_post, _mock_reg):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(
            json=lambda: {
                "id": "c1",
                "name": "My Gong",
                "source_template": {"source_definition_id": "def-gong", "key": "val"},
            },
            raise_for_status=lambda: None,
        )

        result = runner.invoke(cloud_app, ["connectors", "get", "c1"])
        assert result.exit_code == 0
        assert "c1" in result.output
        assert "My Gong" in result.output
        assert "gong" in result.output
        assert "airbyte-agent-gong" in result.output
        assert "source_template" not in result.output

    def test_missing_connector_id(self):
        result = runner.invoke(cloud_app, ["connectors", "get"])
        assert result.exit_code != 0


class TestMissingCredentials:
    def test_list_missing_env_vars(self, monkeypatch):
        monkeypatch.delenv("AIRBYTE_CLIENT_ID", raising=False)
        monkeypatch.delenv("AIRBYTE_CLIENT_SECRET", raising=False)

        result = runner.invoke(cloud_app, ["connectors", "list", "--customer-id", "ws-123"])
        assert result.exit_code == 1

    def test_get_missing_env_vars(self, monkeypatch):
        monkeypatch.delenv("AIRBYTE_CLIENT_ID", raising=False)
        monkeypatch.delenv("AIRBYTE_CLIENT_SECRET", raising=False)

        result = runner.invoke(cloud_app, ["connectors", "get", "c1"])
        assert result.exit_code == 1
