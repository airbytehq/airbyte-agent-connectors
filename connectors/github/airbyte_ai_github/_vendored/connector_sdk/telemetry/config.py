"""Telemetry configuration from environment variables."""

import os
from enum import Enum

# Hardcoded Segment write key for Airbyte telemetry
SEGMENT_WRITE_KEY = "zHeE6sffXQCENrvPHzrhPUdXj7v7gt2u"


class TelemetryMode(Enum):
    """Telemetry tracking modes."""

    BASIC = "basic"
    DISABLED = "disabled"


class TelemetryConfig:
    """Telemetry configuration from environment variables."""

    @staticmethod
    def get_mode() -> TelemetryMode:
        """Get telemetry mode from environment variable."""
        mode_str = os.getenv("AIRBYTE_TELEMETRY_MODE", "basic").lower()
        try:
            return TelemetryMode(mode_str)
        except ValueError:
            return TelemetryMode.BASIC

    @staticmethod
    def is_enabled() -> bool:
        """Telemetry is enabled if mode is not disabled."""
        return TelemetryConfig.get_mode() != TelemetryMode.DISABLED
