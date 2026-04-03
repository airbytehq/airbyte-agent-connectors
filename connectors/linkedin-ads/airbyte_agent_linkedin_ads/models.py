"""
Pydantic models for linkedin-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class LinkedinAdsAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    refresh_token: str
    """OAuth 2.0 refresh token for automatic renewal"""
    client_id: str
    """OAuth 2.0 application client ID"""
    client_secret: str
    """OAuth 2.0 application client secret"""

# Replication configuration

class LinkedinAdsReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from LinkedIn Ads."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class AccountVersion(BaseModel):
    """Version information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version_tag: Union[str | None, Any] = Field(default=None, alias="versionTag")

class AccountChangeauditstampsCreated(BaseModel):
    """Nested schema for AccountChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class AccountChangeauditstampsLastmodified(BaseModel):
    """Nested schema for AccountChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class AccountChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: Union[AccountChangeauditstampsCreated | None, Any] = Field(default=None)
    last_modified: Union[AccountChangeauditstampsLastmodified | None, Any] = Field(default=None, alias="lastModified")

class Account(BaseModel):
    """LinkedIn ad account object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    reference: Union[str | None, Any] = Field(default=None)
    test: Union[bool | None, Any] = Field(default=None)
    change_audit_stamps: Union[AccountChangeauditstamps | None, Any] = Field(default=None, alias="changeAuditStamps")
    notified_on_campaign_optimization: Union[bool | None, Any] = Field(default=None, alias="notifiedOnCampaignOptimization")
    notified_on_creative_approval: Union[bool | None, Any] = Field(default=None, alias="notifiedOnCreativeApproval")
    notified_on_creative_rejection: Union[bool | None, Any] = Field(default=None, alias="notifiedOnCreativeRejection")
    notified_on_end_of_campaign: Union[bool | None, Any] = Field(default=None, alias="notifiedOnEndOfCampaign")
    notified_on_new_features_enabled: Union[bool | None, Any] = Field(default=None, alias="notifiedOnNewFeaturesEnabled")
    serving_statuses: Union[list[str] | None, Any] = Field(default=None, alias="servingStatuses")
    version: Union[AccountVersion | None, Any] = Field(default=None)

class AccountsListMetadata(BaseModel):
    """Nested schema for AccountsList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class AccountsList(BaseModel):
    """Paginated list of ad accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[Account], Any] = Field(default=None)
    metadata: Union[AccountsListMetadata, Any] = Field(default=None)

class AccountUserChangeauditstampsLastmodified(BaseModel):
    """Nested schema for AccountUserChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class AccountUserChangeauditstampsCreated(BaseModel):
    """Nested schema for AccountUserChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class AccountUserChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: Union[AccountUserChangeauditstampsCreated | None, Any] = Field(default=None)
    last_modified: Union[AccountUserChangeauditstampsLastmodified | None, Any] = Field(default=None, alias="lastModified")

class AccountUser(BaseModel):
    """LinkedIn ad account user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: Union[str | None, Any] = Field(default=None)
    user: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    change_audit_stamps: Union[AccountUserChangeauditstamps | None, Any] = Field(default=None, alias="changeAuditStamps")

class AccountUsersListMetadata(BaseModel):
    """Nested schema for AccountUsersList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class AccountUsersList(BaseModel):
    """Paginated list of account users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[AccountUser], Any] = Field(default=None)
    metadata: Union[AccountUsersListMetadata, Any] = Field(default=None)

class CampaignUnitcost(BaseModel):
    """Cost per unit (bid amount)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[str | None, Any] = Field(default=None)
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")

class CampaignLocale(BaseModel):
    """Campaign locale settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    country: Union[str | None, Any] = Field(default=None)
    language: Union[str | None, Any] = Field(default=None)

class CampaignChangeauditstampsCreated(BaseModel):
    """Nested schema for CampaignChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class CampaignChangeauditstampsLastmodified(BaseModel):
    """Nested schema for CampaignChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class CampaignChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: Union[CampaignChangeauditstampsCreated | None, Any] = Field(default=None)
    last_modified: Union[CampaignChangeauditstampsLastmodified | None, Any] = Field(default=None, alias="lastModified")

class CampaignTotalbudget(BaseModel):
    """Total budget configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[str | None, Any] = Field(default=None)
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")

class CampaignDailybudget(BaseModel):
    """Daily budget configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[str | None, Any] = Field(default=None)
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")

class CampaignRunschedule(BaseModel):
    """Campaign run schedule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: Union[int | None, Any] = Field(default=None)
    end: Union[int | None, Any] = Field(default=None)

class CampaignVersion(BaseModel):
    """Version information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version_tag: Union[str | None, Any] = Field(default=None, alias="versionTag")

class Campaign(BaseModel):
    """LinkedIn ad campaign object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account: Union[str | None, Any] = Field(default=None)
    campaign_group: Union[str | None, Any] = Field(default=None, alias="campaignGroup")
    status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    cost_type: Union[str | None, Any] = Field(default=None, alias="costType")
    format: Union[str | None, Any] = Field(default=None)
    objective_type: Union[str | None, Any] = Field(default=None, alias="objectiveType")
    optimization_target_type: Union[str | None, Any] = Field(default=None, alias="optimizationTargetType")
    creative_selection: Union[str | None, Any] = Field(default=None, alias="creativeSelection")
    pacing_strategy: Union[str | None, Any] = Field(default=None, alias="pacingStrategy")
    audience_expansion_enabled: Union[bool | None, Any] = Field(default=None, alias="audienceExpansionEnabled")
    offsite_delivery_enabled: Union[bool | None, Any] = Field(default=None, alias="offsiteDeliveryEnabled")
    story_delivery_enabled: Union[bool | None, Any] = Field(default=None, alias="storyDeliveryEnabled")
    test: Union[bool | None, Any] = Field(default=None)
    associated_entity: Union[str | None, Any] = Field(default=None, alias="associatedEntity")
    connected_television_only: Union[bool | None, Any] = Field(default=None, alias="connectedTelevisionOnly")
    political_intent: Union[str | None, Any] = Field(default=None, alias="politicalIntent")
    change_audit_stamps: Union[CampaignChangeauditstamps | None, Any] = Field(default=None, alias="changeAuditStamps")
    daily_budget: Union[CampaignDailybudget | None, Any] = Field(default=None, alias="dailyBudget")
    total_budget: Union[CampaignTotalbudget | None, Any] = Field(default=None, alias="totalBudget")
    unit_cost: Union[CampaignUnitcost | None, Any] = Field(default=None, alias="unitCost")
    run_schedule: Union[CampaignRunschedule | None, Any] = Field(default=None, alias="runSchedule")
    locale: Union[CampaignLocale | None, Any] = Field(default=None)
    targeting_criteria: Union[dict[str, Any] | None, Any] = Field(default=None, alias="targetingCriteria")
    offsite_preferences: Union[dict[str, Any] | None, Any] = Field(default=None, alias="offsitePreferences")
    serving_statuses: Union[list[str] | None, Any] = Field(default=None, alias="servingStatuses")
    version: Union[CampaignVersion | None, Any] = Field(default=None)

class CampaignsListMetadata(BaseModel):
    """Nested schema for CampaignsList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class CampaignsList(BaseModel):
    """Paginated list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[Campaign], Any] = Field(default=None)
    metadata: Union[CampaignsListMetadata, Any] = Field(default=None)

class CampaignGroupTotalbudget(BaseModel):
    """Total budget for the campaign group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[str | None, Any] = Field(default=None)
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")

class CampaignGroupRunschedule(BaseModel):
    """Campaign group run schedule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: Union[int | None, Any] = Field(default=None)
    end: Union[int | None, Any] = Field(default=None)

class CampaignGroupChangeauditstampsLastmodified(BaseModel):
    """Nested schema for CampaignGroupChangeauditstamps.lastModified"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class CampaignGroupChangeauditstampsCreated(BaseModel):
    """Nested schema for CampaignGroupChangeauditstamps.created"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    actor: Union[str | None, Any] = Field(default=None)
    time: Union[int | None, Any] = Field(default=None)

class CampaignGroupChangeauditstamps(BaseModel):
    """Creation and last modification audit stamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: Union[CampaignGroupChangeauditstampsCreated | None, Any] = Field(default=None)
    last_modified: Union[CampaignGroupChangeauditstampsLastmodified | None, Any] = Field(default=None, alias="lastModified")

