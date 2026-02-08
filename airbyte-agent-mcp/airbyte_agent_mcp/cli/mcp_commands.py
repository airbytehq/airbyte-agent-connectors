"""MCP CLI commands."""

from pathlib import Path
from typing import Annotated, Literal

import typer
from rich.console import Console

from ..mcp_server import mcp, register_connector_tools
from .helpers import load_connector_from_config
from .register_commands import register_app

mcp_app = typer.Typer(help="MCP server commands", no_args_is_help=True)
mcp_app.add_typer(register_app, name="add-to")


@mcp_app.command("serve")
def serve(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    transport: Annotated[
        Literal["stdio", "http"],
        typer.Option("--transport", "-t", help="Transport protocol"),
    ] = "stdio",
    host: Annotated[
        str,
        typer.Option("--host", "-h", help="Host to bind to (for http)"),
    ] = "127.0.0.1",
    port: Annotated[
        int,
        typer.Option("--port", "-p", help="Port to bind to (for http)"),
    ] = 8000,
) -> None:
    """Start the MCP server with a connector configuration."""
    console = Console(stderr=True)
    connector = load_connector_from_config(config, console)
    register_connector_tools(connector)

    if transport == "stdio":
        mcp.run(transport="stdio")
    elif transport == "http":
        mcp.run(transport="http", host=host, port=port)
