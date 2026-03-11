<!-- AUTO-GENERATED from connectors/paypal-transaction/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# PayPal Transaction

The Paypal-Transaction agent connector is a Python package that equips AI agents to interact with Paypal-Transaction through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-paypal-transaction` v0.1.0
- **Auth:** OAuth
- **Docs:** [Official API docs](https://developer.paypal.com/docs/api/transaction-search/v1/)
- **Status:** complete

## Example Prompts

- List all balances for my PayPal account
- Show recent transactions from the last 7 days
- List all catalog products
- Show details for a specific product
- List all disputes
- Show recent payments
- What transactions had the highest amounts last month?
- Find all declined transactions
- Show disputes grouped by status
- What is the total balance across all currencies?

## Unsupported

- Create a new payment
- Refund a transaction
- Delete a dispute
- Update product details

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-paypal-transaction
```

### OSS Mode

```python
from airbyte_agent_paypal_transaction import PaypalTransactionConnector
from airbyte_agent_paypal_transaction.models import PaypalTransactionAuthConfig

connector = PaypalTransactionConnector(
    auth_config=PaypalTransactionAuthConfig(
        client_id="<The Client ID of your PayPal developer application.>",
        client_secret="<The Client Secret of your PayPal developer application.>",
        access_token="<OAuth2 access token obtained via client credentials grant. Use the PayPal token endpoint with your client_id and client_secret to obtain this.
>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PaypalTransactionConnector.tool_utils
async def paypal_transaction_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_paypal_transaction import PaypalTransactionConnector, AirbyteAuthConfig

connector = PaypalTransactionConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@PaypalTransactionConnector.tool_utils
async def paypal_transaction_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Balances | List, Search |
| Transactions | List, Search |
| List Payments | List, Search |
| List Disputes | List, Search |
| List Products | List, Search |
| Show Product Details | Get, Search |
| Search Invoices | List, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/paypal-transaction/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/paypal-transaction/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/paypal-transaction)*
