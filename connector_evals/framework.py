"""Core framework for connector evaluations.

Provides functions to create connector agents and run evaluations.
"""

from __future__ import annotations

import json
from contextlib import nullcontext
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from pydantic_ai import Agent, capture_run_messages
from pydantic_ai.messages import ToolCallPart
from pydantic_ai.models import override_allow_model_requests
from pydantic_evals import Case, Dataset
from pydantic_evals.dataset import set_eval_attribute
from pydantic_evals.reporting import EvaluationReport

from connector_evals.cassette_loader import CassetteLoader, load_cassettes_from_files
from connector_evals.evaluators import (
    ConnectorEvalCaseMetadata,
    ConnectorToolsCalledEvaluator,
    ExpectedToolCall,
    LLMJudgeEvaluator,
)


@dataclass
class ConnectorOperation:
    """Represents a connector operation (entity + action)."""

    entity: str
    action: str
    description: str
    parameters: list[dict[str, Any]] = field(default_factory=list)
    request_body: dict[str, Any] | None = None


@dataclass
class EvalCase:
    """Represents a single evaluation case."""

    name: str
    question: str
    cassettes: list[str]
    expected_tools: list[ExpectedToolCall]
    expected_answer_contains: list[str]
    score_threshold: float = 0.7


@dataclass
class EvaluationConfig:
    """Configuration for running evaluations."""

    connector_name: str
    eval_cases_path: Path
    cassette_dir: Path
    connector_yaml_path: Path | None = None


def parse_connector_yaml(connector_yaml_path: str | Path) -> list[ConnectorOperation]:
    """Parse connector.yaml to extract entities/actions.

    Args:
        connector_yaml_path: Path to the connector.yaml file

    Returns:
        List of ConnectorOperation objects
    """
    with open(connector_yaml_path) as f:
        spec = yaml.safe_load(f)

    operations: list[ConnectorOperation] = []

    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            if method in ("get", "post", "put", "delete", "patch"):
                entity = details.get("x-airbyte-entity")
                action = details.get("x-airbyte-action")

                if entity and action:
                    description = details.get("description", details.get("summary", ""))
                    parameters = details.get("parameters", [])
                    request_body = details.get("requestBody")

                    operations.append(
                        ConnectorOperation(
                            entity=entity,
                            action=action,
                            description=description,
                            parameters=parameters,
                            request_body=request_body,
                        )
                    )

    return operations


def create_connector_agent(
    connector_yaml_path: str | Path,
    cassette_loader: CassetteLoader,
    model: str = "openai:gpt-4o",
) -> Agent[None, str]:
    """Create a pydantic-ai agent with connector operations as tools.

    Args:
        connector_yaml_path: Path to the connector.yaml file
        cassette_loader: CassetteLoader with loaded cassettes
        model: The model to use for the agent

    Returns:
        A pydantic-ai Agent with connector tools registered
    """
    operations = parse_connector_yaml(connector_yaml_path)

    system_prompt = """You are a helpful assistant that answers business questions using data from a connector.
You have access to tools that can query different entities from the connector.
Use the appropriate tools to gather the data needed to answer the user's question.
After gathering data, provide a clear and concise answer based on the data you retrieved.
Always cite specific data points from the tool responses in your answer."""

    agent: Agent[None, str] = Agent(model=model, system_prompt=system_prompt)

    for op in operations:
        def make_tool_fn(
            entity: str, action: str, loader: CassetteLoader
        ) -> Any:
            async def tool_fn(**kwargs: Any) -> dict[str, Any]:
                response = loader.get_response(entity, action, kwargs)
                if response is None:
                    return {"error": f"No cassette found for {entity}/{action}"}
                return response.body

            tool_fn.__name__ = f"{entity}_{action}"
            tool_fn.__doc__ = f"Query {entity} with action {action}"
            return tool_fn

        tool_fn = make_tool_fn(op.entity, op.action, cassette_loader)
        agent.tool_plain(tool_fn)

    return agent


def load_eval_cases(eval_cases_path: str | Path) -> list[EvalCase]:
    """Load evaluation cases from a YAML file.

    Args:
        eval_cases_path: Path to the eval_cases.yaml file

    Returns:
        List of EvalCase objects
    """
    with open(eval_cases_path) as f:
        data = yaml.safe_load(f)

    cases = []
    for case_data in data.get("cases", []):
        expected_tools = []
        for tool in case_data.get("expected_tools", []):
            expected_tools.append(
                ExpectedToolCall(
                    entity=tool.get("entity", ""),
                    action=tool.get("action", ""),
                    args=tool.get("args"),
                )
            )

        cases.append(
            EvalCase(
                name=case_data.get("name", ""),
                question=case_data.get("question", ""),
                cassettes=case_data.get("cassettes", []),
                expected_tools=expected_tools,
                expected_answer_contains=case_data.get("expected_answer_contains", []),
                score_threshold=case_data.get("score_threshold", 0.7),
            )
        )

    return cases


