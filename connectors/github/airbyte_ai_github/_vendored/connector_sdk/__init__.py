"""
Airbyte SDK - Async-first type-safe connector execution framework.

Provides:
- Async executor for all connectors
- Custom connector support
- Performance monitoring and instrumentation
- Connection pooling and concurrent execution
"""

from __future__ import annotations

from .auth_strategies import AuthStrategy
from .constants import SDK_VERSION
from .executor import (
    LocalExecutor,
    HostedExecutor,
    ExecutorProtocol,
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    EntityNotFoundError,
    ActionNotSupportedError,
    MissingParameterError,
    InvalidParameterError,
)
from .http_client import HTTPClient
from .types import ConnectorConfig, Action, AuthType, EntityDefinition
from .config_loader import load_connector_config
from .logging import RequestLogger, NullLogger, RequestLog, LogSession
from .performance import PerformanceMonitor, instrument
from .exceptions import (
    HTTPClientError,
    AuthenticationError,
    RateLimitError,
    NetworkError,
    TimeoutError,
)
from .utils import save_download

__version__ = SDK_VERSION

__all__ = [
    # All Executors
    "LocalExecutor",
    "HostedExecutor",
    "ExecutorProtocol",
    "HTTPClient",
    # Execution Config and Result Types
    "ExecutionConfig",
    "ExecutionResult",
    # Types
    "ConnectorConfig",
    "Action",
    "AuthType",
    "EntityDefinition",
    "load_connector_config",
    # Authentication
    "AuthStrategy",
    # Executor Exceptions
    "ExecutorError",
    "EntityNotFoundError",
    "ActionNotSupportedError",
    "MissingParameterError",
    "InvalidParameterError",
    # HTTP Exceptions
    "HTTPClientError",
    "AuthenticationError",
    "RateLimitError",
    "NetworkError",
    "TimeoutError",
    # Logging
    "RequestLogger",
    "NullLogger",
    "RequestLog",
    "LogSession",
    # Performance monitoring
    "PerformanceMonitor",
    "instrument",
    # Utilities
    "save_download",
]
