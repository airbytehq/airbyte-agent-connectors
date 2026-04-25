"""
Pydantic models for tiktok-marketing connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

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

    advertiser_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    address: str | None = Field(default=None)
    company: str | None = Field(default=None)
    contacter: str | None = Field(default=None)
    country: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    description: str | None = Field(default=None)
    email: str | None = Field(default=None)
    industry: str | None = Field(default=None)
    language: str | None = Field(default=None)
    license_no: str | None = Field(default=None)
    license_url: str | None = Field(default=None)
    cellphone_number: str | None = Field(default=None)
    promotion_area: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    role: str | None = Field(default=None)
    status: str | None = Field(default=None)
    timezone: str | None = Field(default=None)
    balance: float | None = Field(default=None)
    create_time: int | None = Field(default=None)
    telephone_number: str | None = Field(default=None)
    display_timezone: str | None = Field(default=None)
    promotion_center_province: str | None = Field(default=None)
    advertiser_account_type: str | None = Field(default=None)
    license_city: str | None = Field(default=None)
    brand: str | None = Field(default=None)
    license_province: str | None = Field(default=None)
    promotion_center_city: str | None = Field(default=None)

class Campaign(BaseModel):
    """TikTok marketing campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: str | None = Field(default=None)
    campaign_name: str | None = Field(default=None)
    campaign_type: str | None = Field(default=None)
    advertiser_id: str | None = Field(default=None)
    budget: float | None = Field(default=None)
    budget_mode: str | None = Field(default=None)
    secondary_status: str | None = Field(default=None)
    operation_status: str | None = Field(default=None)
    objective: str | None = Field(default=None)
    objective_type: str | None = Field(default=None)
    budget_optimize_on: bool | None = Field(default=None)
    bid_type: str | None = Field(default=None)
    deep_bid_type: str | None = Field(default=None)
    optimization_goal: str | None = Field(default=None)
    split_test_variable: str | None = Field(default=None)
    is_new_structure: bool | None = Field(default=None)
    create_time: str | None = Field(default=None)
    modify_time: str | None = Field(default=None)
    roas_bid: float | None = Field(default=None)
    is_smart_performance_campaign: bool | None = Field(default=None)
    is_search_campaign: bool | None = Field(default=None)
    app_promotion_type: str | None = Field(default=None)
    rf_campaign_type: str | None = Field(default=None)
    disable_skan_campaign: bool | None = Field(default=None)
    is_advanced_dedicated_campaign: bool | None = Field(default=None)
    rta_id: str | None = Field(default=None)
    campaign_automation_type: str | None = Field(default=None)
    rta_bid_enabled: bool | None = Field(default=None)
    rta_product_selection_enabled: bool | None = Field(default=None)

