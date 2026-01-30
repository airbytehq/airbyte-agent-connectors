"""
Shared introspection utilities for connector metadata.

This module provides utilities for introspecting connector metadata,
generating descriptions, and formatting parameter signatures. These
functions are used by both the runtime decorators and the generated
connector code.

The module is designed to work with any object conforming to the
ConnectorModel and EndpointDefinition interfaces from connector_sdk.types.
"""

from __future__ import annotations

from typing import Any, Protocol

# Constants
MAX_EXAMPLE_QUESTIONS = 5  # Maximum number of example questions to include in description


def _type_includes(type_value: Any, target: str) -> bool:
    if isinstance(type_value, list):
        return target in type_value
    return type_value == target


def _is_object_schema(schema: dict[str, Any]) -> bool:
    if "properties" in schema:
        return True
    return _type_includes(schema.get("type"), "object")


def _is_array_schema(schema: dict[str, Any]) -> bool:
    if "items" in schema:
        return True
    return _type_includes(schema.get("type"), "array")


def _dedupe_param_entries(entries: list[tuple[str, bool]]) -> list[tuple[str, bool]]:
    seen: dict[str, bool] = {}
    ordered: list[str] = []
    for name, required in entries:
        if name not in seen:
            seen[name] = required
            ordered.append(name)
        else:
            seen[name] = seen[name] or required
    return [(name, seen[name]) for name in ordered]


def _flatten_schema_params(
    schema: dict[str, Any],
    prefix: str = "",
    parent_required: bool = True,
    seen_stack: set[int] | None = None,
) -> list[tuple[str, bool]]:
    if not isinstance(schema, dict):
        return []

    if seen_stack is None:
        seen_stack = set()

    schema_id = id(schema)
    if schema_id in seen_stack:
        return []

    seen_stack.add(schema_id)
    try:
        entries: list[tuple[str, bool]] = []

        for subschema in schema.get("allOf", []) or []:
            if isinstance(subschema, dict):
                entries.extend(_flatten_schema_params(subschema, prefix, parent_required, seen_stack))

        for keyword in ("anyOf", "oneOf"):
            for subschema in schema.get(keyword, []) or []:
                if isinstance(subschema, dict):
                    entries.extend(_flatten_schema_params(subschema, prefix, False, seen_stack))

        properties = schema.get("properties")
        if isinstance(properties, dict):
            required_fields = set(schema.get("required", [])) if isinstance(schema.get("required"), list) else set()
            for prop_name, prop_schema in properties.items():
                path = f"{prefix}{prop_name}" if prefix else prop_name
                is_required = parent_required and prop_name in required_fields
                entries.append((path, is_required))

                if isinstance(prop_schema, dict):
                    if _is_array_schema(prop_schema):
                        array_path = f"{path}[]"
                        entries.append((array_path, is_required))
                        items = prop_schema.get("items")
                        if isinstance(items, dict):
                            entries.extend(_flatten_schema_params(items, prefix=f"{array_path}.", parent_required=is_required, seen_stack=seen_stack))
                    if _is_object_schema(prop_schema):
                        entries.extend(_flatten_schema_params(prop_schema, prefix=f"{path}.", parent_required=is_required, seen_stack=seen_stack))

        return _dedupe_param_entries(entries)
    finally:
        seen_stack.remove(schema_id)


def _cache_field_value(field: Any, key: str) -> Any:
    if isinstance(field, dict):
        return field.get(key)
    return getattr(field, key, None)


def _flatten_cache_properties(properties: dict[str, Any], prefix: str) -> list[str]:
    entries: list[str] = []
    for prop_name, prop in properties.items():
        path = f"{prefix}{prop_name}" if prefix else prop_name
        entries.append(path)

        prop_type = _cache_field_value(prop, "type")
        prop_properties = _cache_field_value(prop, "properties")

        if _type_includes(prop_type, "array"):
            array_path = f"{path}[]"
            entries.append(array_path)
            if isinstance(prop_properties, dict):
                entries.extend(_flatten_cache_properties(prop_properties, prefix=f"{array_path}."))
        elif isinstance(prop_properties, dict):
            entries.extend(_flatten_cache_properties(prop_properties, prefix=f"{path}."))

    return entries


