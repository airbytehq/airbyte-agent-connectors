"""
Security scheme models for OpenAPI 3.1.

References:
- https://spec.openapis.org/oas/v3.1.0#security-scheme-object
- https://spec.openapis.org/oas/v3.1.0#oauth-flows-object
"""

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class OAuth2Flow(BaseModel):
    """
    OAuth 2.0 flow configuration.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#oauth-flow-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    authorization_url: Optional[str] = Field(None, alias="authorizationUrl")
    token_url: Optional[str] = Field(None, alias="tokenUrl")
    refresh_url: Optional[str] = Field(None, alias="refreshUrl")
    scopes: Dict[str, str] = Field(default_factory=dict)


class OAuth2Flows(BaseModel):
    """
    Collection of OAuth 2.0 flows.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#oauth-flows-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    implicit: Optional[OAuth2Flow] = None
    password: Optional[OAuth2Flow] = None
    client_credentials: Optional[OAuth2Flow] = Field(None, alias="clientCredentials")
    authorization_code: Optional[OAuth2Flow] = Field(None, alias="authorizationCode")


class AuthConfigFieldSpec(BaseModel):
    """
    Specification for a user-facing authentication config field.

    This defines a single input field that users provide for authentication.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    type: Literal["string", "integer", "boolean", "number"] = "string"
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None  # e.g., "email", "uri"
    pattern: Optional[str] = None  # Regex validation
    airbyte_secret: bool = Field(False, alias="airbyte_secret")
    default: Optional[Any] = None


class AuthConfigOption(BaseModel):
    """
    A single authentication configuration option.

    Defines user-facing fields and how they map to auth parameters.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    title: Optional[str] = None
    description: Optional[str] = None
    type: Literal["object"] = "object"
    required: List[str] = Field(default_factory=list)
    properties: Dict[str, AuthConfigFieldSpec] = Field(default_factory=dict)
    auth_mapping: Dict[str, str] = Field(
        default_factory=dict,
        description="Mapping from auth parameters (e.g., 'username', 'password', 'token') to template strings using ${field} syntax",
    )


class AirbyteAuthConfig(BaseModel):
    """
    Airbyte auth configuration extension (x-airbyte-auth-config).

    Defines user-facing authentication configuration and how it maps to
    the underlying OpenAPI security scheme.

    Either a single auth option or multiple options via oneOf.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Single option fields
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Literal["object"]] = None
    required: Optional[List[str]] = None
    properties: Optional[Dict[str, AuthConfigFieldSpec]] = None
    auth_mapping: Optional[Dict[str, str]] = None

    # Multiple options (oneOf)
    one_of: Optional[List[AuthConfigOption]] = Field(None, alias="oneOf")

    @model_validator(mode="after")
    def validate_config_structure(self) -> "AirbyteAuthConfig":
        """Validate that either single option or oneOf is provided, not both."""
        has_single = self.type is not None or self.properties is not None or self.auth_mapping is not None
        has_one_of = self.one_of is not None and len(self.one_of) > 0

        if not has_single and not has_one_of:
            raise ValueError("Either single auth option (type/properties/auth_mapping) or oneOf must be provided")

        if has_single and has_one_of:
            raise ValueError("Cannot have both single auth option and oneOf")

        if has_single:
            # Validate single option has required fields
            if self.type != "object":
                raise ValueError("Single auth option must have type='object'")
            if not self.properties:
                raise ValueError("Single auth option must have properties")
            if not self.auth_mapping:
                raise ValueError("Single auth option must have auth_mapping")

        return self


class SecurityScheme(BaseModel):
    """
    Security scheme definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#security-scheme-object

    Supported Types:
    - apiKey: API key in header/query/cookie
    - http: HTTP authentication (basic, bearer, digest, etc.)
    - oauth2: OAuth 2.0 flows

    Extensions:
    - x-airbyte-token-path: JSON path to extract token from auth response (Airbyte extension)
    - x-airbyte-token-refresh: OAuth2 token refresh configuration (dict with auth_style, body_format)
    - x-airbyte-auth-config: User-facing authentication configuration (Airbyte extension)

    Future extensions (not yet active):
    - x-grant-type: OAuth grant type for refresh tokens
    - x-refresh-endpoint: Custom refresh endpoint URL
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    # Standard OpenAPI fields
    type: Literal["apiKey", "http", "oauth2", "openIdConnect"]
    description: Optional[str] = None

    # apiKey specific
    name: Optional[str] = None
    in_: Optional[Literal["query", "header", "cookie"]] = Field(None, alias="in")

    # http specific
    scheme: Optional[str] = None  # e.g., "basic", "bearer", "digest"
    bearer_format: Optional[str] = Field(None, alias="bearerFormat")

    # oauth2 specific
    flows: Optional[OAuth2Flows] = None

    # openIdConnect specific
    open_id_connect_url: Optional[str] = Field(None, alias="openIdConnectUrl")

    # Airbyte extensions
    x_token_path: Optional[str] = Field(None, alias="x-airbyte-token-path")
    x_token_refresh: Optional[Dict[str, Any]] = Field(None, alias="x-airbyte-token-refresh")
    x_airbyte_auth_config: Optional[AirbyteAuthConfig] = Field(None, alias="x-airbyte-auth-config")
    x_airbyte_token_extract: Optional[List[str]] = Field(
        None,
        alias="x-airbyte-token-extract",
        description="List of fields to extract from OAuth2 token responses and use as server variables",
    )

    @field_validator("x_airbyte_token_extract", mode="after")
    @classmethod
    def validate_token_extract(cls, v: Optional[List[str]]) -> Optional[List[str]]:
        """Validate x-airbyte-token-extract has no duplicates."""
        if v is not None:
            if len(v) != len(set(v)):
                duplicates = [x for x in v if v.count(x) > 1]
                raise ValueError(f"x-airbyte-token-extract contains duplicate fields: {set(duplicates)}")
        return v

    # Future extensions (commented out, defined for future use)
    # x_grant_type: Optional[Literal["refresh_token", "client_credentials"]] = Field(None, alias="x-grant-type")
    # x_refresh_endpoint: Optional[str] = Field(None, alias="x-refresh-endpoint")

    @model_validator(mode="after")
    def validate_security_scheme(self) -> "SecurityScheme":
        """Validate that required fields are present based on security type."""
        if self.type == "apiKey":
            if not self.name or not self.in_:
                raise ValueError("apiKey type requires 'name' and 'in' fields")
        elif self.type == "http":
            if not self.scheme:
                raise ValueError("http type requires 'scheme' field")
        elif self.type == "oauth2":
            if not self.flows:
                raise ValueError("oauth2 type requires 'flows' field")
        elif self.type == "openIdConnect":
            if not self.open_id_connect_url:
                raise ValueError("openIdConnect type requires 'openIdConnectUrl' field")
        return self


# SecurityRequirement is a dict mapping security scheme name to list of scopes
SecurityRequirement = Dict[str, List[str]]
