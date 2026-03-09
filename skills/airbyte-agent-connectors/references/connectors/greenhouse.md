<!-- AUTO-GENERATED from connectors/greenhouse/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Greenhouse AI Connector

# Package: airbyte-ai-greenhouse v0.17.0

Type-safe Greenhouse API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-greenhouse` v0.17.0
- **Auth:** GreenhouseAuthConfig (api_key)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/greenhouse)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-greenhouse
```

### Usage

```python
from airbyte_ai_greenhouse import GreenhouseConnector
from airbyte_ai_greenhouse.models import GreenhouseAuthConfig

# Create connector
connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Candidates | `list_candidates()` | Returns a paginated list of all candidates in the organization |
| Candidates | `get_candidate()` | Get a single candidate by ID |
| Applications | `list_applications()` | Returns a paginated list of all applications |
| Applications | `get_application()` | Get a single application by ID |
| Jobs | `list_jobs()` | Returns a paginated list of all jobs in the organization |
| Jobs | `get_job()` | Get a single job by ID |

## Authentication

Auth class: `GreenhouseAuthConfig`

Required fields:

- `api_key`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/greenhouse)*
