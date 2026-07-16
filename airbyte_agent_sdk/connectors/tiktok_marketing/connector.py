"""
Tiktok-Marketing connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import TiktokMarketingConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AdGroupsListParams,
    AdGroupsReportsDailyListParams,
    AdsListParams,
    AdsReportsDailyListParams,
    AdsReportsHourlyListParams,
    AdsReportsLifetimeListParams,
    AdvertisersListParams,
    AdvertisersReportsDailyListParams,
    AudiencesListParams,
    CampaignsListParams,
    CampaignsReportsDailyListParams,
    CatalogsListParams,
    CreativeAssetsImagesListParams,
    CreativeAssetsVideosListParams,
    SparkAdsListParams,
    AirbyteSearchParams,
    AdvertisersSearchFilter,
    AdvertisersSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    AdGroupsSearchFilter,
    AdGroupsSearchQuery,
    AdsSearchFilter,
    AdsSearchQuery,
    AudiencesSearchFilter,
    AudiencesSearchQuery,
    CreativeAssetsImagesSearchFilter,
    CreativeAssetsImagesSearchQuery,
    CreativeAssetsVideosSearchFilter,
    CreativeAssetsVideosSearchQuery,
    SparkAdsSearchFilter,
    SparkAdsSearchQuery,
    AdvertisersReportsDailySearchFilter,
    AdvertisersReportsDailySearchQuery,
    CampaignsReportsDailySearchFilter,
    CampaignsReportsDailySearchQuery,
    AdGroupsReportsDailySearchFilter,
    AdGroupsReportsDailySearchQuery,
    AdsReportsDailySearchFilter,
    AdsReportsDailySearchQuery,
    AdsReportsHourlySearchFilter,
    AdsReportsHourlySearchQuery,
    AdsReportsLifetimeSearchFilter,
    AdsReportsLifetimeSearchQuery,
)
from .models import TiktokMarketingAuthConfig
if TYPE_CHECKING:
    from .models import TiktokMarketingReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    TiktokMarketingCheckResult,
    TiktokMarketingExecuteResult,
    TiktokMarketingExecuteResultWithMeta,
    AdvertisersListResult,
    CampaignsListResult,
    AdGroupsListResult,
    AdsListResult,
    AudiencesListResult,
    CreativeAssetsImagesListResult,
    CreativeAssetsVideosListResult,
    SparkAdsListResult,
    CatalogsListResult,
    AdvertisersReportsDailyListResult,
    CampaignsReportsDailyListResult,
    AdGroupsReportsDailyListResult,
    AdsReportsDailyListResult,
    AdsReportsHourlyListResult,
    AdsReportsLifetimeListResult,
    Ad,
    AdGroup,
    AdGroupsReportDaily,
    AdsReportDaily,
    AdsReportHourly,
    AdsReportLifetime,
    Advertiser,
    AdvertisersReportDaily,
    Audience,
    Campaign,
    CampaignsReportDaily,
    Catalog,
    CreativeAssetImage,
    CreativeAssetVideo,
    SparkAd,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AdvertisersSearchData,
    AdvertisersSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdGroupsSearchData,
    AdGroupsSearchResult,
    AdsSearchData,
    AdsSearchResult,
    AudiencesSearchData,
    AudiencesSearchResult,
    CreativeAssetsImagesSearchData,
    CreativeAssetsImagesSearchResult,
    CreativeAssetsVideosSearchData,
    CreativeAssetsVideosSearchResult,
    SparkAdsSearchData,
    SparkAdsSearchResult,
    AdvertisersReportsDailySearchData,
    AdvertisersReportsDailySearchResult,
    CampaignsReportsDailySearchData,
    CampaignsReportsDailySearchResult,
    AdGroupsReportsDailySearchData,
    AdGroupsReportsDailySearchResult,
    AdsReportsDailySearchData,
    AdsReportsDailySearchResult,
    AdsReportsHourlySearchData,
    AdsReportsHourlySearchResult,
    AdsReportsLifetimeSearchData,
    AdsReportsLifetimeSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class TiktokMarketingConnector:
    """
    Type-safe Tiktok-Marketing API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "tiktok-marketing"
    connector_version = "1.1.6"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("advertisers", "list"): True,
        ("campaigns", "list"): True,
        ("ad_groups", "list"): True,
        ("ads", "list"): True,
        ("audiences", "list"): True,
        ("creative_assets_images", "list"): True,
        ("creative_assets_videos", "list"): True,
        ("spark_ads", "list"): True,
        ("catalogs", "list"): True,
        ("advertisers_reports_daily", "list"): True,
        ("campaigns_reports_daily", "list"): True,
        ("ad_groups_reports_daily", "list"): True,
        ("ads_reports_daily", "list"): True,
        ("ads_reports_hourly", "list"): True,
        ("ads_reports_lifetime", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('advertisers', 'list'): {'advertiser_ids': 'advertiser_ids', 'page': 'page', 'page_size': 'page_size'},
        ('campaigns', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('ad_groups', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('ads', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('audiences', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('creative_assets_images', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('creative_assets_videos', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('spark_ads', 'list'): {'advertiser_id': 'advertiser_id', 'page': 'page', 'page_size': 'page_size'},
        ('catalogs', 'list'): {'advertiser_id': 'advertiser_id', 'bc_id': 'bc_id', 'page': 'page', 'page_size': 'page_size'},
        ('advertisers_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('campaigns_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('ad_groups_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('ads_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('ads_reports_hourly', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('ads_reports_lifetime', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (TiktokMarketingAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: TiktokMarketingAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new tiktok-marketing connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., TiktokMarketingAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = TiktokMarketingConnector(auth_config=TiktokMarketingAuthConfig(access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = TiktokMarketingConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = TiktokMarketingConnector(
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
                connector_definition_id=str(TiktokMarketingConnectorModel.id),
                model=TiktokMarketingConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or TiktokMarketingAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=TiktokMarketingConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.advertisers = AdvertisersQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.ad_groups = AdGroupsQuery(self)
        self.ads = AdsQuery(self)
        self.audiences = AudiencesQuery(self)
        self.creative_assets_images = CreativeAssetsImagesQuery(self)
        self.creative_assets_videos = CreativeAssetsVideosQuery(self)
        self.spark_ads = SparkAdsQuery(self)
        self.catalogs = CatalogsQuery(self)
        self.advertisers_reports_daily = AdvertisersReportsDailyQuery(self)
        self.campaigns_reports_daily = CampaignsReportsDailyQuery(self)
        self.ad_groups_reports_daily = AdGroupsReportsDailyQuery(self)
        self.ads_reports_daily = AdsReportsDailyQuery(self)
        self.ads_reports_hourly = AdsReportsHourlyQuery(self)
        self.ads_reports_lifetime = AdsReportsLifetimeQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["advertisers"],
        action: Literal["list"],
        params: "AdvertisersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdvertisersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups"],
        action: Literal["list"],
        params: "AdGroupsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads"],
        action: Literal["list"],
        params: "AdsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["audiences"],
        action: Literal["list"],
        params: "AudiencesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AudiencesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creative_assets_images"],
        action: Literal["list"],
        params: "CreativeAssetsImagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CreativeAssetsImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creative_assets_videos"],
        action: Literal["list"],
        params: "CreativeAssetsVideosListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CreativeAssetsVideosListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["spark_ads"],
        action: Literal["list"],
        params: "SparkAdsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SparkAdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalogs"],
        action: Literal["list"],
        params: "CatalogsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CatalogsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["advertisers_reports_daily"],
        action: Literal["list"],
        params: "AdvertisersReportsDailyListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdvertisersReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns_reports_daily"],
        action: Literal["list"],
        params: "CampaignsReportsDailyListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups_reports_daily"],
        action: Literal["list"],
        params: "AdGroupsReportsDailyListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdGroupsReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads_reports_daily"],
        action: Literal["list"],
        params: "AdsReportsDailyListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdsReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads_reports_hourly"],
        action: Literal["list"],
        params: "AdsReportsHourlyListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdsReportsHourlyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads_reports_lifetime"],
        action: Literal["list"],
        params: "AdsReportsLifetimeListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdsReportsLifetimeListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> TiktokMarketingExecuteResult[Any] | TiktokMarketingExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "context_store_search"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
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
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

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
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return TiktokMarketingExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return TiktokMarketingExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> TiktokMarketingCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            TiktokMarketingCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return TiktokMarketingCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return TiktokMarketingCheckResult(
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
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = TiktokMarketingConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @TiktokMarketingConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @TiktokMarketingConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @TiktokMarketingConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    TiktokMarketingConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

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
        return describe_entities(TiktokMarketingConnectorModel)

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
            (e for e in TiktokMarketingConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in TiktokMarketingConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
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



class AdvertisersQuery:
    """
    Query class for Advertisers entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_ids: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdvertisersListResult:
        """
        Get advertiser account information

        Args:
            advertiser_ids: Advertiser IDs (JSON array of strings)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdvertisersListResult
        """
        params = {k: v for k, v in {
            "advertiser_ids": advertiser_ids,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("advertisers", "list", params)
        # Cast generic envelope to concrete typed result
        return AdvertisersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdvertisersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdvertisersSearchResult:
        """
        Search advertisers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdvertisersSearchFilter):
        - address: The physical address of the advertiser.
        - advertiser_account_type: The type of advertiser's account (e.g., individual, business).
        - advertiser_id: Unique identifier for the advertiser.
        - balance: The current balance in the advertiser's account.
        - brand: The brand name associated with the advertiser.
        - cellphone_number: The cellphone number of the advertiser.
        - company: The name of the company associated with the advertiser.
        - contacter: The contact person for the advertiser.
        - country: The country where the advertiser is located.
        - create_time: The timestamp when the advertiser account was created.
        - currency: The currency used for transactions in the account.
        - description: A brief description or bio of the advertiser or company.
        - display_timezone: The timezone for display purposes.
        - email: The email address associated with the advertiser.
        - industry: The industry or sector the advertiser operates in.
        - language: The preferred language of communication for the advertiser.
        - license_city: The city where the advertiser's license is registered.
        - license_no: The license number of the advertiser.
        - license_province: The province or state where the advertiser's license is registered.
        - license_url: The URL link to the advertiser's license documentation.
        - name: The name of the advertiser or company.
        - promotion_area: The specific area or region where the advertiser focuses promotion.
        - promotion_center_city: The city at the center of the advertiser's promotion activities.
        - promotion_center_province: The province or state at the center of the advertiser's promotion activities.
        - rejection_reason: Reason for any advertisement rejection by the platform.
        - role: The role or position of the advertiser within the company.
        - status: The current status of the advertiser's account.
        - telephone_number: The telephone number of the advertiser.
        - timezone: The timezone setting for the advertiser's activities.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdvertisersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("advertisers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdvertisersSearchResult(
            data=[
                AdvertisersSearchData(**row)
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

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Get campaigns for an advertiser

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
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
        - advertiser_id: The unique identifier of the advertiser associated with the campaign
        - app_promotion_type: Type of app promotion being used in the campaign
        - bid_type: Type of bid strategy being used in the campaign
        - budget: Total budget allocated for the campaign
        - budget_mode: Mode in which the budget is being managed (e.g., daily, lifetime)
        - budget_optimize_on: The metric or event that the budget optimization is based on
        - campaign_id: The unique identifier of the campaign
        - campaign_name: Name of the campaign for easy identification
        - campaign_type: Type of campaign (e.g., awareness, conversion)
        - create_time: Timestamp when the campaign was created
        - deep_bid_type: Advanced bid type used for campaign optimization
        - is_new_structure: Flag indicating if the campaign utilizes a new campaign structure
        - is_search_campaign: Flag indicating if the campaign is a search campaign
        - is_smart_performance_campaign: Flag indicating if the campaign uses smart performance optimization
        - modify_time: Timestamp when the campaign was last modified
        - objective: The objective or goal of the campaign
        - objective_type: Type of objective selected for the campaign
        - operation_status: Current operational status of the campaign
        - optimization_goal: Specific goal to be optimized for in the campaign
        - rf_campaign_type: Type of RF (reach and frequency) campaign being run
        - roas_bid: Return on ad spend goal set for the campaign
        - secondary_status: Additional status information of the campaign
        - split_test_variable: Variable being tested in a split test campaign

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

        result = await self._connector.execute("campaigns", "context_store_search", params)

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

class AdGroupsQuery:
    """
    Query class for AdGroups entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdGroupsListResult:
        """
        Get ad groups for an advertiser

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdGroupsListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdGroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdGroupsSearchResult:
        """
        Search ad_groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdGroupsSearchFilter):
        - adgroup_id: The unique identifier of the ad group
        - adgroup_name: The name of the ad group
        - advertiser_id: The unique identifier of the advertiser
        - budget: The allocated budget for the ad group
        - budget_mode: The mode for managing the budget
        - campaign_id: The unique identifier of the campaign
        - create_time: The timestamp for when the ad group was created
        - modify_time: The timestamp for when the ad group was last modified
        - operation_status: The status of the operation
        - optimization_goal: The goal set for optimization
        - placement_type: The type of ad placement
        - promotion_type: The type of promotion
        - secondary_status: The secondary status of the ad group

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdGroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_groups", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdGroupsSearchResult(
            data=[
                AdGroupsSearchData(**row)
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

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdsListResult:
        """
        Get ads for an advertiser

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdsListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
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
        - ad_format: The format of the ad
        - ad_id: The unique identifier of the ad
        - ad_name: The name of the ad
        - ad_text: The text content of the ad
        - adgroup_id: The unique identifier of the ad group
        - adgroup_name: The name of the ad group
        - advertiser_id: The unique identifier of the advertiser
        - campaign_id: The unique identifier of the campaign
        - campaign_name: The name of the campaign
        - create_time: The timestamp when the ad was created
        - landing_page_url: The URL of the landing page for the ad
        - modify_time: The timestamp when the ad was last modified
        - operation_status: The operational status of the ad
        - secondary_status: The secondary status of the ad
        - video_id: The unique identifier of the video

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

        result = await self._connector.execute("ads", "context_store_search", params)

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

class AudiencesQuery:
    """
    Query class for Audiences entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AudiencesListResult:
        """
        Get custom audiences for an advertiser

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AudiencesListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("audiences", "list", params)
        # Cast generic envelope to concrete typed result
        return AudiencesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AudiencesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AudiencesSearchResult:
        """
        Search audiences records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AudiencesSearchFilter):
        - audience_id: Unique identifier for the audience
        - audience_type: Type of audience
        - cover_num: Number of audience members covered
        - create_time: Timestamp indicating when the audience was created
        - is_valid: Flag indicating if the audience data is valid
        - name: Name of the audience
        - shared: Flag indicating if the audience is shared

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AudiencesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("audiences", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AudiencesSearchResult(
            data=[
                AudiencesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CreativeAssetsImagesQuery:
    """
    Query class for CreativeAssetsImages entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CreativeAssetsImagesListResult:
        """
        Search creative asset images for an advertiser

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            CreativeAssetsImagesListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creative_assets_images", "list", params)
        # Cast generic envelope to concrete typed result
        return CreativeAssetsImagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: CreativeAssetsImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CreativeAssetsImagesSearchResult:
        """
        Search creative_assets_images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CreativeAssetsImagesSearchFilter):
        - create_time: The timestamp when the image was created.
        - file_name: The name of the image file.
        - format: The format type of the image file.
        - height: The height dimension of the image.
        - image_id: The unique identifier for the image.
        - image_url: The URL to access the image.
        - modify_time: The timestamp when the image was last modified.
        - size: The size of the image file.
        - width: The width dimension of the image.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CreativeAssetsImagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("creative_assets_images", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CreativeAssetsImagesSearchResult(
            data=[
                CreativeAssetsImagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CreativeAssetsVideosQuery:
    """
    Query class for CreativeAssetsVideos entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CreativeAssetsVideosListResult:
        """
        Search creative asset videos for an advertiser

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            CreativeAssetsVideosListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creative_assets_videos", "list", params)
        # Cast generic envelope to concrete typed result
        return CreativeAssetsVideosListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: CreativeAssetsVideosSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CreativeAssetsVideosSearchResult:
        """
        Search creative_assets_videos records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CreativeAssetsVideosSearchFilter):
        - create_time: Timestamp when the video was created.
        - duration: Duration of the video in seconds.
        - file_name: Name of the video file.
        - format: Format of the video file.
        - height: Height of the video in pixels.
        - modify_time: Timestamp when the video was last modified.
        - size: Size of the video file in bytes.
        - video_cover_url: URL for the cover image of the video.
        - video_id: ID of the video.
        - width: Width of the video in pixels.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CreativeAssetsVideosSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("creative_assets_videos", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CreativeAssetsVideosSearchResult(
            data=[
                CreativeAssetsVideosSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SparkAdsQuery:
    """
    Query class for SparkAds entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> SparkAdsListResult:
        """
        Get Spark Ad posts that have been authorized to an ad account

        Args:
            advertiser_id: Advertiser ID
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            SparkAdsListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("spark_ads", "list", params)
        # Cast generic envelope to concrete typed result
        return SparkAdsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: SparkAdsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SparkAdsSearchResult:
        """
        Search spark_ads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SparkAdsSearchFilter):
        - item_info: Information about the Spark Ads post including item_id, auth_code, text, status, and item_type.
        - user_info: Information about the TikTok account including tiktok_name, identity_id, and identity_type.
        - auth_info: Authorization details including invite_start_time, auth_start_time, auth_end_time, and ad_auth_status.
        - video_info: Video post details including duration, preview_url, poster_url, height, width, and size.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SparkAdsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("spark_ads", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SparkAdsSearchResult(
            data=[
                SparkAdsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CatalogsQuery:
    """
    Query class for Catalogs entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        bc_id: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CatalogsListResult:
        """
        Get product catalogs for an advertiser

        Args:
            advertiser_id: Advertiser ID
            bc_id: Business Center ID. Required by the TikTok API to scope catalog results.
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            CatalogsListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "bc_id": bc_id,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalogs", "list", params)
        # Cast generic envelope to concrete typed result
        return CatalogsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class AdvertisersReportsDailyQuery:
    """
    Query class for AdvertisersReportsDaily entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: str,
        metrics: str,
        start_date: str,
        end_date: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdvertisersReportsDailyListResult:
        """
        Get daily performance reports at the advertiser level

        Args:
            advertiser_id: Advertiser ID
            service_type: Service type
            report_type: Report type
            data_level: Data level for the report
            dimensions: Dimensions for the report (JSON array)
            metrics: Metrics to retrieve (JSON array)
            start_date: Report start date (YYYY-MM-DD)
            end_date: Report end date (YYYY-MM-DD)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdvertisersReportsDailyListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "service_type": service_type,
            "report_type": report_type,
            "data_level": data_level,
            "dimensions": dimensions,
            "metrics": metrics,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("advertisers_reports_daily", "list", params)
        # Cast generic envelope to concrete typed result
        return AdvertisersReportsDailyListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdvertisersReportsDailySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdvertisersReportsDailySearchResult:
        """
        Search advertisers_reports_daily records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdvertisersReportsDailySearchFilter):
        - advertiser_id: The unique identifier for the advertiser.
        - stat_time_day: The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format).
        - spend: Total amount of money spent.
        - cash_spend: The amount of money spent in cash.
        - voucher_spend: Amount spent using vouchers.
        - cpc: Cost per click.
        - cpm: Cost per thousand impressions.
        - impressions: Number of times the ad was displayed.
        - clicks: Number of clicks on the ad.
        - ctr: Click-through rate.
        - reach: Total number of unique users reached.
        - cost_per_1000_reached: Cost per 1000 unique users reached.
        - frequency: Average number of times each person saw the ad.
        - video_play_actions: Number of video play actions.
        - video_watched_2s: Number of times video was watched for at least 2 seconds.
        - video_watched_6s: Number of times video was watched for at least 6 seconds.
        - average_video_play: Average video play duration.
        - average_video_play_per_user: Average video play duration per user.
        - video_views_p25: Number of times video was watched to 25%.
        - video_views_p50: Number of times video was watched to 50%.
        - video_views_p75: Number of times video was watched to 75%.
        - video_views_p100: Number of times video was watched to 100%.
        - profile_visits: Number of profile visits.
        - likes: Number of likes.
        - comments: Number of comments.
        - shares: Number of shares.
        - follows: Number of follows.
        - clicks_on_music_disc: Number of clicks on the music disc.
        - real_time_app_install: Real-time app installations.
        - real_time_app_install_cost: Cost of real-time app installations.
        - app_install: Number of app installations.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdvertisersReportsDailySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("advertisers_reports_daily", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdvertisersReportsDailySearchResult(
            data=[
                AdvertisersReportsDailySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CampaignsReportsDailyQuery:
    """
    Query class for CampaignsReportsDaily entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: str,
        metrics: str,
        start_date: str,
        end_date: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CampaignsReportsDailyListResult:
        """
        Get daily performance reports at the campaign level

        Args:
            advertiser_id: Advertiser ID
            service_type: Service type
            report_type: Report type
            data_level: Data level for the report
            dimensions: Dimensions for the report (JSON array)
            metrics: Metrics to retrieve (JSON array)
            start_date: Report start date (YYYY-MM-DD)
            end_date: Report end date (YYYY-MM-DD)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            CampaignsReportsDailyListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "service_type": service_type,
            "report_type": report_type,
            "data_level": data_level,
            "dimensions": dimensions,
            "metrics": metrics,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns_reports_daily", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsReportsDailyListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: CampaignsReportsDailySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsReportsDailySearchResult:
        """
        Search campaigns_reports_daily records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsReportsDailySearchFilter):
        - campaign_id: The unique identifier for the campaign.
        - stat_time_day: The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format).
        - campaign_name: The name of the marketing campaign.
        - spend: Total amount of money spent.
        - cpc: Cost per click.
        - cpm: Cost per thousand impressions.
        - impressions: Number of times the ad was displayed.
        - clicks: Number of clicks on the ad.
        - ctr: Click-through rate.
        - reach: Total number of unique users reached.
        - cost_per_1000_reached: Cost per 1000 unique users reached.
        - frequency: Average number of times each person saw the ad.
        - video_play_actions: Number of video play actions.
        - video_watched_2s: Number of times video was watched for at least 2 seconds.
        - video_watched_6s: Number of times video was watched for at least 6 seconds.
        - average_video_play: Average video play duration.
        - average_video_play_per_user: Average video play duration per user.
        - video_views_p25: Number of times video was watched to 25%.
        - video_views_p50: Number of times video was watched to 50%.
        - video_views_p75: Number of times video was watched to 75%.
        - video_views_p100: Number of times video was watched to 100%.
        - profile_visits: Number of profile visits.
        - likes: Number of likes.
        - comments: Number of comments.
        - shares: Number of shares.
        - follows: Number of follows.
        - clicks_on_music_disc: Number of clicks on the music disc.
        - real_time_app_install: Real-time app installations.
        - real_time_app_install_cost: Cost of real-time app installations.
        - app_install: Number of app installations.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsReportsDailySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaigns_reports_daily", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignsReportsDailySearchResult(
            data=[
                CampaignsReportsDailySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdGroupsReportsDailyQuery:
    """
    Query class for AdGroupsReportsDaily entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: str,
        metrics: str,
        start_date: str,
        end_date: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdGroupsReportsDailyListResult:
        """
        Get daily performance reports at the ad group level

        Args:
            advertiser_id: Advertiser ID
            service_type: Service type
            report_type: Report type
            data_level: Data level for the report
            dimensions: Dimensions for the report (JSON array)
            metrics: Metrics to retrieve (JSON array)
            start_date: Report start date (YYYY-MM-DD)
            end_date: Report end date (YYYY-MM-DD)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdGroupsReportsDailyListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "service_type": service_type,
            "report_type": report_type,
            "data_level": data_level,
            "dimensions": dimensions,
            "metrics": metrics,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups_reports_daily", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupsReportsDailyListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdGroupsReportsDailySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdGroupsReportsDailySearchResult:
        """
        Search ad_groups_reports_daily records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdGroupsReportsDailySearchFilter):
        - adgroup_id: The unique identifier for the ad group.
        - stat_time_day: The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format).
        - campaign_name: The name of the marketing campaign.
        - campaign_id: The unique identifier for the campaign.
        - adgroup_name: The name of the ad group.
        - placement_type: Type of ad placement.
        - spend: Total amount of money spent.
        - cpc: Cost per click.
        - cpm: Cost per thousand impressions.
        - impressions: Number of times the ad was displayed.
        - clicks: Number of clicks on the ad.
        - ctr: Click-through rate.
        - reach: Total number of unique users reached.
        - cost_per_1000_reached: Cost per 1000 unique users reached.
        - conversion: Number of conversions.
        - cost_per_conversion: Cost per conversion.
        - conversion_rate: Rate of conversions.
        - real_time_conversion: Real-time conversions.
        - real_time_cost_per_conversion: Real-time cost per conversion.
        - real_time_conversion_rate: Real-time conversion rate.
        - result: Number of results.
        - cost_per_result: Cost per result.
        - result_rate: Rate of results.
        - real_time_result: Real-time results.
        - real_time_cost_per_result: Real-time cost per result.
        - real_time_result_rate: Real-time result rate.
        - secondary_goal_result: Results for secondary goals.
        - cost_per_secondary_goal_result: Cost per secondary goal result.
        - secondary_goal_result_rate: Rate of secondary goal results.
        - frequency: Average number of times each person saw the ad.
        - video_play_actions: Number of video play actions.
        - video_watched_2s: Number of times video was watched for at least 2 seconds.
        - video_watched_6s: Number of times video was watched for at least 6 seconds.
        - average_video_play: Average video play duration.
        - average_video_play_per_user: Average video play duration per user.
        - video_views_p25: Number of times video was watched to 25%.
        - video_views_p50: Number of times video was watched to 50%.
        - video_views_p75: Number of times video was watched to 75%.
        - video_views_p100: Number of times video was watched to 100%.
        - profile_visits: Number of profile visits.
        - likes: Number of likes.
        - comments: Number of comments.
        - shares: Number of shares.
        - follows: Number of follows.
        - clicks_on_music_disc: Number of clicks on the music disc.
        - real_time_app_install: Real-time app installations.
        - real_time_app_install_cost: Cost of real-time app installations.
        - app_install: Number of app installations.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdGroupsReportsDailySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_groups_reports_daily", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdGroupsReportsDailySearchResult(
            data=[
                AdGroupsReportsDailySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdsReportsDailyQuery:
    """
    Query class for AdsReportsDaily entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: str,
        metrics: str,
        start_date: str,
        end_date: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdsReportsDailyListResult:
        """
        Get daily performance reports at the ad level

        Args:
            advertiser_id: Advertiser ID
            service_type: Service type
            report_type: Report type
            data_level: Data level for the report
            dimensions: Dimensions for the report (JSON array)
            metrics: Metrics to retrieve (JSON array)
            start_date: Report start date (YYYY-MM-DD)
            end_date: Report end date (YYYY-MM-DD)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdsReportsDailyListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "service_type": service_type,
            "report_type": report_type,
            "data_level": data_level,
            "dimensions": dimensions,
            "metrics": metrics,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads_reports_daily", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsReportsDailyListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdsReportsDailySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsReportsDailySearchResult:
        """
        Search ads_reports_daily records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsReportsDailySearchFilter):
        - ad_id: The unique identifier for the ad.
        - stat_time_day: The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format).
        - campaign_name: The name of the marketing campaign.
        - campaign_id: The unique identifier for the campaign.
        - adgroup_name: The name of the ad group.
        - adgroup_id: The unique identifier for the ad group.
        - ad_name: The name of the ad.
        - ad_text: The text content of the ad.
        - placement_type: Type of ad placement.
        - spend: Total amount of money spent.
        - cpc: Cost per click.
        - cpm: Cost per thousand impressions.
        - impressions: Number of times the ad was displayed.
        - clicks: Number of clicks on the ad.
        - ctr: Click-through rate.
        - reach: Total number of unique users reached.
        - cost_per_1000_reached: Cost per 1000 unique users reached.
        - conversion: Number of conversions.
        - cost_per_conversion: Cost per conversion.
        - conversion_rate: Rate of conversions.
        - real_time_conversion: Real-time conversions.
        - real_time_cost_per_conversion: Real-time cost per conversion.
        - real_time_conversion_rate: Real-time conversion rate.
        - result: Number of results.
        - cost_per_result: Cost per result.
        - result_rate: Rate of results.
        - real_time_result: Real-time results.
        - real_time_cost_per_result: Real-time cost per result.
        - real_time_result_rate: Real-time result rate.
        - secondary_goal_result: Results for secondary goals.
        - cost_per_secondary_goal_result: Cost per secondary goal result.
        - secondary_goal_result_rate: Rate of secondary goal results.
        - frequency: Average number of times each person saw the ad.
        - video_play_actions: Number of video play actions.
        - video_watched_2s: Number of times video was watched for at least 2 seconds.
        - video_watched_6s: Number of times video was watched for at least 6 seconds.
        - average_video_play: Average video play duration.
        - average_video_play_per_user: Average video play duration per user.
        - video_views_p25: Number of times video was watched to 25%.
        - video_views_p50: Number of times video was watched to 50%.
        - video_views_p75: Number of times video was watched to 75%.
        - video_views_p100: Number of times video was watched to 100%.
        - profile_visits: Number of profile visits.
        - likes: Number of likes.
        - comments: Number of comments.
        - shares: Number of shares.
        - follows: Number of follows.
        - clicks_on_music_disc: Number of clicks on the music disc.
        - real_time_app_install: Real-time app installations.
        - real_time_app_install_cost: Cost of real-time app installations.
        - app_install: Number of app installations.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsReportsDailySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ads_reports_daily", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsReportsDailySearchResult(
            data=[
                AdsReportsDailySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdsReportsHourlyQuery:
    """
    Query class for AdsReportsHourly entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: str,
        metrics: str,
        start_date: str,
        end_date: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdsReportsHourlyListResult:
        """
        Get hourly performance reports at the ad level

        Args:
            advertiser_id: Advertiser ID
            service_type: Service type
            report_type: Report type
            data_level: Data level for the report
            dimensions: Dimensions for the report (JSON array)
            metrics: Metrics to retrieve (JSON array)
            start_date: Report start date (YYYY-MM-DD)
            end_date: Report end date (YYYY-MM-DD)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdsReportsHourlyListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "service_type": service_type,
            "report_type": report_type,
            "data_level": data_level,
            "dimensions": dimensions,
            "metrics": metrics,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads_reports_hourly", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsReportsHourlyListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdsReportsHourlySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsReportsHourlySearchResult:
        """
        Search ads_reports_hourly records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsReportsHourlySearchFilter):
        - ad_id: The unique identifier for the ad.
        - stat_time_hour: The hour for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format).
        - campaign_name: The name of the marketing campaign.
        - campaign_id: The unique identifier for the campaign.
        - adgroup_name: The name of the ad group.
        - adgroup_id: The unique identifier for the ad group.
        - ad_name: The name of the ad.
        - ad_text: The text content of the ad.
        - placement_type: Type of ad placement.
        - spend: Total amount of money spent.
        - cpc: Cost per click.
        - cpm: Cost per thousand impressions.
        - impressions: Number of times the ad was displayed.
        - clicks: Number of clicks on the ad.
        - ctr: Click-through rate.
        - reach: Total number of unique users reached.
        - cost_per_1000_reached: Cost per 1000 unique users reached.
        - conversion: Number of conversions.
        - cost_per_conversion: Cost per conversion.
        - conversion_rate: Rate of conversions.
        - real_time_conversion: Real-time conversions.
        - real_time_cost_per_conversion: Real-time cost per conversion.
        - real_time_conversion_rate: Real-time conversion rate.
        - result: Number of results.
        - cost_per_result: Cost per result.
        - result_rate: Rate of results.
        - real_time_result: Real-time results.
        - real_time_cost_per_result: Real-time cost per result.
        - real_time_result_rate: Real-time result rate.
        - secondary_goal_result: Results for secondary goals.
        - cost_per_secondary_goal_result: Cost per secondary goal result.
        - secondary_goal_result_rate: Rate of secondary goal results.
        - frequency: Average number of times each person saw the ad.
        - video_play_actions: Number of video play actions.
        - video_watched_2s: Number of times video was watched for at least 2 seconds.
        - video_watched_6s: Number of times video was watched for at least 6 seconds.
        - average_video_play: Average video play duration.
        - average_video_play_per_user: Average video play duration per user.
        - video_views_p25: Number of times video was watched to 25%.
        - video_views_p50: Number of times video was watched to 50%.
        - video_views_p75: Number of times video was watched to 75%.
        - video_views_p100: Number of times video was watched to 100%.
        - profile_visits: Number of profile visits.
        - likes: Number of likes.
        - comments: Number of comments.
        - shares: Number of shares.
        - follows: Number of follows.
        - clicks_on_music_disc: Number of clicks on the music disc.
        - real_time_app_install: Real-time app installations.
        - real_time_app_install_cost: Cost of real-time app installations.
        - app_install: Number of app installations.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsReportsHourlySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ads_reports_hourly", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsReportsHourlySearchResult(
            data=[
                AdsReportsHourlySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdsReportsLifetimeQuery:
    """
    Query class for AdsReportsLifetime entity operations.
    """

    def __init__(self, connector: TiktokMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: str,
        metrics: str,
        start_date: str,
        end_date: str,
        page: int | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdsReportsLifetimeListResult:
        """
        Get lifetime performance reports at the ad level

        Args:
            advertiser_id: Advertiser ID
            service_type: Service type
            report_type: Report type
            data_level: Data level for the report
            dimensions: Dimensions for the report (JSON array)
            metrics: Metrics to retrieve (JSON array)
            start_date: Report start date (YYYY-MM-DD)
            end_date: Report end date (YYYY-MM-DD)
            page: Page number
            page_size: Number of items per page
            **kwargs: Additional parameters

        Returns:
            AdsReportsLifetimeListResult
        """
        params = {k: v for k, v in {
            "advertiser_id": advertiser_id,
            "service_type": service_type,
            "report_type": report_type,
            "data_level": data_level,
            "dimensions": dimensions,
            "metrics": metrics,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads_reports_lifetime", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsReportsLifetimeListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AdsReportsLifetimeSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsReportsLifetimeSearchResult:
        """
        Search ads_reports_lifetime records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsReportsLifetimeSearchFilter):
        - ad_id: The unique identifier for the ad.
        - campaign_name: The name of the marketing campaign.
        - campaign_id: The unique identifier for the campaign.
        - adgroup_name: The name of the ad group.
        - adgroup_id: The unique identifier for the ad group.
        - ad_name: The name of the ad.
        - ad_text: The text content of the ad.
        - placement_type: Type of ad placement.
        - spend: Total amount of money spent.
        - cpc: Cost per click.
        - cpm: Cost per thousand impressions.
        - impressions: Number of times the ad was displayed.
        - clicks: Number of clicks on the ad.
        - ctr: Click-through rate.
        - reach: Total number of unique users reached.
        - cost_per_1000_reached: Cost per 1000 unique users reached.
        - conversion: Number of conversions.
        - cost_per_conversion: Cost per conversion.
        - conversion_rate: Rate of conversions.
        - real_time_conversion: Real-time conversions.
        - real_time_cost_per_conversion: Real-time cost per conversion.
        - real_time_conversion_rate: Real-time conversion rate.
        - result: Number of results.
        - cost_per_result: Cost per result.
        - result_rate: Rate of results.
        - real_time_result: Real-time results.
        - real_time_cost_per_result: Real-time cost per result.
        - real_time_result_rate: Real-time result rate.
        - secondary_goal_result: Results for secondary goals.
        - cost_per_secondary_goal_result: Cost per secondary goal result.
        - secondary_goal_result_rate: Rate of secondary goal results.
        - frequency: Average number of times each person saw the ad.
        - video_play_actions: Number of video play actions.
        - video_watched_2s: Number of times video was watched for at least 2 seconds.
        - video_watched_6s: Number of times video was watched for at least 6 seconds.
        - average_video_play: Average video play duration.
        - average_video_play_per_user: Average video play duration per user.
        - video_views_p25: Number of times video was watched to 25%.
        - video_views_p50: Number of times video was watched to 50%.
        - video_views_p75: Number of times video was watched to 75%.
        - video_views_p100: Number of times video was watched to 100%.
        - profile_visits: Number of profile visits.
        - likes: Number of likes.
        - comments: Number of comments.
        - shares: Number of shares.
        - follows: Number of follows.
        - clicks_on_music_disc: Number of clicks on the music disc.
        - real_time_app_install: Real-time app installations.
        - real_time_app_install_cost: Cost of real-time app installations.
        - app_install: Number of app installations.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsReportsLifetimeSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ads_reports_lifetime", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsReportsLifetimeSearchResult(
            data=[
                AdsReportsLifetimeSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
