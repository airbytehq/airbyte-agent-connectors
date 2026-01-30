"""
Airtable connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import AirtableConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    BasesListParams,
    RecordsGetParams,
    RecordsListParams,
    TablesListParams,
    AirbyteSearchParams,
    BasesSearchFilter,
    BasesSearchQuery,
    TablesSearchFilter,
    TablesSearchQuery,
)
if TYPE_CHECKING:
    from .models import AirtableAuthConfig
# Import response models and envelope models at runtime
from .models import (
    AirtableCheckResult,
    AirtableExecuteResult,
    AirtableExecuteResultWithMeta,
    BasesListResult,
    TablesListResult,
    RecordsListResult,
    Base,
    Record,
    Table,
    AirbyteSearchHit,
    AirbyteSearchResult,
    BasesSearchData,
    BasesSearchResult,
    TablesSearchData,
    TablesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 50_000  # ~50KB default, configurable per-tool


def _raise_output_too_large(message: str) -> None:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except Exception as exc:
        raise RuntimeError(message) from exc
    raise ModelRetry(message)


def _check_output_size(result: Any, max_chars: int | None, tool_name: str) -> Any:
    if max_chars is None or max_chars <= 0:
        return result

    try:
        serialized = json.dumps(result, default=str)
    except (TypeError, ValueError):
        return result

    if len(serialized) > max_chars:
        truncated_preview = serialized[:500] + "..." if len(serialized) > 500 else serialized
        _raise_output_too_large(
            f"Tool '{tool_name}' output too large ({len(serialized):,} chars, limit {max_chars:,}). "
            "Please narrow your query by: using the 'fields' parameter to select only needed fields, "
            "adding filters, or reducing the 'limit'. "
            f"Preview: {truncated_preview}"
        )

    return result




class AirtableConnector:
    """
    Type-safe Airtable API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "airtable"
    connector_version = "1.0.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("bases", "list"): True,
        ("tables", "list"): True,
        ("records", "list"): True,
        ("records", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('bases', 'list'): {'offset': 'offset'},
        ('tables', 'list'): {'base_id': 'base_id'},
        ('records', 'list'): {'base_id': 'base_id', 'table_id_or_name': 'table_id_or_name', 'offset': 'offset', 'page_size': 'pageSize', 'view': 'view', 'filter_by_formula': 'filterByFormula', 'sort': 'sort'},
        ('records', 'get'): {'base_id': 'base_id', 'table_id_or_name': 'table_id_or_name', 'record_id': 'record_id'},
    }

    def __init__(
        self,
        auth_config: AirtableAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new airtable connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `external_user_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = AirtableConnector(auth_config=AirtableAuthConfig(personal_access_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = AirtableConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = AirtableConnector(
                auth_config=AirtableAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: external_user_id, airbyte_client_id, and airbyte_client_secret provided
        if external_user_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                external_user_id=external_user_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_definition_id=str(AirtableConnectorModel.id),
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (external_user_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=AirtableConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.bases = BasesQuery(self)
        self.tables = TablesQuery(self)
        self.records = RecordsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["bases"],
        action: Literal["list"],
        params: "BasesListParams"
    ) -> "BasesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tables"],
        action: Literal["list"],
        params: "TablesListParams"
    ) -> "TablesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["records"],
        action: Literal["list"],
        params: "RecordsListParams"
    ) -> "RecordsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["records"],
        action: Literal["get"],
        params: "RecordsGetParams"
    ) -> "Record": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> AirtableExecuteResult[Any] | AirtableExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any] | None = None
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

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

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
            params=resolved_params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return AirtableExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return AirtableExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> AirtableCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            AirtableCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return AirtableCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return AirtableCheckResult(
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
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @AirtableConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @AirtableConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    AirtableConnectorModel,
                    enable_hosted_mode_features=enable_hosted_mode_features,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            if inspect.iscoroutinefunction(inner):

                @wraps(inner)
                async def aw(*args: Any, **kwargs: Any) -> Any:
                    result = await inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = aw
            else:

                @wraps(inner)
                def sw(*args: Any, **kwargs: Any) -> Any:
                    result = inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = sw

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
        return describe_entities(AirtableConnectorModel)

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
            (e for e in AirtableConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in AirtableConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class BasesQuery:
    """
    Query class for Bases entity operations.
    """

    def __init__(self, connector: AirtableConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        offset: str | None = None,
        **kwargs
    ) -> BasesListResult:
        """
        Returns a list of all bases the user has access to

        Args:
            offset: Pagination offset from previous response
            **kwargs: Additional parameters

        Returns:
            BasesListResult
        """
        params = {k: v for k, v in {
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("bases", "list", params)
        # Cast generic envelope to concrete typed result
        return BasesListResult(
            data=result.data
        )



    async def search(
        self,
        query: BasesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BasesSearchResult:
        """
        Search bases records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BasesSearchFilter):
        - id: Unique identifier for the base
        - name: Name of the base
        - permission_level: Permission level for the base

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BasesSearchResult with hits (list of AirbyteSearchHit[BasesSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("bases", "search", params)

        # Parse response into typed result
        return BasesSearchResult(
            hits=[
                AirbyteSearchHit[BasesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=BasesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class TablesQuery:
    """
    Query class for Tables entity operations.
    """

    def __init__(self, connector: AirtableConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        base_id: str,
        **kwargs
    ) -> TablesListResult:
        """
        Returns a list of all tables in the specified base with their schema information

        Args:
            base_id: The ID of the base
            **kwargs: Additional parameters

        Returns:
            TablesListResult
        """
        params = {k: v for k, v in {
            "base_id": base_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tables", "list", params)
        # Cast generic envelope to concrete typed result
        return TablesListResult(
            data=result.data
        )



    async def search(
        self,
        query: TablesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TablesSearchResult:
        """
        Search tables records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TablesSearchFilter):
        - id: Unique identifier for the table
        - name: Name of the table
        - primary_field_id: ID of the primary field
        - fields: List of fields in the table
        - views: List of views in the table

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TablesSearchResult with hits (list of AirbyteSearchHit[TablesSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("tables", "search", params)

        # Parse response into typed result
        return TablesSearchResult(
            hits=[
                AirbyteSearchHit[TablesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TablesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class RecordsQuery:
    """
    Query class for Records entity operations.
    """

    def __init__(self, connector: AirtableConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        base_id: str,
        table_id_or_name: str,
        offset: str | None = None,
        page_size: int | None = None,
        view: str | None = None,
        filter_by_formula: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> RecordsListResult:
        """
        Returns a paginated list of records from the specified table

        Args:
            base_id: The ID of the base
            table_id_or_name: The ID or name of the table
            offset: Pagination offset from previous response
            page_size: Number of records per page (max 100)
            view: Name or ID of a view to filter records
            filter_by_formula: Airtable formula to filter records
            sort: Sort configuration as JSON array
            **kwargs: Additional parameters

        Returns:
            RecordsListResult
        """
        params = {k: v for k, v in {
            "base_id": base_id,
            "table_id_or_name": table_id_or_name,
            "offset": offset,
            "pageSize": page_size,
            "view": view,
            "filterByFormula": filter_by_formula,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("records", "list", params)
        # Cast generic envelope to concrete typed result
        return RecordsListResult(
            data=result.data
        )



    async def get(
        self,
        base_id: str,
        table_id_or_name: str,
        record_id: str,
        **kwargs
    ) -> Record:
        """
        Returns a single record by ID from the specified table

        Args:
            base_id: The ID of the base
            table_id_or_name: The ID or name of the table
            record_id: The ID of the record
            **kwargs: Additional parameters

        Returns:
            Record
        """
        params = {k: v for k, v in {
            "base_id": base_id,
            "table_id_or_name": table_id_or_name,
            "record_id": record_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("records", "get", params)
        return result


