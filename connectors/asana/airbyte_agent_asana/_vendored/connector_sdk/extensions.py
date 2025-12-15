"""
Airbyte OpenAPI Extensions - Single Source of Truth

This module defines all custom Airbyte extensions to the OpenAPI 3.0 specification.
These extensions are prefixed with 'x-airbyte-' to follow OpenAPI vendor extension
conventions and avoid conflicts with other extensions.

All extension names, valid values, and related types are centralized here to ensure
consistency across the codebase.

Usage:
    from .extensions import AIRBYTE_CONNECTOR_NAME, AIRBYTE_ENTITY, ActionType

    # In Pydantic models
    x_entity: Optional[str] = Field(None, alias=AIRBYTE_ENTITY)

    # In tests and validation
    assert operation.get(AIRBYTE_ACTION) in ActionType.__members__.values()
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

AIRBYTE_ENTITY = "x-airbyte-entity"
"""
Extension: x-airbyte-entity
Location: Operation object (on individual HTTP operations)
Type: string
Required: Yes (for operations that should be exposed as Airbyte streams)

Description:
    Identifies which logical entity/stream this operation belongs to. Operations
    with the same x-airbyte-entity value are grouped together to form a single
    Airbyte stream. The entity name is used as the stream name.

Example:
    ```yaml
    paths:
      /customers:
        get:
          x-airbyte-entity: customers
          x-airbyte-action: list
    ```
"""

AIRBYTE_ACTION = "x-airbyte-action"
"""
Extension: x-airbyte-action
Location: Operation object (on individual HTTP operations)
Type: string (enum - see ActionType)
Required: Yes (for operations that should be exposed as Airbyte streams)
Valid Values: get, list, create, update, delete

Description:
    Specifies the semantic intent of this operation within its entity. This helps
    Airbyte understand how to map REST operations to stream operations and determine
    which operation to use for syncing data.

Action Semantics:
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
          x-airbyte-entity: customers
          x-airbyte-action: list
        post:
          x-airbyte-entity: customers
          x-airbyte-action: create
      /customers/{id}:
        get:
          x-airbyte-entity: customers
          x-airbyte-action: get
    ```
"""

AIRBYTE_ENTITY_NAME = "x-airbyte-entity-name"
"""
Extension: x-airbyte-entity-name
Location: Schema object (in components.schemas)
Type: string
Required: No (but recommended for entity schemas)

Description:
    Links a schema definition to a logical entity/stream. This helps identify which
    schema represents the main data model for a particular entity, especially when
    multiple schemas might reference the same entity.

Example:
    ```yaml
    components:
      schemas:
        Customer:
          type: object
          x-airbyte-entity-name: customers
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
    from the real API endpoint. Common for GraphQL APIs where multiple entities
    need unique OpenAPI paths but query the same HTTP endpoint.

    This allows multiple operations (e.g., repositories→search, issues→search) to
    have distinct entity-action mappings in the OpenAPI spec while all sending
    requests to the same physical endpoint (e.g., /graphql).

Structure:
    - path: Actual HTTP path to use (required, must start with '/')

Example:
    ```yaml
    paths:
      /graphql:repositories:  # OpenAPI path (for uniqueness)
        post:
          x-airbyte-entity: repositories
          x-airbyte-action: search
          x-airbyte-path-override:
            path: /graphql  # Actual HTTP endpoint
      /graphql:issues:  # Different OpenAPI path
        post:
          x-airbyte-entity: issues
          x-airbyte-action: search
          x-airbyte-path-override:
            path: /graphql  # Same actual endpoint
    ```
"""

AIRBYTE_RECORD_EXTRACTOR = "x-airbyte-record-extractor"
"""
Extension: x-airbyte-record-extractor
Location: Operation object (on individual HTTP operations)
Type: string (JSONPath expression)
Required: No

Description:
    Specifies a JSONPath expression to extract actual record data from API
    response envelopes. Many APIs wrap responses in metadata structures
    (pagination info, request IDs, etc.). This extension tells the executor
    where to find the actual records.

    Return type is automatically inferred from x-airbyte-action:
    - list, search actions: Returns array ([] if path not found)
    - get, create, update, delete actions: Returns single record (None if path not found)

