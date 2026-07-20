---
name: bootstrapping-agent
description: Wires up an Airbyte connector for use in a PydanticAI or Claude SDK agent, or any other framework via agent_tool. Generates auth config, connector initialization, and tool_utils- or agent_tool-decorated tool functions. Use when adding a connector to an agent or setting up a new agent with a connector.
---

# Bootstrapping an Agent with an Airbyte Connector

## Install the SDK

```bash
uv pip install airbyte-agent-sdk
```

The single `airbyte-agent-sdk` package ships every typed connector. Import them from `airbyte_agent_sdk.connectors.{slug}`. `tool_utils`, `list_entities()`, and `entity_schema()` are only available on typed connectors.

## Core Pattern (PydanticAI)

```python
import os
from pydantic_ai import Agent
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.stripe import StripeConnector

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
        airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
        workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
    )
)

agent = Agent(
    "<provider:model>",
    system_prompt=(
        "You are a helpful assistant with access to Stripe. "
        "Use the stripe_execute tool to look up customer, invoice, and balance data. "
        "Ask for clarification if a request is ambiguous."
    ),
)

@agent.tool_plain
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

**Always hosted mode**: Use `AirbyteAuthConfig` with `airbyte_client_id` and `airbyte_client_secret`. Never generate local auth code.

## Decorator Stacking

The framework decorator goes on top, `tool_utils` goes underneath:

```python
@agent.tool_plain           # Framework registers this as a tool
@StripeConnector.tool_utils # Enriches docstring with connector capabilities
async def stripe_execute(...):
```

`tool_utils` is a `@classmethod` — use `StripeConnector.tool_utils`, not `connector.tool_utils`.

### Automatic Retry Translation

`tool_utils` automatically translates retryable errors to the framework's retry signal (`ModelRetry` for pydantic-ai). The example above continues to work unchanged — translation happens inside `tool_utils` with no extra decorator needed.

Reference demo: `connector-sdk/examples/demo_agent.py` (mocked, no credentials needed: `--mock`).

## Unsupported Frameworks (agent_tool)

For frameworks without a native `tool_utils` strategy (anything other than pydantic-ai, LangChain, OpenAI Agents, FastMCP), use `agent_tool` — the progressive-docs sibling of `tool_utils`. Decorate **three** functions; the role is inferred from each signature (`(entity, action, ...)` → execute, `(section, ...)` → docs, `()` → inspect; extra params allowed, ambiguous signatures must pass the role explicitly, e.g. `agent_tool("execute")`):

```python
@StripeConnector.agent_tool(inspect_tool="stripe_inspect", docs_tool="stripe_read_docs")
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})

@StripeConnector.agent_tool()
async def stripe_inspect():
    return await connector.inspect_connector()

@StripeConnector.agent_tool()
async def stripe_read_docs(section: str | None = None):
    return await connector.read_skill_docs(section)
```

Register all three with the target framework. The execute docstring steers the model through inspect → docs outline → docs section → execute instead of embedding the full entity/action reference. Failures raise `AirbyteToolError` (`from airbyte_agent_sdk import AirbyteToolError`) by default — no framework auto-detection; pass `framework="..."` to target a supported framework's retry signal instead. The optional `inspect_tool=`/`docs_tool=` kwargs put the exact registered sibling-tool names into the execute docstring; omit them for generic phrasing.

## Verify the Setup

```python
check = await connector.check()
if check.status == "healthy":
    print(f"Connected — checked {check.checked_entity}/{check.checked_action}")
else:
    print(f"Failed: {check.error}")
```

## Framework Detection

Detect the developer's framework from their existing imports:
- `from pydantic_ai import Agent` → Use PydanticAI patterns
- `from anthropic import Anthropic` → Use Claude SDK patterns
- If unclear, ask which framework they're using

## Connector Naming Convention

All connectors ship in `airbyte-agent-sdk`. Import each one from `airbyte_agent_sdk.connectors.{slug}`:

| Connector | Import | Class |
|-----------|--------|-------|
| stripe | `airbyte_agent_sdk.connectors.stripe` | `StripeConnector` |
| zendesk-support | `airbyte_agent_sdk.connectors.zendesk_support` | `ZendeskSupportConnector` |
| hubspot | `airbyte_agent_sdk.connectors.hubspot` | `HubspotConnector` |

Hyphens in connector slugs become underscores in the submodule path.

## Environment Variables

The developer needs these in their `.env`:

```
AIRBYTE_CLIENT_ID=your_client_id
AIRBYTE_CLIENT_SECRET=your_client_secret
AIRBYTE_WORKSPACE_NAME=your_workspace_name
```

## References

- [SDK API reference](../airbyte-sdk-reference/sdk-api.md) — full API signatures and options
- [PydanticAI patterns](../airbyte-sdk-reference/pydantic-ai.md) — complete runnable examples
- [Claude SDK patterns](../airbyte-sdk-reference/claude-sdk.md) — Anthropic Python SDK examples
