# Airbyte Github AI Connector

Type-safe Github API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.18.0

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-github
```

## Usage

```python
from airbyte_ai_github import GithubConnector
from airbyte_ai_github.models import GithubAuthConfig

# Create connector
connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Repositories Operations
- `repositories__get()` - Gets information about a specific GitHub repository using GraphQL
- `repositories__list()` - Returns a list of repositories for the specified user using GraphQL
- `repositories__search()` - Search for GitHub repositories using GitHub's powerful search syntax.
Examples: "language:python stars:>1000", "topic:machine-learning", "org:facebook is:public"


## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_github.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
