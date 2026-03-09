<!-- AUTO-GENERATED from connectors/gmail/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Gmail

The Gmail agent connector is a Python package that equips AI agents to interact with Gmail through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-gmail` v0.1.16
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.google.com/gmail/api/reference/rest)
- **Status:** complete

## Example Prompts

- List my recent emails
- Show me unread messages in my inbox
- Get the details of a specific email
- List all my Gmail labels
- Show me details for a specific label
- List my email drafts
- Get the content of a specific draft
- List my email threads
- Show me the full thread for a conversation
- Get my Gmail profile information
- Send an email to someone
- Create a new email draft
- Archive a message by removing the INBOX label
- Mark a message as read
- Mark a message as unread
- Move a message to trash
- Create a new label
- Update a label name or settings
- Delete a label
- Search for messages matching a query
- Find emails from a specific sender
- Show me emails with attachments

## Unsupported

- Attach a file to an email
- Forward an email to someone
- Create a filter or rule
- Manage Gmail settings
- Access Google Calendar events
- Manage contacts

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-gmail
```

### OSS Mode

```python
from airbyte_agent_gmail import GmailConnector
from airbyte_agent_gmail.models import GmailAuthConfig

connector = GmailConnector(
    auth_config=GmailAuthConfig(
        access_token="<Your Google OAuth2 Access Token (optional, will be obtained via refresh)>",
        refresh_token="<Your Google OAuth2 Refresh Token>",
        client_id="<Your Google OAuth2 Client ID>",
        client_secret="<Your Google OAuth2 Client Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GmailConnector.tool_utils
async def gmail_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_gmail import GmailConnector, AirbyteAuthConfig

connector = GmailConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GmailConnector.tool_utils
async def gmail_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Profile | Get |
| Messages | List, Get, Create, Update |
| Labels | List, Create, Get, Update, Delete |
| Drafts | List, Create, Get, Update, Delete |
| Drafts Send | Create |
| Threads | List, Get |
| Messages Trash | Create |
| Messages Untrash | Create |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gmail/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/gmail/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/gmail)*
