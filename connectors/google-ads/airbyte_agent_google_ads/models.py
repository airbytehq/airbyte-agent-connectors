"""
Pydantic models for google-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class GoogleAdsAuthConfig(BaseModel):
    """OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """OAuth2 client ID from Google Cloud Console"""
    client_secret: str
    """OAuth2 client secret from Google Cloud Console"""
    refresh_token: str
    """OAuth2 refresh token"""
    developer_token: str
    """Google Ads API developer token"""

# Replication configuration

class GoogleAdsReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Google Ads."""

    model_config = ConfigDict(extra="forbid")

    customer_id: str
    """Comma-separated list of Google Ads customer IDs (10 digits each, no dashes)."""
    start_date: Optional[str] = None
    """UTC date in YYYY-MM-DD format from which to start replicating data. Defaults to 2 years ago if not specified."""
    conversion_window_days: Optional[int] = None
    """Number of days for the conversion attribution window. Default is 14."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class AccessibleCustomerResourceName(BaseModel):
    """Resource name of an accessible customer (e.g., customers/1234567890)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pass

class AccessibleCustomersList(BaseModel):
    """List of accessible customer resource names"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_names: Union[list[AccessibleCustomerResourceName], Any] = Field(default=None, alias="resourceNames")

class AccountCustomerConversiontrackingsetting(BaseModel):
    """Nested schema for AccountCustomer.conversionTrackingSetting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conversion_tracking_id: Union[str, Any] = Field(default=None, alias="conversionTrackingId")
    cross_account_conversion_tracking_id: Union[str, Any] = Field(default=None, alias="crossAccountConversionTrackingId")

class AccountCustomerCallreportingsetting(BaseModel):
    """Nested schema for AccountCustomer.callReportingSetting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_conversion_action: Union[str, Any] = Field(default=None, alias="callConversionAction")
    call_conversion_reporting_enabled: Union[bool, Any] = Field(default=None, alias="callConversionReportingEnabled")
    call_reporting_enabled: Union[bool, Any] = Field(default=None, alias="callReportingEnabled")

class AccountCustomerRemarketingsetting(BaseModel):
    """Nested schema for AccountCustomer.remarketingSetting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    google_global_site_tag: Union[str, Any] = Field(default=None, alias="googleGlobalSiteTag")

class AccountCustomer(BaseModel):
    """Nested schema for Account.customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auto_tagging_enabled: Union[bool, Any] = Field(default=None, alias="autoTaggingEnabled", description="Whether auto-tagging is enabled")
    """Whether auto-tagging is enabled"""
    call_reporting_setting: Union[AccountCustomerCallreportingsetting, Any] = Field(default=None, alias="callReportingSetting")
    conversion_tracking_setting: Union[AccountCustomerConversiontrackingsetting, Any] = Field(default=None, alias="conversionTrackingSetting")
    currency_code: Union[str, Any] = Field(default=None, alias="currencyCode", description="Currency code (e.g., USD)")
    """Currency code (e.g., USD)"""
    descriptive_name: Union[str, Any] = Field(default=None, alias="descriptiveName", description="Account descriptive name")
    """Account descriptive name"""
    final_url_suffix: Union[str, Any] = Field(default=None, alias="finalUrlSuffix")
    has_partners_badge: Union[bool, Any] = Field(default=None, alias="hasPartnersBadge")
    id: Union[str, Any] = Field(default=None, description="Customer ID")
    """Customer ID"""
    manager: Union[bool, Any] = Field(default=None, description="Whether this is a manager account")
    """Whether this is a manager account"""
    optimization_score: Union[float, Any] = Field(default=None, alias="optimizationScore")
    optimization_score_weight: Union[float, Any] = Field(default=None, alias="optimizationScoreWeight")
    pay_per_conversion_eligibility_failure_reasons: Union[list[str], Any] = Field(default=None, alias="payPerConversionEligibilityFailureReasons")
    remarketing_setting: Union[AccountCustomerRemarketingsetting, Any] = Field(default=None, alias="remarketingSetting")
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName", description="Resource name of the customer")
    """Resource name of the customer"""
    test_account: Union[bool, Any] = Field(default=None, alias="testAccount")
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    tracking_url_template: Union[str, Any] = Field(default=None, alias="trackingUrlTemplate")

