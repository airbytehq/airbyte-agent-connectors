"""
Linear connector.
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

from .connector_model import LinearConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    CommentsCreateParams,
    CommentsGetParams,
    CommentsListParams,
    CommentsUpdateParams,
    IssuesCreateParams,
    IssuesGetParams,
    IssuesListParams,
    IssuesUpdateParams,
    ProjectsGetParams,
    ProjectsListParams,
    TeamsGetParams,
    TeamsListParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    CommentsSearchFilter,
    CommentsSearchQuery,
    IssuesSearchFilter,
    IssuesSearchQuery,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    TeamsSearchFilter,
    TeamsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
)
if TYPE_CHECKING:
    from .models import LinearAuthConfig

# Import response models and envelope models at runtime
from .models import (
    LinearCheckResult,
    LinearExecuteResult,
    LinearExecuteResultWithMeta,
    IssuesListResult,
    ProjectsListResult,
    TeamsListResult,
    UsersListResult,
    CommentsListResult,
    CommentCreateResponse,
    CommentResponse,
    CommentUpdateResponse,
    CommentsListResponse,
    Issue,
    IssueCreateResponse,
    IssueResponse,
    IssueUpdateResponse,
    Project,
    ProjectResponse,
    Team,
    TeamResponse,
    UserResponse,
    UsersListResponse,
    AirbyteSearchHit,
    AirbyteSearchResult,
    CommentsSearchData,
    CommentsSearchResult,
    IssuesSearchData,
    IssuesSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    TeamsSearchData,
    TeamsSearchResult,
    UsersSearchData,
    UsersSearchResult,
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




class LinearConnector:
    """
    Type-safe Linear API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "linear"
    connector_version = "0.1.8"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("issues", "list"): True,
        ("issues", "get"): None,
        ("issues", "create"): None,
        ("issues", "update"): None,
        ("projects", "list"): True,
        ("projects", "get"): None,
        ("teams", "list"): True,
        ("teams", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("comments", "list"): True,
        ("comments", "get"): None,
        ("comments", "create"): None,
        ("comments", "update"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('issues', 'list'): {'first': 'first', 'after': 'after'},
        ('issues', 'get'): {'id': 'id'},
        ('issues', 'create'): {'team_id': 'teamId', 'title': 'title', 'description': 'description', 'state_id': 'stateId', 'priority': 'priority'},
        ('issues', 'update'): {'id': 'id', 'title': 'title', 'description': 'description', 'state_id': 'stateId', 'priority': 'priority', 'assignee_id': 'assigneeId'},
        ('projects', 'list'): {'first': 'first', 'after': 'after'},
        ('projects', 'get'): {'id': 'id'},
        ('teams', 'list'): {'first': 'first', 'after': 'after'},
        ('teams', 'get'): {'id': 'id'},
        ('users', 'list'): {'first': 'first', 'after': 'after'},
        ('users', 'get'): {'id': 'id'},
        ('comments', 'list'): {'issue_id': 'issueId', 'first': 'first', 'after': 'after'},
        ('comments', 'get'): {'id': 'id'},
        ('comments', 'create'): {'issue_id': 'issueId', 'body': 'body'},
        ('comments', 'update'): {'id': 'id', 'body': 'body'},
    }

    def __init__(
        self,
        auth_config: LinearAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new linear connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide Airbyte credentials with either `connector_id` or `external_user_id`

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (for hosted mode lookup)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            connector_id: Specific connector/source ID (for hosted mode, skips lookup)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = LinearConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = LinearConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = LinearConnector(
                auth_config=LinearAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: Airbyte credentials + either connector_id OR external_user_id
        is_hosted = airbyte_client_id and airbyte_client_secret and (connector_id or external_user_id)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_id=connector_id,
                external_user_id=external_user_id,
                connector_definition_id=str(LinearConnectorModel.id) if not connector_id else None,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide Airbyte credentials (airbyte_client_id, airbyte_client_secret) with "
                    "connector_id or external_user_id for hosted mode, or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=LinearConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.issues = IssuesQuery(self)
        self.projects = ProjectsQuery(self)
        self.teams = TeamsQuery(self)
        self.users = UsersQuery(self)
        self.comments = CommentsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["list"],
        params: "IssuesListParams"
    ) -> "IssuesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["get"],
        params: "IssuesGetParams"
    ) -> "IssueResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["create"],
        params: "IssuesCreateParams"
    ) -> "IssueCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["update"],
        params: "IssuesUpdateParams"
    ) -> "IssueUpdateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["get"],
        params: "ProjectsGetParams"
    ) -> "ProjectResponse": ...

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
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "TeamResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "UserResponse": ...

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
        action: Literal["get"],
        params: "CommentsGetParams"
    ) -> "CommentResponse": ...

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
        action: Literal["update"],
        params: "CommentsUpdateParams"
    ) -> "CommentUpdateResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "search"],
        params: Mapping[str, Any]
    ) -> LinearExecuteResult[Any] | LinearExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "search"],
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
                return LinearExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return LinearExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> LinearCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            LinearCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return LinearCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return LinearCheckResult(
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
            @LinearConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @LinearConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    LinearConnectorModel,
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
        return describe_entities(LinearConnectorModel)

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
            (e for e in LinearConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in LinearConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await LinearConnector.create_hosted(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create_hosted(
        cls,
        *,
        external_user_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        auth_config: "LinearAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "LinearConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            external_user_id: Workspace identifier in Airbyte Cloud
            airbyte_client_id: Airbyte OAuth client ID
            airbyte_client_secret: Airbyte OAuth client secret
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).

        Returns:
            A LinearConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await LinearConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=LinearAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config
            credentials = auth_config.model_dump(exclude_none=True)
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(LinearConnectorModel.id),
                external_user_id=external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            airbyte_client_id=airbyte_client_id,
            airbyte_client_secret=airbyte_client_secret,
            connector_id=source_id,
        )



class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> IssuesListResult:
        """
        Returns a paginated list of issues via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            IssuesListResult
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        # Cast generic envelope to concrete typed result
        return IssuesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Get a single issue by ID via GraphQL

        Args:
            id: Issue ID
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result



    async def create(
        self,
        team_id: str,
        title: str,
        description: str | None = None,
        state_id: str | None = None,
        priority: int | None = None,
        **kwargs
    ) -> IssueCreateResponse:
        """
        Create a new issue via GraphQL mutation

        Args:
            team_id: The ID of the team to create the issue in
            title: The title of the issue
            description: The description of the issue (supports markdown)
            state_id: The ID of the workflow state for the issue
            priority: The priority of the issue (0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low)
            **kwargs: Additional parameters

        Returns:
            IssueCreateResponse
        """
        params = {k: v for k, v in {
            "teamId": team_id,
            "title": title,
            "description": description,
            "stateId": state_id,
            "priority": priority,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "create", params)
        return result



    async def update(
        self,
        id: str | None = None,
        title: str | None = None,
        description: str | None = None,
        state_id: str | None = None,
        priority: int | None = None,
        assignee_id: str | None = None,
        **kwargs
    ) -> IssueUpdateResponse:
        """
        Update an existing issue via GraphQL mutation. All fields except id are optional for partial updates.
To assign a user, provide assigneeId with the user's ID (get user IDs from the users list).
Omit assigneeId to leave the current assignee unchanged.


        Args:
            id: The ID of the issue to update
            title: The new title of the issue
            description: The new description of the issue (supports markdown)
            state_id: The ID of the new workflow state for the issue
            priority: The new priority of the issue (0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low)
            assignee_id: The ID of the user to assign to this issue. Get user IDs from the users list.
            **kwargs: Additional parameters

        Returns:
            IssueUpdateResponse
        """
        params = {k: v for k, v in {
            "id": id,
            "title": title,
            "description": description,
            "stateId": state_id,
            "priority": priority,
            "assigneeId": assignee_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "update", params)
        return result



    async def search(
        self,
        query: IssuesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IssuesSearchResult:
        """
        Search issues records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IssuesSearchFilter):
        - added_to_cycle_at: 
        - added_to_project_at: 
        - added_to_team_at: 
        - assignee: 
        - assignee_id: 
        - attachment_ids: 
        - attachments: 
        - branch_name: 
        - canceled_at: 
        - completed_at: 
        - created_at: 
        - creator: 
        - creator_id: 
        - customer_ticket_count: 
        - cycle: 
        - cycle_id: 
        - description: 
        - description_state: 
        - due_date: 
        - estimate: 
        - id: 
        - identifier: 
        - integration_source_type: 
        - label_ids: 
        - labels: 
        - milestone_id: 
        - number: 
        - parent: 
        - parent_id: 
        - previous_identifiers: 
        - priority: 
        - priority_label: 
        - priority_sort_order: 
        - project: 
        - project_id: 
        - project_milestone: 
        - reaction_data: 
        - relation_ids: 
        - relations: 
        - sla_type: 
        - sort_order: 
        - source_comment_id: 
        - started_at: 
        - state: 
        - state_id: 
        - sub_issue_sort_order: 
        - subscriber_ids: 
        - subscribers: 
        - team: 
        - team_id: 
        - title: 
        - updated_at: 
        - url: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IssuesSearchResult with hits (list of AirbyteSearchHit[IssuesSearchData]) and pagination info

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

        result = await self._connector.execute("issues", "search", params)

        # Parse response into typed result
        return IssuesSearchResult(
            hits=[
                AirbyteSearchHit[IssuesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=IssuesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> ProjectsListResult:
        """
        Returns a paginated list of projects via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            ProjectsListResult
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProjectResponse:
        """
        Get a single project by ID via GraphQL

        Args:
            id: Project ID
            **kwargs: Additional parameters

        Returns:
            ProjectResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        return result



    async def search(
        self,
        query: ProjectsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProjectsSearchResult:
        """
        Search projects records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProjectsSearchFilter):
        - canceled_at: 
        - color: 
        - completed_at: 
        - completed_issue_count_history: 
        - completed_scope_history: 
        - content: 
        - content_state: 
        - converted_from_issue: 
        - converted_from_issue_id: 
        - created_at: 
        - creator: 
        - creator_id: 
        - description: 
        - health: 
        - health_updated_at: 
        - icon: 
        - id: 
        - in_progress_scope_history: 
        - issue_count_history: 
        - lead: 
        - lead_id: 
        - name: 
        - priority: 
        - priority_sort_order: 
        - progress: 
        - scope: 
        - scope_history: 
        - slug_id: 
        - sort_order: 
        - start_date: 
        - started_at: 
        - status: 
        - status_id: 
        - target_date: 
        - team_ids: 
        - teams: 
        - update_reminders_day: 
        - update_reminders_hour: 
        - updated_at: 
        - url: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProjectsSearchResult with hits (list of AirbyteSearchHit[ProjectsSearchData]) and pagination info

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

        result = await self._connector.execute("projects", "search", params)

        # Parse response into typed result
        return ProjectsSearchResult(
            hits=[
                AirbyteSearchHit[ProjectsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ProjectsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> TeamsListResult:
        """
        Returns a list of teams via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            TeamsListResult
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> TeamResponse:
        """
        Get a single team by ID via GraphQL

        Args:
            id: Team ID
            **kwargs: Additional parameters

        Returns:
            TeamResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        return result



    async def search(
        self,
        query: TeamsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TeamsSearchResult:
        """
        Search teams records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TeamsSearchFilter):
        - active_cycle: 
        - active_cycle_id: 
        - auto_archive_period: 
        - auto_close_period: 
        - auto_close_state_id: 
        - color: 
        - created_at: 
        - cycle_calender_url: 
        - cycle_cooldown_time: 
        - cycle_duration: 
        - cycle_issue_auto_assign_completed: 
        - cycle_issue_auto_assign_started: 
        - cycle_lock_to_active: 
        - cycle_start_day: 
        - cycles_enabled: 
        - default_issue_estimate: 
        - default_issue_state: 
        - default_issue_state_id: 
        - group_issue_history: 
        - icon: 
        - id: 
        - invite_hash: 
        - issue_count: 
        - issue_estimation_allow_zero: 
        - issue_estimation_extended: 
        - issue_estimation_type: 
        - key: 
        - marked_as_duplicate_workflow_state: 
        - marked_as_duplicate_workflow_state_id: 
        - name: 
        - parent_team_id: 
        - private: 
        - require_priority_to_leave_triage: 
        - scim_managed: 
        - set_issue_sort_order_on_state_change: 
        - timezone: 
        - triage_enabled: 
        - triage_issue_state_id: 
        - upcoming_cycle_count: 
        - updated_at: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TeamsSearchResult with hits (list of AirbyteSearchHit[TeamsSearchData]) and pagination info

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

        result = await self._connector.execute("teams", "search", params)

        # Parse response into typed result
        return TeamsSearchResult(
            hits=[
                AirbyteSearchHit[TeamsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TeamsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a paginated list of users in the organization via GraphQL

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> UserResponse:
        """
        Get a single user by ID via GraphQL

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            UserResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



    async def search(
        self,
        query: UsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> UsersSearchResult:
        """
        Search users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (UsersSearchFilter):
        - active: 
        - admin: 
        - avatar_background_color: 
        - avatar_url: 
        - created_at: 
        - created_issue_count: 
        - display_name: 
        - email: 
        - guest: 
        - id: 
        - initials: 
        - invite_hash: 
        - is_me: 
        - last_seen: 
        - name: 
        - team_ids: 
        - teams: 
        - timezone: 
        - updated_at: 
        - url: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UsersSearchResult with hits (list of AirbyteSearchHit[UsersSearchData]) and pagination info

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

        result = await self._connector.execute("users", "search", params)

        # Parse response into typed result
        return UsersSearchResult(
            hits=[
                AirbyteSearchHit[UsersSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=UsersSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        issue_id: str,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> CommentsListResult:
        """
        Returns a paginated list of comments for an issue via GraphQL

        Args:
            issue_id: Issue ID to get comments for
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            CommentsListResult
        """
        params = {k: v for k, v in {
            "issueId": issue_id,
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "list", params)
        # Cast generic envelope to concrete typed result
        return CommentsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> CommentResponse:
        """
        Get a single comment by ID via GraphQL

        Args:
            id: Comment ID
            **kwargs: Additional parameters

        Returns:
            CommentResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "get", params)
        return result



    async def create(
        self,
        issue_id: str,
        body: str,
        **kwargs
    ) -> CommentCreateResponse:
        """
        Create a new comment on an issue via GraphQL mutation

        Args:
            issue_id: The ID of the issue to add the comment to
            body: The comment content in markdown
            **kwargs: Additional parameters

        Returns:
            CommentCreateResponse
        """
        params = {k: v for k, v in {
            "issueId": issue_id,
            "body": body,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "create", params)
        return result



    async def update(
        self,
        body: str,
        id: str | None = None,
        **kwargs
    ) -> CommentUpdateResponse:
        """
        Update an existing comment via GraphQL mutation

        Args:
            id: The ID of the comment to update
            body: The new comment content in markdown
            **kwargs: Additional parameters

        Returns:
            CommentUpdateResponse
        """
        params = {k: v for k, v in {
            "id": id,
            "body": body,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "update", params)
        return result



    async def search(
        self,
        query: CommentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CommentsSearchResult:
        """
        Search comments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CommentsSearchFilter):
        - body: 
        - body_data: 
        - created_at: 
        - edited_at: 
        - id: 
        - issue: 
        - issue_id: 
        - parent: 
        - parent_comment_id: 
        - resolving_comment_id: 
        - resolving_user_id: 
        - updated_at: 
        - url: 
        - user: 
        - user_id: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CommentsSearchResult with hits (list of AirbyteSearchHit[CommentsSearchData]) and pagination info

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

        result = await self._connector.execute("comments", "search", params)

        # Parse response into typed result
        return CommentsSearchResult(
            hits=[
                AirbyteSearchHit[CommentsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CommentsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )
