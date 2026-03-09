<!-- AUTO-GENERATED from connectors/typeform/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Typeform

The Typeform agent connector is a Python package that equips AI agents to interact with Typeform through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-typeform` v0.1.0
- **Auth:** Token
- **Docs:** [Official API docs](https://developer.typeform.com/)
- **Status:** complete

## Example Prompts

- List all my typeforms
- Show me the responses for my latest form
- What workspaces do I have?
- List all themes in my account
- Get the details of a specific form
- Which forms received the most responses last month?
- Find responses submitted in the last week
- What forms were created this year?
- Show me all forms in a specific workspace

## Unsupported

- Create a new typeform
- Delete a form response
- Update form settings
- Send a webhook notification

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-typeform
```

### OSS Mode

```python
from airbyte_agent_typeform import TypeformConnector
from airbyte_agent_typeform.models import TypeformAuthConfig

connector = TypeformConnector(
    auth_config=TypeformAuthConfig(
        access_token="<Personal access token from your Typeform account settings>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TypeformConnector.tool_utils
async def typeform_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_typeform import TypeformConnector, AirbyteAuthConfig

connector = TypeformConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TypeformConnector.tool_utils
async def typeform_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Forms | List, Get, Search |
| Responses | List, Search |
| Webhooks | List, Search |
| Workspaces | List, Search |
| Images | List, Search |
| Themes | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/typeform/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/typeform/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/typeform)*
