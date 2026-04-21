"""
CLI for airbyte-agent-sdk tools.

Provides commands for code generation, testing, and other SDK utilities.
"""

import asyncio
import json
import traceback
from pathlib import Path

import click

from .codegen.generator import ConnectorGenerator
from .secrets import (
    SecretResolutionError,
)
from .testing.helpers import (
    load_secrets_from_env,
    record_cassette_operation,
    resolve_connector_path,
    resolve_test_directory,
)
from .testing.reporter import TestReporter
from .testing.runner import run_tests
from .testing.spec_loader import validate_test_spec_file
from .validation import validate_connector_readiness as validate_readiness_func
from .validation.overview import (
    diff_overviews,
    format_overview_as_markdown,
    get_base_overview,
    get_connector_overview,
)
from .validation.replication import annotate_replication_version


@click.group()
def cli():
    """Airbyte SDK command-line tools."""
    pass


@cli.command(name="generate-docs")
@click.argument("spec_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=True,
    help="Directory to write REFERENCE.md, AUTH.md, and README.md to",
)
def generate_docs(spec_path: Path, output: Path):
    """
    Generate REFERENCE.md, AUTH.md, and README.md for a connector spec.

    SPEC_PATH: Path to OpenAPI 3.0 YAML specification file (connector.yaml)

    Example:
        uv run airbyte-agent-sdk generate-docs ../integrations/stripe/connector.yaml --output /tmp/stripe-docs
    """
    click.echo(f"Generating docs from {spec_path}...")

    try:
        generator = ConnectorGenerator(spec_path)
        output.mkdir(parents=True, exist_ok=True)

        connector_name = generator.spec.info.x_airbyte_connector_name
        connector_version = generator.spec.info.version

        operations = generator._extract_operations()
        envelope_types = generator._generate_envelope_types(operations)
        auth_config = generator._extract_auth_config()

        generator._generate_docs(output, connector_name, connector_version, operations, envelope_types)
        generator._generate_auth_docs(output, connector_name, auth_config)
        generator._generate_readme(output, connector_name, connector_version, operations, auth_config)

        click.echo(f"✓ Generated REFERENCE.md, AUTH.md, and README.md at {output}")
    except Exception as e:
        click.echo(f"\n✗ Error generating docs: {e}", err=True)
        raise click.Abort()


@cli.command(name="generate-sdk")
@click.argument("spec_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=None,
    help="Unified package source dir (default: auto-detect)",
)
def generate_sdk(spec_path: Path, output: Path | None):
    """
    Generate a typed connector module into the SDK package.

    SPEC_PATH: Path to OpenAPI 3.0 YAML specification file (connector.yaml)

    Example:
        uv run airbyte-agent-sdk generate-sdk ../integrations/stripe/connector.yaml
    """
    if output is None:
        # Default: generate into airbyte_agent_sdk/ alongside this CLI
        output = Path(__file__).parent
        if not output.is_dir():
            raise click.ClickException("Could not auto-detect output dir. Use --output.")

    click.echo(f"Generating SDK module from {spec_path}...")

    try:
        generator = ConnectorGenerator(spec_path)
        generator.generate_sdk(output)
    except Exception as e:
        click.echo(f"\n✗ Error generating SDK module: {e}", err=True)
        raise click.Abort()


@cli.group()
def test():
    """Test connector operations."""
    pass


