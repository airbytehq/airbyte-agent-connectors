"""
Type definitions for zendesk-talk connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict
except ImportError:
    from typing import TypedDict  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class PhoneNumbersListParams(TypedDict):
    """Parameters for phone_numbers.list operation"""
    pass

class PhoneNumbersGetParams(TypedDict):
    """Parameters for phone_numbers.get operation"""
    phone_number_id: str

class AddressesListParams(TypedDict):
    """Parameters for addresses.list operation"""
    pass

class AddressesGetParams(TypedDict):
    """Parameters for addresses.get operation"""
    address_id: str

class GreetingsListParams(TypedDict):
    """Parameters for greetings.list operation"""
    pass

class GreetingsGetParams(TypedDict):
    """Parameters for greetings.get operation"""
    greeting_id: str

class GreetingCategoriesListParams(TypedDict):
    """Parameters for greeting_categories.list operation"""
    pass

class GreetingCategoriesGetParams(TypedDict):
    """Parameters for greeting_categories.get operation"""
    greeting_category_id: str

class IvrsListParams(TypedDict):
    """Parameters for ivrs.list operation"""
    pass

class IvrsGetParams(TypedDict):
    """Parameters for ivrs.get operation"""
    ivr_id: str

class AgentsActivityListParams(TypedDict):
    """Parameters for agents_activity.list operation"""
    pass

class AgentsOverviewListParams(TypedDict):
    """Parameters for agents_overview.list operation"""
    pass

class AccountOverviewListParams(TypedDict):
    """Parameters for account_overview.list operation"""
    pass

class CurrentQueueActivityListParams(TypedDict):
    """Parameters for current_queue_activity.list operation"""
    pass

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    start_time: int

class CallLegsListParams(TypedDict):
    """Parameters for call_legs.list operation"""
    start_time: int

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ADDRESSES SEARCH TYPES =====

class AddressesSearchFilter(TypedDict, total=False):
    """Available fields for filtering addresses search queries."""
    city: str | None
    """City of the address"""
    country_code: str | None
    """ISO country code"""
    id: int | None
    """Unique address identifier"""
    name: str | None
    """Name of the address"""
    provider_reference: str | None
    """Provider reference of the address"""
    province: str | None
    """Province of the address"""
    state: str | None
    """State of the address"""
    street: str | None
    """Street of the address"""
    zip: str | None
    """Zip code of the address"""


class AddressesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    city: list[str]
    """City of the address"""
    country_code: list[str]
    """ISO country code"""
    id: list[int]
    """Unique address identifier"""
    name: list[str]
    """Name of the address"""
    provider_reference: list[str]
    """Provider reference of the address"""
    province: list[str]
    """Province of the address"""
    state: list[str]
    """State of the address"""
    street: list[str]
    """Street of the address"""
    zip: list[str]
    """Zip code of the address"""


class AddressesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    city: Any
    """City of the address"""
    country_code: Any
    """ISO country code"""
    id: Any
    """Unique address identifier"""
    name: Any
    """Name of the address"""
    provider_reference: Any
    """Provider reference of the address"""
    province: Any
    """Province of the address"""
    state: Any
    """State of the address"""
    street: Any
    """Street of the address"""
    zip: Any
    """Zip code of the address"""


class AddressesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    city: str
    """City of the address"""
    country_code: str
    """ISO country code"""
    id: str
    """Unique address identifier"""
    name: str
    """Name of the address"""
    provider_reference: str
    """Provider reference of the address"""
    province: str
    """Province of the address"""
    state: str
    """State of the address"""
    street: str
    """Street of the address"""
    zip: str
    """Zip code of the address"""


class AddressesSortFilter(TypedDict, total=False):
    """Available fields for sorting addresses search results."""
    city: AirbyteSortOrder
    """City of the address"""
    country_code: AirbyteSortOrder
    """ISO country code"""
    id: AirbyteSortOrder
    """Unique address identifier"""
    name: AirbyteSortOrder
    """Name of the address"""
    provider_reference: AirbyteSortOrder
    """Provider reference of the address"""
    province: AirbyteSortOrder
    """Province of the address"""
    state: AirbyteSortOrder
    """State of the address"""
    street: AirbyteSortOrder
    """Street of the address"""
    zip: AirbyteSortOrder
    """Zip code of the address"""


# Entity-specific condition types for addresses
class AddressesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AddressesSearchFilter


class AddressesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AddressesSearchFilter


class AddressesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AddressesSearchFilter


class AddressesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AddressesSearchFilter


class AddressesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AddressesSearchFilter


class AddressesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AddressesSearchFilter


class AddressesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AddressesStringFilter


class AddressesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AddressesStringFilter


class AddressesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AddressesStringFilter


class AddressesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AddressesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AddressesInCondition = TypedDict("AddressesInCondition", {"in": AddressesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AddressesNotCondition = TypedDict("AddressesNotCondition", {"not": "AddressesCondition"}, total=False)
"""Negates the nested condition."""

AddressesAndCondition = TypedDict("AddressesAndCondition", {"and": "list[AddressesCondition]"}, total=False)
"""True if all nested conditions are true."""

AddressesOrCondition = TypedDict("AddressesOrCondition", {"or": "list[AddressesCondition]"}, total=False)
"""True if any nested condition is true."""

AddressesAnyCondition = TypedDict("AddressesAnyCondition", {"any": AddressesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all addresses condition types
AddressesCondition = (
    AddressesEqCondition
    | AddressesNeqCondition
    | AddressesGtCondition
    | AddressesGteCondition
    | AddressesLtCondition
    | AddressesLteCondition
    | AddressesInCondition
    | AddressesLikeCondition
    | AddressesFuzzyCondition
    | AddressesKeywordCondition
    | AddressesContainsCondition
    | AddressesNotCondition
    | AddressesAndCondition
    | AddressesOrCondition
    | AddressesAnyCondition
)


class AddressesSearchQuery(TypedDict, total=False):
    """Search query for addresses entity."""
    filter: AddressesCondition
    sort: list[AddressesSortFilter]


# ===== AGENTS_ACTIVITY SEARCH TYPES =====

class AgentsActivitySearchFilter(TypedDict, total=False):
    """Available fields for filtering agents_activity search queries."""
    accepted_third_party_conferences: int | None
    """Accepted third party conferences"""
    accepted_transfers: int | None
    """Total transfers accepted"""
    agent_id: int | None
    """Agent ID"""
    agent_state: str | None
    """Agent state: online, offline, away, or transfers_only"""
    available_time: int | None
    """Total time agent was available to answer calls"""
    avatar_url: str | None
    """URL to agent avatar"""
    average_hold_time: int | None
    """Average hold time per call"""
    average_talk_time: int | None
    """Average talk time per call"""
    average_wrap_up_time: int | None
    """Average wrap-up time per call"""
    away_time: int | None
    """Total time agent was set to away"""
    call_status: str | None
    """Agent call status: on_call, wrap_up, or null"""
    calls_accepted: int | None
    """Total calls accepted"""
    calls_denied: int | None
    """Total calls denied"""
    calls_missed: int | None
    """Total calls missed"""
    calls_put_on_hold: int | None
    """Total calls placed on hold"""
    forwarding_number: str | None
    """Forwarding number set by the agent"""
    name: str | None
    """Agent name"""
    online_time: int | None
    """Total online time"""
    started_third_party_conferences: int | None
    """Started third party conferences"""
    started_transfers: int | None
    """Total transfers started"""
    total_call_duration: int | None
    """Total call duration"""
    total_hold_time: int | None
    """Total hold time across all calls"""
    total_talk_time: int | None
    """Total talk time (excludes hold)"""
    total_wrap_up_time: int | None
    """Total wrap-up time"""
    transfers_only_time: int | None
    """Total time in transfers-only mode"""
    via: str | None
    """Channel the agent is registered on"""


class AgentsActivityInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    accepted_third_party_conferences: list[int]
    """Accepted third party conferences"""
    accepted_transfers: list[int]
    """Total transfers accepted"""
    agent_id: list[int]
    """Agent ID"""
    agent_state: list[str]
    """Agent state: online, offline, away, or transfers_only"""
    available_time: list[int]
    """Total time agent was available to answer calls"""
    avatar_url: list[str]
    """URL to agent avatar"""
    average_hold_time: list[int]
    """Average hold time per call"""
    average_talk_time: list[int]
    """Average talk time per call"""
    average_wrap_up_time: list[int]
    """Average wrap-up time per call"""
    away_time: list[int]
    """Total time agent was set to away"""
    call_status: list[str]
    """Agent call status: on_call, wrap_up, or null"""
    calls_accepted: list[int]
    """Total calls accepted"""
    calls_denied: list[int]
    """Total calls denied"""
    calls_missed: list[int]
    """Total calls missed"""
    calls_put_on_hold: list[int]
    """Total calls placed on hold"""
    forwarding_number: list[str]
    """Forwarding number set by the agent"""
    name: list[str]
    """Agent name"""
    online_time: list[int]
    """Total online time"""
    started_third_party_conferences: list[int]
    """Started third party conferences"""
    started_transfers: list[int]
    """Total transfers started"""
    total_call_duration: list[int]
    """Total call duration"""
    total_hold_time: list[int]
    """Total hold time across all calls"""
    total_talk_time: list[int]
    """Total talk time (excludes hold)"""
    total_wrap_up_time: list[int]
    """Total wrap-up time"""
    transfers_only_time: list[int]
    """Total time in transfers-only mode"""
    via: list[str]
    """Channel the agent is registered on"""


class AgentsActivityAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    accepted_third_party_conferences: Any
    """Accepted third party conferences"""
    accepted_transfers: Any
    """Total transfers accepted"""
    agent_id: Any
    """Agent ID"""
    agent_state: Any
    """Agent state: online, offline, away, or transfers_only"""
    available_time: Any
    """Total time agent was available to answer calls"""
    avatar_url: Any
    """URL to agent avatar"""
    average_hold_time: Any
    """Average hold time per call"""
    average_talk_time: Any
    """Average talk time per call"""
    average_wrap_up_time: Any
    """Average wrap-up time per call"""
    away_time: Any
    """Total time agent was set to away"""
    call_status: Any
    """Agent call status: on_call, wrap_up, or null"""
    calls_accepted: Any
    """Total calls accepted"""
    calls_denied: Any
    """Total calls denied"""
    calls_missed: Any
    """Total calls missed"""
    calls_put_on_hold: Any
    """Total calls placed on hold"""
    forwarding_number: Any
    """Forwarding number set by the agent"""
    name: Any
    """Agent name"""
    online_time: Any
    """Total online time"""
    started_third_party_conferences: Any
    """Started third party conferences"""
    started_transfers: Any
    """Total transfers started"""
    total_call_duration: Any
    """Total call duration"""
    total_hold_time: Any
    """Total hold time across all calls"""
    total_talk_time: Any
    """Total talk time (excludes hold)"""
    total_wrap_up_time: Any
    """Total wrap-up time"""
    transfers_only_time: Any
    """Total time in transfers-only mode"""
    via: Any
    """Channel the agent is registered on"""


class AgentsActivityStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    accepted_third_party_conferences: str
    """Accepted third party conferences"""
    accepted_transfers: str
    """Total transfers accepted"""
    agent_id: str
    """Agent ID"""
    agent_state: str
    """Agent state: online, offline, away, or transfers_only"""
    available_time: str
    """Total time agent was available to answer calls"""
    avatar_url: str
    """URL to agent avatar"""
    average_hold_time: str
    """Average hold time per call"""
    average_talk_time: str
    """Average talk time per call"""
    average_wrap_up_time: str
    """Average wrap-up time per call"""
    away_time: str
    """Total time agent was set to away"""
    call_status: str
    """Agent call status: on_call, wrap_up, or null"""
    calls_accepted: str
    """Total calls accepted"""
    calls_denied: str
    """Total calls denied"""
    calls_missed: str
    """Total calls missed"""
    calls_put_on_hold: str
    """Total calls placed on hold"""
    forwarding_number: str
    """Forwarding number set by the agent"""
    name: str
    """Agent name"""
    online_time: str
    """Total online time"""
    started_third_party_conferences: str
    """Started third party conferences"""
    started_transfers: str
    """Total transfers started"""
    total_call_duration: str
    """Total call duration"""
    total_hold_time: str
    """Total hold time across all calls"""
    total_talk_time: str
    """Total talk time (excludes hold)"""
    total_wrap_up_time: str
    """Total wrap-up time"""
    transfers_only_time: str
    """Total time in transfers-only mode"""
    via: str
    """Channel the agent is registered on"""


class AgentsActivitySortFilter(TypedDict, total=False):
    """Available fields for sorting agents_activity search results."""
    accepted_third_party_conferences: AirbyteSortOrder
    """Accepted third party conferences"""
    accepted_transfers: AirbyteSortOrder
    """Total transfers accepted"""
    agent_id: AirbyteSortOrder
    """Agent ID"""
    agent_state: AirbyteSortOrder
    """Agent state: online, offline, away, or transfers_only"""
    available_time: AirbyteSortOrder
    """Total time agent was available to answer calls"""
    avatar_url: AirbyteSortOrder
    """URL to agent avatar"""
    average_hold_time: AirbyteSortOrder
    """Average hold time per call"""
    average_talk_time: AirbyteSortOrder
    """Average talk time per call"""
    average_wrap_up_time: AirbyteSortOrder
    """Average wrap-up time per call"""
    away_time: AirbyteSortOrder
    """Total time agent was set to away"""
    call_status: AirbyteSortOrder
    """Agent call status: on_call, wrap_up, or null"""
    calls_accepted: AirbyteSortOrder
    """Total calls accepted"""
    calls_denied: AirbyteSortOrder
    """Total calls denied"""
    calls_missed: AirbyteSortOrder
    """Total calls missed"""
    calls_put_on_hold: AirbyteSortOrder
    """Total calls placed on hold"""
    forwarding_number: AirbyteSortOrder
    """Forwarding number set by the agent"""
    name: AirbyteSortOrder
    """Agent name"""
    online_time: AirbyteSortOrder
    """Total online time"""
    started_third_party_conferences: AirbyteSortOrder
    """Started third party conferences"""
    started_transfers: AirbyteSortOrder
    """Total transfers started"""
    total_call_duration: AirbyteSortOrder
    """Total call duration"""
    total_hold_time: AirbyteSortOrder
    """Total hold time across all calls"""
    total_talk_time: AirbyteSortOrder
    """Total talk time (excludes hold)"""
    total_wrap_up_time: AirbyteSortOrder
    """Total wrap-up time"""
    transfers_only_time: AirbyteSortOrder
    """Total time in transfers-only mode"""
    via: AirbyteSortOrder
    """Channel the agent is registered on"""


# Entity-specific condition types for agents_activity
class AgentsActivityEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AgentsActivitySearchFilter


class AgentsActivityNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AgentsActivitySearchFilter


class AgentsActivityGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AgentsActivitySearchFilter


class AgentsActivityGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AgentsActivitySearchFilter


class AgentsActivityLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AgentsActivitySearchFilter


class AgentsActivityLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AgentsActivitySearchFilter


class AgentsActivityLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AgentsActivityStringFilter


class AgentsActivityFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AgentsActivityStringFilter


class AgentsActivityKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AgentsActivityStringFilter


class AgentsActivityContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AgentsActivityAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AgentsActivityInCondition = TypedDict("AgentsActivityInCondition", {"in": AgentsActivityInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AgentsActivityNotCondition = TypedDict("AgentsActivityNotCondition", {"not": "AgentsActivityCondition"}, total=False)
"""Negates the nested condition."""

AgentsActivityAndCondition = TypedDict("AgentsActivityAndCondition", {"and": "list[AgentsActivityCondition]"}, total=False)
"""True if all nested conditions are true."""

AgentsActivityOrCondition = TypedDict("AgentsActivityOrCondition", {"or": "list[AgentsActivityCondition]"}, total=False)
"""True if any nested condition is true."""

AgentsActivityAnyCondition = TypedDict("AgentsActivityAnyCondition", {"any": AgentsActivityAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all agents_activity condition types
AgentsActivityCondition = (
    AgentsActivityEqCondition
    | AgentsActivityNeqCondition
    | AgentsActivityGtCondition
    | AgentsActivityGteCondition
    | AgentsActivityLtCondition
    | AgentsActivityLteCondition
    | AgentsActivityInCondition
    | AgentsActivityLikeCondition
    | AgentsActivityFuzzyCondition
    | AgentsActivityKeywordCondition
    | AgentsActivityContainsCondition
    | AgentsActivityNotCondition
    | AgentsActivityAndCondition
    | AgentsActivityOrCondition
    | AgentsActivityAnyCondition
)


class AgentsActivitySearchQuery(TypedDict, total=False):
    """Search query for agents_activity entity."""
    filter: AgentsActivityCondition
    sort: list[AgentsActivitySortFilter]


# ===== AGENTS_OVERVIEW SEARCH TYPES =====

class AgentsOverviewSearchFilter(TypedDict, total=False):
    """Available fields for filtering agents_overview search queries."""
    average_accepted_transfers: int | None
    """Average accepted transfers"""
    average_available_time: int | None
    """Average available time"""
    average_away_time: int | None
    """Average away time"""
    average_calls_accepted: int | None
    """Average calls accepted"""
    average_calls_denied: int | None
    """Average calls denied"""
    average_calls_missed: int | None
    """Average calls missed"""
    average_calls_put_on_hold: int | None
    """Average calls put on hold"""
    average_hold_time: int | None
    """Average hold time"""
    average_online_time: int | None
    """Average online time"""
    average_started_transfers: int | None
    """Average started transfers"""
    average_talk_time: int | None
    """Average talk time"""
    average_transfers_only_time: int | None
    """Average transfers-only time"""
    average_wrap_up_time: int | None
    """Average wrap-up time"""
    current_timestamp: int | None
    """Current timestamp"""
    total_accepted_transfers: int | None
    """Total accepted transfers"""
    total_calls_accepted: int | None
    """Total calls accepted"""
    total_calls_denied: int | None
    """Total calls denied"""
    total_calls_missed: int | None
    """Total calls missed"""
    total_calls_put_on_hold: int | None
    """Total calls put on hold"""
    total_hold_time: int | None
    """Total hold time"""
    total_started_transfers: int | None
    """Total started transfers"""
    total_talk_time: int | None
    """Total talk time"""
    total_wrap_up_time: int | None
    """Total wrap-up time"""


class AgentsOverviewInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    average_accepted_transfers: list[int]
    """Average accepted transfers"""
    average_available_time: list[int]
    """Average available time"""
    average_away_time: list[int]
    """Average away time"""
    average_calls_accepted: list[int]
    """Average calls accepted"""
    average_calls_denied: list[int]
    """Average calls denied"""
    average_calls_missed: list[int]
    """Average calls missed"""
    average_calls_put_on_hold: list[int]
    """Average calls put on hold"""
    average_hold_time: list[int]
    """Average hold time"""
    average_online_time: list[int]
    """Average online time"""
    average_started_transfers: list[int]
    """Average started transfers"""
    average_talk_time: list[int]
    """Average talk time"""
    average_transfers_only_time: list[int]
    """Average transfers-only time"""
    average_wrap_up_time: list[int]
    """Average wrap-up time"""
    current_timestamp: list[int]
    """Current timestamp"""
    total_accepted_transfers: list[int]
    """Total accepted transfers"""
    total_calls_accepted: list[int]
    """Total calls accepted"""
    total_calls_denied: list[int]
    """Total calls denied"""
    total_calls_missed: list[int]
    """Total calls missed"""
    total_calls_put_on_hold: list[int]
    """Total calls put on hold"""
    total_hold_time: list[int]
    """Total hold time"""
    total_started_transfers: list[int]
    """Total started transfers"""
    total_talk_time: list[int]
    """Total talk time"""
    total_wrap_up_time: list[int]
    """Total wrap-up time"""


class AgentsOverviewAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    average_accepted_transfers: Any
    """Average accepted transfers"""
    average_available_time: Any
    """Average available time"""
    average_away_time: Any
    """Average away time"""
    average_calls_accepted: Any
    """Average calls accepted"""
    average_calls_denied: Any
    """Average calls denied"""
    average_calls_missed: Any
    """Average calls missed"""
    average_calls_put_on_hold: Any
    """Average calls put on hold"""
    average_hold_time: Any
    """Average hold time"""
    average_online_time: Any
    """Average online time"""
    average_started_transfers: Any
    """Average started transfers"""
    average_talk_time: Any
    """Average talk time"""
    average_transfers_only_time: Any
    """Average transfers-only time"""
    average_wrap_up_time: Any
    """Average wrap-up time"""
    current_timestamp: Any
    """Current timestamp"""
    total_accepted_transfers: Any
    """Total accepted transfers"""
    total_calls_accepted: Any
    """Total calls accepted"""
    total_calls_denied: Any
    """Total calls denied"""
    total_calls_missed: Any
    """Total calls missed"""
    total_calls_put_on_hold: Any
    """Total calls put on hold"""
    total_hold_time: Any
    """Total hold time"""
    total_started_transfers: Any
    """Total started transfers"""
    total_talk_time: Any
    """Total talk time"""
    total_wrap_up_time: Any
    """Total wrap-up time"""


class AgentsOverviewStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    average_accepted_transfers: str
    """Average accepted transfers"""
    average_available_time: str
    """Average available time"""
    average_away_time: str
    """Average away time"""
    average_calls_accepted: str
    """Average calls accepted"""
    average_calls_denied: str
    """Average calls denied"""
    average_calls_missed: str
    """Average calls missed"""
    average_calls_put_on_hold: str
    """Average calls put on hold"""
    average_hold_time: str
    """Average hold time"""
    average_online_time: str
    """Average online time"""
    average_started_transfers: str
    """Average started transfers"""
    average_talk_time: str
    """Average talk time"""
    average_transfers_only_time: str
    """Average transfers-only time"""
    average_wrap_up_time: str
    """Average wrap-up time"""
    current_timestamp: str
    """Current timestamp"""
    total_accepted_transfers: str
    """Total accepted transfers"""
    total_calls_accepted: str
    """Total calls accepted"""
    total_calls_denied: str
    """Total calls denied"""
    total_calls_missed: str
    """Total calls missed"""
    total_calls_put_on_hold: str
    """Total calls put on hold"""
    total_hold_time: str
    """Total hold time"""
    total_started_transfers: str
    """Total started transfers"""
    total_talk_time: str
    """Total talk time"""
    total_wrap_up_time: str
    """Total wrap-up time"""


class AgentsOverviewSortFilter(TypedDict, total=False):
    """Available fields for sorting agents_overview search results."""
    average_accepted_transfers: AirbyteSortOrder
    """Average accepted transfers"""
    average_available_time: AirbyteSortOrder
    """Average available time"""
    average_away_time: AirbyteSortOrder
    """Average away time"""
    average_calls_accepted: AirbyteSortOrder
    """Average calls accepted"""
    average_calls_denied: AirbyteSortOrder
    """Average calls denied"""
    average_calls_missed: AirbyteSortOrder
    """Average calls missed"""
    average_calls_put_on_hold: AirbyteSortOrder
    """Average calls put on hold"""
    average_hold_time: AirbyteSortOrder
    """Average hold time"""
    average_online_time: AirbyteSortOrder
    """Average online time"""
    average_started_transfers: AirbyteSortOrder
    """Average started transfers"""
    average_talk_time: AirbyteSortOrder
    """Average talk time"""
    average_transfers_only_time: AirbyteSortOrder
    """Average transfers-only time"""
    average_wrap_up_time: AirbyteSortOrder
    """Average wrap-up time"""
    current_timestamp: AirbyteSortOrder
    """Current timestamp"""
    total_accepted_transfers: AirbyteSortOrder
    """Total accepted transfers"""
    total_calls_accepted: AirbyteSortOrder
    """Total calls accepted"""
    total_calls_denied: AirbyteSortOrder
    """Total calls denied"""
    total_calls_missed: AirbyteSortOrder
    """Total calls missed"""
    total_calls_put_on_hold: AirbyteSortOrder
    """Total calls put on hold"""
    total_hold_time: AirbyteSortOrder
    """Total hold time"""
    total_started_transfers: AirbyteSortOrder
    """Total started transfers"""
    total_talk_time: AirbyteSortOrder
    """Total talk time"""
    total_wrap_up_time: AirbyteSortOrder
    """Total wrap-up time"""


# Entity-specific condition types for agents_overview
class AgentsOverviewEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AgentsOverviewSearchFilter


class AgentsOverviewNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AgentsOverviewSearchFilter


class AgentsOverviewGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AgentsOverviewSearchFilter


class AgentsOverviewGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AgentsOverviewSearchFilter


class AgentsOverviewLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AgentsOverviewSearchFilter


class AgentsOverviewLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AgentsOverviewSearchFilter


class AgentsOverviewLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AgentsOverviewStringFilter


class AgentsOverviewFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AgentsOverviewStringFilter


class AgentsOverviewKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AgentsOverviewStringFilter


class AgentsOverviewContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AgentsOverviewAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AgentsOverviewInCondition = TypedDict("AgentsOverviewInCondition", {"in": AgentsOverviewInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AgentsOverviewNotCondition = TypedDict("AgentsOverviewNotCondition", {"not": "AgentsOverviewCondition"}, total=False)
"""Negates the nested condition."""

AgentsOverviewAndCondition = TypedDict("AgentsOverviewAndCondition", {"and": "list[AgentsOverviewCondition]"}, total=False)
"""True if all nested conditions are true."""

AgentsOverviewOrCondition = TypedDict("AgentsOverviewOrCondition", {"or": "list[AgentsOverviewCondition]"}, total=False)
"""True if any nested condition is true."""

AgentsOverviewAnyCondition = TypedDict("AgentsOverviewAnyCondition", {"any": AgentsOverviewAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all agents_overview condition types
AgentsOverviewCondition = (
    AgentsOverviewEqCondition
    | AgentsOverviewNeqCondition
    | AgentsOverviewGtCondition
    | AgentsOverviewGteCondition
    | AgentsOverviewLtCondition
    | AgentsOverviewLteCondition
    | AgentsOverviewInCondition
    | AgentsOverviewLikeCondition
    | AgentsOverviewFuzzyCondition
    | AgentsOverviewKeywordCondition
    | AgentsOverviewContainsCondition
    | AgentsOverviewNotCondition
    | AgentsOverviewAndCondition
    | AgentsOverviewOrCondition
    | AgentsOverviewAnyCondition
)


class AgentsOverviewSearchQuery(TypedDict, total=False):
    """Search query for agents_overview entity."""
    filter: AgentsOverviewCondition
    sort: list[AgentsOverviewSortFilter]


# ===== GREETING_CATEGORIES SEARCH TYPES =====

class GreetingCategoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering greeting_categories search queries."""
    id: int | None
    """Greeting category ID"""
    name: str | None
    """Name of the greeting category"""


class GreetingCategoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Greeting category ID"""
    name: list[str]
    """Name of the greeting category"""


class GreetingCategoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Greeting category ID"""
    name: Any
    """Name of the greeting category"""


class GreetingCategoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Greeting category ID"""
    name: str
    """Name of the greeting category"""


class GreetingCategoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting greeting_categories search results."""
    id: AirbyteSortOrder
    """Greeting category ID"""
    name: AirbyteSortOrder
    """Name of the greeting category"""


# Entity-specific condition types for greeting_categories
class GreetingCategoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GreetingCategoriesSearchFilter


class GreetingCategoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GreetingCategoriesSearchFilter


class GreetingCategoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GreetingCategoriesSearchFilter


class GreetingCategoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GreetingCategoriesSearchFilter


class GreetingCategoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GreetingCategoriesSearchFilter


class GreetingCategoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GreetingCategoriesSearchFilter


class GreetingCategoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GreetingCategoriesStringFilter


class GreetingCategoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GreetingCategoriesStringFilter


class GreetingCategoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GreetingCategoriesStringFilter


class GreetingCategoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GreetingCategoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GreetingCategoriesInCondition = TypedDict("GreetingCategoriesInCondition", {"in": GreetingCategoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GreetingCategoriesNotCondition = TypedDict("GreetingCategoriesNotCondition", {"not": "GreetingCategoriesCondition"}, total=False)
"""Negates the nested condition."""

GreetingCategoriesAndCondition = TypedDict("GreetingCategoriesAndCondition", {"and": "list[GreetingCategoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

GreetingCategoriesOrCondition = TypedDict("GreetingCategoriesOrCondition", {"or": "list[GreetingCategoriesCondition]"}, total=False)
"""True if any nested condition is true."""

GreetingCategoriesAnyCondition = TypedDict("GreetingCategoriesAnyCondition", {"any": GreetingCategoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all greeting_categories condition types
GreetingCategoriesCondition = (
    GreetingCategoriesEqCondition
    | GreetingCategoriesNeqCondition
    | GreetingCategoriesGtCondition
    | GreetingCategoriesGteCondition
    | GreetingCategoriesLtCondition
    | GreetingCategoriesLteCondition
    | GreetingCategoriesInCondition
    | GreetingCategoriesLikeCondition
    | GreetingCategoriesFuzzyCondition
    | GreetingCategoriesKeywordCondition
    | GreetingCategoriesContainsCondition
    | GreetingCategoriesNotCondition
    | GreetingCategoriesAndCondition
    | GreetingCategoriesOrCondition
    | GreetingCategoriesAnyCondition
)


class GreetingCategoriesSearchQuery(TypedDict, total=False):
    """Search query for greeting_categories entity."""
    filter: GreetingCategoriesCondition
    sort: list[GreetingCategoriesSortFilter]


# ===== GREETINGS SEARCH TYPES =====

class GreetingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering greetings search queries."""
    active: bool | None
    """Whether the greeting is associated with phone numbers"""
    audio_name: str | None
    """Audio file name"""
    audio_url: str | None
    """Path to the greeting sound file"""
    category_id: int | None
    """ID of the greeting category"""
    default: bool | None
    """Whether this is a system default greeting"""
    default_lang: bool | None
    """Whether the greeting has a default language"""
    has_sub_settings: bool | None
    """Sub-settings for categorized greetings"""
    id: str | None
    """Greeting ID"""
    ivr_ids: list[Any] | None
    """IDs of IVRs associated with the greeting"""
    name: str | None
    """Name of the greeting"""
    pending: bool | None
    """Whether the greeting is pending"""
    phone_number_ids: list[Any] | None
    """IDs of phone numbers associated with the greeting"""
    upload_id: int | None
    """Upload ID associated with the greeting"""


class GreetingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Whether the greeting is associated with phone numbers"""
    audio_name: list[str]
    """Audio file name"""
    audio_url: list[str]
    """Path to the greeting sound file"""
    category_id: list[int]
    """ID of the greeting category"""
    default: list[bool]
    """Whether this is a system default greeting"""
    default_lang: list[bool]
    """Whether the greeting has a default language"""
    has_sub_settings: list[bool]
    """Sub-settings for categorized greetings"""
    id: list[str]
    """Greeting ID"""
    ivr_ids: list[list[Any]]
    """IDs of IVRs associated with the greeting"""
    name: list[str]
    """Name of the greeting"""
    pending: list[bool]
    """Whether the greeting is pending"""
    phone_number_ids: list[list[Any]]
    """IDs of phone numbers associated with the greeting"""
    upload_id: list[int]
    """Upload ID associated with the greeting"""


class GreetingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Whether the greeting is associated with phone numbers"""
    audio_name: Any
    """Audio file name"""
    audio_url: Any
    """Path to the greeting sound file"""
    category_id: Any
    """ID of the greeting category"""
    default: Any
    """Whether this is a system default greeting"""
    default_lang: Any
    """Whether the greeting has a default language"""
    has_sub_settings: Any
    """Sub-settings for categorized greetings"""
    id: Any
    """Greeting ID"""
    ivr_ids: Any
    """IDs of IVRs associated with the greeting"""
    name: Any
    """Name of the greeting"""
    pending: Any
    """Whether the greeting is pending"""
    phone_number_ids: Any
    """IDs of phone numbers associated with the greeting"""
    upload_id: Any
    """Upload ID associated with the greeting"""


class GreetingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Whether the greeting is associated with phone numbers"""
    audio_name: str
    """Audio file name"""
    audio_url: str
    """Path to the greeting sound file"""
    category_id: str
    """ID of the greeting category"""
    default: str
    """Whether this is a system default greeting"""
    default_lang: str
    """Whether the greeting has a default language"""
    has_sub_settings: str
    """Sub-settings for categorized greetings"""
    id: str
    """Greeting ID"""
    ivr_ids: str
    """IDs of IVRs associated with the greeting"""
    name: str
    """Name of the greeting"""
    pending: str
    """Whether the greeting is pending"""
    phone_number_ids: str
    """IDs of phone numbers associated with the greeting"""
    upload_id: str
    """Upload ID associated with the greeting"""


class GreetingsSortFilter(TypedDict, total=False):
    """Available fields for sorting greetings search results."""
    active: AirbyteSortOrder
    """Whether the greeting is associated with phone numbers"""
    audio_name: AirbyteSortOrder
    """Audio file name"""
    audio_url: AirbyteSortOrder
    """Path to the greeting sound file"""
    category_id: AirbyteSortOrder
    """ID of the greeting category"""
    default: AirbyteSortOrder
    """Whether this is a system default greeting"""
    default_lang: AirbyteSortOrder
    """Whether the greeting has a default language"""
    has_sub_settings: AirbyteSortOrder
    """Sub-settings for categorized greetings"""
    id: AirbyteSortOrder
    """Greeting ID"""
    ivr_ids: AirbyteSortOrder
    """IDs of IVRs associated with the greeting"""
    name: AirbyteSortOrder
    """Name of the greeting"""
    pending: AirbyteSortOrder
    """Whether the greeting is pending"""
    phone_number_ids: AirbyteSortOrder
    """IDs of phone numbers associated with the greeting"""
    upload_id: AirbyteSortOrder
    """Upload ID associated with the greeting"""


# Entity-specific condition types for greetings
class GreetingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GreetingsSearchFilter


class GreetingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GreetingsSearchFilter


class GreetingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GreetingsSearchFilter


class GreetingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GreetingsSearchFilter


class GreetingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GreetingsSearchFilter


class GreetingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GreetingsSearchFilter


class GreetingsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GreetingsStringFilter


class GreetingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GreetingsStringFilter


class GreetingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GreetingsStringFilter


class GreetingsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GreetingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GreetingsInCondition = TypedDict("GreetingsInCondition", {"in": GreetingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GreetingsNotCondition = TypedDict("GreetingsNotCondition", {"not": "GreetingsCondition"}, total=False)
"""Negates the nested condition."""

GreetingsAndCondition = TypedDict("GreetingsAndCondition", {"and": "list[GreetingsCondition]"}, total=False)
"""True if all nested conditions are true."""

GreetingsOrCondition = TypedDict("GreetingsOrCondition", {"or": "list[GreetingsCondition]"}, total=False)
"""True if any nested condition is true."""

GreetingsAnyCondition = TypedDict("GreetingsAnyCondition", {"any": GreetingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all greetings condition types
GreetingsCondition = (
    GreetingsEqCondition
    | GreetingsNeqCondition
    | GreetingsGtCondition
    | GreetingsGteCondition
    | GreetingsLtCondition
    | GreetingsLteCondition
    | GreetingsInCondition
    | GreetingsLikeCondition
    | GreetingsFuzzyCondition
    | GreetingsKeywordCondition
    | GreetingsContainsCondition
    | GreetingsNotCondition
    | GreetingsAndCondition
    | GreetingsOrCondition
    | GreetingsAnyCondition
)


class GreetingsSearchQuery(TypedDict, total=False):
    """Search query for greetings entity."""
    filter: GreetingsCondition
    sort: list[GreetingsSortFilter]


# ===== PHONE_NUMBERS SEARCH TYPES =====

class PhoneNumbersSearchFilter(TypedDict, total=False):
    """Available fields for filtering phone_numbers search queries."""
    call_recording_consent: str | None
    """What call recording consent is set to"""
    capabilities: dict[str, Any] | None
    """Phone number capabilities (sms, mms, voice)"""
    categorised_greetings: dict[str, Any] | None
    """Greeting category IDs and names"""
    categorised_greetings_with_sub_settings: dict[str, Any] | None
    """Greeting categories with associated settings"""
    country_code: str | None
    """ISO country code for the number"""
    created_at: str | None
    """Date and time the phone number was created"""
    default_greeting_ids: list[Any] | None
    """Names of default system greetings"""
    default_group_id: int | None
    """Default group ID"""
    display_number: str | None
    """Formatted phone number"""
    external: bool | None
    """Whether this is an external caller ID number"""
    failover_number: str | None
    """Failover number associated with the phone number"""
    greeting_ids: list[Any] | None
    """Custom greeting IDs associated with the phone number"""
    group_ids: list[Any] | None
    """Array of associated group IDs"""
    id: int | None
    """Unique phone number identifier"""
    ivr_id: int | None
    """ID of IVR associated with the phone number"""
    line_type: str | None
    """Type of line (phone or digital)"""
    location: str | None
    """Geographical location of the number"""
    name: str | None
    """Nickname if set, otherwise the display number"""
    nickname: str | None
    """Nickname of the phone number"""
    number: str | None
    """Phone number digits"""
    outbound_enabled: bool | None
    """Whether outbound calls are enabled"""
    priority: int | None
    """Priority level of the phone number"""
    recorded: bool | None
    """Whether calls are recorded"""
    schedule_id: int | None
    """ID of schedule associated with the phone number"""
    sms_enabled: bool | None
    """Whether SMS is enabled"""
    sms_group_id: int | None
    """Group associated with SMS"""
    token: str | None
    """Generated token unique for the phone number"""
    toll_free: bool | None
    """Whether the number is toll-free"""
    transcription: bool | None
    """Whether voicemail transcription is enabled"""
    voice_enabled: bool | None
    """Whether voice is enabled"""


class PhoneNumbersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    call_recording_consent: list[str]
    """What call recording consent is set to"""
    capabilities: list[dict[str, Any]]
    """Phone number capabilities (sms, mms, voice)"""
    categorised_greetings: list[dict[str, Any]]
    """Greeting category IDs and names"""
    categorised_greetings_with_sub_settings: list[dict[str, Any]]
    """Greeting categories with associated settings"""
    country_code: list[str]
    """ISO country code for the number"""
    created_at: list[str]
    """Date and time the phone number was created"""
    default_greeting_ids: list[list[Any]]
    """Names of default system greetings"""
    default_group_id: list[int]
    """Default group ID"""
    display_number: list[str]
    """Formatted phone number"""
    external: list[bool]
    """Whether this is an external caller ID number"""
    failover_number: list[str]
    """Failover number associated with the phone number"""
    greeting_ids: list[list[Any]]
    """Custom greeting IDs associated with the phone number"""
    group_ids: list[list[Any]]
    """Array of associated group IDs"""
    id: list[int]
    """Unique phone number identifier"""
    ivr_id: list[int]
    """ID of IVR associated with the phone number"""
    line_type: list[str]
    """Type of line (phone or digital)"""
    location: list[str]
    """Geographical location of the number"""
    name: list[str]
    """Nickname if set, otherwise the display number"""
    nickname: list[str]
    """Nickname of the phone number"""
    number: list[str]
    """Phone number digits"""
    outbound_enabled: list[bool]
    """Whether outbound calls are enabled"""
    priority: list[int]
    """Priority level of the phone number"""
    recorded: list[bool]
    """Whether calls are recorded"""
    schedule_id: list[int]
    """ID of schedule associated with the phone number"""
    sms_enabled: list[bool]
    """Whether SMS is enabled"""
    sms_group_id: list[int]
    """Group associated with SMS"""
    token: list[str]
    """Generated token unique for the phone number"""
    toll_free: list[bool]
    """Whether the number is toll-free"""
    transcription: list[bool]
    """Whether voicemail transcription is enabled"""
    voice_enabled: list[bool]
    """Whether voice is enabled"""


class PhoneNumbersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    call_recording_consent: Any
    """What call recording consent is set to"""
    capabilities: Any
    """Phone number capabilities (sms, mms, voice)"""
    categorised_greetings: Any
    """Greeting category IDs and names"""
    categorised_greetings_with_sub_settings: Any
    """Greeting categories with associated settings"""
    country_code: Any
    """ISO country code for the number"""
    created_at: Any
    """Date and time the phone number was created"""
    default_greeting_ids: Any
    """Names of default system greetings"""
    default_group_id: Any
    """Default group ID"""
    display_number: Any
    """Formatted phone number"""
    external: Any
    """Whether this is an external caller ID number"""
    failover_number: Any
    """Failover number associated with the phone number"""
    greeting_ids: Any
    """Custom greeting IDs associated with the phone number"""
    group_ids: Any
    """Array of associated group IDs"""
    id: Any
    """Unique phone number identifier"""
    ivr_id: Any
    """ID of IVR associated with the phone number"""
    line_type: Any
    """Type of line (phone or digital)"""
    location: Any
    """Geographical location of the number"""
    name: Any
    """Nickname if set, otherwise the display number"""
    nickname: Any
    """Nickname of the phone number"""
    number: Any
    """Phone number digits"""
    outbound_enabled: Any
    """Whether outbound calls are enabled"""
    priority: Any
    """Priority level of the phone number"""
    recorded: Any
    """Whether calls are recorded"""
    schedule_id: Any
    """ID of schedule associated with the phone number"""
    sms_enabled: Any
    """Whether SMS is enabled"""
    sms_group_id: Any
    """Group associated with SMS"""
    token: Any
    """Generated token unique for the phone number"""
    toll_free: Any
    """Whether the number is toll-free"""
    transcription: Any
    """Whether voicemail transcription is enabled"""
    voice_enabled: Any
    """Whether voice is enabled"""


class PhoneNumbersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    call_recording_consent: str
    """What call recording consent is set to"""
    capabilities: str
    """Phone number capabilities (sms, mms, voice)"""
    categorised_greetings: str
    """Greeting category IDs and names"""
    categorised_greetings_with_sub_settings: str
    """Greeting categories with associated settings"""
    country_code: str
    """ISO country code for the number"""
    created_at: str
    """Date and time the phone number was created"""
    default_greeting_ids: str
    """Names of default system greetings"""
    default_group_id: str
    """Default group ID"""
    display_number: str
    """Formatted phone number"""
    external: str
    """Whether this is an external caller ID number"""
    failover_number: str
    """Failover number associated with the phone number"""
    greeting_ids: str
    """Custom greeting IDs associated with the phone number"""
    group_ids: str
    """Array of associated group IDs"""
    id: str
    """Unique phone number identifier"""
    ivr_id: str
    """ID of IVR associated with the phone number"""
    line_type: str
    """Type of line (phone or digital)"""
    location: str
    """Geographical location of the number"""
    name: str
    """Nickname if set, otherwise the display number"""
    nickname: str
    """Nickname of the phone number"""
    number: str
    """Phone number digits"""
    outbound_enabled: str
    """Whether outbound calls are enabled"""
    priority: str
    """Priority level of the phone number"""
    recorded: str
    """Whether calls are recorded"""
    schedule_id: str
    """ID of schedule associated with the phone number"""
    sms_enabled: str
    """Whether SMS is enabled"""
    sms_group_id: str
    """Group associated with SMS"""
    token: str
    """Generated token unique for the phone number"""
    toll_free: str
    """Whether the number is toll-free"""
    transcription: str
    """Whether voicemail transcription is enabled"""
    voice_enabled: str
    """Whether voice is enabled"""


class PhoneNumbersSortFilter(TypedDict, total=False):
    """Available fields for sorting phone_numbers search results."""
    call_recording_consent: AirbyteSortOrder
    """What call recording consent is set to"""
    capabilities: AirbyteSortOrder
    """Phone number capabilities (sms, mms, voice)"""
    categorised_greetings: AirbyteSortOrder
    """Greeting category IDs and names"""
    categorised_greetings_with_sub_settings: AirbyteSortOrder
    """Greeting categories with associated settings"""
    country_code: AirbyteSortOrder
    """ISO country code for the number"""
    created_at: AirbyteSortOrder
    """Date and time the phone number was created"""
    default_greeting_ids: AirbyteSortOrder
    """Names of default system greetings"""
    default_group_id: AirbyteSortOrder
    """Default group ID"""
    display_number: AirbyteSortOrder
    """Formatted phone number"""
    external: AirbyteSortOrder
    """Whether this is an external caller ID number"""
    failover_number: AirbyteSortOrder
    """Failover number associated with the phone number"""
    greeting_ids: AirbyteSortOrder
    """Custom greeting IDs associated with the phone number"""
    group_ids: AirbyteSortOrder
    """Array of associated group IDs"""
    id: AirbyteSortOrder
    """Unique phone number identifier"""
    ivr_id: AirbyteSortOrder
    """ID of IVR associated with the phone number"""
    line_type: AirbyteSortOrder
    """Type of line (phone or digital)"""
    location: AirbyteSortOrder
    """Geographical location of the number"""
    name: AirbyteSortOrder
    """Nickname if set, otherwise the display number"""
    nickname: AirbyteSortOrder
    """Nickname of the phone number"""
    number: AirbyteSortOrder
    """Phone number digits"""
    outbound_enabled: AirbyteSortOrder
    """Whether outbound calls are enabled"""
    priority: AirbyteSortOrder
    """Priority level of the phone number"""
    recorded: AirbyteSortOrder
    """Whether calls are recorded"""
    schedule_id: AirbyteSortOrder
    """ID of schedule associated with the phone number"""
    sms_enabled: AirbyteSortOrder
    """Whether SMS is enabled"""
    sms_group_id: AirbyteSortOrder
    """Group associated with SMS"""
    token: AirbyteSortOrder
    """Generated token unique for the phone number"""
    toll_free: AirbyteSortOrder
    """Whether the number is toll-free"""
    transcription: AirbyteSortOrder
    """Whether voicemail transcription is enabled"""
    voice_enabled: AirbyteSortOrder
    """Whether voice is enabled"""


# Entity-specific condition types for phone_numbers
class PhoneNumbersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PhoneNumbersSearchFilter


class PhoneNumbersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PhoneNumbersSearchFilter


class PhoneNumbersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PhoneNumbersSearchFilter


class PhoneNumbersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PhoneNumbersSearchFilter


class PhoneNumbersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PhoneNumbersSearchFilter


class PhoneNumbersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PhoneNumbersSearchFilter


class PhoneNumbersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PhoneNumbersStringFilter


class PhoneNumbersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PhoneNumbersStringFilter


class PhoneNumbersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PhoneNumbersStringFilter


class PhoneNumbersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PhoneNumbersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PhoneNumbersInCondition = TypedDict("PhoneNumbersInCondition", {"in": PhoneNumbersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PhoneNumbersNotCondition = TypedDict("PhoneNumbersNotCondition", {"not": "PhoneNumbersCondition"}, total=False)
"""Negates the nested condition."""

PhoneNumbersAndCondition = TypedDict("PhoneNumbersAndCondition", {"and": "list[PhoneNumbersCondition]"}, total=False)
"""True if all nested conditions are true."""

PhoneNumbersOrCondition = TypedDict("PhoneNumbersOrCondition", {"or": "list[PhoneNumbersCondition]"}, total=False)
"""True if any nested condition is true."""

PhoneNumbersAnyCondition = TypedDict("PhoneNumbersAnyCondition", {"any": PhoneNumbersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all phone_numbers condition types
PhoneNumbersCondition = (
    PhoneNumbersEqCondition
    | PhoneNumbersNeqCondition
    | PhoneNumbersGtCondition
    | PhoneNumbersGteCondition
    | PhoneNumbersLtCondition
    | PhoneNumbersLteCondition
    | PhoneNumbersInCondition
    | PhoneNumbersLikeCondition
    | PhoneNumbersFuzzyCondition
    | PhoneNumbersKeywordCondition
    | PhoneNumbersContainsCondition
    | PhoneNumbersNotCondition
    | PhoneNumbersAndCondition
    | PhoneNumbersOrCondition
    | PhoneNumbersAnyCondition
)


class PhoneNumbersSearchQuery(TypedDict, total=False):
    """Search query for phone_numbers entity."""
    filter: PhoneNumbersCondition
    sort: list[PhoneNumbersSortFilter]


# ===== CALL_LEGS SEARCH TYPES =====

class CallLegsSearchFilter(TypedDict, total=False):
    """Available fields for filtering call_legs search queries."""
    agent_id: int | None
    """Agent ID"""
    available_via: str | None
    """Channel agent was available through"""
    call_charge: str | None
    """Call charge amount"""
    call_id: int | None
    """Associated call ID"""
    completion_status: str | None
    """Completion status"""
    conference_from: int | None
    """Conference from time"""
    conference_time: int | None
    """Conference duration"""
    conference_to: int | None
    """Conference to time"""
    consultation_from: int | None
    """Consultation from time"""
    consultation_time: int | None
    """Consultation duration"""
    consultation_to: int | None
    """Consultation to time"""
    created_at: str | None
    """Creation timestamp"""
    duration: int | None
    """Duration in seconds"""
    forwarded_to: str | None
    """Number forwarded to"""
    hold_time: int | None
    """Hold time in seconds"""
    id: int | None
    """Call leg ID"""
    minutes_billed: int | None
    """Minutes billed"""
    quality_issues: list[Any] | None
    """Quality issues detected"""
    talk_time: int | None
    """Talk time in seconds"""
    transferred_from: int | None
    """Transferred from agent ID"""
    transferred_to: int | None
    """Transferred to agent ID"""
    type_: str | None
    """Type of call leg"""
    updated_at: str | None
    """Last update timestamp"""
    user_id: int | None
    """User ID"""
    wrap_up_time: int | None
    """Wrap-up time in seconds"""


class CallLegsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    agent_id: list[int]
    """Agent ID"""
    available_via: list[str]
    """Channel agent was available through"""
    call_charge: list[str]
    """Call charge amount"""
    call_id: list[int]
    """Associated call ID"""
    completion_status: list[str]
    """Completion status"""
    conference_from: list[int]
    """Conference from time"""
    conference_time: list[int]
    """Conference duration"""
    conference_to: list[int]
    """Conference to time"""
    consultation_from: list[int]
    """Consultation from time"""
    consultation_time: list[int]
    """Consultation duration"""
    consultation_to: list[int]
    """Consultation to time"""
    created_at: list[str]
    """Creation timestamp"""
    duration: list[int]
    """Duration in seconds"""
    forwarded_to: list[str]
    """Number forwarded to"""
    hold_time: list[int]
    """Hold time in seconds"""
    id: list[int]
    """Call leg ID"""
    minutes_billed: list[int]
    """Minutes billed"""
    quality_issues: list[list[Any]]
    """Quality issues detected"""
    talk_time: list[int]
    """Talk time in seconds"""
    transferred_from: list[int]
    """Transferred from agent ID"""
    transferred_to: list[int]
    """Transferred to agent ID"""
    type_: list[str]
    """Type of call leg"""
    updated_at: list[str]
    """Last update timestamp"""
    user_id: list[int]
    """User ID"""
    wrap_up_time: list[int]
    """Wrap-up time in seconds"""


class CallLegsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    agent_id: Any
    """Agent ID"""
    available_via: Any
    """Channel agent was available through"""
    call_charge: Any
    """Call charge amount"""
    call_id: Any
    """Associated call ID"""
    completion_status: Any
    """Completion status"""
    conference_from: Any
    """Conference from time"""
    conference_time: Any
    """Conference duration"""
    conference_to: Any
    """Conference to time"""
    consultation_from: Any
    """Consultation from time"""
    consultation_time: Any
    """Consultation duration"""
    consultation_to: Any
    """Consultation to time"""
    created_at: Any
    """Creation timestamp"""
    duration: Any
    """Duration in seconds"""
    forwarded_to: Any
    """Number forwarded to"""
    hold_time: Any
    """Hold time in seconds"""
    id: Any
    """Call leg ID"""
    minutes_billed: Any
    """Minutes billed"""
    quality_issues: Any
    """Quality issues detected"""
    talk_time: Any
    """Talk time in seconds"""
    transferred_from: Any
    """Transferred from agent ID"""
    transferred_to: Any
    """Transferred to agent ID"""
    type_: Any
    """Type of call leg"""
    updated_at: Any
    """Last update timestamp"""
    user_id: Any
    """User ID"""
    wrap_up_time: Any
    """Wrap-up time in seconds"""


class CallLegsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    agent_id: str
    """Agent ID"""
    available_via: str
    """Channel agent was available through"""
    call_charge: str
    """Call charge amount"""
    call_id: str
    """Associated call ID"""
    completion_status: str
    """Completion status"""
    conference_from: str
    """Conference from time"""
    conference_time: str
    """Conference duration"""
    conference_to: str
    """Conference to time"""
    consultation_from: str
    """Consultation from time"""
    consultation_time: str
    """Consultation duration"""
    consultation_to: str
    """Consultation to time"""
    created_at: str
    """Creation timestamp"""
    duration: str
    """Duration in seconds"""
    forwarded_to: str
    """Number forwarded to"""
    hold_time: str
    """Hold time in seconds"""
    id: str
    """Call leg ID"""
    minutes_billed: str
    """Minutes billed"""
    quality_issues: str
    """Quality issues detected"""
    talk_time: str
    """Talk time in seconds"""
    transferred_from: str
    """Transferred from agent ID"""
    transferred_to: str
    """Transferred to agent ID"""
    type_: str
    """Type of call leg"""
    updated_at: str
    """Last update timestamp"""
    user_id: str
    """User ID"""
    wrap_up_time: str
    """Wrap-up time in seconds"""


class CallLegsSortFilter(TypedDict, total=False):
    """Available fields for sorting call_legs search results."""
    agent_id: AirbyteSortOrder
    """Agent ID"""
    available_via: AirbyteSortOrder
    """Channel agent was available through"""
    call_charge: AirbyteSortOrder
    """Call charge amount"""
    call_id: AirbyteSortOrder
    """Associated call ID"""
    completion_status: AirbyteSortOrder
    """Completion status"""
    conference_from: AirbyteSortOrder
    """Conference from time"""
    conference_time: AirbyteSortOrder
    """Conference duration"""
    conference_to: AirbyteSortOrder
    """Conference to time"""
    consultation_from: AirbyteSortOrder
    """Consultation from time"""
    consultation_time: AirbyteSortOrder
    """Consultation duration"""
    consultation_to: AirbyteSortOrder
    """Consultation to time"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    duration: AirbyteSortOrder
    """Duration in seconds"""
    forwarded_to: AirbyteSortOrder
    """Number forwarded to"""
    hold_time: AirbyteSortOrder
    """Hold time in seconds"""
    id: AirbyteSortOrder
    """Call leg ID"""
    minutes_billed: AirbyteSortOrder
    """Minutes billed"""
    quality_issues: AirbyteSortOrder
    """Quality issues detected"""
    talk_time: AirbyteSortOrder
    """Talk time in seconds"""
    transferred_from: AirbyteSortOrder
    """Transferred from agent ID"""
    transferred_to: AirbyteSortOrder
    """Transferred to agent ID"""
    type_: AirbyteSortOrder
    """Type of call leg"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""
    user_id: AirbyteSortOrder
    """User ID"""
    wrap_up_time: AirbyteSortOrder
    """Wrap-up time in seconds"""


# Entity-specific condition types for call_legs
class CallLegsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallLegsSearchFilter


class CallLegsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallLegsSearchFilter


class CallLegsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallLegsSearchFilter


class CallLegsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallLegsSearchFilter


class CallLegsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallLegsSearchFilter


class CallLegsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallLegsSearchFilter


class CallLegsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CallLegsStringFilter


class CallLegsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallLegsStringFilter


class CallLegsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallLegsStringFilter


class CallLegsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CallLegsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallLegsInCondition = TypedDict("CallLegsInCondition", {"in": CallLegsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallLegsNotCondition = TypedDict("CallLegsNotCondition", {"not": "CallLegsCondition"}, total=False)
"""Negates the nested condition."""

CallLegsAndCondition = TypedDict("CallLegsAndCondition", {"and": "list[CallLegsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallLegsOrCondition = TypedDict("CallLegsOrCondition", {"or": "list[CallLegsCondition]"}, total=False)
"""True if any nested condition is true."""

CallLegsAnyCondition = TypedDict("CallLegsAnyCondition", {"any": CallLegsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all call_legs condition types
CallLegsCondition = (
    CallLegsEqCondition
    | CallLegsNeqCondition
    | CallLegsGtCondition
    | CallLegsGteCondition
    | CallLegsLtCondition
    | CallLegsLteCondition
    | CallLegsInCondition
    | CallLegsLikeCondition
    | CallLegsFuzzyCondition
    | CallLegsKeywordCondition
    | CallLegsContainsCondition
    | CallLegsNotCondition
    | CallLegsAndCondition
    | CallLegsOrCondition
    | CallLegsAnyCondition
)


class CallLegsSearchQuery(TypedDict, total=False):
    """Search query for call_legs entity."""
    filter: CallLegsCondition
    sort: list[CallLegsSortFilter]


# ===== CALLS SEARCH TYPES =====

class CallsSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls search queries."""
    agent_id: int | None
    """Agent ID"""
    call_charge: str | None
    """Call charge amount"""
    call_group_id: int | None
    """Call group ID"""
    call_recording_consent: str | None
    """Call recording consent status"""
    call_recording_consent_action: str | None
    """Recording consent action"""
    call_recording_consent_keypress: str | None
    """Recording consent keypress"""
    callback: bool | None
    """Whether this was a callback"""
    callback_source: str | None
    """Source of the callback"""
    completion_status: str | None
    """Call completion status"""
    consultation_time: int | None
    """Consultation time"""
    created_at: str | None
    """Creation timestamp"""
    customer_requested_voicemail: bool | None
    """Whether customer requested voicemail"""
    default_group: bool | None
    """Whether default group was used"""
    direction: str | None
    """Call direction (inbound/outbound)"""
    duration: int | None
    """Call duration in seconds"""
    exceeded_queue_time: bool | None
    """Whether queue time was exceeded"""
    exceeded_queue_wait_time: bool | None
    """Whether max queue wait time was exceeded"""
    hold_time: int | None
    """Hold time in seconds"""
    id: int | None
    """Call ID"""
    ivr_action: str | None
    """IVR action taken"""
    ivr_destination_group_name: str | None
    """IVR destination group name"""
    ivr_hops: int | None
    """Number of IVR hops"""
    ivr_routed_to: str | None
    """Where IVR routed the call"""
    ivr_time_spent: int | None
    """Time spent in IVR"""
    minutes_billed: int | None
    """Minutes billed"""
    not_recording_time: int | None
    """Time not recording"""
    outside_business_hours: bool | None
    """Whether call was outside business hours"""
    overflowed: bool | None
    """Whether call overflowed"""
    overflowed_to: str | None
    """Where call overflowed to"""
    phone_number: str | None
    """Phone number used"""
    phone_number_id: int | None
    """Phone number ID"""
    quality_issues: list[Any] | None
    """Quality issues detected"""
    recording_control_interactions: int | None
    """Recording control interactions count"""
    recording_time: int | None
    """Recording time"""
    talk_time: int | None
    """Talk time in seconds"""
    ticket_id: int | None
    """Associated ticket ID"""
    time_to_answer: int | None
    """Time to answer in seconds"""
    updated_at: str | None
    """Last update timestamp"""
    voicemail: bool | None
    """Whether it was a voicemail"""
    wait_time: int | None
    """Wait time in seconds"""
    wrap_up_time: int | None
    """Wrap-up time in seconds"""


class CallsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    agent_id: list[int]
    """Agent ID"""
    call_charge: list[str]
    """Call charge amount"""
    call_group_id: list[int]
    """Call group ID"""
    call_recording_consent: list[str]
    """Call recording consent status"""
    call_recording_consent_action: list[str]
    """Recording consent action"""
    call_recording_consent_keypress: list[str]
    """Recording consent keypress"""
    callback: list[bool]
    """Whether this was a callback"""
    callback_source: list[str]
    """Source of the callback"""
    completion_status: list[str]
    """Call completion status"""
    consultation_time: list[int]
    """Consultation time"""
    created_at: list[str]
    """Creation timestamp"""
    customer_requested_voicemail: list[bool]
    """Whether customer requested voicemail"""
    default_group: list[bool]
    """Whether default group was used"""
    direction: list[str]
    """Call direction (inbound/outbound)"""
    duration: list[int]
    """Call duration in seconds"""
    exceeded_queue_time: list[bool]
    """Whether queue time was exceeded"""
    exceeded_queue_wait_time: list[bool]
    """Whether max queue wait time was exceeded"""
    hold_time: list[int]
    """Hold time in seconds"""
    id: list[int]
    """Call ID"""
    ivr_action: list[str]
    """IVR action taken"""
    ivr_destination_group_name: list[str]
    """IVR destination group name"""
    ivr_hops: list[int]
    """Number of IVR hops"""
    ivr_routed_to: list[str]
    """Where IVR routed the call"""
    ivr_time_spent: list[int]
    """Time spent in IVR"""
    minutes_billed: list[int]
    """Minutes billed"""
    not_recording_time: list[int]
    """Time not recording"""
    outside_business_hours: list[bool]
    """Whether call was outside business hours"""
    overflowed: list[bool]
    """Whether call overflowed"""
    overflowed_to: list[str]
    """Where call overflowed to"""
    phone_number: list[str]
    """Phone number used"""
    phone_number_id: list[int]
    """Phone number ID"""
    quality_issues: list[list[Any]]
    """Quality issues detected"""
    recording_control_interactions: list[int]
    """Recording control interactions count"""
    recording_time: list[int]
    """Recording time"""
    talk_time: list[int]
    """Talk time in seconds"""
    ticket_id: list[int]
    """Associated ticket ID"""
    time_to_answer: list[int]
    """Time to answer in seconds"""
    updated_at: list[str]
    """Last update timestamp"""
    voicemail: list[bool]
    """Whether it was a voicemail"""
    wait_time: list[int]
    """Wait time in seconds"""
    wrap_up_time: list[int]
    """Wrap-up time in seconds"""


class CallsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    agent_id: Any
    """Agent ID"""
    call_charge: Any
    """Call charge amount"""
    call_group_id: Any
    """Call group ID"""
    call_recording_consent: Any
    """Call recording consent status"""
    call_recording_consent_action: Any
    """Recording consent action"""
    call_recording_consent_keypress: Any
    """Recording consent keypress"""
    callback: Any
    """Whether this was a callback"""
    callback_source: Any
    """Source of the callback"""
    completion_status: Any
    """Call completion status"""
    consultation_time: Any
    """Consultation time"""
    created_at: Any
    """Creation timestamp"""
    customer_requested_voicemail: Any
    """Whether customer requested voicemail"""
    default_group: Any
    """Whether default group was used"""
    direction: Any
    """Call direction (inbound/outbound)"""
    duration: Any
    """Call duration in seconds"""
    exceeded_queue_time: Any
    """Whether queue time was exceeded"""
    exceeded_queue_wait_time: Any
    """Whether max queue wait time was exceeded"""
    hold_time: Any
    """Hold time in seconds"""
    id: Any
    """Call ID"""
    ivr_action: Any
    """IVR action taken"""
    ivr_destination_group_name: Any
    """IVR destination group name"""
    ivr_hops: Any
    """Number of IVR hops"""
    ivr_routed_to: Any
    """Where IVR routed the call"""
    ivr_time_spent: Any
    """Time spent in IVR"""
    minutes_billed: Any
    """Minutes billed"""
    not_recording_time: Any
    """Time not recording"""
    outside_business_hours: Any
    """Whether call was outside business hours"""
    overflowed: Any
    """Whether call overflowed"""
    overflowed_to: Any
    """Where call overflowed to"""
    phone_number: Any
    """Phone number used"""
    phone_number_id: Any
    """Phone number ID"""
    quality_issues: Any
    """Quality issues detected"""
    recording_control_interactions: Any
    """Recording control interactions count"""
    recording_time: Any
    """Recording time"""
    talk_time: Any
    """Talk time in seconds"""
    ticket_id: Any
    """Associated ticket ID"""
    time_to_answer: Any
    """Time to answer in seconds"""
    updated_at: Any
    """Last update timestamp"""
    voicemail: Any
    """Whether it was a voicemail"""
    wait_time: Any
    """Wait time in seconds"""
    wrap_up_time: Any
    """Wrap-up time in seconds"""


class CallsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    agent_id: str
    """Agent ID"""
    call_charge: str
    """Call charge amount"""
    call_group_id: str
    """Call group ID"""
    call_recording_consent: str
    """Call recording consent status"""
    call_recording_consent_action: str
    """Recording consent action"""
    call_recording_consent_keypress: str
    """Recording consent keypress"""
    callback: str
    """Whether this was a callback"""
    callback_source: str
    """Source of the callback"""
    completion_status: str
    """Call completion status"""
    consultation_time: str
    """Consultation time"""
    created_at: str
    """Creation timestamp"""
    customer_requested_voicemail: str
    """Whether customer requested voicemail"""
    default_group: str
    """Whether default group was used"""
    direction: str
    """Call direction (inbound/outbound)"""
    duration: str
    """Call duration in seconds"""
    exceeded_queue_time: str
    """Whether queue time was exceeded"""
    exceeded_queue_wait_time: str
    """Whether max queue wait time was exceeded"""
    hold_time: str
    """Hold time in seconds"""
    id: str
    """Call ID"""
    ivr_action: str
    """IVR action taken"""
    ivr_destination_group_name: str
    """IVR destination group name"""
    ivr_hops: str
    """Number of IVR hops"""
    ivr_routed_to: str
    """Where IVR routed the call"""
    ivr_time_spent: str
    """Time spent in IVR"""
    minutes_billed: str
    """Minutes billed"""
    not_recording_time: str
    """Time not recording"""
    outside_business_hours: str
    """Whether call was outside business hours"""
    overflowed: str
    """Whether call overflowed"""
    overflowed_to: str
    """Where call overflowed to"""
    phone_number: str
    """Phone number used"""
    phone_number_id: str
    """Phone number ID"""
    quality_issues: str
    """Quality issues detected"""
    recording_control_interactions: str
    """Recording control interactions count"""
    recording_time: str
    """Recording time"""
    talk_time: str
    """Talk time in seconds"""
    ticket_id: str
    """Associated ticket ID"""
    time_to_answer: str
    """Time to answer in seconds"""
    updated_at: str
    """Last update timestamp"""
    voicemail: str
    """Whether it was a voicemail"""
    wait_time: str
    """Wait time in seconds"""
    wrap_up_time: str
    """Wrap-up time in seconds"""


class CallsSortFilter(TypedDict, total=False):
    """Available fields for sorting calls search results."""
    agent_id: AirbyteSortOrder
    """Agent ID"""
    call_charge: AirbyteSortOrder
    """Call charge amount"""
    call_group_id: AirbyteSortOrder
    """Call group ID"""
    call_recording_consent: AirbyteSortOrder
    """Call recording consent status"""
    call_recording_consent_action: AirbyteSortOrder
    """Recording consent action"""
    call_recording_consent_keypress: AirbyteSortOrder
    """Recording consent keypress"""
    callback: AirbyteSortOrder
    """Whether this was a callback"""
    callback_source: AirbyteSortOrder
    """Source of the callback"""
    completion_status: AirbyteSortOrder
    """Call completion status"""
    consultation_time: AirbyteSortOrder
    """Consultation time"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    customer_requested_voicemail: AirbyteSortOrder
    """Whether customer requested voicemail"""
    default_group: AirbyteSortOrder
    """Whether default group was used"""
    direction: AirbyteSortOrder
    """Call direction (inbound/outbound)"""
    duration: AirbyteSortOrder
    """Call duration in seconds"""
    exceeded_queue_time: AirbyteSortOrder
    """Whether queue time was exceeded"""
    exceeded_queue_wait_time: AirbyteSortOrder
    """Whether max queue wait time was exceeded"""
    hold_time: AirbyteSortOrder
    """Hold time in seconds"""
    id: AirbyteSortOrder
    """Call ID"""
    ivr_action: AirbyteSortOrder
    """IVR action taken"""
    ivr_destination_group_name: AirbyteSortOrder
    """IVR destination group name"""
    ivr_hops: AirbyteSortOrder
    """Number of IVR hops"""
    ivr_routed_to: AirbyteSortOrder
    """Where IVR routed the call"""
    ivr_time_spent: AirbyteSortOrder
    """Time spent in IVR"""
    minutes_billed: AirbyteSortOrder
    """Minutes billed"""
    not_recording_time: AirbyteSortOrder
    """Time not recording"""
    outside_business_hours: AirbyteSortOrder
    """Whether call was outside business hours"""
    overflowed: AirbyteSortOrder
    """Whether call overflowed"""
    overflowed_to: AirbyteSortOrder
    """Where call overflowed to"""
    phone_number: AirbyteSortOrder
    """Phone number used"""
    phone_number_id: AirbyteSortOrder
    """Phone number ID"""
    quality_issues: AirbyteSortOrder
    """Quality issues detected"""
    recording_control_interactions: AirbyteSortOrder
    """Recording control interactions count"""
    recording_time: AirbyteSortOrder
    """Recording time"""
    talk_time: AirbyteSortOrder
    """Talk time in seconds"""
    ticket_id: AirbyteSortOrder
    """Associated ticket ID"""
    time_to_answer: AirbyteSortOrder
    """Time to answer in seconds"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""
    voicemail: AirbyteSortOrder
    """Whether it was a voicemail"""
    wait_time: AirbyteSortOrder
    """Wait time in seconds"""
    wrap_up_time: AirbyteSortOrder
    """Wrap-up time in seconds"""


# Entity-specific condition types for calls
class CallsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallsSearchFilter


class CallsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallsSearchFilter


class CallsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallsSearchFilter


class CallsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallsSearchFilter


class CallsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallsSearchFilter


class CallsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallsSearchFilter


class CallsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CallsStringFilter


class CallsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallsStringFilter


class CallsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallsStringFilter


class CallsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CallsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallsInCondition = TypedDict("CallsInCondition", {"in": CallsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallsNotCondition = TypedDict("CallsNotCondition", {"not": "CallsCondition"}, total=False)
"""Negates the nested condition."""

CallsAndCondition = TypedDict("CallsAndCondition", {"and": "list[CallsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallsOrCondition = TypedDict("CallsOrCondition", {"or": "list[CallsCondition]"}, total=False)
"""True if any nested condition is true."""

CallsAnyCondition = TypedDict("CallsAnyCondition", {"any": CallsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all calls condition types
CallsCondition = (
    CallsEqCondition
    | CallsNeqCondition
    | CallsGtCondition
    | CallsGteCondition
    | CallsLtCondition
    | CallsLteCondition
    | CallsInCondition
    | CallsLikeCondition
    | CallsFuzzyCondition
    | CallsKeywordCondition
    | CallsContainsCondition
    | CallsNotCondition
    | CallsAndCondition
    | CallsOrCondition
    | CallsAnyCondition
)


class CallsSearchQuery(TypedDict, total=False):
    """Search query for calls entity."""
    filter: CallsCondition
    sort: list[CallsSortFilter]


# ===== CURRENT_QUEUE_ACTIVITY SEARCH TYPES =====

class CurrentQueueActivitySearchFilter(TypedDict, total=False):
    """Available fields for filtering current_queue_activity search queries."""
    agents_online: int | None
    """Current number of agents online"""
    average_wait_time: int | None
    """Average wait time for callers in queue (seconds)"""
    callbacks_waiting: int | None
    """Number of callers in callback queue"""
    calls_waiting: int | None
    """Number of callers waiting in queue"""
    current_timestamp: int | None
    """Current timestamp"""
    embeddable_callbacks_waiting: int | None
    """Number of Web Widget callback requests waiting"""
    longest_wait_time: int | None
    """Longest wait time for any caller (seconds)"""


class CurrentQueueActivityInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    agents_online: list[int]
    """Current number of agents online"""
    average_wait_time: list[int]
    """Average wait time for callers in queue (seconds)"""
    callbacks_waiting: list[int]
    """Number of callers in callback queue"""
    calls_waiting: list[int]
    """Number of callers waiting in queue"""
    current_timestamp: list[int]
    """Current timestamp"""
    embeddable_callbacks_waiting: list[int]
    """Number of Web Widget callback requests waiting"""
    longest_wait_time: list[int]
    """Longest wait time for any caller (seconds)"""


class CurrentQueueActivityAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    agents_online: Any
    """Current number of agents online"""
    average_wait_time: Any
    """Average wait time for callers in queue (seconds)"""
    callbacks_waiting: Any
    """Number of callers in callback queue"""
    calls_waiting: Any
    """Number of callers waiting in queue"""
    current_timestamp: Any
    """Current timestamp"""
    embeddable_callbacks_waiting: Any
    """Number of Web Widget callback requests waiting"""
    longest_wait_time: Any
    """Longest wait time for any caller (seconds)"""


class CurrentQueueActivityStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    agents_online: str
    """Current number of agents online"""
    average_wait_time: str
    """Average wait time for callers in queue (seconds)"""
    callbacks_waiting: str
    """Number of callers in callback queue"""
    calls_waiting: str
    """Number of callers waiting in queue"""
    current_timestamp: str
    """Current timestamp"""
    embeddable_callbacks_waiting: str
    """Number of Web Widget callback requests waiting"""
    longest_wait_time: str
    """Longest wait time for any caller (seconds)"""


class CurrentQueueActivitySortFilter(TypedDict, total=False):
    """Available fields for sorting current_queue_activity search results."""
    agents_online: AirbyteSortOrder
    """Current number of agents online"""
    average_wait_time: AirbyteSortOrder
    """Average wait time for callers in queue (seconds)"""
    callbacks_waiting: AirbyteSortOrder
    """Number of callers in callback queue"""
    calls_waiting: AirbyteSortOrder
    """Number of callers waiting in queue"""
    current_timestamp: AirbyteSortOrder
    """Current timestamp"""
    embeddable_callbacks_waiting: AirbyteSortOrder
    """Number of Web Widget callback requests waiting"""
    longest_wait_time: AirbyteSortOrder
    """Longest wait time for any caller (seconds)"""


# Entity-specific condition types for current_queue_activity
class CurrentQueueActivityEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CurrentQueueActivitySearchFilter


class CurrentQueueActivityNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CurrentQueueActivitySearchFilter


class CurrentQueueActivityGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CurrentQueueActivitySearchFilter


class CurrentQueueActivityGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CurrentQueueActivitySearchFilter


class CurrentQueueActivityLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CurrentQueueActivitySearchFilter


class CurrentQueueActivityLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CurrentQueueActivitySearchFilter


class CurrentQueueActivityLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CurrentQueueActivityStringFilter


class CurrentQueueActivityFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CurrentQueueActivityStringFilter


class CurrentQueueActivityKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CurrentQueueActivityStringFilter


class CurrentQueueActivityContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CurrentQueueActivityAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CurrentQueueActivityInCondition = TypedDict("CurrentQueueActivityInCondition", {"in": CurrentQueueActivityInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CurrentQueueActivityNotCondition = TypedDict("CurrentQueueActivityNotCondition", {"not": "CurrentQueueActivityCondition"}, total=False)
"""Negates the nested condition."""

CurrentQueueActivityAndCondition = TypedDict("CurrentQueueActivityAndCondition", {"and": "list[CurrentQueueActivityCondition]"}, total=False)
"""True if all nested conditions are true."""

CurrentQueueActivityOrCondition = TypedDict("CurrentQueueActivityOrCondition", {"or": "list[CurrentQueueActivityCondition]"}, total=False)
"""True if any nested condition is true."""

CurrentQueueActivityAnyCondition = TypedDict("CurrentQueueActivityAnyCondition", {"any": CurrentQueueActivityAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all current_queue_activity condition types
CurrentQueueActivityCondition = (
    CurrentQueueActivityEqCondition
    | CurrentQueueActivityNeqCondition
    | CurrentQueueActivityGtCondition
    | CurrentQueueActivityGteCondition
    | CurrentQueueActivityLtCondition
    | CurrentQueueActivityLteCondition
    | CurrentQueueActivityInCondition
    | CurrentQueueActivityLikeCondition
    | CurrentQueueActivityFuzzyCondition
    | CurrentQueueActivityKeywordCondition
    | CurrentQueueActivityContainsCondition
    | CurrentQueueActivityNotCondition
    | CurrentQueueActivityAndCondition
    | CurrentQueueActivityOrCondition
    | CurrentQueueActivityAnyCondition
)


class CurrentQueueActivitySearchQuery(TypedDict, total=False):
    """Search query for current_queue_activity entity."""
    filter: CurrentQueueActivityCondition
    sort: list[CurrentQueueActivitySortFilter]


# ===== ACCOUNT_OVERVIEW SEARCH TYPES =====

class AccountOverviewSearchFilter(TypedDict, total=False):
    """Available fields for filtering account_overview search queries."""
    average_call_duration: int | None
    """Average call duration"""
    average_callback_wait_time: int | None
    """Average callback wait time"""
    average_hold_time: int | None
    """Average hold time per call"""
    average_queue_wait_time: int | None
    """Average queue wait time"""
    average_time_to_answer: int | None
    """Average time to answer"""
    average_wrap_up_time: int | None
    """Average wrap-up time"""
    current_timestamp: int | None
    """Current timestamp"""
    max_calls_waiting: int | None
    """Max calls waiting in queue"""
    max_queue_wait_time: int | None
    """Max queue wait time"""
    total_call_duration: int | None
    """Total call duration"""
    total_callback_calls: int | None
    """Total callback calls"""
    total_calls: int | None
    """Total calls"""
    total_calls_abandoned_in_queue: int | None
    """Total calls abandoned in queue"""
    total_calls_outside_business_hours: int | None
    """Total calls outside business hours"""
    total_calls_with_exceeded_queue_wait_time: int | None
    """Total calls exceeding max queue wait time"""
    total_calls_with_requested_voicemail: int | None
    """Total calls requesting voicemail"""
    total_embeddable_callback_calls: int | None
    """Total embeddable callback calls"""
    total_hold_time: int | None
    """Total hold time"""
    total_inbound_calls: int | None
    """Total inbound calls"""
    total_outbound_calls: int | None
    """Total outbound calls"""
    total_textback_requests: int | None
    """Total textback requests"""
    total_voicemails: int | None
    """Total voicemails"""
    total_wrap_up_time: int | None
    """Total wrap-up time"""


class AccountOverviewInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    average_call_duration: list[int]
    """Average call duration"""
    average_callback_wait_time: list[int]
    """Average callback wait time"""
    average_hold_time: list[int]
    """Average hold time per call"""
    average_queue_wait_time: list[int]
    """Average queue wait time"""
    average_time_to_answer: list[int]
    """Average time to answer"""
    average_wrap_up_time: list[int]
    """Average wrap-up time"""
    current_timestamp: list[int]
    """Current timestamp"""
    max_calls_waiting: list[int]
    """Max calls waiting in queue"""
    max_queue_wait_time: list[int]
    """Max queue wait time"""
    total_call_duration: list[int]
    """Total call duration"""
    total_callback_calls: list[int]
    """Total callback calls"""
    total_calls: list[int]
    """Total calls"""
    total_calls_abandoned_in_queue: list[int]
    """Total calls abandoned in queue"""
    total_calls_outside_business_hours: list[int]
    """Total calls outside business hours"""
    total_calls_with_exceeded_queue_wait_time: list[int]
    """Total calls exceeding max queue wait time"""
    total_calls_with_requested_voicemail: list[int]
    """Total calls requesting voicemail"""
    total_embeddable_callback_calls: list[int]
    """Total embeddable callback calls"""
    total_hold_time: list[int]
    """Total hold time"""
    total_inbound_calls: list[int]
    """Total inbound calls"""
    total_outbound_calls: list[int]
    """Total outbound calls"""
    total_textback_requests: list[int]
    """Total textback requests"""
    total_voicemails: list[int]
    """Total voicemails"""
    total_wrap_up_time: list[int]
    """Total wrap-up time"""


class AccountOverviewAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    average_call_duration: Any
    """Average call duration"""
    average_callback_wait_time: Any
    """Average callback wait time"""
    average_hold_time: Any
    """Average hold time per call"""
    average_queue_wait_time: Any
    """Average queue wait time"""
    average_time_to_answer: Any
    """Average time to answer"""
    average_wrap_up_time: Any
    """Average wrap-up time"""
    current_timestamp: Any
    """Current timestamp"""
    max_calls_waiting: Any
    """Max calls waiting in queue"""
    max_queue_wait_time: Any
    """Max queue wait time"""
    total_call_duration: Any
    """Total call duration"""
    total_callback_calls: Any
    """Total callback calls"""
    total_calls: Any
    """Total calls"""
    total_calls_abandoned_in_queue: Any
    """Total calls abandoned in queue"""
    total_calls_outside_business_hours: Any
    """Total calls outside business hours"""
    total_calls_with_exceeded_queue_wait_time: Any
    """Total calls exceeding max queue wait time"""
    total_calls_with_requested_voicemail: Any
    """Total calls requesting voicemail"""
    total_embeddable_callback_calls: Any
    """Total embeddable callback calls"""
    total_hold_time: Any
    """Total hold time"""
    total_inbound_calls: Any
    """Total inbound calls"""
    total_outbound_calls: Any
    """Total outbound calls"""
    total_textback_requests: Any
    """Total textback requests"""
    total_voicemails: Any
    """Total voicemails"""
    total_wrap_up_time: Any
    """Total wrap-up time"""


class AccountOverviewStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    average_call_duration: str
    """Average call duration"""
    average_callback_wait_time: str
    """Average callback wait time"""
    average_hold_time: str
    """Average hold time per call"""
    average_queue_wait_time: str
    """Average queue wait time"""
    average_time_to_answer: str
    """Average time to answer"""
    average_wrap_up_time: str
    """Average wrap-up time"""
    current_timestamp: str
    """Current timestamp"""
    max_calls_waiting: str
    """Max calls waiting in queue"""
    max_queue_wait_time: str
    """Max queue wait time"""
    total_call_duration: str
    """Total call duration"""
    total_callback_calls: str
    """Total callback calls"""
    total_calls: str
    """Total calls"""
    total_calls_abandoned_in_queue: str
    """Total calls abandoned in queue"""
    total_calls_outside_business_hours: str
    """Total calls outside business hours"""
    total_calls_with_exceeded_queue_wait_time: str
    """Total calls exceeding max queue wait time"""
    total_calls_with_requested_voicemail: str
    """Total calls requesting voicemail"""
    total_embeddable_callback_calls: str
    """Total embeddable callback calls"""
    total_hold_time: str
    """Total hold time"""
    total_inbound_calls: str
    """Total inbound calls"""
    total_outbound_calls: str
    """Total outbound calls"""
    total_textback_requests: str
    """Total textback requests"""
    total_voicemails: str
    """Total voicemails"""
    total_wrap_up_time: str
    """Total wrap-up time"""


class AccountOverviewSortFilter(TypedDict, total=False):
    """Available fields for sorting account_overview search results."""
    average_call_duration: AirbyteSortOrder
    """Average call duration"""
    average_callback_wait_time: AirbyteSortOrder
    """Average callback wait time"""
    average_hold_time: AirbyteSortOrder
    """Average hold time per call"""
    average_queue_wait_time: AirbyteSortOrder
    """Average queue wait time"""
    average_time_to_answer: AirbyteSortOrder
    """Average time to answer"""
    average_wrap_up_time: AirbyteSortOrder
    """Average wrap-up time"""
    current_timestamp: AirbyteSortOrder
    """Current timestamp"""
    max_calls_waiting: AirbyteSortOrder
    """Max calls waiting in queue"""
    max_queue_wait_time: AirbyteSortOrder
    """Max queue wait time"""
    total_call_duration: AirbyteSortOrder
    """Total call duration"""
    total_callback_calls: AirbyteSortOrder
    """Total callback calls"""
    total_calls: AirbyteSortOrder
    """Total calls"""
    total_calls_abandoned_in_queue: AirbyteSortOrder
    """Total calls abandoned in queue"""
    total_calls_outside_business_hours: AirbyteSortOrder
    """Total calls outside business hours"""
    total_calls_with_exceeded_queue_wait_time: AirbyteSortOrder
    """Total calls exceeding max queue wait time"""
    total_calls_with_requested_voicemail: AirbyteSortOrder
    """Total calls requesting voicemail"""
    total_embeddable_callback_calls: AirbyteSortOrder
    """Total embeddable callback calls"""
    total_hold_time: AirbyteSortOrder
    """Total hold time"""
    total_inbound_calls: AirbyteSortOrder
    """Total inbound calls"""
    total_outbound_calls: AirbyteSortOrder
    """Total outbound calls"""
    total_textback_requests: AirbyteSortOrder
    """Total textback requests"""
    total_voicemails: AirbyteSortOrder
    """Total voicemails"""
    total_wrap_up_time: AirbyteSortOrder
    """Total wrap-up time"""


# Entity-specific condition types for account_overview
class AccountOverviewEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountOverviewSearchFilter


class AccountOverviewNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountOverviewSearchFilter


class AccountOverviewGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountOverviewSearchFilter


class AccountOverviewGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountOverviewSearchFilter


class AccountOverviewLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountOverviewSearchFilter


class AccountOverviewLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountOverviewSearchFilter


class AccountOverviewLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AccountOverviewStringFilter


class AccountOverviewFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountOverviewStringFilter


class AccountOverviewKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountOverviewStringFilter


class AccountOverviewContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AccountOverviewAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountOverviewInCondition = TypedDict("AccountOverviewInCondition", {"in": AccountOverviewInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountOverviewNotCondition = TypedDict("AccountOverviewNotCondition", {"not": "AccountOverviewCondition"}, total=False)
"""Negates the nested condition."""

AccountOverviewAndCondition = TypedDict("AccountOverviewAndCondition", {"and": "list[AccountOverviewCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountOverviewOrCondition = TypedDict("AccountOverviewOrCondition", {"or": "list[AccountOverviewCondition]"}, total=False)
"""True if any nested condition is true."""

AccountOverviewAnyCondition = TypedDict("AccountOverviewAnyCondition", {"any": AccountOverviewAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all account_overview condition types
AccountOverviewCondition = (
    AccountOverviewEqCondition
    | AccountOverviewNeqCondition
    | AccountOverviewGtCondition
    | AccountOverviewGteCondition
    | AccountOverviewLtCondition
    | AccountOverviewLteCondition
    | AccountOverviewInCondition
    | AccountOverviewLikeCondition
    | AccountOverviewFuzzyCondition
    | AccountOverviewKeywordCondition
    | AccountOverviewContainsCondition
    | AccountOverviewNotCondition
    | AccountOverviewAndCondition
    | AccountOverviewOrCondition
    | AccountOverviewAnyCondition
)


class AccountOverviewSearchQuery(TypedDict, total=False):
    """Search query for account_overview entity."""
    filter: AccountOverviewCondition
    sort: list[AccountOverviewSortFilter]


# ===== IVRS SEARCH TYPES =====

class IvrsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ivrs search queries."""
    id: int | None
    """IVR ID"""
    menus: list[Any] | None
    """List of IVR menus"""
    name: str | None
    """Name of the IVR"""
    phone_number_ids: list[Any] | None
    """IDs of phone numbers configured with this IVR"""
    phone_number_names: list[Any] | None
    """Names of phone numbers configured with this IVR"""


class IvrsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """IVR ID"""
    menus: list[list[Any]]
    """List of IVR menus"""
    name: list[str]
    """Name of the IVR"""
    phone_number_ids: list[list[Any]]
    """IDs of phone numbers configured with this IVR"""
    phone_number_names: list[list[Any]]
    """Names of phone numbers configured with this IVR"""


class IvrsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """IVR ID"""
    menus: Any
    """List of IVR menus"""
    name: Any
    """Name of the IVR"""
    phone_number_ids: Any
    """IDs of phone numbers configured with this IVR"""
    phone_number_names: Any
    """Names of phone numbers configured with this IVR"""


class IvrsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """IVR ID"""
    menus: str
    """List of IVR menus"""
    name: str
    """Name of the IVR"""
    phone_number_ids: str
    """IDs of phone numbers configured with this IVR"""
    phone_number_names: str
    """Names of phone numbers configured with this IVR"""


class IvrsSortFilter(TypedDict, total=False):
    """Available fields for sorting ivrs search results."""
    id: AirbyteSortOrder
    """IVR ID"""
    menus: AirbyteSortOrder
    """List of IVR menus"""
    name: AirbyteSortOrder
    """Name of the IVR"""
    phone_number_ids: AirbyteSortOrder
    """IDs of phone numbers configured with this IVR"""
    phone_number_names: AirbyteSortOrder
    """Names of phone numbers configured with this IVR"""


# Entity-specific condition types for ivrs
class IvrsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IvrsSearchFilter


class IvrsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IvrsSearchFilter


class IvrsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IvrsSearchFilter


class IvrsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IvrsSearchFilter


class IvrsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IvrsSearchFilter


class IvrsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IvrsSearchFilter


class IvrsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IvrsStringFilter


class IvrsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IvrsStringFilter


class IvrsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IvrsStringFilter


class IvrsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IvrsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IvrsInCondition = TypedDict("IvrsInCondition", {"in": IvrsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IvrsNotCondition = TypedDict("IvrsNotCondition", {"not": "IvrsCondition"}, total=False)
"""Negates the nested condition."""

IvrsAndCondition = TypedDict("IvrsAndCondition", {"and": "list[IvrsCondition]"}, total=False)
"""True if all nested conditions are true."""

IvrsOrCondition = TypedDict("IvrsOrCondition", {"or": "list[IvrsCondition]"}, total=False)
"""True if any nested condition is true."""

IvrsAnyCondition = TypedDict("IvrsAnyCondition", {"any": IvrsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ivrs condition types
IvrsCondition = (
    IvrsEqCondition
    | IvrsNeqCondition
    | IvrsGtCondition
    | IvrsGteCondition
    | IvrsLtCondition
    | IvrsLteCondition
    | IvrsInCondition
    | IvrsLikeCondition
    | IvrsFuzzyCondition
    | IvrsKeywordCondition
    | IvrsContainsCondition
    | IvrsNotCondition
    | IvrsAndCondition
    | IvrsOrCondition
    | IvrsAnyCondition
)


class IvrsSearchQuery(TypedDict, total=False):
    """Search query for ivrs entity."""
    filter: IvrsCondition
    sort: list[IvrsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
