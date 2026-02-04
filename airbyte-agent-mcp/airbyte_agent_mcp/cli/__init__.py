from pathlib import Path
from typing import Annotated

import typer
from dotenv import load_dotenv

from ..models.cli_config import Config, set_config_dir
from .chat_commands import chat
from .cloud_commands import cloud_app
from .connector_commands import connectors_app
from .mcp_commands import mcp_app

# Load .env file from current directory
load_dotenv()

cli = typer.Typer(add_completion=False, no_args_is_help=True)


@cli.callback()
def main_callback(
    config_dir: Annotated[
        Path | None,
        typer.Option(
            "--config-dir",
            "-d",
            help="Config directory (default: ~/.airbyte_agent_mcp)",
            envvar="AIRBYTE_CONFIG_DIR",
        ),
    ] = None,
) -> None:
    """Airbyte Agent MCP CLI."""
    # Set global config directory if provided
    if config_dir:
        set_config_dir(config_dir)

    # Initialize config
    Config.load()


# Add commands and subcommand groups
cli.command("chat")(chat)
cli.add_typer(cloud_app, name="cloud")
cli.add_typer(connectors_app, name="connectors")
cli.add_typer(mcp_app, name="mcp")


if __name__ == "__main__":
    cli()
