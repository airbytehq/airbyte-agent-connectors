"""Data models for airbyte-agent-mcp configuration and responses."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class BackoffType(str, Enum):
    """Retry backoff strategy."""

    EXPONENTIAL = "exponential"
    LINEAR = "linear"


class ErrorType(str, Enum):
    """Categorized error types for retry logic."""

    RATE_LIMIT = "rate_limit"
    TIMEOUT = "timeout"
    SERVER_ERROR = "server_error"
    UNKNOWN = "unknown"


class ConnectorType(str, Enum):
    """Type of connector."""

    LOCAL = "local"
    HOSTED = "hosted"


class ConnectorConfig(BaseModel):
    """Configuration for a single connector."""

    id: str = Field(..., description="Unique connector identifier")
    type: ConnectorType = Field(..., description="Connector type")
    path: str | None = Field(None, description="Path to connector.yaml (optional if connector_name provided)")
    connector_name: str | None = Field(None, description="Connector name in registry")
    version: str | None = Field(None, description="Version to pin (optional, defaults to latest)")
    description: str = Field(default="", description="Human-readable description")
    secrets: dict[str, str] = Field(default_factory=dict, description="Mapping of secret param names to secret keys")
    config_values: dict[str, str] = Field(default_factory=dict, description="Non-secret config values (e.g., subdomain, region)")
    auth_scheme: str | None = Field(None, description="Auth scheme for multi-auth connectors (e.g., 'oauth', 'api_token')")

    def model_post_init(self, __context):
        """Validate connector-type-specific fields."""
        if self.type == ConnectorType.LOCAL:
            if not self.path and not self.connector_name:
                raise ValueError(f"LOCAL connector '{self.id}' must specify either 'path' or 'connector_name'")

            # Version pinning only makes sense with registry-based connectors
            if self.path and self.version:
                raise ValueError(
                    f"LOCAL connector '{self.id}' uses 'path' and 'version'. "
                    "Version pinning is only supported for registry-based connectors "
                    "using 'connector_name'. Remove 'version' or switch to 'connector_name'."
                )


class Config(BaseModel):
    """Root configuration model."""

    connectors: list[ConnectorConfig] = Field(..., min_length=1)

    def get_connector(self, connector_id: str) -> ConnectorConfig:
        """Look up connector by ID."""
        for connector in self.connectors:
            if connector.id == connector_id:
                return connector
        raise ValueError(f"Connector not found: {connector_id}")


class ExecuteResponse(BaseModel):
    """Response from execute tool."""

    success: bool
    data: Any = None
    error: dict | None = None
    connector_id: str
    entity: str
    action: str


class ParameterInfo(BaseModel):
    """Information about an operation parameter."""

    name: str = Field(..., description="Parameter name")
    in_: str = Field(..., alias="in", description="Parameter location: path, query, or body")
    required: bool = Field(default=False, description="Whether the parameter is required")
    type: str = Field(default="string", description="Parameter type (string, integer, boolean, etc.)")
    description: str = Field(default="", description="Parameter description")


class EntityInfo(BaseModel):
    """Information about a connector entity."""

    entity_name: str = Field(..., description="Entity name to use in execute() calls")
    description: str = ""
    available_actions: list[str] = Field(default_factory=list)
    parameters: dict[str, list[dict[str, Any]]] = Field(
        default_factory=dict,
        description="Parameters for each action, keyed by action name. Each parameter has: name, in (path/query/body), required, type, description",
    )


class ListEntitiesResponse(BaseModel):
    """Response from list_entities tool."""

    connector_id: str
    entities: list[EntityInfo]


class DescribeEntityResponse(BaseModel):
    """Response from describe_entity tool."""

    connector_id: str
    entity: str
    actions: dict
    schema: dict


class ValidationError(BaseModel):
    """Validation error detail."""

    field: str
    message: str


class ValidateOperationResponse(BaseModel):
    """Response from validate_operation tool."""

    valid: bool
    errors: list[ValidationError] = Field(default_factory=list)


class ConnectorInfo(BaseModel):
    """Information about a configured connector."""

    id: str = Field(..., description="Connector identifier")
    type: str = Field(..., description="Connector type (local or remote)")
    description: str = Field(default="", description="Human-readable description")


class DiscoverConnectorsResponse(BaseModel):
    """Response from discover_connectors tool."""

    connectors: list[ConnectorInfo] = Field(..., description="List of configured connectors")
