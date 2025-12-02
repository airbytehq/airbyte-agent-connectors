"""
Security scheme models for OpenAPI 3.1.

References:
- https://spec.openapis.org/oas/v3.1.0#security-scheme-object
- https://spec.openapis.org/oas/v3.1.0#oauth-flows-object
"""

from typing import Optional, Dict, List, Literal
from pydantic import BaseModel, Field, model_validator, ConfigDict


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

    Future extensions (not yet active):
    - x-grant-type: OAuth grant type for refresh tokens
    - x-refresh-endpoint: Custom refresh endpoint URL
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

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
