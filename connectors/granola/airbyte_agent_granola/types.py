"""
Type definitions for granola connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class NotesListParams(TypedDict):
    """Parameters for notes.list operation"""
    page_size: NotRequired[int]
    cursor: NotRequired[str]
    created_before: NotRequired[str]
    created_after: NotRequired[str]

class NotesGetParams(TypedDict):
    """Parameters for notes.get operation"""
    note_id: str
    include: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== NOTES SEARCH TYPES =====

class NotesSearchFilter(TypedDict, total=False):
    """Available fields for filtering notes search queries."""
    created_at: str | None
    """The creation time of the note in ISO 8601 format."""
    id: str | None
    """The unique identifier of the note."""
    object: str | None
    """The object type, always "note"."""
    owner: dict[str, Any] | None
    """The owner of the note."""
    title: str | None
    """The title of the note."""


class NotesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """The creation time of the note in ISO 8601 format."""
    id: list[str]
    """The unique identifier of the note."""
    object: list[str]
    """The object type, always "note"."""
    owner: list[dict[str, Any]]
    """The owner of the note."""
    title: list[str]
    """The title of the note."""


class NotesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """The creation time of the note in ISO 8601 format."""
    id: Any
    """The unique identifier of the note."""
    object: Any
    """The object type, always "note"."""
    owner: Any
    """The owner of the note."""
    title: Any
    """The title of the note."""


class NotesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """The creation time of the note in ISO 8601 format."""
    id: str
    """The unique identifier of the note."""
    object: str
    """The object type, always "note"."""
    owner: str
    """The owner of the note."""
    title: str
    """The title of the note."""


class NotesSortFilter(TypedDict, total=False):
    """Available fields for sorting notes search results."""
    created_at: AirbyteSortOrder
    """The creation time of the note in ISO 8601 format."""
    id: AirbyteSortOrder
    """The unique identifier of the note."""
    object: AirbyteSortOrder
    """The object type, always "note"."""
    owner: AirbyteSortOrder
    """The owner of the note."""
    title: AirbyteSortOrder
    """The title of the note."""


# Entity-specific condition types for notes
class NotesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: NotesSearchFilter


class NotesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: NotesSearchFilter


class NotesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: NotesSearchFilter


class NotesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: NotesSearchFilter


class NotesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: NotesSearchFilter


class NotesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: NotesSearchFilter


class NotesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: NotesStringFilter


class NotesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: NotesStringFilter


class NotesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: NotesStringFilter


class NotesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: NotesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
NotesInCondition = TypedDict("NotesInCondition", {"in": NotesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

NotesNotCondition = TypedDict("NotesNotCondition", {"not": "NotesCondition"}, total=False)
"""Negates the nested condition."""

NotesAndCondition = TypedDict("NotesAndCondition", {"and": "list[NotesCondition]"}, total=False)
"""True if all nested conditions are true."""

NotesOrCondition = TypedDict("NotesOrCondition", {"or": "list[NotesCondition]"}, total=False)
"""True if any nested condition is true."""

NotesAnyCondition = TypedDict("NotesAnyCondition", {"any": NotesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all notes condition types
NotesCondition = (
    NotesEqCondition
    | NotesNeqCondition
    | NotesGtCondition
    | NotesGteCondition
    | NotesLtCondition
    | NotesLteCondition
    | NotesInCondition
    | NotesLikeCondition
    | NotesFuzzyCondition
    | NotesKeywordCondition
    | NotesContainsCondition
    | NotesNotCondition
    | NotesAndCondition
    | NotesOrCondition
    | NotesAnyCondition
)


class NotesSearchQuery(TypedDict, total=False):
    """Search query for notes entity."""
    filter: NotesCondition
    sort: list[NotesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