class Account(BaseModel):
    """Google Ads customer account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer: Union[AccountCustomer, Any] = Field(default=None)

class AccountSearchResponse(BaseModel):
    """Search response containing account data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Account], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

class CampaignMetrics(BaseModel):
    """Nested schema for Campaign.metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    clicks: Union[str, Any] = Field(default=None)
    ctr: Union[float, Any] = Field(default=None)
    conversions: Union[float, Any] = Field(default=None)
    conversions_value: Union[float, Any] = Field(default=None, alias="conversionsValue")
    cost_micros: Union[str, Any] = Field(default=None, alias="costMicros")
    impressions: Union[str, Any] = Field(default=None)
    average_cpc: Union[float, Any] = Field(default=None, alias="averageCpc")
    average_cpm: Union[float, Any] = Field(default=None, alias="averageCpm")
    interactions: Union[str, Any] = Field(default=None)

class CampaignCampaignbudget(BaseModel):
    """Nested schema for Campaign.campaignBudget"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: Union[str, Any] = Field(default=None, alias="resourceName", description="Resource name of the campaign budget")
    """Resource name of the campaign budget"""
    amount_micros: Union[str, Any] = Field(default=None, alias="amountMicros", description="Budget amount in micros")
    """Budget amount in micros"""

class CampaignSegments(BaseModel):
    """Nested schema for Campaign.segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: Union[str, Any] = Field(default=None, description="Date in YYYY-MM-DD format")
    """Date in YYYY-MM-DD format"""

class CampaignCampaignNetworksettings(BaseModel):
    """Nested schema for CampaignCampaign.networkSettings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target_google_search: Union[bool, Any] = Field(default=None, alias="targetGoogleSearch")
    target_search_network: Union[bool, Any] = Field(default=None, alias="targetSearchNetwork")
    target_content_network: Union[bool, Any] = Field(default=None, alias="targetContentNetwork")
    target_partner_search_network: Union[bool, Any] = Field(default=None, alias="targetPartnerSearchNetwork")

class CampaignCampaign(BaseModel):
    """Nested schema for Campaign.campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Campaign ID")
    """Campaign ID"""
    name: Union[str, Any] = Field(default=None, description="Campaign name")
    """Campaign name"""
    status: Union[str, Any] = Field(default=None, description="Campaign status")
    """Campaign status"""
    advertising_channel_type: Union[str, Any] = Field(default=None, alias="advertisingChannelType", description="Primary channel type")
    """Primary channel type"""
    advertising_channel_sub_type: Union[str, Any] = Field(default=None, alias="advertisingChannelSubType")
    bidding_strategy: Union[str, Any] = Field(default=None, alias="biddingStrategy")
    bidding_strategy_type: Union[str, Any] = Field(default=None, alias="biddingStrategyType")
    campaign_budget: Union[str, Any] = Field(default=None, alias="campaignBudget", description="Campaign budget resource name")
    """Campaign budget resource name"""
    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Campaign start date")
    """Campaign start date"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="Campaign end date")
    """Campaign end date"""
    serving_status: Union[str, Any] = Field(default=None, alias="servingStatus")
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")
    labels: Union[list[str], Any] = Field(default=None)
    network_settings: Union[CampaignCampaignNetworksettings, Any] = Field(default=None, alias="networkSettings")

class Campaign(BaseModel):
    """Google Ads campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: Union[CampaignCampaign, Any] = Field(default=None)
    campaign_budget: Union[CampaignCampaignbudget, Any] = Field(default=None, alias="campaignBudget")
    metrics: Union[CampaignMetrics, Any] = Field(default=None)
    segments: Union[CampaignSegments, Any] = Field(default=None)

class CampaignSearchResponse(BaseModel):
    """Search response containing campaign data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Campaign], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

