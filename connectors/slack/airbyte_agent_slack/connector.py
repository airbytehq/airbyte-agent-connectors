"""
Slack connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import SlackConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    ChannelMessagesListParams,
    ChannelsGetParams,
    ChannelsListParams,
    ThreadsListParams,
    UsersGetParams,
    UsersListParams,
)
if TYPE_CHECKING:
    from .models import SlackAuthConfig
# Import specific auth config classes for multi-auth isinstance checks
from .models import SlackTokenAuthenticationAuthConfig, SlackOauth20AuthenticationAuthConfig
# Import response models and envelope models at runtime
from .models import (
    SlackExecuteResult,
    SlackExecuteResultWithMeta,
    UsersListResult,
    ChannelsListResult,
    ChannelMessagesListResult,
    ThreadsListResult,
    Channel,
    Message,
    Thread,
    User,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])


class SlackConnector:
    """
    Type-safe Slack API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "slack"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("users", "list"): True,
        ("users", "get"): None,
        ("channels", "list"): True,
        ("channels", "get"): None,
        ("channel_messages", "list"): True,
        ("threads", "list"): True,
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
            connector = SlackConnector(auth_config=SlackAuthConfig(access_token="..."))
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
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> SlackExecuteResult[Any] | SlackExecuteResultWithMeta[Any, Any] | Any: ...

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

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def describe(cls, func: _F) -> _F:
        """
        Decorator that populates a function's docstring with connector capabilities.

        This class method can be used as a decorator to automatically generate
        comprehensive documentation for AI tool functions.

        Usage:
            @mcp.tool()
            @SlackConnector.describe
            async def execute(entity: str, action: str, params: dict):
                '''Execute operations.'''
                ...

        The decorated function's __doc__ will be updated with:
        - Available entities and their actions
        - Parameter signatures with required (*) and optional (?) markers
        - Response structure documentation
        - Example questions (if available in OpenAPI spec)

        Args:
            func: The function to decorate

        Returns:
            The same function with updated __doc__
        """
        description = generate_tool_description(SlackConnectorModel)

        original_doc = func.__doc__ or ""
        if original_doc.strip():
            func.__doc__ = f"{original_doc.strip()}\n{description}"
        else:
            func.__doc__ = description

        return func

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


