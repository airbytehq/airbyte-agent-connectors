"""Chat CLI commands."""

import asyncio
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from ..mcp_server import create_mcp_server
from .helpers import load_connectors, register_connectors


def chat(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file (single or aggregate)"),
    ],
    prompt: Annotated[
        str | None,
        typer.Argument(help="Question to ask (omit for interactive mode)"),
    ] = None,
    model: Annotated[
        str,
        typer.Option("--model", "-m", help="Anthropic model to use"),
    ] = "claude-opus-4-6",
    quiet: Annotated[
        bool,
        typer.Option("--quiet", "-q", help="Only show the final answer (hide tool calls)"),
    ] = False,
) -> None:
    """Chat with connector data. Pass a prompt for one-shot mode, or omit it for interactive REPL."""
    console = Console(stderr=True)
    mcp = create_mcp_server()
    connectors = load_connectors(config, console)
    register_connectors(mcp, connectors, console)

    if prompt:
        from ..terminal_chat import run_ask

        asyncio.run(run_ask(connectors, mcp, prompt, model=model, quiet=quiet))
    else:
        from ..terminal_chat import run_chat

        asyncio.run(run_chat(connectors, mcp, model=model, quiet=quiet))
