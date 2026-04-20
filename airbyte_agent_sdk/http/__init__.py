"""HTTP abstraction layer for the Airbyte SDK.

This package provides a client-agnostic HTTP interface that allows the SDK to work
with different HTTP client implementations (httpx, aiohttp, etc.) while maintaining
a consistent API.
"""

from airbyte_agent_sdk.http.config import ClientConfig, ConnectionLimits, TimeoutConfig
from airbyte_agent_sdk.http.exceptions import (
    AuthenticationError,
    ConnectorValidationError,
    HTTPClientError,
    HTTPStatusError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)
from airbyte_agent_sdk.http.protocols import HTTPClientProtocol, HTTPResponseProtocol
from airbyte_agent_sdk.http.response import HTTPResponse

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
    "ConnectorValidationError",
    "RateLimitError",
    "NetworkError",
    "TimeoutError",
]
