<!-- AUTO-GENERATED from connectors/gong/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Gong

The Gong agent connector is a Python package that equips AI agents to interact with Gong through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-gong` v0.19.121
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://gong.app.gong.io/settings/api/documentation)
- **Status:** complete

## Example Prompts

- List all users in my Gong account
- Show me calls from last week
- Get the transcript for a recent call
- List all workspaces in Gong
- Show me the scorecard configurations
- What trackers are set up in my account?
- Get coaching metrics for a manager
- What are the activity stats for our sales team?
- Find calls mentioning \{keyword\} this month
- Show me calls for rep \{user_id\} in the last 30 days
- Which calls had the longest duration last week?

## Unsupported

- Create a new user in Gong
- Delete a call recording
- Update scorecard questions
- Schedule a new meeting
- Send feedback to a team member
- Modify tracker keywords

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-gong
```

### OSS Mode

```python
from airbyte_agent_gong import GongConnector
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig

connector = GongConnector(
    auth_config=GongAccessKeyAuthenticationAuthConfig(
        access_key="<Your Gong API Access Key>",
        access_key_secret="<Your Gong API Access Key Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GongConnector.tool_utils
async def gong_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_gong import GongConnector, AirbyteAuthConfig

connector = GongConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GongConnector.tool_utils
async def gong_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Users | List, Get, Search |
| Calls | List, Get, Search |
| Calls Extensive | List, Search |
| Call Audio | Download |
| Call Video | Download |
| Workspaces | List |
| Call Transcripts | List |
| Stats Activity Aggregate | List |
| Stats Activity Day By Day | List |
| Stats Interaction | List |
| Settings Scorecards | List, Search |
| Settings Trackers | List |
| Library Folders | List |
| Library Folder Content | List |
| Coaching | List |
| Stats Activity Scorecards | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gong/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gong/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/gong)*