Example:
    ```yaml
    paths:
      /v2/users:
        get:
          x-airbyte-entity: users
          x-airbyte-action: list
          x-airbyte-record-extractor: $.users
    ```

    API Response:
    ```json
    {
      "requestId": "abc123",
      "users": [{"id": "1"}, {"id": "2"}]
    }
    ```

    Executor Returns: [{"id": "1"}, {"id": "2"}]
"""

AIRBYTE_META_EXTRACTOR = "x-airbyte-meta-extractor"
"""
Extension: x-airbyte-meta-extractor
Location: Operation object (on individual HTTP operations)
Type: dict[str, str] (field name → JSONPath expression)
Required: No

Description:
    Extracts metadata (pagination info, request IDs, etc.) from API responses.
    Each key in the dict becomes a field in ExecutionResult.meta, with its value
    being a JSONPath expression that extracts data from the original response.

    Supports two usage patterns:

    Pattern 1: Extract entire nested object (when all fields are grouped together)
    Pattern 2: Extract individual fields (when fields are scattered across response)

    Metadata is extracted from the original full response before record extraction,
    ensuring access to envelope metadata that may be removed during record extraction.

Usage Pattern 1 (Extract nested object):
    ```yaml
    paths:
      /v2/users:
        get:
          x-airbyte-resource: users
          x-airbyte-verb: list
          x-airbyte-record-extractor: $.users
          x-airbyte-meta-extractor:
            pagination: $.records  # Extracts entire nested object
    ```

    API Response:
    ```json
    {
      "requestId": "abc123",
      "records": {
        "cursor": "next_page_token",
        "totalRecords": 100,
        "currentPageSize": 20
      },
      "users": [{"id": "1"}, {"id": "2"}]
    }
    ```

    Executor Returns:
    - data: [{"id": "1"}, {"id": "2"}]
    - meta: {"pagination": {"cursor": "next_page_token", "totalRecords": 100, "currentPageSize": 20}}

Usage Pattern 2 (Extract individual fields):
    ```yaml
    paths:
      /v1/customers:
        get:
          x-airbyte-resource: customers
          x-airbyte-verb: list
          x-airbyte-record-extractor: $.data
          x-airbyte-meta-extractor:
            cursor: $.records.cursor
            total_count: $.records.totalRecords
            request_id: $.requestId
            has_more: $.has_more
    ```

    API Response:
    ```json
    {
      "requestId": "xyz789",
      "records": {"cursor": "abc", "totalRecords": 50},
      "has_more": true,
      "data": [{"id": "cus_1"}, {"id": "cus_2"}]
    }
    ```

    Executor Returns:
    - data: [{"id": "cus_1"}, {"id": "cus_2"}]
    - meta: {"cursor": "abc", "total_count": 50, "request_id": "xyz789", "has_more": true}

Behavior:
    - Missing paths return None for that field (does not crash)
    - Invalid JSONPath logs warning and returns None for that field
    - Extraction happens before record extraction to access full response envelope
"""

AIRBYTE_FILE_URL = "x-airbyte-file-url"
"""
Extension: x-airbyte-file-url
Location: Operation object (on individual HTTP operations with x-airbyte-action: download)
Type: string
Required: Yes (when x-airbyte-action is "download")

Description:
    Specifies which field in the metadata response contains the download URL. Used with
    the 'download' action to perform a two-step file retrieval: first fetch metadata,
    then extract and download from the URL field specified here.

    The field path can be a simple field name (e.g., "content_url") or a nested path
    using dot notation (e.g., "data.download_link"). The URL must be absolute.

Example:
    ```yaml
    paths:
      /articles/{article_id}/attachments/{attachment_id}:
        get:
          x-airbyte-entity: article_attachments
          x-airbyte-action: download
          x-airbyte-file-url: content_url
          responses:
            "200":
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: integer
                      content_url:
                        type: string
                        description: URL to download the file
    ```
"""

AIRBYTE_TOKEN_EXTRACT = "x-airbyte-token-extract"
"""
Extension: x-airbyte-token-extract
Location: SecurityScheme object (in components.securitySchemes, under oauth2)
Type: list[str]
Required: No

Description:
    Specifies which fields to extract from OAuth2 token responses and use as server
    variables. This is useful for APIs like Salesforce where the token response includes
    dynamic values (e.g., instance_url) needed to construct API URLs.

    When token refresh occurs, the SDK:
    1. Extracts the specified fields from the token response
    2. Updates config_values with extracted values
    3. Re-renders the base_url with updated server variables
    4. Includes extracted fields in on_token_refresh callback for persistence

