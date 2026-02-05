"""Shared agent setup for pydantic-ai with FastMCP toolset."""

from __future__ import annotations

import json
from collections.abc import AsyncGenerator
from typing import Any, Protocol, runtime_checkable

from pydantic_ai import (
    Agent,
    AgentRunResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    TextPartDelta,
    UnexpectedModelBehavior,
)
from pydantic_ai.messages import ModelMessage, RetryPromptPart, TextPart
from pydantic_ai.toolsets.fastmcp import FastMCPToolset

from .mcp_server import mcp


def entity_name(entity: dict[str, Any]) -> str:
    """Extract the display name from an entity dict."""
    return entity.get("entity_name") or entity.get("entity") or entity.get("name", "unknown")


def tool_title(name: str, tool_input: dict[str, Any]) -> str:
    """Build a human-readable title for a tool call."""
    if name == "execute" and "entity" in tool_input:
        entity = tool_input["entity"]
        action = tool_input.get("action", "")
        detail = f"{entity}, {action}" if action else entity
        return f"Execute ({detail})"
    return name.replace("_", " ").replace("-", " ").title()


def build_system_prompt(connector: Any) -> str:
    """Build a system prompt that includes connector metadata."""
    lines = []
    for ent in connector.list_entities():
        actions = ent.get("available_actions") or ent.get("actions", [])
        action_names = [a.get("name", str(a)) if isinstance(a, dict) else str(a) for a in actions]
        lines.append(f"  - {entity_name(ent)}: {', '.join(action_names)}")

    return (
        f"You are a helpful data assistant connected to the {connector.connector_name} connector "
        f"(v{connector.connector_version}).\n\n"
        f"Available entities and their actions:\n" + "\n".join(lines) + "\n\n"
        "Use the provided tools to fetch data and answer the user's questions. "
        "When presenting data, format it clearly. "
        "If a query returns many results, summarize the key information. "
        "Always use the tools to get real data rather than making up answers.\n\n"
        "CRITICAL RULES — follow these on every query:\n\n"
        "1. QUERY PLANNING: For any time-based question, call `current_datetime` FIRST. "
        "Date mappings: 'recent'/'last week' = 7 days, 'this week' = since Monday, "
        "'this month' = since the 1st, 'today' = since midnight UTC.\n\n"
        "2. CROSS-ENTITY RESOLUTION: When a question mentions an entity by name, resolve it to an ID "
        "before querying. Use `entity_schema` to find fields ending in `Id`/`_id`, search the related "
        "entity by name, then re-query with the ID as a filter. NEVER paginate through large result "
        "sets to find matches — resolve the ID and filter instead.\n\n"
        "3. ACTION SELECTION: Always use `search` as your default action, not `list`. "
        "Only use `list` when you need today's data (search index may lag) or search returned no results.\n\n"
        "4. FIELD SELECTION: You MUST use `select_fields` or `exclude_fields` on every `execute` call. "
        "Fewer fields = faster and cheaper.\n\n"
        "5. PAGINATION: Use limit of 20-25. Do NOT paginate by default — the first page usually suffices. "
        "For 'how many' questions, say 'at least N' rather than exhaustively paginating. "
        "Never fetch more than 3 pages without checking if you have enough data.\n\n"
        "For the full reference (filter syntax, date range handling, downloads), "
        "call the `get_instructions` tool."
    )


def create_agent(connector: Any, model: str = "claude-opus-4-20250514") -> Agent:
    """Create a pydantic-ai Agent wired to the MCP server's tools.

    Args:
        connector: Instantiated connector object (used for system prompt).
        model: Model identifier (e.g. "claude-opus-4-20250514").

    Returns:
        A configured pydantic-ai Agent.
    """
    return Agent(
        f"anthropic:{model}",
        instructions=build_system_prompt(connector),
        toolsets=[FastMCPToolset(mcp)],
    )


def _parse_args(raw: Any) -> dict[str, Any]:
    """Normalise tool-call args to a dict.

    pydantic-ai may provide args as a dict *or* a JSON string depending on
    the model provider.
    """
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                return parsed
        except (json.JSONDecodeError, TypeError):
            pass
    return {}


@runtime_checkable
class StreamConsumer(Protocol):
    """Callback interface for consuming agent stream events.

    All methods have default no-op implementations so subclasses only need to
    override the callbacks they care about.
    """

    async def on_tool_call_start(self, tool_name: str, args: dict[str, Any], tool_call_id: str) -> None:
        """Called when the agent invokes a tool."""

    async def on_tool_call_end(self, tool_name: str, args: dict[str, Any], result: str, tool_call_id: str, *, is_error: bool) -> None:
        """Called when a tool call completes (successfully or with an error)."""

    async def on_intermediate_response(self, text: str) -> None:
        """Called when the agent emits text between tool calls."""

    async def on_final_response(self, text: str) -> None:
        """Called once with the final text response after the last agent step."""

    async def on_error(self, error: str) -> None:
        """Called when the agent run fails with an unrecoverable error."""


class AgentRunner:
    """Runs a pydantic-ai Agent and dispatches stream events to a StreamConsumer.

    Manages conversation history internally so callers don't need to track it.
    """

    def __init__(self, agent: Agent) -> None:
        self._agent = agent
        self._message_history: list[ModelMessage] = []

    async def run(self, prompt: str, consumer: StreamConsumer) -> AsyncGenerator[None]:
        """Run the agent with *prompt* and dispatch events to *consumer*.

        This is an async generator that yields after each consumer callback,
        allowing callers to react (e.g. re-render UI) after every event.
        """
        text_buffer = ""
        pending_args: dict[str, dict[str, Any]] = {}

        try:
            async for event in self._agent.run_stream_events(prompt, message_history=self._message_history):
                if isinstance(event, FunctionToolCallEvent):
                    if text_buffer:
                        await consumer.on_intermediate_response(text_buffer)
                        yield
                        text_buffer = ""

                    args = _parse_args(event.part.args)
                    pending_args[event.tool_call_id] = args
                    await consumer.on_tool_call_start(event.part.tool_name, args, event.tool_call_id)
                    yield

                elif isinstance(event, FunctionToolResultEvent):
                    is_error = isinstance(event.result, RetryPromptPart)
                    if is_error:
                        result_str = str(event.result.content) if event.result.content else "unknown error"
                    else:
                        content = event.result.content
                        result_str = content if isinstance(content, str) else json.dumps(content, default=str)

                    args = pending_args.pop(event.tool_call_id, {})
                    tool_name = event.result.tool_name or ""
                    await consumer.on_tool_call_end(tool_name, args, result_str, event.tool_call_id, is_error=is_error)
                    yield

                elif isinstance(event, PartStartEvent) and isinstance(event.part, TextPart):
                    text_buffer += event.part.content

                elif isinstance(event, PartDeltaEvent) and isinstance(event.delta, TextPartDelta):
                    text_buffer += event.delta.content_delta

                elif isinstance(event, AgentRunResultEvent):
                    self._message_history = list(event.result.all_messages())
                    if text_buffer:
                        await consumer.on_final_response(text_buffer)
                        yield
                        text_buffer = ""
        except UnexpectedModelBehavior as exc:
            await consumer.on_error(str(exc))
            yield