@test.command()
@click.argument("connector_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--test-dir",
    type=click.Path(exists=True, path_type=Path),
    help="Directory containing test specs (default: connector_path/tests/verified)",
)
@click.option(
    "--mode",
    type=click.Choice(["mock"]),
    default="mock",
    help="Test mode (Phase 1: mock only)",
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option(
    "--format",
    type=click.Choice(["console", "json", "html"]),
    default="console",
    help="Output format",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Output file for JSON/HTML format (default: stdout)",
)
@click.option(
    "--show-diffs",
    is_flag=True,
    help="Show detailed diffs for validation failures in console output",
)
def run(
    connector_path: Path,
    test_dir: Path,
    mode: str,
    verbose: bool,
    format: str,
    output: Path,
    show_diffs: bool,
):
    """
    Run connector tests.

    CONNECTOR_PATH: Path to connector.yaml or directory containing it

    Example:
        uv run airbyte-agent-sdk test run ../connectors/stripe/ --test-dir ../connectors/stripe/tests/cassettes --verbose
        uv run airbyte-agent-sdk test run projects/stripe-mcp/ --verbose
        uv run airbyte-agent-sdk test run projects/stripe-mcp/ --format=json --output=results.json
        uv run airbyte-agent-sdk test run projects/stripe-mcp/ --format=html --output=report.html
        uv run airbyte-agent-sdk test run projects/stripe-mcp/ --show-diffs --verbose
    """
    try:
        # Resolve connector path
        connector_file, connector_dir = resolve_connector_path(connector_path)

        # Resolve test directory
        test_dir_resolved = resolve_test_directory(connector_dir, test_dir, "tests/verified")

        # Load auth config from environment (all env vars for test mode)
        auth_config = load_secrets_from_env(use_all_env_vars=True)

        click.echo(f"Running tests for {connector_file}...")
        click.echo(f"Test directory: {test_dir_resolved}")
        click.echo(f"Mode: {mode}\n")

        # Run tests (using sync version for CLI)
        report = run_tests(
            connector_path=connector_file,
            test_dir=test_dir_resolved,
            auth_config=auth_config,
            verbose=verbose,
        )

        # Output results
        reporter = TestReporter(verbose=verbose, show_diffs=show_diffs)

        if format == "json":
            if output:
                reporter.report_json_file(report, str(output))
                click.echo(f"\n✓ Results written to {output}")
            else:
                reporter.report_json(report)
        elif format == "html":
            if output:
                reporter.report_html_file(report, str(output))
                click.echo(f"\n✓ HTML report written to {output}")
            else:
                reporter.report_html(report)
        else:
            reporter.report_console(report)

        # Exit with error code if tests failed
        if report.failed > 0 or report.errors > 0:
            raise click.Abort()

    except FileNotFoundError as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        if not isinstance(e, click.Abort):
            click.echo(f"\n✗ Error running tests: {e}", err=True)
        raise click.Abort()


@test.command()
@click.argument("spec_path", type=click.Path(exists=True, path_type=Path))
def validate_spec(spec_path: Path):
    """
    Validate a test specification file.

    SPEC_PATH: Path to YAML test specification file

    Example:
        uv run airbyte-agent-sdk test validate-spec tests/verified/customers_list.yaml
    """
    click.echo(f"Validating test spec: {spec_path}...")

    is_valid, error_message = validate_test_spec_file(spec_path)

    if is_valid:
        click.echo("✓ Test specification is valid")
    else:
        click.echo("✗ Test specification is invalid:", err=True)
        click.echo(f"  {error_message}", err=True)
        raise click.Abort()


@cli.group()
def cassette():
    """Record and generate cassette test specifications."""
    pass


@cassette.command()
@click.argument("connector_path", type=click.Path(exists=True, path_type=Path))
@click.option("--entity", required=True, help="Entity name (e.g., 'customers')")
@click.option("--action", required=True, help="Operation action (e.g., 'list', 'get')")
@click.option(
    "--params",
    help="Parameters as JSON string (e.g., '{\"limit\": 10}')",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    default="tests/cassettes",
    help="Output directory for cassette files",
)
@click.option(
    "--test-name",
    help="Custom test name (auto-generated if not provided)",
)
@click.option(
    "--description",
    help="Test description (auto-generated if not provided)",
)
@click.option(
    "--auth-config",
    required=True,
    help='Auth config as JSON (e.g., \'{"api_key": "${STRIPE_API_KEY"}\'). Follows x-airbyte-auth-config spec.',
)
@click.option(
    "--config",
    help='Config values as JSON string for server variable substitution (e.g., \'{"subdomain": "acme"}\')',
)
@click.option(
    "--auth-scheme",
    help='Auth scheme name for multi-auth connectors (e.g., "zendeskOAuth", "zendeskAPIToken")',
)
def record(
    connector_path: Path,
    entity: str,
    action: str,
    params: str,
    output: Path,
    test_name: str,
    description: str,
    auth_config: str,
    config: str,
    auth_scheme: str,
):
    """
    Record HTTP interactions and generate cassette test specifications.

    This command executes a connector operation with logging enabled,
    captures the HTTP requests/responses, and generates a YAML test
    specification (cassette) that can be used for testing.

    CONNECTOR_PATH: Path to connector.yaml or directory containing it

    Example:
        uv run airbyte-agent-sdk cassette record connectors/stripe/ \\
            --entity customers \\
            --action list \\
            --params '{"limit": 10}' \\
            --auth-config '{"api_key": "${STRIPE_API_KEY}"}' \\
            --output tests/cassettes

    Example with server variables (e.g., Zendesk):
        uv run airbyte-agent-sdk cassette record integrations/zendesk-support/ \\
            --entity articles \\
            --action list \\
            --secrets '{"client_id": "${ZENDESK_CLIENT_ID}", ...}' \\
            --config '{"subdomain": "d3v-airbyte"}'
    """
    try:
        # Resolve connector path
        connector_file, connector_dir = resolve_connector_path(connector_path)

        # Parse params if provided
        params_dict = {}
        if params:
            try:
                params_dict = json.loads(params)
            except json.JSONDecodeError as e:
                click.echo(f"✗ Error parsing params JSON: {e}", err=True)
                raise click.Abort()
        # Parse auth_config
        try:
            auth_config_dict = json.loads(auth_config)
        except json.JSONDecodeError as e:
            click.echo(f"✗ Error parsing auth-config JSON: {e}", err=True)

        # Parse config if provided (non-sensitive values for server variable substitution)
        config_dict = {}
        if config:
            try:
                config_dict = json.loads(config)
            except json.JSONDecodeError as e:
                click.echo(f"✗ Error parsing config JSON: {e}", err=True)
                raise click.Abort()

        # Load and resolve credentials from environment
        try:
            env_auth_config = load_secrets_from_env(secrets_mapping=auth_config_dict)
        except SecretResolutionError as e:
            click.echo(f"✗ Error resolving credentials: {e}", err=True)
            click.echo("  Ensure all referenced environment variables are set.", err=True)
            raise click.Abort()
        except ValueError as e:
            click.echo(f"✗ Error: {e}", err=True)
            raise click.Abort()

        click.echo(f"Recording cassette for {entity}.{action}...")
        click.echo(f"Connector: {connector_file}")
        click.echo(f"Params: {params_dict}")
        if config_dict:
            click.echo(f"Config: {config_dict}")
        click.echo()

        # Execute operation and record cassette
        async def do_record():
            return await record_cassette_operation(
                connector_file=connector_file,
                connector_dir=connector_dir,
                entity=entity,
                action=action,
                params=params_dict,
                auth_config=env_auth_config,
                config_values=config_dict,
                output_dir=Path(output),
                test_name=test_name,
                description=description,
                auth_config_mapping=auth_config_dict,
                auth_scheme=auth_scheme,
            )

        result = asyncio.run(do_record())

        if not result.success:
            click.echo(f"\n✗ Error recording cassette: {result.error}", err=True)
            if result.traceback:
                click.echo(result.traceback, err=True)
            raise click.Abort()

        click.echo("✓ Operation completed successfully")
        click.echo(f"✓ Logs saved to {result.log_file}")
        click.echo(f"✓ Found {len(result.http_requests)} logged request(s):")
        for log in result.http_requests:
            click.echo(f"  [{log['index']}] {log['method']} {log['path']} -> {log['status']}")
        click.echo(f"\n✓ Cassette saved to {result.cassette_file}")
        click.echo("\nNext steps:")
        click.echo(f"  1. Review the generated cassette: {result.cassette_file}")
        click.echo(f"  2. Validate: uv run airbyte-agent-sdk test validate-spec {result.cassette_file}")
        click.echo(f"  3. Run tests: uv run airbyte-agent-sdk test run {connector_file} --test-dir {output}")

    except FileNotFoundError as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        if not isinstance(e, click.Abort):
            click.echo(f"\n✗ Error recording cassette: {e}", err=True)
            traceback.print_exc()
        raise click.Abort()


@cli.group()
def validate():
    """Validate connector configurations and readiness."""
    pass


@validate.command()
@click.argument("connector_path", type=click.Path(exists=True, path_type=Path))
@click.option("--quiet", "-q", is_flag=True, help="Only show summary")
@click.option("--json-output", is_flag=True, help="Output JSON format")
def readiness(connector_path: Path, quiet: bool, json_output: bool):
    """
    Validate connector readiness for shipping.

    Checks that:
    - connector.yaml exists and is valid
    - All entity/action operations have corresponding cassettes
    - Response schemas match cassette responses
    - Detects undeclared fields (warnings)

    CONNECTOR_PATH: Path to connector directory

    Example:
        uv run airbyte-agent-sdk validate readiness integrations/stripe/
        uv run airbyte-agent-sdk validate readiness integrations/stripe/ --json-output
        uv run airbyte-agent-sdk validate readiness integrations/stripe/ --quiet
    """
    try:
        if not quiet:
            click.echo(f"Validating connector readiness: {connector_path}...")

        result = validate_readiness_func(connector_path)

        if json_output:
            click.echo(json.dumps(result, indent=2))
        else:
            if "error" in result:
                click.echo(f"✗ Error: {result['error']}", err=True)
                raise click.Abort()

            summary = result["summary"]
            connector_name = result["connector_name"]

            if not quiet:
                click.echo(f"\nConnector: {connector_name}")
                click.echo(f"Path: {result['connector_path']}\n")

                click.echo("Summary:")
                click.echo(f"  Total operations: {summary['total_operations']}")
                click.echo(f"  Operations with cassettes: {summary['operations_with_cassettes']}")
                click.echo(f"  Operations missing cassettes: {summary['operations_missing_cassettes']}")
                click.echo(f"  Total cassettes: {summary['total_cassettes']}")
                click.echo(f"  Cassettes valid: {summary['cassettes_valid']}")
                click.echo(f"  Cassettes invalid: {summary['cassettes_invalid']}")
                click.echo(f"  Total warnings: {summary['total_warnings']}")
                click.echo(f"  Total errors: {summary['total_errors']}")

                # Show replication validation summary
                replication = result.get("replication_validation", {})
                replication_errors = replication.get("errors", [])
                replication_warnings = replication.get("warnings", [])
                if replication.get("registry_found"):
                    click.echo(f"  Replication compatibility errors: {len(replication_errors)}")

                cache = result.get("cache_validation", {})
                cache_errs = cache.get("errors", [])
                click.echo(f"  Cache validation errors: {len(cache_errs)}")

                # Show replication errors and warnings in details section
                if replication_errors or replication_warnings:
                    click.echo("\nReplication Compatibility:")
                    for error in replication_errors:
                        click.echo(f"  ✗ {error}", err=True)
                    for warning in replication_warnings:
                        click.echo(f"  ⚠ {warning}")

                # Show cache validation errors and warnings
                cache_validation = result.get("cache_validation", {})
                cache_errors = cache_validation.get("errors", [])
                cache_warnings = cache_validation.get("warnings", [])
                if cache_errors or cache_warnings:
                    click.echo("\nCache Validation:")
                    for error in cache_errors:
                        click.echo(f"  ✗ {error}", err=True)
                    for warning in cache_warnings:
                        click.echo(f"  ⚠ {warning}")

                # Show auth scheme validation errors and warnings
                auth_scheme_validation = result.get("auth_scheme_validation", {})
                auth_errors = auth_scheme_validation.get("errors", [])
                auth_warnings = auth_scheme_validation.get("warnings", [])
                covered_schemes = auth_scheme_validation.get("covered_schemes", [])
                if auth_errors or auth_warnings:
                    click.echo("\nAuth Scheme Coverage:")
                    if covered_schemes:
                        click.echo(f"  ✓ Covered: {', '.join(covered_schemes)}")
                    for error in auth_errors:
                        click.echo(f"  ✗ {error}", err=True)
                    for warning in auth_warnings:
                        click.echo(f"  ⚠ {warning}")

                readiness_errors = result.get("readiness_errors", [])
                if readiness_errors:
                    click.echo("\nRelationship Coverage:", err=True)
                    for error in readiness_errors:
                        click.echo(f"  ✗ {error}", err=True)

                if result["validation_results"]:
                    click.echo("\nDetails:")
                    for val_result in result["validation_results"]:
                        entity = val_result["entity"]
                        action = val_result["action"]
                        cassettes_found = val_result["cassettes_found"]

                        if cassettes_found == 0:
                            click.echo(f"  ✗ {entity}.{action}: No cassettes found", err=True)
                        else:
                            has_errors = any(v.get("errors") for v in val_result.get("schema_validation", []))
                            has_warnings = any(v.get("warnings") for v in val_result.get("schema_validation", []))

                            if has_errors:
                                click.echo(
                                    f"  ✗ {entity}.{action}: {cassettes_found} cassette(s), validation failed",
                                    err=True,
                                )
                                for cassette_val in val_result.get("schema_validation", []):
                                    if cassette_val.get("errors"):
                                        click.echo(
                                            f"      {cassette_val['cassette']}:",
                                            err=True,
                                        )
                                        for error in cassette_val["errors"]:
                                            click.echo(f"        - {error}", err=True)
                            elif has_warnings and not quiet:
                                click.echo(f"  ⚠ {entity}.{action}: {cassettes_found} cassette(s), warnings")
                                for cassette_val in val_result.get("schema_validation", []):
                                    if cassette_val.get("warnings"):
                                        for warning in cassette_val["warnings"]:
                                            click.echo(f"      - {warning}")
                            else:
                                click.echo(f"  ✓ {entity}.{action}: {cassettes_found} cassette(s)")

            if result["success"]:
                if not quiet:
                    click.echo(f"\n✓ Connector {connector_name} is ready to ship")
            else:
                click.echo(f"\n✗ Connector {connector_name} validation failed", err=True)
                raise click.Abort()

    except FileNotFoundError as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        if not isinstance(e, click.Abort):
            click.echo(f"\n✗ Error validating connector: {e}", err=True)
        raise click.Abort()


@cli.group()
def annotate():
    """Annotate connector configurations with metadata."""
    pass


@annotate.command("replication-version")
@click.argument("connector_path", type=click.Path(exists=True, path_type=Path))
@click.option("--dry-run", is_flag=True, help="Show what would be changed without modifying files")
@click.option(
    "--version",
    "version_override",
    default=None,
    help="Use this version instead of fetching from registry",
)
def replication_version(connector_path: Path, dry_run: bool, version_override: str | None):
    """
    Annotate connector.yaml with replication version metadata.

    Fetches the current version of the Airbyte replication connector from the
    registry and adds x-airbyte-replication-version and x-airbyte-replication-compatibility
    fields to the info section.

    When called from CI after a connector publish, use --version to pass the
    known published version directly.

    CONNECTOR_PATH: Path to connector directory containing connector.yaml

    Example:
        uv run airbyte-agent-sdk annotate replication-version integrations/stripe/
        uv run airbyte-agent-sdk annotate replication-version integrations/stripe/ --version 5.2.0
    """
    config_file = connector_path / "connector.yaml"
    if not config_file.exists():
        click.echo(f"Error: connector.yaml not found in {connector_path}", err=True)
        raise click.Abort()

    result = annotate_replication_version(config_file, dry_run=dry_run, version_override=version_override)

    if result.get("error"):
        click.echo(f"Error: {result['error']}", err=True)
        raise click.Abort()

    if result.get("skipped"):
        click.echo(f"Skipped: {result['reason']}")
        return

    version = result["version"]
    compatibility = result["compatibility"]

    if dry_run:
        click.echo(f"Would annotate {config_file}:")
        click.echo(f"  x-airbyte-replication-version: {version}")
        click.echo(f"  x-airbyte-replication-compatibility: {compatibility}")
    else:
        click.echo(f"Annotated {config_file}:")
        click.echo(f"  x-airbyte-replication-version: {version}")
        click.echo(f"  x-airbyte-replication-compatibility: {compatibility}")


@cli.group()
def connector():
    """Connector inspection and reporting tools."""
    pass


@connector.command()
@click.argument("connector_path", type=click.Path(exists=True, path_type=Path))
@click.option("--json-output", is_flag=True, help="Output JSON format")
@click.option("--markdown", is_flag=True, help="Output GitHub-flavored markdown")
@click.option("--base-ref", default=None, help="Git ref to compare against (e.g. main, origin/main, a SHA)")
def overview(connector_path: Path, json_output: bool, markdown: bool, base_ref: str | None):
    """
    Generate a status overview of a connector for review.

    Shows entities, actions, exceptions, example questions, and
    readiness validation summary.

    CONNECTOR_PATH: Path to connector directory

    Example:
        uv run airbyte-agent-sdk connector overview integrations/stripe/
        uv run airbyte-agent-sdk connector overview integrations/stripe/ --markdown
        uv run airbyte-agent-sdk connector overview integrations/stripe/ --markdown --base-ref main
    """
    try:
        result = get_connector_overview(connector_path)

        diff = None
        if base_ref:
            base = get_base_overview(connector_path, base_ref)
            diff = diff_overviews(base, result)

        if json_output:
            output = {"overview": result}
            if diff is not None:
                output["diff"] = diff
            click.echo(json.dumps(output, indent=2))
            return

        if markdown:
            click.echo(format_overview_as_markdown(result, diff=diff))
            return

        if not result.get("success"):
            click.echo(f"Error: {result.get('error', 'Unknown error')}", err=True)
            raise click.Abort()

        name = result["connector_name"]
        click.echo(f"Connector: {name}\n")

        click.echo("Entities & Actions:")
        for entity in result.get("entities", []):
            actions_str = ", ".join(entity["actions"])
            cassettes = sum(entity["cassette_counts"].values())
            untested = f" (untested: {', '.join(entity['untested_actions'])})" if entity["untested_actions"] else ""
            click.echo(f"  {entity['name']}: {actions_str} [{cassettes} cassette(s)]{untested}")

        auth = result.get("auth_schemes", {})
        if auth.get("defined"):
            parts = []
            for scheme in auth["defined"]:
                if scheme in auth.get("untested", []):
                    parts.append(f"{scheme} (untested)")
                else:
                    parts.append(scheme)
            click.echo(f"\nAuth schemes: {', '.join(parts)}")

        exceptions = result.get("exceptions", {})
        if exceptions.get("total_count", 0) > 0:
            click.echo(f"\nExceptions ({exceptions['total_count']}):")
            if exceptions.get("skip_suggested_streams"):
                click.echo(f"  Skipped streams: {', '.join(exceptions['skip_suggested_streams'])}")
            if exceptions.get("skip_auth_methods"):
                click.echo(f"  Skipped auth: {', '.join(exceptions['skip_auth_methods'])}")
            if exceptions.get("untested_operations"):
                click.echo(f"  Untested ops: {', '.join(exceptions['untested_operations'])}")
            if exceptions.get("untested_auth_schemes"):
                click.echo(f"  Untested auth: {', '.join(exceptions['untested_auth_schemes'])}")

        questions = result.get("example_questions", {})
        counts = questions.get("counts", {})
        total_q = sum(counts.values())
        if total_q > 0:
            parts = []
            if counts.get("direct"):
                parts.append(f"{counts['direct']} direct")
            if counts.get("search"):
                parts.append(f"{counts['search']} search")
            if counts.get("unsupported"):
                parts.append(f"{counts['unsupported']} unsupported")
            click.echo(f"\nExample questions: {', '.join(parts)}")

        readiness = result.get("readiness", {})
        status = "PASS" if readiness.get("success") else "FAIL"
        warnings_count = len(readiness.get("warnings", []))
        errors_count = len(readiness.get("errors", []))
        click.echo(f"\nReadiness: {status} | {warnings_count} warnings | {errors_count} errors")

        for error in readiness.get("errors", []):
            click.echo(f"  Error: {error}", err=True)

    except Exception as e:
        if not isinstance(e, click.Abort):
            click.echo(f"\nError: {e}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    cli()
