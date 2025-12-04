# Airbyte Linear AI Connector

Type-safe Linear API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.14.0

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
- `list_issues()` - Returns a paginated list of issues via GraphQL with pagination support
- `get_issue()` - Get a single issue by ID via GraphQL

### Projects Operations
- `list_projects()` - Returns a paginated list of projects via GraphQL with pagination support
- `get_project()` - Get a single project by ID via GraphQL

### Teams Operations
- `list_teams()` - Returns a list of teams via GraphQL with pagination support
- `get_team()` - Get a single team by ID via GraphQL

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_linear.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
