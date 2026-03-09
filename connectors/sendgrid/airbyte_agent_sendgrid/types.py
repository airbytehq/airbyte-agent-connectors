"""
Type definitions for sendgrid connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    pass

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class ListsListParams(TypedDict):
    """Parameters for lists.list operation"""
    page_size: NotRequired[int]

class ListsGetParams(TypedDict):
    """Parameters for lists.get operation"""
    id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    pass

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    segment_id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    page_size: NotRequired[int]

class SinglesendsListParams(TypedDict):
    """Parameters for singlesends.list operation"""
    page_size: NotRequired[int]

class SinglesendsGetParams(TypedDict):
    """Parameters for singlesends.get operation"""
    id: str

class TemplatesListParams(TypedDict):
    """Parameters for templates.list operation"""
    generations: NotRequired[str]
    page_size: NotRequired[int]

class TemplatesGetParams(TypedDict):
    """Parameters for templates.get operation"""
    template_id: str

class SinglesendStatsListParams(TypedDict):
    """Parameters for singlesend_stats.list operation"""
    page_size: NotRequired[int]

class BouncesListParams(TypedDict):
    """Parameters for bounces.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[int]

class BlocksListParams(TypedDict):
    """Parameters for blocks.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[int]

class SpamReportsListParams(TypedDict):
    """Parameters for spam_reports.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[int]

class InvalidEmailsListParams(TypedDict):
    """Parameters for invalid_emails.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[int]

class GlobalSuppressionsListParams(TypedDict):
    """Parameters for global_suppressions.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[int]

class SuppressionGroupsListParams(TypedDict):
    """Parameters for suppression_groups.list operation"""
    pass

class SuppressionGroupsGetParams(TypedDict):
    """Parameters for suppression_groups.get operation"""
    group_id: str

