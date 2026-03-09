<!-- AUTO-GENERATED from connectors/asana/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Asana AI Connector

# Package: airbyte-ai-asana v0.19.0

Type-safe Asana API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-asana` v0.19.0
- **Auth:** AsanaAuthConfig (token)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/asana)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-asana
```

### Usage

```python
from airbyte_ai_asana import AsanaConnector
from airbyte_ai_asana.models import AsanaAuthConfig

# Create connector
connector = AsanaConnector(auth_config=AsanaAuthConfig(token="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Tasks | `list_tasks()` | Returns all tasks in a project |
| Tasks | `get_task()` | Get a single task by its ID |
| Projects | `list_projects()` | Returns a paginated list of projects |
| Projects | `get_project()` | Get a single project by its ID |
| Workspaces | `list_workspaces()` | Returns a paginated list of workspaces |
| Workspaces | `get_workspace()` | Get a single workspace by its ID |
| Users | `list_users()` | Returns a paginated list of users |
| Users | `get_user()` | Get a single user by their ID |

## Authentication

Auth class: `AsanaAuthConfig`

Required fields:

- `token`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/asana)*
