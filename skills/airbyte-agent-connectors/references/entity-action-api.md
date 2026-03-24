# Entity-Action API

Airbyte Agent Connectors use a unified entity-action model for interacting with third-party APIs. This document explains the core concepts, available actions, and how to work with results.

## Contents

- [Core Concepts](#core-concepts)
- [Available Actions](#available-actions)
- [Execution Result](#execution-result)
- [Pagination](#pagination)
- [Field Selection](#field-selection)
- [Validation](#validation)
- [Error Types](#error-types)
- [Using with Agent Frameworks](#using-with-agent-frameworks)
- [Framework Quick Start](#framework-quick-start)
- [Discovering Available Entities and Actions](#discovering-available-entities-and-actions)

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

Return types depend on the action:

- **`list` / `api_search`** actions return a typed envelope:
  ```python
  # For Slack: SlackExecuteResultWithMeta (or similar per connector)
  result.data   # Typed list of Pydantic models (e.g., list[Channel])
  result.meta   # Pagination metadata dict with keys like 'next_cursor', 'has_more'
  ```

- **`get` / `create` / `update` / `delete`** actions return a raw `dict`:
  ```python
  # Returns a dict (raw API response), not a Pydantic model
  user = await connector.execute("users", "get", {"user": "U123"})
  print(user['name'])  # Use dict access, not attribute access
  ```
  > **Note:** The typed query methods (e.g., `connector.users.get()`) return Pydantic models, but the generic `execute()` method returns raw dicts for non-list actions.

- **Errors** are raised as exceptions (`RuntimeError`, `TypeError`, `ValueError`, `NotImplementedError`). There is no `.success` or `.error` attribute on the result — if the call returns, it succeeded.

### Handling Results

```python
# List action — returns envelope with .data and .meta
result = await connector.execute("customers", "list", {"limit": 10})
for customer in result.data:
    print(f"{customer['id']}: {customer.get('email', 'N/A')}")

# Check pagination metadata
if hasattr(result, 'meta') and result.meta:
    next_cursor = result.meta.get('next_cursor')
    if next_cursor:
        print(f"More results available, cursor: {next_cursor}")

# Get action — returns a raw dict
try:
    user = await connector.execute("users", "get", {"user": "U123"})
    print(user['name'])  # dict access, not attribute access
except RuntimeError as e:
    print(f"Operation failed: {e}")
```

### Result Structure by Action

| Action | Return Type | Notes |
|--------|-------------------|-------|
| `get` | `dict` | Single record (raw API response) |
| `list` | Envelope with `.data` and `.meta` | `.data` is a list, `.meta` is a pagination dict |
| `create` | `dict` | Created record |
| `update` | `dict` | Updated record |
| `delete` | `dict` | Deletion confirmation |
| `api_search` | Envelope with `.data` and `.meta` | `.data` is a typed list |
| `download` | `AsyncIterator[bytes]` | Stream for file content |

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

        result = await connector.execute("customers", "list", params)
        all_customers.extend(result.data)

        # Check if more pages exist
        cursor = result.meta.get('next_cursor') if hasattr(result, 'meta') and result.meta else None
        if not cursor:
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

You can discover available entities and actions before executing them to catch errors early. Use `list_entities()` and `entity_schema()` for introspection.

### Discovering Entities and Actions

```python
# List available entities
entities = connector.list_entities()
# Returns list of dicts: [{'entity_name': 'customers', 'available_actions': ['list', 'get', ...], ...}, ...]
for entity in entities:
    print(f"{entity['entity_name']}: {entity['available_actions']}")

# Get schema for an entity
schema = connector.entity_schema("customers")
print(schema)  # JSON schema dict describing the entity structure
```

### Safe Execution in Agent Tools

Since `execute()` raises exceptions on failure, wrap calls in try/except:

```python
@agent.tool_plain
async def safe_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute an operation with error handling."""
    params = params or {}
    try:
        result = await connector.execute(entity, action, params)
        # For list actions, result has .data and .meta
        if hasattr(result, 'data'):
            return json.dumps(result.data, default=str)
        # For get/create/update, result is a raw dict
        return json.dumps(result, default=str)
    except (RuntimeError, TypeError, ValueError) as e:
        return f"Error: {e}"
```

## Error Handling

The `execute()` method raises standard Python exceptions on failure. There is no `.success` or `.error` attribute — if the call returns, it succeeded.

| Error | Common Cause |
|-------|-------------|
| `RuntimeError` | API call failed (e.g., invalid params, auth failure, rate limit) |
| `TypeError` | Wrong parameter types |
| `ValueError` | Invalid parameter values |
| `NotImplementedError` | Action not supported (e.g., `search` in OSS mode) |

### Error Handling Example

```python
try:
    result = await connector.execute("customers", "get", {"id": "cus_xxx"})
except RuntimeError as e:
    # Covers API errors, auth failures, rate limits, etc.
    print(f"Operation failed: {e}")
except TypeError as e:
    print(f"Invalid parameter type: {e}")
except ValueError as e:
    print(f"Invalid parameter value: {e}")
except NotImplementedError:
    print("This action is not supported in the current mode")
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
    result = await connector.execute(entity, action, params or {})
    # For list actions, result has .data; for get/create/update, result is a raw dict
    if hasattr(result, 'data'):
        return json.dumps(result.data, default=str)
    return json.dumps(result, default=str)
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
    result = await connector.execute("customers", "list", params)
    return json.dumps(result.data, default=str)

@agent.tool_plain
async def get_customer(customer_id: str) -> str:
    """Get a specific Stripe customer by ID."""
    result = await connector.execute("customers", "get", {"id": customer_id})
    return json.dumps(result, default=str)  # result is a dict
```

### Framework Quick Start

#### PydanticAI

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", system_prompt="You help with GitHub data.")

@agent.tool_plain
async def github_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

#### LangChain

```python
from langchain.tools import StructuredTool
import asyncio

# For sync contexts, wrap the async call
def execute_sync(entity: str, action: str, params: dict):
    return asyncio.get_event_loop().run_until_complete(
        connector.execute(entity, action, params)
    )

github_tool = StructuredTool.from_function(
    func=execute_sync,
    name="github",
    description="Execute GitHub operations"
)
```

**Note:** If you're already in an async context, use LangChain's async tool support instead.

## Discovering Available Entities and Actions

### Programmatic Discovery

```python
# List available entities
entities = connector.list_entities()
# Returns list of dicts: [{'entity_name': 'customers', 'available_actions': ['list', 'get', ...], ...}, ...]
for entity in entities:
    print(f"{entity['entity_name']}: {entity['available_actions']}")

# Get entity schema
schema = connector.entity_schema("customers")
print(schema)  # JSON schema dict describing the entity structure
```

### Reference Documentation

Each connector's REFERENCE.md provides a complete listing:

- [GitHub REFERENCE.md](../connectors/github/REFERENCE.md)
- [Stripe REFERENCE.md](../connectors/stripe/REFERENCE.md)
- [Salesforce REFERENCE.md](../connectors/salesforce/REFERENCE.md)

The reference docs include:
- All entities with descriptions
- Available actions per entity
- Required and optional parameters
- Example code for each operation
