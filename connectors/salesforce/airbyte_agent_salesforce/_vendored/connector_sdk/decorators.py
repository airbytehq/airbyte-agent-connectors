"""
Decorators for AI agent tool integration.

Provides utilities to auto-generate comprehensive tool descriptions
from connector metadata, enabling easy integration with AI frameworks.
"""

from __future__ import annotations

import importlib
from typing import Any, Callable, TypeVar

from .introspection import (
    MAX_EXAMPLE_QUESTIONS,
    ConnectorModelProtocol,
    EndpointProtocol,
    generate_tool_description,
)

F = TypeVar("F", bound=Callable[..., Any])

__all__ = [
    "airbyte_description",
    "EndpointProtocol",
    "ConnectorModelProtocol",
    "MAX_EXAMPLE_QUESTIONS",
    # Private function exposed for testing
    "_load_connector_model",
]


def airbyte_description(connector_name: str) -> Callable[[F], F]:
    """
    Decorator that generates comprehensive tool descriptions from connector metadata.

    Automatically populates the function's docstring with:
    - Connector description
    - Available entities and their actions
    - Example questions the connector can answer

    Args:
        connector_name: Name of the connector (e.g., "hubspot", "stripe")
                       Must match the generated package name pattern:
                       airbyte_agent_{connector_name}

    Returns:
        Decorator that updates the function's __doc__ attribute

    Example:
        from airbyte_agent_hubspot import HubspotConnector

        connector = HubspotConnector(
            external_user_id=external_user_id,
            airbyte_client_id=airbyte_client_id,
            airbyte_client_secret=airbyte_client_secret
        )

        # IMPORTANT: @airbyte_description must be the INNER decorator (closest to function)
        # This ensures __doc__ is expanded BEFORE frameworks like FastMCP capture it
        @agent.tool_plain  # or @mcp.tool() for FastMCP
        @airbyte_description("hubspot")
        async def hubspot_exec(entity: str, action: str, params: dict | None = None):
            '''Execute HubSpot operations.'''
            return await connector.execute(entity, action, params or {})

    The decorator will update hubspot_exec.__doc__ with a comprehensive
    description including all available entities, actions, and example questions.
    """

    def decorator(func: F) -> F:
        # Load connector model from generated package
        model = _load_connector_model(connector_name)

        # Generate description using shared introspection module
        description = generate_tool_description(model)

        # Preserve original docstring if present, append to it
        original_doc = func.__doc__ or ""
        if original_doc.strip():
            func.__doc__ = f"{original_doc.strip()}\n\n{description}"
        else:
            func.__doc__ = description

        return func

    return decorator


def _load_connector_model(connector_name: str) -> Any:
    """
    Load connector model from generated package.

    Args:
        connector_name: Connector name (e.g., "hubspot")

    Returns:
        ConnectorModel instance from the generated package

    Raises:
        ImportError: If connector package is not installed
        AttributeError: If connector model constant not found
    """
    # Normalize connector name to package name
    package_name = f"airbyte_agent_{connector_name.replace('-', '_')}"

    try:
        # Import the connector_model module from the generated package
        module = importlib.import_module(f"{package_name}.connector_model")
    except ImportError as e:
        raise ImportError(f"Could not import connector package '{package_name}'. " f"Ensure the package is installed. Error: {e}") from e

    # Find the ConnectorModel constant (named like HubspotConnectorModel)
    # Convention: {PascalCase connector name}ConnectorModel
    pascal_name = "".join(word.capitalize() for word in connector_name.replace("-", "_").split("_"))
    model_name = f"{pascal_name}ConnectorModel"

    model = getattr(module, model_name, None)
    if model is None:
        # Fallback: look for any ConnectorModel attribute
        for attr_name in dir(module):
            if attr_name.endswith("ConnectorModel"):
                model = getattr(module, attr_name)
                break

    if model is None:
        raise AttributeError(f"Could not find ConnectorModel in {package_name}.connector_model. " f"Expected constant named '{model_name}'")

    return model
