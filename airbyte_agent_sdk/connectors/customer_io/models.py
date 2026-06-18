"""
Pydantic models for customer-io connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class CustomerIoAuthConfig(BaseModel):
    """App API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    app_api_key: str
    """Your Customer.io App API key. Generate one in your workspace settings at Settings > API Credentials > App API Key.
"""

# Replication configuration

class CustomerIoReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Customer.io."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Campaign(BaseModel):
    """Campaign type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    state: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    created: int | None = Field(default=None)
    updated: int | None = Field(default=None)
    first_started: int | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    actions: list[dict[str, Any]] | None = Field(default=None)
    msg_templates: list[dict[str, Any]] | None = Field(default=None)
    trigger_segment_ids: list[int] | None = Field(default=None)
    filter_segment_ids: list[int] | None = Field(default=None)
    frequency: str | None = Field(default=None)
    event_name: str | None = Field(default=None)
    date_attribute: str | None = Field(default=None)
    start_hour: int | None = Field(default=None)
    start_minutes: int | None = Field(default=None)
    timezone: str | None = Field(default=None)
    use_customer_timezone: bool | None = Field(default=None)
    created_by: str | None = Field(default=None)
    scheduled_start: int | None = Field(default=None)
    scheduled_start_should_backfill: bool | None = Field(default=None)
    scheduled_stop: int | None = Field(default=None)
    scheduled_stop_should_sunset: bool | None = Field(default=None)

class CampaignAction(BaseModel):
    """CampaignAction type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Any | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    campaign_id: int | None = Field(default=None)
    created: int | None = Field(default=None)
    updated: int | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    body: str | None = Field(default=None)
    layout: str | None = Field(default=None)
    from_: str | None = Field(default=None, alias="from")
    from_id: int | None = Field(default=None)
    subject: str | None = Field(default=None)
    preheader_text: str | None = Field(default=None)
    recipient: str | None = Field(default=None)
    reply_to: str | None = Field(default=None)
    reply_to_id: int | None = Field(default=None)
    bcc: str | None = Field(default=None)
    fake_bcc: bool | None = Field(default=None)
    headers: str | None = Field(default=None)
    sending_state: str | None = Field(default=None)
    language: str | None = Field(default=None)
    parent_action_id: int | None = Field(default=None)
    preprocessor: str | None = Field(default=None)
    body_amp: str | None = Field(default=None)
    broadcast_id: int | None = Field(default=None)
    editor: str | None = Field(default=None)
    url: str | None = Field(default=None)
    body_plain: str | None = Field(default=None)

class Newsletter(BaseModel):
    """Newsletter type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    created: int | None = Field(default=None)
    updated: int | None = Field(default=None)
    sent_at: int | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    content_ids: list[int] | None = Field(default=None)
    recipient_segment_ids: list[int] | None = Field(default=None)
    subscription_topic_id: int | None = Field(default=None)

class Segment(BaseModel):
    """Segment type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    state: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    progress: int | None = Field(default=None)
    conditions: dict[str, Any] | None = Field(default=None)

class MessageCustomerIdentifiers(BaseModel):
    """Customer identification details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="Person's ID")
    """Person's ID"""
    cio_id: str | None | None = Field(default=None, description="Customer.io internal ID")
    """Customer.io internal ID"""
    email: str | None | None = Field(default=None, description="Person's email address")
    """Person's email address"""

