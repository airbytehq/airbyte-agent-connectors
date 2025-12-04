"""
gong connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

if TYPE_CHECKING:
    from .types import (
        AsyncIterator,
        CallAudioDownloadParams,
        CallAudioDownloadParamsContentselector,
        CallAudioDownloadParamsFilter,
        CallTranscriptsListParams,
        CallTranscriptsListParamsFilter,
        CallTranscriptsListResult,
        CallVideoDownloadParams,
        CallVideoDownloadParamsContentselector,
        CallVideoDownloadParamsFilter,
        CallsExtensiveListParams,
        CallsExtensiveListParamsContentselector,
        CallsExtensiveListParamsFilter,
        CallsExtensiveListResult,
        CallsGetParams,
        CallsGetResult,
        CallsListParams,
        CallsListResult,
        StatsActivityAggregateListParams,
        StatsActivityAggregateListParamsFilter,
        StatsActivityAggregateListResult,
        StatsActivityDayByDayListParams,
        StatsActivityDayByDayListParamsFilter,
        StatsActivityDayByDayListResult,
        StatsInteractionListParams,
        StatsInteractionListParamsFilter,
        StatsInteractionListResult,
        UsersGetParams,
        UsersGetResult,
        UsersListParams,
        UsersListResult,
        WorkspacesListParams,
        WorkspacesListResult,
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

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("users", "list"): True,
        ("users", "get"): True,
        ("calls", "list"): True,
        ("calls", "get"): True,
        ("calls_extensive", "list"): True,
        ("call_audio", "download"): False,
        ("call_video", "download"): False,
        ("workspaces", "list"): True,
        ("call_transcripts", "list"): True,
        ("stats_activity_aggregate", "list"): True,
        ("stats_activity_day_by_day", "list"): True,
        ("stats_interaction", "list"): True,
    }

    def __init__(
        self,
        auth_config: GongAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new gong connector instance.

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
            connector = GongConnector(auth_config={"api_key": "sk_..."})
            # Hosted mode (executed on Airbyte cloud)
            connector = GongConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GongConnector(
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
        self.users = UsersQuery(self)
        self.calls = CallsQuery(self)
        self.calls_extensive = CallsExtensiveQuery(self)
        self.call_audio = CallAudioQuery(self)
        self.call_video = CallVideoQuery(self)
        self.workspaces = WorkspacesQuery(self)
        self.call_transcripts = CallTranscriptsQuery(self)
        self.stats_activity_aggregate = StatsActivityAggregateQuery(self)
        self.stats_activity_day_by_day = StatsActivityDayByDayQuery(self)
        self.stats_interaction = StatsInteractionQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["calls"],
        action: Literal["list"],
        params: "CallsListParams"
    ) -> "CallsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["get"],
        params: "CallsGetParams"
    ) -> "CallsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls_extensive"],
        action: Literal["list"],
        params: "CallsExtensiveListParams"
    ) -> "CallsExtensiveListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["call_audio"],
        action: Literal["download"],
        params: "CallAudioDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["call_video"],
        action: Literal["download"],
        params: "CallVideoDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

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
        entity: Literal["call_transcripts"],
        action: Literal["list"],
        params: "CallTranscriptsListParams"
    ) -> "CallTranscriptsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_activity_aggregate"],
        action: Literal["list"],
        params: "StatsActivityAggregateListParams"
    ) -> "StatsActivityAggregateListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_activity_day_by_day"],
        action: Literal["list"],
        params: "StatsActivityDayByDayListParams"
    ) -> "StatsActivityDayByDayListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_interaction"],
        action: Literal["list"],
        params: "StatsInteractionListParams"
    ) -> "StatsInteractionListResult": ...


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

        # Check if this operation has extractors configured
        has_extractors = self._EXTRACTOR_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return envelope with data and meta
            envelope: dict[str, Any] = {"data": result.data}
            if result.meta is not None:
                envelope["meta"] = result.meta
            return envelope
        else:
            # No extractors - return raw response data
            return result.data



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a list of all users in the Gong account

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "list", params)



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> UsersGetResult:
        """
        Get a single user by ID

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            UsersGetResult
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("users", "get", params)



