<!-- AUTO-GENERATED from connectors/mailchimp/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Mailchimp

The Mailchimp agent connector is a Python package that equips AI agents to interact with Mailchimp through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-mailchimp` v0.1.70
- **Auth:** Token
- **Docs:** [Official API docs](https://mailchimp.com/developer/marketing/api/)
- **Status:** complete

## Example Prompts

- List all subscribers in my main mailing list
- List all automation workflows in my account
- Show me all segments for my primary audience
- List all interest categories for my primary audience
- Show me email activity for a recent campaign
- Show me the performance report for a recent campaign
- Show me all my email campaigns from the last month
- What are the open rates for my recent campaigns?
- Who unsubscribed from list \{list_id\} this week?
- What tags are applied to my subscribers?
- How many subscribers do I have in each list?
- What are my top performing campaigns by click rate?

## Unsupported

- Create a new email campaign
- Add a subscriber to my list
- Delete a campaign
- Update subscriber information
- Send a campaign now
- Create a new automation workflow

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-mailchimp
```

### OSS Mode

```python
from airbyte_agent_mailchimp import MailchimpConnector
from airbyte_agent_mailchimp.models import MailchimpAuthConfig

connector = MailchimpConnector(
    auth_config=MailchimpAuthConfig(
        api_key="<Your Mailchimp API key. You can find this in your Mailchimp account under Account > Extras > API keys.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@MailchimpConnector.tool_utils
async def mailchimp_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_mailchimp import MailchimpConnector, AirbyteAuthConfig

connector = MailchimpConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@MailchimpConnector.tool_utils
async def mailchimp_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Campaigns | List, Get, Search |
| Lists | List, Get, Search |
| List Members | List, Get |
| Reports | List, Get, Search |
| Email Activity | List, Search |
| Automations | List |
| Tags | List |
| Interest Categories | List, Get |
| Interests | List, Get |
| Segments | List, Get |
| Segment Members | List |
| Unsubscribes | List |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/mailchimp/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/mailchimp/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/mailchimp)*
