"""
Component models for OpenAPI 3.1: Schema, Parameter, RequestBody, Response, Components.

References:
- https://spec.openapis.org/oas/v3.1.0#components-object
- https://spec.openapis.org/oas/v3.1.0#schema-object
- https://spec.openapis.org/oas/v3.1.0#parameter-object
"""

from typing import Any, Dict, List, Literal, Optional, Union

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
    type: Optional[str] = None
    format: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    example: Optional[Any] = None

    # Object properties
    properties: Dict[str, Any] = Field(default_factory=dict)  # May contain $ref
    required: List[str] = Field(default_factory=list)
    additional_properties: Optional[Any] = Field(None, alias="additionalProperties")

    # Array properties
    items: Optional[Any] = None  # May be Schema or $ref

    # Validation
    enum: Optional[List[Any]] = None
    min_length: Optional[int] = Field(None, alias="minLength")
    max_length: Optional[int] = Field(None, alias="maxLength")
    minimum: Optional[float] = None
    maximum: Optional[float] = None
    pattern: Optional[str] = None

    # Composition
    all_of: Optional[List[Any]] = Field(None, alias="allOf")
    any_of: Optional[List[Any]] = Field(None, alias="anyOf")
    one_of: Optional[List[Any]] = Field(None, alias="oneOf")
    not_: Optional[Any] = Field(None, alias="not")

    # Metadata
    nullable: Optional[bool] = Field(None, deprecated="Use type union with null instead (OpenAPI 3.1)")
    read_only: Optional[bool] = Field(None, alias="readOnly")
    write_only: Optional[bool] = Field(None, alias="writeOnly")
    deprecated: Optional[bool] = None

    # Airbyte extension
    x_airbyte_entity_name: Optional[str] = Field(None, alias="x-airbyte-entity-name")


class Parameter(BaseModel):
    """
    Operation parameter definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#parameter-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str
    in_: Literal["query", "header", "path", "cookie"] = Field(alias="in")
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allow_empty_value: Optional[bool] = Field(None, alias="allowEmptyValue")

    # Schema can be inline or reference
    schema_: Optional[Dict[str, Any]] = Field(None, alias="schema")

    # Style and examples
    style: Optional[str] = None
    explode: Optional[bool] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Any]] = None


class MediaType(BaseModel):
    """
    Media type object for request/response content.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#media-type-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    schema_: Optional[Dict[str, Any]] = Field(None, alias="schema")
    example: Optional[Any] = None
    examples: Optional[Dict[str, Any]] = None
    encoding: Optional[Dict[str, Any]] = None


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
    variables: Optional[Dict[str, Any]] = Field(
        None,
        description="Variables to substitute in the GraphQL query using template syntax (e.g., {{ param_name }})",
    )
    operationName: Optional[str] = Field(None, description="Operation name for queries with multiple operations")
    default_fields: Optional[Union[str, List[str]]] = Field(
        None,
        description="Default fields to select if not provided in request parameters. Can be a string or array of field names.",
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
        description=("Actual HTTP path to use for requests (e.g., '/graphql'). " "Must start with '/'"),
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

    description: Optional[str] = None
    content: Dict[str, MediaType] = Field(default_factory=dict)
    required: Optional[bool] = None

    # Airbyte extensions for GraphQL support
    # See connector_sdk.extensions for AIRBYTE_BODY_TYPE constant
    x_airbyte_body_type: Optional[BodyTypeConfig] = Field(
        None,
        alias="x-airbyte-body-type",  # AIRBYTE_BODY_TYPE
        description=(
            "Body type and configuration. Contains 'type' field (e.g., 'graphql') " "and type-specific configuration (query, variables, etc.)."
        ),
    )


class Header(BaseModel):
    """
    Header definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#header-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    schema_: Optional[Dict[str, Any]] = Field(None, alias="schema")
    example: Optional[Any] = None


class Response(BaseModel):
    """
    Response definition.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#response-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    description: str
    headers: Optional[Dict[str, Header]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Any]] = None


class Components(BaseModel):
    """
    Reusable component definitions.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#components-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    schemas: Dict[str, Schema] = Field(default_factory=dict)
    responses: Dict[str, Response] = Field(default_factory=dict)
    parameters: Dict[str, Parameter] = Field(default_factory=dict)
    examples: Optional[Dict[str, Any]] = None
    request_bodies: Dict[str, RequestBody] = Field(default_factory=dict, alias="requestBodies")
    headers: Optional[Dict[str, Header]] = None
    security_schemes: Dict[str, SecurityScheme] = Field(default_factory=dict, alias="securitySchemes")
    links: Optional[Dict[str, Any]] = None
    callbacks: Optional[Dict[str, Any]] = None
