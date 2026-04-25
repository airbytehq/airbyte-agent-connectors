"""
Pydantic models for google-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
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

class AccessibleCustomersList(BaseModel):
    """List of accessible customer resource names"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_names: list[str] | None = Field(default=None, alias="resourceNames")

class AccountCustomerConversiontrackingsetting(BaseModel):
    """Nested schema for AccountCustomer.conversionTrackingSetting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conversion_tracking_id: str | None = Field(default=None, alias="conversionTrackingId")
    cross_account_conversion_tracking_id: str | None = Field(default=None, alias="crossAccountConversionTrackingId")

class AccountCustomerRemarketingsetting(BaseModel):
    """Nested schema for AccountCustomer.remarketingSetting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    google_global_site_tag: str | None = Field(default=None, alias="googleGlobalSiteTag")

class AccountCustomerCallreportingsetting(BaseModel):
    """Nested schema for AccountCustomer.callReportingSetting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_conversion_action: str | None = Field(default=None, alias="callConversionAction")
    call_conversion_reporting_enabled: bool | None = Field(default=None, alias="callConversionReportingEnabled")
    call_reporting_enabled: bool | None = Field(default=None, alias="callReportingEnabled")

class AccountCustomer(BaseModel):
    """Nested schema for Account.customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auto_tagging_enabled: bool | None = Field(default=None, alias="autoTaggingEnabled", description="Whether auto-tagging is enabled")
    """Whether auto-tagging is enabled"""
    call_reporting_setting: AccountCustomerCallreportingsetting | None = Field(default=None, alias="callReportingSetting")
    conversion_tracking_setting: AccountCustomerConversiontrackingsetting | None = Field(default=None, alias="conversionTrackingSetting")
    currency_code: str | None = Field(default=None, alias="currencyCode", description="Currency code (e.g., USD)")
    """Currency code (e.g., USD)"""
    descriptive_name: str | None = Field(default=None, alias="descriptiveName", description="Account descriptive name")
    """Account descriptive name"""
    final_url_suffix: str | None = Field(default=None, alias="finalUrlSuffix")
    has_partners_badge: bool | None = Field(default=None, alias="hasPartnersBadge")
    id: str | None = Field(default=None, description="Customer ID")
    """Customer ID"""
    manager: bool | None = Field(default=None, description="Whether this is a manager account")
    """Whether this is a manager account"""
    optimization_score: float | None = Field(default=None, alias="optimizationScore")
    optimization_score_weight: float | None = Field(default=None, alias="optimizationScoreWeight")
    pay_per_conversion_eligibility_failure_reasons: list[str] | None = Field(default=None, alias="payPerConversionEligibilityFailureReasons")
    remarketing_setting: AccountCustomerRemarketingsetting | None = Field(default=None, alias="remarketingSetting")
    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the customer")
    """Resource name of the customer"""
    test_account: bool | None = Field(default=None, alias="testAccount")
    time_zone: str | None = Field(default=None, alias="timeZone")
    tracking_url_template: str | None = Field(default=None, alias="trackingUrlTemplate")

class Account(BaseModel):
    """Google Ads customer account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer: AccountCustomer | None = Field(default=None)

class AccountSearchResponse(BaseModel):
    """Search response containing account data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Account] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class CampaignCampaignbudget(BaseModel):
    """Nested schema for Campaign.campaignBudget"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the campaign budget")
    """Resource name of the campaign budget"""
    amount_micros: str | None = Field(default=None, alias="amountMicros", description="Budget amount in micros")
    """Budget amount in micros"""

class CampaignMetrics(BaseModel):
    """Nested schema for Campaign.metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    clicks: str | None = Field(default=None)
    ctr: float | None = Field(default=None)
    conversions: float | None = Field(default=None)
    conversions_value: float | None = Field(default=None, alias="conversionsValue")
    cost_micros: str | None = Field(default=None, alias="costMicros")
    impressions: str | None = Field(default=None)
    average_cpc: float | None = Field(default=None, alias="averageCpc")
    average_cpm: float | None = Field(default=None, alias="averageCpm")
    interactions: str | None = Field(default=None)

