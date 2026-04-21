"""Data models and protocols for executor implementations."""

from __future__ import annotations

from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from airbyte_agent_sdk.errors import AirbyteError
from airbyte_agent_sdk.types import Action


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


@dataclass
class ConnectorInfo:
    """A connector instance in a workspace."""

    id: str
    name: str
    connector_type: str | None = None
    created_at: str | None = None
    updated_at: str | None = None


@dataclass
class WorkflowInfo:
    """A workflow in a workspace."""

    id: str
    name: str
    workspace_id: str
    created_at: str | None = None
    updated_at: str | None = None


@dataclass
class AutomationInfo:
    """An automation attached to a workflow."""

    id: str
    workflow_id: str
    workspace_id: str
    enabled: bool
    trigger_type: str
    cron_expression: str | None = None
    timezone: str = "UTC"
    completion_webhook_url: str | None = None
    trigger_webhook_url: str | None = None
    created_at: str | None = None
    updated_at: str | None = None


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

    Concrete implementations accept two call forms:

    1. ``execute(config)`` -- pass an :class:`ExecutionConfig` object.
    2. ``execute(entity, action, *, params=None)`` -- shorthand string form.

    The Protocol signature uses the first form; the overloaded shorthand is
    defined on the concrete classes via ``@overload``.

    Example:
        def run_connector(executor: ExecutorProtocol, config: ExecutionConfig):
            result = await executor.execute(config)
            if result.success:
                print(f"Success: {result.data}")
            else:
                print(f"Error: {result.error}")

        # Shorthand (on concrete implementations):
        result = await executor.execute("customers", "list", params={"limit": 10})
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

    async def check(self) -> ExecutionResult:
        """Perform a health check to verify connectivity and credentials.

        Returns:
            ExecutionResult with data containing:
                - status: "healthy" or "unhealthy"
                - error: Error message if unhealthy
                - checked_entity: Entity used for the check
                - checked_action: Action used for the check
        """
        ...


# ============================================================================
# Executor Exceptions
# ============================================================================


# ============================================================================
# Check Operation Helpers (shared by LocalExecutor and HostedExecutor)
# ============================================================================


def has_required_params(endpoint: Any) -> bool:
    """Check if an endpoint has required parameters without defaults.

    An endpoint has required params if it has path params (e.g., /v1/customers/{id})
    or query params marked required with no default value and no `config_inject` rule
    that will auto-populate the value from connector config at runtime.
    """
    if endpoint.path_params:
        return True
    for schema in endpoint.query_params_schema.values():
        if schema.get("required") and schema.get("default") is None and not schema.get("config_inject"):
            return True
    return False


def find_check_operation(model: Any) -> tuple[str, Any, dict[str, Any]] | None:
    """Find the best operation for a health check from a ConnectorModel.

    Selection logic (same as what the platform backend uses via LocalExecutor.check):
    1. Look for any operation with preferred_for_check=True
    2. Fall back to the first LIST operation with no required parameters

    Args:
        model: ConnectorModel with entities containing endpoints

    Returns:
        Tuple of (entity_name, action, params) or None if no suitable operation found.
        For list operations, params includes {"limit": 1} to minimize data transfer.
    """
    check_entity = None
    check_action = None

    # Look for preferred check operation
    for entity_def in model.entities:
        for action, endpoint in entity_def.endpoints.items():
            if getattr(endpoint, "preferred_for_check", False):
                check_entity = entity_def.name
                check_action = action
                break
        if check_entity:
            break

    # Fallback to first list operation with no required params
    if check_entity is None:
        for entity_def in model.entities:
            if Action.LIST in entity_def.endpoints:
                endpoint = entity_def.endpoints[Action.LIST]
                if not has_required_params(endpoint):
                    check_entity = entity_def.name
                    check_action = Action.LIST
                    break

    if check_entity is None or check_action is None:
        return None

    params: dict[str, Any] = {"limit": 1} if check_action == Action.LIST else {}
    return (check_entity, check_action, params)


class ExecutorError(AirbyteError):
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
