# Entity-Action API

Airbyte Agent Connectors use a unified entity-action model for interacting with third-party APIs. This document explains the core concepts, available actions, and how to work with results.

## Core Concepts

### Entity-Action Model

Every connector operation follows the pattern:

```python
result = await connector.execute(entity, action, params)
```

- **Entity**: The resource type you're working with (e.g., `customers`, `issues`, `contacts`)
- **Action**: The operation to perform (e.g., `list`, `get`, `create`, `update`)
- **Params**: Parameters specific to the entity and action

This model provides a consistent interface across all 21 connectors, regardless of the underlying API's design.

### Example

```python
# Stripe: List customers
await connector.execute("customers", "list", {"limit": 10})

# GitHub: Get a specific issue
await connector.execute("issues", "get", {
    "owner": "airbytehq",
    "repo": "airbyte",
    "number": 123
})

# Salesforce: Search opportunities
await connector.execute("opportunities", "api_search", {
    "query": "Amount > 10000"
})
```

## Available Actions

### get

Retrieve a single record by its identifier.

```python
# Get a specific customer
result = await connector.execute("customers", "get", {"id": "cus_xxx"})

# Get a specific repository
result = await connector.execute("repositories", "get", {
    "owner": "airbytehq",
    "repo": "airbyte"
})
```

**Common Parameters:**
- `id` - Primary identifier for the record
- Additional identifiers vary by entity (e.g., `owner`/`repo` for GitHub)
- `fields` - Optional array of field names to return

### list

Retrieve multiple records with optional filtering and pagination.

```python
# List customers
result = await connector.execute("customers", "list", {
    "limit": 100,
    "starting_after": "cus_xxx"  # Pagination cursor
})

# List issues with filters
result = await connector.execute("issues", "list", {
    "owner": "airbytehq",
    "repo": "airbyte",
    "states": ["OPEN"],
    "per_page": 50
})
```

**Common Parameters:**
- `limit` or `per_page` - Number of records to return
- `after` or `starting_after` - Cursor for pagination
- Filter parameters vary by entity (e.g., `states`, `created_at`)
- `fields` - Optional array of field names to return

### create

Create a new record.

```python
# Create a customer
result = await connector.execute("customers", "create", {
    "email": "user@example.com",
    "name": "Jane Doe",
    "metadata": {"source": "agent"}
})

# Create a product
result = await connector.execute("products", "create", {
    "name": "Premium Plan",
    "description": "Full access subscription"
})
```

**Returns:** The created record with its assigned ID.

### update

Modify an existing record.

```python
# Update a customer
result = await connector.execute("customers", "update", {
    "id": "cus_xxx",
    "name": "Jane Smith",
    "metadata": {"updated": "true"}
})

# Update a product
result = await connector.execute("products", "update", {
    "id": "prod_xxx",
    "name": "Premium Plan v2"
})
```

**Returns:** The updated record.

### delete

Remove a record.

```python
# Delete a customer
result = await connector.execute("customers", "delete", {"id": "cus_xxx"})

# Delete a product
result = await connector.execute("products", "delete", {"id": "prod_xxx"})
```

**Returns:** Confirmation of deletion.

### api_search

Search using the API's native search syntax. This provides access to powerful server-side filtering.

```python
# GitHub: Search repositories
result = await connector.execute("repositories", "api_search", {
    "query": "language:python stars:>1000 topic:machine-learning"
})

# Stripe: Search customers
result = await connector.execute("customers", "api_search", {
    "query": "email:'user@example.com' AND metadata['status']:'active'"
})

# Salesforce: SOQL query
result = await connector.execute("accounts", "api_search", {
    "query": "Industry = 'Technology' AND AnnualRevenue > 1000000"
})
```

**Note:** Query syntax varies by connector. Refer to each connector's REFERENCE.md for syntax details.

### download

Download file content (available on connectors with file entities).

```python
# Google Drive: Download file
result = await connector.execute("files", "download", {
    "file_id": "1abc123..."
})

# The result.data will be an AsyncIterator[bytes] for streaming
```

## Execution Result

Result types vary by connector and operation:

### List Operations (with pagination)

```python
result = await connector.execute("customers", "list", {"limit": 10})
# result.data: list of records
# result.meta: pagination info (cursor, totalRecords, etc.)
```

### Get/Create/Update/Delete Operations

```python
result = await connector.execute("customers", "get", {"id": "cus_xxx"})
# result.data: the entity dict
# result.meta: may be None or contain additional info
```

