"""
Linkedin-Ads connector.
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

from .connector_model import LinkedinAdsConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AccountUsersListParams,
    AccountsGetParams,
    AccountsListParams,
    AdCampaignAnalyticsListParams,
    AdCreativeAnalyticsListParams,
    CampaignGroupsGetParams,
    CampaignGroupsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    ConversionsGetParams,
    ConversionsListParams,
    CreativesGetParams,
    CreativesListParams,
    AirbyteSearchParams,
    AccountsSearchFilter,
    AccountsSearchQuery,
    AccountUsersSearchFilter,
    AccountUsersSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    CampaignGroupsSearchFilter,
    CampaignGroupsSearchQuery,
    CreativesSearchFilter,
    CreativesSearchQuery,
    ConversionsSearchFilter,
    ConversionsSearchQuery,
    AdCampaignAnalyticsSearchFilter,
    AdCampaignAnalyticsSearchQuery,
    AdCreativeAnalyticsSearchFilter,
    AdCreativeAnalyticsSearchQuery,
)
from .models import LinkedinAdsAuthConfig
if TYPE_CHECKING:
    from .models import LinkedinAdsReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    LinkedinAdsCheckResult,
    LinkedinAdsExecuteResult,
    LinkedinAdsExecuteResultWithMeta,
    AccountsListResult,
    AccountUsersListResult,
    CampaignsListResult,
    CampaignGroupsListResult,
    CreativesListResult,
    ConversionsListResult,
    AdCampaignAnalyticsListResult,
    AdCreativeAnalyticsListResult,
    Account,
    AccountUser,
    AdAnalyticsRecord,
    Campaign,
    CampaignGroup,
    Conversion,
    Creative,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    AccountUsersSearchData,
    AccountUsersSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    CampaignGroupsSearchData,
    CampaignGroupsSearchResult,
    CreativesSearchData,
    CreativesSearchResult,
    ConversionsSearchData,
    ConversionsSearchResult,
    AdCampaignAnalyticsSearchData,
    AdCampaignAnalyticsSearchResult,
    AdCreativeAnalyticsSearchData,
    AdCreativeAnalyticsSearchResult,
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




class LinkedinAdsConnector:
    """
    Type-safe Linkedin-Ads API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "linkedin-ads"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("accounts", "list"): True,
        ("accounts", "get"): None,
        ("account_users", "list"): True,
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("campaign_groups", "list"): True,
        ("campaign_groups", "get"): None,
        ("creatives", "list"): True,
        ("creatives", "get"): None,
        ("conversions", "list"): True,
        ("conversions", "get"): None,
        ("ad_campaign_analytics", "list"): True,
        ("ad_creative_analytics", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('accounts', 'list'): {'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('accounts', 'get'): {'id': 'id'},
        ('account_users', 'list'): {'q': 'q', 'accounts': 'accounts', 'count': 'count', 'start': 'start'},
        ('campaigns', 'list'): {'account_id': 'account_id', 'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('campaigns', 'get'): {'account_id': 'account_id', 'id': 'id'},
        ('campaign_groups', 'list'): {'account_id': 'account_id', 'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('campaign_groups', 'get'): {'account_id': 'account_id', 'id': 'id'},
        ('creatives', 'list'): {'account_id': 'account_id', 'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('creatives', 'get'): {'account_id': 'account_id', 'id': 'id'},
        ('conversions', 'list'): {'q': 'q', 'account': 'account', 'count': 'count', 'start': 'start'},
        ('conversions', 'get'): {'id': 'id'},
        ('ad_campaign_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_creative_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'creatives': 'creatives', 'fields': 'fields'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (LinkedinAdsAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: LinkedinAdsAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new linkedin-ads connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., LinkedinAdsAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = LinkedinAdsConnector(auth_config=LinkedinAdsAuthConfig(refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = LinkedinAdsConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = LinkedinAdsConnector(
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
                connector_definition_id=str(LinkedinAdsConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or LinkedinAdsAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=LinkedinAdsConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.accounts = AccountsQuery(self)
        self.account_users = AccountUsersQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.campaign_groups = CampaignGroupsQuery(self)
        self.creatives = CreativesQuery(self)
        self.conversions = ConversionsQuery(self)
        self.ad_campaign_analytics = AdCampaignAnalyticsQuery(self)
        self.ad_creative_analytics = AdCreativeAnalyticsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["list"],
        params: "AccountsListParams"
    ) -> "AccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams"
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["account_users"],
        action: Literal["list"],
        params: "AccountUsersListParams"
    ) -> "AccountUsersListResult": ...

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
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["list"],
        params: "CampaignGroupsListParams"
    ) -> "CampaignGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["get"],
        params: "CampaignGroupsGetParams"
    ) -> "CampaignGroup": ...

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
    ) -> "Creative": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversions"],
        action: Literal["list"],
        params: "ConversionsListParams"
    ) -> "ConversionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversions"],
        action: Literal["get"],
        params: "ConversionsGetParams"
    ) -> "Conversion": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_campaign_analytics"],
        action: Literal["list"],
        params: "AdCampaignAnalyticsListParams"
    ) -> "AdCampaignAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_creative_analytics"],
        action: Literal["list"],
        params: "AdCreativeAnalyticsListParams"
    ) -> "AdCreativeAnalyticsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> LinkedinAdsExecuteResult[Any] | LinkedinAdsExecuteResultWithMeta[Any, Any] | Any: ...

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
                return LinkedinAdsExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return LinkedinAdsExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> LinkedinAdsCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            LinkedinAdsCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return LinkedinAdsCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return LinkedinAdsCheckResult(
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
            @LinkedinAdsConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @LinkedinAdsConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    LinkedinAdsConnectorModel,
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
        return describe_entities(LinkedinAdsConnectorModel)

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
            (e for e in LinkedinAdsConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in LinkedinAdsConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await LinkedinAdsConnector.create(...)
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
        replication_config: "LinkedinAdsReplicationConfig" | None = None,
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
            consent_url = await LinkedinAdsConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Linkedin-Ads Source",
                replication_config=LinkedinAdsReplicationConfig(start_date="..."),
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
                definition_id=str(LinkedinAdsConnectorModel.id),
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
        auth_config: "LinkedinAdsAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "LinkedinAdsReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "LinkedinAdsConnector":
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
            A LinkedinAdsConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await LinkedinAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=LinkedinAdsAuthConfig(refresh_token="...", client_id="...", client_secret="..."),
            )

            # With replication config (required for this connector):
            connector = await LinkedinAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=LinkedinAdsAuthConfig(refresh_token="...", client_id="...", client_secret="..."),
                replication_config=LinkedinAdsReplicationConfig(start_date="..."),
            )

            # With server-side OAuth:
            connector = await LinkedinAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=LinkedinAdsReplicationConfig(start_date="..."),
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
                connector_definition_id=str(LinkedinAdsConnectorModel.id),
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




