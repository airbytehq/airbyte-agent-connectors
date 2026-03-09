"""Telemetry event models."""

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class BaseEvent:
    """Base class for all telemetry events."""

    timestamp: datetime
    session_id: str
    user_id: str
    execution_context: str
    is_internal_user: bool = field(default=False, kw_only=True)

    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary with ISO formatted timestamp."""
        data = asdict(self)
        data["timestamp"] = self.timestamp.isoformat()
        return data


@dataclass
class ConnectorInitEvent(BaseEvent):
    """Connector initialization event."""

    connector_name: str
    python_version: str
    os_name: str
    os_version: str
    public_ip: str | None = None
    connector_version: str | None = None


@dataclass
class OperationEvent(BaseEvent):
    """API operation event."""

    connector_name: str
    entity: str
    action: str
    timing_ms: float
    public_ip: str | None = None
    status_code: int | None = None
    error_type: str | None = None


@dataclass
class SessionEndEvent(BaseEvent):
    """Session end event."""

    connector_name: str
    duration_seconds: float
    operation_count: int
    success_count: int
    failure_count: int
    public_ip: str | None = None