### Error Handling

Operations raise `RuntimeError` on failure rather than returning error flags:

```python
try:
    result = await connector.execute("customers", "list", {"limit": 10})
    customers = result.data
    for customer in customers:
        print(f"{customer['id']}: {customer['email']}")

    # Check pagination
    if result.meta and hasattr(result.meta, 'pagination'):
        print(f"Has more: {result.meta.pagination.cursor is not None}")
except RuntimeError as e:
    print(f"Operation failed: {e}")
```

### Result Structure by Action

| Action | `result.data` Type | `result.meta` | Example Access |
|--------|-------------------|---------------|----------------|
| `get` | `dict` | Typically None | `customer = result.data` |
| `list` | `list[dict]` | Pagination info | `for item in result.data:` |
| `create` | `dict` | Typically None | `new_id = result.data["id"]` |
| `update` | `dict` | Typically None | `updated = result.data` |
| `delete` | `dict` | Typically None | `deleted_id = result.data["id"]` |
| `api_search` | `list[dict]` | Pagination info | `for match in result.data:` |
| `download` | `AsyncIterator[bytes]` | Stream metadata | `async for chunk in result.data:` |

**Note:** Result types are connector-specific Pydantic models (e.g., `GongExecuteResultWithMeta`). Access `.data` and `.meta` attributes directly. The `result.data` type depends on the action: single-record actions (`get`, `create`, `update`, `delete`) return a `dict`, while multi-record actions (`list`, `api_search`) return a `list[dict]`.

## Pagination

### Cursor-Based Pagination

Most connectors use cursor-based pagination:

```python
async def list_all_customers(connector):
    """Iterate through all customers with pagination."""
    all_customers = []
    cursor = None

    while True:
        params = {"limit": 100}
        if cursor:
            params["starting_after"] = cursor

        try:
            result = await connector.execute("customers", "list", params)
        except RuntimeError as e:
            raise Exception(f"Failed: {e}")

        all_customers.extend(result.data)

        # Check if more pages exist
        if result.meta and hasattr(result.meta, 'pagination') and result.meta.pagination:
            cursor = getattr(result.meta.pagination, 'cursor', None)
            if not cursor:
                break
        else:
            break

    return all_customers
```

### Pagination Parameters by Connector

| Connector | Limit Param | Cursor Param | Meta Fields |
|-----------|-------------|--------------|-------------|
| Stripe | `limit` | `starting_after` | `has_more`, `next_cursor` |
| GitHub | `per_page` | `after` | `has_next_page`, `end_cursor` |
| HubSpot | `limit` | `after` | `has_more`, `next_cursor` |
| Salesforce | `limit` | `next_page_token` | `has_more`, `next_page_token` |
| Slack | `limit` | `cursor` | `has_more`, `next_cursor` |

**Important:** The cursor parameter name varies by connector. Check the connector's REFERENCE.md for the exact parameter name, or use the `result.meta.pagination.cursor` value which provides the cursor in a normalized format.

## Field Selection

Many connectors support selecting specific fields to reduce response size:

```python
# Only return id, email, and name fields
result = await connector.execute("customers", "list", {
    "limit": 100,
    "fields": ["id", "email", "name"]
})

# GitHub: Select specific repository fields
result = await connector.execute("repositories", "get", {
    "owner": "airbytehq",
    "repo": "airbyte",
    "fields": ["name", "description", "stargazerCount", "forkCount"]
})
```

## Validation

Validate operations before executing them to catch errors early. This is especially useful in agent workflows where you want to verify parameters before making API calls.

### Basic Validation

```python
# Validate that entity, action, and params are correct
validation = await connector.validate_operation("customers", "get", {"id": "cus_xxx"})

if validation.is_valid:
    result = await connector.execute("customers", "get", {"id": "cus_xxx"})
else:
    print(f"Validation errors: {validation.errors}")
```

### Validation in Agent Tools

```python
@agent.tool_plain
async def safe_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute an operation with validation."""
    params = params or {}

    # Validate first
    validation = await connector.validate_operation(entity, action, params)
    if not validation.is_valid:
        return f"Invalid operation: {', '.join(validation.errors)}"

    # Execute if valid
    try:
        result = await connector.execute(entity, action, params)
        return json.dumps(result.data)
    except RuntimeError as e:
        return f"Error: {e}"
```

### What Validation Checks

