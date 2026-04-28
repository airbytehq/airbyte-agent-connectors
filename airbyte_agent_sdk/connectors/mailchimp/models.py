"""
Pydantic models for mailchimp connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class MailchimpAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Mailchimp API key. You can find this in your Mailchimp account under Account > Extras > API keys."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Link(BaseModel):
    """A HAL-style link relating the current resource to another."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rel: str | None = Field(default=None)
    href: str | None = Field(default=None)
    method: str | None = Field(default=None)
    target_schema: str | None = Field(default=None, alias="targetSchema")
    schema_: str | None = Field(default=None, alias="schema")

class CampaignReportSummaryEcommerce(BaseModel):
    """E-Commerce stats for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_orders: int | None | None = Field(default=None, description="The total orders for a campaign")
    """The total orders for a campaign"""
    total_spent: float | None | None = Field(default=None, description="The total spent for a campaign")
    """The total spent for a campaign"""
    total_revenue: float | None | None = Field(default=None, description="The total revenue for a campaign")
    """The total revenue for a campaign"""

class CampaignReportSummary(BaseModel):
    """For sent campaigns, a summary of opens, clicks, and e-commerce data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    opens: int | None | None = Field(default=None, description="The total number of opens for a campaign")
    """The total number of opens for a campaign"""
    unique_opens: int | None | None = Field(default=None, description="The number of unique opens")
    """The number of unique opens"""
    open_rate: float | None | None = Field(default=None, description="The number of unique opens divided by the total number of successful deliveries")
    """The number of unique opens divided by the total number of successful deliveries"""
    clicks: int | None | None = Field(default=None, description="The total number of clicks for an campaign")
    """The total number of clicks for an campaign"""
    subscriber_clicks: int | None | None = Field(default=None, description="The number of unique clicks")
    """The number of unique clicks"""
    click_rate: float | None | None = Field(default=None, description="The number of unique clicks divided by the total number of successful deliveries")
    """The number of unique clicks divided by the total number of successful deliveries"""
    ecommerce: CampaignReportSummaryEcommerce | None | None = Field(default=None, description="E-Commerce stats for a campaign")
    """E-Commerce stats for a campaign"""

class CampaignRecipients(BaseModel):
    """List settings for the campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_id: str | None | None = Field(default=None, description="The unique list id")
    """The unique list id"""
    list_is_active: bool | None | None = Field(default=None, description="The status of the list used")
    """The status of the list used"""
    list_name: str | None | None = Field(default=None, description="The name of the list")
    """The name of the list"""
    segment_text: str | None | None = Field(default=None, description="A description of the segment used for the campaign")
    """A description of the segment used for the campaign"""
    recipient_count: int | None | None = Field(default=None, description="Count of the recipients on the associated list")
    """Count of the recipients on the associated list"""

class CampaignTracking(BaseModel):
    """The tracking options for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    opens: bool | None | None = Field(default=None, description="Whether to track opens")
    """Whether to track opens"""
    html_clicks: bool | None | None = Field(default=None, description="Whether to track clicks in the HTML version of the campaign")
    """Whether to track clicks in the HTML version of the campaign"""
    text_clicks: bool | None | None = Field(default=None, description="Whether to track clicks in the plain-text version of the campaign")
    """Whether to track clicks in the plain-text version of the campaign"""
    goal_tracking: bool | None | None = Field(default=None, description="Whether to enable Goal tracking")
    """Whether to enable Goal tracking"""
    ecomm360: bool | None | None = Field(default=None, description="Whether to enable eCommerce360 tracking")
    """Whether to enable eCommerce360 tracking"""
    google_analytics: str | None | None = Field(default=None, description="The custom slug for Google Analytics tracking")
    """The custom slug for Google Analytics tracking"""
    clicktale: str | None | None = Field(default=None, description="The custom slug for ClickTale tracking")
    """The custom slug for ClickTale tracking"""

class CampaignSettings(BaseModel):
    """The settings for your campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subject_line: str | None | None = Field(default=None, description="The subject line for the campaign")
    """The subject line for the campaign"""
    preview_text: str | None | None = Field(default=None, description="The preview text for the campaign")
    """The preview text for the campaign"""
    title: str | None | None = Field(default=None, description="The title of the campaign")
    """The title of the campaign"""
    from_name: str | None | None = Field(default=None, description="The from name on the campaign")
    """The from name on the campaign"""
    reply_to: str | None | None = Field(default=None, description="The reply-to email address for the campaign")
    """The reply-to email address for the campaign"""
    use_conversation: bool | None | None = Field(default=None, description="Use Mailchimp Conversation feature to manage out-of-office replies")
    """Use Mailchimp Conversation feature to manage out-of-office replies"""
    to_name: str | None | None = Field(default=None, description="The campaign's custom to name")
    """The campaign's custom to name"""
    folder_id: str | None | None = Field(default=None, description="If the campaign is listed in a folder")
    """If the campaign is listed in a folder"""
    authenticate: bool | None | None = Field(default=None, description="Whether Mailchimp authenticated the campaign")
    """Whether Mailchimp authenticated the campaign"""
    auto_footer: bool | None | None = Field(default=None, description="Automatically append Mailchimp's default footer to the campaign")
    """Automatically append Mailchimp's default footer to the campaign"""
    inline_css: bool | None | None = Field(default=None, description="Automatically inline the CSS included with the campaign content")
    """Automatically inline the CSS included with the campaign content"""
    auto_tweet: bool | None | None = Field(default=None, description="Automatically tweet a link to the campaign archive page when the campaign is sent")
    """Automatically tweet a link to the campaign archive page when the campaign is sent"""
    fb_comments: bool | None | None = Field(default=None, description="Allows Facebook comments on the campaign")
    """Allows Facebook comments on the campaign"""
    timewarp: bool | None | None = Field(default=None, description="Send this campaign using Timewarp")
    """Send this campaign using Timewarp"""
    template_id: int | None | None = Field(default=None, description="The id for the template used in this campaign")
    """The id for the template used in this campaign"""
    drag_and_drop: bool | None | None = Field(default=None, description="Whether the campaign uses the drag-and-drop editor")
    """Whether the campaign uses the drag-and-drop editor"""

class CampaignDeliveryStatus(BaseModel):
    """Updates on campaigns in the process of sending"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None | None = Field(default=None, description="Whether Campaign Delivery Status is enabled for this account and target campaign")
    """Whether Campaign Delivery Status is enabled for this account and target campaign"""
    can_cancel: bool | None | None = Field(default=None, description="Whether a campaign send can be canceled")
    """Whether a campaign send can be canceled"""
    status: str | None | None = Field(default=None, description="The current state of a campaign delivery")
    """The current state of a campaign delivery"""
    emails_sent: int | None | None = Field(default=None, description="The total number of emails confirmed sent for this campaign so far")
    """The total number of emails confirmed sent for this campaign so far"""
    emails_canceled: int | None | None = Field(default=None, description="The total number of emails canceled for this campaign")
    """The total number of emails canceled for this campaign"""

class Campaign(BaseModel):
    """A summary of an individual campaign's settings and content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    web_id: int | None = Field(default=None)
    parent_campaign_id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    create_time: str | None = Field(default=None)
    archive_url: str | None = Field(default=None)
    long_archive_url: str | None = Field(default=None)
    status: str | None = Field(default=None)
    emails_sent: int | None = Field(default=None)
    send_time: str | None = Field(default=None)
    content_type: str | None = Field(default=None)
    needs_block_refresh: bool | None = Field(default=None)
    resendable: bool | None = Field(default=None)
    recipients: CampaignRecipients | None = Field(default=None)
    settings: CampaignSettings | None = Field(default=None)
    tracking: CampaignTracking | None = Field(default=None)
    report_summary: CampaignReportSummary | None = Field(default=None)
    delivery_status: CampaignDeliveryStatus | None = Field(default=None)

class CampaignsList(BaseModel):
    """A collection of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    campaigns: list[Campaign] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class ListCampaignDefaults(BaseModel):
    """Default values for campaigns created for this list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_name: str | None | None = Field(default=None, description="The default from name for campaigns sent to this list")
    """The default from name for campaigns sent to this list"""
    from_email: str | None | None = Field(default=None, description="The default from email for campaigns sent to this list")
    """The default from email for campaigns sent to this list"""
    subject: str | None | None = Field(default=None, description="The default subject line for campaigns sent to this list")
    """The default subject line for campaigns sent to this list"""
    language: str | None | None = Field(default=None, description="The default language for this list's forms")
    """The default language for this list's forms"""

class ListContact(BaseModel):
    """Contact information displayed in campaign footers to comply with international spam laws"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    company: str | None | None = Field(default=None, description="The company name for the list")
    """The company name for the list"""
    address1: str | None | None = Field(default=None, description="The street address for the list contact")
    """The street address for the list contact"""
    address2: str | None | None = Field(default=None, description="The street address for the list contact")
    """The street address for the list contact"""
    city: str | None | None = Field(default=None, description="The city for the list contact")
    """The city for the list contact"""
    state: str | None | None = Field(default=None, description="The state for the list contact")
    """The state for the list contact"""
    zip: str | None | None = Field(default=None, description="The postal or zip code for the list contact")
    """The postal or zip code for the list contact"""
    country: str | None | None = Field(default=None, description="A two-character ISO3166 country code")
    """A two-character ISO3166 country code"""
    phone: str | None | None = Field(default=None, description="The phone number for the list contact")
    """The phone number for the list contact"""

class ListStats(BaseModel):
    """Stats for the list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    member_count: int | None | None = Field(default=None, description="The number of active members in the list")
    """The number of active members in the list"""
    total_contacts: int | None | None = Field(default=None, description="The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed")
    """The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed"""
    unsubscribe_count: int | None | None = Field(default=None, description="The number of members who have unsubscribed from the list")
    """The number of members who have unsubscribed from the list"""
    cleaned_count: int | None | None = Field(default=None, description="The number of members cleaned from the list")
    """The number of members cleaned from the list"""
    member_count_since_send: int | None | None = Field(default=None, description="The number of active members in the list since the last campaign was sent")
    """The number of active members in the list since the last campaign was sent"""
    unsubscribe_count_since_send: int | None | None = Field(default=None, description="The number of members who have unsubscribed since the last campaign was sent")
    """The number of members who have unsubscribed since the last campaign was sent"""
    cleaned_count_since_send: int | None | None = Field(default=None, description="The number of members cleaned from the list since the last campaign was sent")
    """The number of members cleaned from the list since the last campaign was sent"""
    campaign_count: int | None | None = Field(default=None, description="The number of campaigns in any status that use this list")
    """The number of campaigns in any status that use this list"""
    campaign_last_sent: str | None | None = Field(default=None, description="The date and time the last campaign was sent to this list")
    """The date and time the last campaign was sent to this list"""
    merge_field_count: int | None | None = Field(default=None, description="The number of merge fields for this list")
    """The number of merge fields for this list"""
    avg_sub_rate: float | None | None = Field(default=None, description="The average number of subscriptions per month for the list")
    """The average number of subscriptions per month for the list"""
    avg_unsub_rate: float | None | None = Field(default=None, description="The average number of unsubscriptions per month for the list")
    """The average number of unsubscriptions per month for the list"""
    target_sub_rate: float | None | None = Field(default=None, description="The target number of subscriptions per month for the list to keep it growing")
    """The target number of subscriptions per month for the list to keep it growing"""
    open_rate: float | None | None = Field(default=None, description="The average open rate for campaigns sent to this list")
    """The average open rate for campaigns sent to this list"""
    click_rate: float | None | None = Field(default=None, description="The average click rate for campaigns sent to this list")
    """The average click rate for campaigns sent to this list"""
    last_sub_date: str | None | None = Field(default=None, description="The date and time of the last time someone subscribed to this list")
    """The date and time of the last time someone subscribed to this list"""
    last_unsub_date: str | None | None = Field(default=None, description="The date and time of the last time someone unsubscribed from this list")
    """The date and time of the last time someone unsubscribed from this list"""

class List(BaseModel):
    """Information about a specific list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    web_id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    contact: ListContact | None = Field(default=None)
    permission_reminder: str | None = Field(default=None)
    use_archive_bar: bool | None = Field(default=None)
    campaign_defaults: ListCampaignDefaults | None = Field(default=None)
    notify_on_subscribe: str | None = Field(default=None)
    notify_on_unsubscribe: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    list_rating: int | None = Field(default=None)
    email_type_option: bool | None = Field(default=None)
    subscribe_url_short: str | None = Field(default=None)
    subscribe_url_long: str | None = Field(default=None)
    beamer_address: str | None = Field(default=None)
    visibility: str | None = Field(default=None)
    double_optin: bool | None = Field(default=None)
    has_welcome: bool | None = Field(default=None)
    marketing_permissions: bool | None = Field(default=None)
    stats: ListStats | None = Field(default=None)

class ListsList(BaseModel):
    """A collection of subscriber lists for this account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    lists: list[List] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class ListMemberStatsEcommerceData(BaseModel):
    """Ecommerce stats for the list member if the list is attached to a store"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_revenue: float | None | None = Field(default=None, description="The total revenue the list member has brought in")
    """The total revenue the list member has brought in"""
    number_of_orders: float | None | None = Field(default=None, description="The total number of orders placed by the list member")
    """The total number of orders placed by the list member"""
    currency_code: str | None | None = Field(default=None, description="The three-letter ISO 4217 code for the currency that the store accepts")
    """The three-letter ISO 4217 code for the currency that the store accepts"""

class ListMemberStats(BaseModel):
    """Open and click rates for this subscriber"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avg_open_rate: float | None | None = Field(default=None, description="A subscriber's average open rate")
    """A subscriber's average open rate"""
    avg_click_rate: float | None | None = Field(default=None, description="A subscriber's average clickthrough rate")
    """A subscriber's average clickthrough rate"""
    ecommerce_data: ListMemberStatsEcommerceData | None | None = Field(default=None, description="Ecommerce stats for the list member if the list is attached to a store")
    """Ecommerce stats for the list member if the list is attached to a store"""

class ListMemberLocation(BaseModel):
    """Subscriber location information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    latitude: float | None | None = Field(default=None, description="The location latitude")
    """The location latitude"""
    longitude: float | None | None = Field(default=None, description="The location longitude")
    """The location longitude"""
    gmtoff: int | None | None = Field(default=None, description="The time difference in hours from GMT")
    """The time difference in hours from GMT"""
    dstoff: int | None | None = Field(default=None, description="The offset for timezones where daylight saving time is observed")
    """The offset for timezones where daylight saving time is observed"""
    country_code: str | None | None = Field(default=None, description="The unique code for the location country")
    """The unique code for the location country"""
    timezone: str | None | None = Field(default=None, description="The timezone for the location")
    """The timezone for the location"""
    region: str | None | None = Field(default=None, description="The region for the location")
    """The region for the location"""

class ListMemberTagsItem(BaseModel):
    """Nested schema for ListMember.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="The tag id")
    """The tag id"""
    name: str | None | None = Field(default=None, description="The name of the tag")
    """The name of the tag"""

class ListMember(BaseModel):
    """Individuals who are currently or have been previously subscribed to this list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    email_address: str | None = Field(default=None)
    unique_email_id: str | None = Field(default=None)
    contact_id: str | None = Field(default=None)
    full_name: str | None = Field(default=None)
    web_id: int | None = Field(default=None)
    email_type: str | None = Field(default=None)
    status: str | None = Field(default=None)
    unsubscribe_reason: str | None = Field(default=None)
    consents_to_one_to_one_messaging: bool | None = Field(default=None)
    merge_fields: dict[str, Any] | None = Field(default=None)
    interests: dict[str, bool] | None = Field(default=None)
    stats: ListMemberStats | None = Field(default=None)
    ip_signup: str | None = Field(default=None)
    timestamp_signup: str | None = Field(default=None)
    ip_opt: str | None = Field(default=None)
    timestamp_opt: str | None = Field(default=None)
    member_rating: int | None = Field(default=None)
    last_changed: str | None = Field(default=None)
    language: str | None = Field(default=None)
    vip: bool | None = Field(default=None)
    email_client: str | None = Field(default=None)
    location: ListMemberLocation | None = Field(default=None)
    source: str | None = Field(default=None)
    tags_count: int | None = Field(default=None)
    tags: list[ListMemberTagsItem] | None = Field(default=None)
    list_id: str | None = Field(default=None)

class ListMembersList(BaseModel):
    """Manage members of a specific Mailchimp list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    members: list[ListMember] | None = Field(default=None)
    list_id: str | None = Field(default=None)
    total_items: int | None = Field(default=None)

