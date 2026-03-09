"""
Typeform connector.
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

from pydantic import BaseModel

from .connector_model import TypeformConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    FormsGetParams,
    FormsListParams,
    ImagesListParams,
    ResponsesListParams,
    ThemesListParams,
    WebhooksListParams,
    WorkspacesListParams,
    AirbyteSearchParams,
    FormsSearchFilter,
    FormsSearchQuery,
    ResponsesSearchFilter,
    ResponsesSearchQuery,
    WebhooksSearchFilter,
    WebhooksSearchQuery,
    WorkspacesSearchFilter,
    WorkspacesSearchQuery,
    ImagesSearchFilter,
    ImagesSearchQuery,
    ThemesSearchFilter,
    ThemesSearchQuery,
)
from .models import TypeformAuthConfig
if TYPE_CHECKING:
    from .models import TypeformReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    TypeformCheckResult,
    TypeformExecuteResult,
    TypeformExecuteResultWithMeta,
    FormsListResult,
    ResponsesListResult,
    WebhooksListResult,
    WorkspacesListResult,
    ImagesListResult,
    ThemesListResult,
    Form,
    Image,
    Response,
    Theme,
    Webhook,
    Workspace,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    FormsSearchData,
    FormsSearchResult,
    ResponsesSearchData,
    ResponsesSearchResult,
    WebhooksSearchData,
    WebhooksSearchResult,
    WorkspacesSearchData,
    WorkspacesSearchResult,
    ImagesSearchData,
    ImagesSearchResult,
    ThemesSearchData,
    ThemesSearchResult,
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




class TypeformConnector:
    """
    Type-safe Typeform API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "typeform"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("forms", "list"): True,
        ("forms", "get"): None,
        ("responses", "list"): True,
        ("webhooks", "list"): True,
        ("workspaces", "list"): True,
        ("images", "list"): True,
        ("themes", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('forms', 'list'): {'page': 'page', 'page_size': 'page_size'},
        ('forms', 'get'): {'form_id': 'form_id'},
        ('responses', 'list'): {'form_id': 'form_id', 'page_size': 'page_size', 'since': 'since', 'until': 'until', 'after': 'after', 'before': 'before', 'sort': 'sort', 'completed': 'completed', 'query': 'query'},
        ('webhooks', 'list'): {'form_id': 'form_id'},
        ('workspaces', 'list'): {'page': 'page', 'page_size': 'page_size'},
        ('themes', 'list'): {'page': 'page', 'page_size': 'page_size'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (TypeformAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: TypeformAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new typeform connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., TypeformAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = TypeformConnector(auth_config=TypeformAuthConfig(access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = TypeformConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = TypeformConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="user-123",
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
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                customer_name=auth_config.customer_name,
                organization_id=auth_config.organization_id,
                connector_definition_id=str(TypeformConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or TypeformAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=TypeformConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.forms = FormsQuery(self)
        self.responses = ResponsesQuery(self)
        self.webhooks = WebhooksQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.images = ImagesQuery(self)
        self.themes = ThemesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["forms"],
        action: Literal["list"],
        params: "FormsListParams"
    ) -> "FormsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["forms"],
        action: Literal["get"],
        params: "FormsGetParams"
    ) -> "Form": ...

    @overload
    async def execute(
        self,
        entity: Literal["responses"],
        action: Literal["list"],
        params: "ResponsesListParams"
    ) -> "ResponsesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["webhooks"],
        action: Literal["list"],
        params: "WebhooksListParams"
    ) -> "WebhooksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspaces"],
        action: Literal["list"],
        params: "WorkspacesListParams"
    ) -> "WorkspacesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["images"],
        action: Literal["list"],
        params: "ImagesListParams"
    ) -> "ImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["themes"],
        action: Literal["list"],
        params: "ThemesListParams"
    ) -> "ThemesListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> TypeformExecuteResult[Any] | TypeformExecuteResultWithMeta[Any, Any] | Any: ...

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
                return TypeformExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return TypeformExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> TypeformCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            TypeformCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return TypeformCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return TypeformCheckResult(
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
            @TypeformConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @TypeformConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    TypeformConnectorModel,
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
        return describe_entities(TypeformConnectorModel)

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
            (e for e in TypeformConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in TypeformConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await TypeformConnector.create(...)
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
        auth_config: "TypeformAuthConfig",
        name: str | None = None,
        replication_config: "TypeformReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "TypeformConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A TypeformConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await TypeformConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=TypeformAuthConfig(access_token="..."),
            )

            # With replication config (required for this connector):
            connector = await TypeformConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=TypeformAuthConfig(access_token="..."),
                replication_config=TypeformReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(TypeformConnectorModel.id),
                customer_name=airbyte_config.customer_name,
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
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )




class FormsQuery:
    """
    Query class for Forms entity operations.
    """

    def __init__(self, connector: TypeformConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> FormsListResult:
        """
        Returns a paginated list of forms in the account

        Args:
            page: Page number to retrieve
            page_size: Number of forms per page
            **kwargs: Additional parameters

        Returns:
            FormsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("forms", "list", params)
        # Cast generic envelope to concrete typed result
        return FormsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        form_id: str,
        **kwargs
    ) -> Form:
        """
        Retrieves a single form by its ID, including fields, settings, and logic

        Args:
            form_id: Unique ID of the form
            **kwargs: Additional parameters

        Returns:
            Form
        """
        params = {k: v for k, v in {
            "form_id": form_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("forms", "get", params)
        return result



    async def search(
        self,
        query: FormsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FormsSearchResult:
        """
        Search forms records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FormsSearchFilter):
        - links: Links to related resources
        - created_at: Date and time when the form was created
        - fields: List of fields within the form
        - id: Unique identifier of the form
        - last_updated_at: Date and time when the form was last updated
        - logic: Logic rules or conditions applied to the form fields
        - published_at: Date and time when the form was published
        - settings: Settings and configurations for the form
        - thankyou_screens: Thank you screen configurations
        - theme: Theme settings for the form
        - title: Title of the form
        - type_: Type of the form
        - welcome_screens: Welcome screen configurations
        - workspace: Workspace details where the form belongs

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FormsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("forms", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FormsSearchResult(
            data=[
                FormsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ResponsesQuery:
    """
    Query class for Responses entity operations.
    """

    def __init__(self, connector: TypeformConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        form_id: str,
        page_size: int | None = None,
        since: str | None = None,
        until: str | None = None,
        after: str | None = None,
        before: str | None = None,
        sort: str | None = None,
        completed: bool | None = None,
        query: str | None = None,
        **kwargs
    ) -> ResponsesListResult:
        """
        Returns a paginated list of responses for a given form

        Args:
            form_id: Unique ID of the form
            page_size: Number of responses per page
            since: Limit responses to those submitted since the specified date/time (ISO 8601 format, e.g. 2021-03-01T00:00:00Z)
            until: Limit responses to those submitted until the specified date/time (ISO 8601 format)
            after: Cursor token for pagination; returns responses after this token
            before: Cursor token for pagination; returns responses before this token
            sort: Sort order for responses, e.g. submitted_at,asc
            completed: Filter by completed status (true or false)
            query: Search query to filter responses
            **kwargs: Additional parameters

        Returns:
            ResponsesListResult
        """
        params = {k: v for k, v in {
            "form_id": form_id,
            "page_size": page_size,
            "since": since,
            "until": until,
            "after": after,
            "before": before,
            "sort": sort,
            "completed": completed,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("responses", "list", params)
        # Cast generic envelope to concrete typed result
        return ResponsesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ResponsesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ResponsesSearchResult:
        """
        Search responses records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ResponsesSearchFilter):
        - answers: Response data for each question in the form
        - calculated: Calculated data related to the response
        - form_id: ID of the form
        - hidden: Hidden fields in the response
        - landed_at: Timestamp when the respondent landed on the form
        - landing_id: ID of the landing page
        - metadata: Metadata related to the response
        - response_id: ID of the response
        - response_type: Type of the response
        - submitted_at: Timestamp when the response was submitted
        - token: Token associated with the response
        - variables: Variables associated with the response

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ResponsesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("responses", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ResponsesSearchResult(
            data=[
                ResponsesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class WebhooksQuery:
    """
    Query class for Webhooks entity operations.
    """

    def __init__(self, connector: TypeformConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        form_id: str,
        **kwargs
    ) -> WebhooksListResult:
        """
        Returns webhooks configured for a given form

        Args:
            form_id: Unique ID of the form
            **kwargs: Additional parameters

        Returns:
            WebhooksListResult
        """
        params = {k: v for k, v in {
            "form_id": form_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("webhooks", "list", params)
        # Cast generic envelope to concrete typed result
        return WebhooksListResult(
            data=result.data
        )



    async def search(
        self,
        query: WebhooksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> WebhooksSearchResult:
        """
        Search webhooks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (WebhooksSearchFilter):
        - created_at: Timestamp when the webhook was created
        - enabled: Whether the webhook is currently enabled
        - form_id: ID of the form associated with the webhook
        - id: Unique identifier of the webhook
        - tag: Tag to categorize or label the webhook
        - updated_at: Timestamp when the webhook was last updated
        - url: URL where webhook data is sent
        - verify_ssl: Whether SSL verification is enforced

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            WebhooksSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("webhooks", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return WebhooksSearchResult(
            data=[
                WebhooksSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class WorkspacesQuery:
    """
    Query class for Workspaces entity operations.
    """

    def __init__(self, connector: TypeformConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> WorkspacesListResult:
        """
        Returns a paginated list of workspaces in the account

        Args:
            page: Page number to retrieve
            page_size: Number of workspaces per page
            **kwargs: Additional parameters

        Returns:
            WorkspacesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspaces", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspacesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: WorkspacesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> WorkspacesSearchResult:
        """
        Search workspaces records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (WorkspacesSearchFilter):
        - account_id: Account ID associated with the workspace
        - default: Whether this is the default workspace
        - forms: Information about forms in the workspace
        - id: Unique identifier of the workspace
        - name: Name of the workspace
        - self: Self-referential link
        - shared: Whether this workspace is shared

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            WorkspacesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("workspaces", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return WorkspacesSearchResult(
            data=[
                WorkspacesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ImagesQuery:
    """
    Query class for Images entity operations.
    """

    def __init__(self, connector: TypeformConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ImagesListResult:
        """
        Returns a list of images in the account

        Returns:
            ImagesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("images", "list", params)
        # Cast generic envelope to concrete typed result
        return ImagesListResult(
            data=result.data
        )



    async def search(
        self,
        query: ImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ImagesSearchResult:
        """
        Search images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ImagesSearchFilter):
        - avg_color: Average color of the image
        - file_name: Name of the image file
        - has_alpha: Whether the image has an alpha channel
        - height: Height of the image in pixels
        - id: Unique identifier of the image
        - media_type: MIME type of the image
        - src: URL to access the image
        - width: Width of the image in pixels

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ImagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("images", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ImagesSearchResult(
            data=[
                ImagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ThemesQuery:
    """
    Query class for Themes entity operations.
    """

    def __init__(self, connector: TypeformConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> ThemesListResult:
        """
        Returns a paginated list of themes in the account

        Args:
            page: Page number to retrieve
            page_size: Number of themes per page
            **kwargs: Additional parameters

        Returns:
            ThemesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("themes", "list", params)
        # Cast generic envelope to concrete typed result
        return ThemesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ThemesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ThemesSearchResult:
        """
        Search themes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ThemesSearchFilter):
        - background: Background settings for the theme
        - colors: Color settings
        - created_at: Timestamp when the theme was created
        - fields: Field display settings
        - font: Font used in the theme
        - has_transparent_button: Whether the theme has a transparent button
        - id: Unique identifier of the theme
        - name: Name of the theme
        - rounded_corners: Rounded corners setting
        - screens: Screen display settings
        - updated_at: Timestamp when the theme was last updated
        - visibility: Visibility setting of the theme

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ThemesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("themes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ThemesSearchResult(
            data=[
                ThemesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
