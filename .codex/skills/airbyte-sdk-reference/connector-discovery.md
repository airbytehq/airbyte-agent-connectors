# Connector Discovery

## Programmatic Discovery

```python
from airbyte_agent_sdk import list_connectors

available = list_connectors()  # sorted list of connector slugs
# e.g. ["airtable", "asana", "github", "hubspot", "jira", "salesforce", "stripe", ...]
```

## Per-Connector Documentation

Each connector has documentation at:

```
https://github.com/airbytehq/airbyte-agent-sdk/tree/main/connectors/{connector_name}
```

### Documentation Structure

| File | Contains | When to Read |
|------|----------|--------------|
| `README.md` | Quickstart, entities/actions table, install instructions, usage examples | First — overview of capabilities |
| `AUTH.md` | Credential requirements (OAuth, API key, token), hosted setup via API | When setting up authentication |
| `REFERENCE.md` | Full entity/action details, parameters, schemas | When you need parameter details |

### Reading the Entities/Actions Table

Each connector's README.md contains a table like:

```markdown
| Entity | Actions | Description |
|--------|---------|-------------|
| customers | list, get, create, update | Manage customer records |
| invoices | list, get | Retrieve invoice data |
```

This shows what the connector can do at a glance.

## Runtime Introspection

For typed connectors (available after `uv pip install airbyte-agent-sdk`), use runtime methods:

```python
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.stripe import StripeConnector

connector = StripeConnector(auth_config=AirbyteAuthConfig(...))

# List all entities and their actions
entities = connector.list_entities()
for entity in entities:
    print(f"{entity['entity_name']}: {entity['available_actions']}")

# Get JSON schema for a specific entity
schema = connector.entity_schema("customers")
print(list(schema.get("properties", {}).keys()))
```

**Note**: `list_entities()` and `entity_schema()` are only available on typed connectors, not on `HostedExecutor`.

## Example Questions

Connector specs include `x-airbyte-example-questions` with three categories:

- **direct**: Questions answerable with a single API call (e.g. "List my Stripe customers")
- **search**: Questions requiring filtering or context-store search (e.g. "Find customers named John")
- **unsupported**: Questions the connector can't answer (e.g. "What's my Stripe MRR forecast?")

These appear in connector READMEs under "Example questions" and "Unsupported questions" sections.

## Auth Requirements

Each connector's `AUTH.md` documents:
- What credential type is needed (OAuth, API key, bearer token)
- Required credential fields and their descriptions
- Hosted mode setup — how to create a connector via the Airbyte API
- OAuth flow — consent URL initiation and callback handling (for connectors with OAuth)

For hosted mode, API credentials are stored in Airbyte Cloud. You provide Airbyte client credentials (`airbyte_client_id`, `airbyte_client_secret`) instead of direct API keys.
