<!-- AUTO-GENERATED from connectors/zendesk-chat/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Zendesk Chat

The Zendesk-Chat agent connector is a Python package that equips AI agents to interact with Zendesk-Chat through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-zendesk-chat` v0.1.65
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developer.zendesk.com/api-reference/live-chat/chat-api/introduction/)
- **Status:** complete

## Example Prompts

- List all banned visitors
- List all departments with their settings
- Show me all chats from last week
- List all agents in the support department
- What are the most used chat shortcuts?
- Show chat volume by department
- What triggers are currently active?
- Show agent activity timeline for today

## Unsupported

- Start a new chat session
- Send a message to a visitor
- Create a new agent
- Update department settings
- Delete a shortcut

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-zendesk-chat
```

### OSS Mode

```python
from airbyte_agent_zendesk_chat import ZendeskChatConnector
from airbyte_agent_zendesk_chat.models import ZendeskChatAuthConfig

connector = ZendeskChatConnector(
    auth_config=ZendeskChatAuthConfig(
        access_token="<Your Zendesk Chat OAuth 2.0 access token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskChatConnector.tool_utils
async def zendesk_chat_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_zendesk_chat import ZendeskChatConnector, AirbyteAuthConfig

connector = ZendeskChatConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskChatConnector.tool_utils
async def zendesk_chat_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Accounts | Get |
| Agents | List, Get, Search |
| Agent Timeline | List |
| Bans | List, Get |
| Chats | List, Get, Search |
| Departments | List, Get, Search |
| Goals | List, Get |
| Roles | List, Get |
| Routing Settings | Get |
| Shortcuts | List, Get, Search |
| Skills | List, Get |
| Triggers | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-chat/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-chat/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zendesk-chat)*
