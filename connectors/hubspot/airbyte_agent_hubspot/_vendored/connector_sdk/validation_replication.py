"""
Replication compatibility validation for Airbyte connectors.

Validates that connector.yaml replication mappings reference valid fields
in the Airbyte source connector's spec from the registry.
"""

from pathlib import Path
from typing import Any

import httpx
import yaml

REGISTRY_URL = "https://connectors.airbyte.com/files/metadata/airbyte/source-{name}/latest/cloud.json"


def fetch_airbyte_registry_metadata(connector_name: str) -> dict[str, Any] | None:
    """Fetch connector metadata from Airbyte cloud registry.

    Args:
        connector_name: Name from x-airbyte-connector-name (e.g., "zendesk-support", "github")

    Returns:
        Registry metadata dict or None if not found
    """
    url = REGISTRY_URL.format(name=connector_name)

    try:
        response = httpx.get(url, timeout=15.0)
        if response.status_code == 200:
            return response.json()
    except (httpx.HTTPError, ValueError):
        pass
    return None


def _get_available_paths_at_level(spec: dict[str, Any], prefix: str = "") -> list[str]:
    """Get list of available property paths at a given level in the spec.

    Used for helpful error messages showing what paths are available.
    """
    paths = []
    properties = spec.get("properties", {})

    for key in properties:
        full_path = f"{prefix}.{key}" if prefix else key
        paths.append(full_path)

    # Also check oneOf variants
    for one_of_item in spec.get("oneOf", []):
        for key in one_of_item.get("properties", {}):
            full_path = f"{prefix}.{key}" if prefix else key
            if full_path not in paths:
                paths.append(full_path)

    return sorted(paths)


def resolve_spec_path(spec: dict[str, Any], path: str) -> tuple[bool, str | None]:
    """Check if a dotted path resolves in the spec.

    Handles nested structures including:
    - Simple properties: "start_date" -> properties.start_date
    - Nested paths: "credentials.access_token" -> properties.credentials.*.properties.access_token
    - oneOf structures: Searches all oneOf variants

    Args:
        spec: The connectionSpecification from registry
        path: Dotted path like "credentials.access_token"

    Returns:
        (found: bool, error_detail: str | None)
    """
    if not path:
        return False, "Empty path"

    parts = path.split(".")
    current = spec

    for i, part in enumerate(parts):
        properties = current.get("properties", {})

        if part in properties:
            current = properties[part]
            continue

        # Check oneOf variants
        one_of = current.get("oneOf", [])
        found_in_one_of = False
        for variant in one_of:
            variant_props = variant.get("properties", {})
            if part in variant_props:
                current = variant_props[part]
                found_in_one_of = True
                break

        if found_in_one_of:
            continue

        # Not found - build helpful error message
        current_path = ".".join(parts[:i]) if i > 0 else "(root)"
        available = _get_available_paths_at_level(current, ".".join(parts[:i]) if i > 0 else "")
        available_str = ", ".join(available[:10]) if available else "(none)"
        if len(available) > 10:
            available_str += f", ... ({len(available) - 10} more)"

        return False, f"Path segment '{part}' not found at {current_path}. Available: {available_str}"

    return True, None


def validate_connector_id(
    connector_id: str,
    connector_name: str,
    registry_metadata: dict[str, Any] | None,
) -> tuple[bool, list[str], list[str], bool]:
    """Validate connector ID matches registry.

    Args:
        connector_id: The x-airbyte-connector-id from connector.yaml
        connector_name: The x-airbyte-connector-name from connector.yaml
        registry_metadata: Fetched registry metadata or None

    Returns:
        (is_valid, errors, warnings, skip_remaining_checks)
        - is_valid: True if no blocking errors
        - errors: List of error messages
        - warnings: List of warning messages
        - skip_remaining_checks: True if remaining replication checks should be skipped
    """
    errors = []
    warnings = []

    if registry_metadata is None:
        # Connector not in registry - warn but don't fail (could be new connector)
        warnings.append(f"Connector '{connector_name}' not found in Airbyte registry. " f"Skipping replication compatibility checks.")
        return True, errors, warnings, True  # Valid (no blocking error), but skip remaining checks

    registry_id = registry_metadata.get("sourceDefinitionId", "")

    if connector_id.lower() != registry_id.lower():
        errors.append(
            f"Connector ID mismatch: connector.yaml has '{connector_id}' but " f"Airbyte registry has '{registry_id}' for '{connector_name}'."
        )
        return False, errors, warnings, True  # Invalid, skip remaining checks

    return True, errors, warnings, False  # Valid, continue with checks


