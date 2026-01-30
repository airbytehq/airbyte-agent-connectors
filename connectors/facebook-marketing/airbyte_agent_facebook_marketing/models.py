"""
Pydantic models for facebook-marketing connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class FacebookMarketingAuthConfig(BaseModel):
    """Facebook Marketing Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Facebook Marketing API access token"""
    account_id: str
    """Facebook Ad Account ID (without the act_ prefix)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class AdLabel(BaseModel):
    """AdLabel type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    updated_time: Union[str | None, Any] = Field(default=None)

class IssueInfo(BaseModel):
    """IssueInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    error_code: Union[str | None, Any] = Field(default=None)
    error_message: Union[str | None, Any] = Field(default=None)
    error_summary: Union[str | None, Any] = Field(default=None)
    error_type: Union[str | None, Any] = Field(default=None)
    level: Union[str | None, Any] = Field(default=None)

class Campaign(BaseModel):
    """Facebook Ad Campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    adlabels: Union[list[AdLabel] | None, Any] = Field(default=None)
    bid_strategy: Union[str | None, Any] = Field(default=None)
    boosted_object_id: Union[str | None, Any] = Field(default=None)
    budget_rebalance_flag: Union[bool | None, Any] = Field(default=None)
    budget_remaining: Union[float | None, Any] = Field(default=None)
    buying_type: Union[str | None, Any] = Field(default=None)
    daily_budget: Union[float | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    configured_status: Union[str | None, Any] = Field(default=None)
    effective_status: Union[str | None, Any] = Field(default=None)
    issues_info: Union[list[IssueInfo] | None, Any] = Field(default=None)
    lifetime_budget: Union[float | None, Any] = Field(default=None)
    objective: Union[str | None, Any] = Field(default=None)
    smart_promotion_type: Union[str | None, Any] = Field(default=None)
    source_campaign_id: Union[str | None, Any] = Field(default=None)
    special_ad_category: Union[str | None, Any] = Field(default=None)
    special_ad_category_country: Union[list[str | None] | None, Any] = Field(default=None)
    spend_cap: Union[float | None, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    stop_time: Union[str | None, Any] = Field(default=None)
    updated_time: Union[str | None, Any] = Field(default=None)

class PagingCursors(BaseModel):
    """Nested schema for Paging.cursors"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    before: Union[str | None, Any] = Field(default=None, description="Cursor for previous page")
    """Cursor for previous page"""
    after: Union[str | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class Paging(BaseModel):
    """Paging type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursors: Union[PagingCursors, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    previous: Union[str | None, Any] = Field(default=None)

class CampaignsList(BaseModel):
    """CampaignsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Campaign], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class AdSet(BaseModel):
    """Facebook Ad Set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    adlabels: Union[list[AdLabel] | None, Any] = Field(default=None)
    bid_amount: Union[float | None, Any] = Field(default=None)
    bid_info: Union[Any, Any] = Field(default=None)
    bid_strategy: Union[str | None, Any] = Field(default=None)
    bid_constraints: Union[Any, Any] = Field(default=None)
    budget_remaining: Union[float | None, Any] = Field(default=None)
    campaign_id: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    daily_budget: Union[float | None, Any] = Field(default=None)
    effective_status: Union[str | None, Any] = Field(default=None)
    end_time: Union[str | None, Any] = Field(default=None)
    learning_stage_info: Union[Any, Any] = Field(default=None)
    lifetime_budget: Union[float | None, Any] = Field(default=None)
    promoted_object: Union[Any, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    targeting: Union[dict[str, Any] | None, Any] = Field(default=None)
    updated_time: Union[str | None, Any] = Field(default=None)

class AdSetsList(BaseModel):
    """AdSetsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[AdSet], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class Recommendation(BaseModel):
    """Recommendation type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blame_field: Union[str | None, Any] = Field(default=None)
    code: Union[int | None, Any] = Field(default=None)
    confidence: Union[str | None, Any] = Field(default=None)
    importance: Union[str | None, Any] = Field(default=None)
    message: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)

class Ad(BaseModel):
    """Facebook Ad"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    adset_id: Union[str | None, Any] = Field(default=None)
    campaign_id: Union[str | None, Any] = Field(default=None)
    adlabels: Union[list[AdLabel] | None, Any] = Field(default=None)
    bid_amount: Union[int | None, Any] = Field(default=None)
    bid_info: Union[Any, Any] = Field(default=None)
    bid_type: Union[str | None, Any] = Field(default=None)
    configured_status: Union[str | None, Any] = Field(default=None)
    conversion_specs: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    creative: Union[Any, Any] = Field(default=None)
    effective_status: Union[str | None, Any] = Field(default=None)
    last_updated_by_app_id: Union[str | None, Any] = Field(default=None)
    recommendations: Union[list[Recommendation] | None, Any] = Field(default=None)
    source_ad_id: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    tracking_specs: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    updated_time: Union[str | None, Any] = Field(default=None)

