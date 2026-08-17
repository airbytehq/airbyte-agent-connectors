"""
Validate x-airbyte-context-store entities against the Airbyte source connector manifest.

Checks that each cache entity name corresponds to a real stream in the manifest,
and that cache field names exist as properties in the manifest stream schema.
"""

from pathlib import Path
from typing import Any

import yaml

from airbyte_agent_sdk.validation.manifest import fetch_manifest_resolved


def _extract_stream_schema(stream: dict[str, Any]) -> dict[str, Any]:
    """Extract the JSON schema from a fully-resolved stream definition."""
    schema_loader = stream.get("schema_loader", {})

    if not isinstance(schema_loader, dict):
        return {}

    if schema_loader.get("type") == "InlineSchemaLoader":
        schema = schema_loader.get("schema", {})
        return schema if isinstance(schema, dict) else {}

    if "schema" in schema_loader:
        schema = schema_loader["schema"]
        return schema if isinstance(schema, dict) else {}

    return {}


def _extract_manifest_streams(manifest: dict[str, Any]) -> dict[str, set[str]]:
    """Extract stream names and their schema property keys from a resolved manifest.

    Args:
        manifest: Fully-resolved manifest dict (all ``$ref`` already expanded)

    Returns:
        Dict mapping stream name to the set of property keys from its schema.
        Streams with empty/missing schemas map to an empty set.
    """
    result: dict[str, set[str]] = {}

    def _process_stream(stream: dict[str, Any]) -> None:
        name = stream.get("name") or stream.get("$parameters", {}).get("name")
        if not name:
            return
        schema = _extract_stream_schema(stream)
        result[name] = set(schema.get("properties", {}).keys())

    for stream in manifest.get("streams", []):
        if not isinstance(stream, dict):
            continue

        if stream.get("type") == "ConditionalStreams":
            for nested in stream.get("streams", []):
                if isinstance(nested, dict):
                    _process_stream(nested)
            continue

        _process_stream(stream)

    return result


def _extract_direct_operation_entities(connector_def: dict[str, Any]) -> set[str]:
    """Return entities backed by direct API operations in the connector definition."""
    result: set[str] = set()
    paths = connector_def.get("paths", {})
    if not isinstance(paths, dict):
        return result

    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        for operation in path_item.values():
            if not isinstance(operation, dict):
                continue
            entity_name = operation.get("x-airbyte-entity")
            if isinstance(entity_name, str) and entity_name:
                result.add(entity_name)

    return result


def validate_cache_against_manifest(
    connector_yaml_path: str | Path,
    connector_def: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate that x-airbyte-context-store entities match the Airbyte manifest.

    For each entity in x-airbyte-context-store, checks:
    1. A stream with a matching name exists in the manifest.  If the entity has
       an ``x-airbyte-name`` field, that value is used for the manifest lookup;
       otherwise the ``entity`` name is used.
    2. Every field in the cache entity exists as a property in the manifest
       stream's schema (skipped when the manifest schema has no properties).

    Called from ``validate_connector_readiness()`` after basic validation passes.

    Args:
        connector_yaml_path: Path to connector.yaml
        connector_def: Pre-loaded raw spec dict (optional, loaded from file if not provided)

    Returns:
        Dict with ``errors``, ``warnings``, ``entities_checked``, and ``manifest_streams``.
    """
    connector_path = Path(connector_yaml_path)

    if connector_def is None:
        try:
            with open(connector_path) as f:
                connector_def = yaml.safe_load(f)
        except Exception as e:
            return {"errors": [f"Failed to load connector.yaml: {e}"], "warnings": []}

    info = connector_def.get("info", {})
    cache_entities: list[dict[str, Any]] = info.get("x-airbyte-context-store", {}).get("entities", [])

    if not cache_entities:
        return {
            "errors": [],
            "warnings": ["No x-airbyte-context-store entities found in connector.yaml — skipping cache validation"],
            "entities_checked": 0,
            "manifest_streams": [],
        }

    connector_name = info.get("x-airbyte-connector-name", "")
    if not connector_name:
        return {
            "errors": [],
            "warnings": ["No x-airbyte-connector-name found — skipping cache validation"],
            "entities_checked": 0,
            "manifest_streams": [],
        }

    manifest = fetch_manifest_resolved(connector_name)
    if manifest is None:
        return {
            "errors": [],
            "warnings": [
                f"Could not fetch manifest for '{connector_name}' from GitHub. "
                "This connector may not be a low-code connector — skipping cache validation."
            ],
            "entities_checked": 0,
            "manifest_streams": [],
        }

    manifest_streams = _extract_manifest_streams(manifest)

    if not manifest_streams:
        return {
            "errors": [],
            "warnings": [
                f"Manifest for '{connector_name}' has no extractable streams "
                "(may use dynamic_streams or another pattern) — skipping cache validation."
            ],
            "entities_checked": 0,
            "manifest_streams": [],
        }

    direct_operation_entities = _extract_direct_operation_entities(connector_def)

    errors: list[str] = []
    warnings: list[str] = []
    for entity in cache_entities:
        entity_name = entity.get("entity", "")
        if not entity_name:
            continue

        # x-airbyte-name maps the cache entity to a differently-named manifest stream
        manifest_name = entity.get("x-airbyte-name", entity_name)
        if manifest_name is None and entity.get("x-airbyte-skip-searchable-fields"):
            continue

        if manifest_name not in manifest_streams:
            skip_manifest_validation = entity.get("x-airbyte-skip-manifest-validation")
            if skip_manifest_validation is not None and not (isinstance(skip_manifest_validation, str) and skip_manifest_validation.strip()):
                errors.append(f"Cache entity '{entity_name}' has x-airbyte-skip-manifest-validation but the justification is empty")
                continue
            if isinstance(skip_manifest_validation, str) and skip_manifest_validation.strip() and entity_name in direct_operation_entities:
                warnings.append(
                    f"Cache entity '{entity_name}' is backed by a direct connector operation but "
                    "was not found in the replication manifest — skipping manifest cache validation: "
                    f"{skip_manifest_validation.strip()}"
                )
                continue
            if manifest_name != entity_name:
                errors.append(f"Cache entity '{entity_name}' (x-airbyte-name: '{manifest_name}') does not exist as a stream in the manifest")
            else:
                errors.append(f"Cache entity '{entity_name}' does not exist as a stream in the manifest")
            continue

        manifest_fields = manifest_streams[manifest_name]
        if not manifest_fields:
            continue

        cache_field_names = {f.get("x-airbyte-name", f["name"]) for f in entity.get("fields", [])}
        extra_fields = cache_field_names - manifest_fields
        if extra_fields:
            errors.append(f"Cache entity '{entity_name}' has fields not in the manifest: {sorted(extra_fields)}")

    return {
        "errors": errors,
        "warnings": warnings,
        "entities_checked": len(cache_entities),
        "manifest_streams": sorted(manifest_streams.keys()),
    }
