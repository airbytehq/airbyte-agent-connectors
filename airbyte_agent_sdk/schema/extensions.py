"""
Extension models for connector configuration.

Provides Pydantic models for OpenAPI x-airbyte-* extensions:
- RetryConfig: retry strategy with exponential backoff
- CacheConfig / CacheEntityConfig / CacheFieldConfig: cache mapping for api_search
- ReplicationConfig: replication settings for MULTI mode connectors
- EntityRelationshipConfig: entity relationship declarations
- ScopingParamConfig: scoping parameter resolution from config
"""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt, model_validator

from airbyte_agent_sdk.schema.interpolation import resolve_interpolated_constants


class ExtensionAwareModel(BaseModel):
    """Base for models that parse registry-authored connector YAML.

    Accepts unknown ``x-*`` extension fields so that newer connector YAMLs
    (published to the registry independently of the backend) don't break
    older SDK versions.  Unknown non-extension fields are still rejected
    to preserve typo detection.
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
            raise ValueError(f"Unknown field(s) in {cls.__name__}: {unknown_standard}. Use an 'x-' prefix for custom extensions.")
        return data


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


class CacheFieldProperty(ExtensionAwareModel):
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

    type: str | list[str]
    properties: dict[str, "CacheFieldProperty"] | None = None


class SemanticSampling(BaseModel):
    """
    Sampling configuration for semantic search (the `sampling` block).

    Declares how a decoded field value is split into discrete units that get
    embedded. The `sample_type` makes the cardinality intent explicit:

    - ``element``: the field value is a structured collection; ``sample_path``
      anchors each unit and ``text_path`` selects the text leaves under that
      anchor.
    - ``regex``: the decoded text is split into units with ``split_pattern``.
    - ``whole``: the decoded value is a single unit (optionally with ``text_path``
      to pull text leaves out of a structured value).

    Used inside x-airbyte-semantic-search on a context-store field.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    sample_type: Literal["element", "regex", "whole"] = Field(
        description="Explicit cardinality intent for how the field value is split into units.",
    )
    unit_label: str = Field(
        default="chunk",
        description="Names the unit; drives table/column naming. Defaults to 'chunk'.",
    )
    sample_path: str | None = Field(
        default=None,
        description="element: anchor (relative to the field value) for each unit.",
    )
    text_path: str | None = Field(
        default=None,
        description="element/whole: path to text leaves under the anchor.",
    )
    stitch: str = Field(
        default="\n",
        description="Separator used to join multiple text leaves into a unit's text. Defaults to '\\n'.",
    )
    split_pattern: str | None = Field(
        default=None,
        description="regex: boundary pattern used to split the decoded text into samples.",
    )


class SemanticWindowing(BaseModel):
    """
    Windowing configuration for semantic search (the `windowing` block).

    Controls how much surrounding context is embedded alongside each unit.
    When ``context_max_chars`` is 0 or omitted, only the unit itself is embedded.

    Used inside x-airbyte-semantic-search on a context-store field.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    context_max_chars: int = Field(
        default=0,
        ge=0,
        description="Max characters of surrounding context to embed. 0/omitted => embed the unit only.",
    )
    context_boundary: Literal["whole_unit", "char", "regex"] = Field(
        default="whole_unit",
        description="How context is bounded around a unit. Defaults to 'whole_unit'.",
    )
    context_boundary_pattern: str | None = Field(
        default=None,
        description="Boundary pattern used when context_boundary is 'regex'.",
    )


class SemanticEmbedding(BaseModel):
    """
    Embedding configuration for semantic search (the `embedding` block).

    Used inside x-airbyte-semantic-search on a context-store field.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    model: str = Field(
        description="Embedding model identifier (e.g. 'text-embedding-3-small').",
    )