class CampaignCampaignNetworksettings(BaseModel):
    """Nested schema for CampaignCampaign.networkSettings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target_google_search: bool | None = Field(default=None, alias="targetGoogleSearch")
    target_search_network: bool | None = Field(default=None, alias="targetSearchNetwork")
    target_content_network: bool | None = Field(default=None, alias="targetContentNetwork")
    target_partner_search_network: bool | None = Field(default=None, alias="targetPartnerSearchNetwork")

class CampaignCampaign(BaseModel):
    """Nested schema for Campaign.campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Campaign ID")
    """Campaign ID"""
    name: str | None = Field(default=None, description="Campaign name")
    """Campaign name"""
    status: str | None = Field(default=None, description="Campaign status")
    """Campaign status"""
    advertising_channel_type: str | None = Field(default=None, alias="advertisingChannelType", description="Primary channel type")
    """Primary channel type"""
    advertising_channel_sub_type: str | None = Field(default=None, alias="advertisingChannelSubType")
    bidding_strategy: str | None = Field(default=None, alias="biddingStrategy")
    bidding_strategy_type: str | None = Field(default=None, alias="biddingStrategyType")
    campaign_budget: str | None = Field(default=None, alias="campaignBudget", description="Campaign budget resource name")
    """Campaign budget resource name"""
    start_date: str | None = Field(default=None, alias="startDate", description="Campaign start date")
    """Campaign start date"""
    end_date: str | None = Field(default=None, alias="endDate", description="Campaign end date")
    """Campaign end date"""
    serving_status: str | None = Field(default=None, alias="servingStatus")
    resource_name: str | None = Field(default=None, alias="resourceName")
    labels: list[str] | None = Field(default=None)
    network_settings: CampaignCampaignNetworksettings | None = Field(default=None, alias="networkSettings")

class CampaignSegments(BaseModel):
    """Nested schema for Campaign.segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = Field(default=None, description="Date in YYYY-MM-DD format")
    """Date in YYYY-MM-DD format"""

class Campaign(BaseModel):
    """Google Ads campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: CampaignCampaign | None = Field(default=None)
    campaign_budget: CampaignCampaignbudget | None = Field(default=None, alias="campaignBudget")
    metrics: CampaignMetrics | None = Field(default=None)
    segments: CampaignSegments | None = Field(default=None)

class CampaignSearchResponse(BaseModel):
    """Search response containing campaign data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Campaign] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class AdGroupSegments(BaseModel):
    """Nested schema for AdGroup.segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = Field(default=None)

class AdGroupCampaign(BaseModel):
    """Nested schema for AdGroup.campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Parent campaign ID")
    """Parent campaign ID"""
    resource_name: str | None = Field(default=None, alias="resourceName", description="Parent campaign resource name")
    """Parent campaign resource name"""

class AdGroupAdgroup(BaseModel):
    """Nested schema for AdGroup.adGroup"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Ad group ID")
    """Ad group ID"""
    name: str | None = Field(default=None, description="Ad group name")
    """Ad group name"""
    status: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    ad_rotation_mode: str | None = Field(default=None, alias="adRotationMode")
    base_ad_group: str | None = Field(default=None, alias="baseAdGroup")
    campaign: str | None = Field(default=None, description="Parent campaign resource name")
    """Parent campaign resource name"""
    cpc_bid_micros: str | None = Field(default=None, alias="cpcBidMicros")
    cpm_bid_micros: str | None = Field(default=None, alias="cpmBidMicros")
    cpv_bid_micros: str | None = Field(default=None, alias="cpvBidMicros")
    effective_target_cpa_micros: str | None = Field(default=None, alias="effectiveTargetCpaMicros")
    effective_target_cpa_source: str | None = Field(default=None, alias="effectiveTargetCpaSource")
    effective_target_roas: float | None = Field(default=None, alias="effectiveTargetRoas")
    effective_target_roas_source: str | None = Field(default=None, alias="effectiveTargetRoasSource")
    labels: list[str] | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")
    target_cpa_micros: str | None = Field(default=None, alias="targetCpaMicros")
    target_roas: float | None = Field(default=None, alias="targetRoas")
    tracking_url_template: str | None = Field(default=None, alias="trackingUrlTemplate")

class AdGroupMetrics(BaseModel):
    """Nested schema for AdGroup.metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cost_micros: str | None = Field(default=None, alias="costMicros")

class AdGroup(BaseModel):
    """Google Ads ad group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: AdGroupCampaign | None = Field(default=None)
    ad_group: AdGroupAdgroup | None = Field(default=None, alias="adGroup")
    metrics: AdGroupMetrics | None = Field(default=None)
    segments: AdGroupSegments | None = Field(default=None)

