"""
Pydantic models for snapchat-marketing connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class SnapchatMarketingAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The Client ID of your Snapchat developer application"""
    client_secret: str
    """The Client Secret of your Snapchat developer application"""
    refresh_token: str
    """Refresh Token to renew the expired Access Token"""

# Replication configuration

class SnapchatMarketingReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Snapchat Marketing."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """Date in YYYY-MM-DD format. Data before this date will not be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class OrganizationConfigurationSettings(BaseModel):
    """Organization configuration settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    notifications_enabled: Union[bool, Any] = Field(default=None, description="Whether notifications are enabled")
    """Whether notifications are enabled"""

class Organization(BaseModel):
    """Snapchat organization object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    state: Union[str, Any] = Field(default=None)
    address_line_1: Union[str, Any] = Field(default=None)
    administrative_district_level_1: Union[str, Any] = Field(default=None)
    locality: Union[str, Any] = Field(default=None)
    postal_code: Union[str, Any] = Field(default=None)
    country: Union[str, Any] = Field(default=None)
    contact_name: Union[str, Any] = Field(default=None)
    contact_email: Union[str, Any] = Field(default=None)
    contact_phone: Union[str, Any] = Field(default=None)
    contact_phone_optin: Union[bool, Any] = Field(default=None)
    accepted_term_version: Union[str, Any] = Field(default=None)
    configuration_settings: Union[OrganizationConfigurationSettings, Any] = Field(default=None)
    my_display_name: Union[str, Any] = Field(default=None)
    my_invited_email: Union[str, Any] = Field(default=None)
    my_member_id: Union[str, Any] = Field(default=None)
    roles: Union[list[str], Any] = Field(default=None)
    created_by_caller: Union[bool, Any] = Field(default=None, alias="createdByCaller")
    is_agency: Union[bool, Any] = Field(default=None)
    verification_request_id: Union[str, Any] = Field(default=None)
    demand_source: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class AdAccountRegulations(BaseModel):
    """Regulatory settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    restricted_delivery_signals: Union[bool, Any] = Field(default=None, description="Whether restricted delivery signals are enabled")
    """Whether restricted delivery signals are enabled"""

class AdAccount(BaseModel):
    """Snapchat ad account object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    status: Union[str, Any] = Field(default=None)
    organization_id: Union[str, Any] = Field(default=None)
    advertiser_organization_id: Union[str, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    timezone: Union[str, Any] = Field(default=None)
    billing_type: Union[str, Any] = Field(default=None)
    billing_center_id: Union[str, Any] = Field(default=None)
    agency_representing_client: Union[bool, Any] = Field(default=None)
    client_paying_invoices: Union[bool, Any] = Field(default=None)
    funding_source_ids: Union[list[str], Any] = Field(default=None)
    regulations: Union[AdAccountRegulations, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class CampaignObjectiveV2Properties(BaseModel):
    """Objective V2 properties for the campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    objective_v2_type: Union[str, Any] = Field(default=None)
    is_auto_generated: Union[bool, Any] = Field(default=None)

class Campaign(BaseModel):
    """Snapchat campaign object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    ad_account_id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    objective: Union[str, Any] = Field(default=None)
    buy_model: Union[str, Any] = Field(default=None)
    creation_state: Union[str, Any] = Field(default=None)
    start_time: Union[str, Any] = Field(default=None)
    delivery_status: Union[list[str], Any] = Field(default=None)
    objective_v2_properties: Union[CampaignObjectiveV2Properties, Any] = Field(default=None)
    pacing_properties_version: Union[int, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class AdSquadSkadnetworkProperties(BaseModel):
    """SKAdNetwork properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecid_enrollment_status: Union[str, Any] = Field(default=None)
    enable_skoverlay: Union[bool, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)

class AdSquadTargetingAutoExpansionOptionsInterestExpansionOption(BaseModel):
    """Nested schema for AdSquadTargetingAutoExpansionOptions.interest_expansion_option"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None)

class AdSquadTargetingAutoExpansionOptions(BaseModel):
    """Nested schema for AdSquadTargeting.auto_expansion_options"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    interest_expansion_option: Union[AdSquadTargetingAutoExpansionOptionsInterestExpansionOption, Any] = Field(default=None)

class AdSquadTargetingGeosItem(BaseModel):
    """Nested schema for AdSquadTargeting.geos_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    country_code: Union[str, Any] = Field(default=None)
    operation: Union[str, Any] = Field(default=None)

class AdSquadTargeting(BaseModel):
    """Targeting specification"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    regulated_content: Union[bool, Any] = Field(default=None)
    geos: Union[list[AdSquadTargetingGeosItem], Any] = Field(default=None)
    enable_targeting_expansion: Union[bool, Any] = Field(default=None)
    auto_expansion_options: Union[AdSquadTargetingAutoExpansionOptions, Any] = Field(default=None)
    demographics: Union[list[dict[str, Any]], Any] = Field(default=None)
    interests: Union[list[dict[str, Any]], Any] = Field(default=None)
    locations: Union[list[dict[str, Any]], Any] = Field(default=None)

class AdSquad(BaseModel):
    """Snapchat ad squad object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    campaign_id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    auto_bid: Union[bool, Any] = Field(default=None)
    bid_strategy: Union[str, Any] = Field(default=None)
    billing_event: Union[str, Any] = Field(default=None)
    child_ad_type: Union[str, Any] = Field(default=None)
    creation_state: Union[str, Any] = Field(default=None)
    daily_budget_micro: Union[int, Any] = Field(default=None)
    lifetime_budget_micro: Union[int, Any] = Field(default=None)
    delivery_constraint: Union[str, Any] = Field(default=None)
    delivery_properties_version: Union[int, Any] = Field(default=None)
    delivery_status: Union[list[str], Any] = Field(default=None)
    end_time: Union[str, Any] = Field(default=None)
    start_time: Union[str, Any] = Field(default=None)
    forced_view_setting: Union[str, Any] = Field(default=None)
    optimization_goal: Union[str, Any] = Field(default=None)
    pacing_type: Union[str, Any] = Field(default=None)
    placement: Union[str, Any] = Field(default=None)
    target_bid: Union[bool, Any] = Field(default=None)
    targeting: Union[AdSquadTargeting, Any] = Field(default=None)
    targeting_reach_status: Union[str, Any] = Field(default=None)
    skadnetwork_properties: Union[AdSquadSkadnetworkProperties, Any] = Field(default=None)
    event_sources: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Ad(BaseModel):
    """Snapchat ad object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    ad_squad_id: Union[str, Any] = Field(default=None)
    creative_id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    render_type: Union[str, Any] = Field(default=None)
    review_status: Union[str, Any] = Field(default=None)
    review_status_reasons: Union[list[str], Any] = Field(default=None)
    delivery_status: Union[list[str], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class CreativeAdToPlaceProperties(BaseModel):
    """Ad-to-place properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    place_id: Union[str, Any] = Field(default=None)

class CreativeWebViewProperties(BaseModel):
    """Web view properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_snap_javascript_sdk: Union[bool, Any] = Field(default=None)
    block_preload: Union[bool, Any] = Field(default=None)
    deep_link_urls: Union[list[str], Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    use_immersive_mode: Union[bool, Any] = Field(default=None)

class Creative(BaseModel):
    """Snapchat creative object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    ad_account_id: Union[str, Any] = Field(default=None)
    ad_product: Union[str, Any] = Field(default=None)
    brand_name: Union[str, Any] = Field(default=None)
    call_to_action: Union[str, Any] = Field(default=None)
    headline: Union[str, Any] = Field(default=None)
    render_type: Union[str, Any] = Field(default=None)
    review_status: Union[str, Any] = Field(default=None)
    review_status_details: Union[str, Any] = Field(default=None)
    shareable: Union[bool, Any] = Field(default=None)
    forced_view_eligibility: Union[str, Any] = Field(default=None)
    packaging_status: Union[str, Any] = Field(default=None)
    top_snap_crop_position: Union[str, Any] = Field(default=None)
    top_snap_media_id: Union[str, Any] = Field(default=None)
    ad_to_place_properties: Union[CreativeAdToPlaceProperties, Any] = Field(default=None)
    web_view_properties: Union[CreativeWebViewProperties, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class MediaImageMetadata(BaseModel):
    """Image-specific metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    height_px: Union[int, Any] = Field(default=None)
    width_px: Union[int, Any] = Field(default=None)
    image_format: Union[str, Any] = Field(default=None)

class Media(BaseModel):
    """Snapchat media object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    ad_account_id: Union[str, Any] = Field(default=None)
    media_status: Union[str, Any] = Field(default=None)
    file_name: Union[str, Any] = Field(default=None)
    file_size_in_bytes: Union[int, Any] = Field(default=None)
    duration_in_seconds: Union[float, Any] = Field(default=None)
    hash: Union[str, Any] = Field(default=None)
    download_link: Union[str, Any] = Field(default=None)
    is_demo_media: Union[bool, Any] = Field(default=None)
    visibility: Union[str, Any] = Field(default=None)
    media_usages: Union[list[str], Any] = Field(default=None)
    image_metadata: Union[MediaImageMetadata, Any] = Field(default=None)
    video_metadata: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Segment(BaseModel):
    """Snapchat audience segment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    ad_account_id: Union[str, Any] = Field(default=None)
    source_ad_account_id: Union[str, Any] = Field(default=None)
    organization_id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    source_type: Union[str, Any] = Field(default=None)
    targetable_status: Union[str, Any] = Field(default=None)
    upload_status: Union[str, Any] = Field(default=None)
    retention_in_days: Union[int, Any] = Field(default=None)
    approximate_number_users: Union[int, Any] = Field(default=None)
    visible_to: Union[list[str], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class OrganizationsListResultMeta(BaseModel):
    """Metadata for organizations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class AdaccountsListResultMeta(BaseModel):
    """Metadata for adaccounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class AdsquadsListResultMeta(BaseModel):
    """Metadata for adsquads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class AdsListResultMeta(BaseModel):
    """Metadata for ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class CreativesListResultMeta(BaseModel):
    """Metadata for creatives.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class MediaListResultMeta(BaseModel):
    """Metadata for media.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

class SegmentsListResultMeta(BaseModel):
    """Metadata for segments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class SnapchatMarketingCheckResult(BaseModel):
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


class SnapchatMarketingExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class SnapchatMarketingExecuteResultWithMeta(SnapchatMarketingExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class OrganizationsSearchData(BaseModel):
    """Search result data for organizations entity."""
    model_config = ConfigDict(extra="allow")

    accepted_term_version: str | None = None
    """Version of accepted terms"""
    address_line_1: str | None = None
    """Street address"""
    administrative_district_level_1: str | None = None
    """State or province"""
    configuration_settings: dict[str, Any] | None = None
    """Organization configuration settings"""
    contact_email: str | None = None
    """Contact email address"""
    contact_name: str | None = None
    """Contact person name"""
    contact_phone: str | None = None
    """Contact phone number"""
    contact_phone_optin: bool | None = None
    """Whether the contact opted in for phone communications"""
    country: str | None = None
    """Country code"""
    created_by_caller: bool | None = None
    """Whether the organization was created by the caller"""
    created_at: str | None = None
    """Creation timestamp"""
    id: str | None = None
    """Unique organization identifier"""
    locality: str | None = None
    """City or locality"""
    my_display_name: str | None = None
    """Display name of the authenticated user in the organization"""
    my_invited_email: str | None = None
    """Email used to invite the authenticated user"""
    my_member_id: str | None = None
    """Member ID of the authenticated user"""
    name: str | None = None
    """Organization name"""
    postal_code: str | None = None
    """Postal code"""
    roles: list[Any] | None = None
    """Roles of the authenticated user in this organization"""
    state: str | None = None
    """Organization state"""
    type_: str | None = None
    """Organization type"""
    updated_at: str | None = None
    """Last update timestamp"""


class AdaccountsSearchData(BaseModel):
    """Search result data for adaccounts entity."""
    model_config = ConfigDict(extra="allow")

    advertiser_organization_id: str | None = None
    """Advertiser organization ID"""
    agency_representing_client: bool | None = None
    """Whether the account is managed by an agency"""
    billing_center_id: str | None = None
    """Billing center ID"""
    billing_type: str | None = None
    """Billing type"""
    client_paying_invoices: bool | None = None
    """Whether the client pays invoices directly"""
    created_at: str | None = None
    """Creation timestamp"""
    currency: str | None = None
    """Account currency code"""
    funding_source_ids: list[Any] | None = None
    """Associated funding source IDs"""
    id: str | None = None
    """Unique ad account identifier"""
    name: str | None = None
    """Ad account name"""
    organization_id: str | None = None
    """Parent organization ID"""
    regulations: dict[str, Any] | None = None
    """Regulatory settings"""
    status: str | None = None
    """Ad account status"""
    timezone: str | None = None
    """Account timezone"""
    type_: str | None = None
    """Ad account type"""
    updated_at: str | None = None
    """Last update timestamp"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Parent ad account ID"""
    buy_model: str | None = None
    """Buy model type"""
    created_at: str | None = None
    """Creation timestamp"""
    creation_state: str | None = None
    """Creation state"""
    delivery_status: list[Any] | None = None
    """Delivery status messages"""
    id: str | None = None
    """Unique campaign identifier"""
    name: str | None = None
    """Campaign name"""
    objective: str | None = None
    """Campaign objective"""
    start_time: str | None = None
    """Campaign start time"""
    status: str | None = None
    """Campaign status"""
    updated_at: str | None = None
    """Last update timestamp"""


class AdsquadsSearchData(BaseModel):
    """Search result data for adsquads entity."""
    model_config = ConfigDict(extra="allow")

    auto_bid: bool | None = None
    """Whether auto bidding is enabled"""
    bid_strategy: str | None = None
    """Bid strategy"""
    billing_event: str | None = None
    """Billing event type"""
    campaign_id: str | None = None
    """Parent campaign ID"""
    child_ad_type: str | None = None
    """Child ad type"""
    created_at: str | None = None
    """Creation timestamp"""
    creation_state: str | None = None
    """Creation state"""
    daily_budget_micro: int | None = None
    """Daily budget in micro-currency"""
    delivery_constraint: str | None = None
    """Delivery constraint"""
    delivery_properties_version: int | None = None
    """Delivery properties version"""
    delivery_status: list[Any] | None = None
    """Delivery status messages"""
    end_time: str | None = None
    """Ad squad end time"""
    event_sources: dict[str, Any] | None = None
    """Event sources configuration"""
    forced_view_setting: str | None = None
    """Forced view setting"""
    id: str | None = None
    """Unique ad squad identifier"""
    lifetime_budget_micro: int | None = None
    """Lifetime budget in micro-currency"""
    name: str | None = None
    """Ad squad name"""
    optimization_goal: str | None = None
    """Optimization goal"""
    pacing_type: str | None = None
    """Pacing type"""
    placement: str | None = None
    """Placement type"""
    skadnetwork_properties: dict[str, Any] | None = None
    """SKAdNetwork properties"""
    start_time: str | None = None
    """Ad squad start time"""
    status: str | None = None
    """Ad squad status"""
    target_bid: bool | None = None
    """Whether target bid is enabled"""
    targeting: dict[str, Any] | None = None
    """Targeting specification"""
    targeting_reach_status: str | None = None
    """Targeting reach status"""
    type_: str | None = None
    """Ad squad type"""
    updated_at: str | None = None
    """Last update timestamp"""


class AdsSearchData(BaseModel):
    """Search result data for ads entity."""
    model_config = ConfigDict(extra="allow")

    ad_squad_id: str | None = None
    """Parent ad squad ID"""
    created_at: str | None = None
    """Creation timestamp"""
    creative_id: str | None = None
    """Associated creative ID"""
    delivery_status: list[Any] | None = None
    """Delivery status messages"""
    id: str | None = None
    """Unique ad identifier"""
    name: str | None = None
    """Ad name"""
    render_type: str | None = None
    """Render type"""
    review_status: str | None = None
    """Review status"""
    review_status_reasons: list[Any] | None = None
    """Reasons for review status"""
    status: str | None = None
    """Ad status"""
    type_: str | None = None
    """Ad type"""
    updated_at: str | None = None
    """Last update timestamp"""


class CreativesSearchData(BaseModel):
    """Search result data for creatives entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Parent ad account ID"""
    ad_product: str | None = None
    """Ad product type"""
    ad_to_place_properties: dict[str, Any] | None = None
    """Ad-to-place properties"""
    brand_name: str | None = None
    """Brand name displayed in the creative"""
    call_to_action: str | None = None
    """Call to action text"""
    created_at: str | None = None
    """Creation timestamp"""
    forced_view_eligibility: str | None = None
    """Forced view eligibility status"""
    headline: str | None = None
    """Creative headline"""
    id: str | None = None
    """Unique creative identifier"""
    name: str | None = None
    """Creative name"""
    packaging_status: str | None = None
    """Packaging status"""
    render_type: str | None = None
    """Render type"""
    review_status: str | None = None
    """Review status"""
    review_status_details: str | None = None
    """Details about the review status"""
    shareable: bool | None = None
    """Whether the creative is shareable"""
    top_snap_crop_position: str | None = None
    """Top snap crop position"""
    top_snap_media_id: str | None = None
    """Top snap media ID"""
    type_: str | None = None
    """Creative type"""
    updated_at: str | None = None
    """Last update timestamp"""
    web_view_properties: dict[str, Any] | None = None
    """Web view properties"""


class MediaSearchData(BaseModel):
    """Search result data for media entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Parent ad account ID"""
    created_at: str | None = None
    """Creation timestamp"""
    download_link: str | None = None
    """Download URL for the media"""
    duration_in_seconds: float | None = None
    """Duration in seconds for video media"""
    file_name: str | None = None
    """Original file name"""
    file_size_in_bytes: int | None = None
    """File size in bytes"""
    hash: str | None = None
    """Media file hash"""
    id: str | None = None
    """Unique media identifier"""
    image_metadata: dict[str, Any] | None = None
    """Image-specific metadata"""
    is_demo_media: bool | None = None
    """Whether this is demo media"""
    media_status: str | None = None
    """Media processing status"""
    media_usages: list[Any] | None = None
    """Where the media is used"""
    name: str | None = None
    """Media name"""
    type_: str | None = None
    """Media type"""
    updated_at: str | None = None
    """Last update timestamp"""
    video_metadata: dict[str, Any] | None = None
    """Video-specific metadata"""
    visibility: str | None = None
    """Media visibility setting"""


class SegmentsSearchData(BaseModel):
    """Search result data for segments entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """Parent ad account ID"""
    approximate_number_users: int | None = None
    """Approximate number of users in the segment"""
    created_at: str | None = None
    """Creation timestamp"""
    description: str | None = None
    """Segment description"""
    id: str | None = None
    """Unique segment identifier"""
    name: str | None = None
    """Segment name"""
    organization_id: str | None = None
    """Parent organization ID"""
    retention_in_days: int | None = None
    """Data retention period in days"""
    source_type: str | None = None
    """Segment source type"""
    status: str | None = None
    """Segment status"""
    targetable_status: str | None = None
    """Whether the segment is targetable"""
    updated_at: str | None = None
    """Last update timestamp"""
    upload_status: str | None = None
    """Upload processing status"""
    visible_to: list[Any] | None = None
    """Visibility settings"""


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

OrganizationsSearchResult = AirbyteSearchResult[OrganizationsSearchData]
"""Search result type for organizations entity."""

AdaccountsSearchResult = AirbyteSearchResult[AdaccountsSearchData]
"""Search result type for adaccounts entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

AdsquadsSearchResult = AirbyteSearchResult[AdsquadsSearchData]
"""Search result type for adsquads entity."""

AdsSearchResult = AirbyteSearchResult[AdsSearchData]
"""Search result type for ads entity."""

CreativesSearchResult = AirbyteSearchResult[CreativesSearchData]
"""Search result type for creatives entity."""

MediaSearchResult = AirbyteSearchResult[MediaSearchData]
"""Search result type for media entity."""

SegmentsSearchResult = AirbyteSearchResult[SegmentsSearchData]
"""Search result type for segments entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

OrganizationsListResult = SnapchatMarketingExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]
"""Result type for organizations.list operation with data and metadata."""

AdaccountsListResult = SnapchatMarketingExecuteResultWithMeta[list[AdAccount], AdaccountsListResultMeta]
"""Result type for adaccounts.list operation with data and metadata."""

CampaignsListResult = SnapchatMarketingExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

AdsquadsListResult = SnapchatMarketingExecuteResultWithMeta[list[AdSquad], AdsquadsListResultMeta]
"""Result type for adsquads.list operation with data and metadata."""

AdsListResult = SnapchatMarketingExecuteResultWithMeta[list[Ad], AdsListResultMeta]
"""Result type for ads.list operation with data and metadata."""

CreativesListResult = SnapchatMarketingExecuteResultWithMeta[list[Creative], CreativesListResultMeta]
"""Result type for creatives.list operation with data and metadata."""

MediaListResult = SnapchatMarketingExecuteResultWithMeta[list[Media], MediaListResultMeta]
"""Result type for media.list operation with data and metadata."""

SegmentsListResult = SnapchatMarketingExecuteResultWithMeta[list[Segment], SegmentsListResultMeta]
"""Result type for segments.list operation with data and metadata."""

