"""Connector Evals - A pydantic-evals based evaluation framework for testing connector quality.

This framework evaluates how well an LLM agent can answer business questions using connector tools.
"""

from __future__ import annotations

from connector_evals.cassette_loader import CassetteLoader
from connector_evals.evaluators import ConnectorToolsCalledEvaluator, LLMJudgeEvaluator
from connector_evals.framework import create_connector_agent, run_connector_evals

__all__ = [
    "create_connector_agent",
    "run_connector_evals",
    "ConnectorToolsCalledEvaluator",
    "LLMJudgeEvaluator",
    "CassetteLoader",
]
