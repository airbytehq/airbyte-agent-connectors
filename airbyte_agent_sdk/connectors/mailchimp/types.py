"""
Type definitions for mailchimp connector.
"""
# ruff: noqa: E501
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    type: NotRequired[str]
    status: NotRequired[str]
    before_send_time: NotRequired[str]
    since_send_time: NotRequired[str]
    before_create_time: NotRequired[str]
    since_create_time: NotRequired[str]
    list_id: NotRequired[str]
    folder_id: NotRequired[str]
    sort_field: NotRequired[str]
    sort_dir: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    campaign_id: str

class ListsListParams(TypedDict):
    """Parameters for lists.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    before_date_created: NotRequired[str]
    since_date_created: NotRequired[str]
    before_campaign_last_sent: NotRequired[str]
    since_campaign_last_sent: NotRequired[str]
    email: NotRequired[str]
    sort_field: NotRequired[str]
    sort_dir: NotRequired[str]

class ListsGetParams(TypedDict):
    """Parameters for lists.get operation"""
    list_id: str

class ListMembersListParams(TypedDict):
    """Parameters for list_members.list operation"""
    list_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
    email_type: NotRequired[str]
    status: NotRequired[str]
    since_timestamp_opt: NotRequired[str]
    before_timestamp_opt: NotRequired[str]
    since_last_changed: NotRequired[str]
    before_last_changed: NotRequired[str]
    unique_email_id: NotRequired[str]
    vip_only: NotRequired[bool]
    interest_category_id: NotRequired[str]
    interest_ids: NotRequired[str]
    interest_match: NotRequired[str]
    sort_field: NotRequired[str]
    sort_dir: NotRequired[str]

class ListMembersGetParams(TypedDict):
    """Parameters for list_members.get operation"""
    list_id: str
    subscriber_hash: str

class ReportsListParams(TypedDict):
    """Parameters for reports.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    type: NotRequired[str]
    before_send_time: NotRequired[str]
    since_send_time: NotRequired[str]

class ReportsGetParams(TypedDict):
    """Parameters for reports.get operation"""
    campaign_id: str

class EmailActivityListParams(TypedDict):
    """Parameters for email_activity.list operation"""
    campaign_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
    since: NotRequired[str]

