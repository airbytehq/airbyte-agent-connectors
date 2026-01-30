"""
Pydantic models for slack connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration - multiple options available

class SlackTokenAuthenticationAuthConfig(BaseModel):
    """Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_token: str
    """Your Slack Bot Token (xoxb-) or User Token (xoxp-)"""

class SlackOauth20AuthenticationAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Your Slack App's Client ID"""
    client_secret: str
    """Your Slack App's Client Secret"""
    access_token: str
    """OAuth access token (bot token from oauth.v2.access response)"""

SlackAuthConfig = SlackTokenAuthenticationAuthConfig | SlackOauth20AuthenticationAuthConfig

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class User(BaseModel):
    """Slack user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    team_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    real_name: Union[str | None, Any] = Field(default=None)
    tz: Union[str | None, Any] = Field(default=None)
    tz_label: Union[str | None, Any] = Field(default=None)
    tz_offset: Union[int | None, Any] = Field(default=None)
    profile: Union[Any, Any] = Field(default=None)
    is_admin: Union[bool | None, Any] = Field(default=None)
    is_owner: Union[bool | None, Any] = Field(default=None)
    is_primary_owner: Union[bool | None, Any] = Field(default=None)
    is_restricted: Union[bool | None, Any] = Field(default=None)
    is_ultra_restricted: Union[bool | None, Any] = Field(default=None)
    is_bot: Union[bool | None, Any] = Field(default=None)
    is_app_user: Union[bool | None, Any] = Field(default=None)
    updated: Union[int | None, Any] = Field(default=None)
    is_email_confirmed: Union[bool | None, Any] = Field(default=None)
    who_can_share_contact_card: Union[str | None, Any] = Field(default=None)

class UserProfile(BaseModel):
    """User profile information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    skype: Union[str | None, Any] = Field(default=None)
    real_name: Union[str | None, Any] = Field(default=None)
    real_name_normalized: Union[str | None, Any] = Field(default=None)
    display_name: Union[str | None, Any] = Field(default=None)
    display_name_normalized: Union[str | None, Any] = Field(default=None)
    status_text: Union[str | None, Any] = Field(default=None)
    status_emoji: Union[str | None, Any] = Field(default=None)
    status_expiration: Union[int | None, Any] = Field(default=None)
    avatar_hash: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    image_24: Union[str | None, Any] = Field(default=None)
    image_32: Union[str | None, Any] = Field(default=None)
    image_48: Union[str | None, Any] = Field(default=None)
    image_72: Union[str | None, Any] = Field(default=None)
    image_192: Union[str | None, Any] = Field(default=None)
    image_512: Union[str | None, Any] = Field(default=None)
    team: Union[str | None, Any] = Field(default=None)

class ResponseMetadata(BaseModel):
    """Response metadata including pagination"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)

class UsersListResponse(BaseModel):
    """Response containing list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    members: Union[list[User], Any] = Field(default=None)
    cache_ts: Union[int | None, Any] = Field(default=None)
    response_metadata: Union[ResponseMetadata, Any] = Field(default=None)

class UserResponse(BaseModel):
    """Response containing single user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    user: Union[User, Any] = Field(default=None)

class Channel(BaseModel):
    """Slack channel object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    is_channel: Union[bool | None, Any] = Field(default=None)
    is_group: Union[bool | None, Any] = Field(default=None)
    is_im: Union[bool | None, Any] = Field(default=None)
    is_mpim: Union[bool | None, Any] = Field(default=None)
    is_private: Union[bool | None, Any] = Field(default=None)
    created: Union[int | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None)
    is_general: Union[bool | None, Any] = Field(default=None)
    unlinked: Union[int | None, Any] = Field(default=None)
    name_normalized: Union[str | None, Any] = Field(default=None)
    is_shared: Union[bool | None, Any] = Field(default=None)
    is_org_shared: Union[bool | None, Any] = Field(default=None)
    is_pending_ext_shared: Union[bool | None, Any] = Field(default=None)
    pending_shared: Union[list[str] | None, Any] = Field(default=None)
    context_team_id: Union[str | None, Any] = Field(default=None)
    updated: Union[int | None, Any] = Field(default=None)
    creator: Union[str | None, Any] = Field(default=None)
    is_ext_shared: Union[bool | None, Any] = Field(default=None)
    shared_team_ids: Union[list[str] | None, Any] = Field(default=None)
    pending_connected_team_ids: Union[list[str] | None, Any] = Field(default=None)
    is_member: Union[bool | None, Any] = Field(default=None)
    topic: Union[Any, Any] = Field(default=None)
    purpose: Union[Any, Any] = Field(default=None)
    previous_names: Union[list[str] | None, Any] = Field(default=None)
    num_members: Union[int | None, Any] = Field(default=None)
    parent_conversation: Union[str | None, Any] = Field(default=None)
    properties: Union[dict[str, Any] | None, Any] = Field(default=None)
    is_thread_only: Union[bool | None, Any] = Field(default=None)
    is_read_only: Union[bool | None, Any] = Field(default=None)