class MessageMetrics(BaseModel):
    """Delivery metrics timestamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: int | None | None = Field(default=None)
    drafted: int | None | None = Field(default=None)
    sent: int | None | None = Field(default=None)
    delivered: int | None | None = Field(default=None)
    opened: int | None | None = Field(default=None)
    clicked: int | None | None = Field(default=None)
    converted: int | None | None = Field(default=None)
    bounced: int | None | None = Field(default=None)
    failed: int | None | None = Field(default=None)
    undeliverable: int | None | None = Field(default=None)

class Message(BaseModel):
    """Message type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    created: int | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    customer_id: str | None = Field(default=None)
    customer_identifiers: MessageCustomerIdentifiers | None = Field(default=None)
    campaign_id: int | None = Field(default=None)
    newsletter_id: int | None = Field(default=None)
    broadcast_id: int | None = Field(default=None)
    content_id: int | None = Field(default=None)
    action_id: int | None = Field(default=None)
    parent_action_id: int | None = Field(default=None)
    message_template_id: int | None = Field(default=None)
    recipient: str | None = Field(default=None)
    subject: str | None = Field(default=None)
    forgotten: bool | None = Field(default=None)
    failure_message: str | None = Field(default=None)
    trigger_event_id: str | None = Field(default=None)
    metrics: MessageMetrics | None = Field(default=None)

class ActivityCustomerIdentifiers(BaseModel):
    """Customer identification details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    cio_id: str | None | None = Field(default=None)
    email: str | None | None = Field(default=None)

class Activity(BaseModel):
    """Activity type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    timestamp: int | None = Field(default=None)
    customer_id: str | None = Field(default=None)
    customer_identifiers: ActivityCustomerIdentifiers | None = Field(default=None)
    delivery_id: str | None = Field(default=None)
    delivery_type: str | None = Field(default=None)
    data: dict[str, Any] | None = Field(default=None)

class SenderIdentity(BaseModel):
    """SenderIdentity type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    address: str | None = Field(default=None)
    template_type: str | None = Field(default=None)
    auto_generated: bool | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    phone: str | None = Field(default=None)

class Snippet(BaseModel):
    """Snippet type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    value: str | None = Field(default=None)
    updated_at: int | None = Field(default=None)

class Collection(BaseModel):
    """Collection type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    bytes: int | None = Field(default=None)
    rows: int | None = Field(default=None)
    schema_: list[str] | None = Field(default=None, alias="schema")
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)

class ReportingWebhook(BaseModel):
    """ReportingWebhook type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    endpoint: str | None = Field(default=None)
    disabled: bool | None = Field(default=None)
    full_resolution: bool | None = Field(default=None)
    with_content: bool | None = Field(default=None)
    events: list[str] | None = Field(default=None)

class Export(BaseModel):
    """Export type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    status: str | None = Field(default=None)
    description: str | None = Field(default=None)
    total: int | None = Field(default=None)
    downloads: int | None = Field(default=None)
    failed: bool | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    deduplicate_id: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    user_email: str | None = Field(default=None)

class SnippetCreateParams(BaseModel):
    """SnippetCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str

class SnippetUpdateParams(BaseModel):
    """SnippetUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str

class CollectionCreateParams(BaseModel):
    """CollectionCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    data: list[dict[str, Any]] | None = Field(default=None)
    url: str | None = Field(default=None)

class CollectionUpdateParams(BaseModel):
    """CollectionUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    data: list[dict[str, Any]] | None = Field(default=None)
    url: str | None = Field(default=None)

class ReportingWebhookCreateParams(BaseModel):
    """ReportingWebhookCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    endpoint: str
    events: list[str]
    disabled: bool | None = Field(default=None)
    full_resolution: bool | None = Field(default=None)
    with_content: bool | None = Field(default=None)

class ReportingWebhookUpdateParams(BaseModel):
    """ReportingWebhookUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    endpoint: str
    events: list[str]
    disabled: bool | None = Field(default=None)
    full_resolution: bool | None = Field(default=None)
    with_content: bool | None = Field(default=None)

class SegmentCreateParamsSegment(BaseModel):
    """Nested schema for SegmentCreateParams.segment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Name of the manual segment")
    """Name of the manual segment"""
    description: str | None = Field(default=None, description="Optional description of the segment")
    """Optional description of the segment"""

class SegmentCreateParams(BaseModel):
    """SegmentCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    segment: SegmentCreateParamsSegment

class ExportCreateParams(BaseModel):
    """ExportCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    filters: dict[str, Any]

