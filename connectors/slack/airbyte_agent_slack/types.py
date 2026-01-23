"""
Type definitions for slack connector.
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

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user: str

class ChannelsListParams(TypedDict):
    """Parameters for channels.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]
    types: NotRequired[str]
    exclude_archived: NotRequired[bool]

class ChannelsGetParams(TypedDict):
    """Parameters for channels.get operation"""
    channel: str

class ChannelMessagesListParams(TypedDict):
    """Parameters for channel_messages.list operation"""
    channel: str
    cursor: NotRequired[str]
    limit: NotRequired[int]
    oldest: NotRequired[str]
    latest: NotRequired[str]
    inclusive: NotRequired[bool]

class ThreadsListParams(TypedDict):
    """Parameters for threads.list operation"""
    channel: str
    ts: NotRequired[str]
    cursor: NotRequired[str]
    limit: NotRequired[int]
    oldest: NotRequired[str]
    latest: NotRequired[str]
    inclusive: NotRequired[bool]

class MessagesCreateParams(TypedDict):
    """Parameters for messages.create operation"""
    channel: str
    text: str
    thread_ts: NotRequired[str]
    reply_broadcast: NotRequired[bool]
    unfurl_links: NotRequired[bool]
    unfurl_media: NotRequired[bool]

class MessagesUpdateParams(TypedDict):
    """Parameters for messages.update operation"""
    channel: str
    ts: str
    text: str

class ChannelsCreateParams(TypedDict):
    """Parameters for channels.create operation"""
    name: str
    is_private: NotRequired[bool]

class ChannelsUpdateParams(TypedDict):
    """Parameters for channels.update operation"""
    channel: str
    name: str

class ChannelTopicsCreateParams(TypedDict):
    """Parameters for channel_topics.create operation"""
    channel: str
    topic: str

class ChannelPurposesCreateParams(TypedDict):
    """Parameters for channel_purposes.create operation"""
    channel: str
    purpose: str

class ReactionsCreateParams(TypedDict):
    """Parameters for reactions.create operation"""
    channel: str
    timestamp: str
    name: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CHANNELS SEARCH TYPES =====

class ChannelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering channels search queries."""
    context_team_id: str | None
    """The unique identifier of the team context in which the channel exists."""
    created: int | None
    """The timestamp when the channel was created."""
    creator: str | None
    """The ID of the user who created the channel."""
    id: str | None
    """The unique identifier of the channel."""
    is_archived: bool | None
    """Indicates if the channel is archived."""
    is_channel: bool | None
    """Indicates if the entity is a channel."""
    is_ext_shared: bool | None
    """Indicates if the channel is externally shared."""
    is_general: bool | None
    """Indicates if the channel is a general channel in the workspace."""
    is_group: bool | None
    """Indicates if the channel is a group (private channel) rather than a regular channel."""
    is_im: bool | None
    """Indicates if the entity is a direct message (IM) channel."""
    is_member: bool | None
    """Indicates if the calling user is a member of the channel."""
    is_mpim: bool | None
    """Indicates if the entity is a multiple person direct message (MPIM) channel."""
    is_org_shared: bool | None
    """Indicates if the channel is organization-wide shared."""
    is_pending_ext_shared: bool | None
    """Indicates if the channel is pending external shared."""
    is_private: bool | None
    """Indicates if the channel is a private channel."""
    is_read_only: bool | None
    """Indicates if the channel is read-only."""
    is_shared: bool | None
    """Indicates if the channel is shared."""
    last_read: str | None
    """The timestamp of the user's last read message in the channel."""
    locale: str | None
    """The locale of the channel."""
    name: str | None
    """The name of the channel."""
    name_normalized: str | None
    """The normalized name of the channel."""
    num_members: int | None
    """The number of members in the channel."""
    parent_conversation: str | None
    """The parent conversation of the channel."""
    pending_connected_team_ids: list[Any] | None
    """The IDs of teams that are pending to be connected to the channel."""
    pending_shared: list[Any] | None
    """The list of pending shared items of the channel."""
    previous_names: list[Any] | None
    """The previous names of the channel."""
    purpose: dict[str, Any] | None
    """The purpose of the channel."""
    shared_team_ids: list[Any] | None
    """The IDs of teams with which the channel is shared."""
    topic: dict[str, Any] | None
    """The topic of the channel."""
    unlinked: int | None
    """Indicates if the channel is unlinked."""
    updated: int | None
    """The timestamp when the channel was last updated."""


class ChannelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    context_team_id: list[str]
    """The unique identifier of the team context in which the channel exists."""
    created: list[int]
    """The timestamp when the channel was created."""
    creator: list[str]
    """The ID of the user who created the channel."""
    id: list[str]
    """The unique identifier of the channel."""
    is_archived: list[bool]
    """Indicates if the channel is archived."""
    is_channel: list[bool]
    """Indicates if the entity is a channel."""
    is_ext_shared: list[bool]
    """Indicates if the channel is externally shared."""
    is_general: list[bool]
    """Indicates if the channel is a general channel in the workspace."""
    is_group: list[bool]
    """Indicates if the channel is a group (private channel) rather than a regular channel."""
    is_im: list[bool]
    """Indicates if the entity is a direct message (IM) channel."""
    is_member: list[bool]
    """Indicates if the calling user is a member of the channel."""
    is_mpim: list[bool]
    """Indicates if the entity is a multiple person direct message (MPIM) channel."""
    is_org_shared: list[bool]
    """Indicates if the channel is organization-wide shared."""
    is_pending_ext_shared: list[bool]
    """Indicates if the channel is pending external shared."""
    is_private: list[bool]
    """Indicates if the channel is a private channel."""
    is_read_only: list[bool]
    """Indicates if the channel is read-only."""
    is_shared: list[bool]
    """Indicates if the channel is shared."""
    last_read: list[str]
    """The timestamp of the user's last read message in the channel."""
    locale: list[str]
    """The locale of the channel."""
    name: list[str]
    """The name of the channel."""
    name_normalized: list[str]
    """The normalized name of the channel."""
    num_members: list[int]
    """The number of members in the channel."""
    parent_conversation: list[str]
    """The parent conversation of the channel."""
    pending_connected_team_ids: list[list[Any]]
    """The IDs of teams that are pending to be connected to the channel."""
    pending_shared: list[list[Any]]
    """The list of pending shared items of the channel."""
    previous_names: list[list[Any]]
    """The previous names of the channel."""
    purpose: list[dict[str, Any]]
    """The purpose of the channel."""
    shared_team_ids: list[list[Any]]
    """The IDs of teams with which the channel is shared."""
    topic: list[dict[str, Any]]
    """The topic of the channel."""
    unlinked: list[int]
    """Indicates if the channel is unlinked."""
    updated: list[int]
    """The timestamp when the channel was last updated."""


class ChannelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    context_team_id: Any
    """The unique identifier of the team context in which the channel exists."""
    created: Any
    """The timestamp when the channel was created."""
    creator: Any
    """The ID of the user who created the channel."""
    id: Any
    """The unique identifier of the channel."""
    is_archived: Any
    """Indicates if the channel is archived."""
    is_channel: Any
    """Indicates if the entity is a channel."""
    is_ext_shared: Any
    """Indicates if the channel is externally shared."""
    is_general: Any
    """Indicates if the channel is a general channel in the workspace."""
    is_group: Any
    """Indicates if the channel is a group (private channel) rather than a regular channel."""
    is_im: Any
    """Indicates if the entity is a direct message (IM) channel."""
    is_member: Any
    """Indicates if the calling user is a member of the channel."""
    is_mpim: Any
    """Indicates if the entity is a multiple person direct message (MPIM) channel."""
    is_org_shared: Any
    """Indicates if the channel is organization-wide shared."""
    is_pending_ext_shared: Any
    """Indicates if the channel is pending external shared."""
    is_private: Any
    """Indicates if the channel is a private channel."""
    is_read_only: Any
    """Indicates if the channel is read-only."""
    is_shared: Any
    """Indicates if the channel is shared."""
    last_read: Any
    """The timestamp of the user's last read message in the channel."""
    locale: Any
    """The locale of the channel."""
    name: Any
    """The name of the channel."""
    name_normalized: Any
    """The normalized name of the channel."""
    num_members: Any
    """The number of members in the channel."""
    parent_conversation: Any
    """The parent conversation of the channel."""
    pending_connected_team_ids: Any
    """The IDs of teams that are pending to be connected to the channel."""
    pending_shared: Any
    """The list of pending shared items of the channel."""
    previous_names: Any
    """The previous names of the channel."""
    purpose: Any
    """The purpose of the channel."""
    shared_team_ids: Any
    """The IDs of teams with which the channel is shared."""
    topic: Any
    """The topic of the channel."""
    unlinked: Any
    """Indicates if the channel is unlinked."""
    updated: Any
    """The timestamp when the channel was last updated."""


class ChannelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    context_team_id: str
    """The unique identifier of the team context in which the channel exists."""
    created: str
    """The timestamp when the channel was created."""
    creator: str
    """The ID of the user who created the channel."""
    id: str
    """The unique identifier of the channel."""
    is_archived: str
    """Indicates if the channel is archived."""
    is_channel: str
    """Indicates if the entity is a channel."""
    is_ext_shared: str
    """Indicates if the channel is externally shared."""
    is_general: str
    """Indicates if the channel is a general channel in the workspace."""
    is_group: str
    """Indicates if the channel is a group (private channel) rather than a regular channel."""
    is_im: str
    """Indicates if the entity is a direct message (IM) channel."""
    is_member: str
    """Indicates if the calling user is a member of the channel."""
    is_mpim: str
    """Indicates if the entity is a multiple person direct message (MPIM) channel."""
    is_org_shared: str
    """Indicates if the channel is organization-wide shared."""
    is_pending_ext_shared: str
    """Indicates if the channel is pending external shared."""
    is_private: str
    """Indicates if the channel is a private channel."""
    is_read_only: str
    """Indicates if the channel is read-only."""
    is_shared: str
    """Indicates if the channel is shared."""
    last_read: str
    """The timestamp of the user's last read message in the channel."""
    locale: str
    """The locale of the channel."""
    name: str
    """The name of the channel."""
    name_normalized: str
    """The normalized name of the channel."""
    num_members: str
    """The number of members in the channel."""
    parent_conversation: str
    """The parent conversation of the channel."""
    pending_connected_team_ids: str
    """The IDs of teams that are pending to be connected to the channel."""
    pending_shared: str
    """The list of pending shared items of the channel."""
    previous_names: str
    """The previous names of the channel."""
    purpose: str
    """The purpose of the channel."""
    shared_team_ids: str
    """The IDs of teams with which the channel is shared."""
    topic: str
    """The topic of the channel."""
    unlinked: str
    """Indicates if the channel is unlinked."""
    updated: str
    """The timestamp when the channel was last updated."""


