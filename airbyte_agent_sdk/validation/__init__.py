"""Connector validation utilities.

This module provides validation for connector definitions, including:
- Readiness validation (cassettes, schemas, auth coverage)
- Replication compatibility validation (Airbyte registry mappings)
- Cache schema validation (x-airbyte-context-store vs manifest)
- Connector overview (structured status reporting)
"""

from airbyte_agent_sdk.validation.cache import validate_cache_against_manifest
from airbyte_agent_sdk.validation.models import ValidationResult
from airbyte_agent_sdk.validation.overview import (
    compute_golden_questions_hash,
    diff_overviews,
    format_overview_as_markdown,
    get_base_overview,
    get_connector_overview,
    load_golden_questions_report,
)
from airbyte_agent_sdk.validation.qualification import (
    CriterionOutcome,
    QualificationResult,
    validate_connector_qualification,
)
from airbyte_agent_sdk.validation.readiness import validate_connector_readiness
from airbyte_agent_sdk.validation.replication import (
    fetch_airbyte_manifest,
    fetch_airbyte_registry_metadata,
    validate_replication_compatibility,
)

__all__ = [
    "validate_cache_against_manifest",
    "QualificationResult",
    "CriterionOutcome",
    "validate_connector_qualification",
    "ValidationResult",
    "compute_golden_questions_hash",
    "fetch_airbyte_manifest",
    "fetch_airbyte_registry_metadata",
    "diff_overviews",
    "format_overview_as_markdown",
    "get_base_overview",
    "get_connector_overview",
    "load_golden_questions_report",
    "validate_connector_readiness",
    "validate_replication_compatibility",
]
