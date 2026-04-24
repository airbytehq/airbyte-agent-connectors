"""
Base OpenAPI 3.1 models: Info, Server, Contact, License.

References:
- https://spec.openapis.org/oas/v3.1.0#info-object
- https://spec.openapis.org/oas/v3.1.0#server-object
"""

from enum import StrEnum
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from pydantic_core import Url

from airbyte_agent_sdk.schema.extensions import CacheConfig, EntityRelationshipConfig, ReplicationConfig, RetryConfig, ScopingParamConfig


class ExampleQuestions(BaseModel):
    """
    Example questions for AI connector documentation.

    Used to generate supported_questions.md and unsupported_questions.md files
    that appear in the connector's README.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    direct: list[str] = Field(
        default_factory=list,
        description="Example questions answerable via direct API operations",
    )
    context_store_search: list[str] = Field(
        default_factory=list,
        description="Example questions requiring cached context store search operations",
    )
    search: list[str] = Field(
        default_factory=list,
        description="Deprecated alias for context_store_search example questions",
    )
    unsupported: list[str] = Field(
        default_factory=list,
        description="Example questions the connector cannot handle",
    )

    @model_validator(mode="after")
    def sync_legacy_search_questions(self) -> "ExampleQuestions":
        if not self.context_store_search and self.search:
            self.context_store_search = list(self.search)
        return self


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


class ResponseErrorCheck(BaseModel):
    """
    Configuration for detecting application-level errors returned with HTTP 200 status.

    Some APIs (e.g. Slack) return errors as JSON bodies with HTTP 200 instead of using
    HTTP error status codes. This extension allows connectors to declare how to detect
    such errors.

    Example (Slack):
        x-airbyte-response-error-check:
          field: "ok"
          on_value: false
          message_field: "error"
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    field: str
    on_value: Any
    message_field: str | None = None


