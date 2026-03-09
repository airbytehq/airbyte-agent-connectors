"""Shared CLI helper functions."""

import re
from pathlib import Path
from typing import Any

import typer
from fastmcp import FastMCP
from pydantic import ValidationError
from rich.console import Console

from ..connector_utils import ConnectorLoadError, load_connector
from ..mcp_server import register_connector_tools
from ..models.connector_config import ConnectorConfig, resolve_connector_config


def _sanitize_tool_prefix(name: str) -> str:
    prefix = re.sub(r"[^a-zA-Z0-9_]+", "_", name.strip().lower()).strip("_")
    return prefix or "connector"


def build_tool_prefixes(connectors: list[Any]) -> list[str]:
    """Build deterministic unique tool prefixes from connector names."""
    prefixes: list[str] = []
    seen: dict[str, int] = {}

    for connector in connectors:
        base = _sanitize_tool_prefix(connector.connector_name)
        count = seen.get(base, 0) + 1
        seen[base] = count
        if count == 1:
            prefixes.append(base)
        else:
            prefixes.append(f"{base}_{count}")

    return prefixes


def load_connectors(config: Path, console: Console) -> list[Any]:
    """Load connectors from config, supporting single and aggregate files transparently."""
    try:
        config_paths = resolve_connector_config(config)
        connectors: list[Any] = []
        with console.status("Loading connector configuration...") as status:
            for idx, config_path in enumerate(config_paths, start=1):
                status.update(f"Loading connector {idx}/{len(config_paths)} from {config_path}...")
                connector_config = ConnectorConfig.load(config_path)
                connector = load_connector(connector_config)
                connectors.append(connector)

        summary = ", ".join(f"{c.connector_name} v{c.connector_version}" for c in connectors)
        console.print(f"[green]\u2713[/green] Loaded {len(connectors)} connectors: {summary}")
        return connectors
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None
    except ConnectorLoadError as e:
        console.print(f"[red]Connector load error: {e}[/red]")
        raise typer.Exit(1) from None
    except (ValidationError, ValueError) as e:
        console.print(f"[red]Configuration error: {e}[/red]")
        raise typer.Exit(1) from None


def register_connectors(mcp: FastMCP, connectors: list[Any], console: Console) -> None:
    """Register prefixed MCP tools for connectors with a shared progress UI."""
    prefixes = build_tool_prefixes(connectors)
    with console.status("Registering connector tools...") as status:
        for idx, (connector, prefix) in enumerate(zip(connectors, prefixes, strict=True), start=1):
            status.update(f"Registering tools {idx}/{len(connectors)} for {connector.connector_name}...")
            register_connector_tools(mcp, connector, tool_prefix=prefix)
