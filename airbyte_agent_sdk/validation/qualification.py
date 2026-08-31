"""Qualification criteria validation for agent connectors."""

import json
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field, ValidationError

from airbyte_agent_sdk.connector_model_loader import (
    ConnectorModelLoaderError,
    load_connector_model,
)
from airbyte_agent_sdk.schema.base import RuntimeMode
from airbyte_agent_sdk.schema.extensions import QualificationStatus
from airbyte_agent_sdk.types import Action
from airbyte_agent_sdk.validation.overview import (
    compute_golden_questions_hash,
    load_golden_questions_report,
)
from airbyte_agent_sdk.validation.readiness import (
    READINESS_PROGRESS_STEPS,
    build_auth_scheme_coverage,
    build_cassette_map,
    validate_connector_readiness,
)

QUALIFICATION_CRITERIA_VERSION = "v1"
MIN_GOLDEN_QUESTIONS_SUCCESS_RATE = 1.0
MIN_GOLDEN_QUESTIONS_ENTITY_COVERAGE = 1.0
MAX_UNTESTED_OPERATION_RATIO = 0.0
MAX_READINESS_WARNING_COUNT = 5
LIVE_SMOKE_FRESHNESS_HOURS = 48
LIVE_SMOKE_FRESHNESS_SECONDS = LIVE_SMOKE_FRESHNESS_HOURS * 60 * 60
WRITE_ACTIONS = {Action.CREATE.value, Action.UPDATE.value, Action.DELETE.value}
QUALIFICATION_CRITERION_IDS = tuple(f"C{index}" for index in range(1, 18) if index != 13)
QUALIFICATION_PROGRESS_STEPS = (
    "Loading connector model",
    *READINESS_PROGRESS_STEPS,
    "C14: write action coverage",
    "C15: untested-operation budget",
    "C16: smoke suite wiring",
    "C8: golden-questions report",
    "C9: report freshness",
    "C10: golden-questions pass rate",
    "C11: declared questions run",
    "C12: entity/action coverage",
    "C17: live smoke result",
)


class CriterionOutcome(BaseModel):
    """Observed result for one qualification criterion."""

    id: str
    title: str
    kind: Literal["gate", "warn"]
    passed: bool = False
    evaluated: bool = True
    observed: Any = None
    threshold: Any = None
    detail: str
    bypassed: bool = False


class GoldenQuestionsSummary(BaseModel):
    """Summary block of a golden-questions report."""

    success_rate: float | None = None
    total_questions: int | None = None


class GoldenQuestionsCoverage(BaseModel):
    """Coverage block of a golden-questions report."""

    entity_action_pairs: list[Any] = Field(default_factory=list)


class GoldenQuestionsReport(BaseModel):
    """Typed view of tests/golden_questions_report.yaml."""

    freshness_hash: str | None = None
    summary: GoldenQuestionsSummary = Field(default_factory=GoldenQuestionsSummary)
    coverage: GoldenQuestionsCoverage = Field(default_factory=GoldenQuestionsCoverage)

    @classmethod
    def from_raw(cls, raw: dict[str, Any] | None) -> "GoldenQuestionsReport | None":
        """Parse a raw report, treating a malformed one as absent."""
        if raw is None:
            return None
        try:
            return cls.model_validate(raw)
        except ValidationError:
            return None


class QualificationResult(BaseModel):
    """Complete qualification report for one connector."""

    connector_name: str
    claimed_status: QualificationStatus
    qualified: bool = False
    load_error: str | None = None
    criteria_version: str = QUALIFICATION_CRITERIA_VERSION
    criteria: list[CriterionOutcome]
    bypasses_applied: list[str] = Field(default_factory=list)
    invalid_bypasses: list[str] = Field(default_factory=list)
    unevaluated_criteria: list[str] = Field(default_factory=list)
    readiness_warnings: list[str] = Field(default_factory=list)


