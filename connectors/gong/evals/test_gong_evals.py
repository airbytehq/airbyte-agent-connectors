"""Pytest runner for Gong connector evaluations.

This module runs the Gong business question evaluations using the connector_evals framework.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from connector_evals import run_connector_evals
from connector_evals.framework import run_assertions_in_report


EVALS_DIR = Path(__file__).parent
EVAL_CASES_PATH = EVALS_DIR / "eval_cases.yaml"
CASSETTE_DIR = EVALS_DIR / "eval_cassettes"
CONNECTOR_YAML_PATH = EVALS_DIR.parent / "airbyte_ai_gong" / "connector.yaml"


@pytest.mark.asyncio
@pytest.mark.evals
async def test_gong_business_questions(current_test_name: str) -> None:
    """Run all Gong business question evaluations.

    This test evaluates how well an LLM agent can answer business questions
    using the Gong connector tools. It tests both tool selection accuracy
    and response quality.
    """
    report = await run_connector_evals(
        connector_name="gong",
        eval_cases_path=EVAL_CASES_PATH,
        cassette_dir=CASSETTE_DIR,
        connector_yaml_path=CONNECTOR_YAML_PATH,
    )

    report.print(include_input=True, include_output=True, include_reasons=True)

    run_assertions_in_report(report)


@pytest.mark.asyncio
@pytest.mark.evals
async def test_gong_single_case_top_performers(current_test_name: str) -> None:
    """Run a single eval case for quick testing.

    This test runs only the top_performers_by_calls case for faster iteration
    during development.
    """
    report = await run_connector_evals(
        connector_name="gong",
        eval_cases_path=EVAL_CASES_PATH,
        cassette_dir=CASSETTE_DIR,
        connector_yaml_path=CONNECTOR_YAML_PATH,
        max_concurrency=1,
    )

    for case in report.cases:
        if case.name == "top_performers_by_calls":
            print(f"\n=== Case: {case.name} ===")
            print(f"Output: {case.output}")
            print(f"Scores: {case.scores}")
            print(f"Assertions: {case.assertions}")
            break
