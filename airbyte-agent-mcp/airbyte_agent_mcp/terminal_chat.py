"""Terminal chat with Rich rendering of tool calls.

Supports two modes:
- One-shot: pass a prompt and get a single answer (for scripting / piping).
- Interactive REPL: omit the prompt to start a conversation loop.
"""

from __future__ import annotations

import json
import logging
import time
from typing import Any

from rich.console import Console
from rich.markup import escape

from .agent import AgentRunner, create_agent
from .mcp_server import register_connector_tools


def _format_arg_value(value: Any) -> str:
    """Format a single argument value for display."""
    if isinstance(value, str):
        return f'"{value}"'
    return json.dumps(value, separators=(",", ":"), default=str)


def _format_tool_args(args: dict[str, Any]) -> str:
    """Format tool arguments for terminal display.

    Example output::

        (entity: "calls", action: "list", params: {"limit":5})
    """
    parts = [f"{k}: {_format_arg_value(v)}" for k, v in args.items() if v is not None]
    if parts:
        return "(" + ", ".join(parts) + ")"
    return ""


class TerminalStreamConsumer:
    """Renders agent stream events to the terminal using Rich."""

    def __init__(self, *, quiet: bool = False) -> None:
        self._quiet = quiet
        self._stdout = Console()
        self._stderr = Console(stderr=True)
        self._pending_starts: dict[str, float] = {}

    async def on_tool_call_start(self, tool_name: str, args: dict[str, Any], tool_call_id: str) -> None:
        self._pending_starts[tool_call_id] = time.monotonic()
        if self._quiet:
            return
        self._stderr.print()
        desc = _format_tool_args(args)
        self._stderr.print(f"⏺ Tool Call - [bold]{escape(tool_name)}[/bold] {escape(desc)}")

    async def on_tool_call_end(self, tool_name: str, args: dict[str, Any], result: str, tool_call_id: str, *, is_error: bool) -> None:
        start = self._pending_starts.pop(tool_call_id, None)
        if not start or self._quiet:
            return
        elapsed = time.monotonic() - start
        if is_error:
            self._stderr.print(f"   [dim italic red]⎿  {escape(result)}[/dim italic red]")
        else:
            preview = result[:200] + "…" if len(result) > 200 else result
            preview = preview.replace("\n", " ")
            self._stderr.print(f"   [dim italic green]⎿  Success[/dim italic green] [dim italic]{escape(preview)}[/dim italic]")
        size = len(result.encode())
        if size >= 1_000_000:
            size_str = f"{size / 1_000_000:.1f} MB"
        elif size >= 1_000:
            size_str = f"{size / 1_000:.1f} KB"
        else:
            size_str = f"{size} B"
        self._stderr.print(f"   [dim italic]⎿  {elapsed:.1f}s · {size_str}[/dim italic]")

    async def on_intermediate_response(self, text: str) -> None:
        self._stderr.print()
        self._stderr.print(f"[dim]⏺ [/dim][dim italic]{escape(text)}[/dim italic]")

    async def on_final_response(self, text: str) -> None:
        self._stderr.print()
        self._stdout.print(text)

    async def on_error(self, error: str) -> None:
        self._stderr.print(f"\n[bold red]Error:[/bold red] {escape(error)}")


def _setup(connector: Any, model: str) -> tuple[AgentRunner, Console]:
    """Common setup for both one-shot and REPL modes."""
    register_connector_tools(connector)
    agent = create_agent(connector, model=model)
    logging.getLogger("fastmcp").setLevel(logging.CRITICAL)
    return AgentRunner(agent), Console(stderr=True)


async def run_ask(connector: Any, prompt: str, *, model: str = "claude-opus-4-20250514", quiet: bool = False) -> None:
    """Run a single prompt against the connector and stream the response.

    Tool call progress is rendered to stderr via Rich so that piping
    ``adp chat <config> "question" > out.md`` captures only the final answer.

    Args:
        connector: Instantiated connector object.
        prompt: The user's question.
        model: Anthropic model identifier.
        quiet: If True, suppress tool call display.
    """
    runner, _ = _setup(connector, model)
    consumer = TerminalStreamConsumer(quiet=quiet)
    async for _ in runner.run(prompt, consumer):
        pass


async def run_chat(connector: Any, *, model: str = "claude-opus-4-20250514", quiet: bool = False) -> None:
    """Run an interactive REPL session against the connector.

    Reads user input in a loop and streams responses. Conversation history
    is maintained across turns by the AgentRunner.

    Exit with Ctrl-C, Ctrl-D, or by typing ``exit`` / ``quit``.

    Args:
        connector: Instantiated connector object.
        model: Anthropic model identifier.
        quiet: If True, suppress tool call display.
    """
    runner, stderr = _setup(connector, model)
    consumer = TerminalStreamConsumer(quiet=quiet)

    stderr.print(f"[bold]Connected to {connector.connector_name} v{connector.connector_version}[/bold]")
    stderr.print("[dim]Type your question, or 'exit' to quit.[/dim]\n")

    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            stderr.print("\n[dim]Goodbye.[/dim]")
            break

        if not prompt:
            continue
        if prompt.lower() in ("exit", "quit"):
            stderr.print("[dim]Goodbye.[/dim]")
            break

        async for _ in runner.run(prompt, consumer):
            pass
        stderr.print()
