"""
Type definitions for klaviyo connector.
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

class ProfilesListParams(TypedDict):
    """Parameters for profiles.list operation"""
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]

class ProfilesGetParams(TypedDict):
    """Parameters for profiles.get operation"""
    id: str

class ListsListParams(TypedDict):
    """Parameters for lists.list operation"""
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]

class ListsGetParams(TypedDict):
    """Parameters for lists.get operation"""
    id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    filter: str
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    id: str

class EventsListParams(TypedDict):
    """Parameters for events.list operation"""
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]
    sort: NotRequired[str]

class MetricsListParams(TypedDict):
    """Parameters for metrics.list operation"""
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]

class MetricsGetParams(TypedDict):
    """Parameters for metrics.get operation"""
    id: str

class FlowsListParams(TypedDict):
    """Parameters for flows.list operation"""
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]

class FlowsGetParams(TypedDict):
    """Parameters for flows.get operation"""
    id: str

class EmailTemplatesListParams(TypedDict):
    """Parameters for email_templates.list operation"""
    page_size: NotRequired[int]
    page_cursor: NotRequired[str]

class EmailTemplatesGetParams(TypedDict):
    """Parameters for email_templates.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== PROFILES SEARCH TYPES =====

class ProfilesSearchFilter(TypedDict, total=False):
    """Available fields for filtering profiles search queries."""
    attributes: dict[str, Any] | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    relationships: dict[str, Any] | None
    """"""
    segments: dict[str, Any] | None
    """"""
    type: str | None
    """"""
    updated: str | None
    """"""


class ProfilesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    relationships: list[dict[str, Any]]
    """"""
    segments: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""
    updated: list[str]
    """"""


class ProfilesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    relationships: Any
    """"""
    segments: Any
    """"""
    type: Any
    """"""
    updated: Any
    """"""


class ProfilesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    id: str
    """"""
    links: str
    """"""
    relationships: str
    """"""
    segments: str
    """"""
    type: str
    """"""
    updated: str
    """"""


class ProfilesSortFilter(TypedDict, total=False):
    """Available fields for sorting profiles search results."""
    attributes: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    relationships: AirbyteSortOrder
    """"""
    segments: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""
    updated: AirbyteSortOrder
    """"""


# Entity-specific condition types for profiles
class ProfilesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProfilesSearchFilter


class ProfilesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProfilesSearchFilter


class ProfilesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProfilesSearchFilter


class ProfilesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProfilesSearchFilter


class ProfilesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProfilesSearchFilter


class ProfilesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProfilesSearchFilter


class ProfilesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProfilesStringFilter


class ProfilesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProfilesStringFilter


class ProfilesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProfilesStringFilter


class ProfilesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProfilesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProfilesInCondition = TypedDict("ProfilesInCondition", {"in": ProfilesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProfilesNotCondition = TypedDict("ProfilesNotCondition", {"not": "ProfilesCondition"}, total=False)
"""Negates the nested condition."""

ProfilesAndCondition = TypedDict("ProfilesAndCondition", {"and": "list[ProfilesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProfilesOrCondition = TypedDict("ProfilesOrCondition", {"or": "list[ProfilesCondition]"}, total=False)
"""True if any nested condition is true."""

ProfilesAnyCondition = TypedDict("ProfilesAnyCondition", {"any": ProfilesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all profiles condition types
ProfilesCondition = (
    ProfilesEqCondition
    | ProfilesNeqCondition
    | ProfilesGtCondition
    | ProfilesGteCondition
    | ProfilesLtCondition
    | ProfilesLteCondition
    | ProfilesInCondition
    | ProfilesLikeCondition
    | ProfilesFuzzyCondition
    | ProfilesKeywordCondition
    | ProfilesContainsCondition
    | ProfilesNotCondition
    | ProfilesAndCondition
    | ProfilesOrCondition
    | ProfilesAnyCondition
)


class ProfilesSearchQuery(TypedDict, total=False):
    """Search query for profiles entity."""
    filter: ProfilesCondition
    sort: list[ProfilesSortFilter]


# ===== EVENTS SEARCH TYPES =====

class EventsSearchFilter(TypedDict, total=False):
    """Available fields for filtering events search queries."""
    attributes: dict[str, Any] | None
    """"""
    datetime: str | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    relationships: dict[str, Any] | None
    """"""
    type: str | None
    """"""


class EventsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    datetime: list[str]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    relationships: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""


class EventsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    datetime: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    relationships: Any
    """"""
    type: Any
    """"""


class EventsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    datetime: str
    """"""
    id: str
    """"""
    links: str
    """"""
    relationships: str
    """"""
    type: str
    """"""


class EventsSortFilter(TypedDict, total=False):
    """Available fields for sorting events search results."""
    attributes: AirbyteSortOrder
    """"""
    datetime: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    relationships: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""


# Entity-specific condition types for events
class EventsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EventsSearchFilter


class EventsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EventsSearchFilter


class EventsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EventsSearchFilter


class EventsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EventsSearchFilter


class EventsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EventsSearchFilter


class EventsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EventsSearchFilter


class EventsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EventsStringFilter


class EventsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EventsStringFilter


class EventsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EventsStringFilter


class EventsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EventsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EventsInCondition = TypedDict("EventsInCondition", {"in": EventsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EventsNotCondition = TypedDict("EventsNotCondition", {"not": "EventsCondition"}, total=False)
"""Negates the nested condition."""

EventsAndCondition = TypedDict("EventsAndCondition", {"and": "list[EventsCondition]"}, total=False)
"""True if all nested conditions are true."""

EventsOrCondition = TypedDict("EventsOrCondition", {"or": "list[EventsCondition]"}, total=False)
"""True if any nested condition is true."""

EventsAnyCondition = TypedDict("EventsAnyCondition", {"any": EventsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all events condition types
EventsCondition = (
    EventsEqCondition
    | EventsNeqCondition
    | EventsGtCondition
    | EventsGteCondition
    | EventsLtCondition
    | EventsLteCondition
    | EventsInCondition
    | EventsLikeCondition
    | EventsFuzzyCondition
    | EventsKeywordCondition
    | EventsContainsCondition
    | EventsNotCondition
    | EventsAndCondition
    | EventsOrCondition
    | EventsAnyCondition
)


class EventsSearchQuery(TypedDict, total=False):
    """Search query for events entity."""
    filter: EventsCondition
    sort: list[EventsSortFilter]


# ===== EMAIL_TEMPLATES SEARCH TYPES =====

class EmailTemplatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering email_templates search queries."""
    attributes: dict[str, Any] | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    type: str | None
    """"""
    updated: str | None
    """"""


class EmailTemplatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""
    updated: list[str]
    """"""


class EmailTemplatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    type: Any
    """"""
    updated: Any
    """"""


class EmailTemplatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    id: str
    """"""
    links: str
    """"""
    type: str
    """"""
    updated: str
    """"""


class EmailTemplatesSortFilter(TypedDict, total=False):
    """Available fields for sorting email_templates search results."""
    attributes: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""
    updated: AirbyteSortOrder
    """"""


# Entity-specific condition types for email_templates
class EmailTemplatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EmailTemplatesSearchFilter


class EmailTemplatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EmailTemplatesSearchFilter


class EmailTemplatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EmailTemplatesSearchFilter


class EmailTemplatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EmailTemplatesSearchFilter


class EmailTemplatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EmailTemplatesSearchFilter


class EmailTemplatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EmailTemplatesSearchFilter


class EmailTemplatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EmailTemplatesStringFilter


class EmailTemplatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EmailTemplatesStringFilter


class EmailTemplatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EmailTemplatesStringFilter


class EmailTemplatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EmailTemplatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EmailTemplatesInCondition = TypedDict("EmailTemplatesInCondition", {"in": EmailTemplatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EmailTemplatesNotCondition = TypedDict("EmailTemplatesNotCondition", {"not": "EmailTemplatesCondition"}, total=False)
"""Negates the nested condition."""

EmailTemplatesAndCondition = TypedDict("EmailTemplatesAndCondition", {"and": "list[EmailTemplatesCondition]"}, total=False)
"""True if all nested conditions are true."""

EmailTemplatesOrCondition = TypedDict("EmailTemplatesOrCondition", {"or": "list[EmailTemplatesCondition]"}, total=False)
"""True if any nested condition is true."""

EmailTemplatesAnyCondition = TypedDict("EmailTemplatesAnyCondition", {"any": EmailTemplatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all email_templates condition types
EmailTemplatesCondition = (
    EmailTemplatesEqCondition
    | EmailTemplatesNeqCondition
    | EmailTemplatesGtCondition
    | EmailTemplatesGteCondition
    | EmailTemplatesLtCondition
    | EmailTemplatesLteCondition
    | EmailTemplatesInCondition
    | EmailTemplatesLikeCondition
    | EmailTemplatesFuzzyCondition
    | EmailTemplatesKeywordCondition
    | EmailTemplatesContainsCondition
    | EmailTemplatesNotCondition
    | EmailTemplatesAndCondition
    | EmailTemplatesOrCondition
    | EmailTemplatesAnyCondition
)


class EmailTemplatesSearchQuery(TypedDict, total=False):
    """Search query for email_templates entity."""
    filter: EmailTemplatesCondition
    sort: list[EmailTemplatesSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    attributes: dict[str, Any] | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    relationships: dict[str, Any] | None
    """"""
    type: str | None
    """"""
    updated_at: str | None
    """"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    relationships: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""
    updated_at: list[str]
    """"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    relationships: Any
    """"""
    type: Any
    """"""
    updated_at: Any
    """"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    id: str
    """"""
    links: str
    """"""
    relationships: str
    """"""
    type: str
    """"""
    updated_at: str
    """"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    attributes: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    relationships: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""
    updated_at: AirbyteSortOrder
    """"""


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


# ===== FLOWS SEARCH TYPES =====

class FlowsSearchFilter(TypedDict, total=False):
    """Available fields for filtering flows search queries."""
    attributes: dict[str, Any] | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    relationships: dict[str, Any] | None
    """"""
    type: str | None
    """"""
    updated: str | None
    """"""


class FlowsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    relationships: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""
    updated: list[str]
    """"""


class FlowsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    relationships: Any
    """"""
    type: Any
    """"""
    updated: Any
    """"""


class FlowsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    id: str
    """"""
    links: str
    """"""
    relationships: str
    """"""
    type: str
    """"""
    updated: str
    """"""


class FlowsSortFilter(TypedDict, total=False):
    """Available fields for sorting flows search results."""
    attributes: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    relationships: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""
    updated: AirbyteSortOrder
    """"""


# Entity-specific condition types for flows
class FlowsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FlowsSearchFilter


class FlowsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FlowsSearchFilter


class FlowsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FlowsSearchFilter


class FlowsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FlowsSearchFilter


class FlowsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FlowsSearchFilter


class FlowsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FlowsSearchFilter


class FlowsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FlowsStringFilter


class FlowsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FlowsStringFilter


class FlowsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FlowsStringFilter


class FlowsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FlowsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FlowsInCondition = TypedDict("FlowsInCondition", {"in": FlowsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FlowsNotCondition = TypedDict("FlowsNotCondition", {"not": "FlowsCondition"}, total=False)
"""Negates the nested condition."""

FlowsAndCondition = TypedDict("FlowsAndCondition", {"and": "list[FlowsCondition]"}, total=False)
"""True if all nested conditions are true."""

FlowsOrCondition = TypedDict("FlowsOrCondition", {"or": "list[FlowsCondition]"}, total=False)
"""True if any nested condition is true."""

FlowsAnyCondition = TypedDict("FlowsAnyCondition", {"any": FlowsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all flows condition types
FlowsCondition = (
    FlowsEqCondition
    | FlowsNeqCondition
    | FlowsGtCondition
    | FlowsGteCondition
    | FlowsLtCondition
    | FlowsLteCondition
    | FlowsInCondition
    | FlowsLikeCondition
    | FlowsFuzzyCondition
    | FlowsKeywordCondition
    | FlowsContainsCondition
    | FlowsNotCondition
    | FlowsAndCondition
    | FlowsOrCondition
    | FlowsAnyCondition
)


class FlowsSearchQuery(TypedDict, total=False):
    """Search query for flows entity."""
    filter: FlowsCondition
    sort: list[FlowsSortFilter]


# ===== METRICS SEARCH TYPES =====

class MetricsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metrics search queries."""
    attributes: dict[str, Any] | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    relationships: dict[str, Any] | None
    """"""
    type: str | None
    """"""
    updated: str | None
    """"""


class MetricsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    relationships: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""
    updated: list[str]
    """"""


class MetricsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    relationships: Any
    """"""
    type: Any
    """"""
    updated: Any
    """"""


class MetricsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    id: str
    """"""
    links: str
    """"""
    relationships: str
    """"""
    type: str
    """"""
    updated: str
    """"""


class MetricsSortFilter(TypedDict, total=False):
    """Available fields for sorting metrics search results."""
    attributes: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    relationships: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""
    updated: AirbyteSortOrder
    """"""


# Entity-specific condition types for metrics
class MetricsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetricsSearchFilter


class MetricsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetricsSearchFilter


class MetricsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetricsSearchFilter


class MetricsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetricsSearchFilter


class MetricsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetricsSearchFilter


class MetricsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetricsSearchFilter


class MetricsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetricsStringFilter


class MetricsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetricsStringFilter


class MetricsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetricsStringFilter


class MetricsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetricsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetricsInCondition = TypedDict("MetricsInCondition", {"in": MetricsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetricsNotCondition = TypedDict("MetricsNotCondition", {"not": "MetricsCondition"}, total=False)
"""Negates the nested condition."""

MetricsAndCondition = TypedDict("MetricsAndCondition", {"and": "list[MetricsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetricsOrCondition = TypedDict("MetricsOrCondition", {"or": "list[MetricsCondition]"}, total=False)
"""True if any nested condition is true."""

MetricsAnyCondition = TypedDict("MetricsAnyCondition", {"any": MetricsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metrics condition types
MetricsCondition = (
    MetricsEqCondition
    | MetricsNeqCondition
    | MetricsGtCondition
    | MetricsGteCondition
    | MetricsLtCondition
    | MetricsLteCondition
    | MetricsInCondition
    | MetricsLikeCondition
    | MetricsFuzzyCondition
    | MetricsKeywordCondition
    | MetricsContainsCondition
    | MetricsNotCondition
    | MetricsAndCondition
    | MetricsOrCondition
    | MetricsAnyCondition
)


class MetricsSearchQuery(TypedDict, total=False):
    """Search query for metrics entity."""
    filter: MetricsCondition
    sort: list[MetricsSortFilter]


# ===== LISTS SEARCH TYPES =====

class ListsSearchFilter(TypedDict, total=False):
    """Available fields for filtering lists search queries."""
    attributes: dict[str, Any] | None
    """"""
    id: str | None
    """"""
    links: dict[str, Any] | None
    """"""
    relationships: dict[str, Any] | None
    """"""
    type: str | None
    """"""
    updated: str | None
    """"""


class ListsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[dict[str, Any]]
    """"""
    id: list[str]
    """"""
    links: list[dict[str, Any]]
    """"""
    relationships: list[dict[str, Any]]
    """"""
    type: list[str]
    """"""
    updated: list[str]
    """"""


class ListsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """"""
    id: Any
    """"""
    links: Any
    """"""
    relationships: Any
    """"""
    type: Any
    """"""
    updated: Any
    """"""


class ListsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """"""
    id: str
    """"""
    links: str
    """"""
    relationships: str
    """"""
    type: str
    """"""
    updated: str
    """"""


class ListsSortFilter(TypedDict, total=False):
    """Available fields for sorting lists search results."""
    attributes: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    links: AirbyteSortOrder
    """"""
    relationships: AirbyteSortOrder
    """"""
    type: AirbyteSortOrder
    """"""
    updated: AirbyteSortOrder
    """"""


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



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