class CampaignGroup(BaseModel):
    """LinkedIn ad campaign group object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    test: Union[bool | None, Any] = Field(default=None)
    backfilled: Union[bool | None, Any] = Field(default=None)
    change_audit_stamps: Union[CampaignGroupChangeauditstamps | None, Any] = Field(default=None, alias="changeAuditStamps")
    total_budget: Union[CampaignGroupTotalbudget | None, Any] = Field(default=None, alias="totalBudget")
    run_schedule: Union[CampaignGroupRunschedule | None, Any] = Field(default=None, alias="runSchedule")
    serving_statuses: Union[list[str] | None, Any] = Field(default=None, alias="servingStatuses")
    allowed_campaign_types: Union[list[str] | None, Any] = Field(default=None, alias="allowedCampaignTypes")

class CampaignGroupsListMetadata(BaseModel):
    """Nested schema for CampaignGroupsList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class CampaignGroupsList(BaseModel):
    """Paginated list of campaign groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[CampaignGroup], Any] = Field(default=None)
    metadata: Union[CampaignGroupsListMetadata, Any] = Field(default=None)

class CreativeReview(BaseModel):
    """Review status and rejection reasons"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str | None, Any] = Field(default=None)
    rejection_reasons: Union[list[Any] | None, Any] = Field(default=None, alias="rejectionReasons")

class CreativeLeadgencalltoaction(BaseModel):
    """Lead generation call to action"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    destination: Union[str | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)

class Creative(BaseModel):
    """LinkedIn ad creative object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account: Union[str | None, Any] = Field(default=None)
    campaign: Union[str | None, Any] = Field(default=None)
    intended_status: Union[str | None, Any] = Field(default=None, alias="intendedStatus")
    is_serving: Union[bool | None, Any] = Field(default=None, alias="isServing")
    is_test: Union[bool | None, Any] = Field(default=None, alias="isTest")
    created_at: Union[int | None, Any] = Field(default=None, alias="createdAt")
    created_by: Union[str | None, Any] = Field(default=None, alias="createdBy")
    last_modified_at: Union[int | None, Any] = Field(default=None, alias="lastModifiedAt")
    last_modified_by: Union[str | None, Any] = Field(default=None, alias="lastModifiedBy")
    content: Union[dict[str, Any] | None, Any] = Field(default=None)
    review: Union[CreativeReview | None, Any] = Field(default=None)
    serving_hold_reasons: Union[list[str] | None, Any] = Field(default=None, alias="servingHoldReasons")
    leadgen_call_to_action: Union[CreativeLeadgencalltoaction | None, Any] = Field(default=None, alias="leadgenCallToAction")

class CreativesListMetadata(BaseModel):
    """Nested schema for CreativesList.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class CreativesList(BaseModel):
    """Paginated list of creatives"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[Creative], Any] = Field(default=None)
    metadata: Union[CreativesListMetadata, Any] = Field(default=None)

