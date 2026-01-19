"""HTTP abstraction layer for the Airbyte SDK.

This package provides a client-agnostic HTTP interface that allows the SDK to work
with different HTTP client implementations (httpx, aiohttp, etc.) while maintaining
a consistent API.
"""

from .config import ClientConfig, ConnectionLimits, TimeoutConfig
from .exceptions import (
    AuthenticationError,
    HTTPClientError,
    HTTPStatusError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)
from .protocols import HTTPClientProtocol, HTTPResponseProtocol
from .response import HTTPResponse

__all__ = [
    # Configuration
    "ClientConfig",
    "ConnectionLimits",
    "TimeoutConfig",
    # Protocols
    "HTTPClientProtocol",
    "HTTPResponseProtocol",
    # Response
    "HTTPResponse",
    # Exceptions
    "HTTPClientError",
    "HTTPStatusError",
    "AuthenticationError",
    "RateLimitError",
    "NetworkError",
    "TimeoutError",
]
