"""Connector validation utilities.

This module provides validation for connector definitions, including:
- Readiness validation (cassettes, schemas, auth coverage)
- Replication compatibility validation (Airbyte registry mappings)
- Cache schema validation (x-airbyte-cache vs manifest)
- Connector overview (structured status reporting)
"""

from .cache import validate_cache_against_manifest
from .models import ValidationResult
from .overview import (
    compute_golden_questions_hash,
    diff_overviews,
    format_overview_as_markdown,
    get_base_overview,
    get_connector_overview,
)
from .readiness import validate_connector_readiness
from .replication import (
    fetch_airbyte_manifest,
    fetch_airbyte_registry_metadata,
    validate_replication_compatibility,
)

__all__ = [
    "validate_cache_against_manifest",
    "ValidationResult",
    "compute_golden_questions_hash",
    "fetch_airbyte_manifest",
    "fetch_airbyte_registry_metadata",
    "diff_overviews",
    "format_overview_as_markdown",
    "get_base_overview",
    "get_connector_overview",
    "validate_connector_readiness",
    "validate_replication_compatibility",
]