class AdsList(BaseModel):
    """AdsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Ad], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class AdCreative(BaseModel):
    """Facebook Ad Creative"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    actor_id: Union[str | None, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    call_to_action_type: Union[str | None, Any] = Field(default=None)
    effective_object_story_id: Union[str | None, Any] = Field(default=None)
    image_hash: Union[str | None, Any] = Field(default=None)
    image_url: Union[str | None, Any] = Field(default=None)
    link_url: Union[str | None, Any] = Field(default=None)
    object_story_id: Union[str | None, Any] = Field(default=None)
    object_story_spec: Union[dict[str, Any] | None, Any] = Field(default=None)
    object_type: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    thumbnail_url: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    url_tags: Union[str | None, Any] = Field(default=None)

class AdCreativesList(BaseModel):
    """AdCreativesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[AdCreative], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class AdsInsight(BaseModel):
    """Facebook Ads Insight"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: Union[str | None, Any] = Field(default=None)
    account_name: Union[str | None, Any] = Field(default=None)
    campaign_id: Union[str | None, Any] = Field(default=None)
    campaign_name: Union[str | None, Any] = Field(default=None)
    adset_id: Union[str | None, Any] = Field(default=None)
    adset_name: Union[str | None, Any] = Field(default=None)
    ad_id: Union[str | None, Any] = Field(default=None)
    ad_name: Union[str | None, Any] = Field(default=None)
    clicks: Union[int | None, Any] = Field(default=None)
    impressions: Union[int | None, Any] = Field(default=None)
    reach: Union[int | None, Any] = Field(default=None)
    spend: Union[float | None, Any] = Field(default=None)
    cpc: Union[float | None, Any] = Field(default=None)
    cpm: Union[float | None, Any] = Field(default=None)
    ctr: Union[float | None, Any] = Field(default=None)
    date_start: Union[str | None, Any] = Field(default=None)
    date_stop: Union[str | None, Any] = Field(default=None)

