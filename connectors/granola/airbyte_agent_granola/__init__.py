"""
Blessed Granola connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GranolaConnector
from .models import (
    GranolaAuthConfig,
    Owner,
    Attendee,
    CalendarEventInvitee,
    CalendarEvent,
    FolderMembership,
    TranscriptSpeaker,
    TranscriptEntry,
    Note,
    NotesList,
    NotesListResultMeta,
    GranolaCheckResult,
    GranolaExecuteResult,
    GranolaExecuteResultWithMeta,
    NotesListResult,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    NotesSearchData,
    NotesSearchResult
)
from .types import (
    NotesListParams,
    NotesGetParams,
    AirbyteSearchParams,
    AirbyteSortOrder,
    NotesSearchFilter,
    NotesSearchQuery,
    NotesCondition
)
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig

__all__ = [
    "GranolaConnector",
    "AirbyteAuthConfig",
    "GranolaAuthConfig",
    "Owner",
    "Attendee",
    "CalendarEventInvitee",
    "CalendarEvent",
    "FolderMembership",
    "TranscriptSpeaker",
    "TranscriptEntry",
    "Note",
    "NotesList",
    "NotesListResultMeta",
    "GranolaCheckResult",
    "GranolaExecuteResult",
    "GranolaExecuteResultWithMeta",
    "NotesListResult",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "NotesSearchData",
    "NotesSearchResult",
    "NotesListParams",
    "NotesGetParams",
    "AirbyteSearchParams",
    "AirbyteSortOrder",
    "NotesSearchFilter",
    "NotesSearchQuery",
    "NotesCondition",
]