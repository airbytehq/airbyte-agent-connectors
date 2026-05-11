"""
Pydantic models for slack connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration - multiple options available

class SlackTokenAuthenticationAuthConfig(BaseModel):
    """Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    bot_key: str
    """Your Slack Bot Key (xoxb-) or User Token (xoxp-)"""

class SlackOauth20AuthenticationAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: Optional[str] = None
    """Your Slack App's Client ID"""
    client_secret: Optional[str] = None
    """Your Slack App's Client Secret"""
    access_token: str
    """OAuth access token (bot token from oauth.v2.access response)"""

SlackAuthConfig = SlackTokenAuthenticationAuthConfig | SlackOauth20AuthenticationAuthConfig

# Replication configuration

class SlackReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Slack."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data."""
    lookback_window: int
    """Number of days to look back when syncing data (0-365)."""
    join_channels: bool
    """Whether to automatically join public channels to sync messages."""
    include_archived_channels: bool
    """Whether to include archived channels in the sync. When disabled (default), archived channels are excluded from the Slack API response, reducing the number of API calls for downstream streams such as channel_messages, threads, and channel_members."""
    threads_ignore_no_replies: bool
    """When enabled, the threads stream will skip messages that have no replies, reducing the number of API calls. Disabled by default to make the Threads stream contain unthreaded messages in its records."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class User(BaseModel):
    """Slack user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    team_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    color: str | None = Field(default=None)
    real_name: str | None = Field(default=None)
    tz: str | None = Field(default=None)
    tz_label: str | None = Field(default=None)
    tz_offset: int | None = Field(default=None)
    profile: Any | None = Field(default=None)
    is_admin: bool | None = Field(default=None)
    is_owner: bool | None = Field(default=None)
    is_primary_owner: bool | None = Field(default=None)
    is_restricted: bool | None = Field(default=None)
    is_ultra_restricted: bool | None = Field(default=None)
    is_bot: bool | None = Field(default=None)
    is_app_user: bool | None = Field(default=None)
    updated: int | None = Field(default=None)
    is_email_confirmed: bool | None = Field(default=None)
    who_can_share_contact_card: str | None = Field(default=None)

class UserProfile(BaseModel):
    """User profile information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    skype: str | None = Field(default=None)
    real_name: str | None = Field(default=None)
    real_name_normalized: str | None = Field(default=None)
    display_name: str | None = Field(default=None)
    display_name_normalized: str | None = Field(default=None)
    status_text: str | None = Field(default=None)
    status_emoji: str | None = Field(default=None)
    status_expiration: int | None = Field(default=None)
    avatar_hash: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    image_24: str | None = Field(default=None)
    image_32: str | None = Field(default=None)
    image_48: str | None = Field(default=None)
    image_72: str | None = Field(default=None)
    image_192: str | None = Field(default=None)
    image_512: str | None = Field(default=None)
    team: str | None = Field(default=None)

class ResponseMetadata(BaseModel):
    """Response metadata including pagination"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

class UsersListResponse(BaseModel):
    """Response containing list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    members: list[User] | None = Field(default=None)
    cache_ts: int | None = Field(default=None)
    response_metadata: ResponseMetadata | None = Field(default=None)

class UserResponse(BaseModel):
    """Response containing single user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    user: User | None = Field(default=None)