class SemanticMetadataField(BaseModel):
    """
    A single metadata field carried alongside each embedded unit.

    ``type`` MUST be ``string`` or ``array``. ``array`` is required when the
    metadata ``path`` resolves below the sample anchor (cardinality > 1 per
    unit) -- i.e. when the path yields multiple values for a single unit.

    Used inside x-airbyte-semantic-search on a context-store field.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str = Field(description="Metadata column name.")
    path: str = Field(
        description="Path to the metadata value relative to the sample anchor (a leading '/' resolves from the record root).",
    )
    type: Literal["string", "array"] = Field(
        default="string",
        description="Metadata value type. Use 'array' when the path resolves below the sample anchor (cardinality > 1 per unit); 'string' otherwise.",
    )


class SemanticSearchConfig(BaseModel):
    """
    Semantic search configuration extension (x-airbyte-semantic-search).

    Declares, per context-store field, how the raw field value is decoded,
    split into units, windowed, embedded, and what metadata travels with each
    unit. This is the annotation contract consumed by the semantic search
    engine.

    Example YAML usage (on a context-store field):
        x-airbyte-semantic-search:
          content_type: json
          sampling:
            sample_type: element
            unit_label: speaker_turn
            sample_path: "[]"
            text_path: "sentences[].text"
            stitch: "\\n"
          windowing:
            context_max_chars: 2048
            context_boundary: whole_unit
          embedding:
            model: text-embedding-3-small
          metadata:
            - { name: speakerId, path: "speakerId", type: string }
            - { name: callId, path: "/callId", type: string }
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    content_type: Literal["json", "html", "xhtml_storage", "adf", "markdown", "plaintext"] = Field(
        description="How to decode the raw field value before sampling.",
    )
    sampling: SemanticSampling
    windowing: SemanticWindowing = Field(default_factory=SemanticWindowing)
    embedding: SemanticEmbedding
    metadata: list[SemanticMetadataField] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_sampling_consistency(self) -> "SemanticSearchConfig":
        """Validate sample_type-specific field requirements at parse time."""
        sampling = self.sampling
        sample_type = sampling.sample_type
        if sample_type == "element":
            if not sampling.sample_path or not sampling.text_path:
                raise ValueError("x-airbyte-semantic-search: sampling.sample_type 'element' requires both 'sample_path' and 'text_path'.")
        elif sample_type == "regex":
            if not sampling.split_pattern:
                raise ValueError("x-airbyte-semantic-search: sampling.sample_type 'regex' requires 'split_pattern'.")
        elif sample_type == "whole":
            if sampling.sample_path or sampling.split_pattern:
                raise ValueError(
                    "x-airbyte-semantic-search: sampling.sample_type 'whole' must not set "
                    "'sample_path' or 'split_pattern' (only an optional 'text_path' is allowed)."
                )
        if self.windowing.context_boundary == "regex" and not self.windowing.context_boundary_pattern:
            raise ValueError("x-airbyte-semantic-search: windowing.context_boundary 'regex' requires 'context_boundary_pattern'.")
        return self


class CacheFieldConfig(ExtensionAwareModel):
    """
    Field configuration for cache mapping.

    Defines a single field in a cache entity, with optional name aliasing
    to map between user-facing field names and cache storage names.

    For object-type fields, supports nested properties to define the internal structure
    of complex nested schemas.

    Used in x-airbyte-context-store extension for api_search operations.
    """

    name: str
    x_airbyte_name: str | None = Field(default=None, alias="x-airbyte-name")
    type: str | list[str]
    description: str
    properties: dict[str, CacheFieldProperty] | None = None
    x_airbyte_semantic_search: SemanticSearchConfig | None = Field(
        default=None,
        alias="x-airbyte-semantic-search",
        description="Semantic search annotation for this field (dormant contract; "
        "describes how the field value is decoded, sampled, windowed, embedded, "
        "and what metadata travels with each unit).",
    )

    @property
    def cache_name(self) -> str:
        """Return cache name, falling back to name if alias not specified."""
        return self.x_airbyte_name or self.name


class CacheEntityConfig(ExtensionAwareModel):
    """
    Entity configuration for cache mapping.

    Defines a cache-enabled entity with its fields and optional name aliasing
    to map between user-facing entity names and cache storage names.

    Used in x-airbyte-context-store extension for api_search operations.
    """

    entity: str
    suggested: bool = Field(
        default=False,
        description="Whether this entity should be suggested for syncing by default.",
    )
    x_airbyte_name: str | None = Field(default=None, alias="x-airbyte-name")
    fields: list[CacheFieldConfig] = Field(default_factory=list)
    x_airbyte_skip_searchable_fields: str | None = Field(
        default=None,
        alias="x-airbyte-skip-searchable-fields",
        description="Reason why this entity does not define searchable fields. "
        "Entities in x-airbyte-context-store must either declare at least one field "
        "or set x-airbyte-skip-searchable-fields with a justification.",
    )

    @property
    def cache_name(self) -> str:
        """Return cache entity name, falling back to entity if alias not specified."""
        return self.x_airbyte_name or self.entity