class ConversionValue(BaseModel):
    """Conversion value"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[str | None, Any] = Field(default=None)
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")

class Conversion(BaseModel):
    """LinkedIn ad conversion tracking rule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    attribution_type: Union[str | None, Any] = Field(default=None, alias="attributionType")
    conversion_method: Union[str | None, Any] = Field(default=None, alias="conversionMethod")
    value_type: Union[str | None, Any] = Field(default=None, alias="valueType")
    enabled: Union[bool | None, Any] = Field(default=None)
    created: Union[int | None, Any] = Field(default=None)
    last_modified: Union[int | None, Any] = Field(default=None, alias="lastModified")
    post_click_attribution_window_size: Union[int | None, Any] = Field(default=None, alias="postClickAttributionWindowSize")
    view_through_attribution_window_size: Union[int | None, Any] = Field(default=None, alias="viewThroughAttributionWindowSize")
    campaigns: Union[list[str] | None, Any] = Field(default=None)
    associated_campaigns: Union[list[Any] | None, Any] = Field(default=None, alias="associatedCampaigns")
    image_pixel_tag: Union[str | None, Any] = Field(default=None, alias="imagePixelTag")
    last_callback_at: Union[int | None, Any] = Field(default=None, alias="lastCallbackAt")
    latest_first_party_callback_at: Union[int | None, Any] = Field(default=None, alias="latestFirstPartyCallbackAt")
    url_match_rule_expression: Union[list[Any] | None, Any] = Field(default=None, alias="urlMatchRuleExpression")
    url_rules: Union[list[Any] | None, Any] = Field(default=None, alias="urlRules")
    value: Union[ConversionValue | None, Any] = Field(default=None)

class ConversionsListPaging(BaseModel):
    """Nested schema for ConversionsList.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)
    start: Union[int, Any] = Field(default=None)

class ConversionsList(BaseModel):
    """Paginated list of conversions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[Conversion], Any] = Field(default=None)
    paging: Union[ConversionsListPaging, Any] = Field(default=None)

class AdAnalyticsRecordDaterangeStart(BaseModel):
    """Nested schema for AdAnalyticsRecordDaterange.start"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    year: Union[int, Any] = Field(default=None)
    month: Union[int, Any] = Field(default=None)
    day: Union[int, Any] = Field(default=None)

class AdAnalyticsRecordDaterangeEnd(BaseModel):
    """Nested schema for AdAnalyticsRecordDaterange.end"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    year: Union[int, Any] = Field(default=None)
    month: Union[int, Any] = Field(default=None)
    day: Union[int, Any] = Field(default=None)

