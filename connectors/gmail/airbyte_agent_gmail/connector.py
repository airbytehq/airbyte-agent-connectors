"""
Gmail connector.
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

from pydantic import BaseModel

from .connector_model import GmailConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    DraftsCreateParams,
    DraftsCreateParamsMessage,
    DraftsDeleteParams,
    DraftsGetParams,
    DraftsListParams,
    DraftsSendCreateParams,
    DraftsUpdateParams,
    DraftsUpdateParamsMessage,
    LabelsCreateParams,
    LabelsCreateParamsColor,
    LabelsDeleteParams,
    LabelsGetParams,
    LabelsListParams,
    LabelsUpdateParams,
    LabelsUpdateParamsColor,
    MessagesCreateParams,
    MessagesGetParams,
    MessagesListParams,
    MessagesTrashCreateParams,
    MessagesUntrashCreateParams,
    MessagesUpdateParams,
    ProfileGetParams,
    ThreadsGetParams,
    ThreadsListParams,
)
from .models import GmailAuthConfig
if TYPE_CHECKING:
    from .models import GmailReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    GmailCheckResult,
    GmailExecuteResult,
    GmailExecuteResultWithMeta,
    MessagesListResult,
    LabelsListResult,
    DraftsListResult,
    ThreadsListResult,
    Draft,
    DraftRef,
    Label,
    Message,
    MessageRef,
    Profile,
    Thread,
    ThreadRef,
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




class GmailConnector:
    """
    Type-safe Gmail API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "gmail"
    connector_version = "0.1.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("profile", "get"): None,
        ("messages", "list"): True,
        ("messages", "get"): None,
        ("labels", "list"): True,
        ("labels", "create"): None,
        ("labels", "get"): None,
        ("labels", "update"): None,
        ("labels", "delete"): None,
        ("drafts", "list"): True,
        ("drafts", "create"): None,
        ("drafts", "get"): None,
        ("drafts", "update"): None,
        ("drafts", "delete"): None,
        ("drafts_send", "create"): None,
        ("threads", "list"): True,
        ("threads", "get"): None,
        ("messages", "create"): None,
        ("messages", "update"): None,
        ("messages_trash", "create"): None,
        ("messages_untrash", "create"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('messages', 'list'): {'max_results': 'maxResults', 'page_token': 'pageToken', 'q': 'q', 'label_ids': 'labelIds', 'include_spam_trash': 'includeSpamTrash'},
        ('messages', 'get'): {'message_id': 'messageId', 'format': 'format', 'metadata_headers': 'metadataHeaders'},
        ('labels', 'create'): {'name': 'name', 'message_list_visibility': 'messageListVisibility', 'label_list_visibility': 'labelListVisibility', 'color': 'color'},
        ('labels', 'get'): {'label_id': 'labelId'},
        ('labels', 'update'): {'id': 'id', 'name': 'name', 'message_list_visibility': 'messageListVisibility', 'label_list_visibility': 'labelListVisibility', 'color': 'color', 'label_id': 'labelId'},
        ('labels', 'delete'): {'label_id': 'labelId'},
        ('drafts', 'list'): {'max_results': 'maxResults', 'page_token': 'pageToken', 'q': 'q', 'include_spam_trash': 'includeSpamTrash'},
        ('drafts', 'create'): {'message': 'message'},
        ('drafts', 'get'): {'draft_id': 'draftId', 'format': 'format'},
        ('drafts', 'update'): {'message': 'message', 'draft_id': 'draftId'},
        ('drafts', 'delete'): {'draft_id': 'draftId'},
        ('drafts_send', 'create'): {'id': 'id'},
        ('threads', 'list'): {'max_results': 'maxResults', 'page_token': 'pageToken', 'q': 'q', 'label_ids': 'labelIds', 'include_spam_trash': 'includeSpamTrash'},
        ('threads', 'get'): {'thread_id': 'threadId', 'format': 'format', 'metadata_headers': 'metadataHeaders'},
        ('messages', 'create'): {'raw': 'raw', 'thread_id': 'threadId'},
        ('messages', 'update'): {'add_label_ids': 'addLabelIds', 'remove_label_ids': 'removeLabelIds', 'message_id': 'messageId'},
        ('messages_trash', 'create'): {'message_id': 'messageId'},
        ('messages_untrash', 'create'): {'message_id': 'messageId'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GmailAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GmailAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new gmail connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GmailAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `external_user_id`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GmailConnector(auth_config=GmailAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GmailConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by external_user_id
            connector = GmailConnector(
                auth_config=AirbyteAuthConfig(
                    external_user_id="user-123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                external_user_id=auth_config.external_user_id,
                connector_definition_id=str(GmailConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GmailAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GmailConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.profile = ProfileQuery(self)
        self.messages = MessagesQuery(self)
        self.labels = LabelsQuery(self)
        self.drafts = DraftsQuery(self)
        self.drafts_send = DraftsSendQuery(self)
        self.threads = ThreadsQuery(self)
        self.messages_trash = MessagesTrashQuery(self)
        self.messages_untrash = MessagesUntrashQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["profile"],
        action: Literal["get"],
        params: "ProfileGetParams"
    ) -> "Profile": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["list"],
        params: "MessagesListParams"
    ) -> "MessagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["get"],
        params: "MessagesGetParams"
    ) -> "Message": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["list"],
        params: "LabelsListParams"
    ) -> "LabelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["create"],
        params: "LabelsCreateParams"
    ) -> "Label": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["get"],
        params: "LabelsGetParams"
    ) -> "Label": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["update"],
        params: "LabelsUpdateParams"
    ) -> "Label": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["delete"],
        params: "LabelsDeleteParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["drafts"],
        action: Literal["list"],
        params: "DraftsListParams"
    ) -> "DraftsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["drafts"],
        action: Literal["create"],
        params: "DraftsCreateParams"
    ) -> "Draft": ...

    @overload
    async def execute(
        self,
        entity: Literal["drafts"],
        action: Literal["get"],
        params: "DraftsGetParams"
    ) -> "Draft": ...

    @overload
    async def execute(
        self,
        entity: Literal["drafts"],
        action: Literal["update"],
        params: "DraftsUpdateParams"
    ) -> "Draft": ...

    @overload
    async def execute(
        self,
        entity: Literal["drafts"],
        action: Literal["delete"],
        params: "DraftsDeleteParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["drafts_send"],
        action: Literal["create"],
        params: "DraftsSendCreateParams"
    ) -> "Message": ...

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
        entity: Literal["threads"],
        action: Literal["get"],
        params: "ThreadsGetParams"
    ) -> "Thread": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["create"],
        params: "MessagesCreateParams"
    ) -> "Message": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["update"],
        params: "MessagesUpdateParams"
    ) -> "Message": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages_trash"],
        action: Literal["create"],
        params: "MessagesTrashCreateParams"
    ) -> "Message": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages_untrash"],
        action: Literal["create"],
        params: "MessagesUntrashCreateParams"
    ) -> "Message": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "create", "update", "delete"],
        params: Mapping[str, Any]
    ) -> GmailExecuteResult[Any] | GmailExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "create", "update", "delete"],
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
                return GmailExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GmailExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GmailCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GmailCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GmailCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GmailCheckResult(
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
            @GmailConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GmailConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GmailConnectorModel,
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
        return describe_entities(GmailConnectorModel)

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
            (e for e in GmailConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GmailConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GmailConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def get_consent_url(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        redirect_url: str,
        name: str | None = None,
        replication_config: "GmailReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and external_user_id.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + external_user_id.
            replication_config: Typed replication settings. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await GmailConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Gmail Source",
                replication_config=GmailReplicationConfig(include_spam_and_trash="..."),
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.external_user_id:
            raise ValueError("airbyte_config.external_user_id is required for get_consent_url()")

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(GmailConnectorModel.id),
                external_user_id=airbyte_config.external_user_id,
                redirect_url=redirect_url,
                name=name,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        return consent_url

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "GmailAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GmailReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GmailConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and external_user_id.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A GmailConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GmailConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GmailAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
            )

            # With replication config (required for this connector):
            connector = await GmailConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GmailAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
                replication_config=GmailReplicationConfig(include_spam_and_trash="..."),
            )

            # With server-side OAuth:
            connector = await GmailConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GmailReplicationConfig(include_spam_and_trash="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.external_user_id:
            raise ValueError("airbyte_config.external_user_id is required for create()")

        # Validate: exactly one of auth_config or server_side_oauth_secret_id required
        if auth_config is None and server_side_oauth_secret_id is None:
            raise ValueError(
                "Either auth_config or server_side_oauth_secret_id must be provided"
            )
        if auth_config is not None and server_side_oauth_secret_id is not None:
            raise ValueError(
                "Cannot provide both auth_config and server_side_oauth_secret_id"
            )

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(GmailConnectorModel.id),
                external_user_id=airbyte_config.external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
                server_side_oauth_secret_id=server_side_oauth_secret_id,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                connector_id=source_id,
            ),
        )