class ReplicationConfigPropertyItems(BaseModel):
    """
    Items definition for array-type replication configuration fields.

    Defines the schema for items in an array-type replication config property.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    type: str


class ReplicationConfigProperty(BaseModel):
    """
    Property definition for replication configuration fields.

    Defines a single field in the replication configuration with its type,
    description, and optional default value. Supports both simple types
    (string, integer, boolean) and array types.

    Example YAML usage:
        x-airbyte-replication-config:
          properties:
            start_date:
              type: string
              title: Start Date
              description: UTC date and time from which to replicate data
              format: date-time
            account_ids:
              type: array
              title: Account IDs
              description: List of account IDs to replicate
              items:
                type: string
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    type: str
    title: str | None = None
    description: str | None = None
    format: str | None = None
    default: str | int | float | bool | list | None = None
    enum: list[str] | None = None
    items: ReplicationConfigPropertyItems | None = None


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
    replication_config_constants: dict[str, str | int | float | bool] = Field(
        default_factory=dict,
        alias="replication_config_constants",
        description="System-set constant values injected into the Airbyte source config; never shown in the user-facing form",
    )

    def resolved_constants(self) -> dict[str, Any]:
        """Return `replication_config_constants` with Jinja2 date expressions evaluated."""
        return resolve_interpolated_constants(self.replication_config_constants)

    @model_validator(mode="after")
    def validate_replication_config_key_mapping(self) -> "ReplicationConfig":
        """Validate that replication_config_key_mapping keys exist in properties.

        The mapping is: {local_key: airbyte_path}
        We validate that local_key exists in our properties.
        """
        if self.replication_config_key_mapping and self.properties:
            property_names = set(self.properties.keys())
            for local_key, airbyte_path in self.replication_config_key_mapping.items():
                if local_key not in property_names:
                    available = ", ".join(sorted(property_names)) if property_names else "(none)"
                    raise ValueError(
                        f"replication_config_key_mapping: local key '{local_key}' "
                        f"(mapped to '{airbyte_path}') not found in properties. Available: {available}"
                    )
        return self


class CacheConfig(ExtensionAwareModel):
    """
    Cache configuration extension (x-airbyte-context-store).

    Defines cache-enabled entities and their field mappings for api_search operations.
    Supports optional name aliasing via x-airbyte-name for both entities and fields,
    enabling bidirectional mapping between user-facing names and cache storage names.

    This extension is added to the Info model and provides field-level mapping for
    search operations that use cached data.

    Example YAML usage:
        info:
          title: Stripe API
          x-airbyte-context-store:
            flush_batch_size_mb: 200
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

    entities: list[CacheEntityConfig]
    disable_compaction: bool = Field(
        default=False,
        alias="disable_compaction",
        description="When true, Athena compaction (OPTIMIZE + VACUUM) is skipped for this connector type.",
    )
    flush_batch_size_mb: StrictInt | None = Field(
        default=None,
        ge=1,
        le=500,
        description="Optional flush batch size, in MB, for Airbyte-hosted Context Store destination writes.",
    )

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


class EntityRelationshipConfig(BaseModel):
    """
    Entity relationship declaration for cross-entity navigation.

    Defines a foreign-key relationship between two entities, enabling
    the runtime to resolve parent-child dependencies and provide
    relationship metadata to agents.

    Used in x-airbyte-entity-relationships extension in the Info object.

    Example YAML usage:
        info:
          title: My API
          x-airbyte-entity-relationships:
            - source_entity: contacts
              target_entity: accounts
              foreign_key: account_id
              cardinality: many_to_one
              description: "Contact belongs to an account"
    """

    model_config = ConfigDict(extra="forbid")

    source_entity: str = Field(description="Entity that holds the foreign key")
    target_entity: str = Field(description="Entity being referenced")
    foreign_key: str = Field(description="Field on source_entity that references target_entity")
    target_key: str = Field(default="id", description="Field on target_entity being referenced")
    cardinality: Literal["one_to_one", "one_to_many", "many_to_one", "many_to_many"] | None = Field(
        None, description="Optional relationship cardinality"
    )
    description: str | None = Field(None, description="Human-readable description of the relationship")
    parent_record_filter: dict[str, list[str]] | None = Field(
        None,
        description=(
            "Optional filter applied to parent entity records during check-time "
            "parameter resolution. Keys are field names on the parent record, values "
            "are lists of acceptable values. Only records matching all conditions are "
            "considered when resolving the foreign key. Example: "
            "`parent_record_filter: {type: [list, board]}` picks only parent records "
            "whose `type` field is `list` or `board`."
        ),
    )

    def format_line(self) -> str:
        """Format as a human-readable line for tool descriptions."""
        line = f"{self.source_entity} -> {self.target_entity} (via {self.foreign_key}"
        if self.cardinality:
            line += f", {self.cardinality.replace('_', '-')}"
        line += ")"
        if self.description:
            line += f" -- {self.description}"
        return line


class ScopingParamConfig(BaseModel):
    """Scoping parameter resolution from connector configuration.

    Declares a path parameter that should be resolved from the connector's
    `config_values` at runtime, rather than being supplied per-request.
    The resolution applies to **all executor operations** — `execute()`,
    `execute_batch()`, `check_entities()`, and download operations — not
    only probe/check calls.

    When a path template contains a placeholder matching `param`, the
    executor looks up `config_key` (defaulting to `param`) in
    `config_values` and injects the value automatically.  Explicitly
    supplied `params` always take precedence over the scoped default.

    Used in `x-airbyte-scoping` extension in the Info object.

    Example YAML usage:

        info:
          title: My API
          x-airbyte-scoping:
            - param: account_id
              config_key: account_id
    """

    model_config = ConfigDict(extra="forbid")

    param: str = Field(description="Path parameter name to resolve from config")
    config_key: str | None = Field(None, description="Config key to read. Defaults to param name if omitted.")
