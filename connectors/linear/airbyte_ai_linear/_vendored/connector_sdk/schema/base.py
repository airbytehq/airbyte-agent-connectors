"""
Base OpenAPI 3.1 models: Info, Server, Contact, License.

References:
- https://spec.openapis.org/oas/v3.1.0#info-object
- https://spec.openapis.org/oas/v3.1.0#server-object
"""

from enum import StrEnum
from typing import Optional, Dict
from pydantic import BaseModel, Field, field_validator, ConfigDict
from pydantic_core import Url


class Contact(BaseModel):
    """
    Contact information for the API.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#contact-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None


class License(BaseModel):
    """
    License information for the API.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#license-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str
    url: Optional[str] = None


class DocUrlType(StrEnum):
    API_DEPRECATIONS = "api_deprecations"
    API_REFERENCE = "api_reference"
    API_RELEASE_HISTORY = "api_release_history"
    AUTHENTICATION_GUIDE = "authentication_guide"
    CHANGELOG = "changelog"
    DATA_MODEL_REFERENCE = "data_model_reference"
    DEVELOPER_COMMUNITY = "developer_community"
    MIGRATION_GUIDE = "migration_guide"
    OPENAPI_SPEC = "openapi_spec"
    OTHER = "other"
    PERMISSIONS_SCOPES = "permissions_scopes"
    RATE_LIMITS = "rate_limits"
    SQL_REFERENCE = "sql_reference"
    STATUS_PAGE = "status_page"


class DocUrl(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    url: str
    type: DocUrlType
    title: Optional[str] = None

    @field_validator("url")
    def validate_url(cls, v):
        Url(v)
        return v


class Info(BaseModel):
    """
    API metadata information.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#info-object

    Extensions:
    - x-airbyte-connector-name: Name of the connector (Airbyte extension)
    - x-airbyte-external-documentation-urls: List of external documentation URLs (Airbyte extension)
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    title: str
    version: str
    description: Optional[str] = None
    terms_of_service: Optional[str] = Field(None, alias="termsOfService")
    contact: Optional[Contact] = None
    license: Optional[License] = None

    # Airbyte extension
    x_airbyte_connector_name: Optional[str] = Field(
        None, alias="x-airbyte-connector-name"
    )
    x_airbyte_external_documentation_urls: list[DocUrl] = Field(
        ..., alias="x-airbyte-external-documentation-urls"
    )


class ServerVariable(BaseModel):
    """
    Variable for server URL templating.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#server-variable-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    enum: Optional[list[str]] = None
    default: str
    description: Optional[str] = None


class Server(BaseModel):
    """
    Server URL and variable definitions.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#server-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    url: str
    description: Optional[str] = None
    variables: Dict[str, ServerVariable] = Field(default_factory=dict)

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        """Validate that server URL is properly formatted."""
        if not v:
            raise ValueError("Server URL cannot be empty")
        # Allow both absolute URLs and relative paths
        return v
