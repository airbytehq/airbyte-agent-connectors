"""
Type definitions for intercom connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    per_page: NotRequired[int]
    starting_after: NotRequired[str]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class ConversationsListParams(TypedDict):
    """Parameters for conversations.list operation"""
    per_page: NotRequired[int]
    starting_after: NotRequired[str]

class ConversationsGetParams(TypedDict):
    """Parameters for conversations.get operation"""
    id: str

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    per_page: NotRequired[int]
    starting_after: NotRequired[str]

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    id: str

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    pass

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    id: str

class AdminsListParams(TypedDict):
    """Parameters for admins.list operation"""
    pass

class AdminsGetParams(TypedDict):
    """Parameters for admins.get operation"""
    id: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    pass

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    include_count: NotRequired[bool]

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    id: str