def validate_auth_key_mapping(
    auth_mappings: dict[str, str],
    spec: dict[str, Any],
    scheme_name: str,
) -> tuple[bool, list[str], list[str]]:
    """Validate replication_auth_key_mapping paths exist in spec.

    Args:
        auth_mappings: Dict like {"credentials.access_token": "access_token"}
        spec: connectionSpecification from registry
        scheme_name: Name of the security scheme (for error messages)

    Returns:
        (is_valid, errors, warnings)
    """
    errors = []
    warnings = []

    for source_path, _target_key in auth_mappings.items():
        found, error_detail = resolve_spec_path(spec, source_path)
        if not found:
            errors.append(f"replication_auth_key_mapping in '{scheme_name}': " f"path '{source_path}' not found in Airbyte spec. {error_detail}")

    return len(errors) == 0, errors, warnings


def validate_config_key_mapping(
    config_mappings: dict[str, str],
    spec: dict[str, Any],
) -> tuple[bool, list[str], list[str]]:
    """Validate replication_config_key_mapping targets exist in spec.

    Args:
        config_mappings: Dict like {"start_date": "start_date"}
        spec: connectionSpecification from registry

    Returns:
        (is_valid, errors, warnings)
    """
    errors = []
    warnings = []

    for _local_key, target_path in config_mappings.items():
        found, error_detail = resolve_spec_path(spec, target_path)
        if not found:
            errors.append(f"replication_config_key_mapping: target path '{target_path}' " f"not found in Airbyte spec. {error_detail}")

    return len(errors) == 0, errors, warnings


def validate_environment_mapping(
    env_mappings: dict[str, Any],
    spec: dict[str, Any],
) -> tuple[bool, list[str], list[str]]:
    """Validate x-airbyte-replication-environment-mapping targets exist.

    Handles both simple string mappings and transform dicts.

    Args:
        env_mappings: Dict like {"subdomain": "subdomain"} or
                      {"domain": {"source": "subdomain", "format": "..."}}
        spec: connectionSpecification from registry

    Returns:
        (is_valid, errors, warnings)
    """
    errors = []
    warnings = []

    for _env_key, mapping_value in env_mappings.items():
        # Extract the target path from the mapping
        if isinstance(mapping_value, str):
            target_path = mapping_value
        elif isinstance(mapping_value, dict):
            # Transform mapping - the target is still the key in the spec
            # For transforms like {"source": "subdomain", "format": "..."}, the target
            # is typically the same as the env_key or specified separately
            # The mapping maps to the spec field, not from it
            target_path = _env_key  # The env key maps to the same-named spec field
        else:
            warnings.append(f"x-airbyte-replication-environment-mapping: " f"unexpected mapping type for '{_env_key}': {type(mapping_value)}")
            continue

        found, error_detail = resolve_spec_path(spec, target_path)
        if not found:
            errors.append(f"x-airbyte-replication-environment-mapping: " f"target path '{target_path}' not found in Airbyte spec. {error_detail}")

    return len(errors) == 0, errors, warnings


