"""
Auto-generated gong connector. Do not edit manually.

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
        ActivityAggregateResponse,
        ActivityDayByDayResponse,
        CallResponse,
        CallTranscriptsListParams,
        CallsExtensiveListParams,
        CallsGetParams,
        CallsListParams,
        CallsResponse,
        ExtensiveCallsResponse,
        InteractionStatsResponse,
        StatsActivityAggregateListParams,
        StatsActivityDayByDayListParams,
        StatsInteractionListParams,
        TranscriptsResponse,
        UserResponse,
        UsersGetParams,
        UsersListParams,
        UsersResponse,
        WorkspacesListParams,
        WorkspacesResponse,
        GongAuthConfig,
    )


class GongConnector:
    """
    Type-safe Gong API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "gong"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(self, executor: ExecutorProtocol):
        """Initialize connector with an executor."""
        self._executor = executor
        self.users = UsersQuery(self)
        self.calls = CallsQuery(self)
        self.calls_extensive = CallsextensiveQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.call_transcripts = CalltranscriptsQuery(self)
        self.stats_activity_aggregate = StatsactivityaggregateQuery(self)
        self.stats_activity_day_by_day = StatsactivitydaybydayQuery(self)
        self.stats_interaction = StatsinteractionQuery(self)

    @classmethod
    def create(
        cls,
        auth_config: Optional[GongAuthConfig] = None,
        config_path: Optional[str] = None,
        connector_id: Optional[str] = None,
        airbyte_client_id: Optional[str] = None,
        airbyte_client_secret: Optional[str] = None,
        airbyte_connector_api_url: Optional[str] = None,
        on_token_refresh: Optional[Any] = None    ) -> Self:
        """
        Create a new gong connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Returns:
            Configured GongConnector instance

        Examples:
            # Local mode (direct API calls)
            connector = GongConnector.create(auth_config={"api_key": "sk_..."})
            # Hosted mode (executed on Airbyte cloud)
            connector = GongConnector.create(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GongConnector.create(
                auth_config={"access_token": "...", "refresh_token": "..."},
                on_token_refresh=save_tokens
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

        # Local mode: auth_config required
        if not auth_config:
            raise ValueError(
                "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                "or auth_config for local mode"
            )

        from ._vendored.connector_sdk.executor import LocalExecutor

        if not config_path:
            config_path = str(cls.get_default_config_path())

        # Build config_values dict from server variables
        config_values = None

        executor = LocalExecutor(
            config_path=config_path,
            auth_config=auth_config,
            config_values=config_values,
            on_token_refresh=on_token_refresh
        )
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
        resource: Literal["users"],
        verb: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersResponse": ...
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
        resource: Literal["calls"],
        verb: Literal["list"],
        params: "CallsListParams"
    ) -> "CallsResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["calls"],
        verb: Literal["get"],
        params: "CallsGetParams"
    ) -> "CallResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["calls_extensive"],
        verb: Literal["list"],
        params: "CallsExtensiveListParams"
    ) -> "ExtensiveCallsResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["workspaces"],
        verb: Literal["list"],
        params: "WorkspacesListParams"
    ) -> "WorkspacesResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["call_transcripts"],
        verb: Literal["list"],
        params: "CallTranscriptsListParams"
    ) -> "TranscriptsResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["stats_activity_aggregate"],
        verb: Literal["list"],
        params: "StatsActivityAggregateListParams"
    ) -> "ActivityAggregateResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["stats_activity_day_by_day"],
        verb: Literal["list"],
        params: "StatsActivityDayByDayListParams"
    ) -> "ActivityDayByDayResponse": ...
    @overload
    async def execute(
        self,
        resource: Literal["stats_interaction"],
        verb: Literal["list"],
        params: "StatsInteractionListParams"
    ) -> "InteractionStatsResponse": ...

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



class UsersQuery:
    """
    Query class for Users resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: Optional[str] = None,
        **kwargs
    ) -> "UsersResponse":
        """
        List users

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            UsersResponse
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "UserResponse":
        """
        Get a user

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

        return await self._connector.execute("users", "get", params)
class CallsQuery:
    """
    Query class for Calls resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        fromDateTime: str,
        toDateTime: str,
        cursor: Optional[str] = None,
        **kwargs
    ) -> "CallsResponse":
        """
        List calls

        Args:
            fromDateTime: Start date in ISO 8601 format
            toDateTime: End date in ISO 8601 format
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallsResponse
        """
        params = {k: v for k, v in {
            "fromDateTime": fromDateTime,
            "toDateTime": toDateTime,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "CallResponse":
        """
        Get a call

        Args:
            id: Call ID
            **kwargs: Additional parameters

        Returns:
            CallResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls", "get", params)
class CallsextensiveQuery:
    """
    Query class for Callsextensive resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "ExtensiveCallsResponse":
        """
        List calls with extensive data

        Returns:
            ExtensiveCallsResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls_extensive", "list", params)
class WorkspacesQuery:
    """
    Query class for Workspaces resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "WorkspacesResponse":
        """
        List workspaces

        Returns:
            WorkspacesResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("workspaces", "list", params)
class CalltranscriptsQuery:
    """
    Query class for Calltranscripts resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "TranscriptsResponse":
        """
        Retrieve call transcripts

        Returns:
            TranscriptsResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_transcripts", "list", params)
class StatsactivityaggregateQuery:
    """
    Query class for Statsactivityaggregate resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "ActivityAggregateResponse":
        """
        Retrieve aggregated activity statistics

        Returns:
            ActivityAggregateResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_activity_aggregate", "list", params)
class StatsactivitydaybydayQuery:
    """
    Query class for Statsactivitydaybyday resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "ActivityDayByDayResponse":
        """
        Retrieve daily activity statistics

        Returns:
            ActivityDayByDayResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_activity_day_by_day", "list", params)
class StatsinteractionQuery:
    """
    Query class for Statsinteraction resource operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "InteractionStatsResponse":
        """
        Retrieve interaction statistics

        Returns:
            InteractionStatsResponse
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_interaction", "list", params)