class AdGroup(BaseModel):
    """TikTok ad group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    adgroup_id: str | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    advertiser_id: str | None = Field(default=None)
    adgroup_name: str | None = Field(default=None)
    placement_type: str | None = Field(default=None)
    placements: list[str] | None = Field(default=None)
    budget: float | None = Field(default=None)
    budget_mode: str | None = Field(default=None)
    secondary_status: str | None = Field(default=None)
    operation_status: str | None = Field(default=None)
    optimization_goal: str | None = Field(default=None)
    bid_type: str | None = Field(default=None)
    bid_price: float | None = Field(default=None)
    promotion_type: str | None = Field(default=None)
    creative_material_mode: str | None = Field(default=None)
    schedule_type: str | None = Field(default=None)
    schedule_start_time: str | None = Field(default=None)
    schedule_end_time: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    modify_time: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    age_groups: list[str] | None = Field(default=None)
    languages: list[str] | None = Field(default=None)
    location_ids: list[str] | None = Field(default=None)
    audience_ids: list[Any] | None = Field(default=None)
    excluded_audience_ids: list[Any] | None = Field(default=None)
    interest_category_ids: list[str] | None = Field(default=None)
    interest_keyword_ids: list[Any] | None = Field(default=None)
    pixel_id: str | None = Field(default=None)
    deep_bid_type: str | None = Field(default=None)
    deep_cpa_bid: float | None = Field(default=None)
    conversion_bid_price: float | None = Field(default=None)
    billing_event: str | None = Field(default=None)
    pacing: str | None = Field(default=None)
    dayparting: str | None = Field(default=None)
    frequency: int | None = Field(default=None)
    frequency_schedule: int | None = Field(default=None)
    is_new_structure: bool | None = Field(default=None)
    is_smart_performance_campaign: bool | None = Field(default=None)
    app_id: str | None = Field(default=None)
    app_type: str | None = Field(default=None)
    app_download_url: str | None = Field(default=None)
    optimization_event: str | None = Field(default=None)
    secondary_optimization_event: str | None = Field(default=None)
    conversion_window: str | None = Field(default=None)
    comment_disabled: bool | None = Field(default=None)
    video_download_disabled: bool | None = Field(default=None)
    share_disabled: bool | None = Field(default=None)
    auto_targeting_enabled: bool | None = Field(default=None)
    is_hfss: bool | None = Field(default=None)
    search_result_enabled: bool | None = Field(default=None)
    inventory_filter_enabled: bool | None = Field(default=None)
    skip_learning_phase: bool | None = Field(default=None)
    brand_safety_type: str | None = Field(default=None)
    brand_safety_partner: str | None = Field(default=None)
    campaign_name: str | None = Field(default=None)
    campaign_automation_type: str | None = Field(default=None)
    bid_display_mode: str | None = Field(default=None)
    scheduled_budget: float | None = Field(default=None)
    category_id: str | None = Field(default=None)
    feed_type: str | None = Field(default=None)
    delivery_mode: str | None = Field(default=None)
    ios14_quota_type: str | None = Field(default=None)
    spending_power: str | None = Field(default=None)
    next_day_retention: float | None = Field(default=None)
    rf_purchased_type: str | None = Field(default=None)
    rf_estimated_cpr: float | None = Field(default=None)
    rf_estimated_frequency: float | None = Field(default=None)
    purchased_impression: float | None = Field(default=None)
    purchased_reach: float | None = Field(default=None)
    actions: list[Any] | None = Field(default=None)
    network_types: list[Any] | None = Field(default=None)
    operating_systems: list[Any] | None = Field(default=None)
    device_model_ids: list[Any] | None = Field(default=None)
    device_price_ranges: list[Any] | None = Field(default=None)
    included_custom_actions: list[Any] | None = Field(default=None)
    excluded_custom_actions: list[Any] | None = Field(default=None)
    category_exclusion_ids: list[Any] | None = Field(default=None)
    contextual_tag_ids: list[Any] | None = Field(default=None)
    zipcode_ids: list[Any] | None = Field(default=None)
    household_income: list[Any] | None = Field(default=None)
    isp_ids: list[Any] | None = Field(default=None)
    schedule_infos: list[Any] | None = Field(default=None)
    statistic_type: str | None = Field(default=None)
    keywords: str | None = Field(default=None)
    adgroup_app_profile_page_state: str | None = Field(default=None)
    automated_keywords_enabled: bool | None = Field(default=None)
    smart_audience_enabled: bool | None = Field(default=None)
    smart_interest_behavior_enabled: bool | None = Field(default=None)
    vbo_window: str | None = Field(default=None)
    deep_funnel_optimization_status: str | None = Field(default=None)
    deep_funnel_event_source: str | None = Field(default=None)
    deep_funnel_event_source_id: str | None = Field(default=None)
    deep_funnel_optimization_event: str | None = Field(default=None)
    custom_conversion_id: str | None = Field(default=None)
    app_config: dict[str, Any] | None = Field(default=None)

class Ad(BaseModel):
    """TikTok ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_id: str | None = Field(default=None)
    advertiser_id: str | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    campaign_name: str | None = Field(default=None)
    adgroup_id: str | None = Field(default=None)
    adgroup_name: str | None = Field(default=None)
    ad_name: str | None = Field(default=None)
    ad_text: str | None = Field(default=None)
    ad_texts: list[Any] | None = Field(default=None)
    ad_format: str | None = Field(default=None)
    secondary_status: str | None = Field(default=None)
    operation_status: str | None = Field(default=None)
    call_to_action: str | None = Field(default=None)
    call_to_action_id: str | None = Field(default=None)
    landing_page_url: str | None = Field(default=None)
    landing_page_urls: list[Any] | None = Field(default=None)
    display_name: str | None = Field(default=None)
    profile_image_url: str | None = Field(default=None)
    video_id: str | None = Field(default=None)
    image_ids: list[str] | None = Field(default=None)
    image_mode: str | None = Field(default=None)
    is_aco: bool | None = Field(default=None)
    is_new_structure: bool | None = Field(default=None)
    creative_type: str | None = Field(default=None)
    creative_authorized: bool | None = Field(default=None)
    identity_id: str | None = Field(default=None)
    identity_type: str | None = Field(default=None)
    deeplink: str | None = Field(default=None)
    deeplink_type: str | None = Field(default=None)
    fallback_type: str | None = Field(default=None)
    tracking_pixel_id: int | None = Field(default=None)
    impression_tracking_url: str | None = Field(default=None)
    click_tracking_url: str | None = Field(default=None)
    music_id: str | None = Field(default=None)
    optimization_event: str | None = Field(default=None)
    vast_moat_enabled: bool | None = Field(default=None)
    page_id: str | None = Field(default=None)
    viewability_postbid_partner: str | None = Field(default=None)
    viewability_vast_url: str | None = Field(default=None)
    brand_safety_postbid_partner: str | None = Field(default=None)
    brand_safety_vast_url: str | None = Field(default=None)
    app_name: str | None = Field(default=None)
    playable_url: str | None = Field(default=None)
    card_id: str | None = Field(default=None)
    carousel_image_labels: list[Any] | None = Field(default=None)
    avatar_icon_web_uri: str | None = Field(default=None)
    campaign_automation_type: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    modify_time: str | None = Field(default=None)

