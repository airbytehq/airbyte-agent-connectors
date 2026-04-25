"""
Pydantic models for granola connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class GranolaAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Granola Enterprise API key generated from Settings > Workspaces > API tab"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Owner(BaseModel):
    """The owner of the note"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    email: str | None = Field(default=None)

class Attendee(BaseModel):
    """A meeting attendee"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    email: str | None = Field(default=None)

class CalendarEventInvitee(BaseModel):
    """A calendar event invitee"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None)

class CalendarEvent(BaseModel):
    """Associated calendar event details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    event_title: str | None = Field(default=None)
    invitees: list[CalendarEventInvitee] | None = Field(default=None)
    organiser: str | None = Field(default=None)
    calendar_event_id: str | None = Field(default=None)
    scheduled_start_time: str | None = Field(default=None)
    scheduled_end_time: str | None = Field(default=None)

class FolderMembership(BaseModel):
    """Folder the note belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    object_: str | None = Field(default=None, alias="object")
    name: str | None = Field(default=None)

class TranscriptSpeaker(BaseModel):
    """Speaker information in transcript"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    source: str | None = Field(default=None)

class TranscriptEntry(BaseModel):
    """A single transcript entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    speaker: Any | None = Field(default=None)
    text: str | None = Field(default=None)
    start_time: str | None = Field(default=None)
    end_time: str | None = Field(default=None)

class Note(BaseModel):
    """A Granola meeting note"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    object_: str | None = Field(default=None, alias="object")
    title: str | None = Field(default=None)
    owner: Any | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    calendar_event: Any | None = Field(default=None)
    attendees: list[Attendee] | None = Field(default=None)
    folder_membership: list[FolderMembership] | None = Field(default=None)
    summary_text: str | None = Field(default=None)
    summary_markdown: str | None = Field(default=None)
    transcript: list[TranscriptEntry] | None = Field(default=None)

class NotesList(BaseModel):
    """Paginated list of notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    notes: list[Note] | None = Field(default=None)
    has_more: bool | None = Field(default=None, alias="hasMore")
    cursor: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class NotesListResultMeta(BaseModel):
    """Metadata for notes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class GranolaCheckResult(BaseModel):
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


class GranolaExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GranolaExecuteResultWithMeta(GranolaExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class NotesSearchData(BaseModel):
    """Search result data for notes entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """The unique identifier of the note."""
    object_: str | None = None
    """The object type, always "note"."""
    title: str | None = None
    """The title of the note."""
    owner: dict[str, Any] | None = None
    """The owner of the note."""
    created_at: str | None = None
    """The creation time of the note in ISO 8601 format."""
    updated_at: str | None = None
    """The last update time of the note in ISO 8601 format."""
    summary_text: str | None = None
    """Plain text summary of the note."""
    summary_markdown: str | None = None
    """Markdown formatted summary of the note."""
    attendees: list[Any] | None = None
    """The attendees of the meeting."""
    calendar_event: dict[str, Any] | None = None
    """Associated calendar event details."""
    folder_membership: list[Any] | None = None
    """The folder membership of the note."""
    transcript: list[Any] | None = None
    """Transcript of the meeting."""


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

NotesSearchResult = AirbyteSearchResult[NotesSearchData]
"""Search result type for notes entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

NotesListResult = GranolaExecuteResultWithMeta[list[Note], NotesListResultMeta]
"""Result type for notes.list operation with data and metadata."""

