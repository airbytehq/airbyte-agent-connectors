"""
Airbyte OpenAPI Extensions - Single Source of Truth

This module defines all custom Airbyte extensions to the OpenAPI 3.0 specification.
These extensions are prefixed with 'x-airbyte-' to follow OpenAPI vendor extension
conventions and avoid conflicts with other extensions.

All extension names, valid values, and related types are centralized here to ensure
consistency across the codebase.

Usage:
    from .extensions import AIRBYTE_CONNECTOR_NAME, AIRBYTE_RESOURCE, VerbType

    # In Pydantic models
    x_resource: Optional[str] = Field(None, alias=AIRBYTE_RESOURCE)

    # In tests and validation
    assert operation.get(AIRBYTE_VERB) in VerbType.__members__.values()
"""

from enum import Enum
from typing import Literal


# =============================================================================
# Extension Name Constants
# =============================================================================

AIRBYTE_CONNECTOR_NAME = "x-airbyte-connector-name"
"""
Extension: x-airbyte-connector-name
Location: OpenAPI Info object
Type: string
Required: No (but recommended)

Description:
    Specifies the unique identifier/name for this connector. This is used to identify
    the connector in Airbyte's catalog and runtime systems.

Example:
    ```yaml
    info:
      title: Stripe API
      version: 1.0.0
      x-airbyte-connector-name: stripe
    ```
"""

AIRBYTE_EXTERNAL_DOCUMENTATION_URLS = "x-airbyte-external-documentation-urls"
"""
Extension: x-airbyte-external-documentation-urls
Location: OpenAPI Info object
Type: list
Required: Yes

Description:
    List of objects that contain external documentation URLs relevant to the connector. Each object includes:
    - type: Type of documentation (e.g., "api_reference", "other", etc.)
    - title: Human-readable title for the documentation link
    - url: The actual URL to the external documentation

Example:
    ```yaml
    info:
      title: Stripe API
      version: 1.0.0
      x-airbyte-external-documentation-urls:
        - type: api_reference
          title: Stripe API Reference
          url: https://stripe.com/docs/api
        - type: authentication_guide
          title: Stripe APIN Authentication Guide
          url: https://docs.stripe.com/api/authentication
    ```
"""

AIRBYTE_RESOURCE = "x-airbyte-resource"
"""
Extension: x-airbyte-resource
Location: Operation object (on individual HTTP operations)
Type: string
Required: Yes (for operations that should be exposed as Airbyte streams)

Description:
    Identifies which logical resource/stream this operation belongs to. Operations
    with the same x-airbyte-resource value are grouped together to form a single
    Airbyte stream. The resource name is used as the stream name.

Example:
    ```yaml
    paths:
      /customers:
        get:
          x-airbyte-resource: customers
          x-airbyte-verb: list
    ```
"""

AIRBYTE_VERB = "x-airbyte-verb"
"""
Extension: x-airbyte-verb
Location: Operation object (on individual HTTP operations)
Type: string (enum - see VerbType)
Required: Yes (for operations that should be exposed as Airbyte streams)
Valid Values: get, list, create, update, delete

Description:
    Specifies the semantic intent of this operation within its resource. This helps
    Airbyte understand how to map REST operations to stream operations and determine
    which operation to use for syncing data.

Verb Semantics:
    - list: Fetch multiple records (paginated, used for syncing)
    - get: Fetch a single record by ID
    - create: Create a new record
    - update: Update an existing record
    - delete: Delete a record

Example:
    ```yaml
    paths:
      /customers:
        get:
          x-airbyte-resource: customers
          x-airbyte-verb: list
        post:
          x-airbyte-resource: customers
          x-airbyte-verb: create
      /customers/{id}:
        get:
          x-airbyte-resource: customers
          x-airbyte-verb: get
    ```
"""

AIRBYTE_RESOURCE_NAME = "x-airbyte-resource-name"
"""
Extension: x-airbyte-resource-name
Location: Schema object (in components.schemas)
Type: string
Required: No (but recommended for resource schemas)

Description:
    Links a schema definition to a logical resource/stream. This helps identify which
    schema represents the main data model for a particular resource, especially when
    multiple schemas might reference the same resource.

Example:
    ```yaml
    components:
      schemas:
        Customer:
          type: object
          x-airbyte-resource-name: customers
          properties:
            id:
              type: string
            name:
              type: string
    ```
"""

AIRBYTE_TOKEN_PATH = "x-airbyte-token-path"
"""
Extension: x-airbyte-token-path
Location: SecurityScheme object (in components.securitySchemes)
Type: string
Required: No

Description:
    JSON path expression to extract the authentication token from the auth response.
    Used for complex authentication flows where the token is nested in the response.

Example:
    ```yaml
    components:
      securitySchemes:
        oauth2Auth:
          type: oauth2
          flows:
            clientCredentials:
              tokenUrl: https://api.example.com/oauth/token
          x-airbyte-token-path: $.access_token
    ```
"""

AIRBYTE_BODY_TYPE = "x-airbyte-body-type"
"""
Extension: x-airbyte-body-type
Location: RequestBody object (in components.requestBodies or operation.requestBody)
Type: BodyTypeConfig (Union of typed Pydantic models: GraphQLBodyConfig)
Required: No
Validation: Strict - enforced at Pydantic model level

Description:
    Specifies the type and configuration of request body format. Currently supports
    "graphql" for GraphQL queries/mutations. The extension uses strongly-typed Pydantic
    models for validation and contains both the type and type-specific configuration
    in a nested structure. Designed to be extensible to support other body types in
    the future (ie XML/SOAP, MessagePack).

Structure:
    - type: Body type (currently "graphql")
    - For type="graphql":
      - query: GraphQL query/mutation string (required)
      - variables: Variables dict with template placeholders (optional)
      - operationName: Operation name for multi-operation queries (optional)
      - default_fields: Default fields to select if not provided in params (optional)

Example:
    ```yaml
    paths:
      /graphql:
        post:
          requestBody:
            x-airbyte-body-type:
              type: graphql
              query: "query($owner: String!) { repository(owner: $owner) { name } }"
              variables:
                owner: "{{ owner }}"
    ```
"""

