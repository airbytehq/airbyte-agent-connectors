"""Request/response logging implementation."""

import base64
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Optional, Set

from .types import LogSession, RequestLog

# Headers to redact for security
SENSITIVE_HEADERS: Set[str] = {
    "authorization",
    "bearer",
    "api-key",
    "x-api-key",
    "token",
    "secret",
    "password",
    "credential",
}


class RequestLogger:
    """Captures HTTP request/response interactions to a JSON file.

    Implements bounded logging with automatic rotation and flush-before-discard
    to prevent unbounded memory growth in long-running processes.
    """

    def __init__(
        self,
        log_file: Optional[str] = None,
        connector_name: Optional[str] = None,
        max_logs: Optional[int] = 10000,
    ):
        """
        Initialize the request logger.

        Args:
            log_file: Path to write logs. If None, generates timestamped filename.
            connector_name: Name of the connector being logged.
            max_logs: Maximum number of logs to keep in memory before rotation.
                Set to None for unlimited (not recommended for production).
                Defaults to 10000.
        """
        if log_file is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            log_file = f".logs/session_{timestamp}.json"

        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.session = LogSession(
            session_id=str(uuid.uuid4()),
            connector_name=connector_name,
            max_logs=max_logs,
        )
        self._active_requests: Dict[str, Dict[str, Any]] = {}
        # Store rotated logs that have been flushed from active buffer
        self._rotated_logs: list[RequestLog] = []

    def _redact_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Redact sensitive headers."""
        redacted = {}
        for key, value in headers.items():
            if any(sensitive in key.lower() for sensitive in SENSITIVE_HEADERS):
                redacted[key] = "[REDACTED]"
            else:
                redacted[key] = value
        return redacted

    def _rotate_logs_if_needed(self) -> None:
        """Rotate logs if max_logs limit is reached.

        Moves oldest logs to _rotated_logs before removing them from active buffer.
        This ensures logs are preserved for final save() without memory growth.
        """
        max_logs = self.session.max_logs
        if max_logs is None:
            # Unlimited logging, no rotation needed
            return

        current_count = len(self.session.logs)
        if current_count >= max_logs:
            # Calculate how many logs to rotate (keep buffer at ~90% to avoid thrashing)
            num_to_rotate = max(1, current_count - int(max_logs * 0.9))

            # Move oldest logs to rotated buffer
            rotated = self.session.logs[:num_to_rotate]
            self._rotated_logs.extend(rotated)

            # Remove rotated logs from active buffer
            self.session.logs = self.session.logs[num_to_rotate:]

    def log_request(
        self,
        method: str,
        url: str,
        path: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
    ) -> str:
        """
        Log the start of an HTTP request.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Full URL
            path: Request path
            headers: Request headers
            params: Query parameters
            body: Request body

        Returns:
            Request ID for correlating with response
        """
        request_id = str(uuid.uuid4())
        self._active_requests[request_id] = {
            "start_time": time.time(),
            "method": method,
            "url": url,
            "path": path,
            "headers": self._redact_headers(headers or {}),
            "params": params,
            "body": body,
        }
        return request_id

    def log_response(
        self,
        request_id: str,
        status_code: int,
        response_body: Optional[Any] = None,
    ) -> None:
        """
        Log a successful HTTP response.

        Args:
            request_id: ID returned from log_request
            status_code: HTTP status code
            response_body: Response body
        """
        if request_id not in self._active_requests:
            return

        request_data = self._active_requests.pop(request_id)
        timing_ms = (time.time() - request_data["start_time"]) * 1000

        # Convert bytes to base64 for JSON serialization
        serializable_body = response_body
        if isinstance(response_body, bytes):
            serializable_body = {
                "_binary": True,
                "_base64": base64.b64encode(response_body).decode("utf-8"),
            }

        log_entry = RequestLog(
            method=request_data["method"],
            url=request_data["url"],
            path=request_data["path"],
            headers=request_data["headers"],
            params=request_data["params"],
            body=request_data["body"],
            response_status=status_code,
            response_body=serializable_body,
            timing_ms=timing_ms,
        )

        self.session.logs.append(log_entry)
        self._rotate_logs_if_needed()

    def log_error(
        self,
        request_id: str,
        error: str,
        status_code: Optional[int] = None,
    ) -> None:
        """
        Log an HTTP request error.

        Args:
            request_id: ID returned from log_request
            error: Error message
            status_code: HTTP status code if available
        """
        if request_id not in self._active_requests:
            return

        request_data = self._active_requests.pop(request_id)
        timing_ms = (time.time() - request_data["start_time"]) * 1000

        log_entry = RequestLog(
            method=request_data["method"],
            url=request_data["url"],
            path=request_data["path"],
            headers=request_data["headers"],
            params=request_data["params"],
            body=request_data["body"],
            response_status=status_code,
            timing_ms=timing_ms,
            error=error,
        )

        self.session.logs.append(log_entry)
        self._rotate_logs_if_needed()

    def log_chunk_fetch(self, chunk: bytes) -> None:
        """Log a chunk from streaming response.

        Args:
            chunk: Binary chunk data from streaming response
        """
        self.session.chunk_logs.append(chunk)

    def save(self) -> None:
        """Write the current session to the log file.

        Includes both rotated logs and current active logs to ensure
        no data loss during bounded logging.
        """
        # Combine rotated logs with current logs for complete session
        all_logs = self._rotated_logs + self.session.logs

        # Create a temporary session with all logs for serialization
        session_data = self.session.model_dump(mode="json")
        session_data["logs"] = [log.model_dump(mode="json") for log in all_logs]

        with open(self.log_file, "w") as f:
            json.dump(session_data, f, indent=2, default=str)

    def close(self) -> None:
        """Finalize and save the logging session."""
        self.save()


class NullLogger:
    """No-op logger for when logging is disabled."""

    def log_request(self, *args, **kwargs) -> str:
        """No-op log_request."""
        return ""

    def log_response(self, *args, **kwargs) -> None:
        """No-op log_response."""
        pass

    def log_error(self, *args, **kwargs) -> None:
        """No-op log_error."""
        pass

    def log_chunk_fetch(self, chunk: bytes) -> None:
        """No-op chunk logging for production."""
        pass

    def save(self) -> None:
        """No-op save."""
        pass

    def close(self) -> None:
        """No-op close."""
        pass