class AdGroupSearchResponse(BaseModel):
    """Search response containing ad group data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AdGroup] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class AdGroupAdAdgroupadPolicysummary(BaseModel):
    """Nested schema for AdGroupAdAdgroupad.policySummary"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    approval_status: str | None = Field(default=None, alias="approvalStatus")
    review_status: str | None = Field(default=None, alias="reviewStatus")

class AdGroupAdAdgroupadAd(BaseModel):
    """Nested schema for AdGroupAdAdgroupad.ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Ad ID")
    """Ad ID"""
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    display_url: str | None = Field(default=None, alias="displayUrl")
    final_urls: list[str] | None = Field(default=None, alias="finalUrls")
    final_mobile_urls: list[str] | None = Field(default=None, alias="finalMobileUrls")
    final_url_suffix: str | None = Field(default=None, alias="finalUrlSuffix")
    tracking_url_template: str | None = Field(default=None, alias="trackingUrlTemplate")
    resource_name: str | None = Field(default=None, alias="resourceName")

class AdGroupAdAdgroupad(BaseModel):
    """Nested schema for AdGroupAd.adGroupAd"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad: AdGroupAdAdgroupadAd | None = Field(default=None)
    status: str | None = Field(default=None)
    ad_strength: str | None = Field(default=None, alias="adStrength")
    ad_group: str | None = Field(default=None, alias="adGroup")
    resource_name: str | None = Field(default=None, alias="resourceName")
    labels: list[str] | None = Field(default=None)
    policy_summary: AdGroupAdAdgroupadPolicysummary | None = Field(default=None, alias="policySummary")

class AdGroupAdSegments(BaseModel):
    """Nested schema for AdGroupAd.segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = Field(default=None)

class AdGroupAdAdgroup(BaseModel):
    """Nested schema for AdGroupAd.adGroup"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Parent ad group ID")
    """Parent ad group ID"""
    resource_name: str | None = Field(default=None, alias="resourceName", description="Parent ad group resource name")
    """Parent ad group resource name"""

class AdGroupAd(BaseModel):
    """Google Ads ad group ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: AdGroupAdAdgroup | None = Field(default=None, alias="adGroup")
    ad_group_ad: AdGroupAdAdgroupad | None = Field(default=None, alias="adGroupAd")
    segments: AdGroupAdSegments | None = Field(default=None)

class AdGroupAdSearchResponse(BaseModel):
    """Search response containing ad group ad data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AdGroupAd] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class CampaignLabelLabel(BaseModel):
    """Nested schema for CampaignLabel.label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")

class CampaignLabelCampaignlabel(BaseModel):
    """Nested schema for CampaignLabel.campaignLabel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: str | None = Field(default=None)
    label: str | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")

class CampaignLabelCampaign(BaseModel):
    """Nested schema for CampaignLabel.campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class CampaignLabel(BaseModel):
    """Campaign label association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: CampaignLabelCampaign | None = Field(default=None)
    campaign_label: CampaignLabelCampaignlabel | None = Field(default=None, alias="campaignLabel")
    label: CampaignLabelLabel | None = Field(default=None)

class CampaignLabelSearchResponse(BaseModel):
    """Search response containing campaign label data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[CampaignLabel] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class AdGroupLabelAdgroup(BaseModel):
    """Nested schema for AdGroupLabel.adGroup"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class AdGroupLabelLabel(BaseModel):
    """Nested schema for AdGroupLabel.label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")

class AdGroupLabelAdgrouplabel(BaseModel):
    """Nested schema for AdGroupLabel.adGroupLabel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: str | None = Field(default=None, alias="adGroup")
    label: str | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")

class AdGroupLabel(BaseModel):
    """Ad group label association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: AdGroupLabelAdgroup | None = Field(default=None, alias="adGroup")
    ad_group_label: AdGroupLabelAdgrouplabel | None = Field(default=None, alias="adGroupLabel")
    label: AdGroupLabelLabel | None = Field(default=None)

class AdGroupLabelSearchResponse(BaseModel):
    """Search response containing ad group label data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AdGroupLabel] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class AdGroupAdLabelAdgroupadlabel(BaseModel):
    """Nested schema for AdGroupAdLabel.adGroupAdLabel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group_ad: str | None = Field(default=None, alias="adGroupAd")
    label: str | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")

class AdGroupAdLabelAdgroupadAd(BaseModel):
    """Nested schema for AdGroupAdLabelAdgroupad.ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class AdGroupAdLabelAdgroupad(BaseModel):
    """Nested schema for AdGroupAdLabel.adGroupAd"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad: AdGroupAdLabelAdgroupadAd | None = Field(default=None)

class AdGroupAdLabelLabel(BaseModel):
    """Nested schema for AdGroupAdLabel.label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_name: str | None = Field(default=None, alias="resourceName")