class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> AccountsListResult:
        """
        Returns a list of ad accounts the authenticated user has access to

        Args:
            q: Parameter q
            page_size: Number of items per page
            page_token: Token for the next page of results
            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "pageSize": page_size,
            "pageToken": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Account:
        """
        Get a single ad account by ID

        Args:
            id: Ad account ID
            **kwargs: Additional parameters

        Returns:
            Account
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def search(
        self,
        query: AccountsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AccountsSearchResult:
        """
        Search accounts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AccountsSearchFilter):
        - id: Unique account identifier
        - name: Account name
        - currency: Currency code used by the account
        - status: Account status
        - type_: Account type
        - reference: Reference organization URN
        - test: Whether this is a test account
        - notified_on_campaign_optimization: Flag for notifications on campaign optimization
        - notified_on_creative_approval: Flag for notifications on creative approval
        - notified_on_creative_rejection: Flag for notifications on creative rejection
        - notified_on_end_of_campaign: Flag for notifications on end of campaign
        - notified_on_new_features_enabled: Flag for notifications on new features
        - serving_statuses: List of serving statuses
        - version: Version information

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("accounts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AccountsSearchResult(
            data=[
                AccountsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AccountUsersQuery:
    """
    Query class for AccountUsers entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        accounts: str,
        count: int | None = None,
        start: int | None = None,
        **kwargs
    ) -> AccountUsersListResult:
        """
        Returns a list of users associated with ad accounts

        Args:
            q: Parameter q
            accounts: Account URN, e.g. urn:li:sponsoredAccount:123456
            count: Number of items per page
            start: Offset for pagination
            **kwargs: Additional parameters

        Returns:
            AccountUsersListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "accounts": accounts,
            "count": count,
            "start": start,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("account_users", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountUsersListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AccountUsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AccountUsersSearchResult:
        """
        Search account_users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AccountUsersSearchFilter):
        - account: Associated account URN
        - user: User URN
        - role: User role in the account

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountUsersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("account_users", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AccountUsersSearchResult(
            data=[
                AccountUsersSearchData(**row)
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

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        q: str,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a list of campaigns for an ad account

        Args:
            account_id: Ad account ID
            q: Parameter q
            page_size: Number of items per page
            page_token: Token for the next page of results
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "q": q,
            "pageSize": page_size,
            "pageToken": page_token,
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
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> Campaign:
        """
        Get a single campaign by ID

        Args:
            account_id: Ad account ID
            id: Campaign ID
            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "account_id": account_id,
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
        - id: Unique campaign identifier
        - name: Campaign name
        - account: Associated account URN
        - campaign_group: Parent campaign group URN
        - status: Campaign status
        - type_: Campaign type
        - cost_type: Cost type (CPC CPM etc)
        - format: Campaign ad format
        - objective_type: Campaign objective type
        - optimization_target_type: Optimization target type
        - creative_selection: Creative selection mode
        - pacing_strategy: Budget pacing strategy
        - audience_expansion_enabled: Whether audience expansion is enabled
        - offsite_delivery_enabled: Whether offsite delivery is enabled
        - story_delivery_enabled: Whether story delivery is enabled
        - test: Whether this is a test campaign
        - associated_entity: Associated entity URN
        - daily_budget: Daily budget configuration
        - total_budget: Total budget configuration
        - unit_cost: Cost per unit (bid amount)
        - run_schedule: Campaign run schedule
        - locale: Campaign locale settings
        - serving_statuses: List of serving statuses
        - version: Version information

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

class CampaignGroupsQuery:
    """
    Query class for CampaignGroups entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        q: str,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> CampaignGroupsListResult:
        """
        Returns a list of campaign groups for an ad account

        Args:
            account_id: Ad account ID
            q: Parameter q
            page_size: Number of items per page
            page_token: Token for the next page of results
            **kwargs: Additional parameters

        Returns:
            CampaignGroupsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "q": q,
            "pageSize": page_size,
            "pageToken": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignGroupsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> CampaignGroup:
        """
        Get a single campaign group by ID

        Args:
            account_id: Ad account ID
            id: Campaign group ID
            **kwargs: Additional parameters

        Returns:
            CampaignGroup
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_groups", "get", params)
        return result



    async def search(
        self,
        query: CampaignGroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignGroupsSearchResult:
        """
        Search campaign_groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignGroupsSearchFilter):
        - id: Unique campaign group identifier
        - name: Campaign group name
        - account: Associated account URN
        - status: Campaign group status
        - test: Whether this is a test campaign group
        - backfilled: Whether the campaign group is backfilled
        - total_budget: Total budget for the campaign group
        - run_schedule: Campaign group run schedule
        - serving_statuses: List of serving statuses
        - allowed_campaign_types: Types of campaigns allowed in this group

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignGroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaign_groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignGroupsSearchResult(
            data=[
                CampaignGroupsSearchData(**row)
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

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        q: str,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> CreativesListResult:
        """
        Returns a list of creatives for an ad account

        Args:
            account_id: Ad account ID
            q: Parameter q
            page_size: Number of items per page
            page_token: Token for the next page of results
            **kwargs: Additional parameters

        Returns:
            CreativesListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "q": q,
            "pageSize": page_size,
            "pageToken": page_token,
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
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> Creative:
        """
        Get a single creative by ID

        Args:
            account_id: Ad account ID
            id: Creative ID
            **kwargs: Additional parameters

        Returns:
            Creative
        """
        params = {k: v for k, v in {
            "account_id": account_id,
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
        - id: Unique creative identifier
        - name: Creative name
        - account: Associated account URN
        - campaign: Parent campaign URN
        - intended_status: Intended creative status
        - is_serving: Whether the creative is currently serving
        - is_test: Whether this is a test creative
        - created_at: Creation timestamp (epoch milliseconds)
        - created_by: URN of the user who created the creative
        - last_modified_at: Last modification timestamp (epoch milliseconds)
        - last_modified_by: URN of the user who last modified the creative
        - content: Creative content configuration
        - serving_hold_reasons: Reasons for holding creative from serving

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

class ConversionsQuery:
    """
    Query class for Conversions entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        account: str,
        count: int | None = None,
        start: int | None = None,
        **kwargs
    ) -> ConversionsListResult:
        """
        Returns a list of conversion rules for an ad account

        Args:
            q: Parameter q
            account: Account URN, e.g. urn:li:sponsoredAccount:123456
            count: Number of items per page
            start: Offset for pagination
            **kwargs: Additional parameters

        Returns:
            ConversionsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "account": account,
            "count": count,
            "start": start,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversions", "list", params)
        # Cast generic envelope to concrete typed result
        return ConversionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Conversion:
        """
        Get a single conversion rule by ID

        Args:
            id: Conversion ID
            **kwargs: Additional parameters

        Returns:
            Conversion
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversions", "get", params)
        return result



    async def search(
        self,
        query: ConversionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ConversionsSearchResult:
        """
        Search conversions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ConversionsSearchFilter):
        - id: Unique conversion identifier
        - name: Conversion name
        - account: Associated account URN
        - type_: Conversion type
        - attribution_type: Attribution type for the conversion
        - enabled: Whether the conversion tracking is enabled
        - created: Creation timestamp (epoch milliseconds)
        - last_modified: Last modification timestamp (epoch milliseconds)
        - post_click_attribution_window_size: Post-click attribution window size in days
        - view_through_attribution_window_size: View-through attribution window size in days
        - campaigns: Related campaign URNs
        - associated_campaigns: Associated campaigns
        - image_pixel_tag: Image pixel tracking tag
        - value: Conversion value

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ConversionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("conversions", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ConversionsSearchResult(
            data=[
                ConversionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdCampaignAnalyticsQuery:
    """
    Query class for AdCampaignAnalytics entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        pivot: str,
        time_granularity: str,
        date_range: str,
        campaigns: str,
        fields: str | None = None,
        **kwargs
    ) -> AdCampaignAnalyticsListResult:
        """
        Returns ad analytics data pivoted by campaign. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by campaign.


        Args:
            q: Parameter q
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdCampaignAnalyticsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "pivot": pivot,
            "timeGranularity": time_granularity,
            "dateRange": date_range,
            "campaigns": campaigns,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_campaign_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdCampaignAnalyticsListResult(
            data=result.data
        )



    async def search(
        self,
        query: AdCampaignAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdCampaignAnalyticsSearchResult:
        """
        Search ad_campaign_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdCampaignAnalyticsSearchFilter):
        - impressions: Number of times the ad was shown
        - clicks: Number of clicks on the ad
        - cost_in_local_currency: Total cost in the accounts local currency
        - cost_in_usd: Total cost in USD
        - likes: Number of likes
        - shares: Number of shares
        - comments: Number of comments
        - reactions: Number of reactions
        - follows: Number of follows
        - total_engagements: Total number of engagements
        - landing_page_clicks: Number of landing page clicks
        - company_page_clicks: Number of company page clicks
        - external_website_conversions: Number of conversions on external websites
        - external_website_post_click_conversions: Post-click conversions on external websites
        - external_website_post_view_conversions: Post-view conversions on external websites
        - conversion_value_in_local_currency: Conversion value in local currency
        - approximate_member_reach: Approximate unique member reach
        - card_clicks: Number of carousel card clicks
        - card_impressions: Number of carousel card impressions
        - video_starts: Number of video starts
        - video_views: Number of video views
        - video_first_quartile_completions: Number of times video played to 25%
        - video_midpoint_completions: Number of times video played to 50%
        - video_third_quartile_completions: Number of times video played to 75%
        - video_completions: Number of times video played to 100%
        - full_screen_plays: Number of full screen video plays
        - one_click_leads: Number of one-click leads
        - one_click_lead_form_opens: Number of one-click lead form opens
        - other_engagements: Number of other engagements
        - ad_unit_clicks: Number of ad unit clicks
        - action_clicks: Number of action clicks
        - text_url_clicks: Number of text URL clicks
        - comment_likes: Number of comment likes
        - sends: Number of sends (InMail)
        - opens: Number of opens (InMail)
        - download_clicks: Number of download clicks
        - pivot_values: Pivot values (URNs) for this analytics record
        - start_date: Start date of the ad analytics data
        - end_date: End date of the ad analytics data

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdCampaignAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_campaign_analytics", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdCampaignAnalyticsSearchResult(
            data=[
                AdCampaignAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdCreativeAnalyticsQuery:
    """
    Query class for AdCreativeAnalytics entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        pivot: str,
        time_granularity: str,
        date_range: str,
        creatives: str,
        fields: str | None = None,
        **kwargs
    ) -> AdCreativeAnalyticsListResult:
        """
        Returns ad analytics data pivoted by creative. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by creative.


        Args:
            q: Parameter q
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            creatives: List of creative URNs, e.g. List(urn%3Ali%3AsponsoredCreative%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdCreativeAnalyticsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "pivot": pivot,
            "timeGranularity": time_granularity,
            "dateRange": date_range,
            "creatives": creatives,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_creative_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdCreativeAnalyticsListResult(
            data=result.data
        )



    async def search(
        self,
        query: AdCreativeAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdCreativeAnalyticsSearchResult:
        """
        Search ad_creative_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdCreativeAnalyticsSearchFilter):
        - impressions: Number of times the ad was shown
        - clicks: Number of clicks on the ad
        - cost_in_local_currency: Total cost in the accounts local currency
        - cost_in_usd: Total cost in USD
        - likes: Number of likes
        - shares: Number of shares
        - comments: Number of comments
        - reactions: Number of reactions
        - follows: Number of follows
        - total_engagements: Total number of engagements
        - landing_page_clicks: Number of landing page clicks
        - company_page_clicks: Number of company page clicks
        - external_website_conversions: Number of conversions on external websites
        - external_website_post_click_conversions: Post-click conversions on external websites
        - external_website_post_view_conversions: Post-view conversions on external websites
        - conversion_value_in_local_currency: Conversion value in local currency
        - approximate_member_reach: Approximate unique member reach
        - card_clicks: Number of carousel card clicks
        - card_impressions: Number of carousel card impressions
        - video_starts: Number of video starts
        - video_views: Number of video views
        - video_first_quartile_completions: Number of times video played to 25%
        - video_midpoint_completions: Number of times video played to 50%
        - video_third_quartile_completions: Number of times video played to 75%
        - video_completions: Number of times video played to 100%
        - full_screen_plays: Number of full screen video plays
        - one_click_leads: Number of one-click leads
        - one_click_lead_form_opens: Number of one-click lead form opens
        - other_engagements: Number of other engagements
        - ad_unit_clicks: Number of ad unit clicks
        - action_clicks: Number of action clicks
        - text_url_clicks: Number of text URL clicks
        - comment_likes: Number of comment likes
        - sends: Number of sends (InMail)
        - opens: Number of opens (InMail)
        - download_clicks: Number of download clicks
        - pivot_values: Pivot values (URNs) for this analytics record
        - start_date: Start date of the ad analytics data
        - end_date: End date of the ad analytics data

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdCreativeAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_creative_analytics", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdCreativeAnalyticsSearchResult(
            data=[
                AdCreativeAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
