<!-- AUTO-GENERATED from connectors/github/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Github AI Connector

# Package: airbyte-ai-github v0.18.0

Type-safe Github API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-github` v0.18.0
- **Auth:** GithubAuthConfig (access_token, refresh_token, client_id, client_secret)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/github)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-github
```

### Usage

```python
from airbyte_ai_github import GithubConnector
from airbyte_ai_github.models import GithubAuthConfig

# Create connector
connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Repositories | `repositories__get()` | Gets information about a specific GitHub repository using GraphQL |
| Repositories | `repositories__list()` | Returns a list of repositories for the specified user using GraphQL |
| Repositories | `repositories__search()` | Search for GitHub repositories using GitHub's powerful search syntax. |

## Authentication

Auth class: `GithubAuthConfig`

Required fields:

- `access_token`
- `refresh_token`
- `client_id`
- `client_secret`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/github)*
