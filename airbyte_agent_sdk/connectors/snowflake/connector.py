"""
Snowflake connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import SnowflakeConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    ColumnsListParams,
    DatabasesListParams,
    RecordCreateParams,
    RecordDeleteParams,
    RecordGetParams,
    RecordListParams,
    RecordUpdateParams,
    ResultPartitionsGetParams,
    SchemasListParams,
    TablesListParams,
    ViewsListParams,
    WarehousesListParams,
)
from .models import SnowflakeAuthConfig
if TYPE_CHECKING:
    from .models import SnowflakeReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    SnowflakeCheckResult,
    SnowflakeExecuteResult,
    SnowflakeExecuteResultWithMeta,
    DatabasesListResult,
    SchemasListResult,
    TablesListResult,
    ViewsListResult,
    WarehousesListResult,
    ColumnsListResult,
    RecordListResult,
    ColumnsResponse,
    DatabasesResponse,
    RecordResponse,
    ResultPartitionResponse,
    SchemasResponse,
    TablesResponse,
    ViewsResponse,
    WarehousesResponse,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class SnowflakeConnector:
    """
    Type-safe Snowflake API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "snowflake"
    connector_version = "1.0.0"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("databases", "list"): True,
        ("schemas", "list"): True,
        ("tables", "list"): True,
        ("views", "list"): True,
        ("warehouses", "list"): True,
        ("columns", "list"): True,
        ("record", "get"): None,
        ("record", "list"): True,
        ("record", "create"): None,
        ("record", "update"): None,
        ("record", "delete"): None,
        ("result_partitions", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('databases', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('schemas', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('tables', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('views', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('warehouses', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('columns', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('record', 'get'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('record', 'list'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters'},
        ('record', 'create'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters', 'request_id': 'requestId', 'retry': 'retry'},
        ('record', 'update'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters', 'request_id': 'requestId', 'retry': 'retry'},
        ('record', 'delete'): {'statement': 'statement', 'database': 'database', 'schema': 'schema', 'warehouse': 'warehouse', 'role': 'role', 'timeout': 'timeout', 'parameters': 'parameters', 'request_id': 'requestId', 'retry': 'retry'},
        ('result_partitions', 'get'): {'statement_handle': 'statementHandle', 'partition': 'partition', 'request_id': 'requestId'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (SnowflakeAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: SnowflakeAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        account: str | None = None    ):
        """
        Initialize a new snowflake connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., SnowflakeAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            account: Snowflake account identifier in the format orgname-accountname (e.g., myorg-myaccount)
        Examples:
            # Local mode (direct API calls)
            connector = SnowflakeConnector(auth_config=SnowflakeAuthConfig(programmatic_access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = SnowflakeConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = SnowflakeConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(SnowflakeConnectorModel.id),
                model=SnowflakeConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or SnowflakeAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if account:
                config_values["account"] = account

            self._executor = LocalExecutor(
                model=SnowflakeConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if account:
                base_url = base_url.replace("{account}", account)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.databases = DatabasesQuery(self)
        self.schemas = SchemasQuery(self)
        self.tables = TablesQuery(self)
        self.views = ViewsQuery(self)
        self.warehouses = WarehousesQuery(self)
        self.columns = ColumnsQuery(self)
        self.record = RecordQuery(self)
        self.result_partitions = ResultPartitionsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["databases"],
        action: Literal["list"],
        params: "DatabasesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DatabasesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["schemas"],
        action: Literal["list"],
        params: "SchemasListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SchemasListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tables"],
        action: Literal["list"],
        params: "TablesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TablesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["list"],
        params: "ViewsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ViewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["warehouses"],
        action: Literal["list"],
        params: "WarehousesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "WarehousesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["columns"],
        action: Literal["list"],
        params: "ColumnsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ColumnsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["record"],
        action: Literal["get"],
        params: "RecordGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RecordResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["record"],
        action: Literal["list"],
        params: "RecordListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RecordListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["record"],
        action: Literal["create"],
        params: "RecordCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RecordResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["record"],
        action: Literal["update"],
        params: "RecordUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RecordResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["record"],
        action: Literal["delete"],
        params: "RecordDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RecordResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["result_partitions"],
        action: Literal["get"],
        params: "ResultPartitionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ResultPartitionResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "delete"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> SnowflakeExecuteResult[Any] | SnowflakeExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "delete"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

        # Remap parameter names from snake_case (TypedDict keys) to API parameter names
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return SnowflakeExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SnowflakeExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SnowflakeCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SnowflakeCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SnowflakeCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SnowflakeCheckResult(
                status="unhealthy",
                error=result.error or "Unknown error during health check",
            )

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def tool_utils(
        cls,
        func: _F | None = None,
        *,
        update_docstring: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = SnowflakeConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @SnowflakeConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @SnowflakeConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @SnowflakeConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    SnowflakeConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

            if update_docstring:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate

    def list_entities(self) -> list[dict[str, Any]]:
        """
        Get structured data about available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.list_entities()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(SnowflakeConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """
        Get the JSON schema for an entity.

        Args:
            entity: Entity name (e.g., "contacts", "companies")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.

        Example:
            schema = connector.entity_schema("contacts")
            if schema:
                print(f"Contact properties: {list(schema.get('properties', {}).keys())}")
        """
        entity_def = next(
            (e for e in SnowflakeConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SnowflakeConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



class DatabasesQuery:
    """
    Query class for Databases entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        statement: str | None = None,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> DatabasesListResult:
        """
        List databases

        Args:
            statement: SQL statement to execute
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            DatabasesListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("databases", "list", params)
        # Cast generic envelope to concrete typed result
        return DatabasesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class SchemasQuery:
    """
    Query class for Schemas entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        statement: str | None = None,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> SchemasListResult:
        """
        List schemas

        Args:
            statement: SQL statement to execute
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            SchemasListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schemas", "list", params)
        # Cast generic envelope to concrete typed result
        return SchemasListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class TablesQuery:
    """
    Query class for Tables entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        statement: str | None = None,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> TablesListResult:
        """
        List tables

        Args:
            statement: SQL statement to execute
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            TablesListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tables", "list", params)
        # Cast generic envelope to concrete typed result
        return TablesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class ViewsQuery:
    """
    Query class for Views entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        statement: str | None = None,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> ViewsListResult:
        """
        List views

        Args:
            statement: SQL statement to execute
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            ViewsListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "list", params)
        # Cast generic envelope to concrete typed result
        return ViewsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class WarehousesQuery:
    """
    Query class for Warehouses entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        statement: str | None = None,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> WarehousesListResult:
        """
        List warehouses

        Args:
            statement: SQL statement to execute
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            WarehousesListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("warehouses", "list", params)
        # Cast generic envelope to concrete typed result
        return WarehousesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class ColumnsQuery:
    """
    Query class for Columns entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        statement: str | None = None,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> ColumnsListResult:
        """
        List columns

        Args:
            statement: SQL statement to execute
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            ColumnsListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("columns", "list", params)
        # Cast generic envelope to concrete typed result
        return ColumnsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class RecordQuery:
    """
    Query class for Record entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        statement: str,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> RecordResponse:
        """
        Execute a SQL SELECT statement and return the result set. Typically used to retrieve a single row by filtering on a unique identifier (e.g., SELECT * FROM users WHERE id = 42). The result is returned as rows, the same shape as the list action; when the SELECT targets one row the result contains a single row. Intended for row retrieval only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.

        Args:
            statement: SQL SELECT statement to retrieve a single record (e.g., SELECT * FROM users WHERE id = 42)
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            RecordResponse
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("record", "get", params)
        return result



    async def list(
        self,
        statement: str,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        **kwargs
    ) -> RecordListResult:
        """
        Execute a SQL SELECT query that returns multiple records from a Snowflake table or view. Use this action when you need to retrieve a set of rows, optionally with filtering, sorting, or limiting (e.g., SELECT * FROM orders WHERE status = 'active' ORDER BY created_at DESC LIMIT 100). Intended for row retrieval only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.

        Args:
            statement: SQL SELECT statement to retrieve multiple records (e.g., SELECT * FROM orders WHERE status = 'active' LIMIT 100)
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            **kwargs: Additional parameters

        Returns:
            RecordListResult
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("record", "list", params)
        # Cast generic envelope to concrete typed result
        return RecordListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        statement: str,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        request_id: str | None = None,
        retry: bool | None = None,
        **kwargs
    ) -> RecordResponse:
        """
        Execute a SQL INSERT statement to create one or more new rows in a Snowflake table (e.g., INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')). Intended for row insertion only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE TABLE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.

        Args:
            statement: SQL INSERT statement to create new records (e.g., INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com'))
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            request_id: Unique request ID for this DML statement. Reuse the SAME requestId when resubmitting after a network error or timeout so Snowflake deduplicates instead of executing the statement again.
            retry: Set to true when resubmitting a previously-sent statement with the same requestId, so Snowflake treats it as a safe retry rather than a new DML.
            **kwargs: Additional parameters

        Returns:
            RecordResponse
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            "requestId": request_id,
            "retry": retry,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("record", "create", params)
        return result



    async def update(
        self,
        statement: str,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        request_id: str | None = None,
        retry: bool | None = None,
        **kwargs
    ) -> RecordResponse:
        """
        Execute a SQL UPDATE statement to modify existing rows in a Snowflake table (e.g., UPDATE users SET email = 'new@example.com' WHERE id = 7). Intended for row modification only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, ALTER) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.

        Args:
            statement: SQL UPDATE statement to modify existing records (e.g., UPDATE users SET email = 'new@example.com' WHERE id = 7)
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            request_id: Unique request ID for this DML statement. Reuse the SAME requestId when resubmitting after a network error or timeout so Snowflake deduplicates instead of executing the statement again.
            retry: Set to true when resubmitting a previously-sent statement with the same requestId, so Snowflake treats it as a safe retry rather than a new DML.
            **kwargs: Additional parameters

        Returns:
            RecordResponse
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            "requestId": request_id,
            "retry": retry,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("record", "update", params)
        return result



    async def delete(
        self,
        statement: str,
        database: str | None = None,
        schema: str | None = None,
        warehouse: str | None = None,
        role: str | None = None,
        timeout: int | None = None,
        parameters: dict[str, Any] | None = None,
        request_id: str | None = None,
        retry: bool | None = None,
        **kwargs
    ) -> RecordResponse:
        """
        Execute a SQL DELETE statement to remove rows from a Snowflake table (e.g., DELETE FROM logs WHERE id = 99). Intended for row deletion only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.

        Args:
            statement: SQL DELETE statement to remove records (e.g., DELETE FROM logs WHERE id = 99)
            database: Database context for the statement
            schema: Schema context for the statement
            warehouse: Warehouse to use for execution
            role: Role to use for execution
            timeout: Timeout in seconds for the statement execution
            parameters: Session parameters for the statement execution
            request_id: Unique request ID for this DML statement. Reuse the SAME requestId when resubmitting after a network error or timeout so Snowflake deduplicates instead of executing the statement again.
            retry: Set to true when resubmitting a previously-sent statement with the same requestId, so Snowflake treats it as a safe retry rather than a new DML.
            **kwargs: Additional parameters

        Returns:
            RecordResponse
        """
        params = {k: v for k, v in {
            "statement": statement,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
            "role": role,
            "timeout": timeout,
            "parameters": parameters,
            "requestId": request_id,
            "retry": retry,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("record", "delete", params)
        return result



class ResultPartitionsQuery:
    """
    Query class for ResultPartitions entity operations.
    """

    def __init__(self, connector: SnowflakeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        statement_handle: str,
        partition: int,
        request_id: str | None = None,
        **kwargs
    ) -> ResultPartitionResponse:
        """
        Continuation helper for Snowflake list actions. Use this only after a databases, schemas, tables, views, warehouses, or columns list response includes a next_page_url or multiple partitionInfo entries. The initial list response contains partition 0; call this action with partition 1, 2, and so on to retrieve additional rows for the same SHOW statement. This is not a standalone Snowflake resource and does not execute new SQL.

        Args:
            statement_handle: Statement handle returned by the initial list response metadata. Reuse this value when fetching additional partitions for that same result set.
            partition: Zero-based partition number to retrieve. The initial list response contains partition 0; request partition 1 or higher for subsequent pages.
            request_id: Optional request ID from the initial list response metadata. Pass it through when available to continue the same Snowflake SQL API request.
            **kwargs: Additional parameters

        Returns:
            ResultPartitionResponse
        """
        params = {k: v for k, v in {
            "statementHandle": statement_handle,
            "partition": partition,
            "requestId": request_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("result_partitions", "get", params)
        return result


