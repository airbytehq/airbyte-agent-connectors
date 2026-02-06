"""
Google-Drive connector.
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

from pydantic import BaseModel

from .connector_model import GoogleDriveConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AboutGetParams,
    ChangesListParams,
    ChangesStartPageTokenGetParams,
    CommentsGetParams,
    CommentsListParams,
    DrivesGetParams,
    DrivesListParams,
    FilesDownloadParams,
    FilesExportDownloadParams,
    FilesGetParams,
    FilesListParams,
    PermissionsGetParams,
    PermissionsListParams,
    RepliesGetParams,
    RepliesListParams,
    RevisionsGetParams,
    RevisionsListParams,
)
from .models import GoogleDriveAuthConfig
if TYPE_CHECKING:
    from .models import GoogleDriveReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    GoogleDriveCheckResult,
    GoogleDriveExecuteResult,
    GoogleDriveExecuteResultWithMeta,
    FilesListResult,
    DrivesListResult,
    PermissionsListResult,
    CommentsListResult,
    RepliesListResult,
    RevisionsListResult,
    ChangesListResult,
    About,
    Change,
    Comment,
    Drive,
    File,
    Permission,
    Reply,
    Revision,
    StartPageToken,
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




class GoogleDriveConnector:
    """
    Type-safe Google-Drive API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "google-drive"
    connector_version = "0.1.7"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("files", "list"): True,
        ("files", "get"): None,
        ("files", "download"): None,
        ("files_export", "download"): None,
        ("drives", "list"): True,
        ("drives", "get"): None,
        ("permissions", "list"): True,
        ("permissions", "get"): None,
        ("comments", "list"): True,
        ("comments", "get"): None,
        ("replies", "list"): True,
        ("replies", "get"): None,
        ("revisions", "list"): True,
        ("revisions", "get"): None,
        ("changes", "list"): True,
        ("changes_start_page_token", "get"): None,
        ("about", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('files', 'list'): {'page_size': 'pageSize', 'page_token': 'pageToken', 'q': 'q', 'order_by': 'orderBy', 'fields': 'fields', 'spaces': 'spaces', 'corpora': 'corpora', 'drive_id': 'driveId', 'include_items_from_all_drives': 'includeItemsFromAllDrives', 'supports_all_drives': 'supportsAllDrives'},
        ('files', 'get'): {'file_id': 'fileId', 'fields': 'fields', 'supports_all_drives': 'supportsAllDrives'},
        ('files', 'download'): {'file_id': 'fileId', 'alt': 'alt', 'acknowledge_abuse': 'acknowledgeAbuse', 'supports_all_drives': 'supportsAllDrives', 'range_header': 'range_header'},
        ('files_export', 'download'): {'file_id': 'fileId', 'mime_type': 'mimeType', 'range_header': 'range_header'},
        ('drives', 'list'): {'page_size': 'pageSize', 'page_token': 'pageToken', 'q': 'q', 'use_domain_admin_access': 'useDomainAdminAccess'},
        ('drives', 'get'): {'drive_id': 'driveId', 'use_domain_admin_access': 'useDomainAdminAccess'},
        ('permissions', 'list'): {'file_id': 'fileId', 'page_size': 'pageSize', 'page_token': 'pageToken', 'supports_all_drives': 'supportsAllDrives', 'use_domain_admin_access': 'useDomainAdminAccess'},
        ('permissions', 'get'): {'file_id': 'fileId', 'permission_id': 'permissionId', 'supports_all_drives': 'supportsAllDrives', 'use_domain_admin_access': 'useDomainAdminAccess'},
        ('comments', 'list'): {'file_id': 'fileId', 'page_size': 'pageSize', 'page_token': 'pageToken', 'start_modified_time': 'startModifiedTime', 'include_deleted': 'includeDeleted', 'fields': 'fields'},
        ('comments', 'get'): {'file_id': 'fileId', 'comment_id': 'commentId', 'include_deleted': 'includeDeleted', 'fields': 'fields'},
        ('replies', 'list'): {'file_id': 'fileId', 'comment_id': 'commentId', 'page_size': 'pageSize', 'page_token': 'pageToken', 'include_deleted': 'includeDeleted', 'fields': 'fields'},
        ('replies', 'get'): {'file_id': 'fileId', 'comment_id': 'commentId', 'reply_id': 'replyId', 'include_deleted': 'includeDeleted', 'fields': 'fields'},
        ('revisions', 'list'): {'file_id': 'fileId', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('revisions', 'get'): {'file_id': 'fileId', 'revision_id': 'revisionId'},
        ('changes', 'list'): {'page_token': 'pageToken', 'page_size': 'pageSize', 'drive_id': 'driveId', 'include_items_from_all_drives': 'includeItemsFromAllDrives', 'supports_all_drives': 'supportsAllDrives', 'spaces': 'spaces', 'include_removed': 'includeRemoved', 'restrict_to_my_drive': 'restrictToMyDrive'},
        ('changes_start_page_token', 'get'): {'drive_id': 'driveId', 'supports_all_drives': 'supportsAllDrives'},
        ('about', 'get'): {'fields': 'fields'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GoogleDriveAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GoogleDriveAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new google-drive connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GoogleDriveAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `external_user_id`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GoogleDriveConnector(auth_config=GoogleDriveAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GoogleDriveConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by external_user_id
            connector = GoogleDriveConnector(
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
                connector_definition_id=str(GoogleDriveConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GoogleDriveAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GoogleDriveConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.files = FilesQuery(self)
        self.files_export = FilesExportQuery(self)
        self.drives = DrivesQuery(self)
        self.permissions = PermissionsQuery(self)
        self.comments = CommentsQuery(self)
        self.replies = RepliesQuery(self)
        self.revisions = RevisionsQuery(self)
        self.changes = ChangesQuery(self)
        self.changes_start_page_token = ChangesStartPageTokenQuery(self)
        self.about = AboutQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["files"],
        action: Literal["list"],
        params: "FilesListParams"
    ) -> "FilesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["files"],
        action: Literal["get"],
        params: "FilesGetParams"
    ) -> "File": ...

    @overload
    async def execute(
        self,
        entity: Literal["files"],
        action: Literal["download"],
        params: "FilesDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["files_export"],
        action: Literal["download"],
        params: "FilesExportDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["drives"],
        action: Literal["list"],
        params: "DrivesListParams"
    ) -> "DrivesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["drives"],
        action: Literal["get"],
        params: "DrivesGetParams"
    ) -> "Drive": ...

    @overload
    async def execute(
        self,
        entity: Literal["permissions"],
        action: Literal["list"],
        params: "PermissionsListParams"
    ) -> "PermissionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["permissions"],
        action: Literal["get"],
        params: "PermissionsGetParams"
    ) -> "Permission": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["list"],
        params: "CommentsListParams"
    ) -> "CommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["get"],
        params: "CommentsGetParams"
    ) -> "Comment": ...

    @overload
    async def execute(
        self,
        entity: Literal["replies"],
        action: Literal["list"],
        params: "RepliesListParams"
    ) -> "RepliesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["replies"],
        action: Literal["get"],
        params: "RepliesGetParams"
    ) -> "Reply": ...

    @overload
    async def execute(
        self,
        entity: Literal["revisions"],
        action: Literal["list"],
        params: "RevisionsListParams"
    ) -> "RevisionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["revisions"],
        action: Literal["get"],
        params: "RevisionsGetParams"
    ) -> "Revision": ...

    @overload
    async def execute(
        self,
        entity: Literal["changes"],
        action: Literal["list"],
        params: "ChangesListParams"
    ) -> "ChangesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["changes_start_page_token"],
        action: Literal["get"],
        params: "ChangesStartPageTokenGetParams"
    ) -> "StartPageToken": ...

    @overload
    async def execute(
        self,
        entity: Literal["about"],
        action: Literal["get"],
        params: "AboutGetParams"
    ) -> "About": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download"],
        params: Mapping[str, Any]
    ) -> GoogleDriveExecuteResult[Any] | GoogleDriveExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download"],
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
                return GoogleDriveExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GoogleDriveExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GoogleDriveCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GoogleDriveCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GoogleDriveCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GoogleDriveCheckResult(
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
            @GoogleDriveConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GoogleDriveConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GoogleDriveConnectorModel,
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
        return describe_entities(GoogleDriveConnectorModel)

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
            (e for e in GoogleDriveConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GoogleDriveConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GoogleDriveConnector.create(...)
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
        replication_config: "GoogleDriveReplicationConfig" | None = None,
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
            consent_url = await GoogleDriveConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Google-Drive Source",
                replication_config=GoogleDriveReplicationConfig(folder_url="...", streams="..."),
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
                definition_id=str(GoogleDriveConnectorModel.id),
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
        auth_config: "GoogleDriveAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GoogleDriveReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GoogleDriveConnector":
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
            A GoogleDriveConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GoogleDriveConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleDriveAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
            )

            # With replication config (required for this connector):
            connector = await GoogleDriveConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleDriveAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
                replication_config=GoogleDriveReplicationConfig(folder_url="...", streams="..."),
            )

            # With server-side OAuth:
            connector = await GoogleDriveConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GoogleDriveReplicationConfig(folder_url="...", streams="..."),
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
                connector_definition_id=str(GoogleDriveConnectorModel.id),
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