class Info(BaseModel):
    """
    API metadata information.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#info-object

    Unknown ``x-*`` fields are accepted so that older SDK versions can still parse
    specs that carry newer Airbyte extensions. Unknown non-extension fields still
    raise — that's where typos in standard OpenAPI keys get caught.

    Extensions:
    - x-airbyte-connector-name: Name of the connector (Airbyte extension)
    - x-airbyte-connector-definition-id: UUID of the connector (Airbyte extension)
    - x-airbyte-external-documentation-urls: List of external documentation URLs (Airbyte extension)
    - x-airbyte-retry-config: Retry configuration for transient errors (Airbyte extension)
    - x-airbyte-example-questions: Example questions for AI connector README (Airbyte extension)
    - x-airbyte-auth-tooltip: Short, non-technical multiline string shown to end users in the embedded widget to describe how to authenticate the connector (Airbyte extension)
    - x-airbyte-context-store: Cache configuration for field mapping between API and cache schemas (Airbyte extension)
    - x-airbyte-replication-config: Replication configuration for MULTI mode connectors (Airbyte extension)
    - x-airbyte-entity-relationships: Entity relationship declarations (Airbyte extension)
    - x-airbyte-scoping: Scoping parameter resolution from config (Airbyte extension)
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    @model_validator(mode="before")
    @classmethod
    def _reject_unknown_non_extension_fields(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data
        known: set[str] = set()
        for field_name, field_info in cls.model_fields.items():
            known.add(field_name)
            if field_info.alias:
                known.add(field_info.alias)
        unknown_standard = sorted(k for k in data if k not in known and not k.startswith("x-"))
        if unknown_standard:
            raise ValueError(f"Unknown field(s) in Info: {unknown_standard}. Use an 'x-' prefix for custom extensions.")
        return data

    title: str
    version: str
    description: str | None = None
    terms_of_service: str | None = Field(None, alias="termsOfService")
    contact: Contact | None = None
    license: License | None = None

    # Airbyte extension
    x_airbyte_connector_name: str | None = Field(None, alias="x-airbyte-connector-name")
    x_airbyte_connector_definition_id: UUID | None = Field(None, alias="x-airbyte-connector-definition-id")
    x_airbyte_external_documentation_urls: list[DocUrl] = Field(..., alias="x-airbyte-external-documentation-urls")
    x_airbyte_retry_config: RetryConfig | None = Field(None, alias="x-airbyte-retry-config")
    x_airbyte_example_questions: ExampleQuestions | None = Field(None, alias="x-airbyte-example-questions")
    x_airbyte_auth_tooltip: str | dict[str, str] | None = Field(
        default=None,
        alias="x-airbyte-auth-tooltip",
        description="Short, non-technical guidance on how to authenticate the connector, shown to end "
        "users in the embedded widget. Provide a single multiline string to show the same message for "
        "every auth method, or a mapping keyed by the credentials discriminator value (e.g. the const "
        "on `credentials.auth_type` or `credentials.option_title`) to show a different message per "
        "auth method.",
    )
    x_airbyte_context_store: CacheConfig | None = Field(None, alias="x-airbyte-context-store")
    x_airbyte_entity_relationships: list[EntityRelationshipConfig] = Field(default_factory=list, alias="x-airbyte-entity-relationships")
    x_airbyte_scoping: list[ScopingParamConfig] = Field(default_factory=list, alias="x-airbyte-scoping")
    x_airbyte_replication_config: ReplicationConfig | None = Field(None, alias="x-airbyte-replication-config")
    x_airbyte_replication_version: str | None = Field(
        default=None,
        alias="x-airbyte-replication-version",
        description="Airbyte replication connector version this connector was validated against",
    )
    x_airbyte_replication_compatibility: str | None = Field(
        default=None,
        alias="x-airbyte-replication-compatibility",
        description="Semver range of compatible replication connector versions",
    )
    x_airbyte_skip_suggested_streams: list[str] = Field(
        default_factory=list,
        alias="x-airbyte-skip-suggested-streams",
        description="List of Airbyte suggested streams to skip when validating cache entity coverage",
    )
    x_airbyte_skip_auth_methods: list[str] = Field(
        default_factory=list,
        alias="x-airbyte-skip-auth-methods",
        description="List of Airbyte auth methods to skip when validating auth compatibility "
        "and filtering auth options from the connector spec UI. "
        "Use the SelectiveAuthenticator option key (e.g., 'Private App Credentials', 'oauth2.0')",
    )
    x_airbyte_skip_context_store: str | None = Field(
        default=None,
        alias="x-airbyte-skip-context-store",
        description="Reason why this connector does not define x-airbyte-context-store. "
        "Connectors must have either x-airbyte-context-store or x-airbyte-skip-context-store with a justification.",
    )
    x_airbyte_response_error_check: ResponseErrorCheck | None = Field(
        default=None,
        alias="x-airbyte-response-error-check",
        description="Configuration for detecting application-level errors returned with HTTP 200 status. "
        "Checks a field in the response body and raises an error when the field matches on_value.",
    )


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

    @model_validator(mode="after")
    def validate_replication_environment_mapping(self) -> "Server":
        """Validate that x-airbyte-replication-environment-mapping sources exist in variables.

        For simple mappings like {"subdomain": "subdomain"}, the key is the source variable.
        For transform mappings like {"domain": {"source": "subdomain", "format": "..."}},
        the "source" field is the source variable.
        """
        env_mapping = self.x_airbyte_replication_environment_mapping
        if not env_mapping or not self.variables:
            return self

        variable_names = set(self.variables.keys())

        for env_key, mapping_value in env_mapping.items():
            if isinstance(mapping_value, str):
                source_var = env_key
            elif isinstance(mapping_value, EnvironmentMappingTransform):
                source_var = mapping_value.source
            else:
                continue

            if source_var not in variable_names:
                available = ", ".join(sorted(variable_names)) if variable_names else "(none)"
                raise ValueError(
                    f"x-airbyte-replication-environment-mapping: source variable '{source_var}' not found in server variables. Available: {available}"
                )

        return self