class Channel(BaseModel):
    """Slack channel object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    is_channel: bool | None = Field(default=None)
    is_group: bool | None = Field(default=None)
    is_im: bool | None = Field(default=None)
    is_mpim: bool | None = Field(default=None)
    is_private: bool | None = Field(default=None)
    created: int | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    is_general: bool | None = Field(default=None)
    unlinked: int | None = Field(default=None)
    name_normalized: str | None = Field(default=None)
    is_shared: bool | None = Field(default=None)
    is_org_shared: bool | None = Field(default=None)
    is_pending_ext_shared: bool | None = Field(default=None)
    pending_shared: list[str] | None = Field(default=None)
    context_team_id: str | None = Field(default=None)
    updated: int | None = Field(default=None)
    creator: str | None = Field(default=None)
    is_ext_shared: bool | None = Field(default=None)
    shared_team_ids: list[str] | None = Field(default=None)
    pending_connected_team_ids: list[str] | None = Field(default=None)
    is_member: bool | None = Field(default=None)
    topic: Any | None = Field(default=None)
    purpose: Any | None = Field(default=None)
    previous_names: list[str] | None = Field(default=None)
    num_members: int | None = Field(default=None)
    parent_conversation: str | None = Field(default=None)
    properties: dict[str, Any] | None = Field(default=None)
    is_thread_only: bool | None = Field(default=None)
    is_read_only: bool | None = Field(default=None)

class ChannelTopic(BaseModel):
    """Channel topic information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str | None = Field(default=None)
    creator: str | None = Field(default=None)
    last_set: int | None = Field(default=None)

class ChannelPurpose(BaseModel):
    """Channel purpose information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str | None = Field(default=None)
    creator: str | None = Field(default=None)
    last_set: int | None = Field(default=None)

class ChannelsListResponse(BaseModel):
    """Response containing list of channels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channels: list[Channel] | None = Field(default=None)
    response_metadata: ResponseMetadata | None = Field(default=None)

class ChannelResponse(BaseModel):
    """Response containing single channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: Channel | None = Field(default=None)

class File(BaseModel):
    """File object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    title: str | None = Field(default=None)
    mimetype: str | None = Field(default=None)
    filetype: str | None = Field(default=None)
    pretty_type: str | None = Field(default=None)
    user: str | None = Field(default=None)
    size: int | None = Field(default=None)
    mode: str | None = Field(default=None)
    is_external: bool | None = Field(default=None)
    external_type: str | None = Field(default=None)
    is_public: bool | None = Field(default=None)
    public_url_shared: bool | None = Field(default=None)
    url_private: str | None = Field(default=None)
    url_private_download: str | None = Field(default=None)
    permalink: str | None = Field(default=None)
    permalink_public: str | None = Field(default=None)
    created: int | None = Field(default=None)
    timestamp: int | None = Field(default=None)

class Reaction(BaseModel):
    """Message reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    users: list[str] | None = Field(default=None)
    count: int | None = Field(default=None)

class Attachment(BaseModel):
    """Message attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    fallback: str | None = Field(default=None)
    color: str | None = Field(default=None)
    pretext: str | None = Field(default=None)
    author_name: str | None = Field(default=None)
    author_link: str | None = Field(default=None)
    author_icon: str | None = Field(default=None)
    title: str | None = Field(default=None)
    title_link: str | None = Field(default=None)
    text: str | None = Field(default=None)
    fields: list[dict[str, Any]] | None = Field(default=None)
    image_url: str | None = Field(default=None)
    thumb_url: str | None = Field(default=None)
    footer: str | None = Field(default=None)
    footer_icon: str | None = Field(default=None)
    ts: Any | None = Field(default=None)

