# Airbyte Github AI Connector

Type-safe Github API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.7.0

**Connector Version:** 1.0.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-github
```

## Usage

```python
from airbyte_ai_github import GithubConnector

# Create connector
connector = GithubConnector.create(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Repositories Operations
- `repositories__get()` - Get a repository
- `repositories__list()` - List repositories for a user
- `repositories__search()` - Search GitHub repositories using GraphQL

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_github.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
