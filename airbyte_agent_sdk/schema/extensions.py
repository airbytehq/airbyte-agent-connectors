"""
Extension models for connector configuration.

Provides Pydantic models for OpenAPI x-airbyte-* extensions:
- RetryConfig: retry strategy with exponential backoff
- CacheConfig / CacheEntityConfig / CacheFieldConfig: cache mapping for api_search
- ReplicationConfig: replication settings for MULTI mode connectors
- EntityRelationshipConfig: entity relationship declarations
- ScopingParamConfig: scoping parameter resolution from config
"""

import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator, model_validator

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
    text_content_type: Literal["plaintext", "html"] = Field(
        default="plaintext",
        description="element/whole: how each text leaf selected by 'text_path' is decoded. Defaults to 'plaintext'.",
    )
    stitch: str = Field(
        default="\n",
        description="Separator used to join multiple text leaves into a unit's text. Defaults to '\\n'.",
    )
    split_pattern: str | None = Field(
        default=None,
        description="regex: boundary pattern used to split the decoded text into samples.",
    )


class SemanticSampleLookup(BaseModel):
    """
    Lookup supplying a scalar sample's value from a related record.

    The embedding engine resolves the value with a join over raw rows: for each
    record, the related record whose `foreign` column equals this record's `local`
    column is located (one related record per foreign value, latest version), and
    its `from` column becomes the sample's value. A record whose `local` column is
    null or unmatched resolves to no value.

    The lookup side is this record's own stream (a self-join), and a record that
    is its own sibling resolves to no value; a lookup may only reference the same stream.

    `from` may be a dotted path (e.g. `profile.real_name`): the first segment is
    the lookup-side column, and the remaining segments resolve within its value.

    Used inside a scalar SemanticSample in place of `path`.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    local: str = Field(
        min_length=1,
        description="Column on this record whose value identifies the related record.",
    )
    foreign: str = Field(
        min_length=1,
        description="Column on the related record matched against 'local'.",
    )
    source: str = Field(
        alias="from",
        min_length=1,
        description="Column on the related record supplying the sample's value; a dotted path resolves nested values within that column.",
    )

    @field_validator("local", "foreign", "source")
    @classmethod
    def _require_path_segment(cls, value: str) -> str:
        # Every segment must be non-empty, not merely one of them: `local`/`foreign` reach the
        # embedding job as literal column names, so a stray separator ("thread_ts.", ".ts")
        # yields a column that cannot exist and fails every embedding run for the connector.
        if not value or any(not segment.strip() for segment in value.split(".")):
            raise ValueError(f"lookup paths must not contain empty segments, got {value!r}")
        return value


class SemanticSample(BaseModel):
    """
    A single sample contributing to a semantic-search field's embedded text.

    A field declares a list of samples. Exactly one sample is ``windowed`` -- it
    carries the ``sampling`` block that splits the decoded field value into the
    units that get embedded and that drives table/column naming. Every other
    sample is scalar: it resolves a single value -- from this record via `path`,
    or from a related record via `lookup` -- and is rendered into the embedding
    template alongside the windowed text.

    Used inside x-airbyte-semantic-search on a context-store field.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str = Field(
        description="Template key for this sample; must be unique across the field's samples.",
    )
    path: str | None = Field(
        default=None,
        description="Scalar samples only: path to the record-level value (a leading '/' resolves from the record root).",
    )
    lookup: SemanticSampleLookup | None = Field(
        default=None,
        description="Scalar samples only: resolve the value from a related record (mutually exclusive with 'path').",
    )
    max_chars: int | None = Field(
        default=None,
        ge=1,
        description="Scalar samples only: hard cap on the resolved value's length; longer values are "
        "truncated before templating, with an ellipsis appended to mark the cut.",
    )
    prefix: str | None = Field(
        default=None,
        description="Scalar samples only: literal prepended to the resolved value, only when it is non-empty.",
    )
    suffix: str | None = Field(
        default=None,
        description="Scalar samples only: literal appended to the resolved value, only when it is non-empty.",
    )
    windowed: bool = Field(
        default=False,
        description="Whether this sample is the windowed sample (exactly one per field).",
    )
    sampling: SemanticSampling | None = Field(
        default=None,
        description="Windowed sample only: how the decoded field value is split into units.",
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
    template: str | None = Field(
        default=None,
        description="Template for the embedded context text. Each '{name}' placeholder is replaced "
        "with the named sample's value (the windowed sample's window text, or a scalar sample's "
        "resolved value). A '{a|b|c}' placeholder renders the first named scalar sample that "
        "resolves non-empty, so mutually-exclusive-by-convention samples never double-render. "
        "Required when there are >=2 samples; forbidden for a single sample "
        "(which defaults to '{<windowed name>}').",
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


# A template placeholder is a brace group wrapping a bare identifier, or a '|'-separated group of
# identifiers (first-non-empty precedence). Sample names are constrained to the same identifier
# grammar, so this matches the renderer's "brace group whose inner names are all declared sample
# names" rule exactly -- any other brace group (e.g. a JSON-like literal) is left as literal text
# by both the validator and the renderer.
_TEMPLATE_PLACEHOLDER_RE = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*(?:\|[A-Za-z_][A-Za-z0-9_]*)*)\}")
_SAMPLE_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_ENRICHMENT_ARRAY_TOKEN_RE = re.compile(r"^(?P<key>[^\[]*)\[\](?P<rest>.*)$")
_SEMANTIC_COMPUTED_OUTPUT_NAMES = {"context", "score"}


