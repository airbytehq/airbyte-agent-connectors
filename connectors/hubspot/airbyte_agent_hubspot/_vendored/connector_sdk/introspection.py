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

    # Body fields
    if request_schema:
        required_fields = set(request_schema.get("required", []))
        for name in body_fields:
            params.append(f"{name}{'*' if name in required_fields else '?'}")

    return f"({', '.join(params)})" if params else "()"


def describe_entities(model: ConnectorModelProtocol) -> list[dict[str, Any]]:
    """Generate entity descriptions from ConnectorModel.

    Returns a list of entity descriptions with detailed parameter information
    for each action. This is used by generated connectors' describe() method.

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


def generate_tool_description(model: ConnectorModelProtocol) -> str:
    """Generate AI tool description from connector metadata.

    Produces a detailed description that includes:
    - Per-entity/action parameter signatures with required (*) and optional (?) markers
    - Response structure documentation with pagination hints
    - Example questions if available in the OpenAPI spec

    This is used by the @airbyte_description decorator to populate
    function docstrings for AI framework integration.

    Args:
        model: Object conforming to ConnectorModelProtocol (e.g., ConnectorModel)

    Returns:
        Formatted description string suitable for AI tool documentation
    """
    lines = []

    # Entity/action parameter details (including pagination params like limit, starting_after)
    lines.append("ENTITIES AND PARAMETERS:")
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

    # Response structure (brief, includes pagination hint)
    lines.append("")
    lines.append("RESPONSE STRUCTURE:")
    lines.append("  - list/search: {data: [...], meta: {has_more: bool}}")
    lines.append("  - get: Returns entity directly (no envelope)")
    lines.append("  To paginate: pass starting_after=<last_id> while has_more is true")

    # Add example questions if available in openapi_spec
    openapi_spec = getattr(model, "openapi_spec", None)
    if openapi_spec:
        info = getattr(openapi_spec, "info", None)
        if info:
            example_questions = getattr(info, "x_airbyte_example_questions", None)
            if example_questions:
                supported = getattr(example_questions, "supported", None)
                if supported:
                    lines.append("")
                    lines.append("EXAMPLE QUESTIONS:")
                    for q in supported[:MAX_EXAMPLE_QUESTIONS]:
                        lines.append(f"  - {q}")

    # Generic parameter description for function signature
    lines.append("")
    lines.append("FUNCTION PARAMETERS:")
    lines.append("  - entity: Entity name (string)")
    lines.append("  - action: Operation to perform (string)")
    lines.append("  - params: Operation parameters (dict) - see entity details above")
    lines.append("")
    lines.append("Parameter markers: * = required, ? = optional")

    return "\n".join(lines)
