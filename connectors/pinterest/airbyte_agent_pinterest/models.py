"""
Pydantic models for pinterest connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class PinterestAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    refresh_token: str
    """Pinterest OAuth2 refresh token."""
    client_id: str
    """Pinterest OAuth2 client ID."""
    client_secret: str
    """Pinterest OAuth2 client secret."""

# Replication configuration

class PinterestReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Pinterest."""

    model_config = ConfigDict(extra="forbid")

    start_date: Optional[str] = None
    """A date in the format YYYY-MM-DD. If not set, defaults to 89 days ago."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class AdAccountOwner(BaseModel):
    """Owner details of the ad account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None, description="Unique identifier of the owner")
    """Unique identifier of the owner"""
    username: Union[str | None, Any] = Field(default=None, description="Username of the owner")
    """Username of the owner"""

class AdAccount(BaseModel):
    """Pinterest ad account object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    owner: Union[AdAccountOwner | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    created_time: Union[int | None, Any] = Field(default=None)
    updated_time: Union[int | None, Any] = Field(default=None)
    permissions: Union[list[str | None] | None, Any] = Field(default=None)

class AdAccountsList(BaseModel):
    """Paginated list of ad accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[AdAccount], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class BoardMedia(BaseModel):
    """Media content for the board"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    image_cover_url: Union[str | None, Any] = Field(default=None, description="Cover image URL")
    """Cover image URL"""
    pin_thumbnail_urls: Union[list[str] | None, Any] = Field(default=None, description="Thumbnail URLs of pins")
    """Thumbnail URLs of pins"""

class BoardOwner(BaseModel):
    """Board owner details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    username: Union[str | None, Any] = Field(default=None, description="Username of the board owner")
    """Username of the board owner"""

