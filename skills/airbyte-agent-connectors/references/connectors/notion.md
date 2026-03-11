<!-- AUTO-GENERATED from connectors/notion/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Notion

The Notion agent connector is a Python package that equips AI agents to interact with Notion through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-notion` v0.1.15
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.notion.com/reference/intro)
- **Status:** complete

## Example Prompts

- List all users in my Notion workspace
- Show me all pages in my Notion workspace
- What data sources exist in my Notion workspace?
- Get the details of a specific page by ID
- List child blocks of a specific page
- Show me comments on a specific page
- What is the schema of a specific data source?
- Who are the bot users in my workspace?
- Find pages created in the last week
- List data sources that have been recently edited
- Show me all archived pages

## Unsupported

- Create a new page in Notion
- Update a data source property
- Delete a block
- Add a comment to a page

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-notion
```

### OSS Mode

```python
from airbyte_agent_notion import NotionConnector
from airbyte_agent_notion.models import NotionAuthConfig

connector = NotionConnector(
    auth_config=NotionAuthConfig(
        token="<Notion internal integration token (starts with ntn_ or secret_)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@NotionConnector.tool_utils
async def notion_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_notion import NotionConnector, AirbyteAuthConfig

connector = NotionConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@NotionConnector.tool_utils
async def notion_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Users | List, Get, Search |
| Pages | List, Get, Search |
| Data Sources | List, Get, Search |
| Blocks | List, Get, Search |
| Comments | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/notion/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/notion/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/notion)*
