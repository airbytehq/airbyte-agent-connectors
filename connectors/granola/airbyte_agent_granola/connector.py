"""
Granola connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import GranolaConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    NotesGetParams,
    NotesListParams,
    AirbyteSearchParams,
    NotesSearchFilter,
    NotesSearchQuery,
)
from .models import GranolaAuthConfig

# Import response models and envelope models at runtime
from .models import (
    GranolaCheckResult,
    GranolaExecuteResult,
    GranolaExecuteResultWithMeta,
    NotesListResult,
    Note,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    NotesSearchData,
    NotesSearchResult,
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




class GranolaConnector:
    """
    Type-safe Granola API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "granola"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("notes", "list"): True,
        ("notes", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('notes', 'list'): {'page_size': 'page_size', 'cursor': 'cursor', 'created_before': 'created_before', 'created_after': 'created_after'},
        ('notes', 'get'): {'note_id': 'note_id', 'include': 'include'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GranolaAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GranolaAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new granola connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GranolaAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `external_user_id`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GranolaConnector(auth_config=GranolaAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GranolaConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by external_user_id
            connector = GranolaConnector(
                auth_config=AirbyteAuthConfig(
                    external_user_id="user-123",
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
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                external_user_id=auth_config.external_user_id,
                connector_definition_id=str(GranolaConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GranolaAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GranolaConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.notes = NotesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["list"],
        params: "NotesListParams"
    ) -> "NotesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["get"],
        params: "NotesGetParams"
    ) -> "Note": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> GranolaExecuteResult[Any] | GranolaExecuteResultWithMeta[Any, Any] | Any: ...

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
                return GranolaExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GranolaExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GranolaCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GranolaCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GranolaCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GranolaCheckResult(
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
            @GranolaConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GranolaConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GranolaConnectorModel,
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
        return describe_entities(GranolaConnectorModel)

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
            (e for e in GranolaConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GranolaConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GranolaConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "GranolaAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "GranolaConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and external_user_id.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A GranolaConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await GranolaConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GranolaAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.external_user_id:
            raise ValueError("airbyte_config.external_user_id is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(GranolaConnectorModel.id),
                external_user_id=airbyte_config.external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                connector_id=source_id,
            ),
        )




class NotesQuery:
    """
    Query class for Notes entity operations.
    """

    def __init__(self, connector: GranolaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        cursor: str | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        **kwargs
    ) -> NotesListResult:
        """
        Returns a paginated list of meeting notes

        Args:
            page_size: Maximum number of notes to return per page
            cursor: Pagination cursor for next page
            created_before: Return notes created before this date (YYYY-MM-DD)
            created_after: Return notes created after this date (YYYY-MM-DD)
            **kwargs: Additional parameters

        Returns:
            NotesListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "cursor": cursor,
            "created_before": created_before,
            "created_after": created_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "list", params)
        # Cast generic envelope to concrete typed result
        return NotesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        note_id: str,
        include: str | None = None,
        **kwargs
    ) -> Note:
        """
        Get a single note by ID, including full details and optionally the transcript

        Args:
            note_id: The ID of the note
            include: Include the note transcript in the response
            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "note_id": note_id,
            "include": include,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "get", params)
        return result



    async def search(
        self,
        query: NotesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> NotesSearchResult:
        """
        Search notes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (NotesSearchFilter):
        - created_at: The creation time of the note in ISO 8601 format.
        - id: The unique identifier of the note.
        - object: The object type, always "note".
        - owner: The owner of the note.
        - title: The title of the note.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            NotesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("notes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return NotesSearchResult(
            data=[
                NotesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
