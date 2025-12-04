# Airbyte Asana AI Connector

Type-safe Asana API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.13.0

**Connector Version:** 1.0.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-asana
```

## Usage

```python
from airbyte_ai_asana import AsanaConnector

# Create connector
connector = AsanaConnector(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Tasks Operations
- `list_tasks()` - Returns all tasks in a project
- `get_task()` - Get a single task by its ID

### Projects Operations
- `list_projects()` - Returns a paginated list of projects
- `get_project()` - Get a single project by its ID

### Workspaces Operations
- `list_workspaces()` - Returns a paginated list of workspaces
- `get_workspace()` - Get a single workspace by its ID

### Users Operations
- `list_users()` - Returns a paginated list of users
- `get_user()` - Get a single user by their ID

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_asana.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
