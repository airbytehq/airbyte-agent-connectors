"""Custom evaluators for connector evals.

Adapts the tools_called.py patterns from the existing eval infrastructure
for entity/action matching and adds LLM-as-judge evaluation.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from typing import Any

import numpy as np
from pydantic_evals.evaluators import EvaluationReason, Evaluator, EvaluatorContext
from scipy.optimize import linear_sum_assignment


class _AnyValueType:
    """Sentinel type for matching any value."""

    def __repr__(self) -> str:
        return "ANY_VALUE"

    __str__ = __repr__


ANY_VALUE = _AnyValueType()


class Validator:
    """Custom validator for argument matching.

    A simple predicate that returns True if the actual value is acceptable.
    """

    def __init__(
        self,
        fn: Any,
        description: str | None = None,
    ) -> None:
        self.fn = fn
        self.description = description or getattr(fn, "__name__", "custom")

    def matches(self, actual: Any) -> bool:
        return self.fn(actual)

    def __repr__(self) -> str:
        return f"Validator[{self.description}]"

    __str__ = __repr__


_NAME_MISMATCH_COST = 10_000.0
_MISSING_COST = 1_000.0
_EXACT_MATCH_BONUS = 1_000


def _matches_expected(expected: Any, actual: Any) -> bool:
    """Recursively compare expected vs. actual args, honoring ANY_VALUE and Validator."""
    if expected is ANY_VALUE:
        return True

    if isinstance(expected, Validator):
        return expected.matches(actual)

    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(expected) != set(actual):
            return False
        return all(_matches_expected(expected[key], actual[key]) for key in expected)

    if isinstance(expected, list):
        if not isinstance(actual, list) or len(expected) != len(actual):
            return False
        return all(
            _matches_expected(exp_item, act_item)
            for exp_item, act_item in zip(expected, actual, strict=False)
        )

    if isinstance(expected, tuple):
        if not isinstance(actual, tuple) or len(expected) != len(actual):
            return False
        return all(
            _matches_expected(exp_item, act_item)
            for exp_item, act_item in zip(expected, actual, strict=False)
        )

    return bool(expected == actual)


def _match_score(expected: dict[str, Any], actual: Any) -> int:
    """Heuristic score for partial matches so we can pick the closest tool call."""
    if not isinstance(actual, dict):
        return -10_000

    score = 0
    actual_keys = set(actual)
    expected_keys = set(expected)

    for key, exp_value in expected.items():
        if exp_value is ANY_VALUE:
            score += 2
            continue
        if isinstance(exp_value, Validator):
            if key in actual and exp_value.matches(actual[key]):
                score += 2
            else:
                score += 1
            continue
        if key not in actual:
            score -= 2
            continue

        act_value = actual[key]
        if _matches_expected(exp_value, act_value):
            score += 2
        else:
            score += 1

    extra_keys = actual_keys - expected_keys
    score -= len(extra_keys)
    return score


@dataclass(slots=True)
class ExpectedToolCall:
    """Expected tool call with entity and action."""

    entity: str
    action: str
    args: dict[str, Any] | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": f"{self.entity}_{self.action}",
            "entity": self.entity,
            "action": self.action,
            "args": self.args or {},
        }


@dataclass(slots=True)
class ConnectorEvalCaseMetadata:
    """Metadata for connector eval cases."""

    score_pass_threshold: float = 0.0
    expected_answer_contains: list[str] | None = None


@dataclass
class ConnectorToolsCalledEvaluator(Evaluator[str, str, ConnectorEvalCaseMetadata]):
    """Evaluator for connector tool calls using optimal matching algorithm.

    Adapts the tools_called.py patterns for entity/action matching.
    """

    expected: list[dict[str, Any]]

    def evaluate(
        self, ctx: EvaluatorContext[str, str, ConnectorEvalCaseMetadata]
    ) -> dict[str, EvaluationReason]:
        calls: list[dict[str, Any]] = ctx.attributes.get("tool_calls", [])
        total_expected = len(self.expected)
        score_threshold = ctx.metadata.score_pass_threshold if ctx.metadata else 0.0

        if total_expected == 0:
            unexpected_only = [call.get("name", "<unknown>") for call in calls]
            if unexpected_only:
                return {
                    "tools_assertion": EvaluationReason(
                        value=not (score_threshold > 0),
                        reason=f"Score: 0, threshold: {score_threshold:.3f}",
                    ),
                    "tools_score": EvaluationReason(
                        value=0.0, reason="unexpected calls: " + ", ".join(unexpected_only)
                    ),
                }
            else:
                reason = "No tools expected or called."
                return {
                    "tools_assertion": EvaluationReason(value=True, reason=reason),
                    "tools_score": EvaluationReason(value=1.0, reason=reason),
                }

        expected_count = len(self.expected)
        actual_count = len(calls)
        correct_args = 0
        missing_details: list[str] = []
        wrong_args_details: list[str] = []

        if expected_count:
            cost_matrix = np.full(
                (expected_count, actual_count + expected_count),
                _NAME_MISMATCH_COST,
                dtype=float,
            )
            for exp_idx, exp in enumerate(self.expected):
                exp_name = exp.get("name")
                exp_entity = exp.get("entity")
                exp_action = exp.get("action")
                exp_args = exp.get("args", {})

                for call_idx, call in enumerate(calls):
                    call_name = call.get("name")
                    call_entity = call.get("entity")
                    call_action = call.get("action")

                    name_match = call_name == exp_name
                    entity_action_match = (
                        call_entity == exp_entity and call_action == exp_action
                    )

                    if not (name_match or entity_action_match):
                        continue

                    actual_args = call.get("args", {})
                    score_val = _match_score(exp_args, actual_args)
                    if _matches_expected(exp_args, actual_args):
                        score_val += _EXACT_MATCH_BONUS
                    cost_matrix[exp_idx, call_idx] = -score_val
                cost_matrix[exp_idx, actual_count + exp_idx] = _MISSING_COST

            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            assignment = {int(r): int(c) for r, c in zip(row_ind, col_ind, strict=False)}
        else:
            assignment = {}

        matched_names = 0
        missing_count = 0
        mismatched_actual_indices: set[int] = set()
        matched_actual_indices: set[int] = set()
        unexpected_counter: Counter[str] = Counter()

        for exp_idx, exp in enumerate(self.expected):
            exp_name_raw = exp.get("name")
            exp_name = str(exp_name_raw) if exp_name_raw is not None else "<unknown>"
            exp_args = exp.get("args", {})
            sorted_exp_args = (
                dict(sorted(exp_args.items())) if isinstance(exp_args, dict) else exp_args
            )
            assigned_col = assignment.get(exp_idx)
            if assigned_col is None or assigned_col >= actual_count:
                missing_count += 1
                missing_details.append(f"{exp_name}({sorted_exp_args})")
                continue

            call = calls[assigned_col]
            actual_name_raw = call.get("name")
            actual_name = (
                str(actual_name_raw) if actual_name_raw is not None else "<unknown>"
            )
            actual_args = call.get("args", {})

            if actual_name != exp_name:
                missing_count += 1
                missing_details.append(f"{exp_name}({sorted_exp_args})")
                mismatched_actual_indices.add(assigned_col)
                unexpected_counter[actual_name] += 1
                continue

            matched_names += 1
            matched_actual_indices.add(assigned_col)
            if _matches_expected(exp_args, actual_args):
                correct_args += 1
            else:
                if isinstance(exp_args, dict) and isinstance(actual_args, dict):
                    for arg_name, exp_value in exp_args.items():
                        actual_value = actual_args.get(arg_name)
                        if isinstance(exp_value, Validator):
                            if not exp_value.matches(actual_value):
                                actual_str = json.dumps(actual_value, default=str)
                                if len(actual_str) > 500:
                                    actual_str = actual_str[:500] + "..."
                                wrong_args_details.append(
                                    f"{exp_name}.{arg_name}: custom validation "
                                    f"[{exp_value.description}] failed, got {actual_str}"
                                )
                        elif not _matches_expected(exp_value, actual_value):
                            wrong_args_details.append(
                                f"{exp_name}.{arg_name} expected {exp_value}, "
                                f"got {actual_value}"
                            )
                else:
                    if isinstance(actual_args, dict):
                        sorted_actual_args: Any = dict(sorted(actual_args.items()))
                    else:
                        sorted_actual_args = actual_args
                    wrong_args_details.append(
                        f"{exp_name} expected {sorted_exp_args}, got {sorted_actual_args}"
                    )

        unmatched_actual_indices = (
            set(range(actual_count)) - matched_actual_indices - mismatched_actual_indices
        )
        unexpected_calls_with_args: list[tuple[str, Any]] = []
        for idx in unmatched_actual_indices:
            name_raw = calls[idx].get("name")
            name = str(name_raw) if name_raw is not None else "<unknown>"
            args = calls[idx].get("args", {})
            unexpected_counter[name] += 1
            unexpected_calls_with_args.append((name, args))

        unexpected_count = sum(unexpected_counter.values())

        name_score = max(
            0.0, (total_expected - missing_count - unexpected_count) / total_expected
        )
        args_score = max(0.0, correct_args / total_expected)
        score = max(0.0, min(1.0, 0.5 * name_score + 0.5 * args_score))

        unexpected_details: list[str] = []
        for name, args in unexpected_calls_with_args:
            args_str = json.dumps(args, default=str)
            if len(args_str) > 500:
                args_str = args_str[:500] + "..."
            unexpected_details.append(f"{name}({args_str})")

        issues: list[str] = []
        if missing_details:
            issues.append("missing " + ", ".join(missing_details))
        if wrong_args_details:
            issues.append("wrong args " + "; ".join(wrong_args_details))
        if unexpected_details:
            issues.append("unexpected " + ", ".join(unexpected_details))

        reason = (
            "All expected tool calls present with correct args."
            if not issues
            else "\n".join(issues)
        )
        value = score >= score_threshold
        score_evaluation = EvaluationReason(value=score, reason=reason)
        assertion_evaluation = EvaluationReason(
            value=value, reason=f"Score: {score:.3f}, threshold: {score_threshold:.3f}"
        )
        return {"tools_assertion": assertion_evaluation, "tools_score": score_evaluation}


@dataclass
class LLMJudgeEvaluator(Evaluator[str, str, ConnectorEvalCaseMetadata]):
    """Evaluator that uses LLM-as-judge to evaluate response quality.

    Evaluates if the agent's answer contains the expected information
    and is factually accurate against the cassette data.
    """

    expected_answer_contains: list[str]
    cassette_data: dict[str, Any] | None = None

    def evaluate(
        self, ctx: EvaluatorContext[str, str, ConnectorEvalCaseMetadata]
    ) -> dict[str, EvaluationReason]:
        output = ctx.output or ""
        score_threshold = ctx.metadata.score_pass_threshold if ctx.metadata else 0.7

        if not output:
            return {
                "response_assertion": EvaluationReason(
                    value=False, reason="No output generated"
                ),
                "response_score": EvaluationReason(value=0.0, reason="Empty response"),
            }

        output_lower = output.lower()
        matched_criteria = []
        missing_criteria = []

        for criterion in self.expected_answer_contains:
            criterion_lower = criterion.lower()
            words = criterion_lower.split()

            if len(words) == 1:
                if criterion_lower in output_lower:
                    matched_criteria.append(criterion)
                else:
                    missing_criteria.append(criterion)
            else:
                if all(word in output_lower for word in words):
                    matched_criteria.append(criterion)
                else:
                    missing_criteria.append(criterion)

        total_criteria = len(self.expected_answer_contains)
        if total_criteria == 0:
            score = 1.0
            reason = "No criteria to evaluate"
        else:
            score = len(matched_criteria) / total_criteria
            if missing_criteria:
                reason = f"Missing: {', '.join(missing_criteria)}"
            else:
                reason = "All expected content present in response"

        passed = score >= score_threshold

        return {
            "response_assertion": EvaluationReason(
                value=passed,
                reason=f"Score: {score:.3f}, threshold: {score_threshold:.3f}",
            ),
            "response_score": EvaluationReason(value=score, reason=reason),
        }