class ReportClicks(BaseModel):
    """An object describing the click activity for the campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    clicks_total: int | None | None = Field(default=None, description="The total number of clicks for the campaign")
    """The total number of clicks for the campaign"""
    unique_clicks: int | None | None = Field(default=None, description="The total number of unique clicks for links across a campaign")
    """The total number of unique clicks for links across a campaign"""
    unique_subscriber_clicks: int | None | None = Field(default=None, description="The total number of subscribers who clicked on a campaign")
    """The total number of subscribers who clicked on a campaign"""
    click_rate: float | None | None = Field(default=None, description="The number of unique clicks divided by the total number of successful deliveries")
    """The number of unique clicks divided by the total number of successful deliveries"""
    last_click: str | None | None = Field(default=None, description="The date and time of the last recorded click for the campaign")
    """The date and time of the last recorded click for the campaign"""

class ReportBounces(BaseModel):
    """An object describing the bounce summary for the campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hard_bounces: int | None | None = Field(default=None, description="The total number of hard bounced email addresses")
    """The total number of hard bounced email addresses"""
    soft_bounces: int | None | None = Field(default=None, description="The total number of soft bounced email addresses")
    """The total number of soft bounced email addresses"""
    syntax_errors: int | None | None = Field(default=None, description="The total number of addresses that were syntax-related bounces")
    """The total number of addresses that were syntax-related bounces"""

class ReportListStats(BaseModel):
    """The average campaign statistics for your list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sub_rate: float | None | None = Field(default=None, description="The average number of subscriptions per month for the list")
    """The average number of subscriptions per month for the list"""
    unsub_rate: float | None | None = Field(default=None, description="The average number of unsubscriptions per month for the list")
    """The average number of unsubscriptions per month for the list"""
    open_rate: float | None | None = Field(default=None, description="The average open rate for campaigns sent to this list")
    """The average open rate for campaigns sent to this list"""
    click_rate: float | None | None = Field(default=None, description="The average click rate for campaigns sent to this list")
    """The average click rate for campaigns sent to this list"""

class ReportDeliveryStatus(BaseModel):
    """Updates on campaigns in the process of sending"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None | None = Field(default=None, description="Whether Campaign Delivery Status is enabled for this account and target campaign")
    """Whether Campaign Delivery Status is enabled for this account and target campaign"""

class ReportFacebookLikes(BaseModel):
    """An object describing campaign engagement on Facebook"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    recipient_likes: int | None | None = Field(default=None, description="The number of recipients who liked the campaign on Facebook")
    """The number of recipients who liked the campaign on Facebook"""
    unique_likes: int | None | None = Field(default=None, description="The number of unique likes")
    """The number of unique likes"""
    facebook_likes: int | None | None = Field(default=None, description="The number of Facebook likes for the campaign")
    """The number of Facebook likes for the campaign"""

class ReportIndustryStats(BaseModel):
    """The average campaign statistics for your industry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="The type of business industry associated with your account")
    """The type of business industry associated with your account"""
    open_rate: float | None | None = Field(default=None, description="The industry open rate")
    """The industry open rate"""
    click_rate: float | None | None = Field(default=None, description="The industry click rate")
    """The industry click rate"""
    bounce_rate: float | None | None = Field(default=None, description="The industry bounce rate")
    """The industry bounce rate"""
    unopen_rate: float | None | None = Field(default=None, description="The industry unopened rate")
    """The industry unopened rate"""
    unsub_rate: float | None | None = Field(default=None, description="The industry unsubscribe rate")
    """The industry unsubscribe rate"""
    abuse_rate: float | None | None = Field(default=None, description="The industry abuse rate")
    """The industry abuse rate"""

class ReportOpens(BaseModel):
    """An object describing the open activity for the campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    opens_total: int | None | None = Field(default=None, description="The total number of opens for a campaign")
    """The total number of opens for a campaign"""
    unique_opens: int | None | None = Field(default=None, description="The total number of unique opens")
    """The total number of unique opens"""
    open_rate: float | None | None = Field(default=None, description="The number of unique opens divided by the total number of successful deliveries")
    """The number of unique opens divided by the total number of successful deliveries"""
    last_open: str | None | None = Field(default=None, description="The date and time of the last recorded open")
    """The date and time of the last recorded open"""

class ReportEcommerce(BaseModel):
    """E-Commerce stats for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_orders: int | None | None = Field(default=None, description="The total orders for a campaign")
    """The total orders for a campaign"""
    total_spent: float | None | None = Field(default=None, description="The total spent for a campaign")
    """The total spent for a campaign"""
    total_revenue: float | None | None = Field(default=None, description="The total revenue for a campaign")
    """The total revenue for a campaign"""

