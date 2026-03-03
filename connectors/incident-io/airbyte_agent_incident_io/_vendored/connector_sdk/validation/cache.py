"""
Validate x-airbyte-cache entities against the Airbyte source connector manifest.

Checks that each cache entity name corresponds to a real stream in the manifest,
and that cache field names exist as properties in the manifest stream schema.
"""

from pathlib import Path
from typing import Any

import httpx
import yaml

# URL patterns for low-code connector manifests on GitHub.
# Connectors may store their manifest at different paths.
_MANIFEST_URL_PATTERNS = [
    "https://raw.githubusercontent.com/airbytehq/airbyte/refs/heads/master/airbyte-integrations/connectors/source-{name}/source_{name_underscore}/manifest.yaml",
    "https://raw.githubusercontent.com/airbytehq/airbyte/refs/heads/master/airbyte-integrations/connectors/source-{name}/manifest.yaml",
]


def _fetch_manifest(connector_name: str) -> dict[str, Any] | None:
    """Fetch low-code manifest from GitHub.

    Tries multiple URL patterns since connectors may have different directory structures.

    Args:
        connector_name: Name of the connector (e.g., "gong", "hubspot")

    Returns:
        Parsed manifest dict, or None if not found
    """
    name = connector_name.lower().replace(" ", "-")
    name_underscore = name.replace("-", "_")

    for pattern in _MANIFEST_URL_PATTERNS:
        url = pattern.format(name=name, name_underscore=name_underscore)
        try:
            response = httpx.get(url, timeout=15.0)
            if response.status_code == 200:
                return yaml.safe_load(response.text)
        except (httpx.HTTPError, yaml.YAMLError):
            continue

    return None


def _resolve_reference(ref: str, definitions: dict[str, Any]) -> dict[str, Any]:
    """Resolve a ``#/definitions/...`` reference.

    Supports nested paths like ``#/definitions/streams/users``.
    """
    if ref.startswith("#/definitions/"):
        path = ref[len("#/definitions/") :]
        parts = path.split("/")
        current: Any = definitions
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return {}
        return current if isinstance(current, dict) else {}
    return {}


def _resolve_stream_schema(
    stream: dict[str, Any],
    definitions: dict[str, Any],
    schemas: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Extract the JSON schema from a stream definition.

    Handles InlineSchemaLoader with inline schemas, ``$ref`` to definitions,
    and ``#/schemas/name`` top-level references.
    """
    schemas = schemas or {}
    schema_loader = stream.get("schema_loader", {})

    if not isinstance(schema_loader, dict):
        return {}

    if "$ref" in schema_loader:
        resolved = _resolve_reference(schema_loader["$ref"], definitions)
        schema_loader = resolved if resolved else schema_loader

    if schema_loader.get("type") == "InlineSchemaLoader":
        schema = schema_loader.get("schema", {})
        if "$ref" in schema:
            ref = schema["$ref"]
            if ref.startswith("#/schemas/"):
                return schemas.get(ref[len("#/schemas/") :], {})
            return _resolve_reference(ref, definitions)
        return schema

    if "schema" in schema_loader:
        schema = schema_loader["schema"]
        if "$ref" in schema:
            ref = schema["$ref"]
            if ref.startswith("#/schemas/"):
                return schemas.get(ref[len("#/schemas/") :], {})
            return _resolve_reference(ref, definitions)
        return schema

    return {}


def _extract_manifest_streams(manifest: dict[str, Any]) -> dict[str, set[str]]:
    """Extract stream names and their schema property keys from a manifest.

    Handles both stream reference formats found in Airbyte manifests:
    - String refs: ``"#/definitions/users_stream"``
    - Dict refs: ``{"$ref": "#/definitions/streams/users"}``

    Args:
        manifest: Parsed manifest dict

    Returns:
        Dict mapping stream name to the set of property keys from its schema.
        Streams with empty/missing schemas map to an empty set.
    """
    definitions = manifest.get("definitions", {})
    top_schemas = manifest.get("schemas", {})
    result: dict[str, set[str]] = {}

    for stream_entry in manifest.get("streams", []):
        if isinstance(stream_entry, str):
            stream = _resolve_reference(stream_entry, definitions)
        elif isinstance(stream_entry, dict) and "$ref" in stream_entry:
            resolved = _resolve_reference(stream_entry["$ref"], definitions)
            stream = {**resolved, **{k: v for k, v in stream_entry.items() if k != "$ref"}}
        elif isinstance(stream_entry, dict):
            stream = stream_entry
        else:
            continue

        if not isinstance(stream, dict):
            continue

        name = stream.get("name") or stream.get("$parameters", {}).get("name")
        if not name:
            continue

        schema = _resolve_stream_schema(stream, definitions, top_schemas)
        result[name] = set(schema.get("properties", {}).keys())

    return result


def validate_cache_against_manifest(
    connector_yaml_path: str | Path,
    connector_def: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate that x-airbyte-cache entities match the Airbyte manifest.

    For each entity in x-airbyte-cache, checks:
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
    cache_entities: list[dict[str, Any]] = info.get("x-airbyte-cache", {}).get("entities", [])

    if not cache_entities:
        return {
            "errors": [],
            "warnings": ["No x-airbyte-cache entities found in connector.yaml — skipping cache validation"],
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

    manifest = _fetch_manifest(connector_name)
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

    errors: list[str] = []
    for entity in cache_entities:
        entity_name = entity.get("entity", "")
        if not entity_name:
            continue

        # x-airbyte-name maps the cache entity to a differently-named manifest stream
        manifest_name = entity.get("x-airbyte-name", entity_name)

        if manifest_name not in manifest_streams:
            if manifest_name != entity_name:
                errors.append(
                    f"Cache entity '{entity_name}' (x-airbyte-name: '{manifest_name}') "
                    f"does not exist as a stream in the manifest"
                )
            else:
                errors.append(f"Cache entity '{entity_name}' does not exist as a stream in the manifest")
            continue

        manifest_fields = manifest_streams[manifest_name]
        if not manifest_fields:
            continue

        cache_field_names = {f["name"] for f in entity.get("fields", [])}
        extra_fields = cache_field_names - manifest_fields
        if extra_fields:
            errors.append(f"Cache entity '{entity_name}' has fields not in the manifest: {sorted(extra_fields)}")

    return {
        "errors": errors,
        "warnings": [],
        "entities_checked": len(cache_entities),
        "manifest_streams": sorted(manifest_streams.keys()),
    }