def validate_suggested_streams_coverage(
    connector_entities: list[dict[str, str | None]],
    suggested_streams: list[str],
    skip_streams: list[str] | None = None,
) -> tuple[bool, list[str], list[str]]:
    """Check connector entities cover all suggested streams.

    Args:
        connector_entities: List of entity dicts with 'name' and optional 'stream_name'
                           (from x-airbyte-entity and x-airbyte-stream-name)
        suggested_streams: List of stream names from registry
        skip_streams: Optional list of stream names to skip validation for

    Returns:
        (is_valid, errors, warnings)
    """
    errors = []
    warnings = []
    skip_streams = skip_streams or []

    if not suggested_streams:
        # No suggested streams in registry - nothing to validate
        return True, errors, warnings

    # Build set of covered stream names from connector entities
    covered_streams: set[str] = set()
    for entity in connector_entities:
        entity_name = entity.get("name", "")
        if entity_name:
            covered_streams.add(entity_name)
        # x-airbyte-stream-name overrides entity name for stream matching
        stream_name = entity.get("stream_name")
        if stream_name:
            covered_streams.add(stream_name)

    # Check each suggested stream is covered (excluding skipped ones)
    missing_streams = []
    skipped_streams = []
    for stream in suggested_streams:
        if stream in skip_streams:
            skipped_streams.append(stream)
        elif stream not in covered_streams:
            missing_streams.append(stream)

    if skipped_streams:
        warnings.append(f"Skipped suggested streams (via x-airbyte-skip-suggested-streams): {', '.join(skipped_streams)}")

    if missing_streams:
        errors.append(
            f"Suggested streams not covered by connector entities: {', '.join(missing_streams)}. "
            f"Add entities with matching x-airbyte-entity names or x-airbyte-stream-name attributes, "
            f"or add to x-airbyte-skip-suggested-streams to skip."
        )

    return len(errors) == 0, errors, warnings