class AdAnalyticsRecordDaterange(BaseModel):
    """Date range for this analytics record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: Union[AdAnalyticsRecordDaterangeStart, Any] = Field(default=None)
    end: Union[AdAnalyticsRecordDaterangeEnd, Any] = Field(default=None)

class AdAnalyticsRecord(BaseModel):
    """Ad analytics data record with performance metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_range: Union[AdAnalyticsRecordDaterange | None, Any] = Field(default=None, alias="dateRange")
    pivot_values: Union[list[str] | None, Any] = Field(default=None, alias="pivotValues")
    impressions: Union[int | None, Any] = Field(default=None)
    clicks: Union[int | None, Any] = Field(default=None)
    cost_in_local_currency: Union[str | None, Any] = Field(default=None, alias="costInLocalCurrency")
    cost_in_usd: Union[str | None, Any] = Field(default=None, alias="costInUsd")
    likes: Union[int | None, Any] = Field(default=None)
    shares: Union[int | None, Any] = Field(default=None)
    comments: Union[int | None, Any] = Field(default=None)
    reactions: Union[int | None, Any] = Field(default=None)
    follows: Union[int | None, Any] = Field(default=None)
    total_engagements: Union[int | None, Any] = Field(default=None, alias="totalEngagements")
    landing_page_clicks: Union[int | None, Any] = Field(default=None, alias="landingPageClicks")
    company_page_clicks: Union[int | None, Any] = Field(default=None, alias="companyPageClicks")
    external_website_conversions: Union[int | None, Any] = Field(default=None, alias="externalWebsiteConversions")
    external_website_post_click_conversions: Union[int | None, Any] = Field(default=None, alias="externalWebsitePostClickConversions")
    external_website_post_view_conversions: Union[int | None, Any] = Field(default=None, alias="externalWebsitePostViewConversions")
    conversion_value_in_local_currency: Union[str | None, Any] = Field(default=None, alias="conversionValueInLocalCurrency")
    approximate_member_reach: Union[int | None, Any] = Field(default=None, alias="approximateMemberReach")
    card_clicks: Union[int | None, Any] = Field(default=None, alias="cardClicks")
    card_impressions: Union[int | None, Any] = Field(default=None, alias="cardImpressions")
    video_starts: Union[int | None, Any] = Field(default=None, alias="videoStarts")
    video_views: Union[int | None, Any] = Field(default=None, alias="videoViews")
    video_first_quartile_completions: Union[int | None, Any] = Field(default=None, alias="videoFirstQuartileCompletions")
    video_midpoint_completions: Union[int | None, Any] = Field(default=None, alias="videoMidpointCompletions")
    video_third_quartile_completions: Union[int | None, Any] = Field(default=None, alias="videoThirdQuartileCompletions")
    video_completions: Union[int | None, Any] = Field(default=None, alias="videoCompletions")
    full_screen_plays: Union[int | None, Any] = Field(default=None, alias="fullScreenPlays")
    one_click_leads: Union[int | None, Any] = Field(default=None, alias="oneClickLeads")
    one_click_lead_form_opens: Union[int | None, Any] = Field(default=None, alias="oneClickLeadFormOpens")
    other_engagements: Union[int | None, Any] = Field(default=None, alias="otherEngagements")
    ad_unit_clicks: Union[int | None, Any] = Field(default=None, alias="adUnitClicks")
    action_clicks: Union[int | None, Any] = Field(default=None, alias="actionClicks")
    text_url_clicks: Union[int | None, Any] = Field(default=None, alias="textUrlClicks")
    comment_likes: Union[int | None, Any] = Field(default=None, alias="commentLikes")
    sends: Union[int | None, Any] = Field(default=None)
    opens: Union[int | None, Any] = Field(default=None)
    download_clicks: Union[int | None, Any] = Field(default=None, alias="downloadClicks")
    job_applications: Union[int | None, Any] = Field(default=None, alias="jobApplications")
    job_apply_clicks: Union[int | None, Any] = Field(default=None, alias="jobApplyClicks")
    registrations: Union[int | None, Any] = Field(default=None)
    talent_leads: Union[int | None, Any] = Field(default=None, alias="talentLeads")
    valid_work_email_leads: Union[int | None, Any] = Field(default=None, alias="validWorkEmailLeads")
    post_click_job_applications: Union[int | None, Any] = Field(default=None, alias="postClickJobApplications")
    post_click_job_apply_clicks: Union[int | None, Any] = Field(default=None, alias="postClickJobApplyClicks")
    post_click_registrations: Union[int | None, Any] = Field(default=None, alias="postClickRegistrations")
    post_view_job_applications: Union[int | None, Any] = Field(default=None, alias="postViewJobApplications")
    post_view_job_apply_clicks: Union[int | None, Any] = Field(default=None, alias="postViewJobApplyClicks")
    post_view_registrations: Union[int | None, Any] = Field(default=None, alias="postViewRegistrations")
    lead_generation_mail_contact_info_shares: Union[int | None, Any] = Field(default=None, alias="leadGenerationMailContactInfoShares")
    lead_generation_mail_interested_clicks: Union[int | None, Any] = Field(default=None, alias="leadGenerationMailInterestedClicks")
    document_completions: Union[int | None, Any] = Field(default=None, alias="documentCompletions")
    document_first_quartile_completions: Union[int | None, Any] = Field(default=None, alias="documentFirstQuartileCompletions")
    document_midpoint_completions: Union[int | None, Any] = Field(default=None, alias="documentMidpointCompletions")
    document_third_quartile_completions: Union[int | None, Any] = Field(default=None, alias="documentThirdQuartileCompletions")

