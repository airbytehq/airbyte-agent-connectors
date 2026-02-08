"""Shared CLI helper functions."""

from pathlib import Path

import typer
from rich.console import Console

from ..connector_utils import ConnectorLoadError, load_connector
from ..models.connector_config import ConnectorConfig


def load_connector_from_config(config: Path, console: Console):
    """Load a connector from a YAML config file.

    Handles FileNotFoundError, ConnectorLoadError, and ValueError
    by printing an error message and raising typer.Exit(1).
    """
    try:
        connector_config = ConnectorConfig.load(config)
        console.print(f"[dim]Loading connector from config: {config}[/dim]")
        connector = load_connector(connector_config)
        console.print(f"[green]\u2713[/green] Loaded connector: {connector.connector_name} v{connector.connector_version}")
        return connector
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None
    except ConnectorLoadError as e:
        console.print(f"[red]Connector load error: {e}[/red]")
        raise typer.Exit(1) from None
    except ValueError as e:
        console.print(f"[red]Configuration error: {e}[/red]")
        raise typer.Exit(1) from None
