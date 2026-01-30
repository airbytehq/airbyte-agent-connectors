"""
Gong connector.
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

from .connector_model import GongConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    CallAudioDownloadParams,
    CallAudioDownloadParamsContentselector,
    CallAudioDownloadParamsFilter,
    CallTranscriptsListParams,
    CallTranscriptsListParamsFilter,
    CallVideoDownloadParams,
    CallVideoDownloadParamsContentselector,
    CallVideoDownloadParamsFilter,
    CallsExtensiveListParams,
    CallsExtensiveListParamsContentselector,
    CallsExtensiveListParamsFilter,
    CallsGetParams,
    CallsListParams,
    CoachingListParams,
    LibraryFolderContentListParams,
    LibraryFoldersListParams,
    SettingsScorecardsListParams,
    SettingsTrackersListParams,
    StatsActivityAggregateListParams,
    StatsActivityAggregateListParamsFilter,
    StatsActivityDayByDayListParams,
    StatsActivityDayByDayListParamsFilter,
    StatsActivityScorecardsListParams,
    StatsActivityScorecardsListParamsFilter,
    StatsInteractionListParams,
    StatsInteractionListParamsFilter,
    UsersGetParams,
    UsersListParams,
    WorkspacesListParams,
    AirbyteSearchParams,
    UsersSearchFilter,
    UsersSearchQuery,
    CallsSearchFilter,
    CallsSearchQuery,
    CallsExtensiveSearchFilter,
    CallsExtensiveSearchQuery,
    SettingsScorecardsSearchFilter,
    SettingsScorecardsSearchQuery,
    StatsActivityScorecardsSearchFilter,
    StatsActivityScorecardsSearchQuery,
)
if TYPE_CHECKING:
    from .models import GongAuthConfig

# Import specific auth config classes for multi-auth isinstance checks
from .models import GongOauth20AuthenticationAuthConfig, GongAccessKeyAuthenticationAuthConfig
# Import response models and envelope models at runtime
from .models import (
    GongCheckResult,
    GongExecuteResult,
    GongExecuteResultWithMeta,
    UsersListResult,
    CallsListResult,
    CallsExtensiveListResult,
    WorkspacesListResult,
    CallTranscriptsListResult,
    StatsActivityAggregateListResult,
    StatsActivityDayByDayListResult,
    StatsInteractionListResult,
    SettingsScorecardsListResult,
    SettingsTrackersListResult,
    LibraryFoldersListResult,
    LibraryFolderContentListResult,
    CoachingListResult,
    StatsActivityScorecardsListResult,
    AnsweredScorecard,
    Call,
    CallTranscript,
    CoachingData,
    ExtensiveCall,
    FolderCall,
    LibraryFolder,
    Scorecard,
    Tracker,
    User,
    UserAggregateActivity,
    UserDetailedActivity,
    UserInteractionStats,
    Workspace,
    AirbyteSearchHit,
    AirbyteSearchResult,
    UsersSearchData,
    UsersSearchResult,
    CallsSearchData,
    CallsSearchResult,
    CallsExtensiveSearchData,
    CallsExtensiveSearchResult,
    SettingsScorecardsSearchData,
    SettingsScorecardsSearchResult,
    StatsActivityScorecardsSearchData,
    StatsActivityScorecardsSearchResult,
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




class GongConnector:
    """
    Type-safe Gong API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "gong"
    connector_version = "0.1.14"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("users", "list"): True,
        ("users", "get"): None,
        ("calls", "list"): True,
        ("calls", "get"): None,
        ("calls_extensive", "list"): True,
        ("call_audio", "download"): None,
        ("call_video", "download"): None,
        ("workspaces", "list"): True,
        ("call_transcripts", "list"): True,
        ("stats_activity_aggregate", "list"): True,
        ("stats_activity_day_by_day", "list"): True,
        ("stats_interaction", "list"): True,
        ("settings_scorecards", "list"): True,
        ("settings_trackers", "list"): True,
        ("library_folders", "list"): True,
        ("library_folder_content", "list"): True,
        ("coaching", "list"): True,
        ("stats_activity_scorecards", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('users', 'list'): {'cursor': 'cursor'},
        ('users', 'get'): {'id': 'id'},
        ('calls', 'list'): {'from_date_time': 'fromDateTime', 'to_date_time': 'toDateTime', 'cursor': 'cursor'},
        ('calls', 'get'): {'id': 'id'},
        ('calls_extensive', 'list'): {'filter': 'filter', 'content_selector': 'contentSelector', 'cursor': 'cursor'},
        ('call_audio', 'download'): {'filter': 'filter', 'content_selector': 'contentSelector', 'range_header': 'range_header'},
        ('call_video', 'download'): {'filter': 'filter', 'content_selector': 'contentSelector', 'range_header': 'range_header'},
        ('call_transcripts', 'list'): {'filter': 'filter', 'cursor': 'cursor'},
        ('stats_activity_aggregate', 'list'): {'filter': 'filter'},
        ('stats_activity_day_by_day', 'list'): {'filter': 'filter'},
        ('stats_interaction', 'list'): {'filter': 'filter'},
        ('settings_scorecards', 'list'): {'workspace_id': 'workspaceId'},
        ('settings_trackers', 'list'): {'workspace_id': 'workspaceId'},
        ('library_folders', 'list'): {'workspace_id': 'workspaceId'},
        ('library_folder_content', 'list'): {'folder_id': 'folderId', 'cursor': 'cursor'},
        ('coaching', 'list'): {'workspace_id': 'workspace-id', 'manager_id': 'manager-id', 'from_': 'from', 'to': 'to'},
        ('stats_activity_scorecards', 'list'): {'filter': 'filter', 'cursor': 'cursor'},
    }

    def __init__(
        self,
        auth_config: GongAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new gong connector instance.

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
            connector = GongConnector(auth_config=GongAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GongConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = GongConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GongConnector(
                auth_config=GongAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(GongConnectorModel.id) if not connector_id else None,
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
                if isinstance(auth_config, GongOauth20AuthenticationAuthConfig):
                    auth_scheme = "oauth2"
                if isinstance(auth_config, GongAccessKeyAuthenticationAuthConfig):
                    auth_scheme = "basicAuth"

            self._executor = LocalExecutor(
                model=GongConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
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
        self.settings_scorecards = SettingsScorecardsQuery(self)
        self.settings_trackers = SettingsTrackersQuery(self)
        self.library_folders = LibraryFoldersQuery(self)
        self.library_folder_content = LibraryFolderContentQuery(self)
        self.coaching = CoachingQuery(self)
        self.stats_activity_scorecards = StatsActivityScorecardsQuery(self)

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
    ) -> "User": ...

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
    ) -> "Call": ...

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
        entity: Literal["settings_scorecards"],
        action: Literal["list"],
        params: "SettingsScorecardsListParams"
    ) -> "SettingsScorecardsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["settings_trackers"],
        action: Literal["list"],
        params: "SettingsTrackersListParams"
    ) -> "SettingsTrackersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["library_folders"],
        action: Literal["list"],
        params: "LibraryFoldersListParams"
    ) -> "LibraryFoldersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["library_folder_content"],
        action: Literal["list"],
        params: "LibraryFolderContentListParams"
    ) -> "LibraryFolderContentListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["coaching"],
        action: Literal["list"],
        params: "CoachingListParams"
    ) -> "CoachingListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["stats_activity_scorecards"],
        action: Literal["list"],
        params: "StatsActivityScorecardsListParams"
    ) -> "StatsActivityScorecardsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download", "search"],
        params: Mapping[str, Any]
    ) -> GongExecuteResult[Any] | GongExecuteResultWithMeta[Any, Any] | Any: ...

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
                return GongExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GongExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GongCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GongCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GongCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GongCheckResult(
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
            @GongConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GongConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GongConnectorModel,
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
        return describe_entities(GongConnectorModel)

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
            (e for e in GongConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GongConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GongConnector.create_hosted(...)
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
        auth_config: "GongAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "GongConnector":
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
            A GongConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await GongConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=GongAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
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
                connector_definition_id=str(GongConnectorModel.id),
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

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> User:
        """
        Get a single user by ID

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            User
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
        - active: Indicates if the user is currently active or not
        - created: The timestamp denoting when the user account was created
        - email_address: The primary email address associated with the user
        - email_aliases: Additional email addresses that can be used to reach the user
        - extension: The phone extension number for the user
        - first_name: The first name of the user
        - id: Unique identifier for the user
        - last_name: The last name of the user
        - manager_id: The ID of the user's manager
        - meeting_consent_page_url: URL for the consent page related to meetings
        - personal_meeting_urls: URLs for personal meeting rooms assigned to the user
        - phone_number: The phone number associated with the user
        - settings: User-specific settings and configurations
        - spoken_languages: Languages spoken by the user
        - title: The job title or position of the user
        - trusted_email_address: An email address that is considered trusted for the user

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

class CallsQuery:
    """
    Query class for Calls entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        from_date_time: str | None = None,
        to_date_time: str | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> CallsListResult:
        """
        Retrieve calls data by date range

        Args:
            from_date_time: Start date in ISO 8601 format
            to_date_time: End date in ISO 8601 format
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallsListResult
        """
        params = {k: v for k, v in {
            "fromDateTime": from_date_time,
            "toDateTime": to_date_time,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "list", params)
        # Cast generic envelope to concrete typed result
        return CallsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Call:
        """
        Get specific call data by ID

        Args:
            id: Call ID
            **kwargs: Additional parameters

        Returns:
            Call
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "get", params)
        return result



    async def search(
        self,
        query: CallsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CallsSearchResult:
        """
        Search calls records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CallsSearchFilter):
        - calendar_event_id: Unique identifier for the calendar event associated with the call.
        - client_unique_id: Unique identifier for the client related to the call.
        - custom_data: Custom data associated with the call.
        - direction: Direction of the call (inbound/outbound).
        - duration: Duration of the call in seconds.
        - id: Unique identifier for the call.
        - is_private: Indicates if the call is private or not.
        - language: Language used in the call.
        - media: Media type used for communication (voice, video, etc.).
        - meeting_url: URL for accessing the meeting associated with the call.
        - primary_user_id: Unique identifier for the primary user involved in the call.
        - purpose: Purpose or topic of the call.
        - scheduled: Scheduled date and time of the call.
        - scope: Scope or extent of the call.
        - sdr_disposition: Disposition set by the sales development representative.
        - started: Start date and time of the call.
        - system: System information related to the call.
        - title: Title or headline of the call.
        - url: URL associated with the call.
        - workspace_id: Identifier for the workspace to which the call belongs.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CallsSearchResult with hits (list of AirbyteSearchHit[CallsSearchData]) and pagination info

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

        result = await self._connector.execute("calls", "search", params)

        # Parse response into typed result
        return CallsSearchResult(
            hits=[
                AirbyteSearchHit[CallsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CallsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class CallsExtensiveQuery:
    """
    Query class for CallsExtensive entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: CallsExtensiveListParamsFilter,
        content_selector: CallsExtensiveListParamsContentselector | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> CallsExtensiveListResult:
        """
        Retrieve detailed call data including participants, interaction stats, and content

        Args:
            filter: Parameter filter
            content_selector: Select which content to include in the response
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CallsExtensiveListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "contentSelector": content_selector,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls_extensive", "list", params)
        # Cast generic envelope to concrete typed result
        return CallsExtensiveListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CallsExtensiveSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CallsExtensiveSearchResult:
        """
        Search calls_extensive records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CallsExtensiveSearchFilter):
        - id: Unique identifier for the call (from metaData.id).
        - startdatetime: Datetime for extensive calls.
        - collaboration: Collaboration information added to the call
        - content: Analysis of the interaction content.
        - context: A list of the agenda of each part of the call.
        - interaction: Metrics collected around the interaction during the call.
        - media: The media urls of the call.
        - meta_data: call's metadata.
        - parties: A list of the call's participants

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CallsExtensiveSearchResult with hits (list of AirbyteSearchHit[CallsExtensiveSearchData]) and pagination info

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

        result = await self._connector.execute("calls_extensive", "search", params)

        # Parse response into typed result
        return CallsExtensiveSearchResult(
            hits=[
                AirbyteSearchHit[CallsExtensiveSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CallsExtensiveSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
        content_selector: CallAudioDownloadParamsContentselector | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the audio media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


        Args:
            filter: Parameter filter
            content_selector: Parameter contentSelector
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "filter": filter,
            "contentSelector": content_selector,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("call_audio", "download", params)
        return result


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
        content_selector: CallVideoDownloadParamsContentselector | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the video media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


        Args:
            filter: Parameter filter
            content_selector: Parameter contentSelector
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "filter": filter,
            "contentSelector": content_selector,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("call_video", "download", params)
        return result


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

        result = await self._connector.execute("workspaces", "list", params)
        # Cast generic envelope to concrete typed result
        return WorkspacesListResult(
            data=result.data
        )



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

        result = await self._connector.execute("call_transcripts", "list", params)
        # Cast generic envelope to concrete typed result
        return CallTranscriptsListResult(
            data=result.data,
            meta=result.meta
        )



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

        result = await self._connector.execute("stats_activity_aggregate", "list", params)
        # Cast generic envelope to concrete typed result
        return StatsActivityAggregateListResult(
            data=result.data,
            meta=result.meta
        )



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

        result = await self._connector.execute("stats_activity_day_by_day", "list", params)
        # Cast generic envelope to concrete typed result
        return StatsActivityDayByDayListResult(
            data=result.data,
            meta=result.meta
        )



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

        result = await self._connector.execute("stats_interaction", "list", params)
        # Cast generic envelope to concrete typed result
        return StatsInteractionListResult(
            data=result.data,
            meta=result.meta
        )



class SettingsScorecardsQuery:
    """
    Query class for SettingsScorecards entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_id: str | None = None,
        **kwargs
    ) -> SettingsScorecardsListResult:
        """
        Retrieve all scorecard configurations in the company

        Args:
            workspace_id: Filter scorecards by workspace ID
            **kwargs: Additional parameters

        Returns:
            SettingsScorecardsListResult
        """
        params = {k: v for k, v in {
            "workspaceId": workspace_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("settings_scorecards", "list", params)
        # Cast generic envelope to concrete typed result
        return SettingsScorecardsListResult(
            data=result.data
        )



    async def search(
        self,
        query: SettingsScorecardsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SettingsScorecardsSearchResult:
        """
        Search settings_scorecards records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SettingsScorecardsSearchFilter):
        - created: The timestamp when the scorecard was created
        - enabled: Indicates if the scorecard is enabled or disabled
        - questions: An array of questions related to the scorecard
        - scorecard_id: The unique identifier of the scorecard
        - scorecard_name: The name of the scorecard
        - updated: The timestamp when the scorecard was last updated
        - updater_user_id: The user ID of the person who last updated the scorecard
        - workspace_id: The unique identifier of the workspace associated with the scorecard

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SettingsScorecardsSearchResult with hits (list of AirbyteSearchHit[SettingsScorecardsSearchData]) and pagination info

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

        result = await self._connector.execute("settings_scorecards", "search", params)

        # Parse response into typed result
        return SettingsScorecardsSearchResult(
            hits=[
                AirbyteSearchHit[SettingsScorecardsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=SettingsScorecardsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class SettingsTrackersQuery:
    """
    Query class for SettingsTrackers entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_id: str | None = None,
        **kwargs
    ) -> SettingsTrackersListResult:
        """
        Retrieve all keyword tracker configurations in the company

        Args:
            workspace_id: Filter trackers by workspace ID
            **kwargs: Additional parameters

        Returns:
            SettingsTrackersListResult
        """
        params = {k: v for k, v in {
            "workspaceId": workspace_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("settings_trackers", "list", params)
        # Cast generic envelope to concrete typed result
        return SettingsTrackersListResult(
            data=result.data
        )



class LibraryFoldersQuery:
    """
    Query class for LibraryFolders entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_id: str,
        **kwargs
    ) -> LibraryFoldersListResult:
        """
        Retrieve the folder structure of the call library

        Args:
            workspace_id: Workspace ID to retrieve folders from
            **kwargs: Additional parameters

        Returns:
            LibraryFoldersListResult
        """
        params = {k: v for k, v in {
            "workspaceId": workspace_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("library_folders", "list", params)
        # Cast generic envelope to concrete typed result
        return LibraryFoldersListResult(
            data=result.data
        )



class LibraryFolderContentQuery:
    """
    Query class for LibraryFolderContent entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        folder_id: str,
        cursor: str | None = None,
        **kwargs
    ) -> LibraryFolderContentListResult:
        """
        Retrieve calls in a specific library folder

        Args:
            folder_id: Folder ID to retrieve content from
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            LibraryFolderContentListResult
        """
        params = {k: v for k, v in {
            "folderId": folder_id,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("library_folder_content", "list", params)
        # Cast generic envelope to concrete typed result
        return LibraryFolderContentListResult(
            data=result.data,
            meta=result.meta
        )



class CoachingQuery:
    """
    Query class for Coaching entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        workspace_id: str,
        manager_id: str,
        from_: str,
        to: str,
        **kwargs
    ) -> CoachingListResult:
        """
        Retrieve coaching metrics for a manager and their direct reports

        Args:
            workspace_id: Workspace ID
            manager_id: Manager user ID
            from_: Start date in ISO 8601 format
            to: End date in ISO 8601 format
            **kwargs: Additional parameters

        Returns:
            CoachingListResult
        """
        params = {k: v for k, v in {
            "workspace-id": workspace_id,
            "manager-id": manager_id,
            "from": from_,
            "to": to,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("coaching", "list", params)
        # Cast generic envelope to concrete typed result
        return CoachingListResult(
            data=result.data
        )



class StatsActivityScorecardsQuery:
    """
    Query class for StatsActivityScorecards entity operations.
    """

    def __init__(self, connector: GongConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: StatsActivityScorecardsListParamsFilter | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> StatsActivityScorecardsListResult:
        """
        Retrieve answered scorecards for applicable reviewed users or scorecards for a date range

        Args:
            filter: Parameter filter
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            StatsActivityScorecardsListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("stats_activity_scorecards", "list", params)
        # Cast generic envelope to concrete typed result
        return StatsActivityScorecardsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: StatsActivityScorecardsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> StatsActivityScorecardsSearchResult:
        """
        Search stats_activity_scorecards records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (StatsActivityScorecardsSearchFilter):
        - answered_scorecard_id: Unique identifier for the answered scorecard instance.
        - answers: Contains the answered questions in the scorecards
        - call_id: Unique identifier for the call associated with the answered scorecard.
        - call_start_time: Timestamp indicating the start time of the call.
        - review_time: Timestamp indicating when the review of the answered scorecard was completed.
        - reviewed_user_id: Unique identifier for the user whose performance was reviewed.
        - reviewer_user_id: Unique identifier for the user who performed the review.
        - scorecard_id: Unique identifier for the scorecard template used.
        - scorecard_name: Name or title of the scorecard template used.
        - visibility_type: Type indicating the visibility permissions for the answered scorecard.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            StatsActivityScorecardsSearchResult with hits (list of AirbyteSearchHit[StatsActivityScorecardsSearchData]) and pagination info

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

        result = await self._connector.execute("stats_activity_scorecards", "search", params)

        # Parse response into typed result
        return StatsActivityScorecardsSearchResult(
            hits=[
                AirbyteSearchHit[StatsActivityScorecardsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=StatsActivityScorecardsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )
