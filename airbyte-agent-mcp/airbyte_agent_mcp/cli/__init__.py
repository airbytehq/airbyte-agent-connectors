from pathlib import Path
from typing import Annotated

import typer
from dotenv import load_dotenv

from ..models.cli_config import Config, get_org_env_path, set_config_dir
from .chat_commands import chat
from .cloud_commands import cloud_app
from .connector_commands import connectors_app
from .login_commands import login
from .mcp_commands import mcp_app
from .org_commands import orgs_app

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
    org: Annotated[
        str | None,
        typer.Option(
            "--org",
            help="Organization ID to use (overrides default)",
        ),
    ] = None,
) -> None:
    """Airbyte Agent MCP CLI."""
    if config_dir:
        set_config_dir(config_dir)

    config = Config.load()

    org_id = org or config.default_organization_id
    if org_id:
        load_dotenv(get_org_env_path(org_id))

    load_dotenv(override=True)


# Add commands and subcommand groups
cli.command("login")(login)
cli.command("chat")(chat)
cli.add_typer(cloud_app, name="cloud")
cli.add_typer(connectors_app, name="connectors")
cli.add_typer(mcp_app, name="mcp")
cli.add_typer(orgs_app, name="orgs")


if __name__ == "__main__":
    cli()
