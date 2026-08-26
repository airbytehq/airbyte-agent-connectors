"""
Pydantic models for linkedin-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""
# ruff: noqa: E501

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration - multiple options available

class LinkedinAdsOauth20AuthenticationAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    refresh_token: str
    """OAuth 2.0 refresh token for automatic renewal"""
    client_id: str
    """OAuth 2.0 application client ID"""
    client_secret: str
    """OAuth 2.0 application client secret"""

class LinkedinAdsAccessTokenAuthenticationAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """The access token generated for your developer application"""

LinkedinAdsAuthConfig = LinkedinAdsOauth20AuthenticationAuthConfig | LinkedinAdsAccessTokenAuthenticationAuthConfig

# Replication configuration

class LinkedinAdsReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from LinkedIn Ads."""

    model_config = ConfigDict(extra="forbid")

    account_ids: Optional[str] = None
    """Specify the account IDs to pull data from, separated by a space. Leave this field empty if you want to pull the data from all accounts accessible by the authenticated user. See the LinkedIn docs to locate these IDs."""
    start_date: str
    """UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class AccountVersion(BaseModel):
    """Version information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version_tag: str | None | None = Field(default=None, alias="versionTag")

class AccountChangeauditstampsCreated(BaseModel):
    """Nested schema for AccountChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class AccountChangeauditstampsLastmodified(BaseModel):
    """Nested schema for AccountChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class AccountChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: AccountChangeauditstampsCreated | None | None = Field(default=None)
    last_modified: AccountChangeauditstampsLastmodified | None | None = Field(default=None, alias="lastModified")

class Account(BaseModel):
    """LinkedIn ad account object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    status: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    reference: str | None = Field(default=None)
    test: bool | None = Field(default=None)
    change_audit_stamps: AccountChangeauditstamps | None = Field(default=None, alias="changeAuditStamps")
    notified_on_campaign_optimization: bool | None = Field(default=None, alias="notifiedOnCampaignOptimization")
    notified_on_creative_approval: bool | None = Field(default=None, alias="notifiedOnCreativeApproval")
    notified_on_creative_rejection: bool | None = Field(default=None, alias="notifiedOnCreativeRejection")
    notified_on_end_of_campaign: bool | None = Field(default=None, alias="notifiedOnEndOfCampaign")
    notified_on_new_features_enabled: bool | None = Field(default=None, alias="notifiedOnNewFeaturesEnabled")
    serving_statuses: list[str] | None = Field(default=None, alias="servingStatuses")
    version: AccountVersion | None = Field(default=None)

class AccountsListMetadata(BaseModel):
    """Nested schema for AccountsList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class AccountsList(BaseModel):
    """Paginated list of ad accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[Account] | None = Field(default=None)
    metadata: AccountsListMetadata | None = Field(default=None)

class AccountUserChangeauditstampsLastmodified(BaseModel):
    """Nested schema for AccountUserChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class AccountUserChangeauditstampsCreated(BaseModel):
    """Nested schema for AccountUserChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class AccountUserChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: AccountUserChangeauditstampsCreated | None | None = Field(default=None)
    last_modified: AccountUserChangeauditstampsLastmodified | None | None = Field(default=None, alias="lastModified")

class AccountUser(BaseModel):
    """LinkedIn ad account user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: str | None = Field(default=None)
    user: str | None = Field(default=None)
    role: str | None = Field(default=None)
    change_audit_stamps: AccountUserChangeauditstamps | None = Field(default=None, alias="changeAuditStamps")

class AccountUsersListPagingLinksItem(BaseModel):
    """Nested schema for AccountUsersListPaging.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)

class AccountUsersListPaging(BaseModel):
    """Nested schema for AccountUsersList.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)
    links: list[AccountUsersListPagingLinksItem] | None = Field(default=None)

class AccountUsersList(BaseModel):
    """Paginated list of account users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[AccountUser] | None = Field(default=None)
    paging: AccountUsersListPaging | None = Field(default=None)

class CampaignRunschedule(BaseModel):
    """Campaign run schedule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None | None = Field(default=None)
    end: int | None | None = Field(default=None)

class CampaignTotalbudget(BaseModel):
    """Total budget configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    currency_code: str | None | None = Field(default=None, alias="currencyCode")

class CampaignUnitcost(BaseModel):
    """Cost per unit (bid amount)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    currency_code: str | None | None = Field(default=None, alias="currencyCode")

class CampaignChangeauditstampsCreated(BaseModel):
    """Nested schema for CampaignChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class CampaignChangeauditstampsLastmodified(BaseModel):
    """Nested schema for CampaignChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class CampaignChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: CampaignChangeauditstampsCreated | None | None = Field(default=None)
    last_modified: CampaignChangeauditstampsLastmodified | None | None = Field(default=None, alias="lastModified")

class CampaignVersion(BaseModel):
    """Version information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version_tag: str | None | None = Field(default=None, alias="versionTag")

class CampaignLocale(BaseModel):
    """Campaign locale settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    country: str | None | None = Field(default=None)
    language: str | None | None = Field(default=None)

class CampaignDailybudget(BaseModel):
    """Daily budget configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    currency_code: str | None | None = Field(default=None, alias="currencyCode")

class Campaign(BaseModel):
    """LinkedIn ad campaign object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    account: str | None = Field(default=None)
    campaign_group: str | None = Field(default=None, alias="campaignGroup")
    status: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    cost_type: str | None = Field(default=None, alias="costType")
    format: str | None = Field(default=None)
    objective_type: str | None = Field(default=None, alias="objectiveType")
    optimization_target_type: str | None = Field(default=None, alias="optimizationTargetType")
    creative_selection: str | None = Field(default=None, alias="creativeSelection")
    pacing_strategy: str | None = Field(default=None, alias="pacingStrategy")
    audience_expansion_enabled: bool | None = Field(default=None, alias="audienceExpansionEnabled")
    offsite_delivery_enabled: bool | None = Field(default=None, alias="offsiteDeliveryEnabled")
    story_delivery_enabled: bool | None = Field(default=None, alias="storyDeliveryEnabled")
    test: bool | None = Field(default=None)
    associated_entity: str | None = Field(default=None, alias="associatedEntity")
    connected_television_only: bool | None = Field(default=None, alias="connectedTelevisionOnly")
    political_intent: str | None = Field(default=None, alias="politicalIntent")
    change_audit_stamps: CampaignChangeauditstamps | None = Field(default=None, alias="changeAuditStamps")
    daily_budget: CampaignDailybudget | None = Field(default=None, alias="dailyBudget")
    total_budget: CampaignTotalbudget | None = Field(default=None, alias="totalBudget")
    unit_cost: CampaignUnitcost | None = Field(default=None, alias="unitCost")
    run_schedule: CampaignRunschedule | None = Field(default=None, alias="runSchedule")
    locale: CampaignLocale | None = Field(default=None)
    targeting_criteria: dict[str, Any] | None = Field(default=None, alias="targetingCriteria")
    offsite_preferences: dict[str, Any] | None = Field(default=None, alias="offsitePreferences")
    serving_statuses: list[str] | None = Field(default=None, alias="servingStatuses")
    version: CampaignVersion | None = Field(default=None)