class LiveSmokeResult(BaseModel):
    """Machine-readable result for one connector's live smoke run."""

    connector_name: str
    status: Literal["passed", "failed"]
    timestamp: datetime
    workflow_run_id: str | None = None
    workflow_run_url: str | None = None
    commit_sha: str | None = None


def _load_live_smoke_result(path: Path | None, connector_name: str) -> LiveSmokeResult | Literal["invalid"] | None:
    """Load a connector result from a file or result directory.

    Returns "invalid" when a result file exists but cannot be parsed, so a
    corrupt or schema-drifted artifact fails the gate instead of reading as
    "no result available".
    """
    if path is None:
        return None
    candidate = path / f"{connector_name}.json" if path.is_dir() else path
    if path.is_dir() and not candidate.is_file():
        candidate = next(path.rglob(f"{connector_name}.json"), candidate)
    if not candidate.is_file():
        return None
    try:
        payload = json.loads(candidate.read_text())
        if isinstance(payload, list):
            payload = next(
                (item for item in payload if isinstance(item, dict) and item.get("connector_name") == connector_name),
                None,
            )
            if payload is None:
                return None
        if not isinstance(payload, dict) or payload.get("connector_name") != connector_name:
            return "invalid"
        return LiveSmokeResult.model_validate(payload)
    except (OSError, json.JSONDecodeError, ValidationError):
        return "invalid"


def _live_smoke_outcome(
    smoke_result: LiveSmokeResult | Literal["invalid"] | None,
    now: datetime | None = None,
) -> tuple[bool, bool, object, str]:
    """Evaluate live smoke status and freshness."""
    if smoke_result is None:
        return False, False, None, "No plumbed result from the latest live smoke run is available."
    if smoke_result == "invalid":
        return False, True, "invalid", "A live smoke result exists but could not be parsed."
    current_time = now or datetime.now(UTC)
    observed_time = smoke_result.timestamp
    if observed_time.tzinfo is None:
        observed_time = observed_time.replace(tzinfo=UTC)
    age_seconds = max(0.0, (current_time - observed_time).total_seconds())
    if smoke_result.status != "passed":
        return False, True, smoke_result.status, "The latest live smoke run failed."
    if age_seconds > LIVE_SMOKE_FRESHNESS_SECONDS:
        age_hours = age_seconds / 3600
        return (
            False,
            True,
            {"status": smoke_result.status, "age_hours": round(age_hours, 2)},
            f"The live smoke result is stale ({age_hours:.1f} hours old; freshness window is {LIVE_SMOKE_FRESHNESS_HOURS} hours).",
        )
    return True, True, {"status": smoke_result.status, "age_hours": round(age_seconds / 3600, 2)}, "The live smoke result is fresh and passed."


def _build_criterion_outcome(
    criterion_id: str,
    title: str,
    kind: Literal["gate", "warn"],
    passed: bool,
    observed: Any,
    threshold: Any,
    detail: str,
    bypass_reasons: dict[str, str],
    evaluated: bool = True,
) -> CriterionOutcome:
    """Build one criterion outcome, applying a documented bypass."""
    reason = bypass_reasons.get(criterion_id)
    if reason is not None and evaluated:
        return CriterionOutcome(
            id=criterion_id,
            title=title,
            kind=kind,
            passed=True,
            evaluated=evaluated,
            observed=observed,
            threshold=threshold,
            detail=f"Bypassed: {reason}",
            bypassed=True,
        )
    return CriterionOutcome(
        id=criterion_id,
        title=title,
        kind=kind,
        passed=passed if evaluated else False,
        evaluated=evaluated,
        observed=observed,
        threshold=threshold,
        detail=detail,
    )


def _claimed_status_from_raw_yaml(connector_yaml: Path) -> QualificationStatus | None:
    """Best-effort claim recovery for a YAML the typed model cannot load."""
    try:
        raw = yaml.safe_load(connector_yaml.read_text())
        return QualificationStatus(raw["info"]["x-airbyte-qualification"]["status"])
    except (OSError, yaml.YAMLError, KeyError, TypeError, ValueError):
        return None