def _validate_semantic_filter_column_name(name: str, *, label: str) -> None:
    if name.casefold() in _SEMANTIC_COMPUTED_OUTPUT_NAMES:
        raise ValueError(f"x-airbyte-semantic-search: {label} '{name}' conflicts with a computed search output.")
    if "." in name:
        raise ValueError(f"x-airbyte-semantic-search: {label} '{name}' must not contain '.'.")


def _reserved_window_chars(context_max_chars: int) -> int:
    """Chars reserved for the windowed sample so template overhead cannot starve it (half the cap).

    MUST stay in sync with backend ``semantic_chunking._reserved_window_chars``: this validator
    bounds the template's fixed text against this reserve, and the runtime trims scalar values
    against the same reserve, so together they guarantee the windowed sample is always embeddable.
    """
    return max(1, context_max_chars // 2)


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
          samples:
            - name: speaker_turn
              windowed: true
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

    content_type: Literal["json", "html", "xhtml_storage", "adf", "markdown", "plaintext", "document"] = Field(
        description="How to decode the raw field value before sampling.",
    )
    samples: list[SemanticSample]
    windowing: SemanticWindowing = Field(default_factory=SemanticWindowing)
    embedding: SemanticEmbedding
    metadata: list[SemanticMetadataField] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_samples_consistency(self) -> "SemanticSearchConfig":
        """Validate the samples list, the windowed sample's sampling, and the embedding template."""
        for metadata_field in self.metadata:
            _validate_semantic_filter_column_name(metadata_field.name, label="metadata name")

        samples = self.samples
        if not samples:
            raise ValueError("x-airbyte-semantic-search: 'samples' must declare at least one sample.")

        names = [sample.name for sample in samples]
        if len(names) != len(set(names)):
            raise ValueError("x-airbyte-semantic-search: sample 'name's must be unique.")
        bad_names = sorted(name for name in names if not _SAMPLE_NAME_RE.match(name))
        if bad_names:
            raise ValueError(
                f"x-airbyte-semantic-search: sample name(s) {bad_names} must be identifiers "
                "([A-Za-z_][A-Za-z0-9_]*) so they are unambiguous as '{name}' template placeholders."
            )

        windowed_samples = [sample for sample in samples if sample.windowed]
        if len(windowed_samples) != 1:
            raise ValueError("x-airbyte-semantic-search: exactly one sample must set 'windowed: true'.")
        windowed = windowed_samples[0]

        if windowed.sampling is None:
            raise ValueError("x-airbyte-semantic-search: the windowed sample must declare a 'sampling' block.")
        if not windowed.sampling.unit_label:
            raise ValueError("x-airbyte-semantic-search: unit label must not be empty.")
        _validate_semantic_filter_column_name(windowed.sampling.unit_label, label="unit label")
        if windowed.path is not None:
            raise ValueError("x-airbyte-semantic-search: the windowed sample must not set 'path'.")
        if windowed.lookup is not None:
            raise ValueError("x-airbyte-semantic-search: the windowed sample must not set 'lookup'.")
        if windowed.max_chars is not None:
            raise ValueError("x-airbyte-semantic-search: the windowed sample must not set 'max_chars' (use windowing.context_max_chars).")
        if windowed.prefix is not None or windowed.suffix is not None:
            raise ValueError("x-airbyte-semantic-search: the windowed sample must not set 'prefix' or 'suffix' (put literals in the template).")

        for sample in samples:
            if sample is windowed:
                continue
            if (sample.path is None) == (sample.lookup is None):
                raise ValueError(f"x-airbyte-semantic-search: scalar sample '{sample.name}' must set exactly one of 'path' or 'lookup'.")
            if sample.sampling is not None:
                raise ValueError(f"x-airbyte-semantic-search: scalar sample '{sample.name}' must not set 'sampling'.")

        sampling = windowed.sampling
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
        if sampling.text_content_type != "plaintext":
            if sample_type == "regex":
                raise ValueError(
                    "x-airbyte-semantic-search: sampling.text_content_type is not supported for "
                    "sample_type 'regex' (regex sampling splits the container text and never reads text leaves)."
                )
            if not sampling.text_path:
                raise ValueError("x-airbyte-semantic-search: sampling.text_content_type requires 'text_path' (it decodes the selected text leaves).")
            if self.content_type != "json":
                raise ValueError(
                    "x-airbyte-semantic-search: sampling.text_content_type requires content_type 'json' "
                    "(other content types decode to a string, so 'text_path' resolves no leaves and the record embeds nothing)."
                )

        if self.windowing.context_boundary == "regex" and not self.windowing.context_boundary_pattern:
            raise ValueError("x-airbyte-semantic-search: windowing.context_boundary 'regex' requires 'context_boundary_pattern'.")

        # A same-stream lookup is executed as a self-join that excludes the sibling whose foreign
        # value equals the base row's record key -- only meaningful when the foreign column IS that
        # record key. The embedding engine rejects any other foreign column at run time, so without
        # the same check here a connector validates and ships yet fails every embedding run.
        lookup_samples = [sample for sample in samples if sample.lookup is not None]
        record_key = next((meta.name for meta in self.metadata if meta.path.startswith("/")), None)
        if lookup_samples and record_key is None:
            raise ValueError("x-airbyte-semantic-search: same-stream lookup samples require record-root ('/') metadata declaring the record key.")
        mismatched_self_lookups = sorted(
            sample.name for sample in lookup_samples if sample.lookup is not None and sample.lookup.foreign != record_key
        )
        if mismatched_self_lookups:
            raise ValueError(
                f"x-airbyte-semantic-search: same-stream lookup sample(s) {mismatched_self_lookups} must set 'foreign' "
                f"to the record key column ('{record_key}')."
            )

        template = self.embedding.template
        if len(samples) >= 2:
            if template is None:
                raise ValueError("x-airbyte-semantic-search: embedding.template is required when there are 2 or more samples.")
        elif template is not None:
            raise ValueError("x-airbyte-semantic-search: embedding.template is forbidden for a single sample (it defaults to '{<windowed name>}').")

        if template is not None:
            # Only brace groups wrapping a declared identifier are placeholders; every other brace
            # group (JSON-like literals, etc.) is left untouched by the renderer, so it must not be
            # flagged here -- matching the renderer keeps validation and rendering consistent.
            groups = [reference.split("|") for reference in _TEMPLATE_PLACEHOLDER_RE.findall(template)]
            declared = set(names)
            unknown = sorted({name for group in groups for name in group} - declared)
            if unknown:
                raise ValueError(f"x-airbyte-semantic-search: embedding.template references undeclared sample name(s): {unknown}.")
            if any(windowed.name in group for group in groups if len(group) > 1):
                raise ValueError(
                    f"x-airbyte-semantic-search: the windowed sample '{windowed.name}' must not appear in a "
                    "'{a|b}' precedence group (its window text is always rendered)."
                )
            windowed_references = sum(group.count(windowed.name) for group in groups)
            if windowed_references == 0:
                raise ValueError(f"x-airbyte-semantic-search: embedding.template must reference the windowed sample '{windowed.name}'.")
            # The windowed sample is the only variable-length input; the window budget is derived by
            # rendering the template once with the windowed placeholder empty. A second occurrence
            # would be filled with the full window text again, doubling the windowed length past
            # context_max_chars and getting hard-truncated -- so it must appear exactly once.
            if windowed_references > 1:
                raise ValueError(
                    f"x-airbyte-semantic-search: embedding.template must reference the windowed sample "
                    f"'{windowed.name}' exactly once (found {windowed_references})."
                )
            # Bound the template's fixed text so the windowed sample always has room. Scalar VALUES
            # are trimmed at runtime, but the literal text (template minus its placeholders) is fixed;
            # if it alone exceeds the non-reserved budget, no runtime trimming can keep the windowed
            # text from being truncated away. Reject at parse time instead.
            context_max_chars = self.windowing.context_max_chars
            if context_max_chars > 0:
                literal_text = _TEMPLATE_PLACEHOLDER_RE.sub(
                    lambda match: "" if all(name in declared for name in match.group(1).split("|")) else match.group(0),
                    template,
                )
                max_overhead = context_max_chars - _reserved_window_chars(context_max_chars)
                if len(literal_text) > max_overhead:
                    raise ValueError(
                        f"x-airbyte-semantic-search: embedding.template fixed text ({len(literal_text)} chars) leaves too "
                        f"little of windowing.context_max_chars ({context_max_chars}) for the windowed sample "
                        f"'{windowed.name}'; it must not exceed {max_overhead} chars."
                    )

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

    @model_validator(mode="after")
    def validate_semantic_search_field_name(self) -> "CacheFieldConfig":
        if self.x_airbyte_semantic_search is not None:
            # The physical Context Store column (`x-airbyte-name` when aliased) is what
            # semantic search filters on, so that is the name that must be filter-safe.
            _validate_semantic_filter_column_name(self.cache_name, label="source field name")
        return self

    @property
    def cache_name(self) -> str:
        """Return cache name, falling back to name if alias not specified."""
        return self.x_airbyte_name or self.name


class EnrichmentMatch(BaseModel):
    """
    A single join condition for an enrichment (the `match` block entries).

    ``local`` is a path into the record being read (a leading '/' resolves from
    the record root; otherwise relative to the record). ``foreign`` is a path
    into a target-entity row; a path containing an array segment (e.g.
    ``parties[].speakerId``) is matched element-wise in Python, while a top-level
    scalar path (e.g. ``id``) bounds the lookup query's ``WHERE ... IN``.

    Used inside x-airbyte-enrichment on a context-store entity.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    local: str = Field(description="Path to the join key on the record being read.")
    foreign: str = Field(description="Path to the join key on the target-entity row.")


class EnrichmentProjection(BaseModel):
    """
    A single field projected from the target entity onto the record (the
    `project` block entries).

    ``from`` resolves relative to the matched target row (or the matched array
    element when it shares an array prefix with a match condition).

    Used inside x-airbyte-enrichment on a context-store entity.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str = Field(description="Output field name added to the record.")
    from_: str = Field(
        alias="from",
        description="Path to the value on the target entity to project.",
    )


class EnrichmentConfig(BaseModel):
    """
    A single query-time enrichment join (an entry of x-airbyte-enrichment).

    Declares that rows of the entity are decorated at read time by looking up
    fields from another context-store entity (``target``), joined on one or more
    ``match`` conditions, projecting ``project`` fields onto each record. The
    lookup runs over the result set at read time (never a build-time pre-join).

    Example YAML usage (on a context-store entity):
        x-airbyte-enrichment:
          - target: calls_extensive
            match:
              - { local: "/callId",  foreign: "id" }
              - { local: "speakerId", foreign: "parties[].speakerId" }
            project:
              - { name: speakerName, from: "parties[].name" }
              - { name: speakerRole, from: "parties[].title" }
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    target: str = Field(description="Target context-store entity to look up.")
    match: list[EnrichmentMatch] = Field(description="Join conditions (AND-ed).")
    project: list[EnrichmentProjection] = Field(description="Fields to project onto each record.")

    @model_validator(mode="after")
    def validate_non_empty(self) -> "EnrichmentConfig":
        """Require a target and at least one match condition and one projection."""
        if not self.target:
            raise ValueError("x-airbyte-enrichment: 'target' must be a non-empty entity name.")
        if not self.match:
            raise ValueError("x-airbyte-enrichment: at least one 'match' condition is required.")
        if not self.project:
            raise ValueError("x-airbyte-enrichment: at least one 'project' field is required.")
        return self


def combined_reference_pattern(pattern: str, specials_pattern: str | None) -> str:
    """Alternation the rewriter matches with: id-bearing tokens first, then id-less specials.

    Each half is wrapped so a top-level ``|`` inside either one cannot bind across the join.
    """
    if specials_pattern is None:
        return pattern
    return f"(?:{pattern})|(?:{specials_pattern})"


def _compile_reference_pattern(pattern: str, label: str, required_groups: tuple[str, ...]) -> re.Pattern[str]:
    """Compile a text-reference regex, requiring the named groups the rewriter indexes by name.

    Deliberately stricter than ``split_pattern``/``context_boundary_pattern``, which are
    validated presence-only: those feed ``re.split`` in a background embedding job and have
    no contract beyond "a string ``re`` accepts", while these patterns are read on the search
    request path and their *named capture groups* are an API the rewriter dereferences. A
    missing or misnamed group there is a silently unrewritten token in a live response, so it
    is worth catching at schema-validation time.
    """
    try:
        compiled = re.compile(pattern)
    except re.error as exc:
        raise ValueError(f"x-airbyte-text-references: {label} is not a valid regex: {exc}") from exc
    missing = [name for name in required_groups if name not in compiled.groupindex]
    if missing:
        raise ValueError(f"x-airbyte-text-references: {label} must declare the named group(s) {', '.join(missing)}.")
    return compiled


class TextReferenceSpecials(BaseModel):
    """
    Id-less reference tokens rendered without any lookup (a `specials` block).

    Slack's `<!here>` / `<!channel>` name an audience rather than a record, so there is
    nothing to resolve -- the captured command is substituted straight into `render`.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    pattern: str = Field(description="Regex matching an id-less token; must declare a 'command' named group.")
    render: str = Field(description="Rendered replacement; must contain the '{command}' placeholder.")

    @model_validator(mode="after")
    def validate_grammar(self) -> "TextReferenceSpecials":
        """Require a compilable pattern carrying 'command', and a render that uses it."""
        _compile_reference_pattern(self.pattern, "'specials.pattern'", ("command",))
        if "{command}" not in self.render:
            raise ValueError("x-airbyte-text-references: 'specials.render' must contain the '{command}' placeholder.")
        return self


class TextReferenceResolver(BaseModel):
    """
    One sigil resolved against a context-store entity (a `resolve` entry).

    Used inside x-airbyte-text-references on a context-store entity.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    sigil: str = Field(description="Single character captured by the pattern's 'sigil' group.")
    target: str = Field(description="Target context-store entity holding the labels.")
    key: str = Field(description="Column on the target row carrying the token id.")
    render: str = Field(description="Rendered replacement; must contain the '{label}' placeholder.")
    label: list[str] = Field(description="Ordered label paths on the target row; first non-blank wins.")

    @model_validator(mode="after")
    def validate_grammar(self) -> "TextReferenceResolver":
        """Require a one-character sigil and a render that actually interpolates the label."""
        if len(self.sigil) != 1:
            raise ValueError(f"x-airbyte-text-references: 'sigil' must be exactly one character, got {self.sigil!r}.")
        if not self.target.strip():
            raise ValueError("x-airbyte-text-references: 'target' must be non-blank.")
        if not self.key.strip():
            raise ValueError("x-airbyte-text-references: 'key' must be non-blank.")
        if "{label}" not in self.render:
            raise ValueError("x-airbyte-text-references: 'render' must contain the '{label}' placeholder.")
        if not self.label:
            raise ValueError("x-airbyte-text-references: 'label' must list at least one path.")
        # An empty path resolves to the whole target row, which would render a stringified dict
        # as the label instead of a name -- bad output rather than a clean miss.
        if any(not path or any(segment == "" for segment in path.split(".")) for path in self.label):
            raise ValueError(f"x-airbyte-text-references: 'label' paths must not contain empty segments, got {self.label!r}")
        return self


class TextReferenceConfig(BaseModel):
    """
    Read-time rewrite of inline reference tokens into human-readable labels
    (an entity's x-airbyte-text-references block).

    Display-only: the stored text and any embedding vectors keep the raw tokens.
    ``pattern`` is the whole token grammar: the rewriter dereferences its ``sigil``
    and ``id`` groups, and dispatches on the sigil to pick a ``resolve`` entry.
    ``fields`` are the top-level record fields rewritten on the keyword search path.

    Example YAML usage (on a context-store entity):
        x-airbyte-text-references:
          fields: [text]
          pattern: '<(?P<sigil>[@#])(?P<id>[A-Z0-9]+)(\\|[^>]*)?>'
          specials:
            pattern: '<!(?P<command>here|channel|everyone)(\\|[^>]*)?>'
            render: '@{command}'
          resolve:
            - { sigil: '@', target: users, key: id, render: '@{label}', label: ["profile.display_name"] }
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    fields: list[str] = Field(description="Top-level record fields to rewrite on the keyword path.")
    pattern: str = Field(description="Regex matching an id-bearing token; must declare 'sigil' and 'id' named groups.")
    specials: TextReferenceSpecials | None = Field(default=None, description="Optional id-less tokens rendered without a lookup.")
    resolve: list[TextReferenceResolver] = Field(description="Per-sigil label lookups.")

    @model_validator(mode="after")
    def validate_grammar(self) -> "TextReferenceConfig":
        """Require a rewritable field, a group-conformant pattern, and one resolver per distinct sigil."""
        if not self.fields:
            raise ValueError("x-airbyte-text-references: at least one 'fields' entry is required.")
        if any(not field.strip() for field in self.fields):
            raise ValueError("x-airbyte-text-references: 'fields' entries must be non-blank.")
        if not self.resolve:
            raise ValueError("x-airbyte-text-references: at least one 'resolve' entry is required.")
        _compile_reference_pattern(self.pattern, "'pattern'", ("sigil", "id"))
        if len({entry.sigil for entry in self.resolve}) != len(self.resolve):
            raise ValueError("x-airbyte-text-references: duplicate 'sigil' in resolve.")
        if self.specials is not None:
            # The rewriter runs both halves as one alternation, so group names must not collide.
            _compile_reference_pattern(
                combined_reference_pattern(self.pattern, self.specials.pattern), "'pattern' + 'specials.pattern'", ("sigil", "id", "command")
            )
        return self


def split_enrichment_path(path: str) -> tuple[str, ...]:
    """Split a dotted enrichment path, preserving array markers as segments."""
    segments: list[str] = []
    for raw in path.split("."):
        token = raw
        while token:
            match = _ENRICHMENT_ARRAY_TOKEN_RE.match(token)
            if match is None:
                segments.append(token)
                break
            key = match.group("key")
            if key:
                segments.append(key)
            segments.append("[]")
            token = match.group("rest")
    return tuple(segment for segment in segments if segment)


def analyze_enrichment_path(path: str) -> tuple[bool, tuple[str, ...], tuple[str, ...]]:
    """Return scalar status, array prefix, and value segments for an enrichment path."""
    segments = split_enrichment_path(path)
    if "[]" not in segments:
        return True, (), segments
    array_index = segments.index("[]")
    return False, segments[:array_index], segments[array_index + 1 :]


def executable_projections(config: EnrichmentConfig) -> list[EnrichmentProjection]:
    """The projections the current enrichment runtime can actually resolve.

    Config-level problems make the whole join unrunnable and yield nothing. A single unsupported
    projection is dropped on its own, so its siblings survive: one bad projection taking down nine
    working ones is how this PR came to delete zendesk's ticketTags.
    """
    foreign_array_prefixes: set[tuple[str, ...]] = set()
    has_scalar_foreign_match = False

    for match in config.match:
        if not split_enrichment_path(match.foreign):
            return []
        if not split_enrichment_path(match.local.lstrip("/")):
            # An empty local path reaches the renderer as bound_match.local_segments == (), which
            # raises MotherDuckEnrichmentRenderError rather than degrading.
            return []
        is_scalar, array_prefix, _ = analyze_enrichment_path(match.foreign)
        if is_scalar:
            has_scalar_foreign_match = True
        else:
            foreign_array_prefixes.add(array_prefix)

    if not has_scalar_foreign_match or len(foreign_array_prefixes) > 1:
        return []

    usable: list[EnrichmentProjection] = []
    for projection in config.project:
        if not split_enrichment_path(projection.from_):
            continue
        is_scalar, array_prefix, value_segments = analyze_enrichment_path(projection.from_)
        # A terminal array (`tags[]`) projects the list itself, so it needs no per-element
        # correlation with a match array -- the runtime resolves it through the in_array=False
        # branch. Only a projection that indexes THROUGH an array into fields has to share the
        # matched array's prefix.
        if not is_scalar and value_segments and array_prefix not in foreign_array_prefixes:
            continue
        usable.append(projection)
    return usable


def is_enrichment_config_executable(config: EnrichmentConfig) -> bool:
    """Whether the current enrichment runtime can execute any part of this schema-valid config."""
    return bool(executable_projections(config))


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
    x_airbyte_enrichment: list[EnrichmentConfig] | None = Field(
        default=None,
        alias="x-airbyte-enrichment",
        description="Query-time enrichment joins for this entity: each entry looks up "
        "fields from another context-store entity and projects them onto each record "
        "at read time.",
    )
    x_airbyte_text_references: TextReferenceConfig | None = Field(
        default=None,
        alias="x-airbyte-text-references",
        description="Read-time rewrite of inline reference tokens (e.g. Slack <@U123>) "
        "into human-readable labels looked up from another context-store entity. "
        "Display-only: stored text and embeddings keep the raw tokens.",
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
    replication_config_constants: dict[str, str | int | float | bool | dict[str, Any]] = Field(
        default_factory=dict,
        alias="replication_config_constants",
        description="System-set constant values injected into the Airbyte source config; never shown in the user-facing form. "
        "Object values are injected as-is for nested config blocks (e.g. delivery_method).",
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
    kind: Literal["DATA", "FILES"] = Field(
        default="DATA",
        description="Context-store kind. DATA (default) is the structured-records pipeline; "
        "FILES routes replication through the raw-file-transfer destination.",
    )
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
    `config_values`, optionally renders `value_template`, and injects the
    value automatically.  Explicitly supplied `params` always take precedence
    over the scoped default.

    Used in `x-airbyte-scoping` extension in the Info object.

    Example YAML usage:

        info:
          title: My API
          x-airbyte-scoping:
            - param: account_id
              config_key: account_id
            - param: owner
              config_key: repositories
              value_template: "{{ value.split('/')[0] }}"
    """

    model_config = ConfigDict(extra="forbid")

    param: str = Field(description="Path parameter name to resolve from config")
    config_key: str | None = Field(None, description="Config key to read. Defaults to param name if omitted.")
    value_template: str | None = Field(
        None,
        description=(
            "Optional Jinja template rendered with `value`, `config`, and `param` "
            "before injecting the scoped value. Templates that render to `none`, "
            "`null`, or an empty string leave the parameter unresolved."
        ),
    )