class Audience(BaseModel):
    """TikTok custom audience"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    audience_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    audience_type: str | None = Field(default=None)
    cover_num: int | None = Field(default=None)
    is_valid: bool | None = Field(default=None)
    is_expiring: bool | None = Field(default=None)
    is_creator: bool | None = Field(default=None)
    shared: bool | None = Field(default=None)
    calculate_type: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    expired_time: str | None = Field(default=None)

class CreativeAssetImage(BaseModel):
    """TikTok creative asset image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    image_id: str | None = Field(default=None)
    format: str | None = Field(default=None)
    image_url: str | None = Field(default=None)
    height: int | None = Field(default=None)
    width: int | None = Field(default=None)
    signature: str | None = Field(default=None)
    size: int | None = Field(default=None)
    material_id: str | None = Field(default=None)
    is_carousel_usable: bool | None = Field(default=None)
    file_name: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    modify_time: str | None = Field(default=None)
    displayable: bool | None = Field(default=None)

class CreativeAssetVideo(BaseModel):
    """TikTok creative asset video"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    video_id: str | None = Field(default=None)
    video_cover_url: str | None = Field(default=None)
    format: str | None = Field(default=None)
    preview_url: str | None = Field(default=None)
    preview_url_expire_time: str | None = Field(default=None)
    duration: float | None = Field(default=None)
    height: int | None = Field(default=None)
    width: int | None = Field(default=None)
    bit_rate: float | None = Field(default=None)
    signature: str | None = Field(default=None)
    size: int | None = Field(default=None)
    material_id: str | None = Field(default=None)
    allowed_placements: list[str | None] | None = Field(default=None)
    allow_download: bool | None = Field(default=None)
    file_name: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    modify_time: str | None = Field(default=None)
    displayable: bool | None = Field(default=None)
    fix_task_id: str | None = Field(default=None)
    flaw_types: list[Any] | None = Field(default=None)

class AdvertisersReportDaily(BaseModel):
    """Daily performance report at the advertiser level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    advertiser_id: int | None = Field(default=None)
    stat_time_day: str | None = Field(default=None)
    spend: str | None = Field(default=None)
    cash_spend: str | None = Field(default=None)
    voucher_spend: str | None = Field(default=None)
    cpc: str | None = Field(default=None)
    cpm: str | None = Field(default=None)
    impressions: str | None = Field(default=None)
    clicks: str | None = Field(default=None)
    ctr: str | None = Field(default=None)
    reach: str | None = Field(default=None)
    cost_per_1000_reached: str | None = Field(default=None)
    frequency: str | None = Field(default=None)
    video_play_actions: float | None = Field(default=None)
    video_watched_2s: float | None = Field(default=None)
    video_watched_6s: float | None = Field(default=None)
    average_video_play: float | None = Field(default=None)
    average_video_play_per_user: float | None = Field(default=None)
    video_views_p25: float | None = Field(default=None)
    video_views_p50: float | None = Field(default=None)
    video_views_p75: float | None = Field(default=None)
    video_views_p100: float | None = Field(default=None)
    profile_visits: float | None = Field(default=None)
    likes: float | None = Field(default=None)
    comments: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    follows: float | None = Field(default=None)
    clicks_on_music_disc: float | None = Field(default=None)
    real_time_app_install: float | None = Field(default=None)
    real_time_app_install_cost: float | None = Field(default=None)
    app_install: float | None = Field(default=None)