class AdGroupMetrics(BaseModel):
    """Nested schema for AdGroup.metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cost_micros: Union[str, Any] = Field(default=None, alias="costMicros")

class AdGroupAdgroup(BaseModel):
    """Nested schema for AdGroup.adGroup"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Ad group ID")
    """Ad group ID"""
    name: Union[str, Any] = Field(default=None, description="Ad group name")
    """Ad group name"""
    status: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    ad_rotation_mode: Union[str, Any] = Field(default=None, alias="adRotationMode")
    base_ad_group: Union[str, Any] = Field(default=None, alias="baseAdGroup")
    campaign: Union[str, Any] = Field(default=None, description="Parent campaign resource name")
    """Parent campaign resource name"""
    cpc_bid_micros: Union[str, Any] = Field(default=None, alias="cpcBidMicros")
    cpm_bid_micros: Union[str, Any] = Field(default=None, alias="cpmBidMicros")
    cpv_bid_micros: Union[str, Any] = Field(default=None, alias="cpvBidMicros")
    effective_target_cpa_micros: Union[str, Any] = Field(default=None, alias="effectiveTargetCpaMicros")
    effective_target_cpa_source: Union[str, Any] = Field(default=None, alias="effectiveTargetCpaSource")
    effective_target_roas: Union[float, Any] = Field(default=None, alias="effectiveTargetRoas")
    effective_target_roas_source: Union[str, Any] = Field(default=None, alias="effectiveTargetRoasSource")
    labels: Union[list[str], Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")
    target_cpa_micros: Union[str, Any] = Field(default=None, alias="targetCpaMicros")
    target_roas: Union[float, Any] = Field(default=None, alias="targetRoas")
    tracking_url_template: Union[str, Any] = Field(default=None, alias="trackingUrlTemplate")

class AdGroupCampaign(BaseModel):
    """Nested schema for AdGroup.campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Parent campaign ID")
    """Parent campaign ID"""
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName", description="Parent campaign resource name")
    """Parent campaign resource name"""

class AdGroupSegments(BaseModel):
    """Nested schema for AdGroup.segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: Union[str, Any] = Field(default=None)

class AdGroup(BaseModel):
    """Google Ads ad group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: Union[AdGroupCampaign, Any] = Field(default=None)
    ad_group: Union[AdGroupAdgroup, Any] = Field(default=None, alias="adGroup")
    metrics: Union[AdGroupMetrics, Any] = Field(default=None)
    segments: Union[AdGroupSegments, Any] = Field(default=None)

class AdGroupSearchResponse(BaseModel):
    """Search response containing ad group data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[AdGroup], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

class AdGroupAdAdgroupadPolicysummary(BaseModel):
    """Nested schema for AdGroupAdAdgroupad.policySummary"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    approval_status: Union[str, Any] = Field(default=None, alias="approvalStatus")
    review_status: Union[str, Any] = Field(default=None, alias="reviewStatus")

class AdGroupAdAdgroupadAd(BaseModel):
    """Nested schema for AdGroupAdAdgroupad.ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Ad ID")
    """Ad ID"""
    name: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    display_url: Union[str, Any] = Field(default=None, alias="displayUrl")
    final_urls: Union[list[str], Any] = Field(default=None, alias="finalUrls")
    final_mobile_urls: Union[list[str], Any] = Field(default=None, alias="finalMobileUrls")
    final_url_suffix: Union[str, Any] = Field(default=None, alias="finalUrlSuffix")
    tracking_url_template: Union[str, Any] = Field(default=None, alias="trackingUrlTemplate")
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class AdGroupAdAdgroupad(BaseModel):
    """Nested schema for AdGroupAd.adGroupAd"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad: Union[AdGroupAdAdgroupadAd, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    ad_strength: Union[str, Any] = Field(default=None, alias="adStrength")
    ad_group: Union[str, Any] = Field(default=None, alias="adGroup")
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")
    labels: Union[list[str], Any] = Field(default=None)
    policy_summary: Union[AdGroupAdAdgroupadPolicysummary, Any] = Field(default=None, alias="policySummary")

class AdGroupAdAdgroup(BaseModel):
    """Nested schema for AdGroupAd.adGroup"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Parent ad group ID")
    """Parent ad group ID"""
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName", description="Parent ad group resource name")
    """Parent ad group resource name"""