class Message(BaseModel):
    """Slack message object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    subtype: str | None = Field(default=None)
    ts: str | None = Field(default=None)
    user: str | None = Field(default=None)
    text: str | None = Field(default=None)
    thread_ts: str | None = Field(default=None)
    reply_count: int | None = Field(default=None)
    reply_users_count: int | None = Field(default=None)
    latest_reply: str | None = Field(default=None)
    reply_users: list[str] | None = Field(default=None)
    is_locked: bool | None = Field(default=None)
    subscribed: bool | None = Field(default=None)
    reactions: list[Reaction] | None = Field(default=None)
    attachments: list[Attachment] | None = Field(default=None)
    blocks: list[dict[str, Any]] | None = Field(default=None)
    files: list[File] | None = Field(default=None)
    edited: Any | None = Field(default=None)
    bot_id: str | None = Field(default=None)
    bot_profile: Any | None = Field(default=None)
    app_id: str | None = Field(default=None)
    team: str | None = Field(default=None)

class Thread(BaseModel):
    """Slack thread reply message object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    subtype: str | None = Field(default=None)
    ts: str | None = Field(default=None)
    user: str | None = Field(default=None)
    text: str | None = Field(default=None)
    thread_ts: str | None = Field(default=None)
    parent_user_id: str | None = Field(default=None)
    reply_count: int | None = Field(default=None)
    reply_users_count: int | None = Field(default=None)
    latest_reply: str | None = Field(default=None)
    reply_users: list[str] | None = Field(default=None)
    is_locked: bool | None = Field(default=None)
    subscribed: bool | None = Field(default=None)
    reactions: list[Reaction] | None = Field(default=None)
    attachments: list[Attachment] | None = Field(default=None)
    blocks: list[dict[str, Any]] | None = Field(default=None)
    files: list[File] | None = Field(default=None)
    edited: Any | None = Field(default=None)
    bot_id: str | None = Field(default=None)
    bot_profile: Any | None = Field(default=None)
    app_id: str | None = Field(default=None)
    team: str | None = Field(default=None)

class EditedInfo(BaseModel):
    """Message edit information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: str | None = Field(default=None)
    ts: str | None = Field(default=None)

class BotProfile(BaseModel):
    """Bot profile information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    name: str | None = Field(default=None)
    updated: int | None = Field(default=None)
    app_id: str | None = Field(default=None)
    team_id: str | None = Field(default=None)

class MessagesListResponse(BaseModel):
    """Response containing list of messages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    messages: list[Message] | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    pin_count: int | None = Field(default=None)
    response_metadata: ResponseMetadata | None = Field(default=None)

class ThreadRepliesResponse(BaseModel):
    """Response containing thread replies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    messages: list[Thread] | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    response_metadata: ResponseMetadata | None = Field(default=None)

class MessageCreateParams(BaseModel):
    """Parameters for creating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    text: str
    thread_ts: str | None = Field(default=None)
    reply_broadcast: bool | None = Field(default=None)
    unfurl_links: bool | None = Field(default=None)
    unfurl_media: bool | None = Field(default=None)

class CreatedMessage(BaseModel):
    """A message object returned from create/update operations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    subtype: str | None = Field(default=None)
    text: str | None = Field(default=None)
    ts: str | None = Field(default=None)
    user: str | None = Field(default=None)
    bot_id: str | None = Field(default=None)
    app_id: str | None = Field(default=None)
    team: str | None = Field(default=None)
    bot_profile: Any | None = Field(default=None)

class MessageCreateResponse(BaseModel):
    """Response from creating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: str | None = Field(default=None)
    ts: str | None = Field(default=None)
    message: CreatedMessage | None = Field(default=None)

class MessageUpdateParams(BaseModel):
    """Parameters for updating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    ts: str
    text: str

class MessageUpdateResponse(BaseModel):
    """Response from updating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: str | None = Field(default=None)
    ts: str | None = Field(default=None)
    text: str | None = Field(default=None)
    message: CreatedMessage | None = Field(default=None)

class ChannelCreateParams(BaseModel):
    """Parameters for creating a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    is_private: bool | None = Field(default=None)

class ChannelCreateResponse(BaseModel):
    """Response from creating a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: Channel | None = Field(default=None)

class ChannelRenameParams(BaseModel):
    """Parameters for renaming a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    name: str

class ChannelRenameResponse(BaseModel):
    """Response from renaming a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: Channel | None = Field(default=None)

class ChannelTopicParams(BaseModel):
    """Parameters for setting channel topic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    topic: str

class ChannelTopicResponse(BaseModel):
    """Response from setting channel topic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: Channel | None = Field(default=None)

class ChannelPurposeParams(BaseModel):
    """Parameters for setting channel purpose"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    purpose: str

class ChannelPurposeResponse(BaseModel):
    """Response from setting channel purpose"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: Channel | None = Field(default=None)

class ChannelInviteParams(BaseModel):
    """Parameters for inviting users to a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    users: str
    force: bool | None = Field(default=None)

