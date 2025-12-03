"""Telemetry event models."""

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class BaseEvent:
    """Base class for all telemetry events."""

    timestamp: datetime
    session_id: str
    user_id: str
    execution_context: str

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
    public_ip: Optional[str] = None
    connector_version: Optional[str] = None


@dataclass
class OperationEvent(BaseEvent):
    """API operation event."""

    connector_name: str
    entity: str
    action: str
    timing_ms: float
    public_ip: Optional[str] = None
    status_code: Optional[int] = None
    error_type: Optional[str] = None


@dataclass
class SessionEndEvent(BaseEvent):
    """Session end event."""

    connector_name: str
    duration_seconds: float
    operation_count: int
    success_count: int
    failure_count: int
    public_ip: Optional[str] = None
