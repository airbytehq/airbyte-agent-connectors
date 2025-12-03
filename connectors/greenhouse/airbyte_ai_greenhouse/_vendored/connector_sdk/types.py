"""Type definitions for Airbyte SDK."""

from __future__ import annotations

from enum import Enum
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

from .constants import OPENAPI_DEFAULT_VERSION
from .schema.components import PathOverrideConfig
from .schema.security import AirbyteAuthConfig


class Action(str, Enum):
    """Supported actions for Entity operations."""

    GET = "get"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    LIST = "list"
    SEARCH = "search"
    DOWNLOAD = "download"
    AUTHORIZE = "authorize"


class AuthType(str, Enum):
    """Supported authentication types."""

    API_KEY = "api_key"
    BEARER = "bearer"
    HTTP = "http"
    BASIC = "basic"
    OAUTH2 = "oauth2"


class ContentType(str, Enum):
    """Supported content types for request bodies."""

    JSON = "application/json"
    FORM_URLENCODED = "application/x-www-form-urlencoded"
    FORM_DATA = "multipart/form-data"


class ParameterLocation(str, Enum):
    """Location of operation parameters."""

    PATH = "path"
    QUERY = "query"
    HEADER = "header"
    COOKIE = "cookie"


# All comprehensive OpenAPI 3.0 models are now in connector_sdk.schema package
# Import from connector_sdk.schema for: OpenAPIConnector, Components, Schema, Operation, etc.


class AuthConfig(BaseModel):
    """Authentication configuration."""

    type: AuthType
    config: dict[str, Any] = Field(default_factory=dict)
    # User-facing config spec from x-airbyte-auth-config extension
    user_config_spec: AirbyteAuthConfig | None = Field(
        None,
        description="User-facing authentication configuration spec from x-airbyte-auth-config",
    )


# Executor types (used by executor.py)
class EndpointDefinition(BaseModel):
    """Definition of an API endpoint."""

    method: str  # GET, POST, PUT, DELETE, etc.
    path: str  # e.g., /v1/customers/{id} (OpenAPI path)
    path_override: PathOverrideConfig | None = Field(
        None,
        description=(
            "Path override config from x-airbyte-path-override. "
            "When set, overrides the path for actual HTTP requests."
        ),
    )
    action: Action | None = None  # Semantic action (get, list, create, update, delete)
    description: str | None = None
    body_fields: list[str] = Field(default_factory=list)  # For POST/PUT
    query_params: list[str] = Field(default_factory=list)  # For GET
    path_params: list[str] = Field(default_factory=list)  # Extracted from path
    content_type: ContentType = ContentType.JSON
    request_schema: dict[str, Any] | None = None
    response_schema: dict[str, Any] | None = None

    # GraphQL support (Airbyte extension)
    graphql_body: dict[str, Any] | None = Field(
        None,
        description="GraphQL body configuration from x-airbyte-body-type extension",
    )

    # Download support (Airbyte extension)
    file_field: str | None = Field(
        None,
        description="Field in metadata response containing download URL (from x-airbyte-file-url extension)",
    )


class EntityDefinition(BaseModel):
    """Definition of an API entity."""

    model_config = {"populate_by_name": True}

    name: str
    actions: list[Action]
    endpoints: dict[Action, EndpointDefinition]
    entity_schema: dict[str, Any] | None = Field(default=None, alias="schema")


class ConnectorConfig(BaseModel):
    """Complete connector configuration loaded from YAML."""

    model_config = ConfigDict(use_enum_values=True)

    name: str
    version: str = OPENAPI_DEFAULT_VERSION
    base_url: str
    auth: AuthConfig
    entities: list[EntityDefinition]
    openapi_spec: Any | None = None  # Optional reference to OpenAPIConnector