| Check | Description |
|-------|-------------|
| Entity exists | Verifies the entity name is valid for this connector |
| Action supported | Verifies the action is available for this entity |
| Required params | Checks all required parameters are provided |
| Param types | Validates parameter types match expected schema |
| Param values | Checks enum values, ranges, and formats |

### Validation Response

```python
@dataclass
class ValidationResult:
    is_valid: bool
    errors: list[str]  # List of validation error messages
    warnings: list[str]  # Non-blocking issues
```

### Example: Catching Missing Parameters

```python
# Missing required 'owner' parameter
validation = await connector.validate_operation("repositories", "get", {
    "repo": "airbyte"  # Missing 'owner'
})

print(validation.is_valid)  # False
print(validation.errors)    # ["Missing required parameter: owner"]
```

### Example: Invalid Parameter Value

```python
# Invalid state value
validation = await connector.validate_operation("issues", "list", {
    "owner": "airbytehq",
    "repo": "airbyte",
    "states": ["INVALID_STATE"]  # Should be OPEN, CLOSED, or MERGED
})

print(validation.is_valid)  # False
print(validation.errors)    # ["Invalid value for 'states': INVALID_STATE"]
```

## Error Types

The connectors raise specific errors for common failure modes:

| Error | Description | Common Cause |
|-------|-------------|--------------|
| `EntityNotFoundError` | Entity not available in connector | Using wrong entity name |
| `ActionNotSupportedError` | Action not available for entity | E.g., `delete` on read-only entity |
| `MissingParameterError` | Required parameter not provided | Missing `id` on `get` action |
| `InvalidParameterError` | Parameter value is invalid | Wrong type or format |
| `AuthenticationError` | Credentials invalid or expired | Bad API key, expired token |
| `RateLimitError` | API rate limit exceeded | Too many requests |

### Error Handling Example

```python
from airbyte_agent_core.errors import (
    EntityNotFoundError,
    ActionNotSupportedError,
    MissingParameterError,
    AuthenticationError,
    RateLimitError
)

try:
    result = await connector.execute("customers", "get", {"id": "cus_xxx"})
except EntityNotFoundError:
    print("'customers' is not a valid entity for this connector")
except ActionNotSupportedError:
    print("'get' action not supported for customers")
except MissingParameterError as e:
    print(f"Missing required parameter: {e}")
except AuthenticationError:
    print("Authentication failed - check your credentials")
except RateLimitError:
    print("Rate limited - wait and retry")
```

## Using with Agent Frameworks

### Generic Tool Pattern

Create a single tool that handles any entity/action combination:

```python
@agent.tool_plain
@Connector.tool_utils
async def execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute an operation on the connector.

    Args:
        entity: The resource type (e.g., 'customers', 'issues')
        action: The operation (e.g., 'list', 'get', 'create')
        params: Parameters for the operation

    Returns:
        JSON string of the result
    """
    try:
        result = await connector.execute(entity, action, params or {})
        return json.dumps(result.data)
    except RuntimeError as e:
        return f"Error: {e}"
```

### Entity-Specific Tools

Create focused tools for common operations:

```python
@agent.tool_plain
async def list_customers(limit: int = 10, email_filter: str | None = None) -> str:
    """List Stripe customers."""
    params = {"limit": limit}
    if email_filter:
        params["email"] = email_filter
    try:
        result = await connector.execute("customers", "list", params)
        return json.dumps(result.data)
    except RuntimeError as e:
        return f"Error: {e}"

@agent.tool_plain
async def get_customer(customer_id: str) -> str:
    """Get a specific Stripe customer by ID."""
    try:
        result = await connector.execute("customers", "get", {"id": customer_id})
        return json.dumps(result.data)
    except RuntimeError as e:
        return f"Error: {e}"
```

## Discovering Available Entities and Actions

### Programmatic Discovery

```python
# List available entities
entities = connector.list_entities()
print(entities)  # ['customers', 'invoices', 'charges', ...]

# Get entity details
schema = connector.describe_entity("customers")
print(schema)  # Shows available actions and parameters
```

### Reference Documentation

Each connector's REFERENCE.md provides a complete listing:

- [GitHub REFERENCE.md](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/github/REFERENCE.md)
- [Stripe REFERENCE.md](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/stripe/REFERENCE.md)
- [Salesforce REFERENCE.md](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/salesforce/REFERENCE.md)

The reference docs include:
- All entities with descriptions
- Available actions per entity
- Required and optional parameters
- Example code for each operation
