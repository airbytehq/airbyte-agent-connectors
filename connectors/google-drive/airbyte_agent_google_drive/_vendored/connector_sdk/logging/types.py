"""Type definitions for request/response logging."""

import base64
from datetime import UTC, datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_serializer, field_validator


def _utc_now() -> datetime:
    """Get current UTC datetime (timezone-aware)."""
    return datetime.now(UTC)


def _encode_bytes(v: bytes) -> dict:
    """Encode bytes as base64 for JSON serialization."""
    return {"_binary": True, "_base64": base64.b64encode(v).decode("utf-8")}


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
    chunk_logs: List[bytes] = Field(
        default_factory=list,
        description="Captured chunks from streaming responses. " "Each chunk is logged when log_chunk_fetch() is called.",
    )

    @field_validator("chunk_logs", mode="before")
    @classmethod
    def decode_chunk_logs(cls, v: Any) -> List[bytes]:
        """Decode chunk_logs from JSON representation back to bytes."""
        if v is None or v == []:
            return []
        if isinstance(v, list):
            result = []
            for item in v:
                if isinstance(item, bytes):
                    result.append(item)
                elif isinstance(item, dict) and item.get("_binary"):
                    # Decode from {"_binary": True, "_base64": "..."} format
                    result.append(base64.b64decode(item["_base64"]))
                else:
                    result.append(item)
            return result
        return v

    @field_serializer("started_at")
    def serialize_datetime(self, value: datetime) -> str:
        return value.isoformat()

    @field_serializer("chunk_logs")
    def serialize_chunk_logs(self, value: List[bytes]) -> List[dict]:
        """Serialize bytes chunks as base64 for JSON."""
        return [_encode_bytes(chunk) for chunk in value]
