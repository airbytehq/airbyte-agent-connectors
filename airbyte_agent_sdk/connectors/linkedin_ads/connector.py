"""
Linkedin-Ads connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import LinkedinAdsConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.tools import UNSET, AgentToolRole, SkillDocsAccessor, Unset, build_agent_tool_decorator
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AccountUsersCreateParams,
    AccountUsersDeleteParams,
    AccountUsersListParams,
    AccountUsersUpdateParams,
    AccountUsersUpdateParamsPatch,
    AccountsCreateParams,
    AccountsDeleteParams,
    AccountsGetParams,
    AccountsListParams,
    AccountsUpdateParams,
    AccountsUpdateParamsPatch,
    AdCampaignAnalyticsListParams,
    AdCreativeAnalyticsListParams,
    AdImpressionDeviceAnalyticsListParams,
    AdMemberCompanyAnalyticsListParams,
    AdMemberCompanySizeAnalyticsListParams,
    AdMemberCountryAnalyticsListParams,
    AdMemberIndustryAnalyticsListParams,
    AdMemberJobFunctionAnalyticsListParams,
    AdMemberJobTitleAnalyticsListParams,
    AdMemberRegionAnalyticsListParams,
    AdMemberSeniorityAnalyticsListParams,
    CampaignConversionsCreateParams,
    CampaignConversionsDeleteParams,
    CampaignGroupsCreateParams,
    CampaignGroupsCreateParamsRunschedule,
    CampaignGroupsCreateParamsTotalbudget,
    CampaignGroupsDeleteParams,
    CampaignGroupsGetParams,
    CampaignGroupsListParams,
    CampaignGroupsUpdateParams,
    CampaignGroupsUpdateParamsPatch,
    CampaignsCreateParams,
    CampaignsCreateParamsDailybudget,
    CampaignsCreateParamsLocale,
    CampaignsCreateParamsRunschedule,
    CampaignsCreateParamsUnitcost,
    CampaignsDeleteParams,
    CampaignsGetParams,
    CampaignsListParams,
    CampaignsUpdateParams,
    CampaignsUpdateParamsPatch,
    ConversionEventsCreateParams,
    ConversionEventsCreateParamsElementsItem,
    ConversionsCreateParams,
    ConversionsCreateParamsValue,
    ConversionsGetParams,
    ConversionsListParams,
    ConversionsUpdateParams,
    ConversionsUpdateParamsPatch,
    CreativesCreateParams,
    CreativesDeleteParams,
    CreativesGetParams,
    CreativesListParams,
    CreativesUpdateParams,
    CreativesUpdateParamsPatch,
    LeadFormResponsesListParams,
    LeadFormsListParams,
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
    AdImpressionDeviceAnalyticsSearchFilter,
    AdImpressionDeviceAnalyticsSearchQuery,
    AdMemberCompanyAnalyticsSearchFilter,
    AdMemberCompanyAnalyticsSearchQuery,
    AdMemberCompanySizeAnalyticsSearchFilter,
    AdMemberCompanySizeAnalyticsSearchQuery,
    AdMemberCountryAnalyticsSearchFilter,
    AdMemberCountryAnalyticsSearchQuery,
    AdMemberIndustryAnalyticsSearchFilter,
    AdMemberIndustryAnalyticsSearchQuery,
    AdMemberJobFunctionAnalyticsSearchFilter,
    AdMemberJobFunctionAnalyticsSearchQuery,
    AdMemberJobTitleAnalyticsSearchFilter,
    AdMemberJobTitleAnalyticsSearchQuery,
    AdMemberRegionAnalyticsSearchFilter,
    AdMemberRegionAnalyticsSearchQuery,
    AdMemberSeniorityAnalyticsSearchFilter,
    AdMemberSeniorityAnalyticsSearchQuery,
    LeadFormsSearchFilter,
    LeadFormsSearchQuery,
    LeadFormResponsesSearchFilter,
    LeadFormResponsesSearchQuery,
)
from .models import LinkedinAdsOauth20AuthenticationAuthConfig, LinkedinAdsAccessTokenAuthenticationAuthConfig
from .models import LinkedinAdsAuthConfig
if TYPE_CHECKING:
    from .models import LinkedinAdsReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    LinkedinAdsCheckResult,
    LinkedinAdsExecuteResult,
    LinkedinAdsExecuteResultWithMeta,
    AccountsListResult,
    AccountsCreateResult,
    AccountUsersListResult,
    CampaignsListResult,
    CampaignsCreateResult,
    CampaignGroupsListResult,
    CampaignGroupsCreateResult,
    CreativesListResult,
    CreativesCreateResult,
    ConversionsListResult,
    ConversionsCreateResult,
    AdCampaignAnalyticsListResult,
    AdCreativeAnalyticsListResult,
    AdImpressionDeviceAnalyticsListResult,
    AdMemberCompanyAnalyticsListResult,
    AdMemberCompanySizeAnalyticsListResult,
    AdMemberCountryAnalyticsListResult,
    AdMemberIndustryAnalyticsListResult,
    AdMemberJobFunctionAnalyticsListResult,
    AdMemberJobTitleAnalyticsListResult,
    AdMemberRegionAnalyticsListResult,
    AdMemberSeniorityAnalyticsListResult,
    LeadFormsListResult,
    LeadFormResponsesListResult,
    Account,
    AccountUser,
    AdAnalyticsRecord,
    Campaign,
    CampaignGroup,
    Conversion,
    Creative,
    LeadForm,
    LeadFormResponse,
    RestliCreateResponse,
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
    AdImpressionDeviceAnalyticsSearchData,
    AdImpressionDeviceAnalyticsSearchResult,
    AdMemberCompanyAnalyticsSearchData,
    AdMemberCompanyAnalyticsSearchResult,
    AdMemberCompanySizeAnalyticsSearchData,
    AdMemberCompanySizeAnalyticsSearchResult,
    AdMemberCountryAnalyticsSearchData,
    AdMemberCountryAnalyticsSearchResult,
    AdMemberIndustryAnalyticsSearchData,
    AdMemberIndustryAnalyticsSearchResult,
    AdMemberJobFunctionAnalyticsSearchData,
    AdMemberJobFunctionAnalyticsSearchResult,
    AdMemberJobTitleAnalyticsSearchData,
    AdMemberJobTitleAnalyticsSearchResult,
    AdMemberRegionAnalyticsSearchData,
    AdMemberRegionAnalyticsSearchResult,
    AdMemberSeniorityAnalyticsSearchData,
    AdMemberSeniorityAnalyticsSearchResult,
    LeadFormsSearchData,
    LeadFormsSearchResult,
    LeadFormResponsesSearchData,
    LeadFormResponsesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class LinkedinAdsConnector:
    """
    Type-safe Linkedin-Ads API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "linkedin-ads"
    connector_version = "1.2.0"
    sdk_version = "0.1.305"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("accounts", "list"): True,
        ("accounts", "create"): {'created_id': '@header.x-restli-id'},
        ("accounts", "get"): None,
        ("accounts", "update"): None,
        ("accounts", "delete"): None,
        ("account_users", "list"): True,
        ("account_users", "update"): None,
        ("account_users", "create"): None,
        ("account_users", "delete"): None,
        ("campaigns", "list"): True,
        ("campaigns", "create"): {'created_id': '@header.x-restli-id'},
        ("campaigns", "get"): None,
        ("campaigns", "update"): None,
        ("campaigns", "delete"): None,
        ("campaign_groups", "list"): True,
        ("campaign_groups", "create"): {'created_id': '@header.x-restli-id'},
        ("campaign_groups", "get"): None,
        ("campaign_groups", "update"): None,
        ("campaign_groups", "delete"): None,
        ("creatives", "list"): True,
        ("creatives", "create"): {'created_id': '@header.x-restli-id'},
        ("creatives", "get"): None,
        ("creatives", "update"): None,
        ("creatives", "delete"): None,
        ("conversions", "list"): True,
        ("conversions", "create"): {'created_id': '@header.x-restli-id'},
        ("conversions", "get"): None,
        ("conversions", "update"): None,
        ("conversion_events", "create"): None,
        ("campaign_conversions", "create"): None,
        ("campaign_conversions", "delete"): None,
        ("ad_campaign_analytics", "list"): True,
        ("ad_creative_analytics", "list"): True,
        ("ad_impression_device_analytics", "list"): True,
        ("ad_member_company_analytics", "list"): True,
        ("ad_member_company_size_analytics", "list"): True,
        ("ad_member_country_analytics", "list"): True,
        ("ad_member_industry_analytics", "list"): True,
        ("ad_member_job_function_analytics", "list"): True,
        ("ad_member_job_title_analytics", "list"): True,
        ("ad_member_region_analytics", "list"): True,
        ("ad_member_seniority_analytics", "list"): True,
        ("lead_forms", "list"): True,
        ("lead_form_responses", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('accounts', 'list'): {'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('accounts', 'create'): {'name': 'name', 'type': 'type', 'currency': 'currency', 'reference': 'reference', 'test': 'test'},
        ('accounts', 'get'): {'id': 'id'},
        ('accounts', 'update'): {'patch': 'patch', 'id': 'id'},
        ('accounts', 'delete'): {'id': 'id'},
        ('account_users', 'list'): {'q': 'q', 'accounts': 'accounts', 'count': 'count', 'start': 'start'},
        ('account_users', 'update'): {'patch': 'patch', 'account': 'account', 'user': 'user'},
        ('account_users', 'create'): {'role': 'role', 'account': 'account', 'user': 'user'},
        ('account_users', 'delete'): {'account': 'account', 'user': 'user'},
        ('campaigns', 'list'): {'account_id': 'account_id', 'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('campaigns', 'create'): {'account': 'account', 'name': 'name', 'political_intent': 'politicalIntent', 'campaign_group': 'campaignGroup', 'type': 'type', 'objective_type': 'objectiveType', 'status': 'status', 'cost_type': 'costType', 'daily_budget': 'dailyBudget', 'unit_cost': 'unitCost', 'locale': 'locale', 'run_schedule': 'runSchedule', 'targeting_criteria': 'targetingCriteria', 'audience_expansion_enabled': 'audienceExpansionEnabled', 'offsite_delivery_enabled': 'offsiteDeliveryEnabled', 'creative_selection': 'creativeSelection', 'account_id': 'account_id'},
        ('campaigns', 'get'): {'account_id': 'account_id', 'id': 'id'},
        ('campaigns', 'update'): {'patch': 'patch', 'account_id': 'account_id', 'id': 'id'},
        ('campaigns', 'delete'): {'account_id': 'account_id', 'id': 'id'},
        ('campaign_groups', 'list'): {'account_id': 'account_id', 'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('campaign_groups', 'create'): {'account': 'account', 'name': 'name', 'status': 'status', 'run_schedule': 'runSchedule', 'total_budget': 'totalBudget', 'objective_type': 'objectiveType', 'account_id': 'account_id'},
        ('campaign_groups', 'get'): {'account_id': 'account_id', 'id': 'id'},
        ('campaign_groups', 'update'): {'patch': 'patch', 'account_id': 'account_id', 'id': 'id'},
        ('campaign_groups', 'delete'): {'account_id': 'account_id', 'id': 'id'},
        ('creatives', 'list'): {'account_id': 'account_id', 'q': 'q', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('creatives', 'create'): {'campaign': 'campaign', 'content': 'content', 'intended_status': 'intendedStatus', 'name': 'name', 'account_id': 'account_id'},
        ('creatives', 'get'): {'account_id': 'account_id', 'id': 'id'},
        ('creatives', 'update'): {'patch': 'patch', 'account_id': 'account_id', 'id': 'id'},
        ('creatives', 'delete'): {'account_id': 'account_id', 'id': 'id'},
        ('conversions', 'list'): {'q': 'q', 'account': 'account', 'count': 'count', 'start': 'start'},
        ('conversions', 'create'): {'account': 'account', 'name': 'name', 'type': 'type', 'attribution_type': 'attributionType', 'post_click_attribution_window_size': 'postClickAttributionWindowSize', 'view_through_attribution_window_size': 'viewThroughAttributionWindowSize', 'enabled': 'enabled', 'url_match_rule_expression': 'urlMatchRuleExpression', 'value': 'value', 'auto_association_type': 'autoAssociationType'},
        ('conversions', 'get'): {'id': 'id'},
        ('conversions', 'update'): {'patch': 'patch', 'id': 'id', 'account': 'account'},
        ('conversion_events', 'create'): {'elements': 'elements'},
        ('campaign_conversions', 'create'): {'campaign': 'campaign', 'conversion': 'conversion', 'campaign_urn': 'campaign_urn', 'conversion_urn': 'conversion_urn'},
        ('campaign_conversions', 'delete'): {'campaign_urn': 'campaign_urn', 'conversion_urn': 'conversion_urn'},
        ('ad_campaign_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_creative_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'creatives': 'creatives', 'fields': 'fields'},
        ('ad_impression_device_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_company_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_company_size_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_country_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_industry_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_job_function_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_job_title_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_region_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('ad_member_seniority_analytics', 'list'): {'q': 'q', 'pivot': 'pivot', 'time_granularity': 'timeGranularity', 'date_range': 'dateRange', 'campaigns': 'campaigns', 'fields': 'fields'},
        ('lead_forms', 'list'): {'q': 'q', 'owner': 'owner', 'count': 'count', 'start': 'start'},
        ('lead_form_responses', 'list'): {'q': 'q', 'owner': 'owner', 'lead_type': 'leadType', 'count': 'count', 'start': 'start'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (LinkedinAdsOauth20AuthenticationAuthConfig, LinkedinAdsAccessTokenAuthenticationAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: LinkedinAdsAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new linkedin-ads connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., LinkedinAdsAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

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

            # Hosted mode with lookup by workspace_name
            connector = LinkedinAdsConnector(
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
                connector_definition_id=str(LinkedinAdsConnectorModel.id),
                model=LinkedinAdsConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or LinkedinAdsAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, LinkedinAdsOauth20AuthenticationAuthConfig):
                    auth_scheme = "oauth2"
                if isinstance(auth_config, LinkedinAdsAccessTokenAuthenticationAuthConfig):
                    auth_scheme = "bearerAuth"

            self._executor = LocalExecutor(
                model=LinkedinAdsConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
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
        self.conversion_events = ConversionEventsQuery(self)
        self.campaign_conversions = CampaignConversionsQuery(self)
        self.ad_campaign_analytics = AdCampaignAnalyticsQuery(self)
        self.ad_creative_analytics = AdCreativeAnalyticsQuery(self)
        self.ad_impression_device_analytics = AdImpressionDeviceAnalyticsQuery(self)
        self.ad_member_company_analytics = AdMemberCompanyAnalyticsQuery(self)
        self.ad_member_company_size_analytics = AdMemberCompanySizeAnalyticsQuery(self)
        self.ad_member_country_analytics = AdMemberCountryAnalyticsQuery(self)
        self.ad_member_industry_analytics = AdMemberIndustryAnalyticsQuery(self)
        self.ad_member_job_function_analytics = AdMemberJobFunctionAnalyticsQuery(self)
        self.ad_member_job_title_analytics = AdMemberJobTitleAnalyticsQuery(self)
        self.ad_member_region_analytics = AdMemberRegionAnalyticsQuery(self)
        self.ad_member_seniority_analytics = AdMemberSeniorityAnalyticsQuery(self)
        self.lead_forms = LeadFormsQuery(self)
        self.lead_form_responses = LeadFormResponsesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["list"],
        params: "AccountsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["create"],
        params: "AccountsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AccountsCreateResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["update"],
        params: "AccountsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["delete"],
        params: "AccountsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["account_users"],
        action: Literal["list"],
        params: "AccountUsersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AccountUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["account_users"],
        action: Literal["update"],
        params: "AccountUsersUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["account_users"],
        action: Literal["create"],
        params: "AccountUsersCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RestliCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["account_users"],
        action: Literal["delete"],
        params: "AccountUsersDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

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
        entity: Literal["campaigns"],
        action: Literal["create"],
        params: "CampaignsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsCreateResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["update"],
        params: "CampaignsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["delete"],
        params: "CampaignsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["list"],
        params: "CampaignGroupsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["create"],
        params: "CampaignGroupsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignGroupsCreateResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["get"],
        params: "CampaignGroupsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignGroup": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["update"],
        params: "CampaignGroupsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_groups"],
        action: Literal["delete"],
        params: "CampaignGroupsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["list"],
        params: "CreativesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CreativesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["create"],
        params: "CreativesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CreativesCreateResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["get"],
        params: "CreativesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Creative": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["update"],
        params: "CreativesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["creatives"],
        action: Literal["delete"],
        params: "CreativesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversions"],
        action: Literal["list"],
        params: "ConversionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ConversionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversions"],
        action: Literal["create"],
        params: "ConversionsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ConversionsCreateResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversions"],
        action: Literal["get"],
        params: "ConversionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Conversion": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversions"],
        action: Literal["update"],
        params: "ConversionsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversion_events"],
        action: Literal["create"],
        params: "ConversionEventsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RestliCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_conversions"],
        action: Literal["create"],
        params: "CampaignConversionsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RestliCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_conversions"],
        action: Literal["delete"],
        params: "CampaignConversionsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_campaign_analytics"],
        action: Literal["list"],
        params: "AdCampaignAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdCampaignAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_creative_analytics"],
        action: Literal["list"],
        params: "AdCreativeAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdCreativeAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_impression_device_analytics"],
        action: Literal["list"],
        params: "AdImpressionDeviceAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdImpressionDeviceAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_company_analytics"],
        action: Literal["list"],
        params: "AdMemberCompanyAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberCompanyAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_company_size_analytics"],
        action: Literal["list"],
        params: "AdMemberCompanySizeAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberCompanySizeAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_country_analytics"],
        action: Literal["list"],
        params: "AdMemberCountryAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberCountryAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_industry_analytics"],
        action: Literal["list"],
        params: "AdMemberIndustryAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberIndustryAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_job_function_analytics"],
        action: Literal["list"],
        params: "AdMemberJobFunctionAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberJobFunctionAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_job_title_analytics"],
        action: Literal["list"],
        params: "AdMemberJobTitleAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberJobTitleAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_region_analytics"],
        action: Literal["list"],
        params: "AdMemberRegionAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberRegionAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_member_seniority_analytics"],
        action: Literal["list"],
        params: "AdMemberSeniorityAnalyticsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdMemberSeniorityAnalyticsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["lead_forms"],
        action: Literal["list"],
        params: "LeadFormsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "LeadFormsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["lead_form_responses"],
        action: Literal["list"],
        params: "LeadFormResponsesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "LeadFormResponsesListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "delete", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> LinkedinAdsExecuteResult[Any] | LinkedinAdsExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "delete", "context_store_search"],
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

        connector = LinkedinAdsConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @LinkedinAdsConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @LinkedinAdsConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @LinkedinAdsConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
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
                    LinkedinAdsConnectorModel,
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

    @classmethod
    def agent_tool(
        cls,
        role: AgentToolRole | None = None,
        *,
        inspect_tool: str | None = None,
        docs_tool: str | None = None,
        max_output_chars: int | None | Unset = UNSET,
        framework: FrameworkName = "none",
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> Callable[[_F], _F]:
        """
        Framework-agnostic decorator for user-written connector tool functions.

        The progressive-docs sibling of tool_utils: instead of baking the full
        entity/action reference into the docstring, it instructs the agent to
        call this connector's inspect and docs tools before executing. Tool
        failures raise :class:`airbyte_agent_sdk.AirbyteToolError` by default
        (``framework="none"``, no auto-detection) — pass ``framework=...`` to
        translate to a supported framework's signal instead.

        Decorate three functions per connector — execute, inspect and docs.
        The role is inferred from each function's signature (extra parameters
        are allowed); a signature matching more than one role, a generic
        ``(*args, **kwargs)`` wrapper, or a callable whose signature cannot
        be read must pass the role explicitly:

        - ``(entity, action, ...)`` -> ``"execute"``
        - ``(section, ...)``        -> ``"read_skill_docs"``
        - ``()``                    -> ``"inspect_connector"``

        Usage:
            connector = LinkedinAdsConnector(...)

            @LinkedinAdsConnector.agent_tool()
            async def execute(entity: str, action: str, params: dict | None = None):
                return await connector.execute(entity=entity, action=action, params=params or {})

            @LinkedinAdsConnector.agent_tool()
            async def inspect_connector():
                return await connector.inspect_connector()

            @LinkedinAdsConnector.agent_tool()
            async def read_skill_docs(section: str | None = None):
                return await connector.read_skill_docs(section)

        Args:
            role: ``"execute" | "inspect_connector" | "read_skill_docs"``.
                None (default) infers the role from the decorated function's
                signature; an explicit role validates the canonical
                parameters are present (functions accepting ``**kwargs``, or
                callables whose signature cannot be read, pass validation).
            inspect_tool: Exact registered name of the sibling inspect tool,
                woven into the execute docstring for tighter steering.
                Defaults to generic phrasing.
            docs_tool: Exact registered name of the sibling docs tool (see
                inspect_tool).
            max_output_chars: Max serialized output size before failing.
                Defaults per role: execute -> DEFAULT_MAX_OUTPUT_CHARS, docs
                tools -> None.
            framework: Translation target for tool failures. Defaults to
                ``"none"`` (raise AirbyteToolError); never auto-detects.
            internal_retries: How many transient runtime failures (429/5xx,
                network, timeout) to retry silently before surfacing.
                Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate ``(error, args, kwargs)
                -> bool`` further restricting which retryable errors are safe
                for this specific tool. Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback ``(error,
                args, kwargs) -> str | None`` invoked after internal retries
                are exhausted or skipped. Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
        """
        return build_agent_tool_decorator(  # type: ignore[return-value]
            LinkedinAdsConnectorModel,
            role=role,
            inspect_tool=inspect_tool,
            docs_tool=docs_tool,
            max_output_chars=max_output_chars,
            framework=framework,
            internal_retries=internal_retries,
            should_internal_retry=should_internal_retry,
            exhausted_runtime_failure_message=exhausted_runtime_failure_message,
        )

    def _skill_docs(self) -> SkillDocsAccessor:
        accessor: SkillDocsAccessor | None = getattr(self, "_skill_docs_accessor", None)
        if accessor is None:
            accessor = SkillDocsAccessor(self)
            self._skill_docs_accessor = accessor
        return accessor

    async def inspect_connector(self) -> dict[str, Any]:
        """
        Inspect this connector's hosted metadata/readiness and resolve its docs skill id.

        Call this before read_skill_docs in the normal hosted flow. For
        local/offline connectors this returns a local-mode payload with a
        warning instead of a hosted inspection.

        Example:
            info = await connector.inspect_connector()
            print(info["docs_skill_id"])
        """
        return await self._skill_docs().inspect()

    async def read_skill_docs(self, section: str | None = None) -> str:
        """
        Read this connector's usage docs, rendered to text.

        Omit section for the outline and general guidance; pass an exact
        section id from the outline for full details. For local/offline
        connectors the full generated docs are returned and section is
        ignored.

        Example:
            outline = await connector.read_skill_docs()
            details = await connector.read_skill_docs(section="entity:contacts")
        """
        return await self._skill_docs().read(section)

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
            q: LinkedIn API finder method for querying ad accounts
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
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        name: str,
        type: str,
        currency: str | None = None,
        reference: str | None = None,
        test: bool | None = None,
        **kwargs
    ) -> AccountsCreateResult:
        """
        Creates a new ad account. Only type BUSINESS can be created via the API (ENTERPRISE accounts cannot). Requires the rw_ads OAuth scope. The new account ID is returned in the x-restli-id response header.


        Args:
            name: Ad account name
            type: Account type; only BUSINESS accounts can be created via the API
            currency: ISO 4217 currency code, e.g. USD (defaults to USD)
            reference: Optional owning organization URN, e.g. urn:li:organization:123456
            test: Whether to create a test account
            **kwargs: Additional parameters

        Returns:
            AccountsCreateResult
        """
        params = {k: v for k, v in {
            "name": name,
            "type": type,
            "currency": currency,
            "reference": reference,
            "test": test,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "create", params)
        # Cast generic envelope to concrete typed result
        return AccountsCreateResult(
            data=result.data,
            meta=getattr(result, "meta", None)
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



    async def update(
        self,
        patch: AccountsUpdateParamsPatch,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Partially updates an ad account using the Rest.li PARTIAL_UPDATE pattern: the body wraps the fields to change in patch.$set. Requires the rw_ads OAuth scope; most account fields require the ACCOUNT_BILLING_ADMIN role. To soft-delete a non-DRAFT account, set status to PENDING_DELETION here (billing admin only).


        Args:
            patch: Parameter patch
            id: Ad account ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "patch": patch,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Hard-deletes an ad account. Only accounts in DRAFT status accept a true DELETE; for non-DRAFT accounts use the update operation to set status to PENDING_DELETION. Both forms require the ACCOUNT_BILLING_ADMIN role and the rw_ads OAuth scope.


        Args:
            id: Ad account ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "delete", params)
        return result



    async def context_store_search(
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
        - test: Flag indicating if the account is in a test mode.
        - notified_on_creative_rejection: Flag for notifications on creative rejection.
        - notified_on_new_features_enabled: Flag for notifications on new features being enabled.
        - notified_on_end_of_campaign: Flag for notifications on the end of campaign.
        - serving_statuses: The serving statuses associated with the account.
        - notified_on_campaign_optimization: Flag for notifications on campaign optimization.
        - type_: The type or category of the account.
        - version: The version information related to the account.
        - reference: A reference identifier for the account.
        - notified_on_creative_approval: Flag for notifications on creative approval.
        - created: The timestamp indicating when the account was created.
        - last_modified: The timestamp of the last modification made to the account.
        - name: The name of the account.
        - currency: The currency used for financial transactions in the account.
        - id: The unique identifier for the account.
        - status: The status of the account.

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

        result = await self._connector.execute("accounts", "context_store_search", params)

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
            q: LinkedIn API finder method for querying by account URN
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
            meta=getattr(result, "meta", None)
        )



    async def update(
        self,
        patch: AccountUsersUpdateParamsPatch,
        account: str,
        user: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Partially updates an account user's role using the Rest.li PARTIAL_UPDATE pattern: the body wraps the fields to change in patch.$set (e.g. {"patch": {"$set": {"role": "CAMPAIGN_MANAGER"}}}). Pass the raw account and user URNs as parameters; they are URL-encoded automatically. Requires the rw_ads OAuth scope and the ACCOUNT_BILLING_ADMIN or ACCOUNT_MANAGER role.


        Args:
            patch: Parameter patch
            account: Sponsored account URN, e.g. urn:li:sponsoredAccount:123456
            user: Person URN, e.g. urn:li:person:abc123
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "patch": patch,
            "account": account,
            "user": user,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("account_users", "update", params)
        return result



    async def create(
        self,
        role: str,
        account: str,
        user: str,
        **kwargs
    ) -> RestliCreateResponse:
        """
        Grants a user a role on an ad account. Note the non-standard Rest.li compound-key shape: this is a PUT (not POST) keyed by both the account and user URNs. Pass the raw URNs as parameters; they are URL-encoded automatically. Requires the rw_ads OAuth scope and the ACCOUNT_BILLING_ADMIN or ACCOUNT_MANAGER role.


        Args:
            role: Role to grant on the ad account
            account: Sponsored account URN, e.g. urn:li:sponsoredAccount:123456
            user: Person URN, e.g. urn:li:person:abc123
            **kwargs: Additional parameters

        Returns:
            RestliCreateResponse
        """
        params = {k: v for k, v in {
            "role": role,
            "account": account,
            "user": user,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("account_users", "create", params)
        return result



    async def delete(
        self,
        account: str,
        user: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Removes a user's role from an ad account. Pass the raw account and user URNs as parameters; they are URL-encoded automatically. Requires the rw_ads OAuth scope and the ACCOUNT_BILLING_ADMIN or ACCOUNT_MANAGER role.


        Args:
            account: Sponsored account URN, e.g. urn:li:sponsoredAccount:123456
            user: Person URN, e.g. urn:li:person:abc123
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "account": account,
            "user": user,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("account_users", "delete", params)
        return result



    async def context_store_search(
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
        - account: The account associated with the user
        - created: The date and time when the user account was created
        - last_modified: The date and time when the user account was last modified
        - role: The role assigned to the user in the account
        - user: The user details including name, email, etc.

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

        result = await self._connector.execute("account_users", "context_store_search", params)

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
            q: LinkedIn API finder method for querying campaigns
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
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        account: str,
        name: str,
        political_intent: str,
        run_schedule: CampaignsCreateParamsRunschedule,
        offsite_delivery_enabled: bool,
        account_id: str,
        campaign_group: str | None = None,
        type: str | None = None,
        objective_type: str | None = None,
        status: str | None = None,
        cost_type: str | None = None,
        daily_budget: CampaignsCreateParamsDailybudget | None = None,
        unit_cost: CampaignsCreateParamsUnitcost | None = None,
        locale: CampaignsCreateParamsLocale | None = None,
        targeting_criteria: dict[str, Any] | None = None,
        audience_expansion_enabled: bool | None = None,
        creative_selection: str | None = None,
        **kwargs
    ) -> CampaignsCreateResult:
        """
        Creates a new campaign in the ad account. Requires the rw_ads OAuth scope and an ad-account role of CAMPAIGN_MANAGER or higher (VIEWER is read-only). The new campaign ID is returned in the x-restli-id response header. Commonly required fields beyond account and name include type, costType, unitCost or dailyBudget, locale, and targetingCriteria; LinkedIn returns a descriptive 400 when a required field is missing.


        Args:
            account: Sponsored account URN; must match the account_id path parameter, e.g. urn:li:sponsoredAccount:123456
            name: Campaign name
            political_intent: Whether the campaign contains political content; LinkedIn requires this on create
            campaign_group: Campaign group URN, e.g. urn:li:sponsoredCampaignGroup:123456
            type: Campaign format
            objective_type: Campaign objective, e.g. BRAND_AWARENESS, WEBSITE_VISIT, LEAD_GENERATION, WEBSITE_CONVERSION, VIDEO_VIEW, ENGAGEMENT, JOB_APPLICANT
            status: Initial campaign status
            cost_type: Bidding cost type, e.g. CPM, CPC, CPV
            daily_budget: Daily budget
            unit_cost: Bid amount per unit (per click, per impression, etc.)
            locale: Campaign locale
            run_schedule: Scheduled run window (epoch milliseconds)
            targeting_criteria: Audience targeting criteria (include/exclude clauses)
            audience_expansion_enabled: Whether audience expansion is enabled
            offsite_delivery_enabled: Whether ads may be served on the LinkedIn Audience Network
            creative_selection: Creative rotation strategy, e.g. ROUND_ROBIN, OPTIMIZED
            account_id: Ad account ID
            **kwargs: Additional parameters

        Returns:
            CampaignsCreateResult
        """
        params = {k: v for k, v in {
            "account": account,
            "name": name,
            "politicalIntent": political_intent,
            "campaignGroup": campaign_group,
            "type": type,
            "objectiveType": objective_type,
            "status": status,
            "costType": cost_type,
            "dailyBudget": daily_budget,
            "unitCost": unit_cost,
            "locale": locale,
            "runSchedule": run_schedule,
            "targetingCriteria": targeting_criteria,
            "audienceExpansionEnabled": audience_expansion_enabled,
            "offsiteDeliveryEnabled": offsite_delivery_enabled,
            "creativeSelection": creative_selection,
            "account_id": account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "create", params)
        # Cast generic envelope to concrete typed result
        return CampaignsCreateResult(
            data=result.data,
            meta=getattr(result, "meta", None)
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



    async def update(
        self,
        patch: CampaignsUpdateParamsPatch,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Partially updates a campaign using the Rest.li PARTIAL_UPDATE pattern: the body wraps the fields to change in patch.$set. Requires the rw_ads OAuth scope and a CAMPAIGN_MANAGER or higher ad-account role. Note that $set on an array field (e.g. targetingCriteria lists) replaces the whole array, so re-send all existing elements. To soft-delete a non-DRAFT campaign, set status to PENDING_DELETION here.


        Args:
            patch: Parameter patch
            account_id: Ad account ID
            id: Campaign ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "patch": patch,
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "update", params)
        return result



    async def delete(
        self,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Hard-deletes a campaign. Only campaigns in DRAFT status accept a true DELETE; for non-DRAFT campaigns LinkedIn requires a soft delete instead - use the update operation to set status to PENDING_DELETION. Requires the rw_ads OAuth scope and a CAMPAIGN_MANAGER or higher ad-account role.


        Args:
            account_id: Ad account ID
            id: Campaign ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "delete", params)
        return result



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
        - targeting_criteria: Criteria for targeting in the campaign.
        - serving_statuses: The serving statuses of the campaign.
        - type_: The type of campaign.
        - locale: The locale settings for the campaign.
        - version: The version information for the campaign.
        - associated_entity: The entity associated with the campaign.
        - run_schedule: The schedule for running the campaign.
        - optimization_target_type: The type of optimization target for the campaign.
        - created: The date and time when the campaign was created.
        - last_modified: The date and time when the campaign was last modified.
        - campaign_group: The group to which the campaign belongs.
        - daily_budget: The daily budget set for the campaign.
        - total_budget: The total budget amount for the campaign.
        - unit_cost: The unit cost for the campaign.
        - creative_selection: Information about the creative selection for the campaign.
        - cost_type: The type of cost associated with the campaign.
        - name: The name of the campaign.
        - offsite_delivery_enabled: Indicates if offsite delivery is enabled for the campaign.
        - id: The unique identifier of the campaign.
        - audience_expansion_enabled: Indicates if audience expansion is enabled for this campaign.
        - test: Indicates if the campaign is a test campaign.
        - account: The account associated with the campaign data.
        - status: The status of the campaign.
        - story_delivery_enabled: Indicates if story delivery is enabled for the campaign.
        - pacing_strategy: The pacing strategy for the campaign.
        - format: The format of the campaign.
        - objective_type: The type of objective for the campaign.
        - offsite_preferences: Preferences related to offsite delivery.

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
            q: LinkedIn API finder method for querying campaign groups
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
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        account: str,
        name: str,
        run_schedule: CampaignGroupsCreateParamsRunschedule,
        account_id: str,
        status: str | None = None,
        total_budget: CampaignGroupsCreateParamsTotalbudget | None = None,
        objective_type: str | None = None,
        **kwargs
    ) -> CampaignGroupsCreateResult:
        """
        Creates a new campaign group in the ad account. Requires the rw_ads OAuth scope and a CAMPAIGN_MANAGER or higher ad-account role. The new campaign group ID is returned in the x-restli-id response header. runSchedule.start is required when creating with ACTIVE status.


        Args:
            account: Sponsored account URN; must match the account_id path parameter, e.g. urn:li:sponsoredAccount:123456
            name: Campaign group name
            status: Initial status
            run_schedule: Scheduled run window (epoch milliseconds)
            total_budget: Total budget across the group's lifetime
            objective_type: Objective shared by campaigns in this group
            account_id: Ad account ID
            **kwargs: Additional parameters

        Returns:
            CampaignGroupsCreateResult
        """
        params = {k: v for k, v in {
            "account": account,
            "name": name,
            "status": status,
            "runSchedule": run_schedule,
            "totalBudget": total_budget,
            "objectiveType": objective_type,
            "account_id": account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_groups", "create", params)
        # Cast generic envelope to concrete typed result
        return CampaignGroupsCreateResult(
            data=result.data,
            meta=getattr(result, "meta", None)
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



    async def update(
        self,
        patch: CampaignGroupsUpdateParamsPatch,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Partially updates a campaign group using the Rest.li PARTIAL_UPDATE pattern: the body wraps the fields to change in patch.$set. Requires the rw_ads OAuth scope and a CAMPAIGN_MANAGER or higher ad-account role. $set on an array field replaces the whole array, so re-send all existing elements. To soft-delete a non-DRAFT campaign group, set status to PENDING_DELETION here.


        Args:
            patch: Parameter patch
            account_id: Ad account ID
            id: Campaign group ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "patch": patch,
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_groups", "update", params)
        return result



    async def delete(
        self,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Hard-deletes a campaign group. Only campaign groups in DRAFT status accept a true DELETE; for non-DRAFT campaign groups LinkedIn requires a soft delete instead - use the update operation to set status to PENDING_DELETION. Requires the rw_ads OAuth scope and a CAMPAIGN_MANAGER or higher ad-account role.


        Args:
            account_id: Ad account ID
            id: Campaign group ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_groups", "delete", params)
        return result



    async def context_store_search(
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
        - run_schedule: Schedule for running the campaign group.
        - created: The date and time when the campaign group was created.
        - last_modified: The date and time when the campaign group was last modified.
        - name: Name of the campaign group.
        - test: Indicates if the campaign group is a test campaign.
        - total_budget: Total budget allocated for the campaign group.
        - serving_statuses: List of serving statuses for the campaign group.
        - backfilled: Indicates if the campaign group was backfilled.
        - id: Unique identifier for the campaign group.
        - account: The account associated with the campaign group.
        - status: Current status of the campaign group.
        - allowed_campaign_types: List of campaign types allowed for this campaign group.

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

        result = await self._connector.execute("campaign_groups", "context_store_search", params)

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
            q: LinkedIn API finder method for querying creatives
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
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        campaign: str,
        account_id: str,
        content: dict[str, Any] | None = None,
        intended_status: str | None = None,
        name: str | None = None,
        **kwargs
    ) -> CreativesCreateResult:
        """
        Creates a new creative in the ad account. Requires the rw_ads OAuth scope and a CREATIVE_MANAGER or higher ad-account role. The new creative URN is returned in the x-restli-id response header. The creative's content must reference existing assets (e.g. a post URN in content.reference for sponsored content).


        Args:
            campaign: Campaign URN the creative belongs to, e.g. urn:li:sponsoredCampaign:123456
            content: Creative content. For sponsored content, reference an existing post URN via content.reference; other formats (textAd, spotlight, jobs) use their own sub-objects per the LinkedIn Creatives API documentation.

            intended_status: Desired serving status
            name: Creative name
            account_id: Ad account ID
            **kwargs: Additional parameters

        Returns:
            CreativesCreateResult
        """
        params = {k: v for k, v in {
            "campaign": campaign,
            "content": content,
            "intendedStatus": intended_status,
            "name": name,
            "account_id": account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creatives", "create", params)
        # Cast generic envelope to concrete typed result
        return CreativesCreateResult(
            data=result.data,
            meta=getattr(result, "meta", None)
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



    async def update(
        self,
        patch: CreativesUpdateParamsPatch,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Partially updates a creative using the Rest.li PARTIAL_UPDATE pattern: the body wraps the fields to change in patch.$set. Only a limited set of creative fields is mutable (e.g. intendedStatus, name, leadgenCallToAction). Requires the rw_ads OAuth scope and a CREATIVE_MANAGER or higher ad-account role. To soft-delete a non-draft creative, set intendedStatus to PENDING_DELETION here.


        Args:
            patch: Parameter patch
            account_id: Ad account ID
            id: Creative URN, e.g. urn:li:sponsoredCreative:123456
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "patch": patch,
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creatives", "update", params)
        return result



    async def delete(
        self,
        account_id: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Hard-deletes a creative. Only creatives in DRAFT intendedStatus (or linked to a draft campaign, or with failed video uploads) accept a true DELETE; LinkedIn uniquely requires the X-RestLi-Method DELETE header on this call. For other creatives, soft-delete via the update operation by setting intendedStatus to PENDING_DELETION. Requires the rw_ads OAuth scope and a CREATIVE_MANAGER or higher ad-account role.


        Args:
            account_id: Ad account ID
            id: Creative URN, e.g. urn:li:sponsoredCreative:123456
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("creatives", "delete", params)
        return result



    async def context_store_search(
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
        - serving_hold_reasons: Reasons for holding the creative from serving.
        - last_modified_at: The timestamp when the creative was last modified.
        - last_modified_by: The user who last modified the creative.
        - content: The actual content of the creative.
        - created_at: The timestamp when the creative was created.
        - is_test: Boolean indicating if the creative is a test creative.
        - created_by: The user who created the creative.
        - review: Review information for the creative.
        - name: The name of the creative.
        - is_serving: Boolean indicating if the creative is currently serving.
        - campaign: The campaign to which the creative belongs.
        - id: The unique identifier of the creative.
        - intended_status: The intended status of the creative.
        - account: The account associated with the creative.
        - leadgen_call_to_action: Call-to-action information for lead generation purposes.

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

        result = await self._connector.execute("creatives", "context_store_search", params)

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
            q: LinkedIn API finder method for querying conversions by account
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
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        account: str,
        name: str,
        type: str,
        attribution_type: str | None = None,
        post_click_attribution_window_size: int | None = None,
        view_through_attribution_window_size: int | None = None,
        enabled: bool | None = None,
        url_match_rule_expression: list[list[dict[str, Any]]] | None = None,
        value: ConversionsCreateParamsValue | None = None,
        auto_association_type: str | None = None,
        **kwargs
    ) -> ConversionsCreateResult:
        """
        Creates a new conversion tracking rule. Conversions API write access is gated behind a separate LinkedIn partner approval - the rw_conversions OAuth scope alone is not sufficient until access is granted. The new conversion ID is returned in the x-restli-id response header. Set autoAssociationType to ALL_CAMPAIGNS to associate the rule with every campaign in the account automatically.


        Args:
            account: Sponsored account URN, e.g. urn:li:sponsoredAccount:123456
            name: Conversion rule name
            type: Conversion category, e.g. LEAD, PURCHASE, SIGN_UP, DOWNLOAD, ADD_TO_CART, INSTALL, KEY_PAGE_VIEW, OTHER
            attribution_type: How conversions are attributed to campaigns
            post_click_attribution_window_size: Post-click attribution window in days (1, 7, 30, or 90)
            view_through_attribution_window_size: View-through attribution window in days (1, 7, or 30)
            enabled: Whether the rule is active
            url_match_rule_expression: URL match rules for page-based conversion tracking
            value: Monetary value assigned to each conversion
            auto_association_type: Set to ALL_CAMPAIGNS to auto-associate with all campaigns in the account
            **kwargs: Additional parameters

        Returns:
            ConversionsCreateResult
        """
        params = {k: v for k, v in {
            "account": account,
            "name": name,
            "type": type,
            "attributionType": attribution_type,
            "postClickAttributionWindowSize": post_click_attribution_window_size,
            "viewThroughAttributionWindowSize": view_through_attribution_window_size,
            "enabled": enabled,
            "urlMatchRuleExpression": url_match_rule_expression,
            "value": value,
            "autoAssociationType": auto_association_type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversions", "create", params)
        # Cast generic envelope to concrete typed result
        return ConversionsCreateResult(
            data=result.data,
            meta=getattr(result, "meta", None)
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



    async def update(
        self,
        patch: ConversionsUpdateParamsPatch,
        account: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Partially updates a conversion rule using the Rest.li PARTIAL_UPDATE pattern: the body wraps the fields to change in patch.$set. The account query parameter is required. Conversion rules have no hard delete - to retire one, soft-disable it here with {"patch": {"$set": {"enabled": false}}}. Conversions API write access is gated behind a separate LinkedIn partner approval.


        Args:
            patch: Parameter patch
            id: Conversion rule ID
            account: Sponsored account URN, e.g. urn:li:sponsoredAccount:123456
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "patch": patch,
            "id": id,
            "account": account,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversions", "update", params)
        return result



    async def context_store_search(
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
        - attribution_type: The type of attribution for the conversion.
        - account: The account associated with the conversion data.
        - campaigns: List of campaigns related to the conversion.
        - created: Timestamp of when the conversion was created.
        - enabled: Flag indicating if the conversion tracking is enabled.
        - id: Unique identifier for the conversion.
        - image_pixel_tag: Pixel tag used for tracking the conversion.
        - name: Name of the conversion.
        - type_: Type of conversion.
        - latest_first_party_callback_at: Timestamp of the latest first-party callback for the conversion.
        - post_click_attribution_window_size: Window size for post-click attribution.
        - view_through_attribution_window_size: Window size for view-through attribution.
        - last_callback_at: Timestamp of the last callback for the conversion.
        - last_modified: Timestamp of the last modification made to the conversion.
        - value: Value associated with the conversion.
        - associated_campaigns: Campaigns associated with the conversion.
        - url_match_rule_expression: Expression used for matching URLs for attribution.
        - url_rules: Rules for URL matching in the conversion.

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

        result = await self._connector.execute("conversions", "context_store_search", params)

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

class ConversionEventsQuery:
    """
    Query class for ConversionEvents entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        elements: list[ConversionEventsCreateParamsElementsItem],
        **kwargs
    ) -> RestliCreateResponse:
        """
        Streams offline conversion events to LinkedIn (Conversions API event ingestion). This is a write-only Rest.li BATCH_CREATE: the body's elements array accepts up to 5,000 events per request. Each event references a conversion rule URN (urn:lla:llaPartnerConversion:{id}) and identifies the converting user by hashed email or other supported ID types. Conversions API access is gated behind a separate LinkedIn partner approval.


        Args:
            elements: Conversion events to ingest
            **kwargs: Additional parameters

        Returns:
            RestliCreateResponse
        """
        params = {k: v for k, v in {
            "elements": elements,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversion_events", "create", params)
        return result



class CampaignConversionsQuery:
    """
    Query class for CampaignConversions entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        campaign_urn: str,
        conversion_urn: str,
        campaign: str | None = None,
        conversion: str | None = None,
        **kwargs
    ) -> RestliCreateResponse:
        """
        Creates a campaign-to-conversion association using the Rest.li compound-key PUT pattern. Pass the raw campaign URN (urn:li:sponsoredCampaign:{id}) and conversion URN (urn:lla:llaPartnerConversion:{id}); they are URL-encoded automatically. Conversions API access is gated behind a separate LinkedIn partner approval.


        Args:
            campaign: Campaign URN, e.g. urn:li:sponsoredCampaign:123456
            conversion: Conversion rule URN, e.g. urn:lla:llaPartnerConversion:123456
            campaign_urn: Campaign URN, e.g. urn:li:sponsoredCampaign:123456
            conversion_urn: Conversion rule URN, e.g. urn:lla:llaPartnerConversion:123456
            **kwargs: Additional parameters

        Returns:
            RestliCreateResponse
        """
        params = {k: v for k, v in {
            "campaign": campaign,
            "conversion": conversion,
            "campaign_urn": campaign_urn,
            "conversion_urn": conversion_urn,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_conversions", "create", params)
        return result



    async def delete(
        self,
        campaign_urn: str,
        conversion_urn: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Deletes a campaign-to-conversion association by its compound key. Pass the raw campaign and conversion URNs; they are URL-encoded automatically. Conversions API access is gated behind a separate LinkedIn partner approval.


        Args:
            campaign_urn: Campaign URN, e.g. urn:li:sponsoredCampaign:123456
            conversion_urn: Conversion rule URN, e.g. urn:lla:llaPartnerConversion:123456
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "campaign_urn": campaign_urn,
            "conversion_urn": conversion_urn,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_conversions", "delete", params)
        return result



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
            q: LinkedIn API finder method for querying ad analytics
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



    async def context_store_search(
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
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

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

        result = await self._connector.execute("ad_campaign_analytics", "context_store_search", params)

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
            q: LinkedIn API finder method for querying ad analytics
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



    async def context_store_search(
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
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_creative: Sponsored creative

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

        result = await self._connector.execute("ad_creative_analytics", "context_store_search", params)

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

class AdImpressionDeviceAnalyticsQuery:
    """
    Query class for AdImpressionDeviceAnalytics entity operations.
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
    ) -> AdImpressionDeviceAnalyticsListResult:
        """
        Returns ad analytics data pivoted by impression device type. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by impression device type.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdImpressionDeviceAnalyticsListResult
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

        result = await self._connector.execute("ad_impression_device_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdImpressionDeviceAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdImpressionDeviceAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdImpressionDeviceAnalyticsSearchResult:
        """
        Search ad_impression_device_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdImpressionDeviceAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdImpressionDeviceAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_impression_device_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdImpressionDeviceAnalyticsSearchResult(
            data=[
                AdImpressionDeviceAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberCompanyAnalyticsQuery:
    """
    Query class for AdMemberCompanyAnalytics entity operations.
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
    ) -> AdMemberCompanyAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member company. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member company.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberCompanyAnalyticsListResult
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

        result = await self._connector.execute("ad_member_company_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberCompanyAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberCompanyAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberCompanyAnalyticsSearchResult:
        """
        Search ad_member_company_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberCompanyAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberCompanyAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_company_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberCompanyAnalyticsSearchResult(
            data=[
                AdMemberCompanyAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberCompanySizeAnalyticsQuery:
    """
    Query class for AdMemberCompanySizeAnalytics entity operations.
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
    ) -> AdMemberCompanySizeAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member company size. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member company size.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberCompanySizeAnalyticsListResult
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

        result = await self._connector.execute("ad_member_company_size_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberCompanySizeAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberCompanySizeAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberCompanySizeAnalyticsSearchResult:
        """
        Search ad_member_company_size_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberCompanySizeAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberCompanySizeAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_company_size_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberCompanySizeAnalyticsSearchResult(
            data=[
                AdMemberCompanySizeAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberCountryAnalyticsQuery:
    """
    Query class for AdMemberCountryAnalytics entity operations.
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
    ) -> AdMemberCountryAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member country. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member country.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberCountryAnalyticsListResult
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

        result = await self._connector.execute("ad_member_country_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberCountryAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberCountryAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberCountryAnalyticsSearchResult:
        """
        Search ad_member_country_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberCountryAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberCountryAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_country_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberCountryAnalyticsSearchResult(
            data=[
                AdMemberCountryAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberIndustryAnalyticsQuery:
    """
    Query class for AdMemberIndustryAnalytics entity operations.
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
    ) -> AdMemberIndustryAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member industry. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member industry.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberIndustryAnalyticsListResult
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

        result = await self._connector.execute("ad_member_industry_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberIndustryAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberIndustryAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberIndustryAnalyticsSearchResult:
        """
        Search ad_member_industry_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberIndustryAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberIndustryAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_industry_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberIndustryAnalyticsSearchResult(
            data=[
                AdMemberIndustryAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberJobFunctionAnalyticsQuery:
    """
    Query class for AdMemberJobFunctionAnalytics entity operations.
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
    ) -> AdMemberJobFunctionAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member job function. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member job function.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberJobFunctionAnalyticsListResult
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

        result = await self._connector.execute("ad_member_job_function_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberJobFunctionAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberJobFunctionAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberJobFunctionAnalyticsSearchResult:
        """
        Search ad_member_job_function_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberJobFunctionAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberJobFunctionAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_job_function_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberJobFunctionAnalyticsSearchResult(
            data=[
                AdMemberJobFunctionAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberJobTitleAnalyticsQuery:
    """
    Query class for AdMemberJobTitleAnalytics entity operations.
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
    ) -> AdMemberJobTitleAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member job title. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member job title.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberJobTitleAnalyticsListResult
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

        result = await self._connector.execute("ad_member_job_title_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberJobTitleAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberJobTitleAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberJobTitleAnalyticsSearchResult:
        """
        Search ad_member_job_title_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberJobTitleAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberJobTitleAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_job_title_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberJobTitleAnalyticsSearchResult(
            data=[
                AdMemberJobTitleAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberRegionAnalyticsQuery:
    """
    Query class for AdMemberRegionAnalytics entity operations.
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
    ) -> AdMemberRegionAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member region. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member region.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberRegionAnalyticsListResult
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

        result = await self._connector.execute("ad_member_region_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberRegionAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberRegionAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberRegionAnalyticsSearchResult:
        """
        Search ad_member_region_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberRegionAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberRegionAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_region_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberRegionAnalyticsSearchResult(
            data=[
                AdMemberRegionAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdMemberSeniorityAnalyticsQuery:
    """
    Query class for AdMemberSeniorityAnalytics entity operations.
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
    ) -> AdMemberSeniorityAnalyticsListResult:
        """
        Returns ad analytics data pivoted by member seniority. Provides performance metrics including clicks, impressions, spend, and engagement data grouped by member seniority.


        Args:
            q: LinkedIn API finder method for querying ad analytics
            pivot: Pivot dimension for analytics grouping
            time_granularity: Time granularity for analytics data
            date_range: Date range in LinkedIn format, e.g. (start:(year:2024,month:1,day:1),end:(year:2024,month:12,day:31))
            campaigns: List of campaign URNs, e.g. List(urn%3Ali%3AsponsoredCampaign%3A123)
            fields: Comma-separated list of metric fields to return
            **kwargs: Additional parameters

        Returns:
            AdMemberSeniorityAnalyticsListResult
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

        result = await self._connector.execute("ad_member_seniority_analytics", "list", params)
        # Cast generic envelope to concrete typed result
        return AdMemberSeniorityAnalyticsListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AdMemberSeniorityAnalyticsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdMemberSeniorityAnalyticsSearchResult:
        """
        Search ad_member_seniority_analytics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdMemberSeniorityAnalyticsSearchFilter):
        - action_clicks: The number of clicks on action buttons in the ad.
        - ad_unit_clicks: The number of clicks on ad unit components.
        - approximate_member_reach: An approximation of unique ad impressions.
        - card_clicks: The number of clicks on interactive card elements.
        - card_impressions: The number of times interactive cards were displayed.
        - clicks: Total number of clicks on the ad.
        - comment_likes: The count of likes on comments related to the ad.
        - comments: The number of comments on the ad.
        - company_page_clicks: Clicks on the company page associated with the ad.
        - conversion_value_in_local_currency: Conversion value in the local currency.
        - cost_in_local_currency: Cost of ad campaign in the local currency.
        - cost_in_usd: Cost of ad campaign in USD.
        - document_completions: Number of completions for document views.
        - document_first_quartile_completions: Completions for first quartile of document views.
        - document_midpoint_completions: Completions for midpoint of document views.
        - document_third_quartile_completions: Completions for third quartile of document views.
        - download_clicks: Clicks on download links in the ad.
        - end_date: End date of the ad analytics data.
        - external_website_conversions: Conversions that lead to external websites.
        - external_website_post_click_conversions: Post-click conversions on external websites.
        - external_website_post_view_conversions: Post-view conversions on external websites.
        - follows: Number of follows generated by the ad.
        - full_screen_plays: Number of times videos were played in fullscreen mode.
        - impressions: Total number of times the ad was displayed.
        - job_applications: Number of job applications initiated through the ad.
        - job_apply_clicks: Clicks on apply job button in the ad.
        - landing_page_clicks: Clicks on the landing page associated with the ad.
        - lead_generation_mail_contact_info_shares: Shares of contact information through lead generation.
        - lead_generation_mail_interested_clicks: Clicks on expressing interest through lead generation mail.
        - likes: Total likes received on the ad.
        - one_click_lead_form_opens: Number of times lead forms were opened in one click.
        - one_click_leads: Leads generated in one click.
        - opens: The number of times the ad was opened or expanded.
        - other_engagements: Engagements other than clicks on the ad.
        - pivot_values: Values used for pivoting the analytics.
        - string_of_pivot_values: Comma-separated string of pivot values for this analytics record
        - post_click_job_applications: Job applications initiated post-clicking on the ad.
        - post_click_job_apply_clicks: Clicks on apply job button post-clicking on the ad.
        - post_click_registrations: Registrations completed post-clicking on the ad.
        - post_view_job_applications: Job applications initiated post-viewing the ad.
        - post_view_job_apply_clicks: Clicks on apply job button post-viewing the ad.
        - post_view_registrations: Registrations completed post-viewing the ad.
        - reactions: Total reactions (e.g., like, love, celebrate) on the ad.
        - registrations: Total registrations completed through the ad.
        - sends: Number of messages sent through the ad.
        - shares: Total shares generated by the ad.
        - start_date: Start date of the ad analytics data.
        - talent_leads: Number of leads related to talent acquisition.
        - text_url_clicks: Clicks on text URLs within the ad.
        - total_engagements: Total number of engagements on the ad.
        - valid_work_email_leads: Leads generated through valid work emails.
        - video_completions: Number of times videos were watched till completion.
        - video_first_quartile_completions: Completions for first quartile of video views.
        - video_midpoint_completions: Completions for midpoint of video views.
        - video_starts: Total video starts initiated by users.
        - video_third_quartile_completions: Completions for third quartile of video views.
        - video_views: Total views of videos in the ad.
        - viral_card_clicks: Clicks on interactive card components in viral distribution.
        - viral_card_impressions: Impressions of interactive cards in viral distribution.
        - viral_clicks: Total clicks in viral distribution of the ad.
        - viral_comment_likes: Likes received on comments in viral distribution.
        - viral_comments: Number of comments in viral distribution of the ad.
        - viral_company_page_clicks: Clicks on the company page in viral distribution.
        - viral_document_completions: Complete views of documents in viral distribution.
        - viral_document_first_quartile_completions: First quartile completions of documents in viral distribution.
        - viral_document_midpoint_completions: Midpoint completions of documents in viral distribution.
        - viral_document_third_quartile_completions: Third quartile completions of documents in viral distribution.
        - viral_download_clicks: Clicks on downloads in viral distribution of the ad.
        - viral_external_website_conversions: External website conversions in viral distribution.
        - viral_external_website_post_click_conversions: Post-click conversions on external websites in viral distribution.
        - viral_external_website_post_view_conversions: Post-view conversions on external websites in viral distribution.
        - viral_follows: Follows generated in viral distribution of the ad.
        - viral_full_screen_plays: Fullscreen video plays in viral distribution.
        - viral_impressions: Total impressions in viral distribution of the ad.
        - viral_job_applications: Job applications initiated in viral distribution.
        - viral_job_apply_clicks: Clicks on apply job button in viral distribution of the ad.
        - viral_landing_page_clicks: Clicks on landing page in viral distribution.
        - viral_likes: Total likes in viral distribution of the ad.
        - viral_one_click_lead_form_opens: One-click lead form opens in viral distribution.
        - viral_one_click_leads: Leads generated in one click in viral distribution.
        - viral_other_engagements: Other engagements in viral distribution of the ad.
        - viral_post_click_job_applications: Job applications initiated post-clicking in viral distribution.
        - viral_post_click_job_apply_clicks: Clicks on apply job button post-clicking in viral distribution.
        - viral_post_click_registrations: Registrations completed post-clicking in viral distribution.
        - viral_post_view_job_applications: Job applications initiated post-viewing in viral distribution.
        - viral_post_view_job_apply_clicks: Clicks on apply job button post-viewing in viral distribution.
        - viral_post_view_registrations: Registrations completed post-viewing in viral distribution.
        - viral_reactions: Total reactions in viral distribution of the ad.
        - viral_registrations: Total registrations in viral distribution of the ad.
        - viral_shares: Total shares in viral distribution of the ad.
        - viral_total_engagements: Total engagements in viral distribution of the ad.
        - viral_video_completions: Completions of videos in viral distribution.
        - viral_video_first_quartile_completions: First quartile completions of videos in viral distribution.
        - viral_video_midpoint_completions: Midpoint completions of videos in viral distribution.
        - viral_video_starts: Total video starts in viral distribution of the ad.
        - viral_video_third_quartile_completions: Third quartile completions of videos in viral distribution.
        - viral_video_views: Total views of videos in viral distribution of the ad.
        - pivot: Pivot dimension used for this analytics record
        - sponsored_campaign: URN of the sponsored campaign this analytics record belongs to

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdMemberSeniorityAnalyticsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_member_seniority_analytics", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdMemberSeniorityAnalyticsSearchResult(
            data=[
                AdMemberSeniorityAnalyticsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class LeadFormsQuery:
    """
    Query class for LeadForms entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        owner: str,
        count: int | None = None,
        start: int | None = None,
        **kwargs
    ) -> LeadFormsListResult:
        """
        Returns a list of lead generation forms owned by a sponsored ad account

        Args:
            q: LinkedIn API finder method for querying lead forms by owner
            owner: Owner of the lead forms, e.g. (sponsoredAccount:urn%3Ali%3AsponsoredAccount%3A123456)
            count: Number of items per page
            start: Offset for pagination
            **kwargs: Additional parameters

        Returns:
            LeadFormsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "owner": owner,
            "count": count,
            "start": start,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lead_forms", "list", params)
        # Cast generic envelope to concrete typed result
        return LeadFormsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: LeadFormsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LeadFormsSearchResult:
        """
        Search lead_forms records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LeadFormsSearchFilter):
        - id: Numerical identifier for the form.
        - name: Name of the Lead Form provided by the owner.
        - owner: URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.

        - state: Information about the current state of the Lead Form.
        - content: Content of the Lead Form which will be displayed to the viewer.
        - created: An epoch time corresponding to the creation of the form.
        - last_modified: An epoch time corresponding to the last modified of of the form.
        - creation_locale: Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.

        - hidden_fields: Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.

        - review_info: Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.

        - version_id: The version ID of the form. This is a derived field and is generated on the server side.
        - version_tag: The number of times the form has been modified.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LeadFormsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("lead_forms", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LeadFormsSearchResult(
            data=[
                LeadFormsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class LeadFormResponsesQuery:
    """
    Query class for LeadFormResponses entity operations.
    """

    def __init__(self, connector: LinkedinAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        owner: str,
        lead_type: str,
        count: int | None = None,
        start: int | None = None,
        **kwargs
    ) -> LeadFormResponsesListResult:
        """
        Returns a list of lead form responses submitted to forms owned by a sponsored ad account

        Args:
            q: LinkedIn API finder method for querying lead form responses by owner
            owner: Owner of the lead form responses, e.g. (sponsoredAccount:urn%3Ali%3AsponsoredAccount%3A123456)
            lead_type: Type of leads to return, e.g. (leadType:SPONSORED)
            count: Number of items per page
            start: Offset for pagination
            **kwargs: Additional parameters

        Returns:
            LeadFormResponsesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            "owner": owner,
            "leadType": lead_type,
            "count": count,
            "start": start,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lead_form_responses", "list", params)
        # Cast generic envelope to concrete typed result
        return LeadFormResponsesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: LeadFormResponsesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LeadFormResponsesSearchResult:
        """
        Search lead_form_responses records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LeadFormResponsesSearchFilter):
        - id: Unique id to identify the Lead Form Response.
        - lead_type: Type of the lead representing the origination of the lead.
        - form: URN identifying which form this FormResponse belongs to.
        - owner: Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.

        - owner_info: Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo.
        - lead_metadata: Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned.
        - lead_metadata_info: Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned.
        - associated_entity: URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned.
        - associated_entity_info: Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned.
        - submitted_at: An epoch timestamp that recording when the form response was submitted.
        - response_id: The unique identifier for the form response generated in the front-end when a submitter submits the response.
        - form_response: Answers provided by the form submitter.
        - test_lead: Whether this is a test lead created for testing purposes.
        - submitter: From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes

        - versioned_lead_gen_form_urn: URN identifying which form this FormResponse belongs to.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LeadFormResponsesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("lead_form_responses", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LeadFormResponsesSearchResult(
            data=[
                LeadFormResponsesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
