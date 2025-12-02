"""
Auto-generated linear connector. Do not edit manually.

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
        IssueResponse,
        IssuesGetParams,
        IssuesListParams,
        IssuesListResponse,
        ProjectResponse,
        ProjectsGetParams,
        ProjectsListParams,
        ProjectsListResponse,
        TeamResponse,
        TeamsGetParams,
        TeamsListParams,
        TeamsListResponse,
    )


class LinearConnector:
    """
    Type-safe Linear API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "linear"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(self, executor: ExecutorProtocol):
        """Initialize connector with an executor."""
        self._executor = executor
        self.issues = IssuesQuery(self)
        self.projects = ProjectsQuery(self)
        self.teams = TeamsQuery(self)

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
        Create a new linear connector instance.

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
            Configured LinearConnector instance

        Examples:
            # Local mode (direct API calls)
            connector = LinearConnector.create(secrets={"api_key": "sk_..."})

            # Hosted mode (executed on Airbyte cloud)
            connector = LinearConnector.create(
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
        resource: Literal["issues"],
        verb: Literal["list"],
        params: "IssuesListParams"
    ) -> "IssuesListResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["issues"],
        verb: Literal["get"],
        params: "IssuesGetParams"
    ) -> "IssueResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["projects"],
        verb: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsListResponse": ...
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
        resource: Literal["teams"],
        verb: Literal["list"],
        params: "TeamsListParams"
    ) -> "TeamsListResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["teams"],
        verb: Literal["get"],
        params: "TeamsGetParams"
    ) -> "TeamResponse": ...

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



class IssuesQuery:
    """
    Query class for Issues resource operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: Optional[int] = None,
        after: Optional[str] = None,
        **kwargs
    ) -> "IssuesListResponse":
        """
        List issues

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            IssuesListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("issues", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "IssueResponse":
        """
        Get an issue

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

        return await self._connector.execute("issues", "get", params)
class ProjectsQuery:
    """
    Query class for Projects resource operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: Optional[int] = None,
        after: Optional[str] = None,
        **kwargs
    ) -> "ProjectsListResponse":
        """
        List projects

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            ProjectsListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("projects", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "ProjectResponse":
        """
        Get a project

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

        return await self._connector.execute("projects", "get", params)
class TeamsQuery:
    """
    Query class for Teams resource operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: Optional[int] = None,
        after: Optional[str] = None,
        **kwargs
    ) -> "TeamsListResponse":
        """
        List teams

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            TeamsListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("teams", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "TeamResponse":
        """
        Get a team

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

        return await self._connector.execute("teams", "get", params)