class AdAnalyticsResponsePaging(BaseModel):
    """Nested schema for AdAnalyticsResponse.paging"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    count: Union[int, Any] = Field(default=None)
    start: Union[int, Any] = Field(default=None)

class AdAnalyticsResponse(BaseModel):
    """Ad analytics API response"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    elements: Union[list[AdAnalyticsRecord], Any] = Field(default=None)
    paging: Union[AdAnalyticsResponsePaging, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class AccountUsersListResultMeta(BaseModel):
    """Metadata for account_users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class CampaignGroupsListResultMeta(BaseModel):
    """Metadata for campaign_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class CreativesListResultMeta(BaseModel):
    """Metadata for creatives.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str, Any] = Field(default=None, alias="nextPageToken")

class ConversionsListResultMeta(BaseModel):
    """Metadata for conversions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)

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
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique account identifier"""
    name: str | None = None
    """Account name"""
    currency: str | None = None
    """Currency code used by the account"""
    status: str | None = None
    """Account status"""
    type_: str | None = None
    """Account type"""
    reference: str | None = None
    """Reference organization URN"""
    test: bool | None = None
    """Whether this is a test account"""
    notified_on_campaign_optimization: bool | None = None
    """Flag for notifications on campaign optimization"""
    notified_on_creative_approval: bool | None = None
    """Flag for notifications on creative approval"""
    notified_on_creative_rejection: bool | None = None
    """Flag for notifications on creative rejection"""
    notified_on_end_of_campaign: bool | None = None
    """Flag for notifications on end of campaign"""
    notified_on_new_features_enabled: bool | None = None
    """Flag for notifications on new features"""
    serving_statuses: list[Any] | None = None
    """List of serving statuses"""
    version: dict[str, Any] | None = None
    """Version information"""


class AccountUsersSearchData(BaseModel):
    """Search result data for account_users entity."""
    model_config = ConfigDict(extra="allow")

    account: str | None = None
    """Associated account URN"""
    user: str | None = None
    """User URN"""
    role: str | None = None
    """User role in the account"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique campaign identifier"""
    name: str | None = None
    """Campaign name"""
    account: str | None = None
    """Associated account URN"""
    campaign_group: str | None = None
    """Parent campaign group URN"""
    status: str | None = None
    """Campaign status"""
    type_: str | None = None
    """Campaign type"""
    cost_type: str | None = None
    """Cost type (CPC CPM etc)"""
    format: str | None = None
    """Campaign ad format"""
    objective_type: str | None = None
    """Campaign objective type"""
    optimization_target_type: str | None = None
    """Optimization target type"""
    creative_selection: str | None = None
    """Creative selection mode"""
    pacing_strategy: str | None = None
    """Budget pacing strategy"""
    audience_expansion_enabled: bool | None = None
    """Whether audience expansion is enabled"""
    offsite_delivery_enabled: bool | None = None
    """Whether offsite delivery is enabled"""
    story_delivery_enabled: bool | None = None
    """Whether story delivery is enabled"""
    test: bool | None = None
    """Whether this is a test campaign"""
    associated_entity: str | None = None
    """Associated entity URN"""
    daily_budget: dict[str, Any] | None = None
    """Daily budget configuration"""
    total_budget: dict[str, Any] | None = None
    """Total budget configuration"""
    unit_cost: dict[str, Any] | None = None
    """Cost per unit (bid amount)"""
    run_schedule: dict[str, Any] | None = None
    """Campaign run schedule"""
    locale: dict[str, Any] | None = None
    """Campaign locale settings"""
    serving_statuses: list[Any] | None = None
    """List of serving statuses"""
    version: dict[str, Any] | None = None
    """Version information"""


class CampaignGroupsSearchData(BaseModel):
    """Search result data for campaign_groups entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique campaign group identifier"""
    name: str | None = None
    """Campaign group name"""
    account: str | None = None
    """Associated account URN"""
    status: str | None = None
    """Campaign group status"""
    test: bool | None = None
    """Whether this is a test campaign group"""
    backfilled: bool | None = None
    """Whether the campaign group is backfilled"""
    total_budget: dict[str, Any] | None = None
    """Total budget for the campaign group"""
    run_schedule: dict[str, Any] | None = None
    """Campaign group run schedule"""
    serving_statuses: list[Any] | None = None
    """List of serving statuses"""
    allowed_campaign_types: list[Any] | None = None
    """Types of campaigns allowed in this group"""


