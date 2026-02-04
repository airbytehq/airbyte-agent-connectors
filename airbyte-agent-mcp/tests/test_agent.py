"""Tests for agent helper functions, StreamConsumer, and AgentRunner."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from pydantic_ai import (
    AgentRunResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    TextPartDelta,
)
from pydantic_ai.messages import RetryPromptPart, TextPart, ToolCallPart, ToolReturnPart

from airbyte_agent_mcp.agent import (
    AgentRunner,
    StreamConsumer,
    _parse_args,
    build_system_prompt,
    create_agent,
    entity_name,
    tool_title,
)


class TestEntityName:
    def test_entity_name_key(self):
        assert entity_name({"entity_name": "users"}) == "users"

    def test_entity_key(self):
        assert entity_name({"entity": "calls"}) == "calls"

    def test_name_key(self):
        assert entity_name({"name": "deals"}) == "deals"

    def test_fallback_to_unknown(self):
        assert entity_name({}) == "unknown"

    def test_priority_order(self):
        assert entity_name({"entity_name": "first", "entity": "second", "name": "third"}) == "first"

    def test_skips_falsy_entity_name(self):
        assert entity_name({"entity_name": "", "entity": "fallback"}) == "fallback"


class TestToolTitle:
    def test_execute_with_entity_and_action(self):
        assert tool_title("execute", {"entity": "users", "action": "list"}) == "Execute (users, list)"

    def test_execute_with_entity_only(self):
        assert tool_title("execute", {"entity": "users"}) == "Execute (users)"

    def test_execute_without_entity(self):
        assert tool_title("execute", {}) == "Execute"

    def test_non_execute_with_underscores(self):
        assert tool_title("get_instructions", {}) == "Get Instructions"

    def test_non_execute_with_hyphens(self):
        assert tool_title("entity-schema", {}) == "Entity Schema"

    def test_simple_name(self):
        assert tool_title("connector_info", {}) == "Connector Info"


class TestBuildSystemPrompt:
    def test_includes_connector_name_and_version(self):
        connector = MagicMock()
        connector.connector_name = "Gong"
        connector.connector_version = "1.2.3"
        connector.list_entities.return_value = []

        prompt = build_system_prompt(connector)
        assert "Gong" in prompt
        assert "1.2.3" in prompt

    def test_includes_entities_with_actions(self):
        connector = MagicMock()
        connector.connector_name = "Test"
        connector.connector_version = "0.1"
        connector.list_entities.return_value = [
            {"entity_name": "users", "available_actions": [{"name": "list"}, {"name": "get"}]},
            {"entity_name": "calls", "available_actions": [{"name": "search"}]},
        ]

        prompt = build_system_prompt(connector)
        assert "users: list, get" in prompt
        assert "calls: search" in prompt

    def test_handles_string_actions(self):
        connector = MagicMock()
        connector.connector_name = "Test"
        connector.connector_version = "0.1"
        connector.list_entities.return_value = [
            {"entity_name": "items", "actions": ["list", "get"]},
        ]

        prompt = build_system_prompt(connector)
        assert "items: list, get" in prompt


class TestCreateAgent:
    @patch("airbyte_agent_mcp.agent.Agent")
    @patch("airbyte_agent_mcp.agent.FastMCPToolset")
    def test_creates_agent_with_correct_model(self, mock_toolset_cls, mock_agent_cls):
        connector = MagicMock()
        connector.connector_name = "Test"
        connector.connector_version = "1.0"
        connector.list_entities.return_value = []

        create_agent(connector, model="claude-opus-4-20250514")

        mock_agent_cls.assert_called_once()
        call_args = mock_agent_cls.call_args
        assert call_args[0][0] == "anthropic:claude-opus-4-20250514"

    @patch("airbyte_agent_mcp.agent.Agent")
    @patch("airbyte_agent_mcp.agent.FastMCPToolset")
    def test_passes_system_prompt_as_instructions(self, mock_toolset_cls, mock_agent_cls):
        connector = MagicMock()
        connector.connector_name = "Gong"
        connector.connector_version = "2.0"
        connector.list_entities.return_value = []

        create_agent(connector)

        call_kwargs = mock_agent_cls.call_args[1]
        assert "Gong" in call_kwargs["instructions"]
        assert "2.0" in call_kwargs["instructions"]

    @patch("airbyte_agent_mcp.agent.Agent")
    @patch("airbyte_agent_mcp.agent.FastMCPToolset")
    def test_passes_fastmcp_toolset(self, mock_toolset_cls, mock_agent_cls):
        connector = MagicMock()
        connector.connector_name = "Test"
        connector.connector_version = "1.0"
        connector.list_entities.return_value = []

        create_agent(connector)

        mock_toolset_cls.assert_called_once()
        call_kwargs = mock_agent_cls.call_args[1]
        assert len(call_kwargs["toolsets"]) == 1
        assert call_kwargs["toolsets"][0] == mock_toolset_cls.return_value


class TestParseArgs:
    def test_dict_passthrough(self):
        assert _parse_args({"a": 1}) == {"a": 1}

    def test_json_string(self):
        assert _parse_args('{"entity": "users"}') == {"entity": "users"}

    def test_invalid_json(self):
        assert _parse_args("not json") == {}

    def test_none(self):
        assert _parse_args(None) == {}

    def test_non_dict_json(self):
        assert _parse_args("[1,2,3]") == {}


class TestStreamConsumerDefaults:
    """StreamConsumer methods are no-ops by default."""

    @pytest.mark.asyncio
    async def test_on_tool_call_start_is_noop(self):
        consumer = _make_concrete_consumer()
        await consumer.on_tool_call_start("tool", {}, "id")

    @pytest.mark.asyncio
    async def test_on_tool_call_end_is_noop(self):
        consumer = _make_concrete_consumer()
        await consumer.on_tool_call_end("tool", {}, "result", "id", is_error=False)

    @pytest.mark.asyncio
    async def test_on_intermediate_response_is_noop(self):
        consumer = _make_concrete_consumer()
        await consumer.on_intermediate_response("text")

    @pytest.mark.asyncio
    async def test_on_final_response_is_noop(self):
        consumer = _make_concrete_consumer()
        await consumer.on_final_response("text")

    @pytest.mark.asyncio
    async def test_on_error_is_noop(self):
        consumer = _make_concrete_consumer()
        await consumer.on_error("something broke")


def _make_concrete_consumer() -> StreamConsumer:
    """Create a StreamConsumer with default no-op implementations."""

    class ConcreteConsumer(StreamConsumer): ...

    return ConcreteConsumer()


# --- Helpers for AgentRunner tests ---


def _tool_call_event(tool_name: str, args: dict[str, Any], tool_call_id: str) -> FunctionToolCallEvent:
    return FunctionToolCallEvent(part=ToolCallPart(tool_name=tool_name, args=args, tool_call_id=tool_call_id))


def _tool_result_event(tool_name: str, content: str, tool_call_id: str) -> FunctionToolResultEvent:
    return FunctionToolResultEvent(result=ToolReturnPart(tool_name=tool_name, content=content, tool_call_id=tool_call_id))


def _tool_error_event(tool_name: str, error: str, tool_call_id: str) -> FunctionToolResultEvent:
    return FunctionToolResultEvent(result=RetryPromptPart(content=error, tool_name=tool_name, tool_call_id=tool_call_id))


def _text_start_event(text: str) -> PartStartEvent:
    return PartStartEvent(index=0, part=TextPart(content=text))


def _text_delta_event(text: str) -> PartDeltaEvent:
    return PartDeltaEvent(index=0, delta=TextPartDelta(content_delta=text))


def _run_result_event(messages: list | None = None) -> AgentRunResultEvent:
    mock_result = MagicMock()
    mock_result.all_messages.return_value = messages or []
    return AgentRunResultEvent(result=mock_result)


class RecordingConsumer(StreamConsumer):
    """Records all callbacks for assertions."""

    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, Any]]] = []

    async def on_tool_call_start(self, tool_name: str, args: dict[str, Any], tool_call_id: str) -> None:
        self.events.append(("tool_call_start", {"tool_name": tool_name, "args": args, "tool_call_id": tool_call_id}))

    async def on_tool_call_end(self, tool_name: str, args: dict[str, Any], result: str, tool_call_id: str, *, is_error: bool) -> None:
        self.events.append(
            (
                "tool_call_end",
                {"tool_name": tool_name, "args": args, "result": result, "tool_call_id": tool_call_id, "is_error": is_error},
            )
        )

    async def on_intermediate_response(self, text: str) -> None:
        self.events.append(("intermediate_response", {"text": text}))

    async def on_final_response(self, text: str) -> None:
        self.events.append(("final_response", {"text": text}))

    async def on_error(self, error: str) -> None:
        self.events.append(("error", {"error": error}))


def _make_runner(events: list, *, raise_after: Exception | None = None) -> AgentRunner:
    """Create an AgentRunner with a mocked agent that yields the given events."""
    agent = MagicMock()

    async def fake_stream(prompt, message_history=None):
        for e in events:
            yield e
        if raise_after:
            raise raise_after

    agent.run_stream_events = fake_stream
    return AgentRunner(agent)


async def _collect(runner: AgentRunner, prompt: str, consumer: RecordingConsumer) -> list:
    """Drain the runner generator and return consumer events."""
    async for _ in runner.run(prompt, consumer):
        pass
    return consumer.events


class TestAgentRunner:
    @pytest.mark.asyncio
    async def test_final_response_text_only(self):
        events = [
            _text_start_event("Hello "),
            _text_delta_event("world"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "hi", consumer)

        assert len(result) == 1
        assert result[0] == ("final_response", {"text": "Hello world"})

    @pytest.mark.asyncio
    async def test_tool_call_dispatches_start_and_end(self):
        events = [
            _tool_call_event("execute", {"entity": "users"}, "tc1"),
            _tool_result_event("execute", '{"data": []}', "tc1"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "list users", consumer)

        assert result[0] == ("tool_call_start", {"tool_name": "execute", "args": {"entity": "users"}, "tool_call_id": "tc1"})
        assert result[1][0] == "tool_call_end"
        assert result[1][1]["tool_name"] == "execute"
        assert result[1][1]["is_error"] is False
        assert result[1][1]["result"] == '{"data": []}'

    @pytest.mark.asyncio
    async def test_tool_error_sets_is_error_flag(self):
        events = [
            _tool_call_event("execute", {}, "tc1"),
            _tool_error_event("execute", "validation failed", "tc1"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "bad call", consumer)

        end_event = next(e for e in result if e[0] == "tool_call_end")
        assert end_event[1]["is_error"] is True
        assert "validation failed" in end_event[1]["result"]

    @pytest.mark.asyncio
    async def test_intermediate_response_flushed_before_tool_call(self):
        events = [
            _text_start_event("thinking... "),
            _tool_call_event("execute", {}, "tc1"),
            _tool_result_event("execute", "ok", "tc1"),
            _text_start_event("done"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "think then act", consumer)

        assert result[0] == ("intermediate_response", {"text": "thinking... "})
        assert result[1][0] == "tool_call_start"
        assert result[-1] == ("final_response", {"text": "done"})

    @pytest.mark.asyncio
    async def test_message_history_accumulates(self):
        messages_run1 = [MagicMock(), MagicMock()]
        events = [
            _text_start_event("response"),
            _run_result_event(messages=messages_run1),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        await _collect(runner, "first", consumer)

        assert runner._message_history == messages_run1

    @pytest.mark.asyncio
    async def test_yields_after_each_callback(self):
        events = [
            _tool_call_event("tool", {}, "tc1"),
            _tool_result_event("tool", "ok", "tc1"),
            _text_delta_event("done"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()

        yield_count = 0
        async for _ in runner.run("test", consumer):
            yield_count += 1

        # tool_call_start, tool_call_end, final_response
        assert yield_count == 3

    @pytest.mark.asyncio
    async def test_non_text_delta_ignored(self):
        """PartDeltaEvent with non-TextPartDelta delta is ignored."""
        non_text_delta = MagicMock()
        non_text_delta.__class__ = type("ThinkingPartDelta", (), {})

        events = [
            PartDeltaEvent(index=0, delta=non_text_delta),
            _text_delta_event("answer"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "think", consumer)

        assert len(result) == 1
        assert result[0] == ("final_response", {"text": "answer"})

    @pytest.mark.asyncio
    async def test_tool_call_args_as_json_string(self):
        """Args provided as JSON string are parsed correctly."""
        events = [
            FunctionToolCallEvent(part=ToolCallPart(tool_name="execute", args='{"entity": "calls"}', tool_call_id="tc1")),
            _tool_result_event("execute", "ok", "tc1"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "test", consumer)

        assert result[0][1]["args"] == {"entity": "calls"}

    @pytest.mark.asyncio
    async def test_empty_text_buffer_no_final_response(self):
        """If no text is emitted, on_final_response is not called."""
        events = [
            _tool_call_event("tool", {}, "tc1"),
            _tool_result_event("tool", "ok", "tc1"),
            _run_result_event(),
        ]
        runner = _make_runner(events)
        consumer = RecordingConsumer()
        result = await _collect(runner, "test", consumer)

        assert not any(e[0] == "final_response" for e in result)
        assert not any(e[0] == "intermediate_response" for e in result)

    @pytest.mark.asyncio
    async def test_unexpected_model_behavior_calls_on_error(self):
        """UnexpectedModelBehavior is caught and dispatched via on_error."""
        from pydantic_ai import UnexpectedModelBehavior

        events = [
            _tool_call_event("execute", {}, "tc1"),
            _tool_result_event("execute", "ok", "tc1"),
        ]
        runner = _make_runner(events, raise_after=UnexpectedModelBehavior("Tool 'execute' exceeded max retries count of 1"))
        consumer = RecordingConsumer()
        result = await _collect(runner, "test", consumer)

        error_event = next(e for e in result if e[0] == "error")
        assert "exceeded max retries" in error_event[1]["error"]
