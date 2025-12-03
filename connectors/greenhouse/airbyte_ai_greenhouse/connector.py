"""
Auto-generated greenhouse connector. Do not edit manually.

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
        Application,
        ApplicationsGetParams,
        ApplicationsListParams,
        Candidate,
        CandidatesGetParams,
        CandidatesListParams,
        Job,
        JobsGetParams,
        JobsListParams,
        GreenhouseAuthConfig,
    )


class GreenhouseConnector:
    """
    Type-safe Greenhouse API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "greenhouse"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(
        self,
        auth_config: GreenhouseAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new greenhouse connector instance.

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
            connector = GreenhouseConnector(auth_config={"api_key": "sk_..."})
            # Hosted mode (executed on Airbyte cloud)
            connector = GreenhouseConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GreenhouseConnector(
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
        self.candidates = CandidatesQuery(self)
        self.applications = ApplicationsQuery(self)
        self.jobs = JobsQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["list"],
        params: "CandidatesListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["get"],
        params: "CandidatesGetParams"
    ) -> "Candidate": ...

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["list"],
        params: "ApplicationsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["get"],
        params: "ApplicationsGetParams"
    ) -> "Application": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["list"],
        params: "JobsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["get"],
        params: "JobsGetParams"
    ) -> "Job": ...


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



class CandidatesQuery:
    """
    Query class for Candidates entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        List candidates

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("candidates", "list", params)



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Candidate:
        """
        Get a candidate

        Args:
            id: Candidate ID
            **kwargs: Additional parameters

        Returns:
            Candidate
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("candidates", "get", params)



class ApplicationsQuery:
    """
    Query class for Applications entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        last_activity_after: str | None = None,
        job_id: int | None = None,
        status: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        List applications

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by applications created before this timestamp
            created_after: Filter by applications created after this timestamp
            last_activity_after: Filter by applications with activity after this timestamp
            job_id: Filter by job ID
            status: Filter by application status
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "last_activity_after": last_activity_after,
            "job_id": job_id,
            "status": status,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("applications", "list", params)



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Application:
        """
        Get an application

        Args:
            id: Application ID
            **kwargs: Additional parameters

        Returns:
            Application
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("applications", "get", params)



class JobsQuery:
    """
    Query class for Jobs entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        List jobs

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("jobs", "list", params)



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Job:
        """
        Get a job

        Args:
            id: Job ID
            **kwargs: Additional parameters

        Returns:
            Job
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("jobs", "get", params)


