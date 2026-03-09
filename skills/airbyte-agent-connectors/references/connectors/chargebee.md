<!-- AUTO-GENERATED from connectors/chargebee/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Chargebee

The Chargebee agent connector is a Python package that equips AI agents to interact with Chargebee through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-chargebee` v0.1.1
- **Auth:** Token
- **Docs:** [Official API docs](https://apidocs.chargebee.com/docs/api)
- **Status:** complete

## Example Prompts

- List all active subscriptions
- Show me details for a specific customer
- List recent invoices
- Show me details for a specific subscription
- List all coupons
- List recent transactions
- List recent events
- Show me customers with the highest monthly recurring revenue
- Which subscriptions are set to cancel in the next 30 days?
- List all overdue invoices and their amounts
- Analyze subscription churn trends over the past quarter
- What are the most popular items by number of subscriptions?
- Show me total revenue breakdown by currency
- Identify customers with expiring payment sources
- Compare subscription plan distribution across item prices
- List all credit notes issued in the past month
- What is the average subscription lifetime for each plan?

## Unsupported

- Create a new subscription in Chargebee
- Update a customer's billing address
- Cancel a subscription
- Apply a coupon to a subscription
- Issue a refund for an invoice

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-chargebee
```

### OSS Mode

```python
from airbyte_agent_chargebee import ChargebeeConnector
from airbyte_agent_chargebee.models import ChargebeeAuthConfig

connector = ChargebeeConnector(
    auth_config=ChargebeeAuthConfig(
        api_key="<Your Chargebee API key (used as the HTTP Basic username)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ChargebeeConnector.tool_utils
async def chargebee_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_chargebee import ChargebeeConnector, AirbyteAuthConfig

connector = ChargebeeConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@ChargebeeConnector.tool_utils
async def chargebee_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Customer | List, Get, Search |
| Subscription | List, Get, Search |
| Invoice | List, Get, Search |
| Credit Note | List, Get, Search |
| Coupon | List, Get, Search |
| Transaction | List, Get, Search |
| Event | List, Get, Search |
| Order | List, Get, Search |
| Item | List, Get, Search |
| Item Price | List, Get, Search |
| Payment Source | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/chargebee/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/chargebee/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/chargebee)*
