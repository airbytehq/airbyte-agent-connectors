"""CLI commands for managing organizations."""

from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from ..models.cli_config import Config, get_config_dir

orgs_app = typer.Typer(add_completion=False, no_args_is_help=True)


@orgs_app.command("list")
def orgs_list() -> None:
    """List all logged-in organizations."""
    console = Console()
    config_dir = get_config_dir()
    orgs_dir = config_dir / "orgs"

    if not orgs_dir.exists():
        console.print("No organizations logged in. Run [bold]adp login <org-id>[/bold] to get started.")
        return

    org_ids = sorted(d.name for d in orgs_dir.iterdir() if d.is_dir() and (d / ".env").exists())
    if not org_ids:
        console.print("No organizations logged in. Run [bold]adp login <org-id>[/bold] to get started.")
        return

    config = Config.load()
    default_org = config.default_organization_id

    table = Table(show_header=True)
    table.add_column("ID")
    table.add_column("Default")

    for org_id in org_ids:
        marker = "\u2713" if org_id == default_org else ""
        table.add_row(org_id, marker)

    console.print(table)


@orgs_app.command("default")
def orgs_default(
    org_id: Annotated[
        str | None,
        typer.Argument(help="Organization ID to set as default"),
    ] = None,
) -> None:
    """Show or set the default organization."""
    console = Console()
    config = Config.load()

    if org_id is None:
        if config.default_organization_id:
            console.print(f"Default organization: [bold]{config.default_organization_id}[/bold]")
        else:
            console.print("No default organization set. Run [bold]adp login <org-id>[/bold] to set one.")
        return

    config_dir = get_config_dir()
    org_env = config_dir / "orgs" / org_id / ".env"
    if not org_env.exists():
        console.print(f"[red]Organization {org_id} not found. Run [bold]adp login {org_id}[/bold] first.[/red]")
        raise typer.Exit(code=1)

    config.default_organization_id = org_id
    config.save()
    console.print(f"[green]Default organization set to {org_id}.[/green]")
