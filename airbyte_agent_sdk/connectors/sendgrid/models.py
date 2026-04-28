"""
Pydantic models for sendgrid connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class SendgridAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your SendGrid API key (generated at https://app.sendgrid.com/settings/api_keys)"""

# Replication configuration

class SendgridReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from SendGrid."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Contact(BaseModel):
    """A SendGrid marketing contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    email: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    unique_name: str | None = Field(default=None)
    alternate_emails: list[str] | None = Field(default=None)
    address_line_1: str | None = Field(default=None)
    address_line_2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    state_province_region: str | None = Field(default=None)
    country: str | None = Field(default=None)
    postal_code: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    whatsapp: str | None = Field(default=None)
    line: str | None = Field(default=None)
    facebook: str | None = Field(default=None)
    list_ids: list[str] | None = Field(default=None)
    segment_ids: list[str] | None = Field(default=None)
    custom_fields: dict[str, Any] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class ContactsListMetadata(BaseModel):
    """Nested schema for ContactsList._metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None | None = Field(default=None)

class ContactsList(BaseModel):
    """Response containing a list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    result: list[Contact] | None = Field(default=None)
    contact_count: int | None = Field(default=None)
    metadata: ContactsListMetadata | None = Field(default=None, alias="_metadata")

class ListMetadata(BaseModel):
    """Metadata about the list resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None)

class List(BaseModel):
    """A SendGrid marketing list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    contact_count: int | None = Field(default=None)
    metadata: ListMetadata | None = Field(default=None, alias="_metadata")

class ListsListMetadata(BaseModel):
    """Nested schema for ListsList._metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None | None = Field(default=None)

class ListsList(BaseModel):
    """Response containing a list of marketing lists"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    result: list[List] | None = Field(default=None)
    metadata: ListsListMetadata | None = Field(default=None, alias="_metadata")

class SegmentStatus(BaseModel):
    """Segment status details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    query_validation: str | None = Field(default=None)

class Segment(BaseModel):
    """A SendGrid marketing segment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    contacts_count: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    sample_updated_at: str | None = Field(default=None)
    next_sample_update: str | None = Field(default=None)
    parent_list_ids: list[str | None] | None = Field(default=None)
    query_version: str | None = Field(default=None)
    status: SegmentStatus | None = Field(default=None)

class SegmentsList(BaseModel):
    """Response containing a list of segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Segment] | None = Field(default=None)

class Campaign(BaseModel):
    """A SendGrid marketing campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    channels: list[str] | None = Field(default=None)
    is_abtest: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class CampaignsListMetadata(BaseModel):
    """Nested schema for CampaignsList._metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None | None = Field(default=None)

class CampaignsList(BaseModel):
    """Response containing a list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    result: list[Campaign] | None = Field(default=None)
    metadata: CampaignsListMetadata | None = Field(default=None, alias="_metadata")

class SingleSendEmailConfig(BaseModel):
    """Email configuration details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subject: str | None | None = Field(default=None)
    html_content: str | None | None = Field(default=None)
    plain_content: str | None | None = Field(default=None)
    generate_plain_content: bool | None = Field(default=None)
    design_id: str | None | None = Field(default=None)
    editor: str | None | None = Field(default=None)
    suppression_group_id: int | None | None = Field(default=None)
    custom_unsubscribe_url: str | None | None = Field(default=None)
    sender_id: int | None | None = Field(default=None)
    ip_pool: str | None | None = Field(default=None)

class SingleSendSendTo(BaseModel):
    """Recipients configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_ids: list[str] | None | None = Field(default=None)
    segment_ids: list[str] | None | None = Field(default=None)
    all: bool | None = Field(default=None)

class SingleSend(BaseModel):
    """A SendGrid single send"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    categories: list[str] | None = Field(default=None)
    send_at: str | None = Field(default=None)
    send_to: SingleSendSendTo | None = Field(default=None)
    email_config: SingleSendEmailConfig | None = Field(default=None)
    is_abtest: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class SingleSendsListMetadata(BaseModel):
    """Nested schema for SingleSendsList._metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None | None = Field(default=None)

class SingleSendsList(BaseModel):
    """Response containing a list of single sends"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    result: list[SingleSend] | None = Field(default=None)
    metadata: SingleSendsListMetadata | None = Field(default=None, alias="_metadata")

class Template(BaseModel):
    """A SendGrid transactional template"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    generation: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    versions: list[Any] | None = Field(default=None)

class TemplatesListMetadata(BaseModel):
    """Nested schema for TemplatesList._metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None | None = Field(default=None)

