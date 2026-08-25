"""
Type definitions for ashby connector.
"""
# ruff: noqa: E501
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


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

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== APPLICATIONS SEARCH TYPES =====

class ApplicationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering applications search queries."""
    id: str | None
    """Unique identifier for the application"""
    status: str | None
    """Current application status (e.g. active, archived, hired)"""
    archive_reason: str | None
    """Reason the application was archived, if applicable"""
    created_at: str | None
    """Timestamp when the application was created, in ISO 8601 format"""
    updated_at: str | None
    """Timestamp when the application was last updated, in ISO 8601 format"""


class ApplicationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the application"""
    status: list[str]
    """Current application status (e.g. active, archived, hired)"""
    archive_reason: list[str]
    """Reason the application was archived, if applicable"""
    created_at: list[str]
    """Timestamp when the application was created, in ISO 8601 format"""
    updated_at: list[str]
    """Timestamp when the application was last updated, in ISO 8601 format"""


class ApplicationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the application"""
    status: Any
    """Current application status (e.g. active, archived, hired)"""
    archive_reason: Any
    """Reason the application was archived, if applicable"""
    created_at: Any
    """Timestamp when the application was created, in ISO 8601 format"""
    updated_at: Any
    """Timestamp when the application was last updated, in ISO 8601 format"""


class ApplicationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the application"""
    status: str
    """Current application status (e.g. active, archived, hired)"""
    archive_reason: str
    """Reason the application was archived, if applicable"""
    created_at: str
    """Timestamp when the application was created, in ISO 8601 format"""
    updated_at: str
    """Timestamp when the application was last updated, in ISO 8601 format"""


class ApplicationsSortFilter(TypedDict, total=False):
    """Available fields for sorting applications search results."""
    id: AirbyteSortOrder
    """Unique identifier for the application"""
    status: AirbyteSortOrder
    """Current application status (e.g. active, archived, hired)"""
    archive_reason: AirbyteSortOrder
    """Reason the application was archived, if applicable"""
    created_at: AirbyteSortOrder
    """Timestamp when the application was created, in ISO 8601 format"""
    updated_at: AirbyteSortOrder
    """Timestamp when the application was last updated, in ISO 8601 format"""


# Entity-specific condition types for applications
class ApplicationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ApplicationsSearchFilter


class ApplicationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ApplicationsSearchFilter


class ApplicationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ApplicationsSearchFilter


class ApplicationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ApplicationsSearchFilter


class ApplicationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ApplicationsSearchFilter


class ApplicationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ApplicationsSearchFilter


class ApplicationsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ApplicationsStringFilter


class ApplicationsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ApplicationsStringFilter


class ApplicationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ApplicationsStringFilter


class ApplicationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ApplicationsStringFilter


class ApplicationsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: ApplicationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ApplicationsInCondition = TypedDict("ApplicationsInCondition", {"in": ApplicationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ApplicationsNotCondition = TypedDict("ApplicationsNotCondition", {"not": "ApplicationsCondition"}, total=False)
"""Negates the nested condition."""

ApplicationsAndCondition = TypedDict("ApplicationsAndCondition", {"and": "list[ApplicationsCondition]"}, total=False)
"""True if all nested conditions are true."""

ApplicationsOrCondition = TypedDict("ApplicationsOrCondition", {"or": "list[ApplicationsCondition]"}, total=False)
"""True if any nested condition is true."""

ApplicationsAnyCondition = TypedDict("ApplicationsAnyCondition", {"any": ApplicationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all applications condition types
ApplicationsCondition = (
    ApplicationsEqCondition
    | ApplicationsNeqCondition
    | ApplicationsGtCondition
    | ApplicationsGteCondition
    | ApplicationsLtCondition
    | ApplicationsLteCondition
    | ApplicationsInCondition
    | ApplicationsStartswithCondition
    | ApplicationsEndswithCondition
    | ApplicationsFuzzyCondition
    | ApplicationsKeywordCondition
    | ApplicationsContainsCondition
    | ApplicationsNotCondition
    | ApplicationsAndCondition
    | ApplicationsOrCondition
    | ApplicationsAnyCondition
)


class ApplicationsSearchQuery(TypedDict, total=False):
    """Search query for applications entity."""
    filter: ApplicationsCondition
    sort: list[ApplicationsSortFilter]


# ===== CANDIDATES SEARCH TYPES =====

class CandidatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering candidates search queries."""
    id: str | None
    """Unique identifier for the candidate"""
    name: str | None
    """Full name of the candidate"""
    company: str | None
    """Candidate's current company"""
    position: str | None
    """Candidate's current position or title"""
    school: str | None
    """School associated with the candidate's education"""


class CandidatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the candidate"""
    name: list[str]
    """Full name of the candidate"""
    company: list[str]
    """Candidate's current company"""
    position: list[str]
    """Candidate's current position or title"""
    school: list[str]
    """School associated with the candidate's education"""


class CandidatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the candidate"""
    name: Any
    """Full name of the candidate"""
    company: Any
    """Candidate's current company"""
    position: Any
    """Candidate's current position or title"""
    school: Any
    """School associated with the candidate's education"""


class CandidatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the candidate"""
    name: str
    """Full name of the candidate"""
    company: str
    """Candidate's current company"""
    position: str
    """Candidate's current position or title"""
    school: str
    """School associated with the candidate's education"""


class CandidatesSortFilter(TypedDict, total=False):
    """Available fields for sorting candidates search results."""
    id: AirbyteSortOrder
    """Unique identifier for the candidate"""
    name: AirbyteSortOrder
    """Full name of the candidate"""
    company: AirbyteSortOrder
    """Candidate's current company"""
    position: AirbyteSortOrder
    """Candidate's current position or title"""
    school: AirbyteSortOrder
    """School associated with the candidate's education"""


# Entity-specific condition types for candidates
class CandidatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CandidatesSearchFilter


class CandidatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CandidatesSearchFilter


class CandidatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CandidatesSearchFilter


class CandidatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CandidatesSearchFilter


class CandidatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CandidatesSearchFilter


class CandidatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CandidatesSearchFilter


class CandidatesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CandidatesStringFilter


class CandidatesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CandidatesStringFilter


class CandidatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CandidatesStringFilter


class CandidatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CandidatesStringFilter


class CandidatesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: CandidatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CandidatesInCondition = TypedDict("CandidatesInCondition", {"in": CandidatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CandidatesNotCondition = TypedDict("CandidatesNotCondition", {"not": "CandidatesCondition"}, total=False)
"""Negates the nested condition."""

CandidatesAndCondition = TypedDict("CandidatesAndCondition", {"and": "list[CandidatesCondition]"}, total=False)
"""True if all nested conditions are true."""

CandidatesOrCondition = TypedDict("CandidatesOrCondition", {"or": "list[CandidatesCondition]"}, total=False)
"""True if any nested condition is true."""

CandidatesAnyCondition = TypedDict("CandidatesAnyCondition", {"any": CandidatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all candidates condition types
CandidatesCondition = (
    CandidatesEqCondition
    | CandidatesNeqCondition
    | CandidatesGtCondition
    | CandidatesGteCondition
    | CandidatesLtCondition
    | CandidatesLteCondition
    | CandidatesInCondition
    | CandidatesStartswithCondition
    | CandidatesEndswithCondition
    | CandidatesFuzzyCondition
    | CandidatesKeywordCondition
    | CandidatesContainsCondition
    | CandidatesNotCondition
    | CandidatesAndCondition
    | CandidatesOrCondition
    | CandidatesAnyCondition
)


class CandidatesSearchQuery(TypedDict, total=False):
    """Search query for candidates entity."""
    filter: CandidatesCondition
    sort: list[CandidatesSortFilter]


# ===== JOB_POSTINGS SEARCH TYPES =====

class JobPostingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering job_postings search queries."""
    id: str | None
    """Unique identifier for the job posting"""
    title: str | None
    """Title of the job posting"""
    is_listed: bool | None
    """Whether the job posting is currently published/listed"""
    job_id: str | None
    """Identifier of the job this posting belongs to"""
    location_name: str | None
    """Name of the location associated with the posting"""


class JobPostingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the job posting"""
    title: list[str]
    """Title of the job posting"""
    is_listed: list[bool]
    """Whether the job posting is currently published/listed"""
    job_id: list[str]
    """Identifier of the job this posting belongs to"""
    location_name: list[str]
    """Name of the location associated with the posting"""


class JobPostingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the job posting"""
    title: Any
    """Title of the job posting"""
    is_listed: Any
    """Whether the job posting is currently published/listed"""
    job_id: Any
    """Identifier of the job this posting belongs to"""
    location_name: Any
    """Name of the location associated with the posting"""


class JobPostingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the job posting"""
    title: str
    """Title of the job posting"""
    is_listed: str
    """Whether the job posting is currently published/listed"""
    job_id: str
    """Identifier of the job this posting belongs to"""
    location_name: str
    """Name of the location associated with the posting"""


class JobPostingsSortFilter(TypedDict, total=False):
    """Available fields for sorting job_postings search results."""
    id: AirbyteSortOrder
    """Unique identifier for the job posting"""
    title: AirbyteSortOrder
    """Title of the job posting"""
    is_listed: AirbyteSortOrder
    """Whether the job posting is currently published/listed"""
    job_id: AirbyteSortOrder
    """Identifier of the job this posting belongs to"""
    location_name: AirbyteSortOrder
    """Name of the location associated with the posting"""


# Entity-specific condition types for job_postings
class JobPostingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: JobPostingsSearchFilter


class JobPostingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: JobPostingsSearchFilter


class JobPostingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: JobPostingsSearchFilter


class JobPostingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: JobPostingsSearchFilter


class JobPostingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: JobPostingsSearchFilter


class JobPostingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: JobPostingsSearchFilter


class JobPostingsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: JobPostingsStringFilter


class JobPostingsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: JobPostingsStringFilter


class JobPostingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: JobPostingsStringFilter


class JobPostingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: JobPostingsStringFilter


class JobPostingsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: JobPostingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
JobPostingsInCondition = TypedDict("JobPostingsInCondition", {"in": JobPostingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

JobPostingsNotCondition = TypedDict("JobPostingsNotCondition", {"not": "JobPostingsCondition"}, total=False)
"""Negates the nested condition."""

JobPostingsAndCondition = TypedDict("JobPostingsAndCondition", {"and": "list[JobPostingsCondition]"}, total=False)
"""True if all nested conditions are true."""

JobPostingsOrCondition = TypedDict("JobPostingsOrCondition", {"or": "list[JobPostingsCondition]"}, total=False)
"""True if any nested condition is true."""

JobPostingsAnyCondition = TypedDict("JobPostingsAnyCondition", {"any": JobPostingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all job_postings condition types
JobPostingsCondition = (
    JobPostingsEqCondition
    | JobPostingsNeqCondition
    | JobPostingsGtCondition
    | JobPostingsGteCondition
    | JobPostingsLtCondition
    | JobPostingsLteCondition
    | JobPostingsInCondition
    | JobPostingsStartswithCondition
    | JobPostingsEndswithCondition
    | JobPostingsFuzzyCondition
    | JobPostingsKeywordCondition
    | JobPostingsContainsCondition
    | JobPostingsNotCondition
    | JobPostingsAndCondition
    | JobPostingsOrCondition
    | JobPostingsAnyCondition
)


class JobPostingsSearchQuery(TypedDict, total=False):
    """Search query for job_postings entity."""
    filter: JobPostingsCondition
    sort: list[JobPostingsSortFilter]


# ===== JOBS SEARCH TYPES =====

class JobsSearchFilter(TypedDict, total=False):
    """Available fields for filtering jobs search queries."""
    id: str | None
    """Unique identifier for the job"""
    title: str | None
    """Title of the job"""
    status: str | None
    """Current status of the job (e.g. open, closed, draft)"""
    department_id: str | None
    """Identifier of the department the job belongs to"""
    location_id: str | None
    """Identifier of the primary location of the job"""


class JobsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the job"""
    title: list[str]
    """Title of the job"""
    status: list[str]
    """Current status of the job (e.g. open, closed, draft)"""
    department_id: list[str]
    """Identifier of the department the job belongs to"""
    location_id: list[str]
    """Identifier of the primary location of the job"""


class JobsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the job"""
    title: Any
    """Title of the job"""
    status: Any
    """Current status of the job (e.g. open, closed, draft)"""
    department_id: Any
    """Identifier of the department the job belongs to"""
    location_id: Any
    """Identifier of the primary location of the job"""


class JobsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the job"""
    title: str
    """Title of the job"""
    status: str
    """Current status of the job (e.g. open, closed, draft)"""
    department_id: str
    """Identifier of the department the job belongs to"""
    location_id: str
    """Identifier of the primary location of the job"""


class JobsSortFilter(TypedDict, total=False):
    """Available fields for sorting jobs search results."""
    id: AirbyteSortOrder
    """Unique identifier for the job"""
    title: AirbyteSortOrder
    """Title of the job"""
    status: AirbyteSortOrder
    """Current status of the job (e.g. open, closed, draft)"""
    department_id: AirbyteSortOrder
    """Identifier of the department the job belongs to"""
    location_id: AirbyteSortOrder
    """Identifier of the primary location of the job"""


# Entity-specific condition types for jobs
class JobsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: JobsSearchFilter


class JobsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: JobsSearchFilter


class JobsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: JobsSearchFilter


class JobsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: JobsSearchFilter


class JobsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: JobsSearchFilter


class JobsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: JobsSearchFilter


class JobsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: JobsStringFilter


class JobsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: JobsStringFilter


class JobsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: JobsStringFilter


class JobsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: JobsStringFilter


class JobsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: JobsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
JobsInCondition = TypedDict("JobsInCondition", {"in": JobsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

JobsNotCondition = TypedDict("JobsNotCondition", {"not": "JobsCondition"}, total=False)
"""Negates the nested condition."""

JobsAndCondition = TypedDict("JobsAndCondition", {"and": "list[JobsCondition]"}, total=False)
"""True if all nested conditions are true."""

JobsOrCondition = TypedDict("JobsOrCondition", {"or": "list[JobsCondition]"}, total=False)
"""True if any nested condition is true."""

JobsAnyCondition = TypedDict("JobsAnyCondition", {"any": JobsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all jobs condition types
JobsCondition = (
    JobsEqCondition
    | JobsNeqCondition
    | JobsGtCondition
    | JobsGteCondition
    | JobsLtCondition
    | JobsLteCondition
    | JobsInCondition
    | JobsStartswithCondition
    | JobsEndswithCondition
    | JobsFuzzyCondition
    | JobsKeywordCondition
    | JobsContainsCondition
    | JobsNotCondition
    | JobsAndCondition
    | JobsOrCondition
    | JobsAnyCondition
)


class JobsSearchQuery(TypedDict, total=False):
    """Search query for jobs entity."""
    filter: JobsCondition
    sort: list[JobsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    id: str | None
    """Unique identifier for the user"""
    first_name: str | None
    """First name of the user"""
    last_name: str | None
    """Last name of the user"""
    email: str | None
    """Primary email address of the user"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the user"""
    first_name: list[str]
    """First name of the user"""
    last_name: list[str]
    """Last name of the user"""
    email: list[str]
    """Primary email address of the user"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the user"""
    first_name: Any
    """First name of the user"""
    last_name: Any
    """Last name of the user"""
    email: Any
    """Primary email address of the user"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the user"""
    first_name: str
    """First name of the user"""
    last_name: str
    """Last name of the user"""
    email: str
    """Primary email address of the user"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    first_name: AirbyteSortOrder
    """First name of the user"""
    last_name: AirbyteSortOrder
    """Last name of the user"""
    email: AirbyteSortOrder
    """Primary email address of the user"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UsersStringFilter


class UsersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersStartswithCondition
    | UsersEndswithCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