class ChannelInviteResponse(BaseModel):
    """Response from inviting users to a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: Channel | None = Field(default=None)

class ReactionAddParams(BaseModel):
    """Parameters for adding a reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    timestamp: str
    name: str

class ReactionAddResponse(BaseModel):
    """Response from adding a reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)

class ReactionRemoveParams(BaseModel):
    """Parameters for removing a reaction from a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    timestamp: str
    name: str

class ReactionRemoveResponse(BaseModel):
    """Response from removing a reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)

class EphemeralMessageCreateParams(BaseModel):
    """Parameters for sending an ephemeral message visible only to one user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    user: str
    text: str
    thread_ts: str | None = Field(default=None)
    blocks: str | None = Field(default=None)

class EphemeralMessageCreateResponse(BaseModel):
    """Response from sending an ephemeral message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    message_ts: str | None = Field(default=None)

class ScheduledMessageCreateParams(BaseModel):
    """Parameters for scheduling a message for future delivery"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    text: str
    post_at: int
    thread_ts: str | None = Field(default=None)
    reply_broadcast: bool | None = Field(default=None)
    unfurl_links: bool | None = Field(default=None)
    unfurl_media: bool | None = Field(default=None)

class ScheduledMessageCreateResponse(BaseModel):
    """Response from scheduling a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: str | None = Field(default=None)
    scheduled_message_id: str | None = Field(default=None)
    post_at: int | None = Field(default=None)
    message: Any | None = Field(default=None)

class ScheduledMessageContent(BaseModel):
    """Content of a scheduled message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text: str | None = Field(default=None)
    username: str | None = Field(default=None)
    bot_id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    subtype: str | None = Field(default=None)
    user: str | None = Field(default=None)
    team: str | None = Field(default=None)
    app_id: str | None = Field(default=None)
    bot_profile: dict[str, Any] | None = Field(default=None)
    blocks: list[dict[str, Any]] | None = Field(default=None)
    attachments: list[Attachment] | None = Field(default=None)

class MessageDeleteParams(BaseModel):
    """Parameters for deleting a message. Bot tokens can only delete messages posted by the bot."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    ts: str

class MessageDeleteResponse(BaseModel):
    """Response from deleting a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    channel: str | None = Field(default=None)
    ts: str | None = Field(default=None)

class ChannelArchiveParams(BaseModel):
    """Parameters for archiving a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str

class ChannelArchiveResponse(BaseModel):
    """Response from archiving a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)

class ChannelKickParams(BaseModel):
    """Parameters for removing a user from a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    user: str

class ChannelKickResponse(BaseModel):
    """Response from removing a user from a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    errors: dict[str, Any] | None = Field(default=None)

class PinAddParams(BaseModel):
    """Parameters for pinning a message to a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: str
    timestamp: str

class PinAddResponse(BaseModel):
    """Response from pinning a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)

class BookmarkAddParams(BaseModel):
    """Parameters for adding a bookmark to a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel_id: str
    title: str
    type_: str = Field(alias="type")
    link: str | None = Field(default=None)
    emoji: str | None = Field(default=None)

class Bookmark(BaseModel):
    """A channel bookmark"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    channel_id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    link: str | None = Field(default=None)
    emoji: str | None = Field(default=None)
    icon_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    entity_id: str | None = Field(default=None)
    date_created: int | None = Field(default=None)
    date_updated: int | None = Field(default=None)
    rank: str | None = Field(default=None)
    last_updated_by_user_id: str | None = Field(default=None)
    last_updated_by_team_id: str | None = Field(default=None)
    shortcut_id: str | None = Field(default=None)
    app_id: str | None = Field(default=None)

class BookmarkAddResponse(BaseModel):
    """Response from adding a bookmark"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: bool | None = Field(default=None)
    bookmark: Bookmark | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

class ChannelsListResultMeta(BaseModel):
    """Metadata for channels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