class CampaignsReportDaily(BaseModel):
    """Daily performance report at the campaign level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: int | None = Field(default=None)
    stat_time_day: str | None = Field(default=None)
    campaign_name: str | None = Field(default=None)
    spend: str | None = Field(default=None)
    cpc: str | None = Field(default=None)
    cpm: str | None = Field(default=None)
    impressions: str | None = Field(default=None)
    clicks: str | None = Field(default=None)
    ctr: str | None = Field(default=None)
    reach: str | None = Field(default=None)
    cost_per_1000_reached: str | None = Field(default=None)
    frequency: str | None = Field(default=None)
    video_play_actions: float | None = Field(default=None)
    video_watched_2s: float | None = Field(default=None)
    video_watched_6s: float | None = Field(default=None)
    average_video_play: float | None = Field(default=None)
    average_video_play_per_user: float | None = Field(default=None)
    video_views_p25: float | None = Field(default=None)
    video_views_p50: float | None = Field(default=None)
    video_views_p75: float | None = Field(default=None)
    video_views_p100: float | None = Field(default=None)
    profile_visits: float | None = Field(default=None)
    likes: float | None = Field(default=None)
    comments: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    follows: float | None = Field(default=None)
    clicks_on_music_disc: float | None = Field(default=None)
    real_time_app_install: float | None = Field(default=None)
    real_time_app_install_cost: float | None = Field(default=None)
    app_install: float | None = Field(default=None)

class AdGroupsReportDaily(BaseModel):
    """Daily performance report at the ad group level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    adgroup_id: int | None = Field(default=None)
    stat_time_day: str | None = Field(default=None)
    campaign_name: str | None = Field(default=None)
    campaign_id: int | None = Field(default=None)
    adgroup_name: str | None = Field(default=None)
    placement_type: str | None = Field(default=None)
    spend: str | None = Field(default=None)
    cpc: str | None = Field(default=None)
    cpm: str | None = Field(default=None)
    impressions: str | None = Field(default=None)
    clicks: str | None = Field(default=None)
    ctr: str | None = Field(default=None)
    reach: str | None = Field(default=None)
    cost_per_1000_reached: str | None = Field(default=None)
    conversion: str | None = Field(default=None)
    cost_per_conversion: str | None = Field(default=None)
    conversion_rate: str | None = Field(default=None)
    real_time_conversion: str | None = Field(default=None)
    real_time_cost_per_conversion: str | None = Field(default=None)
    real_time_conversion_rate: str | None = Field(default=None)
    result: str | None = Field(default=None)
    cost_per_result: str | None = Field(default=None)
    result_rate: str | None = Field(default=None)
    real_time_result: str | None = Field(default=None)
    real_time_cost_per_result: str | None = Field(default=None)
    real_time_result_rate: str | None = Field(default=None)
    secondary_goal_result: str | None = Field(default=None)
    cost_per_secondary_goal_result: str | None = Field(default=None)
    secondary_goal_result_rate: str | None = Field(default=None)
    frequency: str | None = Field(default=None)
    video_play_actions: float | None = Field(default=None)
    video_watched_2s: float | None = Field(default=None)
    video_watched_6s: float | None = Field(default=None)
    average_video_play: float | None = Field(default=None)
    average_video_play_per_user: float | None = Field(default=None)
    video_views_p25: float | None = Field(default=None)
    video_views_p50: float | None = Field(default=None)
    video_views_p75: float | None = Field(default=None)
    video_views_p100: float | None = Field(default=None)
    profile_visits: float | None = Field(default=None)
    likes: float | None = Field(default=None)
    comments: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    follows: float | None = Field(default=None)
    clicks_on_music_disc: float | None = Field(default=None)
    real_time_app_install: float | None = Field(default=None)
    real_time_app_install_cost: float | None = Field(default=None)
    app_install: float | None = Field(default=None)