def _load_connector_claim(connector_path: Path, connector_yaml: Path) -> tuple[Any, Any, str, str | None, QualificationStatus]:
    """Load the connector model and recover its qualification claim."""
    config = None
    load_error: str | None = None
    connector_name = connector_path.name
    if connector_yaml.exists():
        try:
            config = load_connector_model(connector_yaml)
            connector_name = config.name
        except ConnectorModelLoaderError as error:
            load_error = str(error)
    else:
        load_error = f"connector.yaml not found in {connector_path}"

    metadata = config.openapi_spec.info.x_airbyte_qualification if config is not None and config.openapi_spec is not None else None
    claimed_status = metadata.status if metadata is not None else QualificationStatus.UNVERIFIED
    if config is None and connector_yaml.exists():
        claimed_status = _claimed_status_from_raw_yaml(connector_yaml) or QualificationStatus.UNVERIFIED
    return config, metadata, connector_name, load_error, claimed_status


def _load_smoke_config(path: Path) -> dict[str, Any] | None:
    """Load smoke-test YAML, returning `None` when it is unavailable."""
    try:
        with path.open() as config_file:
            config = yaml.safe_load(config_file)
    except (OSError, yaml.YAMLError):
        return None
    return config if isinstance(config, dict) else None


def _get_connector_smoke_test_config(config: dict[str, Any] | None, connector_name: str) -> dict[str, Any] | None:
    """Return one connector's smoke-test configuration."""
    if config is None:
        return None
    connectors = config.get("connectors")
    if not isinstance(connectors, list):
        return None
    return next(
        (connector for connector in connectors if isinstance(connector, dict) and connector.get("name") == connector_name),
        None,
    )


def _smoke_cases_for_operation(
    smoke_connector: dict[str, Any] | None,
    entity: str,
    action: str,
) -> list[dict[str, Any]]:
    """Return non-skipped smoke cases for one operation."""
    if smoke_connector is None:
        return []
    cases = smoke_connector.get("test_cases")
    if not isinstance(cases, list):
        return []
    return [
        case
        for case in cases
        if isinstance(case, dict) and case.get("entity") == entity and case.get("action") == action and not case.get("skip", False)
    ]


