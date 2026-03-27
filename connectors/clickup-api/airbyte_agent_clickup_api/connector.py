"""
Clickup-Api connector.
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

from .connector_model import ClickupApiConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    CommentsCreateParams,
    CommentsGetParams,
    CommentsListParams,
    CommentsUpdateParams,
    DocsGetParams,
    DocsListParams,
    FoldersGetParams,
    FoldersListParams,
    GoalsGetParams,
    GoalsListParams,
    ListsGetParams,
    ListsListParams,
    MembersListParams,
    SpacesGetParams,
    SpacesListParams,
    TasksApiSearchParams,
    TasksGetParams,
    TasksListParams,
    TeamsListParams,
    TimeTrackingGetParams,
    TimeTrackingListParams,
    UserGetParams,
    ViewTasksListParams,
    ViewsGetParams,
    ViewsListParams,
)
from .models import ClickupApiAuthConfig

# Import response models and envelope models at runtime
from .models import (
    ClickupApiCheckResult,
    ClickupApiExecuteResult,
    ClickupApiExecuteResultWithMeta,
    TeamsListResult,
    SpacesListResult,
    FoldersListResult,
    ListsListResult,
    TasksListResult,
    TasksApiSearchResult,
    CommentsListResult,
    GoalsListResult,
    ViewsListResult,
    ViewTasksListResult,
    TimeTrackingListResult,
    MembersListResult,
    DocsListResult,
    Comment,
    CommentCreateResponse,
    CommentUpdateResponse,
    Doc,
    Folder,
    Goal,
    List,
    Member,
    Space,
    Task,
    Team,
    TimeEntry,
    User,
    View,
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




class ClickupApiConnector:
    """
    Type-safe Clickup-Api API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "clickup-api"
    connector_version = "0.1.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("user", "get"): None,
        ("teams", "list"): True,
        ("spaces", "list"): True,
        ("spaces", "get"): None,
        ("folders", "list"): True,
        ("folders", "get"): None,
        ("lists", "list"): True,
        ("lists", "get"): None,
        ("tasks", "list"): True,
        ("tasks", "get"): None,
        ("tasks", "api_search"): True,
        ("comments", "list"): True,
        ("comments", "create"): None,
        ("comments", "get"): None,
        ("comments", "update"): None,
        ("goals", "list"): True,
        ("goals", "get"): None,
        ("views", "list"): True,
        ("views", "get"): None,
        ("view_tasks", "list"): True,
        ("time_tracking", "list"): True,
        ("time_tracking", "get"): None,
        ("members", "list"): True,
        ("docs", "list"): True,
        ("docs", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('spaces', 'list'): {'team_id': 'team_id'},
        ('spaces', 'get'): {'space_id': 'space_id'},
        ('folders', 'list'): {'space_id': 'space_id'},
        ('folders', 'get'): {'folder_id': 'folder_id'},
        ('lists', 'list'): {'folder_id': 'folder_id'},
        ('lists', 'get'): {'list_id': 'list_id'},
        ('tasks', 'list'): {'list_id': 'list_id', 'page': 'page'},
        ('tasks', 'get'): {'task_id': 'task_id', 'custom_task_ids': 'custom_task_ids', 'include_subtasks': 'include_subtasks'},
        ('tasks', 'api_search'): {'team_id': 'team_id', 'search': 'search', 'statuses': 'statuses[]', 'assignees': 'assignees[]', 'tags': 'tags[]', 'priority': 'priority', 'due_date_gt': 'due_date_gt', 'due_date_lt': 'due_date_lt', 'date_created_gt': 'date_created_gt', 'date_created_lt': 'date_created_lt', 'date_updated_gt': 'date_updated_gt', 'date_updated_lt': 'date_updated_lt', 'custom_fields': 'custom_fields', 'include_closed': 'include_closed', 'page': 'page'},
        ('comments', 'list'): {'task_id': 'task_id'},
        ('comments', 'create'): {'comment_text': 'comment_text', 'assignee': 'assignee', 'notify_all': 'notify_all', 'task_id': 'task_id'},
        ('comments', 'get'): {'comment_id': 'comment_id'},
        ('comments', 'update'): {'comment_text': 'comment_text', 'assignee': 'assignee', 'resolved': 'resolved', 'comment_id': 'comment_id'},
        ('goals', 'list'): {'team_id': 'team_id'},
        ('goals', 'get'): {'goal_id': 'goal_id'},
        ('views', 'list'): {'team_id': 'team_id'},
        ('views', 'get'): {'view_id': 'view_id'},
        ('view_tasks', 'list'): {'view_id': 'view_id', 'page': 'page'},
        ('time_tracking', 'list'): {'team_id': 'team_id', 'start_date': 'start_date', 'end_date': 'end_date', 'assignee': 'assignee'},
        ('time_tracking', 'get'): {'team_id': 'team_id', 'time_entry_id': 'time_entry_id'},
        ('members', 'list'): {'task_id': 'task_id'},
        ('docs', 'list'): {'workspace_id': 'workspace_id'},
        ('docs', 'get'): {'workspace_id': 'workspace_id', 'doc_id': 'doc_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ClickupApiAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ClickupApiAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new clickup-api connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ClickupApiAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = ClickupApiConnector(auth_config=ClickupApiAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ClickupApiConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = ClickupApiConnector(
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
                connector_definition_id=str(ClickupApiConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ClickupApiAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=ClickupApiConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.user = UserQuery(self)
        self.teams = TeamsQuery(self)
        self.spaces = SpacesQuery(self)
        self.folders = FoldersQuery(self)
        self.lists = ListsQuery(self)
        self.tasks = TasksQuery(self)
        self.comments = CommentsQuery(self)
        self.goals = GoalsQuery(self)
        self.views = ViewsQuery(self)
        self.view_tasks = ViewTasksQuery(self)
        self.time_tracking = TimeTrackingQuery(self)
        self.members = MembersQuery(self)
        self.docs = DocsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["user"],
        action: Literal["get"],
        params: "UserGetParams"
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["list"],
        params: "TeamsListParams"
    ) -> "TeamsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["spaces"],
        action: Literal["list"],
        params: "SpacesListParams"
    ) -> "SpacesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["spaces"],
        action: Literal["get"],
        params: "SpacesGetParams"
    ) -> "Space": ...

    @overload
    async def execute(
        self,
        entity: Literal["folders"],
        action: Literal["list"],
        params: "FoldersListParams"
    ) -> "FoldersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["folders"],
        action: Literal["get"],
        params: "FoldersGetParams"
    ) -> "Folder": ...

    @overload
    async def execute(
        self,
        entity: Literal["lists"],
        action: Literal["list"],
        params: "ListsListParams"
    ) -> "ListsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["lists"],
        action: Literal["get"],
        params: "ListsGetParams"
    ) -> "List": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["list"],
        params: "TasksListParams"
    ) -> "TasksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["get"],
        params: "TasksGetParams"
    ) -> "Task": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["api_search"],
        params: "TasksApiSearchParams"
    ) -> "TasksApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["list"],
        params: "CommentsListParams"
    ) -> "CommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["create"],
        params: "CommentsCreateParams"
    ) -> "CommentCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["get"],
        params: "CommentsGetParams"
    ) -> "list[Comment]": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["update"],
        params: "CommentsUpdateParams"
    ) -> "CommentUpdateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["goals"],
        action: Literal["list"],
        params: "GoalsListParams"
    ) -> "GoalsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["goals"],
        action: Literal["get"],
        params: "GoalsGetParams"
    ) -> "Goal": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["list"],
        params: "ViewsListParams"
    ) -> "ViewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["get"],
        params: "ViewsGetParams"
    ) -> "View": ...

    @overload
    async def execute(
        self,
        entity: Literal["view_tasks"],
        action: Literal["list"],
        params: "ViewTasksListParams"
    ) -> "ViewTasksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_tracking"],
        action: Literal["list"],
        params: "TimeTrackingListParams"
    ) -> "TimeTrackingListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_tracking"],
        action: Literal["get"],
        params: "TimeTrackingGetParams"
    ) -> "TimeEntry": ...

    @overload
    async def execute(
        self,
        entity: Literal["members"],
        action: Literal["list"],
        params: "MembersListParams"
    ) -> "MembersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["docs"],
        action: Literal["list"],
        params: "DocsListParams"
    ) -> "DocsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["docs"],
        action: Literal["get"],
        params: "DocsGetParams"
    ) -> "Doc": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "api_search", "create", "update"],
        params: Mapping[str, Any]
    ) -> ClickupApiExecuteResult[Any] | ClickupApiExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "api_search", "create", "update"],
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
                return ClickupApiExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ClickupApiExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ClickupApiCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ClickupApiCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ClickupApiCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ClickupApiCheckResult(
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
            @ClickupApiConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @ClickupApiConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    ClickupApiConnectorModel,
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
        return describe_entities(ClickupApiConnectorModel)

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
            (e for e in ClickupApiConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ClickupApiConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await ClickupApiConnector.create(...)
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
        auth_config: "ClickupApiAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "ClickupApiConnector":
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
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A ClickupApiConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await ClickupApiConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=ClickupApiAuthConfig(api_key="..."),
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
                connector_definition_id=str(ClickupApiConnectorModel.id),
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




class UserQuery:
    """
    Query class for User entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> User:
        """
        View the details of the authenticated user's ClickUp account

        Returns:
            User
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("user", "get", params)
        return result



class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TeamsListResult:
        """
        Get the workspaces (teams) available to the authenticated user

        Returns:
            TeamsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamsListResult(
            data=result.data
        )



class SpacesQuery:
    """
    Query class for Spaces entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        team_id: str,
        **kwargs
    ) -> SpacesListResult:
        """
        Get the spaces available in a workspace

        Args:
            team_id: The ID of the workspace
            **kwargs: Additional parameters

        Returns:
            SpacesListResult
        """
        params = {k: v for k, v in {
            "team_id": team_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("spaces", "list", params)
        # Cast generic envelope to concrete typed result
        return SpacesListResult(
            data=result.data
        )



    async def get(
        self,
        space_id: str,
        **kwargs
    ) -> Space:
        """
        Get a single space by ID

        Args:
            space_id: The ID of the space
            **kwargs: Additional parameters

        Returns:
            Space
        """
        params = {k: v for k, v in {
            "space_id": space_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("spaces", "get", params)
        return result



class FoldersQuery:
    """
    Query class for Folders entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        space_id: str,
        **kwargs
    ) -> FoldersListResult:
        """
        Get the folders in a space

        Args:
            space_id: The ID of the space
            **kwargs: Additional parameters

        Returns:
            FoldersListResult
        """
        params = {k: v for k, v in {
            "space_id": space_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("folders", "list", params)
        # Cast generic envelope to concrete typed result
        return FoldersListResult(
            data=result.data
        )



    async def get(
        self,
        folder_id: str,
        **kwargs
    ) -> Folder:
        """
        Get a single folder by ID

        Args:
            folder_id: The ID of the folder
            **kwargs: Additional parameters

        Returns:
            Folder
        """
        params = {k: v for k, v in {
            "folder_id": folder_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("folders", "get", params)
        return result



class ListsQuery:
    """
    Query class for Lists entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        folder_id: str,
        **kwargs
    ) -> ListsListResult:
        """
        Get the lists in a folder

        Args:
            folder_id: The ID of the folder
            **kwargs: Additional parameters

        Returns:
            ListsListResult
        """
        params = {k: v for k, v in {
            "folder_id": folder_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lists", "list", params)
        # Cast generic envelope to concrete typed result
        return ListsListResult(
            data=result.data
        )



    async def get(
        self,
        list_id: str,
        **kwargs
    ) -> List:
        """
        Get a single list by ID

        Args:
            list_id: The ID of the list
            **kwargs: Additional parameters

        Returns:
            List
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lists", "get", params)
        return result



class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        page: int | None = None,
        **kwargs
    ) -> TasksListResult:
        """
        Get the tasks in a list

        Args:
            list_id: The ID of the list
            page: Page number (0-indexed)
            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TasksListResult(
            data=result.data
        )



    async def get(
        self,
        task_id: str,
        custom_task_ids: bool | None = None,
        include_subtasks: bool | None = None,
        **kwargs
    ) -> Task:
        """
        Get a single task by ID

        Args:
            task_id: The ID of the task
            custom_task_ids: Set to true to use a custom task ID
            include_subtasks: Include subtasks
            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "task_id": task_id,
            "custom_task_ids": custom_task_ids,
            "include_subtasks": include_subtasks,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def api_search(
        self,
        team_id: str,
        search: str | None = None,
        statuses: list[str] | None = None,
        assignees: list[str] | None = None,
        tags: list[str] | None = None,
        priority: int | None = None,
        due_date_gt: int | None = None,
        due_date_lt: int | None = None,
        date_created_gt: int | None = None,
        date_created_lt: int | None = None,
        date_updated_gt: int | None = None,
        date_updated_lt: int | None = None,
        custom_fields: list[dict[str, Any]] | None = None,
        include_closed: bool | None = None,
        page: int | None = None,
        **kwargs
    ) -> TasksApiSearchResult:
        """
        View the tasks that meet specific criteria from a workspace. Supports free-text search
and structured filters including status, assignee, tags, priority, and date ranges.
Responses are limited to 100 tasks per page.


        Args:
            team_id: The workspace ID to search within
            search: Free-text search across task name, description, and custom field text
            statuses: Filter by status names (e.g. "in progress", "done")
            assignees: Filter by user IDs
            tags: Filter by tag names
            priority: Filter by priority: 1=Urgent, 2=High, 3=Normal, 4=Low
            due_date_gt: Due date after (Unix ms)
            due_date_lt: Due date before (Unix ms)
            date_created_gt: Created after (Unix ms)
            date_created_lt: Created before (Unix ms)
            date_updated_gt: Updated after (Unix ms)
            date_updated_lt: Updated before (Unix ms)
            custom_fields: JSON array of custom field filters. Each object: {"field_id": "<UUID>", "operator": "<OP>", "value": "<DATA>"}.
Operators: = (contains), == (exact), <, <=, >, >=, !=, !==, IS NULL, IS NOT NULL, RANGE, ANY, ALL, NOT ANY, NOT ALL

            include_closed: Include closed tasks (excluded by default)
            page: Page number (0-indexed), results capped at 100/page
            **kwargs: Additional parameters

        Returns:
            TasksApiSearchResult
        """
        params = {k: v for k, v in {
            "team_id": team_id,
            "search": search,
            "statuses[]": statuses,
            "assignees[]": assignees,
            "tags[]": tags,
            "priority": priority,
            "due_date_gt": due_date_gt,
            "due_date_lt": due_date_lt,
            "date_created_gt": date_created_gt,
            "date_created_lt": date_created_lt,
            "date_updated_gt": date_updated_gt,
            "date_updated_lt": date_updated_lt,
            "custom_fields": custom_fields,
            "include_closed": include_closed,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "api_search", params)
        # Cast generic envelope to concrete typed result
        return TasksApiSearchResult(
            data=result.data
        )



class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        task_id: str,
        **kwargs
    ) -> CommentsListResult:
        """
        Get the comments on a task

        Args:
            task_id: The ID of the task
            **kwargs: Additional parameters

        Returns:
            CommentsListResult
        """
        params = {k: v for k, v in {
            "task_id": task_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "list", params)
        # Cast generic envelope to concrete typed result
        return CommentsListResult(
            data=result.data
        )



    async def create(
        self,
        comment_text: str,
        task_id: str,
        assignee: int | None = None,
        notify_all: bool | None = None,
        **kwargs
    ) -> CommentCreateResponse:
        """
        Create a comment on a task

        Args:
            comment_text: The comment text
            assignee: User ID to assign
            notify_all: Notify all assignees and watchers
            task_id: The ID of the task
            **kwargs: Additional parameters

        Returns:
            CommentCreateResponse
        """
        params = {k: v for k, v in {
            "comment_text": comment_text,
            "assignee": assignee,
            "notify_all": notify_all,
            "task_id": task_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "create", params)
        return result



    async def get(
        self,
        comment_id: str,
        **kwargs
    ) -> list[Comment]:
        """
        Get threaded replies on a comment

        Args:
            comment_id: The ID of the comment
            **kwargs: Additional parameters

        Returns:
            list[Comment]
        """
        params = {k: v for k, v in {
            "comment_id": comment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "get", params)
        return result



    async def update(
        self,
        comment_id: str,
        comment_text: str | None = None,
        assignee: int | None = None,
        resolved: bool | None = None,
        **kwargs
    ) -> CommentUpdateResponse:
        """
        Update an existing comment

        Args:
            comment_text: Updated comment text
            assignee: User ID to assign
            resolved: Whether the comment is resolved
            comment_id: The ID of the comment
            **kwargs: Additional parameters

        Returns:
            CommentUpdateResponse
        """
        params = {k: v for k, v in {
            "comment_text": comment_text,
            "assignee": assignee,
            "resolved": resolved,
            "comment_id": comment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "update", params)
        return result



class GoalsQuery:
    """
    Query class for Goals entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        team_id: str,
        **kwargs
    ) -> GoalsListResult:
        """
        Get the goals in a workspace

        Args:
            team_id: The ID of the workspace
            **kwargs: Additional parameters

        Returns:
            GoalsListResult
        """
        params = {k: v for k, v in {
            "team_id": team_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("goals", "list", params)
        # Cast generic envelope to concrete typed result
        return GoalsListResult(
            data=result.data
        )



    async def get(
        self,
        goal_id: str,
        **kwargs
    ) -> Goal:
        """
        Get a single goal by ID

        Args:
            goal_id: The ID of the goal
            **kwargs: Additional parameters

        Returns:
            Goal
        """
        params = {k: v for k, v in {
            "goal_id": goal_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("goals", "get", params)
        return result



class ViewsQuery:
    """
    Query class for Views entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        team_id: str,
        **kwargs
    ) -> ViewsListResult:
        """
        Get the workspace-level (Everything level) views

        Args:
            team_id: The ID of the workspace
            **kwargs: Additional parameters

        Returns:
            ViewsListResult
        """
        params = {k: v for k, v in {
            "team_id": team_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "list", params)
        # Cast generic envelope to concrete typed result
        return ViewsListResult(
            data=result.data
        )



    async def get(
        self,
        view_id: str,
        **kwargs
    ) -> View:
        """
        Get a single view by ID

        Args:
            view_id: The ID of the view
            **kwargs: Additional parameters

        Returns:
            View
        """
        params = {k: v for k, v in {
            "view_id": view_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "get", params)
        return result



class ViewTasksQuery:
    """
    Query class for ViewTasks entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        view_id: str,
        page: int | None = None,
        **kwargs
    ) -> ViewTasksListResult:
        """
        Get tasks matching a view's pre-configured filters — useful as a secondary search mechanism

        Args:
            view_id: The ID of the view
            page: Page number (0-indexed)
            **kwargs: Additional parameters

        Returns:
            ViewTasksListResult
        """
        params = {k: v for k, v in {
            "view_id": view_id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("view_tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return ViewTasksListResult(
            data=result.data
        )



class TimeTrackingQuery:
    """
    Query class for TimeTracking entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        team_id: str,
        start_date: int | None = None,
        end_date: int | None = None,
        assignee: str | None = None,
        **kwargs
    ) -> TimeTrackingListResult:
        """
        Get time entries within a date range for a workspace

        Args:
            team_id: The ID of the workspace
            start_date: Start date (Unix ms)
            end_date: End date (Unix ms)
            assignee: Filter by user ID
            **kwargs: Additional parameters

        Returns:
            TimeTrackingListResult
        """
        params = {k: v for k, v in {
            "team_id": team_id,
            "start_date": start_date,
            "end_date": end_date,
            "assignee": assignee,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_tracking", "list", params)
        # Cast generic envelope to concrete typed result
        return TimeTrackingListResult(
            data=result.data
        )



    async def get(
        self,
        team_id: str,
        time_entry_id: str,
        **kwargs
    ) -> TimeEntry:
        """
        Get a single time entry by ID

        Args:
            team_id: The ID of the workspace
            time_entry_id: The ID of the time entry
            **kwargs: Additional parameters

        Returns:
            TimeEntry
        """
        params = {k: v for k, v in {
            "team_id": team_id,
            "time_entry_id": time_entry_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_tracking", "get", params)
        return result



class MembersQuery:
    """
    Query class for Members entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        task_id: str,
        **kwargs
    ) -> MembersListResult:
        """
        Get the members assigned to a task

        Args:
            task_id: The ID of the task
            **kwargs: Additional parameters

        Returns:
            MembersListResult
        """
        params = {k: v for k, v in {
            "task_id": task_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("members", "list", params)
        # Cast generic envelope to concrete typed result
        return MembersListResult(
            data=result.data
        )



class DocsQuery:
    """
    Query class for Docs entity operations.
    """

    def __init__(self, connector: ClickupApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_id: str,
        **kwargs
    ) -> DocsListResult:
        """
        Search for docs in a workspace

        Args:
            workspace_id: The ID of the workspace
            **kwargs: Additional parameters

        Returns:
            DocsListResult
        """
        params = {k: v for k, v in {
            "workspace_id": workspace_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("docs", "list", params)
        # Cast generic envelope to concrete typed result
        return DocsListResult(
            data=result.data
        )



    async def get(
        self,
        workspace_id: str,
        doc_id: str,
        **kwargs
    ) -> Doc:
        """
        Fetch a single doc by ID

        Args:
            workspace_id: The ID of the workspace
            doc_id: The ID of the doc
            **kwargs: Additional parameters

        Returns:
            Doc
        """
        params = {k: v for k, v in {
            "workspace_id": workspace_id,
            "doc_id": doc_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("docs", "get", params)
        return result


