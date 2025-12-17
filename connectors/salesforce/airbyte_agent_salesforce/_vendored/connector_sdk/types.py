"""Type definitions for Airbyte SDK."""

from __future__ import annotations

from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from .constants import OPENAPI_DEFAULT_VERSION
from .schema.components import PathOverrideConfig
from .schema.extensions import RetryConfig
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


class AuthOption(BaseModel):
    """A single authentication option in a multi-auth connector.

    Represents one security scheme from OpenAPI components.securitySchemes.
    Each option defines a complete authentication method with its own type,
    configuration, and user-facing credential specification.

    Example:
        For a connector supporting both OAuth2 and API Key auth:
        - AuthOption(scheme_name="oauth", type=OAUTH2, ...)
        - AuthOption(scheme_name="apikey", type=BEARER, ...)
    """

    scheme_name: str = Field(description="Security scheme name from OpenAPI spec (e.g., 'githubOAuth', 'githubPAT')")
    type: AuthType = Field(description="Authentication type for this option")
    config: dict[str, Any] = Field(
        default_factory=dict,
        description="Auth-specific configuration (e.g., OAuth2 refresh settings)",
    )
    user_config_spec: AirbyteAuthConfig | None = Field(
        None,
        description="User-facing credential specification from x-airbyte-auth-config",
    )


class AuthConfig(BaseModel):
    """Authentication configuration supporting single or multiple auth methods.

    Connectors can define either:
    - Single auth: One authentication method (backwards compatible)
    - Multi-auth: Multiple authentication methods (user/agent selects one)

    For single-auth connectors (most common):
        AuthConfig(type=OAUTH2, config={...}, user_config_spec={...})

    For multi-auth connectors:
        AuthConfig(options=[
            AuthOption(scheme_name="oauth", type=OAUTH2, ...),
            AuthOption(scheme_name="apikey", type=BEARER, ...)
        ])
    """

    # Single-auth mode (backwards compatible)
    type: AuthType | None = Field(
        None,
        description="Authentication type (single-auth mode only)",
    )
    config: dict[str, Any] = Field(
        default_factory=dict,
        description="Auth configuration (single-auth mode only)",
    )
    user_config_spec: AirbyteAuthConfig | None = Field(
        None,
        description="User-facing config spec from x-airbyte-auth-config (single-auth mode)",
    )

    # Multi-auth mode
    options: list[AuthOption] | None = Field(
        None,
        description="Multiple authentication options (multi-auth mode only)",
    )

    def is_multi_auth(self) -> bool:
        """Check if this configuration supports multiple authentication methods.

        Returns:
            True if multiple auth options are available, False for single-auth
        """
        return self.options is not None and len(self.options) > 0

    def get_single_option(self) -> AuthOption:
        """Get single auth option (for backwards compatibility).

        Converts single-auth config to AuthOption format for uniform handling.

        Returns:
            AuthOption containing the single auth configuration

        Raises:
            ValueError: If this is a multi-auth config or invalid
        """
        if self.is_multi_auth():
            raise ValueError("Cannot call get_single_option() on multi-auth config. " "Use options list instead.")

        if self.type is None:
            raise ValueError("Invalid AuthConfig: neither single-auth nor multi-auth")

        return AuthOption(
            scheme_name="default",
            type=self.type,
            config=self.config,
            user_config_spec=self.user_config_spec,
        )


# Executor types (used by executor.py)
class EndpointDefinition(BaseModel):
    """Definition of an API endpoint."""

    method: str  # GET, POST, PUT, DELETE, etc.
    path: str  # e.g., /v1/customers/{id} (OpenAPI path)
    path_override: PathOverrideConfig | None = Field(
        None,
        description=("Path override config from x-airbyte-path-override. " "When set, overrides the path for actual HTTP requests."),
    )
    action: Action | None = None  # Semantic action (get, list, create, update, delete)
    description: str | None = None
    body_fields: list[str] = Field(default_factory=list)  # For POST/PUT
    query_params: list[str] = Field(default_factory=list)  # For GET
    query_params_schema: dict[str, dict[str, Any]] = Field(
        default_factory=dict,
        description="Schema for query params including defaults: {name: {type, default, required}}",
    )
    deep_object_params: list[str] = Field(
        default_factory=list,
        description="Query parameters using deepObject style (e.g., filter[key]=value)",
    )  # For GET with deepObject query params
    path_params: list[str] = Field(default_factory=list)  # Extracted from path
    path_params_schema: dict[str, dict[str, Any]] = Field(
        default_factory=dict,
        description="Schema for path params including defaults: {name: {type, default, required}}",
    )
    content_type: ContentType = ContentType.JSON
    request_schema: dict[str, Any] | None = None
    response_schema: dict[str, Any] | None = None

    # GraphQL support (Airbyte extension)
    graphql_body: dict[str, Any] | None = Field(
        None,
        description="GraphQL body configuration from x-airbyte-body-type extension",
    )

    # Record extractor support (Airbyte extension)
    record_extractor: str | None = Field(
        None,
        description="JSONPath expression to extract records from response envelopes",
    )

    # Metadata extractor support (Airbyte extension)
    meta_extractor: dict[str, str] | None = Field(
        None,
        description="Dictionary mapping field names to JSONPath expressions for extracting metadata from response envelopes",
    )

    # Download support (Airbyte extension)
    file_field: str | None = Field(
        None,
        description="Field in metadata response containing download URL (from x-airbyte-file-url extension)",
    )

    # Test validation support (Airbyte extension)
    untested: bool = Field(
        False,
        description="Mark operation as untested to skip cassette validation (from x-airbyte-untested extension)",
    )


class EntityDefinition(BaseModel):
    """Definition of an API entity."""

    model_config = {"populate_by_name": True}

    name: str
    actions: list[Action]
    endpoints: dict[Action, EndpointDefinition]
    entity_schema: dict[str, Any] | None = Field(default=None, alias="schema")


class ConnectorModel(BaseModel):
    """Complete connector model loaded from YAML definition."""

    model_config = ConfigDict(use_enum_values=True)

    id: UUID
    name: str
    version: str = OPENAPI_DEFAULT_VERSION
    base_url: str
    auth: AuthConfig
    entities: list[EntityDefinition]
    openapi_spec: Any | None = None  # Optional reference to OpenAPIConnector
    retry_config: RetryConfig | None = None  # Optional retry configuration
