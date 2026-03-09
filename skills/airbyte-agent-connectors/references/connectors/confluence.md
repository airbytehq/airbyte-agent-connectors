<!-- AUTO-GENERATED from connectors/confluence/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Confluence

The Confluence agent connector is a Python package that equips AI agents to interact with Confluence through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-confluence` v0.1.0
- **Auth:** Token
- **Docs:** [Official API docs](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- **Status:** complete

## Example Prompts

- List all spaces in my Confluence instance
- Show me the most recently created pages
- List all blog posts
- Show me details for a specific page
- List all groups in Confluence
- Show me recent audit log entries
- Get details about a specific space
- Show me blog post details
- Find pages created in the last 7 days
- What spaces have the most pages?
- Show me all pages in a specific space
- Find blog posts by a specific author
- What audit events happened this week?

## Unsupported

- Create a new page in Confluence
- Update an existing page
- Delete a space
- Upload an attachment to a page
- Manage space permissions

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-confluence
```

### OSS Mode

```python
from airbyte_agent_confluence import ConfluenceConnector
from airbyte_agent_confluence.models import ConfluenceAuthConfig

connector = ConfluenceConnector(
    auth_config=ConfluenceAuthConfig(
        username="<Your Atlassian account email address>",
        password="<Your Confluence API token from https://id.atlassian.com/manage-profile/security/api-tokens>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ConfluenceConnector.tool_utils
async def confluence_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_confluence import ConfluenceConnector, AirbyteAuthConfig

connector = ConfluenceConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ConfluenceConnector.tool_utils
async def confluence_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Spaces | List, Get, Search |
| Pages | List, Get, Search |
| Blog Posts | List, Get, Search |
| Groups | List, Search |
| Audit | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/confluence/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/confluence/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/confluence)*