class AutomationsListParams(TypedDict):
    """Parameters for automations.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    before_create_time: NotRequired[str]
    since_create_time: NotRequired[str]
    before_start_time: NotRequired[str]
    since_start_time: NotRequired[str]
    status: NotRequired[str]

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    list_id: str
    name: NotRequired[str]

class InterestCategoriesListParams(TypedDict):
    """Parameters for interest_categories.list operation"""
    list_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

class InterestCategoriesGetParams(TypedDict):
    """Parameters for interest_categories.get operation"""
    list_id: str
    interest_category_id: str

class InterestsListParams(TypedDict):
    """Parameters for interests.list operation"""
    list_id: str
    interest_category_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

class InterestsGetParams(TypedDict):
    """Parameters for interests.get operation"""
    list_id: str
    interest_category_id: str
    interest_id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    list_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
    type: NotRequired[str]
    since_created_at: NotRequired[str]
    before_created_at: NotRequired[str]
    since_updated_at: NotRequired[str]
    before_updated_at: NotRequired[str]

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    list_id: str
    segment_id: str

class SegmentMembersListParams(TypedDict):
    """Parameters for segment_members.list operation"""
    list_id: str
    segment_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

class UnsubscribesListParams(TypedDict):
    """Parameters for unsubscribes.list operation"""
    campaign_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    ab_split_opts: dict[str, Any] | None
    """[A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign."""
    archive_url: str | None
    """The link to the campaign's archive version in ISO 8601 format."""
    content_type: str | None
    """How the campaign's content is put together."""
    create_time: str | None
    """The date and time the campaign was created in ISO 8601 format."""
    delivery_status: dict[str, Any] | None
    """Updates on campaigns in the process of sending."""
    emails_sent: int | None
    """The total number of emails sent for this campaign."""
    id: str | None
    """A string that uniquely identifies this campaign."""
    long_archive_url: str | None
    """The original link to the campaign's archive version."""
    needs_block_refresh: bool | None
    """Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D..."""
    parent_campaign_id: str | None
    """If this campaign is the child of another campaign, this identifies the parent campaign. For Examp..."""
    recipients: dict[str, Any] | None
    """List settings for the campaign."""
    report_summary: dict[str, Any] | None
    """For sent campaigns, a summary of opens, clicks, and e-commerce data."""
    resendable: bool | None
    """Determines if the campaign qualifies to be resent to non-openers."""
    rss_opts: dict[str, Any] | None
    """[RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign."""
    send_time: str | None
    """The date and time a campaign was sent."""
    settings: dict[str, Any] | None
    """The settings for your campaign, including subject, from name, reply-to address, and more."""
    social_card: dict[str, Any] | None
    """The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]..."""
    status: str | None
    """The current status of the campaign."""
    tracking: dict[str, Any] | None
    """The tracking options for a campaign."""
    type_: str | None
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: dict[str, Any] | None
    """The settings specific to A/B test campaigns."""
    web_id: int | None
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ab_split_opts: list[dict[str, Any]]
    """[A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign."""
    archive_url: list[str]
    """The link to the campaign's archive version in ISO 8601 format."""
    content_type: list[str]
    """How the campaign's content is put together."""
    create_time: list[str]
    """The date and time the campaign was created in ISO 8601 format."""
    delivery_status: list[dict[str, Any]]
    """Updates on campaigns in the process of sending."""
    emails_sent: list[int]
    """The total number of emails sent for this campaign."""
    id: list[str]
    """A string that uniquely identifies this campaign."""
    long_archive_url: list[str]
    """The original link to the campaign's archive version."""
    needs_block_refresh: list[bool]
    """Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D..."""
    parent_campaign_id: list[str]
    """If this campaign is the child of another campaign, this identifies the parent campaign. For Examp..."""
    recipients: list[dict[str, Any]]
    """List settings for the campaign."""
    report_summary: list[dict[str, Any]]
    """For sent campaigns, a summary of opens, clicks, and e-commerce data."""
    resendable: list[bool]
    """Determines if the campaign qualifies to be resent to non-openers."""
    rss_opts: list[dict[str, Any]]
    """[RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign."""
    send_time: list[str]
    """The date and time a campaign was sent."""
    settings: list[dict[str, Any]]
    """The settings for your campaign, including subject, from name, reply-to address, and more."""
    social_card: list[dict[str, Any]]
    """The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]..."""
    status: list[str]
    """The current status of the campaign."""
    tracking: list[dict[str, Any]]
    """The tracking options for a campaign."""
    type_: list[str]
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: list[dict[str, Any]]
    """The settings specific to A/B test campaigns."""
    web_id: list[int]
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ab_split_opts: Any
    """[A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign."""
    archive_url: Any
    """The link to the campaign's archive version in ISO 8601 format."""
    content_type: Any
    """How the campaign's content is put together."""
    create_time: Any
    """The date and time the campaign was created in ISO 8601 format."""
    delivery_status: Any
    """Updates on campaigns in the process of sending."""
    emails_sent: Any
    """The total number of emails sent for this campaign."""
    id: Any
    """A string that uniquely identifies this campaign."""
    long_archive_url: Any
    """The original link to the campaign's archive version."""
    needs_block_refresh: Any
    """Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D..."""
    parent_campaign_id: Any
    """If this campaign is the child of another campaign, this identifies the parent campaign. For Examp..."""
    recipients: Any
    """List settings for the campaign."""
    report_summary: Any
    """For sent campaigns, a summary of opens, clicks, and e-commerce data."""
    resendable: Any
    """Determines if the campaign qualifies to be resent to non-openers."""
    rss_opts: Any
    """[RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign."""
    send_time: Any
    """The date and time a campaign was sent."""
    settings: Any
    """The settings for your campaign, including subject, from name, reply-to address, and more."""
    social_card: Any
    """The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]..."""
    status: Any
    """The current status of the campaign."""
    tracking: Any
    """The tracking options for a campaign."""
    type_: Any
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: Any
    """The settings specific to A/B test campaigns."""
    web_id: Any
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    ab_split_opts: str
    """[A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign."""
    archive_url: str
    """The link to the campaign's archive version in ISO 8601 format."""
    content_type: str
    """How the campaign's content is put together."""
    create_time: str
    """The date and time the campaign was created in ISO 8601 format."""
    delivery_status: str
    """Updates on campaigns in the process of sending."""
    emails_sent: str
    """The total number of emails sent for this campaign."""
    id: str
    """A string that uniquely identifies this campaign."""
    long_archive_url: str
    """The original link to the campaign's archive version."""
    needs_block_refresh: str
    """Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D..."""
    parent_campaign_id: str
    """If this campaign is the child of another campaign, this identifies the parent campaign. For Examp..."""
    recipients: str
    """List settings for the campaign."""
    report_summary: str
    """For sent campaigns, a summary of opens, clicks, and e-commerce data."""
    resendable: str
    """Determines if the campaign qualifies to be resent to non-openers."""
    rss_opts: str
    """[RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign."""
    send_time: str
    """The date and time a campaign was sent."""
    settings: str
    """The settings for your campaign, including subject, from name, reply-to address, and more."""
    social_card: str
    """The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]..."""
    status: str
    """The current status of the campaign."""
    tracking: str
    """The tracking options for a campaign."""
    type_: str
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: str
    """The settings specific to A/B test campaigns."""
    web_id: str
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    ab_split_opts: AirbyteSortOrder
    """[A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign."""
    archive_url: AirbyteSortOrder
    """The link to the campaign's archive version in ISO 8601 format."""
    content_type: AirbyteSortOrder
    """How the campaign's content is put together."""
    create_time: AirbyteSortOrder
    """The date and time the campaign was created in ISO 8601 format."""
    delivery_status: AirbyteSortOrder
    """Updates on campaigns in the process of sending."""
    emails_sent: AirbyteSortOrder
    """The total number of emails sent for this campaign."""
    id: AirbyteSortOrder
    """A string that uniquely identifies this campaign."""
    long_archive_url: AirbyteSortOrder
    """The original link to the campaign's archive version."""
    needs_block_refresh: AirbyteSortOrder
    """Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D..."""
    parent_campaign_id: AirbyteSortOrder
    """If this campaign is the child of another campaign, this identifies the parent campaign. For Examp..."""
    recipients: AirbyteSortOrder
    """List settings for the campaign."""
    report_summary: AirbyteSortOrder
    """For sent campaigns, a summary of opens, clicks, and e-commerce data."""
    resendable: AirbyteSortOrder
    """Determines if the campaign qualifies to be resent to non-openers."""
    rss_opts: AirbyteSortOrder
    """[RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign."""
    send_time: AirbyteSortOrder
    """The date and time a campaign was sent."""
    settings: AirbyteSortOrder
    """The settings for your campaign, including subject, from name, reply-to address, and more."""
    social_card: AirbyteSortOrder
    """The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]..."""
    status: AirbyteSortOrder
    """The current status of the campaign."""
    tracking: AirbyteSortOrder
    """The tracking options for a campaign."""
    type_: AirbyteSortOrder
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: AirbyteSortOrder
    """The settings specific to A/B test campaigns."""
    web_id: AirbyteSortOrder
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


# Entity-specific condition types for campaigns
class CampaignsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignsSearchFilter


class CampaignsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignsSearchFilter


class CampaignsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignsSearchFilter


class CampaignsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignsSearchFilter


class CampaignsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignsSearchFilter


class CampaignsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignsSearchFilter


class CampaignsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CampaignsStringFilter


class CampaignsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: CampaignsAnyValueFilter


class CampaignsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: CampaignsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignsInCondition = TypedDict("CampaignsInCondition", {"in": CampaignsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignsNotCondition = TypedDict("CampaignsNotCondition", {"not": "CampaignsCondition"}, total=False)
"""Negates the nested condition."""

CampaignsAndCondition = TypedDict("CampaignsAndCondition", {"and": "list[CampaignsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignsOrCondition = TypedDict("CampaignsOrCondition", {"or": "list[CampaignsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignsAnyCondition = TypedDict("CampaignsAnyCondition", {"any": CampaignsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaigns condition types
CampaignsCondition = (
    CampaignsEqCondition
    | CampaignsNeqCondition
    | CampaignsGtCondition
    | CampaignsGteCondition
    | CampaignsLtCondition
    | CampaignsLteCondition
    | CampaignsInCondition
    | CampaignsStartswithCondition
    | CampaignsEndswithCondition
    | CampaignsFuzzyCondition
    | CampaignsKeywordCondition
    | CampaignsContainsCondition
    | CampaignsArrayContainsCondition
    | CampaignsNotCondition
    | CampaignsAndCondition
    | CampaignsOrCondition
    | CampaignsAnyCondition
)


class CampaignsSearchQuery(TypedDict, total=False):
    """Search query for campaigns entity."""
    filter: CampaignsCondition
    sort: list[CampaignsSortFilter]


# ===== EMAIL_ACTIVITY SEARCH TYPES =====

class EmailActivitySearchFilter(TypedDict, total=False):
    """Available fields for filtering email_activity search queries."""
    action: str | None
    """One of the following actions: 'open', 'click', or 'bounce'"""
    campaign_id: str | None
    """The unique id for the campaign."""
    email_address: str | None
    """Email address for a subscriber."""
    email_id: str | None
    """The MD5 hash of the lowercase version of the list member's email address."""
    ip: str | None
    """The IP address recorded for the action."""
    list_id: str | None
    """The unique id for the list."""
    list_is_active: bool | None
    """The status of the list used, namely if it's deleted or disabled."""
    timestamp: str | None
    """The date and time recorded for the action in ISO 8601 format."""
    type_: str | None
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: str | None
    """If the action is a 'click', the URL on which the member clicked."""


class EmailActivityInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action: list[str]
    """One of the following actions: 'open', 'click', or 'bounce'"""
    campaign_id: list[str]
    """The unique id for the campaign."""
    email_address: list[str]
    """Email address for a subscriber."""
    email_id: list[str]
    """The MD5 hash of the lowercase version of the list member's email address."""
    ip: list[str]
    """The IP address recorded for the action."""
    list_id: list[str]
    """The unique id for the list."""
    list_is_active: list[bool]
    """The status of the list used, namely if it's deleted or disabled."""
    timestamp: list[str]
    """The date and time recorded for the action in ISO 8601 format."""
    type_: list[str]
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: list[str]
    """If the action is a 'click', the URL on which the member clicked."""


class EmailActivityAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action: Any
    """One of the following actions: 'open', 'click', or 'bounce'"""
    campaign_id: Any
    """The unique id for the campaign."""
    email_address: Any
    """Email address for a subscriber."""
    email_id: Any
    """The MD5 hash of the lowercase version of the list member's email address."""
    ip: Any
    """The IP address recorded for the action."""
    list_id: Any
    """The unique id for the list."""
    list_is_active: Any
    """The status of the list used, namely if it's deleted or disabled."""
    timestamp: Any
    """The date and time recorded for the action in ISO 8601 format."""
    type_: Any
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: Any
    """If the action is a 'click', the URL on which the member clicked."""


class EmailActivityStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action: str
    """One of the following actions: 'open', 'click', or 'bounce'"""
    campaign_id: str
    """The unique id for the campaign."""
    email_address: str
    """Email address for a subscriber."""
    email_id: str
    """The MD5 hash of the lowercase version of the list member's email address."""
    ip: str
    """The IP address recorded for the action."""
    list_id: str
    """The unique id for the list."""
    list_is_active: str
    """The status of the list used, namely if it's deleted or disabled."""
    timestamp: str
    """The date and time recorded for the action in ISO 8601 format."""
    type_: str
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: str
    """If the action is a 'click', the URL on which the member clicked."""


class EmailActivitySortFilter(TypedDict, total=False):
    """Available fields for sorting email_activity search results."""
    action: AirbyteSortOrder
    """One of the following actions: 'open', 'click', or 'bounce'"""
    campaign_id: AirbyteSortOrder
    """The unique id for the campaign."""
    email_address: AirbyteSortOrder
    """Email address for a subscriber."""
    email_id: AirbyteSortOrder
    """The MD5 hash of the lowercase version of the list member's email address."""
    ip: AirbyteSortOrder
    """The IP address recorded for the action."""
    list_id: AirbyteSortOrder
    """The unique id for the list."""
    list_is_active: AirbyteSortOrder
    """The status of the list used, namely if it's deleted or disabled."""
    timestamp: AirbyteSortOrder
    """The date and time recorded for the action in ISO 8601 format."""
    type_: AirbyteSortOrder
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: AirbyteSortOrder
    """If the action is a 'click', the URL on which the member clicked."""


# Entity-specific condition types for email_activity
class EmailActivityEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EmailActivitySearchFilter


class EmailActivityNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EmailActivitySearchFilter


class EmailActivityGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EmailActivitySearchFilter


class EmailActivityGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EmailActivitySearchFilter


class EmailActivityLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EmailActivitySearchFilter


class EmailActivityLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EmailActivitySearchFilter


class EmailActivityStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: EmailActivityStringFilter


class EmailActivityEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: EmailActivityStringFilter


class EmailActivityFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EmailActivityStringFilter


class EmailActivityKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EmailActivityStringFilter


class EmailActivityContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: EmailActivityAnyValueFilter


class EmailActivityArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: EmailActivityAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EmailActivityInCondition = TypedDict("EmailActivityInCondition", {"in": EmailActivityInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EmailActivityNotCondition = TypedDict("EmailActivityNotCondition", {"not": "EmailActivityCondition"}, total=False)
"""Negates the nested condition."""

EmailActivityAndCondition = TypedDict("EmailActivityAndCondition", {"and": "list[EmailActivityCondition]"}, total=False)
"""True if all nested conditions are true."""

EmailActivityOrCondition = TypedDict("EmailActivityOrCondition", {"or": "list[EmailActivityCondition]"}, total=False)
"""True if any nested condition is true."""

EmailActivityAnyCondition = TypedDict("EmailActivityAnyCondition", {"any": EmailActivityAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all email_activity condition types
EmailActivityCondition = (
    EmailActivityEqCondition
    | EmailActivityNeqCondition
    | EmailActivityGtCondition
    | EmailActivityGteCondition
    | EmailActivityLtCondition
    | EmailActivityLteCondition
    | EmailActivityInCondition
    | EmailActivityStartswithCondition
    | EmailActivityEndswithCondition
    | EmailActivityFuzzyCondition
    | EmailActivityKeywordCondition
    | EmailActivityContainsCondition
    | EmailActivityArrayContainsCondition
    | EmailActivityNotCondition
    | EmailActivityAndCondition
    | EmailActivityOrCondition
    | EmailActivityAnyCondition
)


class EmailActivitySearchQuery(TypedDict, total=False):
    """Search query for email_activity entity."""
    filter: EmailActivityCondition
    sort: list[EmailActivitySortFilter]


# ===== LISTS SEARCH TYPES =====

class ListsSearchFilter(TypedDict, total=False):
    """Available fields for filtering lists search queries."""
    beamer_address: str | None
    """The list's Email Beamer address."""
    campaign_defaults: dict[str, Any] | None
    """Default values for campaigns created for this list."""
    contact: dict[str, Any] | None
    """Contact information displayed in campaign footers to comply with international spam laws."""
    date_created: str | None
    """The date and time that this list was created in ISO 8601 format."""
    double_optin: bool | None
    """Whether or not to require the subscriber to confirm subscription via email."""
    email_type_option: bool | None
    """Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose..."""
    has_welcome: bool | None
    """Whether or not this list has a welcome automation connected."""
    id: str | None
    """A string that uniquely identifies this list."""
    list_rating: int | None
    """An auto-generated activity score for the list (0-5)."""
    marketing_permissions: bool | None
    """Whether or not the list has marketing permissions (eg. GDPR) enabled."""
    modules: list[Any] | None
    """Any list-specific modules installed for this list."""
    name: str | None
    """The name of the list."""
    notify_on_subscribe: str | None
    """The email address to send subscribe notifications to."""
    notify_on_unsubscribe: str | None
    """The email address to send unsubscribe notifications to."""
    permission_reminder: str | None
    """The permission reminder for the list."""
    stats: dict[str, Any] | None
    """Stats for the list. Many of these are cached for at least five minutes."""
    subscribe_url_long: str | None
    """The full version of this list's subscribe form (host will vary)."""
    subscribe_url_short: str | None
    """Our EepURL shortened version of this list's subscribe form."""
    use_archive_bar: bool | None
    """Whether campaigns for this list use the Archive Bar in archives by default."""
    visibility: str | None
    """Whether this list is public or private."""
    web_id: int | None
    """The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:..."""


class ListsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    beamer_address: list[str]
    """The list's Email Beamer address."""
    campaign_defaults: list[dict[str, Any]]
    """Default values for campaigns created for this list."""
    contact: list[dict[str, Any]]
    """Contact information displayed in campaign footers to comply with international spam laws."""
    date_created: list[str]
    """The date and time that this list was created in ISO 8601 format."""
    double_optin: list[bool]
    """Whether or not to require the subscriber to confirm subscription via email."""
    email_type_option: list[bool]
    """Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose..."""
    has_welcome: list[bool]
    """Whether or not this list has a welcome automation connected."""
    id: list[str]
    """A string that uniquely identifies this list."""
    list_rating: list[int]
    """An auto-generated activity score for the list (0-5)."""
    marketing_permissions: list[bool]
    """Whether or not the list has marketing permissions (eg. GDPR) enabled."""
    modules: list[list[Any]]
    """Any list-specific modules installed for this list."""
    name: list[str]
    """The name of the list."""
    notify_on_subscribe: list[str]
    """The email address to send subscribe notifications to."""
    notify_on_unsubscribe: list[str]
    """The email address to send unsubscribe notifications to."""
    permission_reminder: list[str]
    """The permission reminder for the list."""
    stats: list[dict[str, Any]]
    """Stats for the list. Many of these are cached for at least five minutes."""
    subscribe_url_long: list[str]
    """The full version of this list's subscribe form (host will vary)."""
    subscribe_url_short: list[str]
    """Our EepURL shortened version of this list's subscribe form."""
    use_archive_bar: list[bool]
    """Whether campaigns for this list use the Archive Bar in archives by default."""
    visibility: list[str]
    """Whether this list is public or private."""
    web_id: list[int]
    """The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:..."""


class ListsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    beamer_address: Any
    """The list's Email Beamer address."""
    campaign_defaults: Any
    """Default values for campaigns created for this list."""
    contact: Any
    """Contact information displayed in campaign footers to comply with international spam laws."""
    date_created: Any
    """The date and time that this list was created in ISO 8601 format."""
    double_optin: Any
    """Whether or not to require the subscriber to confirm subscription via email."""
    email_type_option: Any
    """Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose..."""
    has_welcome: Any
    """Whether or not this list has a welcome automation connected."""
    id: Any
    """A string that uniquely identifies this list."""
    list_rating: Any
    """An auto-generated activity score for the list (0-5)."""
    marketing_permissions: Any
    """Whether or not the list has marketing permissions (eg. GDPR) enabled."""
    modules: Any
    """Any list-specific modules installed for this list."""
    name: Any
    """The name of the list."""
    notify_on_subscribe: Any
    """The email address to send subscribe notifications to."""
    notify_on_unsubscribe: Any
    """The email address to send unsubscribe notifications to."""
    permission_reminder: Any
    """The permission reminder for the list."""
    stats: Any
    """Stats for the list. Many of these are cached for at least five minutes."""
    subscribe_url_long: Any
    """The full version of this list's subscribe form (host will vary)."""
    subscribe_url_short: Any
    """Our EepURL shortened version of this list's subscribe form."""
    use_archive_bar: Any
    """Whether campaigns for this list use the Archive Bar in archives by default."""
    visibility: Any
    """Whether this list is public or private."""
    web_id: Any
    """The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:..."""


class ListsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    beamer_address: str
    """The list's Email Beamer address."""
    campaign_defaults: str
    """Default values for campaigns created for this list."""
    contact: str
    """Contact information displayed in campaign footers to comply with international spam laws."""
    date_created: str
    """The date and time that this list was created in ISO 8601 format."""
    double_optin: str
    """Whether or not to require the subscriber to confirm subscription via email."""
    email_type_option: str
    """Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose..."""
    has_welcome: str
    """Whether or not this list has a welcome automation connected."""
    id: str
    """A string that uniquely identifies this list."""
    list_rating: str
    """An auto-generated activity score for the list (0-5)."""
    marketing_permissions: str
    """Whether or not the list has marketing permissions (eg. GDPR) enabled."""
    modules: str
    """Any list-specific modules installed for this list."""
    name: str
    """The name of the list."""
    notify_on_subscribe: str
    """The email address to send subscribe notifications to."""
    notify_on_unsubscribe: str
    """The email address to send unsubscribe notifications to."""
    permission_reminder: str
    """The permission reminder for the list."""
    stats: str
    """Stats for the list. Many of these are cached for at least five minutes."""
    subscribe_url_long: str
    """The full version of this list's subscribe form (host will vary)."""
    subscribe_url_short: str
    """Our EepURL shortened version of this list's subscribe form."""
    use_archive_bar: str
    """Whether campaigns for this list use the Archive Bar in archives by default."""
    visibility: str
    """Whether this list is public or private."""
    web_id: str
    """The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:..."""


class ListsSortFilter(TypedDict, total=False):
    """Available fields for sorting lists search results."""
    beamer_address: AirbyteSortOrder
    """The list's Email Beamer address."""
    campaign_defaults: AirbyteSortOrder
    """Default values for campaigns created for this list."""
    contact: AirbyteSortOrder
    """Contact information displayed in campaign footers to comply with international spam laws."""
    date_created: AirbyteSortOrder
    """The date and time that this list was created in ISO 8601 format."""
    double_optin: AirbyteSortOrder
    """Whether or not to require the subscriber to confirm subscription via email."""
    email_type_option: AirbyteSortOrder
    """Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose..."""
    has_welcome: AirbyteSortOrder
    """Whether or not this list has a welcome automation connected."""
    id: AirbyteSortOrder
    """A string that uniquely identifies this list."""
    list_rating: AirbyteSortOrder
    """An auto-generated activity score for the list (0-5)."""
    marketing_permissions: AirbyteSortOrder
    """Whether or not the list has marketing permissions (eg. GDPR) enabled."""
    modules: AirbyteSortOrder
    """Any list-specific modules installed for this list."""
    name: AirbyteSortOrder
    """The name of the list."""
    notify_on_subscribe: AirbyteSortOrder
    """The email address to send subscribe notifications to."""
    notify_on_unsubscribe: AirbyteSortOrder
    """The email address to send unsubscribe notifications to."""
    permission_reminder: AirbyteSortOrder
    """The permission reminder for the list."""
    stats: AirbyteSortOrder
    """Stats for the list. Many of these are cached for at least five minutes."""
    subscribe_url_long: AirbyteSortOrder
    """The full version of this list's subscribe form (host will vary)."""
    subscribe_url_short: AirbyteSortOrder
    """Our EepURL shortened version of this list's subscribe form."""
    use_archive_bar: AirbyteSortOrder
    """Whether campaigns for this list use the Archive Bar in archives by default."""
    visibility: AirbyteSortOrder
    """Whether this list is public or private."""
    web_id: AirbyteSortOrder
    """The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:..."""


# Entity-specific condition types for lists
class ListsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListsSearchFilter


class ListsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListsSearchFilter


class ListsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListsSearchFilter


class ListsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListsSearchFilter


class ListsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListsSearchFilter


class ListsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListsSearchFilter


class ListsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ListsStringFilter


class ListsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ListsStringFilter


class ListsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListsStringFilter


class ListsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListsStringFilter


class ListsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: ListsAnyValueFilter


class ListsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: ListsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListsInCondition = TypedDict("ListsInCondition", {"in": ListsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListsNotCondition = TypedDict("ListsNotCondition", {"not": "ListsCondition"}, total=False)
"""Negates the nested condition."""

ListsAndCondition = TypedDict("ListsAndCondition", {"and": "list[ListsCondition]"}, total=False)
"""True if all nested conditions are true."""

ListsOrCondition = TypedDict("ListsOrCondition", {"or": "list[ListsCondition]"}, total=False)
"""True if any nested condition is true."""

ListsAnyCondition = TypedDict("ListsAnyCondition", {"any": ListsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all lists condition types
ListsCondition = (
    ListsEqCondition
    | ListsNeqCondition
    | ListsGtCondition
    | ListsGteCondition
    | ListsLtCondition
    | ListsLteCondition
    | ListsInCondition
    | ListsStartswithCondition
    | ListsEndswithCondition
    | ListsFuzzyCondition
    | ListsKeywordCondition
    | ListsContainsCondition
    | ListsArrayContainsCondition
    | ListsNotCondition
    | ListsAndCondition
    | ListsOrCondition
    | ListsAnyCondition
)


class ListsSearchQuery(TypedDict, total=False):
    """Search query for lists entity."""
    filter: ListsCondition
    sort: list[ListsSortFilter]


# ===== REPORTS SEARCH TYPES =====

class ReportsSearchFilter(TypedDict, total=False):
    """Available fields for filtering reports search queries."""
    ab_split: dict[str, Any] | None
    """General stats about different groups of an A/B Split campaign. Does not return information about ..."""
    abuse_reports: int | None
    """The number of abuse reports generated for this campaign."""
    bounces: dict[str, Any] | None
    """An object describing the bounce summary for the campaign."""
    campaign_title: str | None
    """The title of the campaign."""
    clicks: dict[str, Any] | None
    """An object describing the click activity for the campaign."""
    delivery_status: dict[str, Any] | None
    """Updates on campaigns in the process of sending."""
    ecommerce: dict[str, Any] | None
    """E-Commerce stats for a campaign."""
    emails_sent: int | None
    """The total number of emails sent for this campaign."""
    facebook_likes: dict[str, Any] | None
    """An object describing campaign engagement on Facebook."""
    forwards: dict[str, Any] | None
    """An object describing the forwards and forward activity for the campaign."""
    id: str | None
    """A string that uniquely identifies this campaign."""
    industry_stats: dict[str, Any] | None
    """The average campaign statistics for your industry."""
    list_id: str | None
    """The unique list id."""
    list_is_active: bool | None
    """The status of the list used, namely if it's deleted or disabled."""
    list_name: str | None
    """The name of the list."""
    list_stats: dict[str, Any] | None
    """The average campaign statistics for your list. This won't be present if we haven't calculated i..."""
    opens: dict[str, Any] | None
    """An object describing the open activity for the campaign."""
    preview_text: str | None
    """The preview text for the campaign."""
    rss_last_send: str | None
    """For RSS campaigns, the date and time of the last send in ISO 8601 format."""
    send_time: str | None
    """The date and time a campaign was sent in ISO 8601 format."""
    share_report: dict[str, Any] | None
    """The url and password for the VIP report."""
    subject_line: str | None
    """The subject line for the campaign."""
    timeseries: list[Any] | None
    """An hourly breakdown of the performance of the campaign over the first 24 hours."""
    timewarp: list[Any] | None
    """An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp."""
    type_: str | None
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: int | None
    """The total number of unsubscribed members for this campaign."""


class ReportsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ab_split: list[dict[str, Any]]
    """General stats about different groups of an A/B Split campaign. Does not return information about ..."""
    abuse_reports: list[int]
    """The number of abuse reports generated for this campaign."""
    bounces: list[dict[str, Any]]
    """An object describing the bounce summary for the campaign."""
    campaign_title: list[str]
    """The title of the campaign."""
    clicks: list[dict[str, Any]]
    """An object describing the click activity for the campaign."""
    delivery_status: list[dict[str, Any]]
    """Updates on campaigns in the process of sending."""
    ecommerce: list[dict[str, Any]]
    """E-Commerce stats for a campaign."""
    emails_sent: list[int]
    """The total number of emails sent for this campaign."""
    facebook_likes: list[dict[str, Any]]
    """An object describing campaign engagement on Facebook."""
    forwards: list[dict[str, Any]]
    """An object describing the forwards and forward activity for the campaign."""
    id: list[str]
    """A string that uniquely identifies this campaign."""
    industry_stats: list[dict[str, Any]]
    """The average campaign statistics for your industry."""
    list_id: list[str]
    """The unique list id."""
    list_is_active: list[bool]
    """The status of the list used, namely if it's deleted or disabled."""
    list_name: list[str]
    """The name of the list."""
    list_stats: list[dict[str, Any]]
    """The average campaign statistics for your list. This won't be present if we haven't calculated i..."""
    opens: list[dict[str, Any]]
    """An object describing the open activity for the campaign."""
    preview_text: list[str]
    """The preview text for the campaign."""
    rss_last_send: list[str]
    """For RSS campaigns, the date and time of the last send in ISO 8601 format."""
    send_time: list[str]
    """The date and time a campaign was sent in ISO 8601 format."""
    share_report: list[dict[str, Any]]
    """The url and password for the VIP report."""
    subject_line: list[str]
    """The subject line for the campaign."""
    timeseries: list[list[Any]]
    """An hourly breakdown of the performance of the campaign over the first 24 hours."""
    timewarp: list[list[Any]]
    """An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp."""
    type_: list[str]
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: list[int]
    """The total number of unsubscribed members for this campaign."""


class ReportsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ab_split: Any
    """General stats about different groups of an A/B Split campaign. Does not return information about ..."""
    abuse_reports: Any
    """The number of abuse reports generated for this campaign."""
    bounces: Any
    """An object describing the bounce summary for the campaign."""
    campaign_title: Any
    """The title of the campaign."""
    clicks: Any
    """An object describing the click activity for the campaign."""
    delivery_status: Any
    """Updates on campaigns in the process of sending."""
    ecommerce: Any
    """E-Commerce stats for a campaign."""
    emails_sent: Any
    """The total number of emails sent for this campaign."""
    facebook_likes: Any
    """An object describing campaign engagement on Facebook."""
    forwards: Any
    """An object describing the forwards and forward activity for the campaign."""
    id: Any
    """A string that uniquely identifies this campaign."""
    industry_stats: Any
    """The average campaign statistics for your industry."""
    list_id: Any
    """The unique list id."""
    list_is_active: Any
    """The status of the list used, namely if it's deleted or disabled."""
    list_name: Any
    """The name of the list."""
    list_stats: Any
    """The average campaign statistics for your list. This won't be present if we haven't calculated i..."""
    opens: Any
    """An object describing the open activity for the campaign."""
    preview_text: Any
    """The preview text for the campaign."""
    rss_last_send: Any
    """For RSS campaigns, the date and time of the last send in ISO 8601 format."""
    send_time: Any
    """The date and time a campaign was sent in ISO 8601 format."""
    share_report: Any
    """The url and password for the VIP report."""
    subject_line: Any
    """The subject line for the campaign."""
    timeseries: Any
    """An hourly breakdown of the performance of the campaign over the first 24 hours."""
    timewarp: Any
    """An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp."""
    type_: Any
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: Any
    """The total number of unsubscribed members for this campaign."""


class ReportsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    ab_split: str
    """General stats about different groups of an A/B Split campaign. Does not return information about ..."""
    abuse_reports: str
    """The number of abuse reports generated for this campaign."""
    bounces: str
    """An object describing the bounce summary for the campaign."""
    campaign_title: str
    """The title of the campaign."""
    clicks: str
    """An object describing the click activity for the campaign."""
    delivery_status: str
    """Updates on campaigns in the process of sending."""
    ecommerce: str
    """E-Commerce stats for a campaign."""
    emails_sent: str
    """The total number of emails sent for this campaign."""
    facebook_likes: str
    """An object describing campaign engagement on Facebook."""
    forwards: str
    """An object describing the forwards and forward activity for the campaign."""
    id: str
    """A string that uniquely identifies this campaign."""
    industry_stats: str
    """The average campaign statistics for your industry."""
    list_id: str
    """The unique list id."""
    list_is_active: str
    """The status of the list used, namely if it's deleted or disabled."""
    list_name: str
    """The name of the list."""
    list_stats: str
    """The average campaign statistics for your list. This won't be present if we haven't calculated i..."""
    opens: str
    """An object describing the open activity for the campaign."""
    preview_text: str
    """The preview text for the campaign."""
    rss_last_send: str
    """For RSS campaigns, the date and time of the last send in ISO 8601 format."""
    send_time: str
    """The date and time a campaign was sent in ISO 8601 format."""
    share_report: str
    """The url and password for the VIP report."""
    subject_line: str
    """The subject line for the campaign."""
    timeseries: str
    """An hourly breakdown of the performance of the campaign over the first 24 hours."""
    timewarp: str
    """An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp."""
    type_: str
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: str
    """The total number of unsubscribed members for this campaign."""


class ReportsSortFilter(TypedDict, total=False):
    """Available fields for sorting reports search results."""
    ab_split: AirbyteSortOrder
    """General stats about different groups of an A/B Split campaign. Does not return information about ..."""
    abuse_reports: AirbyteSortOrder
    """The number of abuse reports generated for this campaign."""
    bounces: AirbyteSortOrder
    """An object describing the bounce summary for the campaign."""
    campaign_title: AirbyteSortOrder
    """The title of the campaign."""
    clicks: AirbyteSortOrder
    """An object describing the click activity for the campaign."""
    delivery_status: AirbyteSortOrder
    """Updates on campaigns in the process of sending."""
    ecommerce: AirbyteSortOrder
    """E-Commerce stats for a campaign."""
    emails_sent: AirbyteSortOrder
    """The total number of emails sent for this campaign."""
    facebook_likes: AirbyteSortOrder
    """An object describing campaign engagement on Facebook."""
    forwards: AirbyteSortOrder
    """An object describing the forwards and forward activity for the campaign."""
    id: AirbyteSortOrder
    """A string that uniquely identifies this campaign."""
    industry_stats: AirbyteSortOrder
    """The average campaign statistics for your industry."""
    list_id: AirbyteSortOrder
    """The unique list id."""
    list_is_active: AirbyteSortOrder
    """The status of the list used, namely if it's deleted or disabled."""
    list_name: AirbyteSortOrder
    """The name of the list."""
    list_stats: AirbyteSortOrder
    """The average campaign statistics for your list. This won't be present if we haven't calculated i..."""
    opens: AirbyteSortOrder
    """An object describing the open activity for the campaign."""
    preview_text: AirbyteSortOrder
    """The preview text for the campaign."""
    rss_last_send: AirbyteSortOrder
    """For RSS campaigns, the date and time of the last send in ISO 8601 format."""
    send_time: AirbyteSortOrder
    """The date and time a campaign was sent in ISO 8601 format."""
    share_report: AirbyteSortOrder
    """The url and password for the VIP report."""
    subject_line: AirbyteSortOrder
    """The subject line for the campaign."""
    timeseries: AirbyteSortOrder
    """An hourly breakdown of the performance of the campaign over the first 24 hours."""
    timewarp: AirbyteSortOrder
    """An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp."""
    type_: AirbyteSortOrder
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: AirbyteSortOrder
    """The total number of unsubscribed members for this campaign."""


# Entity-specific condition types for reports
class ReportsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ReportsSearchFilter


class ReportsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ReportsSearchFilter


class ReportsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ReportsSearchFilter


class ReportsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ReportsSearchFilter


class ReportsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ReportsSearchFilter


class ReportsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ReportsSearchFilter


class ReportsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ReportsStringFilter


class ReportsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ReportsStringFilter


class ReportsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ReportsStringFilter


class ReportsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ReportsStringFilter


class ReportsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: ReportsAnyValueFilter


class ReportsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: ReportsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ReportsInCondition = TypedDict("ReportsInCondition", {"in": ReportsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ReportsNotCondition = TypedDict("ReportsNotCondition", {"not": "ReportsCondition"}, total=False)
"""Negates the nested condition."""

ReportsAndCondition = TypedDict("ReportsAndCondition", {"and": "list[ReportsCondition]"}, total=False)
"""True if all nested conditions are true."""

ReportsOrCondition = TypedDict("ReportsOrCondition", {"or": "list[ReportsCondition]"}, total=False)
"""True if any nested condition is true."""

ReportsAnyCondition = TypedDict("ReportsAnyCondition", {"any": ReportsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all reports condition types
ReportsCondition = (
    ReportsEqCondition
    | ReportsNeqCondition
    | ReportsGtCondition
    | ReportsGteCondition
    | ReportsLtCondition
    | ReportsLteCondition
    | ReportsInCondition
    | ReportsStartswithCondition
    | ReportsEndswithCondition
    | ReportsFuzzyCondition
    | ReportsKeywordCondition
    | ReportsContainsCondition
    | ReportsArrayContainsCondition
    | ReportsNotCondition
    | ReportsAndCondition
    | ReportsOrCondition
    | ReportsAnyCondition
)


class ReportsSearchQuery(TypedDict, total=False):
    """Search query for reports entity."""
    filter: ReportsCondition
    sort: list[ReportsSortFilter]


# ===== LIST_MEMBERS SEARCH TYPES =====

class ListMembersSearchFilter(TypedDict, total=False):
    """Available fields for filtering list_members search queries."""
    id: str
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: str | None
    """Email address for a subscriber"""
    unique_email_id: str | None
    """An identifier for the address across all of Mailchimp"""
    contact_id: str | None
    """As Mailchimp evolves beyond email, you may eventually have contacts without email addresses"""
    full_name: str | None
    """The contact's full name"""
    web_id: int | None
    """The ID used in the Mailchimp web application"""
    email_type: str | None
    """Type of email this member asked to get"""
    status: str | None
    """Subscriber's current status"""
    unsubscribe_reason: str | None
    """A subscriber's reason for unsubscribing"""
    consents_to_one_to_one_messaging: bool | None
    """Indicates whether a contact consents to 1:1 messaging"""
    merge_fields: dict[str, Any] | None
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: dict[str, Any] | None
    """The key of this object's properties is the ID of the interest in question"""
    stats: dict[str, Any] | None
    """Open and click rates for this subscriber"""
    ip_signup: str | None
    """IP address the subscriber signed up from"""
    timestamp_signup: str | None
    """The date and time the subscriber signed up for the list"""
    ip_opt: str | None
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: str | None
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: int | None
    """Star rating for this member, between 1 and 5"""
    last_changed: str | None
    """The date and time the member's info was last changed"""
    language: str | None
    """If set/detected, the subscriber's language"""
    vip: bool | None
    """VIP status for subscriber"""
    email_client: str | None
    """The list member's email client"""
    location: dict[str, Any] | None
    """Subscriber location information"""
    source: str | None
    """The source from which the subscriber was added to this list"""
    tags_count: int | None
    """The number of tags applied to this member"""
    tags: list[Any] | None
    """Returns up to 50 tags applied to this member"""
    list_id: str | None
    """The list id"""


class ListMembersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: list[str]
    """Email address for a subscriber"""
    unique_email_id: list[str]
    """An identifier for the address across all of Mailchimp"""
    contact_id: list[str]
    """As Mailchimp evolves beyond email, you may eventually have contacts without email addresses"""
    full_name: list[str]
    """The contact's full name"""
    web_id: list[int]
    """The ID used in the Mailchimp web application"""
    email_type: list[str]
    """Type of email this member asked to get"""
    status: list[str]
    """Subscriber's current status"""
    unsubscribe_reason: list[str]
    """A subscriber's reason for unsubscribing"""
    consents_to_one_to_one_messaging: list[bool]
    """Indicates whether a contact consents to 1:1 messaging"""
    merge_fields: list[dict[str, Any]]
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: list[dict[str, Any]]
    """The key of this object's properties is the ID of the interest in question"""
    stats: list[dict[str, Any]]
    """Open and click rates for this subscriber"""
    ip_signup: list[str]
    """IP address the subscriber signed up from"""
    timestamp_signup: list[str]
    """The date and time the subscriber signed up for the list"""
    ip_opt: list[str]
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: list[str]
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: list[int]
    """Star rating for this member, between 1 and 5"""
    last_changed: list[str]
    """The date and time the member's info was last changed"""
    language: list[str]
    """If set/detected, the subscriber's language"""
    vip: list[bool]
    """VIP status for subscriber"""
    email_client: list[str]
    """The list member's email client"""
    location: list[dict[str, Any]]
    """Subscriber location information"""
    source: list[str]
    """The source from which the subscriber was added to this list"""
    tags_count: list[int]
    """The number of tags applied to this member"""
    tags: list[list[Any]]
    """Returns up to 50 tags applied to this member"""
    list_id: list[str]
    """The list id"""


class ListMembersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: Any
    """Email address for a subscriber"""
    unique_email_id: Any
    """An identifier for the address across all of Mailchimp"""
    contact_id: Any
    """As Mailchimp evolves beyond email, you may eventually have contacts without email addresses"""
    full_name: Any
    """The contact's full name"""
    web_id: Any
    """The ID used in the Mailchimp web application"""
    email_type: Any
    """Type of email this member asked to get"""
    status: Any
    """Subscriber's current status"""
    unsubscribe_reason: Any
    """A subscriber's reason for unsubscribing"""
    consents_to_one_to_one_messaging: Any
    """Indicates whether a contact consents to 1:1 messaging"""
    merge_fields: Any
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: Any
    """The key of this object's properties is the ID of the interest in question"""
    stats: Any
    """Open and click rates for this subscriber"""
    ip_signup: Any
    """IP address the subscriber signed up from"""
    timestamp_signup: Any
    """The date and time the subscriber signed up for the list"""
    ip_opt: Any
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: Any
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: Any
    """Star rating for this member, between 1 and 5"""
    last_changed: Any
    """The date and time the member's info was last changed"""
    language: Any
    """If set/detected, the subscriber's language"""
    vip: Any
    """VIP status for subscriber"""
    email_client: Any
    """The list member's email client"""
    location: Any
    """Subscriber location information"""
    source: Any
    """The source from which the subscriber was added to this list"""
    tags_count: Any
    """The number of tags applied to this member"""
    tags: Any
    """Returns up to 50 tags applied to this member"""
    list_id: Any
    """The list id"""


class ListMembersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: str
    """Email address for a subscriber"""
    unique_email_id: str
    """An identifier for the address across all of Mailchimp"""
    contact_id: str
    """As Mailchimp evolves beyond email, you may eventually have contacts without email addresses"""
    full_name: str
    """The contact's full name"""
    web_id: str
    """The ID used in the Mailchimp web application"""
    email_type: str
    """Type of email this member asked to get"""
    status: str
    """Subscriber's current status"""
    unsubscribe_reason: str
    """A subscriber's reason for unsubscribing"""
    consents_to_one_to_one_messaging: str
    """Indicates whether a contact consents to 1:1 messaging"""
    merge_fields: str
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: str
    """The key of this object's properties is the ID of the interest in question"""
    stats: str
    """Open and click rates for this subscriber"""
    ip_signup: str
    """IP address the subscriber signed up from"""
    timestamp_signup: str
    """The date and time the subscriber signed up for the list"""
    ip_opt: str
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: str
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: str
    """Star rating for this member, between 1 and 5"""
    last_changed: str
    """The date and time the member's info was last changed"""
    language: str
    """If set/detected, the subscriber's language"""
    vip: str
    """VIP status for subscriber"""
    email_client: str
    """The list member's email client"""
    location: str
    """Subscriber location information"""
    source: str
    """The source from which the subscriber was added to this list"""
    tags_count: str
    """The number of tags applied to this member"""
    tags: str
    """Returns up to 50 tags applied to this member"""
    list_id: str
    """The list id"""


class ListMembersSortFilter(TypedDict, total=False):
    """Available fields for sorting list_members search results."""
    id: AirbyteSortOrder
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: AirbyteSortOrder
    """Email address for a subscriber"""
    unique_email_id: AirbyteSortOrder
    """An identifier for the address across all of Mailchimp"""
    contact_id: AirbyteSortOrder
    """As Mailchimp evolves beyond email, you may eventually have contacts without email addresses"""
    full_name: AirbyteSortOrder
    """The contact's full name"""
    web_id: AirbyteSortOrder
    """The ID used in the Mailchimp web application"""
    email_type: AirbyteSortOrder
    """Type of email this member asked to get"""
    status: AirbyteSortOrder
    """Subscriber's current status"""
    unsubscribe_reason: AirbyteSortOrder
    """A subscriber's reason for unsubscribing"""
    consents_to_one_to_one_messaging: AirbyteSortOrder
    """Indicates whether a contact consents to 1:1 messaging"""
    merge_fields: AirbyteSortOrder
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: AirbyteSortOrder
    """The key of this object's properties is the ID of the interest in question"""
    stats: AirbyteSortOrder
    """Open and click rates for this subscriber"""
    ip_signup: AirbyteSortOrder
    """IP address the subscriber signed up from"""
    timestamp_signup: AirbyteSortOrder
    """The date and time the subscriber signed up for the list"""
    ip_opt: AirbyteSortOrder
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: AirbyteSortOrder
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: AirbyteSortOrder
    """Star rating for this member, between 1 and 5"""
    last_changed: AirbyteSortOrder
    """The date and time the member's info was last changed"""
    language: AirbyteSortOrder
    """If set/detected, the subscriber's language"""
    vip: AirbyteSortOrder
    """VIP status for subscriber"""
    email_client: AirbyteSortOrder
    """The list member's email client"""
    location: AirbyteSortOrder
    """Subscriber location information"""
    source: AirbyteSortOrder
    """The source from which the subscriber was added to this list"""
    tags_count: AirbyteSortOrder
    """The number of tags applied to this member"""
    tags: AirbyteSortOrder
    """Returns up to 50 tags applied to this member"""
    list_id: AirbyteSortOrder
    """The list id"""


# Entity-specific condition types for list_members
class ListMembersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListMembersSearchFilter


class ListMembersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListMembersSearchFilter


class ListMembersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListMembersSearchFilter


class ListMembersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListMembersSearchFilter


class ListMembersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListMembersSearchFilter


class ListMembersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListMembersSearchFilter


class ListMembersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ListMembersStringFilter


class ListMembersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ListMembersStringFilter


class ListMembersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListMembersStringFilter


class ListMembersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListMembersStringFilter


class ListMembersContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: ListMembersAnyValueFilter


class ListMembersArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: ListMembersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListMembersInCondition = TypedDict("ListMembersInCondition", {"in": ListMembersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListMembersNotCondition = TypedDict("ListMembersNotCondition", {"not": "ListMembersCondition"}, total=False)
"""Negates the nested condition."""

ListMembersAndCondition = TypedDict("ListMembersAndCondition", {"and": "list[ListMembersCondition]"}, total=False)
"""True if all nested conditions are true."""

ListMembersOrCondition = TypedDict("ListMembersOrCondition", {"or": "list[ListMembersCondition]"}, total=False)
"""True if any nested condition is true."""

ListMembersAnyCondition = TypedDict("ListMembersAnyCondition", {"any": ListMembersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all list_members condition types
ListMembersCondition = (
    ListMembersEqCondition
    | ListMembersNeqCondition
    | ListMembersGtCondition
    | ListMembersGteCondition
    | ListMembersLtCondition
    | ListMembersLteCondition
    | ListMembersInCondition
    | ListMembersStartswithCondition
    | ListMembersEndswithCondition
    | ListMembersFuzzyCondition
    | ListMembersKeywordCondition
    | ListMembersContainsCondition
    | ListMembersArrayContainsCondition
    | ListMembersNotCondition
    | ListMembersAndCondition
    | ListMembersOrCondition
    | ListMembersAnyCondition
)


class ListMembersSearchQuery(TypedDict, total=False):
    """Search query for list_members entity."""
    filter: ListMembersCondition
    sort: list[ListMembersSortFilter]


# ===== AUTOMATIONS SEARCH TYPES =====

class AutomationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering automations search queries."""
    id: str
    """A string that uniquely identifies an Automation workflow"""
    create_time: str | None
    """The date and time the Automation was created"""
    start_time: str | None
    """The date and time the Automation was started"""
    status: str | None
    """The current status of the Automation"""
    emails_sent: int | None
    """The total number of emails sent for the Automation"""
    recipients: dict[str, Any] | None
    """List settings for the Automation"""
    settings: dict[str, Any] | None
    """The settings for the Automation workflow"""
    tracking: dict[str, Any] | None
    """The tracking options for the Automation"""
    report_summary: dict[str, Any] | None
    """A summary of opens and clicks for sent campaigns"""


class AutomationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """A string that uniquely identifies an Automation workflow"""
    create_time: list[str]
    """The date and time the Automation was created"""
    start_time: list[str]
    """The date and time the Automation was started"""
    status: list[str]
    """The current status of the Automation"""
    emails_sent: list[int]
    """The total number of emails sent for the Automation"""
    recipients: list[dict[str, Any]]
    """List settings for the Automation"""
    settings: list[dict[str, Any]]
    """The settings for the Automation workflow"""
    tracking: list[dict[str, Any]]
    """The tracking options for the Automation"""
    report_summary: list[dict[str, Any]]
    """A summary of opens and clicks for sent campaigns"""


class AutomationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """A string that uniquely identifies an Automation workflow"""
    create_time: Any
    """The date and time the Automation was created"""
    start_time: Any
    """The date and time the Automation was started"""
    status: Any
    """The current status of the Automation"""
    emails_sent: Any
    """The total number of emails sent for the Automation"""
    recipients: Any
    """List settings for the Automation"""
    settings: Any
    """The settings for the Automation workflow"""
    tracking: Any
    """The tracking options for the Automation"""
    report_summary: Any
    """A summary of opens and clicks for sent campaigns"""


class AutomationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """A string that uniquely identifies an Automation workflow"""
    create_time: str
    """The date and time the Automation was created"""
    start_time: str
    """The date and time the Automation was started"""
    status: str
    """The current status of the Automation"""
    emails_sent: str
    """The total number of emails sent for the Automation"""
    recipients: str
    """List settings for the Automation"""
    settings: str
    """The settings for the Automation workflow"""
    tracking: str
    """The tracking options for the Automation"""
    report_summary: str
    """A summary of opens and clicks for sent campaigns"""


class AutomationsSortFilter(TypedDict, total=False):
    """Available fields for sorting automations search results."""
    id: AirbyteSortOrder
    """A string that uniquely identifies an Automation workflow"""
    create_time: AirbyteSortOrder
    """The date and time the Automation was created"""
    start_time: AirbyteSortOrder
    """The date and time the Automation was started"""
    status: AirbyteSortOrder
    """The current status of the Automation"""
    emails_sent: AirbyteSortOrder
    """The total number of emails sent for the Automation"""
    recipients: AirbyteSortOrder
    """List settings for the Automation"""
    settings: AirbyteSortOrder
    """The settings for the Automation workflow"""
    tracking: AirbyteSortOrder
    """The tracking options for the Automation"""
    report_summary: AirbyteSortOrder
    """A summary of opens and clicks for sent campaigns"""


# Entity-specific condition types for automations
class AutomationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AutomationsSearchFilter


class AutomationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AutomationsSearchFilter


class AutomationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AutomationsSearchFilter


class AutomationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AutomationsSearchFilter


class AutomationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AutomationsSearchFilter


class AutomationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AutomationsSearchFilter


class AutomationsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AutomationsStringFilter


class AutomationsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AutomationsStringFilter


class AutomationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AutomationsStringFilter


class AutomationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AutomationsStringFilter


class AutomationsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: AutomationsAnyValueFilter


class AutomationsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: AutomationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AutomationsInCondition = TypedDict("AutomationsInCondition", {"in": AutomationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AutomationsNotCondition = TypedDict("AutomationsNotCondition", {"not": "AutomationsCondition"}, total=False)
"""Negates the nested condition."""

AutomationsAndCondition = TypedDict("AutomationsAndCondition", {"and": "list[AutomationsCondition]"}, total=False)
"""True if all nested conditions are true."""

AutomationsOrCondition = TypedDict("AutomationsOrCondition", {"or": "list[AutomationsCondition]"}, total=False)
"""True if any nested condition is true."""

AutomationsAnyCondition = TypedDict("AutomationsAnyCondition", {"any": AutomationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all automations condition types
AutomationsCondition = (
    AutomationsEqCondition
    | AutomationsNeqCondition
    | AutomationsGtCondition
    | AutomationsGteCondition
    | AutomationsLtCondition
    | AutomationsLteCondition
    | AutomationsInCondition
    | AutomationsStartswithCondition
    | AutomationsEndswithCondition
    | AutomationsFuzzyCondition
    | AutomationsKeywordCondition
    | AutomationsContainsCondition
    | AutomationsArrayContainsCondition
    | AutomationsNotCondition
    | AutomationsAndCondition
    | AutomationsOrCondition
    | AutomationsAnyCondition
)


class AutomationsSearchQuery(TypedDict, total=False):
    """Search query for automations entity."""
    filter: AutomationsCondition
    sort: list[AutomationsSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    id: int
    """The unique id for the tag"""
    name: str | None
    """The name of the tag"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """The unique id for the tag"""
    name: list[str]
    """The name of the tag"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique id for the tag"""
    name: Any
    """The name of the tag"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """The unique id for the tag"""
    name: str
    """The name of the tag"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    id: AirbyteSortOrder
    """The unique id for the tag"""
    name: AirbyteSortOrder
    """The name of the tag"""


# Entity-specific condition types for tags
class TagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TagsSearchFilter


class TagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TagsSearchFilter


class TagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TagsSearchFilter


class TagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TagsSearchFilter


class TagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TagsSearchFilter


class TagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TagsSearchFilter


class TagsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TagsStringFilter


class TagsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TagsStringFilter


class TagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TagsStringFilter


class TagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TagsStringFilter


class TagsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: TagsAnyValueFilter


class TagsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: TagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TagsInCondition = TypedDict("TagsInCondition", {"in": TagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TagsNotCondition = TypedDict("TagsNotCondition", {"not": "TagsCondition"}, total=False)
"""Negates the nested condition."""

TagsAndCondition = TypedDict("TagsAndCondition", {"and": "list[TagsCondition]"}, total=False)
"""True if all nested conditions are true."""

TagsOrCondition = TypedDict("TagsOrCondition", {"or": "list[TagsCondition]"}, total=False)
"""True if any nested condition is true."""

TagsAnyCondition = TypedDict("TagsAnyCondition", {"any": TagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tags condition types
TagsCondition = (
    TagsEqCondition
    | TagsNeqCondition
    | TagsGtCondition
    | TagsGteCondition
    | TagsLtCondition
    | TagsLteCondition
    | TagsInCondition
    | TagsStartswithCondition
    | TagsEndswithCondition
    | TagsFuzzyCondition
    | TagsKeywordCondition
    | TagsContainsCondition
    | TagsArrayContainsCondition
    | TagsNotCondition
    | TagsAndCondition
    | TagsOrCondition
    | TagsAnyCondition
)


class TagsSearchQuery(TypedDict, total=False):
    """Search query for tags entity."""
    filter: TagsCondition
    sort: list[TagsSortFilter]


# ===== INTEREST_CATEGORIES SEARCH TYPES =====

class InterestCategoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering interest_categories search queries."""
    list_id: str | None
    """The unique list id for the category"""
    id: str
    """The id for the interest category"""
    title: str | None
    """The text description of this category"""
    display_order: int | None
    """The order that the categories are displayed in the list"""
    type_: str | None
    """Determines how this category's interests appear on signup forms"""


class InterestCategoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    list_id: list[str]
    """The unique list id for the category"""
    id: list[str]
    """The id for the interest category"""
    title: list[str]
    """The text description of this category"""
    display_order: list[int]
    """The order that the categories are displayed in the list"""
    type_: list[str]
    """Determines how this category's interests appear on signup forms"""


class InterestCategoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    list_id: Any
    """The unique list id for the category"""
    id: Any
    """The id for the interest category"""
    title: Any
    """The text description of this category"""
    display_order: Any
    """The order that the categories are displayed in the list"""
    type_: Any
    """Determines how this category's interests appear on signup forms"""


class InterestCategoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    list_id: str
    """The unique list id for the category"""
    id: str
    """The id for the interest category"""
    title: str
    """The text description of this category"""
    display_order: str
    """The order that the categories are displayed in the list"""
    type_: str
    """Determines how this category's interests appear on signup forms"""


class InterestCategoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting interest_categories search results."""
    list_id: AirbyteSortOrder
    """The unique list id for the category"""
    id: AirbyteSortOrder
    """The id for the interest category"""
    title: AirbyteSortOrder
    """The text description of this category"""
    display_order: AirbyteSortOrder
    """The order that the categories are displayed in the list"""
    type_: AirbyteSortOrder
    """Determines how this category's interests appear on signup forms"""


# Entity-specific condition types for interest_categories
class InterestCategoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InterestCategoriesSearchFilter


class InterestCategoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InterestCategoriesSearchFilter


class InterestCategoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InterestCategoriesSearchFilter


class InterestCategoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InterestCategoriesSearchFilter


class InterestCategoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InterestCategoriesSearchFilter


class InterestCategoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InterestCategoriesSearchFilter


class InterestCategoriesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: InterestCategoriesStringFilter


class InterestCategoriesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: InterestCategoriesStringFilter


class InterestCategoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InterestCategoriesStringFilter


class InterestCategoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InterestCategoriesStringFilter


class InterestCategoriesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: InterestCategoriesAnyValueFilter


class InterestCategoriesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: InterestCategoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InterestCategoriesInCondition = TypedDict("InterestCategoriesInCondition", {"in": InterestCategoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InterestCategoriesNotCondition = TypedDict("InterestCategoriesNotCondition", {"not": "InterestCategoriesCondition"}, total=False)
"""Negates the nested condition."""

InterestCategoriesAndCondition = TypedDict("InterestCategoriesAndCondition", {"and": "list[InterestCategoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

InterestCategoriesOrCondition = TypedDict("InterestCategoriesOrCondition", {"or": "list[InterestCategoriesCondition]"}, total=False)
"""True if any nested condition is true."""

InterestCategoriesAnyCondition = TypedDict("InterestCategoriesAnyCondition", {"any": InterestCategoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all interest_categories condition types
InterestCategoriesCondition = (
    InterestCategoriesEqCondition
    | InterestCategoriesNeqCondition
    | InterestCategoriesGtCondition
    | InterestCategoriesGteCondition
    | InterestCategoriesLtCondition
    | InterestCategoriesLteCondition
    | InterestCategoriesInCondition
    | InterestCategoriesStartswithCondition
    | InterestCategoriesEndswithCondition
    | InterestCategoriesFuzzyCondition
    | InterestCategoriesKeywordCondition
    | InterestCategoriesContainsCondition
    | InterestCategoriesArrayContainsCondition
    | InterestCategoriesNotCondition
    | InterestCategoriesAndCondition
    | InterestCategoriesOrCondition
    | InterestCategoriesAnyCondition
)


class InterestCategoriesSearchQuery(TypedDict, total=False):
    """Search query for interest_categories entity."""
    filter: InterestCategoriesCondition
    sort: list[InterestCategoriesSortFilter]


# ===== INTERESTS SEARCH TYPES =====

class InterestsSearchFilter(TypedDict, total=False):
    """Available fields for filtering interests search queries."""
    category_id: str | None
    """The id for the interest category"""
    list_id: str | None
    """The ID for the list that this interest belongs to"""
    id: str
    """The ID for the interest"""
    name: str | None
    """The name of the interest"""
    subscriber_count: str | None
    """The number of subscribers associated with this interest"""
    display_order: int | None
    """The display order for interests"""


class InterestsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    category_id: list[str]
    """The id for the interest category"""
    list_id: list[str]
    """The ID for the list that this interest belongs to"""
    id: list[str]
    """The ID for the interest"""
    name: list[str]
    """The name of the interest"""
    subscriber_count: list[str]
    """The number of subscribers associated with this interest"""
    display_order: list[int]
    """The display order for interests"""


class InterestsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    category_id: Any
    """The id for the interest category"""
    list_id: Any
    """The ID for the list that this interest belongs to"""
    id: Any
    """The ID for the interest"""
    name: Any
    """The name of the interest"""
    subscriber_count: Any
    """The number of subscribers associated with this interest"""
    display_order: Any
    """The display order for interests"""


class InterestsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    category_id: str
    """The id for the interest category"""
    list_id: str
    """The ID for the list that this interest belongs to"""
    id: str
    """The ID for the interest"""
    name: str
    """The name of the interest"""
    subscriber_count: str
    """The number of subscribers associated with this interest"""
    display_order: str
    """The display order for interests"""


class InterestsSortFilter(TypedDict, total=False):
    """Available fields for sorting interests search results."""
    category_id: AirbyteSortOrder
    """The id for the interest category"""
    list_id: AirbyteSortOrder
    """The ID for the list that this interest belongs to"""
    id: AirbyteSortOrder
    """The ID for the interest"""
    name: AirbyteSortOrder
    """The name of the interest"""
    subscriber_count: AirbyteSortOrder
    """The number of subscribers associated with this interest"""
    display_order: AirbyteSortOrder
    """The display order for interests"""


# Entity-specific condition types for interests
class InterestsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InterestsSearchFilter


class InterestsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InterestsSearchFilter


class InterestsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InterestsSearchFilter


class InterestsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InterestsSearchFilter


class InterestsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InterestsSearchFilter


class InterestsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InterestsSearchFilter


class InterestsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: InterestsStringFilter


class InterestsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: InterestsStringFilter


class InterestsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InterestsStringFilter


class InterestsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InterestsStringFilter


class InterestsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: InterestsAnyValueFilter


class InterestsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: InterestsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InterestsInCondition = TypedDict("InterestsInCondition", {"in": InterestsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InterestsNotCondition = TypedDict("InterestsNotCondition", {"not": "InterestsCondition"}, total=False)
"""Negates the nested condition."""

InterestsAndCondition = TypedDict("InterestsAndCondition", {"and": "list[InterestsCondition]"}, total=False)
"""True if all nested conditions are true."""

InterestsOrCondition = TypedDict("InterestsOrCondition", {"or": "list[InterestsCondition]"}, total=False)
"""True if any nested condition is true."""

InterestsAnyCondition = TypedDict("InterestsAnyCondition", {"any": InterestsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all interests condition types
InterestsCondition = (
    InterestsEqCondition
    | InterestsNeqCondition
    | InterestsGtCondition
    | InterestsGteCondition
    | InterestsLtCondition
    | InterestsLteCondition
    | InterestsInCondition
    | InterestsStartswithCondition
    | InterestsEndswithCondition
    | InterestsFuzzyCondition
    | InterestsKeywordCondition
    | InterestsContainsCondition
    | InterestsArrayContainsCondition
    | InterestsNotCondition
    | InterestsAndCondition
    | InterestsOrCondition
    | InterestsAnyCondition
)


class InterestsSearchQuery(TypedDict, total=False):
    """Search query for interests entity."""
    filter: InterestsCondition
    sort: list[InterestsSortFilter]


# ===== SEGMENTS SEARCH TYPES =====

class SegmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering segments search queries."""
    id: int
    """The unique id for the segment"""
    name: str | None
    """The name of the segment"""
    member_count: int | None
    """The number of active subscribers currently included in the segment"""
    type_: str | None
    """The type of segment"""
    created_at: str | None
    """The date and time the segment was created"""
    updated_at: str | None
    """The date and time the segment was last updated"""
    options: dict[str, Any] | None
    """The conditions of the segment"""
    list_id: str | None
    """The list id"""


class SegmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """The unique id for the segment"""
    name: list[str]
    """The name of the segment"""
    member_count: list[int]
    """The number of active subscribers currently included in the segment"""
    type_: list[str]
    """The type of segment"""
    created_at: list[str]
    """The date and time the segment was created"""
    updated_at: list[str]
    """The date and time the segment was last updated"""
    options: list[dict[str, Any]]
    """The conditions of the segment"""
    list_id: list[str]
    """The list id"""


class SegmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique id for the segment"""
    name: Any
    """The name of the segment"""
    member_count: Any
    """The number of active subscribers currently included in the segment"""
    type_: Any
    """The type of segment"""
    created_at: Any
    """The date and time the segment was created"""
    updated_at: Any
    """The date and time the segment was last updated"""
    options: Any
    """The conditions of the segment"""
    list_id: Any
    """The list id"""


class SegmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """The unique id for the segment"""
    name: str
    """The name of the segment"""
    member_count: str
    """The number of active subscribers currently included in the segment"""
    type_: str
    """The type of segment"""
    created_at: str
    """The date and time the segment was created"""
    updated_at: str
    """The date and time the segment was last updated"""
    options: str
    """The conditions of the segment"""
    list_id: str
    """The list id"""


class SegmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting segments search results."""
    id: AirbyteSortOrder
    """The unique id for the segment"""
    name: AirbyteSortOrder
    """The name of the segment"""
    member_count: AirbyteSortOrder
    """The number of active subscribers currently included in the segment"""
    type_: AirbyteSortOrder
    """The type of segment"""
    created_at: AirbyteSortOrder
    """The date and time the segment was created"""
    updated_at: AirbyteSortOrder
    """The date and time the segment was last updated"""
    options: AirbyteSortOrder
    """The conditions of the segment"""
    list_id: AirbyteSortOrder
    """The list id"""


# Entity-specific condition types for segments
class SegmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SegmentsSearchFilter


class SegmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SegmentsSearchFilter


class SegmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SegmentsSearchFilter


class SegmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SegmentsSearchFilter


class SegmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SegmentsSearchFilter


class SegmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SegmentsSearchFilter


class SegmentsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SegmentsStringFilter


class SegmentsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SegmentsStringFilter


class SegmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SegmentsStringFilter


class SegmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SegmentsStringFilter


class SegmentsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SegmentsAnyValueFilter


class SegmentsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SegmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SegmentsInCondition = TypedDict("SegmentsInCondition", {"in": SegmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SegmentsNotCondition = TypedDict("SegmentsNotCondition", {"not": "SegmentsCondition"}, total=False)
"""Negates the nested condition."""

SegmentsAndCondition = TypedDict("SegmentsAndCondition", {"and": "list[SegmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

SegmentsOrCondition = TypedDict("SegmentsOrCondition", {"or": "list[SegmentsCondition]"}, total=False)
"""True if any nested condition is true."""

SegmentsAnyCondition = TypedDict("SegmentsAnyCondition", {"any": SegmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all segments condition types
SegmentsCondition = (
    SegmentsEqCondition
    | SegmentsNeqCondition
    | SegmentsGtCondition
    | SegmentsGteCondition
    | SegmentsLtCondition
    | SegmentsLteCondition
    | SegmentsInCondition
    | SegmentsStartswithCondition
    | SegmentsEndswithCondition
    | SegmentsFuzzyCondition
    | SegmentsKeywordCondition
    | SegmentsContainsCondition
    | SegmentsArrayContainsCondition
    | SegmentsNotCondition
    | SegmentsAndCondition
    | SegmentsOrCondition
    | SegmentsAnyCondition
)


class SegmentsSearchQuery(TypedDict, total=False):
    """Search query for segments entity."""
    filter: SegmentsCondition
    sort: list[SegmentsSortFilter]


# ===== SEGMENT_MEMBERS SEARCH TYPES =====

class SegmentMembersSearchFilter(TypedDict, total=False):
    """Available fields for filtering segment_members search queries."""
    id: str
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: str | None
    """Email address for a subscriber"""
    unique_email_id: str | None
    """An identifier for the address across all of Mailchimp"""
    email_type: str | None
    """Type of email this member asked to get"""
    status: str | None
    """Subscriber's current status"""
    merge_fields: dict[str, Any] | None
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: dict[str, Any] | None
    """The key of this object's properties is the ID of the interest in question"""
    stats: dict[str, Any] | None
    """Open and click rates for this subscriber"""
    ip_signup: str | None
    """IP address the subscriber signed up from"""
    timestamp_signup: str | None
    """The date and time the subscriber signed up for the list"""
    ip_opt: str | None
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: str | None
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: int | None
    """Star rating for this member, between 1 and 5"""
    last_changed: str | None
    """The date and time the member's info was last changed"""
    language: str | None
    """If set/detected, the subscriber's language"""
    vip: bool | None
    """VIP status for subscriber"""
    email_client: str | None
    """The list member's email client"""
    location: dict[str, Any] | None
    """Subscriber location information"""
    list_id: str | None
    """The list id"""


class SegmentMembersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: list[str]
    """Email address for a subscriber"""
    unique_email_id: list[str]
    """An identifier for the address across all of Mailchimp"""
    email_type: list[str]
    """Type of email this member asked to get"""
    status: list[str]
    """Subscriber's current status"""
    merge_fields: list[dict[str, Any]]
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: list[dict[str, Any]]
    """The key of this object's properties is the ID of the interest in question"""
    stats: list[dict[str, Any]]
    """Open and click rates for this subscriber"""
    ip_signup: list[str]
    """IP address the subscriber signed up from"""
    timestamp_signup: list[str]
    """The date and time the subscriber signed up for the list"""
    ip_opt: list[str]
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: list[str]
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: list[int]
    """Star rating for this member, between 1 and 5"""
    last_changed: list[str]
    """The date and time the member's info was last changed"""
    language: list[str]
    """If set/detected, the subscriber's language"""
    vip: list[bool]
    """VIP status for subscriber"""
    email_client: list[str]
    """The list member's email client"""
    location: list[dict[str, Any]]
    """Subscriber location information"""
    list_id: list[str]
    """The list id"""


class SegmentMembersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: Any
    """Email address for a subscriber"""
    unique_email_id: Any
    """An identifier for the address across all of Mailchimp"""
    email_type: Any
    """Type of email this member asked to get"""
    status: Any
    """Subscriber's current status"""
    merge_fields: Any
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: Any
    """The key of this object's properties is the ID of the interest in question"""
    stats: Any
    """Open and click rates for this subscriber"""
    ip_signup: Any
    """IP address the subscriber signed up from"""
    timestamp_signup: Any
    """The date and time the subscriber signed up for the list"""
    ip_opt: Any
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: Any
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: Any
    """Star rating for this member, between 1 and 5"""
    last_changed: Any
    """The date and time the member's info was last changed"""
    language: Any
    """If set/detected, the subscriber's language"""
    vip: Any
    """VIP status for subscriber"""
    email_client: Any
    """The list member's email client"""
    location: Any
    """Subscriber location information"""
    list_id: Any
    """The list id"""


class SegmentMembersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: str
    """Email address for a subscriber"""
    unique_email_id: str
    """An identifier for the address across all of Mailchimp"""
    email_type: str
    """Type of email this member asked to get"""
    status: str
    """Subscriber's current status"""
    merge_fields: str
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: str
    """The key of this object's properties is the ID of the interest in question"""
    stats: str
    """Open and click rates for this subscriber"""
    ip_signup: str
    """IP address the subscriber signed up from"""
    timestamp_signup: str
    """The date and time the subscriber signed up for the list"""
    ip_opt: str
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: str
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: str
    """Star rating for this member, between 1 and 5"""
    last_changed: str
    """The date and time the member's info was last changed"""
    language: str
    """If set/detected, the subscriber's language"""
    vip: str
    """VIP status for subscriber"""
    email_client: str
    """The list member's email client"""
    location: str
    """Subscriber location information"""
    list_id: str
    """The list id"""


class SegmentMembersSortFilter(TypedDict, total=False):
    """Available fields for sorting segment_members search results."""
    id: AirbyteSortOrder
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: AirbyteSortOrder
    """Email address for a subscriber"""
    unique_email_id: AirbyteSortOrder
    """An identifier for the address across all of Mailchimp"""
    email_type: AirbyteSortOrder
    """Type of email this member asked to get"""
    status: AirbyteSortOrder
    """Subscriber's current status"""
    merge_fields: AirbyteSortOrder
    """A dictionary of merge fields where the keys are the merge tags"""
    interests: AirbyteSortOrder
    """The key of this object's properties is the ID of the interest in question"""
    stats: AirbyteSortOrder
    """Open and click rates for this subscriber"""
    ip_signup: AirbyteSortOrder
    """IP address the subscriber signed up from"""
    timestamp_signup: AirbyteSortOrder
    """The date and time the subscriber signed up for the list"""
    ip_opt: AirbyteSortOrder
    """The IP address the subscriber used to confirm their opt-in status"""
    timestamp_opt: AirbyteSortOrder
    """The date and time the subscriber confirmed their opt-in status"""
    member_rating: AirbyteSortOrder
    """Star rating for this member, between 1 and 5"""
    last_changed: AirbyteSortOrder
    """The date and time the member's info was last changed"""
    language: AirbyteSortOrder
    """If set/detected, the subscriber's language"""
    vip: AirbyteSortOrder
    """VIP status for subscriber"""
    email_client: AirbyteSortOrder
    """The list member's email client"""
    location: AirbyteSortOrder
    """Subscriber location information"""
    list_id: AirbyteSortOrder
    """The list id"""


# Entity-specific condition types for segment_members
class SegmentMembersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SegmentMembersSearchFilter


class SegmentMembersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SegmentMembersSearchFilter


class SegmentMembersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SegmentMembersSearchFilter


class SegmentMembersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SegmentMembersSearchFilter


class SegmentMembersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SegmentMembersSearchFilter


class SegmentMembersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SegmentMembersSearchFilter


class SegmentMembersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SegmentMembersStringFilter


class SegmentMembersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SegmentMembersStringFilter


class SegmentMembersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SegmentMembersStringFilter


class SegmentMembersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SegmentMembersStringFilter


class SegmentMembersContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SegmentMembersAnyValueFilter


class SegmentMembersArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SegmentMembersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SegmentMembersInCondition = TypedDict("SegmentMembersInCondition", {"in": SegmentMembersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SegmentMembersNotCondition = TypedDict("SegmentMembersNotCondition", {"not": "SegmentMembersCondition"}, total=False)
"""Negates the nested condition."""

SegmentMembersAndCondition = TypedDict("SegmentMembersAndCondition", {"and": "list[SegmentMembersCondition]"}, total=False)
"""True if all nested conditions are true."""

SegmentMembersOrCondition = TypedDict("SegmentMembersOrCondition", {"or": "list[SegmentMembersCondition]"}, total=False)
"""True if any nested condition is true."""

SegmentMembersAnyCondition = TypedDict("SegmentMembersAnyCondition", {"any": SegmentMembersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all segment_members condition types
SegmentMembersCondition = (
    SegmentMembersEqCondition
    | SegmentMembersNeqCondition
    | SegmentMembersGtCondition
    | SegmentMembersGteCondition
    | SegmentMembersLtCondition
    | SegmentMembersLteCondition
    | SegmentMembersInCondition
    | SegmentMembersStartswithCondition
    | SegmentMembersEndswithCondition
    | SegmentMembersFuzzyCondition
    | SegmentMembersKeywordCondition
    | SegmentMembersContainsCondition
    | SegmentMembersArrayContainsCondition
    | SegmentMembersNotCondition
    | SegmentMembersAndCondition
    | SegmentMembersOrCondition
    | SegmentMembersAnyCondition
)


class SegmentMembersSearchQuery(TypedDict, total=False):
    """Search query for segment_members entity."""
    filter: SegmentMembersCondition
    sort: list[SegmentMembersSortFilter]


# ===== UNSUBSCRIBES SEARCH TYPES =====

class UnsubscribesSearchFilter(TypedDict, total=False):
    """Available fields for filtering unsubscribes search queries."""
    email_id: str | None
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: str | None
    """Email address for a subscriber"""
    merge_fields: dict[str, Any] | None
    """A dictionary of merge fields where the keys are the merge tags"""
    vip: bool | None
    """VIP status for subscriber"""
    timestamp: str | None
    """The date and time the member opted-out"""
    reason: str | None
    """If available, the reason listed by the member for unsubscribing"""
    campaign_id: str | None
    """The campaign id"""
    list_id: str | None
    """The list id"""
    list_is_active: bool | None
    """The status of the list used"""


class UnsubscribesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    email_id: list[str]
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: list[str]
    """Email address for a subscriber"""
    merge_fields: list[dict[str, Any]]
    """A dictionary of merge fields where the keys are the merge tags"""
    vip: list[bool]
    """VIP status for subscriber"""
    timestamp: list[str]
    """The date and time the member opted-out"""
    reason: list[str]
    """If available, the reason listed by the member for unsubscribing"""
    campaign_id: list[str]
    """The campaign id"""
    list_id: list[str]
    """The list id"""
    list_is_active: list[bool]
    """The status of the list used"""


class UnsubscribesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    email_id: Any
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: Any
    """Email address for a subscriber"""
    merge_fields: Any
    """A dictionary of merge fields where the keys are the merge tags"""
    vip: Any
    """VIP status for subscriber"""
    timestamp: Any
    """The date and time the member opted-out"""
    reason: Any
    """If available, the reason listed by the member for unsubscribing"""
    campaign_id: Any
    """The campaign id"""
    list_id: Any
    """The list id"""
    list_is_active: Any
    """The status of the list used"""


class UnsubscribesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    email_id: str
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: str
    """Email address for a subscriber"""
    merge_fields: str
    """A dictionary of merge fields where the keys are the merge tags"""
    vip: str
    """VIP status for subscriber"""
    timestamp: str
    """The date and time the member opted-out"""
    reason: str
    """If available, the reason listed by the member for unsubscribing"""
    campaign_id: str
    """The campaign id"""
    list_id: str
    """The list id"""
    list_is_active: str
    """The status of the list used"""


class UnsubscribesSortFilter(TypedDict, total=False):
    """Available fields for sorting unsubscribes search results."""
    email_id: AirbyteSortOrder
    """The MD5 hash of the lowercase version of the list member's email address"""
    email_address: AirbyteSortOrder
    """Email address for a subscriber"""
    merge_fields: AirbyteSortOrder
    """A dictionary of merge fields where the keys are the merge tags"""
    vip: AirbyteSortOrder
    """VIP status for subscriber"""
    timestamp: AirbyteSortOrder
    """The date and time the member opted-out"""
    reason: AirbyteSortOrder
    """If available, the reason listed by the member for unsubscribing"""
    campaign_id: AirbyteSortOrder
    """The campaign id"""
    list_id: AirbyteSortOrder
    """The list id"""
    list_is_active: AirbyteSortOrder
    """The status of the list used"""


# Entity-specific condition types for unsubscribes
class UnsubscribesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UnsubscribesSearchFilter


class UnsubscribesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UnsubscribesSearchFilter


class UnsubscribesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UnsubscribesSearchFilter


class UnsubscribesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UnsubscribesSearchFilter


class UnsubscribesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UnsubscribesSearchFilter


class UnsubscribesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UnsubscribesSearchFilter


class UnsubscribesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UnsubscribesStringFilter


class UnsubscribesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UnsubscribesStringFilter


class UnsubscribesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UnsubscribesStringFilter


class UnsubscribesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UnsubscribesStringFilter


class UnsubscribesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: UnsubscribesAnyValueFilter


class UnsubscribesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: UnsubscribesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UnsubscribesInCondition = TypedDict("UnsubscribesInCondition", {"in": UnsubscribesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UnsubscribesNotCondition = TypedDict("UnsubscribesNotCondition", {"not": "UnsubscribesCondition"}, total=False)
"""Negates the nested condition."""

UnsubscribesAndCondition = TypedDict("UnsubscribesAndCondition", {"and": "list[UnsubscribesCondition]"}, total=False)
"""True if all nested conditions are true."""

UnsubscribesOrCondition = TypedDict("UnsubscribesOrCondition", {"or": "list[UnsubscribesCondition]"}, total=False)
"""True if any nested condition is true."""

UnsubscribesAnyCondition = TypedDict("UnsubscribesAnyCondition", {"any": UnsubscribesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all unsubscribes condition types
UnsubscribesCondition = (
    UnsubscribesEqCondition
    | UnsubscribesNeqCondition
    | UnsubscribesGtCondition
    | UnsubscribesGteCondition
    | UnsubscribesLtCondition
    | UnsubscribesLteCondition
    | UnsubscribesInCondition
    | UnsubscribesStartswithCondition
    | UnsubscribesEndswithCondition
    | UnsubscribesFuzzyCondition
    | UnsubscribesKeywordCondition
    | UnsubscribesContainsCondition
    | UnsubscribesArrayContainsCondition
    | UnsubscribesNotCondition
    | UnsubscribesAndCondition
    | UnsubscribesOrCondition
    | UnsubscribesAnyCondition
)


class UnsubscribesSearchQuery(TypedDict, total=False):
    """Search query for unsubscribes entity."""
    filter: UnsubscribesCondition
    sort: list[UnsubscribesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
