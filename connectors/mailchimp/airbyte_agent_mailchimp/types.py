"""
Type definitions for mailchimp connector.
"""
from __future__ import annotations

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
    type: str | None
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
    type: list[str]
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
    type: Any
    """There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y..."""
    variate_settings: Any
    """The settings specific to A/B test campaigns."""
    web_id: Any
    """The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht..."""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
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
    type: str
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
    type: AirbyteSortOrder
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


class CampaignsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignsAnyValueFilter


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
    | CampaignsLikeCondition
    | CampaignsFuzzyCondition
    | CampaignsKeywordCondition
    | CampaignsContainsCondition
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
    type: str | None
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
    type: list[str]
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
    type: Any
    """If the action is a 'bounce', the type of bounce received: 'hard', 'soft'."""
    url: Any
    """If the action is a 'click', the URL on which the member clicked."""


class EmailActivityStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
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
    type: str
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
    type: AirbyteSortOrder
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


class EmailActivityLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EmailActivityStringFilter


class EmailActivityFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EmailActivityStringFilter


class EmailActivityKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EmailActivityStringFilter


class EmailActivityContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EmailActivityAnyValueFilter


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
    | EmailActivityLikeCondition
    | EmailActivityFuzzyCondition
    | EmailActivityKeywordCondition
    | EmailActivityContainsCondition
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
    """String fields for text search conditions (like, fuzzy, keyword)."""
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


class ListsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ListsStringFilter


class ListsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListsStringFilter


class ListsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListsStringFilter


class ListsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ListsAnyValueFilter


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
    | ListsLikeCondition
    | ListsFuzzyCondition
    | ListsKeywordCondition
    | ListsContainsCondition
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
    type: str | None
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
    type: list[str]
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
    type: Any
    """The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto)."""
    unsubscribed: Any
    """The total number of unsubscribed members for this campaign."""


class ReportsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
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
    type: str
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
    type: AirbyteSortOrder
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


class ReportsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ReportsStringFilter


class ReportsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ReportsStringFilter


class ReportsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ReportsStringFilter


class ReportsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ReportsAnyValueFilter


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
    | ReportsLikeCondition
    | ReportsFuzzyCondition
    | ReportsKeywordCondition
    | ReportsContainsCondition
    | ReportsNotCondition
    | ReportsAndCondition
    | ReportsOrCondition
    | ReportsAnyCondition
)


class ReportsSearchQuery(TypedDict, total=False):
    """Search query for reports entity."""
    filter: ReportsCondition
    sort: list[ReportsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