class ChannelTopic(BaseModel):
    """Channel topic information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str | None, Any] = Field(default=None)
    creator: Union[str | None, Any] = Field(default=None)
    last_set: Union[int | None, Any] = Field(default=None)

class ChannelPurpose(BaseModel):
    """Channel purpose information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str | None, Any] = Field(default=None)
    creator: Union[str | None, Any] = Field(default=None)
    last_set: Union[int | None, Any] = Field(default=None)

class ChannelsListResponse(BaseModel):
    """Response containing list of channels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channels: Union[list[Channel], Any] = Field(default=None)
    response_metadata: Union[ResponseMetadata, Any] = Field(default=None)

class ChannelResponse(BaseModel):
    """Response containing single channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[Channel, Any] = Field(default=None)

class Reaction(BaseModel):
    """Message reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None)
    users: Union[list[str] | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class Attachment(BaseModel):
    """Message attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    fallback: Union[str | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    pretext: Union[str | None, Any] = Field(default=None)
    author_name: Union[str | None, Any] = Field(default=None)
    author_link: Union[str | None, Any] = Field(default=None)
    author_icon: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    title_link: Union[str | None, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    fields: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    image_url: Union[str | None, Any] = Field(default=None)
    thumb_url: Union[str | None, Any] = Field(default=None)
    footer: Union[str | None, Any] = Field(default=None)
    footer_icon: Union[str | None, Any] = Field(default=None)
    ts: Union[Any, Any] = Field(default=None)

class File(BaseModel):
    """File object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    mimetype: Union[str | None, Any] = Field(default=None)
    filetype: Union[str | None, Any] = Field(default=None)
    pretty_type: Union[str | None, Any] = Field(default=None)
    user: Union[str | None, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)
    mode: Union[str | None, Any] = Field(default=None)
    is_external: Union[bool | None, Any] = Field(default=None)
    external_type: Union[str | None, Any] = Field(default=None)
    is_public: Union[bool | None, Any] = Field(default=None)
    public_url_shared: Union[bool | None, Any] = Field(default=None)
    url_private: Union[str | None, Any] = Field(default=None)
    url_private_download: Union[str | None, Any] = Field(default=None)
    permalink: Union[str | None, Any] = Field(default=None)
    permalink_public: Union[str | None, Any] = Field(default=None)
    created: Union[int | None, Any] = Field(default=None)
    timestamp: Union[int | None, Any] = Field(default=None)

class Message(BaseModel):
    """Slack message object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    subtype: Union[str | None, Any] = Field(default=None)
    ts: Union[str, Any] = Field(default=None)
    user: Union[str | None, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    thread_ts: Union[str | None, Any] = Field(default=None)
    reply_count: Union[int | None, Any] = Field(default=None)
    reply_users_count: Union[int | None, Any] = Field(default=None)
    latest_reply: Union[str | None, Any] = Field(default=None)
    reply_users: Union[list[str] | None, Any] = Field(default=None)
    is_locked: Union[bool | None, Any] = Field(default=None)
    subscribed: Union[bool | None, Any] = Field(default=None)
    reactions: Union[list[Reaction] | None, Any] = Field(default=None)
    attachments: Union[list[Attachment] | None, Any] = Field(default=None)
    blocks: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    files: Union[list[File] | None, Any] = Field(default=None)
    edited: Union[Any, Any] = Field(default=None)
    bot_id: Union[str | None, Any] = Field(default=None)
    bot_profile: Union[Any, Any] = Field(default=None)
    app_id: Union[str | None, Any] = Field(default=None)
    team: Union[str | None, Any] = Field(default=None)

class Thread(BaseModel):
    """Slack thread reply message object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    subtype: Union[str | None, Any] = Field(default=None)
    ts: Union[str, Any] = Field(default=None)
    user: Union[str | None, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    thread_ts: Union[str | None, Any] = Field(default=None)
    parent_user_id: Union[str | None, Any] = Field(default=None)
    reply_count: Union[int | None, Any] = Field(default=None)
    reply_users_count: Union[int | None, Any] = Field(default=None)
    latest_reply: Union[str | None, Any] = Field(default=None)
    reply_users: Union[list[str] | None, Any] = Field(default=None)
    is_locked: Union[bool | None, Any] = Field(default=None)
    subscribed: Union[bool | None, Any] = Field(default=None)
    reactions: Union[list[Reaction] | None, Any] = Field(default=None)
    attachments: Union[list[Attachment] | None, Any] = Field(default=None)
    blocks: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    files: Union[list[File] | None, Any] = Field(default=None)
    edited: Union[Any, Any] = Field(default=None)
    bot_id: Union[str | None, Any] = Field(default=None)
    bot_profile: Union[Any, Any] = Field(default=None)
    app_id: Union[str | None, Any] = Field(default=None)
    team: Union[str | None, Any] = Field(default=None)

class EditedInfo(BaseModel):
    """Message edit information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: Union[str | None, Any] = Field(default=None)
    ts: Union[str | None, Any] = Field(default=None)

class BotProfile(BaseModel):
    """Bot profile information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    updated: Union[int | None, Any] = Field(default=None)
    app_id: Union[str | None, Any] = Field(default=None)
    team_id: Union[str | None, Any] = Field(default=None)

class MessagesListResponse(BaseModel):
    """Response containing list of messages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    messages: Union[list[Message], Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    pin_count: Union[int | None, Any] = Field(default=None)
    response_metadata: Union[ResponseMetadata, Any] = Field(default=None)

class ThreadRepliesResponse(BaseModel):
    """Response containing thread replies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    messages: Union[list[Thread], Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    response_metadata: Union[ResponseMetadata, Any] = Field(default=None)

class MessageCreateParams(BaseModel):
    """Parameters for creating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: Union[str, Any] = Field(default=None)
    text: Union[str, Any] = Field(default=None)
    thread_ts: Union[str, Any] = Field(default=None)
    reply_broadcast: Union[bool, Any] = Field(default=None)
    unfurl_links: Union[bool, Any] = Field(default=None)
    unfurl_media: Union[bool, Any] = Field(default=None)

class CreatedMessage(BaseModel):
    """A message object returned from create/update operations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    subtype: Union[str | None, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    ts: Union[str, Any] = Field(default=None)
    user: Union[str | None, Any] = Field(default=None)
    bot_id: Union[str | None, Any] = Field(default=None)
    app_id: Union[str | None, Any] = Field(default=None)
    team: Union[str | None, Any] = Field(default=None)
    bot_profile: Union[Any, Any] = Field(default=None)

class MessageCreateResponse(BaseModel):
    """Response from creating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[str | None, Any] = Field(default=None)
    ts: Union[str | None, Any] = Field(default=None)
    message: Union[CreatedMessage, Any] = Field(default=None)

class MessageUpdateParams(BaseModel):
    """Parameters for updating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: Union[str, Any] = Field(default=None)
    ts: Union[str, Any] = Field(default=None)
    text: Union[str, Any] = Field(default=None)

class MessageUpdateResponse(BaseModel):
    """Response from updating a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[str | None, Any] = Field(default=None)
    ts: Union[str | None, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    message: Union[CreatedMessage, Any] = Field(default=None)

class ChannelCreateParams(BaseModel):
    """Parameters for creating a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    is_private: Union[bool, Any] = Field(default=None)

class ChannelCreateResponse(BaseModel):
    """Response from creating a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[Channel, Any] = Field(default=None)

class ChannelRenameParams(BaseModel):
    """Parameters for renaming a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class ChannelRenameResponse(BaseModel):
    """Response from renaming a channel"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[Channel, Any] = Field(default=None)

class ChannelTopicParams(BaseModel):
    """Parameters for setting channel topic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: Union[str, Any] = Field(default=None)
    topic: Union[str, Any] = Field(default=None)

class ChannelTopicResponse(BaseModel):
    """Response from setting channel topic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[Channel, Any] = Field(default=None)

class ChannelPurposeParams(BaseModel):
    """Parameters for setting channel purpose"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: Union[str, Any] = Field(default=None)
    purpose: Union[str, Any] = Field(default=None)

class ChannelPurposeResponse(BaseModel):
    """Response from setting channel purpose"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)
    channel: Union[Channel, Any] = Field(default=None)

class ReactionAddParams(BaseModel):
    """Parameters for adding a reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel: Union[str, Any] = Field(default=None)
    timestamp: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class ReactionAddResponse(BaseModel):
    """Response from adding a reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ok: Union[bool, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)

class ChannelsListResultMeta(BaseModel):
    """Metadata for channels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)

class ChannelMessagesListResultMeta(BaseModel):
    """Metadata for channel_messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

class ThreadsListResultMeta(BaseModel):
    """Metadata for threads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

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
    meta: S
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

class AirbyteSearchHit(BaseModel, Generic[D]):
    """A single search result with typed data."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the record."""
    score: float | None = None
    """Relevance score for the match."""
    data: D
    """The matched record data."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed hits."""
    model_config = ConfigDict(extra="allow")

    hits: list[AirbyteSearchHit[D]] = Field(default_factory=list)
    """List of matching records."""
    next_cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

ChannelsSearchResult = AirbyteSearchResult[ChannelsSearchData]
"""Search result type for channels entity."""

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

