"""
Auto-generated asana connector. Do not edit manually.

Generated from OpenAPI specification.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from ._vendored.connector_sdk import save_download

if TYPE_CHECKING:
    from .types import (
        ProjectResponse,
        ProjectsGetParams,
        ProjectsList,
        ProjectsListParams,
        TaskResponse,
        TasksGetParams,
        TasksList,
        TasksListParams,
        UserResponse,
        UsersGetParams,
        UsersList,
        UsersListParams,
        WorkspaceResponse,
        WorkspacesGetParams,
        WorkspacesList,
        WorkspacesListParams,
        AsanaAuthConfig,
    )


class AsanaConnector:
    """
    Type-safe Asana API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "asana"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

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
            connector = AsanaConnector(auth_config={"api_key": "sk_..."})
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
                auth_config={"access_token": "...", "refresh_token": "..."},
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
                auth_config=auth_config,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.tasks = TasksQuery(self)
        self.projects = ProjectsQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.users = UsersQuery(self)

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
    ) -> "TasksList": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["get"],
        params: "TasksGetParams"
    ) -> "TaskResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsList": ...

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
        entity: Literal["workspaces"],
        action: Literal["list"],
        params: "WorkspacesListParams"
    ) -> "WorkspacesList": ...

    @overload
    async def execute(
        self,
        entity: Literal["workspaces"],
        action: Literal["get"],
        params: "WorkspacesGetParams"
    ) -> "WorkspaceResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersList": ...

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
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> dict[str, Any]: ...

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

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

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
        project_gid: str,
        limit: int | None = None,
        offset: str | None = None,
        **kwargs
    ) -> TasksList:
        """
        List tasks from a project

        Args:
            project_gid: Project GID to list tasks from
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            TasksList
        """
        params = {k: v for k, v in {
            "project_gid": project_gid,
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("tasks", "list", params)



    async def get(
        self,
        task_gid: str,
        **kwargs
    ) -> TaskResponse:
        """
        Get a task

        Args:
            task_gid: Task GID
            **kwargs: Additional parameters

        Returns:
            TaskResponse
        """
        params = {k: v for k, v in {
            "task_gid": task_gid,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("tasks", "get", params)



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
        **kwargs
    ) -> ProjectsList:
        """
        List projects

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            workspace: The workspace to filter projects on
            **kwargs: Additional parameters

        Returns:
            ProjectsList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "workspace": workspace,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("projects", "list", params)



    async def get(
        self,
        project_gid: str,
        **kwargs
    ) -> ProjectResponse:
        """
        Get a project

        Args:
            project_gid: Project GID
            **kwargs: Additional parameters

        Returns:
            ProjectResponse
        """
        params = {k: v for k, v in {
            "project_gid": project_gid,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("projects", "get", params)



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
    ) -> WorkspacesList:
        """
        List workspaces

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            **kwargs: Additional parameters

        Returns:
            WorkspacesList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("workspaces", "list", params)



    async def get(
        self,
        workspace_gid: str,
        **kwargs
    ) -> WorkspaceResponse:
        """
        Get a workspace

        Args:
            workspace_gid: Workspace GID
            **kwargs: Additional parameters

        Returns:
            WorkspaceResponse
        """
        params = {k: v for k, v in {
            "workspace_gid": workspace_gid,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("workspaces", "get", params)



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
        **kwargs
    ) -> UsersList:
        """
        List users

        Args:
            limit: Number of items to return per page
            offset: Pagination offset token
            workspace: The workspace to filter users on
            **kwargs: Additional parameters

        Returns:
            UsersList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "workspace": workspace,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "list", params)



    async def get(
        self,
        user_gid: str,
        **kwargs
    ) -> UserResponse:
        """
        Get a user

        Args:
            user_gid: User GID
            **kwargs: Additional parameters

        Returns:
            UserResponse
        """
        params = {k: v for k, v in {
            "user_gid": user_gid,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "get", params)


