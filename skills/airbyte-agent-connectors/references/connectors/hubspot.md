<!-- AUTO-GENERATED from connectors/hubspot/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airbyte Hubspot AI Connector

# Package: airbyte-ai-hubspot v0.15.0

Type-safe Hubspot API connector with full IDE autocomplete support for AI applications.

**Key metadata:**

- **Package:** `airbyte-ai-hubspot` v0.15.0
- **Auth:** HubspotAuthConfig (access_token)
- **Docs:** [Official API docs](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/hubspot)
- **Status:** docs pending

## Quick Start

### Installation

```bash
uv pip install airbyte-ai-hubspot
```

### Usage

```python
from airbyte_ai_hubspot import HubspotConnector
from airbyte_ai_hubspot.models import HubspotAuthConfig

# Create connector
connector = HubspotConnector(auth_config=HubspotAuthConfig(access_token="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Entities and Actions

| Entity | Action | Description |
|--------|--------|-------------|
| Contacts | `list_contacts()` | Returns a paginated list of contacts |
| Contacts | `get_contact()` | Get a single contact by ID |
| Companies | `list_companies()` | Returns a paginated list of companies |
| Companies | `get_company()` | Get a single company by ID |
| Deals | `list_deals()` | Returns a paginated list of deals |
| Deals | `get_deal()` | Get a single deal by ID |
| Tickets | `list_tickets()` | Returns a paginated list of tickets |
| Tickets | `get_ticket()` | Get a single ticket by ID |
| Schemas | `list_schemas()` | Returns all custom object schemas to discover available custom objects |
| Objects | `list_objects()` | Returns a paginated list of objects for any custom object type |
| Objects | `get_object()` | Get a single object by ID for any custom object type |

## Authentication

Auth class: `HubspotAuthConfig`

Required fields:

- `access_token`

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-ai-connectors/tree/main/connectors/hubspot)*