async def _run_agent_with_capture(
    agent: Agent[None, str], prompt: str, *, allow_model_requests: bool
) -> tuple[str, list[dict[str, Any]]]:
    """Run agent and capture tool calls.

    Args:
        agent: The pydantic-ai agent
        prompt: The user prompt
        allow_model_requests: Whether to allow model requests

    Returns:
        Tuple of (output, tool_calls)
    """
    with override_allow_model_requests(allow_model_requests):
        with capture_run_messages() as recorded_msgs:
            result = await agent.run(user_prompt=prompt)

        output = result.data if hasattr(result, "data") else str(result)
        tool_calls: list[dict[str, Any]] = []

        for msg in recorded_msgs:
            if hasattr(msg, "parts"):
                for part in msg.parts:
                    if isinstance(part, ToolCallPart):
                        tool_args = (
                            json.loads(part.args)
                            if isinstance(part.args, str)
                            else part.args
                        )
                        tool_name = part.tool_name

                        parts = tool_name.rsplit("_", 1)
                        if len(parts) == 2:
                            entity, action = parts[0], parts[1]
                        else:
                            entity, action = tool_name, "unknown"

                        tool_calls.append(
                            {
                                "name": tool_name,
                                "entity": entity,
                                "action": action,
                                "args": tool_args,
                            }
                        )

        return output, tool_calls


async def run_connector_evals(
    connector_name: str,
    eval_cases_path: str | Path,
    cassette_dir: str | Path,
    connector_yaml_path: str | Path | None = None,
    model: str = "openai:gpt-4o",
    allow_model_requests: bool = True,
    max_concurrency: int = 4,
) -> EvaluationReport[str, Any, Any]:
    """Run all eval cases for a connector.

    Args:
        connector_name: Name of the connector (e.g., "gong")
        eval_cases_path: Path to the eval_cases.yaml file
        cassette_dir: Directory containing cassette files
        connector_yaml_path: Path to connector.yaml (auto-detected if None)
        model: The model to use for the agent
        allow_model_requests: Whether to allow model requests
        max_concurrency: Maximum concurrent evaluations

    Returns:
        EvaluationReport with results
    """
    eval_cases_path = Path(eval_cases_path)
    cassette_dir = Path(cassette_dir)

    if connector_yaml_path is None:
        possible_paths = [
            eval_cases_path.parent.parent / f"airbyte_ai_{connector_name}" / "connector.yaml",
            eval_cases_path.parent.parent / "connector.yaml",
        ]
        for path in possible_paths:
            if path.exists():
                connector_yaml_path = path
                break

        if connector_yaml_path is None:
            raise ValueError(
                f"Could not find connector.yaml for {connector_name}. "
                "Please provide connector_yaml_path explicitly."
            )

    eval_cases = load_eval_cases(eval_cases_path)

    all_cassettes: set[str] = set()
    for case in eval_cases:
        all_cassettes.update(case.cassettes)

    cassette_loader = load_cassettes_from_files(cassette_dir, list(all_cassettes))

    agent = create_connector_agent(connector_yaml_path, cassette_loader, model)

    dataset_cases: list[Case[str, str, ConnectorEvalCaseMetadata]] = []

    for case in eval_cases:
        expected_calls = [tool.as_dict() for tool in case.expected_tools]

        tools_evaluator = ConnectorToolsCalledEvaluator(expected=expected_calls)
        response_evaluator = LLMJudgeEvaluator(
            expected_answer_contains=case.expected_answer_contains
        )

        metadata = ConnectorEvalCaseMetadata(
            score_pass_threshold=case.score_threshold,
            expected_answer_contains=case.expected_answer_contains,
        )

        dataset_cases.append(
            Case(
                name=case.name,
                inputs=case.question,
                expected_output=None,
                evaluators=(tools_evaluator, response_evaluator),
                metadata=metadata,
            )
        )

    dataset = Dataset(cases=dataset_cases)

    async def connector_eval(prompt: str) -> str:
        output, tool_calls = await _run_agent_with_capture(
            agent, prompt, allow_model_requests=allow_model_requests
        )
        set_eval_attribute("tool_calls", tool_calls)
        return output

    report = await dataset.evaluate(
        connector_eval,
        name=f"{connector_name}_evals",
        max_concurrency=max_concurrency,
    )

    return report


def run_assertions_in_report(
    report: EvaluationReport[str, Any, Any], *, subtests: Any | None = None
) -> None:
    """Run assertions on the evaluation report.

    Args:
        report: The evaluation report
        subtests: Optional pytest subtests fixture
    """
    if report.failures:
        raise AssertionError(report.failures[0].error_message)

    for report_case in report.cases:
        score_reason_by_name = {k: v.reason for k, v in report_case.scores.items()}
        context = (
            subtests.test(msg=report_case.name) if subtests is not None else nullcontext()
        )
        if report_case.evaluator_failures:
            raise AssertionError(
                f"Evaluator failures in case '{report_case.name}': "
                f"{report_case.evaluator_failures}"
            )
        with context:
            for name, result in report_case.assertions.items():
                assert result.value is True, (
                    f"Case '{report_case.name}' failed assertion '{name}': {result.reason}\n"
                    f"Output: {report_case.output}\n"
                    f"Details: {score_reason_by_name.get('score', '<none>')}"
                )
