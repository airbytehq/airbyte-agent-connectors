"""
Type definitions for ashby connector.
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

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CandidatesListParams(TypedDict):
    """Parameters for candidates.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class CandidatesGetParams(TypedDict):
    """Parameters for candidates.get operation"""
    id: str

class ApplicationsListParams(TypedDict):
    """Parameters for applications.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ApplicationsGetParams(TypedDict):
    """Parameters for applications.get operation"""
    application_id: str

class JobsListParams(TypedDict):
    """Parameters for jobs.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class JobsGetParams(TypedDict):
    """Parameters for jobs.get operation"""
    id: str

class DepartmentsListParams(TypedDict):
    """Parameters for departments.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class DepartmentsGetParams(TypedDict):
    """Parameters for departments.get operation"""
    department_id: str

class LocationsListParams(TypedDict):
    """Parameters for locations.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class LocationsGetParams(TypedDict):
    """Parameters for locations.get operation"""
    location_id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_id: str

class JobPostingsListParams(TypedDict):
    """Parameters for job_postings.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class JobPostingsGetParams(TypedDict):
    """Parameters for job_postings.get operation"""
    job_posting_id: str

class SourcesListParams(TypedDict):
    """Parameters for sources.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ArchiveReasonsListParams(TypedDict):
    """Parameters for archive_reasons.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class CandidateTagsListParams(TypedDict):
    """Parameters for candidate_tags.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class CustomFieldsListParams(TypedDict):
    """Parameters for custom_fields.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

class FeedbackFormDefinitionsListParams(TypedDict):
    """Parameters for feedback_form_definitions.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]

