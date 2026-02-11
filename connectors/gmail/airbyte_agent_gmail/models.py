"""
Pydantic models for gmail connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class GmailAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """Your Google OAuth2 Access Token (optional, will be obtained via refresh)"""
    refresh_token: str
    """Your Google OAuth2 Refresh Token"""
    client_id: Optional[str] = None
    """Your Google OAuth2 Client ID"""
    client_secret: Optional[str] = None
    """Your Google OAuth2 Client Secret"""

# Replication configuration

class GmailReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Gmail."""

    model_config = ConfigDict(extra="forbid")

    include_spam_and_trash: Optional[bool] = None
    """Include messages from SPAM and TRASH in the results. Defaults to false."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Profile(BaseModel):
    """Gmail user profile information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email_address: Union[str | None, Any] = Field(default=None, alias="emailAddress")
    messages_total: Union[int | None, Any] = Field(default=None, alias="messagesTotal")
    threads_total: Union[int | None, Any] = Field(default=None, alias="threadsTotal")
    history_id: Union[str | None, Any] = Field(default=None, alias="historyId")

class MessageHeader(BaseModel):
    """A single email header key-value pair"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)

class MessagePartBody(BaseModel):
    """The body data of a MIME message part"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    attachment_id: Union[str | None, Any] = Field(default=None, alias="attachmentId")
    size: Union[int | None, Any] = Field(default=None)
    data: Union[str | None, Any] = Field(default=None)

class MessagePart(BaseModel):
    """A single MIME message part"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    part_id: Union[str | None, Any] = Field(default=None, alias="partId")
    mime_type: Union[str | None, Any] = Field(default=None, alias="mimeType")
    filename: Union[str | None, Any] = Field(default=None)
    headers: Union[list[MessageHeader] | None, Any] = Field(default=None)
    body: Union[Any, Any] = Field(default=None)
    parts: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class Message(BaseModel):
    """A Gmail email message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    thread_id: Union[str | None, Any] = Field(default=None, alias="threadId")
    label_ids: Union[list[str] | None, Any] = Field(default=None, alias="labelIds")
    snippet: Union[str | None, Any] = Field(default=None)
    history_id: Union[str | None, Any] = Field(default=None, alias="historyId")
    internal_date: Union[str | None, Any] = Field(default=None, alias="internalDate")
    size_estimate: Union[int | None, Any] = Field(default=None, alias="sizeEstimate")
    raw: Union[str | None, Any] = Field(default=None)
    payload: Union[Any, Any] = Field(default=None)