class SuppressionGroupMembersListParams(TypedDict):
    """Parameters for suppression_group_members.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== BOUNCES SEARCH TYPES =====

class BouncesSearchFilter(TypedDict, total=False):
    """Available fields for filtering bounces search queries."""
    created: int | None
    """Unix timestamp when the bounce occurred"""
    email: str | None
    """The email address that bounced"""
    reason: str | None
    """The reason for the bounce"""
    status: str | None
    """The enhanced status code for the bounce"""


class BouncesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created: list[int]
    """Unix timestamp when the bounce occurred"""
    email: list[str]
    """The email address that bounced"""
    reason: list[str]
    """The reason for the bounce"""
    status: list[str]
    """The enhanced status code for the bounce"""


class BouncesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created: Any
    """Unix timestamp when the bounce occurred"""
    email: Any
    """The email address that bounced"""
    reason: Any
    """The reason for the bounce"""
    status: Any
    """The enhanced status code for the bounce"""


class BouncesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created: str
    """Unix timestamp when the bounce occurred"""
    email: str
    """The email address that bounced"""
    reason: str
    """The reason for the bounce"""
    status: str
    """The enhanced status code for the bounce"""


class BouncesSortFilter(TypedDict, total=False):
    """Available fields for sorting bounces search results."""
    created: AirbyteSortOrder
    """Unix timestamp when the bounce occurred"""
    email: AirbyteSortOrder
    """The email address that bounced"""
    reason: AirbyteSortOrder
    """The reason for the bounce"""
    status: AirbyteSortOrder
    """The enhanced status code for the bounce"""


# Entity-specific condition types for bounces
class BouncesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BouncesSearchFilter


class BouncesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BouncesSearchFilter


class BouncesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BouncesSearchFilter


class BouncesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BouncesSearchFilter


class BouncesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BouncesSearchFilter


class BouncesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BouncesSearchFilter


class BouncesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BouncesStringFilter


class BouncesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BouncesStringFilter


class BouncesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BouncesStringFilter


class BouncesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BouncesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BouncesInCondition = TypedDict("BouncesInCondition", {"in": BouncesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BouncesNotCondition = TypedDict("BouncesNotCondition", {"not": "BouncesCondition"}, total=False)
"""Negates the nested condition."""

BouncesAndCondition = TypedDict("BouncesAndCondition", {"and": "list[BouncesCondition]"}, total=False)
"""True if all nested conditions are true."""

BouncesOrCondition = TypedDict("BouncesOrCondition", {"or": "list[BouncesCondition]"}, total=False)
"""True if any nested condition is true."""

BouncesAnyCondition = TypedDict("BouncesAnyCondition", {"any": BouncesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all bounces condition types
BouncesCondition = (
    BouncesEqCondition
    | BouncesNeqCondition
    | BouncesGtCondition
    | BouncesGteCondition
    | BouncesLtCondition
    | BouncesLteCondition
    | BouncesInCondition
    | BouncesLikeCondition
    | BouncesFuzzyCondition
    | BouncesKeywordCondition
    | BouncesContainsCondition
    | BouncesNotCondition
    | BouncesAndCondition
    | BouncesOrCondition
    | BouncesAnyCondition
)


class BouncesSearchQuery(TypedDict, total=False):
    """Search query for bounces entity."""
    filter: BouncesCondition
    sort: list[BouncesSortFilter]


# ===== BLOCKS SEARCH TYPES =====

class BlocksSearchFilter(TypedDict, total=False):
    """Available fields for filtering blocks search queries."""
    created: int | None
    """Unix timestamp when the block occurred"""
    email: str | None
    """The blocked email address"""
    reason: str | None
    """The reason for the block"""
    status: str | None
    """The status code for the block"""


class BlocksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created: list[int]
    """Unix timestamp when the block occurred"""
    email: list[str]
    """The blocked email address"""
    reason: list[str]
    """The reason for the block"""
    status: list[str]
    """The status code for the block"""


class BlocksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created: Any
    """Unix timestamp when the block occurred"""
    email: Any
    """The blocked email address"""
    reason: Any
    """The reason for the block"""
    status: Any
    """The status code for the block"""


class BlocksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created: str
    """Unix timestamp when the block occurred"""
    email: str
    """The blocked email address"""
    reason: str
    """The reason for the block"""
    status: str
    """The status code for the block"""


class BlocksSortFilter(TypedDict, total=False):
    """Available fields for sorting blocks search results."""
    created: AirbyteSortOrder
    """Unix timestamp when the block occurred"""
    email: AirbyteSortOrder
    """The blocked email address"""
    reason: AirbyteSortOrder
    """The reason for the block"""
    status: AirbyteSortOrder
    """The status code for the block"""


# Entity-specific condition types for blocks
class BlocksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BlocksSearchFilter


class BlocksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BlocksSearchFilter


class BlocksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BlocksSearchFilter


class BlocksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BlocksSearchFilter


class BlocksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BlocksSearchFilter


class BlocksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BlocksSearchFilter


class BlocksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BlocksStringFilter


class BlocksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BlocksStringFilter


class BlocksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BlocksStringFilter


class BlocksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BlocksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BlocksInCondition = TypedDict("BlocksInCondition", {"in": BlocksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BlocksNotCondition = TypedDict("BlocksNotCondition", {"not": "BlocksCondition"}, total=False)
"""Negates the nested condition."""

BlocksAndCondition = TypedDict("BlocksAndCondition", {"and": "list[BlocksCondition]"}, total=False)
"""True if all nested conditions are true."""

BlocksOrCondition = TypedDict("BlocksOrCondition", {"or": "list[BlocksCondition]"}, total=False)
"""True if any nested condition is true."""

BlocksAnyCondition = TypedDict("BlocksAnyCondition", {"any": BlocksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all blocks condition types
BlocksCondition = (
    BlocksEqCondition
    | BlocksNeqCondition
    | BlocksGtCondition
    | BlocksGteCondition
    | BlocksLtCondition
    | BlocksLteCondition
    | BlocksInCondition
    | BlocksLikeCondition
    | BlocksFuzzyCondition
    | BlocksKeywordCondition
    | BlocksContainsCondition
    | BlocksNotCondition
    | BlocksAndCondition
    | BlocksOrCondition
    | BlocksAnyCondition
)


class BlocksSearchQuery(TypedDict, total=False):
    """Search query for blocks entity."""
    filter: BlocksCondition
    sort: list[BlocksSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    channels: list[Any] | None
    """Channels for this campaign"""
    created_at: str | None
    """When the campaign was created"""
    id: str | None
    """Unique campaign identifier"""
    is_abtest: bool | None
    """Whether this campaign is an A/B test"""
    name: str | None
    """Campaign name"""
    status: str | None
    """Campaign status"""
    updated_at: str | None
    """When the campaign was last updated"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    channels: list[list[Any]]
    """Channels for this campaign"""
    created_at: list[str]
    """When the campaign was created"""
    id: list[str]
    """Unique campaign identifier"""
    is_abtest: list[bool]
    """Whether this campaign is an A/B test"""
    name: list[str]
    """Campaign name"""
    status: list[str]
    """Campaign status"""
    updated_at: list[str]
    """When the campaign was last updated"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    channels: Any
    """Channels for this campaign"""
    created_at: Any
    """When the campaign was created"""
    id: Any
    """Unique campaign identifier"""
    is_abtest: Any
    """Whether this campaign is an A/B test"""
    name: Any
    """Campaign name"""
    status: Any
    """Campaign status"""
    updated_at: Any
    """When the campaign was last updated"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    channels: str
    """Channels for this campaign"""
    created_at: str
    """When the campaign was created"""
    id: str
    """Unique campaign identifier"""
    is_abtest: str
    """Whether this campaign is an A/B test"""
    name: str
    """Campaign name"""
    status: str
    """Campaign status"""
    updated_at: str
    """When the campaign was last updated"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    channels: AirbyteSortOrder
    """Channels for this campaign"""
    created_at: AirbyteSortOrder
    """When the campaign was created"""
    id: AirbyteSortOrder
    """Unique campaign identifier"""
    is_abtest: AirbyteSortOrder
    """Whether this campaign is an A/B test"""
    name: AirbyteSortOrder
    """Campaign name"""
    status: AirbyteSortOrder
    """Campaign status"""
    updated_at: AirbyteSortOrder
    """When the campaign was last updated"""


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


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    address_line_1: str | None
    """Address line 1"""
    address_line_2: str | None
    """Address line 2"""
    alternate_emails: list[Any] | None
    """Alternate email addresses"""
    city: str | None
    """City"""
    contact_id: str | None
    """Unique contact identifier used by Airbyte"""
    country: str | None
    """Country"""
    created_at: str | None
    """When the contact was created"""
    custom_fields: dict[str, Any] | None
    """Custom field values"""
    email: str | None
    """Contact email address"""
    facebook: str | None
    """Facebook ID"""
    first_name: str | None
    """Contact first name"""
    last_name: str | None
    """Contact last name"""
    line: str | None
    """LINE ID"""
    list_ids: list[Any] | None
    """IDs of lists the contact belongs to"""
    phone_number: str | None
    """Phone number"""
    postal_code: str | None
    """Postal code"""
    state_province_region: str | None
    """State, province, or region"""
    unique_name: str | None
    """Unique name for the contact"""
    updated_at: str | None
    """When the contact was last updated"""
    whatsapp: str | None
    """WhatsApp number"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    address_line_1: list[str]
    """Address line 1"""
    address_line_2: list[str]
    """Address line 2"""
    alternate_emails: list[list[Any]]
    """Alternate email addresses"""
    city: list[str]
    """City"""
    contact_id: list[str]
    """Unique contact identifier used by Airbyte"""
    country: list[str]
    """Country"""
    created_at: list[str]
    """When the contact was created"""
    custom_fields: list[dict[str, Any]]
    """Custom field values"""
    email: list[str]
    """Contact email address"""
    facebook: list[str]
    """Facebook ID"""
    first_name: list[str]
    """Contact first name"""
    last_name: list[str]
    """Contact last name"""
    line: list[str]
    """LINE ID"""
    list_ids: list[list[Any]]
    """IDs of lists the contact belongs to"""
    phone_number: list[str]
    """Phone number"""
    postal_code: list[str]
    """Postal code"""
    state_province_region: list[str]
    """State, province, or region"""
    unique_name: list[str]
    """Unique name for the contact"""
    updated_at: list[str]
    """When the contact was last updated"""
    whatsapp: list[str]
    """WhatsApp number"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    address_line_1: Any
    """Address line 1"""
    address_line_2: Any
    """Address line 2"""
    alternate_emails: Any
    """Alternate email addresses"""
    city: Any
    """City"""
    contact_id: Any
    """Unique contact identifier used by Airbyte"""
    country: Any
    """Country"""
    created_at: Any
    """When the contact was created"""
    custom_fields: Any
    """Custom field values"""
    email: Any
    """Contact email address"""
    facebook: Any
    """Facebook ID"""
    first_name: Any
    """Contact first name"""
    last_name: Any
    """Contact last name"""
    line: Any
    """LINE ID"""
    list_ids: Any
    """IDs of lists the contact belongs to"""
    phone_number: Any
    """Phone number"""
    postal_code: Any
    """Postal code"""
    state_province_region: Any
    """State, province, or region"""
    unique_name: Any
    """Unique name for the contact"""
    updated_at: Any
    """When the contact was last updated"""
    whatsapp: Any
    """WhatsApp number"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    address_line_1: str
    """Address line 1"""
    address_line_2: str
    """Address line 2"""
    alternate_emails: str
    """Alternate email addresses"""
    city: str
    """City"""
    contact_id: str
    """Unique contact identifier used by Airbyte"""
    country: str
    """Country"""
    created_at: str
    """When the contact was created"""
    custom_fields: str
    """Custom field values"""
    email: str
    """Contact email address"""
    facebook: str
    """Facebook ID"""
    first_name: str
    """Contact first name"""
    last_name: str
    """Contact last name"""
    line: str
    """LINE ID"""
    list_ids: str
    """IDs of lists the contact belongs to"""
    phone_number: str
    """Phone number"""
    postal_code: str
    """Postal code"""
    state_province_region: str
    """State, province, or region"""
    unique_name: str
    """Unique name for the contact"""
    updated_at: str
    """When the contact was last updated"""
    whatsapp: str
    """WhatsApp number"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    address_line_1: AirbyteSortOrder
    """Address line 1"""
    address_line_2: AirbyteSortOrder
    """Address line 2"""
    alternate_emails: AirbyteSortOrder
    """Alternate email addresses"""
    city: AirbyteSortOrder
    """City"""
    contact_id: AirbyteSortOrder
    """Unique contact identifier used by Airbyte"""
    country: AirbyteSortOrder
    """Country"""
    created_at: AirbyteSortOrder
    """When the contact was created"""
    custom_fields: AirbyteSortOrder
    """Custom field values"""
    email: AirbyteSortOrder
    """Contact email address"""
    facebook: AirbyteSortOrder
    """Facebook ID"""
    first_name: AirbyteSortOrder
    """Contact first name"""
    last_name: AirbyteSortOrder
    """Contact last name"""
    line: AirbyteSortOrder
    """LINE ID"""
    list_ids: AirbyteSortOrder
    """IDs of lists the contact belongs to"""
    phone_number: AirbyteSortOrder
    """Phone number"""
    postal_code: AirbyteSortOrder
    """Postal code"""
    state_province_region: AirbyteSortOrder
    """State, province, or region"""
    unique_name: AirbyteSortOrder
    """Unique name for the contact"""
    updated_at: AirbyteSortOrder
    """When the contact was last updated"""
    whatsapp: AirbyteSortOrder
    """WhatsApp number"""


# Entity-specific condition types for contacts
class ContactsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ContactsSearchFilter


class ContactsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ContactsSearchFilter


class ContactsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ContactsSearchFilter


class ContactsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ContactsSearchFilter


class ContactsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ContactsSearchFilter


class ContactsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ContactsSearchFilter


class ContactsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ContactsStringFilter


class ContactsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ContactsStringFilter


class ContactsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ContactsStringFilter


class ContactsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ContactsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ContactsInCondition = TypedDict("ContactsInCondition", {"in": ContactsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ContactsNotCondition = TypedDict("ContactsNotCondition", {"not": "ContactsCondition"}, total=False)
"""Negates the nested condition."""

ContactsAndCondition = TypedDict("ContactsAndCondition", {"and": "list[ContactsCondition]"}, total=False)
"""True if all nested conditions are true."""

ContactsOrCondition = TypedDict("ContactsOrCondition", {"or": "list[ContactsCondition]"}, total=False)
"""True if any nested condition is true."""

ContactsAnyCondition = TypedDict("ContactsAnyCondition", {"any": ContactsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all contacts condition types
ContactsCondition = (
    ContactsEqCondition
    | ContactsNeqCondition
    | ContactsGtCondition
    | ContactsGteCondition
    | ContactsLtCondition
    | ContactsLteCondition
    | ContactsInCondition
    | ContactsLikeCondition
    | ContactsFuzzyCondition
    | ContactsKeywordCondition
    | ContactsContainsCondition
    | ContactsNotCondition
    | ContactsAndCondition
    | ContactsOrCondition
    | ContactsAnyCondition
)


class ContactsSearchQuery(TypedDict, total=False):
    """Search query for contacts entity."""
    filter: ContactsCondition
    sort: list[ContactsSortFilter]


# ===== GLOBAL_SUPPRESSIONS SEARCH TYPES =====

class GlobalSuppressionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering global_suppressions search queries."""
    created: int | None
    """Unix timestamp when the global suppression was created"""
    email: str | None
    """The globally suppressed email address"""


class GlobalSuppressionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created: list[int]
    """Unix timestamp when the global suppression was created"""
    email: list[str]
    """The globally suppressed email address"""


class GlobalSuppressionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created: Any
    """Unix timestamp when the global suppression was created"""
    email: Any
    """The globally suppressed email address"""


class GlobalSuppressionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created: str
    """Unix timestamp when the global suppression was created"""
    email: str
    """The globally suppressed email address"""


class GlobalSuppressionsSortFilter(TypedDict, total=False):
    """Available fields for sorting global_suppressions search results."""
    created: AirbyteSortOrder
    """Unix timestamp when the global suppression was created"""
    email: AirbyteSortOrder
    """The globally suppressed email address"""


# Entity-specific condition types for global_suppressions
class GlobalSuppressionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GlobalSuppressionsSearchFilter


class GlobalSuppressionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GlobalSuppressionsSearchFilter


class GlobalSuppressionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GlobalSuppressionsSearchFilter


class GlobalSuppressionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GlobalSuppressionsSearchFilter


class GlobalSuppressionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GlobalSuppressionsSearchFilter


class GlobalSuppressionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GlobalSuppressionsSearchFilter


class GlobalSuppressionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GlobalSuppressionsStringFilter


class GlobalSuppressionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GlobalSuppressionsStringFilter


class GlobalSuppressionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GlobalSuppressionsStringFilter


class GlobalSuppressionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GlobalSuppressionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GlobalSuppressionsInCondition = TypedDict("GlobalSuppressionsInCondition", {"in": GlobalSuppressionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GlobalSuppressionsNotCondition = TypedDict("GlobalSuppressionsNotCondition", {"not": "GlobalSuppressionsCondition"}, total=False)
"""Negates the nested condition."""

GlobalSuppressionsAndCondition = TypedDict("GlobalSuppressionsAndCondition", {"and": "list[GlobalSuppressionsCondition]"}, total=False)
"""True if all nested conditions are true."""

GlobalSuppressionsOrCondition = TypedDict("GlobalSuppressionsOrCondition", {"or": "list[GlobalSuppressionsCondition]"}, total=False)
"""True if any nested condition is true."""

GlobalSuppressionsAnyCondition = TypedDict("GlobalSuppressionsAnyCondition", {"any": GlobalSuppressionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all global_suppressions condition types
GlobalSuppressionsCondition = (
    GlobalSuppressionsEqCondition
    | GlobalSuppressionsNeqCondition
    | GlobalSuppressionsGtCondition
    | GlobalSuppressionsGteCondition
    | GlobalSuppressionsLtCondition
    | GlobalSuppressionsLteCondition
    | GlobalSuppressionsInCondition
    | GlobalSuppressionsLikeCondition
    | GlobalSuppressionsFuzzyCondition
    | GlobalSuppressionsKeywordCondition
    | GlobalSuppressionsContainsCondition
    | GlobalSuppressionsNotCondition
    | GlobalSuppressionsAndCondition
    | GlobalSuppressionsOrCondition
    | GlobalSuppressionsAnyCondition
)


class GlobalSuppressionsSearchQuery(TypedDict, total=False):
    """Search query for global_suppressions entity."""
    filter: GlobalSuppressionsCondition
    sort: list[GlobalSuppressionsSortFilter]


# ===== INVALID_EMAILS SEARCH TYPES =====

class InvalidEmailsSearchFilter(TypedDict, total=False):
    """Available fields for filtering invalid_emails search queries."""
    created: int | None
    """Unix timestamp when the invalid email was recorded"""
    email: str | None
    """The invalid email address"""
    reason: str | None
    """The reason the email is invalid"""


class InvalidEmailsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created: list[int]
    """Unix timestamp when the invalid email was recorded"""
    email: list[str]
    """The invalid email address"""
    reason: list[str]
    """The reason the email is invalid"""


class InvalidEmailsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created: Any
    """Unix timestamp when the invalid email was recorded"""
    email: Any
    """The invalid email address"""
    reason: Any
    """The reason the email is invalid"""


class InvalidEmailsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created: str
    """Unix timestamp when the invalid email was recorded"""
    email: str
    """The invalid email address"""
    reason: str
    """The reason the email is invalid"""


class InvalidEmailsSortFilter(TypedDict, total=False):
    """Available fields for sorting invalid_emails search results."""
    created: AirbyteSortOrder
    """Unix timestamp when the invalid email was recorded"""
    email: AirbyteSortOrder
    """The invalid email address"""
    reason: AirbyteSortOrder
    """The reason the email is invalid"""


# Entity-specific condition types for invalid_emails
class InvalidEmailsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InvalidEmailsSearchFilter


class InvalidEmailsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InvalidEmailsSearchFilter


class InvalidEmailsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InvalidEmailsSearchFilter


class InvalidEmailsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InvalidEmailsSearchFilter


class InvalidEmailsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InvalidEmailsSearchFilter


class InvalidEmailsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InvalidEmailsSearchFilter


class InvalidEmailsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InvalidEmailsStringFilter


class InvalidEmailsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InvalidEmailsStringFilter


class InvalidEmailsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InvalidEmailsStringFilter


class InvalidEmailsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InvalidEmailsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InvalidEmailsInCondition = TypedDict("InvalidEmailsInCondition", {"in": InvalidEmailsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InvalidEmailsNotCondition = TypedDict("InvalidEmailsNotCondition", {"not": "InvalidEmailsCondition"}, total=False)
"""Negates the nested condition."""

InvalidEmailsAndCondition = TypedDict("InvalidEmailsAndCondition", {"and": "list[InvalidEmailsCondition]"}, total=False)
"""True if all nested conditions are true."""

InvalidEmailsOrCondition = TypedDict("InvalidEmailsOrCondition", {"or": "list[InvalidEmailsCondition]"}, total=False)
"""True if any nested condition is true."""

InvalidEmailsAnyCondition = TypedDict("InvalidEmailsAnyCondition", {"any": InvalidEmailsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all invalid_emails condition types
InvalidEmailsCondition = (
    InvalidEmailsEqCondition
    | InvalidEmailsNeqCondition
    | InvalidEmailsGtCondition
    | InvalidEmailsGteCondition
    | InvalidEmailsLtCondition
    | InvalidEmailsLteCondition
    | InvalidEmailsInCondition
    | InvalidEmailsLikeCondition
    | InvalidEmailsFuzzyCondition
    | InvalidEmailsKeywordCondition
    | InvalidEmailsContainsCondition
    | InvalidEmailsNotCondition
    | InvalidEmailsAndCondition
    | InvalidEmailsOrCondition
    | InvalidEmailsAnyCondition
)


class InvalidEmailsSearchQuery(TypedDict, total=False):
    """Search query for invalid_emails entity."""
    filter: InvalidEmailsCondition
    sort: list[InvalidEmailsSortFilter]


# ===== LISTS SEARCH TYPES =====

class ListsSearchFilter(TypedDict, total=False):
    """Available fields for filtering lists search queries."""
    metadata: dict[str, Any] | None
    """Metadata about the list resource"""
    contact_count: int | None
    """Number of contacts in the list"""
    id: str | None
    """Unique list identifier"""
    name: str | None
    """Name of the list"""


class ListsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    metadata: list[dict[str, Any]]
    """Metadata about the list resource"""
    contact_count: list[int]
    """Number of contacts in the list"""
    id: list[str]
    """Unique list identifier"""
    name: list[str]
    """Name of the list"""


class ListsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    metadata: Any
    """Metadata about the list resource"""
    contact_count: Any
    """Number of contacts in the list"""
    id: Any
    """Unique list identifier"""
    name: Any
    """Name of the list"""


class ListsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    metadata: str
    """Metadata about the list resource"""
    contact_count: str
    """Number of contacts in the list"""
    id: str
    """Unique list identifier"""
    name: str
    """Name of the list"""


class ListsSortFilter(TypedDict, total=False):
    """Available fields for sorting lists search results."""
    metadata: AirbyteSortOrder
    """Metadata about the list resource"""
    contact_count: AirbyteSortOrder
    """Number of contacts in the list"""
    id: AirbyteSortOrder
    """Unique list identifier"""
    name: AirbyteSortOrder
    """Name of the list"""


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


# ===== SEGMENTS SEARCH TYPES =====

class SegmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering segments search queries."""
    contacts_count: int | None
    """Number of contacts in the segment"""
    created_at: str | None
    """When the segment was created"""
    id: str | None
    """Unique segment identifier"""
    name: str | None
    """Segment name"""
    next_sample_update: str | None
    """When the next sample update will occur"""
    parent_list_ids: list[Any] | None
    """IDs of parent lists"""
    query_version: str | None
    """Query version used"""
    sample_updated_at: str | None
    """When the sample was last updated"""
    status: dict[str, Any] | None
    """Segment status details"""
    updated_at: str | None
    """When the segment was last updated"""


class SegmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    contacts_count: list[int]
    """Number of contacts in the segment"""
    created_at: list[str]
    """When the segment was created"""
    id: list[str]
    """Unique segment identifier"""
    name: list[str]
    """Segment name"""
    next_sample_update: list[str]
    """When the next sample update will occur"""
    parent_list_ids: list[list[Any]]
    """IDs of parent lists"""
    query_version: list[str]
    """Query version used"""
    sample_updated_at: list[str]
    """When the sample was last updated"""
    status: list[dict[str, Any]]
    """Segment status details"""
    updated_at: list[str]
    """When the segment was last updated"""


class SegmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    contacts_count: Any
    """Number of contacts in the segment"""
    created_at: Any
    """When the segment was created"""
    id: Any
    """Unique segment identifier"""
    name: Any
    """Segment name"""
    next_sample_update: Any
    """When the next sample update will occur"""
    parent_list_ids: Any
    """IDs of parent lists"""
    query_version: Any
    """Query version used"""
    sample_updated_at: Any
    """When the sample was last updated"""
    status: Any
    """Segment status details"""
    updated_at: Any
    """When the segment was last updated"""


class SegmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    contacts_count: str
    """Number of contacts in the segment"""
    created_at: str
    """When the segment was created"""
    id: str
    """Unique segment identifier"""
    name: str
    """Segment name"""
    next_sample_update: str
    """When the next sample update will occur"""
    parent_list_ids: str
    """IDs of parent lists"""
    query_version: str
    """Query version used"""
    sample_updated_at: str
    """When the sample was last updated"""
    status: str
    """Segment status details"""
    updated_at: str
    """When the segment was last updated"""


class SegmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting segments search results."""
    contacts_count: AirbyteSortOrder
    """Number of contacts in the segment"""
    created_at: AirbyteSortOrder
    """When the segment was created"""
    id: AirbyteSortOrder
    """Unique segment identifier"""
    name: AirbyteSortOrder
    """Segment name"""
    next_sample_update: AirbyteSortOrder
    """When the next sample update will occur"""
    parent_list_ids: AirbyteSortOrder
    """IDs of parent lists"""
    query_version: AirbyteSortOrder
    """Query version used"""
    sample_updated_at: AirbyteSortOrder
    """When the sample was last updated"""
    status: AirbyteSortOrder
    """Segment status details"""
    updated_at: AirbyteSortOrder
    """When the segment was last updated"""


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


class SegmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SegmentsStringFilter


class SegmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SegmentsStringFilter


class SegmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SegmentsStringFilter


class SegmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SegmentsAnyValueFilter


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
    | SegmentsLikeCondition
    | SegmentsFuzzyCondition
    | SegmentsKeywordCondition
    | SegmentsContainsCondition
    | SegmentsNotCondition
    | SegmentsAndCondition
    | SegmentsOrCondition
    | SegmentsAnyCondition
)


class SegmentsSearchQuery(TypedDict, total=False):
    """Search query for segments entity."""
    filter: SegmentsCondition
    sort: list[SegmentsSortFilter]


# ===== SINGLESEND_STATS SEARCH TYPES =====

class SinglesendStatsSearchFilter(TypedDict, total=False):
    """Available fields for filtering singlesend_stats search queries."""
    ab_phase: str | None
    """The A/B test phase"""
    ab_variation: str | None
    """The A/B test variation"""
    aggregation: str | None
    """The aggregation type"""
    id: str | None
    """The single send ID"""
    stats: dict[str, Any] | None
    """Email statistics for the single send"""


class SinglesendStatsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ab_phase: list[str]
    """The A/B test phase"""
    ab_variation: list[str]
    """The A/B test variation"""
    aggregation: list[str]
    """The aggregation type"""
    id: list[str]
    """The single send ID"""
    stats: list[dict[str, Any]]
    """Email statistics for the single send"""


class SinglesendStatsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ab_phase: Any
    """The A/B test phase"""
    ab_variation: Any
    """The A/B test variation"""
    aggregation: Any
    """The aggregation type"""
    id: Any
    """The single send ID"""
    stats: Any
    """Email statistics for the single send"""


class SinglesendStatsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ab_phase: str
    """The A/B test phase"""
    ab_variation: str
    """The A/B test variation"""
    aggregation: str
    """The aggregation type"""
    id: str
    """The single send ID"""
    stats: str
    """Email statistics for the single send"""


class SinglesendStatsSortFilter(TypedDict, total=False):
    """Available fields for sorting singlesend_stats search results."""
    ab_phase: AirbyteSortOrder
    """The A/B test phase"""
    ab_variation: AirbyteSortOrder
    """The A/B test variation"""
    aggregation: AirbyteSortOrder
    """The aggregation type"""
    id: AirbyteSortOrder
    """The single send ID"""
    stats: AirbyteSortOrder
    """Email statistics for the single send"""


# Entity-specific condition types for singlesend_stats
class SinglesendStatsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SinglesendStatsSearchFilter


class SinglesendStatsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SinglesendStatsSearchFilter


class SinglesendStatsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SinglesendStatsSearchFilter


class SinglesendStatsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SinglesendStatsSearchFilter


class SinglesendStatsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SinglesendStatsSearchFilter


class SinglesendStatsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SinglesendStatsSearchFilter


class SinglesendStatsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SinglesendStatsStringFilter


class SinglesendStatsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SinglesendStatsStringFilter


class SinglesendStatsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SinglesendStatsStringFilter


class SinglesendStatsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SinglesendStatsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SinglesendStatsInCondition = TypedDict("SinglesendStatsInCondition", {"in": SinglesendStatsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SinglesendStatsNotCondition = TypedDict("SinglesendStatsNotCondition", {"not": "SinglesendStatsCondition"}, total=False)
"""Negates the nested condition."""

SinglesendStatsAndCondition = TypedDict("SinglesendStatsAndCondition", {"and": "list[SinglesendStatsCondition]"}, total=False)
"""True if all nested conditions are true."""

SinglesendStatsOrCondition = TypedDict("SinglesendStatsOrCondition", {"or": "list[SinglesendStatsCondition]"}, total=False)
"""True if any nested condition is true."""

SinglesendStatsAnyCondition = TypedDict("SinglesendStatsAnyCondition", {"any": SinglesendStatsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all singlesend_stats condition types
SinglesendStatsCondition = (
    SinglesendStatsEqCondition
    | SinglesendStatsNeqCondition
    | SinglesendStatsGtCondition
    | SinglesendStatsGteCondition
    | SinglesendStatsLtCondition
    | SinglesendStatsLteCondition
    | SinglesendStatsInCondition
    | SinglesendStatsLikeCondition
    | SinglesendStatsFuzzyCondition
    | SinglesendStatsKeywordCondition
    | SinglesendStatsContainsCondition
    | SinglesendStatsNotCondition
    | SinglesendStatsAndCondition
    | SinglesendStatsOrCondition
    | SinglesendStatsAnyCondition
)


class SinglesendStatsSearchQuery(TypedDict, total=False):
    """Search query for singlesend_stats entity."""
    filter: SinglesendStatsCondition
    sort: list[SinglesendStatsSortFilter]


# ===== SINGLESENDS SEARCH TYPES =====

class SinglesendsSearchFilter(TypedDict, total=False):
    """Available fields for filtering singlesends search queries."""
    categories: list[Any] | None
    """Categories associated with this single send"""
    created_at: str | None
    """When the single send was created"""
    id: str | None
    """Unique single send identifier"""
    is_abtest: bool | None
    """Whether this is an A/B test"""
    name: str | None
    """Single send name"""
    send_at: str | None
    """Scheduled send time"""
    status: str | None
    """Current status: draft, scheduled, or triggered"""
    updated_at: str | None
    """When the single send was last updated"""


class SinglesendsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    categories: list[list[Any]]
    """Categories associated with this single send"""
    created_at: list[str]
    """When the single send was created"""
    id: list[str]
    """Unique single send identifier"""
    is_abtest: list[bool]
    """Whether this is an A/B test"""
    name: list[str]
    """Single send name"""
    send_at: list[str]
    """Scheduled send time"""
    status: list[str]
    """Current status: draft, scheduled, or triggered"""
    updated_at: list[str]
    """When the single send was last updated"""


class SinglesendsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    categories: Any
    """Categories associated with this single send"""
    created_at: Any
    """When the single send was created"""
    id: Any
    """Unique single send identifier"""
    is_abtest: Any
    """Whether this is an A/B test"""
    name: Any
    """Single send name"""
    send_at: Any
    """Scheduled send time"""
    status: Any
    """Current status: draft, scheduled, or triggered"""
    updated_at: Any
    """When the single send was last updated"""


class SinglesendsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    categories: str
    """Categories associated with this single send"""
    created_at: str
    """When the single send was created"""
    id: str
    """Unique single send identifier"""
    is_abtest: str
    """Whether this is an A/B test"""
    name: str
    """Single send name"""
    send_at: str
    """Scheduled send time"""
    status: str
    """Current status: draft, scheduled, or triggered"""
    updated_at: str
    """When the single send was last updated"""


class SinglesendsSortFilter(TypedDict, total=False):
    """Available fields for sorting singlesends search results."""
    categories: AirbyteSortOrder
    """Categories associated with this single send"""
    created_at: AirbyteSortOrder
    """When the single send was created"""
    id: AirbyteSortOrder
    """Unique single send identifier"""
    is_abtest: AirbyteSortOrder
    """Whether this is an A/B test"""
    name: AirbyteSortOrder
    """Single send name"""
    send_at: AirbyteSortOrder
    """Scheduled send time"""
    status: AirbyteSortOrder
    """Current status: draft, scheduled, or triggered"""
    updated_at: AirbyteSortOrder
    """When the single send was last updated"""


# Entity-specific condition types for singlesends
class SinglesendsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SinglesendsSearchFilter


class SinglesendsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SinglesendsSearchFilter


class SinglesendsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SinglesendsSearchFilter


class SinglesendsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SinglesendsSearchFilter


class SinglesendsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SinglesendsSearchFilter


class SinglesendsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SinglesendsSearchFilter


class SinglesendsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SinglesendsStringFilter


class SinglesendsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SinglesendsStringFilter


class SinglesendsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SinglesendsStringFilter


class SinglesendsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SinglesendsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SinglesendsInCondition = TypedDict("SinglesendsInCondition", {"in": SinglesendsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SinglesendsNotCondition = TypedDict("SinglesendsNotCondition", {"not": "SinglesendsCondition"}, total=False)
"""Negates the nested condition."""

SinglesendsAndCondition = TypedDict("SinglesendsAndCondition", {"and": "list[SinglesendsCondition]"}, total=False)
"""True if all nested conditions are true."""

SinglesendsOrCondition = TypedDict("SinglesendsOrCondition", {"or": "list[SinglesendsCondition]"}, total=False)
"""True if any nested condition is true."""

SinglesendsAnyCondition = TypedDict("SinglesendsAnyCondition", {"any": SinglesendsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all singlesends condition types
SinglesendsCondition = (
    SinglesendsEqCondition
    | SinglesendsNeqCondition
    | SinglesendsGtCondition
    | SinglesendsGteCondition
    | SinglesendsLtCondition
    | SinglesendsLteCondition
    | SinglesendsInCondition
    | SinglesendsLikeCondition
    | SinglesendsFuzzyCondition
    | SinglesendsKeywordCondition
    | SinglesendsContainsCondition
    | SinglesendsNotCondition
    | SinglesendsAndCondition
    | SinglesendsOrCondition
    | SinglesendsAnyCondition
)


class SinglesendsSearchQuery(TypedDict, total=False):
    """Search query for singlesends entity."""
    filter: SinglesendsCondition
    sort: list[SinglesendsSortFilter]


# ===== SUPPRESSION_GROUP_MEMBERS SEARCH TYPES =====

class SuppressionGroupMembersSearchFilter(TypedDict, total=False):
    """Available fields for filtering suppression_group_members search queries."""
    created_at: int | None
    """Unix timestamp when the suppression was created"""
    email: str | None
    """The suppressed email address"""
    group_id: int | None
    """ID of the suppression group"""
    group_name: str | None
    """Name of the suppression group"""


class SuppressionGroupMembersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[int]
    """Unix timestamp when the suppression was created"""
    email: list[str]
    """The suppressed email address"""
    group_id: list[int]
    """ID of the suppression group"""
    group_name: list[str]
    """Name of the suppression group"""


class SuppressionGroupMembersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Unix timestamp when the suppression was created"""
    email: Any
    """The suppressed email address"""
    group_id: Any
    """ID of the suppression group"""
    group_name: Any
    """Name of the suppression group"""


class SuppressionGroupMembersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """Unix timestamp when the suppression was created"""
    email: str
    """The suppressed email address"""
    group_id: str
    """ID of the suppression group"""
    group_name: str
    """Name of the suppression group"""


class SuppressionGroupMembersSortFilter(TypedDict, total=False):
    """Available fields for sorting suppression_group_members search results."""
    created_at: AirbyteSortOrder
    """Unix timestamp when the suppression was created"""
    email: AirbyteSortOrder
    """The suppressed email address"""
    group_id: AirbyteSortOrder
    """ID of the suppression group"""
    group_name: AirbyteSortOrder
    """Name of the suppression group"""


# Entity-specific condition types for suppression_group_members
class SuppressionGroupMembersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SuppressionGroupMembersSearchFilter


class SuppressionGroupMembersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SuppressionGroupMembersSearchFilter


class SuppressionGroupMembersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SuppressionGroupMembersSearchFilter


class SuppressionGroupMembersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SuppressionGroupMembersSearchFilter


class SuppressionGroupMembersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SuppressionGroupMembersSearchFilter


class SuppressionGroupMembersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SuppressionGroupMembersSearchFilter


class SuppressionGroupMembersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SuppressionGroupMembersStringFilter


class SuppressionGroupMembersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SuppressionGroupMembersStringFilter


class SuppressionGroupMembersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SuppressionGroupMembersStringFilter


class SuppressionGroupMembersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SuppressionGroupMembersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SuppressionGroupMembersInCondition = TypedDict("SuppressionGroupMembersInCondition", {"in": SuppressionGroupMembersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SuppressionGroupMembersNotCondition = TypedDict("SuppressionGroupMembersNotCondition", {"not": "SuppressionGroupMembersCondition"}, total=False)
"""Negates the nested condition."""

SuppressionGroupMembersAndCondition = TypedDict("SuppressionGroupMembersAndCondition", {"and": "list[SuppressionGroupMembersCondition]"}, total=False)
"""True if all nested conditions are true."""

SuppressionGroupMembersOrCondition = TypedDict("SuppressionGroupMembersOrCondition", {"or": "list[SuppressionGroupMembersCondition]"}, total=False)
"""True if any nested condition is true."""

SuppressionGroupMembersAnyCondition = TypedDict("SuppressionGroupMembersAnyCondition", {"any": SuppressionGroupMembersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all suppression_group_members condition types
SuppressionGroupMembersCondition = (
    SuppressionGroupMembersEqCondition
    | SuppressionGroupMembersNeqCondition
    | SuppressionGroupMembersGtCondition
    | SuppressionGroupMembersGteCondition
    | SuppressionGroupMembersLtCondition
    | SuppressionGroupMembersLteCondition
    | SuppressionGroupMembersInCondition
    | SuppressionGroupMembersLikeCondition
    | SuppressionGroupMembersFuzzyCondition
    | SuppressionGroupMembersKeywordCondition
    | SuppressionGroupMembersContainsCondition
    | SuppressionGroupMembersNotCondition
    | SuppressionGroupMembersAndCondition
    | SuppressionGroupMembersOrCondition
    | SuppressionGroupMembersAnyCondition
)


class SuppressionGroupMembersSearchQuery(TypedDict, total=False):
    """Search query for suppression_group_members entity."""
    filter: SuppressionGroupMembersCondition
    sort: list[SuppressionGroupMembersSortFilter]


# ===== SUPPRESSION_GROUPS SEARCH TYPES =====

class SuppressionGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering suppression_groups search queries."""
    description: str | None
    """Description of the suppression group"""
    id: int | None
    """Unique suppression group identifier"""
    is_default: bool | None
    """Whether this is the default suppression group"""
    name: str | None
    """Suppression group name"""
    unsubscribes: int | None
    """Number of unsubscribes in this group"""


class SuppressionGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    description: list[str]
    """Description of the suppression group"""
    id: list[int]
    """Unique suppression group identifier"""
    is_default: list[bool]
    """Whether this is the default suppression group"""
    name: list[str]
    """Suppression group name"""
    unsubscribes: list[int]
    """Number of unsubscribes in this group"""


class SuppressionGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    description: Any
    """Description of the suppression group"""
    id: Any
    """Unique suppression group identifier"""
    is_default: Any
    """Whether this is the default suppression group"""
    name: Any
    """Suppression group name"""
    unsubscribes: Any
    """Number of unsubscribes in this group"""


class SuppressionGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    description: str
    """Description of the suppression group"""
    id: str
    """Unique suppression group identifier"""
    is_default: str
    """Whether this is the default suppression group"""
    name: str
    """Suppression group name"""
    unsubscribes: str
    """Number of unsubscribes in this group"""


class SuppressionGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting suppression_groups search results."""
    description: AirbyteSortOrder
    """Description of the suppression group"""
    id: AirbyteSortOrder
    """Unique suppression group identifier"""
    is_default: AirbyteSortOrder
    """Whether this is the default suppression group"""
    name: AirbyteSortOrder
    """Suppression group name"""
    unsubscribes: AirbyteSortOrder
    """Number of unsubscribes in this group"""


# Entity-specific condition types for suppression_groups
class SuppressionGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SuppressionGroupsSearchFilter


class SuppressionGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SuppressionGroupsSearchFilter


class SuppressionGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SuppressionGroupsSearchFilter


class SuppressionGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SuppressionGroupsSearchFilter


class SuppressionGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SuppressionGroupsSearchFilter


class SuppressionGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SuppressionGroupsSearchFilter


class SuppressionGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SuppressionGroupsStringFilter


class SuppressionGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SuppressionGroupsStringFilter


class SuppressionGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SuppressionGroupsStringFilter


class SuppressionGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SuppressionGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SuppressionGroupsInCondition = TypedDict("SuppressionGroupsInCondition", {"in": SuppressionGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SuppressionGroupsNotCondition = TypedDict("SuppressionGroupsNotCondition", {"not": "SuppressionGroupsCondition"}, total=False)
"""Negates the nested condition."""

SuppressionGroupsAndCondition = TypedDict("SuppressionGroupsAndCondition", {"and": "list[SuppressionGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

SuppressionGroupsOrCondition = TypedDict("SuppressionGroupsOrCondition", {"or": "list[SuppressionGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

SuppressionGroupsAnyCondition = TypedDict("SuppressionGroupsAnyCondition", {"any": SuppressionGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all suppression_groups condition types
SuppressionGroupsCondition = (
    SuppressionGroupsEqCondition
    | SuppressionGroupsNeqCondition
    | SuppressionGroupsGtCondition
    | SuppressionGroupsGteCondition
    | SuppressionGroupsLtCondition
    | SuppressionGroupsLteCondition
    | SuppressionGroupsInCondition
    | SuppressionGroupsLikeCondition
    | SuppressionGroupsFuzzyCondition
    | SuppressionGroupsKeywordCondition
    | SuppressionGroupsContainsCondition
    | SuppressionGroupsNotCondition
    | SuppressionGroupsAndCondition
    | SuppressionGroupsOrCondition
    | SuppressionGroupsAnyCondition
)


class SuppressionGroupsSearchQuery(TypedDict, total=False):
    """Search query for suppression_groups entity."""
    filter: SuppressionGroupsCondition
    sort: list[SuppressionGroupsSortFilter]


# ===== TEMPLATES SEARCH TYPES =====

class TemplatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering templates search queries."""
    generation: str | None
    """Template generation (legacy or dynamic)"""
    id: str | None
    """Unique template identifier"""
    name: str | None
    """Template name"""
    updated_at: str | None
    """When the template was last updated"""
    versions: list[Any] | None
    """Template versions"""


class TemplatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    generation: list[str]
    """Template generation (legacy or dynamic)"""
    id: list[str]
    """Unique template identifier"""
    name: list[str]
    """Template name"""
    updated_at: list[str]
    """When the template was last updated"""
    versions: list[list[Any]]
    """Template versions"""


class TemplatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    generation: Any
    """Template generation (legacy or dynamic)"""
    id: Any
    """Unique template identifier"""
    name: Any
    """Template name"""
    updated_at: Any
    """When the template was last updated"""
    versions: Any
    """Template versions"""


class TemplatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    generation: str
    """Template generation (legacy or dynamic)"""
    id: str
    """Unique template identifier"""
    name: str
    """Template name"""
    updated_at: str
    """When the template was last updated"""
    versions: str
    """Template versions"""


class TemplatesSortFilter(TypedDict, total=False):
    """Available fields for sorting templates search results."""
    generation: AirbyteSortOrder
    """Template generation (legacy or dynamic)"""
    id: AirbyteSortOrder
    """Unique template identifier"""
    name: AirbyteSortOrder
    """Template name"""
    updated_at: AirbyteSortOrder
    """When the template was last updated"""
    versions: AirbyteSortOrder
    """Template versions"""


# Entity-specific condition types for templates
class TemplatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TemplatesSearchFilter


class TemplatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TemplatesSearchFilter


class TemplatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TemplatesSearchFilter


class TemplatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TemplatesSearchFilter


class TemplatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TemplatesSearchFilter


class TemplatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TemplatesSearchFilter


class TemplatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TemplatesStringFilter


class TemplatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TemplatesStringFilter


class TemplatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TemplatesStringFilter


class TemplatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TemplatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TemplatesInCondition = TypedDict("TemplatesInCondition", {"in": TemplatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TemplatesNotCondition = TypedDict("TemplatesNotCondition", {"not": "TemplatesCondition"}, total=False)
"""Negates the nested condition."""

TemplatesAndCondition = TypedDict("TemplatesAndCondition", {"and": "list[TemplatesCondition]"}, total=False)
"""True if all nested conditions are true."""

TemplatesOrCondition = TypedDict("TemplatesOrCondition", {"or": "list[TemplatesCondition]"}, total=False)
"""True if any nested condition is true."""

TemplatesAnyCondition = TypedDict("TemplatesAnyCondition", {"any": TemplatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all templates condition types
TemplatesCondition = (
    TemplatesEqCondition
    | TemplatesNeqCondition
    | TemplatesGtCondition
    | TemplatesGteCondition
    | TemplatesLtCondition
    | TemplatesLteCondition
    | TemplatesInCondition
    | TemplatesLikeCondition
    | TemplatesFuzzyCondition
    | TemplatesKeywordCondition
    | TemplatesContainsCondition
    | TemplatesNotCondition
    | TemplatesAndCondition
    | TemplatesOrCondition
    | TemplatesAnyCondition
)


class TemplatesSearchQuery(TypedDict, total=False):
    """Search query for templates entity."""
    filter: TemplatesCondition
    sort: list[TemplatesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