class ReportForwards(BaseModel):
    """An object describing the forwards and forward activity for the campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    forwards_count: int | None | None = Field(default=None, description="How many times the campaign has been forwarded")
    """How many times the campaign has been forwarded"""
    forwards_opens: int | None | None = Field(default=None, description="How many times the forwarded campaign has been opened")
    """How many times the forwarded campaign has been opened"""

class Report(BaseModel):
    """Report details about a sent campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    campaign_title: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    list_id: str | None = Field(default=None)
    list_is_active: bool | None = Field(default=None)
    list_name: str | None = Field(default=None)
    subject_line: str | None = Field(default=None)
    preview_text: str | None = Field(default=None)
    emails_sent: int | None = Field(default=None)
    abuse_reports: int | None = Field(default=None)
    unsubscribed: int | None = Field(default=None)
    send_time: str | None = Field(default=None)
    rss_last_send: str | None = Field(default=None)
    bounces: ReportBounces | None = Field(default=None)
    forwards: ReportForwards | None = Field(default=None)
    opens: ReportOpens | None = Field(default=None)
    clicks: ReportClicks | None = Field(default=None)
    facebook_likes: ReportFacebookLikes | None = Field(default=None)
    industry_stats: ReportIndustryStats | None = Field(default=None)
    list_stats: ReportListStats | None = Field(default=None)
    ecommerce: ReportEcommerce | None = Field(default=None)
    delivery_status: ReportDeliveryStatus | None = Field(default=None)

class ReportsList(BaseModel):
    """A list of reports containing campaigns marked as Sent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    reports: list[Report] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class EmailActivityActivityItem(BaseModel):
    """Nested schema for EmailActivity.activity_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: str | None | None = Field(default=None, description="One of the following actions open, click, or bounce")
    """One of the following actions open, click, or bounce"""
    timestamp: str | None | None = Field(default=None, description="The date and time recorded for the action")
    """The date and time recorded for the action"""
    url: str | None | None = Field(default=None, description="If the action is a click, the URL on which the member clicked")
    """If the action is a click, the URL on which the member clicked"""
    type_: str | None | None = Field(default=None, alias="type", description="If the action is a bounce, the type of bounce received hard, soft, or blocked")
    """If the action is a bounce, the type of bounce received hard, soft, or blocked"""
    ip: str | None | None = Field(default=None, description="The IP address recorded for the action")
    """The IP address recorded for the action"""

class EmailActivity(BaseModel):
    """A summary of the email activity for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: str | None = Field(default=None)
    list_id: str | None = Field(default=None)
    list_is_active: bool | None = Field(default=None)
    email_id: str | None = Field(default=None)
    email_address: str | None = Field(default=None)
    activity: list[EmailActivityActivityItem] | None = Field(default=None)

class EmailActivityList(BaseModel):
    """A list of member's subscriber activity in a specific campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    emails: list[EmailActivity] | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    total_items: int | None = Field(default=None)

class AutomationReportSummary(BaseModel):
    """A summary of opens and clicks for sent campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    opens: int | None | None = Field(default=None, description="The total number of opens for a campaign")
    """The total number of opens for a campaign"""
    unique_opens: int | None | None = Field(default=None, description="The number of unique opens")
    """The number of unique opens"""
    open_rate: float | None | None = Field(default=None, description="The number of unique opens divided by the total number of successful deliveries")
    """The number of unique opens divided by the total number of successful deliveries"""
    clicks: int | None | None = Field(default=None, description="The total number of clicks for an campaign")
    """The total number of clicks for an campaign"""
    subscriber_clicks: int | None | None = Field(default=None, description="The number of unique clicks")
    """The number of unique clicks"""
    click_rate: float | None | None = Field(default=None, description="The number of unique clicks divided by the total number of successful deliveries")
    """The number of unique clicks divided by the total number of successful deliveries"""

class AutomationSettings(BaseModel):
    """The settings for the Automation workflow"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None, description="The title of the Automation")
    """The title of the Automation"""
    from_name: str | None | None = Field(default=None, description="The from name for the Automation")
    """The from name for the Automation"""
    reply_to: str | None | None = Field(default=None, description="The reply-to email address for the Automation")
    """The reply-to email address for the Automation"""
    use_conversation: bool | None | None = Field(default=None, description="Whether to use Mailchimp Conversation feature")
    """Whether to use Mailchimp Conversation feature"""
    to_name: str | None | None = Field(default=None, description="The Automation's custom to name")
    """The Automation's custom to name"""
    authenticate: bool | None | None = Field(default=None, description="Whether Mailchimp authenticated the Automation")
    """Whether Mailchimp authenticated the Automation"""
    auto_footer: bool | None | None = Field(default=None, description="Whether to automatically append Mailchimp's default footer")
    """Whether to automatically append Mailchimp's default footer"""
    inline_css: bool | None | None = Field(default=None, description="Whether to automatically inline the CSS")
    """Whether to automatically inline the CSS"""

class AutomationTracking(BaseModel):
    """The tracking options for the Automation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    opens: bool | None | None = Field(default=None, description="Whether to track opens")
    """Whether to track opens"""
    html_clicks: bool | None | None = Field(default=None, description="Whether to track clicks in the HTML version")
    """Whether to track clicks in the HTML version"""
    text_clicks: bool | None | None = Field(default=None, description="Whether to track clicks in the plain-text version")
    """Whether to track clicks in the plain-text version"""
    goal_tracking: bool | None | None = Field(default=None, description="Whether to enable Goal tracking")
    """Whether to enable Goal tracking"""
    ecomm360: bool | None | None = Field(default=None, description="Whether to enable eCommerce360 tracking")
    """Whether to enable eCommerce360 tracking"""
    google_analytics: str | None | None = Field(default=None, description="The custom slug for Google Analytics tracking")
    """The custom slug for Google Analytics tracking"""
    clicktale: str | None | None = Field(default=None, description="The custom slug for ClickTale tracking")
    """The custom slug for ClickTale tracking"""

class AutomationRecipientsSegmentOpts(BaseModel):
    """An object representing all segmentation options"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    saved_segment_id: int | None | None = Field(default=None, description="The id for an existing saved segment")
    """The id for an existing saved segment"""
    match: str | None | None = Field(default=None, description="Segment match type")
    """Segment match type"""
    conditions: list[dict[str, Any]] | None | None = Field(default=None, description="Segment match conditions")
    """Segment match conditions"""

