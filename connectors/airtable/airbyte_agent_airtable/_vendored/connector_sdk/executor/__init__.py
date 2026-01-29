"""Executor implementations for connector operations."""

from .hosted_executor import HostedExecutor
from .local_executor import LocalExecutor
from .models import (
    ActionNotSupportedError,
    EntityNotFoundError,
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    ExecutorProtocol,
    InvalidParameterError,
    MissingParameterError,
)

__all__ = [
    # Config and Result types
    "ExecutionConfig",
    "ExecutionResult",
    # Protocol
    "ExecutorProtocol",
    # Executors
    "LocalExecutor",
    "HostedExecutor",
    # Exceptions
    "ExecutorError",
    "EntityNotFoundError",
    "ActionNotSupportedError",
    "MissingParameterError",
    "InvalidParameterError",
]
