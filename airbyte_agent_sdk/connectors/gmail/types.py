"""
Type definitions for gmail connector.
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

class LabelsCreateParamsColor(TypedDict):
    """The color to assign to the label"""
    text_color: NotRequired[str]
    background_color: NotRequired[str]

class LabelsUpdateParamsColor(TypedDict):
    """The color to assign to the label"""
    text_color: NotRequired[str]
    background_color: NotRequired[str]

class DraftsCreateParamsMessage(TypedDict):
    """The draft message content encoded in Gmail raw message format"""
    raw: str
    thread_id: NotRequired[str]

class DraftsUpdateParamsMessage(TypedDict):
    """The draft message content encoded in Gmail raw message format"""
    raw: str
    thread_id: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ProfileGetParams(TypedDict):
    """Parameters for profile.get operation"""
    pass

class MessagesListParams(TypedDict):
    """Parameters for messages.list operation"""
    max_results: NotRequired[int]
    page_token: NotRequired[str]
    q: NotRequired[str]
    label_ids: NotRequired[str]
    include_spam_trash: NotRequired[bool]

class MessagesGetParams(TypedDict):
    """Parameters for messages.get operation"""
    message_id: str
    format: NotRequired[str]
    metadata_headers: NotRequired[str]

class LabelsListParams(TypedDict):
    """Parameters for labels.list operation"""
    pass

class LabelsCreateParams(TypedDict):
    """Parameters for labels.create operation"""
    name: str
    message_list_visibility: NotRequired[str]
    label_list_visibility: NotRequired[str]
    color: NotRequired[LabelsCreateParamsColor]

class LabelsGetParams(TypedDict):
    """Parameters for labels.get operation"""
    label_id: str

class LabelsUpdateParams(TypedDict):
    """Parameters for labels.update operation"""
    id: NotRequired[str]
    name: NotRequired[str]
    message_list_visibility: NotRequired[str]
    label_list_visibility: NotRequired[str]
    color: NotRequired[LabelsUpdateParamsColor]
    label_id: str

class LabelsDeleteParams(TypedDict):
    """Parameters for labels.delete operation"""
    label_id: str

class DraftsListParams(TypedDict):
    """Parameters for drafts.list operation"""
    max_results: NotRequired[int]
    page_token: NotRequired[str]
    q: NotRequired[str]
    include_spam_trash: NotRequired[bool]

class DraftsCreateParams(TypedDict):
    """Parameters for drafts.create operation"""
    message: DraftsCreateParamsMessage

class DraftsGetParams(TypedDict):
    """Parameters for drafts.get operation"""
    draft_id: str
    format: NotRequired[str]

class DraftsUpdateParams(TypedDict):
    """Parameters for drafts.update operation"""
    message: DraftsUpdateParamsMessage
    draft_id: str

class DraftsDeleteParams(TypedDict):
    """Parameters for drafts.delete operation"""
    draft_id: str

class DraftsSendCreateParams(TypedDict):
    """Parameters for drafts_send.create operation"""
    id: str

class ThreadsListParams(TypedDict):
    """Parameters for threads.list operation"""
    max_results: NotRequired[int]
    page_token: NotRequired[str]
    q: NotRequired[str]
    label_ids: NotRequired[str]
    include_spam_trash: NotRequired[bool]

class ThreadsGetParams(TypedDict):
    """Parameters for threads.get operation"""
    thread_id: str
    format: NotRequired[str]
    metadata_headers: NotRequired[str]

class MessagesCreateParams(TypedDict):
    """Parameters for messages.create operation"""
    raw: str
    thread_id: NotRequired[str]

class MessagesUpdateParams(TypedDict):
    """Parameters for messages.update operation"""
    add_label_ids: NotRequired[list[str]]
    remove_label_ids: NotRequired[list[str]]
    message_id: str

class MessagesTrashCreateParams(TypedDict):
    """Parameters for messages_trash.create operation"""
    message_id: str

class MessagesUntrashCreateParams(TypedDict):
    """Parameters for messages_untrash.create operation"""
    message_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== PROFILE SEARCH TYPES =====

class ProfileSearchFilter(TypedDict, total=False):
    """Available fields for filtering profile search queries."""
    email_address: str | None
    """Email address of the authenticated Gmail account"""
    history_id: str | None
    """Mailbox history record identifier used for incremental sync"""
    messages_total: float | None
    """Total number of messages currently in the mailbox"""
    threads_total: float | None
    """Total number of threads currently in the mailbox"""


class ProfileInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    email_address: list[str]
    """Email address of the authenticated Gmail account"""
    history_id: list[str]
    """Mailbox history record identifier used for incremental sync"""
    messages_total: list[float]
    """Total number of messages currently in the mailbox"""
    threads_total: list[float]
    """Total number of threads currently in the mailbox"""


class ProfileAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    email_address: Any
    """Email address of the authenticated Gmail account"""
    history_id: Any
    """Mailbox history record identifier used for incremental sync"""
    messages_total: Any
    """Total number of messages currently in the mailbox"""
    threads_total: Any
    """Total number of threads currently in the mailbox"""


class ProfileStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    email_address: str
    """Email address of the authenticated Gmail account"""
    history_id: str
    """Mailbox history record identifier used for incremental sync"""
    messages_total: str
    """Total number of messages currently in the mailbox"""
    threads_total: str
    """Total number of threads currently in the mailbox"""


class ProfileSortFilter(TypedDict, total=False):
    """Available fields for sorting profile search results."""
    email_address: AirbyteSortOrder
    """Email address of the authenticated Gmail account"""
    history_id: AirbyteSortOrder
    """Mailbox history record identifier used for incremental sync"""
    messages_total: AirbyteSortOrder
    """Total number of messages currently in the mailbox"""
    threads_total: AirbyteSortOrder
    """Total number of threads currently in the mailbox"""


# Entity-specific condition types for profile
class ProfileEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProfileSearchFilter


class ProfileNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProfileSearchFilter


class ProfileGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProfileSearchFilter


class ProfileGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProfileSearchFilter


class ProfileLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProfileSearchFilter


class ProfileLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProfileSearchFilter


class ProfileLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProfileStringFilter


class ProfileFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProfileStringFilter


class ProfileKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProfileStringFilter


class ProfileContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProfileAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProfileInCondition = TypedDict("ProfileInCondition", {"in": ProfileInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProfileNotCondition = TypedDict("ProfileNotCondition", {"not": "ProfileCondition"}, total=False)
"""Negates the nested condition."""

ProfileAndCondition = TypedDict("ProfileAndCondition", {"and": "list[ProfileCondition]"}, total=False)
"""True if all nested conditions are true."""

ProfileOrCondition = TypedDict("ProfileOrCondition", {"or": "list[ProfileCondition]"}, total=False)
"""True if any nested condition is true."""

ProfileAnyCondition = TypedDict("ProfileAnyCondition", {"any": ProfileAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all profile condition types
ProfileCondition = (
    ProfileEqCondition
    | ProfileNeqCondition
    | ProfileGtCondition
    | ProfileGteCondition
    | ProfileLtCondition
    | ProfileLteCondition
    | ProfileInCondition
    | ProfileLikeCondition
    | ProfileFuzzyCondition
    | ProfileKeywordCondition
    | ProfileContainsCondition
    | ProfileNotCondition
    | ProfileAndCondition
    | ProfileOrCondition
    | ProfileAnyCondition
)


class ProfileSearchQuery(TypedDict, total=False):
    """Search query for profile entity."""
    filter: ProfileCondition
    sort: list[ProfileSortFilter]


# ===== MESSAGES SEARCH TYPES =====

class MessagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering messages search queries."""
    id: str
    """Unique identifier for the message"""
    thread_id: str | None
    """Identifier of the thread this message belongs to"""
    label_ids: list[Any] | None
    """Labels applied to the message"""
    snippet: str | None
    """Short snippet of the message text"""
    history_id: str | None
    """Mailbox history record identifier for the message"""
    internal_date: str | None
    """Internal message creation timestamp in epoch milliseconds"""
    size_estimate: int | None
    """Estimated size of the message in bytes"""
    payload: dict[str, Any] | None
    """Parsed MIME payload including headers, body, nested MIME parts, and attachment metadata. Use payload.headers for sender, recipients, subject, date, and other email headers."""


class MessagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the message"""
    thread_id: list[str]
    """Identifier of the thread this message belongs to"""
    label_ids: list[list[Any]]
    """Labels applied to the message"""
    snippet: list[str]
    """Short snippet of the message text"""
    history_id: list[str]
    """Mailbox history record identifier for the message"""
    internal_date: list[str]
    """Internal message creation timestamp in epoch milliseconds"""
    size_estimate: list[int]
    """Estimated size of the message in bytes"""
    payload: list[dict[str, Any]]
    """Parsed MIME payload including headers, body, nested MIME parts, and attachment metadata. Use payload.headers for sender, recipients, subject, date, and other email headers."""


class MessagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the message"""
    thread_id: Any
    """Identifier of the thread this message belongs to"""
    label_ids: Any
    """Labels applied to the message"""
    snippet: Any
    """Short snippet of the message text"""
    history_id: Any
    """Mailbox history record identifier for the message"""
    internal_date: Any
    """Internal message creation timestamp in epoch milliseconds"""
    size_estimate: Any
    """Estimated size of the message in bytes"""
    payload: Any
    """Parsed MIME payload including headers, body, nested MIME parts, and attachment metadata. Use payload.headers for sender, recipients, subject, date, and other email headers."""


class MessagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the message"""
    thread_id: str
    """Identifier of the thread this message belongs to"""
    label_ids: str
    """Labels applied to the message"""
    snippet: str
    """Short snippet of the message text"""
    history_id: str
    """Mailbox history record identifier for the message"""
    internal_date: str
    """Internal message creation timestamp in epoch milliseconds"""
    size_estimate: str
    """Estimated size of the message in bytes"""
    payload: str
    """Parsed MIME payload including headers, body, nested MIME parts, and attachment metadata. Use payload.headers for sender, recipients, subject, date, and other email headers."""


class MessagesSortFilter(TypedDict, total=False):
    """Available fields for sorting messages search results."""
    id: AirbyteSortOrder
    """Unique identifier for the message"""
    thread_id: AirbyteSortOrder
    """Identifier of the thread this message belongs to"""
    label_ids: AirbyteSortOrder
    """Labels applied to the message"""
    snippet: AirbyteSortOrder
    """Short snippet of the message text"""
    history_id: AirbyteSortOrder
    """Mailbox history record identifier for the message"""
    internal_date: AirbyteSortOrder
    """Internal message creation timestamp in epoch milliseconds"""
    size_estimate: AirbyteSortOrder
    """Estimated size of the message in bytes"""
    payload: AirbyteSortOrder
    """Parsed MIME payload including headers, body, nested MIME parts, and attachment metadata. Use payload.headers for sender, recipients, subject, date, and other email headers."""


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


# ===== LABELS SEARCH TYPES =====

class LabelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering labels search queries."""
    id: str
    """Unique identifier for the label"""
    name: str | None
    """Display name of the label"""
    type_: str | None
    """Label type: `system` or `user`"""
    label_list_visibility: str | None
    """Visibility of the label in the label list"""
    message_list_visibility: str | None
    """Visibility of the label when viewing a message list"""


class LabelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the label"""
    name: list[str]
    """Display name of the label"""
    type_: list[str]
    """Label type: `system` or `user`"""
    label_list_visibility: list[str]
    """Visibility of the label in the label list"""
    message_list_visibility: list[str]
    """Visibility of the label when viewing a message list"""


class LabelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the label"""
    name: Any
    """Display name of the label"""
    type_: Any
    """Label type: `system` or `user`"""
    label_list_visibility: Any
    """Visibility of the label in the label list"""
    message_list_visibility: Any
    """Visibility of the label when viewing a message list"""


class LabelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the label"""
    name: str
    """Display name of the label"""
    type_: str
    """Label type: `system` or `user`"""
    label_list_visibility: str
    """Visibility of the label in the label list"""
    message_list_visibility: str
    """Visibility of the label when viewing a message list"""


class LabelsSortFilter(TypedDict, total=False):
    """Available fields for sorting labels search results."""
    id: AirbyteSortOrder
    """Unique identifier for the label"""
    name: AirbyteSortOrder
    """Display name of the label"""
    type_: AirbyteSortOrder
    """Label type: `system` or `user`"""
    label_list_visibility: AirbyteSortOrder
    """Visibility of the label in the label list"""
    message_list_visibility: AirbyteSortOrder
    """Visibility of the label when viewing a message list"""


# Entity-specific condition types for labels
class LabelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LabelsSearchFilter


class LabelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LabelsSearchFilter


class LabelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LabelsSearchFilter


class LabelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LabelsSearchFilter


class LabelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LabelsSearchFilter


class LabelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LabelsSearchFilter


class LabelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LabelsStringFilter


class LabelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LabelsStringFilter


class LabelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LabelsStringFilter


class LabelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LabelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LabelsInCondition = TypedDict("LabelsInCondition", {"in": LabelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LabelsNotCondition = TypedDict("LabelsNotCondition", {"not": "LabelsCondition"}, total=False)
"""Negates the nested condition."""

LabelsAndCondition = TypedDict("LabelsAndCondition", {"and": "list[LabelsCondition]"}, total=False)
"""True if all nested conditions are true."""

LabelsOrCondition = TypedDict("LabelsOrCondition", {"or": "list[LabelsCondition]"}, total=False)
"""True if any nested condition is true."""

LabelsAnyCondition = TypedDict("LabelsAnyCondition", {"any": LabelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all labels condition types
LabelsCondition = (
    LabelsEqCondition
    | LabelsNeqCondition
    | LabelsGtCondition
    | LabelsGteCondition
    | LabelsLtCondition
    | LabelsLteCondition
    | LabelsInCondition
    | LabelsLikeCondition
    | LabelsFuzzyCondition
    | LabelsKeywordCondition
    | LabelsContainsCondition
    | LabelsNotCondition
    | LabelsAndCondition
    | LabelsOrCondition
    | LabelsAnyCondition
)


class LabelsSearchQuery(TypedDict, total=False):
    """Search query for labels entity."""
    filter: LabelsCondition
    sort: list[LabelsSortFilter]


# ===== DRAFTS SEARCH TYPES =====

class DraftsSearchFilter(TypedDict, total=False):
    """Available fields for filtering drafts search queries."""
    id: str
    """Unique identifier for the draft"""
    message: dict[str, Any] | None
    """Draft message payload (headers, body, and metadata)"""


class DraftsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the draft"""
    message: list[dict[str, Any]]
    """Draft message payload (headers, body, and metadata)"""


class DraftsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the draft"""
    message: Any
    """Draft message payload (headers, body, and metadata)"""


class DraftsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the draft"""
    message: str
    """Draft message payload (headers, body, and metadata)"""


class DraftsSortFilter(TypedDict, total=False):
    """Available fields for sorting drafts search results."""
    id: AirbyteSortOrder
    """Unique identifier for the draft"""
    message: AirbyteSortOrder
    """Draft message payload (headers, body, and metadata)"""


# Entity-specific condition types for drafts
class DraftsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DraftsSearchFilter


class DraftsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DraftsSearchFilter


class DraftsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DraftsSearchFilter


class DraftsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DraftsSearchFilter


class DraftsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DraftsSearchFilter


class DraftsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DraftsSearchFilter


class DraftsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DraftsStringFilter


class DraftsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DraftsStringFilter


class DraftsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DraftsStringFilter


class DraftsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DraftsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DraftsInCondition = TypedDict("DraftsInCondition", {"in": DraftsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DraftsNotCondition = TypedDict("DraftsNotCondition", {"not": "DraftsCondition"}, total=False)
"""Negates the nested condition."""

DraftsAndCondition = TypedDict("DraftsAndCondition", {"and": "list[DraftsCondition]"}, total=False)
"""True if all nested conditions are true."""

DraftsOrCondition = TypedDict("DraftsOrCondition", {"or": "list[DraftsCondition]"}, total=False)
"""True if any nested condition is true."""

DraftsAnyCondition = TypedDict("DraftsAnyCondition", {"any": DraftsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all drafts condition types
DraftsCondition = (
    DraftsEqCondition
    | DraftsNeqCondition
    | DraftsGtCondition
    | DraftsGteCondition
    | DraftsLtCondition
    | DraftsLteCondition
    | DraftsInCondition
    | DraftsLikeCondition
    | DraftsFuzzyCondition
    | DraftsKeywordCondition
    | DraftsContainsCondition
    | DraftsNotCondition
    | DraftsAndCondition
    | DraftsOrCondition
    | DraftsAnyCondition
)


class DraftsSearchQuery(TypedDict, total=False):
    """Search query for drafts entity."""
    filter: DraftsCondition
    sort: list[DraftsSortFilter]


# ===== THREADS SEARCH TYPES =====

class ThreadsSearchFilter(TypedDict, total=False):
    """Available fields for filtering threads search queries."""
    id: str
    """Unique identifier for the thread"""
    history_id: str | None
    """Mailbox history record identifier for the thread"""
    snippet: str | None
    """Short snippet of the thread's most recent message"""


class ThreadsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the thread"""
    history_id: list[str]
    """Mailbox history record identifier for the thread"""
    snippet: list[str]
    """Short snippet of the thread's most recent message"""


class ThreadsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the thread"""
    history_id: Any
    """Mailbox history record identifier for the thread"""
    snippet: Any
    """Short snippet of the thread's most recent message"""


class ThreadsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the thread"""
    history_id: str
    """Mailbox history record identifier for the thread"""
    snippet: str
    """Short snippet of the thread's most recent message"""


class ThreadsSortFilter(TypedDict, total=False):
    """Available fields for sorting threads search results."""
    id: AirbyteSortOrder
    """Unique identifier for the thread"""
    history_id: AirbyteSortOrder
    """Mailbox history record identifier for the thread"""
    snippet: AirbyteSortOrder
    """Short snippet of the thread's most recent message"""


# Entity-specific condition types for threads
class ThreadsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ThreadsSearchFilter


class ThreadsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ThreadsSearchFilter


class ThreadsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ThreadsSearchFilter


class ThreadsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ThreadsSearchFilter


class ThreadsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ThreadsSearchFilter


class ThreadsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ThreadsSearchFilter


class ThreadsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ThreadsStringFilter


class ThreadsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ThreadsStringFilter


class ThreadsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ThreadsStringFilter


class ThreadsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ThreadsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ThreadsInCondition = TypedDict("ThreadsInCondition", {"in": ThreadsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ThreadsNotCondition = TypedDict("ThreadsNotCondition", {"not": "ThreadsCondition"}, total=False)
"""Negates the nested condition."""

ThreadsAndCondition = TypedDict("ThreadsAndCondition", {"and": "list[ThreadsCondition]"}, total=False)
"""True if all nested conditions are true."""

ThreadsOrCondition = TypedDict("ThreadsOrCondition", {"or": "list[ThreadsCondition]"}, total=False)
"""True if any nested condition is true."""

ThreadsAnyCondition = TypedDict("ThreadsAnyCondition", {"any": ThreadsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all threads condition types
ThreadsCondition = (
    ThreadsEqCondition
    | ThreadsNeqCondition
    | ThreadsGtCondition
    | ThreadsGteCondition
    | ThreadsLtCondition
    | ThreadsLteCondition
    | ThreadsInCondition
    | ThreadsLikeCondition
    | ThreadsFuzzyCondition
    | ThreadsKeywordCondition
    | ThreadsContainsCondition
    | ThreadsNotCondition
    | ThreadsAndCondition
    | ThreadsOrCondition
    | ThreadsAnyCondition
)


class ThreadsSearchQuery(TypedDict, total=False):
    """Search query for threads entity."""
    filter: ThreadsCondition
    sort: list[ThreadsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
