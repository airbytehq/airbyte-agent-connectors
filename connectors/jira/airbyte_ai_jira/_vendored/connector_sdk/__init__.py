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
from .config_loader import load_connector_config
from .constants import SDK_VERSION
from .exceptions import (
    AuthenticationError,
    HTTPClientError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)
from .executor import (
    ActionNotSupportedError,
    EntityNotFoundError,
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    ExecutorProtocol,
    HostedExecutor,
    InvalidParameterError,
    LocalExecutor,
    MissingParameterError,
)
from .http_client import HTTPClient
from .logging import LogSession, NullLogger, RequestLog, RequestLogger
from .performance import PerformanceMonitor, instrument
from .types import Action, AuthType, ConnectorConfig, EntityDefinition
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
