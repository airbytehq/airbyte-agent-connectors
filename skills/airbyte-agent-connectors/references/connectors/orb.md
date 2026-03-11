<!-- AUTO-GENERATED from connectors/orb/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Orb

The Orb agent connector is a Python package that equips AI agents to interact with Orb through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-orb` v0.1.45
- **Auth:** Token
- **Docs:** [Official API docs](https://docs.withorb.com/api-reference)
- **Status:** complete

## Example Prompts

- Show me all my customers in Orb
- List all active subscriptions
- What plans are available?
- Show me recent invoices
- Show me details for a recent customer
- What is the status of a recent subscription?
- Show me the pricing details for a plan
- Confirm the Stripe ID linked to a customer
- What is the payment provider ID for a customer?
- List all invoices for a specific customer
- List all subscriptions for customer XYZ
- Show all active subscriptions for a specific customer
- What subscriptions does customer \{external_customer_id\} have?
- Pull all invoices from the last month
- Show invoices created after \{date\}
- List all paid invoices for customer \{customer_id\}
- What invoices are in draft status?
- Show all issued invoices for subscription \{subscription_id\}

## Unsupported

- Create a new customer in Orb
- Update subscription details
- Delete a customer record
- Send an invoice to a customer
- Filter subscriptions by plan name (must filter client-side after listing)
- Pull customers billed for specific products (must examine invoice line_items client-side)

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-orb
```

### OSS Mode

```python
from airbyte_agent_orb import OrbConnector
from airbyte_agent_orb.models import OrbAuthConfig

connector = OrbConnector(
    auth_config=OrbAuthConfig(
        api_key="<Your Orb API key>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@OrbConnector.tool_utils
async def orb_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_orb import OrbConnector, AirbyteAuthConfig

connector = OrbConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@OrbConnector.tool_utils
async def orb_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Customers | List, Get, Search |
| Subscriptions | List, Get, Search |
| Plans | List, Get, Search |
| Invoices | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/orb/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/orb/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/orb)*
