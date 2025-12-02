"""
Auto-generated asana connector. Do not edit manually.

Generated from OpenAPI specification.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Any, Dict, overload, Self
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from pathlib import Path

if TYPE_CHECKING:
    from ._vendored.connector_sdk.executor import ExecutorProtocol
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
    )


class AsanaConnector:
    """
    Type-safe Asana API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "asana"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(self, executor: ExecutorProtocol):
        """Initialize connector with an executor."""
        self._executor = executor
        self.tasks = TasksQuery(self)
        self.projects = ProjectsQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.users = UsersQuery(self)

    @classmethod
    def create(
        cls,
        secrets: Optional[dict[str, str]] = None,
        config_path: Optional[str] = None,
        connector_id: Optional[str] = None,
        airbyte_client_id: Optional[str] = None,
        airbyte_client_secret: Optional[str] = None,
        airbyte_connector_api_url: Optional[str] = None    ) -> Self:
        """
        Create a new asana connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `secrets` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            secrets: API secrets/credentials (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
        Returns:
            Configured AsanaConnector instance

        Examples:
            # Local mode (direct API calls)
            connector = AsanaConnector.create(secrets={"api_key": "sk_..."})

            # Hosted mode (executed on Airbyte cloud)
            connector = AsanaConnector.create(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )
        """
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
            return cls(executor)

        # Local mode: secrets required
        if not secrets:
            raise ValueError(
                "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                "or secrets for local mode"
            )

        from ._vendored.connector_sdk.executor import LocalExecutor

        if not config_path:
            config_path = str(cls.get_default_config_path())

        executor = LocalExecutor(config_path=config_path, secrets=secrets)
        connector = cls(executor)

        # Update base_url with server variables if provided

        return connector

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====
    @overload
    async def execute(
        self,
        resource: Literal["tasks"],
        verb: Literal["list"],
        params: "TasksListParams"
    ) -> "TasksList": ...
    @overload
    async def execute(
        self,
        resource: Literal["tasks"],
        verb: Literal["get"],
        params: "TasksGetParams"
    ) -> "TaskResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["projects"],
        verb: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsList": ...
    @overload
    async def execute(
        self,
        resource: Literal["projects"],
        verb: Literal["get"],
        params: "ProjectsGetParams"
    ) -> "ProjectResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["workspaces"],
        verb: Literal["list"],
        params: "WorkspacesListParams"
    ) -> "WorkspacesList": ...
    @overload
    async def execute(
        self,
        resource: Literal["workspaces"],
        verb: Literal["get"],
        params: "WorkspacesGetParams"
    ) -> "WorkspaceResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["users"],
        verb: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersList": ...
    @overload
    async def execute(
        self,
        resource: Literal["users"],
        verb: Literal["get"],
        params: "UsersGetParams"
    ) -> "UserResponse": ...

    @overload
    async def execute(
        self,
        resource: str,
        verb: str,
        params: Dict[str, Any]
    ) -> Dict[str, Any]: ...

    async def execute(
        self,
        resource: str,
        verb: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Execute a resource operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for resource/verb/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            resource: Resource name (e.g., "customers")
            verb: Operation verb (e.g., "create", "get", "list")
            params: Operation parameters (typed based on resource+verb)

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                resource="customers",
                verb="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            resource=resource,
            verb=verb,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        return result.data



class TasksQuery:
    """
    Query class for Tasks resource operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_gid: str,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        **kwargs
    ) -> "TasksList":
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
    ) -> "TaskResponse":
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
    Query class for Projects resource operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        workspace: Optional[str] = None,
        **kwargs
    ) -> "ProjectsList":
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
    ) -> "ProjectResponse":
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
    Query class for Workspaces resource operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        **kwargs
    ) -> "WorkspacesList":
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
    ) -> "WorkspaceResponse":
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
    Query class for Users resource operations.
    """

    def __init__(self, connector: AsanaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        workspace: Optional[str] = None,
        **kwargs
    ) -> "UsersList":
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
    ) -> "UserResponse":
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