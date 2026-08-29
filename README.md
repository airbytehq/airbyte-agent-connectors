# Airbyte Agent SDK

Type-safe connector execution framework with blessed connectors and full IDE autocomplete.

## Overview

The Airbyte Agent SDK gives AI agents access to 50+ third-party APIs through strongly typed, well-documented tools. Connectors can run through the Airbyte platform (which manages credentials, rate limiting, and execution) or locally in OSS mode.

## How to install

```bash
uv pip install airbyte-agent-sdk
```

## Documentation

Full documentation is available at [docs.airbyte.com/ai-agents/about/](https://docs.airbyte.com/ai-agents/).

- [SDK guides](https://docs.airbyte.com/ai-agents/interfaces/sdk) — authentication, adding connectors, executing operations.
- [SDK API reference](https://docs.airbyte.com/ai-agents/reference/sdk) — generated from the SDK's docstrings.
- [pdoc site](https://airbytehq.github.io/sonar/airbyte_agent_sdk.html) — the same reference rendered by pdoc; requires access to the `airbytehq/sonar` repo.

## Tool integration

The SDK ships a hosted tool builder and two decorators for turning connector calls into LLM tools with retry-aware exception translation, output-size guards, and framework-specific error signalling.

- **`build_connector_tools(connector, framework="...")`** — preferred for hosted connector agents. Returns `inspect_connector`, `read_skill_docs`, and `execute` callables bound to one connector. Hosted connectors, or local connectors passed an explicit `docs_provider`, use outline-only guidance and tell the agent to inspect/read docs before execution; local/offline connectors without a docs provider keep generated YAML-derived rich docs. Pass `use_progressive_docs=False` to make `tools.as_list()` expose only `execute` with the legacy rich description.
- **`@<Connector>.agent_tool(...)`** — preferred when you write your own tool functions, especially on frameworks the SDK does not natively support. The progressive-docs sibling of `tool_utils`: decorate three functions (execute, inspect, docs) and the execute docstring steers the agent through the inspect → docs → execute flow instead of embedding the full entity/action reference. Tool failures raise `AirbyteToolError` by default (`framework="none"`, no auto-detection); pass `framework="..."` to target a supported framework's signal.
- **`@<Connector>.tool_utils`** — preferred for typed connectors on supported frameworks. Auto-detects the installed framework (pydantic-ai, LangChain, OpenAI Agents, or FastMCP; falls back to `framework="none"` with a warning when none is installed) and composes [`translate_exceptions`](https://airbytehq.github.io/sonar/airbyte_agent_sdk/translation.html) under the hood. Pass `framework="..."` to override auto-detection. Forwards `update_docstring`, `max_output_chars`, `framework`, `internal_retries`, `should_internal_retry`, and `exhausted_runtime_failure_message`.
- **`@translate_exceptions`** — same translation behaviour for any callable that is not a generated `Connector` (custom helpers, eval harnesses, ad-hoc tools).

The builder and decorators preserve async callables, `__name__`, and `__doc__`. Transient runtime failures (429/5xx, network, timeout) can be retried silently via `internal_retries=N`. Output exceeding `max_output_chars` (default 100 KB) is converted to the framework's retry signal so the LLM can narrow the query.

> **Pick one decorator per tool.** Stacking `@translate_exceptions` over `@<Connector>.tool_utils` (or vice versa) is detected at decoration time: the inner layer is preserved and the outer layer logs a warning and short-circuits, so double-translation is impossible.

### Hosted connector tools

```python
from pydantic_ai import Agent
from airbyte_agent_sdk import build_connector_tools
from airbyte_agent_sdk.connectors.stripe import StripeConnector
from airbyte_agent_sdk.types import AirbyteAuthConfig

stripe = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id="client_abc123",
        airbyte_client_secret="secret_xyz789",
        connector_id="src_123",
    )
)
tools = build_connector_tools(stripe, framework="pydantic_ai")

agent = Agent("openai:gpt-4o", tools=tools.as_list())
```

The model-facing docs flow is `inspect_connector()` -> `read_skill_docs()` -> `read_skill_docs(section="...")` -> `execute(...)`. The docs tool binds the hosted `docs_skill_id` internally, so the model only passes an optional `section`.

To opt out of the progressive inspect/docs flow:

```python
tools = build_connector_tools(stripe, framework="pydantic_ai", use_progressive_docs=False)
agent = Agent("openai:gpt-4o", tools=tools.as_list())  # exposes execute only
```

### Unsupported frameworks — `agent_tool`

For frameworks without a native strategy (or any harness that consumes plain
callables), write the three tool functions yourself and decorate each with
`agent_tool`. The role is inferred from the signature — `(entity, action, ...)`
is execute, `(section, ...)` is docs, `()` is inspect — or pass it explicitly
(`agent_tool("execute")`). Extra parameters are allowed.

```python
from airbyte_agent_sdk import AirbyteToolError
from airbyte_agent_sdk.connectors.stripe import StripeConnector
from airbyte_agent_sdk.types import AirbyteAuthConfig

stripe = StripeConnector(auth_config=AirbyteAuthConfig(...))

@StripeConnector.agent_tool(inspect_tool="stripe_inspect", docs_tool="stripe_read_docs")
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    result = await stripe.execute(entity, action, params or {})
    return result.data if hasattr(result, "data") else result

@StripeConnector.agent_tool()
async def stripe_inspect():
    return await stripe.inspect_connector()

@StripeConnector.agent_tool()
async def stripe_read_docs(section: str | None = None):
    return await stripe.read_skill_docs(section)

# Register the three callables with your framework of choice. Failures raise
# AirbyteToolError — catch it in your tool-dispatch loop and feed the message
# back to the model.
```

The optional `inspect_tool=`/`docs_tool=` kwargs weave the exact registered
sibling-tool names into the execute docstring for tighter steering; omitting
them uses generic phrasing. On a supported framework, pass `framework="..."`
to raise that framework's retry signal instead of `AirbyteToolError`.

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

See the [`translate_exceptions`](https://airbytehq.github.io/sonar/airbyte_agent_sdk/translation.html) reference for advanced kwargs (`internal_retries`, `should_internal_retry`, `exhausted_runtime_failure_message`).

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
