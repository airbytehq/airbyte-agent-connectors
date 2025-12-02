"""Type definitions for request/response logging."""

from datetime import UTC, datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_serializer


def _utc_now() -> datetime:
    """Get current UTC datetime (timezone-aware)."""
    return datetime.now(UTC)


class RequestLog(BaseModel):
    """Captures a single HTTP request/response interaction."""

    model_config = ConfigDict()

    timestamp: datetime = Field(default_factory=_utc_now)
    method: str
    url: str
    path: str
    headers: Dict[str, str] = Field(default_factory=dict)
    params: Optional[Dict[str, Any]] = None
    body: Optional[Any] = None
    response_status: Optional[int] = None
    response_body: Optional[Any] = None
    timing_ms: Optional[float] = None
    error: Optional[str] = None

    @field_serializer("timestamp")
    def serialize_datetime(self, value: datetime) -> str:
        return value.isoformat()


class LogSession(BaseModel):
    """Collection of request logs with session metadata.

    When max_logs is set, the session will maintain a bounded buffer of recent logs.
    Older logs should be flushed to disk before being discarded (handled by RequestLogger).
    """

    model_config = ConfigDict()

    session_id: str
    started_at: datetime = Field(default_factory=_utc_now)
    connector_name: Optional[str] = None
    logs: List[RequestLog] = Field(default_factory=list)
    max_logs: Optional[int] = Field(
        default=10000,
        description="Maximum number of logs to keep in memory. "
        "When limit is reached, oldest logs should be flushed before removal. "
        "Set to None for unlimited (not recommended for production).",
    )

    @field_serializer("started_at")
    def serialize_datetime(self, value: datetime) -> str:
        return value.isoformat()
