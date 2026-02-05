"""CLI command implementations."""

import json
from pathlib import Path
from typing import Annotated

import typer
import yaml
from rich.console import Console
from rich.table import Table

from ..airbyte_api import fetch_registry, get_api, registry_lookup
from ..connector_utils import (
    get_additional_connector_params,
    get_auth_config_types,
    get_cloud_auth_config_type,
)
from ..installer import ConnectorInstallError, get_package_name, install_package, is_git_url, is_local_path
from ..models.connector_config import (
    ConnectorConfig,
    ConnectorSource,
    auth_config_to_env_template,
    connector_params_to_template,
)

_PACKAGE_PREFIXES = ("airbyte-agent-", "airbyte_agent_")


def _connector_name_from_package(package_name: str) -> str:
    """Derive a connector name from a package name.

    Strips the ``airbyte-agent-`` / ``airbyte_agent_`` prefix when present.
    """
    lower = package_name.lower()
    for prefix in _PACKAGE_PREFIXES:
        if lower.startswith(prefix):
            return package_name[len(prefix) :]
    return package_name


def _parse_git_url(spec: str) -> dict:
    """Parse a ``git+https://...`` spec into ConnectorSource fields.

    Handles ``git+<url>@<ref>#subdirectory=<subdir>``.
    """
    url = spec.removeprefix("git+")
    result: dict = {}

    if "#subdirectory=" in url:
        url, subdir = url.rsplit("#subdirectory=", 1)
        result["subdirectory"] = subdir

    if "@" in url:
        url, ref = url.rsplit("@", 1)
        result["ref"] = ref

    result["git"] = url
    return result


connectors_app = typer.Typer(help="Manage Airbyte agent connectors.", no_args_is_help=True)
internal_app = typer.Typer(help="Internal commands.", hidden=True)
connectors_app.add_typer(internal_app, name="internal")


@connectors_app.command("list")
def list_connectors(
    pattern: Annotated[
        str | None,
        typer.Option("--pattern", "-p", help="Filter connectors by name pattern (e.g., 'salesforce')"),
    ] = None,
) -> None:
    """List available Airbyte agent connectors."""
    console = Console()

    with console.status("Fetching connector registry..."):
        connectors = fetch_registry()

    if pattern:
        pattern_lower = pattern.lower()
        connectors = [c for c in connectors if pattern_lower in c.get("connector_name", "").lower()]

    if not connectors:
        console.print("[yellow]No connectors found matching the criteria.[/yellow]")
        raise typer.Exit(0)

    table = Table()
    table.add_column("Name", style="cyan")
    table.add_column("Package", style="dim")
    table.add_column("Version", style="yellow")
    table.add_column("ID", style="dim")

    for c in connectors:
        name = c.get("connector_name", "")
        table.add_row(
            name,
            f"airbyte-agent-{name}" if name else "",
            c.get("latest_version", ""),
            c.get("connector_definition_id", ""),
        )

    console.print(table)
    console.print(f"\n[dim]Total: {len(connectors)} connectors[/dim]")