class AdGroupAdLabel(BaseModel):
    """Ad group ad label association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group_ad: AdGroupAdLabelAdgroupad | None = Field(default=None, alias="adGroupAd")
    ad_group_ad_label: AdGroupAdLabelAdgroupadlabel | None = Field(default=None, alias="adGroupAdLabel")
    label: AdGroupAdLabelLabel | None = Field(default=None)

class AdGroupAdLabelSearchResponse(BaseModel):
    """Search response containing ad group ad label data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AdGroupAdLabel] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    field_mask: str | None = Field(default=None, alias="fieldMask")
    query_resource_consumption: str | None = Field(default=None, alias="queryResourceConsumption")

class CampaignMutateRequestOperationsItemUpdate(BaseModel):
    """Campaign fields to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str = Field(alias="resourceName", description="Resource name of the campaign to update (e.g., customers/1234567890/campaigns/111222333)")
    """Resource name of the campaign to update (e.g., customers/1234567890/campaigns/111222333)"""
    name: str | None = Field(default=None, description="New campaign name")
    """New campaign name"""
    status: str | None = Field(default=None, description="Campaign status (ENABLED or PAUSED)")
    """Campaign status (ENABLED or PAUSED)"""

class CampaignMutateRequestOperationsItem(BaseModel):
    """Nested schema for CampaignMutateRequest.operations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    update_mask: str | None = Field(default=None, alias="updateMask", description="Comma-separated list of field paths to update (e.g., name,status)")
    """Comma-separated list of field paths to update (e.g., name,status)"""
    update: CampaignMutateRequestOperationsItemUpdate | None = Field(default=None, description="Campaign fields to update")
    """Campaign fields to update"""

class CampaignMutateRequest(BaseModel):
    """Request to mutate (update) campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    operations: list[CampaignMutateRequestOperationsItem]

class CampaignMutateResponseResultsItem(BaseModel):
    """Nested schema for CampaignMutateResponse.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the mutated campaign")
    """Resource name of the mutated campaign"""

class CampaignMutateResponse(BaseModel):
    """Response from campaign mutate operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[CampaignMutateResponseResultsItem] | None = Field(default=None)

class AdGroupMutateRequestOperationsItemUpdate(BaseModel):
    """Ad group fields to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str = Field(alias="resourceName", description="Resource name of the ad group to update (e.g., customers/1234567890/adGroups/111222333)")
    """Resource name of the ad group to update (e.g., customers/1234567890/adGroups/111222333)"""
    name: str | None = Field(default=None, description="New ad group name")
    """New ad group name"""
    status: str | None = Field(default=None, description="Ad group status (ENABLED or PAUSED)")
    """Ad group status (ENABLED or PAUSED)"""
    cpc_bid_micros: str | None = Field(default=None, alias="cpcBidMicros", description="CPC bid amount in micros (1,000,000 micros = 1 currency unit)")
    """CPC bid amount in micros (1,000,000 micros = 1 currency unit)"""

class AdGroupMutateRequestOperationsItem(BaseModel):
    """Nested schema for AdGroupMutateRequest.operations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    update_mask: str | None = Field(default=None, alias="updateMask", description="Comma-separated list of field paths to update (e.g., name,status,cpcBidMicros)")
    """Comma-separated list of field paths to update (e.g., name,status,cpcBidMicros)"""
    update: AdGroupMutateRequestOperationsItemUpdate | None = Field(default=None, description="Ad group fields to update")
    """Ad group fields to update"""

class AdGroupMutateRequest(BaseModel):
    """Request to mutate (update) ad groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    operations: list[AdGroupMutateRequestOperationsItem]

class AdGroupMutateResponseResultsItem(BaseModel):
    """Nested schema for AdGroupMutateResponse.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the mutated ad group")
    """Resource name of the mutated ad group"""

class AdGroupMutateResponse(BaseModel):
    """Response from ad group mutate operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AdGroupMutateResponseResultsItem] | None = Field(default=None)

