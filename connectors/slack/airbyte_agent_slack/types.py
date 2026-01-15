"""
Type definitions for slack connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



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
