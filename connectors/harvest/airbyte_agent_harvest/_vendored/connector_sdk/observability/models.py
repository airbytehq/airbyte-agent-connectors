"""Shared operation metadata models."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


@dataclass
class OperationMetadata:
    """Shared operation metadata."""

    entity: str
    action: str
    timestamp: datetime
    timing_ms: float | None = None
    status_code: int | None = None
    error_type: str | None = None
    error_message: str | None = None
    params: Dict[str, Any] | None = None
