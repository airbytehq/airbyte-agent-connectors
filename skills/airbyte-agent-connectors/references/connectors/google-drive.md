<!-- AUTO-GENERATED from connectors/google-drive/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Google Drive

The Google-Drive agent connector is a Python package that equips AI agents to interact with Google-Drive through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-google-drive` v0.1.86
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developers.google.com/workspace/drive/api/reference/rest/v3)
- **Status:** complete

## Example Prompts

- List all files in my Google Drive
- Show me details for a recent file
- Download a recent file from my Drive
- Export a recent Google Doc as PDF
- Export a recent Google Sheet as CSV
- Show me the content of a recent file
- List all shared drives I have access to
- Show me details for a shared drive I have access to
- Show permissions for a recent file
- List comments on a recent file
- Show replies to a recent comment on a file
- Show revision history for a recent file
- Get my Drive storage quota and user info
- List files in a folder I have access to
- Create a new file in Google Drive
- Upload a document to Drive
- Delete a file from Drive
- Move a file to a different folder
- Show me files modified in the last week
- What changes have been made since my last sync?

## Unsupported

- Update file permissions
- Add a comment to a file

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-google-drive
```

### OSS Mode

```python
from airbyte_agent_google_drive import GoogleDriveConnector
from airbyte_agent_google_drive.models import GoogleDriveAuthConfig

connector = GoogleDriveConnector(
    auth_config=GoogleDriveAuthConfig(
        access_token="<Your Google OAuth2 Access Token (optional, will be obtained via refresh)>",
        refresh_token="<Your Google OAuth2 Refresh Token>",
        client_id="<Your Google OAuth2 Client ID>",
        client_secret="<Your Google OAuth2 Client Secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleDriveConnector.tool_utils
async def google_drive_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_google_drive import GoogleDriveConnector, AirbyteAuthConfig

connector = GoogleDriveConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GoogleDriveConnector.tool_utils
async def google_drive_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Files | List, Get, Create, Update, Delete, Download |
| Files Upload | Create |
| Files Export | Download |
| Drives | List, Get |
| Permissions | List, Get |
| Comments | List, Get |
| Replies | List, Get |
| Revisions | List, Get |
| Changes | List |
| Changes Start Page Token | Get |
| About | Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-drive/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/google-drive/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/google-drive)*
