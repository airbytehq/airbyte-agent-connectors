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
        model="<model>",
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

## Single Connector — progressive docs (`agent_tool`)

`agent_tool` is the progressive-docs alternative to `tool_utils`: instead of one tool with the full ENTITIES/ACTIONS/PARAMETERS block baked in, register three tools and let Claude fetch docs on demand (inspect → outline → section → execute). Roles are inferred from each function's signature. Failures raise `AirbyteToolError` by default (`framework="none"`, no auto-detection).

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
@StripeConnector.agent_tool(inspect_tool="stripe_inspect", docs_tool="stripe_read_docs")
async def stripe_execute(entity: str, action: str, params: dict | None = None) -> str:
    result = await connector.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


@beta_async_tool
@StripeConnector.agent_tool()
async def stripe_inspect() -> str:
    return json.dumps(await connector.inspect_connector(), default=str)


@beta_async_tool
@StripeConnector.agent_tool()
async def stripe_read_docs(section: str | None = None) -> str:
    return await connector.read_skill_docs(section)


async def main():
    runner = client.beta.messages.tool_runner(
        model="<model>",
        max_tokens=4096,
        tools=[stripe_execute, stripe_inspect, stripe_read_docs],
        messages=[{"role": "user", "content": "List my recent customers"}],
    )
    try:
        async for message in runner:
            for block in message.content:
                if block.type == "text":
                    print(block.text)
    finally:
        await connector.close()


if __name__ == "__main__":
    asyncio.run(main())
```

A tool failure raises `AirbyteToolError`, which propagates out of the runner loop — catch it around the loop, or have the tool body catch it and return an error string if you want Claude to see the failure and retry. The `inspect_tool=`/`docs_tool=` kwargs on the execute decorator weave the exact registered sibling-tool names into the docstring Claude sees; omit them for generic phrasing (they are only valid on the execute tool). Ambiguous signatures, generic `(*args, **kwargs)` wrappers, or callables whose signature can't be read must pass the role explicitly: `agent_tool("execute")`.

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
        model="<model>",
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