class CampaignsListMetadata(BaseModel):
    """Nested schema for CampaignsList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CampaignsList(BaseModel):
    """Paginated list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[Campaign] | None = Field(default=None)
    metadata: CampaignsListMetadata | None = Field(default=None)

class CampaignGroupRunschedule(BaseModel):
    """Campaign group run schedule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None | None = Field(default=None)
    end: int | None | None = Field(default=None)

class CampaignGroupChangeauditstampsLastmodified(BaseModel):
    """Nested schema for CampaignGroupChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class CampaignGroupChangeauditstampsCreated(BaseModel):
    """Nested schema for CampaignGroupChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: str | None | None = Field(default=None)
    time: int | None | None = Field(default=None)

class CampaignGroupChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: CampaignGroupChangeauditstampsCreated | None | None = Field(default=None)
    last_modified: CampaignGroupChangeauditstampsLastmodified | None | None = Field(default=None, alias="lastModified")

class CampaignGroupTotalbudget(BaseModel):
    """Total budget for the campaign group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    currency_code: str | None | None = Field(default=None, alias="currencyCode")

class CampaignGroup(BaseModel):
    """LinkedIn ad campaign group object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    account: str | None = Field(default=None)
    status: str | None = Field(default=None)
    test: bool | None = Field(default=None)
    backfilled: bool | None = Field(default=None)
    change_audit_stamps: CampaignGroupChangeauditstamps | None = Field(default=None, alias="changeAuditStamps")
    total_budget: CampaignGroupTotalbudget | None = Field(default=None, alias="totalBudget")
    run_schedule: CampaignGroupRunschedule | None = Field(default=None, alias="runSchedule")
    serving_statuses: list[str] | None = Field(default=None, alias="servingStatuses")
    allowed_campaign_types: list[str] | None = Field(default=None, alias="allowedCampaignTypes")

class CampaignGroupsListPagingLinksItem(BaseModel):
    """Nested schema for CampaignGroupsListPaging.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)

class CampaignGroupsListPaging(BaseModel):
    """Nested schema for CampaignGroupsList.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)
    links: list[CampaignGroupsListPagingLinksItem] | None = Field(default=None)

class CampaignGroupsListMetadata(BaseModel):
    """Nested schema for CampaignGroupsList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CampaignGroupsList(BaseModel):
    """Paginated list of campaign groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[CampaignGroup] | None = Field(default=None)
    paging: CampaignGroupsListPaging | None = Field(default=None)
    metadata: CampaignGroupsListMetadata | None = Field(default=None)

class CreativeReview(BaseModel):
    """Review status and rejection reasons"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: str | None | None = Field(default=None)
    rejection_reasons: list[Any] | None | None = Field(default=None, alias="rejectionReasons")

class CreativeLeadgencalltoaction(BaseModel):
    """Lead generation call to action"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    destination: str | None | None = Field(default=None)
    label: str | None | None = Field(default=None)

class Creative(BaseModel):
    """LinkedIn ad creative object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    account: str | None = Field(default=None)
    campaign: str | None = Field(default=None)
    intended_status: str | None = Field(default=None, alias="intendedStatus")
    is_serving: bool | None = Field(default=None, alias="isServing")
    is_test: bool | None = Field(default=None, alias="isTest")
    created_at: int | None = Field(default=None, alias="createdAt")
    created_by: str | None = Field(default=None, alias="createdBy")
    last_modified_at: int | None = Field(default=None, alias="lastModifiedAt")
    last_modified_by: str | None = Field(default=None, alias="lastModifiedBy")
    content: dict[str, Any] | None = Field(default=None)
    review: CreativeReview | None = Field(default=None)
    serving_hold_reasons: list[str] | None = Field(default=None, alias="servingHoldReasons")
    leadgen_call_to_action: CreativeLeadgencalltoaction | None = Field(default=None, alias="leadgenCallToAction")

class CreativesListMetadata(BaseModel):
    """Nested schema for CreativesList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CreativesList(BaseModel):
    """Paginated list of creatives"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[Creative] | None = Field(default=None)
    metadata: CreativesListMetadata | None = Field(default=None)

class ConversionValue(BaseModel):
    """Conversion value"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    currency_code: str | None | None = Field(default=None, alias="currencyCode")

class Conversion(BaseModel):
    """LinkedIn ad conversion tracking rule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    account: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attribution_type: str | None = Field(default=None, alias="attributionType")
    ownership_type: str | None = Field(default=None, alias="ownershipType")
    conversion_method: str | None = Field(default=None, alias="conversionMethod")
    value_type: str | None = Field(default=None, alias="valueType")
    enabled: bool | None = Field(default=None)
    created: int | None = Field(default=None)
    last_modified: int | None = Field(default=None, alias="lastModified")
    post_click_attribution_window_size: int | None = Field(default=None, alias="postClickAttributionWindowSize")
    view_through_attribution_window_size: int | None = Field(default=None, alias="viewThroughAttributionWindowSize")
    campaigns: list[str] | None = Field(default=None)
    associated_campaigns: list[Any] | None = Field(default=None, alias="associatedCampaigns")
    image_pixel_tag: str | None = Field(default=None, alias="imagePixelTag")
    last_callback_at: int | None = Field(default=None, alias="lastCallbackAt")
    latest_first_party_callback_at: int | None = Field(default=None, alias="latestFirstPartyCallbackAt")
    url_match_rule_expression: list[Any] | None = Field(default=None, alias="urlMatchRuleExpression")
    url_rules: list[Any] | None = Field(default=None, alias="urlRules")
    value: ConversionValue | None = Field(default=None)

class ConversionsListPagingLinksItem(BaseModel):
    """Nested schema for ConversionsListPaging.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)

class ConversionsListPaging(BaseModel):
    """Nested schema for ConversionsList.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    count: int | None = Field(default=None)
    start: int | None = Field(default=None)
    links: list[ConversionsListPagingLinksItem] | None = Field(default=None)

class ConversionsList(BaseModel):
    """Paginated list of conversions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[Conversion] | None = Field(default=None)
    paging: ConversionsListPaging | None = Field(default=None)

class AdAnalyticsRecordDaterangeEnd(BaseModel):
    """Nested schema for AdAnalyticsRecordDaterange.end"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    year: int | None = Field(default=None)
    month: int | None = Field(default=None)
    day: int | None = Field(default=None)

class AdAnalyticsRecordDaterangeStart(BaseModel):
    """Nested schema for AdAnalyticsRecordDaterange.start"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    year: int | None = Field(default=None)
    month: int | None = Field(default=None)
    day: int | None = Field(default=None)

class AdAnalyticsRecordDaterange(BaseModel):
    """Date range for this analytics record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: AdAnalyticsRecordDaterangeStart | None = Field(default=None)
    end: AdAnalyticsRecordDaterangeEnd | None = Field(default=None)

