"""Data models and protocols for executor implementations."""

from __future__ import annotations

from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from dotenv import load_dotenv

# Load environment variables from .env file
_env_path = Path(__file__).parent.parent.parent / ".env"
if _env_path.exists():
    load_dotenv(dotenv_path=_env_path)


@dataclass
class ExecutionConfig:
    """Configuration for connector execution.

    Used by both LocalExecutor and HostedExecutor to specify the operation to execute.
    Executor-specific configuration (like api_url for HostedExecutor) is passed to
    the executor's constructor instead of being part of the execution config.

    Args:
        entity: Entity name (e.g., "customers", "invoices")
        action: Operation action (e.g., "list", "get", "create")
        params: Optional parameters for the operation
            - For GET: {"id": "cus_123"}
            - For LIST: {"limit": 10}
            - For CREATE: {"email": "...", "name": "..."}

    Example:
        config = ExecutionConfig(
            entity="customers",
            action="list",
            params={"limit": 10}
        )
    """

    entity: str
    action: str
    params: dict[str, Any] | None = field(default=None, kw_only=True)


@dataclass
class StandardExecuteResult:
    """Result from standard operation handlers (GET, LIST, CREATE, UPDATE, DELETE, etc.).

    This is returned by _StandardOperationHandler to provide type-safe data and metadata
    returns instead of using tuples. Download operations continue to return AsyncIterator[bytes]
    directly for simplicity.

    Args:
        data: Response data from the operation
        metadata: Optional metadata extracted from response (e.g., pagination info)

    Example:
        result = StandardExecuteResult(
            data={"id": "1", "name": "Test"},
            metadata={"pagination": {"cursor": "next123", "totalRecords": 100}}
        )
    """

    data: dict[str, Any]
    metadata: dict[str, Any] | None = None


@dataclass
class ExecutionResult:
    """Result of a connector execution.

    This is returned by all executor implementations. It provides a consistent
    interface for handling both successful executions and execution failures.

    Args:
        success: True if execution completed successfully, False if it failed
        data: Response data from the execution
            - dict[str, Any] for standard operations (GET, LIST, CREATE, etc.)
            - AsyncIterator[bytes] for download operations (streaming file content)
        error: Error message if success=False, None otherwise
        meta: Optional metadata extracted from response (e.g., pagination info)

    Example (Success - Standard):
        result = ExecutionResult(
            success=True,
            data=[{"id": "1"}, {"id": "2"}],
            error=None,
            meta={"pagination": {"cursor": "next123", "totalRecords": 100}}
        )

    Example (Success - Download):
        result = ExecutionResult(
            success=True,
            data=async_iterator_of_bytes,
            error=None
        )

    Example (Failure):
        result = ExecutionResult(
            success=False,
            data={},
            error="Entity 'invalid' not found",
            meta=None
        )
    """

    success: bool
    data: dict[str, Any] | AsyncIterator[bytes]
    error: str | None = None
    meta: dict[str, Any] | None = None


# ============================================================================
# Executor Protocol
# ============================================================================


@runtime_checkable
class ExecutorProtocol(Protocol):
    """Protocol for connector execution.

    This defines the interface that both LocalExecutor and HostedExecutor implement.
    Uses structural typing (Protocol) - any class with a matching execute() method
    satisfies this protocol, regardless of inheritance.

    The @runtime_checkable decorator allows isinstance() checks at runtime.

    Example:
        def run_connector(executor: ExecutorProtocol, config: ExecutionConfig):
            result = await executor.execute(config)
            if result.success:
                print(f"Success: {result.data}")
            else:
                print(f"Error: {result.error}")
    """

    async def execute(self, config: ExecutionConfig) -> ExecutionResult:
        """Execute connector with given configuration.

        Args:
            config: Configuration for execution (entity, action, params)

        Returns:
            ExecutionResult with success status, data, and optional error message

        Raises:
            Infrastructure exceptions (network errors, HTTP errors, auth failures)
            These are exceptional cases where the system cannot complete the request.

            Execution errors (entity not found, invalid operation) are returned
            in ExecutionResult.error instead of being raised.
        """
        ...


# ============================================================================
# Executor Exceptions
# ============================================================================


class ExecutorError(Exception):
    """Base exception for executor errors."""

    pass


class EntityNotFoundError(ExecutorError):
    """Raised when an entity is not found in the connector."""

    pass


class ActionNotSupportedError(ExecutorError):
    """Raised when an action is not supported for an entity."""

    pass


class MissingParameterError(ExecutorError):
    """Raised when a required parameter is missing."""

    pass


class InvalidParameterError(ExecutorError):
    """Raised when a parameter has an invalid type or value."""

    pass
