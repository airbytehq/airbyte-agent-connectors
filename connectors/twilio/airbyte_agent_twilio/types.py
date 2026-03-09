"""
Type definitions for twilio connector.
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

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    page_size: NotRequired[int]

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    sid: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    account_sid: str
    sid: str

class MessagesListParams(TypedDict):
    """Parameters for messages.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class MessagesGetParams(TypedDict):
    """Parameters for messages.get operation"""
    account_sid: str
    sid: str

class IncomingPhoneNumbersListParams(TypedDict):
    """Parameters for incoming_phone_numbers.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class IncomingPhoneNumbersGetParams(TypedDict):
    """Parameters for incoming_phone_numbers.get operation"""
    account_sid: str
    sid: str

class RecordingsListParams(TypedDict):
    """Parameters for recordings.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class RecordingsGetParams(TypedDict):
    """Parameters for recordings.get operation"""
    account_sid: str
    sid: str

class ConferencesListParams(TypedDict):
    """Parameters for conferences.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class ConferencesGetParams(TypedDict):
    """Parameters for conferences.get operation"""
    account_sid: str
    sid: str

class UsageRecordsListParams(TypedDict):
    """Parameters for usage_records.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class AddressesListParams(TypedDict):
    """Parameters for addresses.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class AddressesGetParams(TypedDict):
    """Parameters for addresses.get operation"""
    account_sid: str
    sid: str

class QueuesListParams(TypedDict):
    """Parameters for queues.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class QueuesGetParams(TypedDict):
    """Parameters for queues.get operation"""
    account_sid: str
    sid: str

class TranscriptionsListParams(TypedDict):
    """Parameters for transcriptions.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class TranscriptionsGetParams(TypedDict):
    """Parameters for transcriptions.get operation"""
    account_sid: str
    sid: str

class OutgoingCallerIdsListParams(TypedDict):
    """Parameters for outgoing_caller_ids.list operation"""
    account_sid: str
    page_size: NotRequired[int]

class OutgoingCallerIdsGetParams(TypedDict):
    """Parameters for outgoing_caller_ids.get operation"""
    account_sid: str
    sid: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    sid: str | None
    """The unique identifier for the account"""
    friendly_name: str | None
    """A user-defined friendly name for the account"""
    status: str | None
    """The current status of the account"""
    type_: str | None
    """The type of the account"""
    owner_account_sid: str | None
    """The SID of the owner account"""
    date_created: str | None
    """The timestamp when the account was created"""
    date_updated: str | None
    """The timestamp when the account was last updated"""
    uri: str | None
    """The URI for accessing the account resource"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier for the account"""
    friendly_name: list[str]
    """A user-defined friendly name for the account"""
    status: list[str]
    """The current status of the account"""
    type_: list[str]
    """The type of the account"""
    owner_account_sid: list[str]
    """The SID of the owner account"""
    date_created: list[str]
    """The timestamp when the account was created"""
    date_updated: list[str]
    """The timestamp when the account was last updated"""
    uri: list[str]
    """The URI for accessing the account resource"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier for the account"""
    friendly_name: Any
    """A user-defined friendly name for the account"""
    status: Any
    """The current status of the account"""
    type_: Any
    """The type of the account"""
    owner_account_sid: Any
    """The SID of the owner account"""
    date_created: Any
    """The timestamp when the account was created"""
    date_updated: Any
    """The timestamp when the account was last updated"""
    uri: Any
    """The URI for accessing the account resource"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier for the account"""
    friendly_name: str
    """A user-defined friendly name for the account"""
    status: str
    """The current status of the account"""
    type_: str
    """The type of the account"""
    owner_account_sid: str
    """The SID of the owner account"""
    date_created: str
    """The timestamp when the account was created"""
    date_updated: str
    """The timestamp when the account was last updated"""
    uri: str
    """The URI for accessing the account resource"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    sid: AirbyteSortOrder
    """The unique identifier for the account"""
    friendly_name: AirbyteSortOrder
    """A user-defined friendly name for the account"""
    status: AirbyteSortOrder
    """The current status of the account"""
    type_: AirbyteSortOrder
    """The type of the account"""
    owner_account_sid: AirbyteSortOrder
    """The SID of the owner account"""
    date_created: AirbyteSortOrder
    """The timestamp when the account was created"""
    date_updated: AirbyteSortOrder
    """The timestamp when the account was last updated"""
    uri: AirbyteSortOrder
    """The URI for accessing the account resource"""


# Entity-specific condition types for accounts
class AccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountsSearchFilter


class AccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountsSearchFilter


class AccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountsSearchFilter


class AccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountsSearchFilter


class AccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountsSearchFilter


class AccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountsSearchFilter


class AccountsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AccountsStringFilter


class AccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountsStringFilter


class AccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountsStringFilter


class AccountsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountsInCondition = TypedDict("AccountsInCondition", {"in": AccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountsNotCondition = TypedDict("AccountsNotCondition", {"not": "AccountsCondition"}, total=False)
"""Negates the nested condition."""

AccountsAndCondition = TypedDict("AccountsAndCondition", {"and": "list[AccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountsOrCondition = TypedDict("AccountsOrCondition", {"or": "list[AccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AccountsAnyCondition = TypedDict("AccountsAnyCondition", {"any": AccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all accounts condition types
AccountsCondition = (
    AccountsEqCondition
    | AccountsNeqCondition
    | AccountsGtCondition
    | AccountsGteCondition
    | AccountsLtCondition
    | AccountsLteCondition
    | AccountsInCondition
    | AccountsLikeCondition
    | AccountsFuzzyCondition
    | AccountsKeywordCondition
    | AccountsContainsCondition
    | AccountsNotCondition
    | AccountsAndCondition
    | AccountsOrCondition
    | AccountsAnyCondition
)


class AccountsSearchQuery(TypedDict, total=False):
    """Search query for accounts entity."""
    filter: AccountsCondition
    sort: list[AccountsSortFilter]


# ===== CALLS SEARCH TYPES =====

class CallsSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls search queries."""
    sid: str | None
    """The unique identifier for the call"""
    account_sid: str | None
    """The unique identifier for the account associated with the call"""
    to: str | None
    """The phone number that received the call"""
    from_: str | None
    """The phone number that made the call"""
    status: str | None
    """The current status of the call"""
    direction: str | None
    """The direction of the call (inbound or outbound)"""
    duration: str | None
    """The duration of the call in seconds"""
    price: str | None
    """The cost of the call"""
    price_unit: str | None
    """The currency unit of the call cost"""
    start_time: str | None
    """The date and time when the call started"""
    end_time: str | None
    """The date and time when the call ended"""
    date_created: str | None
    """The date and time when the call record was created"""
    date_updated: str | None
    """The date and time when the call record was last updated"""


class CallsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier for the call"""
    account_sid: list[str]
    """The unique identifier for the account associated with the call"""
    to: list[str]
    """The phone number that received the call"""
    from_: list[str]
    """The phone number that made the call"""
    status: list[str]
    """The current status of the call"""
    direction: list[str]
    """The direction of the call (inbound or outbound)"""
    duration: list[str]
    """The duration of the call in seconds"""
    price: list[str]
    """The cost of the call"""
    price_unit: list[str]
    """The currency unit of the call cost"""
    start_time: list[str]
    """The date and time when the call started"""
    end_time: list[str]
    """The date and time when the call ended"""
    date_created: list[str]
    """The date and time when the call record was created"""
    date_updated: list[str]
    """The date and time when the call record was last updated"""


class CallsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier for the call"""
    account_sid: Any
    """The unique identifier for the account associated with the call"""
    to: Any
    """The phone number that received the call"""
    from_: Any
    """The phone number that made the call"""
    status: Any
    """The current status of the call"""
    direction: Any
    """The direction of the call (inbound or outbound)"""
    duration: Any
    """The duration of the call in seconds"""
    price: Any
    """The cost of the call"""
    price_unit: Any
    """The currency unit of the call cost"""
    start_time: Any
    """The date and time when the call started"""
    end_time: Any
    """The date and time when the call ended"""
    date_created: Any
    """The date and time when the call record was created"""
    date_updated: Any
    """The date and time when the call record was last updated"""


class CallsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier for the call"""
    account_sid: str
    """The unique identifier for the account associated with the call"""
    to: str
    """The phone number that received the call"""
    from_: str
    """The phone number that made the call"""
    status: str
    """The current status of the call"""
    direction: str
    """The direction of the call (inbound or outbound)"""
    duration: str
    """The duration of the call in seconds"""
    price: str
    """The cost of the call"""
    price_unit: str
    """The currency unit of the call cost"""
    start_time: str
    """The date and time when the call started"""
    end_time: str
    """The date and time when the call ended"""
    date_created: str
    """The date and time when the call record was created"""
    date_updated: str
    """The date and time when the call record was last updated"""


class CallsSortFilter(TypedDict, total=False):
    """Available fields for sorting calls search results."""
    sid: AirbyteSortOrder
    """The unique identifier for the call"""
    account_sid: AirbyteSortOrder
    """The unique identifier for the account associated with the call"""
    to: AirbyteSortOrder
    """The phone number that received the call"""
    from_: AirbyteSortOrder
    """The phone number that made the call"""
    status: AirbyteSortOrder
    """The current status of the call"""
    direction: AirbyteSortOrder
    """The direction of the call (inbound or outbound)"""
    duration: AirbyteSortOrder
    """The duration of the call in seconds"""
    price: AirbyteSortOrder
    """The cost of the call"""
    price_unit: AirbyteSortOrder
    """The currency unit of the call cost"""
    start_time: AirbyteSortOrder
    """The date and time when the call started"""
    end_time: AirbyteSortOrder
    """The date and time when the call ended"""
    date_created: AirbyteSortOrder
    """The date and time when the call record was created"""
    date_updated: AirbyteSortOrder
    """The date and time when the call record was last updated"""


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


# ===== MESSAGES SEARCH TYPES =====

class MessagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering messages search queries."""
    sid: str | None
    """The unique identifier for this message"""
    account_sid: str | None
    """The unique identifier for the account associated with this message"""
    to: str | None
    """The phone number or recipient ID the message was sent to"""
    from_: str | None
    """The phone number or sender ID that sent the message"""
    body: str | None
    """The text body of the message"""
    status: str | None
    """The status of the message"""
    direction: str | None
    """The direction of the message"""
    price: str | None
    """The cost of the message"""
    price_unit: str | None
    """The currency unit used for pricing"""
    date_created: str | None
    """The date and time when the message was created"""
    date_sent: str | None
    """The date and time when the message was sent"""
    error_code: str | None
    """The error code associated with the message if any"""
    error_message: str | None
    """The error message description if the message failed"""
    num_segments: str | None
    """The number of message segments"""
    num_media: str | None
    """The number of media files included in the message"""


class MessagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier for this message"""
    account_sid: list[str]
    """The unique identifier for the account associated with this message"""
    to: list[str]
    """The phone number or recipient ID the message was sent to"""
    from_: list[str]
    """The phone number or sender ID that sent the message"""
    body: list[str]
    """The text body of the message"""
    status: list[str]
    """The status of the message"""
    direction: list[str]
    """The direction of the message"""
    price: list[str]
    """The cost of the message"""
    price_unit: list[str]
    """The currency unit used for pricing"""
    date_created: list[str]
    """The date and time when the message was created"""
    date_sent: list[str]
    """The date and time when the message was sent"""
    error_code: list[str]
    """The error code associated with the message if any"""
    error_message: list[str]
    """The error message description if the message failed"""
    num_segments: list[str]
    """The number of message segments"""
    num_media: list[str]
    """The number of media files included in the message"""


class MessagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier for this message"""
    account_sid: Any
    """The unique identifier for the account associated with this message"""
    to: Any
    """The phone number or recipient ID the message was sent to"""
    from_: Any
    """The phone number or sender ID that sent the message"""
    body: Any
    """The text body of the message"""
    status: Any
    """The status of the message"""
    direction: Any
    """The direction of the message"""
    price: Any
    """The cost of the message"""
    price_unit: Any
    """The currency unit used for pricing"""
    date_created: Any
    """The date and time when the message was created"""
    date_sent: Any
    """The date and time when the message was sent"""
    error_code: Any
    """The error code associated with the message if any"""
    error_message: Any
    """The error message description if the message failed"""
    num_segments: Any
    """The number of message segments"""
    num_media: Any
    """The number of media files included in the message"""


class MessagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier for this message"""
    account_sid: str
    """The unique identifier for the account associated with this message"""
    to: str
    """The phone number or recipient ID the message was sent to"""
    from_: str
    """The phone number or sender ID that sent the message"""
    body: str
    """The text body of the message"""
    status: str
    """The status of the message"""
    direction: str
    """The direction of the message"""
    price: str
    """The cost of the message"""
    price_unit: str
    """The currency unit used for pricing"""
    date_created: str
    """The date and time when the message was created"""
    date_sent: str
    """The date and time when the message was sent"""
    error_code: str
    """The error code associated with the message if any"""
    error_message: str
    """The error message description if the message failed"""
    num_segments: str
    """The number of message segments"""
    num_media: str
    """The number of media files included in the message"""


class MessagesSortFilter(TypedDict, total=False):
    """Available fields for sorting messages search results."""
    sid: AirbyteSortOrder
    """The unique identifier for this message"""
    account_sid: AirbyteSortOrder
    """The unique identifier for the account associated with this message"""
    to: AirbyteSortOrder
    """The phone number or recipient ID the message was sent to"""
    from_: AirbyteSortOrder
    """The phone number or sender ID that sent the message"""
    body: AirbyteSortOrder
    """The text body of the message"""
    status: AirbyteSortOrder
    """The status of the message"""
    direction: AirbyteSortOrder
    """The direction of the message"""
    price: AirbyteSortOrder
    """The cost of the message"""
    price_unit: AirbyteSortOrder
    """The currency unit used for pricing"""
    date_created: AirbyteSortOrder
    """The date and time when the message was created"""
    date_sent: AirbyteSortOrder
    """The date and time when the message was sent"""
    error_code: AirbyteSortOrder
    """The error code associated with the message if any"""
    error_message: AirbyteSortOrder
    """The error message description if the message failed"""
    num_segments: AirbyteSortOrder
    """The number of message segments"""
    num_media: AirbyteSortOrder
    """The number of media files included in the message"""


# Entity-specific condition types for messages
class MessagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MessagesSearchFilter


class MessagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MessagesSearchFilter


class MessagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MessagesSearchFilter


class MessagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MessagesSearchFilter


class MessagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MessagesSearchFilter


class MessagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MessagesSearchFilter


class MessagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MessagesStringFilter


class MessagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MessagesStringFilter


class MessagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MessagesStringFilter


class MessagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MessagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MessagesInCondition = TypedDict("MessagesInCondition", {"in": MessagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MessagesNotCondition = TypedDict("MessagesNotCondition", {"not": "MessagesCondition"}, total=False)
"""Negates the nested condition."""

MessagesAndCondition = TypedDict("MessagesAndCondition", {"and": "list[MessagesCondition]"}, total=False)
"""True if all nested conditions are true."""

MessagesOrCondition = TypedDict("MessagesOrCondition", {"or": "list[MessagesCondition]"}, total=False)
"""True if any nested condition is true."""

MessagesAnyCondition = TypedDict("MessagesAnyCondition", {"any": MessagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all messages condition types
MessagesCondition = (
    MessagesEqCondition
    | MessagesNeqCondition
    | MessagesGtCondition
    | MessagesGteCondition
    | MessagesLtCondition
    | MessagesLteCondition
    | MessagesInCondition
    | MessagesLikeCondition
    | MessagesFuzzyCondition
    | MessagesKeywordCondition
    | MessagesContainsCondition
    | MessagesNotCondition
    | MessagesAndCondition
    | MessagesOrCondition
    | MessagesAnyCondition
)


class MessagesSearchQuery(TypedDict, total=False):
    """Search query for messages entity."""
    filter: MessagesCondition
    sort: list[MessagesSortFilter]


# ===== INCOMING_PHONE_NUMBERS SEARCH TYPES =====

class IncomingPhoneNumbersSearchFilter(TypedDict, total=False):
    """Available fields for filtering incoming_phone_numbers search queries."""
    sid: str | None
    """The SID of this phone number"""
    account_sid: str | None
    """The SID of the account that owns this phone number"""
    phone_number: str | None
    """The phone number in E.164 format"""
    friendly_name: str | None
    """A user-assigned friendly name for this phone number"""
    status: str | None
    """Status of the phone number"""
    capabilities: dict[str, Any] | None
    """Capabilities of this phone number"""
    date_created: str | None
    """When the phone number was created"""
    date_updated: str | None
    """When the phone number was last updated"""


class IncomingPhoneNumbersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The SID of this phone number"""
    account_sid: list[str]
    """The SID of the account that owns this phone number"""
    phone_number: list[str]
    """The phone number in E.164 format"""
    friendly_name: list[str]
    """A user-assigned friendly name for this phone number"""
    status: list[str]
    """Status of the phone number"""
    capabilities: list[dict[str, Any]]
    """Capabilities of this phone number"""
    date_created: list[str]
    """When the phone number was created"""
    date_updated: list[str]
    """When the phone number was last updated"""


class IncomingPhoneNumbersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The SID of this phone number"""
    account_sid: Any
    """The SID of the account that owns this phone number"""
    phone_number: Any
    """The phone number in E.164 format"""
    friendly_name: Any
    """A user-assigned friendly name for this phone number"""
    status: Any
    """Status of the phone number"""
    capabilities: Any
    """Capabilities of this phone number"""
    date_created: Any
    """When the phone number was created"""
    date_updated: Any
    """When the phone number was last updated"""


class IncomingPhoneNumbersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The SID of this phone number"""
    account_sid: str
    """The SID of the account that owns this phone number"""
    phone_number: str
    """The phone number in E.164 format"""
    friendly_name: str
    """A user-assigned friendly name for this phone number"""
    status: str
    """Status of the phone number"""
    capabilities: str
    """Capabilities of this phone number"""
    date_created: str
    """When the phone number was created"""
    date_updated: str
    """When the phone number was last updated"""


class IncomingPhoneNumbersSortFilter(TypedDict, total=False):
    """Available fields for sorting incoming_phone_numbers search results."""
    sid: AirbyteSortOrder
    """The SID of this phone number"""
    account_sid: AirbyteSortOrder
    """The SID of the account that owns this phone number"""
    phone_number: AirbyteSortOrder
    """The phone number in E.164 format"""
    friendly_name: AirbyteSortOrder
    """A user-assigned friendly name for this phone number"""
    status: AirbyteSortOrder
    """Status of the phone number"""
    capabilities: AirbyteSortOrder
    """Capabilities of this phone number"""
    date_created: AirbyteSortOrder
    """When the phone number was created"""
    date_updated: AirbyteSortOrder
    """When the phone number was last updated"""


# Entity-specific condition types for incoming_phone_numbers
class IncomingPhoneNumbersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IncomingPhoneNumbersSearchFilter


class IncomingPhoneNumbersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IncomingPhoneNumbersSearchFilter


class IncomingPhoneNumbersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IncomingPhoneNumbersSearchFilter


class IncomingPhoneNumbersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IncomingPhoneNumbersSearchFilter


class IncomingPhoneNumbersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IncomingPhoneNumbersSearchFilter


class IncomingPhoneNumbersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IncomingPhoneNumbersSearchFilter


class IncomingPhoneNumbersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IncomingPhoneNumbersStringFilter


class IncomingPhoneNumbersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IncomingPhoneNumbersStringFilter


class IncomingPhoneNumbersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IncomingPhoneNumbersStringFilter


class IncomingPhoneNumbersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IncomingPhoneNumbersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IncomingPhoneNumbersInCondition = TypedDict("IncomingPhoneNumbersInCondition", {"in": IncomingPhoneNumbersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IncomingPhoneNumbersNotCondition = TypedDict("IncomingPhoneNumbersNotCondition", {"not": "IncomingPhoneNumbersCondition"}, total=False)
"""Negates the nested condition."""

IncomingPhoneNumbersAndCondition = TypedDict("IncomingPhoneNumbersAndCondition", {"and": "list[IncomingPhoneNumbersCondition]"}, total=False)
"""True if all nested conditions are true."""

IncomingPhoneNumbersOrCondition = TypedDict("IncomingPhoneNumbersOrCondition", {"or": "list[IncomingPhoneNumbersCondition]"}, total=False)
"""True if any nested condition is true."""

IncomingPhoneNumbersAnyCondition = TypedDict("IncomingPhoneNumbersAnyCondition", {"any": IncomingPhoneNumbersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all incoming_phone_numbers condition types
IncomingPhoneNumbersCondition = (
    IncomingPhoneNumbersEqCondition
    | IncomingPhoneNumbersNeqCondition
    | IncomingPhoneNumbersGtCondition
    | IncomingPhoneNumbersGteCondition
    | IncomingPhoneNumbersLtCondition
    | IncomingPhoneNumbersLteCondition
    | IncomingPhoneNumbersInCondition
    | IncomingPhoneNumbersLikeCondition
    | IncomingPhoneNumbersFuzzyCondition
    | IncomingPhoneNumbersKeywordCondition
    | IncomingPhoneNumbersContainsCondition
    | IncomingPhoneNumbersNotCondition
    | IncomingPhoneNumbersAndCondition
    | IncomingPhoneNumbersOrCondition
    | IncomingPhoneNumbersAnyCondition
)


class IncomingPhoneNumbersSearchQuery(TypedDict, total=False):
    """Search query for incoming_phone_numbers entity."""
    filter: IncomingPhoneNumbersCondition
    sort: list[IncomingPhoneNumbersSortFilter]


# ===== RECORDINGS SEARCH TYPES =====

class RecordingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering recordings search queries."""
    sid: str | None
    """The unique identifier of the recording"""
    account_sid: str | None
    """The account SID that owns the recording"""
    call_sid: str | None
    """The SID of the associated call"""
    duration: str | None
    """Duration in seconds"""
    status: str | None
    """The status of the recording"""
    channels: int | None
    """Number of audio channels"""
    price: str | None
    """The cost of storing the recording"""
    price_unit: str | None
    """The currency unit"""
    date_created: str | None
    """When the recording was created"""
    start_time: str | None
    """When the recording started"""


class RecordingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier of the recording"""
    account_sid: list[str]
    """The account SID that owns the recording"""
    call_sid: list[str]
    """The SID of the associated call"""
    duration: list[str]
    """Duration in seconds"""
    status: list[str]
    """The status of the recording"""
    channels: list[int]
    """Number of audio channels"""
    price: list[str]
    """The cost of storing the recording"""
    price_unit: list[str]
    """The currency unit"""
    date_created: list[str]
    """When the recording was created"""
    start_time: list[str]
    """When the recording started"""


class RecordingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier of the recording"""
    account_sid: Any
    """The account SID that owns the recording"""
    call_sid: Any
    """The SID of the associated call"""
    duration: Any
    """Duration in seconds"""
    status: Any
    """The status of the recording"""
    channels: Any
    """Number of audio channels"""
    price: Any
    """The cost of storing the recording"""
    price_unit: Any
    """The currency unit"""
    date_created: Any
    """When the recording was created"""
    start_time: Any
    """When the recording started"""


class RecordingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier of the recording"""
    account_sid: str
    """The account SID that owns the recording"""
    call_sid: str
    """The SID of the associated call"""
    duration: str
    """Duration in seconds"""
    status: str
    """The status of the recording"""
    channels: str
    """Number of audio channels"""
    price: str
    """The cost of storing the recording"""
    price_unit: str
    """The currency unit"""
    date_created: str
    """When the recording was created"""
    start_time: str
    """When the recording started"""


class RecordingsSortFilter(TypedDict, total=False):
    """Available fields for sorting recordings search results."""
    sid: AirbyteSortOrder
    """The unique identifier of the recording"""
    account_sid: AirbyteSortOrder
    """The account SID that owns the recording"""
    call_sid: AirbyteSortOrder
    """The SID of the associated call"""
    duration: AirbyteSortOrder
    """Duration in seconds"""
    status: AirbyteSortOrder
    """The status of the recording"""
    channels: AirbyteSortOrder
    """Number of audio channels"""
    price: AirbyteSortOrder
    """The cost of storing the recording"""
    price_unit: AirbyteSortOrder
    """The currency unit"""
    date_created: AirbyteSortOrder
    """When the recording was created"""
    start_time: AirbyteSortOrder
    """When the recording started"""


# Entity-specific condition types for recordings
class RecordingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RecordingsSearchFilter


class RecordingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RecordingsSearchFilter


class RecordingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RecordingsSearchFilter


class RecordingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RecordingsSearchFilter


class RecordingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RecordingsSearchFilter


class RecordingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RecordingsSearchFilter


class RecordingsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: RecordingsStringFilter


class RecordingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RecordingsStringFilter


class RecordingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RecordingsStringFilter


class RecordingsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: RecordingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RecordingsInCondition = TypedDict("RecordingsInCondition", {"in": RecordingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RecordingsNotCondition = TypedDict("RecordingsNotCondition", {"not": "RecordingsCondition"}, total=False)
"""Negates the nested condition."""

RecordingsAndCondition = TypedDict("RecordingsAndCondition", {"and": "list[RecordingsCondition]"}, total=False)
"""True if all nested conditions are true."""

RecordingsOrCondition = TypedDict("RecordingsOrCondition", {"or": "list[RecordingsCondition]"}, total=False)
"""True if any nested condition is true."""

RecordingsAnyCondition = TypedDict("RecordingsAnyCondition", {"any": RecordingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all recordings condition types
RecordingsCondition = (
    RecordingsEqCondition
    | RecordingsNeqCondition
    | RecordingsGtCondition
    | RecordingsGteCondition
    | RecordingsLtCondition
    | RecordingsLteCondition
    | RecordingsInCondition
    | RecordingsLikeCondition
    | RecordingsFuzzyCondition
    | RecordingsKeywordCondition
    | RecordingsContainsCondition
    | RecordingsNotCondition
    | RecordingsAndCondition
    | RecordingsOrCondition
    | RecordingsAnyCondition
)


class RecordingsSearchQuery(TypedDict, total=False):
    """Search query for recordings entity."""
    filter: RecordingsCondition
    sort: list[RecordingsSortFilter]


# ===== CONFERENCES SEARCH TYPES =====

class ConferencesSearchFilter(TypedDict, total=False):
    """Available fields for filtering conferences search queries."""
    sid: str | None
    """The unique identifier of the conference"""
    account_sid: str | None
    """The account SID associated with the conference"""
    friendly_name: str | None
    """A friendly name for the conference"""
    status: str | None
    """The current status of the conference"""
    region: str | None
    """The region where the conference is hosted"""
    date_created: str | None
    """When the conference was created"""
    date_updated: str | None
    """When the conference was last updated"""


class ConferencesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier of the conference"""
    account_sid: list[str]
    """The account SID associated with the conference"""
    friendly_name: list[str]
    """A friendly name for the conference"""
    status: list[str]
    """The current status of the conference"""
    region: list[str]
    """The region where the conference is hosted"""
    date_created: list[str]
    """When the conference was created"""
    date_updated: list[str]
    """When the conference was last updated"""


class ConferencesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier of the conference"""
    account_sid: Any
    """The account SID associated with the conference"""
    friendly_name: Any
    """A friendly name for the conference"""
    status: Any
    """The current status of the conference"""
    region: Any
    """The region where the conference is hosted"""
    date_created: Any
    """When the conference was created"""
    date_updated: Any
    """When the conference was last updated"""


class ConferencesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier of the conference"""
    account_sid: str
    """The account SID associated with the conference"""
    friendly_name: str
    """A friendly name for the conference"""
    status: str
    """The current status of the conference"""
    region: str
    """The region where the conference is hosted"""
    date_created: str
    """When the conference was created"""
    date_updated: str
    """When the conference was last updated"""


class ConferencesSortFilter(TypedDict, total=False):
    """Available fields for sorting conferences search results."""
    sid: AirbyteSortOrder
    """The unique identifier of the conference"""
    account_sid: AirbyteSortOrder
    """The account SID associated with the conference"""
    friendly_name: AirbyteSortOrder
    """A friendly name for the conference"""
    status: AirbyteSortOrder
    """The current status of the conference"""
    region: AirbyteSortOrder
    """The region where the conference is hosted"""
    date_created: AirbyteSortOrder
    """When the conference was created"""
    date_updated: AirbyteSortOrder
    """When the conference was last updated"""


# Entity-specific condition types for conferences
class ConferencesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ConferencesSearchFilter


class ConferencesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ConferencesSearchFilter


class ConferencesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ConferencesSearchFilter


class ConferencesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ConferencesSearchFilter


class ConferencesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ConferencesSearchFilter


class ConferencesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ConferencesSearchFilter


class ConferencesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ConferencesStringFilter


class ConferencesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ConferencesStringFilter


class ConferencesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ConferencesStringFilter


class ConferencesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ConferencesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ConferencesInCondition = TypedDict("ConferencesInCondition", {"in": ConferencesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ConferencesNotCondition = TypedDict("ConferencesNotCondition", {"not": "ConferencesCondition"}, total=False)
"""Negates the nested condition."""

ConferencesAndCondition = TypedDict("ConferencesAndCondition", {"and": "list[ConferencesCondition]"}, total=False)
"""True if all nested conditions are true."""

ConferencesOrCondition = TypedDict("ConferencesOrCondition", {"or": "list[ConferencesCondition]"}, total=False)
"""True if any nested condition is true."""

ConferencesAnyCondition = TypedDict("ConferencesAnyCondition", {"any": ConferencesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all conferences condition types
ConferencesCondition = (
    ConferencesEqCondition
    | ConferencesNeqCondition
    | ConferencesGtCondition
    | ConferencesGteCondition
    | ConferencesLtCondition
    | ConferencesLteCondition
    | ConferencesInCondition
    | ConferencesLikeCondition
    | ConferencesFuzzyCondition
    | ConferencesKeywordCondition
    | ConferencesContainsCondition
    | ConferencesNotCondition
    | ConferencesAndCondition
    | ConferencesOrCondition
    | ConferencesAnyCondition
)


class ConferencesSearchQuery(TypedDict, total=False):
    """Search query for conferences entity."""
    filter: ConferencesCondition
    sort: list[ConferencesSortFilter]


# ===== USAGE_RECORDS SEARCH TYPES =====

class UsageRecordsSearchFilter(TypedDict, total=False):
    """Available fields for filtering usage_records search queries."""
    account_sid: str | None
    """The account SID associated with this usage record"""
    category: str | None
    """The usage category (calls, SMS, recordings, etc.)"""
    description: str | None
    """A description of the usage record"""
    usage: str | None
    """The total usage value"""
    usage_unit: str | None
    """The unit of measurement for usage"""
    count: str | None
    """The number of units consumed"""
    count_unit: str | None
    """The unit of measurement for count"""
    price: str | None
    """The total price for consumed units"""
    price_unit: str | None
    """The currency unit"""
    start_date: str | None
    """The start date of the usage period"""
    end_date: str | None
    """The end date of the usage period"""


class UsageRecordsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_sid: list[str]
    """The account SID associated with this usage record"""
    category: list[str]
    """The usage category (calls, SMS, recordings, etc.)"""
    description: list[str]
    """A description of the usage record"""
    usage: list[str]
    """The total usage value"""
    usage_unit: list[str]
    """The unit of measurement for usage"""
    count: list[str]
    """The number of units consumed"""
    count_unit: list[str]
    """The unit of measurement for count"""
    price: list[str]
    """The total price for consumed units"""
    price_unit: list[str]
    """The currency unit"""
    start_date: list[str]
    """The start date of the usage period"""
    end_date: list[str]
    """The end date of the usage period"""


class UsageRecordsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_sid: Any
    """The account SID associated with this usage record"""
    category: Any
    """The usage category (calls, SMS, recordings, etc.)"""
    description: Any
    """A description of the usage record"""
    usage: Any
    """The total usage value"""
    usage_unit: Any
    """The unit of measurement for usage"""
    count: Any
    """The number of units consumed"""
    count_unit: Any
    """The unit of measurement for count"""
    price: Any
    """The total price for consumed units"""
    price_unit: Any
    """The currency unit"""
    start_date: Any
    """The start date of the usage period"""
    end_date: Any
    """The end date of the usage period"""


class UsageRecordsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_sid: str
    """The account SID associated with this usage record"""
    category: str
    """The usage category (calls, SMS, recordings, etc.)"""
    description: str
    """A description of the usage record"""
    usage: str
    """The total usage value"""
    usage_unit: str
    """The unit of measurement for usage"""
    count: str
    """The number of units consumed"""
    count_unit: str
    """The unit of measurement for count"""
    price: str
    """The total price for consumed units"""
    price_unit: str
    """The currency unit"""
    start_date: str
    """The start date of the usage period"""
    end_date: str
    """The end date of the usage period"""


class UsageRecordsSortFilter(TypedDict, total=False):
    """Available fields for sorting usage_records search results."""
    account_sid: AirbyteSortOrder
    """The account SID associated with this usage record"""
    category: AirbyteSortOrder
    """The usage category (calls, SMS, recordings, etc.)"""
    description: AirbyteSortOrder
    """A description of the usage record"""
    usage: AirbyteSortOrder
    """The total usage value"""
    usage_unit: AirbyteSortOrder
    """The unit of measurement for usage"""
    count: AirbyteSortOrder
    """The number of units consumed"""
    count_unit: AirbyteSortOrder
    """The unit of measurement for count"""
    price: AirbyteSortOrder
    """The total price for consumed units"""
    price_unit: AirbyteSortOrder
    """The currency unit"""
    start_date: AirbyteSortOrder
    """The start date of the usage period"""
    end_date: AirbyteSortOrder
    """The end date of the usage period"""


# Entity-specific condition types for usage_records
class UsageRecordsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsageRecordsSearchFilter


class UsageRecordsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsageRecordsSearchFilter


class UsageRecordsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsageRecordsSearchFilter


class UsageRecordsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsageRecordsSearchFilter


class UsageRecordsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsageRecordsSearchFilter


class UsageRecordsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsageRecordsSearchFilter


class UsageRecordsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsageRecordsStringFilter


class UsageRecordsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsageRecordsStringFilter


class UsageRecordsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsageRecordsStringFilter


class UsageRecordsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsageRecordsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsageRecordsInCondition = TypedDict("UsageRecordsInCondition", {"in": UsageRecordsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsageRecordsNotCondition = TypedDict("UsageRecordsNotCondition", {"not": "UsageRecordsCondition"}, total=False)
"""Negates the nested condition."""

UsageRecordsAndCondition = TypedDict("UsageRecordsAndCondition", {"and": "list[UsageRecordsCondition]"}, total=False)
"""True if all nested conditions are true."""

UsageRecordsOrCondition = TypedDict("UsageRecordsOrCondition", {"or": "list[UsageRecordsCondition]"}, total=False)
"""True if any nested condition is true."""

UsageRecordsAnyCondition = TypedDict("UsageRecordsAnyCondition", {"any": UsageRecordsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all usage_records condition types
UsageRecordsCondition = (
    UsageRecordsEqCondition
    | UsageRecordsNeqCondition
    | UsageRecordsGtCondition
    | UsageRecordsGteCondition
    | UsageRecordsLtCondition
    | UsageRecordsLteCondition
    | UsageRecordsInCondition
    | UsageRecordsLikeCondition
    | UsageRecordsFuzzyCondition
    | UsageRecordsKeywordCondition
    | UsageRecordsContainsCondition
    | UsageRecordsNotCondition
    | UsageRecordsAndCondition
    | UsageRecordsOrCondition
    | UsageRecordsAnyCondition
)


class UsageRecordsSearchQuery(TypedDict, total=False):
    """Search query for usage_records entity."""
    filter: UsageRecordsCondition
    sort: list[UsageRecordsSortFilter]


# ===== ADDRESSES SEARCH TYPES =====

class AddressesSearchFilter(TypedDict, total=False):
    """Available fields for filtering addresses search queries."""
    sid: str | None
    """The unique identifier of the address"""
    account_sid: str | None
    """The account SID associated with this address"""
    customer_name: str | None
    """The customer name associated with this address"""
    friendly_name: str | None
    """A friendly name for the address"""
    street: str | None
    """The street address"""
    city: str | None
    """The city of the address"""
    region: str | None
    """The region or state"""
    postal_code: str | None
    """The postal code"""
    iso_country: str | None
    """The ISO 3166-1 alpha-2 country code"""
    validated: bool | None
    """Whether the address has been validated"""
    verified: bool | None
    """Whether the address has been verified"""


class AddressesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier of the address"""
    account_sid: list[str]
    """The account SID associated with this address"""
    customer_name: list[str]
    """The customer name associated with this address"""
    friendly_name: list[str]
    """A friendly name for the address"""
    street: list[str]
    """The street address"""
    city: list[str]
    """The city of the address"""
    region: list[str]
    """The region or state"""
    postal_code: list[str]
    """The postal code"""
    iso_country: list[str]
    """The ISO 3166-1 alpha-2 country code"""
    validated: list[bool]
    """Whether the address has been validated"""
    verified: list[bool]
    """Whether the address has been verified"""


class AddressesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier of the address"""
    account_sid: Any
    """The account SID associated with this address"""
    customer_name: Any
    """The customer name associated with this address"""
    friendly_name: Any
    """A friendly name for the address"""
    street: Any
    """The street address"""
    city: Any
    """The city of the address"""
    region: Any
    """The region or state"""
    postal_code: Any
    """The postal code"""
    iso_country: Any
    """The ISO 3166-1 alpha-2 country code"""
    validated: Any
    """Whether the address has been validated"""
    verified: Any
    """Whether the address has been verified"""


class AddressesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier of the address"""
    account_sid: str
    """The account SID associated with this address"""
    customer_name: str
    """The customer name associated with this address"""
    friendly_name: str
    """A friendly name for the address"""
    street: str
    """The street address"""
    city: str
    """The city of the address"""
    region: str
    """The region or state"""
    postal_code: str
    """The postal code"""
    iso_country: str
    """The ISO 3166-1 alpha-2 country code"""
    validated: str
    """Whether the address has been validated"""
    verified: str
    """Whether the address has been verified"""


class AddressesSortFilter(TypedDict, total=False):
    """Available fields for sorting addresses search results."""
    sid: AirbyteSortOrder
    """The unique identifier of the address"""
    account_sid: AirbyteSortOrder
    """The account SID associated with this address"""
    customer_name: AirbyteSortOrder
    """The customer name associated with this address"""
    friendly_name: AirbyteSortOrder
    """A friendly name for the address"""
    street: AirbyteSortOrder
    """The street address"""
    city: AirbyteSortOrder
    """The city of the address"""
    region: AirbyteSortOrder
    """The region or state"""
    postal_code: AirbyteSortOrder
    """The postal code"""
    iso_country: AirbyteSortOrder
    """The ISO 3166-1 alpha-2 country code"""
    validated: AirbyteSortOrder
    """Whether the address has been validated"""
    verified: AirbyteSortOrder
    """Whether the address has been verified"""


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


# ===== QUEUES SEARCH TYPES =====

class QueuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering queues search queries."""
    sid: str | None
    """The unique identifier for the queue"""
    account_sid: str | None
    """The account SID that owns this queue"""
    friendly_name: str | None
    """A friendly name for the queue"""
    current_size: int | None
    """Current number of callers waiting"""
    max_size: int | None
    """Maximum number of callers allowed"""
    average_wait_time: int | None
    """Average wait time in seconds"""
    date_created: str | None
    """When the queue was created"""
    date_updated: str | None
    """When the queue was last updated"""


class QueuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier for the queue"""
    account_sid: list[str]
    """The account SID that owns this queue"""
    friendly_name: list[str]
    """A friendly name for the queue"""
    current_size: list[int]
    """Current number of callers waiting"""
    max_size: list[int]
    """Maximum number of callers allowed"""
    average_wait_time: list[int]
    """Average wait time in seconds"""
    date_created: list[str]
    """When the queue was created"""
    date_updated: list[str]
    """When the queue was last updated"""


class QueuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier for the queue"""
    account_sid: Any
    """The account SID that owns this queue"""
    friendly_name: Any
    """A friendly name for the queue"""
    current_size: Any
    """Current number of callers waiting"""
    max_size: Any
    """Maximum number of callers allowed"""
    average_wait_time: Any
    """Average wait time in seconds"""
    date_created: Any
    """When the queue was created"""
    date_updated: Any
    """When the queue was last updated"""


class QueuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier for the queue"""
    account_sid: str
    """The account SID that owns this queue"""
    friendly_name: str
    """A friendly name for the queue"""
    current_size: str
    """Current number of callers waiting"""
    max_size: str
    """Maximum number of callers allowed"""
    average_wait_time: str
    """Average wait time in seconds"""
    date_created: str
    """When the queue was created"""
    date_updated: str
    """When the queue was last updated"""


class QueuesSortFilter(TypedDict, total=False):
    """Available fields for sorting queues search results."""
    sid: AirbyteSortOrder
    """The unique identifier for the queue"""
    account_sid: AirbyteSortOrder
    """The account SID that owns this queue"""
    friendly_name: AirbyteSortOrder
    """A friendly name for the queue"""
    current_size: AirbyteSortOrder
    """Current number of callers waiting"""
    max_size: AirbyteSortOrder
    """Maximum number of callers allowed"""
    average_wait_time: AirbyteSortOrder
    """Average wait time in seconds"""
    date_created: AirbyteSortOrder
    """When the queue was created"""
    date_updated: AirbyteSortOrder
    """When the queue was last updated"""


# Entity-specific condition types for queues
class QueuesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: QueuesSearchFilter


class QueuesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: QueuesSearchFilter


class QueuesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: QueuesSearchFilter


class QueuesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: QueuesSearchFilter


class QueuesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: QueuesSearchFilter


class QueuesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: QueuesSearchFilter


class QueuesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: QueuesStringFilter


class QueuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: QueuesStringFilter


class QueuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: QueuesStringFilter


class QueuesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: QueuesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
QueuesInCondition = TypedDict("QueuesInCondition", {"in": QueuesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

QueuesNotCondition = TypedDict("QueuesNotCondition", {"not": "QueuesCondition"}, total=False)
"""Negates the nested condition."""

QueuesAndCondition = TypedDict("QueuesAndCondition", {"and": "list[QueuesCondition]"}, total=False)
"""True if all nested conditions are true."""

QueuesOrCondition = TypedDict("QueuesOrCondition", {"or": "list[QueuesCondition]"}, total=False)
"""True if any nested condition is true."""

QueuesAnyCondition = TypedDict("QueuesAnyCondition", {"any": QueuesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all queues condition types
QueuesCondition = (
    QueuesEqCondition
    | QueuesNeqCondition
    | QueuesGtCondition
    | QueuesGteCondition
    | QueuesLtCondition
    | QueuesLteCondition
    | QueuesInCondition
    | QueuesLikeCondition
    | QueuesFuzzyCondition
    | QueuesKeywordCondition
    | QueuesContainsCondition
    | QueuesNotCondition
    | QueuesAndCondition
    | QueuesOrCondition
    | QueuesAnyCondition
)


class QueuesSearchQuery(TypedDict, total=False):
    """Search query for queues entity."""
    filter: QueuesCondition
    sort: list[QueuesSortFilter]


# ===== TRANSCRIPTIONS SEARCH TYPES =====

class TranscriptionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering transcriptions search queries."""
    sid: str | None
    """The unique identifier for the transcription"""
    account_sid: str | None
    """The account SID"""
    recording_sid: str | None
    """The SID of the associated recording"""
    status: str | None
    """The status of the transcription"""
    duration: str | None
    """Duration of the audio recording in seconds"""
    price: str | None
    """The cost of the transcription"""
    price_unit: str | None
    """The currency unit"""
    date_created: str | None
    """When the transcription was created"""
    date_updated: str | None
    """When the transcription was last updated"""


class TranscriptionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier for the transcription"""
    account_sid: list[str]
    """The account SID"""
    recording_sid: list[str]
    """The SID of the associated recording"""
    status: list[str]
    """The status of the transcription"""
    duration: list[str]
    """Duration of the audio recording in seconds"""
    price: list[str]
    """The cost of the transcription"""
    price_unit: list[str]
    """The currency unit"""
    date_created: list[str]
    """When the transcription was created"""
    date_updated: list[str]
    """When the transcription was last updated"""


class TranscriptionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier for the transcription"""
    account_sid: Any
    """The account SID"""
    recording_sid: Any
    """The SID of the associated recording"""
    status: Any
    """The status of the transcription"""
    duration: Any
    """Duration of the audio recording in seconds"""
    price: Any
    """The cost of the transcription"""
    price_unit: Any
    """The currency unit"""
    date_created: Any
    """When the transcription was created"""
    date_updated: Any
    """When the transcription was last updated"""


class TranscriptionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier for the transcription"""
    account_sid: str
    """The account SID"""
    recording_sid: str
    """The SID of the associated recording"""
    status: str
    """The status of the transcription"""
    duration: str
    """Duration of the audio recording in seconds"""
    price: str
    """The cost of the transcription"""
    price_unit: str
    """The currency unit"""
    date_created: str
    """When the transcription was created"""
    date_updated: str
    """When the transcription was last updated"""


class TranscriptionsSortFilter(TypedDict, total=False):
    """Available fields for sorting transcriptions search results."""
    sid: AirbyteSortOrder
    """The unique identifier for the transcription"""
    account_sid: AirbyteSortOrder
    """The account SID"""
    recording_sid: AirbyteSortOrder
    """The SID of the associated recording"""
    status: AirbyteSortOrder
    """The status of the transcription"""
    duration: AirbyteSortOrder
    """Duration of the audio recording in seconds"""
    price: AirbyteSortOrder
    """The cost of the transcription"""
    price_unit: AirbyteSortOrder
    """The currency unit"""
    date_created: AirbyteSortOrder
    """When the transcription was created"""
    date_updated: AirbyteSortOrder
    """When the transcription was last updated"""


# Entity-specific condition types for transcriptions
class TranscriptionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TranscriptionsSearchFilter


class TranscriptionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TranscriptionsSearchFilter


class TranscriptionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TranscriptionsSearchFilter


class TranscriptionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TranscriptionsSearchFilter


class TranscriptionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TranscriptionsSearchFilter


class TranscriptionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TranscriptionsSearchFilter


class TranscriptionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TranscriptionsStringFilter


class TranscriptionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TranscriptionsStringFilter


class TranscriptionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TranscriptionsStringFilter


class TranscriptionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TranscriptionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TranscriptionsInCondition = TypedDict("TranscriptionsInCondition", {"in": TranscriptionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TranscriptionsNotCondition = TypedDict("TranscriptionsNotCondition", {"not": "TranscriptionsCondition"}, total=False)
"""Negates the nested condition."""

TranscriptionsAndCondition = TypedDict("TranscriptionsAndCondition", {"and": "list[TranscriptionsCondition]"}, total=False)
"""True if all nested conditions are true."""

TranscriptionsOrCondition = TypedDict("TranscriptionsOrCondition", {"or": "list[TranscriptionsCondition]"}, total=False)
"""True if any nested condition is true."""

TranscriptionsAnyCondition = TypedDict("TranscriptionsAnyCondition", {"any": TranscriptionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all transcriptions condition types
TranscriptionsCondition = (
    TranscriptionsEqCondition
    | TranscriptionsNeqCondition
    | TranscriptionsGtCondition
    | TranscriptionsGteCondition
    | TranscriptionsLtCondition
    | TranscriptionsLteCondition
    | TranscriptionsInCondition
    | TranscriptionsLikeCondition
    | TranscriptionsFuzzyCondition
    | TranscriptionsKeywordCondition
    | TranscriptionsContainsCondition
    | TranscriptionsNotCondition
    | TranscriptionsAndCondition
    | TranscriptionsOrCondition
    | TranscriptionsAnyCondition
)


class TranscriptionsSearchQuery(TypedDict, total=False):
    """Search query for transcriptions entity."""
    filter: TranscriptionsCondition
    sort: list[TranscriptionsSortFilter]


# ===== OUTGOING_CALLER_IDS SEARCH TYPES =====

class OutgoingCallerIdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering outgoing_caller_ids search queries."""
    sid: str | None
    """The unique identifier"""
    account_sid: str | None
    """The account SID"""
    phone_number: str | None
    """The phone number"""
    friendly_name: str | None
    """A friendly name"""
    date_created: str | None
    """When the outgoing caller ID was created"""
    date_updated: str | None
    """When the outgoing caller ID was last updated"""


class OutgoingCallerIdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sid: list[str]
    """The unique identifier"""
    account_sid: list[str]
    """The account SID"""
    phone_number: list[str]
    """The phone number"""
    friendly_name: list[str]
    """A friendly name"""
    date_created: list[str]
    """When the outgoing caller ID was created"""
    date_updated: list[str]
    """When the outgoing caller ID was last updated"""


class OutgoingCallerIdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sid: Any
    """The unique identifier"""
    account_sid: Any
    """The account SID"""
    phone_number: Any
    """The phone number"""
    friendly_name: Any
    """A friendly name"""
    date_created: Any
    """When the outgoing caller ID was created"""
    date_updated: Any
    """When the outgoing caller ID was last updated"""


class OutgoingCallerIdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sid: str
    """The unique identifier"""
    account_sid: str
    """The account SID"""
    phone_number: str
    """The phone number"""
    friendly_name: str
    """A friendly name"""
    date_created: str
    """When the outgoing caller ID was created"""
    date_updated: str
    """When the outgoing caller ID was last updated"""


class OutgoingCallerIdsSortFilter(TypedDict, total=False):
    """Available fields for sorting outgoing_caller_ids search results."""
    sid: AirbyteSortOrder
    """The unique identifier"""
    account_sid: AirbyteSortOrder
    """The account SID"""
    phone_number: AirbyteSortOrder
    """The phone number"""
    friendly_name: AirbyteSortOrder
    """A friendly name"""
    date_created: AirbyteSortOrder
    """When the outgoing caller ID was created"""
    date_updated: AirbyteSortOrder
    """When the outgoing caller ID was last updated"""


# Entity-specific condition types for outgoing_caller_ids
class OutgoingCallerIdsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OutgoingCallerIdsSearchFilter


class OutgoingCallerIdsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OutgoingCallerIdsSearchFilter


class OutgoingCallerIdsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OutgoingCallerIdsSearchFilter


class OutgoingCallerIdsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OutgoingCallerIdsSearchFilter


class OutgoingCallerIdsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OutgoingCallerIdsSearchFilter


class OutgoingCallerIdsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OutgoingCallerIdsSearchFilter


class OutgoingCallerIdsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OutgoingCallerIdsStringFilter


class OutgoingCallerIdsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OutgoingCallerIdsStringFilter


class OutgoingCallerIdsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OutgoingCallerIdsStringFilter


class OutgoingCallerIdsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OutgoingCallerIdsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OutgoingCallerIdsInCondition = TypedDict("OutgoingCallerIdsInCondition", {"in": OutgoingCallerIdsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OutgoingCallerIdsNotCondition = TypedDict("OutgoingCallerIdsNotCondition", {"not": "OutgoingCallerIdsCondition"}, total=False)
"""Negates the nested condition."""

OutgoingCallerIdsAndCondition = TypedDict("OutgoingCallerIdsAndCondition", {"and": "list[OutgoingCallerIdsCondition]"}, total=False)
"""True if all nested conditions are true."""

OutgoingCallerIdsOrCondition = TypedDict("OutgoingCallerIdsOrCondition", {"or": "list[OutgoingCallerIdsCondition]"}, total=False)
"""True if any nested condition is true."""

OutgoingCallerIdsAnyCondition = TypedDict("OutgoingCallerIdsAnyCondition", {"any": OutgoingCallerIdsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all outgoing_caller_ids condition types
OutgoingCallerIdsCondition = (
    OutgoingCallerIdsEqCondition
    | OutgoingCallerIdsNeqCondition
    | OutgoingCallerIdsGtCondition
    | OutgoingCallerIdsGteCondition
    | OutgoingCallerIdsLtCondition
    | OutgoingCallerIdsLteCondition
    | OutgoingCallerIdsInCondition
    | OutgoingCallerIdsLikeCondition
    | OutgoingCallerIdsFuzzyCondition
    | OutgoingCallerIdsKeywordCondition
    | OutgoingCallerIdsContainsCondition
    | OutgoingCallerIdsNotCondition
    | OutgoingCallerIdsAndCondition
    | OutgoingCallerIdsOrCondition
    | OutgoingCallerIdsAnyCondition
)


class OutgoingCallerIdsSearchQuery(TypedDict, total=False):
    """Search query for outgoing_caller_ids entity."""
    filter: OutgoingCallerIdsCondition
    sort: list[OutgoingCallerIdsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
