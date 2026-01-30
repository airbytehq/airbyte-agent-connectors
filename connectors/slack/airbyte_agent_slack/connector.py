"""
Slack connector.
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

from .connector_model import SlackConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    ChannelMessagesListParams,
    ChannelPurposesCreateParams,
    ChannelTopicsCreateParams,
    ChannelsCreateParams,
    ChannelsGetParams,
    ChannelsListParams,
    ChannelsUpdateParams,
    MessagesCreateParams,
    MessagesUpdateParams,
    ReactionsCreateParams,
    ThreadsListParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    ChannelsSearchFilter,
    ChannelsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
)
if TYPE_CHECKING:
    from .models import SlackAuthConfig
# Import specific auth config classes for multi-auth isinstance checks
from .models import SlackTokenAuthenticationAuthConfig, SlackOauth20AuthenticationAuthConfig
# Import response models and envelope models at runtime
from .models import (
    SlackCheckResult,
    SlackExecuteResult,
    SlackExecuteResultWithMeta,
    UsersListResult,
    ChannelsListResult,
    ChannelMessagesListResult,
    ThreadsListResult,
    Channel,
    CreatedMessage,
    Message,
    ReactionAddResponse,
    Thread,
    User,
    AirbyteSearchHit,
    AirbyteSearchResult,
    ChannelsSearchData,
    ChannelsSearchResult,
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




class SlackConnector:
    """
    Type-safe Slack API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "slack"
    connector_version = "0.1.12"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("users", "list"): True,
        ("users", "get"): None,
        ("channels", "list"): True,
        ("channels", "get"): None,
        ("channel_messages", "list"): True,
        ("threads", "list"): True,
        ("messages", "create"): None,
        ("messages", "update"): None,
        ("channels", "create"): None,
        ("channels", "update"): None,
        ("channel_topics", "create"): None,
        ("channel_purposes", "create"): None,
        ("reactions", "create"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('users', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('users', 'get'): {'user': 'user'},
        ('channels', 'list'): {'cursor': 'cursor', 'limit': 'limit', 'types': 'types', 'exclude_archived': 'exclude_archived'},
        ('channels', 'get'): {'channel': 'channel'},
        ('channel_messages', 'list'): {'channel': 'channel', 'cursor': 'cursor', 'limit': 'limit', 'oldest': 'oldest', 'latest': 'latest', 'inclusive': 'inclusive'},
        ('threads', 'list'): {'channel': 'channel', 'ts': 'ts', 'cursor': 'cursor', 'limit': 'limit', 'oldest': 'oldest', 'latest': 'latest', 'inclusive': 'inclusive'},
        ('messages', 'create'): {'channel': 'channel', 'text': 'text', 'thread_ts': 'thread_ts', 'reply_broadcast': 'reply_broadcast', 'unfurl_links': 'unfurl_links', 'unfurl_media': 'unfurl_media'},
        ('messages', 'update'): {'channel': 'channel', 'ts': 'ts', 'text': 'text'},
        ('channels', 'create'): {'name': 'name', 'is_private': 'is_private'},
        ('channels', 'update'): {'channel': 'channel', 'name': 'name'},
        ('channel_topics', 'create'): {'channel': 'channel', 'topic': 'topic'},
        ('channel_purposes', 'create'): {'channel': 'channel', 'purpose': 'purpose'},
        ('reactions', 'create'): {'channel': 'channel', 'timestamp': 'timestamp', 'name': 'name'},
    }

    def __init__(
        self,
        auth_config: SlackAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new slack connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `external_user_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = SlackConnector(auth_config=SlackAuthConfig(api_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = SlackConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = SlackConnector(
                auth_config=SlackAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: external_user_id, airbyte_client_id, and airbyte_client_secret provided
        if external_user_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                external_user_id=external_user_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_definition_id=str(SlackConnectorModel.id),
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (external_user_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, SlackTokenAuthenticationAuthConfig):
                    auth_scheme = "bearerAuth"
                if isinstance(auth_config, SlackOauth20AuthenticationAuthConfig):
                    auth_scheme = "oauth2"

            self._executor = LocalExecutor(
                model=SlackConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.users = UsersQuery(self)
        self.channels = ChannelsQuery(self)
        self.channel_messages = ChannelMessagesQuery(self)
        self.threads = ThreadsQuery(self)
        self.messages = MessagesQuery(self)
        self.channel_topics = ChannelTopicsQuery(self)
        self.channel_purposes = ChannelPurposesQuery(self)
        self.reactions = ReactionsQuery(self)

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
        entity: Literal["channels"],
        action: Literal["list"],
        params: "ChannelsListParams"
    ) -> "ChannelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["channels"],
        action: Literal["get"],
        params: "ChannelsGetParams"
    ) -> "Channel": ...

    @overload
    async def execute(
        self,
        entity: Literal["channel_messages"],
        action: Literal["list"],
        params: "ChannelMessagesListParams"
    ) -> "ChannelMessagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["threads"],
        action: Literal["list"],
        params: "ThreadsListParams"
    ) -> "ThreadsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["create"],
        params: "MessagesCreateParams"
    ) -> "CreatedMessage": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["update"],
        params: "MessagesUpdateParams"
    ) -> "CreatedMessage": ...

    @overload
    async def execute(
        self,
        entity: Literal["channels"],
        action: Literal["create"],
        params: "ChannelsCreateParams"
    ) -> "Channel": ...

    @overload
    async def execute(
        self,
        entity: Literal["channels"],
        action: Literal["update"],
        params: "ChannelsUpdateParams"
    ) -> "Channel": ...

    @overload
    async def execute(
        self,
        entity: Literal["channel_topics"],
        action: Literal["create"],
        params: "ChannelTopicsCreateParams"
    ) -> "Channel": ...

    @overload
    async def execute(
        self,
        entity: Literal["channel_purposes"],
        action: Literal["create"],
        params: "ChannelPurposesCreateParams"
    ) -> "Channel": ...

    @overload
    async def execute(
        self,
        entity: Literal["reactions"],
        action: Literal["create"],
        params: "ReactionsCreateParams"
    ) -> "ReactionAddResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "search"],
        params: Mapping[str, Any]
    ) -> SlackExecuteResult[Any] | SlackExecuteResultWithMeta[Any, Any] | Any: ...

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
                return SlackExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SlackExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SlackCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SlackCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SlackCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SlackCheckResult(
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
            @SlackConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @SlackConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    SlackConnectorModel,
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
        return describe_entities(SlackConnectorModel)

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
            (e for e in SlackConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SlackConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a list of all users in the Slack workspace

        Args:
            cursor: Pagination cursor for next page
            limit: Number of users to return per page
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
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
        user: str,
        **kwargs
    ) -> User:
        """
        Get information about a single user by ID

        Args:
            user: User ID
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "user": user,
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
        - color: The color assigned to the user for visual purposes.
        - deleted: Indicates if the user is deleted or not.
        - has_2fa: Flag indicating if the user has two-factor authentication enabled.
        - id: Unique identifier for the user.
        - is_admin: Flag specifying if the user is an admin or not.
        - is_app_user: Specifies if the user is an app user.
        - is_bot: Indicates if the user is a bot account.
        - is_email_confirmed: Flag indicating if the user's email is confirmed.
        - is_forgotten: Specifies if the user is marked as forgotten.
        - is_invited_user: Indicates if the user is invited or not.
        - is_owner: Flag indicating if the user is an owner.
        - is_primary_owner: Specifies if the user is the primary owner.
        - is_restricted: Flag specifying if the user is restricted.
        - is_ultra_restricted: Indicates if the user has ultra-restricted access.
        - name: The username of the user.
        - profile: User's profile information containing detailed details.
        - real_name: The real name of the user.
        - team_id: Unique identifier for the team the user belongs to.
        - tz: Timezone of the user.
        - tz_label: Label representing the timezone of the user.
        - tz_offset: Offset of the user's timezone.
        - updated: Timestamp of when the user's information was last updated.
        - who_can_share_contact_card: Specifies who can share the user's contact card.

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

class ChannelsQuery:
    """
    Query class for Channels entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        types: str | None = None,
        exclude_archived: bool | None = None,
        **kwargs
    ) -> ChannelsListResult:
        """
        Returns a list of all channels in the Slack workspace

        Args:
            cursor: Pagination cursor for next page
            limit: Number of channels to return per page
            types: Mix and match channel types (public_channel, private_channel, mpim, im)
            exclude_archived: Exclude archived channels
            **kwargs: Additional parameters

        Returns:
            ChannelsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            "types": types,
            "exclude_archived": exclude_archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channels", "list", params)
        # Cast generic envelope to concrete typed result
        return ChannelsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        channel: str,
        **kwargs
    ) -> Channel:
        """
        Get information about a single channel by ID

        Args:
            channel: Channel ID
            **kwargs: Additional parameters

        Returns:
            Channel
        """
        params = {k: v for k, v in {
            "channel": channel,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channels", "get", params)
        return result



    async def create(
        self,
        name: str,
        is_private: bool | None = None,
        **kwargs
    ) -> Channel:
        """
        Creates a new public or private channel

        Args:
            name: Channel name (lowercase, no spaces, max 80 chars)
            is_private: Create a private channel instead of public
            **kwargs: Additional parameters

        Returns:
            Channel
        """
        params = {k: v for k, v in {
            "name": name,
            "is_private": is_private,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channels", "create", params)
        return result



    async def update(
        self,
        channel: str,
        name: str,
        **kwargs
    ) -> Channel:
        """
        Renames an existing channel

        Args:
            channel: Channel ID to rename
            name: New channel name (lowercase, no spaces, max 80 chars)
            **kwargs: Additional parameters

        Returns:
            Channel
        """
        params = {k: v for k, v in {
            "channel": channel,
            "name": name,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channels", "update", params)
        return result



    async def search(
        self,
        query: ChannelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ChannelsSearchResult:
        """
        Search channels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ChannelsSearchFilter):
        - context_team_id: The unique identifier of the team context in which the channel exists.
        - created: The timestamp when the channel was created.
        - creator: The ID of the user who created the channel.
        - id: The unique identifier of the channel.
        - is_archived: Indicates if the channel is archived.
        - is_channel: Indicates if the entity is a channel.
        - is_ext_shared: Indicates if the channel is externally shared.
        - is_general: Indicates if the channel is a general channel in the workspace.
        - is_group: Indicates if the channel is a group (private channel) rather than a regular channel.
        - is_im: Indicates if the entity is a direct message (IM) channel.
        - is_member: Indicates if the calling user is a member of the channel.
        - is_mpim: Indicates if the entity is a multiple person direct message (MPIM) channel.
        - is_org_shared: Indicates if the channel is organization-wide shared.
        - is_pending_ext_shared: Indicates if the channel is pending external shared.
        - is_private: Indicates if the channel is a private channel.
        - is_read_only: Indicates if the channel is read-only.
        - is_shared: Indicates if the channel is shared.
        - last_read: The timestamp of the user's last read message in the channel.
        - locale: The locale of the channel.
        - name: The name of the channel.
        - name_normalized: The normalized name of the channel.
        - num_members: The number of members in the channel.
        - parent_conversation: The parent conversation of the channel.
        - pending_connected_team_ids: The IDs of teams that are pending to be connected to the channel.
        - pending_shared: The list of pending shared items of the channel.
        - previous_names: The previous names of the channel.
        - purpose: The purpose of the channel.
        - shared_team_ids: The IDs of teams with which the channel is shared.
        - topic: The topic of the channel.
        - unlinked: Indicates if the channel is unlinked.
        - updated: The timestamp when the channel was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ChannelsSearchResult with hits (list of AirbyteSearchHit[ChannelsSearchData]) and pagination info

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

        result = await self._connector.execute("channels", "search", params)

        # Parse response into typed result
        return ChannelsSearchResult(
            hits=[
                AirbyteSearchHit[ChannelsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ChannelsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ChannelMessagesQuery:
    """
    Query class for ChannelMessages entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        channel: str,
        cursor: str | None = None,
        limit: int | None = None,
        oldest: str | None = None,
        latest: str | None = None,
        inclusive: bool | None = None,
        **kwargs
    ) -> ChannelMessagesListResult:
        """
        Returns messages from a channel

        Args:
            channel: Channel ID to get messages from
            cursor: Pagination cursor for next page
            limit: Number of messages to return per page
            oldest: Start of time range (Unix timestamp)
            latest: End of time range (Unix timestamp)
            inclusive: Include messages with oldest or latest timestamps
            **kwargs: Additional parameters

        Returns:
            ChannelMessagesListResult
        """
        params = {k: v for k, v in {
            "channel": channel,
            "cursor": cursor,
            "limit": limit,
            "oldest": oldest,
            "latest": latest,
            "inclusive": inclusive,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channel_messages", "list", params)
        # Cast generic envelope to concrete typed result
        return ChannelMessagesListResult(
            data=result.data,
            meta=result.meta
        )



class ThreadsQuery:
    """
    Query class for Threads entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        channel: str,
        ts: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        oldest: str | None = None,
        latest: str | None = None,
        inclusive: bool | None = None,
        **kwargs
    ) -> ThreadsListResult:
        """
        Returns messages in a thread (thread replies from conversations.replies endpoint)

        Args:
            channel: Channel ID containing the thread
            ts: Timestamp of the parent message (required for thread replies)
            cursor: Pagination cursor for next page
            limit: Number of replies to return per page
            oldest: Start of time range (Unix timestamp)
            latest: End of time range (Unix timestamp)
            inclusive: Include messages with oldest or latest timestamps
            **kwargs: Additional parameters

        Returns:
            ThreadsListResult
        """
        params = {k: v for k, v in {
            "channel": channel,
            "ts": ts,
            "cursor": cursor,
            "limit": limit,
            "oldest": oldest,
            "latest": latest,
            "inclusive": inclusive,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("threads", "list", params)
        # Cast generic envelope to concrete typed result
        return ThreadsListResult(
            data=result.data,
            meta=result.meta
        )



class MessagesQuery:
    """
    Query class for Messages entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        channel: str,
        text: str,
        thread_ts: str | None = None,
        reply_broadcast: bool | None = None,
        unfurl_links: bool | None = None,
        unfurl_media: bool | None = None,
        **kwargs
    ) -> CreatedMessage:
        """
        Posts a message to a public channel, private channel, or direct message conversation

        Args:
            channel: Channel ID, private group ID, or user ID to send message to
            text: Message text content (supports mrkdwn formatting)
            thread_ts: Thread timestamp to reply to (for threaded messages)
            reply_broadcast: Also post reply to channel when replying to a thread
            unfurl_links: Enable unfurling of primarily text-based content
            unfurl_media: Enable unfurling of media content
            **kwargs: Additional parameters

        Returns:
            CreatedMessage
        """
        params = {k: v for k, v in {
            "channel": channel,
            "text": text,
            "thread_ts": thread_ts,
            "reply_broadcast": reply_broadcast,
            "unfurl_links": unfurl_links,
            "unfurl_media": unfurl_media,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "create", params)
        return result



    async def update(
        self,
        channel: str,
        ts: str,
        text: str,
        **kwargs
    ) -> CreatedMessage:
        """
        Updates an existing message in a channel

        Args:
            channel: Channel ID containing the message
            ts: Timestamp of the message to update
            text: New message text content
            **kwargs: Additional parameters

        Returns:
            CreatedMessage
        """
        params = {k: v for k, v in {
            "channel": channel,
            "ts": ts,
            "text": text,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "update", params)
        return result



class ChannelTopicsQuery:
    """
    Query class for ChannelTopics entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        channel: str,
        topic: str,
        **kwargs
    ) -> Channel:
        """
        Sets the topic for a channel

        Args:
            channel: Channel ID to set topic for
            topic: New topic text (max 250 characters)
            **kwargs: Additional parameters

        Returns:
            Channel
        """
        params = {k: v for k, v in {
            "channel": channel,
            "topic": topic,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channel_topics", "create", params)
        return result



class ChannelPurposesQuery:
    """
    Query class for ChannelPurposes entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        channel: str,
        purpose: str,
        **kwargs
    ) -> Channel:
        """
        Sets the purpose for a channel

        Args:
            channel: Channel ID to set purpose for
            purpose: New purpose text (max 250 characters)
            **kwargs: Additional parameters

        Returns:
            Channel
        """
        params = {k: v for k, v in {
            "channel": channel,
            "purpose": purpose,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("channel_purposes", "create", params)
        return result



class ReactionsQuery:
    """
    Query class for Reactions entity operations.
    """

    def __init__(self, connector: SlackConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        channel: str,
        timestamp: str,
        name: str,
        **kwargs
    ) -> ReactionAddResponse:
        """
        Adds a reaction (emoji) to a message

        Args:
            channel: Channel ID containing the message
            timestamp: Timestamp of the message to react to
            name: Reaction emoji name (without colons, e.g., "thumbsup")
            **kwargs: Additional parameters

        Returns:
            ReactionAddResponse
        """
        params = {k: v for k, v in {
            "channel": channel,
            "timestamp": timestamp,
            "name": name,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reactions", "create", params)
        return result


