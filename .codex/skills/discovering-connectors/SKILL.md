---
name: discovering-connectors
description: Discovers available Airbyte connectors, explores their entities/actions/schemas, and checks auth requirements. Use when asking what connectors exist, what a connector can do, or what fields/entities are available.
---

# Discovering Connectors

## Programmatic Discovery

```python
from airbyte_agent_sdk import list_connectors

available = list_connectors()
# Returns sorted list of connector slugs: ["airtable", "asana", "github", ...]
```

## Exploring a Connector's Capabilities

Each connector has documentation at:
`https://github.com/airbytehq/airbyte-agent-sdk/tree/main/connectors/{name}`

| File | What it tells you |
|------|-------------------|
| `README.md` | Entities/actions table, install instructions, example questions |
| `AUTH.md` | Credential requirements (OAuth, API key, etc.), hosted setup |
| `REFERENCE.md` | Full entity/action parameters and schemas |

Read the connector's README first to understand what it can do.

## Runtime Introspection

When a typed connector package is installed, use runtime methods for schema details:

```python
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.stripe import StripeConnector

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
        airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
        workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
    )
)

# List all entities and their available actions
entities = connector.list_entities()
for entity in entities:
    print(f"{entity['entity_name']}: {entity['available_actions']}")

# Get JSON schema for a specific entity
schema = connector.entity_schema("customers")
```

**Note**: `list_entities()` and `entity_schema()` require a typed connector (available after `uv pip install airbyte-agent-sdk`). They are not available on the generic `HostedExecutor`.

## Auth Requirements

Read the connector's `AUTH.md` to understand what credentials are needed. For hosted mode (the default), API credentials are stored in Airbyte Cloud — you provide Airbyte client credentials instead.

## References

- [SDK API reference](../airbyte-sdk-reference/sdk-api.md)
- [Connector discovery details](../airbyte-sdk-reference/connector-discovery.md)