Precedence rules (highest wins):
    1. Server variable `default` in YAML (lowest)
    2. User-provided `config_values` at init (optional, may be unset)
    3. Token-extracted values via `x-airbyte-token-extract` (highest)

Validation (at connector load time):
    - Error if extracted field doesn't match a defined server variable
    - Error if duplicate fields in x-airbyte-token-extract

Example:
    ```yaml
    servers:
      - url: "{instance_url}/services/data/v59.0"
        variables:
          instance_url:
            default: "https://login.salesforce.com"

    components:
      securitySchemes:
        oauth2:
          type: oauth2
          flows:
            authorizationCode:
              tokenUrl: https://login.salesforce.com/services/oauth2/token
              refreshUrl: https://login.salesforce.com/services/oauth2/token
              scopes: {}
          x-airbyte-token-extract:
            - instance_url  # Extract from token response → updates {instance_url}
    ```
"""


# =============================================================================
# Enums and Type Definitions
# =============================================================================


class ActionType(str, Enum):
    """
    Valid values for x-airbyte-action extension.

    These actions represent the semantic operations that can be performed on an entity.
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

    DOWNLOAD = "download"
    """Download file content from a URL specified in the metadata response"""


class BodyType(str, Enum):
    """
    Valid values for x-airbyte-body-type extension.

    These types represent the supported request body formats.
    """

    GRAPHQL = "graphql"
    """GraphQL query/mutation format"""


# Type alias for use in Pydantic models
ActionTypeLiteral = Literal["get", "list", "create", "update", "delete", "search", "download"]


# =============================================================================
# Validation Helpers
# =============================================================================


def is_valid_action(action: str) -> bool:
    """
    Check if a string is a valid Airbyte action.

    Args:
        action: The action string to validate

    Returns:
        True if the action is valid, False otherwise
    """
    return action in [a.value for a in ActionType]


def get_all_extension_names() -> list[str]:
    """
    Get a list of all defined Airbyte extension names.

    Returns:
        List of extension name constants
    """
    return [
        AIRBYTE_CONNECTOR_NAME,
        AIRBYTE_EXTERNAL_DOCUMENTATION_URLS,
        AIRBYTE_ENTITY,
        AIRBYTE_ACTION,
        AIRBYTE_ENTITY_NAME,
        AIRBYTE_TOKEN_PATH,
        AIRBYTE_BODY_TYPE,
        AIRBYTE_PATH_OVERRIDE,
        AIRBYTE_RECORD_EXTRACTOR,
        AIRBYTE_META_EXTRACTOR,
        AIRBYTE_FILE_URL,
        AIRBYTE_TOKEN_EXTRACT,
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
    AIRBYTE_ENTITY: {
        "location": "operation",
        "type": "string",
        "required": True,
        "description": "Entity/stream name this operation belongs to",
    },
    AIRBYTE_ACTION: {
        "location": "operation",
        "type": "string",
        "required": True,
        "enum": [a.value for a in ActionType],
        "description": "Semantic operation type",
    },
    AIRBYTE_ENTITY_NAME: {
        "location": "schema",
        "type": "string",
        "required": False,
        "description": "Links schema to an entity/stream",
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
    AIRBYTE_RECORD_EXTRACTOR: {
        "location": "operation",
        "type": "string",
        "required": False,
        "description": "JSONPath expression to extract records from response envelopes",
    },
    AIRBYTE_META_EXTRACTOR: {
        "location": "operation",
        "type": "dict[str, str]",
        "required": False,
        "description": (
            "Dictionary mapping field names to JSONPath expressions for extracting metadata "
            "(pagination, request IDs, etc.) from response envelopes"
        ),
    },
    AIRBYTE_FILE_URL: {
        "location": "operation",
        "type": "string",
        "required": "conditional",  # Required when action is 'download'
        "description": "Field in metadata response containing download URL (required for download action)",
    },
    AIRBYTE_TOKEN_EXTRACT: {
        "location": "securityScheme",
        "type": "list[str]",
        "required": False,
        "description": "List of fields to extract from OAuth2 token responses and use as server variables",
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