class CallsQuery:
    """
    Query class for Calls entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        fromDateTime: str | None = None,
        toDateTime: str | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> CallsListResult:
        """
        Retrieve calls data by date range

        Args:
            fromDateTime: Start date in ISO 8601 format
            toDateTime: End date in ISO 8601 format
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallsListResult
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
        id: str | None = None,
        **kwargs
    ) -> CallsGetResult:
        """
        Get specific call data by ID

        Args:
            id: Call ID
            **kwargs: Additional parameters

        Returns:
            CallsGetResult
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls", "get", params)



class CallsExtensiveQuery:
    """
    Query class for CallsExtensive entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: CallsExtensiveListParamsFilter | None = None,
        contentSelector: CallsExtensiveListParamsContentselector | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> CallsExtensiveListResult:
        """
        Retrieve detailed call data including participants, interaction stats, and content

        Args:
            filter: Parameter filter
            contentSelector: Select which content to include in the response
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallsExtensiveListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "contentSelector": contentSelector,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("calls_extensive", "list", params)



class CallAudioQuery:
    """
    Query class for CallAudio entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        filter: CallAudioDownloadParamsFilter | None = None,
        contentSelector: CallAudioDownloadParamsContentselector | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the audio media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


        Args:
            filter: Parameter filter
            contentSelector: Parameter contentSelector
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "filter": filter,
            "contentSelector": contentSelector,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_audio", "download", params)


    async def download_local(
        self,
        path: str,
        filter: CallAudioDownloadParamsFilter | None = None,
        contentSelector: CallAudioDownloadParamsContentselector | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the audio media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}
 and save to file.

        Args:
            filter: Parameter filter
            contentSelector: Parameter contentSelector
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            filter=filter,
            contentSelector=contentSelector,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class CallVideoQuery:
    """
    Query class for CallVideo entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        filter: CallVideoDownloadParamsFilter | None = None,
        contentSelector: CallVideoDownloadParamsContentselector | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the video media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


        Args:
            filter: Parameter filter
            contentSelector: Parameter contentSelector
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "filter": filter,
            "contentSelector": contentSelector,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_video", "download", params)


    async def download_local(
        self,
        path: str,
        filter: CallVideoDownloadParamsFilter | None = None,
        contentSelector: CallVideoDownloadParamsContentselector | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the video media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}
 and save to file.

        Args:
            filter: Parameter filter
            contentSelector: Parameter contentSelector
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            filter=filter,
            contentSelector=contentSelector,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class WorkspacesQuery:
    """
    Query class for Workspaces entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> WorkspacesListResult:
        """
        List all company workspaces

        Returns:
            WorkspacesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("workspaces", "list", params)



class CallTranscriptsQuery:
    """
    Query class for CallTranscripts entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: CallTranscriptsListParamsFilter | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> CallTranscriptsListResult:
        """
        Returns transcripts for calls in a specified date range or specific call IDs

        Args:
            filter: Parameter filter
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallTranscriptsListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("call_transcripts", "list", params)



class StatsActivityAggregateQuery:
    """
    Query class for StatsActivityAggregate entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: StatsActivityAggregateListParamsFilter | None = None,
        **kwargs
    ) -> StatsActivityAggregateListResult:
        """
        Provides aggregated user activity metrics across a specified period

        Args:
            filter: Parameter filter
            **kwargs: Additional parameters

        Returns:
            StatsActivityAggregateListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_activity_aggregate", "list", params)



class StatsActivityDayByDayQuery:
    """
    Query class for StatsActivityDayByDay entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: StatsActivityDayByDayListParamsFilter | None = None,
        **kwargs
    ) -> StatsActivityDayByDayListResult:
        """
        Delivers daily user activity metrics across a specified date range

        Args:
            filter: Parameter filter
            **kwargs: Additional parameters

        Returns:
            StatsActivityDayByDayListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_activity_day_by_day", "list", params)



class StatsInteractionQuery:
    """
    Query class for StatsInteraction entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: StatsInteractionListParamsFilter | None = None,
        **kwargs
    ) -> StatsInteractionListResult:
        """
        Returns interaction stats for users based on calls that have Whisper turned on

        Args:
            filter: Parameter filter
            **kwargs: Additional parameters

        Returns:
            StatsInteractionListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("stats_interaction", "list", params)


