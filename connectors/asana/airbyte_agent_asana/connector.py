"""
Asana connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import AsanaConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    AttachmentsListParams,
    ProjectSectionsListParams,
    ProjectTasksListParams,
    ProjectsGetParams,
    ProjectsListParams,
    SectionsGetParams,
    TagsGetParams,
    TaskDependenciesListParams,
    TaskDependentsListParams,
    TaskProjectsListParams,
    TaskSubtasksListParams,
    TasksGetParams,
    TasksListParams,
    TeamProjectsListParams,
    TeamUsersListParams,
    TeamsGetParams,
    UserTeamsListParams,
    UsersGetParams,
    UsersListParams,
    WorkspaceProjectsListParams,
    WorkspaceTagsListParams,
    WorkspaceTaskSearchListParams,
    WorkspaceTeamsListParams,
    WorkspaceUsersListParams,
    WorkspacesGetParams,
    WorkspacesListParams,
    AirbyteSearchParams,
    AttachmentsSearchFilter,
    AttachmentsSearchQuery,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    SectionsSearchFilter,
    SectionsSearchQuery,
    TagsSearchFilter,
    TagsSearchQuery,
    TasksSearchFilter,
    TasksSearchQuery,
    TeamsSearchFilter,
    TeamsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    WorkspacesSearchFilter,
    WorkspacesSearchQuery,
)
if TYPE_CHECKING:
    from .models import AsanaAuthConfig

# Import specific auth config classes for multi-auth isinstance checks
from .models import AsanaOauth2AuthConfig, AsanaPersonalAccessTokenAuthConfig
# Import response models and envelope models at runtime
from .models import (
    AsanaCheckResult,
    AsanaExecuteResult,
    AsanaExecuteResultWithMeta,
    TasksListResult,
    ProjectTasksListResult,
    WorkspaceTaskSearchListResult,
    ProjectsListResult,
    TaskProjectsListResult,
    TeamProjectsListResult,
    WorkspaceProjectsListResult,
    WorkspacesListResult,
    UsersListResult,
    WorkspaceUsersListResult,
    TeamUsersListResult,
    WorkspaceTeamsListResult,
    UserTeamsListResult,
    AttachmentsListResult,
    WorkspaceTagsListResult,
    ProjectSectionsListResult,
    TaskSubtasksListResult,
    TaskDependenciesListResult,
    TaskDependentsListResult,
    Attachment,
    AttachmentCompact,
    Project,
    ProjectCompact,
    Section,
    SectionCompact,
    Tag,
    TagCompact,
    Task,
    TaskCompact,
    Team,
    TeamCompact,
    User,
    UserCompact,
    Workspace,
    WorkspaceCompact,
    AirbyteSearchHit,
    AirbyteSearchResult,
    AttachmentsSearchData,
    AttachmentsSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    SectionsSearchData,
    SectionsSearchResult,
    TagsSearchData,
    TagsSearchResult,
    TasksSearchData,
    TasksSearchResult,
    TeamsSearchData,
    TeamsSearchResult,
    UsersSearchData,
    UsersSearchResult,
    WorkspacesSearchData,
    WorkspacesSearchResult,
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




class AsanaConnector:
    """
    Type-safe Asana API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "asana"
    connector_version = "0.1.10"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("tasks", "list"): True,
        ("project_tasks", "list"): True,
        ("tasks", "get"): None,
        ("workspace_task_search", "list"): True,
        ("projects", "list"): True,
        ("projects", "get"): None,
        ("task_projects", "list"): True,
        ("team_projects", "list"): True,
        ("workspace_projects", "list"): True,
        ("workspaces", "list"): True,
        ("workspaces", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("workspace_users", "list"): True,
        ("team_users", "list"): True,
        ("teams", "get"): None,
        ("workspace_teams", "list"): True,
        ("user_teams", "list"): True,
        ("attachments", "list"): True,
        ("attachments", "get"): None,
        ("attachments", "download"): None,
        ("workspace_tags", "list"): True,
        ("tags", "get"): None,
        ("project_sections", "list"): True,
        ("sections", "get"): None,
        ("task_subtasks", "list"): True,
        ("task_dependencies", "list"): True,
        ("task_dependents", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('tasks', 'list'): {'limit': 'limit', 'offset': 'offset', 'project': 'project', 'workspace': 'workspace', 'section': 'section', 'assignee': 'assignee', 'completed_since': 'completed_since', 'modified_since': 'modified_since'},
        ('project_tasks', 'list'): {'project_gid': 'project_gid', 'limit': 'limit', 'offset': 'offset', 'completed_since': 'completed_since'},
        ('tasks', 'get'): {'task_gid': 'task_gid'},
        ('workspace_task_search', 'list'): {'workspace_gid': 'workspace_gid', 'limit': 'limit', 'offset': 'offset', 'text': 'text', 'completed': 'completed', 'assignee_any': 'assignee.any', 'projects_any': 'projects.any', 'sections_any': 'sections.any', 'teams_any': 'teams.any', 'followers_any': 'followers.any', 'created_at_after': 'created_at.after', 'created_at_before': 'created_at.before', 'modified_at_after': 'modified_at.after', 'modified_at_before': 'modified_at.before', 'due_on_after': 'due_on.after', 'due_on_before': 'due_on.before', 'resource_subtype': 'resource_subtype', 'sort_by': 'sort_by', 'sort_ascending': 'sort_ascending'},
        ('projects', 'list'): {'limit': 'limit', 'offset': 'offset', 'workspace': 'workspace', 'team': 'team', 'archived': 'archived'},
        ('projects', 'get'): {'project_gid': 'project_gid'},
        ('task_projects', 'list'): {'task_gid': 'task_gid', 'limit': 'limit', 'offset': 'offset'},
        ('team_projects', 'list'): {'team_gid': 'team_gid', 'limit': 'limit', 'offset': 'offset', 'archived': 'archived'},
        ('workspace_projects', 'list'): {'workspace_gid': 'workspace_gid', 'limit': 'limit', 'offset': 'offset', 'archived': 'archived'},
        ('workspaces', 'list'): {'limit': 'limit', 'offset': 'offset'},
        ('workspaces', 'get'): {'workspace_gid': 'workspace_gid'},
        ('users', 'list'): {'limit': 'limit', 'offset': 'offset', 'workspace': 'workspace', 'team': 'team'},
        ('users', 'get'): {'user_gid': 'user_gid'},
        ('workspace_users', 'list'): {'workspace_gid': 'workspace_gid', 'limit': 'limit', 'offset': 'offset'},
        ('team_users', 'list'): {'team_gid': 'team_gid', 'limit': 'limit', 'offset': 'offset'},
        ('teams', 'get'): {'team_gid': 'team_gid'},
        ('workspace_teams', 'list'): {'workspace_gid': 'workspace_gid', 'limit': 'limit', 'offset': 'offset'},
        ('user_teams', 'list'): {'user_gid': 'user_gid', 'organization': 'organization', 'limit': 'limit', 'offset': 'offset'},
        ('attachments', 'list'): {'parent': 'parent', 'limit': 'limit', 'offset': 'offset'},
        ('attachments', 'get'): {'attachment_gid': 'attachment_gid'},
        ('attachments', 'download'): {'attachment_gid': 'attachment_gid', 'range_header': 'range_header'},
        ('workspace_tags', 'list'): {'workspace_gid': 'workspace_gid', 'limit': 'limit', 'offset': 'offset'},
        ('tags', 'get'): {'tag_gid': 'tag_gid'},
        ('project_sections', 'list'): {'project_gid': 'project_gid', 'limit': 'limit', 'offset': 'offset'},
        ('sections', 'get'): {'section_gid': 'section_gid'},
        ('task_subtasks', 'list'): {'task_gid': 'task_gid', 'limit': 'limit', 'offset': 'offset'},
        ('task_dependencies', 'list'): {'task_gid': 'task_gid', 'limit': 'limit', 'offset': 'offset'},
        ('task_dependents', 'list'): {'task_gid': 'task_gid', 'limit': 'limit', 'offset': 'offset'},
    }

    def __init__(
        self,
        auth_config: AsanaAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new asana connector instance.

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
            connector = AsanaConnector(auth_config=AsanaAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = AsanaConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = AsanaConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = AsanaConnector(
                auth_config=AsanaAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(AsanaConnectorModel.id) if not connector_id else None,
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

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, AsanaOauth2AuthConfig):
                    auth_scheme = "oauth2"
                if isinstance(auth_config, AsanaPersonalAccessTokenAuthConfig):
                    auth_scheme = "personalAccessToken"

            self._executor = LocalExecutor(
                model=AsanaConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.tasks = TasksQuery(self)
        self.project_tasks = ProjectTasksQuery(self)
        self.workspace_task_search = WorkspaceTaskSearchQuery(self)
        self.projects = ProjectsQuery(self)
        self.task_projects = TaskProjectsQuery(self)
        self.team_projects = TeamProjectsQuery(self)
        self.workspace_projects = WorkspaceProjectsQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.users = UsersQuery(self)
        self.workspace_users = WorkspaceUsersQuery(self)
        self.team_users = TeamUsersQuery(self)
        self.teams = TeamsQuery(self)
        self.workspace_teams = WorkspaceTeamsQuery(self)
        self.user_teams = UserTeamsQuery(self)
        self.attachments = AttachmentsQuery(self)
        self.workspace_tags = WorkspaceTagsQuery(self)
        self.tags = TagsQuery(self)
        self.project_sections = ProjectSectionsQuery(self)
        self.sections = SectionsQuery(self)
        self.task_subtasks = TaskSubtasksQuery(self)
        self.task_dependencies = TaskDependenciesQuery(self)
        self.task_dependents = TaskDependentsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["project_tasks"],
        action: Literal["list"],
        params: "ProjectTasksListParams"
    ) -> "ProjectTasksListResult": ...

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
        entity: Literal["workspace_task_search"],
        action: Literal["list"],
        params: "WorkspaceTaskSearchListParams"
    ) -> "WorkspaceTaskSearchListResult": ...

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
    ) -> "Project": ...

    @overload
    async def execute(
        self,
        entity: Literal["task_projects"],
        action: Literal["list"],
        params: "TaskProjectsListParams"
    ) -> "TaskProjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["team_projects"],
        action: Literal["list"],
        params: "TeamProjectsListParams"
    ) -> "TeamProjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspace_projects"],
        action: Literal["list"],
        params: "WorkspaceProjectsListParams"
    ) -> "WorkspaceProjectsListResult": ...

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
        entity: Literal["workspaces"],
        action: Literal["get"],
        params: "WorkspacesGetParams"
    ) -> "Workspace": ...

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
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspace_users"],
        action: Literal["list"],
        params: "WorkspaceUsersListParams"
    ) -> "WorkspaceUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["team_users"],
        action: Literal["list"],
        params: "TeamUsersListParams"
    ) -> "TeamUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "Team": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspace_teams"],
        action: Literal["list"],
        params: "WorkspaceTeamsListParams"
    ) -> "WorkspaceTeamsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["user_teams"],
        action: Literal["list"],
        params: "UserTeamsListParams"
    ) -> "UserTeamsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["list"],
        params: "AttachmentsListParams"
    ) -> "AttachmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["get"],
        params: "AttachmentsGetParams"
    ) -> "Attachment": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["download"],
        params: "AttachmentsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspace_tags"],
        action: Literal["list"],
        params: "WorkspaceTagsListParams"
    ) -> "WorkspaceTagsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tags"],
        action: Literal["get"],
        params: "TagsGetParams"
    ) -> "Tag": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_sections"],
        action: Literal["list"],
        params: "ProjectSectionsListParams"
    ) -> "ProjectSectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sections"],
        action: Literal["get"],
        params: "SectionsGetParams"
    ) -> "Section": ...

    @overload
    async def execute(
        self,
        entity: Literal["task_subtasks"],
        action: Literal["list"],
        params: "TaskSubtasksListParams"
    ) -> "TaskSubtasksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["task_dependencies"],
        action: Literal["list"],
        params: "TaskDependenciesListParams"
    ) -> "TaskDependenciesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["task_dependents"],
        action: Literal["list"],
        params: "TaskDependentsListParams"
    ) -> "TaskDependentsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download", "search"],
        params: Mapping[str, Any]
    ) -> AsanaExecuteResult[Any] | AsanaExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download", "search"],
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
                return AsanaExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return AsanaExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> AsanaCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            AsanaCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return AsanaCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return AsanaCheckResult(
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
            @AsanaConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @AsanaConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    AsanaConnectorModel,
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
        return describe_entities(AsanaConnectorModel)

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
            (e for e in AsanaConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in AsanaConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await AsanaConnector.create_hosted(...)
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
        auth_config: "AsanaAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "AsanaConnector":
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
            A AsanaConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await AsanaConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=AsanaAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
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
                connector_definition_id=str(AsanaConnectorModel.id),
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



class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: str | None = None,
        project: str | None = None,
        workspace: str | None = None,
        section: str | None = None,
        assignee: str | None = None,
        completed_since: str | None = None,
        modified_since: str | None = None,
        **kwargs
    ) -> TasksListResult:
        """
        Returns a paginated list of tasks. Must include either a project OR a section OR a workspace AND assignee parameter.

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            project: The project to filter tasks on
            workspace: The workspace to filter tasks on
            section: The workspace to filter tasks on
            assignee: The assignee to filter tasks on
            completed_since: Only return tasks that have been completed since this time
            modified_since: Only return tasks that have been completed since this time
            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "project": project,
            "workspace": workspace,
            "section": section,
            "assignee": assignee,
            "completed_since": completed_since,
            "modified_since": modified_since,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TasksListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        task_gid: str,
        **kwargs
    ) -> Task:
        """
        Get a single task by its ID

        Args:
            task_gid: Task GID
            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def search(
        self,
        query: TasksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TasksSearchResult:
        """
        Search tasks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TasksSearchFilter):
        - actual_time_minutes: The actual time spent on the task in minutes
        - approval_status: 
        - assignee: 
        - completed: 
        - completed_at: 
        - completed_by: 
        - created_at: 
        - custom_fields: 
        - dependencies: 
        - dependents: 
        - due_at: 
        - due_on: 
        - external: 
        - followers: 
        - gid: 
        - hearted: 
        - hearts: 
        - html_notes: 
        - is_rendered_as_separator: 
        - liked: 
        - likes: 
        - memberships: 
        - modified_at: 
        - name: 
        - notes: 
        - num_hearts: 
        - num_likes: 
        - num_subtasks: 
        - parent: 
        - permalink_url: 
        - projects: 
        - resource_subtype: 
        - resource_type: 
        - start_on: 
        - tags: 
        - workspace: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TasksSearchResult with hits (list of AirbyteSearchHit[TasksSearchData]) and pagination info

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

        result = await self._connector.execute("tasks", "search", params)

        # Parse response into typed result
        return TasksSearchResult(
            hits=[
                AirbyteSearchHit[TasksSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TasksSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ProjectTasksQuery:
    """
    Query class for ProjectTasks entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        completed_since: str | None = None,
        **kwargs
    ) -> ProjectTasksListResult:
        """
        Returns all tasks in a project

        Args:
            project_gid: Project GID to list tasks from
            limit: Number of items to return per page
            offset: Pagination offset token
            completed_since: Only return tasks that have been completed since this time
            **kwargs: Additional parameters

        Returns:
            ProjectTasksListResult
        """
        params = {k: v for k, v in {
            "project_gid": project_gid,
            "limit": limit,
            "offset": offset,
            "completed_since": completed_since,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectTasksListResult(
            data=result.data,
            meta=result.meta
        )



class WorkspaceTaskSearchQuery:
    """
    Query class for WorkspaceTaskSearch entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        text: str | None = None,
        completed: bool | None = None,
        assignee_any: str | None = None,
        projects_any: str | None = None,
        sections_any: str | None = None,
        teams_any: str | None = None,
        followers_any: str | None = None,
        created_at_after: str | None = None,
        created_at_before: str | None = None,
        modified_at_after: str | None = None,
        modified_at_before: str | None = None,
        due_on_after: str | None = None,
        due_on_before: str | None = None,
        resource_subtype: str | None = None,
        sort_by: str | None = None,
        sort_ascending: bool | None = None,
        **kwargs
    ) -> WorkspaceTaskSearchListResult:
        """
        Returns tasks that match the specified search criteria. This endpoint requires a premium Asana account.

IMPORTANT: At least one search filter parameter must be provided. Valid filter parameters include: text, completed, assignee.any, projects.any, sections.any, teams.any, followers.any, created_at.after, created_at.before, modified_at.after, modified_at.before, due_on.after, due_on.before, and resource_subtype. The sort_by and sort_ascending parameters are for ordering results and do not count as search filters.


        Args:
            workspace_gid: Workspace GID to search tasks in
            limit: Number of items to return per page
            offset: Pagination offset token
            text: Search text to filter tasks
            completed: Filter by completion status
            assignee_any: Comma-separated list of assignee GIDs
            projects_any: Comma-separated list of project GIDs
            sections_any: Comma-separated list of section GIDs
            teams_any: Comma-separated list of team GIDs
            followers_any: Comma-separated list of follower GIDs
            created_at_after: Filter tasks created after this date (ISO 8601 format)
            created_at_before: Filter tasks created before this date (ISO 8601 format)
            modified_at_after: Filter tasks modified after this date (ISO 8601 format)
            modified_at_before: Filter tasks modified before this date (ISO 8601 format)
            due_on_after: Filter tasks due after this date (ISO 8601 date format)
            due_on_before: Filter tasks due before this date (ISO 8601 date format)
            resource_subtype: Filter by task resource subtype (e.g., default_task, milestone)
            sort_by: Field to sort by (e.g., created_at, modified_at, due_date)
            sort_ascending: Sort order (true for ascending, false for descending)
            **kwargs: Additional parameters

        Returns:
            WorkspaceTaskSearchListResult
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            "limit": limit,
            "offset": offset,
            "text": text,
            "completed": completed,
            "assignee.any": assignee_any,
            "projects.any": projects_any,
            "sections.any": sections_any,
            "teams.any": teams_any,
            "followers.any": followers_any,
            "created_at.after": created_at_after,
            "created_at.before": created_at_before,
            "modified_at.after": modified_at_after,
            "modified_at.before": modified_at_before,
            "due_on.after": due_on_after,
            "due_on.before": due_on_before,
            "resource_subtype": resource_subtype,
            "sort_by": sort_by,
            "sort_ascending": sort_ascending,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspace_task_search", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspaceTaskSearchListResult(
            data=result.data,
            meta=result.meta
        )



class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: str | None = None,
        workspace: str | None = None,
        team: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> ProjectsListResult:
        """
        Returns a paginated list of projects

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            workspace: The workspace to filter projects on
            team: The team to filter projects on
            archived: Filter by archived status
            **kwargs: Additional parameters

        Returns:
            ProjectsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "workspace": workspace,
            "team": team,
            "archived": archived,
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
        project_gid: str,
        **kwargs
    ) -> Project:
        """
        Get a single project by its ID

        Args:
            project_gid: Project GID
            **kwargs: Additional parameters

        Returns:
            Project
        """
        params = {k: v for k, v in {
            "project_gid": project_gid,
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
        - archived: 
        - color: 
        - created_at: 
        - current_status: 
        - custom_field_settings: 
        - custom_fields: 
        - default_view: 
        - due_date: 
        - due_on: 
        - followers: 
        - gid: 
        - html_notes: 
        - icon: 
        - is_template: 
        - members: 
        - modified_at: 
        - name: 
        - notes: 
        - owner: 
        - permalink_url: 
        - public: 
        - resource_type: 
        - start_on: 
        - team: 
        - workspace: 

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

class TaskProjectsQuery:
    """
    Query class for TaskProjects entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        task_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> TaskProjectsListResult:
        """
        Returns all projects a task is in

        Args:
            task_gid: Task GID to list projects from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            TaskProjectsListResult
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("task_projects", "list", params)
        # Cast generic envelope to concrete typed result
        return TaskProjectsListResult(
            data=result.data,
            meta=result.meta
        )



class TeamProjectsQuery:
    """
    Query class for TeamProjects entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        team_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> TeamProjectsListResult:
        """
        Returns all projects for a team

        Args:
            team_gid: Team GID to list projects from
            limit: Number of items to return per page
            offset: Pagination offset token
            archived: Filter by archived status
            **kwargs: Additional parameters

        Returns:
            TeamProjectsListResult
        """
        params = {k: v for k, v in {
            "team_gid": team_gid,
            "limit": limit,
            "offset": offset,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("team_projects", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamProjectsListResult(
            data=result.data,
            meta=result.meta
        )



class WorkspaceProjectsQuery:
    """
    Query class for WorkspaceProjects entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> WorkspaceProjectsListResult:
        """
        Returns all projects in a workspace

        Args:
            workspace_gid: Workspace GID to list projects from
            limit: Number of items to return per page
            offset: Pagination offset token
            archived: Filter by archived status
            **kwargs: Additional parameters

        Returns:
            WorkspaceProjectsListResult
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            "limit": limit,
            "offset": offset,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspace_projects", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspaceProjectsListResult(
            data=result.data,
            meta=result.meta
        )



class WorkspacesQuery:
    """
    Query class for Workspaces entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> WorkspacesListResult:
        """
        Returns a paginated list of workspaces

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            WorkspacesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspaces", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspacesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        workspace_gid: str,
        **kwargs
    ) -> Workspace:
        """
        Get a single workspace by its ID

        Args:
            workspace_gid: Workspace GID
            **kwargs: Additional parameters

        Returns:
            Workspace
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspaces", "get", params)
        return result



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
        - email_domains: 
        - gid: 
        - is_organization: 
        - name: 
        - resource_type: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            WorkspacesSearchResult with hits (list of AirbyteSearchHit[WorkspacesSearchData]) and pagination info

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
        return WorkspacesSearchResult(
            hits=[
                AirbyteSearchHit[WorkspacesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=WorkspacesSearchData(**hit.get("data", {}))
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

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: str | None = None,
        workspace: str | None = None,
        team: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a paginated list of users

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            workspace: The workspace to filter users on
            team: The team to filter users on
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "workspace": workspace,
            "team": team,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        user_gid: str,
        **kwargs
    ) -> User:
        """
        Get a single user by their ID

        Args:
            user_gid: User GID
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "user_gid": user_gid,
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
        - email: 
        - gid: 
        - name: 
        - photo: 
        - resource_type: 
        - workspaces: 

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

class WorkspaceUsersQuery:
    """
    Query class for WorkspaceUsers entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> WorkspaceUsersListResult:
        """
        Returns all users in a workspace

        Args:
            workspace_gid: Workspace GID to list users from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            WorkspaceUsersListResult
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspace_users", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspaceUsersListResult(
            data=result.data,
            meta=result.meta
        )



class TeamUsersQuery:
    """
    Query class for TeamUsers entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        team_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> TeamUsersListResult:
        """
        Returns all users in a team

        Args:
            team_gid: Team GID to list users from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            TeamUsersListResult
        """
        params = {k: v for k, v in {
            "team_gid": team_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("team_users", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamUsersListResult(
            data=result.data,
            meta=result.meta
        )



class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        team_gid: str,
        **kwargs
    ) -> Team:
        """
        Get a single team by its ID

        Args:
            team_gid: Team GID
            **kwargs: Additional parameters

        Returns:
            Team
        """
        params = {k: v for k, v in {
            "team_gid": team_gid,
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
        - description: 
        - gid: 
        - html_description: 
        - name: 
        - organization: 
        - permalink_url: 
        - resource_type: 

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

class WorkspaceTeamsQuery:
    """
    Query class for WorkspaceTeams entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> WorkspaceTeamsListResult:
        """
        Returns all teams in a workspace

        Args:
            workspace_gid: Workspace GID to list teams from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            WorkspaceTeamsListResult
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspace_teams", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspaceTeamsListResult(
            data=result.data,
            meta=result.meta
        )



class UserTeamsQuery:
    """
    Query class for UserTeams entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        user_gid: str,
        organization: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> UserTeamsListResult:
        """
        Returns all teams a user is a member of

        Args:
            user_gid: User GID to list teams from
            organization: The workspace or organization to filter teams on
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            UserTeamsListResult
        """
        params = {k: v for k, v in {
            "user_gid": user_gid,
            "organization": organization,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("user_teams", "list", params)
        # Cast generic envelope to concrete typed result
        return UserTeamsListResult(
            data=result.data,
            meta=result.meta
        )



class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        parent: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> AttachmentsListResult:
        """
        Returns a list of attachments for an object (task, project, etc.)

        Args:
            parent: Globally unique identifier for the object to fetch attachments for (e.g., a task GID)
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            AttachmentsListResult
        """
        params = {k: v for k, v in {
            "parent": parent,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "list", params)
        # Cast generic envelope to concrete typed result
        return AttachmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        attachment_gid: str,
        **kwargs
    ) -> Attachment:
        """
        Get details for a single attachment by its GID

        Args:
            attachment_gid: Globally unique identifier for the attachment
            **kwargs: Additional parameters

        Returns:
            Attachment
        """
        params = {k: v for k, v in {
            "attachment_gid": attachment_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        return result



    async def download(
        self,
        attachment_gid: str,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the file content of an attachment. This operation first retrieves the attachment
metadata to get the download_url, then downloads the file from that URL.


        Args:
            attachment_gid: Globally unique identifier for the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "attachment_gid": attachment_gid,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_local(
        self,
        attachment_gid: str,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the file content of an attachment. This operation first retrieves the attachment
metadata to get the download_url, then downloads the file from that URL.
 and save to file.

        Args:
            attachment_gid: Globally unique identifier for the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            attachment_gid=attachment_gid,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


    async def search(
        self,
        query: AttachmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AttachmentsSearchResult:
        """
        Search attachments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AttachmentsSearchFilter):
        - connected_to_app: 
        - created_at: 
        - download_url: 
        - gid: 
        - host: 
        - name: 
        - parent: 
        - permanent_url: 
        - resource_subtype: 
        - resource_type: 
        - size: 
        - view_url: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AttachmentsSearchResult with hits (list of AirbyteSearchHit[AttachmentsSearchData]) and pagination info

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

        result = await self._connector.execute("attachments", "search", params)

        # Parse response into typed result
        return AttachmentsSearchResult(
            hits=[
                AirbyteSearchHit[AttachmentsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=AttachmentsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class WorkspaceTagsQuery:
    """
    Query class for WorkspaceTags entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> WorkspaceTagsListResult:
        """
        Returns all tags in a workspace

        Args:
            workspace_gid: Workspace GID to list tags from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            WorkspaceTagsListResult
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspace_tags", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspaceTagsListResult(
            data=result.data,
            meta=result.meta
        )



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        tag_gid: str,
        **kwargs
    ) -> Tag:
        """
        Get a single tag by its ID

        Args:
            tag_gid: Tag GID
            **kwargs: Additional parameters

        Returns:
            Tag
        """
        params = {k: v for k, v in {
            "tag_gid": tag_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "get", params)
        return result



    async def search(
        self,
        query: TagsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TagsSearchResult:
        """
        Search tags records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TagsSearchFilter):
        - color: 
        - followers: 
        - gid: 
        - name: 
        - permalink_url: 
        - resource_type: 
        - workspace: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TagsSearchResult with hits (list of AirbyteSearchHit[TagsSearchData]) and pagination info

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

        result = await self._connector.execute("tags", "search", params)

        # Parse response into typed result
        return TagsSearchResult(
            hits=[
                AirbyteSearchHit[TagsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TagsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ProjectSectionsQuery:
    """
    Query class for ProjectSections entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> ProjectSectionsListResult:
        """
        Returns all sections in a project

        Args:
            project_gid: Project GID to list sections from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            ProjectSectionsListResult
        """
        params = {k: v for k, v in {
            "project_gid": project_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_sections", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectSectionsListResult(
            data=result.data,
            meta=result.meta
        )



class SectionsQuery:
    """
    Query class for Sections entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        section_gid: str,
        **kwargs
    ) -> Section:
        """
        Get a single section by its ID

        Args:
            section_gid: Section GID
            **kwargs: Additional parameters

        Returns:
            Section
        """
        params = {k: v for k, v in {
            "section_gid": section_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sections", "get", params)
        return result



    async def search(
        self,
        query: SectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SectionsSearchResult:
        """
        Search sections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SectionsSearchFilter):
        - created_at: 
        - gid: 
        - name: 
        - project: 
        - resource_type: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SectionsSearchResult with hits (list of AirbyteSearchHit[SectionsSearchData]) and pagination info

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

        result = await self._connector.execute("sections", "search", params)

        # Parse response into typed result
        return SectionsSearchResult(
            hits=[
                AirbyteSearchHit[SectionsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=SectionsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class TaskSubtasksQuery:
    """
    Query class for TaskSubtasks entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        task_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> TaskSubtasksListResult:
        """
        Returns all subtasks of a task

        Args:
            task_gid: Task GID to list subtasks from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            TaskSubtasksListResult
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("task_subtasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TaskSubtasksListResult(
            data=result.data,
            meta=result.meta
        )



class TaskDependenciesQuery:
    """
    Query class for TaskDependencies entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        task_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> TaskDependenciesListResult:
        """
        Returns all tasks that this task depends on

        Args:
            task_gid: Task GID to list dependencies from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            TaskDependenciesListResult
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("task_dependencies", "list", params)
        # Cast generic envelope to concrete typed result
        return TaskDependenciesListResult(
            data=result.data,
            meta=result.meta
        )



class TaskDependentsQuery:
    """
    Query class for TaskDependents entity operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        task_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> TaskDependentsListResult:
        """
        Returns all tasks that depend on this task

        Args:
            task_gid: Task GID to list dependents from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            TaskDependentsListResult
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("task_dependents", "list", params)
        # Cast generic envelope to concrete typed result
        return TaskDependentsListResult(
            data=result.data,
            meta=result.meta
        )


