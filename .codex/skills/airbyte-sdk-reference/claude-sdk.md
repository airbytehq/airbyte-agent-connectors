# Claude SDK (Anthropic Python) Wiring Patterns

## Single Connector

Use `@beta_async_tool` with `tool_runner` on the async client. Stack `@StripeConnector.tool_utils` underneath the framework decorator so the ENTITIES/ACTIONS/PARAMETERS block is appended to the tool description Claude sees.

```python
import asyncio
import json
import os
from anthropic import AsyncAnthropic, beta_async_tool
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.stripe import StripeConnector

client = AsyncAnthropic()

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
        airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
        workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
    )
)


@beta_async_tool
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Stripe API operation.

    Args:
        entity: Entity name (e.g. "customers", "invoices", "balance")
        action: Action to perform (e.g. "list", "get", "create")
        params: Optional parameters for the operation

    Returns:
        JSON string with the operation result
    """
    result = await connector.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


async def main():
    runner = client.beta.messages.tool_runner(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        tools=[stripe_execute],
        messages=[{"role": "user", "content": "List my recent customers"}],
    )
    async for message in runner:
        for block in message.content:
            if block.type == "text":
                print(block.text)

    await connector.close()


if __name__ == "__main__":
    asyncio.run(main())
```

**Note**: The framework decorator (`@beta_async_tool`) goes on top; `@StripeConnector.tool_utils` goes underneath. `@beta_async_tool` introspects the function's `__doc__` to build the tool description Claude sees, and `tool_utils` has already appended the ENTITIES/ACTIONS/PARAMETERS block to `__doc__`, so the enriched description is passed through automatically.

## Multi-Connector

Mirror the single-connector pattern for each connector: one `@beta_async_tool` + `@Connector.tool_utils` async function per connector, sharing a single `AirbyteAuthConfig` and an `AsyncAnthropic` client with `tool_runner`.

```python
import asyncio
import json
import os
from anthropic import AsyncAnthropic, beta_async_tool
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.jira import JiraConnector
from airbyte_agent_sdk.connectors.slack import SlackConnector

client = AsyncAnthropic()

auth = AirbyteAuthConfig(
    airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
    airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
    workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
)

jira = JiraConnector(auth_config=auth)
slack = SlackConnector(auth_config=auth)


@beta_async_tool
@JiraConnector.tool_utils
async def jira_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Jira operation (issues, projects, comments, etc.).

    Args:
        entity: Entity name (e.g. "issues", "projects")
        action: Action to perform (e.g. "list", "get", "create")
        params: Optional parameters for the operation

    Returns:
        JSON string with the operation result
    """
    result = await jira.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


@beta_async_tool
@SlackConnector.tool_utils
async def slack_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Slack operation (channels, messages, users, etc.).

    Args:
        entity: Entity name (e.g. "channels", "messages")
        action: Action to perform (e.g. "list", "get", "create")
        params: Optional parameters for the operation

    Returns:
        JSON string with the operation result
    """
    result = await slack.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


async def main():
    runner = client.beta.messages.tool_runner(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        tools=[jira_execute, slack_execute],
        messages=[{"role": "user", "content": "Find open bugs in Jira and post a summary to #engineering"}],
    )
    async for message in runner:
        for block in message.content:
            if block.type == "text":
                print(block.text)

    await jira.close()
    await slack.close()


if __name__ == "__main__":
    asyncio.run(main())
```