class AdAnalyticsRecord(BaseModel):
    """Ad analytics data record with performance metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_range: AdAnalyticsRecordDaterange | None = Field(default=None, alias="dateRange")
    pivot_values: list[str] | None = Field(default=None, alias="pivotValues")
    impressions: int | None = Field(default=None)
    clicks: int | None = Field(default=None)
    cost_in_local_currency: str | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: str | None = Field(default=None, alias="costInUsd")
    likes: int | None = Field(default=None)
    shares: int | None = Field(default=None)
    comments: int | None = Field(default=None)
    reactions: int | None = Field(default=None)
    follows: int | None = Field(default=None)
    total_engagements: int | None = Field(default=None, alias="totalEngagements")
    landing_page_clicks: int | None = Field(default=None, alias="landingPageClicks")
    company_page_clicks: int | None = Field(default=None, alias="companyPageClicks")
    external_website_conversions: int | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: int | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: int | None = Field(default=None, alias="externalWebsitePostViewConversions")
    conversion_value_in_local_currency: str | None = Field(default=None, alias="conversionValueInLocalCurrency")
    approximate_member_reach: int | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: int | None = Field(default=None, alias="cardClicks")
    card_impressions: int | None = Field(default=None, alias="cardImpressions")
    video_starts: int | None = Field(default=None, alias="videoStarts")
    video_views: int | None = Field(default=None, alias="videoViews")
    video_first_quartile_completions: int | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: int | None = Field(default=None, alias="videoMidpointCompletions")
    video_third_quartile_completions: int | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_completions: int | None = Field(default=None, alias="videoCompletions")
    full_screen_plays: int | None = Field(default=None, alias="fullScreenPlays")
    one_click_leads: int | None = Field(default=None, alias="oneClickLeads")
    one_click_lead_form_opens: int | None = Field(default=None, alias="oneClickLeadFormOpens")
    other_engagements: int | None = Field(default=None, alias="otherEngagements")
    ad_unit_clicks: int | None = Field(default=None, alias="adUnitClicks")
    action_clicks: int | None = Field(default=None, alias="actionClicks")
    text_url_clicks: int | None = Field(default=None, alias="textUrlClicks")
    comment_likes: int | None = Field(default=None, alias="commentLikes")
    sends: int | None = Field(default=None)
    opens: int | None = Field(default=None)
    download_clicks: int | None = Field(default=None, alias="downloadClicks")
    job_applications: int | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: int | None = Field(default=None, alias="jobApplyClicks")
    registrations: int | None = Field(default=None)
    talent_leads: int | None = Field(default=None, alias="talentLeads")
    valid_work_email_leads: int | None = Field(default=None, alias="validWorkEmailLeads")
    post_click_job_applications: int | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: int | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: int | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: int | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: int | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: int | None = Field(default=None, alias="postViewRegistrations")
    lead_generation_mail_contact_info_shares: int | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: int | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    document_completions: int | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: int | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: int | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: int | None = Field(default=None, alias="documentThirdQuartileCompletions")

class AdAnalyticsResponsePagingLinksItem(BaseModel):
    """Nested schema for AdAnalyticsResponsePaging.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)

class AdAnalyticsResponsePaging(BaseModel):
    """Nested schema for AdAnalyticsResponse.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    count: int | None = Field(default=None)
    start: int | None = Field(default=None)
    total: int | None = Field(default=None)
    links: list[AdAnalyticsResponsePagingLinksItem] | None = Field(default=None)

class AdAnalyticsResponse(BaseModel):
    """Ad analytics API response"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[AdAnalyticsRecord] | None = Field(default=None)
    paging: AdAnalyticsResponsePaging | None = Field(default=None)

