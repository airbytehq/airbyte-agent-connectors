"""
Base OpenAPI 3.1 models: Info, Server, Contact, License.

References:
- https://spec.openapis.org/oas/v3.1.0#info-object
- https://spec.openapis.org/oas/v3.1.0#server-object
"""

from enum import StrEnum
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic_core import Url

from .extensions import CacheConfig, ReplicationConfig, RetryConfig


class ExampleQuestions(BaseModel):
    """
    Example questions for AI connector documentation.

    Used to generate supported_questions.md and unsupported_questions.md files
    that appear in the connector's README.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    supported: list[str] = Field(
        default_factory=list,
        description="Example questions the connector can handle",
    )
    unsupported: list[str] = Field(
        default_factory=list,
        description="Example questions the connector cannot handle",
    )


class Contact(BaseModel):
    """
    Contact information for the API.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#contact-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str | None = None
    url: str | None = None
    email: str | None = None


class License(BaseModel):
    """
    License information for the API.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#license-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str
    url: str | None = None


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
    title: str | None = None

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
    - x-airbyte-connector-id: UUID of the connector (Airbyte extension)
    - x-airbyte-external-documentation-urls: List of external documentation URLs (Airbyte extension)
    - x-airbyte-retry-config: Retry configuration for transient errors (Airbyte extension)
    - x-airbyte-example-questions: Example questions for AI connector README (Airbyte extension)
    - x-airbyte-cache: Cache configuration for field mapping between API and cache schemas (Airbyte extension)
    - x-airbyte-replication-config: Replication configuration for MULTI mode connectors (Airbyte extension)
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    title: str
    version: str
    description: str | None = None
    terms_of_service: str | None = Field(None, alias="termsOfService")
    contact: Contact | None = None
    license: License | None = None

    # Airbyte extension
    x_airbyte_connector_name: str | None = Field(None, alias="x-airbyte-connector-name")
    x_airbyte_connector_id: UUID | None = Field(None, alias="x-airbyte-connector-id")
    x_airbyte_external_documentation_urls: list[DocUrl] = Field(..., alias="x-airbyte-external-documentation-urls")
    x_airbyte_retry_config: RetryConfig | None = Field(None, alias="x-airbyte-retry-config")
    x_airbyte_example_questions: ExampleQuestions | None = Field(None, alias="x-airbyte-example-questions")
    x_airbyte_cache: CacheConfig | None = Field(None, alias="x-airbyte-cache")
    x_airbyte_replication_config: ReplicationConfig | None = Field(None, alias="x-airbyte-replication-config")


class ServerVariable(BaseModel):
    """
    Variable for server URL templating.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#server-variable-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    enum: list[str] | None = None
    default: str
    description: str | None = None


class EnvironmentMappingTransform(BaseModel):
    """
    Structured transform for environment mapping values.

    Allows transforming environment values before storing in source_config.

    Example:
        source: subdomain
        format: "{value}.atlassian.net"

    The format string uses {value} as a placeholder for the source value.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    source: str = Field(description="The environment config key to read the value from")
    format: str | None = Field(
        default=None,
        description="Optional format string to transform the value. Use {value} as placeholder.",
    )


# Type alias for environment mapping values: either a simple string (config key)
# or a structured transform with source and optional transform template
EnvironmentMappingValue = str | EnvironmentMappingTransform


class Server(BaseModel):
    """
    Server URL and variable definitions.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#server-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    url: str
    description: str | None = None
    variables: Dict[str, ServerVariable] = Field(default_factory=dict)
    x_airbyte_replication_environment_mapping: Dict[str, EnvironmentMappingValue] | None = Field(
        default=None,
        alias="x-airbyte-replication-environment-mapping",
    )
    x_airbyte_replication_environment_constants: Dict[str, Any] | None = Field(
        default=None,
        alias="x-airbyte-replication-environment-constants",
        description="Constant values to always inject at environment config paths (e.g., 'region': 'us-east-1')",
    )

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        """Validate that server URL is properly formatted."""
        if not v:
            raise ValueError("Server URL cannot be empty")
        # Allow both absolute URLs and relative paths
        return v
