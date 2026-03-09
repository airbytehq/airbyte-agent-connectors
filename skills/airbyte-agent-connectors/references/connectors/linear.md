<!-- AUTO-GENERATED from connectors/linear/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Linear AI Connector

# Package: airbyte-ai-linear v0.19.0

Type-safe Linear API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-linear` v0.19.0
- **Auth:** LinearAuthConfig (api_key)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/linear)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-linear
```

### Usage

```python
from airbyte_ai_linear import LinearConnector
from airbyte_ai_linear.models import LinearAuthConfig

# Create connector
connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Issues | `list_issues()` | Returns a paginated list of issues via GraphQL with pagination support |
| Issues | `get_issue()` | Get a single issue by ID via GraphQL |
| Projects | `list_projects()` | Returns a paginated list of projects via GraphQL with pagination support |
| Projects | `get_project()` | Get a single project by ID via GraphQL |
| Teams | `list_teams()` | Returns a list of teams via GraphQL with pagination support |
| Teams | `get_team()` | Get a single team by ID via GraphQL |

## Authentication

Auth class: `LinearAuthConfig`

Required fields:

- `api_key`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/linear)*
