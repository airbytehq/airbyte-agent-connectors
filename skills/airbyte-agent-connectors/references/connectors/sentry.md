<!-- AUTO-GENERATED from connectors/sentry/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Sentry

The Sentry agent connector is a Python package that equips AI agents to interact with Sentry through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-sentry` v0.1.0
- **Auth:** Token
- **Docs:** [Official API docs](https://docs.sentry.io/api/)
- **Status:** complete

## Example Prompts

- List all projects in my Sentry organization
- Show me the issues for a specific project
- List recent events from a project
- Show me all releases for my organization
- Get the details of a specific project
- What are the most common unresolved issues?
- Which projects have the most events?
- Show me issues that were first seen this week
- Find releases created in the last month

## Unsupported

- Create a new project in Sentry
- Delete an issue
- Update a release
- Resolve all issues in a project

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-sentry
```

### OSS Mode

```python
from airbyte_agent_sentry import SentryConnector
from airbyte_agent_sentry.models import SentryAuthConfig

connector = SentryConnector(
    auth_config=SentryAuthConfig(
        auth_token="<Sentry authentication token. Log into Sentry and create one at Settings > Account > API > Auth Tokens.>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SentryConnector.tool_utils
async def sentry_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_sentry import SentryConnector, AirbyteAuthConfig

connector = SentryConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@SentryConnector.tool_utils
async def sentry_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Projects | List, Get, Search |
| Issues | List, Get, Search |
| Events | List, Get, Search |
| Releases | List, Get, Search |
| Project Detail | Get |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/sentry/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/sentry/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/sentry)*
