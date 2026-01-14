"""
Type definitions for salesforce connector.
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

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    q: str

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str
    fields: NotRequired[str]

class AccountsApiSearchParams(TypedDict):
    """Parameters for accounts.api_search operation"""
    q: str

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    q: str

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str
    fields: NotRequired[str]

class ContactsApiSearchParams(TypedDict):
    """Parameters for contacts.api_search operation"""
    q: str

class LeadsListParams(TypedDict):
    """Parameters for leads.list operation"""
    q: str

class LeadsGetParams(TypedDict):
    """Parameters for leads.get operation"""
    id: str
    fields: NotRequired[str]

class LeadsApiSearchParams(TypedDict):
    """Parameters for leads.api_search operation"""
    q: str

class OpportunitiesListParams(TypedDict):
    """Parameters for opportunities.list operation"""
    q: str

class OpportunitiesGetParams(TypedDict):
    """Parameters for opportunities.get operation"""
    id: str
    fields: NotRequired[str]

class OpportunitiesApiSearchParams(TypedDict):
    """Parameters for opportunities.api_search operation"""
    q: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    q: str

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    id: str
    fields: NotRequired[str]

class TasksApiSearchParams(TypedDict):
    """Parameters for tasks.api_search operation"""
    q: str

class EventsListParams(TypedDict):
    """Parameters for events.list operation"""
    q: str

class EventsGetParams(TypedDict):
    """Parameters for events.get operation"""
    id: str
    fields: NotRequired[str]

class EventsApiSearchParams(TypedDict):
    """Parameters for events.api_search operation"""
    q: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    q: str

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    id: str
    fields: NotRequired[str]

class CampaignsApiSearchParams(TypedDict):
    """Parameters for campaigns.api_search operation"""
    q: str

class CasesListParams(TypedDict):
    """Parameters for cases.list operation"""
    q: str

class CasesGetParams(TypedDict):
    """Parameters for cases.get operation"""
    id: str
    fields: NotRequired[str]

class CasesApiSearchParams(TypedDict):
    """Parameters for cases.api_search operation"""
    q: str

class NotesListParams(TypedDict):
    """Parameters for notes.list operation"""
    q: str

class NotesGetParams(TypedDict):
    """Parameters for notes.get operation"""
    id: str
    fields: NotRequired[str]

class NotesApiSearchParams(TypedDict):
    """Parameters for notes.api_search operation"""
    q: str

class ContentVersionsListParams(TypedDict):
    """Parameters for content_versions.list operation"""
    q: str

class ContentVersionsGetParams(TypedDict):
    """Parameters for content_versions.get operation"""
    id: str
    fields: NotRequired[str]

class ContentVersionsDownloadParams(TypedDict):
    """Parameters for content_versions.download operation"""
    id: str
    range_header: NotRequired[str]

class AttachmentsListParams(TypedDict):
    """Parameters for attachments.list operation"""
    q: str

class AttachmentsGetParams(TypedDict):
    """Parameters for attachments.get operation"""
    id: str
    fields: NotRequired[str]

class AttachmentsDownloadParams(TypedDict):
    """Parameters for attachments.download operation"""
    id: str
    range_header: NotRequired[str]

class QueryListParams(TypedDict):
    """Parameters for query.list operation"""
    q: str
