"""Commands for registering the MCP server with AI coding tools."""

import json
import subprocess
import sys
from pathlib import Path
from typing import Annotated, Any, Literal

import typer
from rich.console import Console

from ..connector_utils import load_connector
from ..models.connector_config import ConnectorConfig
from ..shell_utils import find_executable


def _get_claude_desktop_config_path() -> Path:
    """Get the Claude Desktop config file path based on platform."""
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif sys.platform == "win32":
        return Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
    else:
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"


def _get_cursor_config_path(scope: str) -> Path:
    """Get the Cursor MCP config file path."""
    if scope == "project":
        return Path.cwd() / ".cursor" / "mcp.json"
    return Path.home() / ".cursor" / "mcp.json"


def _load_json_config(config_path: Path) -> dict[str, Any]:
    """Load a JSON config file or return empty structure."""
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {}


def _save_json_config(config_path: Path, config: dict[str, Any]) -> None:
    """Save a JSON config file, creating parent directories if needed."""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")


def _get_server_name(config: Path, name: str | None) -> str:
    """Resolve the MCP server name from a connector config.

    If *name* is provided it is returned as-is. Otherwise the connector is
    loaded to derive a name.

    Raises:
        FileNotFoundError: If the config file does not exist.
        Exception: Any error from loading the connector config or connector.
    """
    if name is not None:
        return name

    if not config.exists():
        raise FileNotFoundError(f"Config file not found: {config}")

    connector_config = ConnectorConfig.load(config)
    connector = load_connector(connector_config)
    return f"airbyte-{connector.connector_name}"


def _uv_serve_args(config: Path) -> list[str]:
    """Build the uv command args to run the MCP server."""
    config_absolute = config.resolve()
    config_dir = str(config_absolute.parent)
    return ["uv", "--directory", config_dir, "run", "adp", "mcp", "serve", str(config_absolute)]


def _add_to_json_config(
    config_path: Path,
    server_name: str,
    config: Path,
    target_name: str,
    console: Console,
) -> None:
    """Add an MCP server entry to a JSON config file (Claude Desktop, Cursor)."""
    try:
        app_config = _load_json_config(config_path)
    except json.JSONDecodeError as e:
        console.print(f"[red]Error parsing {target_name} config: {e}[/red]")
        raise typer.Exit(1) from None

    if "mcpServers" not in app_config:
        app_config["mcpServers"] = {}

    uv_args = _uv_serve_args(config)
    app_config["mcpServers"][server_name] = {
        "type": "stdio",
        "command": uv_args[0],
        "args": uv_args[1:],
    }

    try:
        _save_json_config(config_path, app_config)
        console.print(f"[green]✓[/green] Registered MCP server '[bold]{server_name}[/bold]' with {target_name}")
        console.print(f"[dim]Config updated: {config_path}[/dim]")
        console.print(f"[yellow]Note: Restart {target_name} for changes to take effect[/yellow]")
    except OSError as e:
        console.print(f"[red]Error saving {target_name} config: {e}[/red]")
        raise typer.Exit(1) from None


def _run_cli_add(cmd: list[str], server_name: str, target_name: str, console: Console) -> None:
    """Run a CLI command to register the MCP server (Claude Code, Codex)."""
    console.print(f"[dim]Running: {' '.join(cmd)}[/dim]")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout:
            console.print(result.stdout)
        console.print(f"[green]✓[/green] Registered MCP server '[bold]{server_name}[/bold]' with {target_name}")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error registering with {target_name}:[/red]")
        if e.stderr:
            console.print(e.stderr)
        raise typer.Exit(1) from None


register_app = typer.Typer(help="Register the MCP server with an AI coding tool", no_args_is_help=True)


