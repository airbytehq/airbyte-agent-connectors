---
name: building-multi-connector-agent
description: Builds a complete agent with multiple Airbyte connectors using PydanticAI or Claude SDK. Scaffolds project structure, wires up connectors, composes tools, and creates a run loop. Use when building an agent with multiple connectors or scaffolding a new agent project.
---

# Building a Multi-Connector Agent

Use this when an agent needs two or more Airbyte connectors.

## Going from Single to Multi

The `bootstrapping-agent` skill shows the single-connector pattern: direct class construction with `AirbyteAuthConfig` + `@Connector.tool_utils` decorator. Multi-connector agents use the **same pattern**, just repeated:

1. Build a single `AirbyteAuthConfig(...)` so credentials are shared across connectors.
2. Construct one typed connector per service (e.g. `JiraConnector(auth_config=auth)`).
3. Define one tool function per connector, each with its own `@Connector.tool_utils` decorator.

There are no new APIs — same install, same constructor, same classmethod decorator.

## Install the SDK

```bash
uv pip install airbyte-agent-sdk
```

The single `airbyte-agent-sdk` package bundles every typed connector, so `tool_utils`, `list_entities()`, and `entity_schema()` are available on each one without per-connector installs.

## Core Pattern (PydanticAI)

```python
import os
from pydantic_ai import Agent
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.jira import JiraConnector
from airbyte_agent_sdk.connectors.slack import SlackConnector

# Shared credentials — all connectors reuse the same AirbyteAuthConfig
auth = AirbyteAuthConfig(
    airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
    airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
    workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
)

jira = JiraConnector(auth_config=auth)
slack = SlackConnector(auth_config=auth)
```

If the workspace contains multiple connectors of the same type, pin one by passing `connector_id=os.getenv("JIRA_CONNECTOR_ID")` to the constructor.

## One Tool Per Connector

Each connector gets its own tool function — don't combine them into a mega-tool. Separate tools give the LLM clear, independent tool descriptions.

`tool_utils` is a `@classmethod` — decorate with `@JiraConnector.tool_utils`, not `@jira.tool_utils`.

```python
agent = Agent(
    "openai:gpt-4o",
    system_prompt="You monitor Jira issues and post summaries to Slack.",
)

@agent.tool_plain
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None):
    return await jira.execute(entity, action, params or {})

@agent.tool_plain
@SlackConnector.tool_utils
async def slack_execute(entity: str, action: str, params: dict | None = None):
    return await slack.execute(entity, action, params or {})
```

## System Prompt

Describe the agent's purpose and what each connector does:

```python
agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You are a customer support assistant. "
        "Use the stripe tool to look up customer billing data. "
        "Use the jira tool to create and track support tickets. "
        "Use the slack tool to notify the support team."
    ),
)
```

## Run Loop

### PydanticAI

```python
import asyncio

async def main():
    result = await agent.run("Find open P0 bugs and post a summary to #engineering")
    print(result.output)
    await jira.close()
    await slack.close()

asyncio.run(main())
```

### Claude SDK (Anthropic Python)

See [Claude SDK patterns](../airbyte-sdk-reference/claude-sdk.md) for the full message loop with tool handling.

## Project Structure

For a new agent project:

```
my-agent/
├── pyproject.toml       # dependencies: airbyte-agent-sdk, pydantic-ai or anthropic
├── .env                 # AIRBYTE_CLIENT_ID, AIRBYTE_CLIENT_SECRET, AIRBYTE_WORKSPACE_NAME
├── agent.py             # Entry point: auth config, connectors, agent + tools, run loop
└── README.md
```

### pyproject.toml

```toml
[project]
name = "my-agent"
requires-python = ">=3.11"
dependencies = [
    "airbyte-agent-sdk",
    "pydantic-ai",
    "python-dotenv",
]
```

## Environment Variables

```
AIRBYTE_CLIENT_ID=your_client_id
AIRBYTE_CLIENT_SECRET=your_client_secret
AIRBYTE_WORKSPACE_NAME=your_workspace_name
```

## References

- [SDK API reference](../airbyte-sdk-reference/sdk-api.md) — `AirbyteAuthConfig`, typed connector constructors, `tool_utils`
- [PydanticAI patterns](../airbyte-sdk-reference/pydantic-ai.md) — multi-connector example
- [Claude SDK patterns](../airbyte-sdk-reference/claude-sdk.md) — multi-connector example
- [Connector discovery](../airbyte-sdk-reference/connector-discovery.md) — finding available connectors