class LabelMutateRequestOperationsItemCreateTextlabel(BaseModel):
    """Text label styling"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    background_color: str | None = Field(default=None, alias="backgroundColor", description="Background color in hex format (e.g., #FF0000)")
    """Background color in hex format (e.g., #FF0000)"""
    description: str | None = Field(default=None, description="Description of the text label")
    """Description of the text label"""

class LabelMutateRequestOperationsItemCreate(BaseModel):
    """Label to create"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Name for the new label")
    """Name for the new label"""
    description: str | None = Field(default=None, description="Description for the label")
    """Description for the label"""
    text_label: LabelMutateRequestOperationsItemCreateTextlabel | None = Field(default=None, alias="textLabel", description="Text label styling")
    """Text label styling"""

class LabelMutateRequestOperationsItem(BaseModel):
    """Nested schema for LabelMutateRequest.operations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    create: LabelMutateRequestOperationsItemCreate | None = Field(default=None, description="Label to create")
    """Label to create"""

class LabelMutateRequest(BaseModel):
    """Request to create labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    operations: list[LabelMutateRequestOperationsItem]

class LabelMutateResponseResultsItem(BaseModel):
    """Nested schema for LabelMutateResponse.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the created label")
    """Resource name of the created label"""

class LabelMutateResponse(BaseModel):
    """Response from label mutate operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[LabelMutateResponseResultsItem] | None = Field(default=None)

class CampaignLabelMutateRequestOperationsItemCreate(BaseModel):
    """Campaign label association to create"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: str = Field(description="Resource name of the campaign (e.g., customers/1234567890/campaigns/111222333)")
    """Resource name of the campaign (e.g., customers/1234567890/campaigns/111222333)"""
    label: str = Field(description="Resource name of the label (e.g., customers/1234567890/labels/444555666)")
    """Resource name of the label (e.g., customers/1234567890/labels/444555666)"""

class CampaignLabelMutateRequestOperationsItem(BaseModel):
    """Nested schema for CampaignLabelMutateRequest.operations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    create: CampaignLabelMutateRequestOperationsItemCreate | None = Field(default=None, description="Campaign label association to create")
    """Campaign label association to create"""

class CampaignLabelMutateRequest(BaseModel):
    """Request to create campaign-label associations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    operations: list[CampaignLabelMutateRequestOperationsItem]

class CampaignLabelMutateResponseResultsItem(BaseModel):
    """Nested schema for CampaignLabelMutateResponse.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the created campaign label association")
    """Resource name of the created campaign label association"""

class CampaignLabelMutateResponse(BaseModel):
    """Response from campaign label mutate operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[CampaignLabelMutateResponseResultsItem] | None = Field(default=None)

class AdGroupLabelMutateRequestOperationsItemCreate(BaseModel):
    """Ad group label association to create"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group: str = Field(alias="adGroup", description="Resource name of the ad group (e.g., customers/1234567890/adGroups/111222333)")
    """Resource name of the ad group (e.g., customers/1234567890/adGroups/111222333)"""
    label: str = Field(description="Resource name of the label (e.g., customers/1234567890/labels/444555666)")
    """Resource name of the label (e.g., customers/1234567890/labels/444555666)"""

class AdGroupLabelMutateRequestOperationsItem(BaseModel):
    """Nested schema for AdGroupLabelMutateRequest.operations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    create: AdGroupLabelMutateRequestOperationsItemCreate | None = Field(default=None, description="Ad group label association to create")
    """Ad group label association to create"""

class AdGroupLabelMutateRequest(BaseModel):
    """Request to create ad group-label associations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    operations: list[AdGroupLabelMutateRequestOperationsItem]

class AdGroupLabelMutateResponseResultsItem(BaseModel):
    """Nested schema for AdGroupLabelMutateResponse.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    resource_name: str | None = Field(default=None, alias="resourceName", description="Resource name of the created ad group label association")
    """Resource name of the created ad group label association"""

class AdGroupLabelMutateResponse(BaseModel):
    """Response from ad group label mutate operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AdGroupLabelMutateResponseResultsItem] | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

class AdGroupsListResultMeta(BaseModel):
    """Metadata for ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

class AdGroupAdsListResultMeta(BaseModel):
    """Metadata for ad_group_ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

class CampaignLabelsListResultMeta(BaseModel):
    """Metadata for campaign_labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

class AdGroupLabelsListResultMeta(BaseModel):
    """Metadata for ad_group_labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

class AdGroupAdLabelsListResultMeta(BaseModel):
    """Metadata for ad_group_ad_labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None)

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

