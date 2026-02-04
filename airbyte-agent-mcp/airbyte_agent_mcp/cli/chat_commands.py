"""Chat CLI commands."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from ..connector_utils import ConnectorLoadError, load_connector
from ..models.connector_config import ConnectorConfig


def _load_connector_from_config(config: Path, console: Console):
    """Load a connector from a config file, handling common errors."""
    try:
        connector_config = ConnectorConfig.load(config)
        console.print(f"[dim]Loading connector from config: {config}[/dim]")
        connector = load_connector(connector_config)
        console.print(f"[green]✓[/green] Loaded connector: {connector.connector_name} v{connector.connector_version}")
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


def chat(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    prompt: Annotated[
        str | None,
        typer.Argument(help="Question to ask (omit for interactive mode)"),
    ] = None,
    model: Annotated[
        str,
        typer.Option("--model", "-m", help="Anthropic model to use"),
    ] = "claude-opus-4-20250514",
    quiet: Annotated[
        bool,
        typer.Option("--quiet", "-q", help="Only show the final answer (hide tool calls)"),
    ] = False,
) -> None:
    """Chat with connector data. Pass a prompt for one-shot mode, or omit it for interactive REPL."""
    console = Console(stderr=True)
    connector = _load_connector_from_config(config, console)

    if prompt:
        from ..terminal_chat import run_ask

        asyncio.run(run_ask(connector, prompt, model=model, quiet=quiet))
    else:
        from ..terminal_chat import run_chat

        asyncio.run(run_chat(connector, model=model, quiet=quiet))
