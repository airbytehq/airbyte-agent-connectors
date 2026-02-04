"""MCP CLI commands."""

from pathlib import Path
from typing import Annotated, Literal

import typer
from rich.console import Console

from ..connector_utils import ConnectorLoadError, load_connector
from ..mcp_server import mcp, register_connector_tools
from ..models.connector_config import ConnectorConfig
from .register_commands import register_app

mcp_app = typer.Typer(help="MCP server commands.", no_args_is_help=True)
mcp_app.add_typer(register_app, name="add-to")


@mcp_app.command("serve")
def serve(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    transport: Annotated[
        Literal["stdio", "http", "sse"],
        typer.Option("--transport", "-t", help="Transport protocol"),
    ] = "stdio",
    host: Annotated[
        str,
        typer.Option("--host", "-h", help="Host to bind to (for http/sse)"),
    ] = "127.0.0.1",
    port: Annotated[
        int,
        typer.Option("--port", "-p", help="Port to bind to (for http/sse)"),
    ] = 8000,
) -> None:
    """Start the MCP server with a connector configuration."""
    console = Console(stderr=True)

    try:
        connector_config = ConnectorConfig.load(config)
        console.print(f"[dim]Loading connector from config: {config}[/dim]")
        connector = load_connector(connector_config)
        console.print(f"[green]✓[/green] Loaded connector: {connector.connector_name} v{connector.connector_version}")
        register_connector_tools(connector)
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None
    except ConnectorLoadError as e:
        console.print(f"[red]Connector load error: {e}[/red]")
        raise typer.Exit(1) from None
    except ValueError as e:
        console.print(f"[red]Configuration error: {e}[/red]")
        raise typer.Exit(1) from None

    if transport == "stdio":
        mcp.run(transport="stdio")
    elif transport == "http":
        mcp.run(transport="http", host=host, port=port)
    elif transport == "sse":
        mcp.run(transport="sse", host=host, port=port)
