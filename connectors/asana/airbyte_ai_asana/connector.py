"""
asana connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    AttachmentsListParams,
    ProjectTasksListParams,
    ProjectsGetParams,
    ProjectsListParams,
    TaskProjectsListParams,
    TasksGetParams,
    TasksListParams,
    TeamProjectsListParams,
    TeamUsersListParams,
    TeamsGetParams,
    UserTeamsListParams,
    UsersGetParams,
    UsersListParams,
    WorkspaceProjectsListParams,
    WorkspaceTaskSearchListParams,
    WorkspaceTeamsListParams,
    WorkspaceUsersListParams,
    WorkspacesGetParams,
    WorkspacesListParams,
)

if TYPE_CHECKING:
    from .models import AsanaAuthConfig
# Import response models and envelope models at runtime
from .models import (
    AsanaExecuteResult,
    AsanaExecuteResultWithMeta,
    TasksListResult,
    ProjectTasksListResult,
    TasksGetResult,
    WorkspaceTaskSearchListResult,
    ProjectsListResult,
    ProjectsGetResult,
    TaskProjectsListResult,
    TeamProjectsListResult,
    WorkspaceProjectsListResult,
    WorkspacesListResult,
    WorkspacesGetResult,
    UsersListResult,
    UsersGetResult,
    WorkspaceUsersListResult,
    TeamUsersListResult,
    TeamsGetResult,
    WorkspaceTeamsListResult,
    UserTeamsListResult,
    AttachmentsListResult,
    AttachmentsGetResult,
)


class AsanaConnector:
    """
    Type-safe Asana API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "asana"
    connector_version = "0.1.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("tasks", "list"): True,
        ("project_tasks", "list"): True,
        ("tasks", "get"): True,
        ("workspace_task_search", "list"): True,
        ("projects", "list"): True,
        ("projects", "get"): True,
        ("task_projects", "list"): True,
        ("team_projects", "list"): True,
        ("workspace_projects", "list"): True,
        ("workspaces", "list"): True,
        ("workspaces", "get"): True,
        ("users", "list"): True,
        ("users", "get"): True,
        ("workspace_users", "list"): True,
        ("team_users", "list"): True,
        ("teams", "get"): True,
        ("workspace_teams", "list"): True,
        ("user_teams", "list"): True,
        ("attachments", "list"): True,
        ("attachments", "get"): True,
        ("attachments", "download"): False,
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
    }

    def __init__(
        self,
        auth_config: AsanaAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new asana connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            airbyte_connector_api_url: Airbyte connector API URL (defaults to Airbyte Cloud API URL)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = AsanaConnector(auth_config=AsanaAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = AsanaConnector(
                connector_id="connector-456",
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
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            if not config_path:
                config_path = str(self.get_default_config_path())

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
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

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

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
    ) -> "TasksGetResult": ...

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
    ) -> "ProjectsGetResult": ...

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
    ) -> "WorkspacesGetResult": ...

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
    ) -> "UsersGetResult": ...

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
    ) -> "TeamsGetResult": ...

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
    ) -> "AttachmentsGetResult": ...

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
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> AsanaExecuteResult[Any] | AsanaExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None
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
        if params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                params = {param_map.get(k, k): v for k, v in params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._EXTRACTOR_MAP.get((entity, action), False)

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
        Returns a paginated list of tasks

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
            meta=result.meta        )



    async def get(
        self,
        task_gid: str,
        **kwargs
    ) -> TasksGetResult:
        """
        Get a single task by its ID

        Args:
            task_gid: Task GID
            **kwargs: Additional parameters

        Returns:
            TasksGetResult
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        # Cast generic envelope to concrete typed result
        return TasksGetResult(
            data=result.data        )



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
            meta=result.meta        )



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
        Returns tasks that match the specified search criteria. Note - This endpoint requires a premium Asana account.

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
            meta=result.meta        )



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
            meta=result.meta        )



    async def get(
        self,
        project_gid: str,
        **kwargs
    ) -> ProjectsGetResult:
        """
        Get a single project by its ID

        Args:
            project_gid: Project GID
            **kwargs: Additional parameters

        Returns:
            ProjectsGetResult
        """
        params = {k: v for k, v in {
            "project_gid": project_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        # Cast generic envelope to concrete typed result
        return ProjectsGetResult(
            data=result.data        )



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
            meta=result.meta        )



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
            meta=result.meta        )



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
            meta=result.meta        )



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
            meta=result.meta        )



    async def get(
        self,
        workspace_gid: str,
        **kwargs
    ) -> WorkspacesGetResult:
        """
        Get a single workspace by its ID

        Args:
            workspace_gid: Workspace GID
            **kwargs: Additional parameters

        Returns:
            WorkspacesGetResult
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("workspaces", "get", params)
        # Cast generic envelope to concrete typed result
        return WorkspacesGetResult(
            data=result.data        )



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
            meta=result.meta        )



    async def get(
        self,
        user_gid: str,
        **kwargs
    ) -> UsersGetResult:
        """
        Get a single user by their ID

        Args:
            user_gid: User GID
            **kwargs: Additional parameters

        Returns:
            UsersGetResult
        """
        params = {k: v for k, v in {
            "user_gid": user_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        # Cast generic envelope to concrete typed result
        return UsersGetResult(
            data=result.data        )



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
            meta=result.meta        )



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
            meta=result.meta        )



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
    ) -> TeamsGetResult:
        """
        Get a single team by its ID

        Args:
            team_gid: Team GID
            **kwargs: Additional parameters

        Returns:
            TeamsGetResult
        """
        params = {k: v for k, v in {
            "team_gid": team_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        # Cast generic envelope to concrete typed result
        return TeamsGetResult(
            data=result.data        )



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
            meta=result.meta        )



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
            meta=result.meta        )



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
            meta=result.meta        )



    async def get(
        self,
        attachment_gid: str,
        **kwargs
    ) -> AttachmentsGetResult:
        """
        Get details for a single attachment by its GID

        Args:
            attachment_gid: Globally unique identifier for the attachment
            **kwargs: Additional parameters

        Returns:
            AttachmentsGetResult
        """
        params = {k: v for k, v in {
            "attachment_gid": attachment_gid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        # Cast generic envelope to concrete typed result
        return AttachmentsGetResult(
            data=result.data        )



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

