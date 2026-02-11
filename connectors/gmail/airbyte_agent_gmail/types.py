"""
Type definitions for gmail connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class LabelsCreateParamsColor(TypedDict):
    """The color to assign to the label"""
    textColor: NotRequired[str]
    backgroundColor: NotRequired[str]

class LabelsUpdateParamsColor(TypedDict):
    """The color to assign to the label"""
    textColor: NotRequired[str]
    backgroundColor: NotRequired[str]

class DraftsCreateParamsMessage(TypedDict):
    """The draft message content"""
    raw: str
    threadId: NotRequired[str]

class DraftsUpdateParamsMessage(TypedDict):
    """The draft message content"""
    raw: str
    threadId: NotRequired[str]

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