class AdGroupAdSegments(BaseModel):
    """Nested schema for AdGroupAd.segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: Union[str, Any] = Field(default=None)

class AdGroupAd(BaseModel):
    """Google Ads ad group ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: Union[AdGroupAdAdgroup, Any] = Field(default=None, alias="adGroup")
    ad_group_ad: Union[AdGroupAdAdgroupad, Any] = Field(default=None, alias="adGroupAd")
    segments: Union[AdGroupAdSegments, Any] = Field(default=None)

class AdGroupAdSearchResponse(BaseModel):
    """Search response containing ad group ad data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[AdGroupAd], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

class CampaignLabelCampaignlabel(BaseModel):
    """Nested schema for CampaignLabel.campaignLabel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: Union[str, Any] = Field(default=None)
    label: Union[str, Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class CampaignLabelLabel(BaseModel):
    """Nested schema for CampaignLabel.label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class CampaignLabelCampaign(BaseModel):
    """Nested schema for CampaignLabel.campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)

class CampaignLabel(BaseModel):
    """Campaign label association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: Union[CampaignLabelCampaign, Any] = Field(default=None)
    campaign_label: Union[CampaignLabelCampaignlabel, Any] = Field(default=None, alias="campaignLabel")
    label: Union[CampaignLabelLabel, Any] = Field(default=None)

class CampaignLabelSearchResponse(BaseModel):
    """Search response containing campaign label data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[CampaignLabel], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

class AdGroupLabelAdgrouplabel(BaseModel):
    """Nested schema for AdGroupLabel.adGroupLabel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: Union[str, Any] = Field(default=None, alias="adGroup")
    label: Union[str, Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class AdGroupLabelAdgroup(BaseModel):
    """Nested schema for AdGroupLabel.adGroup"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)

class AdGroupLabelLabel(BaseModel):
    """Nested schema for AdGroupLabel.label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class AdGroupLabel(BaseModel):
    """Ad group label association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: Union[AdGroupLabelAdgroup, Any] = Field(default=None, alias="adGroup")
    ad_group_label: Union[AdGroupLabelAdgrouplabel, Any] = Field(default=None, alias="adGroupLabel")
    label: Union[AdGroupLabelLabel, Any] = Field(default=None)

class AdGroupLabelSearchResponse(BaseModel):
    """Search response containing ad group label data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[AdGroupLabel], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

class AdGroupAdLabelLabel(BaseModel):
    """Nested schema for AdGroupAdLabel.label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class AdGroupAdLabelAdgroupadlabel(BaseModel):
    """Nested schema for AdGroupAdLabel.adGroupAdLabel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group_ad: Union[str, Any] = Field(default=None, alias="adGroupAd")
    label: Union[str, Any] = Field(default=None)
    resource_name: Union[str, Any] = Field(default=None, alias="resourceName")

class AdGroupAdLabelAdgroupadAd(BaseModel):
    """Nested schema for AdGroupAdLabelAdgroupad.ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)

class AdGroupAdLabelAdgroupad(BaseModel):
    """Nested schema for AdGroupAdLabel.adGroupAd"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad: Union[AdGroupAdLabelAdgroupadAd, Any] = Field(default=None)

class AdGroupAdLabel(BaseModel):
    """Ad group ad label association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group_ad: Union[AdGroupAdLabelAdgroupad, Any] = Field(default=None, alias="adGroupAd")
    ad_group_ad_label: Union[AdGroupAdLabelAdgroupadlabel, Any] = Field(default=None, alias="adGroupAdLabel")
    label: Union[AdGroupAdLabelLabel, Any] = Field(default=None)

class AdGroupAdLabelSearchResponse(BaseModel):
    """Search response containing ad group ad label data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[AdGroupAdLabel], Any] = Field(default=None)
    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")
    field_mask: Union[str, Any] = Field(default=None, alias="fieldMask")
    query_resource_consumption: Union[str, Any] = Field(default=None, alias="queryResourceConsumption")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

class AdGroupsListResultMeta(BaseModel):
    """Metadata for ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

class AdGroupAdsListResultMeta(BaseModel):
    """Metadata for ad_group_ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

class CampaignLabelsListResultMeta(BaseModel):
    """Metadata for campaign_labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

