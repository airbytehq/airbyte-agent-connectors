"""MCP CLI commands."""

from pathlib import Path
from typing import Annotated, Literal

import typer
from rich.console import Console

from ..mcp_server import create_mcp_server
from .helpers import load_connectors, register_connectors
from .register_commands import register_app

mcp_app = typer.Typer(help="MCP server commands", no_args_is_help=True)
mcp_app.add_typer(register_app, name="add-to")


@mcp_app.command("serve")
def serve(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file (single or aggregate)"),
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
    mcp = create_mcp_server()
    connectors = load_connectors(config, console)
    register_connectors(mcp, connectors, console)

    if transport == "stdio":
        mcp.run(transport="stdio")
    elif transport == "http":
        mcp.run(transport="http", host=host, port=port)
