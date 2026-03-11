"""
Component models for OpenAPI 3.1: Schema, Parameter, RequestBody, Response, Components.

References:
- https://spec.openapis.org/oas/v3.1.0#components-object
- https://spec.openapis.org/oas/v3.1.0#schema-object
- https://spec.openapis.org/oas/v3.1.0#parameter-object
"""

from typing import Any, Dict, List, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from .security import SecurityScheme


class Schema(BaseModel):
    """
    JSON Schema definition for data models.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#schema-object

    Note: Uses Dict[str, Any] for properties to support nested schemas and $ref.
    Reference resolution happens at runtime in config_loader.py.

    Extensions:
    - x-airbyte-resource-name: Name of the resource this schema represents (Airbyte extension)
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Core JSON Schema fields
    type: str | None = None
    format: str | None = None
    title: str | None = None
    description: str | None = None
    default: Any | None = None
    example: Any | None = None

    # Object properties
    properties: Dict[str, Any] = Field(default_factory=dict)  # May contain $ref
    required: List[str] = Field(default_factory=list)
    additional_properties: Any | None = Field(None, alias="additionalProperties")

    # Array properties
    items: Any | None = None  # May be Schema or $ref

    # Validation
    enum: List[Any] | None = None
    min_length: int | None = Field(None, alias="minLength")
    max_length: int | None = Field(None, alias="maxLength")
    minimum: float | None = None
    maximum: float | None = None
    pattern: str | None = None

    # Composition
    all_of: List[Any] | None = Field(None, alias="allOf")
    any_of: List[Any] | None = Field(None, alias="anyOf")
    one_of: List[Any] | None = Field(None, alias="oneOf")
    not_: Any | None = Field(None, alias="not")

    # Metadata
    nullable: bool | None = Field(None, deprecated="Use type union with null instead (OpenAPI 3.1)")
    read_only: bool | None = Field(None, alias="readOnly")
    write_only: bool | None = Field(None, alias="writeOnly")
    deprecated: bool | None = None

    # Airbyte extensions
    x_airbyte_entity_name: str | None = Field(None, alias="x-airbyte-entity-name")
    x_airbyte_stream_name: str | None = Field(None, alias="x-airbyte-stream-name")


class Parameter(BaseModel):
    """
    Operation parameter definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#parameter-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str
    in_: Literal["query", "header", "path", "cookie"] = Field(alias="in")
    description: str | None = None
    required: bool | None = None
    deprecated: bool | None = None
    allow_empty_value: bool | None = Field(None, alias="allowEmptyValue")

    # Schema can be inline or reference
    schema_: Dict[str, Any] | None = Field(None, alias="schema")

    # Style and examples
    style: str | None = None
    explode: bool | None = None
    example: Any | None = None
    examples: Dict[str, Any] | None = None


class MediaType(BaseModel):
    """
    Media type object for request/response content.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#media-type-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    schema_: Dict[str, Any] | None = Field(None, alias="schema")
    example: Any | None = None
    examples: Dict[str, Any] | None = None
    encoding: Dict[str, Any] | None = None


class GraphQLBodyConfig(BaseModel):
    """
    GraphQL body type configuration for x-airbyte-body-type extension.

    Used when x-airbyte-body-type.type = "graphql"
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    type: Literal["graphql"] = Field(..., description="Body type identifier (must be 'graphql')")
    query: str = Field(
        ...,
        description="GraphQL query or mutation string with optional template placeholders (e.g., {{ variable }})",
    )
    variables: Dict[str, Any] | None = Field(
        None,
        description="Variables to substitute in the GraphQL query using template syntax (e.g., {{ param_name }})",
    )
    operationName: str | None = Field(None, description="Operation name for queries with multiple operations")
    default_fields: Union[str, List[str]] | None = Field(
        None,
        description="Default fields to select if not provided in request parameters. Can be a string or array of field names.",
    )
    nullable_variables: List[str] | None = Field(
        default=None,
        alias="x-airbyte-nullable-variables",
        description="Variable names that can be explicitly set to null (e.g., to unassign a user)",
    )


# Union type for all body type configs (extensible for future types like XML, SOAP, etc.)
BodyTypeConfig = Union[GraphQLBodyConfig]


class PathOverrideConfig(BaseModel):
    """
    Path override configuration for x-airbyte-path-override extension.

    Used when the OpenAPI path differs from the actual HTTP endpoint path.
    Common for GraphQL APIs where multiple resources share the same endpoint (e.g., /graphql).

    Example:
        OpenAPI path: /graphql:repositories (for uniqueness)
        Actual HTTP path: /graphql (configured here)
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    path: str = Field(
        ...,
        description=("Actual HTTP path to use for requests (e.g., '/graphql'). Must start with '/'"),
    )


class RequestBody(BaseModel):
    """
    Request body definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#request-body-object

    Airbyte Extensions:
    See connector_sdk.extensions for documentation:
    - AIRBYTE_BODY_TYPE: Body type and configuration (nested structure)
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    description: str | None = None
    content: Dict[str, MediaType] = Field(default_factory=dict)
    required: bool | None = None

    # Airbyte extensions for GraphQL support
    # See connector_sdk.extensions for AIRBYTE_BODY_TYPE constant
    x_airbyte_body_type: BodyTypeConfig | None = Field(
        None,
        alias="x-airbyte-body-type",  # AIRBYTE_BODY_TYPE
        description=(
            "Body type and configuration. Contains 'type' field (e.g., 'graphql') and type-specific configuration (query, variables, etc.)."
        ),
    )


class Header(BaseModel):
    """
    Header definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#header-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    description: str | None = None
    required: bool | None = None
    deprecated: bool | None = None
    schema_: Dict[str, Any] | None = Field(None, alias="schema")
    example: Any | None = None


class Response(BaseModel):
    """
    Response definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#response-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    description: str
    headers: Dict[str, Header] | None = None
    content: Dict[str, MediaType] | None = None
    links: Dict[str, Any] | None = None


class Components(BaseModel):
    """
    Reusable component definitions.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#components-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    schemas: Dict[str, Schema] = Field(default_factory=dict)
    responses: Dict[str, Response] = Field(default_factory=dict)
    parameters: Dict[str, Parameter] = Field(default_factory=dict)
    examples: Dict[str, Any] | None = None
    request_bodies: Dict[str, RequestBody] = Field(default_factory=dict, alias="requestBodies")
    headers: Dict[str, Header] | None = None
    security_schemes: Dict[str, SecurityScheme] = Field(default_factory=dict, alias="securitySchemes")
    links: Dict[str, Any] | None = None
    callbacks: Dict[str, Any] | None = None