class TransactionalMessage(BaseModel):
    """TransactionalMessage type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    send_to_unsubscribed: bool | None = Field(default=None)
    link_tracking: bool | None = Field(default=None)
    open_tracking: bool | None = Field(default=None)
    hide_message_body: bool | None = Field(default=None)
    queue_drafts: bool | None = Field(default=None)
    trigger_name: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)

class TransactionalMessageContent(BaseModel):
    """TransactionalMessageContent type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    created: int | None = Field(default=None)
    updated: int | None = Field(default=None)
    body: str | None = Field(default=None)
    language: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    from_: str | None = Field(default=None, alias="from")
    from_id: int | None = Field(default=None)
    reply_to: str | None = Field(default=None)
    reply_to_id: int | None = Field(default=None)
    preprocessor: str | None = Field(default=None)
    recipient: str | None = Field(default=None)
    subject: str | None = Field(default=None)
    bcc: str | None = Field(default=None)
    fake_bcc: bool | None = Field(default=None)
    preheader_text: str | None = Field(default=None)
    body_amp: str | None = Field(default=None)
    headers: str | None = Field(default=None)

class TransactionalMessageContentUpdateParamsHeadersItem(BaseModel):
    """Nested schema for TransactionalMessageContentUpdateParams.headers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Header name")
    """Header name"""
    value: str | None = Field(default=None, description="Header value")
    """Header value"""

class TransactionalMessageContentUpdateParams(BaseModel):
    """TransactionalMessageContentUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = Field(default=None)
    from_id: int | None = Field(default=None)
    reply_to_id: int | None = Field(default=None)
    recipient: str | None = Field(default=None)
    subject: str | None = Field(default=None)
    preheader_text: str | None = Field(default=None)
    body_amp: str | None = Field(default=None)
    headers: list[TransactionalMessageContentUpdateParamsHeadersItem] | None = Field(default=None)

class TransactionalSendResponse(BaseModel):
    """TransactionalSendResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    delivery_id: str | None = Field(default=None)
    queued_at: int | None = Field(default=None)

class TransactionalEmailParams(BaseModel):
    """TransactionalEmailParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactional_message_id: Any | None = Field(default=None)
    to: str
    identifiers: dict[str, Any]
    message_data: dict[str, Any] | None = Field(default=None)
    from_: str | None = Field(default=None, alias="from")
    subject: str | None = Field(default=None)
    body: str | None = Field(default=None)
    body_plain: str | None = Field(default=None)
    reply_to: str | None = Field(default=None)
    bcc: str | None = Field(default=None)
    headers: dict[str, Any] | None = Field(default=None)
    preheader_text: str | None = Field(default=None)
    attachments: dict[str, Any] | None = Field(default=None)
    disable_message_retention: bool | None = Field(default=None)
    send_to_unsubscribed: bool | None = Field(default=None)
    tracked: bool | None = Field(default=None)
    queue_draft: bool | None = Field(default=None)
    send_at: int | None = Field(default=None)

class TransactionalSmsParams(BaseModel):
    """TransactionalSmsParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactional_message_id: Any
    to: str
    identifiers: dict[str, Any]
    message_data: dict[str, Any] | None = Field(default=None)
    from_: str | None = Field(default=None, alias="from")
    send_to_unsubscribed: bool | None = Field(default=None)
    tracked: bool | None = Field(default=None)
    queue_draft: bool | None = Field(default=None)
    disable_message_retention: bool | None = Field(default=None)

class TransactionalPushParams(BaseModel):
    """TransactionalPushParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactional_message_id: Any | None = Field(default=None)
    to: str | None = Field(default=None)
    identifiers: dict[str, Any]
    message_data: dict[str, Any] | None = Field(default=None)
    title: str | None = Field(default=None)
    message: str | None = Field(default=None)
    link: str | None = Field(default=None)
    image_url: str | None = Field(default=None)
    custom_data: dict[str, Any] | None = Field(default=None)
    custom_payload: dict[str, Any] | None = Field(default=None)
    sound: str | None = Field(default=None)
    send_to_unsubscribed: bool | None = Field(default=None)
    queue_draft: bool | None = Field(default=None)
    disable_message_retention: bool | None = Field(default=None)
    send_at: int | None = Field(default=None)

