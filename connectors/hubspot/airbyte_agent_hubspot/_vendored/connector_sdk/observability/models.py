"""Shared operation metadata models."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class OperationMetadata:
    """Shared operation metadata."""

    entity: str
    action: str
    timestamp: datetime
    timing_ms: Optional[float] = None
    status_code: Optional[int] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    params: Optional[Dict[str, Any]] = None
