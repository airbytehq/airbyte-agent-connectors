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

    access_token: str
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

class Reaction(BaseModel):
    """Message reaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None)
    users: Union[list[str] | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

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

