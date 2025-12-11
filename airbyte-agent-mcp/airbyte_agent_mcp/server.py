"""FastMCP server with connector tools."""

import logging
from typing import Any

from fastmcp import FastMCP

from airbyte_agent_mcp.config import load_connector_config, validate_connectors
from airbyte_agent_mcp.connector_manager import ConnectorManager
from airbyte_agent_mcp.models import ExecuteResponse, ListEntitiesResponse
from airbyte_agent_mcp.secret_manager import DotEnvSecretsBackend, SecretsManager

logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("airbyte-agent-mcp")


def _serialize_exception(e: Exception) -> dict:
    """Serialize an exception to a JSON-safe dictionary.

    Handles SDK exceptions that may contain non-serializable objects
    like HTTPResponse in their __dict__.

    Args:
        e: The exception to serialize

    Returns:
        A JSON-serializable error dictionary
    """
    error_type = type(e).__name__

    # Build error dict with safe, serializable values
    error_dict: dict = {
        "type": error_type,
        "message": str(e),
    }

    # Extract useful fields from HTTP exceptions without including HTTPResponse objects
    if hasattr(e, "status_code"):
        error_dict["status_code"] = e.status_code

    if hasattr(e, "retry_after") and e.retry_after is not None:
        error_dict["retry_after"] = e.retry_after

    if hasattr(e, "timeout_type") and e.timeout_type is not None:
        error_dict["timeout_type"] = e.timeout_type

    return error_dict


@mcp.tool()
async def execute(connector_id: str, entity: str, action: str, params: dict[str, Any] | None = None) -> dict:
    """Execute an operation on a connector.

    This is the primary tool for interacting with connectors. It creates a fresh
    connector instance, executes the operation, and returns the result.

    Args:
        connector_id: Connector identifier from configured_connectors.yaml
        entity: Entity name (e.g., "customers", "invoices"). The entity is not a URL path.
        action: Operation action (e.g., "get", "list", "create", "update", "delete")
        params: Operation parameters (optional, depends on action)
            - For "get": {"id": "..."}
            - For "list": {"limit": 10, "starting_after": "..."}
            - For "create": {"field1": "value1", ...}

    Returns:
        Execution result with success status and data or error

    Example:
        execute(
            connector_id="stripe",
            entity="customers",
            action="list",
            params={"limit": 10}
        )
    """
    params = params or {}

    try:
        logger.info(f"Tool call: execute({connector_id}, {entity}, {action})")

        # Execute operation
        result = await mcp.connector_manager.execute(
            connector_id=connector_id,
            entity=entity,
            action=action,
            params=params,
        )

        response = ExecuteResponse(
            success=True,
            data=result,
            connector_id=connector_id,
            entity=entity,
            action=action,
        )

        return response.model_dump()

    except Exception as e:
        logger.error(f"Execution failed: {e}", exc_info=True)

        response = ExecuteResponse(
            success=False,
            error=_serialize_exception(e),
            connector_id=connector_id,
            entity=entity,
            action=action,
        )

        return response.model_dump()


@mcp.tool()
async def describe_connector(connector_id: str) -> dict:
    """Describe a connector's available entities and operations.

    Discovers what entities (data types) a connector provides and what
    operations (actions) are available for each entity by parsing the
    connector's OpenAPI specification.

    Args:
        connector_id: Connector identifier from configured_connectors.yaml

    Returns:
        Dictionary containing:
        - connector_id: The connector identifier
        - entities: List of entity objects, each with:
          - entity_name: Entity identifier used in operations
          - description: Entity description
          - available_actions: List of supported operation actions

    Example:
        describe_connector(connector_id="stripe")

        Returns:
        {
            "connector_id": "stripe",
            "entities": [
                {
                    "entity_name": "customers",
                    "description": "Customer objects",
                    "available_actions": ["list", "retrieve"]
                },
                ...
            ]
        }
    """
    try:
        logger.info(f"Tool call: describe_connector({connector_id})")

        entities = await mcp.connector_manager.describe_connector(connector_id)

        response = ListEntitiesResponse(connector_id=connector_id, entities=entities)

        return response.model_dump()

    except Exception as e:
        logger.error(f"Failed to list entities: {e}", exc_info=True)
        return {"error": str(e), "connector_id": connector_id}


@mcp.tool()
async def discover_connectors() -> dict:
    """Discover all available configured connectors.

    Returns a list of all connectors defined in the configured_connectors.yaml configuration
    file. This allows you to see what connectors are available before executing
    operations or describing their resources.

    Returns:
        Dictionary containing:
        - connectors: List of connector objects, each with:
          - id: Connector identifier used in other operations
          - type: Connector type (local or remote)
          - description: Human-readable description

    Example:
        discover_connectors()

        Returns:
        {
            "connectors": [
                {
                    "id": "stripe",
                    "type": "local",
                    "description": "Stripe API connector"
                },
                {
                    "id": "shopify",
                    "type": "remote",
                    "description": "Shopify connector from registry"
                }
            ]
        }
    """
    try:
        logger.info("Tool call: discover_connectors()")
        return mcp.connector_manager.discover_connectors()

    except Exception as e:
        logger.error(f"Failed to discover connectors: {e}", exc_info=True)
        return {"error": str(e), "connectors": []}


def init_server(config_path: str = "configured_connectors.yaml", dotenv_path: str = ".env"):
    """Initialize the MCP server with configuration.

    Args:
        config_path: Path to configured_connectors.yaml
        dotenv_path: Path to .env file with secrets

    Raises:
        SystemExit: If initialization fails
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger.info("Initializing airbyte-agent-mcp server...")

    try:
        # Load configuration
        config = load_connector_config(config_path)
        logger.info(f"Loaded configuration with {len(config.connectors)} connector(s)")

        # Validate connectors
        errors = validate_connectors(config)
        if errors:
            logger.error("Connector validation failed:")
            for error in errors:
                logger.error(f"  - {error}")
            raise SystemExit(1)

        # Initialize secrets manager
        secrets_backend = DotEnvSecretsBackend(dotenv_path)
        secrets_manager = SecretsManager(secrets_backend)
        logger.info("Initialized secrets manager")

        # Store managers on MCP instance (application-wide state)
        mcp.connector_manager = ConnectorManager(config, secrets_manager)
        logger.info("Initialized connector manager")

        logger.info(" Server initialization complete")

    except Exception as e:
        logger.error(f"Failed to initialize server: {e}", exc_info=True)
        raise SystemExit(1)


def run_server(config_path: str = "configured_connectors.yaml", dotenv_path: str = ".env"):
    """Run the MCP server.

    Args:
        config_path: Path to configured_connectors.yaml
        dotenv_path: Path to .env file
    """
    init_server(config_path, dotenv_path)

    # FastMCP handles the server loop
    logger.info("Starting MCP server on stdio transport...")
    mcp.run()