class TransactionalInboxMessageParams(BaseModel):
    """TransactionalInboxMessageParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactional_message_id: Any
    identifiers: dict[str, Any]
    message_data: dict[str, Any] | None = Field(default=None)

class BroadcastTriggerParams(BaseModel):
    """BroadcastTriggerParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: dict[str, Any] | None = Field(default=None)
    recipients: dict[str, Any] | None = Field(default=None)
    ids: list[str] | None = Field(default=None)
    emails: list[str] | None = Field(default=None)
    per_user_data: list[dict[str, Any]] | None = Field(default=None)
    data_file_url: str | None = Field(default=None)
    id_ignore_missing: bool | None = Field(default=None)
    email_ignore_missing: bool | None = Field(default=None)
    email_add_duplicates: bool | None = Field(default=None)

class BroadcastTriggerResponse(BaseModel):
    """BroadcastTriggerResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CampaignActionsListResultMeta(BaseModel):
    """Metadata for campaign_actions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class NewslettersListResultMeta(BaseModel):
    """Metadata for newsletters.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class ActivitiesListResultMeta(BaseModel):
    """Metadata for activities.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SenderIdentitiesListResultMeta(BaseModel):
    """Metadata for sender_identities.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class CustomerIoCheckResult(BaseModel):
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


class CustomerIoExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class CustomerIoExecuteResultWithMeta(CustomerIoExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    actions: list[Any] | None = None
    """Actions defined in this campaign"""
    active: bool | None = None
    """Whether the campaign is active"""
    created: int | None = None
    """Creation timestamp (Unix)"""
    created_by: str | None = None
    """Who created the campaign"""
    date_attribute: str | None = None
    """Date attribute used for date-triggered campaigns"""
    deduplicate_id: str | None = None
    """Deduplication identifier"""
    event_name: str | None = None
    """Event name that triggers the campaign"""
    first_started: int | None = None
    """When the campaign was first started (Unix)"""
    frequency: str | None = None
    """How frequently a person can receive this campaign"""
    id: int | None = None
    """Unique campaign identifier"""
    msg_templates: list[Any] | None = None
    """Message templates used in the campaign"""
    name: str | None = None
    """Campaign name"""
    start_hour: int | None = None
    """Hour of the day to trigger"""
    start_minutes: int | None = None
    """Minute of the hour to trigger"""
    state: str | None = None
    """Campaign status (draft, active, stopped)"""
    tags: list[Any] | None = None
    """Tags associated with the campaign"""
    timezone: str | None = None
    """Timezone for trigger scheduling"""
    trigger_segment_ids: list[Any] | None = None
    """Segment IDs that trigger this campaign"""
    type_: str | None = None
    """Campaign trigger type"""
    updated: int | None = None
    """Last update timestamp (Unix)"""
    use_customer_timezone: bool | None = None
    """Whether to use the customer's timezone"""


class CampaignActionsSearchData(BaseModel):
    """Search result data for campaign_actions entity."""
    model_config = ConfigDict(extra="allow")

    bcc: str | None = None
    """BCC addresses"""
    body: str | None = None
    """Action body content (HTML for emails)"""
    campaign_id: int | None = None
    """Parent campaign ID"""
    created: int | None = None
    """Creation timestamp (Unix)"""
    deduplicate_id: str | None = None
    """Deduplication identifier"""
    editor: str | None = None
    """Editor used to create the action"""
    fake_bcc: bool | None = None
    """Whether to use fake BCC"""
    from_: str | None = None
    """From address"""
    from_id: str | None = None
    """Sender identity ID"""
    headers: str | None = None
    """Custom email headers as JSON"""
    id: str | None = None
    """Unique action identifier"""
    language: str | None = None
    """Language variant"""
    layout: str | None = None
    """Layout template used"""
    name: str | None = None
    """Action name"""
    parent_action_id: int | None = None
    """Parent action ID for language variants"""
    preheader_text: str | None = None
    """Email preheader/preview text"""
    preprocessor: str | None = None
    """CSS preprocessor setting"""
    recipient: str | None = None
    """Recipient address"""
    recipient_environment_id: int | None = None
    """Recipient environment ID"""
    reply_to: str | None = None
    """Reply-to address"""
    reply_to_id: str | None = None
    """Reply-to sender identity ID"""
    request_method: str | None = None
    """HTTP request method for webhook actions"""
    sending_state: str | None = None
    """Sending behavior (automatic or draft)"""
    subject: str | None = None
    """Email subject line"""
    type_: str | None = None
    """Action type (email, webhook, twilio, push, slack, in_app, whatsapp)"""
    updated: int | None = None
    """Last update timestamp (Unix)"""
    url: str | None = None
    """Webhook URL (for webhook actions)"""


class NewslettersSearchData(BaseModel):
    """Search result data for newsletters entity."""
    model_config = ConfigDict(extra="allow")

    content_ids: list[Any] | None = None
    """Content variant IDs for this newsletter"""
    created: int | None = None
    """Creation timestamp (Unix)"""
    deduplicate_id: str | None = None
    """Deduplication identifier"""
    id: int | None = None
    """Unique newsletter identifier"""
    name: str | None = None
    """Newsletter name"""
    sent_at: int | None = None
    """When the newsletter was last sent (Unix)"""
    tags: list[Any] | None = None
    """Tags associated with the newsletter"""
    type_: str | None = None
    """Channel type (email, webhook, twilio, push, in_app, inbox)"""
    updated: int | None = None
    """Last update timestamp (Unix)"""


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

CampaignActionsSearchResult = AirbyteSearchResult[CampaignActionsSearchData]
"""Search result type for campaign_actions entity."""

NewslettersSearchResult = AirbyteSearchResult[NewslettersSearchData]
"""Search result type for newsletters entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CampaignsListResult = CustomerIoExecuteResult[list[Campaign]]
"""Result type for campaigns.list operation."""

CampaignActionsListResult = CustomerIoExecuteResultWithMeta[list[CampaignAction], CampaignActionsListResultMeta]
"""Result type for campaign_actions.list operation with data and metadata."""

NewslettersListResult = CustomerIoExecuteResultWithMeta[list[Newsletter], NewslettersListResultMeta]
"""Result type for newsletters.list operation with data and metadata."""

SegmentsListResult = CustomerIoExecuteResult[list[Segment]]
"""Result type for segments.list operation."""

MessagesListResult = CustomerIoExecuteResultWithMeta[list[Message], MessagesListResultMeta]
"""Result type for messages.list operation with data and metadata."""

ActivitiesListResult = CustomerIoExecuteResultWithMeta[list[Activity], ActivitiesListResultMeta]
"""Result type for activities.list operation with data and metadata."""

SenderIdentitiesListResult = CustomerIoExecuteResultWithMeta[list[SenderIdentity], SenderIdentitiesListResultMeta]
"""Result type for sender_identities.list operation with data and metadata."""

SnippetsListResult = CustomerIoExecuteResult[list[Snippet]]
"""Result type for snippets.list operation."""

CollectionsListResult = CustomerIoExecuteResult[list[Collection]]
"""Result type for collections.list operation."""

ReportingWebhooksListResult = CustomerIoExecuteResult[list[ReportingWebhook]]
"""Result type for reporting_webhooks.list operation."""

ExportsListResult = CustomerIoExecuteResult[list[Export]]
"""Result type for exports.list operation."""

TransactionalMessagesListResult = CustomerIoExecuteResult[list[TransactionalMessage]]
"""Result type for transactional_messages.list operation."""

TransactionalMessageContentsListResult = CustomerIoExecuteResult[list[TransactionalMessageContent]]
"""Result type for transactional_message_contents.list operation."""

