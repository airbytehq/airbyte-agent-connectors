"""Models for connector validation."""

from typing import NamedTuple


class ValidationResult(NamedTuple):
    """Result of a validation check.

    Attributes:
        is_valid: Whether the validation passed
        errors: List of error messages (validation failures)
        warnings: List of warning messages (non-blocking issues)
    """

    is_valid: bool
    errors: list[str]
    warnings: list[str]