class AdImpressionDeviceAnalytics(BaseModel):
    """Ad analytics record pivoted by device type"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberCompanyAnalytics(BaseModel):
    """Ad analytics record pivoted by member company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberCompanySizeAnalytics(BaseModel):
    """Ad analytics record pivoted by member company size"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberCountryAnalytics(BaseModel):
    """Ad analytics record pivoted by member country"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberIndustryAnalytics(BaseModel):
    """Ad analytics record pivoted by member industry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberJobFunctionAnalytics(BaseModel):
    """Ad analytics record pivoted by member job function"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberJobTitleAnalytics(BaseModel):
    """Ad analytics record pivoted by member job title"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberRegionAnalytics(BaseModel):
    """Ad analytics record pivoted by member region"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class AdMemberSeniorityAnalytics(BaseModel):
    """Ad analytics record pivoted by member seniority"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action_clicks: float | None = Field(default=None, alias="actionClicks")
    ad_unit_clicks: float | None = Field(default=None, alias="adUnitClicks")
    approximate_member_reach: float | None = Field(default=None, alias="approximateMemberReach")
    card_clicks: float | None = Field(default=None, alias="cardClicks")
    card_impressions: float | None = Field(default=None, alias="cardImpressions")
    clicks: float | None = Field(default=None)
    comment_likes: float | None = Field(default=None, alias="commentLikes")
    comments: float | None = Field(default=None)
    company_page_clicks: float | None = Field(default=None, alias="companyPageClicks")
    conversion_value_in_local_currency: float | None = Field(default=None, alias="conversionValueInLocalCurrency")
    cost_in_local_currency: float | None = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: float | None = Field(default=None, alias="costInUsd")
    document_completions: float | None = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: float | None = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: float | None = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: float | None = Field(default=None, alias="documentThirdQuartileCompletions")
    download_clicks: float | None = Field(default=None, alias="downloadClicks")
    end_date: str | None = Field(default=None)
    external_website_conversions: float | None = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: float | None = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: float | None = Field(default=None, alias="externalWebsitePostViewConversions")
    follows: float | None = Field(default=None)
    full_screen_plays: float | None = Field(default=None, alias="fullScreenPlays")
    impressions: float | None = Field(default=None)
    job_applications: float | None = Field(default=None, alias="jobApplications")
    job_apply_clicks: float | None = Field(default=None, alias="jobApplyClicks")
    landing_page_clicks: float | None = Field(default=None, alias="landingPageClicks")
    lead_generation_mail_contact_info_shares: float | None = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: float | None = Field(default=None, alias="leadGenerationMailInterestedClicks")
    likes: float | None = Field(default=None)
    one_click_lead_form_opens: float | None = Field(default=None, alias="oneClickLeadFormOpens")
    one_click_leads: float | None = Field(default=None, alias="oneClickLeads")
    opens: float | None = Field(default=None)
    other_engagements: float | None = Field(default=None, alias="otherEngagements")
    pivot_values: list[Any] | None = Field(default=None, alias="pivotValues")
    string_of_pivot_values: str | None = Field(default=None)
    post_click_job_applications: float | None = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: float | None = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: float | None = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: float | None = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: float | None = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: float | None = Field(default=None, alias="postViewRegistrations")
    reactions: float | None = Field(default=None)
    registrations: float | None = Field(default=None)
    sends: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    start_date: str | None = Field(default=None)
    talent_leads: float | None = Field(default=None, alias="talentLeads")
    text_url_clicks: float | None = Field(default=None, alias="textUrlClicks")
    total_engagements: float | None = Field(default=None, alias="totalEngagements")
    valid_work_email_leads: float | None = Field(default=None, alias="validWorkEmailLeads")
    video_completions: float | None = Field(default=None, alias="videoCompletions")
    video_first_quartile_completions: float | None = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: float | None = Field(default=None, alias="videoMidpointCompletions")
    video_starts: float | None = Field(default=None, alias="videoStarts")
    video_third_quartile_completions: float | None = Field(default=None, alias="videoThirdQuartileCompletions")
    video_views: float | None = Field(default=None, alias="videoViews")
    viral_card_clicks: float | None = Field(default=None, alias="viralCardClicks")
    viral_card_impressions: float | None = Field(default=None, alias="viralCardImpressions")
    viral_clicks: float | None = Field(default=None, alias="viralClicks")
    viral_comment_likes: float | None = Field(default=None, alias="viralCommentLikes")
    viral_comments: float | None = Field(default=None, alias="viralComments")
    viral_company_page_clicks: float | None = Field(default=None, alias="viralCompanyPageClicks")
    viral_document_completions: float | None = Field(default=None, alias="viralDocumentCompletions")
    viral_document_first_quartile_completions: float | None = Field(default=None, alias="viralDocumentFirstQuartileCompletions")
    viral_document_midpoint_completions: float | None = Field(default=None, alias="viralDocumentMidpointCompletions")
    viral_document_third_quartile_completions: float | None = Field(default=None, alias="viralDocumentThirdQuartileCompletions")
    viral_download_clicks: float | None = Field(default=None, alias="viralDownloadClicks")
    viral_external_website_conversions: float | None = Field(default=None, alias="viralExternalWebsiteConversions")
    viral_external_website_post_click_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostClickConversions")
    viral_external_website_post_view_conversions: float | None = Field(default=None, alias="viralExternalWebsitePostViewConversions")
    viral_follows: float | None = Field(default=None, alias="viralFollows")
    viral_full_screen_plays: float | None = Field(default=None, alias="viralFullScreenPlays")
    viral_impressions: float | None = Field(default=None, alias="viralImpressions")
    viral_job_applications: float | None = Field(default=None, alias="viralJobApplications")
    viral_job_apply_clicks: float | None = Field(default=None, alias="viralJobApplyClicks")
    viral_landing_page_clicks: float | None = Field(default=None, alias="viralLandingPageClicks")
    viral_likes: float | None = Field(default=None, alias="viralLikes")
    viral_one_click_lead_form_opens: float | None = Field(default=None, alias="viralOneClickLeadFormOpens")
    viral_one_click_leads: float | None = Field(default=None, alias="viralOneClickLeads")
    viral_other_engagements: float | None = Field(default=None, alias="viralOtherEngagements")
    viral_post_click_job_applications: float | None = Field(default=None, alias="viralPostClickJobApplications")
    viral_post_click_job_apply_clicks: float | None = Field(default=None, alias="viralPostClickJobApplyClicks")
    viral_post_click_registrations: float | None = Field(default=None, alias="viralPostClickRegistrations")
    viral_post_view_job_applications: float | None = Field(default=None, alias="viralPostViewJobApplications")
    viral_post_view_job_apply_clicks: float | None = Field(default=None, alias="viralPostViewJobApplyClicks")
    viral_post_view_registrations: float | None = Field(default=None, alias="viralPostViewRegistrations")
    viral_reactions: float | None = Field(default=None, alias="viralReactions")
    viral_registrations: float | None = Field(default=None, alias="viralRegistrations")
    viral_shares: float | None = Field(default=None, alias="viralShares")
    viral_total_engagements: float | None = Field(default=None, alias="viralTotalEngagements")
    viral_video_completions: float | None = Field(default=None, alias="viralVideoCompletions")
    viral_video_first_quartile_completions: float | None = Field(default=None, alias="viralVideoFirstQuartileCompletions")
    viral_video_midpoint_completions: float | None = Field(default=None, alias="viralVideoMidpointCompletions")
    viral_video_starts: float | None = Field(default=None, alias="viralVideoStarts")
    viral_video_third_quartile_completions: float | None = Field(default=None, alias="viralVideoThirdQuartileCompletions")
    viral_video_views: float | None = Field(default=None, alias="viralVideoViews")
    pivot: str | None = Field(default=None)
    sponsored_campaign: str | None = Field(default=None, alias="sponsoredCampaign")

class LeadForm(BaseModel):
    """LinkedIn lead generation form"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    owner: dict[str, Any] | None = Field(default=None)
    state: str | None = Field(default=None)
    content: dict[str, Any] | None = Field(default=None)
    created: int | None = Field(default=None)
    last_modified: int | None = Field(default=None, alias="lastModified")
    creation_locale: dict[str, Any] | None = Field(default=None, alias="creationLocale")
    hidden_fields: list[Any] | None = Field(default=None, alias="hiddenFields")
    review_info: dict[str, Any] | None = Field(default=None, alias="reviewInfo")
    version_id: int | None = Field(default=None, alias="versionId")
    version_tag: str | None = Field(default=None, alias="versionTag")

class LeadFormResponse(BaseModel):
    """LinkedIn lead form response (submitted lead)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    lead_type: str | None = Field(default=None, alias="leadType")
    form: dict[str, Any] | None = Field(default=None)
    owner: dict[str, Any] | None = Field(default=None)
    owner_info: dict[str, Any] | None = Field(default=None, alias="ownerInfo")
    lead_metadata: dict[str, Any] | None = Field(default=None, alias="leadMetadata")
    lead_metadata_info: dict[str, Any] | None = Field(default=None, alias="leadMetadataInfo")
    associated_entity: dict[str, Any] | None = Field(default=None, alias="associatedEntity")
    associated_entity_info: dict[str, Any] | None = Field(default=None, alias="associatedEntityInfo")
    submitted_at: int | None = Field(default=None, alias="submittedAt")
    response_id: dict[str, Any] | None = Field(default=None, alias="responseId")
    form_response: dict[str, Any] | None = Field(default=None, alias="formResponse")
    test_lead: bool | None = Field(default=None, alias="testLead")
    submitter: str | None = Field(default=None)
    versioned_lead_gen_form_urn: str | None = Field(default=None, alias="versionedLeadGenFormUrn")

class LeadFormsListPagingLinksItem(BaseModel):
    """Nested schema for LeadFormsListPaging.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)

