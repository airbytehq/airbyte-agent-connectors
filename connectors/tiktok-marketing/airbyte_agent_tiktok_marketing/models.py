"""
Pydantic models for tiktok-marketing connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class TiktokMarketingAuthConfig(BaseModel):
    """OAuth Access Token"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Your TikTok Marketing API access token"""

# Replication configuration

class TiktokMarketingReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from TikTok Marketing."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """The start date in YYYY-MM-DD format. Any data before this date will not be replicated. If not set, defaults to 2016-09-01."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Advertiser(BaseModel):
    """TikTok advertiser account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    advertiser_id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    address: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    contacter: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    industry: Union[str | None, Any] = Field(default=None)
    language: Union[str | None, Any] = Field(default=None)
    license_no: Union[str | None, Any] = Field(default=None)
    license_url: Union[str | None, Any] = Field(default=None)
    cellphone_number: Union[str | None, Any] = Field(default=None)
    promotion_area: Union[str | None, Any] = Field(default=None)
    rejection_reason: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    timezone: Union[str | None, Any] = Field(default=None)
    balance: Union[float, Any] = Field(default=None)
    create_time: Union[int, Any] = Field(default=None)
    telephone_number: Union[str | None, Any] = Field(default=None)
    display_timezone: Union[str | None, Any] = Field(default=None)
    promotion_center_province: Union[str | None, Any] = Field(default=None)
    advertiser_account_type: Union[str | None, Any] = Field(default=None)
    license_city: Union[str | None, Any] = Field(default=None)
    brand: Union[str | None, Any] = Field(default=None)
    license_province: Union[str | None, Any] = Field(default=None)
    promotion_center_city: Union[str | None, Any] = Field(default=None)

class Campaign(BaseModel):
    """TikTok marketing campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: Union[str, Any] = Field(default=None)
    campaign_name: Union[str, Any] = Field(default=None)
    campaign_type: Union[str, Any] = Field(default=None)
    advertiser_id: Union[str, Any] = Field(default=None)
    budget: Union[float, Any] = Field(default=None)
    budget_mode: Union[str, Any] = Field(default=None)
    secondary_status: Union[str, Any] = Field(default=None)
    operation_status: Union[str | None, Any] = Field(default=None)
    objective: Union[str | None, Any] = Field(default=None)
    objective_type: Union[str | None, Any] = Field(default=None)
    budget_optimize_on: Union[bool | None, Any] = Field(default=None)
    bid_type: Union[str | None, Any] = Field(default=None)
    deep_bid_type: Union[str | None, Any] = Field(default=None)
    optimization_goal: Union[str | None, Any] = Field(default=None)
    split_test_variable: Union[str | None, Any] = Field(default=None)
    is_new_structure: Union[bool, Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    modify_time: Union[str, Any] = Field(default=None)
    roas_bid: Union[float | None, Any] = Field(default=None)
    is_smart_performance_campaign: Union[bool | None, Any] = Field(default=None)
    is_search_campaign: Union[bool | None, Any] = Field(default=None)
    app_promotion_type: Union[str | None, Any] = Field(default=None)
    rf_campaign_type: Union[str | None, Any] = Field(default=None)
    disable_skan_campaign: Union[bool | None, Any] = Field(default=None)
    is_advanced_dedicated_campaign: Union[bool | None, Any] = Field(default=None)
    rta_id: Union[str | None, Any] = Field(default=None)
    campaign_automation_type: Union[str | None, Any] = Field(default=None)
    rta_bid_enabled: Union[bool | None, Any] = Field(default=None)
    rta_product_selection_enabled: Union[bool | None, Any] = Field(default=None)

class AdGroup(BaseModel):
    """TikTok ad group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    adgroup_id: Union[str, Any] = Field(default=None)
    campaign_id: Union[str, Any] = Field(default=None)
    advertiser_id: Union[str, Any] = Field(default=None)
    adgroup_name: Union[str, Any] = Field(default=None)
    placement_type: Union[str, Any] = Field(default=None)
    placements: Union[list[str] | None, Any] = Field(default=None)
    budget: Union[float, Any] = Field(default=None)
    budget_mode: Union[str, Any] = Field(default=None)
    secondary_status: Union[str, Any] = Field(default=None)
    operation_status: Union[str, Any] = Field(default=None)
    optimization_goal: Union[str, Any] = Field(default=None)
    bid_type: Union[str | None, Any] = Field(default=None)
    bid_price: Union[float, Any] = Field(default=None)
    promotion_type: Union[str, Any] = Field(default=None)
    creative_material_mode: Union[str, Any] = Field(default=None)
    schedule_type: Union[str, Any] = Field(default=None)
    schedule_start_time: Union[str, Any] = Field(default=None)
    schedule_end_time: Union[str, Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    modify_time: Union[str, Any] = Field(default=None)
    gender: Union[str | None, Any] = Field(default=None)
    age_groups: Union[list[str] | None, Any] = Field(default=None)
    languages: Union[list[str] | None, Any] = Field(default=None)
    location_ids: Union[list[str] | None, Any] = Field(default=None)
    audience_ids: Union[list[Any] | None, Any] = Field(default=None)
    excluded_audience_ids: Union[list[Any] | None, Any] = Field(default=None)
    interest_category_ids: Union[list[str] | None, Any] = Field(default=None)
    interest_keyword_ids: Union[list[Any] | None, Any] = Field(default=None)
    pixel_id: Union[str | None, Any] = Field(default=None)
    deep_bid_type: Union[str | None, Any] = Field(default=None)
    deep_cpa_bid: Union[float, Any] = Field(default=None)
    conversion_bid_price: Union[float, Any] = Field(default=None)
    billing_event: Union[str | None, Any] = Field(default=None)
    pacing: Union[str | None, Any] = Field(default=None)
    dayparting: Union[str | None, Any] = Field(default=None)
    frequency: Union[int | None, Any] = Field(default=None)
    frequency_schedule: Union[int | None, Any] = Field(default=None)
    is_new_structure: Union[bool, Any] = Field(default=None)
    is_smart_performance_campaign: Union[bool | None, Any] = Field(default=None)
    app_id: Union[str | None, Any] = Field(default=None)
    app_type: Union[str | None, Any] = Field(default=None)
    app_download_url: Union[str | None, Any] = Field(default=None)
    optimization_event: Union[str | None, Any] = Field(default=None)
    secondary_optimization_event: Union[str | None, Any] = Field(default=None)
    conversion_window: Union[str | None, Any] = Field(default=None)
    comment_disabled: Union[bool | None, Any] = Field(default=None)
    video_download_disabled: Union[bool | None, Any] = Field(default=None)
    share_disabled: Union[bool | None, Any] = Field(default=None)
    auto_targeting_enabled: Union[bool | None, Any] = Field(default=None)
    is_hfss: Union[bool | None, Any] = Field(default=None)
    search_result_enabled: Union[bool | None, Any] = Field(default=None)
    inventory_filter_enabled: Union[bool | None, Any] = Field(default=None)
    skip_learning_phase: Union[bool | None, Any] = Field(default=None)
    brand_safety_type: Union[str | None, Any] = Field(default=None)
    brand_safety_partner: Union[str | None, Any] = Field(default=None)
    campaign_name: Union[str | None, Any] = Field(default=None)
    campaign_automation_type: Union[str | None, Any] = Field(default=None)
    bid_display_mode: Union[str | None, Any] = Field(default=None)
    scheduled_budget: Union[float | None, Any] = Field(default=None)
    category_id: Union[str | None, Any] = Field(default=None)
    feed_type: Union[str | None, Any] = Field(default=None)
    delivery_mode: Union[str | None, Any] = Field(default=None)
    ios14_quota_type: Union[str | None, Any] = Field(default=None)
    spending_power: Union[str | None, Any] = Field(default=None)
    next_day_retention: Union[float | None, Any] = Field(default=None)
    rf_purchased_type: Union[str | None, Any] = Field(default=None)
    rf_estimated_cpr: Union[float | None, Any] = Field(default=None)
    rf_estimated_frequency: Union[float | None, Any] = Field(default=None)
    purchased_impression: Union[float | None, Any] = Field(default=None)
    purchased_reach: Union[float | None, Any] = Field(default=None)
    actions: Union[list[Any] | None, Any] = Field(default=None)
    network_types: Union[list[Any] | None, Any] = Field(default=None)
    operating_systems: Union[list[Any] | None, Any] = Field(default=None)
    device_model_ids: Union[list[Any] | None, Any] = Field(default=None)
    device_price_ranges: Union[list[Any] | None, Any] = Field(default=None)
    included_custom_actions: Union[list[Any] | None, Any] = Field(default=None)
    excluded_custom_actions: Union[list[Any] | None, Any] = Field(default=None)
    category_exclusion_ids: Union[list[Any] | None, Any] = Field(default=None)
    contextual_tag_ids: Union[list[Any] | None, Any] = Field(default=None)
    zipcode_ids: Union[list[Any] | None, Any] = Field(default=None)
    household_income: Union[list[Any] | None, Any] = Field(default=None)
    isp_ids: Union[list[Any] | None, Any] = Field(default=None)
    schedule_infos: Union[list[Any] | None, Any] = Field(default=None)
    statistic_type: Union[str | None, Any] = Field(default=None)
    keywords: Union[str | None, Any] = Field(default=None)
    adgroup_app_profile_page_state: Union[str | None, Any] = Field(default=None)
    automated_keywords_enabled: Union[bool | None, Any] = Field(default=None)
    smart_audience_enabled: Union[bool | None, Any] = Field(default=None)
    smart_interest_behavior_enabled: Union[bool | None, Any] = Field(default=None)
    vbo_window: Union[str | None, Any] = Field(default=None)
    deep_funnel_optimization_status: Union[str | None, Any] = Field(default=None)
    deep_funnel_event_source: Union[str | None, Any] = Field(default=None)
    deep_funnel_event_source_id: Union[str | None, Any] = Field(default=None)
    deep_funnel_optimization_event: Union[str | None, Any] = Field(default=None)
    custom_conversion_id: Union[str | None, Any] = Field(default=None)
    app_config: Union[dict[str, Any] | None, Any] = Field(default=None)

class Ad(BaseModel):
    """TikTok ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_id: Union[str, Any] = Field(default=None)
    advertiser_id: Union[str, Any] = Field(default=None)
    campaign_id: Union[str, Any] = Field(default=None)
    campaign_name: Union[str, Any] = Field(default=None)
    adgroup_id: Union[str, Any] = Field(default=None)
    adgroup_name: Union[str, Any] = Field(default=None)
    ad_name: Union[str, Any] = Field(default=None)
    ad_text: Union[str | None, Any] = Field(default=None)
    ad_texts: Union[list[Any] | None, Any] = Field(default=None)
    ad_format: Union[str | None, Any] = Field(default=None)
    secondary_status: Union[str, Any] = Field(default=None)
    operation_status: Union[str | None, Any] = Field(default=None)
    call_to_action: Union[str | None, Any] = Field(default=None)
    call_to_action_id: Union[str | None, Any] = Field(default=None)
    landing_page_url: Union[str | None, Any] = Field(default=None)
    landing_page_urls: Union[list[Any] | None, Any] = Field(default=None)
    display_name: Union[str | None, Any] = Field(default=None)
    profile_image_url: Union[str | None, Any] = Field(default=None)
    video_id: Union[str | None, Any] = Field(default=None)
    image_ids: Union[list[str] | None, Any] = Field(default=None)
    image_mode: Union[str | None, Any] = Field(default=None)
    is_aco: Union[bool | None, Any] = Field(default=None)
    is_new_structure: Union[bool | None, Any] = Field(default=None)
    creative_type: Union[str | None, Any] = Field(default=None)
    creative_authorized: Union[bool | None, Any] = Field(default=None)
    identity_id: Union[str | None, Any] = Field(default=None)
    identity_type: Union[str | None, Any] = Field(default=None)
    deeplink: Union[str | None, Any] = Field(default=None)
    deeplink_type: Union[str | None, Any] = Field(default=None)
    fallback_type: Union[str | None, Any] = Field(default=None)
    tracking_pixel_id: Union[int | None, Any] = Field(default=None)
    impression_tracking_url: Union[str | None, Any] = Field(default=None)
    click_tracking_url: Union[str | None, Any] = Field(default=None)
    music_id: Union[str | None, Any] = Field(default=None)
    optimization_event: Union[str | None, Any] = Field(default=None)
    vast_moat_enabled: Union[bool | None, Any] = Field(default=None)
    page_id: Union[str | None, Any] = Field(default=None)
    viewability_postbid_partner: Union[str | None, Any] = Field(default=None)
    viewability_vast_url: Union[str | None, Any] = Field(default=None)
    brand_safety_postbid_partner: Union[str | None, Any] = Field(default=None)
    brand_safety_vast_url: Union[str | None, Any] = Field(default=None)
    app_name: Union[str | None, Any] = Field(default=None)
    playable_url: Union[str | None, Any] = Field(default=None)
    card_id: Union[str | None, Any] = Field(default=None)
    carousel_image_labels: Union[list[Any] | None, Any] = Field(default=None)
    avatar_icon_web_uri: Union[str | None, Any] = Field(default=None)
    campaign_automation_type: Union[str | None, Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    modify_time: Union[str, Any] = Field(default=None)

class Audience(BaseModel):
    """TikTok custom audience"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    audience_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    audience_type: Union[str | None, Any] = Field(default=None)
    cover_num: Union[int | None, Any] = Field(default=None)
    is_valid: Union[bool | None, Any] = Field(default=None)
    is_expiring: Union[bool | None, Any] = Field(default=None)
    is_creator: Union[bool | None, Any] = Field(default=None)
    shared: Union[bool | None, Any] = Field(default=None)
    calculate_type: Union[str | None, Any] = Field(default=None)
    create_time: Union[str | None, Any] = Field(default=None)
    expired_time: Union[str | None, Any] = Field(default=None)

class CreativeAssetImage(BaseModel):
    """TikTok creative asset image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    image_id: Union[str | None, Any] = Field(default=None)
    format: Union[str | None, Any] = Field(default=None)
    image_url: Union[str | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)
    signature: Union[str | None, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)
    material_id: Union[str | None, Any] = Field(default=None)
    is_carousel_usable: Union[bool | None, Any] = Field(default=None)
    file_name: Union[str | None, Any] = Field(default=None)
    create_time: Union[str | None, Any] = Field(default=None)
    modify_time: Union[str | None, Any] = Field(default=None)
    displayable: Union[bool | None, Any] = Field(default=None)

class CreativeAssetVideo(BaseModel):
    """TikTok creative asset video"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    video_id: Union[str | None, Any] = Field(default=None)
    video_cover_url: Union[str | None, Any] = Field(default=None)
    format: Union[str | None, Any] = Field(default=None)
    preview_url: Union[str | None, Any] = Field(default=None)
    preview_url_expire_time: Union[str | None, Any] = Field(default=None)
    duration: Union[float | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)
    bit_rate: Union[float | None, Any] = Field(default=None)
    signature: Union[str | None, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)
    material_id: Union[str | None, Any] = Field(default=None)
    allowed_placements: Union[list[str | None] | None, Any] = Field(default=None)
    allow_download: Union[bool | None, Any] = Field(default=None)
    file_name: Union[str | None, Any] = Field(default=None)
    create_time: Union[str | None, Any] = Field(default=None)
    modify_time: Union[str | None, Any] = Field(default=None)
    displayable: Union[bool | None, Any] = Field(default=None)
    fix_task_id: Union[str | None, Any] = Field(default=None)
    flaw_types: Union[list[Any] | None, Any] = Field(default=None)

class AdvertisersReportDaily(BaseModel):
    """Daily performance report at the advertiser level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    advertiser_id: Union[int | None, Any] = Field(default=None)
    stat_time_day: Union[str | None, Any] = Field(default=None)
    spend: Union[str | None, Any] = Field(default=None)
    cash_spend: Union[str | None, Any] = Field(default=None)
    voucher_spend: Union[str | None, Any] = Field(default=None)
    cpc: Union[str | None, Any] = Field(default=None)
    cpm: Union[str | None, Any] = Field(default=None)
    impressions: Union[str | None, Any] = Field(default=None)
    clicks: Union[str | None, Any] = Field(default=None)
    ctr: Union[str | None, Any] = Field(default=None)
    reach: Union[str | None, Any] = Field(default=None)
    cost_per_1000_reached: Union[str | None, Any] = Field(default=None)
    frequency: Union[str | None, Any] = Field(default=None)
    video_play_actions: Union[float | None, Any] = Field(default=None)
    video_watched_2s: Union[float | None, Any] = Field(default=None)
    video_watched_6s: Union[float | None, Any] = Field(default=None)
    average_video_play: Union[float | None, Any] = Field(default=None)
    average_video_play_per_user: Union[float | None, Any] = Field(default=None)
    video_views_p25: Union[float | None, Any] = Field(default=None)
    video_views_p50: Union[float | None, Any] = Field(default=None)
    video_views_p75: Union[float | None, Any] = Field(default=None)
    video_views_p100: Union[float | None, Any] = Field(default=None)
    profile_visits: Union[float | None, Any] = Field(default=None)
    likes: Union[float | None, Any] = Field(default=None)
    comments: Union[float | None, Any] = Field(default=None)
    shares: Union[float | None, Any] = Field(default=None)
    follows: Union[float | None, Any] = Field(default=None)
    clicks_on_music_disc: Union[float | None, Any] = Field(default=None)
    real_time_app_install: Union[float | None, Any] = Field(default=None)
    real_time_app_install_cost: Union[float | None, Any] = Field(default=None)
    app_install: Union[float | None, Any] = Field(default=None)

class CampaignsReportDaily(BaseModel):
    """Daily performance report at the campaign level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: Union[int | None, Any] = Field(default=None)
    stat_time_day: Union[str | None, Any] = Field(default=None)
    campaign_name: Union[str | None, Any] = Field(default=None)
    spend: Union[str | None, Any] = Field(default=None)
    cpc: Union[str | None, Any] = Field(default=None)
    cpm: Union[str | None, Any] = Field(default=None)
    impressions: Union[str | None, Any] = Field(default=None)
    clicks: Union[str | None, Any] = Field(default=None)
    ctr: Union[str | None, Any] = Field(default=None)
    reach: Union[str | None, Any] = Field(default=None)
    cost_per_1000_reached: Union[str | None, Any] = Field(default=None)
    frequency: Union[str | None, Any] = Field(default=None)
    video_play_actions: Union[float | None, Any] = Field(default=None)
    video_watched_2s: Union[float | None, Any] = Field(default=None)
    video_watched_6s: Union[float | None, Any] = Field(default=None)
    average_video_play: Union[float | None, Any] = Field(default=None)
    average_video_play_per_user: Union[float | None, Any] = Field(default=None)
    video_views_p25: Union[float | None, Any] = Field(default=None)
    video_views_p50: Union[float | None, Any] = Field(default=None)
    video_views_p75: Union[float | None, Any] = Field(default=None)
    video_views_p100: Union[float | None, Any] = Field(default=None)
    profile_visits: Union[float | None, Any] = Field(default=None)
    likes: Union[float | None, Any] = Field(default=None)
    comments: Union[float | None, Any] = Field(default=None)
    shares: Union[float | None, Any] = Field(default=None)
    follows: Union[float | None, Any] = Field(default=None)
    clicks_on_music_disc: Union[float | None, Any] = Field(default=None)
    real_time_app_install: Union[float | None, Any] = Field(default=None)
    real_time_app_install_cost: Union[float | None, Any] = Field(default=None)
    app_install: Union[float | None, Any] = Field(default=None)

class AdGroupsReportDaily(BaseModel):
    """Daily performance report at the ad group level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    adgroup_id: Union[int | None, Any] = Field(default=None)
    stat_time_day: Union[str | None, Any] = Field(default=None)
    campaign_name: Union[str | None, Any] = Field(default=None)
    campaign_id: Union[int | None, Any] = Field(default=None)
    adgroup_name: Union[str | None, Any] = Field(default=None)
    placement_type: Union[str | None, Any] = Field(default=None)
    spend: Union[str | None, Any] = Field(default=None)
    cpc: Union[str | None, Any] = Field(default=None)
    cpm: Union[str | None, Any] = Field(default=None)
    impressions: Union[str | None, Any] = Field(default=None)
    clicks: Union[str | None, Any] = Field(default=None)
    ctr: Union[str | None, Any] = Field(default=None)
    reach: Union[str | None, Any] = Field(default=None)
    cost_per_1000_reached: Union[str | None, Any] = Field(default=None)
    conversion: Union[str | None, Any] = Field(default=None)
    cost_per_conversion: Union[str | None, Any] = Field(default=None)
    conversion_rate: Union[str | None, Any] = Field(default=None)
    real_time_conversion: Union[str | None, Any] = Field(default=None)
    real_time_cost_per_conversion: Union[str | None, Any] = Field(default=None)
    real_time_conversion_rate: Union[str | None, Any] = Field(default=None)
    result: Union[str | None, Any] = Field(default=None)
    cost_per_result: Union[str | None, Any] = Field(default=None)
    result_rate: Union[str | None, Any] = Field(default=None)
    real_time_result: Union[str | None, Any] = Field(default=None)
    real_time_cost_per_result: Union[str | None, Any] = Field(default=None)
    real_time_result_rate: Union[str | None, Any] = Field(default=None)
    secondary_goal_result: Union[str | None, Any] = Field(default=None)
    cost_per_secondary_goal_result: Union[str | None, Any] = Field(default=None)
    secondary_goal_result_rate: Union[str | None, Any] = Field(default=None)
    frequency: Union[str | None, Any] = Field(default=None)
    video_play_actions: Union[float | None, Any] = Field(default=None)
    video_watched_2s: Union[float | None, Any] = Field(default=None)
    video_watched_6s: Union[float | None, Any] = Field(default=None)
    average_video_play: Union[float | None, Any] = Field(default=None)
    average_video_play_per_user: Union[float | None, Any] = Field(default=None)
    video_views_p25: Union[float | None, Any] = Field(default=None)
    video_views_p50: Union[float | None, Any] = Field(default=None)
    video_views_p75: Union[float | None, Any] = Field(default=None)
    video_views_p100: Union[float | None, Any] = Field(default=None)
    profile_visits: Union[float | None, Any] = Field(default=None)
    likes: Union[float | None, Any] = Field(default=None)
    comments: Union[float | None, Any] = Field(default=None)
    shares: Union[float | None, Any] = Field(default=None)
    follows: Union[float | None, Any] = Field(default=None)
    clicks_on_music_disc: Union[float | None, Any] = Field(default=None)
    real_time_app_install: Union[float | None, Any] = Field(default=None)
    real_time_app_install_cost: Union[float | None, Any] = Field(default=None)
    app_install: Union[float | None, Any] = Field(default=None)

class AdsReportDaily(BaseModel):
    """Daily performance report at the ad level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_id: Union[int | None, Any] = Field(default=None)
    stat_time_day: Union[str | None, Any] = Field(default=None)
    campaign_name: Union[str | None, Any] = Field(default=None)
    campaign_id: Union[int | None, Any] = Field(default=None)
    adgroup_name: Union[str | None, Any] = Field(default=None)
    adgroup_id: Union[int | None, Any] = Field(default=None)
    ad_name: Union[str | None, Any] = Field(default=None)
    ad_text: Union[str | None, Any] = Field(default=None)
    placement_type: Union[str | None, Any] = Field(default=None)
    spend: Union[str | None, Any] = Field(default=None)
    cpc: Union[str | None, Any] = Field(default=None)
    cpm: Union[str | None, Any] = Field(default=None)
    impressions: Union[str | None, Any] = Field(default=None)
    clicks: Union[str | None, Any] = Field(default=None)
    ctr: Union[str | None, Any] = Field(default=None)
    reach: Union[str | None, Any] = Field(default=None)
    cost_per_1000_reached: Union[str | None, Any] = Field(default=None)
    conversion: Union[str | None, Any] = Field(default=None)
    cost_per_conversion: Union[str | None, Any] = Field(default=None)
    conversion_rate: Union[str | None, Any] = Field(default=None)
    real_time_conversion: Union[str | None, Any] = Field(default=None)
    real_time_cost_per_conversion: Union[str | None, Any] = Field(default=None)
    real_time_conversion_rate: Union[str | None, Any] = Field(default=None)
    result: Union[str | None, Any] = Field(default=None)
    cost_per_result: Union[str | None, Any] = Field(default=None)
    result_rate: Union[str | None, Any] = Field(default=None)
    real_time_result: Union[str | None, Any] = Field(default=None)
    real_time_cost_per_result: Union[str | None, Any] = Field(default=None)
    real_time_result_rate: Union[str | None, Any] = Field(default=None)
    secondary_goal_result: Union[str | None, Any] = Field(default=None)
    cost_per_secondary_goal_result: Union[str | None, Any] = Field(default=None)
    secondary_goal_result_rate: Union[str | None, Any] = Field(default=None)
    frequency: Union[str | None, Any] = Field(default=None)
    video_play_actions: Union[float | None, Any] = Field(default=None)
    video_watched_2s: Union[float | None, Any] = Field(default=None)
    video_watched_6s: Union[float | None, Any] = Field(default=None)
    average_video_play: Union[float | None, Any] = Field(default=None)
    average_video_play_per_user: Union[float | None, Any] = Field(default=None)
    video_views_p25: Union[float | None, Any] = Field(default=None)
    video_views_p50: Union[float | None, Any] = Field(default=None)
    video_views_p75: Union[float | None, Any] = Field(default=None)
    video_views_p100: Union[float | None, Any] = Field(default=None)
    profile_visits: Union[float | None, Any] = Field(default=None)
    likes: Union[float | None, Any] = Field(default=None)
    comments: Union[float | None, Any] = Field(default=None)
    shares: Union[float | None, Any] = Field(default=None)
    follows: Union[float | None, Any] = Field(default=None)
    clicks_on_music_disc: Union[float | None, Any] = Field(default=None)
    real_time_app_install: Union[float | None, Any] = Field(default=None)
    real_time_app_install_cost: Union[float | None, Any] = Field(default=None)
    app_install: Union[float | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class AdGroupsListResultMeta(BaseModel):
    """Metadata for ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class AdsListResultMeta(BaseModel):
    """Metadata for ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class AudiencesListResultMeta(BaseModel):
    """Metadata for audiences.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class CreativeAssetsImagesListResultMeta(BaseModel):
    """Metadata for creative_assets_images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class CreativeAssetsVideosListResultMeta(BaseModel):
    """Metadata for creative_assets_videos.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class AdvertisersReportsDailyListResultMeta(BaseModel):
    """Metadata for advertisers_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class CampaignsReportsDailyListResultMeta(BaseModel):
    """Metadata for campaigns_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class AdGroupsReportsDailyListResultMeta(BaseModel):
    """Metadata for ad_groups_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

class AdsReportsDailyListResultMeta(BaseModel):
    """Metadata for ads_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: Union[dict[str, Any], Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class TiktokMarketingCheckResult(BaseModel):
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


class TiktokMarketingExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class TiktokMarketingExecuteResultWithMeta(TiktokMarketingExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AdvertisersSearchData(BaseModel):
    """Search result data for advertisers entity."""
    model_config = ConfigDict(extra="allow")

    address: str | None = None
    """The physical address of the advertiser."""
    advertiser_account_type: str | None = None
    """The type of advertiser's account (e.g., individual, business)."""
    advertiser_id: int | None = None
    """Unique identifier for the advertiser."""
    balance: float | None = None
    """The current balance in the advertiser's account."""
    brand: str | None = None
    """The brand name associated with the advertiser."""
    cellphone_number: str | None = None
    """The cellphone number of the advertiser."""
    company: str | None = None
    """The name of the company associated with the advertiser."""
    contacter: str | None = None
    """The contact person for the advertiser."""
    country: str | None = None
    """The country where the advertiser is located."""
    create_time: int | None = None
    """The timestamp when the advertiser account was created."""
    currency: str | None = None
    """The currency used for transactions in the account."""
    description: str | None = None
    """A brief description or bio of the advertiser or company."""
    display_timezone: str | None = None
    """The timezone for display purposes."""
    email: str | None = None
    """The email address associated with the advertiser."""
    industry: str | None = None
    """The industry or sector the advertiser operates in."""
    language: str | None = None
    """The preferred language of communication for the advertiser."""
    license_city: str | None = None
    """The city where the advertiser's license is registered."""
    license_no: str | None = None
    """The license number of the advertiser."""
    license_province: str | None = None
    """The province or state where the advertiser's license is registered."""
    license_url: str | None = None
    """The URL link to the advertiser's license documentation."""
    name: str | None = None
    """The name of the advertiser or company."""
    promotion_area: str | None = None
    """The specific area or region where the advertiser focuses promotion."""
    promotion_center_city: str | None = None
    """The city at the center of the advertiser's promotion activities."""
    promotion_center_province: str | None = None
    """The province or state at the center of the advertiser's promotion activities."""
    rejection_reason: str | None = None
    """Reason for any advertisement rejection by the platform."""
    role: str | None = None
    """The role or position of the advertiser within the company."""
    status: str | None = None
    """The current status of the advertiser's account."""
    telephone_number: str | None = None
    """The telephone number of the advertiser."""
    timezone: str | None = None
    """The timezone setting for the advertiser's activities."""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    advertiser_id: int | None = None
    """The unique identifier of the advertiser associated with the campaign"""
    app_promotion_type: str | None = None
    """Type of app promotion being used in the campaign"""
    bid_type: str | None = None
    """Type of bid strategy being used in the campaign"""
    budget: float | None = None
    """Total budget allocated for the campaign"""
    budget_mode: str | None = None
    """Mode in which the budget is being managed (e.g., daily, lifetime)"""
    budget_optimize_on: bool | None = None
    """The metric or event that the budget optimization is based on"""
    campaign_id: int | None = None
    """The unique identifier of the campaign"""
    campaign_name: str | None = None
    """Name of the campaign for easy identification"""
    campaign_type: str | None = None
    """Type of campaign (e.g., awareness, conversion)"""
    create_time: str | None = None
    """Timestamp when the campaign was created"""
    deep_bid_type: str | None = None
    """Advanced bid type used for campaign optimization"""
    is_new_structure: bool | None = None
    """Flag indicating if the campaign utilizes a new campaign structure"""
    is_search_campaign: bool | None = None
    """Flag indicating if the campaign is a search campaign"""
    is_smart_performance_campaign: bool | None = None
    """Flag indicating if the campaign uses smart performance optimization"""
    modify_time: str | None = None
    """Timestamp when the campaign was last modified"""
    objective: str | None = None
    """The objective or goal of the campaign"""
    objective_type: str | None = None
    """Type of objective selected for the campaign"""
    operation_status: str | None = None
    """Current operational status of the campaign"""
    optimization_goal: str | None = None
    """Specific goal to be optimized for in the campaign"""
    rf_campaign_type: str | None = None
    """Type of RF (reach and frequency) campaign being run"""
    roas_bid: float | None = None
    """Return on ad spend goal set for the campaign"""
    secondary_status: str | None = None
    """Additional status information of the campaign"""
    split_test_variable: str | None = None
    """Variable being tested in a split test campaign"""


class AdGroupsSearchData(BaseModel):
    """Search result data for ad_groups entity."""
    model_config = ConfigDict(extra="allow")

    adgroup_id: int | None = None
    """The unique identifier of the ad group"""
    adgroup_name: str | None = None
    """The name of the ad group"""
    advertiser_id: int | None = None
    """The unique identifier of the advertiser"""
    budget: float | None = None
    """The allocated budget for the ad group"""
    budget_mode: str | None = None
    """The mode for managing the budget"""
    campaign_id: int | None = None
    """The unique identifier of the campaign"""
    create_time: str | None = None
    """The timestamp for when the ad group was created"""
    modify_time: str | None = None
    """The timestamp for when the ad group was last modified"""
    operation_status: str | None = None
    """The status of the operation"""
    optimization_goal: str | None = None
    """The goal set for optimization"""
    placement_type: str | None = None
    """The type of ad placement"""
    promotion_type: str | None = None
    """The type of promotion"""
    secondary_status: str | None = None
    """The secondary status of the ad group"""


class AdsSearchData(BaseModel):
    """Search result data for ads entity."""
    model_config = ConfigDict(extra="allow")

    ad_format: str | None = None
    """The format of the ad"""
    ad_id: int | None = None
    """The unique identifier of the ad"""
    ad_name: str | None = None
    """The name of the ad"""
    ad_text: str | None = None
    """The text content of the ad"""
    adgroup_id: int | None = None
    """The unique identifier of the ad group"""
    adgroup_name: str | None = None
    """The name of the ad group"""
    advertiser_id: int | None = None
    """The unique identifier of the advertiser"""
    campaign_id: int | None = None
    """The unique identifier of the campaign"""
    campaign_name: str | None = None
    """The name of the campaign"""
    create_time: str | None = None
    """The timestamp when the ad was created"""
    landing_page_url: str | None = None
    """The URL of the landing page for the ad"""
    modify_time: str | None = None
    """The timestamp when the ad was last modified"""
    operation_status: str | None = None
    """The operational status of the ad"""
    secondary_status: str | None = None
    """The secondary status of the ad"""
    video_id: str | None = None
    """The unique identifier of the video"""


class AudiencesSearchData(BaseModel):
    """Search result data for audiences entity."""
    model_config = ConfigDict(extra="allow")

    audience_id: str | None = None
    """Unique identifier for the audience"""
    audience_type: str | None = None
    """Type of audience"""
    cover_num: int | None = None
    """Number of audience members covered"""
    create_time: str | None = None
    """Timestamp indicating when the audience was created"""
    is_valid: bool | None = None
    """Flag indicating if the audience data is valid"""
    name: str | None = None
    """Name of the audience"""
    shared: bool | None = None
    """Flag indicating if the audience is shared"""


class CreativeAssetsImagesSearchData(BaseModel):
    """Search result data for creative_assets_images entity."""
    model_config = ConfigDict(extra="allow")

    create_time: str | None = None
    """The timestamp when the image was created."""
    file_name: str | None = None
    """The name of the image file."""
    format: str | None = None
    """The format type of the image file."""
    height: int | None = None
    """The height dimension of the image."""
    image_id: str | None = None
    """The unique identifier for the image."""
    image_url: str | None = None
    """The URL to access the image."""
    modify_time: str | None = None
    """The timestamp when the image was last modified."""
    size: int | None = None
    """The size of the image file."""
    width: int | None = None
    """The width dimension of the image."""


class CreativeAssetsVideosSearchData(BaseModel):
    """Search result data for creative_assets_videos entity."""
    model_config = ConfigDict(extra="allow")

    create_time: str | None = None
    """Timestamp when the video was created."""
    duration: float | None = None
    """Duration of the video in seconds."""
    file_name: str | None = None
    """Name of the video file."""
    format: str | None = None
    """Format of the video file."""
    height: int | None = None
    """Height of the video in pixels."""
    modify_time: str | None = None
    """Timestamp when the video was last modified."""
    size: int | None = None
    """Size of the video file in bytes."""
    video_cover_url: str | None = None
    """URL for the cover image of the video."""
    video_id: str | None = None
    """ID of the video."""
    width: int | None = None
    """Width of the video in pixels."""


class AdvertisersReportsDailySearchData(BaseModel):
    """Search result data for advertisers_reports_daily entity."""
    model_config = ConfigDict(extra="allow")

    advertiser_id: int | None = None
    """The unique identifier for the advertiser."""
    stat_time_day: str | None = None
    """The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format)."""
    spend: str | None = None
    """Total amount of money spent."""
    cash_spend: str | None = None
    """The amount of money spent in cash."""
    voucher_spend: str | None = None
    """Amount spent using vouchers."""
    cpc: str | None = None
    """Cost per click."""
    cpm: str | None = None
    """Cost per thousand impressions."""
    impressions: str | None = None
    """Number of times the ad was displayed."""
    clicks: str | None = None
    """Number of clicks on the ad."""
    ctr: str | None = None
    """Click-through rate."""
    reach: str | None = None
    """Total number of unique users reached."""
    cost_per_1000_reached: str | None = None
    """Cost per 1000 unique users reached."""
    frequency: str | None = None
    """Average number of times each person saw the ad."""
    video_play_actions: float | None = None
    """Number of video play actions."""
    video_watched_2s: float | None = None
    """Number of times video was watched for at least 2 seconds."""
    video_watched_6s: float | None = None
    """Number of times video was watched for at least 6 seconds."""
    average_video_play: float | None = None
    """Average video play duration."""
    average_video_play_per_user: float | None = None
    """Average video play duration per user."""
    video_views_p25: float | None = None
    """Number of times video was watched to 25%."""
    video_views_p50: float | None = None
    """Number of times video was watched to 50%."""
    video_views_p75: float | None = None
    """Number of times video was watched to 75%."""
    video_views_p100: float | None = None
    """Number of times video was watched to 100%."""
    profile_visits: float | None = None
    """Number of profile visits."""
    likes: float | None = None
    """Number of likes."""
    comments: float | None = None
    """Number of comments."""
    shares: float | None = None
    """Number of shares."""
    follows: float | None = None
    """Number of follows."""
    clicks_on_music_disc: float | None = None
    """Number of clicks on the music disc."""
    real_time_app_install: float | None = None
    """Real-time app installations."""
    real_time_app_install_cost: float | None = None
    """Cost of real-time app installations."""
    app_install: float | None = None
    """Number of app installations."""


class CampaignsReportsDailySearchData(BaseModel):
    """Search result data for campaigns_reports_daily entity."""
    model_config = ConfigDict(extra="allow")

    campaign_id: int | None = None
    """The unique identifier for the campaign."""
    stat_time_day: str | None = None
    """The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format)."""
    campaign_name: str | None = None
    """The name of the marketing campaign."""
    spend: str | None = None
    """Total amount of money spent."""
    cpc: str | None = None
    """Cost per click."""
    cpm: str | None = None
    """Cost per thousand impressions."""
    impressions: str | None = None
    """Number of times the ad was displayed."""
    clicks: str | None = None
    """Number of clicks on the ad."""
    ctr: str | None = None
    """Click-through rate."""
    reach: str | None = None
    """Total number of unique users reached."""
    cost_per_1000_reached: str | None = None
    """Cost per 1000 unique users reached."""
    frequency: str | None = None
    """Average number of times each person saw the ad."""
    video_play_actions: float | None = None
    """Number of video play actions."""
    video_watched_2s: float | None = None
    """Number of times video was watched for at least 2 seconds."""
    video_watched_6s: float | None = None
    """Number of times video was watched for at least 6 seconds."""
    average_video_play: float | None = None
    """Average video play duration."""
    average_video_play_per_user: float | None = None
    """Average video play duration per user."""
    video_views_p25: float | None = None
    """Number of times video was watched to 25%."""
    video_views_p50: float | None = None
    """Number of times video was watched to 50%."""
    video_views_p75: float | None = None
    """Number of times video was watched to 75%."""
    video_views_p100: float | None = None
    """Number of times video was watched to 100%."""
    profile_visits: float | None = None
    """Number of profile visits."""
    likes: float | None = None
    """Number of likes."""
    comments: float | None = None
    """Number of comments."""
    shares: float | None = None
    """Number of shares."""
    follows: float | None = None
    """Number of follows."""
    clicks_on_music_disc: float | None = None
    """Number of clicks on the music disc."""
    real_time_app_install: float | None = None
    """Real-time app installations."""
    real_time_app_install_cost: float | None = None
    """Cost of real-time app installations."""
    app_install: float | None = None
    """Number of app installations."""


class AdGroupsReportsDailySearchData(BaseModel):
    """Search result data for ad_groups_reports_daily entity."""
    model_config = ConfigDict(extra="allow")

    adgroup_id: int | None = None
    """The unique identifier for the ad group."""
    stat_time_day: str | None = None
    """The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format)."""
    campaign_name: str | None = None
    """The name of the marketing campaign."""
    campaign_id: int | None = None
    """The unique identifier for the campaign."""
    adgroup_name: str | None = None
    """The name of the ad group."""
    placement_type: str | None = None
    """Type of ad placement."""
    spend: str | None = None
    """Total amount of money spent."""
    cpc: str | None = None
    """Cost per click."""
    cpm: str | None = None
    """Cost per thousand impressions."""
    impressions: str | None = None
    """Number of times the ad was displayed."""
    clicks: str | None = None
    """Number of clicks on the ad."""
    ctr: str | None = None
    """Click-through rate."""
    reach: str | None = None
    """Total number of unique users reached."""
    cost_per_1000_reached: str | None = None
    """Cost per 1000 unique users reached."""
    conversion: str | None = None
    """Number of conversions."""
    cost_per_conversion: str | None = None
    """Cost per conversion."""
    conversion_rate: str | None = None
    """Rate of conversions."""
    real_time_conversion: str | None = None
    """Real-time conversions."""
    real_time_cost_per_conversion: str | None = None
    """Real-time cost per conversion."""
    real_time_conversion_rate: str | None = None
    """Real-time conversion rate."""
    result: str | None = None
    """Number of results."""
    cost_per_result: str | None = None
    """Cost per result."""
    result_rate: str | None = None
    """Rate of results."""
    real_time_result: str | None = None
    """Real-time results."""
    real_time_cost_per_result: str | None = None
    """Real-time cost per result."""
    real_time_result_rate: str | None = None
    """Real-time result rate."""
    secondary_goal_result: str | None = None
    """Results for secondary goals."""
    cost_per_secondary_goal_result: str | None = None
    """Cost per secondary goal result."""
    secondary_goal_result_rate: str | None = None
    """Rate of secondary goal results."""
    frequency: str | None = None
    """Average number of times each person saw the ad."""
    video_play_actions: float | None = None
    """Number of video play actions."""
    video_watched_2s: float | None = None
    """Number of times video was watched for at least 2 seconds."""
    video_watched_6s: float | None = None
    """Number of times video was watched for at least 6 seconds."""
    average_video_play: float | None = None
    """Average video play duration."""
    average_video_play_per_user: float | None = None
    """Average video play duration per user."""
    video_views_p25: float | None = None
    """Number of times video was watched to 25%."""
    video_views_p50: float | None = None
    """Number of times video was watched to 50%."""
    video_views_p75: float | None = None
    """Number of times video was watched to 75%."""
    video_views_p100: float | None = None
    """Number of times video was watched to 100%."""
    profile_visits: float | None = None
    """Number of profile visits."""
    likes: float | None = None
    """Number of likes."""
    comments: float | None = None
    """Number of comments."""
    shares: float | None = None
    """Number of shares."""
    follows: float | None = None
    """Number of follows."""
    clicks_on_music_disc: float | None = None
    """Number of clicks on the music disc."""
    real_time_app_install: float | None = None
    """Real-time app installations."""
    real_time_app_install_cost: float | None = None
    """Cost of real-time app installations."""
    app_install: float | None = None
    """Number of app installations."""


class AdsReportsDailySearchData(BaseModel):
    """Search result data for ads_reports_daily entity."""
    model_config = ConfigDict(extra="allow")

    ad_id: int | None = None
    """The unique identifier for the ad."""
    stat_time_day: str | None = None
    """The date for which the statistical data is recorded (YYYY-MM-DD HH:MM:SS format)."""
    campaign_name: str | None = None
    """The name of the marketing campaign."""
    campaign_id: int | None = None
    """The unique identifier for the campaign."""
    adgroup_name: str | None = None
    """The name of the ad group."""
    adgroup_id: int | None = None
    """The unique identifier for the ad group."""
    ad_name: str | None = None
    """The name of the ad."""
    ad_text: str | None = None
    """The text content of the ad."""
    placement_type: str | None = None
    """Type of ad placement."""
    spend: str | None = None
    """Total amount of money spent."""
    cpc: str | None = None
    """Cost per click."""
    cpm: str | None = None
    """Cost per thousand impressions."""
    impressions: str | None = None
    """Number of times the ad was displayed."""
    clicks: str | None = None
    """Number of clicks on the ad."""
    ctr: str | None = None
    """Click-through rate."""
    reach: str | None = None
    """Total number of unique users reached."""
    cost_per_1000_reached: str | None = None
    """Cost per 1000 unique users reached."""
    conversion: str | None = None
    """Number of conversions."""
    cost_per_conversion: str | None = None
    """Cost per conversion."""
    conversion_rate: str | None = None
    """Rate of conversions."""
    real_time_conversion: str | None = None
    """Real-time conversions."""
    real_time_cost_per_conversion: str | None = None
    """Real-time cost per conversion."""
    real_time_conversion_rate: str | None = None
    """Real-time conversion rate."""
    result: str | None = None
    """Number of results."""
    cost_per_result: str | None = None
    """Cost per result."""
    result_rate: str | None = None
    """Rate of results."""
    real_time_result: str | None = None
    """Real-time results."""
    real_time_cost_per_result: str | None = None
    """Real-time cost per result."""
    real_time_result_rate: str | None = None
    """Real-time result rate."""
    secondary_goal_result: str | None = None
    """Results for secondary goals."""
    cost_per_secondary_goal_result: str | None = None
    """Cost per secondary goal result."""
    secondary_goal_result_rate: str | None = None
    """Rate of secondary goal results."""
    frequency: str | None = None
    """Average number of times each person saw the ad."""
    video_play_actions: float | None = None
    """Number of video play actions."""
    video_watched_2s: float | None = None
    """Number of times video was watched for at least 2 seconds."""
    video_watched_6s: float | None = None
    """Number of times video was watched for at least 6 seconds."""
    average_video_play: float | None = None
    """Average video play duration."""
    average_video_play_per_user: float | None = None
    """Average video play duration per user."""
    video_views_p25: float | None = None
    """Number of times video was watched to 25%."""
    video_views_p50: float | None = None
    """Number of times video was watched to 50%."""
    video_views_p75: float | None = None
    """Number of times video was watched to 75%."""
    video_views_p100: float | None = None
    """Number of times video was watched to 100%."""
    profile_visits: float | None = None
    """Number of profile visits."""
    likes: float | None = None
    """Number of likes."""
    comments: float | None = None
    """Number of comments."""
    shares: float | None = None
    """Number of shares."""
    follows: float | None = None
    """Number of follows."""
    clicks_on_music_disc: float | None = None
    """Number of clicks on the music disc."""
    real_time_app_install: float | None = None
    """Real-time app installations."""
    real_time_app_install_cost: float | None = None
    """Cost of real-time app installations."""
    app_install: float | None = None
    """Number of app installations."""


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

AdvertisersSearchResult = AirbyteSearchResult[AdvertisersSearchData]
"""Search result type for advertisers entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

AdGroupsSearchResult = AirbyteSearchResult[AdGroupsSearchData]
"""Search result type for ad_groups entity."""

AdsSearchResult = AirbyteSearchResult[AdsSearchData]
"""Search result type for ads entity."""

AudiencesSearchResult = AirbyteSearchResult[AudiencesSearchData]
"""Search result type for audiences entity."""

CreativeAssetsImagesSearchResult = AirbyteSearchResult[CreativeAssetsImagesSearchData]
"""Search result type for creative_assets_images entity."""

CreativeAssetsVideosSearchResult = AirbyteSearchResult[CreativeAssetsVideosSearchData]
"""Search result type for creative_assets_videos entity."""

AdvertisersReportsDailySearchResult = AirbyteSearchResult[AdvertisersReportsDailySearchData]
"""Search result type for advertisers_reports_daily entity."""

CampaignsReportsDailySearchResult = AirbyteSearchResult[CampaignsReportsDailySearchData]
"""Search result type for campaigns_reports_daily entity."""

AdGroupsReportsDailySearchResult = AirbyteSearchResult[AdGroupsReportsDailySearchData]
"""Search result type for ad_groups_reports_daily entity."""

AdsReportsDailySearchResult = AirbyteSearchResult[AdsReportsDailySearchData]
"""Search result type for ads_reports_daily entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AdvertisersListResult = TiktokMarketingExecuteResult[list[Advertiser]]
"""Result type for advertisers.list operation."""

CampaignsListResult = TiktokMarketingExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

AdGroupsListResult = TiktokMarketingExecuteResultWithMeta[list[AdGroup], AdGroupsListResultMeta]
"""Result type for ad_groups.list operation with data and metadata."""

AdsListResult = TiktokMarketingExecuteResultWithMeta[list[Ad], AdsListResultMeta]
"""Result type for ads.list operation with data and metadata."""

AudiencesListResult = TiktokMarketingExecuteResultWithMeta[list[Audience], AudiencesListResultMeta]
"""Result type for audiences.list operation with data and metadata."""

CreativeAssetsImagesListResult = TiktokMarketingExecuteResultWithMeta[list[CreativeAssetImage], CreativeAssetsImagesListResultMeta]
"""Result type for creative_assets_images.list operation with data and metadata."""

CreativeAssetsVideosListResult = TiktokMarketingExecuteResultWithMeta[list[CreativeAssetVideo], CreativeAssetsVideosListResultMeta]
"""Result type for creative_assets_videos.list operation with data and metadata."""

AdvertisersReportsDailyListResult = TiktokMarketingExecuteResultWithMeta[list[AdvertisersReportDaily], AdvertisersReportsDailyListResultMeta]
"""Result type for advertisers_reports_daily.list operation with data and metadata."""

CampaignsReportsDailyListResult = TiktokMarketingExecuteResultWithMeta[list[CampaignsReportDaily], CampaignsReportsDailyListResultMeta]
"""Result type for campaigns_reports_daily.list operation with data and metadata."""

AdGroupsReportsDailyListResult = TiktokMarketingExecuteResultWithMeta[list[AdGroupsReportDaily], AdGroupsReportsDailyListResultMeta]
"""Result type for ad_groups_reports_daily.list operation with data and metadata."""

AdsReportsDailyListResult = TiktokMarketingExecuteResultWithMeta[list[AdsReportDaily], AdsReportsDailyListResultMeta]
"""Result type for ads_reports_daily.list operation with data and metadata."""