class AdsInsightsList(BaseModel):
    """AdsInsightsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[AdsInsight], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class DataSource(BaseModel):
    """DataSource type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    source_type: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class CustomConversion(BaseModel):
    """Facebook Custom Conversion"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    business: Union[str | None, Any] = Field(default=None)
    creation_time: Union[str | None, Any] = Field(default=None)
    custom_event_type: Union[str | None, Any] = Field(default=None)
    data_sources: Union[list[DataSource] | None, Any] = Field(default=None)
    default_conversion_value: Union[float | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    event_source_type: Union[str | None, Any] = Field(default=None)
    first_fired_time: Union[str | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None)
    is_unavailable: Union[bool | None, Any] = Field(default=None)
    last_fired_time: Union[str | None, Any] = Field(default=None)
    offline_conversion_data_set: Union[str | None, Any] = Field(default=None)
    retention_days: Union[float | None, Any] = Field(default=None)
    rule: Union[str | None, Any] = Field(default=None)

class CustomConversionsList(BaseModel):
    """CustomConversionsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[CustomConversion], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class Image(BaseModel):
    """Image type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    creatives: Union[list[str | None] | None, Any] = Field(default=None)
    filename: Union[str | None, Any] = Field(default=None)
    hash: Union[str | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    is_associated_creatives_in_adgroups: Union[bool | None, Any] = Field(default=None)
    original_height: Union[int | None, Any] = Field(default=None)
    original_width: Union[int | None, Any] = Field(default=None)
    permalink_url: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    updated_time: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    url_128: Union[str | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)

class ImagesList(BaseModel):
    """ImagesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Image], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class VideoFormat(BaseModel):
    """VideoFormat type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    filter: Union[str | None, Any] = Field(default=None)
    embed_html: Union[str | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    picture: Union[str | None, Any] = Field(default=None)

class Video(BaseModel):
    """Video type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    ad_breaks: Union[list[int] | None, Any] = Field(default=None)
    backdated_time: Union[str | None, Any] = Field(default=None)
    backdated_time_granularity: Union[str | None, Any] = Field(default=None)
    content_category: Union[str | None, Any] = Field(default=None)
    content_tags: Union[list[str] | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    custom_labels: Union[list[str] | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    embed_html: Union[str | None, Any] = Field(default=None)
    embeddable: Union[bool | None, Any] = Field(default=None)
    format: Union[list[VideoFormat] | None, Any] = Field(default=None)
    icon: Union[str | None, Any] = Field(default=None)
    is_crosspost_video: Union[bool | None, Any] = Field(default=None)
    is_crossposting_eligible: Union[bool | None, Any] = Field(default=None)
    is_episode: Union[bool | None, Any] = Field(default=None)
    is_instagram_eligible: Union[bool | None, Any] = Field(default=None)
    length: Union[float | None, Any] = Field(default=None)
    live_status: Union[str | None, Any] = Field(default=None)
    permalink_url: Union[str | None, Any] = Field(default=None)
    post_views: Union[int | None, Any] = Field(default=None)
    premiere_living_room_status: Union[bool | None, Any] = Field(default=None)
    published: Union[bool | None, Any] = Field(default=None)
    scheduled_publish_time: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    universal_video_id: Union[str | None, Any] = Field(default=None)
    updated_time: Union[str | None, Any] = Field(default=None)
    views: Union[int | None, Any] = Field(default=None)

class VideosList(BaseModel):
    """VideosList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Video], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class BidInfo(BaseModel):
    """BidInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    clicks: Union[int | None, Any] = Field(default=None, alias="CLICKS")
    actions: Union[int | None, Any] = Field(default=None, alias="ACTIONS")
    reach: Union[int | None, Any] = Field(default=None, alias="REACH")
    impressions: Union[int | None, Any] = Field(default=None, alias="IMPRESSIONS")
    social: Union[int | None, Any] = Field(default=None, alias="SOCIAL")

class BidConstraints(BaseModel):
    """BidConstraints type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    roas_average_floor: Union[int | None, Any] = Field(default=None)

class LearningStageInfo(BaseModel):
    """LearningStageInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str | None, Any] = Field(default=None)
    conversions: Union[int | None, Any] = Field(default=None)
    last_sig_edit_ts: Union[int | None, Any] = Field(default=None)
    attribution_windows: Union[list[str | None] | None, Any] = Field(default=None)

class PromotedObject(BaseModel):
    """PromotedObject type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    custom_event_type: Union[str | None, Any] = Field(default=None)
    pixel_id: Union[str | None, Any] = Field(default=None)
    pixel_rule: Union[str | None, Any] = Field(default=None)
    page_id: Union[str | None, Any] = Field(default=None)
    object_store_url: Union[str | None, Any] = Field(default=None)
    application_id: Union[str | None, Any] = Field(default=None)
    product_set_id: Union[str | None, Any] = Field(default=None)
    offer_id: Union[str | None, Any] = Field(default=None)

class AdCreativeRef(BaseModel):
    """AdCreativeRef type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    creative_id: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class AdSetsListResultMeta(BaseModel):
    """Metadata for ad_sets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class AdsListResultMeta(BaseModel):
    """Metadata for ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class AdCreativesListResultMeta(BaseModel):
    """Metadata for ad_creatives.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class AdsInsightsListResultMeta(BaseModel):
    """Metadata for ads_insights.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class CustomConversionsListResultMeta(BaseModel):
    """Metadata for custom_conversions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class ImagesListResultMeta(BaseModel):
    """Metadata for images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

class VideosListResultMeta(BaseModel):
    """Metadata for videos.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class FacebookMarketingCheckResult(BaseModel):
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


class FacebookMarketingExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class FacebookMarketingExecuteResultWithMeta(FacebookMarketingExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Campaign ID"""
    name: str | None = None
    """Campaign name"""
    account_id: str | None = None
    """Ad account ID"""
    status: str | None = None
    """Campaign status"""
    effective_status: str | None = None
    """Effective status"""
    objective: str | None = None
    """Campaign objective"""
    daily_budget: float | None = None
    """Daily budget in account currency"""
    lifetime_budget: float | None = None
    """Lifetime budget"""
    budget_remaining: float | None = None
    """Remaining budget"""
    created_time: str | None = None
    """Campaign creation time"""
    start_time: str | None = None
    """Campaign start time"""
    stop_time: str | None = None
    """Campaign stop time"""
    updated_time: str | None = None
    """Last update time"""


class AdSetsSearchData(BaseModel):
    """Search result data for ad_sets entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Ad Set ID"""
    name: str | None = None
    """Ad Set name"""
    account_id: str | None = None
    """Ad account ID"""
    campaign_id: str | None = None
    """Parent campaign ID"""
    effective_status: str | None = None
    """Effective status"""
    daily_budget: float | None = None
    """Daily budget"""
    lifetime_budget: float | None = None
    """Lifetime budget"""
    budget_remaining: float | None = None
    """Remaining budget"""
    bid_amount: float | None = None
    """Bid amount"""
    bid_strategy: str | None = None
    """Bid strategy"""
    created_time: str | None = None
    """Ad set creation time"""
    start_time: str | None = None
    """Ad set start time"""
    end_time: str | None = None
    """Ad set end time"""
    updated_time: str | None = None
    """Last update time"""


class AdsSearchData(BaseModel):
    """Search result data for ads entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Ad ID"""
    name: str | None = None
    """Ad name"""
    account_id: str | None = None
    """Ad account ID"""
    adset_id: str | None = None
    """Parent ad set ID"""
    campaign_id: str | None = None
    """Parent campaign ID"""
    status: str | None = None
    """Ad status"""
    effective_status: str | None = None
    """Effective status"""
    created_time: str | None = None
    """Ad creation time"""
    updated_time: str | None = None
    """Last update time"""


class AdCreativesSearchData(BaseModel):
    """Search result data for ad_creatives entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Ad Creative ID"""
    name: str | None = None
    """Ad Creative name"""
    account_id: str | None = None
    """Ad account ID"""
    body: str | None = None
    """Ad body text"""
    title: str | None = None
    """Ad title"""
    status: str | None = None
    """Creative status"""
    image_url: str | None = None
    """Image URL"""
    thumbnail_url: str | None = None
    """Thumbnail URL"""
    link_url: str | None = None
    """Link URL"""
    call_to_action_type: str | None = None
    """Call to action type"""


class AdsInsightsSearchData(BaseModel):
    """Search result data for ads_insights entity."""
    model_config = ConfigDict(extra="allow")

    account_id: str | None = None
    """Ad account ID"""
    account_name: str | None = None
    """Ad account name"""
    campaign_id: str | None = None
    """Campaign ID"""
    campaign_name: str | None = None
    """Campaign name"""
    adset_id: str | None = None
    """Ad set ID"""
    adset_name: str | None = None
    """Ad set name"""
    ad_id: str | None = None
    """Ad ID"""
    ad_name: str | None = None
    """Ad name"""
    clicks: int | None = None
    """Number of clicks"""
    impressions: int | None = None
    """Number of impressions"""
    reach: int | None = None
    """Number of unique people reached"""
    spend: float | None = None
    """Amount spent"""
    cpc: float | None = None
    """Cost per click"""
    cpm: float | None = None
    """Cost per 1000 impressions"""
    ctr: float | None = None
    """Click-through rate"""
    date_start: str | None = None
    """Start date of the reporting period"""
    date_stop: str | None = None
    """End date of the reporting period"""


class CustomConversionsSearchData(BaseModel):
    """Search result data for custom_conversions entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Custom Conversion ID"""
    name: str | None = None
    """Custom Conversion name"""
    account_id: str | None = None
    """Ad account ID"""
    description: str | None = None
    """Description"""
    custom_event_type: str | None = None
    """Custom event type"""
    creation_time: str | None = None
    """Creation time"""
    first_fired_time: str | None = None
    """First fired time"""
    last_fired_time: str | None = None
    """Last fired time"""
    is_archived: bool | None = None
    """Whether the conversion is archived"""


class ImagesSearchData(BaseModel):
    """Search result data for images entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Image ID"""
    name: str | None = None
    """Image name"""
    account_id: str | None = None
    """Ad account ID"""
    hash: str | None = None
    """Image hash"""
    url: str | None = None
    """Image URL"""
    permalink_url: str | None = None
    """Permalink URL"""
    width: int | None = None
    """Image width"""
    height: int | None = None
    """Image height"""
    status: str | None = None
    """Image status"""
    created_time: str | None = None
    """Creation time"""
    updated_time: str | None = None
    """Last update time"""


class VideosSearchData(BaseModel):
    """Search result data for videos entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Video ID"""
    title: str | None = None
    """Video title"""
    account_id: str | None = None
    """Ad account ID"""
    description: str | None = None
    """Video description"""
    length: float | None = None
    """Video length in seconds"""
    source: str | None = None
    """Video source URL"""
    permalink_url: str | None = None
    """Permalink URL"""
    views: int | None = None
    """Number of views"""
    created_time: str | None = None
    """Creation time"""
    updated_time: str | None = None
    """Last update time"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchHit(BaseModel, Generic[D]):
    """A single search result with typed data."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the record."""
    score: float | None = None
    """Relevance score for the match."""
    data: D
    """The matched record data."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed hits."""
    model_config = ConfigDict(extra="allow")

    hits: list[AirbyteSearchHit[D]] = Field(default_factory=list)
    """List of matching records."""
    next_cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

AdSetsSearchResult = AirbyteSearchResult[AdSetsSearchData]
"""Search result type for ad_sets entity."""

AdsSearchResult = AirbyteSearchResult[AdsSearchData]
"""Search result type for ads entity."""

AdCreativesSearchResult = AirbyteSearchResult[AdCreativesSearchData]
"""Search result type for ad_creatives entity."""

AdsInsightsSearchResult = AirbyteSearchResult[AdsInsightsSearchData]
"""Search result type for ads_insights entity."""

CustomConversionsSearchResult = AirbyteSearchResult[CustomConversionsSearchData]
"""Search result type for custom_conversions entity."""

ImagesSearchResult = AirbyteSearchResult[ImagesSearchData]
"""Search result type for images entity."""

VideosSearchResult = AirbyteSearchResult[VideosSearchData]
"""Search result type for videos entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CampaignsListResult = FacebookMarketingExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

AdSetsListResult = FacebookMarketingExecuteResultWithMeta[list[AdSet], AdSetsListResultMeta]
"""Result type for ad_sets.list operation with data and metadata."""

AdsListResult = FacebookMarketingExecuteResultWithMeta[list[Ad], AdsListResultMeta]
"""Result type for ads.list operation with data and metadata."""

AdCreativesListResult = FacebookMarketingExecuteResultWithMeta[list[AdCreative], AdCreativesListResultMeta]
"""Result type for ad_creatives.list operation with data and metadata."""

AdsInsightsListResult = FacebookMarketingExecuteResultWithMeta[list[AdsInsight], AdsInsightsListResultMeta]
"""Result type for ads_insights.list operation with data and metadata."""

CustomConversionsListResult = FacebookMarketingExecuteResultWithMeta[list[CustomConversion], CustomConversionsListResultMeta]
"""Result type for custom_conversions.list operation with data and metadata."""

ImagesListResult = FacebookMarketingExecuteResultWithMeta[list[Image], ImagesListResultMeta]
"""Result type for images.list operation with data and metadata."""

VideosListResult = FacebookMarketingExecuteResultWithMeta[list[Video], VideosListResultMeta]
"""Result type for videos.list operation with data and metadata."""