class CreativesSearchData(BaseModel):
    """Search result data for creatives entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique creative identifier"""
    name: str | None = None
    """Creative name"""
    account: str | None = None
    """Associated account URN"""
    campaign: str | None = None
    """Parent campaign URN"""
    intended_status: str | None = None
    """Intended creative status"""
    is_serving: bool | None = None
    """Whether the creative is currently serving"""
    is_test: bool | None = None
    """Whether this is a test creative"""
    created_at: int | None = None
    """Creation timestamp (epoch milliseconds)"""
    created_by: str | None = None
    """URN of the user who created the creative"""
    last_modified_at: int | None = None
    """Last modification timestamp (epoch milliseconds)"""
    last_modified_by: str | None = None
    """URN of the user who last modified the creative"""
    content: dict[str, Any] | None = None
    """Creative content configuration"""
    serving_hold_reasons: list[Any] | None = None
    """Reasons for holding creative from serving"""


class ConversionsSearchData(BaseModel):
    """Search result data for conversions entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique conversion identifier"""
    name: str | None = None
    """Conversion name"""
    account: str | None = None
    """Associated account URN"""
    type_: str | None = None
    """Conversion type"""
    attribution_type: str | None = None
    """Attribution type for the conversion"""
    enabled: bool | None = None
    """Whether the conversion tracking is enabled"""
    created: int | None = None
    """Creation timestamp (epoch milliseconds)"""
    last_modified: int | None = None
    """Last modification timestamp (epoch milliseconds)"""
    post_click_attribution_window_size: int | None = None
    """Post-click attribution window size in days"""
    view_through_attribution_window_size: int | None = None
    """View-through attribution window size in days"""
    campaigns: list[Any] | None = None
    """Related campaign URNs"""
    associated_campaigns: list[Any] | None = None
    """Associated campaigns"""
    image_pixel_tag: str | None = None
    """Image pixel tracking tag"""
    value: dict[str, Any] | None = None
    """Conversion value"""


