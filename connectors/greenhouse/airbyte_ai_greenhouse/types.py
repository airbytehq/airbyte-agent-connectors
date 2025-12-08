"""
Type definitions for greenhouse connector.
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

class CandidatesListParams(TypedDict):
    """Parameters for candidates.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class CandidatesGetParams(TypedDict):
    """Parameters for candidates.get operation"""
    id: str

class ApplicationsListParams(TypedDict):
    """Parameters for applications.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    last_activity_after: NotRequired[str]
    job_id: NotRequired[int]
    status: NotRequired[str]

class ApplicationsGetParams(TypedDict):
    """Parameters for applications.get operation"""
    id: str

class JobsListParams(TypedDict):
    """Parameters for jobs.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class JobsGetParams(TypedDict):
    """Parameters for jobs.get operation"""
    id: str
