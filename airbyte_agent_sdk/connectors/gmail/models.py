"""
Pydantic models for gmail connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
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

    email_address: str | None = Field(default=None, alias="emailAddress")
    messages_total: int | None = Field(default=None, alias="messagesTotal")
    threads_total: int | None = Field(default=None, alias="threadsTotal")
    history_id: str | None = Field(default=None, alias="historyId")

class MessageHeader(BaseModel):
    """A single email header key-value pair"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    value: str | None = Field(default=None)

class MessagePartBody(BaseModel):
    """The body data of a MIME message part"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    attachment_id: str | None = Field(default=None, alias="attachmentId")
    size: int | None = Field(default=None)
    data: str | None = Field(default=None)

class MessagePart(BaseModel):
    """A single MIME message part"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    part_id: str | None = Field(default=None, alias="partId")
    mime_type: str | None = Field(default=None, alias="mimeType")
    filename: str | None = Field(default=None)
    headers: list[MessageHeader] | None = Field(default=None)
    body: Any | None = Field(default=None)
    parts: list[dict[str, Any]] | None = Field(default=None)

class Message(BaseModel):
    """A Gmail email message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    thread_id: str | None = Field(default=None, alias="threadId")
    label_ids: list[str] | None = Field(default=None, alias="labelIds")
    snippet: str | None = Field(default=None)
    history_id: str | None = Field(default=None, alias="historyId")
    internal_date: str | None = Field(default=None, alias="internalDate")
    size_estimate: int | None = Field(default=None, alias="sizeEstimate")
    raw: str | None = Field(default=None)
    payload: Any | None = Field(default=None)

class MessageRef(BaseModel):
    """A lightweight reference to a message (used in list responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    thread_id: str | None = Field(default=None, alias="threadId")

class MessagesListResponse(BaseModel):
    """Response from listing messages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    messages: list[MessageRef] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    result_size_estimate: int | None = Field(default=None, alias="resultSizeEstimate")

class LabelColor(BaseModel):
    """The color to assign to a label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text_color: str | None = Field(default=None, alias="textColor")
    background_color: str | None = Field(default=None, alias="backgroundColor")

class Label(BaseModel):
    """A Gmail label used to organize messages and threads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    message_list_visibility: str | None = Field(default=None, alias="messageListVisibility")
    label_list_visibility: str | None = Field(default=None, alias="labelListVisibility")
    messages_total: int | None = Field(default=None, alias="messagesTotal")
    messages_unread: int | None = Field(default=None, alias="messagesUnread")
    threads_total: int | None = Field(default=None, alias="threadsTotal")
    threads_unread: int | None = Field(default=None, alias="threadsUnread")
    color: Any | None = Field(default=None)

class LabelsListResponse(BaseModel):
    """Response from listing labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    labels: list[Label] | None = Field(default=None)

class DraftRef(BaseModel):
    """A lightweight reference to a draft (used in list responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    message: Any | None = Field(default=None)

class Draft(BaseModel):
    """A Gmail draft message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    message: Any | None = Field(default=None)

class DraftsListResponse(BaseModel):
    """Response from listing drafts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    drafts: list[DraftRef] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    result_size_estimate: int | None = Field(default=None, alias="resultSizeEstimate")

class ThreadRef(BaseModel):
    """A lightweight reference to a thread (used in list responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    snippet: str | None = Field(default=None)
    history_id: str | None = Field(default=None, alias="historyId")

class Thread(BaseModel):
    """A Gmail thread (email conversation)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    snippet: str | None = Field(default=None)
    history_id: str | None = Field(default=None, alias="historyId")
    messages: list[Message] | None = Field(default=None)

class ThreadsListResponse(BaseModel):
    """Response from listing threads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    threads: list[ThreadRef] | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    result_size_estimate: int | None = Field(default=None, alias="resultSizeEstimate")

class MessageSendParams(BaseModel):
    """Parameters for sending a message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    raw: str
    thread_id: str | None = Field(default=None, alias="threadId")

class MessageModifyParams(BaseModel):
    """Parameters for modifying message labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    add_label_ids: list[str] | None = Field(default=None, alias="addLabelIds")
    remove_label_ids: list[str] | None = Field(default=None, alias="removeLabelIds")

class LabelCreateParamsColor(BaseModel):
    """The color to assign to the label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text_color: str | None = Field(default=None, alias="textColor", description="The text color of the label as a hex string (#RRGGBB)")
    """The text color of the label as a hex string (#RRGGBB)"""
    background_color: str | None = Field(default=None, alias="backgroundColor", description="The background color of the label as a hex string (#RRGGBB)")
    """The background color of the label as a hex string (#RRGGBB)"""

class LabelCreateParams(BaseModel):
    """Parameters for creating a label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    message_list_visibility: str | None = Field(default=None, alias="messageListVisibility")
    label_list_visibility: str | None = Field(default=None, alias="labelListVisibility")
    color: LabelCreateParamsColor | None = Field(default=None)

class LabelUpdateParamsColor(BaseModel):
    """The color to assign to the label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text_color: str | None = Field(default=None, alias="textColor", description="The text color of the label as a hex string (#RRGGBB)")
    """The text color of the label as a hex string (#RRGGBB)"""
    background_color: str | None = Field(default=None, alias="backgroundColor", description="The background color of the label as a hex string (#RRGGBB)")
    """The background color of the label as a hex string (#RRGGBB)"""

class LabelUpdateParams(BaseModel):
    """Parameters for updating a label"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    message_list_visibility: str | None = Field(default=None, alias="messageListVisibility")
    label_list_visibility: str | None = Field(default=None, alias="labelListVisibility")
    color: LabelUpdateParamsColor | None = Field(default=None)

class DraftCreateParamsMessage(BaseModel):
    """The draft message content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    raw: str = Field(description="The draft message in RFC 2822 format, base64url encoded")
    """The draft message in RFC 2822 format, base64url encoded"""
    thread_id: str | None = Field(default=None, alias="threadId", description="The thread ID for the draft (for threading in a conversation)")
    """The thread ID for the draft (for threading in a conversation)"""

class DraftCreateParams(BaseModel):
    """Parameters for creating or updating a draft"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: DraftCreateParamsMessage

class DraftSendParams(BaseModel):
    """Parameters for sending an existing draft"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    result_size_estimate: int | None = Field(default=None, alias="resultSizeEstimate")

class DraftsListResultMeta(BaseModel):
    """Metadata for drafts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    result_size_estimate: int | None = Field(default=None, alias="resultSizeEstimate")

class ThreadsListResultMeta(BaseModel):
    """Metadata for threads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    result_size_estimate: int | None = Field(default=None, alias="resultSizeEstimate")

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

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ProfileSearchData(BaseModel):
    """Search result data for profile entity."""
    model_config = ConfigDict(extra="allow")

    email_address: str | None = None
    """Email address of the authenticated Gmail account"""
    history_id: str | None = None
    """Mailbox history record identifier used for incremental sync"""
    messages_total: float | None = None
    """Total number of messages currently in the mailbox"""
    threads_total: float | None = None
    """Total number of threads currently in the mailbox"""


class MessagesSearchData(BaseModel):
    """Search result data for messages entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the message"""
    thread_id: str | None = None
    """Identifier of the thread this message belongs to"""


class LabelsSearchData(BaseModel):
    """Search result data for labels entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the label"""
    name: str | None = None
    """Display name of the label"""
    type_: str | None = None
    """Label type: `system` or `user`"""
    label_list_visibility: str | None = None
    """Visibility of the label in the label list"""
    message_list_visibility: str | None = None
    """Visibility of the label when viewing a message list"""


class DraftsSearchData(BaseModel):
    """Search result data for drafts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the draft"""
    message: dict[str, Any] | None = None
    """Draft message payload (headers, body, and metadata)"""


class ThreadsSearchData(BaseModel):
    """Search result data for threads entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the thread"""
    history_id: str | None = None
    """Mailbox history record identifier for the thread"""
    snippet: str | None = None
    """Short snippet of the thread's most recent message"""


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

ProfileSearchResult = AirbyteSearchResult[ProfileSearchData]
"""Search result type for profile entity."""

MessagesSearchResult = AirbyteSearchResult[MessagesSearchData]
"""Search result type for messages entity."""

LabelsSearchResult = AirbyteSearchResult[LabelsSearchData]
"""Search result type for labels entity."""

DraftsSearchResult = AirbyteSearchResult[DraftsSearchData]
"""Search result type for drafts entity."""

ThreadsSearchResult = AirbyteSearchResult[ThreadsSearchData]
"""Search result type for threads entity."""



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

