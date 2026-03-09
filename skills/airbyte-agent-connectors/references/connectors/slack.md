<!-- AUTO-GENERATED from connectors/slack/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Slack

The Slack agent connector is a Python package that equips AI agents to interact with Slack through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-slack` v0.1.79
- **Auth:** OAuth, Token
- **Docs:** [Official API docs](https://api.slack.com/methods)
- **Status:** complete

## Example Prompts

- List all users in my Slack workspace
- Show me all public channels
- List members of a public channel
- Show me recent messages in a public channel
- Show me thread replies for a recent message
- List all channels I have access to
- Show me user details for a workspace member
- List channel members for a public channel
- Send a message to a channel saying 'Hello team!'
- Post a message in the general channel
- Update the most recent message in a channel
- Create a new public channel called 'project-updates'
- Create a private channel named 'team-internal'
- Rename a channel to 'new-channel-name'
- Set the topic for a channel to 'Daily standup notes'
- Update the purpose of a channel
- Add a thumbsup reaction to the latest message in a channel
- React with :rocket: to the latest message in a channel
- Reply to a recent thread with 'Thanks for the update!'
- What messages were posted in channel \{channel_id\} last week?
- Show me the conversation history for channel \{channel_id\}
- Search for messages mentioning \{keyword\} in channel \{channel_id\}

## Unsupported

- Delete a message from channel \{channel_id\}
- Remove a reaction from a message
- Archive channel \{channel_id\}
- Invite user \{user_id\} to channel \{channel_id\}
- Remove user \{user_id\} from channel \{channel_id\}
- Delete channel \{channel_id\}
- Create a new user in the workspace
- Update user profile information

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-slack
```

### OSS Mode

```python
from airbyte_agent_slack import SlackConnector
from airbyte_agent_slack.models import SlackTokenAuthenticationAuthConfig

connector = SlackConnector(
    auth_config=SlackTokenAuthenticationAuthConfig(
        api_token="<Your Slack Bot Token (xoxb-) or User Token (xoxp-)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SlackConnector.tool_utils
async def slack_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_slack import SlackConnector, AirbyteAuthConfig

connector = SlackConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SlackConnector.tool_utils
async def slack_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Users | List, Get, Search |
| Channels | List, Get, Create, Update, Search |
| Channel Messages | List |
| Threads | List |
| Messages | Create, Update |
| Channel Topics | Create |
| Channel Purposes | Create |
| Reactions | Create |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/slack/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/slack/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/slack)*