class ChannelMessagesListResultMeta(BaseModel):
    """Metadata for channel_messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class ThreadsListResultMeta(BaseModel):
    """Metadata for threads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class SlackCheckResult(BaseModel):
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


class SlackExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class SlackExecuteResultWithMeta(SlackExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ChannelsSearchData(BaseModel):
    """Search result data for channels entity."""
    model_config = ConfigDict(extra="allow")

    context_team_id: str | None = None
    """The unique identifier of the team context in which the channel exists."""
    created: int | None = None
    """The timestamp when the channel was created."""
    creator: str | None = None
    """The ID of the user who created the channel."""
    id: str | None = None
    """The unique identifier of the channel."""
    is_archived: bool | None = None
    """Indicates if the channel is archived."""
    is_channel: bool | None = None
    """Indicates if the entity is a channel."""
    is_ext_shared: bool | None = None
    """Indicates if the channel is externally shared."""
    is_general: bool | None = None
    """Indicates if the channel is a general channel in the workspace."""
    is_group: bool | None = None
    """Indicates if the channel is a group (private channel) rather than a regular channel."""
    is_im: bool | None = None
    """Indicates if the entity is a direct message (IM) channel."""
    is_member: bool | None = None
    """Indicates if the calling user is a member of the channel."""
    is_mpim: bool | None = None
    """Indicates if the entity is a multiple person direct message (MPIM) channel."""
    is_org_shared: bool | None = None
    """Indicates if the channel is organization-wide shared."""
    is_pending_ext_shared: bool | None = None
    """Indicates if the channel is pending external shared."""
    is_private: bool | None = None
    """Indicates if the channel is a private channel."""
    is_read_only: bool | None = None
    """Indicates if the channel is read-only."""
    is_shared: bool | None = None
    """Indicates if the channel is shared."""
    last_read: str | None = None
    """The timestamp of the user's last read message in the channel."""
    locale: str | None = None
    """The locale of the channel."""
    name: str | None = None
    """The name of the channel."""
    name_normalized: str | None = None
    """The normalized name of the channel."""
    num_members: int | None = None
    """The number of members in the channel."""
    parent_conversation: str | None = None
    """The parent conversation of the channel."""
    pending_connected_team_ids: list[Any] | None = None
    """The IDs of teams that are pending to be connected to the channel."""
    pending_shared: list[Any] | None = None
    """The list of pending shared items of the channel."""
    previous_names: list[Any] | None = None
    """The previous names of the channel."""
    purpose: dict[str, Any] | None = None
    """The purpose of the channel."""
    shared_team_ids: list[Any] | None = None
    """The IDs of teams with which the channel is shared."""
    topic: dict[str, Any] | None = None
    """The topic of the channel."""
    unlinked: int | None = None
    """Indicates if the channel is unlinked."""
    updated: int | None = None
    """The timestamp when the channel was last updated."""


class ChannelMessagesSearchData(BaseModel):
    """Search result data for channel_messages entity."""
    model_config = ConfigDict(extra="allow")

    type_: str | None = None
    """Message type."""
    subtype: str | None = None
    """Message subtype."""
    ts: str | None = None
    """Message timestamp (unique identifier)."""
    user: str | None = None
    """User ID who sent the message."""
    text: str | None = None
    """Message text content."""
    thread_ts: str | None = None
    """Thread parent timestamp."""
    reply_count: int | None = None
    """Number of replies in thread."""
    reply_users_count: int | None = None
    """Number of unique users who replied."""
    latest_reply: str | None = None
    """Timestamp of latest reply."""
    reply_users: list[Any] | None = None
    """User IDs who replied to the thread."""
    is_locked: bool | None = None
    """Whether the thread is locked."""
    subscribed: bool | None = None
    """Whether the user is subscribed to the thread."""
    reactions: list[Any] | None = None
    """Reactions to the message."""
    attachments: list[Any] | None = None
    """Message attachments."""
    blocks: list[Any] | None = None
    """Block kit blocks."""
    bot_id: str | None = None
    """Bot ID if message was sent by a bot."""
    bot_profile: dict[str, Any] | None = None
    """Bot profile information."""
    team: str | None = None
    """Team ID."""


class ThreadsSearchData(BaseModel):
    """Search result data for threads entity."""
    model_config = ConfigDict(extra="allow")

    type_: str | None = None
    """Message type."""
    subtype: str | None = None
    """Message subtype."""
    ts: str | None = None
    """Message timestamp (unique identifier)."""
    user: str | None = None
    """User ID who sent the message."""
    text: str | None = None
    """Message text content."""
    thread_ts: str | None = None
    """Thread parent timestamp."""
    parent_user_id: str | None = None
    """User ID of the parent message author (present in thread replies)."""
    reply_count: int | None = None
    """Number of replies in thread."""
    reply_users_count: int | None = None
    """Number of unique users who replied."""
    latest_reply: str | None = None
    """Timestamp of latest reply."""
    reply_users: list[Any] | None = None
    """User IDs who replied to the thread."""
    is_locked: bool | None = None
    """Whether the thread is locked."""
    subscribed: bool | None = None
    """Whether the user is subscribed to the thread."""
    blocks: list[Any] | None = None
    """Block kit blocks."""
    bot_id: str | None = None
    """Bot ID if message was sent by a bot."""
    team: str | None = None
    """Team ID."""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    color: str | None = None
    """The color assigned to the user for visual purposes."""
    deleted: bool | None = None
    """Indicates if the user is deleted or not."""
    has_2fa: bool | None = None
    """Flag indicating if the user has two-factor authentication enabled."""
    id: str | None = None
    """Unique identifier for the user."""
    is_admin: bool | None = None
    """Flag specifying if the user is an admin or not."""
    is_app_user: bool | None = None
    """Specifies if the user is an app user."""
    is_bot: bool | None = None
    """Indicates if the user is a bot account."""
    is_email_confirmed: bool | None = None
    """Flag indicating if the user's email is confirmed."""
    is_forgotten: bool | None = None
    """Specifies if the user is marked as forgotten."""
    is_invited_user: bool | None = None
    """Indicates if the user is invited or not."""
    is_owner: bool | None = None
    """Flag indicating if the user is an owner."""
    is_primary_owner: bool | None = None
    """Specifies if the user is the primary owner."""
    is_restricted: bool | None = None
    """Flag specifying if the user is restricted."""
    is_ultra_restricted: bool | None = None
    """Indicates if the user has ultra-restricted access."""
    name: str | None = None
    """The username of the user."""
    profile: dict[str, Any] | None = None
    """User's profile information containing detailed details."""
    real_name: str | None = None
    """The real name of the user."""
    team_id: str | None = None
    """Unique identifier for the team the user belongs to."""
    tz: str | None = None
    """Timezone of the user."""
    tz_label: str | None = None
    """Label representing the timezone of the user."""
    tz_offset: int | None = None
    """Offset of the user's timezone."""
    updated: int | None = None
    """Timestamp of when the user's information was last updated."""
    who_can_share_contact_card: str | None = None
    """Specifies who can share the user's contact card."""


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

ChannelsSearchResult = AirbyteSearchResult[ChannelsSearchData]
"""Search result type for channels entity."""

ChannelMessagesSearchResult = AirbyteSearchResult[ChannelMessagesSearchData]
"""Search result type for channel_messages entity."""

ThreadsSearchResult = AirbyteSearchResult[ThreadsSearchData]
"""Search result type for threads entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = SlackExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

ChannelsListResult = SlackExecuteResultWithMeta[list[Channel], ChannelsListResultMeta]
"""Result type for channels.list operation with data and metadata."""

ChannelMessagesListResult = SlackExecuteResultWithMeta[list[Message], ChannelMessagesListResultMeta]
"""Result type for channel_messages.list operation with data and metadata."""

ThreadsListResult = SlackExecuteResultWithMeta[list[Thread], ThreadsListResultMeta]
"""Result type for threads.list operation with data and metadata."""

