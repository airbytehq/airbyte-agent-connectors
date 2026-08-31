"""Monitoring helpers for fleet qualification results."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ValidationError

from airbyte_agent_sdk.validation.qualification import QualificationResult

QUALIFICATION_ISSUE_MARKER = "[connector-qualification]"


class QualificationAggregateEntry(BaseModel):
    """One entry in the fleet runner's aggregate output."""

    connector_name: str
    status: Literal["evaluated", "skipped", "failed"]
    claimed_status: str | None = None
    result: QualificationResult | None = None
    error: str | None = None


class QualificationGateFailure(BaseModel):
    """One evaluated Gate failure from an aggregate report."""

    connector_name: str
    criterion: str
    claimed_status: str
    observed: object
    threshold: object
    detail: str

    @property
    def key(self) -> str:
        """Return the durable connector/criterion identity."""
        return f"{self.connector_name}:{self.criterion}"


class QualificationIssue(BaseModel):
    """An existing GitHub issue used for qualification state."""

    number: int
    title: str
    state: Literal["OPEN", "CLOSED"]


@dataclass(frozen=True)
class FailureTransitions:
    """Issue and notification transitions for one aggregate run."""

    new: tuple[str, ...]
    reappeared: tuple[str, ...]
    recovered: tuple[str, ...]
    persistent: tuple[str, ...]


def load_aggregate(path: Path) -> list[QualificationAggregateEntry]:
    """Load and validate a fleet aggregate JSON file."""
    if not path.is_file():
        raise ValueError(f"aggregate JSON does not exist: {path}")
    try:
        payload = json.loads(path.read_text())
        if not isinstance(payload, list):
            raise ValueError("aggregate JSON must be an array")
        return [QualificationAggregateEntry.model_validate(item) for item in payload]
    except (OSError, json.JSONDecodeError, ValidationError) as error:
        raise ValueError(f"invalid aggregate JSON: {error}") from error


def gate_failures(entries: list[QualificationAggregateEntry]) -> list[QualificationGateFailure]:
    """Extract evaluated Gate failures, including candidate failures."""
    failures: list[QualificationGateFailure] = []
    for entry in entries:
        if entry.status != "evaluated" or entry.result is None:
            continue
        for criterion in entry.result.criteria:
            if criterion.kind != "gate" or not criterion.evaluated or criterion.passed:
                continue
            failures.append(
                QualificationGateFailure(
                    connector_name=entry.connector_name,
                    criterion=criterion.id,
                    claimed_status=entry.claimed_status or entry.result.claimed_status.value,
                    observed=criterion.observed,
                    threshold=criterion.threshold,
                    detail=criterion.detail,
                )
            )
    return failures


def failure_transitions(
    current: set[str],
    open_failures: set[str],
    closed_failures: set[str],
    evaluated_connectors: set[str],
    unevaluated_keys: set[str],
) -> FailureTransitions:
    """Classify issue transitions, recovering only keys actually evaluated this run."""
    known_evaluated = {
        key for key in open_failures | closed_failures if key.partition(":")[0] in evaluated_connectors and key not in unevaluated_keys
    }
    return FailureTransitions(
        new=tuple(sorted(current - open_failures - closed_failures)),
        reappeared=tuple(sorted(current & closed_failures)),
        recovered=tuple(sorted(known_evaluated - current)),
        persistent=tuple(sorted(current & open_failures)),
    )


def issue_title(failure: QualificationGateFailure) -> str:
    """Build the deterministic issue title."""
    return f"{QUALIFICATION_ISSUE_MARKER} {failure.connector_name} {failure.criterion}"


def _issue_key(title: str) -> str | None:
    """Extract a connector/criterion key from a qualification issue title."""
    prefix, separator, suffix = title.partition(" ")
    if prefix != QUALIFICATION_ISSUE_MARKER or not separator:
        return None
    parts = suffix.split()
    if len(parts) != 2 or not parts[1].startswith("C"):
        return None
    return f"{parts[0]}:{parts[1]}"


class QualificationIssuePlan(BaseModel):
    """Actions and notifications for one qualification run."""

    failures: list[QualificationGateFailure]
    create: list[QualificationGateFailure]
    reopen: list[QualificationIssue]
    close: list[QualificationIssue]
    message_text: str


def build_issue_plan(
    entries: list[QualificationAggregateEntry],
    issues: list[QualificationIssue],
) -> QualificationIssuePlan:
    """Build issue actions from aggregate results and current issue state."""
    failures = gate_failures(entries)
    failures_by_key = {failure.key: failure for failure in failures}
    issues_by_key = {key: issue for issue in issues if (key := _issue_key(issue.title)) is not None}
    open_keys = {key for key, issue in issues_by_key.items() if issue.state == "OPEN"}
    closed_keys = {key for key, issue in issues_by_key.items() if issue.state == "CLOSED"}
    evaluated_connectors = {entry.connector_name for entry in entries if entry.status == "evaluated"}
    unevaluated_keys = {
        f"{entry.connector_name}:{criterion}" for entry in entries if entry.result is not None for criterion in entry.result.unevaluated_criteria
    }
    transitions = failure_transitions(
        set(failures_by_key),
        open_keys,
        closed_keys,
        evaluated_connectors,
        unevaluated_keys,
    )
    create = [failures_by_key[key] for key in transitions.new]
    reopen = [issues_by_key[key] for key in transitions.reappeared]
    close = [issues_by_key[key] for key in transitions.recovered if key in open_keys]
    messages = [
        *(f"New qualification failure: {failure.key}" for failure in create),
        *(f"Qualification failure reappeared: {_issue_key(issue.title)}" for issue in reopen),
        *(f"Qualification failure recovered: {_issue_key(issue.title)}" for issue in close),
    ]
    return QualificationIssuePlan(
        failures=failures,
        create=create,
        reopen=reopen,
        close=close,
        message_text="\n".join(messages),
    )