class AutomationRecipients(BaseModel):
    """List settings for the Automation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_id: str | None | None = Field(default=None, description="The unique list id")
    """The unique list id"""
    list_is_active: bool | None | None = Field(default=None, description="The status of the list used")
    """The status of the list used"""
    list_name: str | None | None = Field(default=None, description="The name of the list")
    """The name of the list"""
    segment_opts: AutomationRecipientsSegmentOpts | None | None = Field(default=None, description="An object representing all segmentation options")
    """An object representing all segmentation options"""
    store_id: str | None | None = Field(default=None, description="The id of the store")
    """The id of the store"""

class Automation(BaseModel):
    """A summary of an individual Automation workflow's settings and content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    start_time: str | None = Field(default=None)
    status: str | None = Field(default=None)
    emails_sent: int | None = Field(default=None)
    recipients: AutomationRecipients | None = Field(default=None)
    settings: AutomationSettings | None = Field(default=None)
    tracking: AutomationTracking | None = Field(default=None)
    report_summary: AutomationReportSummary | None = Field(default=None)

class AutomationsList(BaseModel):
    """A summary of the Automations for an account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    automations: list[Automation] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class Tag(BaseModel):
    """A tag that can be assigned to a list member"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)

class TagsList(BaseModel):
    """A list of tags assigned to a list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    tags: list[Tag] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class InterestCategory(BaseModel):
    """Interest categories organize interests, which are used to group subscribers based on their preferences"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_id: str | None = Field(default=None)
    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    display_order: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")

class InterestCategoriesList(BaseModel):
    """Information about this list's interest categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    list_id: str | None = Field(default=None)
    categories: list[InterestCategory] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class Interest(BaseModel):
    """Assign subscribers to interests to group them together"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    category_id: str | None = Field(default=None)
    list_id: str | None = Field(default=None)
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    subscriber_count: str | None = Field(default=None)
    display_order: int | None = Field(default=None)

class InterestsList(BaseModel):
    """A list of interests for a specific list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    interests: list[Interest] | None = Field(default=None)
    list_id: str | None = Field(default=None)
    category_id: str | None = Field(default=None)
    total_items: int | None = Field(default=None)

class SegmentOptions(BaseModel):
    """The conditions of the segment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    match: str | None | None = Field(default=None, description="Match type")
    """Match type"""
    conditions: list[dict[str, Any]] | None | None = Field(default=None, description="Segment match conditions")
    """Segment match conditions"""

class Segment(BaseModel):
    """Information about a specific segment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    member_count: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    options: SegmentOptions | None = Field(default=None)
    list_id: str | None = Field(default=None)

class SegmentsList(BaseModel):
    """A list of available segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    segments: list[Segment] | None = Field(default=None)
    list_id: str | None = Field(default=None)
    total_items: int | None = Field(default=None)

class SegmentMemberStats(BaseModel):
    """Open and click rates for this subscriber"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avg_open_rate: float | None | None = Field(default=None, description="A subscriber's average open rate")
    """A subscriber's average open rate"""
    avg_click_rate: float | None | None = Field(default=None, description="A subscriber's average clickthrough rate")
    """A subscriber's average clickthrough rate"""

class SegmentMemberLocation(BaseModel):
    """Subscriber location information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    latitude: float | None | None = Field(default=None, description="The location latitude")
    """The location latitude"""
    longitude: float | None | None = Field(default=None, description="The location longitude")
    """The location longitude"""
    gmtoff: int | None | None = Field(default=None, description="The time difference in hours from GMT")
    """The time difference in hours from GMT"""
    dstoff: int | None | None = Field(default=None, description="The offset for timezones where daylight saving time is observed")
    """The offset for timezones where daylight saving time is observed"""
    country_code: str | None | None = Field(default=None, description="The unique code for the location country")
    """The unique code for the location country"""
    timezone: str | None | None = Field(default=None, description="The timezone for the location")
    """The timezone for the location"""
    region: str | None | None = Field(default=None, description="The region for the location")
    """The region for the location"""

class SegmentMember(BaseModel):
    """Individuals who are currently or have been previously subscribed to this list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    email_address: str | None = Field(default=None)
    unique_email_id: str | None = Field(default=None)
    email_type: str | None = Field(default=None)
    status: str | None = Field(default=None)
    merge_fields: dict[str, Any] | None = Field(default=None)
    interests: dict[str, bool] | None = Field(default=None)
    stats: SegmentMemberStats | None = Field(default=None)
    ip_signup: str | None = Field(default=None)
    timestamp_signup: str | None = Field(default=None)
    ip_opt: str | None = Field(default=None)
    timestamp_opt: str | None = Field(default=None)
    member_rating: int | None = Field(default=None)
    last_changed: str | None = Field(default=None)
    language: str | None = Field(default=None)
    vip: bool | None = Field(default=None)
    email_client: str | None = Field(default=None)
    location: SegmentMemberLocation | None = Field(default=None)
    list_id: str | None = Field(default=None)

