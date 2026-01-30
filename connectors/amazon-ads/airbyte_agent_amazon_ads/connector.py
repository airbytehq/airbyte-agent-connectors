"""
Amazon-Ads connector.
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

from .connector_model import AmazonAdsConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    PortfoliosGetParams,
    PortfoliosListParams,
    ProfilesGetParams,
    ProfilesListParams,
    SponsoredProductCampaignsGetParams,
    SponsoredProductCampaignsListParams,
    SponsoredProductCampaignsListParamsStatefilter,
    AirbyteSearchParams,
    ProfilesSearchFilter,
    ProfilesSearchQuery,
)
if TYPE_CHECKING:
    from .models import AmazonAdsAuthConfig
# Import response models and envelope models at runtime
from .models import (
    AmazonAdsCheckResult,
    AmazonAdsExecuteResult,
    AmazonAdsExecuteResultWithMeta,
    ProfilesListResult,
    PortfoliosListResult,
    SponsoredProductCampaignsListResult,
    Portfolio,
    Profile,
    SponsoredProductCampaign,
    AirbyteSearchHit,
    AirbyteSearchResult,
    ProfilesSearchData,
    ProfilesSearchResult,
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




class AmazonAdsConnector:
    """
    Type-safe Amazon-Ads API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "amazon-ads"
    connector_version = "1.0.5"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("profiles", "list"): True,
        ("profiles", "get"): None,
        ("portfolios", "list"): True,
        ("portfolios", "get"): None,
        ("sponsored_product_campaigns", "list"): True,
        ("sponsored_product_campaigns", "get"): None,
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
    }

    def __init__(
        self,
        auth_config: AmazonAdsAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None,
        region: str | None = None    ):
        """
        Initialize a new amazon-ads connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            region: The Amazon Ads API endpoint URL based on region:
- NA (North America): https://advertising-api.amazon.com
- EU (Europe): https://advertising-api-eu.amazon.com
- FE (Far East): https://advertising-api-fe.amazon.com

        Examples:
            # Local mode (direct API calls)
            connector = AmazonAdsConnector(auth_config=AmazonAdsAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = AmazonAdsConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = AmazonAdsConnector(
                auth_config=AmazonAdsAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(AmazonAdsConnectorModel.id),
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
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> AmazonAdsExecuteResult[Any] | AmazonAdsExecuteResultWithMeta[Any, Any] | Any: ...

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
        enable_hosted_mode_features: bool = True,
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
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    AmazonAdsConnectorModel,
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



    async def search(
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
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProfilesSearchResult with hits (list of AirbyteSearchHit[ProfilesSearchData]) and pagination info

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

        result = await self._connector.execute("profiles", "search", params)

        # Parse response into typed result
        return ProfilesSearchResult(
            hits=[
                AirbyteSearchHit[ProfilesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ProfilesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
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
            data=result.data
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
            data=result.data
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


