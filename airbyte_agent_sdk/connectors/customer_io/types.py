"""
Type definitions for customer-io connector.
"""
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

class SegmentsCreateParamsSegment(TypedDict):
    """Nested schema for SegmentsCreateParams.segment"""
    name: str
    description: NotRequired[str]

class TransactionalMessageContentsUpdateParamsHeadersItem(TypedDict):
    """Nested schema for TransactionalMessageContentsUpdateParams.headers_item"""
    name: NotRequired[str]
    value: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    pass

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    campaign_id: str

class CampaignActionsListParams(TypedDict):
    """Parameters for campaign_actions.list operation"""
    campaign_id: str
    start: NotRequired[str]

class CampaignActionsGetParams(TypedDict):
    """Parameters for campaign_actions.get operation"""
    campaign_id: str
    action_id: str

class NewslettersListParams(TypedDict):
    """Parameters for newsletters.list operation"""
    start: NotRequired[str]
    limit: NotRequired[int]
    sort: NotRequired[str]

class NewslettersGetParams(TypedDict):
    """Parameters for newsletters.get operation"""
    newsletter_id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    pass

class SegmentsCreateParams(TypedDict):
    """Parameters for segments.create operation"""
    segment: SegmentsCreateParamsSegment

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    segment_id: str

class MessagesListParams(TypedDict):
    """Parameters for messages.list operation"""
    start: NotRequired[str]
    limit: NotRequired[int]
    type: NotRequired[str]
    metric: NotRequired[str]
    campaign_id: NotRequired[int]
    newsletter_id: NotRequired[int]

class MessagesGetParams(TypedDict):
    """Parameters for messages.get operation"""
    message_id: str

class ActivitiesListParams(TypedDict):
    """Parameters for activities.list operation"""
    start: NotRequired[str]
    limit: NotRequired[int]
    type: NotRequired[str]
    name: NotRequired[str]

class SenderIdentitiesListParams(TypedDict):
    """Parameters for sender_identities.list operation"""
    start: NotRequired[str]
    limit: NotRequired[int]
    sort: NotRequired[str]

class SenderIdentitiesGetParams(TypedDict):
    """Parameters for sender_identities.get operation"""
    sender_id: str

class SnippetsListParams(TypedDict):
    """Parameters for snippets.list operation"""
    pass

class SnippetsCreateParams(TypedDict):
    """Parameters for snippets.create operation"""
    name: str
    value: str

class SnippetsUpdateParams(TypedDict):
    """Parameters for snippets.update operation"""
    name: str
    value: str

class CollectionsListParams(TypedDict):
    """Parameters for collections.list operation"""
    pass

class CollectionsCreateParams(TypedDict):
    """Parameters for collections.create operation"""
    name: str
    data: NotRequired[list[dict[str, Any]]]
    url: NotRequired[str]

class CollectionsGetParams(TypedDict):
    """Parameters for collections.get operation"""
    collection_id: str

class CollectionsUpdateParams(TypedDict):
    """Parameters for collections.update operation"""
    name: NotRequired[str]
    data: NotRequired[list[dict[str, Any]]]
    url: NotRequired[str]
    collection_id: str

class ReportingWebhooksListParams(TypedDict):
    """Parameters for reporting_webhooks.list operation"""
    pass

class ReportingWebhooksCreateParams(TypedDict):
    """Parameters for reporting_webhooks.create operation"""
    name: str
    endpoint: str
    events: list[str]
    disabled: NotRequired[bool]
    full_resolution: NotRequired[bool]
    with_content: NotRequired[bool]

class ReportingWebhooksGetParams(TypedDict):
    """Parameters for reporting_webhooks.get operation"""
    webhook_id: str

class ReportingWebhooksUpdateParams(TypedDict):
    """Parameters for reporting_webhooks.update operation"""
    name: str
    endpoint: str
    events: list[str]
    disabled: NotRequired[bool]
    full_resolution: NotRequired[bool]
    with_content: NotRequired[bool]
    webhook_id: str

class ExportsListParams(TypedDict):
    """Parameters for exports.list operation"""
    pass

class ExportsCreateParams(TypedDict):
    """Parameters for exports.create operation"""
    filters: dict[str, Any]

class ExportsGetParams(TypedDict):
    """Parameters for exports.get operation"""
    export_id: str

class TransactionalMessagesListParams(TypedDict):
    """Parameters for transactional_messages.list operation"""
    pass

class TransactionalMessagesGetParams(TypedDict):
    """Parameters for transactional_messages.get operation"""
    transactional_id: str

class TransactionalMessageContentsListParams(TypedDict):
    """Parameters for transactional_message_contents.list operation"""
    transactional_id: str

class TransactionalMessageContentsUpdateParams(TypedDict):
    """Parameters for transactional_message_contents.update operation"""
    body: NotRequired[str]
    from_id: NotRequired[int]
    reply_to_id: NotRequired[int | None]
    recipient: NotRequired[str]
    subject: NotRequired[str]
    preheader_text: NotRequired[str]
    body_amp: NotRequired[str]
    headers: NotRequired[list[TransactionalMessageContentsUpdateParamsHeadersItem]]
    transactional_id: str
    content_id: str

class TransactionalEmailCreateParams(TypedDict):
    """Parameters for transactional_email.create operation"""
    transactional_message_id: NotRequired[Any]
    to: str
    identifiers: dict[str, Any]
    message_data: NotRequired[dict[str, Any]]
    from_: NotRequired[str]
    subject: NotRequired[str]
    body: NotRequired[str]
    body_plain: NotRequired[str]
    reply_to: NotRequired[str]
    bcc: NotRequired[str]
    headers: NotRequired[dict[str, Any]]
    preheader_text: NotRequired[str]
    attachments: NotRequired[dict[str, Any]]
    disable_message_retention: NotRequired[bool]
    send_to_unsubscribed: NotRequired[bool]
    tracked: NotRequired[bool]
    queue_draft: NotRequired[bool]
    send_at: NotRequired[int]

class TransactionalSmsCreateParams(TypedDict):
    """Parameters for transactional_sms.create operation"""
    transactional_message_id: Any
    to: str
    identifiers: dict[str, Any]
    message_data: NotRequired[dict[str, Any]]
    from_: NotRequired[str]
    send_to_unsubscribed: NotRequired[bool]
    tracked: NotRequired[bool]
    queue_draft: NotRequired[bool]
    disable_message_retention: NotRequired[bool]

class TransactionalPushCreateParams(TypedDict):
    """Parameters for transactional_push.create operation"""
    transactional_message_id: NotRequired[Any]
    to: NotRequired[str]
    identifiers: dict[str, Any]
    message_data: NotRequired[dict[str, Any]]
    title: NotRequired[str]
    message: NotRequired[str]
    link: NotRequired[str]
    image_url: NotRequired[str]
    custom_data: NotRequired[dict[str, Any]]
    custom_payload: NotRequired[dict[str, Any]]
    sound: NotRequired[str]
    send_to_unsubscribed: NotRequired[bool]
    queue_draft: NotRequired[bool]
    disable_message_retention: NotRequired[bool]
    send_at: NotRequired[int]

class TransactionalInboxMessageCreateParams(TypedDict):
    """Parameters for transactional_inbox_message.create operation"""
    transactional_message_id: Any
    identifiers: dict[str, Any]
    message_data: NotRequired[dict[str, Any]]

class BroadcastTriggerCreateParams(TypedDict):
    """Parameters for broadcast_trigger.create operation"""
    data: NotRequired[dict[str, Any]]
    recipients: NotRequired[dict[str, Any]]
    ids: NotRequired[list[str]]
    emails: NotRequired[list[str]]
    per_user_data: NotRequired[list[dict[str, Any]]]
    data_file_url: NotRequired[str]
    id_ignore_missing: NotRequired[bool]
    email_ignore_missing: NotRequired[bool]
    email_add_duplicates: NotRequired[bool]
    campaign_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    actions: list[Any] | None
    """Actions defined in this campaign"""
    active: bool | None
    """Whether the campaign is active"""
    created: int | None
    """Creation timestamp (Unix)"""
    created_by: str | None
    """Who created the campaign"""
    date_attribute: str | None
    """Date attribute used for date-triggered campaigns"""
    deduplicate_id: str | None
    """Deduplication identifier"""
    event_name: str | None
    """Event name that triggers the campaign"""
    first_started: int | None
    """When the campaign was first started (Unix)"""
    frequency: str | None
    """How frequently a person can receive this campaign"""
    id: int | None
    """Unique campaign identifier"""
    msg_templates: list[Any] | None
    """Message templates used in the campaign"""
    name: str | None
    """Campaign name"""
    start_hour: int | None
    """Hour of the day to trigger"""
    start_minutes: int | None
    """Minute of the hour to trigger"""
    state: str | None
    """Campaign status (draft, active, stopped)"""
    tags: list[Any] | None
    """Tags associated with the campaign"""
    timezone: str | None
    """Timezone for trigger scheduling"""
    trigger_segment_ids: list[Any] | None
    """Segment IDs that trigger this campaign"""
    type_: str | None
    """Campaign trigger type"""
    updated: int | None
    """Last update timestamp (Unix)"""
    use_customer_timezone: bool | None
    """Whether to use the customer's timezone"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    actions: list[list[Any]]
    """Actions defined in this campaign"""
    active: list[bool]
    """Whether the campaign is active"""
    created: list[int]
    """Creation timestamp (Unix)"""
    created_by: list[str]
    """Who created the campaign"""
    date_attribute: list[str]
    """Date attribute used for date-triggered campaigns"""
    deduplicate_id: list[str]
    """Deduplication identifier"""
    event_name: list[str]
    """Event name that triggers the campaign"""
    first_started: list[int]
    """When the campaign was first started (Unix)"""
    frequency: list[str]
    """How frequently a person can receive this campaign"""
    id: list[int]
    """Unique campaign identifier"""
    msg_templates: list[list[Any]]
    """Message templates used in the campaign"""
    name: list[str]
    """Campaign name"""
    start_hour: list[int]
    """Hour of the day to trigger"""
    start_minutes: list[int]
    """Minute of the hour to trigger"""
    state: list[str]
    """Campaign status (draft, active, stopped)"""
    tags: list[list[Any]]
    """Tags associated with the campaign"""
    timezone: list[str]
    """Timezone for trigger scheduling"""
    trigger_segment_ids: list[list[Any]]
    """Segment IDs that trigger this campaign"""
    type_: list[str]
    """Campaign trigger type"""
    updated: list[int]
    """Last update timestamp (Unix)"""
    use_customer_timezone: list[bool]
    """Whether to use the customer's timezone"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    actions: Any
    """Actions defined in this campaign"""
    active: Any
    """Whether the campaign is active"""
    created: Any
    """Creation timestamp (Unix)"""
    created_by: Any
    """Who created the campaign"""
    date_attribute: Any
    """Date attribute used for date-triggered campaigns"""
    deduplicate_id: Any
    """Deduplication identifier"""
    event_name: Any
    """Event name that triggers the campaign"""
    first_started: Any
    """When the campaign was first started (Unix)"""
    frequency: Any
    """How frequently a person can receive this campaign"""
    id: Any
    """Unique campaign identifier"""
    msg_templates: Any
    """Message templates used in the campaign"""
    name: Any
    """Campaign name"""
    start_hour: Any
    """Hour of the day to trigger"""
    start_minutes: Any
    """Minute of the hour to trigger"""
    state: Any
    """Campaign status (draft, active, stopped)"""
    tags: Any
    """Tags associated with the campaign"""
    timezone: Any
    """Timezone for trigger scheduling"""
    trigger_segment_ids: Any
    """Segment IDs that trigger this campaign"""
    type_: Any
    """Campaign trigger type"""
    updated: Any
    """Last update timestamp (Unix)"""
    use_customer_timezone: Any
    """Whether to use the customer's timezone"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    actions: str
    """Actions defined in this campaign"""
    active: str
    """Whether the campaign is active"""
    created: str
    """Creation timestamp (Unix)"""
    created_by: str
    """Who created the campaign"""
    date_attribute: str
    """Date attribute used for date-triggered campaigns"""
    deduplicate_id: str
    """Deduplication identifier"""
    event_name: str
    """Event name that triggers the campaign"""
    first_started: str
    """When the campaign was first started (Unix)"""
    frequency: str
    """How frequently a person can receive this campaign"""
    id: str
    """Unique campaign identifier"""
    msg_templates: str
    """Message templates used in the campaign"""
    name: str
    """Campaign name"""
    start_hour: str
    """Hour of the day to trigger"""
    start_minutes: str
    """Minute of the hour to trigger"""
    state: str
    """Campaign status (draft, active, stopped)"""
    tags: str
    """Tags associated with the campaign"""
    timezone: str
    """Timezone for trigger scheduling"""
    trigger_segment_ids: str
    """Segment IDs that trigger this campaign"""
    type_: str
    """Campaign trigger type"""
    updated: str
    """Last update timestamp (Unix)"""
    use_customer_timezone: str
    """Whether to use the customer's timezone"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    actions: AirbyteSortOrder
    """Actions defined in this campaign"""
    active: AirbyteSortOrder
    """Whether the campaign is active"""
    created: AirbyteSortOrder
    """Creation timestamp (Unix)"""
    created_by: AirbyteSortOrder
    """Who created the campaign"""
    date_attribute: AirbyteSortOrder
    """Date attribute used for date-triggered campaigns"""
    deduplicate_id: AirbyteSortOrder
    """Deduplication identifier"""
    event_name: AirbyteSortOrder
    """Event name that triggers the campaign"""
    first_started: AirbyteSortOrder
    """When the campaign was first started (Unix)"""
    frequency: AirbyteSortOrder
    """How frequently a person can receive this campaign"""
    id: AirbyteSortOrder
    """Unique campaign identifier"""
    msg_templates: AirbyteSortOrder
    """Message templates used in the campaign"""
    name: AirbyteSortOrder
    """Campaign name"""
    start_hour: AirbyteSortOrder
    """Hour of the day to trigger"""
    start_minutes: AirbyteSortOrder
    """Minute of the hour to trigger"""
    state: AirbyteSortOrder
    """Campaign status (draft, active, stopped)"""
    tags: AirbyteSortOrder
    """Tags associated with the campaign"""
    timezone: AirbyteSortOrder
    """Timezone for trigger scheduling"""
    trigger_segment_ids: AirbyteSortOrder
    """Segment IDs that trigger this campaign"""
    type_: AirbyteSortOrder
    """Campaign trigger type"""
    updated: AirbyteSortOrder
    """Last update timestamp (Unix)"""
    use_customer_timezone: AirbyteSortOrder
    """Whether to use the customer's timezone"""


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


# ===== CAMPAIGN_ACTIONS SEARCH TYPES =====

class CampaignActionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaign_actions search queries."""
    bcc: str | None
    """BCC addresses"""
    body: str | None
    """Action body content (HTML for emails)"""
    campaign_id: int | None
    """Parent campaign ID"""
    created: int | None
    """Creation timestamp (Unix)"""
    deduplicate_id: str | None
    """Deduplication identifier"""
    editor: str | None
    """Editor used to create the action"""
    fake_bcc: bool | None
    """Whether to use fake BCC"""
    from_: str | None
    """From address"""
    from_id: str | None
    """Sender identity ID"""
    headers: str | None
    """Custom email headers as JSON"""
    id: str | None
    """Unique action identifier"""
    language: str | None
    """Language variant"""
    layout: str | None
    """Layout template used"""
    name: str | None
    """Action name"""
    parent_action_id: int | None
    """Parent action ID for language variants"""
    preheader_text: str | None
    """Email preheader/preview text"""
    preprocessor: str | None
    """CSS preprocessor setting"""
    recipient: str | None
    """Recipient address"""
    recipient_environment_id: int | None
    """Recipient environment ID"""
    reply_to: str | None
    """Reply-to address"""
    reply_to_id: str | None
    """Reply-to sender identity ID"""
    request_method: str | None
    """HTTP request method for webhook actions"""
    sending_state: str | None
    """Sending behavior (automatic or draft)"""
    subject: str | None
    """Email subject line"""
    type_: str | None
    """Action type (email, webhook, twilio, push, slack, in_app, whatsapp)"""
    updated: int | None
    """Last update timestamp (Unix)"""
    url: str | None
    """Webhook URL (for webhook actions)"""


class CampaignActionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    bcc: list[str]
    """BCC addresses"""
    body: list[str]
    """Action body content (HTML for emails)"""
    campaign_id: list[int]
    """Parent campaign ID"""
    created: list[int]
    """Creation timestamp (Unix)"""
    deduplicate_id: list[str]
    """Deduplication identifier"""
    editor: list[str]
    """Editor used to create the action"""
    fake_bcc: list[bool]
    """Whether to use fake BCC"""
    from_: list[str]
    """From address"""
    from_id: list[str]
    """Sender identity ID"""
    headers: list[str]
    """Custom email headers as JSON"""
    id: list[str]
    """Unique action identifier"""
    language: list[str]
    """Language variant"""
    layout: list[str]
    """Layout template used"""
    name: list[str]
    """Action name"""
    parent_action_id: list[int]
    """Parent action ID for language variants"""
    preheader_text: list[str]
    """Email preheader/preview text"""
    preprocessor: list[str]
    """CSS preprocessor setting"""
    recipient: list[str]
    """Recipient address"""
    recipient_environment_id: list[int]
    """Recipient environment ID"""
    reply_to: list[str]
    """Reply-to address"""
    reply_to_id: list[str]
    """Reply-to sender identity ID"""
    request_method: list[str]
    """HTTP request method for webhook actions"""
    sending_state: list[str]
    """Sending behavior (automatic or draft)"""
    subject: list[str]
    """Email subject line"""
    type_: list[str]
    """Action type (email, webhook, twilio, push, slack, in_app, whatsapp)"""
    updated: list[int]
    """Last update timestamp (Unix)"""
    url: list[str]
    """Webhook URL (for webhook actions)"""


class CampaignActionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    bcc: Any
    """BCC addresses"""
    body: Any
    """Action body content (HTML for emails)"""
    campaign_id: Any
    """Parent campaign ID"""
    created: Any
    """Creation timestamp (Unix)"""
    deduplicate_id: Any
    """Deduplication identifier"""
    editor: Any
    """Editor used to create the action"""
    fake_bcc: Any
    """Whether to use fake BCC"""
    from_: Any
    """From address"""
    from_id: Any
    """Sender identity ID"""
    headers: Any
    """Custom email headers as JSON"""
    id: Any
    """Unique action identifier"""
    language: Any
    """Language variant"""
    layout: Any
    """Layout template used"""
    name: Any
    """Action name"""
    parent_action_id: Any
    """Parent action ID for language variants"""
    preheader_text: Any
    """Email preheader/preview text"""
    preprocessor: Any
    """CSS preprocessor setting"""
    recipient: Any
    """Recipient address"""
    recipient_environment_id: Any
    """Recipient environment ID"""
    reply_to: Any
    """Reply-to address"""
    reply_to_id: Any
    """Reply-to sender identity ID"""
    request_method: Any
    """HTTP request method for webhook actions"""
    sending_state: Any
    """Sending behavior (automatic or draft)"""
    subject: Any
    """Email subject line"""
    type_: Any
    """Action type (email, webhook, twilio, push, slack, in_app, whatsapp)"""
    updated: Any
    """Last update timestamp (Unix)"""
    url: Any
    """Webhook URL (for webhook actions)"""


class CampaignActionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    bcc: str
    """BCC addresses"""
    body: str
    """Action body content (HTML for emails)"""
    campaign_id: str
    """Parent campaign ID"""
    created: str
    """Creation timestamp (Unix)"""
    deduplicate_id: str
    """Deduplication identifier"""
    editor: str
    """Editor used to create the action"""
    fake_bcc: str
    """Whether to use fake BCC"""
    from_: str
    """From address"""
    from_id: str
    """Sender identity ID"""
    headers: str
    """Custom email headers as JSON"""
    id: str
    """Unique action identifier"""
    language: str
    """Language variant"""
    layout: str
    """Layout template used"""
    name: str
    """Action name"""
    parent_action_id: str
    """Parent action ID for language variants"""
    preheader_text: str
    """Email preheader/preview text"""
    preprocessor: str
    """CSS preprocessor setting"""
    recipient: str
    """Recipient address"""
    recipient_environment_id: str
    """Recipient environment ID"""
    reply_to: str
    """Reply-to address"""
    reply_to_id: str
    """Reply-to sender identity ID"""
    request_method: str
    """HTTP request method for webhook actions"""
    sending_state: str
    """Sending behavior (automatic or draft)"""
    subject: str
    """Email subject line"""
    type_: str
    """Action type (email, webhook, twilio, push, slack, in_app, whatsapp)"""
    updated: str
    """Last update timestamp (Unix)"""
    url: str
    """Webhook URL (for webhook actions)"""


class CampaignActionsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaign_actions search results."""
    bcc: AirbyteSortOrder
    """BCC addresses"""
    body: AirbyteSortOrder
    """Action body content (HTML for emails)"""
    campaign_id: AirbyteSortOrder
    """Parent campaign ID"""
    created: AirbyteSortOrder
    """Creation timestamp (Unix)"""
    deduplicate_id: AirbyteSortOrder
    """Deduplication identifier"""
    editor: AirbyteSortOrder
    """Editor used to create the action"""
    fake_bcc: AirbyteSortOrder
    """Whether to use fake BCC"""
    from_: AirbyteSortOrder
    """From address"""
    from_id: AirbyteSortOrder
    """Sender identity ID"""
    headers: AirbyteSortOrder
    """Custom email headers as JSON"""
    id: AirbyteSortOrder
    """Unique action identifier"""
    language: AirbyteSortOrder
    """Language variant"""
    layout: AirbyteSortOrder
    """Layout template used"""
    name: AirbyteSortOrder
    """Action name"""
    parent_action_id: AirbyteSortOrder
    """Parent action ID for language variants"""
    preheader_text: AirbyteSortOrder
    """Email preheader/preview text"""
    preprocessor: AirbyteSortOrder
    """CSS preprocessor setting"""
    recipient: AirbyteSortOrder
    """Recipient address"""
    recipient_environment_id: AirbyteSortOrder
    """Recipient environment ID"""
    reply_to: AirbyteSortOrder
    """Reply-to address"""
    reply_to_id: AirbyteSortOrder
    """Reply-to sender identity ID"""
    request_method: AirbyteSortOrder
    """HTTP request method for webhook actions"""
    sending_state: AirbyteSortOrder
    """Sending behavior (automatic or draft)"""
    subject: AirbyteSortOrder
    """Email subject line"""
    type_: AirbyteSortOrder
    """Action type (email, webhook, twilio, push, slack, in_app, whatsapp)"""
    updated: AirbyteSortOrder
    """Last update timestamp (Unix)"""
    url: AirbyteSortOrder
    """Webhook URL (for webhook actions)"""


# Entity-specific condition types for campaign_actions
class CampaignActionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignActionsSearchFilter


class CampaignActionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignActionsSearchFilter


class CampaignActionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignActionsSearchFilter


class CampaignActionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignActionsSearchFilter


class CampaignActionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignActionsSearchFilter


class CampaignActionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignActionsSearchFilter


class CampaignActionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignActionsStringFilter


class CampaignActionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignActionsStringFilter


class CampaignActionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignActionsStringFilter


class CampaignActionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignActionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignActionsInCondition = TypedDict("CampaignActionsInCondition", {"in": CampaignActionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignActionsNotCondition = TypedDict("CampaignActionsNotCondition", {"not": "CampaignActionsCondition"}, total=False)
"""Negates the nested condition."""

CampaignActionsAndCondition = TypedDict("CampaignActionsAndCondition", {"and": "list[CampaignActionsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignActionsOrCondition = TypedDict("CampaignActionsOrCondition", {"or": "list[CampaignActionsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignActionsAnyCondition = TypedDict("CampaignActionsAnyCondition", {"any": CampaignActionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaign_actions condition types
CampaignActionsCondition = (
    CampaignActionsEqCondition
    | CampaignActionsNeqCondition
    | CampaignActionsGtCondition
    | CampaignActionsGteCondition
    | CampaignActionsLtCondition
    | CampaignActionsLteCondition
    | CampaignActionsInCondition
    | CampaignActionsLikeCondition
    | CampaignActionsFuzzyCondition
    | CampaignActionsKeywordCondition
    | CampaignActionsContainsCondition
    | CampaignActionsNotCondition
    | CampaignActionsAndCondition
    | CampaignActionsOrCondition
    | CampaignActionsAnyCondition
)


class CampaignActionsSearchQuery(TypedDict, total=False):
    """Search query for campaign_actions entity."""
    filter: CampaignActionsCondition
    sort: list[CampaignActionsSortFilter]


# ===== NEWSLETTERS SEARCH TYPES =====

class NewslettersSearchFilter(TypedDict, total=False):
    """Available fields for filtering newsletters search queries."""
    content_ids: list[Any] | None
    """Content variant IDs for this newsletter"""
    created: int | None
    """Creation timestamp (Unix)"""
    deduplicate_id: str | None
    """Deduplication identifier"""
    id: int | None
    """Unique newsletter identifier"""
    name: str | None
    """Newsletter name"""
    sent_at: int | None
    """When the newsletter was last sent (Unix)"""
    tags: list[Any] | None
    """Tags associated with the newsletter"""
    type_: str | None
    """Channel type (email, webhook, twilio, push, in_app, inbox)"""
    updated: int | None
    """Last update timestamp (Unix)"""


class NewslettersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    content_ids: list[list[Any]]
    """Content variant IDs for this newsletter"""
    created: list[int]
    """Creation timestamp (Unix)"""
    deduplicate_id: list[str]
    """Deduplication identifier"""
    id: list[int]
    """Unique newsletter identifier"""
    name: list[str]
    """Newsletter name"""
    sent_at: list[int]
    """When the newsletter was last sent (Unix)"""
    tags: list[list[Any]]
    """Tags associated with the newsletter"""
    type_: list[str]
    """Channel type (email, webhook, twilio, push, in_app, inbox)"""
    updated: list[int]
    """Last update timestamp (Unix)"""


class NewslettersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    content_ids: Any
    """Content variant IDs for this newsletter"""
    created: Any
    """Creation timestamp (Unix)"""
    deduplicate_id: Any
    """Deduplication identifier"""
    id: Any
    """Unique newsletter identifier"""
    name: Any
    """Newsletter name"""
    sent_at: Any
    """When the newsletter was last sent (Unix)"""
    tags: Any
    """Tags associated with the newsletter"""
    type_: Any
    """Channel type (email, webhook, twilio, push, in_app, inbox)"""
    updated: Any
    """Last update timestamp (Unix)"""


class NewslettersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    content_ids: str
    """Content variant IDs for this newsletter"""
    created: str
    """Creation timestamp (Unix)"""
    deduplicate_id: str
    """Deduplication identifier"""
    id: str
    """Unique newsletter identifier"""
    name: str
    """Newsletter name"""
    sent_at: str
    """When the newsletter was last sent (Unix)"""
    tags: str
    """Tags associated with the newsletter"""
    type_: str
    """Channel type (email, webhook, twilio, push, in_app, inbox)"""
    updated: str
    """Last update timestamp (Unix)"""


class NewslettersSortFilter(TypedDict, total=False):
    """Available fields for sorting newsletters search results."""
    content_ids: AirbyteSortOrder
    """Content variant IDs for this newsletter"""
    created: AirbyteSortOrder
    """Creation timestamp (Unix)"""
    deduplicate_id: AirbyteSortOrder
    """Deduplication identifier"""
    id: AirbyteSortOrder
    """Unique newsletter identifier"""
    name: AirbyteSortOrder
    """Newsletter name"""
    sent_at: AirbyteSortOrder
    """When the newsletter was last sent (Unix)"""
    tags: AirbyteSortOrder
    """Tags associated with the newsletter"""
    type_: AirbyteSortOrder
    """Channel type (email, webhook, twilio, push, in_app, inbox)"""
    updated: AirbyteSortOrder
    """Last update timestamp (Unix)"""


# Entity-specific condition types for newsletters
class NewslettersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: NewslettersSearchFilter


class NewslettersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: NewslettersSearchFilter


class NewslettersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: NewslettersSearchFilter


class NewslettersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: NewslettersSearchFilter


class NewslettersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: NewslettersSearchFilter


class NewslettersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: NewslettersSearchFilter


class NewslettersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: NewslettersStringFilter


class NewslettersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: NewslettersStringFilter


class NewslettersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: NewslettersStringFilter


class NewslettersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: NewslettersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
NewslettersInCondition = TypedDict("NewslettersInCondition", {"in": NewslettersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

NewslettersNotCondition = TypedDict("NewslettersNotCondition", {"not": "NewslettersCondition"}, total=False)
"""Negates the nested condition."""

NewslettersAndCondition = TypedDict("NewslettersAndCondition", {"and": "list[NewslettersCondition]"}, total=False)
"""True if all nested conditions are true."""

NewslettersOrCondition = TypedDict("NewslettersOrCondition", {"or": "list[NewslettersCondition]"}, total=False)
"""True if any nested condition is true."""

NewslettersAnyCondition = TypedDict("NewslettersAnyCondition", {"any": NewslettersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all newsletters condition types
NewslettersCondition = (
    NewslettersEqCondition
    | NewslettersNeqCondition
    | NewslettersGtCondition
    | NewslettersGteCondition
    | NewslettersLtCondition
    | NewslettersLteCondition
    | NewslettersInCondition
    | NewslettersLikeCondition
    | NewslettersFuzzyCondition
    | NewslettersKeywordCondition
    | NewslettersContainsCondition
    | NewslettersNotCondition
    | NewslettersAndCondition
    | NewslettersOrCondition
    | NewslettersAnyCondition
)


class NewslettersSearchQuery(TypedDict, total=False):
    """Search query for newsletters entity."""
    filter: NewslettersCondition
    sort: list[NewslettersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