class ProfileQuery:
    """
    Query class for Profile entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> Profile:
        """
        Gets the current user's Gmail profile including email address and mailbox statistics

        Returns:
            Profile
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("profile", "get", params)
        return result



class MessagesQuery:
    """
    Query class for Messages entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        max_results: int | None = None,
        page_token: str | None = None,
        q: str | None = None,
        label_ids: str | None = None,
        include_spam_trash: bool | None = None,
        **kwargs
    ) -> MessagesListResult:
        """
        Lists the messages in the user's mailbox. Returns message IDs and thread IDs.

        Args:
            max_results: Maximum number of messages to return (1-500)
            page_token: Page token to retrieve a specific page of results
            q: Gmail search query (same format as Gmail search box, e.g. "from:user@example.com", "is:unread", "subject:hello")
            label_ids: Only return messages with labels matching all of the specified label IDs (comma-separated)
            include_spam_trash: Include messages from SPAM and TRASH in the results
            **kwargs: Additional parameters

        Returns:
            MessagesListResult
        """
        params = {k: v for k, v in {
            "maxResults": max_results,
            "pageToken": page_token,
            "q": q,
            "labelIds": label_ids,
            "includeSpamTrash": include_spam_trash,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "list", params)
        # Cast generic envelope to concrete typed result
        return MessagesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        message_id: str,
        format: str | None = None,
        metadata_headers: str | None = None,
        **kwargs
    ) -> Message:
        """
        Gets the full email message content including headers, body, and attachments metadata

        Args:
            message_id: The ID of the message to retrieve
            format: The format to return the message in (full, metadata, minimal, raw)
            metadata_headers: When format is METADATA, only include headers specified (comma-separated)
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "messageId": message_id,
            "format": format,
            "metadataHeaders": metadata_headers,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "get", params)
        return result



    async def create(
        self,
        raw: str,
        thread_id: str | None = None,
        **kwargs
    ) -> Message:
        """
        Sends a new email message. The message should be provided as a base64url-encoded
RFC 2822 formatted string in the 'raw' field.


        Args:
            raw: The entire email message in RFC 2822 format, base64url encoded
            thread_id: The thread ID to reply to (for threading replies in a conversation)
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "raw": raw,
            "threadId": thread_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "create", params)
        return result



    async def update(
        self,
        message_id: str,
        add_label_ids: list[str] | None = None,
        remove_label_ids: list[str] | None = None,
        **kwargs
    ) -> Message:
        """
        Modifies the labels on a message. Use this to archive (remove INBOX label),
