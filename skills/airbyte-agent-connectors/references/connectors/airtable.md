<!-- AUTO-GENERATED from connectors/airtable/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Airtable

The Airtable agent connector is a Python package that equips AI agents to interact with Airtable through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-airtable` v0.1.43
- **Auth:** Token
- **Docs:** [Official API docs](https://airtable.com/developers/web/api/introduction)
- **Status:** complete

## Example Prompts

- List all my Airtable bases
- What tables are in my first base?
- Show me the schema for tables in a base
- List records from a table in my base
- Show me recent records from a table
- What fields are in a table?
- List records where Status is 'Done' in table tblXXX
- Find records created last week in table tblXXX
- Show me records updated in the last 30 days in base appXXX

## Unsupported

- Create a new record in Airtable
- Update a record in Airtable
- Delete a record from Airtable
- Create a new table
- Modify table schema

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-airtable
```

### OSS Mode

```python
from airbyte_agent_airtable import AirtableConnector
from airbyte_agent_airtable.models import AirtableAuthConfig

connector = AirtableConnector(
    auth_config=AirtableAuthConfig(
        personal_access_token="<Airtable Personal Access Token. See https://airtable.com/developers/web/guides/personal-access-tokens>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AirtableConnector.tool_utils
async def airtable_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_airtable import AirtableConnector, AirbyteAuthConfig

connector = AirtableConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AirtableConnector.tool_utils
async def airtable_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Bases | List, Search |
| Tables | List, Search |
| Records | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/airtable/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/airtable/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/airtable)*