AIRBYTE_PATH_OVERRIDE = "x-airbyte-path-override"
"""
Extension: x-airbyte-path-override
Location: Operation object (on individual HTTP operations)
Type: PathOverrideConfig (strongly-typed Pydantic model)
Required: No
Validation: Strict - enforced at Pydantic model level

Description:
    Overrides the HTTP path used for actual requests when the OpenAPI path differs
    from the real API endpoint. Common for GraphQL APIs where multiple resources
    need unique OpenAPI paths but query the same HTTP endpoint.

    This allows multiple operations (e.g., repositories→search, issues→search) to
    have distinct resource-verb mappings in the OpenAPI spec while all sending
    requests to the same physical endpoint (e.g., /graphql).

Structure:
    - path: Actual HTTP path to use (required, must start with '/')

Example:
    ```yaml
    paths:
      /graphql:repositories:  # OpenAPI path (for uniqueness)
        post:
          x-airbyte-resource: repositories
          x-airbyte-verb: search
          x-airbyte-path-override:
            path: /graphql  # Actual HTTP endpoint
      /graphql:issues:  # Different OpenAPI path
        post:
          x-airbyte-resource: issues
          x-airbyte-verb: search
          x-airbyte-path-override:
            path: /graphql  # Same actual endpoint
    ```
"""


# =============================================================================
# Enums and Type Definitions
# =============================================================================


class VerbType(str, Enum):
    """
    Valid values for x-airbyte-verb extension.

    These verbs represent the semantic operations that can be performed on a resource.
    """

    GET = "get"
    """Fetch a single record by identifier"""

    LIST = "list"
    """Fetch multiple records (typically paginated, used for data syncing)"""

    CREATE = "create"
    """Create a new record"""

    UPDATE = "update"
    """Update an existing record"""

    DELETE = "delete"
    """Delete a record"""

    SEARCH = "search"
    """Search for records matching specific query criteria"""


class BodyType(str, Enum):
    """
    Valid values for x-airbyte-body-type extension.

    These types represent the supported request body formats.
    """

    GRAPHQL = "graphql"
    """GraphQL query/mutation format"""


# Type alias for use in Pydantic models
VerbTypeLiteral = Literal["get", "list", "create", "update", "delete", "search"]


# =============================================================================
# Validation Helpers
# =============================================================================


def is_valid_verb(verb: str) -> bool:
    """
    Check if a string is a valid Airbyte verb.

    Args:
        verb: The verb string to validate

    Returns:
        True if the verb is valid, False otherwise
    """
    return verb in [v.value for v in VerbType]


def get_all_extension_names() -> list[str]:
    """
    Get a list of all defined Airbyte extension names.

    Returns:
        List of extension name constants
    """
    return [
        AIRBYTE_CONNECTOR_NAME,
        AIRBYTE_EXTERNAL_DOCUMENTATION_URLS,
        AIRBYTE_RESOURCE,
        AIRBYTE_VERB,
        AIRBYTE_RESOURCE_NAME,
        AIRBYTE_TOKEN_PATH,
        AIRBYTE_BODY_TYPE,
        AIRBYTE_PATH_OVERRIDE,
    ]


# =============================================================================
# Extension Registry
# =============================================================================

EXTENSION_REGISTRY = {
    AIRBYTE_CONNECTOR_NAME: {
        "location": "info",
        "type": "string",
        "required": False,
        "description": "Unique identifier for the connector",
    },
    AIRBYTE_EXTERNAL_DOCUMENTATION_URLS: {
        "location": "info",
        "type": "list",
        "required": True,
        "description": "List of external documentation URLs relevant to the connector",
    },
    AIRBYTE_RESOURCE: {
        "location": "operation",
        "type": "string",
        "required": True,
        "description": "Resource/stream name this operation belongs to",
    },
    AIRBYTE_VERB: {
        "location": "operation",
        "type": "string",
        "required": True,
        "enum": [v.value for v in VerbType],
        "description": "Semantic operation type",
    },
    AIRBYTE_RESOURCE_NAME: {
        "location": "schema",
        "type": "string",
        "required": False,
        "description": "Links schema to a resource/stream",
    },
    AIRBYTE_TOKEN_PATH: {
        "location": "securityScheme",
        "type": "string",
        "required": False,
        "description": "JSON path to extract token from auth response",
    },
    AIRBYTE_BODY_TYPE: {
        "location": "requestBody",
        "type": "BodyTypeConfig",
        "model": "Union[GraphQLBodyConfig]",
        "required": False,
        "validation": "strict",
        "description": "Body type and configuration (strongly-typed Pydantic models, extensible for future body types)",
    },
    AIRBYTE_PATH_OVERRIDE: {
        "location": "operation",
        "type": "PathOverrideConfig",
        "model": "PathOverrideConfig",
        "required": False,
        "validation": "strict",
        "description": "Override actual HTTP path when OpenAPI path differs from real endpoint (strongly-typed Pydantic model)",
    },
}
"""
Complete registry of all Airbyte extensions with metadata.

This can be used for:
- Validation
- Documentation generation
- Runtime introspection
- Tool development
"""
