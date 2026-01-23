"""
Type definitions for greenhouse connector.
"""
from __future__ import annotations

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

class OffersListParams(TypedDict):
    """Parameters for offers.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    resolved_after: NotRequired[str]

class OffersGetParams(TypedDict):
    """Parameters for offers.get operation"""
    id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    updated_before: NotRequired[str]
    updated_after: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class DepartmentsListParams(TypedDict):
    """Parameters for departments.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class DepartmentsGetParams(TypedDict):
    """Parameters for departments.get operation"""
    id: str

class OfficesListParams(TypedDict):
    """Parameters for offices.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class OfficesGetParams(TypedDict):
    """Parameters for offices.get operation"""
    id: str

class JobPostsListParams(TypedDict):
    """Parameters for job_posts.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    live: NotRequired[bool]
    active: NotRequired[bool]

class JobPostsGetParams(TypedDict):
    """Parameters for job_posts.get operation"""
    id: str

class SourcesListParams(TypedDict):
    """Parameters for sources.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class ScheduledInterviewsListParams(TypedDict):
    """Parameters for scheduled_interviews.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    updated_before: NotRequired[str]
    updated_after: NotRequired[str]
    starts_after: NotRequired[str]
    ends_before: NotRequired[str]

class ScheduledInterviewsGetParams(TypedDict):
    """Parameters for scheduled_interviews.get operation"""
    id: str

class ApplicationAttachmentDownloadParams(TypedDict):
    """Parameters for application_attachment.download operation"""
    id: str
    attachment_index: str
    range_header: NotRequired[str]

class CandidateAttachmentDownloadParams(TypedDict):
    """Parameters for candidate_attachment.download operation"""
    id: str
    attachment_index: str
    range_header: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== APPLICATIONS SEARCH TYPES =====

class ApplicationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering applications search queries."""
    answers: list[Any] | None
    """Answers provided in the application."""
    applied_at: str | None
    """Timestamp when the candidate applied."""
    attachments: list[Any] | None
    """Attachments uploaded with the application."""
    candidate_id: int | None
    """Unique identifier for the candidate."""
    credited_to: dict[str, Any] | None
    """Information about the employee who credited the application."""
    current_stage: dict[str, Any] | None
    """Current stage of the application process."""
    id: int | None
    """Unique identifier for the application."""
    job_post_id: int | None
    """"""
    jobs: list[Any] | None
    """Jobs applied for by the candidate."""
    last_activity_at: str | None
    """Timestamp of the last activity on the application."""
    location: str | None
    """Location related to the application."""
    prospect: bool | None
    """Status of the application prospect."""
    prospect_detail: dict[str, Any] | None
    """Details related to the application prospect."""
    prospective_department: str | None
    """Prospective department for the candidate."""
    prospective_office: str | None
    """Prospective office for the candidate."""
    rejected_at: str | None
    """Timestamp when the application was rejected."""
    rejection_details: dict[str, Any] | None
    """Details related to the application rejection."""
    rejection_reason: dict[str, Any] | None
    """Reason for the application rejection."""
    source: dict[str, Any] | None
    """Source of the application."""
    status: str | None
    """Status of the application."""


class ApplicationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    answers: list[list[Any]]
    """Answers provided in the application."""
    applied_at: list[str]
    """Timestamp when the candidate applied."""
    attachments: list[list[Any]]
    """Attachments uploaded with the application."""
    candidate_id: list[int]
    """Unique identifier for the candidate."""
    credited_to: list[dict[str, Any]]
    """Information about the employee who credited the application."""
    current_stage: list[dict[str, Any]]
    """Current stage of the application process."""
    id: list[int]
    """Unique identifier for the application."""
    job_post_id: list[int]
    """"""
    jobs: list[list[Any]]
    """Jobs applied for by the candidate."""
    last_activity_at: list[str]
    """Timestamp of the last activity on the application."""
    location: list[str]
    """Location related to the application."""
    prospect: list[bool]
    """Status of the application prospect."""
    prospect_detail: list[dict[str, Any]]
    """Details related to the application prospect."""
    prospective_department: list[str]
    """Prospective department for the candidate."""
    prospective_office: list[str]
    """Prospective office for the candidate."""
    rejected_at: list[str]
    """Timestamp when the application was rejected."""
    rejection_details: list[dict[str, Any]]
    """Details related to the application rejection."""
    rejection_reason: list[dict[str, Any]]
    """Reason for the application rejection."""
    source: list[dict[str, Any]]
    """Source of the application."""
    status: list[str]
    """Status of the application."""


class ApplicationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    answers: Any
    """Answers provided in the application."""
    applied_at: Any
    """Timestamp when the candidate applied."""
    attachments: Any
    """Attachments uploaded with the application."""
    candidate_id: Any
    """Unique identifier for the candidate."""
    credited_to: Any
    """Information about the employee who credited the application."""
    current_stage: Any
    """Current stage of the application process."""
    id: Any
    """Unique identifier for the application."""
    job_post_id: Any
    """"""
    jobs: Any
    """Jobs applied for by the candidate."""
    last_activity_at: Any
    """Timestamp of the last activity on the application."""
    location: Any
    """Location related to the application."""
    prospect: Any
    """Status of the application prospect."""
    prospect_detail: Any
    """Details related to the application prospect."""
    prospective_department: Any
    """Prospective department for the candidate."""
    prospective_office: Any
    """Prospective office for the candidate."""
    rejected_at: Any
    """Timestamp when the application was rejected."""
    rejection_details: Any
    """Details related to the application rejection."""
    rejection_reason: Any
    """Reason for the application rejection."""
    source: Any
    """Source of the application."""
    status: Any
    """Status of the application."""


class ApplicationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    answers: str
    """Answers provided in the application."""
    applied_at: str
    """Timestamp when the candidate applied."""
    attachments: str
    """Attachments uploaded with the application."""
    candidate_id: str
    """Unique identifier for the candidate."""
    credited_to: str
    """Information about the employee who credited the application."""
    current_stage: str
    """Current stage of the application process."""
    id: str
    """Unique identifier for the application."""
    job_post_id: str
    """"""
    jobs: str
    """Jobs applied for by the candidate."""
    last_activity_at: str
    """Timestamp of the last activity on the application."""
    location: str
    """Location related to the application."""
    prospect: str
    """Status of the application prospect."""
    prospect_detail: str
    """Details related to the application prospect."""
    prospective_department: str
    """Prospective department for the candidate."""
    prospective_office: str
    """Prospective office for the candidate."""
    rejected_at: str
    """Timestamp when the application was rejected."""
    rejection_details: str
    """Details related to the application rejection."""
    rejection_reason: str
    """Reason for the application rejection."""
    source: str
    """Source of the application."""
    status: str
    """Status of the application."""


class ApplicationsSortFilter(TypedDict, total=False):
    """Available fields for sorting applications search results."""
    answers: AirbyteSortOrder
    """Answers provided in the application."""
    applied_at: AirbyteSortOrder
    """Timestamp when the candidate applied."""
    attachments: AirbyteSortOrder
    """Attachments uploaded with the application."""
    candidate_id: AirbyteSortOrder
    """Unique identifier for the candidate."""
    credited_to: AirbyteSortOrder
    """Information about the employee who credited the application."""
    current_stage: AirbyteSortOrder
    """Current stage of the application process."""
    id: AirbyteSortOrder
    """Unique identifier for the application."""
    job_post_id: AirbyteSortOrder
    """"""
    jobs: AirbyteSortOrder
    """Jobs applied for by the candidate."""
    last_activity_at: AirbyteSortOrder
    """Timestamp of the last activity on the application."""
    location: AirbyteSortOrder
    """Location related to the application."""
    prospect: AirbyteSortOrder
    """Status of the application prospect."""
    prospect_detail: AirbyteSortOrder
    """Details related to the application prospect."""
    prospective_department: AirbyteSortOrder
    """Prospective department for the candidate."""
    prospective_office: AirbyteSortOrder
    """Prospective office for the candidate."""
    rejected_at: AirbyteSortOrder
    """Timestamp when the application was rejected."""
    rejection_details: AirbyteSortOrder
    """Details related to the application rejection."""
    rejection_reason: AirbyteSortOrder
    """Reason for the application rejection."""
    source: AirbyteSortOrder
    """Source of the application."""
    status: AirbyteSortOrder
    """Status of the application."""


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


class ApplicationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ApplicationsStringFilter


class ApplicationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ApplicationsStringFilter


class ApplicationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ApplicationsStringFilter


class ApplicationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
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
    | ApplicationsLikeCondition
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
    addresses: list[Any] | None
    """Candidate's addresses"""
    application_ids: list[Any] | None
    """List of application IDs"""
    applications: list[Any] | None
    """An array of all applications made by candidates."""
    attachments: list[Any] | None
    """Attachments related to the candidate"""
    can_email: bool | None
    """Indicates if candidate can be emailed"""
    company: str | None
    """Company where the candidate is associated"""
    coordinator: str | None
    """Coordinator assigned to the candidate"""
    created_at: str | None
    """Date and time of creation"""
    custom_fields: dict[str, Any] | None
    """Custom fields associated with the candidate"""
    educations: list[Any] | None
    """List of candidate's educations"""
    email_addresses: list[Any] | None
    """Candidate's email addresses"""
    employments: list[Any] | None
    """List of candidate's employments"""
    first_name: str | None
    """Candidate's first name"""
    id: int | None
    """Candidate's ID"""
    is_private: bool | None
    """Indicates if the candidate's data is private"""
    keyed_custom_fields: dict[str, Any] | None
    """Keyed custom fields associated with the candidate"""
    last_activity: str | None
    """Details of the last activity related to the candidate"""
    last_name: str | None
    """Candidate's last name"""
    phone_numbers: list[Any] | None
    """Candidate's phone numbers"""
    photo_url: str | None
    """URL of the candidate's profile photo"""
    recruiter: str | None
    """Recruiter assigned to the candidate"""
    social_media_addresses: list[Any] | None
    """Candidate's social media addresses"""
    tags: list[Any] | None
    """Tags associated with the candidate"""
    title: str | None
    """Candidate's title (e.g., Mr., Mrs., Dr.)"""
    updated_at: str | None
    """Date and time of last update"""
    website_addresses: list[Any] | None
    """List of candidate's website addresses"""


class CandidatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    addresses: list[list[Any]]
    """Candidate's addresses"""
    application_ids: list[list[Any]]
    """List of application IDs"""
    applications: list[list[Any]]
    """An array of all applications made by candidates."""
    attachments: list[list[Any]]
    """Attachments related to the candidate"""
    can_email: list[bool]
    """Indicates if candidate can be emailed"""
    company: list[str]
    """Company where the candidate is associated"""
    coordinator: list[str]
    """Coordinator assigned to the candidate"""
    created_at: list[str]
    """Date and time of creation"""
    custom_fields: list[dict[str, Any]]
    """Custom fields associated with the candidate"""
    educations: list[list[Any]]
    """List of candidate's educations"""
    email_addresses: list[list[Any]]
    """Candidate's email addresses"""
    employments: list[list[Any]]
    """List of candidate's employments"""
    first_name: list[str]
    """Candidate's first name"""
    id: list[int]
    """Candidate's ID"""
    is_private: list[bool]
    """Indicates if the candidate's data is private"""
    keyed_custom_fields: list[dict[str, Any]]
    """Keyed custom fields associated with the candidate"""
    last_activity: list[str]
    """Details of the last activity related to the candidate"""
    last_name: list[str]
    """Candidate's last name"""
    phone_numbers: list[list[Any]]
    """Candidate's phone numbers"""
    photo_url: list[str]
    """URL of the candidate's profile photo"""
    recruiter: list[str]
    """Recruiter assigned to the candidate"""
    social_media_addresses: list[list[Any]]
    """Candidate's social media addresses"""
    tags: list[list[Any]]
    """Tags associated with the candidate"""
    title: list[str]
    """Candidate's title (e.g., Mr., Mrs., Dr.)"""
    updated_at: list[str]
    """Date and time of last update"""
    website_addresses: list[list[Any]]
    """List of candidate's website addresses"""


class CandidatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    addresses: Any
    """Candidate's addresses"""
    application_ids: Any
    """List of application IDs"""
    applications: Any
    """An array of all applications made by candidates."""
    attachments: Any
    """Attachments related to the candidate"""
    can_email: Any
    """Indicates if candidate can be emailed"""
    company: Any
    """Company where the candidate is associated"""
    coordinator: Any
    """Coordinator assigned to the candidate"""
    created_at: Any
    """Date and time of creation"""
    custom_fields: Any
    """Custom fields associated with the candidate"""
    educations: Any
    """List of candidate's educations"""
    email_addresses: Any
    """Candidate's email addresses"""
    employments: Any
    """List of candidate's employments"""
    first_name: Any
    """Candidate's first name"""
    id: Any
    """Candidate's ID"""
    is_private: Any
    """Indicates if the candidate's data is private"""
    keyed_custom_fields: Any
    """Keyed custom fields associated with the candidate"""
    last_activity: Any
    """Details of the last activity related to the candidate"""
    last_name: Any
    """Candidate's last name"""
    phone_numbers: Any
    """Candidate's phone numbers"""
    photo_url: Any
    """URL of the candidate's profile photo"""
    recruiter: Any
    """Recruiter assigned to the candidate"""
    social_media_addresses: Any
    """Candidate's social media addresses"""
    tags: Any
    """Tags associated with the candidate"""
    title: Any
    """Candidate's title (e.g., Mr., Mrs., Dr.)"""
    updated_at: Any
    """Date and time of last update"""
    website_addresses: Any
    """List of candidate's website addresses"""


class CandidatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    addresses: str
    """Candidate's addresses"""
    application_ids: str
    """List of application IDs"""
    applications: str
    """An array of all applications made by candidates."""
    attachments: str
    """Attachments related to the candidate"""
    can_email: str
    """Indicates if candidate can be emailed"""
    company: str
    """Company where the candidate is associated"""
    coordinator: str
    """Coordinator assigned to the candidate"""
    created_at: str
    """Date and time of creation"""
    custom_fields: str
    """Custom fields associated with the candidate"""
    educations: str
    """List of candidate's educations"""
    email_addresses: str
    """Candidate's email addresses"""
    employments: str
    """List of candidate's employments"""
    first_name: str
    """Candidate's first name"""
    id: str
    """Candidate's ID"""
    is_private: str
    """Indicates if the candidate's data is private"""
    keyed_custom_fields: str
    """Keyed custom fields associated with the candidate"""
    last_activity: str
    """Details of the last activity related to the candidate"""
    last_name: str
    """Candidate's last name"""
    phone_numbers: str
    """Candidate's phone numbers"""
    photo_url: str
    """URL of the candidate's profile photo"""
    recruiter: str
    """Recruiter assigned to the candidate"""
    social_media_addresses: str
    """Candidate's social media addresses"""
    tags: str
    """Tags associated with the candidate"""
    title: str
    """Candidate's title (e.g., Mr., Mrs., Dr.)"""
    updated_at: str
    """Date and time of last update"""
    website_addresses: str
    """List of candidate's website addresses"""


class CandidatesSortFilter(TypedDict, total=False):
    """Available fields for sorting candidates search results."""
    addresses: AirbyteSortOrder
    """Candidate's addresses"""
    application_ids: AirbyteSortOrder
    """List of application IDs"""
    applications: AirbyteSortOrder
    """An array of all applications made by candidates."""
    attachments: AirbyteSortOrder
    """Attachments related to the candidate"""
    can_email: AirbyteSortOrder
    """Indicates if candidate can be emailed"""
    company: AirbyteSortOrder
    """Company where the candidate is associated"""
    coordinator: AirbyteSortOrder
    """Coordinator assigned to the candidate"""
    created_at: AirbyteSortOrder
    """Date and time of creation"""
    custom_fields: AirbyteSortOrder
    """Custom fields associated with the candidate"""
    educations: AirbyteSortOrder
    """List of candidate's educations"""
    email_addresses: AirbyteSortOrder
    """Candidate's email addresses"""
    employments: AirbyteSortOrder
    """List of candidate's employments"""
    first_name: AirbyteSortOrder
    """Candidate's first name"""
    id: AirbyteSortOrder
    """Candidate's ID"""
    is_private: AirbyteSortOrder
    """Indicates if the candidate's data is private"""
    keyed_custom_fields: AirbyteSortOrder
    """Keyed custom fields associated with the candidate"""
    last_activity: AirbyteSortOrder
    """Details of the last activity related to the candidate"""
    last_name: AirbyteSortOrder
    """Candidate's last name"""
    phone_numbers: AirbyteSortOrder
    """Candidate's phone numbers"""
    photo_url: AirbyteSortOrder
    """URL of the candidate's profile photo"""
    recruiter: AirbyteSortOrder
    """Recruiter assigned to the candidate"""
    social_media_addresses: AirbyteSortOrder
    """Candidate's social media addresses"""
    tags: AirbyteSortOrder
    """Tags associated with the candidate"""
    title: AirbyteSortOrder
    """Candidate's title (e.g., Mr., Mrs., Dr.)"""
    updated_at: AirbyteSortOrder
    """Date and time of last update"""
    website_addresses: AirbyteSortOrder
    """List of candidate's website addresses"""


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


class CandidatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CandidatesStringFilter


class CandidatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CandidatesStringFilter


class CandidatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CandidatesStringFilter


class CandidatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
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
    | CandidatesLikeCondition
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


# ===== DEPARTMENTS SEARCH TYPES =====

class DepartmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering departments search queries."""
    child_department_external_ids: list[Any] | None
    """External IDs of child departments associated with this department."""
    child_ids: list[Any] | None
    """Unique IDs of child departments associated with this department."""
    external_id: str | None
    """External ID of this department."""
    id: int | None
    """Unique ID of this department."""
    name: str | None
    """Name of the department."""
    parent_department_external_id: str | None
    """External ID of the parent department of this department."""
    parent_id: int | None
    """Unique ID of the parent department of this department."""


class DepartmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    child_department_external_ids: list[list[Any]]
    """External IDs of child departments associated with this department."""
    child_ids: list[list[Any]]
    """Unique IDs of child departments associated with this department."""
    external_id: list[str]
    """External ID of this department."""
    id: list[int]
    """Unique ID of this department."""
    name: list[str]
    """Name of the department."""
    parent_department_external_id: list[str]
    """External ID of the parent department of this department."""
    parent_id: list[int]
    """Unique ID of the parent department of this department."""


class DepartmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    child_department_external_ids: Any
    """External IDs of child departments associated with this department."""
    child_ids: Any
    """Unique IDs of child departments associated with this department."""
    external_id: Any
    """External ID of this department."""
    id: Any
    """Unique ID of this department."""
    name: Any
    """Name of the department."""
    parent_department_external_id: Any
    """External ID of the parent department of this department."""
    parent_id: Any
    """Unique ID of the parent department of this department."""


class DepartmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    child_department_external_ids: str
    """External IDs of child departments associated with this department."""
    child_ids: str
    """Unique IDs of child departments associated with this department."""
    external_id: str
    """External ID of this department."""
    id: str
    """Unique ID of this department."""
    name: str
    """Name of the department."""
    parent_department_external_id: str
    """External ID of the parent department of this department."""
    parent_id: str
    """Unique ID of the parent department of this department."""


class DepartmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting departments search results."""
    child_department_external_ids: AirbyteSortOrder
    """External IDs of child departments associated with this department."""
    child_ids: AirbyteSortOrder
    """Unique IDs of child departments associated with this department."""
    external_id: AirbyteSortOrder
    """External ID of this department."""
    id: AirbyteSortOrder
    """Unique ID of this department."""
    name: AirbyteSortOrder
    """Name of the department."""
    parent_department_external_id: AirbyteSortOrder
    """External ID of the parent department of this department."""
    parent_id: AirbyteSortOrder
    """Unique ID of the parent department of this department."""


# Entity-specific condition types for departments
class DepartmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DepartmentsSearchFilter


class DepartmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DepartmentsSearchFilter


class DepartmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DepartmentsSearchFilter


class DepartmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DepartmentsSearchFilter


class DepartmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DepartmentsSearchFilter


class DepartmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DepartmentsSearchFilter


class DepartmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DepartmentsStringFilter


class DepartmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DepartmentsStringFilter


class DepartmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DepartmentsStringFilter


class DepartmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DepartmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DepartmentsInCondition = TypedDict("DepartmentsInCondition", {"in": DepartmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DepartmentsNotCondition = TypedDict("DepartmentsNotCondition", {"not": "DepartmentsCondition"}, total=False)
"""Negates the nested condition."""

DepartmentsAndCondition = TypedDict("DepartmentsAndCondition", {"and": "list[DepartmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

DepartmentsOrCondition = TypedDict("DepartmentsOrCondition", {"or": "list[DepartmentsCondition]"}, total=False)
"""True if any nested condition is true."""

DepartmentsAnyCondition = TypedDict("DepartmentsAnyCondition", {"any": DepartmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all departments condition types
DepartmentsCondition = (
    DepartmentsEqCondition
    | DepartmentsNeqCondition
    | DepartmentsGtCondition
    | DepartmentsGteCondition
    | DepartmentsLtCondition
    | DepartmentsLteCondition
    | DepartmentsInCondition
    | DepartmentsLikeCondition
    | DepartmentsFuzzyCondition
    | DepartmentsKeywordCondition
    | DepartmentsContainsCondition
    | DepartmentsNotCondition
    | DepartmentsAndCondition
    | DepartmentsOrCondition
    | DepartmentsAnyCondition
)


class DepartmentsSearchQuery(TypedDict, total=False):
    """Search query for departments entity."""
    filter: DepartmentsCondition
    sort: list[DepartmentsSortFilter]


# ===== JOB_POSTS SEARCH TYPES =====

class JobPostsSearchFilter(TypedDict, total=False):
    """Available fields for filtering job_posts search queries."""
    active: bool | None
    """Flag indicating if the job post is active or not."""
    content: str | None
    """Content or description of the job post."""
    created_at: str | None
    """Date and time when the job post was created."""
    demographic_question_set_id: int | None
    """ID of the demographic question set associated with the job post."""
    external: bool | None
    """Flag indicating if the job post is external or not."""
    first_published_at: str | None
    """Date and time when the job post was first published."""
    id: int | None
    """Unique identifier of the job post."""
    internal: bool | None
    """Flag indicating if the job post is internal or not."""
    internal_content: str | None
    """Internal content or description of the job post."""
    job_id: int | None
    """ID of the job associated with the job post."""
    live: bool | None
    """Flag indicating if the job post is live or not."""
    location: dict[str, Any] | None
    """Details about the job post location."""
    questions: list[Any] | None
    """List of questions related to the job post."""
    title: str | None
    """Title or headline of the job post."""
    updated_at: str | None
    """Date and time when the job post was last updated."""


class JobPostsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Flag indicating if the job post is active or not."""
    content: list[str]
    """Content or description of the job post."""
    created_at: list[str]
    """Date and time when the job post was created."""
    demographic_question_set_id: list[int]
    """ID of the demographic question set associated with the job post."""
    external: list[bool]
    """Flag indicating if the job post is external or not."""
    first_published_at: list[str]
    """Date and time when the job post was first published."""
    id: list[int]
    """Unique identifier of the job post."""
    internal: list[bool]
    """Flag indicating if the job post is internal or not."""
    internal_content: list[str]
    """Internal content or description of the job post."""
    job_id: list[int]
    """ID of the job associated with the job post."""
    live: list[bool]
    """Flag indicating if the job post is live or not."""
    location: list[dict[str, Any]]
    """Details about the job post location."""
    questions: list[list[Any]]
    """List of questions related to the job post."""
    title: list[str]
    """Title or headline of the job post."""
    updated_at: list[str]
    """Date and time when the job post was last updated."""


class JobPostsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Flag indicating if the job post is active or not."""
    content: Any
    """Content or description of the job post."""
    created_at: Any
    """Date and time when the job post was created."""
    demographic_question_set_id: Any
    """ID of the demographic question set associated with the job post."""
    external: Any
    """Flag indicating if the job post is external or not."""
    first_published_at: Any
    """Date and time when the job post was first published."""
    id: Any
    """Unique identifier of the job post."""
    internal: Any
    """Flag indicating if the job post is internal or not."""
    internal_content: Any
    """Internal content or description of the job post."""
    job_id: Any
    """ID of the job associated with the job post."""
    live: Any
    """Flag indicating if the job post is live or not."""
    location: Any
    """Details about the job post location."""
    questions: Any
    """List of questions related to the job post."""
    title: Any
    """Title or headline of the job post."""
    updated_at: Any
    """Date and time when the job post was last updated."""


class JobPostsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Flag indicating if the job post is active or not."""
    content: str
    """Content or description of the job post."""
    created_at: str
    """Date and time when the job post was created."""
    demographic_question_set_id: str
    """ID of the demographic question set associated with the job post."""
    external: str
    """Flag indicating if the job post is external or not."""
    first_published_at: str
    """Date and time when the job post was first published."""
    id: str
    """Unique identifier of the job post."""
    internal: str
    """Flag indicating if the job post is internal or not."""
    internal_content: str
    """Internal content or description of the job post."""
    job_id: str
    """ID of the job associated with the job post."""
    live: str
    """Flag indicating if the job post is live or not."""
    location: str
    """Details about the job post location."""
    questions: str
    """List of questions related to the job post."""
    title: str
    """Title or headline of the job post."""
    updated_at: str
    """Date and time when the job post was last updated."""


class JobPostsSortFilter(TypedDict, total=False):
    """Available fields for sorting job_posts search results."""
    active: AirbyteSortOrder
    """Flag indicating if the job post is active or not."""
    content: AirbyteSortOrder
    """Content or description of the job post."""
    created_at: AirbyteSortOrder
    """Date and time when the job post was created."""
    demographic_question_set_id: AirbyteSortOrder
    """ID of the demographic question set associated with the job post."""
    external: AirbyteSortOrder
    """Flag indicating if the job post is external or not."""
    first_published_at: AirbyteSortOrder
    """Date and time when the job post was first published."""
    id: AirbyteSortOrder
    """Unique identifier of the job post."""
    internal: AirbyteSortOrder
    """Flag indicating if the job post is internal or not."""
    internal_content: AirbyteSortOrder
    """Internal content or description of the job post."""
    job_id: AirbyteSortOrder
    """ID of the job associated with the job post."""
    live: AirbyteSortOrder
    """Flag indicating if the job post is live or not."""
    location: AirbyteSortOrder
    """Details about the job post location."""
    questions: AirbyteSortOrder
    """List of questions related to the job post."""
    title: AirbyteSortOrder
    """Title or headline of the job post."""
    updated_at: AirbyteSortOrder
    """Date and time when the job post was last updated."""


# Entity-specific condition types for job_posts
class JobPostsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: JobPostsSearchFilter


class JobPostsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: JobPostsSearchFilter


class JobPostsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: JobPostsSearchFilter


class JobPostsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: JobPostsSearchFilter


class JobPostsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: JobPostsSearchFilter


class JobPostsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: JobPostsSearchFilter


class JobPostsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: JobPostsStringFilter


class JobPostsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: JobPostsStringFilter


class JobPostsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: JobPostsStringFilter


class JobPostsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: JobPostsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
JobPostsInCondition = TypedDict("JobPostsInCondition", {"in": JobPostsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

JobPostsNotCondition = TypedDict("JobPostsNotCondition", {"not": "JobPostsCondition"}, total=False)
"""Negates the nested condition."""

JobPostsAndCondition = TypedDict("JobPostsAndCondition", {"and": "list[JobPostsCondition]"}, total=False)
"""True if all nested conditions are true."""

JobPostsOrCondition = TypedDict("JobPostsOrCondition", {"or": "list[JobPostsCondition]"}, total=False)
"""True if any nested condition is true."""

JobPostsAnyCondition = TypedDict("JobPostsAnyCondition", {"any": JobPostsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all job_posts condition types
JobPostsCondition = (
    JobPostsEqCondition
    | JobPostsNeqCondition
    | JobPostsGtCondition
    | JobPostsGteCondition
    | JobPostsLtCondition
    | JobPostsLteCondition
    | JobPostsInCondition
    | JobPostsLikeCondition
    | JobPostsFuzzyCondition
    | JobPostsKeywordCondition
    | JobPostsContainsCondition
    | JobPostsNotCondition
    | JobPostsAndCondition
    | JobPostsOrCondition
    | JobPostsAnyCondition
)


class JobPostsSearchQuery(TypedDict, total=False):
    """Search query for job_posts entity."""
    filter: JobPostsCondition
    sort: list[JobPostsSortFilter]


# ===== JOBS SEARCH TYPES =====

class JobsSearchFilter(TypedDict, total=False):
    """Available fields for filtering jobs search queries."""
    closed_at: str | None
    """The date and time the job was closed"""
    confidential: bool | None
    """Indicates if the job details are confidential"""
    copied_from_id: int | None
    """The ID of the job from which this job was copied"""
    created_at: str | None
    """The date and time the job was created"""
    custom_fields: dict[str, Any] | None
    """Custom fields related to the job"""
    departments: list[Any] | None
    """Departments associated with the job"""
    hiring_team: dict[str, Any] | None
    """Members of the hiring team for the job"""
    id: int | None
    """Unique ID of the job"""
    is_template: bool | None
    """Indicates if the job is a template"""
    keyed_custom_fields: dict[str, Any] | None
    """Keyed custom fields related to the job"""
    name: str | None
    """Name of the job"""
    notes: str | None
    """Additional notes or comments about the job"""
    offices: list[Any] | None
    """Offices associated with the job"""
    opened_at: str | None
    """The date and time the job was opened"""
    openings: list[Any] | None
    """Openings associated with the job"""
    requisition_id: str | None
    """ID associated with the job requisition"""
    status: str | None
    """Current status of the job"""
    updated_at: str | None
    """The date and time the job was last updated"""


class JobsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    closed_at: list[str]
    """The date and time the job was closed"""
    confidential: list[bool]
    """Indicates if the job details are confidential"""
    copied_from_id: list[int]
    """The ID of the job from which this job was copied"""
    created_at: list[str]
    """The date and time the job was created"""
    custom_fields: list[dict[str, Any]]
    """Custom fields related to the job"""
    departments: list[list[Any]]
    """Departments associated with the job"""
    hiring_team: list[dict[str, Any]]
    """Members of the hiring team for the job"""
    id: list[int]
    """Unique ID of the job"""
    is_template: list[bool]
    """Indicates if the job is a template"""
    keyed_custom_fields: list[dict[str, Any]]
    """Keyed custom fields related to the job"""
    name: list[str]
    """Name of the job"""
    notes: list[str]
    """Additional notes or comments about the job"""
    offices: list[list[Any]]
    """Offices associated with the job"""
    opened_at: list[str]
    """The date and time the job was opened"""
    openings: list[list[Any]]
    """Openings associated with the job"""
    requisition_id: list[str]
    """ID associated with the job requisition"""
    status: list[str]
    """Current status of the job"""
    updated_at: list[str]
    """The date and time the job was last updated"""


class JobsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    closed_at: Any
    """The date and time the job was closed"""
    confidential: Any
    """Indicates if the job details are confidential"""
    copied_from_id: Any
    """The ID of the job from which this job was copied"""
    created_at: Any
    """The date and time the job was created"""
    custom_fields: Any
    """Custom fields related to the job"""
    departments: Any
    """Departments associated with the job"""
    hiring_team: Any
    """Members of the hiring team for the job"""
    id: Any
    """Unique ID of the job"""
    is_template: Any
    """Indicates if the job is a template"""
    keyed_custom_fields: Any
    """Keyed custom fields related to the job"""
    name: Any
    """Name of the job"""
    notes: Any
    """Additional notes or comments about the job"""
    offices: Any
    """Offices associated with the job"""
    opened_at: Any
    """The date and time the job was opened"""
    openings: Any
    """Openings associated with the job"""
    requisition_id: Any
    """ID associated with the job requisition"""
    status: Any
    """Current status of the job"""
    updated_at: Any
    """The date and time the job was last updated"""


class JobsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    closed_at: str
    """The date and time the job was closed"""
    confidential: str
    """Indicates if the job details are confidential"""
    copied_from_id: str
    """The ID of the job from which this job was copied"""
    created_at: str
    """The date and time the job was created"""
    custom_fields: str
    """Custom fields related to the job"""
    departments: str
    """Departments associated with the job"""
    hiring_team: str
    """Members of the hiring team for the job"""
    id: str
    """Unique ID of the job"""
    is_template: str
    """Indicates if the job is a template"""
    keyed_custom_fields: str
    """Keyed custom fields related to the job"""
    name: str
    """Name of the job"""
    notes: str
    """Additional notes or comments about the job"""
    offices: str
    """Offices associated with the job"""
    opened_at: str
    """The date and time the job was opened"""
    openings: str
    """Openings associated with the job"""
    requisition_id: str
    """ID associated with the job requisition"""
    status: str
    """Current status of the job"""
    updated_at: str
    """The date and time the job was last updated"""


class JobsSortFilter(TypedDict, total=False):
    """Available fields for sorting jobs search results."""
    closed_at: AirbyteSortOrder
    """The date and time the job was closed"""
    confidential: AirbyteSortOrder
    """Indicates if the job details are confidential"""
    copied_from_id: AirbyteSortOrder
    """The ID of the job from which this job was copied"""
    created_at: AirbyteSortOrder
    """The date and time the job was created"""
    custom_fields: AirbyteSortOrder
    """Custom fields related to the job"""
    departments: AirbyteSortOrder
    """Departments associated with the job"""
    hiring_team: AirbyteSortOrder
    """Members of the hiring team for the job"""
    id: AirbyteSortOrder
    """Unique ID of the job"""
    is_template: AirbyteSortOrder
    """Indicates if the job is a template"""
    keyed_custom_fields: AirbyteSortOrder
    """Keyed custom fields related to the job"""
    name: AirbyteSortOrder
    """Name of the job"""
    notes: AirbyteSortOrder
    """Additional notes or comments about the job"""
    offices: AirbyteSortOrder
    """Offices associated with the job"""
    opened_at: AirbyteSortOrder
    """The date and time the job was opened"""
    openings: AirbyteSortOrder
    """Openings associated with the job"""
    requisition_id: AirbyteSortOrder
    """ID associated with the job requisition"""
    status: AirbyteSortOrder
    """Current status of the job"""
    updated_at: AirbyteSortOrder
    """The date and time the job was last updated"""


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


class JobsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: JobsStringFilter


class JobsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: JobsStringFilter


class JobsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: JobsStringFilter


class JobsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
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
    | JobsLikeCondition
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


# ===== OFFERS SEARCH TYPES =====

class OffersSearchFilter(TypedDict, total=False):
    """Available fields for filtering offers search queries."""
    application_id: int | None
    """Unique identifier for the application associated with the offer"""
    candidate_id: int | None
    """Unique identifier for the candidate associated with the offer"""
    created_at: str | None
    """Timestamp indicating when the offer was created"""
    custom_fields: dict[str, Any] | None
    """Additional custom fields related to the offer"""
    id: int | None
    """Unique identifier for the offer"""
    job_id: int | None
    """Unique identifier for the job associated with the offer"""
    keyed_custom_fields: dict[str, Any] | None
    """Keyed custom fields associated with the offer"""
    opening: dict[str, Any] | None
    """Details about the job opening"""
    resolved_at: str | None
    """Timestamp indicating when the offer was resolved"""
    sent_at: str | None
    """Timestamp indicating when the offer was sent"""
    starts_at: str | None
    """Timestamp indicating when the offer starts"""
    status: str | None
    """Status of the offer"""
    updated_at: str | None
    """Timestamp indicating when the offer was last updated"""
    version: int | None
    """Version of the offer data"""


class OffersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    application_id: list[int]
    """Unique identifier for the application associated with the offer"""
    candidate_id: list[int]
    """Unique identifier for the candidate associated with the offer"""
    created_at: list[str]
    """Timestamp indicating when the offer was created"""
    custom_fields: list[dict[str, Any]]
    """Additional custom fields related to the offer"""
    id: list[int]
    """Unique identifier for the offer"""
    job_id: list[int]
    """Unique identifier for the job associated with the offer"""
    keyed_custom_fields: list[dict[str, Any]]
    """Keyed custom fields associated with the offer"""
    opening: list[dict[str, Any]]
    """Details about the job opening"""
    resolved_at: list[str]
    """Timestamp indicating when the offer was resolved"""
    sent_at: list[str]
    """Timestamp indicating when the offer was sent"""
    starts_at: list[str]
    """Timestamp indicating when the offer starts"""
    status: list[str]
    """Status of the offer"""
    updated_at: list[str]
    """Timestamp indicating when the offer was last updated"""
    version: list[int]
    """Version of the offer data"""


class OffersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    application_id: Any
    """Unique identifier for the application associated with the offer"""
    candidate_id: Any
    """Unique identifier for the candidate associated with the offer"""
    created_at: Any
    """Timestamp indicating when the offer was created"""
    custom_fields: Any
    """Additional custom fields related to the offer"""
    id: Any
    """Unique identifier for the offer"""
    job_id: Any
    """Unique identifier for the job associated with the offer"""
    keyed_custom_fields: Any
    """Keyed custom fields associated with the offer"""
    opening: Any
    """Details about the job opening"""
    resolved_at: Any
    """Timestamp indicating when the offer was resolved"""
    sent_at: Any
    """Timestamp indicating when the offer was sent"""
    starts_at: Any
    """Timestamp indicating when the offer starts"""
    status: Any
    """Status of the offer"""
    updated_at: Any
    """Timestamp indicating when the offer was last updated"""
    version: Any
    """Version of the offer data"""


class OffersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    application_id: str
    """Unique identifier for the application associated with the offer"""
    candidate_id: str
    """Unique identifier for the candidate associated with the offer"""
    created_at: str
    """Timestamp indicating when the offer was created"""
    custom_fields: str
    """Additional custom fields related to the offer"""
    id: str
    """Unique identifier for the offer"""
    job_id: str
    """Unique identifier for the job associated with the offer"""
    keyed_custom_fields: str
    """Keyed custom fields associated with the offer"""
    opening: str
    """Details about the job opening"""
    resolved_at: str
    """Timestamp indicating when the offer was resolved"""
    sent_at: str
    """Timestamp indicating when the offer was sent"""
    starts_at: str
    """Timestamp indicating when the offer starts"""
    status: str
    """Status of the offer"""
    updated_at: str
    """Timestamp indicating when the offer was last updated"""
    version: str
    """Version of the offer data"""


class OffersSortFilter(TypedDict, total=False):
    """Available fields for sorting offers search results."""
    application_id: AirbyteSortOrder
    """Unique identifier for the application associated with the offer"""
    candidate_id: AirbyteSortOrder
    """Unique identifier for the candidate associated with the offer"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the offer was created"""
    custom_fields: AirbyteSortOrder
    """Additional custom fields related to the offer"""
    id: AirbyteSortOrder
    """Unique identifier for the offer"""
    job_id: AirbyteSortOrder
    """Unique identifier for the job associated with the offer"""
    keyed_custom_fields: AirbyteSortOrder
    """Keyed custom fields associated with the offer"""
    opening: AirbyteSortOrder
    """Details about the job opening"""
    resolved_at: AirbyteSortOrder
    """Timestamp indicating when the offer was resolved"""
    sent_at: AirbyteSortOrder
    """Timestamp indicating when the offer was sent"""
    starts_at: AirbyteSortOrder
    """Timestamp indicating when the offer starts"""
    status: AirbyteSortOrder
    """Status of the offer"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the offer was last updated"""
    version: AirbyteSortOrder
    """Version of the offer data"""


# Entity-specific condition types for offers
class OffersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OffersSearchFilter


class OffersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OffersSearchFilter


class OffersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OffersSearchFilter


class OffersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OffersSearchFilter


class OffersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OffersSearchFilter


class OffersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OffersSearchFilter


class OffersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OffersStringFilter


class OffersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OffersStringFilter


class OffersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OffersStringFilter


class OffersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OffersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OffersInCondition = TypedDict("OffersInCondition", {"in": OffersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OffersNotCondition = TypedDict("OffersNotCondition", {"not": "OffersCondition"}, total=False)
"""Negates the nested condition."""

OffersAndCondition = TypedDict("OffersAndCondition", {"and": "list[OffersCondition]"}, total=False)
"""True if all nested conditions are true."""

OffersOrCondition = TypedDict("OffersOrCondition", {"or": "list[OffersCondition]"}, total=False)
"""True if any nested condition is true."""

OffersAnyCondition = TypedDict("OffersAnyCondition", {"any": OffersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all offers condition types
OffersCondition = (
    OffersEqCondition
    | OffersNeqCondition
    | OffersGtCondition
    | OffersGteCondition
    | OffersLtCondition
    | OffersLteCondition
    | OffersInCondition
    | OffersLikeCondition
    | OffersFuzzyCondition
    | OffersKeywordCondition
    | OffersContainsCondition
    | OffersNotCondition
    | OffersAndCondition
    | OffersOrCondition
    | OffersAnyCondition
)


class OffersSearchQuery(TypedDict, total=False):
    """Search query for offers entity."""
    filter: OffersCondition
    sort: list[OffersSortFilter]


# ===== OFFICES SEARCH TYPES =====

class OfficesSearchFilter(TypedDict, total=False):
    """Available fields for filtering offices search queries."""
    child_ids: list[Any] | None
    """IDs of child offices associated with this office"""
    child_office_external_ids: list[Any] | None
    """External IDs of child offices associated with this office"""
    external_id: str | None
    """Unique identifier for this office in the external system"""
    id: int | None
    """Unique identifier for this office in the API system"""
    location: dict[str, Any] | None
    """Location details of this office"""
    name: str | None
    """Name of the office"""
    parent_id: int | None
    """ID of the parent office, if this office is a branch office"""
    parent_office_external_id: str | None
    """External ID of the parent office in the external system"""
    primary_contact_user_id: int | None
    """User ID of the primary contact person for this office"""


class OfficesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    child_ids: list[list[Any]]
    """IDs of child offices associated with this office"""
    child_office_external_ids: list[list[Any]]
    """External IDs of child offices associated with this office"""
    external_id: list[str]
    """Unique identifier for this office in the external system"""
    id: list[int]
    """Unique identifier for this office in the API system"""
    location: list[dict[str, Any]]
    """Location details of this office"""
    name: list[str]
    """Name of the office"""
    parent_id: list[int]
    """ID of the parent office, if this office is a branch office"""
    parent_office_external_id: list[str]
    """External ID of the parent office in the external system"""
    primary_contact_user_id: list[int]
    """User ID of the primary contact person for this office"""


class OfficesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    child_ids: Any
    """IDs of child offices associated with this office"""
    child_office_external_ids: Any
    """External IDs of child offices associated with this office"""
    external_id: Any
    """Unique identifier for this office in the external system"""
    id: Any
    """Unique identifier for this office in the API system"""
    location: Any
    """Location details of this office"""
    name: Any
    """Name of the office"""
    parent_id: Any
    """ID of the parent office, if this office is a branch office"""
    parent_office_external_id: Any
    """External ID of the parent office in the external system"""
    primary_contact_user_id: Any
    """User ID of the primary contact person for this office"""


class OfficesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    child_ids: str
    """IDs of child offices associated with this office"""
    child_office_external_ids: str
    """External IDs of child offices associated with this office"""
    external_id: str
    """Unique identifier for this office in the external system"""
    id: str
    """Unique identifier for this office in the API system"""
    location: str
    """Location details of this office"""
    name: str
    """Name of the office"""
    parent_id: str
    """ID of the parent office, if this office is a branch office"""
    parent_office_external_id: str
    """External ID of the parent office in the external system"""
    primary_contact_user_id: str
    """User ID of the primary contact person for this office"""


class OfficesSortFilter(TypedDict, total=False):
    """Available fields for sorting offices search results."""
    child_ids: AirbyteSortOrder
    """IDs of child offices associated with this office"""
    child_office_external_ids: AirbyteSortOrder
    """External IDs of child offices associated with this office"""
    external_id: AirbyteSortOrder
    """Unique identifier for this office in the external system"""
    id: AirbyteSortOrder
    """Unique identifier for this office in the API system"""
    location: AirbyteSortOrder
    """Location details of this office"""
    name: AirbyteSortOrder
    """Name of the office"""
    parent_id: AirbyteSortOrder
    """ID of the parent office, if this office is a branch office"""
    parent_office_external_id: AirbyteSortOrder
    """External ID of the parent office in the external system"""
    primary_contact_user_id: AirbyteSortOrder
    """User ID of the primary contact person for this office"""


# Entity-specific condition types for offices
class OfficesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OfficesSearchFilter


class OfficesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OfficesSearchFilter


class OfficesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OfficesSearchFilter


class OfficesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OfficesSearchFilter


class OfficesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OfficesSearchFilter


class OfficesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OfficesSearchFilter


class OfficesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OfficesStringFilter


class OfficesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OfficesStringFilter


class OfficesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OfficesStringFilter


class OfficesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OfficesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OfficesInCondition = TypedDict("OfficesInCondition", {"in": OfficesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OfficesNotCondition = TypedDict("OfficesNotCondition", {"not": "OfficesCondition"}, total=False)
"""Negates the nested condition."""

OfficesAndCondition = TypedDict("OfficesAndCondition", {"and": "list[OfficesCondition]"}, total=False)
"""True if all nested conditions are true."""

OfficesOrCondition = TypedDict("OfficesOrCondition", {"or": "list[OfficesCondition]"}, total=False)
"""True if any nested condition is true."""

OfficesAnyCondition = TypedDict("OfficesAnyCondition", {"any": OfficesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all offices condition types
OfficesCondition = (
    OfficesEqCondition
    | OfficesNeqCondition
    | OfficesGtCondition
    | OfficesGteCondition
    | OfficesLtCondition
    | OfficesLteCondition
    | OfficesInCondition
    | OfficesLikeCondition
    | OfficesFuzzyCondition
    | OfficesKeywordCondition
    | OfficesContainsCondition
    | OfficesNotCondition
    | OfficesAndCondition
    | OfficesOrCondition
    | OfficesAnyCondition
)


class OfficesSearchQuery(TypedDict, total=False):
    """Search query for offices entity."""
    filter: OfficesCondition
    sort: list[OfficesSortFilter]


# ===== SOURCES SEARCH TYPES =====

class SourcesSearchFilter(TypedDict, total=False):
    """Available fields for filtering sources search queries."""
    id: int | None
    """The unique identifier for the source."""
    name: str | None
    """The name of the source."""
    type: dict[str, Any] | None
    """Type of the data source"""


class SourcesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """The unique identifier for the source."""
    name: list[str]
    """The name of the source."""
    type: list[dict[str, Any]]
    """Type of the data source"""


class SourcesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique identifier for the source."""
    name: Any
    """The name of the source."""
    type: Any
    """Type of the data source"""


class SourcesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """The unique identifier for the source."""
    name: str
    """The name of the source."""
    type: str
    """Type of the data source"""


class SourcesSortFilter(TypedDict, total=False):
    """Available fields for sorting sources search results."""
    id: AirbyteSortOrder
    """The unique identifier for the source."""
    name: AirbyteSortOrder
    """The name of the source."""
    type: AirbyteSortOrder
    """Type of the data source"""


# Entity-specific condition types for sources
class SourcesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SourcesSearchFilter


class SourcesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SourcesSearchFilter


class SourcesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SourcesSearchFilter


class SourcesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SourcesSearchFilter


class SourcesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SourcesSearchFilter


class SourcesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SourcesSearchFilter


class SourcesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SourcesStringFilter


class SourcesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SourcesStringFilter


class SourcesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SourcesStringFilter


class SourcesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SourcesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SourcesInCondition = TypedDict("SourcesInCondition", {"in": SourcesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SourcesNotCondition = TypedDict("SourcesNotCondition", {"not": "SourcesCondition"}, total=False)
"""Negates the nested condition."""

SourcesAndCondition = TypedDict("SourcesAndCondition", {"and": "list[SourcesCondition]"}, total=False)
"""True if all nested conditions are true."""

SourcesOrCondition = TypedDict("SourcesOrCondition", {"or": "list[SourcesCondition]"}, total=False)
"""True if any nested condition is true."""

SourcesAnyCondition = TypedDict("SourcesAnyCondition", {"any": SourcesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sources condition types
SourcesCondition = (
    SourcesEqCondition
    | SourcesNeqCondition
    | SourcesGtCondition
    | SourcesGteCondition
    | SourcesLtCondition
    | SourcesLteCondition
    | SourcesInCondition
    | SourcesLikeCondition
    | SourcesFuzzyCondition
    | SourcesKeywordCondition
    | SourcesContainsCondition
    | SourcesNotCondition
    | SourcesAndCondition
    | SourcesOrCondition
    | SourcesAnyCondition
)


class SourcesSearchQuery(TypedDict, total=False):
    """Search query for sources entity."""
    filter: SourcesCondition
    sort: list[SourcesSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    created_at: str | None
    """The date and time when the user account was created."""
    departments: list[Any] | None
    """List of departments associated with users"""
    disabled: bool | None
    """Indicates whether the user account is disabled."""
    emails: list[Any] | None
    """Email addresses of the users"""
    employee_id: str | None
    """Employee identifier for the user."""
    first_name: str | None
    """The first name of the user."""
    id: int | None
    """Unique identifier for the user."""
    last_name: str | None
    """The last name of the user."""
    linked_candidate_ids: list[Any] | None
    """IDs of candidates linked to the user."""
    name: str | None
    """The full name of the user."""
    offices: list[Any] | None
    """List of office locations where users are based"""
    primary_email_address: str | None
    """The primary email address of the user."""
    site_admin: bool | None
    """Indicates whether the user is a site administrator."""
    updated_at: str | None
    """The date and time when the user account was last updated."""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """The date and time when the user account was created."""
    departments: list[list[Any]]
    """List of departments associated with users"""
    disabled: list[bool]
    """Indicates whether the user account is disabled."""
    emails: list[list[Any]]
    """Email addresses of the users"""
    employee_id: list[str]
    """Employee identifier for the user."""
    first_name: list[str]
    """The first name of the user."""
    id: list[int]
    """Unique identifier for the user."""
    last_name: list[str]
    """The last name of the user."""
    linked_candidate_ids: list[list[Any]]
    """IDs of candidates linked to the user."""
    name: list[str]
    """The full name of the user."""
    offices: list[list[Any]]
    """List of office locations where users are based"""
    primary_email_address: list[str]
    """The primary email address of the user."""
    site_admin: list[bool]
    """Indicates whether the user is a site administrator."""
    updated_at: list[str]
    """The date and time when the user account was last updated."""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """The date and time when the user account was created."""
    departments: Any
    """List of departments associated with users"""
    disabled: Any
    """Indicates whether the user account is disabled."""
    emails: Any
    """Email addresses of the users"""
    employee_id: Any
    """Employee identifier for the user."""
    first_name: Any
    """The first name of the user."""
    id: Any
    """Unique identifier for the user."""
    last_name: Any
    """The last name of the user."""
    linked_candidate_ids: Any
    """IDs of candidates linked to the user."""
    name: Any
    """The full name of the user."""
    offices: Any
    """List of office locations where users are based"""
    primary_email_address: Any
    """The primary email address of the user."""
    site_admin: Any
    """Indicates whether the user is a site administrator."""
    updated_at: Any
    """The date and time when the user account was last updated."""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """The date and time when the user account was created."""
    departments: str
    """List of departments associated with users"""
    disabled: str
    """Indicates whether the user account is disabled."""
    emails: str
    """Email addresses of the users"""
    employee_id: str
    """Employee identifier for the user."""
    first_name: str
    """The first name of the user."""
    id: str
    """Unique identifier for the user."""
    last_name: str
    """The last name of the user."""
    linked_candidate_ids: str
    """IDs of candidates linked to the user."""
    name: str
    """The full name of the user."""
    offices: str
    """List of office locations where users are based"""
    primary_email_address: str
    """The primary email address of the user."""
    site_admin: str
    """Indicates whether the user is a site administrator."""
    updated_at: str
    """The date and time when the user account was last updated."""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    created_at: AirbyteSortOrder
    """The date and time when the user account was created."""
    departments: AirbyteSortOrder
    """List of departments associated with users"""
    disabled: AirbyteSortOrder
    """Indicates whether the user account is disabled."""
    emails: AirbyteSortOrder
    """Email addresses of the users"""
    employee_id: AirbyteSortOrder
    """Employee identifier for the user."""
    first_name: AirbyteSortOrder
    """The first name of the user."""
    id: AirbyteSortOrder
    """Unique identifier for the user."""
    last_name: AirbyteSortOrder
    """The last name of the user."""
    linked_candidate_ids: AirbyteSortOrder
    """IDs of candidates linked to the user."""
    name: AirbyteSortOrder
    """The full name of the user."""
    offices: AirbyteSortOrder
    """List of office locations where users are based"""
    primary_email_address: AirbyteSortOrder
    """The primary email address of the user."""
    site_admin: AirbyteSortOrder
    """Indicates whether the user is a site administrator."""
    updated_at: AirbyteSortOrder
    """The date and time when the user account was last updated."""


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


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
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
    | UsersLikeCondition
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
