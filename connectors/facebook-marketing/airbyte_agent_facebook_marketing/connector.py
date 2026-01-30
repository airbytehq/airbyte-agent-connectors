"""
Facebook-Marketing connector.
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

from .connector_model import FacebookMarketingConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    AdCreativesListParams,
    AdSetsGetParams,
    AdSetsListParams,
    AdsGetParams,
    AdsInsightsListParams,
    AdsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    CustomConversionsListParams,
    ImagesListParams,
    VideosListParams,
    AirbyteSearchParams,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    AdSetsSearchFilter,
    AdSetsSearchQuery,
    AdsSearchFilter,
    AdsSearchQuery,
    AdCreativesSearchFilter,
    AdCreativesSearchQuery,
    AdsInsightsSearchFilter,
    AdsInsightsSearchQuery,
    CustomConversionsSearchFilter,
    CustomConversionsSearchQuery,
    ImagesSearchFilter,
    ImagesSearchQuery,
    VideosSearchFilter,
    VideosSearchQuery,
)
if TYPE_CHECKING:
    from .models import FacebookMarketingAuthConfig
# Import response models and envelope models at runtime
from .models import (
    FacebookMarketingCheckResult,
    FacebookMarketingExecuteResult,
    FacebookMarketingExecuteResultWithMeta,
    CampaignsListResult,
    AdSetsListResult,
    AdsListResult,
    AdCreativesListResult,
    AdsInsightsListResult,
    CustomConversionsListResult,
    ImagesListResult,
    VideosListResult,
    Ad,
    AdCreative,
    AdSet,
    AdsInsight,
    Campaign,
    CustomConversion,
    Image,
    Video,
    AirbyteSearchHit,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdSetsSearchData,
    AdSetsSearchResult,
    AdsSearchData,
    AdsSearchResult,
    AdCreativesSearchData,
    AdCreativesSearchResult,
    AdsInsightsSearchData,
    AdsInsightsSearchResult,
    CustomConversionsSearchData,
    CustomConversionsSearchResult,
    ImagesSearchData,
    ImagesSearchResult,
    VideosSearchData,
    VideosSearchResult,
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




class FacebookMarketingConnector:
    """
    Type-safe Facebook-Marketing API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "facebook-marketing"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("campaigns", "list"): True,
        ("ad_sets", "list"): True,
        ("ads", "list"): True,
        ("ad_creatives", "list"): True,
        ("ads_insights", "list"): True,
        ("custom_conversions", "list"): True,
        ("images", "list"): True,
        ("videos", "list"): True,
        ("campaigns", "get"): None,
        ("ad_sets", "get"): None,
        ("ads", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('campaigns', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('ad_sets', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('ads', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('ad_creatives', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('ads_insights', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'date_preset': 'date_preset', 'time_range': 'time_range', 'level': 'level', 'limit': 'limit', 'after': 'after'},
        ('custom_conversions', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('images', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('videos', 'list'): {'account_id': 'account_id', 'fields': 'fields', 'limit': 'limit', 'after': 'after'},
        ('campaigns', 'get'): {'campaign_id': 'campaign_id', 'fields': 'fields'},
        ('ad_sets', 'get'): {'adset_id': 'adset_id', 'fields': 'fields'},
        ('ads', 'get'): {'ad_id': 'ad_id', 'fields': 'fields'},
    }

    def __init__(
        self,
        auth_config: FacebookMarketingAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new facebook-marketing connector instance.

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
            connector = FacebookMarketingConnector(auth_config=FacebookMarketingAuthConfig(access_token="...", client_id="...", client_secret="...", account_id="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = FacebookMarketingConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = FacebookMarketingConnector(
                auth_config=FacebookMarketingAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(FacebookMarketingConnectorModel.id),
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

            self._executor = LocalExecutor(
                model=FacebookMarketingConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.campaigns = CampaignsQuery(self)
        self.ad_sets = AdSetsQuery(self)
        self.ads = AdsQuery(self)
        self.ad_creatives = AdCreativesQuery(self)
        self.ads_insights = AdsInsightsQuery(self)
        self.custom_conversions = CustomConversionsQuery(self)
        self.images = ImagesQuery(self)
        self.videos = VideosQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["ad_sets"],
        action: Literal["list"],
        params: "AdSetsListParams"
    ) -> "AdSetsListResult": ...

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
        entity: Literal["ad_creatives"],
        action: Literal["list"],
        params: "AdCreativesListParams"
    ) -> "AdCreativesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads_insights"],
        action: Literal["list"],
        params: "AdsInsightsListParams"
    ) -> "AdsInsightsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_conversions"],
        action: Literal["list"],
        params: "CustomConversionsListParams"
    ) -> "CustomConversionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["images"],
        action: Literal["list"],
        params: "ImagesListParams"
    ) -> "ImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["videos"],
        action: Literal["list"],
        params: "VideosListParams"
    ) -> "VideosListResult": ...

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
        entity: Literal["ad_sets"],
        action: Literal["get"],
        params: "AdSetsGetParams"
    ) -> "AdSet": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads"],
        action: Literal["get"],
        params: "AdsGetParams"
    ) -> "Ad": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> FacebookMarketingExecuteResult[Any] | FacebookMarketingExecuteResultWithMeta[Any, Any] | Any: ...

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
                return FacebookMarketingExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return FacebookMarketingExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> FacebookMarketingCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            FacebookMarketingCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return FacebookMarketingCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return FacebookMarketingCheckResult(
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
            @FacebookMarketingConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @FacebookMarketingConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    FacebookMarketingConnectorModel,
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
        return describe_entities(FacebookMarketingConnectorModel)

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
            (e for e in FacebookMarketingConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in FacebookMarketingConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a list of campaigns for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
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
        campaign_id: str,
        fields: str | None = None,
        **kwargs
    ) -> Campaign:
        """
        Returns a single campaign by ID

        Args:
            campaign_id: The campaign ID
            fields: Comma-separated list of fields to return
            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            "fields": fields,
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
        - id: Campaign ID
        - name: Campaign name
        - account_id: Ad account ID
        - status: Campaign status
        - effective_status: Effective status
        - objective: Campaign objective
        - daily_budget: Daily budget in account currency
        - lifetime_budget: Lifetime budget
        - budget_remaining: Remaining budget
        - created_time: Campaign creation time
        - start_time: Campaign start time
        - stop_time: Campaign stop time
        - updated_time: Last update time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with hits (list of AirbyteSearchHit[CampaignsSearchData]) and pagination info

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
        return CampaignsSearchResult(
            hits=[
                AirbyteSearchHit[CampaignsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CampaignsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class AdSetsQuery:
    """
    Query class for AdSets entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> AdSetsListResult:
        """
        Returns a list of ad sets for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            AdSetsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_sets", "list", params)
        # Cast generic envelope to concrete typed result
        return AdSetsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        adset_id: str,
        fields: str | None = None,
        **kwargs
    ) -> AdSet:
        """
        Returns a single ad set by ID

        Args:
            adset_id: The ad set ID
            fields: Comma-separated list of fields to return
            **kwargs: Additional parameters

        Returns:
            AdSet
        """
        params = {k: v for k, v in {
            "adset_id": adset_id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_sets", "get", params)
        return result



    async def search(
        self,
        query: AdSetsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdSetsSearchResult:
        """
        Search ad_sets records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdSetsSearchFilter):
        - id: Ad Set ID
        - name: Ad Set name
        - account_id: Ad account ID
        - campaign_id: Parent campaign ID
        - effective_status: Effective status
        - daily_budget: Daily budget
        - lifetime_budget: Lifetime budget
        - budget_remaining: Remaining budget
        - bid_amount: Bid amount
        - bid_strategy: Bid strategy
        - created_time: Ad set creation time
        - start_time: Ad set start time
        - end_time: Ad set end time
        - updated_time: Last update time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdSetsSearchResult with hits (list of AirbyteSearchHit[AdSetsSearchData]) and pagination info

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

        result = await self._connector.execute("ad_sets", "search", params)

        # Parse response into typed result
        return AdSetsSearchResult(
            hits=[
                AirbyteSearchHit[AdSetsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=AdSetsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class AdsQuery:
    """
    Query class for Ads entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> AdsListResult:
        """
        Returns a list of ads for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            AdsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
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
        ad_id: str,
        fields: str | None = None,
        **kwargs
    ) -> Ad:
        """
        Returns a single ad by ID

        Args:
            ad_id: The ad ID
            fields: Comma-separated list of fields to return
            **kwargs: Additional parameters

        Returns:
            Ad
        """
        params = {k: v for k, v in {
            "ad_id": ad_id,
            "fields": fields,
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
        - id: Ad ID
        - name: Ad name
        - account_id: Ad account ID
        - adset_id: Parent ad set ID
        - campaign_id: Parent campaign ID
        - status: Ad status
        - effective_status: Effective status
        - created_time: Ad creation time
        - updated_time: Last update time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsSearchResult with hits (list of AirbyteSearchHit[AdsSearchData]) and pagination info

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
        return AdsSearchResult(
            hits=[
                AirbyteSearchHit[AdsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=AdsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class AdCreativesQuery:
    """
    Query class for AdCreatives entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> AdCreativesListResult:
        """
        Returns a list of ad creatives for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            AdCreativesListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_creatives", "list", params)
        # Cast generic envelope to concrete typed result
        return AdCreativesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AdCreativesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdCreativesSearchResult:
        """
        Search ad_creatives records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdCreativesSearchFilter):
        - id: Ad Creative ID
        - name: Ad Creative name
        - account_id: Ad account ID
        - body: Ad body text
        - title: Ad title
        - status: Creative status
        - image_url: Image URL
        - thumbnail_url: Thumbnail URL
        - link_url: Link URL
        - call_to_action_type: Call to action type

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdCreativesSearchResult with hits (list of AirbyteSearchHit[AdCreativesSearchData]) and pagination info

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

        result = await self._connector.execute("ad_creatives", "search", params)

        # Parse response into typed result
        return AdCreativesSearchResult(
            hits=[
                AirbyteSearchHit[AdCreativesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=AdCreativesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class AdsInsightsQuery:
    """
    Query class for AdsInsights entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        date_preset: str | None = None,
        time_range: str | None = None,
        level: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> AdsInsightsListResult:
        """
        Returns performance insights for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            date_preset: Predefined date range
            time_range: Time range as JSON object with since and until dates (YYYY-MM-DD)
            level: Level of aggregation
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            AdsInsightsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "date_preset": date_preset,
            "time_range": time_range,
            "level": level,
            "limit": limit,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads_insights", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsInsightsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AdsInsightsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsInsightsSearchResult:
        """
        Search ads_insights records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsInsightsSearchFilter):
        - account_id: Ad account ID
        - account_name: Ad account name
        - campaign_id: Campaign ID
        - campaign_name: Campaign name
        - adset_id: Ad set ID
        - adset_name: Ad set name
        - ad_id: Ad ID
        - ad_name: Ad name
        - clicks: Number of clicks
        - impressions: Number of impressions
        - reach: Number of unique people reached
        - spend: Amount spent
        - cpc: Cost per click
        - cpm: Cost per 1000 impressions
        - ctr: Click-through rate
        - date_start: Start date of the reporting period
        - date_stop: End date of the reporting period

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsInsightsSearchResult with hits (list of AirbyteSearchHit[AdsInsightsSearchData]) and pagination info

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

        result = await self._connector.execute("ads_insights", "search", params)

        # Parse response into typed result
        return AdsInsightsSearchResult(
            hits=[
                AirbyteSearchHit[AdsInsightsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=AdsInsightsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class CustomConversionsQuery:
    """
    Query class for CustomConversions entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> CustomConversionsListResult:
        """
        Returns a list of custom conversions for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CustomConversionsListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_conversions", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomConversionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CustomConversionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomConversionsSearchResult:
        """
        Search custom_conversions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomConversionsSearchFilter):
        - id: Custom Conversion ID
        - name: Custom Conversion name
        - account_id: Ad account ID
        - description: Description
        - custom_event_type: Custom event type
        - creation_time: Creation time
        - first_fired_time: First fired time
        - last_fired_time: Last fired time
        - is_archived: Whether the conversion is archived

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomConversionsSearchResult with hits (list of AirbyteSearchHit[CustomConversionsSearchData]) and pagination info

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

        result = await self._connector.execute("custom_conversions", "search", params)

        # Parse response into typed result
        return CustomConversionsSearchResult(
            hits=[
                AirbyteSearchHit[CustomConversionsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CustomConversionsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ImagesQuery:
    """
    Query class for Images entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> ImagesListResult:
        """
        Returns a list of ad images for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            ImagesListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("images", "list", params)
        # Cast generic envelope to concrete typed result
        return ImagesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ImagesSearchResult:
        """
        Search images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ImagesSearchFilter):
        - id: Image ID
        - name: Image name
        - account_id: Ad account ID
        - hash: Image hash
        - url: Image URL
        - permalink_url: Permalink URL
        - width: Image width
        - height: Image height
        - status: Image status
        - created_time: Creation time
        - updated_time: Last update time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ImagesSearchResult with hits (list of AirbyteSearchHit[ImagesSearchData]) and pagination info

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

        result = await self._connector.execute("images", "search", params)

        # Parse response into typed result
        return ImagesSearchResult(
            hits=[
                AirbyteSearchHit[ImagesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ImagesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class VideosQuery:
    """
    Query class for Videos entity operations.
    """

    def __init__(self, connector: FacebookMarketingConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_id: str,
        fields: str | None = None,
        limit: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> VideosListResult:
        """
        Returns a list of ad videos for the specified ad account

        Args:
            account_id: The Facebook Ad Account ID (without act_ prefix)
            fields: Comma-separated list of fields to return
            limit: Maximum number of results to return
            after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            VideosListResult
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "fields": fields,
            "limit": limit,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("videos", "list", params)
        # Cast generic envelope to concrete typed result
        return VideosListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: VideosSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> VideosSearchResult:
        """
        Search videos records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (VideosSearchFilter):
        - id: Video ID
        - title: Video title
        - account_id: Ad account ID
        - description: Video description
        - length: Video length in seconds
        - source: Video source URL
        - permalink_url: Permalink URL
        - views: Number of views
        - created_time: Creation time
        - updated_time: Last update time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            VideosSearchResult with hits (list of AirbyteSearchHit[VideosSearchData]) and pagination info

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

        result = await self._connector.execute("videos", "search", params)

        # Parse response into typed result
        return VideosSearchResult(
            hits=[
                AirbyteSearchHit[VideosSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=VideosSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )
