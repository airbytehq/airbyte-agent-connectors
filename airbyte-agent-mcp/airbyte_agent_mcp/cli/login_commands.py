"""CLI command for saving Airbyte Cloud credentials."""

from typing import Annotated

import typer
from rich.console import Console

from ..models.cli_config import Config, get_org_env_path


def login(
    organization_id: Annotated[
        str,
        typer.Argument(help="Airbyte Organization ID"),
    ],
) -> None:
    """Save Airbyte Cloud credentials to the global config directory."""
    console = Console()

    url = f"https://app.airbyte.ai/organizations/{organization_id}/authentication-module"
    console.print(f"You can find your Client ID and Secret at:\n[link={url}]{url}[/link]\n")

    client_id = typer.prompt("Airbyte Client ID")
    client_secret = typer.prompt("Airbyte Client Secret", hide_input=True)

    env_file = get_org_env_path(organization_id)
    env_file.parent.mkdir(parents=True, exist_ok=True)

    env_file.write_text(f"AIRBYTE_CLIENT_ID={client_id}\nAIRBYTE_CLIENT_SECRET={client_secret}\nAIRBYTE_ORGANIZATION_ID={organization_id}\n")

    config = Config.load()
    config.default_organization_id = organization_id
    config.save()

    console.print(f"\n[green]Credentials saved to {env_file}[/green]")
    console.print(f"[green]Organization {organization_id} set as default.[/green]")
