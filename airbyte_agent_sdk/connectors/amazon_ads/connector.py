"""
Amazon-Ads connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import AmazonAdsConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    PortfoliosGetParams,
    PortfoliosListParams,
    ProfilesGetParams,
    ProfilesListParams,
    SponsoredBrandsAdGroupsListParams,
    SponsoredBrandsAdGroupsListParamsStatefilter,
    SponsoredBrandsCampaignsListParams,
    SponsoredBrandsCampaignsListParamsStatefilter,
    SponsoredProductAdGroupsListParams,
    SponsoredProductAdGroupsListParamsStatefilter,
    SponsoredProductCampaignsGetParams,
    SponsoredProductCampaignsListParams,
    SponsoredProductCampaignsListParamsStatefilter,
    SponsoredProductKeywordsListParams,
    SponsoredProductKeywordsListParamsStatefilter,
    SponsoredProductNegativeKeywordsListParams,
    SponsoredProductNegativeKeywordsListParamsStatefilter,
    SponsoredProductNegativeTargetsListParams,
    SponsoredProductNegativeTargetsListParamsStatefilter,
    SponsoredProductProductAdsListParams,
    SponsoredProductProductAdsListParamsStatefilter,
    SponsoredProductTargetsListParams,
    SponsoredProductTargetsListParamsStatefilter,
    AirbyteSearchParams,
    ProfilesSearchFilter,
    ProfilesSearchQuery,
)
from .models import AmazonAdsAuthConfig

# Import response models and envelope models at runtime
from .models import (
    AmazonAdsCheckResult,
    AmazonAdsExecuteResult,
    AmazonAdsExecuteResultWithMeta,
    ProfilesListResult,
    PortfoliosListResult,
    SponsoredProductCampaignsListResult,
    SponsoredProductAdGroupsListResult,
    SponsoredProductKeywordsListResult,
    SponsoredProductProductAdsListResult,
    SponsoredProductTargetsListResult,
    SponsoredProductNegativeKeywordsListResult,
    SponsoredProductNegativeTargetsListResult,
    SponsoredBrandsCampaignsListResult,
    SponsoredBrandsAdGroupsListResult,
    Portfolio,
    Profile,
    SponsoredProductCampaign,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ProfilesSearchData,
    ProfilesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 100_000  # ~100KB default, configurable per-tool


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




class AmazonAdsConnector:
    """
    Type-safe Amazon-Ads API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "amazon-ads"
    connector_version = "1.0.10"
    sdk_version = "0.1.66"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("profiles", "list"): True,
        ("profiles", "get"): None,
        ("portfolios", "list"): True,
        ("portfolios", "get"): None,
        ("sponsored_product_campaigns", "list"): True,
        ("sponsored_product_campaigns", "get"): None,
        ("sponsored_product_ad_groups", "list"): True,
        ("sponsored_product_keywords", "list"): True,
        ("sponsored_product_product_ads", "list"): True,
        ("sponsored_product_targets", "list"): True,
        ("sponsored_product_negative_keywords", "list"): True,
        ("sponsored_product_negative_targets", "list"): True,
        ("sponsored_brands_campaigns", "list"): True,
        ("sponsored_brands_ad_groups", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('profiles', 'list'): {'profile_type_filter': 'profileTypeFilter'},
        ('profiles', 'get'): {'profile_id': 'profileId'},
        ('portfolios', 'list'): {'include_extended_data_fields': 'includeExtendedDataFields'},
        ('portfolios', 'get'): {'portfolio_id': 'portfolioId'},
        ('sponsored_product_campaigns', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_product_campaigns', 'get'): {'campaign_id': 'campaignId'},
        ('sponsored_product_ad_groups', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_product_keywords', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_product_product_ads', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_product_targets', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_product_negative_keywords', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_product_negative_targets', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_brands_campaigns', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
        ('sponsored_brands_ad_groups', 'list'): {'state_filter': 'stateFilter', 'max_results': 'maxResults', 'next_token': 'nextToken'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (AmazonAdsAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: AmazonAdsAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        region: str | None = None    ):
        """
        Initialize a new amazon-ads connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., AmazonAdsAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            region: The Amazon Ads API endpoint URL based on region:
- NA (North America): https://advertising-api.amazon.com
- EU (Europe): https://advertising-api-eu.amazon.com
- FE (Far East): https://advertising-api-fe.amazon.com

        Examples:
            # Local mode (direct API calls)
            connector = AmazonAdsConnector(auth_config=AmazonAdsAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = AmazonAdsConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = AmazonAdsConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
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
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(AmazonAdsConnectorModel.id),
                model=AmazonAdsConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or AmazonAdsAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if region:
                config_values["region"] = region

            self._executor = LocalExecutor(
                model=AmazonAdsConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if region:
                base_url = base_url.replace("{region}", region)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.profiles = ProfilesQuery(self)
        self.portfolios = PortfoliosQuery(self)
        self.sponsored_product_campaigns = SponsoredProductCampaignsQuery(self)
        self.sponsored_product_ad_groups = SponsoredProductAdGroupsQuery(self)
        self.sponsored_product_keywords = SponsoredProductKeywordsQuery(self)
        self.sponsored_product_product_ads = SponsoredProductProductAdsQuery(self)
        self.sponsored_product_targets = SponsoredProductTargetsQuery(self)
        self.sponsored_product_negative_keywords = SponsoredProductNegativeKeywordsQuery(self)
        self.sponsored_product_negative_targets = SponsoredProductNegativeTargetsQuery(self)
        self.sponsored_brands_campaigns = SponsoredBrandsCampaignsQuery(self)
        self.sponsored_brands_ad_groups = SponsoredBrandsAdGroupsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["profiles"],
        action: Literal["list"],
        params: "ProfilesListParams"
    ) -> "ProfilesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["profiles"],
        action: Literal["get"],
        params: "ProfilesGetParams"
    ) -> "Profile": ...

    @overload
    async def execute(
        self,
        entity: Literal["portfolios"],
        action: Literal["list"],
        params: "PortfoliosListParams"
    ) -> "PortfoliosListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["portfolios"],
        action: Literal["get"],
        params: "PortfoliosGetParams"
    ) -> "Portfolio": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_campaigns"],
        action: Literal["list"],
        params: "SponsoredProductCampaignsListParams"
    ) -> "SponsoredProductCampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_campaigns"],
        action: Literal["get"],
        params: "SponsoredProductCampaignsGetParams"
    ) -> "SponsoredProductCampaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_ad_groups"],
        action: Literal["list"],
        params: "SponsoredProductAdGroupsListParams"
    ) -> "SponsoredProductAdGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_keywords"],
        action: Literal["list"],
        params: "SponsoredProductKeywordsListParams"
    ) -> "SponsoredProductKeywordsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_product_ads"],
        action: Literal["list"],
        params: "SponsoredProductProductAdsListParams"
    ) -> "SponsoredProductProductAdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_targets"],
        action: Literal["list"],
        params: "SponsoredProductTargetsListParams"
    ) -> "SponsoredProductTargetsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_negative_keywords"],
        action: Literal["list"],
        params: "SponsoredProductNegativeKeywordsListParams"
    ) -> "SponsoredProductNegativeKeywordsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_product_negative_targets"],
        action: Literal["list"],
        params: "SponsoredProductNegativeTargetsListParams"
    ) -> "SponsoredProductNegativeTargetsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_brands_campaigns"],
        action: Literal["list"],
        params: "SponsoredBrandsCampaignsListParams"
    ) -> "SponsoredBrandsCampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sponsored_brands_ad_groups"],
        action: Literal["list"],
        params: "SponsoredBrandsAdGroupsListParams"
    ) -> "SponsoredBrandsAdGroupsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "context_store_search"],
        params: Mapping[str, Any]
    ) -> AmazonAdsExecuteResult[Any] | AmazonAdsExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "context_store_search"],
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
        from airbyte_agent_sdk.executor import ExecutionConfig

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
                return AmazonAdsExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return AmazonAdsExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> AmazonAdsCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            AmazonAdsCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return AmazonAdsCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return AmazonAdsCheckResult(
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
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @AmazonAdsConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @AmazonAdsConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    AmazonAdsConnectorModel,
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
        return describe_entities(AmazonAdsConnectorModel)

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
            (e for e in AmazonAdsConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in AmazonAdsConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await AmazonAdsConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def get_consent_url(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        redirect_url: str,
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and workspace_name.
                Optionally include organization_id for multi-org request routing.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + workspace_name.
            replication_config: Optional replication settings dict. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await AmazonAdsConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Amazon-Ads Source",
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.workspace_name:
            raise ValueError("airbyte_config.workspace_name is required for get_consent_url()")

        from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(AmazonAdsConnectorModel.id),
                workspace_name=airbyte_config.workspace_name,
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
        auth_config: "AmazonAdsAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "AmazonAdsConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and workspace_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + workspace_name)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A AmazonAdsConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await AmazonAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AmazonAdsAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
            )

            # With server-side OAuth:
            connector = await AmazonAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.workspace_name:
            raise ValueError("airbyte_config.workspace_name is required for create()")

        # Validate: exactly one of auth_config or server_side_oauth_secret_id required
        if auth_config is None and server_side_oauth_secret_id is None:
            raise ValueError(
                "Either auth_config or server_side_oauth_secret_id must be provided"
            )
        if auth_config is not None and server_side_oauth_secret_id is not None:
            raise ValueError(
                "Cannot provide both auth_config and server_side_oauth_secret_id"
            )

        from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
        from airbyte_agent_sdk.types import AirbyteAuthConfig as _AirbyteAuthConfig

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
            source_name = name or f"{cls.connector_name} - {airbyte_config.workspace_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(AmazonAdsConnectorModel.id),
                workspace_name=airbyte_config.workspace_name,
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




class ProfilesQuery:
    """
    Query class for Profiles entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        profile_type_filter: str | None = None,
        **kwargs
    ) -> ProfilesListResult:
        """
        Returns a list of advertising profiles associated with the authenticated user.
Profiles represent an advertiser's account in a specific marketplace. Advertisers
may have a single profile if they advertise in only one marketplace, or a separate
profile for each marketplace if they advertise regionally or globally.


        Args:
            profile_type_filter: Filter profiles by type. Comma-separated list of profile types.
Valid values: seller, vendor, agency

            **kwargs: Additional parameters

        Returns:
            ProfilesListResult
        """
        params = {k: v for k, v in {
            "profileTypeFilter": profile_type_filter,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("profiles", "list", params)
        # Cast generic envelope to concrete typed result
        return ProfilesListResult(
            data=result.data
        )



    async def get(
        self,
        profile_id: str,
        **kwargs
    ) -> Profile:
        """
        Retrieves a single advertising profile by its ID. The profile contains
information about the advertiser's account in a specific marketplace.


        Args:
            profile_id: The unique identifier of the profile
            **kwargs: Additional parameters

        Returns:
            Profile
        """
        params = {k: v for k, v in {
            "profileId": profile_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("profiles", "get", params)
        return result



    async def context_store_search(
        self,
        query: ProfilesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProfilesSearchResult:
        """
        Search profiles records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProfilesSearchFilter):
        - account_info: 
        - country_code: 
        - currency_code: 
        - daily_budget: 
        - profile_id: 
        - timezone: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProfilesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("profiles", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProfilesSearchResult(
            data=[
                ProfilesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class PortfoliosQuery:
    """
    Query class for Portfolios entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        include_extended_data_fields: str | None = None,
        **kwargs
    ) -> PortfoliosListResult:
        """
        Returns a list of portfolios for the specified profile. Portfolios are used to
group campaigns together for organizational and budget management purposes.


        Args:
            include_extended_data_fields: Whether to include extended data fields in the response
            **kwargs: Additional parameters

        Returns:
            PortfoliosListResult
        """
        params = {k: v for k, v in {
            "includeExtendedDataFields": include_extended_data_fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("portfolios", "list", params)
        # Cast generic envelope to concrete typed result
        return PortfoliosListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        portfolio_id: str,
        **kwargs
    ) -> Portfolio:
        """
        Retrieves a single portfolio by its ID using the v2 API.


        Args:
            portfolio_id: The unique identifier of the portfolio
            **kwargs: Additional parameters

        Returns:
            Portfolio
        """
        params = {k: v for k, v in {
            "portfolioId": portfolio_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("portfolios", "get", params)
        return result



class SponsoredProductCampaignsQuery:
    """
    Query class for SponsoredProductCampaigns entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductCampaignsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductCampaignsListResult:
        """
        Returns a list of sponsored product campaigns for the specified profile.
Sponsored Products campaigns promote individual product listings on Amazon.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductCampaignsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductCampaignsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        campaign_id: str,
        **kwargs
    ) -> SponsoredProductCampaign:
        """
        Retrieves a single sponsored product campaign by its ID using the v2 API.


        Args:
            campaign_id: The unique identifier of the campaign
            **kwargs: Additional parameters

        Returns:
            SponsoredProductCampaign
        """
        params = {k: v for k, v in {
            "campaignId": campaign_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_campaigns", "get", params)
        return result



class SponsoredProductAdGroupsQuery:
    """
    Query class for SponsoredProductAdGroups entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductAdGroupsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductAdGroupsListResult:
        """
        Returns a list of sponsored product ad groups for the specified profile.
Ad groups are used to organize ads and targeting within a campaign.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductAdGroupsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_ad_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductAdGroupsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredProductKeywordsQuery:
    """
    Query class for SponsoredProductKeywords entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductKeywordsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductKeywordsListResult:
        """
        Returns a list of sponsored product keywords for the specified profile.
Keywords are used in manual targeting campaigns to match shopper search queries.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductKeywordsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_keywords", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductKeywordsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredProductProductAdsQuery:
    """
    Query class for SponsoredProductProductAds entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductProductAdsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductProductAdsListResult:
        """
        Returns a list of sponsored product ads for the specified profile.
Product ads associate an advertised product with an ad group.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductProductAdsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_product_ads", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductProductAdsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredProductTargetsQuery:
    """
    Query class for SponsoredProductTargets entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductTargetsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductTargetsListResult:
        """
        Returns a list of sponsored product targeting clauses for the specified profile.
Targeting clauses define product or category targeting for ad groups.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductTargetsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_targets", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductTargetsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredProductNegativeKeywordsQuery:
    """
    Query class for SponsoredProductNegativeKeywords entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductNegativeKeywordsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductNegativeKeywordsListResult:
        """
        Returns a list of sponsored product negative keywords for the specified profile.
Negative keywords prevent ads from showing for specific search terms.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductNegativeKeywordsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_negative_keywords", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductNegativeKeywordsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredProductNegativeTargetsQuery:
    """
    Query class for SponsoredProductNegativeTargets entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredProductNegativeTargetsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredProductNegativeTargetsListResult:
        """
        Returns a list of sponsored product negative targeting clauses for the specified profile.
Negative targeting clauses exclude specific products or categories from targeting.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredProductNegativeTargetsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_product_negative_targets", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredProductNegativeTargetsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredBrandsCampaignsQuery:
    """
    Query class for SponsoredBrandsCampaigns entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredBrandsCampaignsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredBrandsCampaignsListResult:
        """
        Returns a list of sponsored brands campaigns for the specified profile.
Sponsored Brands campaigns help drive discovery and sales with creative ad experiences.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredBrandsCampaignsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_brands_campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredBrandsCampaignsListResult(
            data=result.data,
            meta=result.meta
        )



class SponsoredBrandsAdGroupsQuery:
    """
    Query class for SponsoredBrandsAdGroups entity operations.
    """

    def __init__(self, connector: AmazonAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        state_filter: SponsoredBrandsAdGroupsListParamsStatefilter | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> SponsoredBrandsAdGroupsListResult:
        """
        Returns a list of sponsored brands ad groups for the specified profile.
Ad groups organize ads and targeting within a Sponsored Brands campaign.


        Args:
            state_filter: Parameter stateFilter
            max_results: Maximum number of results to return
            next_token: Token for pagination
            **kwargs: Additional parameters

        Returns:
            SponsoredBrandsAdGroupsListResult
        """
        params = {k: v for k, v in {
            "stateFilter": state_filter,
            "maxResults": max_results,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sponsored_brands_ad_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return SponsoredBrandsAdGroupsListResult(
            data=result.data,
            meta=result.meta
        )


