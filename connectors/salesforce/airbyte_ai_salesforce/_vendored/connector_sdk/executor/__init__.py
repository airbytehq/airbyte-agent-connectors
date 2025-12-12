"""Executor implementations for connector operations."""

from .models import (
    ExecutionConfig,
    ExecutionResult,
    ExecutorProtocol,
    ExecutorError,
    EntityNotFoundError,
    ActionNotSupportedError,
    MissingParameterError,
    InvalidParameterError,
)
from .local_executor import LocalExecutor
from .hosted_executor import HostedExecutor

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
