"""Shared test fixtures for CLI tests."""

from unittest.mock import MagicMock

import pytest
from typer.testing import CliRunner

from airbyte_agent_mcp.cli import cli


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def mock_connector():
    connector = MagicMock()
    connector.connector_name = "test-connector"
    connector.connector_version = "1.0.0"
    return connector


@pytest.fixture
def invoke(cli_runner):
    """Helper to invoke CLI commands."""

    def _invoke(*args, **kwargs):
        return cli_runner.invoke(cli, list(args), **kwargs)

    return _invoke