class SegmentMembersList(BaseModel):
    """View members in a specific list segment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    members: list[SegmentMember] | None = Field(default=None)
    total_items: int | None = Field(default=None)

class Unsubscribe(BaseModel):
    """A member who unsubscribed from a specific campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email_id: str | None = Field(default=None)
    email_address: str | None = Field(default=None)
    merge_fields: dict[str, Any] | None = Field(default=None)
    vip: bool | None = Field(default=None)
    timestamp: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    list_id: str | None = Field(default=None)
    list_is_active: bool | None = Field(default=None)

class UnsubscribesList(BaseModel):
    """A list of members who have unsubscribed from a specific campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None, alias="_links")
    unsubscribes: list[Unsubscribe] | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    total_items: int | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class ListsListResultMeta(BaseModel):
    """Metadata for lists.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class ListMembersListResultMeta(BaseModel):
    """Metadata for list_members.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class ReportsListResultMeta(BaseModel):
    """Metadata for reports.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class EmailActivityListResultMeta(BaseModel):
    """Metadata for email_activity.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class AutomationsListResultMeta(BaseModel):
    """Metadata for automations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class InterestCategoriesListResultMeta(BaseModel):
    """Metadata for interest_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class InterestsListResultMeta(BaseModel):
    """Metadata for interests.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class SegmentsListResultMeta(BaseModel):
    """Metadata for segments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class SegmentMembersListResultMeta(BaseModel):
    """Metadata for segment_members.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

