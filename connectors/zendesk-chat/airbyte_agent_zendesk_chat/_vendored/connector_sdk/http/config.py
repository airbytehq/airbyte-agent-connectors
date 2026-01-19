"""Configuration classes for HTTP clients."""

from __future__ import annotations

from dataclasses import dataclass

from ..constants import (
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_MAX_CONNECTIONS,
    DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
    DEFAULT_POOL_TIMEOUT,
    DEFAULT_READ_TIMEOUT,
    DEFAULT_WRITE_TIMEOUT,
)


@dataclass
class ConnectionLimits:
    """Configuration for HTTP connection pooling limits.

    This replaces httpx.Limits and provides a client-agnostic way to configure
    connection pooling behavior.
    """

    max_connections: int = DEFAULT_MAX_CONNECTIONS
    """Maximum number of concurrent connections to allow."""

    max_keepalive_connections: int = DEFAULT_MAX_KEEPALIVE_CONNECTIONS
    """Maximum number of connections to keep alive in the pool."""

    def __post_init__(self) -> None:
        """Validate configuration values."""
        if self.max_connections < 1:
            raise ValueError("max_connections must be at least 1")
        if self.max_keepalive_connections < 0:
            raise ValueError("max_keepalive_connections must be non-negative")
        if self.max_keepalive_connections > self.max_connections:
            raise ValueError("max_keepalive_connections cannot exceed max_connections")


@dataclass
class TimeoutConfig:
    """Configuration for HTTP request timeouts.

    This replaces httpx.Timeout and provides a client-agnostic way to configure
    timeout behavior for different phases of the HTTP request.
    """

    connect: float | None = DEFAULT_CONNECT_TIMEOUT
    """Timeout for establishing a connection (seconds). None means no timeout."""

    read: float | None = DEFAULT_READ_TIMEOUT
    """Timeout for reading response data (seconds). None means no timeout."""

    write: float | None = DEFAULT_WRITE_TIMEOUT
    """Timeout for writing request data (seconds). None means no timeout."""

    pool: float | None = DEFAULT_POOL_TIMEOUT
    """Timeout for acquiring a connection from the pool (seconds). None means no timeout."""

    def __post_init__(self) -> None:
        """Validate configuration values."""
        for name, value in [
            ("connect", self.connect),
            ("read", self.read),
            ("write", self.write),
            ("pool", self.pool),
        ]:
            if value is not None and value <= 0:
                raise ValueError(f"{name} timeout must be positive or None")


@dataclass
class ClientConfig:
    """Overall configuration for an HTTP client.

    This provides a complete, client-agnostic configuration for HTTP clients
    that can be mapped to any underlying HTTP client implementation.
    """

    timeout: TimeoutConfig | None = None
    """Timeout configuration. If None, uses default timeouts."""

    limits: ConnectionLimits | None = None
    """Connection pooling limits. If None, uses default limits."""

    base_url: str | None = None
    """Optional base URL to prepend to all requests."""

    follow_redirects: bool = True
    """Whether to automatically follow HTTP redirects."""

    def __post_init__(self) -> None:
        """Set default values for None fields."""
        if self.timeout is None:
            self.timeout = TimeoutConfig()
        if self.limits is None:
            self.limits = ConnectionLimits()
