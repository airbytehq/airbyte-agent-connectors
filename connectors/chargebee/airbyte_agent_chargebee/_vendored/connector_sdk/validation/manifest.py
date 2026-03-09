"""Shared utilities for fetching Airbyte connector manifests from GitHub."""

from typing import Any

import httpx
import yaml

# URL patterns for low-code connector manifests on GitHub.
# Connectors may store their manifest at different paths.
_MANIFEST_URL_PATTERNS = [
    "https://raw.githubusercontent.com/airbytehq/airbyte/refs/heads/master/airbyte-integrations/connectors/source-{name}/source_{name_underscore}/manifest.yaml",
    "https://raw.githubusercontent.com/airbytehq/airbyte/refs/heads/master/airbyte-integrations/connectors/source-{name}/manifest.yaml",
]


def fetch_manifest(connector_name: str) -> dict[str, Any] | None:
    """Fetch a low-code connector manifest from GitHub.

    Tries multiple URL patterns since connectors may store their manifest
    at different paths (e.g. ``source_asana/manifest.yaml`` vs ``manifest.yaml``).

    Returns the raw parsed YAML without resolving ``$ref`` references.

    Args:
        connector_name: Name of the connector (e.g., "gong", "hubspot", "asana")

    Returns:
        Parsed manifest dict, or None if not found
    """
    name = connector_name.lower().replace("_", "-").replace(" ", "-")
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


def resolve_ref(ref: str, root: dict[str, Any]) -> Any:
    """Resolve a single ``#/...`` JSON reference path against a root dict.

    Walks the path segments and returns whatever is found (dict, list, scalar),
    or an empty dict if any segment is missing.

    Args:
        ref: Reference string (e.g., ``"#/definitions/users"``, ``"#/schemas/calls"``)
        root: The root dict to resolve against

    Returns:
        The resolved value, or ``{}`` if the path cannot be followed
    """
    if not ref.startswith("#/"):
        return {}
    parts = ref[2:].split("/")
    current: Any = root
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return {}
    return current


def resolve_manifest_refs(obj: Any, root: dict[str, Any]) -> Any:
    """Recursively resolve ``$ref`` and string references in a manifest.

    Handles both:
    - Dict refs: ``{"$ref": "#/definitions/foo"}``
    - String refs: ``"#/definitions/foo"``

    Args:
        obj: The object to resolve (can be any YAML-parsed type)
        root: The root manifest dict for resolving references

    Returns:
        The fully-resolved object
    """
    if isinstance(obj, dict):
        if "$ref" in obj and len(obj) == 1:
            ref_path = obj["$ref"]
            if ref_path.startswith("#/"):
                resolved = resolve_ref(ref_path, root)
                return resolve_manifest_refs(resolved, root)
            return obj
        return {k: resolve_manifest_refs(v, root) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [resolve_manifest_refs(item, root) for item in obj]
    elif isinstance(obj, str) and obj.startswith("#/definitions/"):
        resolved = resolve_ref(obj, root)
        return resolve_manifest_refs(resolved, root)
    return obj


def fetch_manifest_resolved(connector_name: str) -> dict[str, Any] | None:
    """Fetch a connector manifest and recursively resolve all references.

    This is a convenience wrapper around :func:`fetch_manifest` +
    :func:`resolve_manifest_refs` for callers that need a fully-resolved manifest.

    Args:
        connector_name: Name of the connector (e.g., "gong", "hubspot")

    Returns:
        Fully-resolved manifest dict, or None if not found
    """
    manifest = fetch_manifest(connector_name)
    if manifest is None:
        return None
    return resolve_manifest_refs(manifest, manifest)