def _flatten_cache_field_paths(field: Any) -> list[str]:
    field_name = _cache_field_value(field, "name")
    if not isinstance(field_name, str) or not field_name:
        return []

    field_type = _cache_field_value(field, "type")
    field_properties = _cache_field_value(field, "properties")

    entries = [field_name]
    if _type_includes(field_type, "array"):
        array_path = f"{field_name}[]"
        entries.append(array_path)
        if isinstance(field_properties, dict):
            entries.extend(_flatten_cache_properties(field_properties, prefix=f"{array_path}."))
    elif isinstance(field_properties, dict):
        entries.extend(_flatten_cache_properties(field_properties, prefix=f"{field_name}."))

    return entries


def _dedupe_strings(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def _collect_search_field_paths(model: ConnectorModelProtocol) -> dict[str, list[str]]:
    search_field_paths = getattr(model, "search_field_paths", None)
    if isinstance(search_field_paths, dict) and search_field_paths:
        normalized: dict[str, list[str]] = {}
        for entity, fields in search_field_paths.items():
            if not isinstance(entity, str) or not entity:
                continue
            if isinstance(fields, list):
                normalized[entity] = _dedupe_strings([field for field in fields if isinstance(field, str) and field])
        return normalized

    openapi_spec = getattr(model, "openapi_spec", None)
    info = getattr(openapi_spec, "info", None)
    cache_config = getattr(info, "x_airbyte_cache", None)
    entities = getattr(cache_config, "entities", None)
    if not isinstance(entities, list):
        return {}

    search_fields: dict[str, list[str]] = {}
    for entity in entities:
        entity_name = _cache_field_value(entity, "entity")
        if not isinstance(entity_name, str) or not entity_name:
            continue

        fields = _cache_field_value(entity, "fields") or []
        if not isinstance(fields, list):
            continue
        field_paths: list[str] = []
        for field in fields:
            field_paths.extend(_flatten_cache_field_paths(field))

        search_fields[entity_name] = _dedupe_strings(field_paths)

    return search_fields


def _format_search_param_signature() -> str:
    params = ["query*", "limit?", "cursor?", "fields?"]
    return f"({', '.join(params)})"


class EndpointProtocol(Protocol):
    """Protocol defining the expected interface for endpoint parameters.

    This allows functions to work with any endpoint-like object
    that has these attributes, including EndpointDefinition and mock objects.
    """

    path_params: list[str]
    path_params_schema: dict[str, dict[str, Any]]
    query_params: list[str]
    query_params_schema: dict[str, dict[str, Any]]
    body_fields: list[str]
    request_schema: dict[str, Any] | None


class EntityProtocol(Protocol):
    """Protocol defining the expected interface for entity definitions."""

    name: str
    actions: list[Any]
    endpoints: dict[Any, EndpointProtocol]


class ConnectorModelProtocol(Protocol):
    """Protocol defining the expected interface for connector model parameters.

    This allows functions to work with any connector-like object
    that has these attributes, including ConnectorModel and mock objects.
    """

    @property
    def entities(self) -> list[EntityProtocol]: ...

    @property
    def openapi_spec(self) -> Any: ...

    @property
    def search_field_paths(self) -> dict[str, list[str]] | None: ...


def format_param_signature(endpoint: EndpointProtocol) -> str:
    """Format parameter signature for an endpoint action.

    Returns a string like: (id*) or (limit?, starting_after?, email?)
    where * = required, ? = optional

    Args:
        endpoint: Object conforming to EndpointProtocol (e.g., EndpointDefinition)

    Returns:
        Formatted parameter signature string
    """
    params = []

    # Defensive: safely access attributes with defaults for malformed endpoints
    path_params = getattr(endpoint, "path_params", []) or []
    query_params = getattr(endpoint, "query_params", []) or []
    query_params_schema = getattr(endpoint, "query_params_schema", {}) or {}
    body_fields = getattr(endpoint, "body_fields", []) or []
    request_schema = getattr(endpoint, "request_schema", None)

    # Path params (always required)
    for name in path_params:
        params.append(f"{name}*")

    # Query params
    for name in query_params:
        schema = query_params_schema.get(name, {})
        required = schema.get("required", False)
        params.append(f"{name}{'*' if required else '?'}")

    # Body fields (include nested params from schema when available)
    if isinstance(request_schema, dict):
        for name, required in _flatten_schema_params(request_schema):
            params.append(f"{name}{'*' if required else '?'}")
    elif request_schema:
        required_fields = set(request_schema.get("required", [])) if isinstance(request_schema, dict) else set()
        for name in body_fields:
            params.append(f"{name}{'*' if name in required_fields else '?'}")

    return f"({', '.join(params)})" if params else "()"


def describe_entities(model: ConnectorModelProtocol) -> list[dict[str, Any]]:
    """Generate entity descriptions from ConnectorModel.

    Returns a list of entity descriptions with detailed parameter information
    for each action. This is used by generated connectors' list_entities() method.

    Args:
        model: Object conforming to ConnectorModelProtocol (e.g., ConnectorModel)

    Returns:
        List of entity description dicts with keys:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts
    """
    entities = []
    for entity_def in model.entities:
        description = ""
        parameters: dict[str, list[dict[str, Any]]] = {}

        endpoints = getattr(entity_def, "endpoints", {}) or {}
        if endpoints:
            for action, endpoint in endpoints.items():
                # Get description from first endpoint that has one
                if not description:
                    endpoint_desc = getattr(endpoint, "description", None)
                    if endpoint_desc:
                        description = endpoint_desc

                action_params: list[dict[str, Any]] = []

                # Defensive: safely access endpoint attributes
                path_params = getattr(endpoint, "path_params", []) or []
                path_params_schema = getattr(endpoint, "path_params_schema", {}) or {}
                query_params = getattr(endpoint, "query_params", []) or []
                query_params_schema = getattr(endpoint, "query_params_schema", {}) or {}
                body_fields = getattr(endpoint, "body_fields", []) or []
                request_schema = getattr(endpoint, "request_schema", None)

                # Path params (always required)
                for param_name in path_params:
                    schema = path_params_schema.get(param_name, {})
                    action_params.append(
                        {
                            "name": param_name,
                            "in": "path",
                            "required": True,
                            "type": schema.get("type", "string"),
                            "description": schema.get("description", ""),
                        }
                    )

                # Query params
                for param_name in query_params:
                    schema = query_params_schema.get(param_name, {})
                    action_params.append(
                        {
                            "name": param_name,
                            "in": "query",
                            "required": schema.get("required", False),
                            "type": schema.get("type", "string"),
                            "description": schema.get("description", ""),
                        }
                    )

                # Body fields
                if request_schema:
                    required_fields = request_schema.get("required", [])
                    properties = request_schema.get("properties", {})
                    for param_name in body_fields:
                        prop = properties.get(param_name, {})
                        action_params.append(
                            {
                                "name": param_name,
                                "in": "body",
                                "required": param_name in required_fields,
                                "type": prop.get("type", "string"),
                                "description": prop.get("description", ""),
                            }
                        )

                if action_params:
                    # Action is an enum, use .value to get string
                    action_key = action.value if hasattr(action, "value") else str(action)
                    parameters[action_key] = action_params

        actions = getattr(entity_def, "actions", []) or []
        entities.append(
            {
                "entity_name": entity_def.name,
                "description": description,
                "available_actions": [a.value if hasattr(a, "value") else str(a) for a in actions],
                "parameters": parameters,
            }
        )

    return entities


def generate_tool_description(
    model: ConnectorModelProtocol,
    *,
    enable_hosted_mode_features: bool = True,
) -> str:
    """Generate AI tool description from connector metadata.

    Produces a detailed description that includes:
    - Per-entity/action parameter signatures with required (*) and optional (?) markers
    - Response structure documentation with pagination hints
    - Example questions if available in the OpenAPI spec

    This is used by the Connector.tool_utils decorator to populate function
    docstrings for AI framework integration.

    Args:
        model: Object conforming to ConnectorModelProtocol (e.g., ConnectorModel)
        enable_hosted_mode_features: When False, omit hosted-mode search guidance from the docstring.

    Returns:
        Formatted description string suitable for AI tool documentation
    """
    lines = []
    # NOTE: Do not insert blank lines in the docstring; pydantic-ai parsing truncates
    # at the first empty line and only keeps the initial section.

    # Entity/action parameter details (including pagination params like limit, starting_after)
    search_field_paths = _collect_search_field_paths(model) if enable_hosted_mode_features else {}
    # Avoid a "PARAMETERS:" header because some docstring parsers treat it as a params section marker.
    lines.append("ENTITIES (ACTIONS + PARAMS):")
    for entity in model.entities:
        lines.append(f"  {entity.name}:")
        actions = getattr(entity, "actions", []) or []
        endpoints = getattr(entity, "endpoints", {}) or {}
        for action in actions:
            action_str = action.value if hasattr(action, "value") else str(action)
            endpoint = endpoints.get(action)
            if endpoint:
                param_sig = format_param_signature(endpoint)
                lines.append(f"    - {action_str}{param_sig}")
            else:
                lines.append(f"    - {action_str}()")
        if entity.name in search_field_paths:
            search_sig = _format_search_param_signature()
            lines.append(f"    - search{search_sig}")

    # Response structure (brief, includes pagination hint)
    lines.append("RESPONSE STRUCTURE:")
    lines.append("  - list/api_search: {data: [...], meta: {has_more: bool}}")
    lines.append("  - get: Returns entity directly (no envelope)")
    lines.append("  To paginate: pass starting_after=<last_id> while has_more is true")

    lines.append("GUIDELINES:")
    if enable_hosted_mode_features:
        lines.append('  - Prefer cached search over direct API calls when using execute(): action="search" whenever possible.')
        lines.append("  - Direct API actions (list/get/download) are slower and should be used only if search cannot answer the query.")
    lines.append("  - Keep results small: use params.fields, params.query.filter, small params.limit, and cursor pagination.")
    lines.append("  - If output is too large, refine the query with tighter filters/fields/limit.")

    if search_field_paths:
        lines.append("SEARCH (PREFERRED):")
        lines.append('  execute(entity, action="search", params={')
        lines.append('    "query": {"filter": <condition>, "sort": [{"field": "asc|desc"}, ...]},')
        lines.append('    "limit": <int>, "cursor": <str>, "fields": ["field", "nested.field", ...]')
        lines.append("  })")
        lines.append('  Example: {"query": {"filter": {"eq": {"title": "Intro to Airbyte | Miinto"}}}, "limit": 1,')
        lines.append('            "fields": ["id", "title", "started", "primaryUserId"]}')
        lines.append("  Conditions are composable:")
        lines.append("    - eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, contains, any")
        lines.append('    - and/or/not to combine conditions (e.g., {"and": [cond1, cond2]})')

        lines.append("SEARCHABLE FIELDS:")
        for entity_name, field_paths in search_field_paths.items():
            if field_paths:
                lines.append(f"  {entity_name}: {', '.join(field_paths)}")
            else:
                lines.append(f"  {entity_name}: (no fields listed)")

    # Add example questions if available in openapi_spec
    openapi_spec = getattr(model, "openapi_spec", None)
    if openapi_spec:
        info = getattr(openapi_spec, "info", None)
        if info:
            example_questions = getattr(info, "x_airbyte_example_questions", None)
            if example_questions:
                supported = getattr(example_questions, "supported", None)
                if supported:
                    lines.append("EXAMPLE QUESTIONS:")
                    for q in supported[:MAX_EXAMPLE_QUESTIONS]:
                        lines.append(f"  - {q}")

    # Generic parameter description for function signature
    lines.append("FUNCTION PARAMETERS:")
    lines.append("  - entity: Entity name (string)")
    lines.append("  - action: Operation to perform (string)")
    lines.append("  - params: Operation parameters (dict) - see entity details above")
    lines.append("Parameter markers: * = required, ? = optional")

    return "\n".join(lines)
