"""
Tiktok-Marketing connector.
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

from .connector_model import TiktokMarketingConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AdGroupsListParams,
    AdGroupsReportsDailyListParams,
    AdsListParams,
    AdsReportsDailyListParams,
    AdvertisersListParams,
    AdvertisersReportsDailyListParams,
    AudiencesListParams,
    CampaignsListParams,
    CampaignsReportsDailyListParams,
    CreativeAssetsImagesListParams,
    CreativeAssetsVideosListParams,
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
    AdvertisersReportsDailySearchFilter,
    AdvertisersReportsDailySearchQuery,
    CampaignsReportsDailySearchFilter,
    CampaignsReportsDailySearchQuery,
    AdGroupsReportsDailySearchFilter,
    AdGroupsReportsDailySearchQuery,
    AdsReportsDailySearchFilter,
    AdsReportsDailySearchQuery,
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
    AdvertisersReportsDailyListResult,
    CampaignsReportsDailyListResult,
    AdGroupsReportsDailyListResult,
    AdsReportsDailyListResult,
    Ad,
    AdGroup,
    AdGroupsReportDaily,
    AdsReportDaily,
    Advertiser,
    AdvertisersReportDaily,
    Audience,
    Campaign,
    CampaignsReportDaily,
    CreativeAssetImage,
    CreativeAssetVideo,
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
    AdvertisersReportsDailySearchData,
    AdvertisersReportsDailySearchResult,
    CampaignsReportsDailySearchData,
    CampaignsReportsDailySearchResult,
    AdGroupsReportsDailySearchData,
    AdGroupsReportsDailySearchResult,
    AdsReportsDailySearchData,
    AdsReportsDailySearchResult,
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




class TiktokMarketingConnector:
    """
    Type-safe Tiktok-Marketing API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "tiktok-marketing"
    connector_version = "1.1.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("advertisers", "list"): True,
        ("campaigns", "list"): True,
        ("ad_groups", "list"): True,
        ("ads", "list"): True,
        ("audiences", "list"): True,
        ("creative_assets_images", "list"): True,
        ("creative_assets_videos", "list"): True,
        ("advertisers_reports_daily", "list"): True,
        ("campaigns_reports_daily", "list"): True,
        ("ad_groups_reports_daily", "list"): True,
        ("ads_reports_daily", "list"): True,
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
        ('advertisers_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('campaigns_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('ad_groups_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
        ('ads_reports_daily', 'list'): {'advertiser_id': 'advertiser_id', 'service_type': 'service_type', 'report_type': 'report_type', 'data_level': 'data_level', 'dimensions': 'dimensions', 'metrics': 'metrics', 'start_date': 'start_date', 'end_date': 'end_date', 'page': 'page', 'page_size': 'page_size'},
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
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

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

            # Hosted mode with lookup by customer_name
            connector = TiktokMarketingConnector(
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
                connector_definition_id=str(TiktokMarketingConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or TiktokMarketingAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

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
        self.advertisers_reports_daily = AdvertisersReportsDailyQuery(self)
        self.campaigns_reports_daily = CampaignsReportsDailyQuery(self)
        self.ad_groups_reports_daily = AdGroupsReportsDailyQuery(self)
        self.ads_reports_daily = AdsReportsDailyQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["advertisers"],
        action: Literal["list"],
        params: "AdvertisersListParams"
    ) -> "AdvertisersListResult": ...

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
        entity: Literal["ad_groups"],
        action: Literal["list"],
        params: "AdGroupsListParams"
    ) -> "AdGroupsListResult": ...

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
        entity: Literal["audiences"],
        action: Literal["list"],
        params: "AudiencesListParams"
    ) -> "AudiencesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creative_assets_images"],
        action: Literal["list"],
        params: "CreativeAssetsImagesListParams"
    ) -> "CreativeAssetsImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creative_assets_videos"],
        action: Literal["list"],
        params: "CreativeAssetsVideosListParams"
    ) -> "CreativeAssetsVideosListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["advertisers_reports_daily"],
        action: Literal["list"],
        params: "AdvertisersReportsDailyListParams"
    ) -> "AdvertisersReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns_reports_daily"],
        action: Literal["list"],
        params: "CampaignsReportsDailyListParams"
    ) -> "CampaignsReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups_reports_daily"],
        action: Literal["list"],
        params: "AdGroupsReportsDailyListParams"
    ) -> "AdGroupsReportsDailyListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads_reports_daily"],
        action: Literal["list"],
        params: "AdsReportsDailyListParams"
    ) -> "AdsReportsDailyListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "search"],
        params: Mapping[str, Any]
    ) -> TiktokMarketingExecuteResult[Any] | TiktokMarketingExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "search"],
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
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @TiktokMarketingConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @TiktokMarketingConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    TiktokMarketingConnectorModel,
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

        Example:
            connector = await TiktokMarketingConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "TiktokMarketingAuthConfig",
        name: str | None = None,
        replication_config: "TiktokMarketingReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "TiktokMarketingConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A TiktokMarketingConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await TiktokMarketingConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=TiktokMarketingAuthConfig(access_token="..."),
            )

            # With replication config (required for this connector):
            connector = await TiktokMarketingConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=TiktokMarketingAuthConfig(access_token="..."),
                replication_config=TiktokMarketingReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")


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
                connector_definition_id=str(TiktokMarketingConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
                replication_config=replication_config_dict,
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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("advertisers", "search", params)

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
            meta=result.meta
        )



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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("ad_groups", "search", params)

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
            meta=result.meta
        )



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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("audiences", "search", params)

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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("creative_assets_images", "search", params)

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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("creative_assets_videos", "search", params)

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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("advertisers_reports_daily", "search", params)

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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("campaigns_reports_daily", "search", params)

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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("ad_groups_reports_daily", "search", params)

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
            meta=result.meta
        )



    async def search(
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

        result = await self._connector.execute("ads_reports_daily", "search", params)

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