class AdCampaignAnalyticsSearchData(BaseModel):
    """Search result data for ad_campaign_analytics entity."""
    model_config = ConfigDict(extra="allow")

    impressions: float | None = None
    """Number of times the ad was shown"""
    clicks: float | None = None
    """Number of clicks on the ad"""
    cost_in_local_currency: float | None = None
    """Total cost in the accounts local currency"""
    cost_in_usd: float | None = None
    """Total cost in USD"""
    likes: float | None = None
    """Number of likes"""
    shares: float | None = None
    """Number of shares"""
    comments: float | None = None
    """Number of comments"""
    reactions: float | None = None
    """Number of reactions"""
    follows: float | None = None
    """Number of follows"""
    total_engagements: float | None = None
    """Total number of engagements"""
    landing_page_clicks: float | None = None
    """Number of landing page clicks"""
    company_page_clicks: float | None = None
    """Number of company page clicks"""
    external_website_conversions: float | None = None
    """Number of conversions on external websites"""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in local currency"""
    approximate_member_reach: float | None = None
    """Approximate unique member reach"""
    card_clicks: float | None = None
    """Number of carousel card clicks"""
    card_impressions: float | None = None
    """Number of carousel card impressions"""
    video_starts: float | None = None
    """Number of video starts"""
    video_views: float | None = None
    """Number of video views"""
    video_first_quartile_completions: float | None = None
    """Number of times video played to 25%"""
    video_midpoint_completions: float | None = None
    """Number of times video played to 50%"""
    video_third_quartile_completions: float | None = None
    """Number of times video played to 75%"""
    video_completions: float | None = None
    """Number of times video played to 100%"""
    full_screen_plays: float | None = None
    """Number of full screen video plays"""
    one_click_leads: float | None = None
    """Number of one-click leads"""
    one_click_lead_form_opens: float | None = None
    """Number of one-click lead form opens"""
    other_engagements: float | None = None
    """Number of other engagements"""
    ad_unit_clicks: float | None = None
    """Number of ad unit clicks"""
    action_clicks: float | None = None
    """Number of action clicks"""
    text_url_clicks: float | None = None
    """Number of text URL clicks"""
    comment_likes: float | None = None
    """Number of comment likes"""
    sends: float | None = None
    """Number of sends (InMail)"""
    opens: float | None = None
    """Number of opens (InMail)"""
    download_clicks: float | None = None
    """Number of download clicks"""
    pivot_values: list[Any] | None = None
    """Pivot values (URNs) for this analytics record"""
    start_date: str | None = None
    """Start date of the ad analytics data"""
    end_date: str | None = None
    """End date of the ad analytics data"""


class AdCreativeAnalyticsSearchData(BaseModel):
    """Search result data for ad_creative_analytics entity."""
    model_config = ConfigDict(extra="allow")

    impressions: float | None = None
    """Number of times the ad was shown"""
    clicks: float | None = None
    """Number of clicks on the ad"""
    cost_in_local_currency: float | None = None
    """Total cost in the accounts local currency"""
    cost_in_usd: float | None = None
    """Total cost in USD"""
    likes: float | None = None
    """Number of likes"""
    shares: float | None = None
    """Number of shares"""
    comments: float | None = None
    """Number of comments"""
    reactions: float | None = None
    """Number of reactions"""
    follows: float | None = None
    """Number of follows"""
    total_engagements: float | None = None
    """Total number of engagements"""
    landing_page_clicks: float | None = None
    """Number of landing page clicks"""
    company_page_clicks: float | None = None
    """Number of company page clicks"""
    external_website_conversions: float | None = None
    """Number of conversions on external websites"""
    external_website_post_click_conversions: float | None = None
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: float | None = None
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: float | None = None
    """Conversion value in local currency"""
    approximate_member_reach: float | None = None
    """Approximate unique member reach"""
    card_clicks: float | None = None
    """Number of carousel card clicks"""
    card_impressions: float | None = None
    """Number of carousel card impressions"""
    video_starts: float | None = None
    """Number of video starts"""
    video_views: float | None = None
    """Number of video views"""
    video_first_quartile_completions: float | None = None
    """Number of times video played to 25%"""
    video_midpoint_completions: float | None = None
    """Number of times video played to 50%"""
    video_third_quartile_completions: float | None = None
    """Number of times video played to 75%"""
    video_completions: float | None = None
    """Number of times video played to 100%"""
    full_screen_plays: float | None = None
    """Number of full screen video plays"""
    one_click_leads: float | None = None
    """Number of one-click leads"""
    one_click_lead_form_opens: float | None = None
    """Number of one-click lead form opens"""
    other_engagements: float | None = None
    """Number of other engagements"""
    ad_unit_clicks: float | None = None
    """Number of ad unit clicks"""
    action_clicks: float | None = None
    """Number of action clicks"""
    text_url_clicks: float | None = None
    """Number of text URL clicks"""
    comment_likes: float | None = None
    """Number of comment likes"""
    sends: float | None = None
    """Number of sends (InMail)"""
    opens: float | None = None
    """Number of opens (InMail)"""
    download_clicks: float | None = None
    """Number of download clicks"""
    pivot_values: list[Any] | None = None
    """Pivot values (URNs) for this analytics record"""
    start_date: str | None = None
    """Start date of the ad analytics data"""
    end_date: str | None = None
    """End date of the ad analytics data"""


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



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AccountsListResult = LinkedinAdsExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

AccountUsersListResult = LinkedinAdsExecuteResultWithMeta[list[AccountUser], AccountUsersListResultMeta]
"""Result type for account_users.list operation with data and metadata."""

CampaignsListResult = LinkedinAdsExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

CampaignGroupsListResult = LinkedinAdsExecuteResultWithMeta[list[CampaignGroup], CampaignGroupsListResultMeta]
"""Result type for campaign_groups.list operation with data and metadata."""

CreativesListResult = LinkedinAdsExecuteResultWithMeta[list[Creative], CreativesListResultMeta]
"""Result type for creatives.list operation with data and metadata."""

ConversionsListResult = LinkedinAdsExecuteResultWithMeta[list[Conversion], ConversionsListResultMeta]
"""Result type for conversions.list operation with data and metadata."""

AdCampaignAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_campaign_analytics.list operation."""

AdCreativeAnalyticsListResult = LinkedinAdsExecuteResult[list[AdAnalyticsRecord]]
"""Result type for ad_creative_analytics.list operation."""

