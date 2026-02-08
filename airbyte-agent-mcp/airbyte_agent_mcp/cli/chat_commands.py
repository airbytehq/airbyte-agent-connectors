"""Chat CLI commands."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from .helpers import load_connector_from_config


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
    connector = load_connector_from_config(config, console)

    if prompt:
        from ..terminal_chat import run_ask

        asyncio.run(run_ask(connector, prompt, model=model, quiet=quiet))
    else:
        from ..terminal_chat import run_chat

        asyncio.run(run_chat(connector, model=model, quiet=quiet))