def validate_connector_qualification(
    connector_dir: str | Path,
    smoke_test_config_path: str | Path | None = None,
    smoke_results_path: str | Path | None = None,
    progress_callback: Callable[[str], None] | None = None,
) -> QualificationResult:
    """Evaluate qualification criteria for a connector directory."""

    def _step(message: str) -> None:
        if progress_callback is not None:
            progress_callback(message)

    _step("Loading connector model")
    connector_path = Path(connector_dir)
    connector_yaml = connector_path / "connector.yaml"
    config, metadata, connector_name, load_error, claimed_status = _load_connector_claim(connector_path, connector_yaml)
    bypass_reasons: dict[str, str] = {}
    invalid_bypasses: list[str] = []
    if metadata is not None:
        for bypass in metadata.bypassed_criteria:
            if bypass.criterion in QUALIFICATION_CRITERION_IDS:
                bypass_reasons[bypass.criterion] = bypass.reason
            else:
                invalid_bypasses.append(bypass.criterion)

    readiness = validate_connector_readiness(connector_path, progress_callback=progress_callback)
    readiness_summary = readiness.get("summary", {})
    readiness_warnings = readiness.get("readiness_warnings", [])
    all_warnings: list[str] = [str(warning) for warning in readiness_warnings]
    for operation_result in readiness.get("validation_results", []):
        all_warnings.extend(str(warning) for warning in operation_result.get("warnings", []))
        for cassette_validation in operation_result.get("schema_validation", []):
            all_warnings.extend(str(warning) for warning in cassette_validation.get("warnings", []))
    for section in ("replication_validation", "cache_validation", "auth_scheme_validation"):
        all_warnings.extend(str(warning) for warning in (readiness.get(section) or {}).get("warnings", []))
    _step("C14: write action coverage")
    _step("C15: untested-operation budget")
    _step("C16: smoke suite wiring")
    cassettes_dir = connector_path / "tests" / "cassettes"
    cassette_map = build_cassette_map(cassettes_dir)
    smoke_path = Path(smoke_test_config_path) if smoke_test_config_path else connector_path.parent.parent / "smoke-tests" / "test-config.yaml"
    smoke_connector = _get_connector_smoke_test_config(_load_smoke_config(smoke_path), connector_name)

    operations: list[tuple[str, str]] = []
    write_operations: list[tuple[str, str]] = []
    untested_operations: list[tuple[str, str]] = []
    missing_untested_operation_reasons: list[str] = []
    if config is not None:
        for entity in config.entities:
            for action in entity.actions:
                action_value = action.value
                operation = (entity.name, action_value)
                operations.append(operation)
                endpoint = entity.endpoints[action]
                if endpoint.untested:
                    untested_operations.append(operation)
                    if not endpoint.untested_reason or not endpoint.untested_reason.strip():
                        missing_untested_operation_reasons.append(f"{entity.name}.{action_value}")
                if action_value in WRITE_ACTIONS:
                    write_operations.append(operation)

    _step("C8: golden-questions report")
    _step("C9: report freshness")
    _step("C10: golden-questions pass rate")
    _step("C11: declared questions run")
    _step("C12: entity/action coverage")
    report = GoldenQuestionsReport.from_raw(load_golden_questions_report(connector_path))
    report_hash = report.freshness_hash if report else None
    current_hash = None
    if report_hash and connector_yaml.exists():
        try:
            current_hash = compute_golden_questions_hash(connector_yaml)
        except (OSError, ValueError, yaml.YAMLError):
            current_hash = None

    direct_questions: list[str] = []
    if config is not None and config.openapi_spec is not None:
        example_questions = config.openapi_spec.info.x_airbyte_example_questions
        if example_questions is not None:
            direct_questions = list(example_questions.direct)
    covered_pair_count = len(report.coverage.entity_action_pairs) if report else 0
    operation_count = len(operations)
    gq_rate = report.summary.success_rate if report else None
    untested_ratio = len(untested_operations) / operation_count if operation_count else 0.0
    warning_count = readiness_summary.get("total_warnings", len(readiness_warnings))

    auth_options = list(config.auth.options or []) if config is not None else []
    auth_coverage, _ = build_auth_scheme_coverage(cassettes_dir, auth_options)
    covered_schemes = {scheme for scheme in auth_coverage if scheme is not None}
    declared_schemes = set()
    untested_schemes: list[str] = []
    if config is not None and config.openapi_spec is not None and config.openapi_spec.components is not None:
        declared_schemes = set(config.openapi_spec.components.security_schemes)
        for scheme_name, scheme in config.openapi_spec.components.security_schemes.items():
            if scheme.x_airbyte_untested:
                untested_schemes.append(scheme_name)
    if config is not None and config.auth.is_multi_auth():
        missing_schemes = sorted(declared_schemes - covered_schemes)
    else:
        # Single-auth cassettes may record their scheme either explicitly by
        # name or in the unnamed bucket; both count as coverage.
        single_auth_covered = bool(auth_coverage.get(None)) or bool(declared_schemes & covered_schemes)
        missing_schemes = [] if single_auth_covered else sorted(declared_schemes)
    auth_passed = not missing_schemes and not untested_schemes

    smoke_write_missing = [
        f"{entity}.{action}"
        for entity, action in write_operations
        if not cassette_map.get((entity, action)) or not _smoke_cases_for_operation(smoke_connector, entity, action)
    ]
    active_auth_configs = [auth for auth in (smoke_connector or {}).get("auth_configs", []) if isinstance(auth, dict) and not auth.get("skip", False)]
    has_smoke_case = any(isinstance(case, dict) and not case.get("skip", False) for case in (smoke_connector or {}).get("test_cases", []))
    live_smoke_result = _load_live_smoke_result(
        Path(smoke_results_path) if smoke_results_path else None,
        connector_name,
    )
    c17_passed, c17_evaluated, c17_observed, c17_detail = _live_smoke_outcome(live_smoke_result)

    undeclared_warnings = [warning for warning in all_warnings if "undeclared" in warning.lower()]
    info = config.openapi_spec.info if config is not None and config.openapi_spec is not None else None
    direct_only = info is not None and info.x_airbyte_runtime_mode is RuntimeMode.DIRECT_ONLY
    context_store_justification = bool(info and (info.x_airbyte_context_store or info.x_airbyte_skip_context_store))
    replication_errors = (readiness.get("replication_validation") or {}).get("errors", [])

    _step("C17: live smoke result")
    c1_passed = load_error is None and readiness_summary.get("operations_missing_cassettes") == 0
    c2_passed = load_error is None and readiness_summary.get("cassettes_invalid") == 0
    c3_passed = not undeclared_warnings
    c4_passed = direct_only or context_store_justification
    c5_passed = not replication_errors
    c6_passed = warning_count <= MAX_READINESS_WARNING_COUNT
    c8_passed = report is not None
    c9_passed = report_hash is not None and current_hash is not None and report_hash == current_hash
    c10_passed = isinstance(gq_rate, (int, float)) and gq_rate >= MIN_GOLDEN_QUESTIONS_SUCCESS_RATE
    c11_passed = report is not None and report.summary.total_questions == len(direct_questions)
    c12_passed = bool(operation_count) and covered_pair_count / operation_count >= MIN_GOLDEN_QUESTIONS_ENTITY_COVERAGE
    c14_passed = not write_operations or not smoke_write_missing
    c15_passed = bool(operation_count) and untested_ratio <= MAX_UNTESTED_OPERATION_RATIO and not missing_untested_operation_reasons
    if c15_passed:
        c15_detail = "Untested-operation ratio and marker reasons meet the threshold."
    elif missing_untested_operation_reasons:
        c15_detail = f"Untested markers lack reasons: {missing_untested_operation_reasons}."
    else:
        c15_detail = f"Untested-operation ratio {untested_ratio:.2f} exceeds the budget."
    c16_passed = smoke_connector is not None and bool(active_auth_configs) and has_smoke_case

    criteria = [
        _build_criterion_outcome(
            "C1",
            "Every tested operation has a cassette",
            "gate",
            c1_passed,
            {
                "missing": readiness_summary.get("operations_missing_cassettes"),
                "covered": readiness_summary.get("operations_with_cassettes"),
                "total_operations": readiness_summary.get("total_operations"),
            },
            {"missing": 0},
            load_error or ("No tested operations are missing cassettes." if c1_passed else "One or more tested operations are missing cassettes."),
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C2",
            "Cassette responses validate against declared schemas",
            "gate",
            c2_passed,
            {
                "invalid": readiness_summary.get("cassettes_invalid"),
                "valid": readiness_summary.get("cassettes_valid"),
                "total_cassettes": readiness_summary.get("total_cassettes"),
            },
            {"invalid": 0},
            "All cassette responses validate." if c2_passed else "Invalid cassette responses were found.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C3",
            "No undeclared response fields",
            "warn",
            c3_passed,
            undeclared_warnings,
            0,
            "No undeclared-field warnings were reported." if c3_passed else "Undeclared response fields were reported.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C4",
            "Context store declared or justified",
            "gate",
            c4_passed,
            {"direct_only": direct_only, "justified": context_store_justification},
            "present except for direct_only",
            "Context store is not required for direct_only connectors."
            if direct_only
            else ("Context store is declared or justified." if c4_passed else "Context store declaration or justification is missing."),
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C5",
            "Replication compatibility annotated",
            "gate",
            c5_passed,
            replication_errors,
            0,
            "Replication validation has no errors." if c5_passed else "Replication validation reported errors.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C6",
            "Static-validation warning budget",
            "warn",
            c6_passed,
            warning_count,
            f"<= {MAX_READINESS_WARNING_COUNT}",
            "Warning count is within the budget." if c6_passed else "Warning count exceeds the budget.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C7",
            "Every declared auth scheme is exercised by a cassette",
            "gate",
            auth_passed,
            {"missing": missing_schemes, "untested": untested_schemes, "declared": sorted(declared_schemes)},
            {"missing": 0, "untested": 0},
            "All declared auth schemes have cassette coverage."
            if auth_passed
            else f"Missing schemes: {missing_schemes}; untested schemes: {untested_schemes}.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C8",
            "Golden-questions report exists",
            "gate",
            c8_passed,
            c8_passed,
            True,
            "Report is present." if c8_passed else "Report file is absent or malformed.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C9",
            "Golden-questions report is non-stale",
            "gate",
            c9_passed,
            {"report_hash": report_hash, "current_hash": current_hash},
            "equal",
            "Freshness hash matches connector.yaml." if c9_passed else "Freshness hash is absent, unavailable, or stale.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C10",
            "Golden-questions pass rate",
            "gate",
            c10_passed,
            gq_rate,
            f">= {MIN_GOLDEN_QUESTIONS_SUCCESS_RATE}",
            "Pass rate meets the qualification threshold." if c10_passed else "Pass rate is missing or below the qualification threshold.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C11",
            "Every declared question was actually run",
            "gate",
            c11_passed,
            report.summary.total_questions if report else None,
            len(direct_questions),
            "Report total matches declared direct questions." if c11_passed else "Report total does not match declared direct questions.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C12",
            "Entity/action coverage of the run",
            "warn",
            c12_passed,
            {
                "ratio": covered_pair_count / operation_count if operation_count else 0.0,
                "covered_pairs": covered_pair_count,
                "total_operations": operation_count,
            },
            f">= {MIN_GOLDEN_QUESTIONS_ENTITY_COVERAGE}",
            "Entity/action coverage meets the warning threshold." if c12_passed else "Entity/action coverage is below the warning threshold.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C14",
            "Every write action has a cassette and a smoke-test case",
            "gate",
            c14_passed,
            {"uncovered": smoke_write_missing, "total_write_actions": len(write_operations)},
            "all covered",
            f"All {len(write_operations)} declared write actions have cassettes and smoke cases."
            if c14_passed
            else f"Uncovered write actions: {smoke_write_missing}.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C15",
            "Untested-operation budget",
            "gate",
            c15_passed,
            {
                "ratio": untested_ratio,
                "untested_operations": len(untested_operations),
                "total_operations": operation_count,
                "missing_reasons": missing_untested_operation_reasons,
            },
            f"<= {MAX_UNTESTED_OPERATION_RATIO} and every marker has a reason",
            c15_detail,
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C16",
            "Wired into the smoke suite",
            "gate",
            c16_passed,
            {"connector": smoke_connector is not None, "active_auth_configs": len(active_auth_configs), "non_skipped_cases": has_smoke_case},
            "entry with ≥1 non-skipped auth config and ≥1 non-skipped test case",
            "Smoke-test entry has active auth configuration and non-skipped cases."
            if c16_passed
            else f"Smoke-test config is missing or has no active auth/test coverage at {smoke_path}.",
            bypass_reasons,
        ),
        _build_criterion_outcome(
            "C17",
            "Live smoke test passes",
            "gate",
            c17_passed,
            c17_observed,
            "pass",
            c17_detail,
            bypass_reasons,
            evaluated=c17_evaluated,
        ),
    ]
    unevaluated_criteria = [criterion.id for criterion in criteria if not criterion.evaluated]
    qualified = not invalid_bypasses and all(criterion.passed for criterion in criteria if criterion.kind == "gate" and criterion.evaluated)
    return QualificationResult(
        connector_name=connector_name,
        claimed_status=claimed_status,
        qualified=qualified,
        load_error=load_error,
        criteria=criteria,
        bypasses_applied=sorted(bypass_reasons),
        invalid_bypasses=invalid_bypasses,
        unevaluated_criteria=unevaluated_criteria,
        readiness_warnings=all_warnings,
    )
