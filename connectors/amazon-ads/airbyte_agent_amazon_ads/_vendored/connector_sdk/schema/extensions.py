"""
Extension models for future features.

These models are defined but NOT yet added to the main schema models.
They serve as:
1. Type hints for future use
2. Documentation of planned extensions
3. Ready-to-use structures when features are implemented

NOTE: These are not currently active in the schema. They will be added
to Operation, Schema, or other models when their respective features
are implemented.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class PaginationConfig(BaseModel):
    """
    Configuration for pagination support.

    NOT YET USED - Defined for future implementation.

    When active, will be added to Operation model as:
        x_pagination: Optional[PaginationConfig] = Field(None, alias="x-pagination")
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    style: Literal["cursor", "offset", "page", "link"]
    limit_param: str = "limit"

    # Cursor-based pagination
    cursor_param: str | None = None
    cursor_source: Literal["body", "headers"] | None = "body"
    cursor_path: str | None = None

    # Offset-based pagination
    offset_param: str | None = None

    # Page-based pagination
    page_param: str | None = None

    # Response parsing
    data_path: str = "data"
    has_more_path: str | None = None

    # Limits
    max_page_size: int | None = None
    default_page_size: int = 100


class RateLimitConfig(BaseModel):
    """
    Configuration for rate limiting.

    NOT YET USED - Defined for future implementation.

    When active, might be added to Server or root OpenAPIConnector as:
        x_rate_limit: Optional[RateLimitConfig] = Field(None, alias="x-rate-limit")
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    max_requests: int
    time_window_seconds: int
    retry_after_header: str | None = "Retry-After"
    respect_retry_after: bool = True


class RetryConfig(BaseModel):
    """
    Configuration for retry strategy with exponential backoff.

    Used to configure automatic retries for transient errors (429, 5xx, timeouts, network errors).
    Can be specified at the connector level via x-airbyte-retry-config in the OpenAPI spec's info section.

    By default, retries are enabled with max_attempts=3. To disable retries, set max_attempts=1
    in your connector's x-airbyte-retry-config.

    Example YAML usage:
        info:
          title: My API
          x-airbyte-retry-config:
            max_attempts: 5
            initial_delay_seconds: 2.0
            retry_after_header: "X-RateLimit-Reset"
            retry_after_format: "unix_timestamp"
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Core retry settings (max_attempts=3 enables retries by default)
    max_attempts: int = 3
    initial_delay_seconds: float = 1.0
    max_delay_seconds: float = 60.0
    exponential_base: float = 2.0
    jitter: bool = True

    # Which errors to retry
    retry_on_status_codes: list[int] = [429, 500, 502, 503, 504]
    retry_on_timeout: bool = True
    retry_on_network_error: bool = True

    # Header-based delay extraction
    retry_after_header: str = "Retry-After"
    retry_after_format: Literal["seconds", "milliseconds", "unix_timestamp"] = "seconds"


class CacheFieldProperty(BaseModel):
    """
    Nested property definition for object-type cache fields.

    Supports recursive nesting to represent complex nested schemas in cache field definitions.
    Used when a cache field has type 'object' and needs to define its internal structure.

    Example YAML usage:
        - name: collaboration
          type: ['null', 'object']
          description: "Collaboration data"
          properties:
            brief:
              type: ['null', 'string']
            comments:
              type: ['null', 'array']
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    type: str | list[str]
    properties: dict[str, "CacheFieldProperty"] | None = None


class CacheFieldConfig(BaseModel):
    """
    Field configuration for cache mapping.

    Defines a single field in a cache entity, with optional name aliasing
    to map between user-facing field names and cache storage names.

    For object-type fields, supports nested properties to define the internal structure
    of complex nested schemas.

    Used in x-airbyte-cache extension for api_search operations.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str
    x_airbyte_name: str | None = Field(default=None, alias="x-airbyte-name")
    type: str | list[str]
    description: str
    properties: dict[str, CacheFieldProperty] | None = None

    @property
    def cache_name(self) -> str:
        """Return cache name, falling back to name if alias not specified."""
        return self.x_airbyte_name or self.name


class CacheEntityConfig(BaseModel):
    """
    Entity configuration for cache mapping.

    Defines a cache-enabled entity with its fields and optional name aliasing
    to map between user-facing entity names and cache storage names.

    Used in x-airbyte-cache extension for api_search operations.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    entity: str
    x_airbyte_name: str | None = Field(default=None, alias="x-airbyte-name")
    fields: list[CacheFieldConfig]

    @property
    def cache_name(self) -> str:
        """Return cache entity name, falling back to entity if alias not specified."""
        return self.x_airbyte_name or self.entity


class ReplicationConfigProperty(BaseModel):
    """
    Property definition for replication configuration fields.

    Defines a single field in the replication configuration with its type,
    description, and optional default value.

    Example YAML usage:
        x-airbyte-replication-config:
          properties:
            start_date:
              type: string
              title: Start Date
              description: UTC date and time from which to replicate data
              format: date-time
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    type: str
    title: str | None = None
    description: str | None = None
    format: str | None = None
    default: str | int | float | bool | None = None
    enum: list[str] | None = None


class ReplicationConfig(BaseModel):
    """
    Replication configuration extension (x-airbyte-replication-config).

    Defines replication-specific settings for MULTI mode connectors that need
    to configure the underlying replication connector. This allows users who
    use the direct-style API (credentials + environment) to also specify
    replication settings like start_date, lookback_window, etc.

    This extension is added to the Info model and provides field definitions
    for replication configuration that gets merged into the source config
    when creating sources.

    Example YAML usage:
        info:
          title: HubSpot API
          x-airbyte-replication-config:
            title: Replication Configuration
            description: Settings for data replication
            properties:
              start_date:
                type: string
                title: Start Date
                description: UTC date and time from which to replicate data
                format: date-time
            required:
              - start_date
            replication_config_key_mapping:
              start_date: start_date
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    title: str | None = None
    description: str | None = None
    properties: dict[str, ReplicationConfigProperty] = Field(default_factory=dict)
    required: list[str] = Field(default_factory=list)
    replication_config_key_mapping: dict[str, str] = Field(
        default_factory=dict,
        alias="replication_config_key_mapping",
        description="Mapping from replication_config field names to source_config field names",
    )


class CacheConfig(BaseModel):
    """
    Cache configuration extension (x-airbyte-cache).

    Defines cache-enabled entities and their field mappings for api_search operations.
    Supports optional name aliasing via x-airbyte-name for both entities and fields,
    enabling bidirectional mapping between user-facing names and cache storage names.

    This extension is added to the Info model and provides field-level mapping for
    search operations that use cached data.

    Example YAML usage:
        info:
          title: Stripe API
          x-airbyte-cache:
            entities:
              - entity: customers
                stream: customers
                fields:
                  - name: email
                    type: ["null", "string"]
                    description: "Customer email address"
                  - name: customer_name
                    x-airbyte-name: name
                    type: ["null", "string"]
                    description: "Customer full name"
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    entities: list[CacheEntityConfig]

    def get_entity_mapping(self, user_entity: str) -> CacheEntityConfig | None:
        """
        Get entity config by user-facing name.

        Args:
            user_entity: User-facing entity name to look up

        Returns:
            CacheEntityConfig if found, None otherwise
        """
        for entity in self.entities:
            if entity.entity == user_entity:
                return entity
        return None
