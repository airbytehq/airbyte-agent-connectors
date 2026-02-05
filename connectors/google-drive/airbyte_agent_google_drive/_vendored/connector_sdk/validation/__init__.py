"""Connector validation utilities.

This module provides validation for connector definitions, including:
- Readiness validation (cassettes, schemas, auth coverage)
- Replication compatibility validation (Airbyte registry mappings)
"""

from .models import ValidationResult
from .readiness import validate_connector_readiness
from .replication import (
    fetch_airbyte_manifest,
    fetch_airbyte_registry_metadata,
    validate_replication_compatibility,
)

__all__ = [
    "ValidationResult",
    "fetch_airbyte_manifest",
    "fetch_airbyte_registry_metadata",
    "validate_connector_readiness",
    "validate_replication_compatibility",
]