class LeadFormsListPaging(BaseModel):
    """Nested schema for LeadFormsList.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)
    links: list[LeadFormsListPagingLinksItem] | None = Field(default=None)

class LeadFormsList(BaseModel):
    """Paginated list of lead forms"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[LeadForm] | None = Field(default=None)
    paging: LeadFormsListPaging | None = Field(default=None)

class LeadFormResponsesListPagingLinksItem(BaseModel):
    """Nested schema for LeadFormResponsesListPaging.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)

class LeadFormResponsesListPaging(BaseModel):
    """Nested schema for LeadFormResponsesList.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)
    links: list[LeadFormResponsesListPagingLinksItem] | None = Field(default=None)

class LeadFormResponsesList(BaseModel):
    """Paginated list of lead form responses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[LeadFormResponse] | None = Field(default=None)
    paging: LeadFormResponsesListPaging | None = Field(default=None)

class RestliCreateResponse(BaseModel):
    """Rest.li create responses have an empty JSON body; the created entity ID or URN is returned in the x-restli-id response header (surfaced via the operation's meta extractor as created_id).
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pass

class RestliPartialUpdateRequestPatch(BaseModel):
    """Nested schema for RestliPartialUpdateRequest.patch"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    set_: dict[str, Any] = Field(alias="$set", description="Map of field names to their new values")
    """Map of field names to their new values"""

class RestliPartialUpdateRequest(BaseModel):
    """Rest.li partial update envelope shared by all LinkedIn Ads update operations. Wrap the fields to change in patch.$set. Setting an array field replaces the entire array, so include all existing elements you want to keep.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    patch: RestliPartialUpdateRequestPatch

class CampaignCreateRequestDailybudget(BaseModel):
    """Daily budget"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class CampaignCreateRequestRunschedule(BaseModel):
    """Scheduled run window (epoch milliseconds)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    end: int | None = Field(default=None)

class CampaignCreateRequestLocale(BaseModel):
    """Campaign locale"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    country: str | None = Field(default=None)
    language: str | None = Field(default=None)

class CampaignCreateRequestUnitcost(BaseModel):
    """Bid amount per unit (per click, per impression, etc.)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class CampaignCreateRequest(BaseModel):
    """Fields for creating a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: str
    name: str
    political_intent: str = Field(alias="politicalIntent")
    campaign_group: str | None = Field(default=None, alias="campaignGroup")
    type_: str | None = Field(default=None, alias="type")
    objective_type: str | None = Field(default=None, alias="objectiveType")
    status: str | None = Field(default=None)
    cost_type: str | None = Field(default=None, alias="costType")
    daily_budget: CampaignCreateRequestDailybudget | None = Field(default=None, alias="dailyBudget")
    unit_cost: CampaignCreateRequestUnitcost | None = Field(default=None, alias="unitCost")
    locale: CampaignCreateRequestLocale | None = Field(default=None)
    run_schedule: CampaignCreateRequestRunschedule = Field(alias="runSchedule")
    targeting_criteria: dict[str, Any] | None = Field(default=None, alias="targetingCriteria")
    audience_expansion_enabled: bool | None = Field(default=None, alias="audienceExpansionEnabled")
    offsite_delivery_enabled: bool = Field(alias="offsiteDeliveryEnabled")
    creative_selection: str | None = Field(default=None, alias="creativeSelection")

class CampaignGroupCreateRequestRunschedule(BaseModel):
    """Scheduled run window (epoch milliseconds)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    end: int | None = Field(default=None)

class CampaignGroupCreateRequestTotalbudget(BaseModel):
    """Total budget across the group's lifetime"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class CampaignGroupCreateRequest(BaseModel):
    """Fields for creating a campaign group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: str
    name: str
    status: str | None = Field(default=None)
    run_schedule: CampaignGroupCreateRequestRunschedule = Field(alias="runSchedule")
    total_budget: CampaignGroupCreateRequestTotalbudget | None = Field(default=None, alias="totalBudget")
    objective_type: str | None = Field(default=None, alias="objectiveType")

class CreativeCreateRequest(BaseModel):
    """Fields for creating a creative"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: str
    content: dict[str, Any] | None = Field(default=None)
    intended_status: str | None = Field(default=None, alias="intendedStatus")
    name: str | None = Field(default=None)

class AccountCreateRequest(BaseModel):
    """Fields for creating an ad account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    type_: str = Field(alias="type")
    currency: str | None = Field(default=None)
    reference: str | None = Field(default=None)
    test: bool | None = Field(default=None)

class AccountUserUpsertRequest(BaseModel):
    """Role grant for an ad account user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    role: str

class ConversionCreateRequestValue(BaseModel):
    """Monetary value assigned to each conversion"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class ConversionCreateRequest(BaseModel):
    """Fields for creating a conversion tracking rule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: str
    name: str
    type_: str = Field(alias="type")
    attribution_type: str | None = Field(default=None, alias="attributionType")
    post_click_attribution_window_size: int | None = Field(default=None, alias="postClickAttributionWindowSize")
    view_through_attribution_window_size: int | None = Field(default=None, alias="viewThroughAttributionWindowSize")
    enabled: bool | None = Field(default=None)
    url_match_rule_expression: list[list[dict[str, Any]]] | None = Field(default=None, alias="urlMatchRuleExpression")
    value: ConversionCreateRequestValue | None = Field(default=None)

class ConversionEventsBatchRequestElementsItemConversionvalue(BaseModel):
    """Monetary value of this conversion"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class ConversionEventsBatchRequestElementsItemUserUseridsItem(BaseModel):
    """Nested schema for ConversionEventsBatchRequestElementsItemUser.userIds_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id_type: str | None = Field(default=None, alias="idType", description="e.g. SHA256_EMAIL, LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID")
    """e.g. SHA256_EMAIL, LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID"""
    id_value: str | None = Field(default=None, alias="idValue")

class ConversionEventsBatchRequestElementsItemUser(BaseModel):
    """Identifies the converting user (hashed email or other supported ID types)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_ids: list[ConversionEventsBatchRequestElementsItemUserUseridsItem] | None = Field(default=None, alias="userIds")
    user_info: dict[str, Any] | None = Field(default=None, alias="userInfo")

class ConversionEventsBatchRequestElementsItem(BaseModel):
    """Nested schema for ConversionEventsBatchRequest.elements_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conversion: str = Field(description="Conversion rule URN, e.g. urn:lla:llaPartnerConversion:123456")
    """Conversion rule URN, e.g. urn:lla:llaPartnerConversion:123456"""
    conversion_happened_at: int = Field(alias="conversionHappenedAt", description="Epoch milliseconds when the conversion occurred")
    """Epoch milliseconds when the conversion occurred"""
    user: ConversionEventsBatchRequestElementsItemUser | None = Field(default=None, description="Identifies the converting user (hashed email or other supported ID types)")
    """Identifies the converting user (hashed email or other supported ID types)"""
    conversion_value: ConversionEventsBatchRequestElementsItemConversionvalue | None = Field(default=None, alias="conversionValue", description="Monetary value of this conversion")
    """Monetary value of this conversion"""
    event_id: str | None = Field(default=None, alias="eventId", description="Optional unique event ID for deduplication")
    """Optional unique event ID for deduplication"""

class ConversionEventsBatchRequest(BaseModel):
    """Batch of offline conversion events (Rest.li BATCH_CREATE, max 5,000 per request)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: list[ConversionEventsBatchRequestElementsItem]

class CampaignConversionUpsertRequest(BaseModel):
    """Campaign-to-conversion association record; may be empty since the key carries both URNs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign: str | None = Field(default=None)
    conversion: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class AccountsCreateResultMeta(BaseModel):
    """Metadata for accounts.Action.CREATE operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_id: str | None = Field(default=None)

class AccountUsersListResultMeta(BaseModel):
    """Metadata for account_users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CampaignsCreateResultMeta(BaseModel):
    """Metadata for campaigns.Action.CREATE operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_id: str | None = Field(default=None)

class CampaignGroupsListResultMeta(BaseModel):
    """Metadata for campaign_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CampaignGroupsCreateResultMeta(BaseModel):
    """Metadata for campaign_groups.Action.CREATE operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_id: str | None = Field(default=None)

class CreativesListResultMeta(BaseModel):
    """Metadata for creatives.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CreativesCreateResultMeta(BaseModel):
    """Metadata for creatives.Action.CREATE operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_id: str | None = Field(default=None)

class ConversionsListResultMeta(BaseModel):
    """Metadata for conversions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)

class ConversionsCreateResultMeta(BaseModel):
    """Metadata for conversions.Action.CREATE operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_id: str | None = Field(default=None)

class LeadFormsListResultMeta(BaseModel):
    """Metadata for lead_forms.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)

class LeadFormResponsesListResultMeta(BaseModel):
    """Metadata for lead_form_responses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None)
    count: int | None = Field(default=None)
    total: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class LinkedinAdsCheckResult(BaseModel):
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


class LinkedinAdsExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class LinkedinAdsExecuteResultWithMeta(LinkedinAdsExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    test: bool | None = None
    """Flag indicating if the account is in a test mode."""
    notified_on_creative_rejection: bool | None = None
    """Flag for notifications on creative rejection."""
    notified_on_new_features_enabled: bool | None = None
    """Flag for notifications on new features being enabled."""
    notified_on_end_of_campaign: bool | None = None
    """Flag for notifications on the end of campaign."""
    serving_statuses: list[Any] | None = None
    """The serving statuses associated with the account."""
    notified_on_campaign_optimization: bool | None = None
    """Flag for notifications on campaign optimization."""
    type_: str | None = None
    """The type or category of the account."""
    version: dict[str, Any] | None = None
    """The version information related to the account."""
    reference: str | None = None
    """A reference identifier for the account."""
    notified_on_creative_approval: bool | None = None
    """Flag for notifications on creative approval."""
    created: str | None = None
    """The timestamp indicating when the account was created."""
    last_modified: str | None = None
    """The timestamp of the last modification made to the account."""
    name: str | None = None
    """The name of the account."""
    currency: str | None = None
    """The currency used for financial transactions in the account."""
    id: int | None = None
    """The unique identifier for the account."""
    status: str | None = None
    """The status of the account."""


class AccountUsersSearchData(BaseModel):
    """Search result data for account_users entity."""
    model_config = ConfigDict(extra="allow")

    account: str | None = None
    """The account associated with the user"""
    created: str | None = None
    """The date and time when the user account was created"""
    last_modified: str | None = None
    """The date and time when the user account was last modified"""
    role: str | None = None
    """The role assigned to the user in the account"""
    user: str | None = None
    """The user details including name, email, etc."""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    targeting_criteria: dict[str, Any] | None = None
    """Criteria for targeting in the campaign."""
    serving_statuses: list[Any] | None = None
    """The serving statuses of the campaign."""
    type_: str | None = None
    """The type of campaign."""
    locale: dict[str, Any] | None = None
    """The locale settings for the campaign."""
    version: dict[str, Any] | None = None
    """The version information for the campaign."""
    associated_entity: str | None = None
    """The entity associated with the campaign."""
    run_schedule: dict[str, Any] | None = None
    """The schedule for running the campaign."""
    optimization_target_type: str | None = None
    """The type of optimization target for the campaign."""
    created: str | None = None
    """The date and time when the campaign was created."""
    last_modified: str | None = None
    """The date and time when the campaign was last modified."""
    campaign_group: str | None = None
    """The group to which the campaign belongs."""
    daily_budget: dict[str, Any] | None = None
    """The daily budget set for the campaign."""
    total_budget: dict[str, Any] | None = None
    """The total budget amount for the campaign."""
    unit_cost: dict[str, Any] | None = None
    """The unit cost for the campaign."""
    creative_selection: str | None = None
    """Information about the creative selection for the campaign."""
    cost_type: str | None = None
    """The type of cost associated with the campaign."""
    name: str | None = None
    """The name of the campaign."""
    offsite_delivery_enabled: bool | None = None
    """Indicates if offsite delivery is enabled for the campaign."""
    id: int | None = None
    """The unique identifier of the campaign."""
    audience_expansion_enabled: bool | None = None
    """Indicates if audience expansion is enabled for this campaign."""
    test: bool | None = None
    """Indicates if the campaign is a test campaign."""
    account: str | None = None
    """The account associated with the campaign data."""
    status: str | None = None
    """The status of the campaign."""
    story_delivery_enabled: bool | None = None
    """Indicates if story delivery is enabled for the campaign."""
    pacing_strategy: str | None = None
    """The pacing strategy for the campaign."""
    format: str | None = None
    """The format of the campaign."""
    objective_type: str | None = None
    """The type of objective for the campaign."""
    offsite_preferences: dict[str, Any] | None = None
    """Preferences related to offsite delivery."""


class CampaignGroupsSearchData(BaseModel):
    """Search result data for campaign_groups entity."""
    model_config = ConfigDict(extra="allow")

    run_schedule: dict[str, Any] | None = None
    """Schedule for running the campaign group."""
    created: str | None = None
    """The date and time when the campaign group was created."""
    last_modified: str | None = None
    """The date and time when the campaign group was last modified."""
    name: str | None = None
    """Name of the campaign group."""
    test: bool | None = None
    """Indicates if the campaign group is a test campaign."""
    total_budget: dict[str, Any] | None = None
    """Total budget allocated for the campaign group."""
    serving_statuses: list[Any] | None = None
    """List of serving statuses for the campaign group."""
    backfilled: bool | None = None
    """Indicates if the campaign group was backfilled."""
    id: int | None = None
    """Unique identifier for the campaign group."""
    account: str | None = None
    """The account associated with the campaign group."""
    status: str | None = None
    """Current status of the campaign group."""
    allowed_campaign_types: list[Any] | None = None
    """List of campaign types allowed for this campaign group."""


class CreativesSearchData(BaseModel):
    """Search result data for creatives entity."""
    model_config = ConfigDict(extra="allow")

    serving_hold_reasons: list[Any] | None = None
    """Reasons for holding the creative from serving."""
    last_modified_at: int | None = None
    """The timestamp when the creative was last modified."""
    last_modified_by: str | None = None
    """The user who last modified the creative."""
    content: dict[str, Any] | None = None
    """The actual content of the creative."""
    created_at: int | None = None
    """The timestamp when the creative was created."""
    is_test: bool | None = None
    """Boolean indicating if the creative is a test creative."""
    created_by: str | None = None
    """The user who created the creative."""
    review: dict[str, Any] | None = None
    """Review information for the creative."""
    name: str | None = None
    """The name of the creative."""
    is_serving: bool | None = None
    """Boolean indicating if the creative is currently serving."""
    campaign: str | None = None
    """The campaign to which the creative belongs."""
    id: str | None = None
    """The unique identifier of the creative."""
    intended_status: str | None = None
    """The intended status of the creative."""
    account: str | None = None
    """The account associated with the creative."""
    leadgen_call_to_action: dict[str, Any] | None = None
    """Call-to-action information for lead generation purposes."""


class ConversionsSearchData(BaseModel):
    """Search result data for conversions entity."""
    model_config = ConfigDict(extra="allow")

    attribution_type: str | None = None
    """The type of attribution for the conversion."""
    account: str | None = None
    """The account associated with the conversion data."""
    campaigns: list[Any] | None = None
    """List of campaigns related to the conversion."""
    created: int | None = None
    """Timestamp of when the conversion was created."""
    enabled: bool | None = None
    """Flag indicating if the conversion tracking is enabled."""
    id: int | None = None
    """Unique identifier for the conversion."""
    image_pixel_tag: str | None = None
    """Pixel tag used for tracking the conversion."""
    name: str | None = None
    """Name of the conversion."""
    type_: str | None = None
    """Type of conversion."""
    latest_first_party_callback_at: int | None = None
    """Timestamp of the latest first-party callback for the conversion."""
    post_click_attribution_window_size: int | None = None
    """Window size for post-click attribution."""
    view_through_attribution_window_size: int | None = None
    """Window size for view-through attribution."""
    last_callback_at: int | None = None
    """Timestamp of the last callback for the conversion."""
    last_modified: int | None = None
    """Timestamp of the last modification made to the conversion."""
    value: dict[str, Any] | None = None
    """Value associated with the conversion."""
    associated_campaigns: list[Any] | None = None
    """Campaigns associated with the conversion."""
    url_match_rule_expression: list[Any] | None = None
    """Expression used for matching URLs for attribution."""
    url_rules: list[Any] | None = None
    """Rules for URL matching in the conversion."""


class AdCampaignAnalyticsSearchData(BaseModel):
    """Search result data for ad_campaign_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdCreativeAnalyticsSearchData(BaseModel):
    """Search result data for ad_creative_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_creative: str | None = None
    """Sponsored creative"""


class AdImpressionDeviceAnalyticsSearchData(BaseModel):
    """Search result data for ad_impression_device_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanyAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_company_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanySizeAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_company_size_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCountryAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_country_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberIndustryAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_industry_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobFunctionAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_job_function_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobTitleAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_job_title_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberRegionAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_region_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberSeniorityAnalyticsSearchData(BaseModel):
    """Search result data for ad_member_seniority_analytics entity."""
    model_config = ConfigDict(extra="allow")

    action_clicks: float | None = None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None = None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None = None
    """An approximation of unique ad impressions."""
    card_clicks: float | None = None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None = None
    """The number of times interactive cards were displayed."""
    clicks: float | None = None
    """Total number of clicks on the ad."""
    comment_likes: float | None = None
    """The count of likes on comments related to the ad."""
    comments: float | None = None
    """The number of comments on the ad."""
    company_page_clicks: float | None = None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None = None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None = None
    """Cost of ad campaign in USD."""
    document_completions: float | None = None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None = None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None = None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None = None
    """Completions for third quartile of document views."""
    download_clicks: float | None = None
    """Clicks on download links in the ad."""
    end_date: str | None = None
    """End date of the ad analytics data."""
    external_website_conversions: float | None = None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites."""
    follows: float | None = None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None = None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None = None
    """Total number of times the ad was displayed."""
    job_applications: float | None = None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None = None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None = None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None = None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None = None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None = None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None = None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None = None
    """Leads generated in one click."""
    opens: float | None = None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None = None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None = None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None = None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None = None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None = None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None = None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None = None
    """Registrations completed post-viewing the ad."""
    reactions: float | None = None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None = None
    """Total registrations completed through the ad."""
    sends: float | None = None
    """Number of messages sent through the ad."""
    shares: float | None = None
    """Total shares generated by the ad."""
    start_date: str | None = None
    """Start date of the ad analytics data."""
    talent_leads: float | None = None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None = None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None = None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None = None
    """Leads generated through valid work emails."""
    video_completions: float | None = None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None = None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None = None
    """Completions for midpoint of video views."""
    video_starts: float | None = None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None = None
    """Completions for third quartile of video views."""
    video_views: float | None = None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None = None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None = None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None = None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None = None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None = None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None = None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None = None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None = None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None = None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None = None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None = None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None = None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None = None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None = None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None = None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None = None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None = None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None = None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None = None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None = None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None = None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None = None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None = None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None = None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None = None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None = None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None = None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None = None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None = None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None = None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None = None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None = None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None = None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None = None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None = None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None = None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None = None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None = None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None = None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None = None
    """URN of the sponsored campaign this analytics record belongs to"""


class LeadFormsSearchData(BaseModel):
    """Search result data for lead_forms entity."""
    model_config = ConfigDict(extra="allow")

    id: int = None
    """Numerical identifier for the form."""
    name: str | None = None
    """Name of the Lead Form provided by the owner."""
    owner: dict[str, Any] | None = None
    """URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.
"""
    state: str | None = None
    """Information about the current state of the Lead Form."""
    content: dict[str, Any] | None = None
    """Content of the Lead Form which will be displayed to the viewer."""
    created: int | None = None
    """An epoch time corresponding to the creation of the form."""
    last_modified: int | None = None
    """An epoch time corresponding to the last modified of of the form."""
    creation_locale: dict[str, Any] | None = None
    """Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.
"""
    hidden_fields: list[Any] | None = None
    """Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.
"""
    review_info: dict[str, Any] | None = None
    """Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.
"""
    version_id: int | None = None
    """The version ID of the form. This is a derived field and is generated on the server side."""
    version_tag: str | None = None
    """The number of times the form has been modified."""


class LeadFormResponsesSearchData(BaseModel):
    """Search result data for lead_form_responses entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique id to identify the Lead Form Response."""
    lead_type: str | None = None
    """Type of the lead representing the origination of the lead."""
    form: dict[str, Any] | None = None
    """URN identifying which form this FormResponse belongs to."""
    owner: dict[str, Any] | None = None
    """Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.
"""
    owner_info: dict[str, Any] | None = None
    """Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo."""
    lead_metadata: dict[str, Any] | None = None
    """Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned."""
    lead_metadata_info: dict[str, Any] | None = None
    """Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned."""
    associated_entity: dict[str, Any] | None = None
    """URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned."""
    associated_entity_info: dict[str, Any] | None = None
    """Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned."""
    submitted_at: int | None = None
    """An epoch timestamp that recording when the form response was submitted."""
    response_id: dict[str, Any] | None = None
    """The unique identifier for the form response generated in the front-end when a submitter submits the response."""
    form_response: dict[str, Any] | None = None
    """Answers provided by the form submitter."""
    test_lead: bool | None = None
    """Whether this is a test lead created for testing purposes."""
    submitter: str | None = None
    """From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes
"""
    versioned_lead_gen_form_urn: str | None = None
    """URN identifying which form this FormResponse belongs to."""


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

AccountUsersSearchResult = AirbyteSearchResult[AccountUsersSearchData]
"""Search result type for account_users entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

CampaignGroupsSearchResult = AirbyteSearchResult[CampaignGroupsSearchData]
"""Search result type for campaign_groups entity."""

CreativesSearchResult = AirbyteSearchResult[CreativesSearchData]
"""Search result type for creatives entity."""

ConversionsSearchResult = AirbyteSearchResult[ConversionsSearchData]
"""Search result type for conversions entity."""

AdCampaignAnalyticsSearchResult = AirbyteSearchResult[AdCampaignAnalyticsSearchData]
"""Search result type for ad_campaign_analytics entity."""

AdCreativeAnalyticsSearchResult = AirbyteSearchResult[AdCreativeAnalyticsSearchData]
"""Search result type for ad_creative_analytics entity."""

AdImpressionDeviceAnalyticsSearchResult = AirbyteSearchResult[AdImpressionDeviceAnalyticsSearchData]
"""Search result type for ad_impression_device_analytics entity."""

AdMemberCompanyAnalyticsSearchResult = AirbyteSearchResult[AdMemberCompanyAnalyticsSearchData]
"""Search result type for ad_member_company_analytics entity."""

AdMemberCompanySizeAnalyticsSearchResult = AirbyteSearchResult[AdMemberCompanySizeAnalyticsSearchData]
"""Search result type for ad_member_company_size_analytics entity."""

AdMemberCountryAnalyticsSearchResult = AirbyteSearchResult[AdMemberCountryAnalyticsSearchData]
"""Search result type for ad_member_country_analytics entity."""

AdMemberIndustryAnalyticsSearchResult = AirbyteSearchResult[AdMemberIndustryAnalyticsSearchData]
"""Search result type for ad_member_industry_analytics entity."""

AdMemberJobFunctionAnalyticsSearchResult = AirbyteSearchResult[AdMemberJobFunctionAnalyticsSearchData]
"""Search result type for ad_member_job_function_analytics entity."""

AdMemberJobTitleAnalyticsSearchResult = AirbyteSearchResult[AdMemberJobTitleAnalyticsSearchData]
"""Search result type for ad_member_job_title_analytics entity."""

AdMemberRegionAnalyticsSearchResult = AirbyteSearchResult[AdMemberRegionAnalyticsSearchData]
"""Search result type for ad_member_region_analytics entity."""

AdMemberSeniorityAnalyticsSearchResult = AirbyteSearchResult[AdMemberSeniorityAnalyticsSearchData]
"""Search result type for ad_member_seniority_analytics entity."""

LeadFormsSearchResult = AirbyteSearchResult[LeadFormsSearchData]
"""Search result type for lead_forms entity."""

LeadFormResponsesSearchResult = AirbyteSearchResult[LeadFormResponsesSearchData]
"""Search result type for lead_form_responses entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AccountsListResult = LinkedinAdsExecuteResultWithMeta[list[dict[str, Any]], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

AccountsCreateResult = LinkedinAdsExecuteResultWithMeta[RestliCreateResponse, AccountsCreateResultMeta]
"""Result type for accounts.create operation with data and metadata."""

AccountUsersListResult = LinkedinAdsExecuteResultWithMeta[list[AccountUser], AccountUsersListResultMeta]
"""Result type for account_users.list operation with data and metadata."""

CampaignsListResult = LinkedinAdsExecuteResultWithMeta[list[dict[str, Any]], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

CampaignsCreateResult = LinkedinAdsExecuteResultWithMeta[RestliCreateResponse, CampaignsCreateResultMeta]
"""Result type for campaigns.create operation with data and metadata."""

CampaignGroupsListResult = LinkedinAdsExecuteResultWithMeta[list[CampaignGroup], CampaignGroupsListResultMeta]
"""Result type for campaign_groups.list operation with data and metadata."""

CampaignGroupsCreateResult = LinkedinAdsExecuteResultWithMeta[RestliCreateResponse, CampaignGroupsCreateResultMeta]
"""Result type for campaign_groups.create operation with data and metadata."""

CreativesListResult = LinkedinAdsExecuteResultWithMeta[list[dict[str, Any]], CreativesListResultMeta]
"""Result type for creatives.list operation with data and metadata."""

CreativesCreateResult = LinkedinAdsExecuteResultWithMeta[RestliCreateResponse, CreativesCreateResultMeta]
"""Result type for creatives.create operation with data and metadata."""

ConversionsListResult = LinkedinAdsExecuteResultWithMeta[list[Conversion], ConversionsListResultMeta]
"""Result type for conversions.list operation with data and metadata."""

ConversionsCreateResult = LinkedinAdsExecuteResultWithMeta[RestliCreateResponse, ConversionsCreateResultMeta]
"""Result type for conversions.create operation with data and metadata."""

AdCampaignAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_campaign_analytics.list operation."""

AdCreativeAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_creative_analytics.list operation."""

AdImpressionDeviceAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_impression_device_analytics.list operation."""

AdMemberCompanyAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_company_analytics.list operation."""

AdMemberCompanySizeAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_company_size_analytics.list operation."""

AdMemberCountryAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_country_analytics.list operation."""

AdMemberIndustryAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_industry_analytics.list operation."""

AdMemberJobFunctionAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_job_function_analytics.list operation."""

AdMemberJobTitleAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_job_title_analytics.list operation."""

AdMemberRegionAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_region_analytics.list operation."""

AdMemberSeniorityAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_member_seniority_analytics.list operation."""

LeadFormsListResult = LinkedinAdsExecuteResultWithMeta[list[LeadForm], LeadFormsListResultMeta]
"""Result type for lead_forms.list operation with data and metadata."""

LeadFormResponsesListResult = LinkedinAdsExecuteResultWithMeta[list[LeadFormResponse], LeadFormResponsesListResultMeta]
"""Result type for lead_form_responses.list operation with data and metadata."""

