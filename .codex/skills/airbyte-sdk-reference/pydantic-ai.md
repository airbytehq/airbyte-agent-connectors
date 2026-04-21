# PydanticAI Wiring Patterns

## Single Connector

```python
import asyncio
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
    "openai:gpt-4o",
    system_prompt="You are a helpful assistant with access to Stripe data.",
)


@agent.tool_plain
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    """Execute a Stripe operation."""
    return await connector.execute(entity, action, params or {})


async def main():
    result = await agent.run("List my recent customers")
    print(result.output)
    await connector.close()


if __name__ == "__main__":
    asyncio.run(main())
```

### Decorator Stacking Order

The framework decorator goes on top, `tool_utils` goes underneath:

```python
@agent.tool_plain      # PydanticAI registers this as a tool
@StripeConnector.tool_utils  # Appends connector capabilities to docstring + output guard
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

`tool_utils` enriches the docstring BEFORE PydanticAI reads it for tool registration.

## Multi-Connector

Same pattern as single-connector, repeated. Extract `AirbyteAuthConfig(...)` into a shared `auth` variable and construct one typed connector per service.

```python
import asyncio
import os
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.jira import JiraConnector
from airbyte_agent_sdk.connectors.slack import SlackConnector
from pydantic_ai import Agent

auth = AirbyteAuthConfig(
    airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
    airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
    workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
)

jira = JiraConnector(auth_config=auth)
slack = SlackConnector(auth_config=auth)

agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You are a project assistant. You can read Jira issues and post to Slack channels. "
        "Use the jira tool to query project data and the slack tool to send messages."
    ),
)


@agent.tool_plain
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None):
    """Execute a Jira operation."""
    return await jira.execute(entity, action, params or {})


@agent.tool_plain
@SlackConnector.tool_utils
async def slack_execute(entity: str, action: str, params: dict | None = None):
    """Execute a Slack operation."""
    return await slack.execute(entity, action, params or {})


async def main():
    result = await agent.run("Find open bugs in Jira and post a summary to #engineering")
    print(result.output)
    await jira.close()
    await slack.close()


if __name__ == "__main__":
    asyncio.run(main())
```

### Key Points

- `AirbyteAuthConfig` is exported at the `airbyte_agent_sdk` package root — import it once and share across connectors
- Each connector gets its own tool function with its own `tool_utils` decorator
- One tool per connector gives the LLM clear, separate tool descriptions
- Per-connector overrides (e.g. `connector_id=` when multiple of the same type exist in the workspace) go on the typed constructor

## System Prompt Patterns

Describe what the agent can do in terms of the connectors:

```python
agent = Agent(
    "openai:gpt-4o",
    system_prompt=(
        "You are a customer support assistant. "
        "You can look up customer details in Stripe and create tickets in Jira. "
        "Always verify customer identity before sharing billing information."
    ),
)
```

## Verifying Setup

After creating a connector, verify credentials work:

```python
check = await connector.check()
if check.status == "healthy":
    print(f"Connected — checked {check.checked_entity}/{check.checked_action}")
else:
    print(f"Connection failed: {check.error}")
```