mark as read (remove UNREAD label), mark as unread (add UNREAD label),
star (add STARRED label), or apply custom labels.


        Args:
            add_label_ids: A list of label IDs to add to the message (e.g. STARRED, UNREAD, or custom label IDs)
            remove_label_ids: A list of label IDs to remove from the message (e.g. INBOX to archive, UNREAD to mark as read)
            message_id: The ID of the message to modify
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "addLabelIds": add_label_ids,
            "removeLabelIds": remove_label_ids,
            "messageId": message_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "update", params)
        return result



class LabelsQuery:
    """
    Query class for Labels entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> LabelsListResult:
        """
        Lists all labels in the user's mailbox including system and user-created labels

        Returns:
            LabelsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "list", params)
        # Cast generic envelope to concrete typed result
        return LabelsListResult(
            data=result.data
        )



    async def create(
        self,
        name: str,
        message_list_visibility: str | None = None,
        label_list_visibility: str | None = None,
        color: LabelsCreateParamsColor | None = None,
        **kwargs
    ) -> Label:
        """
        Creates a new label in the user's mailbox

        Args:
            name: The display name of the label
            message_list_visibility: The visibility of messages with this label in the message list (show or hide)
            label_list_visibility: The visibility of the label in the label list
            color: The color to assign to the label
            **kwargs: Additional parameters

        Returns:
            Label
        """
        params = {k: v for k, v in {
            "name": name,
            "messageListVisibility": message_list_visibility,
            "labelListVisibility": label_list_visibility,
            "color": color,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "create", params)
        return result



    async def get(
        self,
        label_id: str,
        **kwargs
    ) -> Label:
        """
        Gets a specific label by ID including message and thread counts

        Args:
            label_id: The ID of the label to retrieve
            **kwargs: Additional parameters

        Returns:
            Label
        """
        params = {k: v for k, v in {
            "labelId": label_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "get", params)
        return result



    async def update(
        self,
        label_id: str,
        id: str | None = None,
        name: str | None = None,
        message_list_visibility: str | None = None,
        label_list_visibility: str | None = None,
        color: LabelsUpdateParamsColor | None = None,
        **kwargs
    ) -> Label:
        """
        Updates the specified label

        Args:
            id: The ID of the label (must match the path parameter)
            name: The new display name of the label
            message_list_visibility: The visibility of messages with this label in the message list
            label_list_visibility: The visibility of the label in the label list
            color: The color to assign to the label
            label_id: The ID of the label to update
            **kwargs: Additional parameters

        Returns:
            Label
        """
        params = {k: v for k, v in {
            "id": id,
            "name": name,
            "messageListVisibility": message_list_visibility,
            "labelListVisibility": label_list_visibility,
            "color": color,
            "labelId": label_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "update", params)
        return result



    async def delete(
        self,
        label_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Deletes the specified label and removes it from any messages and threads

        Args:
            label_id: The ID of the label to delete
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "labelId": label_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "delete", params)
        return result



class DraftsQuery:
    """
    Query class for Drafts entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        max_results: int | None = None,
        page_token: str | None = None,
        q: str | None = None,
        include_spam_trash: bool | None = None,
        **kwargs
    ) -> DraftsListResult:
        """
        Lists the drafts in the user's mailbox

        Args:
            max_results: Maximum number of drafts to return (1-500)
            page_token: Page token to retrieve a specific page of results
            q: Gmail search query to filter drafts
            include_spam_trash: Include drafts from SPAM and TRASH in the results
            **kwargs: Additional parameters

        Returns:
            DraftsListResult
        """
        params = {k: v for k, v in {
            "maxResults": max_results,
            "pageToken": page_token,
            "q": q,
            "includeSpamTrash": include_spam_trash,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drafts", "list", params)
        # Cast generic envelope to concrete typed result
        return DraftsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        message: DraftsCreateParamsMessage,
        **kwargs
    ) -> Draft:
        """
        Creates a new draft with the specified message content

        Args:
            message: The draft message content
            **kwargs: Additional parameters

        Returns:
            Draft
        """
        params = {k: v for k, v in {
            "message": message,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drafts", "create", params)
        return result



    async def get(
        self,
        draft_id: str,
        format: str | None = None,
        **kwargs
    ) -> Draft:
        """
        Gets the specified draft including its message content

        Args:
            draft_id: The ID of the draft to retrieve
            format: The format to return the draft message in (full, metadata, minimal, raw)
            **kwargs: Additional parameters

        Returns:
            Draft
        """
        params = {k: v for k, v in {
            "draftId": draft_id,
            "format": format,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drafts", "get", params)
        return result



    async def update(
        self,
        message: DraftsUpdateParamsMessage,
        draft_id: str,
        **kwargs
    ) -> Draft:
        """
        Replaces a draft's content with the specified message content

        Args:
            message: The draft message content
            draft_id: The ID of the draft to update
            **kwargs: Additional parameters

        Returns:
            Draft
        """
        params = {k: v for k, v in {
            "message": message,
            "draftId": draft_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drafts", "update", params)
        return result



    async def delete(
        self,
        draft_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Immediately and permanently deletes the specified draft (does not move to trash)

        Args:
            draft_id: The ID of the draft to delete
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "draftId": draft_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drafts", "delete", params)
        return result



class DraftsSendQuery:
    """
    Query class for DraftsSend entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        id: str | None = None,
        **kwargs
    ) -> Message:
        """
        Sends the specified existing draft to its recipients

        Args:
            id: The ID of the draft to send
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drafts_send", "create", params)
        return result



class ThreadsQuery:
    """
    Query class for Threads entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        max_results: int | None = None,
        page_token: str | None = None,
        q: str | None = None,
        label_ids: str | None = None,
        include_spam_trash: bool | None = None,
        **kwargs
    ) -> ThreadsListResult:
        """
        Lists the threads in the user's mailbox

        Args:
            max_results: Maximum number of threads to return (1-500)
            page_token: Page token to retrieve a specific page of results
            q: Gmail search query to filter threads
            label_ids: Only return threads with labels matching all of the specified label IDs (comma-separated)
            include_spam_trash: Include threads from SPAM and TRASH in the results
            **kwargs: Additional parameters

        Returns:
            ThreadsListResult
        """
        params = {k: v for k, v in {
            "maxResults": max_results,
            "pageToken": page_token,
            "q": q,
            "labelIds": label_ids,
            "includeSpamTrash": include_spam_trash,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("threads", "list", params)
        # Cast generic envelope to concrete typed result
        return ThreadsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        thread_id: str,
        format: str | None = None,
        metadata_headers: str | None = None,
        **kwargs
    ) -> Thread:
        """
        Gets the specified thread including all messages in the conversation

        Args:
            thread_id: The ID of the thread to retrieve
            format: The format to return the messages in (full, metadata, minimal)
            metadata_headers: When format is METADATA, only include headers specified (comma-separated)
            **kwargs: Additional parameters

        Returns:
            Thread
        """
        params = {k: v for k, v in {
            "threadId": thread_id,
            "format": format,
            "metadataHeaders": metadata_headers,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("threads", "get", params)
        return result



class MessagesTrashQuery:
    """
    Query class for MessagesTrash entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        message_id: str,
        **kwargs
    ) -> Message:
        """
        Moves the specified message to the trash

        Args:
            message_id: The ID of the message to trash
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "messageId": message_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages_trash", "create", params)
        return result



class MessagesUntrashQuery:
    """
    Query class for MessagesUntrash entity operations.
    """

    def __init__(self, connector: GmailConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        message_id: str,
        **kwargs
    ) -> Message:
        """
        Removes the specified message from the trash

        Args:
            message_id: The ID of the message to untrash
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "messageId": message_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages_untrash", "create", params)
        return result


