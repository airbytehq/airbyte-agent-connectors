"""CLI commands for Airbyte Cloud resources."""

from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from ..airbyte_api import get_api, registry_lookup

cloud_app = typer.Typer(help="Manage Airbyte Cloud resources.", no_args_is_help=True)
customers_app = typer.Typer(help="Manage customers.", no_args_is_help=True)
connectors_cloud_app = typer.Typer(help="Manage cloud connectors.", no_args_is_help=True)

cloud_app.add_typer(customers_app, name="customers")
cloud_app.add_typer(connectors_cloud_app, name="connectors")


@customers_app.command("list")
def list_customers() -> None:
    """List available customers."""
    console = Console()
    api = get_api()

    with console.status("Fetching customers..."):
        customers = api.list_customers()

    if not customers:
        console.print("[yellow]No customers found.[/yellow]")
        raise typer.Exit(0)

    table = Table()
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")

    for c in customers:
        table.add_row(c.get("id", ""), c.get("name", ""))

    console.print(table)
    console.print(f"\n[dim]Total: {len(customers)} customers[/dim]")


@connectors_cloud_app.command("list")
def list_cloud_connectors(
    customer_id: Annotated[
        str,
        typer.Option("--customer-id", "-c", help="Customer ID", envvar="AIRBYTE_CUSTOMER_ID"),
    ],
) -> None:
    """List cloud connector sources for a customer."""
    console = Console()
    api = get_api()

    with console.status("Fetching cloud connectors..."):
        connectors = api.list_connector_sources(customer_id)
        registry = registry_lookup()

    if not connectors:
        console.print("[yellow]No cloud connectors found for this customer.[/yellow]")
        raise typer.Exit(0)

    table = Table()
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Connector", style="yellow")
    table.add_column("Package", style="dim")
    table.add_column("Created", style="dim")

    for connector in connectors:
        defn_id = connector.get("summarized_source_template", {}).get("actor_definition_id", "")
        reg = registry.get(defn_id, {})
        connector_name = reg.get("connector_name", "")
        package_name = f"airbyte-agent-{connector_name}" if connector_name else ""
        table.add_row(
            connector.get("id", ""),
            connector.get("name", ""),
            connector_name,
            package_name,
            connector.get("created_at", ""),
        )

    console.print(table)
    console.print(f"\n[dim]Total: {len(connectors)} connectors[/dim]")


@connectors_cloud_app.command("get")
def get_cloud_connector(
    connector_id: Annotated[
        str,
        typer.Argument(help="Connector ID"),
    ],
) -> None:
    """Get details for a cloud connector source."""
    console = Console()
    api = get_api()

    with console.status("Fetching connector details..."):
        connector = api.get_connector(connector_id)
        registry = registry_lookup()

    defn_id = connector.get("source_template", {}).get("source_definition_id", "")
    reg = registry.get(defn_id, {})
    connector_name = reg.get("connector_name", "")

    table = Table(show_header=False)
    table.add_column("Field", style="cyan")
    table.add_column("Value")

    if connector_name:
        table.add_row("connector_name", connector_name)
        table.add_row("package", f"airbyte-agent-{connector_name}")
        table.add_section()

    hidden_fields = {"source_template"}
    for key, value in connector.items():
        if key not in hidden_fields:
            table.add_row(key, str(value))

    console.print(table)