class MessageRef(BaseModel):
    """A lightweight reference to a message (used in list responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    thread_id: Union[str | None, Any] = Field(default=None, alias="threadId")

class MessagesListResponse(BaseModel):
    """Response from listing messages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    messages: Union[list[MessageRef], Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    result_size_estimate: Union[int | None, Any] = Field(default=None, alias="resultSizeEstimate")

class LabelColor(BaseModel):
    """The color to assign to a label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text_color: Union[str | None, Any] = Field(default=None, alias="textColor")
    background_color: Union[str | None, Any] = Field(default=None, alias="backgroundColor")

class Label(BaseModel):
    """A Gmail label used to organize messages and threads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    message_list_visibility: Union[str | None, Any] = Field(default=None, alias="messageListVisibility")
    label_list_visibility: Union[str | None, Any] = Field(default=None, alias="labelListVisibility")
    messages_total: Union[int | None, Any] = Field(default=None, alias="messagesTotal")
    messages_unread: Union[int | None, Any] = Field(default=None, alias="messagesUnread")
    threads_total: Union[int | None, Any] = Field(default=None, alias="threadsTotal")
    threads_unread: Union[int | None, Any] = Field(default=None, alias="threadsUnread")
    color: Union[Any, Any] = Field(default=None)

class LabelsListResponse(BaseModel):
    """Response from listing labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    labels: Union[list[Label], Any] = Field(default=None)

class DraftRef(BaseModel):
    """A lightweight reference to a draft (used in list responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    message: Union[Any, Any] = Field(default=None)

class Draft(BaseModel):
    """A Gmail draft message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    message: Union[Any, Any] = Field(default=None)

class DraftsListResponse(BaseModel):
    """Response from listing drafts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    drafts: Union[list[DraftRef], Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    result_size_estimate: Union[int | None, Any] = Field(default=None, alias="resultSizeEstimate")

class ThreadRef(BaseModel):
    """A lightweight reference to a thread (used in list responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    snippet: Union[str | None, Any] = Field(default=None)
    history_id: Union[str | None, Any] = Field(default=None, alias="historyId")

class Thread(BaseModel):
    """A Gmail thread (email conversation)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    snippet: Union[str | None, Any] = Field(default=None)
    history_id: Union[str | None, Any] = Field(default=None, alias="historyId")
    messages: Union[list[Message] | None, Any] = Field(default=None)

class ThreadsListResponse(BaseModel):
    """Response from listing threads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    threads: Union[list[ThreadRef], Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    result_size_estimate: Union[int | None, Any] = Field(default=None, alias="resultSizeEstimate")

class MessageSendParams(BaseModel):
    """Parameters for sending a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    raw: Union[str, Any] = Field(default=None)
    thread_id: Union[str, Any] = Field(default=None, alias="threadId")

class MessageModifyParams(BaseModel):
    """Parameters for modifying message labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    add_label_ids: Union[list[str], Any] = Field(default=None, alias="addLabelIds")
    remove_label_ids: Union[list[str], Any] = Field(default=None, alias="removeLabelIds")

class LabelCreateParamsColor(BaseModel):
    """The color to assign to the label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text_color: Union[str, Any] = Field(default=None, alias="textColor", description="The text color of the label as a hex string (#RRGGBB)")
    """The text color of the label as a hex string (#RRGGBB)"""
    background_color: Union[str, Any] = Field(default=None, alias="backgroundColor", description="The background color of the label as a hex string (#RRGGBB)")
    """The background color of the label as a hex string (#RRGGBB)"""

class LabelCreateParams(BaseModel):
    """Parameters for creating a label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    message_list_visibility: Union[str, Any] = Field(default=None, alias="messageListVisibility")
    label_list_visibility: Union[str, Any] = Field(default=None, alias="labelListVisibility")
    color: Union[LabelCreateParamsColor, Any] = Field(default=None)

class LabelUpdateParamsColor(BaseModel):
    """The color to assign to the label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text_color: Union[str, Any] = Field(default=None, alias="textColor", description="The text color of the label as a hex string (#RRGGBB)")
    """The text color of the label as a hex string (#RRGGBB)"""
    background_color: Union[str, Any] = Field(default=None, alias="backgroundColor", description="The background color of the label as a hex string (#RRGGBB)")
    """The background color of the label as a hex string (#RRGGBB)"""

class LabelUpdateParams(BaseModel):
    """Parameters for updating a label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    message_list_visibility: Union[str, Any] = Field(default=None, alias="messageListVisibility")
    label_list_visibility: Union[str, Any] = Field(default=None, alias="labelListVisibility")
    color: Union[LabelUpdateParamsColor, Any] = Field(default=None)

class DraftCreateParamsMessage(BaseModel):
    """The draft message content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    raw: Union[str, Any] = Field(default=None, description="The draft message in RFC 2822 format, base64url encoded")
    """The draft message in RFC 2822 format, base64url encoded"""
    thread_id: Union[str, Any] = Field(default=None, alias="threadId", description="The thread ID for the draft (for threading in a conversation)")
    """The thread ID for the draft (for threading in a conversation)"""

class DraftCreateParams(BaseModel):
    """Parameters for creating or updating a draft"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: Union[DraftCreateParamsMessage, Any] = Field(default=None)

class DraftSendParams(BaseModel):
    """Parameters for sending an existing draft"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    result_size_estimate: Union[int | None, Any] = Field(default=None, alias="resultSizeEstimate")

class DraftsListResultMeta(BaseModel):
    """Metadata for drafts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    result_size_estimate: Union[int | None, Any] = Field(default=None, alias="resultSizeEstimate")

class ThreadsListResultMeta(BaseModel):
    """Metadata for threads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    result_size_estimate: Union[int | None, Any] = Field(default=None, alias="resultSizeEstimate")

# ===== CHECK RESULT MODEL =====

class GmailCheckResult(BaseModel):
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


class GmailExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GmailExecuteResultWithMeta(GmailExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

MessagesListResult = GmailExecuteResultWithMeta[list[MessageRef], MessagesListResultMeta]
"""Result type for messages.list operation with data and metadata."""

LabelsListResult = GmailExecuteResult[list[Label]]
"""Result type for labels.list operation."""

DraftsListResult = GmailExecuteResultWithMeta[list[DraftRef], DraftsListResultMeta]
"""Result type for drafts.list operation with data and metadata."""

ThreadsListResult = GmailExecuteResultWithMeta[list[ThreadRef], ThreadsListResultMeta]
"""Result type for threads.list operation with data and metadata."""