@register_app.command("claude-code")
def claude_code(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    name: Annotated[
        str | None,
        typer.Option("--name", "-n", help="Name for the MCP server (default: airbyte-<connector>)"),
    ] = None,
    scope: Annotated[
        Literal["user", "project"],
        typer.Option("--scope", "-s", help="Configuration scope"),
    ] = "user",
) -> None:
    """Register this MCP server with Claude Code.

    Uses the 'claude mcp add' command to register the server.

    Examples:
        adp mcp add-to claude-code connector-config-gong.yaml
        adp mcp add-to claude-code connector-config-gong.yaml --name my-gong-server
        adp mcp add-to claude-code connector-config-gong.yaml --scope project
    """
    console = Console(stderr=True)

    claude_cmd = find_executable("claude")
    if claude_cmd is None:
        console.print("[red]Error: 'claude' CLI not found in PATH[/red]")
        raise typer.Exit(1) from None

    try:
        server_name = _get_server_name(config, name)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None

    subprocess.run([claude_cmd, "mcp", "remove", "--scope", scope, server_name], capture_output=True, text=True)

    _run_cli_add(
        [
            claude_cmd,
            "mcp",
            "add",
            "--transport",
            "stdio",
            "--scope",
            scope,
            server_name,
            "--",
            *_uv_serve_args(config),
        ],
        server_name,
        "Claude Code",
        console,
    )


@register_app.command("codex")
def codex(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    name: Annotated[
        str | None,
        typer.Option("--name", "-n", help="Name for the MCP server (default: airbyte-<connector>)"),
    ] = None,
) -> None:
    """Register this MCP server with OpenAI Codex CLI.

    Uses the 'codex mcp add' command to register the server.

    Examples:
        adp mcp add-to codex connector-config-gong.yaml
        adp mcp add-to codex connector-config-gong.yaml --name my-gong-server
    """
    console = Console(stderr=True)

    codex_cmd = find_executable("codex")
    if codex_cmd is None:
        console.print("[red]Error: 'codex' CLI not found in PATH[/red]")
        raise typer.Exit(1) from None

    try:
        server_name = _get_server_name(config, name)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None

    _run_cli_add(
        [
            codex_cmd,
            "mcp",
            "add",
            server_name,
            "--",
            *_uv_serve_args(config),
        ],
        server_name,
        "Codex",
        console,
    )


@register_app.command("claude-desktop")
def claude_desktop(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    name: Annotated[
        str | None,
        typer.Option("--name", "-n", help="Name for the MCP server (default: airbyte-<connector>)"),
    ] = None,
) -> None:
    """Register this MCP server with Claude Desktop.

    Modifies the Claude Desktop configuration file directly.

    Examples:
        adp mcp add-to claude-desktop connector-config-gong.yaml
        adp mcp add-to claude-desktop connector-config-gong.yaml --name my-gong-server
    """
    console = Console(stderr=True)
    try:
        server_name = _get_server_name(config, name)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None
    _add_to_json_config(
        _get_claude_desktop_config_path(),
        server_name,
        config,
        "Claude Desktop",
        console,
    )


@register_app.command("cursor")
def cursor(
    config: Annotated[
        Path,
        typer.Argument(help="Path to connector config YAML file"),
    ],
    name: Annotated[
        str | None,
        typer.Option("--name", "-n", help="Name for the MCP server (default: airbyte-<connector>)"),
    ] = None,
    scope: Annotated[
        Literal["user", "project"],
        typer.Option("--scope", "-s", help="Configuration scope"),
    ] = "user",
) -> None:
    """Register this MCP server with Cursor.

    Modifies the Cursor MCP configuration file directly.

    Examples:
        adp mcp add-to cursor connector-config-gong.yaml
        adp mcp add-to cursor connector-config-gong.yaml --name my-gong-server
        adp mcp add-to cursor connector-config-gong.yaml --scope project
    """
    console = Console(stderr=True)
    try:
        server_name = _get_server_name(config, name)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None
    scope_label = "project" if scope == "project" else "user"
    _add_to_json_config(
        _get_cursor_config_path(scope),
        server_name,
        config,
        f"Cursor ({scope_label})",
        console,
    )