@connectors_app.command("configure")
def configure_connector(
    connector_id: Annotated[str | None, typer.Option("--connector-id", help="Airbyte Cloud connector ID")] = None,
    package: Annotated[
        str | None,
        typer.Option("--package", help="Package to install: PyPI name, local path, or git+https:// URL"),
    ] = None,
    version: Annotated[str | None, typer.Option("--version", "-v", help="Package version (PyPI only)")] = None,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="Output file path (defaults to stdout)")] = None,
    overwrite: Annotated[bool, typer.Option("--overwrite", help="Overwrite output file if it already exists")] = False,
) -> None:
    """Configure a connector by installing it and generating a config."""
    console = Console(stderr=True)

    if not connector_id and not package:
        console.print("[red]Error: Must provide at least one of --connector-id or --package[/red]")
        raise typer.Exit(1)

    if version and not package:
        console.print("[red]Error: --version can only be used with --package[/red]")
        raise typer.Exit(1)

    if version and package and is_local_path(package):
        console.print("[red]Error: --version can only be used with PyPI packages[/red]")
        raise typer.Exit(1)

    # Check if output file already exists
    if output and output.exists() and not overwrite:
        console.print(f"[red]Error: Output file already exists: {output} (use --overwrite to replace)[/red]")
        raise typer.Exit(1)

    try:
        # Build the ConnectorSource
        source_kwargs: dict = {}

        if connector_id:
            source_kwargs["connector_id"] = connector_id

        if package:
            if is_local_path(package):
                source_kwargs["path"] = package
            elif is_git_url(package):
                source_kwargs.update(_parse_git_url(package))
            else:
                source_kwargs["package"] = package
                if version:
                    source_kwargs["version"] = version

        source = ConnectorSource(**source_kwargs)

        # Determine auth types and connector name
        if connector_id:
            api = get_api()
            connector_source = api.get_connector(connector_id)
            registry = registry_lookup()
            defn_id = connector_source.get("source_template", {}).get("source_definition_id", "")
            reg = registry.get(defn_id, {})
            connector_name = reg.get("connector_name", "unknown")
            auth_types = [get_cloud_auth_config_type()]
            additional_params: list = []
            console.print(f"[green]✓[/green] Cloud connector configured: {connector_name} ({connector_id})")
        elif package:
            spec = f"{package}=={version}" if version else package
            install_package(spec)
            package_name = get_package_name(spec)
            connector_name = _connector_name_from_package(package_name)
            auth_types = get_auth_config_types(package_name)
            additional_params = get_additional_connector_params(package_name)
            console.print("[green]✓[/green] Connector installed and configured")
        else:
            console.print("[red]Error: No valid source option provided[/red]")
            raise typer.Exit(1)

        # Create connector config with credentials and config templates
        # Cloud auth fields are global (AIRBYTE_CLIENT_ID), not connector-prefixed
        credentials = auth_config_to_env_template(auth_types[0], connector_name if not connector_id else None)
        config = connector_params_to_template(additional_params)
        connector_config = ConnectorConfig(connector=source, credentials=credentials, config=config)

        # Output config
        config_yaml = yaml.safe_dump(
            connector_config.to_dict(),
            default_flow_style=False,
            sort_keys=False,
        )

        # Add alternative auth methods as comments if there are multiple
        if len(auth_types) > 1:
            for auth_type in auth_types[1:]:
                template = auth_config_to_env_template(auth_type, connector_name)
                yaml_str = yaml.safe_dump({"credentials": template}, default_flow_style=False, sort_keys=False)
                lines = ["", "#", "# Connectors can have more than one way to auth.", "#"]
                for line in yaml_str.strip().split("\n"):
                    lines.append(f"# {line}")
                lines.extend(["#", ""])
                config_yaml += "\n".join(lines)

        if output:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(config_yaml)
            console.print(f"[green]✓[/green] Configuration saved to: {output}")
        else:
            print(config_yaml, end="")

    except ConnectorInstallError as e:
        console.print(f"[red]Installation error: {e}[/red]")
        raise typer.Exit(1) from None
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None


@internal_app.command("auth-schemas")
def auth_schemas(
    connector_id: Annotated[str | None, typer.Option("--connector-id", help="Airbyte Cloud connector ID")] = None,
    package: Annotated[
        str | None,
        typer.Option("--package", help="Package to install: PyPI name, local path, or git+https:// URL"),
    ] = None,
    version: Annotated[str | None, typer.Option("--version", "-v", help="Package version (PyPI only)")] = None,
) -> None:
    """Get the JSON schema for a connector's auth configuration."""
    console = Console(stderr=True)

    if not connector_id and not package:
        console.print("[red]Error: Must provide at least one of --connector-id or --package[/red]")
        raise typer.Exit(1)

    if version and not package:
        console.print("[red]Error: --version can only be used with --package[/red]")
        raise typer.Exit(1)

    try:
        if connector_id:
            auth_types = [get_cloud_auth_config_type()]
        elif package:
            spec = f"{package}=={version}" if version else package
            install_package(spec)
            pkg_name = get_package_name(spec)
            auth_types = get_auth_config_types(pkg_name)
        else:
            console.print("[red]Error: No valid source option provided[/red]")
            raise typer.Exit(1)

        schemas = [t.model_json_schema() for t in auth_types]
        print(json.dumps(schemas, indent=2))

    except ConnectorInstallError as e:
        console.print(f"[red]Installation error: {e}[/red]")
        raise typer.Exit(1) from None
    except ModuleNotFoundError as e:
        console.print(f"[red]Error: Package not found: {e}[/red]")
        raise typer.Exit(1) from None
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from None
