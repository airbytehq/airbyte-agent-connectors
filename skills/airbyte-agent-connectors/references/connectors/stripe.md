<!-- AUTO-GENERATED from connectors/stripe/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Stripe

The Stripe agent connector is a Python package that equips AI agents to interact with Stripe through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-stripe` v0.5.113
- **Auth:** Token
- **Docs:** [Official API docs](https://docs.stripe.com/api)
- **Status:** complete

## Example Prompts

- List customers created in the last 7 days
- Show me details for a recent customer
- List recent charges
- Show me details for a recent charge
- List recent invoices
- List active subscriptions
- Show me my top 10 customers by total revenue this month
- List all customers who have spent over $5,000 in the last quarter
- Analyze payment trends for my Stripe customers
- Identify which customers have the most consistent subscription payments
- Give me insights into my customer retention rates
- Summarize the payment history for \{customer\}
- Compare customer spending patterns from last month to this month
- Show me details about my highest-value Stripe customers
- What are the key financial insights from my customer base?
- Break down my customers by their average transaction value

## Unsupported

- Create a new customer profile in Stripe
- Update the billing information for \{customer\}
- Delete a customer record
- Send a payment reminder to \{customer\}
- Schedule an automatic invoice for \{company\}

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-stripe
```

### OSS Mode

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = StripeConnector(
    auth_config=StripeAuthConfig(
        api_key="<Your Stripe API Key (starts with sk_test_ or sk_live_)>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_stripe import StripeConnector, AirbyteAuthConfig

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Customers | List, Create, Get, Update, Delete, API Search, Search |
| Invoices | List, Get, API Search, Search |
| Charges | List, Get, API Search, Search |
| Subscriptions | List, Get, API Search, Search |
| Refunds | List, Create, Get, Search |
| Products | List, Create, Get, Update, Delete, API Search |
| Balance | Get |
| Balance Transactions | List, Get |
| Payment Intents | List, Get, API Search |
| Disputes | List, Get |
| Payouts | List, Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/stripe/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/stripe/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/stripe)*
