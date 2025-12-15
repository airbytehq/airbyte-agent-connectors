"""Anonymous telemetry tracker using Segment."""

import logging
import platform
import sys
from datetime import datetime
from typing import Optional

from ..observability import ObservabilitySession

from .config import SEGMENT_WRITE_KEY, TelemetryConfig, TelemetryMode
from .events import ConnectorInitEvent, OperationEvent, SessionEndEvent

logger = logging.getLogger(__name__)


class SegmentTracker:
    """Anonymous telemetry tracker using Segment."""

    def __init__(
        self,
        session: ObservabilitySession,
        mode: Optional[TelemetryMode] = None,
    ):
        self.session = session
        self.mode = mode or TelemetryConfig.get_mode()
        self.success_count = 0
        self.failure_count = 0
        self.enabled = TelemetryConfig.is_enabled()
        self._analytics = None

        if self.enabled:
            try:
                import segment.analytics as analytics

                analytics.write_key = SEGMENT_WRITE_KEY
                self._analytics = analytics
                self._log_startup_message()
            except ImportError:
                logger.warning("Telemetry disabled: segment-analytics-python not installed")
                self.enabled = False

    def _log_startup_message(self):
        """Log message when telemetry is enabled."""
        logger.info(f"Anonymous telemetry enabled (mode: {self.mode.value})")
        logger.info("To opt-out: export AIRBYTE_TELEMETRY_MODE=disabled")

    def track_connector_init(
        self,
        connector_version: Optional[str] = None,
    ) -> None:
        """Track connector initialization."""
        if not self.enabled or not self._analytics:
            return

        try:
            event = ConnectorInitEvent(
                timestamp=datetime.utcnow(),
                session_id=self.session.session_id,
                user_id=self.session.user_id,
                execution_context=self.session.execution_context,
                public_ip=self.session.public_ip,
                connector_name=self.session.connector_name,
                connector_version=connector_version,
                python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
                os_name=platform.system(),
                os_version=platform.release(),
            )

            self._analytics.track(
                user_id=self.session.user_id,
                anonymous_id=event.session_id,
                event="Connector Initialized",
                properties=event.to_dict(),
            )
        except Exception as e:
            # Never fail on tracking errors
            logger.error(f"Telemetry error: {e}")

    def track_operation(
        self,
        entity: str,
        action: str,
        status_code: Optional[int],
        timing_ms: float,
        error_type: Optional[str] = None,
    ) -> None:
        """Track API operation."""
        # Always track success/failure counts (useful even when tracking is disabled)
        if status_code and 200 <= status_code < 300:
            self.success_count += 1
        else:
            self.failure_count += 1

        if not self.enabled or not self._analytics:
            return

        try:
            event = OperationEvent(
                timestamp=datetime.utcnow(),
                session_id=self.session.session_id,
                user_id=self.session.user_id,
                execution_context=self.session.execution_context,
                public_ip=self.session.public_ip,
                connector_name=self.session.connector_name,
                entity=entity,
                action=action,
                status_code=status_code,
                timing_ms=timing_ms,
                error_type=error_type,
            )

            self._analytics.track(
                user_id=self.session.user_id,
                anonymous_id=event.session_id,
                event="Operation Executed",
                properties=event.to_dict(),
            )
        except Exception as e:
            logger.error(f"Telemetry error: {e}")

    def track_session_end(self) -> None:
        """Track session end."""
        if not self.enabled or not self._analytics:
            return

        try:
            event = SessionEndEvent(
                timestamp=datetime.utcnow(),
                session_id=self.session.session_id,
                user_id=self.session.user_id,
                execution_context=self.session.execution_context,
                public_ip=self.session.public_ip,
                connector_name=self.session.connector_name,
                duration_seconds=self.session.duration_seconds(),
                operation_count=self.session.operation_count,
                success_count=self.success_count,
                failure_count=self.failure_count,
            )

            self._analytics.track(
                user_id=self.session.user_id,
                anonymous_id=event.session_id,
                event="Session Ended",
                properties=event.to_dict(),
            )

            # Ensure events are sent before shutdown
            self._analytics.flush()
        except Exception as e:
            logger.error(f"Telemetry error: {e}")
