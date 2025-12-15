"""Connector instantiation and execution management."""

import base64
import inspect
import logging
from typing import Any

from ._vendored.connector_sdk import LocalExecutor as ConnectorExecutor
from ._vendored.connector_sdk.connector_model_loader import load_connector_model
from ._vendored.connector_sdk.executor.models import ExecutionConfig

from airbyte_agent_mcp.models import Config, ConnectorConfig, ConnectorInfo, ConnectorType, DiscoverConnectorsResponse
from airbyte_agent_mcp.registry_client import RegistryClient
from airbyte_agent_mcp.secret_manager import SecretsManager

logger = logging.getLogger(__name__)


class ConnectorManager:
    """Manages connector lifecycle and execution."""

    def __init__(
        self,
        config: Config,
        secrets_manager: SecretsManager,
        registry_client: RegistryClient | None = None,
    ):
        """Initialize manager.

        Args:
            config: Configuration with connector definitions
            secrets_manager: Secrets manager for resolving credentials
            registry_client: Optional registry client for fetching remote connectors
        """
        self.config = config
        self.secrets_manager = secrets_manager
        self.registry_client = registry_client or RegistryClient()

    async def _get_connector_path(self, connector_config: ConnectorConfig) -> str:
        """Get path to connector.yaml (local file or downloaded from registry).

        Args:
            connector_config: The connector configuration

        Returns:
            Path to the connector.yaml file
        """
        if connector_config.path:
            # Use local path
            return connector_config.path

        # Download from registry
        path = await self.registry_client.download_connector(
            connector_name=connector_config.connector_name,
            version=connector_config.version,
        )
        return str(path)

    async def execute(
        self,
        connector_id: str,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute an operation on a connector.

        This is stateless - creates a fresh connector instance for each call.

        Args:
            connector_id: Connector ID from config
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "list", "get", "create")
            params: Operation parameters (optional)

        Returns:
            Result from connector execution

        Raises:
            ValueError: If connector not found
            Exception: Any error from connector execution
        """
        params = params or {}

        logger.info(f"Executing: {connector_id}.{entity}.{action} with params: {list(params.keys())}")

        connector_config = self.config.get_connector(connector_id)

        secrets = {}
        if connector_config.secrets:
            secrets = self.secrets_manager.get_secrets(connector_config.secrets)

        # Resolve config_values from environment variables
        config_values = {}
        if connector_config.config_values:
            config_values = self.secrets_manager.get_secrets(connector_config.config_values)

        # Get path (local or from registry)
        path = await self._get_connector_path(connector_config)
        logger.info(f"Using connector path: {path}")
        connector = self._create_yaml_connector(path, secrets, auth_scheme=connector_config.auth_scheme, config_values=config_values)

        logger.debug(f"Calling connector.execute({entity}, {action}, ...)")
        result = await connector.execute(ExecutionConfig(entity=entity, action=action, params=params))

        # Handle ExecutionResult from SDK
        if not result.success:
            raise Exception(result.error or "Execution failed")

        # Handle download operations (data is AsyncIterator[bytes])
        if inspect.isasyncgen(result.data):
            return await self._handle_download(result.data)

        logger.info("Execution successful")
        return result.data

    def _create_yaml_connector(
        self, path: str, secrets: dict[str, Any], auth_scheme: str | None = None, config_values: dict[str, str] | None = None
    ) -> Any:
        """Create a YAML-based connector instance.

        Args:
            path: Path to connector.yaml file
            secrets: Resolved secrets dict
            auth_scheme: Auth scheme for multi-auth connectors (optional)
            config_values: Non-secret config values like subdomain, region (optional)

        Returns:
            ConnectorExecutor instance
        """
        connector = ConnectorExecutor(
            config_path=path, auth_config=secrets, auth_scheme=auth_scheme, config_values=config_values, execution_context="mcp"
        )

        return connector

    async def _handle_download(self, stream: Any) -> dict[str, Any]:
        """Handle download operations by collecting bytes and base64 encoding.

        Args:
            stream: AsyncIterator[bytes] from connector download operation

        Returns:
            Dict with base64-encoded data and metadata

        Raises:
            Exception: If file exceeds maximum size limit
        """
        max_size = 50 * 1024 * 1024  # 50MB limit for MCP downloads
        chunks: list[bytes] = []
        total_size = 0

        async for chunk in stream:
            total_size += len(chunk)
            if total_size > max_size:
                raise Exception(
                    f"Download exceeds maximum size limit ({max_size // (1024 * 1024)}MB). Use the SDK directly for large file downloads."
                )
            chunks.append(chunk)

        binary_data = b"".join(chunks)

        logger.info(f"Download successful: {len(binary_data)} bytes")

        return {
            "data": base64.b64encode(binary_data).decode("utf-8"),
            "size": len(binary_data),
            "encoding": "base64",
        }

    async def describe_connector(self, connector_id: str) -> list[dict[str, Any]]:
        """List available entities for a connector.

        Args:
            connector_id: Connector ID from config

        Returns:
            List of entity info dicts
        """
        logger.info(f"Listing entities for: {connector_id}")

        connector_config = self.config.get_connector(connector_id)
        if connector_config.type == ConnectorType.LOCAL:
            path = await self._get_connector_path(connector_config)
            return await self._describe_connector_from_sdk(path)

    async def _describe_connector_from_sdk(self, path: str) -> list[dict[str, Any]]:
        """List entities from a YAML connector definition.

        Args:
            path: Path to connector.yaml (OpenAPI spec)

        Returns:
            List of entity info dicts
        """

        # Load and parse the connector model using SDK
        connector_model = load_connector_model(path)

        # Build parameter lookup from OpenAPI spec for full metadata
        param_lookup = self._build_param_lookup(connector_model)

        entities = []
        for entity_def in connector_model.entities:
            description = ""
            parameters: dict[str, list[dict[str, Any]]] = {}

            # Extract parameters for each action from endpoints
            if entity_def.endpoints:
                for action, endpoint in entity_def.endpoints.items():
                    if not description and endpoint.description:
                        description = endpoint.description

                    # Get the lookup key for this endpoint
                    lookup_key = (endpoint.path, endpoint.method.lower())
                    operation_params = param_lookup.get(lookup_key, {})

                    # Collect all parameters for this action with full metadata
                    action_params = []

                    # Path params (always required)
                    for param_name in endpoint.path_params:
                        param_meta = operation_params.get(param_name, {})
                        action_params.append(
                            {
                                "name": param_name,
                                "in": "path",
                                "required": True,  # Path params are always required
                                "type": param_meta.get("type", "string"),
                                "description": param_meta.get("description", ""),
                            }
                        )

                    # Query params (get required/type/description from spec)
                    for param_name in endpoint.query_params:
                        param_meta = operation_params.get(param_name, {})
                        action_params.append(
                            {
                                "name": param_name,
                                "in": "query",
                                "required": param_meta.get("required", False),
                                "type": param_meta.get("type", "string"),
                                "description": param_meta.get("description", ""),
                            }
                        )

                    # Body fields (get required from request schema)
                    request_schema = endpoint.request_schema or {}
                    required_fields = request_schema.get("required", [])
                    properties = request_schema.get("properties", {})

                    for param_name in endpoint.body_fields:
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
                        parameters[action.value] = action_params

            # Convert Action enums to strings
            available_actions = [action.value for action in entity_def.actions]

            entities.append(
                {
                    "entity_name": entity_def.name,
                    "description": description,
                    "available_actions": available_actions,
                    "parameters": parameters,
                }
            )

        return entities

    def _build_param_lookup(self, connector_model: Any) -> dict[tuple[str, str], dict[str, dict[str, Any]]]:
        """Build a lookup of parameter metadata from OpenAPI spec.

        Args:
            connector_model: Loaded connector model with openapi_spec

        Returns:
            Dict mapping (path, method) -> {param_name -> {type, description, required}}
        """
        lookup: dict[tuple[str, str], dict[str, dict[str, Any]]] = {}

        openapi_spec = getattr(connector_model, "openapi_spec", None)
        if not openapi_spec or not hasattr(openapi_spec, "paths"):
            return lookup

        for path, path_item in openapi_spec.paths.items():
            for method_name in ["get", "post", "put", "delete", "patch"]:
                operation = getattr(path_item, method_name, None)
                if not operation:
                    continue

                param_map: dict[str, dict[str, Any]] = {}
                if operation.parameters:
                    for param in operation.parameters:
                        # Extract type from schema if available
                        param_type = "string"
                        if param.schema_:
                            param_type = param.schema_.get("type", "string")

                        param_map[param.name] = {
                            "type": param_type,
                            "description": param.description or "",
                            "required": param.required or False,
                        }

                lookup[(path, method_name)] = param_map

        return lookup

    def discover_connectors(self) -> dict[str, Any]:
        """Discover all available configured connectors.

        Returns:
            Dictionary with list of connector information
        """
        logger.info("Discovering connectors from configuration")

        # Build list of connector info
        connector_infos = [
            ConnectorInfo(
                id=connector.id,
                type=connector.type.value,  # Convert enum to string
                description=connector.description,
            )
            for connector in self.config.connectors
        ]

        response = DiscoverConnectorsResponse(connectors=connector_infos)

        return response.model_dump()
