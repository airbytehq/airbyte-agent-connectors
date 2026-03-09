<!-- AUTO-GENERATED from connectors/zendesk-talk/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Zendesk Talk

The Zendesk-Talk agent connector is a Python package that equips AI agents to interact with Zendesk-Talk through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-zendesk-talk` v0.1.0
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://developer.zendesk.com/api-reference/voice/talk-api/introduction/)
- **Status:** complete

## Example Prompts

- List all phone numbers in our Zendesk Talk account
- Show all addresses on file
- List all IVR configurations
- Show all greetings
- List greeting categories
- Show agent activity statistics
- Show the account overview stats
- Show current queue activity
- Which phone numbers have SMS enabled?
- Find agents who have missed the most calls today
- What is the average call duration across all calls?
- Which phone numbers are toll-free?

## Unsupported

- Create a new phone number
- Delete an IVR configuration
- Update a greeting
- Make an outbound call

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-zendesk-talk
```

### OSS Mode

```python
from airbyte_agent_zendesk_talk import ZendeskTalkConnector
from airbyte_agent_zendesk_talk.models import ZendeskTalkApiTokenAuthConfig

connector = ZendeskTalkConnector(
    auth_config=ZendeskTalkApiTokenAuthConfig(
        email="<Your Zendesk account email address>",
        api_token="<Your Zendesk API token from Admin Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskTalkConnector.tool_utils
async def zendesk_talk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_zendesk_talk import ZendeskTalkConnector, AirbyteAuthConfig

connector = ZendeskTalkConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ZendeskTalkConnector.tool_utils
async def zendesk_talk_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Phone Numbers | List, Get, Search |
| Addresses | List, Get, Search |
| Greetings | List, Get, Search |
| Greeting Categories | List, Get, Search |
| Ivrs | List, Get, Search |
| Agents Activity | List, Search |
| Agents Overview | List, Search |
| Account Overview | List, Search |
| Current Queue Activity | List, Search |
| Calls | List, Search |
| Call Legs | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-talk/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/zendesk-talk/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/zendesk-talk)*