class AdGroupLabelsListResultMeta(BaseModel):
    """Metadata for ad_group_labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

class AdGroupAdLabelsListResultMeta(BaseModel):
    """Metadata for ad_group_ad_labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class GoogleAdsCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class GoogleAdsExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GoogleAdsExecuteResultWithMeta(GoogleAdsExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    customer_auto_tagging_enabled: bool | None = None
    """Whether auto-tagging is enabled for the account"""
    customer_call_reporting_setting_call_conversion_action: str | None = None
    """Call conversion action resource name"""
    customer_call_reporting_setting_call_conversion_reporting_enabled: bool | None = None
    """Whether call conversion reporting is enabled"""
    customer_call_reporting_setting_call_reporting_enabled: bool | None = None
    """Whether call reporting is enabled"""
    customer_conversion_tracking_setting_conversion_tracking_id: int | None = None
    """Conversion tracking ID"""
    customer_conversion_tracking_setting_cross_account_conversion_tracking_id: int | None = None
    """Cross-account conversion tracking ID"""
    customer_currency_code: str | None = None
    """Currency code for the account (e.g., USD)"""
    customer_descriptive_name: str | None = None
    """Descriptive name of the customer account"""
    customer_final_url_suffix: str | None = None
    """URL suffix appended to final URLs"""
    customer_has_partners_badge: bool | None = None
    """Whether the account has a Google Partners badge"""
    customer_id: int | None = None
    """Unique customer account ID"""
    customer_manager: bool | None = None
    """Whether this is a manager (MCC) account"""
    customer_optimization_score: float | None = None
    """Optimization score for the account (0.0 to 1.0)"""
    customer_optimization_score_weight: float | None = None
    """Weight of the optimization score"""
    customer_pay_per_conversion_eligibility_failure_reasons: list[Any] | None = None
    """Reasons why pay-per-conversion is not eligible"""
    customer_remarketing_setting_google_global_site_tag: str | None = None
    """Google global site tag snippet"""
    customer_resource_name: str | None = None
    """Resource name of the customer"""
    customer_test_account: bool | None = None
    """Whether this is a test account"""
    customer_time_zone: str | None = None
    """Time zone of the account"""
    customer_tracking_url_template: str | None = None
    """Tracking URL template for the account"""
    segments_date: str | None = None
    """Date segment for the report row"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    campaign_id: int | None = None
    """Campaign ID"""
    campaign_name: str | None = None
    """Campaign name"""
    campaign_status: str | None = None
    """Campaign status (ENABLED, PAUSED, REMOVED)"""
    campaign_advertising_channel_type: str | None = None
    """Advertising channel type (SEARCH, DISPLAY, etc.)"""
    campaign_advertising_channel_sub_type: str | None = None
    """Advertising channel sub-type"""
    campaign_bidding_strategy: str | None = None
    """Bidding strategy resource name"""
    campaign_bidding_strategy_type: str | None = None
    """Bidding strategy type"""
    campaign_campaign_budget: str | None = None
    """Campaign budget resource name"""
    campaign_budget_amount_micros: int | None = None
    """Campaign budget amount in micros"""
    campaign_start_date: str | None = None
    """Campaign start date"""
    campaign_end_date: str | None = None
    """Campaign end date"""
    campaign_serving_status: str | None = None
    """Campaign serving status"""
    campaign_resource_name: str | None = None
    """Resource name of the campaign"""
    campaign_labels: list[Any] | None = None
    """Labels applied to the campaign"""
    campaign_network_settings_target_google_search: bool | None = None
    """Whether targeting Google Search"""
    campaign_network_settings_target_search_network: bool | None = None
    """Whether targeting search network"""
    campaign_network_settings_target_content_network: bool | None = None
    """Whether targeting content network"""
    campaign_network_settings_target_partner_search_network: bool | None = None
    """Whether targeting partner search network"""
    metrics_clicks: int | None = None
    """Number of clicks"""
    metrics_ctr: float | None = None
    """Click-through rate"""
    metrics_conversions: float | None = None
    """Number of conversions"""
    metrics_conversions_value: float | None = None
    """Total conversions value"""
    metrics_cost_micros: int | None = None
    """Cost in micros"""
    metrics_impressions: int | None = None
    """Number of impressions"""
    metrics_average_cpc: float | None = None
    """Average cost per click"""
    metrics_average_cpm: float | None = None
    """Average cost per thousand impressions"""
    metrics_interactions: int | None = None
    """Number of interactions"""
    segments_date: str | None = None
    """Date segment for the report row"""
    segments_hour: int | None = None
    """Hour segment"""
    segments_ad_network_type: str | None = None
    """Ad network type segment"""


class AdGroupsSearchData(BaseModel):
    """Search result data for ad_groups entity."""
    model_config = ConfigDict(extra="allow")

    campaign_id: int | None = None
    """Parent campaign ID"""
    ad_group_id: int | None = None
    """Ad group ID"""
    ad_group_name: str | None = None
    """Ad group name"""
    ad_group_status: str | None = None
    """Ad group status (ENABLED, PAUSED, REMOVED)"""
    ad_group_type: str | None = None
    """Ad group type"""
    ad_group_ad_rotation_mode: str | None = None
    """Ad rotation mode"""
    ad_group_base_ad_group: str | None = None
    """Base ad group resource name"""
    ad_group_campaign: str | None = None
    """Parent campaign resource name"""
    ad_group_cpc_bid_micros: int | None = None
    """CPC bid in micros"""
    ad_group_cpm_bid_micros: int | None = None
    """CPM bid in micros"""
    ad_group_cpv_bid_micros: int | None = None
    """CPV bid in micros"""
    ad_group_effective_target_cpa_micros: int | None = None
    """Effective target CPA in micros"""
    ad_group_effective_target_cpa_source: str | None = None
    """Source of the effective target CPA"""
    ad_group_effective_target_roas: float | None = None
    """Effective target ROAS"""
    ad_group_effective_target_roas_source: str | None = None
    """Source of the effective target ROAS"""
    ad_group_labels: list[Any] | None = None
    """Labels applied to the ad group"""
    ad_group_resource_name: str | None = None
    """Resource name of the ad group"""
    ad_group_target_cpa_micros: int | None = None
    """Target CPA in micros"""
    ad_group_target_roas: float | None = None
    """Target ROAS"""
    ad_group_tracking_url_template: str | None = None
    """Tracking URL template"""
    metrics_cost_micros: int | None = None
    """Cost in micros"""
    segments_date: str | None = None
    """Date segment for the report row"""


class AdGroupAdsSearchData(BaseModel):
    """Search result data for ad_group_ads entity."""
    model_config = ConfigDict(extra="allow")

    ad_group_id: int | None = None
    """Parent ad group ID"""
    ad_group_ad_ad_id: int | None = None
    """Ad ID"""
    ad_group_ad_ad_name: str | None = None
    """Ad name"""
    ad_group_ad_ad_type: str | None = None
    """Ad type"""
    ad_group_ad_status: str | None = None
    """Ad group ad status (ENABLED, PAUSED, REMOVED)"""
    ad_group_ad_ad_strength: str | None = None
    """Ad strength rating"""
    ad_group_ad_ad_display_url: str | None = None
    """Display URL of the ad"""
    ad_group_ad_ad_final_urls: list[Any] | None = None
    """Final URLs for the ad"""
    ad_group_ad_ad_final_mobile_urls: list[Any] | None = None
    """Final mobile URLs for the ad"""
    ad_group_ad_ad_final_url_suffix: str | None = None
    """Final URL suffix"""
    ad_group_ad_ad_tracking_url_template: str | None = None
    """Tracking URL template"""
    ad_group_ad_ad_resource_name: str | None = None
    """Resource name of the ad"""
    ad_group_ad_ad_group: str | None = None
    """Ad group resource name"""
    ad_group_ad_resource_name: str | None = None
    """Resource name of the ad group ad"""
    ad_group_ad_labels: list[Any] | None = None
    """Labels applied to the ad group ad"""
    ad_group_ad_policy_summary_approval_status: str | None = None
    """Policy approval status"""
    ad_group_ad_policy_summary_review_status: str | None = None
    """Policy review status"""
    segments_date: str | None = None
    """Date segment for the report row"""


class CampaignLabelsSearchData(BaseModel):
    """Search result data for campaign_labels entity."""
    model_config = ConfigDict(extra="allow")

    campaign_id: int | None = None
    """Campaign ID"""
    campaign_label_campaign: str | None = None
    """Campaign resource name"""
    campaign_label_label: str | None = None
    """Label resource name"""
    campaign_label_resource_name: str | None = None
    """Resource name of the campaign label"""
    label_id: int | None = None
    """Label ID"""
    label_name: str | None = None
    """Label name"""
    label_resource_name: str | None = None
    """Resource name of the label"""


class AdGroupLabelsSearchData(BaseModel):
    """Search result data for ad_group_labels entity."""
    model_config = ConfigDict(extra="allow")

    ad_group_id: int | None = None
    """Ad group ID"""
    ad_group_label_ad_group: str | None = None
    """Ad group resource name"""
    ad_group_label_label: str | None = None
    """Label resource name"""
    ad_group_label_resource_name: str | None = None
    """Resource name of the ad group label"""
    label_id: int | None = None
    """Label ID"""
    label_name: str | None = None
    """Label name"""
    label_resource_name: str | None = None
    """Resource name of the label"""


class AdGroupAdLabelsSearchData(BaseModel):
    """Search result data for ad_group_ad_labels entity."""
    model_config = ConfigDict(extra="allow")

    ad_group_ad_ad_id: int | None = None
    """Ad ID"""
    ad_group_ad_label_ad_group_ad: str | None = None
    """Ad group ad resource name"""
    ad_group_ad_label_label: str | None = None
    """Label resource name"""
    ad_group_ad_label_resource_name: str | None = None
    """Resource name of the ad group ad label"""
    label_id: int | None = None
    """Label ID"""
    label_name: str | None = None
    """Label name"""
    label_resource_name: str | None = None
    """Resource name of the label"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

AccountsSearchResult = AirbyteSearchResult[AccountsSearchData]
"""Search result type for accounts entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

AdGroupsSearchResult = AirbyteSearchResult[AdGroupsSearchData]
"""Search result type for ad_groups entity."""

AdGroupAdsSearchResult = AirbyteSearchResult[AdGroupAdsSearchData]
"""Search result type for ad_group_ads entity."""

CampaignLabelsSearchResult = AirbyteSearchResult[CampaignLabelsSearchData]
"""Search result type for campaign_labels entity."""

AdGroupLabelsSearchResult = AirbyteSearchResult[AdGroupLabelsSearchData]
"""Search result type for ad_group_labels entity."""

AdGroupAdLabelsSearchResult = AirbyteSearchResult[AdGroupAdLabelsSearchData]
"""Search result type for ad_group_ad_labels entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AccessibleCustomersListResult = GoogleAdsExecuteResult[AccessibleCustomersList]
"""Result type for accessible_customers.list operation."""

AccountsListResult = GoogleAdsExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

CampaignsListResult = GoogleAdsExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

AdGroupsListResult = GoogleAdsExecuteResultWithMeta[list[AdGroup], AdGroupsListResultMeta]
"""Result type for ad_groups.list operation with data and metadata."""

AdGroupAdsListResult = GoogleAdsExecuteResultWithMeta[list[AdGroupAd], AdGroupAdsListResultMeta]
"""Result type for ad_group_ads.list operation with data and metadata."""

CampaignLabelsListResult = GoogleAdsExecuteResultWithMeta[list[CampaignLabel], CampaignLabelsListResultMeta]
"""Result type for campaign_labels.list operation with data and metadata."""

AdGroupLabelsListResult = GoogleAdsExecuteResultWithMeta[list[AdGroupLabel], AdGroupLabelsListResultMeta]
"""Result type for ad_group_labels.list operation with data and metadata."""

AdGroupAdLabelsListResult = GoogleAdsExecuteResultWithMeta[list[AdGroupAdLabel], AdGroupAdLabelsListResultMeta]
"""Result type for ad_group_ad_labels.list operation with data and metadata."""

