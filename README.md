# Airbyte Agent SDK

Type-safe connector execution framework with blessed connectors and full IDE autocomplete.

## Overview

The Airbyte Agent SDK gives AI agents access to 50+ third-party APIs through strongly typed, well-documented tools. Connectors can run through the Airbyte platform (which manages credentials, rate limiting, and execution) or locally in OSS mode.

## How to install

```bash
uv pip install airbyte-agent-sdk
```

## CLI Quickstart

The `airbyte-agent-sdk` console script ships seven subcommands:

```bash
uv run airbyte-agent-sdk --help
```

```bash
uv run airbyte-agent-sdk annotate --help
```

```bash
uv run airbyte-agent-sdk cassette --help
```

```bash
uv run airbyte-agent-sdk connector --help
```

```bash
uv run airbyte-agent-sdk generate-docs --help
```

```bash
uv run airbyte-agent-sdk generate-sdk --help
```

```bash
uv run airbyte-agent-sdk test --help
```

```bash
uv run airbyte-agent-sdk validate --help
```

## Documentation

Full documentation is available at [docs.airbyte.com/ai-agents/about/](https://docs.airbyte.com/ai-agents/about/).

## Tool integration

The SDK ships two decorators for turning a connector call into an LLM tool with retry-aware exception translation, output-size guards, and framework-specific error signalling.

- **`@<Connector>.tool_utils`** — preferred for typed connectors. Auto-detects the installed framework (pydantic-ai, LangChain, OpenAI Agents, or FastMCP) and composes [`translate_exceptions`](https://airbytehq.github.io/airbyte-embedded/airbyte_agent_sdk/translation.html) under the hood. Pass `framework="..."` to override auto-detection. Forwards `update_docstring`, `max_output_chars`, `framework`, `internal_retries`, `should_internal_retry`, and `exhausted_runtime_failure_message`.
- **`@translate_exceptions`** — same translation behaviour for any callable that is not a generated `Connector` (custom helpers, eval harnesses, ad-hoc tools).

Both decorators preserve sync/async, `__name__`, and `__doc__`. Transient runtime failures (429/5xx, network, timeout) can be retried silently via `internal_retries=N` on **either** decorator. Output exceeding `max_output_chars` (default 100 KB) is converted to the framework's retry signal so the LLM can narrow the query.

> **Pick one decorator per tool.** Stacking `@translate_exceptions` over `@<Connector>.tool_utils` (or vice versa) is detected at decoration time: the inner layer is preserved and the outer layer logs a warning and short-circuits, so double-translation is impossible.

### pydantic-ai

```python
from pydantic_ai import Agent
from airbyte_agent_sdk.connectors.stripe import StripeConnector

agent = Agent("openai:gpt-4o")

@agent.tool_plain
@StripeConnector.tool_utils
async def list_customers(limit: int = 10) -> list[dict]:
    async with StripeConnector(connector_id="src_123") as stripe:
        result = await stripe.execute("customers", "list", params={"limit": limit})
        return result.data
```

Failures raise `pydantic_ai.ModelRetry` so the agent can retry with corrected arguments.

### LangChain

```python
from langchain_core.tools import StructuredTool
from airbyte_agent_sdk.connectors.stripe import StripeConnector

@StripeConnector.tool_utils(framework="langchain")
async def list_customers(limit: int = 10) -> list[dict]:
    async with StripeConnector(connector_id="src_123") as stripe:
        result = await stripe.execute("customers", "list", params={"limit": limit})
        return result.data

tool = StructuredTool.from_function(
    coroutine=list_customers,
    name="list_customers",
    description="List Stripe customers.",
    handle_tool_error=True,  # surfaces ToolException as the tool's string result
)
```

Failures raise `langchain_core.tools.ToolException`; `handle_tool_error=True` turns that into the tool's string result for the LLM.

> Alternative for non-typed callables: replace `@StripeConnector.tool_utils(framework="langchain")` with `@translate_exceptions(framework="langchain")` from `airbyte_agent_sdk`.

### OpenAI Agents

```python
from agents import Agent, function_tool
from airbyte_agent_sdk.connectors.stripe import StripeConnector

@function_tool
@StripeConnector.tool_utils(framework="openai_agents")
async def list_customers(limit: int = 10) -> list[dict]:
    async with StripeConnector(connector_id="src_123") as stripe:
        result = await stripe.execute("customers", "list", params={"limit": limit})
        return result.data

agent = Agent(name="stripe", tools=[list_customers])
```

Note: the OpenAI Agents strategy uses **catch-and-return-string semantics** — `tool_utils` catches the failure and *returns* a string (e.g. `"ConnectorValidationError: entity must be one of: ..."`) instead of raising. The OpenAI runner serialises this string verbatim into the tool result the LLM sees.

> Alternative for non-typed callables: replace `@StripeConnector.tool_utils(framework="openai_agents")` with `@translate_exceptions(framework="openai_agents")` from `airbyte_agent_sdk`.

### FastMCP

```python
from fastmcp import FastMCP
from airbyte_agent_sdk.connectors.stripe import StripeConnector

mcp = FastMCP("stripe-tools")

@mcp.tool()
@StripeConnector.tool_utils(framework="mcp")
async def list_customers(limit: int = 10) -> list[dict]:
    async with StripeConnector(connector_id="src_123") as stripe:
        result = await stripe.execute("customers", "list", params={"limit": limit})
        return result.data
```

Failures raise `fastmcp.exceptions.ToolError`, which FastMCP serialises as an MCP error response to the client.

See the [`translate_exceptions`](https://airbytehq.github.io/airbyte-embedded/airbyte_agent_sdk/translation.html) reference for advanced kwargs (`internal_retries`, `should_internal_retry`, `exhausted_runtime_failure_message`).

## How to install the skills

The repo ships skills that walk agents through setting up and using the connectors. Three install paths:

**skills.sh** (works for Claude Code, Codex, Cursor, OpenCode, and 40+ other agents):

```bash
npx skills add airbytehq/airbyte-agent-sdk
```

**Claude Code** (native plugin):

```
/plugin marketplace add airbytehq/airbyte-agent-sdk
/plugin install airbyte-agent-sdk@airbyte-agent-sdk
```

**Codex** (clone + symlink):

```bash
git clone https://github.com/airbytehq/airbyte-agent-sdk ~/.codex/skills/airbyte-agent-sdk-src
ln -s ~/.codex/skills/airbyte-agent-sdk-src/connector-sdk/.claude/skills/* ~/.codex/skills/
```

See [docs.airbyte.com/ai-agents/about/](https://docs.airbyte.com/ai-agents/about/) for full documentation.
