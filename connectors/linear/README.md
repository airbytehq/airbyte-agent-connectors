# Airbyte Linear AI Connector

Type-safe Linear API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.9.0

**Connector Version:** 1.0.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-linear
```

## Usage

```python
from airbyte_ai_linear import LinearConnector

# Create connector
connector = LinearConnector(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Issues Operations
- `list_issues()` - List issues
- `get_issue()` - Get an issue

### Projects Operations
- `list_projects()` - List projects
- `get_project()` - Get a project

### Teams Operations
- `list_teams()` - List teams
- `get_team()` - Get a team

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_linear.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