class Board(BaseModel):
    """Pinterest board object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    owner: Union[BoardOwner | None, Any] = Field(default=None)
    is_ads_only: Union[bool | None, Any] = Field(default=None)
    privacy: Union[str | None, Any] = Field(default=None)
    follower_count: Union[int | None, Any] = Field(default=None)
    collaborator_count: Union[int | None, Any] = Field(default=None)
    pin_count: Union[int | None, Any] = Field(default=None)
    media: Union[BoardMedia | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    board_pins_modified_at: Union[str | None, Any] = Field(default=None)

class BoardsList(BaseModel):
    """Paginated list of boards"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Board], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class CampaignTrackingUrls(BaseModel):
    """Third-party tracking URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    impression: Union[list[str] | None, Any] = Field(default=None, description="Impression tracking URLs")
    """Impression tracking URLs"""
    click: Union[list[str] | None, Any] = Field(default=None, description="Click tracking URLs")
    """Click tracking URLs"""
    engagement: Union[list[str] | None, Any] = Field(default=None, description="Engagement tracking URLs")
    """Engagement tracking URLs"""
    buyable_button: Union[list[str] | None, Any] = Field(default=None, description="Buyable button tracking URLs")
    """Buyable button tracking URLs"""
    audience_verification: Union[list[str] | None, Any] = Field(default=None, description="Audience verification tracking URLs")
    """Audience verification tracking URLs"""

class Campaign(BaseModel):
    """Pinterest campaign object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    ad_account_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    lifetime_spend_cap: Union[int | None, Any] = Field(default=None)
    daily_spend_cap: Union[int | None, Any] = Field(default=None)
    order_line_id: Union[str | None, Any] = Field(default=None)
    tracking_urls: Union[CampaignTrackingUrls | None, Any] = Field(default=None)
    objective_type: Union[str | None, Any] = Field(default=None)
    created_time: Union[int | None, Any] = Field(default=None)
    updated_time: Union[int | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    start_time: Union[int | None, Any] = Field(default=None)
    end_time: Union[int | None, Any] = Field(default=None)
    summary_status: Union[str | None, Any] = Field(default=None)
    is_campaign_budget_optimization: Union[bool | None, Any] = Field(default=None)
    is_flexible_daily_budgets: Union[bool | None, Any] = Field(default=None)
    is_performance_plus: Union[bool | None, Any] = Field(default=None)
    is_top_of_search: Union[bool | None, Any] = Field(default=None)
    is_automated_campaign: Union[bool | None, Any] = Field(default=None)
    bid_options: Union[dict[str, Any] | None, Any] = Field(default=None)

class CampaignsList(BaseModel):
    """Paginated list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Campaign], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class AdGroupTrackingUrls(BaseModel):
    """Third-party tracking URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    impression: Union[list[str] | None, Any] = Field(default=None, description="Impression tracking URLs")
    """Impression tracking URLs"""
    click: Union[list[str] | None, Any] = Field(default=None, description="Click tracking URLs")
    """Click tracking URLs"""
    engagement: Union[list[str] | None, Any] = Field(default=None, description="Engagement tracking URLs")
    """Engagement tracking URLs"""
    buyable_button: Union[list[str] | None, Any] = Field(default=None, description="Buyable button tracking URLs")
    """Buyable button tracking URLs"""
    audience_verification: Union[list[str] | None, Any] = Field(default=None, description="Audience verification tracking URLs")
    """Audience verification tracking URLs"""

class AdGroup(BaseModel):
    """Pinterest ad group object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    ad_account_id: Union[str | None, Any] = Field(default=None)
    campaign_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    budget_in_micro_currency: Union[float | None, Any] = Field(default=None)
    bid_in_micro_currency: Union[float | None, Any] = Field(default=None)
    budget_type: Union[str | None, Any] = Field(default=None)
    start_time: Union[float | None, Any] = Field(default=None)
    end_time: Union[float | None, Any] = Field(default=None)
    targeting_spec: Union[dict[str, Any] | None, Any] = Field(default=None)
    lifetime_frequency_cap: Union[float | None, Any] = Field(default=None)
    tracking_urls: Union[AdGroupTrackingUrls | None, Any] = Field(default=None)
    auto_targeting_enabled: Union[bool | None, Any] = Field(default=None)
    placement_group: Union[str | None, Any] = Field(default=None)
    pacing_delivery_type: Union[str | None, Any] = Field(default=None)
    conversion_learning_mode_type: Union[str | None, Any] = Field(default=None)
    summary_status: Union[str | None, Any] = Field(default=None)
    feed_profile_id: Union[str | None, Any] = Field(default=None)
    billable_event: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    created_time: Union[float | None, Any] = Field(default=None)
    updated_time: Union[float | None, Any] = Field(default=None)
    bid_strategy_type: Union[str | None, Any] = Field(default=None)
    optimization_goal_metadata: Union[dict[str, Any] | None, Any] = Field(default=None)
    placement_traffic_type: Union[str | None, Any] = Field(default=None)
    targeting_template_ids: Union[list[str] | None, Any] = Field(default=None)
    is_creative_optimization: Union[bool | None, Any] = Field(default=None)
    promotion_id: Union[str | None, Any] = Field(default=None)
    promotion_ids: Union[list[str] | None, Any] = Field(default=None)
    promotion_application_level: Union[str | None, Any] = Field(default=None)
    bid_multiplier: Union[float | None, Any] = Field(default=None)

class AdGroupsList(BaseModel):
    """Paginated list of ad groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[AdGroup], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class AdTrackingUrls(BaseModel):
    """Third-party tracking URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    impression: Union[list[str] | None, Any] = Field(default=None, description="Impression tracking URLs")
    """Impression tracking URLs"""
    click: Union[list[str] | None, Any] = Field(default=None, description="Click tracking URLs")
    """Click tracking URLs"""
    engagement: Union[list[str] | None, Any] = Field(default=None, description="Engagement tracking URLs")
    """Engagement tracking URLs"""
    buyable_button: Union[list[str] | None, Any] = Field(default=None, description="Buyable button tracking URLs")
    """Buyable button tracking URLs"""
    audience_verification: Union[list[str] | None, Any] = Field(default=None, description="Audience verification tracking URLs")
    """Audience verification tracking URLs"""

class Ad(BaseModel):
    """Pinterest ad object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    ad_group_id: Union[str | None, Any] = Field(default=None)
    ad_account_id: Union[str | None, Any] = Field(default=None)
    campaign_id: Union[str | None, Any] = Field(default=None)
    pin_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    creative_type: Union[str | None, Any] = Field(default=None)
    destination_url: Union[str | None, Any] = Field(default=None)
    click_tracking_url: Union[str | None, Any] = Field(default=None)
    view_tracking_url: Union[str | None, Any] = Field(default=None)
    android_deep_link: Union[str | None, Any] = Field(default=None)
    ios_deep_link: Union[str | None, Any] = Field(default=None)
    carousel_android_deep_links: Union[list[str] | None, Any] = Field(default=None)
    carousel_destination_urls: Union[list[str] | None, Any] = Field(default=None)
    carousel_ios_deep_links: Union[list[str] | None, Any] = Field(default=None)
    tracking_urls: Union[AdTrackingUrls | None, Any] = Field(default=None)
    is_pin_deleted: Union[bool | None, Any] = Field(default=None)
    is_removable: Union[bool | None, Any] = Field(default=None)
    lead_form_id: Union[str | None, Any] = Field(default=None)
    collection_items_destination_url_template: Union[str | None, Any] = Field(default=None)
    created_time: Union[int | None, Any] = Field(default=None)
    updated_time: Union[int | None, Any] = Field(default=None)
    rejected_reasons: Union[list[str] | None, Any] = Field(default=None)
    rejection_labels: Union[list[str] | None, Any] = Field(default=None)
    review_status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    summary_status: Union[str | None, Any] = Field(default=None)
    quiz_pin_data: Union[dict[str, Any] | None, Any] = Field(default=None)
    grid_click_type: Union[str | None, Any] = Field(default=None)
    customizable_cta_type: Union[str | None, Any] = Field(default=None)
    disclosure_type: Union[str | None, Any] = Field(default=None)
    disclosure_url: Union[str | None, Any] = Field(default=None)

class AdsList(BaseModel):
    """Paginated list of ads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Ad], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class BoardSection(BaseModel):
    """Pinterest board section object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class BoardSectionsList(BaseModel):
    """Paginated list of board sections"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[BoardSection], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class BoardPinBoardOwner(BaseModel):
    """Board owner info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    username: Union[str | None, Any] = Field(default=None, description="Username of the board owner")
    """Username of the board owner"""

class BoardPinMedia(BaseModel):
    """Media content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    media_type: Union[str | None, Any] = Field(default=None, description="Type of media")
    """Type of media"""

class BoardPin(BaseModel):
    """Pinterest pin on a board"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    creative_type: Union[str | None, Any] = Field(default=None)
    is_standard: Union[bool | None, Any] = Field(default=None)
    is_owner: Union[bool | None, Any] = Field(default=None)
    dominant_color: Union[str | None, Any] = Field(default=None)
    parent_pin_id: Union[str | None, Any] = Field(default=None)
    link: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    alt_text: Union[str | None, Any] = Field(default=None)
    board_id: Union[str | None, Any] = Field(default=None)
    board_section_id: Union[str | None, Any] = Field(default=None)
    board_owner: Union[BoardPinBoardOwner | None, Any] = Field(default=None)
    media: Union[BoardPinMedia | None, Any] = Field(default=None)
    pin_metrics: Union[dict[str, Any] | None, Any] = Field(default=None)
    has_been_promoted: Union[bool | None, Any] = Field(default=None)
    is_removable: Union[bool | None, Any] = Field(default=None)
    product_tags: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class BoardPinsList(BaseModel):
    """Paginated list of board pins"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[BoardPin], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class Catalog(BaseModel):
    """Pinterest catalog object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    catalog_type: Union[str | None, Any] = Field(default=None)

class CatalogsList(BaseModel):
    """Paginated list of catalogs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Catalog], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class CatalogsFeedPreferredProcessingSchedule(BaseModel):
    """Preferred processing schedule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    time: Union[str | None, Any] = Field(default=None, description="Preferred processing time")
    """Preferred processing time"""
    timezone: Union[str | None, Any] = Field(default=None, description="Timezone for processing")
    """Timezone for processing"""

class CatalogsFeed(BaseModel):
    """Pinterest catalog feed object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    format: Union[str | None, Any] = Field(default=None)
    catalog_type: Union[str | None, Any] = Field(default=None)
    location: Union[str | None, Any] = Field(default=None)
    preferred_processing_schedule: Union[CatalogsFeedPreferredProcessingSchedule | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    default_currency: Union[str | None, Any] = Field(default=None)
    default_locale: Union[str | None, Any] = Field(default=None)
    default_country: Union[str | None, Any] = Field(default=None)
    default_availability: Union[str | None, Any] = Field(default=None)

class CatalogsFeedsList(BaseModel):
    """Paginated list of catalog feeds"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[CatalogsFeed], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class CatalogsProductGroup(BaseModel):
    """Pinterest catalog product group object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    updated_at: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    feed_id: Union[str | None, Any] = Field(default=None)
    is_featured: Union[bool | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")

class CatalogsProductGroupsList(BaseModel):
    """Paginated list of catalog product groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[CatalogsProductGroup], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class AudienceRule(BaseModel):
    """Audience targeting rules"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    country: Union[str | None, Any] = Field(default=None, description="Country criteria")
    """Country criteria"""
    customer_list_id: Union[str | None, Any] = Field(default=None, description="Customer list ID")
    """Customer list ID"""
    engagement_domain: Union[list[str] | None, Any] = Field(default=None, description="Domains for engagement tracking")
    """Domains for engagement tracking"""
    engagement_type: Union[str | None, Any] = Field(default=None, description="Engagement type")
    """Engagement type"""
    event: Union[str | None, Any] = Field(default=None, description="Pinterest tag event")
    """Pinterest tag event"""
    retention_days: Union[int | None, Any] = Field(default=None, description="Days to retain audience data")
    """Days to retain audience data"""
    visitor_source_id: Union[str | None, Any] = Field(default=None, description="Visitor source ID")
    """Visitor source ID"""

class Audience(BaseModel):
    """Pinterest audience object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    ad_account_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    audience_type: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    rule: Union[AudienceRule | None, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    created_timestamp: Union[int | None, Any] = Field(default=None)
    updated_timestamp: Union[int | None, Any] = Field(default=None)
    created_by_company_name: Union[str | None, Any] = Field(default=None)

class AudiencesList(BaseModel):
    """Paginated list of audiences"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Audience], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class ConversionTagConfigs(BaseModel):
    """Tag configurations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    aem_enabled: Union[bool | None, Any] = Field(default=None, description="AEM email integration enabled")
    """AEM email integration enabled"""
    md_frequency: Union[float | None, Any] = Field(default=None, description="Metadata ingestion frequency")
    """Metadata ingestion frequency"""
    aem_fnln_enabled: Union[bool | None, Any] = Field(default=None, description="AEM name integration enabled")
    """AEM name integration enabled"""
    aem_ph_enabled: Union[bool | None, Any] = Field(default=None, description="AEM phone integration enabled")
    """AEM phone integration enabled"""
    aem_ge_enabled: Union[bool | None, Any] = Field(default=None, description="AEM gender integration enabled")
    """AEM gender integration enabled"""
    aem_db_enabled: Union[bool | None, Any] = Field(default=None, description="AEM birthdate integration enabled")
    """AEM birthdate integration enabled"""
    aem_loc_enabled: Union[bool | None, Any] = Field(default=None, description="AEM location integration enabled")
    """AEM location integration enabled"""

class ConversionTag(BaseModel):
    """Pinterest conversion tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    ad_account_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    code_snippet: Union[str | None, Any] = Field(default=None)
    enhanced_match_status: Union[str | None, Any] = Field(default=None)
    last_fired_time_ms: Union[int | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    version: Union[str | None, Any] = Field(default=None)
    configs: Union[ConversionTagConfigs | None, Any] = Field(default=None)

class ConversionTagsList(BaseModel):
    """Paginated list of conversion tags"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[ConversionTag], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class CustomerList(BaseModel):
    """Pinterest customer list object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    ad_account_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    created_time: Union[int | None, Any] = Field(default=None)
    updated_time: Union[int | None, Any] = Field(default=None)
    num_batches: Union[int | None, Any] = Field(default=None)
    num_removed_user_records: Union[int | None, Any] = Field(default=None)
    num_uploaded_user_records: Union[int | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")

class CustomerListsList(BaseModel):
    """Paginated list of customer lists"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[CustomerList], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

class Keyword(BaseModel):
    """Pinterest keyword object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    archived: Union[bool | None, Any] = Field(default=None)
    parent_id: Union[str | None, Any] = Field(default=None)
    parent_type: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    bid: Union[int | None, Any] = Field(default=None)
    match_type: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)

class KeywordsList(BaseModel):
    """Paginated list of keywords"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Keyword], Any] = Field(default=None)
    bookmark: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AdAccountsListResultMeta(BaseModel):
    """Metadata for ad_accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class BoardsListResultMeta(BaseModel):
    """Metadata for boards.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class AdGroupsListResultMeta(BaseModel):
    """Metadata for ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class AdsListResultMeta(BaseModel):
    """Metadata for ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class BoardSectionsListResultMeta(BaseModel):
    """Metadata for board_sections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class BoardPinsListResultMeta(BaseModel):
    """Metadata for board_pins.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class CatalogsListResultMeta(BaseModel):
    """Metadata for catalogs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class CatalogsFeedsListResultMeta(BaseModel):
    """Metadata for catalogs_feeds.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class CatalogsProductGroupsListResultMeta(BaseModel):
    """Metadata for catalogs_product_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class AudiencesListResultMeta(BaseModel):
    """Metadata for audiences.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class ConversionTagsListResultMeta(BaseModel):
    """Metadata for conversion_tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class CustomerListsListResultMeta(BaseModel):
    """Metadata for customer_lists.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

class KeywordsListResultMeta(BaseModel):
    """Metadata for keywords.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bookmark: Union[str | None, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class PinterestCheckResult(BaseModel):
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


class PinterestExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class PinterestExecuteResultWithMeta(PinterestExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AdAccountsSearchData(BaseModel):
    """Search result data for ad_accounts entity."""
    model_config = ConfigDict(extra="allow")

    country: str | None = None
    """Country associated with the ad account"""
    created_time: int | None = None
    """Timestamp when the ad account was created (Unix seconds)"""
    currency: str | None = None
    """Currency used for billing"""
    id: str | None = None
    """Unique identifier for the ad account"""
    name: str | None = None
    """Name of the ad account"""
    owner: dict[str, Any] | None = None
    """Owner details of the ad account"""
    permissions: list[Any] | None = None
    """Permissions assigned to the ad account"""
    updated_time: int | None = None
    """Timestamp when the ad account was last updated (Unix seconds)"""


class BoardsSearchData(BaseModel):
    """Search result data for boards entity."""
    model_config = ConfigDict(extra="allow")

    board_pins_modified_at: str | None = None
    """Timestamp when pins on the board were last modified"""
    collaborator_count: int | None = None
    """Number of collaborators"""
    created_at: str | None = None
    """Timestamp when the board was created"""
    description: str | None = None
    """Board description"""
    follower_count: int | None = None
    """Number of followers"""
    id: str | None = None
    """Unique identifier for the board"""
    media: dict[str, Any] | None = None
    """Media content for the board"""
    name: str | None = None
    """Board name"""
    owner: dict[str, Any] | None = None
    """Board owner details"""
    pin_count: int | None = None
    """Number of pins on the board"""
    privacy: str | None = None
    """Board privacy setting"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Ad account ID"""
    created_time: int | None = None
    """Creation timestamp (Unix seconds)"""
    daily_spend_cap: int | None = None
    """Maximum daily spend in microcurrency"""
    end_time: int | None = None
    """End timestamp (Unix seconds)"""
    id: str | None = None
    """Campaign ID"""
    is_campaign_budget_optimization: bool | None = None
    """Whether CBO is enabled"""
    is_flexible_daily_budgets: bool | None = None
    """Whether flexible daily budgets are enabled"""
    lifetime_spend_cap: int | None = None
    """Maximum lifetime spend in microcurrency"""
    name: str | None = None
    """Campaign name"""
    objective_type: str | None = None
    """Campaign objective type"""
    order_line_id: str | None = None
    """Order line ID on invoice"""
    start_time: int | None = None
    """Start timestamp (Unix seconds)"""
    status: str | None = None
    """Entity status"""
    summary_status: str | None = None
    """Summary status"""
    tracking_urls: dict[str, Any] | None = None
    """Third-party tracking URLs"""
    type_: str | None = None
    """Always 'campaign'"""
    updated_time: int | None = None
    """Last update timestamp (Unix seconds)"""


class AdGroupsSearchData(BaseModel):
    """Search result data for ad_groups entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Ad account ID"""
    auto_targeting_enabled: bool | None = None
    """Whether auto targeting is enabled"""
    bid_in_micro_currency: float | None = None
    """Bid in microcurrency"""
    bid_strategy_type: str | None = None
    """Bid strategy type"""
    billable_event: str | None = None
    """Billable event type"""
    budget_in_micro_currency: float | None = None
    """Budget in microcurrency"""
    budget_type: str | None = None
    """Budget type"""
    campaign_id: str | None = None
    """Parent campaign ID"""
    conversion_learning_mode_type: str | None = None
    """oCPM learn mode type"""
    created_time: float | None = None
    """Creation timestamp (Unix seconds)"""
    end_time: float | None = None
    """End time (Unix seconds)"""
    feed_profile_id: str | None = None
    """Feed profile ID"""
    id: str | None = None
    """Ad group ID"""
    lifetime_frequency_cap: float | None = None
    """Max impressions per user in 30 days"""
    name: str | None = None
    """Ad group name"""
    optimization_goal_metadata: dict[str, Any] | None = None
    """Optimization goal metadata"""
    pacing_delivery_type: str | None = None
    """Pacing delivery type"""
    placement_group: str | None = None
    """Placement group"""
    start_time: float | None = None
    """Start time (Unix seconds)"""
    status: str | None = None
    """Entity status"""
    summary_status: str | None = None
    """Summary status"""
    targeting_spec: dict[str, Any] | None = None
    """Targeting specifications"""
    tracking_urls: dict[str, Any] | None = None
    """Third-party tracking URLs"""
    type_: str | None = None
    """Always 'adgroup'"""
    updated_time: float | None = None
    """Last update timestamp (Unix seconds)"""


class AdsSearchData(BaseModel):
    """Search result data for ads entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Ad account ID"""
    ad_group_id: str | None = None
    """Ad group ID"""
    android_deep_link: str | None = None
    """Android deep link"""
    campaign_id: str | None = None
    """Campaign ID"""
    carousel_android_deep_links: list[Any] | None = None
    """Carousel Android deep links"""
    carousel_destination_urls: list[Any] | None = None
    """Carousel destination URLs"""
    carousel_ios_deep_links: list[Any] | None = None
    """Carousel iOS deep links"""
    click_tracking_url: str | None = None
    """Click tracking URL"""
    collection_items_destination_url_template: str | None = None
    """Template URL for collection items"""
    created_time: int | None = None
    """Creation timestamp (Unix seconds)"""
    creative_type: str | None = None
    """Creative type"""
    destination_url: str | None = None
    """Main destination URL"""
    id: str | None = None
    """Unique ad ID"""
    ios_deep_link: str | None = None
    """iOS deep link"""
    is_pin_deleted: bool | None = None
    """Whether the original pin is deleted"""
    is_removable: bool | None = None
    """Whether the ad is removable"""
    lead_form_id: str | None = None
    """Lead form ID"""
    name: str | None = None
    """Ad name"""
    pin_id: str | None = None
    """Associated pin ID"""
    rejected_reasons: list[Any] | None = None
    """Rejection reasons"""
    rejection_labels: list[Any] | None = None
    """Rejection text labels"""
    review_status: str | None = None
    """Review status"""
    status: str | None = None
    """Entity status"""
    summary_status: str | None = None
    """Summary status"""
    tracking_urls: dict[str, Any] | None = None
    """Third-party tracking URLs"""
    type_: str | None = None
    """Always 'pinpromotion'"""
    updated_time: int | None = None
    """Last update timestamp (Unix seconds)"""
    view_tracking_url: str | None = None
    """View tracking URL"""


class BoardSectionsSearchData(BaseModel):
    """Search result data for board_sections entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the board section"""
    name: str | None = None
    """Name of the board section"""


class BoardPinsSearchData(BaseModel):
    """Search result data for board_pins entity."""
    model_config = ConfigDict(extra="allow")

    alt_text: str | None = None
    """Alternate text for accessibility"""
    board_id: str | None = None
    """Board the pin belongs to"""
    board_owner: dict[str, Any] | None = None
    """Board owner info"""
    board_section_id: str | None = None
    """Section within the board"""
    created_at: str | None = None
    """Timestamp when the pin was created"""
    creative_type: str | None = None
    """Creative type"""
    description: str | None = None
    """Pin description"""
    dominant_color: str | None = None
    """Dominant color from the pin image"""
    has_been_promoted: bool | None = None
    """Whether the pin has been promoted"""
    id: str | None = None
    """Unique pin identifier"""
    is_owner: bool | None = None
    """Whether the current user is the owner"""
    is_standard: bool | None = None
    """Whether the pin is a standard pin"""
    link: str | None = None
    """URL link associated with the pin"""
    media: dict[str, Any] | None = None
    """Media content"""
    parent_pin_id: str | None = None
    """Parent pin ID if this is a repin"""
    pin_metrics: dict[str, Any] | None = None
    """Pin metrics data"""
    title: str | None = None
    """Pin title"""


class CatalogsSearchData(BaseModel):
    """Search result data for catalogs entity."""
    model_config = ConfigDict(extra="allow")

    catalog_type: str | None = None
    """Type of catalog"""
    created_at: str | None = None
    """Timestamp when the catalog was created"""
    id: str | None = None
    """Unique catalog identifier"""
    name: str | None = None
    """Catalog name"""
    updated_at: str | None = None
    """Timestamp when the catalog was last updated"""


class CatalogsFeedsSearchData(BaseModel):
    """Search result data for catalogs_feeds entity."""
    model_config = ConfigDict(extra="allow")

    catalog_type: str | None = None
    """Type of catalog"""
    created_at: str | None = None
    """Timestamp when the feed was created"""
    default_availability: str | None = None
    """Default availability status"""
    default_country: str | None = None
    """Default country"""
    default_currency: str | None = None
    """Default currency for pricing"""
    default_locale: str | None = None
    """Default locale"""
    format: str | None = None
    """Feed format"""
    id: str | None = None
    """Unique feed identifier"""
    location: str | None = None
    """URL where the feed is available"""
    name: str | None = None
    """Feed name"""
    preferred_processing_schedule: dict[str, Any] | None = None
    """Preferred processing schedule"""
    status: str | None = None
    """Feed status"""
    updated_at: str | None = None
    """Timestamp when the feed was last updated"""


class CatalogsProductGroupsSearchData(BaseModel):
    """Search result data for catalogs_product_groups entity."""
    model_config = ConfigDict(extra="allow")

    created_at: int | None = None
    """Creation timestamp (Unix seconds)"""
    description: str | None = None
    """Product group description"""
    feed_id: str | None = None
    """Associated feed ID"""
    id: str | None = None
    """Unique product group identifier"""
    is_featured: bool | None = None
    """Whether the product group is featured"""
    name: str | None = None
    """Product group name"""
    status: str | None = None
    """Product group status"""
    type_: str | None = None
    """Product group type"""
    updated_at: int | None = None
    """Last update timestamp (Unix seconds)"""


class AudiencesSearchData(BaseModel):
    """Search result data for audiences entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Ad account ID"""
    audience_type: str | None = None
    """Audience type"""
    created_timestamp: int | None = None
    """Creation time (Unix seconds)"""
    description: str | None = None
    """Audience description"""
    id: str | None = None
    """Unique audience identifier"""
    name: str | None = None
    """Audience name"""
    rule: dict[str, Any] | None = None
    """Audience targeting rules"""
    size: int | None = None
    """Estimated audience size"""
    status: str | None = None
    """Audience status"""
    type_: str | None = None
    """Always 'audience'"""
    updated_timestamp: int | None = None
    """Last update time (Unix seconds)"""


class ConversionTagsSearchData(BaseModel):
    """Search result data for conversion_tags entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Ad account ID"""
    code_snippet: str | None = None
    """JavaScript code snippet for tracking"""
    configs: dict[str, Any] | None = None
    """Tag configurations"""
    enhanced_match_status: str | None = None
    """Enhanced match status"""
    id: str | None = None
    """Unique conversion tag identifier"""
    last_fired_time_ms: int | None = None
    """Timestamp of last event fired (milliseconds)"""
    name: str | None = None
    """Conversion tag name"""
    status: str | None = None
    """Status"""
    version: str | None = None
    """Version number"""


class CustomerListsSearchData(BaseModel):
    """Search result data for customer_lists entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Associated ad account ID"""
    created_time: int | None = None
    """Creation time (Unix seconds)"""
    id: str | None = None
    """Unique customer list identifier"""
    name: str | None = None
    """Customer list name"""
    num_batches: int | None = None
    """Total number of list updates"""
    num_removed_user_records: int | None = None
    """Count of removed user records"""
    num_uploaded_user_records: int | None = None
    """Count of uploaded user records"""
    status: str | None = None
    """Status"""
    type_: str | None = None
    """Always 'customerlist'"""
    updated_time: int | None = None
    """Last update time (Unix seconds)"""


class KeywordsSearchData(BaseModel):
    """Search result data for keywords entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Whether the keyword is archived"""
    bid: int | None = None
    """Bid value in microcurrency"""
    id: str | None = None
    """Unique keyword identifier"""
    match_type: str | None = None
    """Match type"""
    parent_id: str | None = None
    """Parent entity ID"""
    parent_type: str | None = None
    """Parent entity type"""
    type_: str | None = None
    """Always 'keyword'"""
    value: str | None = None
    """Keyword text value"""


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

AdAccountsSearchResult = AirbyteSearchResult[AdAccountsSearchData]
"""Search result type for ad_accounts entity."""

BoardsSearchResult = AirbyteSearchResult[BoardsSearchData]
"""Search result type for boards entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

AdGroupsSearchResult = AirbyteSearchResult[AdGroupsSearchData]
"""Search result type for ad_groups entity."""

AdsSearchResult = AirbyteSearchResult[AdsSearchData]
"""Search result type for ads entity."""

BoardSectionsSearchResult = AirbyteSearchResult[BoardSectionsSearchData]
"""Search result type for board_sections entity."""

BoardPinsSearchResult = AirbyteSearchResult[BoardPinsSearchData]
"""Search result type for board_pins entity."""

CatalogsSearchResult = AirbyteSearchResult[CatalogsSearchData]
"""Search result type for catalogs entity."""

CatalogsFeedsSearchResult = AirbyteSearchResult[CatalogsFeedsSearchData]
"""Search result type for catalogs_feeds entity."""

CatalogsProductGroupsSearchResult = AirbyteSearchResult[CatalogsProductGroupsSearchData]
"""Search result type for catalogs_product_groups entity."""

AudiencesSearchResult = AirbyteSearchResult[AudiencesSearchData]
"""Search result type for audiences entity."""

ConversionTagsSearchResult = AirbyteSearchResult[ConversionTagsSearchData]
"""Search result type for conversion_tags entity."""

CustomerListsSearchResult = AirbyteSearchResult[CustomerListsSearchData]
"""Search result type for customer_lists entity."""

KeywordsSearchResult = AirbyteSearchResult[KeywordsSearchData]
"""Search result type for keywords entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AdAccountsListResult = PinterestExecuteResultWithMeta[list[AdAccount], AdAccountsListResultMeta]
"""Result type for ad_accounts.list operation with data and metadata."""

BoardsListResult = PinterestExecuteResultWithMeta[list[Board], BoardsListResultMeta]
"""Result type for boards.list operation with data and metadata."""

CampaignsListResult = PinterestExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

AdGroupsListResult = PinterestExecuteResultWithMeta[list[AdGroup], AdGroupsListResultMeta]
"""Result type for ad_groups.list operation with data and metadata."""

AdsListResult = PinterestExecuteResultWithMeta[list[Ad], AdsListResultMeta]
"""Result type for ads.list operation with data and metadata."""

BoardSectionsListResult = PinterestExecuteResultWithMeta[list[BoardSection], BoardSectionsListResultMeta]
"""Result type for board_sections.list operation with data and metadata."""

BoardPinsListResult = PinterestExecuteResultWithMeta[list[BoardPin], BoardPinsListResultMeta]
"""Result type for board_pins.list operation with data and metadata."""

CatalogsListResult = PinterestExecuteResultWithMeta[list[Catalog], CatalogsListResultMeta]
"""Result type for catalogs.list operation with data and metadata."""

CatalogsFeedsListResult = PinterestExecuteResultWithMeta[list[CatalogsFeed], CatalogsFeedsListResultMeta]
"""Result type for catalogs_feeds.list operation with data and metadata."""

CatalogsProductGroupsListResult = PinterestExecuteResultWithMeta[list[CatalogsProductGroup], CatalogsProductGroupsListResultMeta]
"""Result type for catalogs_product_groups.list operation with data and metadata."""

AudiencesListResult = PinterestExecuteResultWithMeta[list[Audience], AudiencesListResultMeta]
"""Result type for audiences.list operation with data and metadata."""

ConversionTagsListResult = PinterestExecuteResultWithMeta[list[ConversionTag], ConversionTagsListResultMeta]
"""Result type for conversion_tags.list operation with data and metadata."""

CustomerListsListResult = PinterestExecuteResultWithMeta[list[CustomerList], CustomerListsListResultMeta]
"""Result type for customer_lists.list operation with data and metadata."""

KeywordsListResult = PinterestExecuteResultWithMeta[list[Keyword], KeywordsListResultMeta]
"""Result type for keywords.list operation with data and metadata."""