class FilesQuery:
    """
    Query class for Files entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_token: str | None = None,
        q: str | None = None,
        order_by: str | None = None,
        fields: str | None = None,
        spaces: str | None = None,
        corpora: str | None = None,
        drive_id: str | None = None,
        include_items_from_all_drives: bool | None = None,
        supports_all_drives: bool | None = None,
        **kwargs
    ) -> FilesListResult:
        """
        Lists the user's files. Returns a paginated list of files.

        Args:
            page_size: Maximum number of files to return per page (1-1000)
            page_token: Token for continuing a previous list request
            q: Query string for searching files
            order_by: Sort order (e.g., 'modifiedTime desc', 'name')
            fields: Fields to include in the response
            spaces: Comma-separated list of spaces to query (drive, appDataFolder)
            corpora: Bodies of items to search (user, drive, allDrives)
            drive_id: ID of the shared drive to search
            include_items_from_all_drives: Whether to include items from all drives
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            **kwargs: Additional parameters

        Returns:
            FilesListResult
        """
        params = {k: v for k, v in {
            "pageSize": page_size,
            "pageToken": page_token,
            "q": q,
            "orderBy": order_by,
            "fields": fields,
            "spaces": spaces,
            "corpora": corpora,
            "driveId": drive_id,
            "includeItemsFromAllDrives": include_items_from_all_drives,
            "supportsAllDrives": supports_all_drives,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("files", "list", params)
        # Cast generic envelope to concrete typed result
        return FilesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        file_id: str,
        fields: str | None = None,
        supports_all_drives: bool | None = None,
        **kwargs
    ) -> File:
        """
        Gets a file's metadata by ID

        Args:
            file_id: The ID of the file
            fields: Fields to include in the response
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            **kwargs: Additional parameters

        Returns:
            File
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "fields": fields,
            "supportsAllDrives": supports_all_drives,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("files", "get", params)
        return result



    async def download(
        self,
        file_id: str,
        alt: str,
        acknowledge_abuse: bool | None = None,
        supports_all_drives: bool | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary content of a file. This works for non-Google Workspace files
(PDFs, images, zip files, etc.). For Google Docs, Sheets, Slides, or Drawings,
use the export action instead.


        Args:
            file_id: The ID of the file to download
            alt: Must be set to 'media' to download file content
            acknowledge_abuse: Whether the user is acknowledging the risk of downloading known malware or other abusive files
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "alt": alt,
            "acknowledgeAbuse": acknowledge_abuse,
            "supportsAllDrives": supports_all_drives,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("files", "download", params)
        return result


    async def download_local(
        self,
        fileId: str,
        alt: str,
        path: str,
        acknowledgeAbuse: bool | None = None,
        supportsAllDrives: bool | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary content of a file. This works for non-Google Workspace files
(PDFs, images, zip files, etc.). For Google Docs, Sheets, Slides, or Drawings,
use the export action instead.
 and save to file.

        Args:
            fileId: The ID of the file to download
            alt: Must be set to 'media' to download file content
            acknowledgeAbuse: Whether the user is acknowledging the risk of downloading known malware or other abusive files
            supportsAllDrives: Whether the requesting application supports both My Drives and shared drives
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            fileId=fileId,
            alt=alt,
            acknowledgeAbuse=acknowledgeAbuse,
            supportsAllDrives=supportsAllDrives,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class FilesExportQuery:
    """
    Query class for FilesExport entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        file_id: str,
        mime_type: str,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Exports a Google Workspace file (Docs, Sheets, Slides, Drawings) to a specified format.
Common export formats:
- application/pdf (all types)
- text/plain (Docs)
- text/csv (Sheets)
- application/vnd.openxmlformats-officedocument.wordprocessingml.document (Docs to .docx)
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet (Sheets to .xlsx)
- application/vnd.openxmlformats-officedocument.presentationml.presentation (Slides to .pptx)
Note: Export has a 10MB limit. For larger files, use the Drive UI.


        Args:
            file_id: The ID of the Google Workspace file to export
            mime_type: The MIME type of the format to export to. Common values:
- application/pdf
- text/plain
- text/csv
- application/vnd.openxmlformats-officedocument.wordprocessingml.document
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- application/vnd.openxmlformats-officedocument.presentationml.presentation

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "mimeType": mime_type,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("files_export", "download", params)
        return result


    async def download_local(
        self,
        fileId: str,
        mimeType: str,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Exports a Google Workspace file (Docs, Sheets, Slides, Drawings) to a specified format.
Common export formats:
- application/pdf (all types)
- text/plain (Docs)
- text/csv (Sheets)
- application/vnd.openxmlformats-officedocument.wordprocessingml.document (Docs to .docx)
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet (Sheets to .xlsx)
- application/vnd.openxmlformats-officedocument.presentationml.presentation (Slides to .pptx)
Note: Export has a 10MB limit. For larger files, use the Drive UI.
 and save to file.

        Args:
            fileId: The ID of the Google Workspace file to export
            mimeType: The MIME type of the format to export to. Common values:
- application/pdf
- text/plain
- text/csv
- application/vnd.openxmlformats-officedocument.wordprocessingml.document
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- application/vnd.openxmlformats-officedocument.presentationml.presentation

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            fileId=fileId,
            mimeType=mimeType,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class DrivesQuery:
    """
    Query class for Drives entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_token: str | None = None,
        q: str | None = None,
        use_domain_admin_access: bool | None = None,
        **kwargs
    ) -> DrivesListResult:
        """
        Lists the user's shared drives

        Args:
            page_size: Maximum number of shared drives to return (1-100)
            page_token: Token for continuing a previous list request
            q: Query string for searching shared drives
            use_domain_admin_access: Issue the request as a domain administrator
            **kwargs: Additional parameters

        Returns:
            DrivesListResult
        """
        params = {k: v for k, v in {
            "pageSize": page_size,
            "pageToken": page_token,
            "q": q,
            "useDomainAdminAccess": use_domain_admin_access,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drives", "list", params)
        # Cast generic envelope to concrete typed result
        return DrivesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        drive_id: str,
        use_domain_admin_access: bool | None = None,
        **kwargs
    ) -> Drive:
        """
        Gets a shared drive's metadata by ID

        Args:
            drive_id: The ID of the shared drive
            use_domain_admin_access: Issue the request as a domain administrator
            **kwargs: Additional parameters

        Returns:
            Drive
        """
        params = {k: v for k, v in {
            "driveId": drive_id,
            "useDomainAdminAccess": use_domain_admin_access,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("drives", "get", params)
        return result



class PermissionsQuery:
    """
    Query class for Permissions entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        file_id: str,
        page_size: int | None = None,
        page_token: str | None = None,
        supports_all_drives: bool | None = None,
        use_domain_admin_access: bool | None = None,
        **kwargs
    ) -> PermissionsListResult:
        """
        Lists a file's or shared drive's permissions

        Args:
            file_id: The ID of the file or shared drive
            page_size: Maximum number of permissions to return (1-100)
            page_token: Token for continuing a previous list request
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            use_domain_admin_access: Issue the request as a domain administrator
            **kwargs: Additional parameters

        Returns:
            PermissionsListResult
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "pageSize": page_size,
            "pageToken": page_token,
            "supportsAllDrives": supports_all_drives,
            "useDomainAdminAccess": use_domain_admin_access,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("permissions", "list", params)
        # Cast generic envelope to concrete typed result
        return PermissionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        file_id: str,
        permission_id: str,
        supports_all_drives: bool | None = None,
        use_domain_admin_access: bool | None = None,
        **kwargs
    ) -> Permission:
        """
        Gets a permission by ID

        Args:
            file_id: The ID of the file
            permission_id: The ID of the permission
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            use_domain_admin_access: Issue the request as a domain administrator
            **kwargs: Additional parameters

        Returns:
            Permission
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "permissionId": permission_id,
            "supportsAllDrives": supports_all_drives,
            "useDomainAdminAccess": use_domain_admin_access,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("permissions", "get", params)
        return result



class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        file_id: str,
        page_size: int | None = None,
        page_token: str | None = None,
        start_modified_time: str | None = None,
        include_deleted: bool | None = None,
        fields: str | None = None,
        **kwargs
    ) -> CommentsListResult:
        """
        Lists a file's comments

        Args:
            file_id: The ID of the file
            page_size: Maximum number of comments to return (1-100)
            page_token: Token for continuing a previous list request
            start_modified_time: Minimum value of modifiedTime to filter by (RFC 3339)
            include_deleted: Whether to include deleted comments
            fields: Fields to include in the response (required for comments)
            **kwargs: Additional parameters

        Returns:
            CommentsListResult
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "pageSize": page_size,
            "pageToken": page_token,
            "startModifiedTime": start_modified_time,
            "includeDeleted": include_deleted,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "list", params)
        # Cast generic envelope to concrete typed result
        return CommentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        file_id: str,
        comment_id: str,
        include_deleted: bool | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Comment:
        """
        Gets a comment by ID

        Args:
            file_id: The ID of the file
            comment_id: The ID of the comment
            include_deleted: Whether to return deleted comments
            fields: Fields to include in the response (required for comments)
            **kwargs: Additional parameters

        Returns:
            Comment
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "commentId": comment_id,
            "includeDeleted": include_deleted,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "get", params)
        return result



class RepliesQuery:
    """
    Query class for Replies entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        file_id: str,
        comment_id: str,
        page_size: int | None = None,
        page_token: str | None = None,
        include_deleted: bool | None = None,
        fields: str | None = None,
        **kwargs
    ) -> RepliesListResult:
        """
        Lists a comment's replies

        Args:
            file_id: The ID of the file
            comment_id: The ID of the comment
            page_size: Maximum number of replies to return (1-100)
            page_token: Token for continuing a previous list request
            include_deleted: Whether to include deleted replies
            fields: Fields to include in the response (required for replies)
            **kwargs: Additional parameters

        Returns:
            RepliesListResult
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "commentId": comment_id,
            "pageSize": page_size,
            "pageToken": page_token,
            "includeDeleted": include_deleted,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("replies", "list", params)
        # Cast generic envelope to concrete typed result
        return RepliesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        file_id: str,
        comment_id: str,
        reply_id: str,
        include_deleted: bool | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Reply:
        """
        Gets a reply by ID

        Args:
            file_id: The ID of the file
            comment_id: The ID of the comment
            reply_id: The ID of the reply
            include_deleted: Whether to return deleted replies
            fields: Fields to include in the response (required for replies)
            **kwargs: Additional parameters

        Returns:
            Reply
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "commentId": comment_id,
            "replyId": reply_id,
            "includeDeleted": include_deleted,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("replies", "get", params)
        return result



class RevisionsQuery:
    """
    Query class for Revisions entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        file_id: str,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> RevisionsListResult:
        """
        Lists a file's revisions

        Args:
            file_id: The ID of the file
            page_size: Maximum number of revisions to return (1-1000)
            page_token: Token for continuing a previous list request
            **kwargs: Additional parameters

        Returns:
            RevisionsListResult
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "pageSize": page_size,
            "pageToken": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("revisions", "list", params)
        # Cast generic envelope to concrete typed result
        return RevisionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        file_id: str,
        revision_id: str,
        **kwargs
    ) -> Revision:
        """
        Gets a revision's metadata by ID

        Args:
            file_id: The ID of the file
            revision_id: The ID of the revision
            **kwargs: Additional parameters

        Returns:
            Revision
        """
        params = {k: v for k, v in {
            "fileId": file_id,
            "revisionId": revision_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("revisions", "get", params)
        return result



class ChangesQuery:
    """
    Query class for Changes entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_token: str,
        page_size: int | None = None,
        drive_id: str | None = None,
        include_items_from_all_drives: bool | None = None,
        supports_all_drives: bool | None = None,
        spaces: str | None = None,
        include_removed: bool | None = None,
        restrict_to_my_drive: bool | None = None,
        **kwargs
    ) -> ChangesListResult:
        """
        Lists the changes for a user or shared drive

        Args:
            page_token: Token for the page of changes to retrieve (from changes.getStartPageToken or previous response)
            page_size: Maximum number of changes to return (1-1000)
            drive_id: The shared drive from which changes are returned
            include_items_from_all_drives: Whether to include changes from all drives
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            spaces: Comma-separated list of spaces to query
            include_removed: Whether to include changes indicating that items have been removed
            restrict_to_my_drive: Whether to restrict the results to changes inside the My Drive hierarchy
            **kwargs: Additional parameters

        Returns:
            ChangesListResult
        """
        params = {k: v for k, v in {
            "pageToken": page_token,
            "pageSize": page_size,
            "driveId": drive_id,
            "includeItemsFromAllDrives": include_items_from_all_drives,
            "supportsAllDrives": supports_all_drives,
            "spaces": spaces,
            "includeRemoved": include_removed,
            "restrictToMyDrive": restrict_to_my_drive,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("changes", "list", params)
        # Cast generic envelope to concrete typed result
        return ChangesListResult(
            data=result.data,
            meta=result.meta
        )



class ChangesStartPageTokenQuery:
    """
    Query class for ChangesStartPageToken entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        drive_id: str | None = None,
        supports_all_drives: bool | None = None,
        **kwargs
    ) -> StartPageToken:
        """
        Gets the starting pageToken for listing future changes

        Args:
            drive_id: The ID of the shared drive for which the starting pageToken is returned
            supports_all_drives: Whether the requesting application supports both My Drives and shared drives
            **kwargs: Additional parameters

        Returns:
            StartPageToken
        """
        params = {k: v for k, v in {
            "driveId": drive_id,
            "supportsAllDrives": supports_all_drives,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("changes_start_page_token", "get", params)
        return result



class AboutQuery:
    """
    Query class for About entity operations.
    """

    def __init__(self, connector: GoogleDriveConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        fields: str | None = None,
        **kwargs
    ) -> About:
        """
        Gets information about the user, the user's Drive, and system capabilities

        Args:
            fields: Fields to include in the response (use * for all fields)
            **kwargs: Additional parameters

        Returns:
            About
        """
        params = {k: v for k, v in {
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("about", "get", params)
        return result