def _extract_auth_mappings_from_spec(raw_spec: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Extract all replication_auth_key_mapping from security schemes.

    Returns:
        Dict mapping scheme_name -> auth_mappings
    """
    result = {}
    security_schemes = raw_spec.get("components", {}).get("securitySchemes", {})

    for scheme_name, scheme_def in security_schemes.items():
        auth_config = scheme_def.get("x-airbyte-auth-config", {})
        auth_mappings = auth_config.get("replication_auth_key_mapping", {})
        if auth_mappings:
            result[scheme_name] = auth_mappings

    return result


def _extract_config_mappings_from_spec(raw_spec: dict[str, Any]) -> dict[str, str]:
    """Extract replication_config_key_mapping from info section."""
    replication_config = raw_spec.get("info", {}).get("x-airbyte-replication-config", {})
    return replication_config.get("replication_config_key_mapping", {})


def _extract_environment_mappings_from_spec(raw_spec: dict[str, Any]) -> dict[str, Any]:
    """Extract x-airbyte-replication-environment-mapping from servers."""
    servers = raw_spec.get("servers", [])
    result = {}

    for server in servers:
        env_mapping = server.get("x-airbyte-replication-environment-mapping", {})
        result.update(env_mapping)

    return result


def _extract_cache_entities_from_spec(raw_spec: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract x-airbyte-cache entities from info section."""
    cache_config = raw_spec.get("info", {}).get("x-airbyte-cache", {})
    return cache_config.get("entities", [])


def _extract_connector_entities_from_spec(raw_spec: dict[str, Any]) -> list[dict[str, str | None]]:
    """Extract entities from connector spec paths/operations.

    Entities are defined via x-airbyte-entity on operations. Each entity can have
    an optional x-airbyte-stream-name on its response schema that maps to the
    Airbyte stream name.

    Stream name resolution order:
    1. x-airbyte-stream-name on schema (explicit stream name)
    2. Schema name when x-airbyte-entity-name points to an entity (e.g., Account schema with x-airbyte-entity-name: accounts)
    3. Entity name itself (fallback)

    Returns:
        List of dicts with 'name' (entity name) and 'stream_name' (optional stream name)
    """
    entities: dict[str, str | None] = {}  # entity_name -> stream_name

    paths = raw_spec.get("paths", {})
    schemas = raw_spec.get("components", {}).get("schemas", {})

    # First pass: collect all entity names from operations
    for _path, path_item in paths.items():
        for method in ["get", "post", "put", "patch", "delete", "options", "head", "trace"]:
            operation = path_item.get(method) if isinstance(path_item, dict) else None
            if not operation:
                continue

            entity_name = operation.get("x-airbyte-entity")
            if entity_name and entity_name not in entities:
                entities[entity_name] = None

    # Second pass: look for x-airbyte-stream-name or x-airbyte-entity-name in schemas
    for schema_name, schema_def in schemas.items():
        if not isinstance(schema_def, dict):
            continue

        stream_name = schema_def.get("x-airbyte-stream-name")
        entity_name_attr = schema_def.get("x-airbyte-entity-name")

        if stream_name:
            # Explicit x-airbyte-stream-name takes precedence
            if entity_name_attr and entity_name_attr in entities:
                entities[entity_name_attr] = stream_name
            elif schema_name.lower() in entities:
                entities[schema_name.lower()] = stream_name
            else:
                for ent_name in entities:
                    if ent_name.lower() == schema_name.lower():
                        entities[ent_name] = stream_name
                        break
        elif entity_name_attr and entity_name_attr in entities:
            # No x-airbyte-stream-name, but x-airbyte-entity-name maps to an entity
            # Use schema name as the stream name (e.g., Account schema for accounts entity)
            if entities[entity_name_attr] is None:
                entities[entity_name_attr] = schema_name

    return [{"name": name, "stream_name": stream_name} for name, stream_name in entities.items()]


def _extract_skip_suggested_streams_from_spec(raw_spec: dict[str, Any]) -> list[str]:
    """Extract x-airbyte-skip-suggested-streams from info section."""
    return raw_spec.get("info", {}).get("x-airbyte-skip-suggested-streams", [])


def _extract_skip_auth_methods_from_spec(raw_spec: dict[str, Any]) -> list[str]:
    """Extract x-airbyte-skip-auth-methods from info section."""
    return raw_spec.get("info", {}).get("x-airbyte-skip-auth-methods", [])


# ============================================
# AUTH METHOD VALIDATION
# ============================================

MANIFEST_URL = "https://raw.githubusercontent.com/airbytehq/airbyte/refs/heads/master/airbyte-integrations/connectors/source-{name}/manifest.yaml"


def _resolve_manifest_refs(obj: Any, root: dict[str, Any]) -> Any:
    """Recursively resolve $ref and string references in a manifest.

    Handles both:
    - Dict refs: {"$ref": "#/definitions/foo"}
    - String refs: "#/definitions/foo"
    """
    if isinstance(obj, dict):
        if "$ref" in obj and len(obj) == 1:
            ref_path = obj["$ref"]
            if ref_path.startswith("#/"):
                parts = ref_path[2:].split("/")
                resolved = root
                for part in parts:
                    resolved = resolved.get(part, {})
                return _resolve_manifest_refs(resolved, root)
            return obj
        return {k: _resolve_manifest_refs(v, root) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_resolve_manifest_refs(item, root) for item in obj]
    elif isinstance(obj, str) and obj.startswith("#/definitions/"):
        parts = obj[2:].split("/")
        resolved = root
        for part in parts:
            resolved = resolved.get(part, {})
        return _resolve_manifest_refs(resolved, root)
    return obj


def fetch_airbyte_manifest(connector_name: str) -> dict[str, Any] | None:
    """Fetch connector manifest from Airbyte GitHub repo.

    Args:
        connector_name: Name like "gong" or "hubspot"

    Returns:
        Parsed manifest dict with refs resolved, or None if not found
    """
    name = connector_name.lower().replace("_", "-").replace(" ", "-")
    url = MANIFEST_URL.format(name=name)

    try:
        response = httpx.get(url, timeout=15.0)
        if response.status_code == 200:
            manifest = yaml.safe_load(response.text)
            # Resolve all refs
            return _resolve_manifest_refs(manifest, manifest)
    except (httpx.HTTPError, ValueError, yaml.YAMLError):
        pass
    return None


def _normalize_auth_type(auth_type: str) -> str:
    """Normalize auth type names to canonical form.

    Maps various naming conventions to: oauth2, bearer, basic, api_key
    """
    auth_type_lower = auth_type.lower()

    # OAuth variations
    if "oauth" in auth_type_lower:
        return "oauth2"

    # Bearer token variations
    if "bearer" in auth_type_lower or auth_type_lower == "bearerauth":
        return "bearer"

    # Basic auth variations
    if "basic" in auth_type_lower:
        return "basic"

    # API key variations
    if "api" in auth_type_lower and "key" in auth_type_lower:
        return "api_key"
    if auth_type_lower == "apikeyauthenticator":
        return "api_key"

    return auth_type_lower


def _extract_auth_types_from_manifest(manifest: dict[str, Any]) -> tuple[set[str], dict[str, str]]:
    """Extract auth types from a resolved Airbyte manifest.

    Looks for the authenticator used by the connector in:
    - definitions.base_requester.authenticator
    - definitions.retriever.requester.authenticator

    The manifest should already have $ref references resolved.

    Returns:
        Tuple of:
        - Set of normalized auth types (e.g., {"oauth2", "bearer"})
        - Dict mapping auth type to SelectiveAuthenticator option key for display
          (e.g., {"bearer": "Private App Credentials"})
    """
    auth_types: set[str] = set()
    auth_option_keys: dict[str, str] = {}  # Maps auth type -> SelectiveAuthenticator key

    defs = manifest.get("definitions", {})

    # Find the authenticator - could be in base_requester or retriever.requester
    authenticator = None

    if "base_requester" in defs:
        authenticator = defs["base_requester"].get("authenticator")

    if not authenticator and "retriever" in defs:
        requester = defs["retriever"].get("requester", {})
        authenticator = requester.get("authenticator")

    if authenticator:
        _extract_auth_from_authenticator(authenticator, auth_types, auth_option_keys, defs)

    return auth_types, auth_option_keys


def _extract_auth_from_authenticator(
    authenticator: dict[str, Any],
    auth_types: set[str],
    auth_option_keys: dict[str, str],
    defs: dict[str, Any],
    option_key: str | None = None,
) -> None:
    """Extract auth types from an authenticator definition.

    Handles:
    - Single authenticators (e.g., BearerAuthenticator, ApiKeyAuthenticator)
    - SelectiveAuthenticator with multiple options
    - $ref references to other definitions

    Args:
        authenticator: The authenticator definition
        auth_types: Set to add found auth types to
        auth_option_keys: Dict to add auth type -> SelectiveAuthenticator option key mappings
        defs: The definitions dict for resolving refs
        option_key: The SelectiveAuthenticator option key (e.g., "Private App Credentials")
    """
    # Handle $ref references that weren't fully resolved
    if "$ref" in authenticator and len(authenticator) == 1:
        ref_path = authenticator["$ref"]
        if ref_path.startswith("#/definitions/"):
            ref_name = ref_path.split("/")[-1]
            authenticator = defs.get(ref_name, {})

    auth_type = authenticator.get("type", "")

    if auth_type == "SelectiveAuthenticator":
        # Multiple auth options - extract from each, passing the option key
        authenticators = authenticator.get("authenticators", {})
        for key, auth_def in authenticators.items():
            if isinstance(auth_def, dict):
                _extract_auth_from_authenticator(auth_def, auth_types, auth_option_keys, defs, key)
            elif isinstance(auth_def, str) and auth_def.startswith("#/definitions/"):
                # String reference
                ref_name = auth_def.split("/")[-1]
                ref_def = defs.get(ref_name, {})
                if ref_def:
                    _extract_auth_from_authenticator(ref_def, auth_types, auth_option_keys, defs, key)
    elif auth_type:
        normalized = _normalize_auth_type(auth_type)
        auth_types.add(normalized)
        # Store the option key if provided and not already set
        if option_key and normalized not in auth_option_keys:
            auth_option_keys[normalized] = option_key


def _extract_auth_types_from_registry(registry_metadata: dict[str, Any]) -> set[str]:
    """Extract auth types from Airbyte registry metadata.

    Only extracts OAuth from the registry since it's the only reliable indicator.
    The registry's credential property names are ambiguous (e.g., "access_token"
    could be OAuth, bearer token, or API key depending on context).

    For non-OAuth auth types, use _extract_auth_types_from_manifest() which has
    explicit authenticator type declarations.
    """
    auth_types: set[str] = set()

    spec = registry_metadata.get("spec", {})

    # Check advanced_auth for OAuth - this is the only reliable indicator from registry
    advanced_auth = spec.get("advanced_auth", {})
    if advanced_auth.get("auth_flow_type") == "oauth2.0":
        auth_types.add("oauth2")

    return auth_types


def _extract_auth_types_from_connector(raw_spec: dict[str, Any]) -> set[str]:
    """Extract auth types from our connector.yaml.

    Looks at components.securitySchemes.
    """
    auth_types: set[str] = set()

    security_schemes = raw_spec.get("components", {}).get("securitySchemes", {})

    for _name, scheme in security_schemes.items():
        scheme_type = scheme.get("type", "")

        if scheme_type == "oauth2":
            auth_types.add("oauth2")
        elif scheme_type == "http":
            http_scheme = scheme.get("scheme", "").lower()
            if http_scheme == "bearer":
                auth_types.add("bearer")
            elif http_scheme == "basic":
                auth_types.add("basic")
        elif scheme_type == "apiKey":
            auth_types.add("api_key")

    return auth_types


def validate_auth_methods(
    raw_spec: dict[str, Any],
    connector_name: str,
    registry_metadata: dict[str, Any] | None,
) -> tuple[bool, list[str], list[str]]:
    """Validate that connector supports required auth methods.

    Strategy:
    1. If manifest exists, use it to get auth types (source of truth)
    2. If NO manifest, fall back to registry advanced_auth to detect OAuth only

    Args:
        raw_spec: Our connector.yaml as dict
        connector_name: Connector name for fetching manifest
        registry_metadata: Pre-fetched registry metadata

    Returns:
        (is_valid, errors, warnings)
    """
    errors: list[str] = []
    warnings: list[str] = []

    # Get our auth types
    our_auth_types = _extract_auth_types_from_connector(raw_spec)

    # Get skip list from connector spec (these are normalized auth types like "bearer", "oauth2")
    skip_auth_types = set(_extract_skip_auth_methods_from_spec(raw_spec))

    # Try to get auth types from manifest (source of truth)
    manifest = fetch_airbyte_manifest(connector_name)
    airbyte_auth_types: set[str] = set()
    auth_option_keys: dict[str, str] = {}  # Maps auth type to SelectiveAuthenticator option key

    if manifest:
        airbyte_auth_types, auth_option_keys = _extract_auth_types_from_manifest(manifest)
    elif registry_metadata:
        # No manifest - fall back to registry for OAuth detection only
        airbyte_auth_types = _extract_auth_types_from_registry(registry_metadata)

    # If we couldn't determine any Airbyte auth types, skip validation
    if not airbyte_auth_types:
        warnings.append(
            f"Could not determine Airbyte auth types for '{connector_name}' "
            f"(no manifest found and no OAuth in registry). Skipping auth validation."
        )
        return True, errors, warnings

    # Apply skip list and report
    skipped = airbyte_auth_types & skip_auth_types
    if skipped:
        skipped_formatted = []
        for auth_type in sorted(skipped):
            option_key = auth_option_keys.get(auth_type)
            if option_key:
                skipped_formatted.append(f'{auth_type} ("{option_key}")')
            else:
                skipped_formatted.append(auth_type)
        warnings.append(f"Skipped auth methods (via x-airbyte-skip-auth-methods): {', '.join(skipped_formatted)}")
        airbyte_auth_types = airbyte_auth_types - skip_auth_types

    # Compare auth types
    missing = airbyte_auth_types - our_auth_types
    extra = our_auth_types - airbyte_auth_types

    if missing:
        # Format missing auth types with option keys if available
        missing_formatted = []
        for auth_type in sorted(missing):
            option_key = auth_option_keys.get(auth_type)
            if option_key:
                missing_formatted.append(f'{auth_type} ("{option_key}")')
            else:
                missing_formatted.append(auth_type)

        errors.append(
            f"Missing auth methods: {', '.join(missing_formatted)}. "
            f"Our connector supports: {', '.join(sorted(our_auth_types)) if our_auth_types else '(none)'}. "
            f"Add the missing auth scheme to components.securitySchemes, or if this auth method "
            f"cannot be supported, add to info.x-airbyte-skip-auth-methods: [{', '.join(sorted(missing))}]"
        )

    if extra:
        warnings.append(
            f"Extra auth methods in our connector: {', '.join(sorted(extra))}. " f"These are not in Airbyte's connector but may still be valid."
        )

    return len(errors) == 0, errors, warnings


def validate_replication_compatibility(
    connector_yaml_path: str | Path,
    raw_spec: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate all replication compatibility aspects.

    Called from validate_connector_readiness() after basic validation passes.

    Args:
        connector_yaml_path: Path to connector.yaml
        raw_spec: Pre-loaded raw spec dict (optional, will load from file if not provided)

    Returns:
        {
            "registry_found": bool,
            "connector_id_matches": bool,
            "checks": [
                {"name": "connector_id", "status": "pass|warn|fail", "messages": [...]},
                {"name": "auth_key_mapping", ...},
                ...
            ],
            "errors": list[str],
            "warnings": list[str]
        }
    """
    connector_path = Path(connector_yaml_path)

    # Load raw spec if not provided
    if raw_spec is None:
        try:
            with open(connector_path) as f:
                raw_spec = yaml.safe_load(f)
        except Exception as e:
            return {
                "registry_found": False,
                "connector_id_matches": False,
                "checks": [],
                "errors": [f"Failed to load connector.yaml: {str(e)}"],
                "warnings": [],
            }

    # Extract connector info
    info = raw_spec.get("info", {})
    connector_id = info.get("x-airbyte-connector-id", "")
    connector_name = info.get("x-airbyte-connector-name", "")

    if not connector_id or not connector_name:
        return {
            "registry_found": False,
            "connector_id_matches": False,
            "checks": [],
            "errors": ["Missing x-airbyte-connector-id or x-airbyte-connector-name in connector.yaml"],
            "warnings": [],
        }

    # Fetch registry metadata
    registry_metadata = fetch_airbyte_registry_metadata(connector_name)

    all_errors: list[str] = []
    all_warnings: list[str] = []
    checks: list[dict[str, Any]] = []

    # Check 1: Connector ID validation
    id_valid, id_errors, id_warnings, skip_remaining = validate_connector_id(connector_id, connector_name, registry_metadata)
    all_errors.extend(id_errors)
    all_warnings.extend(id_warnings)

    # Determine status: pass if valid, warn if skipping (not found in registry), fail if ID mismatch
    if not id_valid:
        id_status = "fail"
    elif skip_remaining:
        id_status = "skip"  # Not in registry, but not an error
    else:
        id_status = "pass"

    checks.append(
        {
            "name": "connector_id",
            "status": id_status,
            "messages": id_errors + id_warnings,
        }
    )

    # If connector ID doesn't match or registry not found, skip remaining checks
    if skip_remaining:
        return {
            "registry_found": registry_metadata is not None,
            "connector_id_matches": id_valid and not skip_remaining,
            "checks": checks,
            "errors": all_errors,
            "warnings": all_warnings,
        }

    # Get the connection spec from registry
    connection_spec = registry_metadata.get("spec", {}).get("connectionSpecification", {})

    # Check 2: Auth key mappings
    auth_mappings_by_scheme = _extract_auth_mappings_from_spec(raw_spec)
    auth_valid = True
    auth_messages: list[str] = []

    for scheme_name, auth_mappings in auth_mappings_by_scheme.items():
        valid, errors, warnings = validate_auth_key_mapping(auth_mappings, connection_spec, scheme_name)
        if not valid:
            auth_valid = False
        auth_messages.extend(errors)
        auth_messages.extend(warnings)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    checks.append(
        {
            "name": "auth_key_mapping",
            "status": "pass" if auth_valid else "fail",
            "messages": auth_messages,
        }
    )

    # Check 3: Config key mappings
    config_mappings = _extract_config_mappings_from_spec(raw_spec)
    if config_mappings:
        config_valid, config_errors, config_warnings = validate_config_key_mapping(config_mappings, connection_spec)
        all_errors.extend(config_errors)
        all_warnings.extend(config_warnings)
        checks.append(
            {
                "name": "config_key_mapping",
                "status": "pass" if config_valid else "fail",
                "messages": config_errors + config_warnings,
            }
        )
    else:
        checks.append(
            {
                "name": "config_key_mapping",
                "status": "pass",
                "messages": ["No replication_config_key_mapping defined (skipped)"],
            }
        )

    # Check 4: Environment mappings
    env_mappings = _extract_environment_mappings_from_spec(raw_spec)
    if env_mappings:
        env_valid, env_errors, env_warnings = validate_environment_mapping(env_mappings, connection_spec)
        all_errors.extend(env_errors)
        all_warnings.extend(env_warnings)
        checks.append(
            {
                "name": "environment_mapping",
                "status": "pass" if env_valid else "fail",
                "messages": env_errors + env_warnings,
            }
        )
    else:
        checks.append(
            {
                "name": "environment_mapping",
                "status": "pass",
                "messages": ["No x-airbyte-replication-environment-mapping defined (skipped)"],
            }
        )

    # Check 5: Suggested streams coverage (based on entities, not cache)
    connector_entities = _extract_connector_entities_from_spec(raw_spec)
    suggested_streams = registry_metadata.get("suggestedStreams", {}).get("streams", [])
    skip_streams = _extract_skip_suggested_streams_from_spec(raw_spec)

    if connector_entities:
        streams_valid, streams_errors, streams_warnings = validate_suggested_streams_coverage(connector_entities, suggested_streams, skip_streams)
        all_errors.extend(streams_errors)
        all_warnings.extend(streams_warnings)
        checks.append(
            {
                "name": "suggested_streams_coverage",
                "status": "pass" if streams_valid else "fail",
                "messages": streams_errors + streams_warnings,
            }
        )
    elif suggested_streams:
        # No entities defined but there ARE suggested streams
        # Check if all suggested streams are in skip list
        non_skipped_streams = [s for s in suggested_streams if s not in skip_streams]
        skipped_streams = [s for s in suggested_streams if s in skip_streams]

        if non_skipped_streams:
            # Some suggested streams are not skipped - this is an error
            error_msg = (
                f"No entities defined, but Airbyte has {len(non_skipped_streams)} suggested streams: "
                f"{', '.join(non_skipped_streams)}. Add entities with matching x-airbyte-entity names, "
                f"or add to x-airbyte-skip-suggested-streams to skip."
            )
            all_errors.append(error_msg)
            messages = [error_msg]
            if skipped_streams:
                skip_msg = f"Skipped suggested streams (via x-airbyte-skip-suggested-streams): {', '.join(skipped_streams)}"
                all_warnings.append(skip_msg)
                messages.append(skip_msg)
            checks.append(
                {
                    "name": "suggested_streams_coverage",
                    "status": "fail",
                    "messages": messages,
                }
            )
        else:
            # All suggested streams are skipped - this is fine (with warning)
            skip_msg = f"All {len(skipped_streams)} suggested streams skipped via x-airbyte-skip-suggested-streams: {', '.join(skipped_streams)}"
            all_warnings.append(skip_msg)
            checks.append(
                {
                    "name": "suggested_streams_coverage",
                    "status": "pass",
                    "messages": [skip_msg],
                }
            )
    else:
        # No entities defined and no suggested streams - this is fine
        checks.append(
            {
                "name": "suggested_streams_coverage",
                "status": "pass",
                "messages": ["No entities defined, and no suggested streams in registry (skipped)"],
            }
        )

    # Check 6: Auth methods compatibility
    auth_valid, auth_errors, auth_warnings = validate_auth_methods(raw_spec, connector_name, registry_metadata)
    all_errors.extend(auth_errors)
    all_warnings.extend(auth_warnings)

    # Determine status: pass, warn (extra methods), or fail (missing methods)
    if not auth_valid:
        auth_status = "fail"
    elif auth_warnings:
        auth_status = "warn"
    else:
        auth_status = "pass"

    checks.append(
        {
            "name": "auth_methods",
            "status": auth_status,
            "messages": auth_errors + auth_warnings,
        }
    )

    return {
        "registry_found": True,
        "connector_id_matches": True,
        "checks": checks,
        "errors": all_errors,
        "warnings": all_warnings,
    }
