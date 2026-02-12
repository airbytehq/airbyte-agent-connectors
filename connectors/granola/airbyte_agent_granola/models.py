"""
Pydantic models for granola connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)

class Attendee(BaseModel):
    """A meeting attendee"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)

class CalendarEventInvitee(BaseModel):
    """A calendar event invitee"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str | None, Any] = Field(default=None)

class CalendarEvent(BaseModel):
    """Associated calendar event details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    event_title: Union[str | None, Any] = Field(default=None)
    invitees: Union[list[CalendarEventInvitee] | None, Any] = Field(default=None)
    organiser: Union[str | None, Any] = Field(default=None)
    calendar_event_id: Union[str | None, Any] = Field(default=None)
    scheduled_start_time: Union[str | None, Any] = Field(default=None)
    scheduled_end_time: Union[str | None, Any] = Field(default=None)

class FolderMembership(BaseModel):
    """Folder the note belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class TranscriptSpeaker(BaseModel):
    """Speaker information in transcript"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    source: Union[str | None, Any] = Field(default=None)

class TranscriptEntry(BaseModel):
    """A single transcript entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    speaker: Union[Any, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    end_time: Union[str | None, Any] = Field(default=None)

class Note(BaseModel):
    """A Granola meeting note"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    owner: Union[Any, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    calendar_event: Union[Any, Any] = Field(default=None)
    attendees: Union[list[Attendee] | None, Any] = Field(default=None)
    folder_membership: Union[list[FolderMembership] | None, Any] = Field(default=None)
    summary_text: Union[str | None, Any] = Field(default=None)
    summary_markdown: Union[str | None, Any] = Field(default=None)
    transcript: Union[list[TranscriptEntry] | None, Any] = Field(default=None)

class NotesList(BaseModel):
    """Paginated list of notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    notes: Union[list[Note], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None, alias="hasMore")
    cursor: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class NotesListResultMeta(BaseModel):
    """Metadata for notes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

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

    created_at: str | None = None
    """The creation time of the note in ISO 8601 format."""
    id: str | None = None
    """The unique identifier of the note."""
    object: str | None = None
    """The object type, always "note"."""
    owner: dict[str, Any] | None = None
    """The owner of the note."""
    title: str | None = None
    """The title of the note."""


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

