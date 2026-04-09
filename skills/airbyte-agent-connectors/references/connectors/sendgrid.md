<!-- AUTO-GENERATED from connectors/sendgrid/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-04-09 -->

# SendGrid

The Sendgrid agent connector is a Python package that equips AI agents to interact with Sendgrid through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-sendgrid` v0.1.23
- **Auth:** Token
- **Docs:** [Official API docs](https://docs.sendgrid.com/api-reference)
- **Status:** complete

## Example Prompts

- List all marketing contacts
- Get the details of a specific contact
- Show me all marketing lists
- List all transactional templates
- Show all single sends
- List all bounced emails
- Show all blocked email addresses
- List all spam reports
- Show all suppression groups
- How many contacts are in each marketing list?
- Which single sends were scheduled in the last month?
- What are the most common bounce reasons?
- Show me contacts created in the last 7 days

## Unsupported

- Send an email
- Create a new contact
- Delete a bounce record
- Update a marketing list

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-sendgrid
```

### OSS Mode

```python
from airbyte_agent_sendgrid import SendgridConnector
from airbyte_agent_sendgrid.models import SendgridAuthConfig

connector = SendgridConnector(
    auth_config=SendgridAuthConfig(
        api_key="<Your SendGrid API key (generated at https://app.sendgrid.com/settings/api_keys)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SendgridConnector.tool_utils
async def sendgrid_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_sendgrid import SendgridConnector, AirbyteAuthConfig

connector = SendgridConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SendgridConnector.tool_utils
async def sendgrid_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Contacts | List, Get, Context Store Search |
| Lists | List, Get, Context Store Search |
| Segments | List, Get, Context Store Search |
| Campaigns | List, Context Store Search |
| Singlesends | List, Get, Context Store Search |
| Templates | List, Get, Context Store Search |
| Singlesend Stats | List, Context Store Search |
| Bounces | List, Context Store Search |
| Blocks | List, Context Store Search |
| Spam Reports | List |
| Invalid Emails | List, Context Store Search |
| Global Suppressions | List, Context Store Search |
| Suppression Groups | List, Get, Context Store Search |
| Suppression Group Members | List, Context Store Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/sendgrid/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/sendgrid/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/sendgrid)*
