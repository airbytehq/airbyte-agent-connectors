"""
Constants used throughout the Airbyte SDK.

This module centralizes configuration defaults and commonly used values to improve
maintainability and consistency across the codebase.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

# ============================================================================
# HTTP Connection and Timeout Defaults
# ============================================================================

# Connection pooling limits
DEFAULT_MAX_CONNECTIONS = 100
"""Maximum number of concurrent HTTP connections to maintain in the pool."""

DEFAULT_MAX_KEEPALIVE_CONNECTIONS = 20
"""Maximum number of keepalive connections to maintain in the pool."""

# Timeout values (in seconds)
DEFAULT_CONNECT_TIMEOUT = 5.0
"""Default timeout for establishing a new connection (seconds)."""

DEFAULT_READ_TIMEOUT = 30.0
"""Default timeout for reading response data (seconds)."""

DEFAULT_WRITE_TIMEOUT = 30.0
"""Default timeout for writing request data (seconds)."""

DEFAULT_POOL_TIMEOUT = 5.0
"""Default timeout for acquiring a connection from the pool (seconds)."""

DEFAULT_REQUEST_TIMEOUT = 30.0
"""Default overall request timeout (seconds)."""

# ============================================================================
# OpenAPI Specification
# ============================================================================

OPENAPI_VERSION_PREFIX = "3.1."
"""Required OpenAPI version prefix. Only 3.1.x specifications are supported."""

OPENAPI_DEFAULT_VERSION = "1.0.0"
"""Default version string for connectors that don't specify a version."""

# ============================================================================
# Performance and Metrics
# ============================================================================

MILLISECONDS_PER_SECOND = 1000
"""Conversion factor from seconds to milliseconds."""

# ============================================================================
# Retry and Backoff Defaults
# ============================================================================

DEFAULT_INITIAL_DELAY_SECONDS = 1.0
"""Default initial delay for retry backoff (seconds)."""

DEFAULT_MAX_DELAY_SECONDS = 60.0
"""Default maximum delay for retry backoff (seconds)."""

# ============================================================================
# SDK Version
# ============================================================================

try:
    SDK_VERSION = version("connector-sdk")
except PackageNotFoundError:
    # Fallback for development when package isn't installed
    SDK_VERSION = "0.0.0-dev"
"""Current version of the Airbyte SDK."""

MINIMUM_PYTHON_VERSION = "3.9"
"""Minimum Python version required to run the SDK."""
