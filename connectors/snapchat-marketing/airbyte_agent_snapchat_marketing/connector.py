"""
Snapchat-Marketing connector.
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

from .connector_model import SnapchatMarketingConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AdaccountsGetParams,
    AdaccountsListParams,
    AdsGetParams,
    AdsListParams,
    AdsquadsGetParams,
    AdsquadsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    CreativesGetParams,
    CreativesListParams,
    MediaGetParams,
    MediaListParams,
    OrganizationsGetParams,
    OrganizationsListParams,
    SegmentsGetParams,
    SegmentsListParams,
    AirbyteSearchParams,
    OrganizationsSearchFilter,
    OrganizationsSearchQuery,
    AdaccountsSearchFilter,
    AdaccountsSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    AdsquadsSearchFilter,
    AdsquadsSearchQuery,
    AdsSearchFilter,
    AdsSearchQuery,
    CreativesSearchFilter,
    CreativesSearchQuery,
    MediaSearchFilter,
    MediaSearchQuery,
    SegmentsSearchFilter,
    SegmentsSearchQuery,
)
from .models import SnapchatMarketingAuthConfig
if TYPE_CHECKING:
    from .models import SnapchatMarketingReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    SnapchatMarketingCheckResult,
    SnapchatMarketingExecuteResult,
    SnapchatMarketingExecuteResultWithMeta,
    OrganizationsListResult,
    AdaccountsListResult,
    CampaignsListResult,
    AdsquadsListResult,
    AdsListResult,
    CreativesListResult,
    MediaListResult,
    SegmentsListResult,
    Ad,
    AdAccount,
    AdSquad,
    Campaign,
    Creative,
    Media,
    Organization,
    Segment,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    OrganizationsSearchData,
    OrganizationsSearchResult,
    AdaccountsSearchData,
    AdaccountsSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdsquadsSearchData,
    AdsquadsSearchResult,
    AdsSearchData,
    AdsSearchResult,
    CreativesSearchData,
    CreativesSearchResult,
    MediaSearchData,
    MediaSearchResult,
    SegmentsSearchData,
    SegmentsSearchResult,
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




class SnapchatMarketingConnector:
    """
    Type-safe Snapchat-Marketing API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "snapchat-marketing"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("organizations", "list"): True,
        ("organizations", "get"): None,
        ("adaccounts", "list"): True,
        ("adaccounts", "get"): None,
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("adsquads", "list"): True,
        ("adsquads", "get"): None,
        ("ads", "list"): True,
        ("ads", "get"): None,
        ("creatives", "list"): True,
        ("creatives", "get"): None,
        ("media", "list"): True,
        ("media", "get"): None,
        ("segments", "list"): True,
        ("segments", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('organizations', 'get'): {'id': 'id'},
        ('adaccounts', 'list'): {'organization_id': 'organization_id'},
        ('adaccounts', 'get'): {'id': 'id'},
        ('campaigns', 'list'): {'ad_account_id': 'ad_account_id'},
        ('campaigns', 'get'): {'id': 'id'},
        ('adsquads', 'list'): {'ad_account_id': 'ad_account_id'},
        ('adsquads', 'get'): {'id': 'id'},
        ('ads', 'list'): {'ad_account_id': 'ad_account_id'},
        ('ads', 'get'): {'id': 'id'},
        ('creatives', 'list'): {'ad_account_id': 'ad_account_id'},
        ('creatives', 'get'): {'id': 'id'},
        ('media', 'list'): {'ad_account_id': 'ad_account_id'},
        ('media', 'get'): {'id': 'id'},
        ('segments', 'list'): {'ad_account_id': 'ad_account_id'},
        ('segments', 'get'): {'id': 'id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (SnapchatMarketingAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: SnapchatMarketingAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new snapchat-marketing connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., SnapchatMarketingAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = SnapchatMarketingConnector(auth_config=SnapchatMarketingAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = SnapchatMarketingConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = SnapchatMarketingConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
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
                customer_name=auth_config.customer_name,
                organization_id=auth_config.organization_id,
                connector_definition_id=str(SnapchatMarketingConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or SnapchatMarketingAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=SnapchatMarketingConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.organizations = OrganizationsQuery(self)
        self.adaccounts = AdaccountsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.adsquads = AdsquadsQuery(self)
        self.ads = AdsQuery(self)
        self.creatives = CreativesQuery(self)
        self.media = MediaQuery(self)
        self.segments = SegmentsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["list"],
        params: "OrganizationsListParams"
    ) -> "OrganizationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["get"],
        params: "OrganizationsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["adaccounts"],
        action: Literal["list"],
        params: "AdaccountsListParams"
    ) -> "AdaccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["adaccounts"],
        action: Literal["get"],
        params: "AdaccountsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams"
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["adsquads"],
        action: Literal["list"],
        params: "AdsquadsListParams"
    ) -> "AdsquadsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["adsquads"],
        action: Literal["get"],
        params: "AdsquadsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads"],
        action: Literal["list"],
        params: "AdsListParams"
    ) -> "AdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads"],
        action: Literal["get"],
        params: "AdsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["list"],
        params: "CreativesListParams"
    ) -> "CreativesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["get"],
        params: "CreativesGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["media"],
        action: Literal["list"],
        params: "MediaListParams"
    ) -> "MediaListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["media"],
        action: Literal["get"],
        params: "MediaGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["list"],
        params: "SegmentsListParams"
    ) -> "SegmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["get"],
        params: "SegmentsGetParams"
    ) -> "dict[str, Any]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> SnapchatMarketingExecuteResult[Any] | SnapchatMarketingExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
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
                return SnapchatMarketingExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SnapchatMarketingExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SnapchatMarketingCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SnapchatMarketingCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SnapchatMarketingCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SnapchatMarketingCheckResult(
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
            @SnapchatMarketingConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @SnapchatMarketingConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    SnapchatMarketingConnectorModel,
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
        return describe_entities(SnapchatMarketingConnectorModel)

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
            (e for e in SnapchatMarketingConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SnapchatMarketingConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await SnapchatMarketingConnector.create(...)
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
        replication_config: "SnapchatMarketingReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + customer_name.
            replication_config: Typed replication settings. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await SnapchatMarketingConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Snapchat-Marketing Source",
                replication_config=SnapchatMarketingReplicationConfig(start_date="..."),
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for get_consent_url()")

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(SnapchatMarketingConnectorModel.id),
                customer_name=airbyte_config.customer_name,
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
        auth_config: "SnapchatMarketingAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "SnapchatMarketingReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "SnapchatMarketingConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A SnapchatMarketingConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await SnapchatMarketingConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=SnapchatMarketingAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
            )

            # With replication config (required for this connector):
            connector = await SnapchatMarketingConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=SnapchatMarketingAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
                replication_config=SnapchatMarketingReplicationConfig(start_date="..."),
            )

            # With server-side OAuth:
            connector = await SnapchatMarketingConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=SnapchatMarketingReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")

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
            organization_id=airbyte_config.organization_id,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(SnapchatMarketingConnectorModel.id),
                customer_name=airbyte_config.customer_name,
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
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )




class OrganizationsQuery:
    """
    Query class for Organizations entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> OrganizationsListResult:
        """
        Returns the organizations the authenticated user belongs to

        Returns:
            OrganizationsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "list", params)
        # Cast generic envelope to concrete typed result
        return OrganizationsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single organization by ID

        Args:
            id: Organization ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "get", params)
        return result



    async def search(
        self,
        query: OrganizationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrganizationsSearchResult:
        """
        Search organizations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrganizationsSearchFilter):
        - accepted_term_version: Version of accepted terms
        - address_line_1: Street address
        - administrative_district_level_1: State or province
        - configuration_settings: Organization configuration settings
        - contact_email: Contact email address
        - contact_name: Contact person name
        - contact_phone: Contact phone number
        - contact_phone_optin: Whether the contact opted in for phone communications
        - country: Country code
        - created_by_caller: Whether the organization was created by the caller
        - created_at: Creation timestamp
        - id: Unique organization identifier
        - locality: City or locality
        - my_display_name: Display name of the authenticated user in the organization
        - my_invited_email: Email used to invite the authenticated user
        - my_member_id: Member ID of the authenticated user
        - name: Organization name
        - postal_code: Postal code
        - roles: Roles of the authenticated user in this organization
        - state: Organization state
        - type_: Organization type
        - updated_at: Last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrganizationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("organizations", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrganizationsSearchResult(
            data=[
                OrganizationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdaccountsQuery:
    """
    Query class for Adaccounts entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        organization_id: str,
        **kwargs
    ) -> AdaccountsListResult:
        """
        Returns ad accounts belonging to an organization

        Args:
            organization_id: Organization ID
            **kwargs: Additional parameters

        Returns:
            AdaccountsListResult
        """
        params = {k: v for k, v in {
            "organization_id": organization_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("adaccounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AdaccountsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single ad account by ID

        Args:
            id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("adaccounts", "get", params)
        return result



    async def search(
        self,
        query: AdaccountsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdaccountsSearchResult:
        """
        Search adaccounts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdaccountsSearchFilter):
        - advertiser_organization_id: Advertiser organization ID
        - agency_representing_client: Whether the account is managed by an agency
        - billing_center_id: Billing center ID
        - billing_type: Billing type
        - client_paying_invoices: Whether the client pays invoices directly
        - created_at: Creation timestamp
        - currency: Account currency code
        - funding_source_ids: Associated funding source IDs
        - id: Unique ad account identifier
        - name: Ad account name
        - organization_id: Parent organization ID
        - regulations: Regulatory settings
        - status: Ad account status
        - timezone: Account timezone
        - type_: Ad account type
        - updated_at: Last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdaccountsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("adaccounts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdaccountsSearchResult(
            data=[
                AdaccountsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns campaigns belonging to an ad account

        Args:
            ad_account_id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single campaign by ID

        Args:
            id: Campaign ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def search(
        self,
        query: CampaignsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsSearchResult:
        """
        Search campaigns records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsSearchFilter):
        - ad_account_id: Parent ad account ID
        - buy_model: Buy model type
        - created_at: Creation timestamp
        - creation_state: Creation state
        - delivery_status: Delivery status messages
        - id: Unique campaign identifier
        - name: Campaign name
        - objective: Campaign objective
        - start_time: Campaign start time
        - status: Campaign status
        - updated_at: Last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaigns", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignsSearchResult(
            data=[
                CampaignsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdsquadsQuery:
    """
    Query class for Adsquads entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        **kwargs
    ) -> AdsquadsListResult:
        """
        Returns ad squads belonging to an ad account

        Args:
            ad_account_id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            AdsquadsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("adsquads", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsquadsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single ad squad by ID

        Args:
            id: Ad Squad ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("adsquads", "get", params)
        return result



    async def search(
        self,
        query: AdsquadsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsquadsSearchResult:
        """
        Search adsquads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsquadsSearchFilter):
        - auto_bid: Whether auto bidding is enabled
        - bid_strategy: Bid strategy
        - billing_event: Billing event type
        - campaign_id: Parent campaign ID
        - child_ad_type: Child ad type
        - created_at: Creation timestamp
        - creation_state: Creation state
        - daily_budget_micro: Daily budget in micro-currency
        - delivery_constraint: Delivery constraint
        - delivery_properties_version: Delivery properties version
        - delivery_status: Delivery status messages
        - end_time: Ad squad end time
        - event_sources: Event sources configuration
        - forced_view_setting: Forced view setting
        - id: Unique ad squad identifier
        - lifetime_budget_micro: Lifetime budget in micro-currency
        - name: Ad squad name
        - optimization_goal: Optimization goal
        - pacing_type: Pacing type
        - placement: Placement type
        - skadnetwork_properties: SKAdNetwork properties
        - start_time: Ad squad start time
        - status: Ad squad status
        - target_bid: Whether target bid is enabled
        - targeting: Targeting specification
        - targeting_reach_status: Targeting reach status
        - type_: Ad squad type
        - updated_at: Last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsquadsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("adsquads", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsquadsSearchResult(
            data=[
                AdsquadsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdsQuery:
    """
    Query class for Ads entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        **kwargs
    ) -> AdsListResult:
        """
        Returns ads belonging to an ad account

        Args:
            ad_account_id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            AdsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single ad by ID

        Args:
            id: Ad ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads", "get", params)
        return result



    async def search(
        self,
        query: AdsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsSearchResult:
        """
        Search ads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsSearchFilter):
        - ad_squad_id: Parent ad squad ID
        - created_at: Creation timestamp
        - creative_id: Associated creative ID
        - delivery_status: Delivery status messages
        - id: Unique ad identifier
        - name: Ad name
        - render_type: Render type
        - review_status: Review status
        - review_status_reasons: Reasons for review status
        - status: Ad status
        - type_: Ad type
        - updated_at: Last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ads", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsSearchResult(
            data=[
                AdsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CreativesQuery:
    """
    Query class for Creatives entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        **kwargs
    ) -> CreativesListResult:
        """
        Returns creatives belonging to an ad account

        Args:
            ad_account_id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            CreativesListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creatives", "list", params)
        # Cast generic envelope to concrete typed result
        return CreativesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single creative by ID

        Args:
            id: Creative ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creatives", "get", params)
        return result



    async def search(
        self,
        query: CreativesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CreativesSearchResult:
        """
        Search creatives records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CreativesSearchFilter):
        - ad_account_id: Parent ad account ID
        - ad_product: Ad product type
        - ad_to_place_properties: Ad-to-place properties
        - brand_name: Brand name displayed in the creative
        - call_to_action: Call to action text
        - created_at: Creation timestamp
        - forced_view_eligibility: Forced view eligibility status
        - headline: Creative headline
        - id: Unique creative identifier
        - name: Creative name
        - packaging_status: Packaging status
        - render_type: Render type
        - review_status: Review status
        - review_status_details: Details about the review status
        - shareable: Whether the creative is shareable
        - top_snap_crop_position: Top snap crop position
        - top_snap_media_id: Top snap media ID
        - type_: Creative type
        - updated_at: Last update timestamp
        - web_view_properties: Web view properties

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CreativesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("creatives", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CreativesSearchResult(
            data=[
                CreativesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MediaQuery:
    """
    Query class for Media entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        **kwargs
    ) -> MediaListResult:
        """
        Returns media belonging to an ad account

        Args:
            ad_account_id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            MediaListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("media", "list", params)
        # Cast generic envelope to concrete typed result
        return MediaListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single media item by ID

        Args:
            id: Media ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("media", "get", params)
        return result



    async def search(
        self,
        query: MediaSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MediaSearchResult:
        """
        Search media records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MediaSearchFilter):
        - ad_account_id: Parent ad account ID
        - created_at: Creation timestamp
        - download_link: Download URL for the media
        - duration_in_seconds: Duration in seconds for video media
        - file_name: Original file name
        - file_size_in_bytes: File size in bytes
        - hash: Media file hash
        - id: Unique media identifier
        - image_metadata: Image-specific metadata
        - is_demo_media: Whether this is demo media
        - media_status: Media processing status
        - media_usages: Where the media is used
        - name: Media name
        - type_: Media type
        - updated_at: Last update timestamp
        - video_metadata: Video-specific metadata
        - visibility: Media visibility setting

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MediaSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("media", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MediaSearchResult(
            data=[
                MediaSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SegmentsQuery:
    """
    Query class for Segments entity operations.
    """

    def __init__(self, connector: SnapchatMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        **kwargs
    ) -> SegmentsListResult:
        """
        Returns audience segments belonging to an ad account

        Args:
            ad_account_id: Ad Account ID
            **kwargs: Additional parameters

        Returns:
            SegmentsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "list", params)
        # Cast generic envelope to concrete typed result
        return SegmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single audience segment by ID

        Args:
            id: Segment ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "get", params)
        return result



    async def search(
        self,
        query: SegmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SegmentsSearchResult:
        """
        Search segments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SegmentsSearchFilter):
        - ad_account_id: Parent ad account ID
        - approximate_number_users: Approximate number of users in the segment
        - created_at: Creation timestamp
        - description: Segment description
        - id: Unique segment identifier
        - name: Segment name
        - organization_id: Parent organization ID
        - retention_in_days: Data retention period in days
        - source_type: Segment source type
        - status: Segment status
        - targetable_status: Whether the segment is targetable
        - updated_at: Last update timestamp
        - upload_status: Upload processing status
        - visible_to: Visibility settings

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SegmentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("segments", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SegmentsSearchResult(
            data=[
                SegmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