class TemplatesList(BaseModel):
    """Response containing a list of templates"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    templates: list[Template] | None = Field(default=None)
    metadata: TemplatesListMetadata | None = Field(default=None, alias="_metadata")

class SingleSendStatsStats(BaseModel):
    """Email statistics for the single send"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bounce_drops: int | None = Field(default=None)
    bounces: int | None = Field(default=None)
    clicks: int | None = Field(default=None)
    delivered: int | None = Field(default=None)
    invalid_emails: int | None = Field(default=None)
    opens: int | None = Field(default=None)
    requests: int | None = Field(default=None)
    spam_report_drops: int | None = Field(default=None)
    spam_reports: int | None = Field(default=None)
    unique_clicks: int | None = Field(default=None)
    unique_opens: int | None = Field(default=None)
    unsubscribes: int | None = Field(default=None)

class SingleSendStats(BaseModel):
    """Stats for a single send"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    ab_phase: str | None = Field(default=None)
    ab_variation: str | None = Field(default=None)
    aggregation: str | None = Field(default=None)
    stats: SingleSendStatsStats | None = Field(default=None)

class SingleSendStatsListMetadata(BaseModel):
    """Nested schema for SingleSendStatsList._metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None | None = Field(default=None)

class SingleSendStatsList(BaseModel):
    """Response containing a list of single send stats"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[SingleSendStats] | None = Field(default=None)
    metadata: SingleSendStatsListMetadata | None = Field(default=None, alias="_metadata")

class Bounce(BaseModel):
    """A bounced email record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: int | None = Field(default=None)
    email: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str | None = Field(default=None)

class Block(BaseModel):
    """A blocked email record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: int | None = Field(default=None)
    email: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    status: str | None = Field(default=None)

class SpamReport(BaseModel):
    """A spam report record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: int | None = Field(default=None)
    email: str | None = Field(default=None)
    ip: str | None = Field(default=None)

class InvalidEmail(BaseModel):
    """An invalid email record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: int | None = Field(default=None)
    email: str | None = Field(default=None)
    reason: str | None = Field(default=None)

class GlobalSuppression(BaseModel):
    """A globally suppressed email address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: int | None = Field(default=None)
    email: str | None = Field(default=None)

class SuppressionGroup(BaseModel):
    """A suppression (unsubscribe) group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    is_default: bool | None = Field(default=None)
    unsubscribes: int | None = Field(default=None)

class SuppressionGroupMember(BaseModel):
    """A member of a suppression group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None)
    group_id: int | None = Field(default=None)
    group_name: str | None = Field(default=None)
    created_at: int | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)
    contact_count: int | None = Field(default=None)

class ListsListResultMeta(BaseModel):
    """Metadata for lists.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SinglesendsListResultMeta(BaseModel):
    """Metadata for singlesends.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class TemplatesListResultMeta(BaseModel):
    """Metadata for templates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SinglesendStatsListResultMeta(BaseModel):
    """Metadata for singlesend_stats.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class BouncesListResultMeta(BaseModel):
    """Metadata for bounces.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class BlocksListResultMeta(BaseModel):
    """Metadata for blocks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SpamReportsListResultMeta(BaseModel):
    """Metadata for spam_reports.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class InvalidEmailsListResultMeta(BaseModel):
    """Metadata for invalid_emails.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class GlobalSuppressionsListResultMeta(BaseModel):
    """Metadata for global_suppressions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SuppressionGroupMembersListResultMeta(BaseModel):
    """Metadata for suppression_group_members.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class SendgridCheckResult(BaseModel):
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


class SendgridExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class SendgridExecuteResultWithMeta(SendgridExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class BouncesSearchData(BaseModel):
    """Search result data for bounces entity."""
    model_config = ConfigDict(extra="allow")

    created: int | None = None
    """Unix timestamp when the bounce occurred"""
    email: str | None = None
    """The email address that bounced"""
    reason: str | None = None
    """The reason for the bounce"""
    status: str | None = None
    """The enhanced status code for the bounce"""


class BlocksSearchData(BaseModel):
    """Search result data for blocks entity."""
    model_config = ConfigDict(extra="allow")

    created: int | None = None
    """Unix timestamp when the block occurred"""
    email: str | None = None
    """The blocked email address"""
    reason: str | None = None
    """The reason for the block"""
    status: str | None = None
    """The status code for the block"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    channels: list[Any] | None = None
    """Channels for this campaign"""
    created_at: str | None = None
    """When the campaign was created"""
    id: str | None = None
    """Unique campaign identifier"""
    is_abtest: bool | None = None
    """Whether this campaign is an A/B test"""
    name: str | None = None
    """Campaign name"""
    status: str | None = None
    """Campaign status"""
    updated_at: str | None = None
    """When the campaign was last updated"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    address_line_1: str | None = None
    """Address line 1"""
    address_line_2: str | None = None
    """Address line 2"""
    alternate_emails: list[Any] | None = None
    """Alternate email addresses"""
    city: str | None = None
    """City"""
    contact_id: str | None = None
    """Unique contact identifier used by Airbyte"""
    country: str | None = None
    """Country"""
    created_at: str | None = None
    """When the contact was created"""
    custom_fields: dict[str, Any] | None = None
    """Custom field values"""
    email: str | None = None
    """Contact email address"""
    facebook: str | None = None
    """Facebook ID"""
    first_name: str | None = None
    """Contact first name"""
    last_name: str | None = None
    """Contact last name"""
    line: str | None = None
    """LINE ID"""
    list_ids: list[Any] | None = None
    """IDs of lists the contact belongs to"""
    phone_number: str | None = None
    """Phone number"""
    postal_code: str | None = None
    """Postal code"""
    state_province_region: str | None = None
    """State, province, or region"""
    unique_name: str | None = None
    """Unique name for the contact"""
    updated_at: str | None = None
    """When the contact was last updated"""
    whatsapp: str | None = None
    """WhatsApp number"""


class GlobalSuppressionsSearchData(BaseModel):
    """Search result data for global_suppressions entity."""
    model_config = ConfigDict(extra="allow")

    created: int | None = None
    """Unix timestamp when the global suppression was created"""
    email: str | None = None
    """The globally suppressed email address"""


class InvalidEmailsSearchData(BaseModel):
    """Search result data for invalid_emails entity."""
    model_config = ConfigDict(extra="allow")

    created: int | None = None
    """Unix timestamp when the invalid email was recorded"""
    email: str | None = None
    """The invalid email address"""
    reason: str | None = None
    """The reason the email is invalid"""


class ListsSearchData(BaseModel):
    """Search result data for lists entity."""
    model_config = ConfigDict(extra="allow")

    metadata: dict[str, Any] | None = None
    """Metadata about the list resource"""
    contact_count: int | None = None
    """Number of contacts in the list"""
    id: str | None = None
    """Unique list identifier"""
    name: str | None = None
    """Name of the list"""


class SegmentsSearchData(BaseModel):
    """Search result data for segments entity."""
    model_config = ConfigDict(extra="allow")

    contacts_count: int | None = None
    """Number of contacts in the segment"""
    created_at: str | None = None
    """When the segment was created"""
    id: str | None = None
    """Unique segment identifier"""
    name: str | None = None
    """Segment name"""
    next_sample_update: str | None = None
    """When the next sample update will occur"""
    parent_list_ids: list[Any] | None = None
    """IDs of parent lists"""
    query_version: str | None = None
    """Query version used"""
    sample_updated_at: str | None = None
    """When the sample was last updated"""
    status: dict[str, Any] | None = None
    """Segment status details"""
    updated_at: str | None = None
    """When the segment was last updated"""


class SinglesendStatsSearchData(BaseModel):
    """Search result data for singlesend_stats entity."""
    model_config = ConfigDict(extra="allow")

    ab_phase: str | None = None
    """The A/B test phase"""
    ab_variation: str | None = None
    """The A/B test variation"""
    aggregation: str | None = None
    """The aggregation type"""
    id: str | None = None
    """The single send ID"""
    stats: dict[str, Any] | None = None
    """Email statistics for the single send"""


class SinglesendsSearchData(BaseModel):
    """Search result data for singlesends entity."""
    model_config = ConfigDict(extra="allow")

    categories: list[Any] | None = None
    """Categories associated with this single send"""
    created_at: str | None = None
    """When the single send was created"""
    id: str | None = None
    """Unique single send identifier"""
    is_abtest: bool | None = None
    """Whether this is an A/B test"""
    name: str | None = None
    """Single send name"""
    send_at: str | None = None
    """Scheduled send time"""
    status: str | None = None
    """Current status: draft, scheduled, or triggered"""
    updated_at: str | None = None
    """When the single send was last updated"""


class SuppressionGroupMembersSearchData(BaseModel):
    """Search result data for suppression_group_members entity."""
    model_config = ConfigDict(extra="allow")

    created_at: int | None = None
    """Unix timestamp when the suppression was created"""
    email: str | None = None
    """The suppressed email address"""
    group_id: int | None = None
    """ID of the suppression group"""
    group_name: str | None = None
    """Name of the suppression group"""


class SuppressionGroupsSearchData(BaseModel):
    """Search result data for suppression_groups entity."""
    model_config = ConfigDict(extra="allow")

    description: str | None = None
    """Description of the suppression group"""
    id: int | None = None
    """Unique suppression group identifier"""
    is_default: bool | None = None
    """Whether this is the default suppression group"""
    name: str | None = None
    """Suppression group name"""
    unsubscribes: int | None = None
    """Number of unsubscribes in this group"""


class TemplatesSearchData(BaseModel):
    """Search result data for templates entity."""
    model_config = ConfigDict(extra="allow")

    generation: str | None = None
    """Template generation (legacy or dynamic)"""
    id: str | None = None
    """Unique template identifier"""
    name: str | None = None
    """Template name"""
    updated_at: str | None = None
    """When the template was last updated"""
    versions: list[Any] | None = None
    """Template versions"""


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

BouncesSearchResult = AirbyteSearchResult[BouncesSearchData]
"""Search result type for bounces entity."""

BlocksSearchResult = AirbyteSearchResult[BlocksSearchData]
"""Search result type for blocks entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

ContactsSearchResult = AirbyteSearchResult[ContactsSearchData]
"""Search result type for contacts entity."""

GlobalSuppressionsSearchResult = AirbyteSearchResult[GlobalSuppressionsSearchData]
"""Search result type for global_suppressions entity."""

InvalidEmailsSearchResult = AirbyteSearchResult[InvalidEmailsSearchData]
"""Search result type for invalid_emails entity."""

ListsSearchResult = AirbyteSearchResult[ListsSearchData]
"""Search result type for lists entity."""

SegmentsSearchResult = AirbyteSearchResult[SegmentsSearchData]
"""Search result type for segments entity."""

SinglesendStatsSearchResult = AirbyteSearchResult[SinglesendStatsSearchData]
"""Search result type for singlesend_stats entity."""

SinglesendsSearchResult = AirbyteSearchResult[SinglesendsSearchData]
"""Search result type for singlesends entity."""

SuppressionGroupMembersSearchResult = AirbyteSearchResult[SuppressionGroupMembersSearchData]
"""Search result type for suppression_group_members entity."""

SuppressionGroupsSearchResult = AirbyteSearchResult[SuppressionGroupsSearchData]
"""Search result type for suppression_groups entity."""

TemplatesSearchResult = AirbyteSearchResult[TemplatesSearchData]
"""Search result type for templates entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ContactsListResult = SendgridExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

ListsListResult = SendgridExecuteResultWithMeta[list[List], ListsListResultMeta]
"""Result type for lists.list operation with data and metadata."""

SegmentsListResult = SendgridExecuteResult[list[Segment]]
"""Result type for segments.list operation."""

CampaignsListResult = SendgridExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

SinglesendsListResult = SendgridExecuteResultWithMeta[list[SingleSend], SinglesendsListResultMeta]
"""Result type for singlesends.list operation with data and metadata."""

TemplatesListResult = SendgridExecuteResultWithMeta[list[Template], TemplatesListResultMeta]
"""Result type for templates.list operation with data and metadata."""

SinglesendStatsListResult = SendgridExecuteResultWithMeta[list[SingleSendStats], SinglesendStatsListResultMeta]
"""Result type for singlesend_stats.list operation with data and metadata."""

BouncesListResult = SendgridExecuteResultWithMeta[list[Bounce], BouncesListResultMeta]
"""Result type for bounces.list operation with data and metadata."""

BlocksListResult = SendgridExecuteResultWithMeta[list[Block], BlocksListResultMeta]
"""Result type for blocks.list operation with data and metadata."""

SpamReportsListResult = SendgridExecuteResultWithMeta[list[SpamReport], SpamReportsListResultMeta]
"""Result type for spam_reports.list operation with data and metadata."""

InvalidEmailsListResult = SendgridExecuteResultWithMeta[list[InvalidEmail], InvalidEmailsListResultMeta]
"""Result type for invalid_emails.list operation with data and metadata."""

GlobalSuppressionsListResult = SendgridExecuteResultWithMeta[list[GlobalSuppression], GlobalSuppressionsListResultMeta]
"""Result type for global_suppressions.list operation with data and metadata."""

SuppressionGroupsListResult = SendgridExecuteResult[list[SuppressionGroup]]
"""Result type for suppression_groups.list operation."""

SuppressionGroupMembersListResult = SendgridExecuteResultWithMeta[list[SuppressionGroupMember], SuppressionGroupMembersListResultMeta]
"""Result type for suppression_group_members.list operation with data and metadata."""