class AdsReportDaily(BaseModel):
    """Daily performance report at the ad level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_id: int | None = Field(default=None)
    stat_time_day: str | None = Field(default=None)
    campaign_name: str | None = Field(default=None)
    campaign_id: int | None = Field(default=None)
    adgroup_name: str | None = Field(default=None)
    adgroup_id: int | None = Field(default=None)
    ad_name: str | None = Field(default=None)
    ad_text: str | None = Field(default=None)
    placement_type: str | None = Field(default=None)
    spend: str | None = Field(default=None)
    cpc: str | None = Field(default=None)
    cpm: str | None = Field(default=None)
    impressions: str | None = Field(default=None)
    clicks: str | None = Field(default=None)
    ctr: str | None = Field(default=None)
    reach: str | None = Field(default=None)
    cost_per_1000_reached: str | None = Field(default=None)
    conversion: str | None = Field(default=None)
    cost_per_conversion: str | None = Field(default=None)
    conversion_rate: str | None = Field(default=None)
    real_time_conversion: str | None = Field(default=None)
    real_time_cost_per_conversion: str | None = Field(default=None)
    real_time_conversion_rate: str | None = Field(default=None)
    result: str | None = Field(default=None)
    cost_per_result: str | None = Field(default=None)
    result_rate: str | None = Field(default=None)
    real_time_result: str | None = Field(default=None)
    real_time_cost_per_result: str | None = Field(default=None)
    real_time_result_rate: str | None = Field(default=None)
    secondary_goal_result: str | None = Field(default=None)
    cost_per_secondary_goal_result: str | None = Field(default=None)
    secondary_goal_result_rate: str | None = Field(default=None)
    frequency: str | None = Field(default=None)
    video_play_actions: float | None = Field(default=None)
    video_watched_2s: float | None = Field(default=None)
    video_watched_6s: float | None = Field(default=None)
    average_video_play: float | None = Field(default=None)
    average_video_play_per_user: float | None = Field(default=None)
    video_views_p25: float | None = Field(default=None)
    video_views_p50: float | None = Field(default=None)
    video_views_p75: float | None = Field(default=None)
    video_views_p100: float | None = Field(default=None)
    profile_visits: float | None = Field(default=None)
    likes: float | None = Field(default=None)
    comments: float | None = Field(default=None)
    shares: float | None = Field(default=None)
    follows: float | None = Field(default=None)
    clicks_on_music_disc: float | None = Field(default=None)
    real_time_app_install: float | None = Field(default=None)
    real_time_app_install_cost: float | None = Field(default=None)
    app_install: float | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AdvertisersListResultMeta(BaseModel):
    """Metadata for advertisers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class AdGroupsListResultMeta(BaseModel):
    """Metadata for ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class AdsListResultMeta(BaseModel):
    """Metadata for ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class AudiencesListResultMeta(BaseModel):
    """Metadata for audiences.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class CreativeAssetsImagesListResultMeta(BaseModel):
    """Metadata for creative_assets_images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class CreativeAssetsVideosListResultMeta(BaseModel):
    """Metadata for creative_assets_videos.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class AdvertisersReportsDailyListResultMeta(BaseModel):
    """Metadata for advertisers_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class CampaignsReportsDailyListResultMeta(BaseModel):
    """Metadata for campaigns_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class AdGroupsReportsDailyListResultMeta(BaseModel):
    """Metadata for ad_groups_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

class AdsReportsDailyListResultMeta(BaseModel):
    """Metadata for ads_reports_daily.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_info: dict[str, Any] | None = Field(default=None)

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

AdvertisersListResult = TiktokMarketingExecuteResultWithMeta[list[Advertiser], AdvertisersListResultMeta]
"""Result type for advertisers.list operation with data and metadata."""

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