class UnsubscribesListResultMeta(BaseModel):
    """Metadata for unsubscribes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: list[Link] | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class MailchimpCheckResult(BaseModel):
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


class MailchimpExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class MailchimpExecuteResultWithMeta(MailchimpExecuteResult[T], Generic[T, S]):
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

    ab_split_opts: dict[str, Any] | None = None
    """[A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign."""
    archive_url: str | None = None
    """The link to the campaign's archive version in ISO 8601 format."""
    content_type: str | None = None
    """How the campaign's content is put together."""
    create_time: str | None = None
    """The date and time the campaign was created in ISO 8601 format."""
    delivery_status: dict[str, Any] | None = None
    """Updates on campaigns in the process of sending."""
    emails_sent: int | None = None
    """The total number of emails sent for this campaign."""
    id: str | None = None
    """A string that uniquely identifies this campaign."""
    long_archive_url: str | None = None
    """The original link to the campaign's archive version."""
    needs_block_refresh: bool | None = None
    """Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D..."""
    parent_campaign_id: str | None = None
    """If this campaign is the child of another campaign, this identifies the parent campaign. For Examp..."""
    recipients: dict[str, Any] | None = None
    """List settings for the campaign."""
    report_summary: dict[str, Any] | None = None
    """For sent campaigns, a summary of opens, clicks, and e-commerce data."""
    resendable: bool | None = None
    """Determines if the campaign qualifies to be resent to non-openers."""
    rss_opts: dict[str, Any] | None = None
    """[RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign."""
    send_time: str | None = None
    """The date and time a campaign was sent."""
    settings: dict[str, Any] | None = None
    """The settings for your campaign, including subject, from name, reply-to address, and more."""
    social_card: dict[str, Any] | None = None
    """The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]..."""
    status: str | None = None
    """The current status of the campaign."""
    tracking: dict[str, Any] | None = None
    """The tracking options for a campaign."""
    type_: str | None = None
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: dict[str, Any] | None = None
    """The settings specific to A/B test campaigns."""
    web_id: int | None = None
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


class EmailActivitySearchData(BaseModel):
    """Search result data for email_activity entity."""
    model_config = ConfigDict(extra="allow")

    action: str | None = None
    """One of the following actions: 'open', 'click', or 'bounce'"""
    campaign_id: str | None = None
    """The unique id for the campaign."""
    email_address: str | None = None
    """Email address for a subscriber."""
    email_id: str | None = None
    """The MD5 hash of the lowercase version of the list member's email address."""
    ip: str | None = None
    """The IP address recorded for the action."""
    list_id: str | None = None
    """The unique id for the list."""
    list_is_active: bool | None = None
    """The status of the list used, namely if it's deleted or disabled."""
    timestamp: str | None = None
    """The date and time recorded for the action in ISO 8601 format."""
    type_: str | None = None
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: str | None = None
    """If the action is a 'click', the URL on which the member clicked."""


class ListsSearchData(BaseModel):
    """Search result data for lists entity."""
    model_config = ConfigDict(extra="allow")

    beamer_address: str | None = None
    """The list's Email Beamer address."""
    campaign_defaults: dict[str, Any] | None = None
    """Default values for campaigns created for this list."""
    contact: dict[str, Any] | None = None
    """Contact information displayed in campaign footers to comply with international spam laws."""
    date_created: str | None = None
    """The date and time that this list was created in ISO 8601 format."""
    double_optin: bool | None = None
    """Whether or not to require the subscriber to confirm subscription via email."""
    email_type_option: bool | None = None
    """Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose..."""
    has_welcome: bool | None = None
    """Whether or not this list has a welcome automation connected."""
    id: str | None = None
    """A string that uniquely identifies this list."""
    list_rating: int | None = None
    """An auto-generated activity score for the list (0-5)."""
    marketing_permissions: bool | None = None
    """Whether or not the list has marketing permissions (eg. GDPR) enabled."""
    modules: list[Any] | None = None
    """Any list-specific modules installed for this list."""
    name: str | None = None
    """The name of the list."""
    notify_on_subscribe: str | None = None
    """The email address to send subscribe notifications to."""
    notify_on_unsubscribe: str | None = None
    """The email address to send unsubscribe notifications to."""
    permission_reminder: str | None = None
    """The permission reminder for the list."""
    stats: dict[str, Any] | None = None
    """Stats for the list. Many of these are cached for at least five minutes."""
    subscribe_url_long: str | None = None
    """The full version of this list's subscribe form (host will vary)."""
    subscribe_url_short: str | None = None
    """Our EepURL shortened version of this list's subscribe form."""
    use_archive_bar: bool | None = None
    """Whether campaigns for this list use the Archive Bar in archives by default."""
    visibility: str | None = None
    """Whether this list is public or private."""
    web_id: int | None = None
    """The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:..."""


class ReportsSearchData(BaseModel):
    """Search result data for reports entity."""
    model_config = ConfigDict(extra="allow")

    ab_split: dict[str, Any] | None = None
    """General stats about different groups of an A/B Split campaign. Does not return information about ..."""
    abuse_reports: int | None = None
    """The number of abuse reports generated for this campaign."""
    bounces: dict[str, Any] | None = None
    """An object describing the bounce summary for the campaign."""
    campaign_title: str | None = None
    """The title of the campaign."""
    clicks: dict[str, Any] | None = None
    """An object describing the click activity for the campaign."""
    delivery_status: dict[str, Any] | None = None
    """Updates on campaigns in the process of sending."""
    ecommerce: dict[str, Any] | None = None
    """E-Commerce stats for a campaign."""
    emails_sent: int | None = None
    """The total number of emails sent for this campaign."""
    facebook_likes: dict[str, Any] | None = None
    """An object describing campaign engagement on Facebook."""
    forwards: dict[str, Any] | None = None
    """An object describing the forwards and forward activity for the campaign."""
    id: str | None = None
    """A string that uniquely identifies this campaign."""
    industry_stats: dict[str, Any] | None = None
    """The average campaign statistics for your industry."""
    list_id: str | None = None
    """The unique list id."""
    list_is_active: bool | None = None
    """The status of the list used, namely if it's deleted or disabled."""
    list_name: str | None = None
    """The name of the list."""
    list_stats: dict[str, Any] | None = None
    """The average campaign statistics for your list. This won't be present if we haven't calculated i..."""
    opens: dict[str, Any] | None = None
    """An object describing the open activity for the campaign."""
    preview_text: str | None = None
    """The preview text for the campaign."""
    rss_last_send: str | None = None
    """For RSS campaigns, the date and time of the last send in ISO 8601 format."""
    send_time: str | None = None
    """The date and time a campaign was sent in ISO 8601 format."""
    share_report: dict[str, Any] | None = None
    """The url and password for the VIP report."""
    subject_line: str | None = None
    """The subject line for the campaign."""
    timeseries: list[Any] | None = None
    """An hourly breakdown of the performance of the campaign over the first 24 hours."""
    timewarp: list[Any] | None = None
    """An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp."""
    type_: str | None = None
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: int | None = None
    """The total number of unsubscribed members for this campaign."""


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

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

EmailActivitySearchResult = AirbyteSearchResult[EmailActivitySearchData]
"""Search result type for email_activity entity."""

ListsSearchResult = AirbyteSearchResult[ListsSearchData]
"""Search result type for lists entity."""

ReportsSearchResult = AirbyteSearchResult[ReportsSearchData]
"""Search result type for reports entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CampaignsListResult = MailchimpExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

ListsListResult = MailchimpExecuteResultWithMeta[list[List], ListsListResultMeta]
"""Result type for lists.list operation with data and metadata."""

ListMembersListResult = MailchimpExecuteResultWithMeta[list[ListMember], ListMembersListResultMeta]
"""Result type for list_members.list operation with data and metadata."""

ReportsListResult = MailchimpExecuteResultWithMeta[list[Report], ReportsListResultMeta]
"""Result type for reports.list operation with data and metadata."""

EmailActivityListResult = MailchimpExecuteResultWithMeta[list[EmailActivity], EmailActivityListResultMeta]
"""Result type for email_activity.list operation with data and metadata."""

AutomationsListResult = MailchimpExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]
"""Result type for automations.list operation with data and metadata."""

TagsListResult = MailchimpExecuteResultWithMeta[list[Tag], TagsListResultMeta]
"""Result type for tags.list operation with data and metadata."""

InterestCategoriesListResult = MailchimpExecuteResultWithMeta[list[InterestCategory], InterestCategoriesListResultMeta]
"""Result type for interest_categories.list operation with data and metadata."""

InterestsListResult = MailchimpExecuteResultWithMeta[list[Interest], InterestsListResultMeta]
"""Result type for interests.list operation with data and metadata."""

SegmentsListResult = MailchimpExecuteResultWithMeta[list[Segment], SegmentsListResultMeta]
"""Result type for segments.list operation with data and metadata."""

SegmentMembersListResult = MailchimpExecuteResultWithMeta[list[SegmentMember], SegmentMembersListResultMeta]
"""Result type for segment_members.list operation with data and metadata."""

UnsubscribesListResult = MailchimpExecuteResultWithMeta[list[Unsubscribe], UnsubscribesListResultMeta]
"""Result type for unsubscribes.list operation with data and metadata."""