class ChannelsSortFilter(TypedDict, total=False):
    """Available fields for sorting channels search results."""
    context_team_id: AirbyteSortOrder
    """The unique identifier of the team context in which the channel exists."""
    created: AirbyteSortOrder
    """The timestamp when the channel was created."""
    creator: AirbyteSortOrder
    """The ID of the user who created the channel."""
    id: AirbyteSortOrder
    """The unique identifier of the channel."""
    is_archived: AirbyteSortOrder
    """Indicates if the channel is archived."""
    is_channel: AirbyteSortOrder
    """Indicates if the entity is a channel."""
    is_ext_shared: AirbyteSortOrder
    """Indicates if the channel is externally shared."""
    is_general: AirbyteSortOrder
    """Indicates if the channel is a general channel in the workspace."""
    is_group: AirbyteSortOrder
    """Indicates if the channel is a group (private channel) rather than a regular channel."""
    is_im: AirbyteSortOrder
    """Indicates if the entity is a direct message (IM) channel."""
    is_member: AirbyteSortOrder
    """Indicates if the calling user is a member of the channel."""
    is_mpim: AirbyteSortOrder
    """Indicates if the entity is a multiple person direct message (MPIM) channel."""
    is_org_shared: AirbyteSortOrder
    """Indicates if the channel is organization-wide shared."""
    is_pending_ext_shared: AirbyteSortOrder
    """Indicates if the channel is pending external shared."""
    is_private: AirbyteSortOrder
    """Indicates if the channel is a private channel."""
    is_read_only: AirbyteSortOrder
    """Indicates if the channel is read-only."""
    is_shared: AirbyteSortOrder
    """Indicates if the channel is shared."""
    last_read: AirbyteSortOrder
    """The timestamp of the user's last read message in the channel."""
    locale: AirbyteSortOrder
    """The locale of the channel."""
    name: AirbyteSortOrder
    """The name of the channel."""
    name_normalized: AirbyteSortOrder
    """The normalized name of the channel."""
    num_members: AirbyteSortOrder
    """The number of members in the channel."""
    parent_conversation: AirbyteSortOrder
    """The parent conversation of the channel."""
    pending_connected_team_ids: AirbyteSortOrder
    """The IDs of teams that are pending to be connected to the channel."""
    pending_shared: AirbyteSortOrder
    """The list of pending shared items of the channel."""
    previous_names: AirbyteSortOrder
    """The previous names of the channel."""
    purpose: AirbyteSortOrder
    """The purpose of the channel."""
    shared_team_ids: AirbyteSortOrder
    """The IDs of teams with which the channel is shared."""
    topic: AirbyteSortOrder
    """The topic of the channel."""
    unlinked: AirbyteSortOrder
    """Indicates if the channel is unlinked."""
    updated: AirbyteSortOrder
    """The timestamp when the channel was last updated."""


# Entity-specific condition types for channels
class ChannelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ChannelsSearchFilter


class ChannelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ChannelsSearchFilter


class ChannelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ChannelsSearchFilter


class ChannelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ChannelsSearchFilter


class ChannelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ChannelsSearchFilter


class ChannelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ChannelsSearchFilter


class ChannelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ChannelsStringFilter


class ChannelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ChannelsStringFilter


class ChannelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ChannelsStringFilter


class ChannelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ChannelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ChannelsInCondition = TypedDict("ChannelsInCondition", {"in": ChannelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ChannelsNotCondition = TypedDict("ChannelsNotCondition", {"not": "ChannelsCondition"}, total=False)
"""Negates the nested condition."""

ChannelsAndCondition = TypedDict("ChannelsAndCondition", {"and": "list[ChannelsCondition]"}, total=False)
"""True if all nested conditions are true."""

ChannelsOrCondition = TypedDict("ChannelsOrCondition", {"or": "list[ChannelsCondition]"}, total=False)
"""True if any nested condition is true."""

ChannelsAnyCondition = TypedDict("ChannelsAnyCondition", {"any": ChannelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all channels condition types
ChannelsCondition = (
    ChannelsEqCondition
    | ChannelsNeqCondition
    | ChannelsGtCondition
    | ChannelsGteCondition
    | ChannelsLtCondition
    | ChannelsLteCondition
    | ChannelsInCondition
    | ChannelsLikeCondition
    | ChannelsFuzzyCondition
    | ChannelsKeywordCondition
    | ChannelsContainsCondition
    | ChannelsNotCondition
    | ChannelsAndCondition
    | ChannelsOrCondition
    | ChannelsAnyCondition
)


class ChannelsSearchQuery(TypedDict, total=False):
    """Search query for channels entity."""
    filter: ChannelsCondition
    sort: list[ChannelsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    color: str | None
    """The color assigned to the user for visual purposes."""
    deleted: bool | None
    """Indicates if the user is deleted or not."""
    has_2fa: bool | None
    """Flag indicating if the user has two-factor authentication enabled."""
    id: str | None
    """Unique identifier for the user."""
    is_admin: bool | None
    """Flag specifying if the user is an admin or not."""
    is_app_user: bool | None
    """Specifies if the user is an app user."""
    is_bot: bool | None
    """Indicates if the user is a bot account."""
    is_email_confirmed: bool | None
    """Flag indicating if the user's email is confirmed."""
    is_forgotten: bool | None
    """Specifies if the user is marked as forgotten."""
    is_invited_user: bool | None
    """Indicates if the user is invited or not."""
    is_owner: bool | None
    """Flag indicating if the user is an owner."""
    is_primary_owner: bool | None
    """Specifies if the user is the primary owner."""
    is_restricted: bool | None
    """Flag specifying if the user is restricted."""
    is_ultra_restricted: bool | None
    """Indicates if the user has ultra-restricted access."""
    name: str | None
    """The username of the user."""
    profile: dict[str, Any] | None
    """User's profile information containing detailed details."""
    real_name: str | None
    """The real name of the user."""
    team_id: str | None
    """Unique identifier for the team the user belongs to."""
    tz: str | None
    """Timezone of the user."""
    tz_label: str | None
    """Label representing the timezone of the user."""
    tz_offset: int | None
    """Offset of the user's timezone."""
    updated: int | None
    """Timestamp of when the user's information was last updated."""
    who_can_share_contact_card: str | None
    """Specifies who can share the user's contact card."""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    color: list[str]
    """The color assigned to the user for visual purposes."""
    deleted: list[bool]
    """Indicates if the user is deleted or not."""
    has_2fa: list[bool]
    """Flag indicating if the user has two-factor authentication enabled."""
    id: list[str]
    """Unique identifier for the user."""
    is_admin: list[bool]
    """Flag specifying if the user is an admin or not."""
    is_app_user: list[bool]
    """Specifies if the user is an app user."""
    is_bot: list[bool]
    """Indicates if the user is a bot account."""
    is_email_confirmed: list[bool]
    """Flag indicating if the user's email is confirmed."""
    is_forgotten: list[bool]
    """Specifies if the user is marked as forgotten."""
    is_invited_user: list[bool]
    """Indicates if the user is invited or not."""
    is_owner: list[bool]
    """Flag indicating if the user is an owner."""
    is_primary_owner: list[bool]
    """Specifies if the user is the primary owner."""
    is_restricted: list[bool]
    """Flag specifying if the user is restricted."""
    is_ultra_restricted: list[bool]
    """Indicates if the user has ultra-restricted access."""
    name: list[str]
    """The username of the user."""
    profile: list[dict[str, Any]]
    """User's profile information containing detailed details."""
    real_name: list[str]
    """The real name of the user."""
    team_id: list[str]
    """Unique identifier for the team the user belongs to."""
    tz: list[str]
    """Timezone of the user."""
    tz_label: list[str]
    """Label representing the timezone of the user."""
    tz_offset: list[int]
    """Offset of the user's timezone."""
    updated: list[int]
    """Timestamp of when the user's information was last updated."""
    who_can_share_contact_card: list[str]
    """Specifies who can share the user's contact card."""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    color: Any
    """The color assigned to the user for visual purposes."""
    deleted: Any
    """Indicates if the user is deleted or not."""
    has_2fa: Any
    """Flag indicating if the user has two-factor authentication enabled."""
    id: Any
    """Unique identifier for the user."""
    is_admin: Any
    """Flag specifying if the user is an admin or not."""
    is_app_user: Any
    """Specifies if the user is an app user."""
    is_bot: Any
    """Indicates if the user is a bot account."""
    is_email_confirmed: Any
    """Flag indicating if the user's email is confirmed."""
    is_forgotten: Any
    """Specifies if the user is marked as forgotten."""
    is_invited_user: Any
    """Indicates if the user is invited or not."""
    is_owner: Any
    """Flag indicating if the user is an owner."""
    is_primary_owner: Any
    """Specifies if the user is the primary owner."""
    is_restricted: Any
    """Flag specifying if the user is restricted."""
    is_ultra_restricted: Any
    """Indicates if the user has ultra-restricted access."""
    name: Any
    """The username of the user."""
    profile: Any
    """User's profile information containing detailed details."""
    real_name: Any
    """The real name of the user."""
    team_id: Any
    """Unique identifier for the team the user belongs to."""
    tz: Any
    """Timezone of the user."""
    tz_label: Any
    """Label representing the timezone of the user."""
    tz_offset: Any
    """Offset of the user's timezone."""
    updated: Any
    """Timestamp of when the user's information was last updated."""
    who_can_share_contact_card: Any
    """Specifies who can share the user's contact card."""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    color: str
    """The color assigned to the user for visual purposes."""
    deleted: str
    """Indicates if the user is deleted or not."""
    has_2fa: str
    """Flag indicating if the user has two-factor authentication enabled."""
    id: str
    """Unique identifier for the user."""
    is_admin: str
    """Flag specifying if the user is an admin or not."""
    is_app_user: str
    """Specifies if the user is an app user."""
    is_bot: str
    """Indicates if the user is a bot account."""
    is_email_confirmed: str
    """Flag indicating if the user's email is confirmed."""
    is_forgotten: str
    """Specifies if the user is marked as forgotten."""
    is_invited_user: str
    """Indicates if the user is invited or not."""
    is_owner: str
    """Flag indicating if the user is an owner."""
    is_primary_owner: str
    """Specifies if the user is the primary owner."""
    is_restricted: str
    """Flag specifying if the user is restricted."""
    is_ultra_restricted: str
    """Indicates if the user has ultra-restricted access."""
    name: str
    """The username of the user."""
    profile: str
    """User's profile information containing detailed details."""
    real_name: str
    """The real name of the user."""
    team_id: str
    """Unique identifier for the team the user belongs to."""
    tz: str
    """Timezone of the user."""
    tz_label: str
    """Label representing the timezone of the user."""
    tz_offset: str
    """Offset of the user's timezone."""
    updated: str
    """Timestamp of when the user's information was last updated."""
    who_can_share_contact_card: str
    """Specifies who can share the user's contact card."""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    color: AirbyteSortOrder
    """The color assigned to the user for visual purposes."""
    deleted: AirbyteSortOrder
    """Indicates if the user is deleted or not."""
    has_2fa: AirbyteSortOrder
    """Flag indicating if the user has two-factor authentication enabled."""
    id: AirbyteSortOrder
    """Unique identifier for the user."""
    is_admin: AirbyteSortOrder
    """Flag specifying if the user is an admin or not."""
    is_app_user: AirbyteSortOrder
    """Specifies if the user is an app user."""
    is_bot: AirbyteSortOrder
    """Indicates if the user is a bot account."""
    is_email_confirmed: AirbyteSortOrder
    """Flag indicating if the user's email is confirmed."""
    is_forgotten: AirbyteSortOrder
    """Specifies if the user is marked as forgotten."""
    is_invited_user: AirbyteSortOrder
    """Indicates if the user is invited or not."""
    is_owner: AirbyteSortOrder
    """Flag indicating if the user is an owner."""
    is_primary_owner: AirbyteSortOrder
    """Specifies if the user is the primary owner."""
    is_restricted: AirbyteSortOrder
    """Flag specifying if the user is restricted."""
    is_ultra_restricted: AirbyteSortOrder
    """Indicates if the user has ultra-restricted access."""
    name: AirbyteSortOrder
    """The username of the user."""
    profile: AirbyteSortOrder
    """User's profile information containing detailed details."""
    real_name: AirbyteSortOrder
    """The real name of the user."""
    team_id: AirbyteSortOrder
    """Unique identifier for the team the user belongs to."""
    tz: AirbyteSortOrder
    """Timezone of the user."""
    tz_label: AirbyteSortOrder
    """Label representing the timezone of the user."""
    tz_offset: AirbyteSortOrder
    """Offset of the user's timezone."""
    updated: AirbyteSortOrder
    """Timestamp of when the user's information was last updated."""
    who_can_share_contact_card: AirbyteSortOrder
    """Specifies who can share the user's contact card."""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
