"""
Pydantic models for greenhouse connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class GreenhouseAuthConfig(BaseModel):
    """Harvest API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Greenhouse Harvest API Key from the Dev Center"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Attachment(BaseModel):
    """File attachment (resume, cover letter, etc.)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    filename: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)

class Candidate(BaseModel):
    """Greenhouse candidate object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    first_name: Union[str, Any] = Field(default=None)
    last_name: Union[str, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    last_activity: Union[str, Any] = Field(default=None)
    is_private: Union[bool, Any] = Field(default=None)
    photo_url: Union[str | None, Any] = Field(default=None)
    attachments: Union[list[Attachment], Any] = Field(default=None)
    application_ids: Union[list[int], Any] = Field(default=None)
    phone_numbers: Union[list[dict[str, Any]], Any] = Field(default=None)
    addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    email_addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    website_addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    social_media_addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    recruiter: Union[dict[str, Any] | None, Any] = Field(default=None)
    coordinator: Union[dict[str, Any] | None, Any] = Field(default=None)
    can_email: Union[bool, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)

class Application(BaseModel):
    """Greenhouse application object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    candidate_id: Union[int, Any] = Field(default=None)
    prospect: Union[bool, Any] = Field(default=None)
    applied_at: Union[str, Any] = Field(default=None)
    rejected_at: Union[str | None, Any] = Field(default=None)
    last_activity_at: Union[str, Any] = Field(default=None)
    location: Union[dict[str, Any] | None, Any] = Field(default=None)
    source: Union[dict[str, Any], Any] = Field(default=None)
    credited_to: Union[dict[str, Any], Any] = Field(default=None)
    rejection_reason: Union[dict[str, Any] | None, Any] = Field(default=None)
    rejection_details: Union[dict[str, Any] | None, Any] = Field(default=None)
    jobs: Union[list[dict[str, Any]], Any] = Field(default=None)
    job_post_id: Union[int | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    current_stage: Union[dict[str, Any] | None, Any] = Field(default=None)
    answers: Union[list[dict[str, Any]], Any] = Field(default=None)
    prospective_office: Union[dict[str, Any] | None, Any] = Field(default=None)
    prospective_department: Union[dict[str, Any] | None, Any] = Field(default=None)
    prospect_detail: Union[dict[str, Any], Any] = Field(default=None)
    attachments: Union[list[Attachment], Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)

class Job(BaseModel):
    """Greenhouse job object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    requisition_id: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    confidential: Union[bool, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    opened_at: Union[str, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    departments: Union[list[dict[str, Any] | None], Any] = Field(default=None)
    offices: Union[list[dict[str, Any]], Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)
    hiring_team: Union[dict[str, Any], Any] = Field(default=None)
    openings: Union[list[dict[str, Any]], Any] = Field(default=None)

class Offer(BaseModel):
    """Greenhouse offer object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    version: Union[int, Any] = Field(default=None)
    application_id: Union[int, Any] = Field(default=None)
    job_id: Union[int, Any] = Field(default=None)
    candidate_id: Union[int, Any] = Field(default=None)
    opening: Union[dict[str, Any] | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    sent_at: Union[str | None, Any] = Field(default=None)
    resolved_at: Union[str | None, Any] = Field(default=None)
    starts_at: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)

class User(BaseModel):
    """Greenhouse user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    first_name: Union[str, Any] = Field(default=None)
    last_name: Union[str, Any] = Field(default=None)
    primary_email_address: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    disabled: Union[bool, Any] = Field(default=None)
    site_admin: Union[bool, Any] = Field(default=None)
    emails: Union[list[str], Any] = Field(default=None)
    employee_id: Union[str | None, Any] = Field(default=None)
    linked_candidate_ids: Union[list[int], Any] = Field(default=None)
    offices: Union[list[dict[str, Any]], Any] = Field(default=None)
    departments: Union[list[dict[str, Any]], Any] = Field(default=None)

class Department(BaseModel):
    """Greenhouse department object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    parent_department_external_id: Union[str | None, Any] = Field(default=None)
    child_ids: Union[list[int], Any] = Field(default=None)
    child_department_external_ids: Union[list[str], Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)

class Office(BaseModel):
    """Greenhouse office object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    location: Union[dict[str, Any] | None, Any] = Field(default=None)
    primary_contact_user_id: Union[int | None, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    parent_office_external_id: Union[str | None, Any] = Field(default=None)
    child_ids: Union[list[int], Any] = Field(default=None)
    child_office_external_ids: Union[list[str], Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)

class JobPost(BaseModel):
    """Greenhouse job post object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    location: Union[dict[str, Any] | None, Any] = Field(default=None)
    internal: Union[bool, Any] = Field(default=None)
    external: Union[bool, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    live: Union[bool, Any] = Field(default=None)
    first_published_at: Union[str | None, Any] = Field(default=None)
    job_id: Union[int, Any] = Field(default=None)
    content: Union[str | None, Any] = Field(default=None)
    internal_content: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    demographic_question_set_id: Union[int | None, Any] = Field(default=None)
    questions: Union[list[dict[str, Any]], Any] = Field(default=None)

class Source(BaseModel):
    """Greenhouse source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type: Union[dict[str, Any] | None, Any] = Field(default=None)

class ScheduledInterview(BaseModel):
    """Greenhouse scheduled interview object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    application_id: Union[int, Any] = Field(default=None)
    external_event_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    start: Union[dict[str, Any] | None, Any] = Field(default=None)
    end: Union[dict[str, Any] | None, Any] = Field(default=None)
    location: Union[str | None, Any] = Field(default=None)
    video_conferencing_url: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    interview: Union[dict[str, Any] | None, Any] = Field(default=None)
    organizer: Union[dict[str, Any] | None, Any] = Field(default=None)
    interviewers: Union[list[dict[str, Any]], Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class GreenhouseCheckResult(BaseModel):
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


class GreenhouseExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GreenhouseExecuteResultWithMeta(GreenhouseExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ApplicationsSearchData(BaseModel):
    """Search result data for applications entity."""
    model_config = ConfigDict(extra="allow")

    answers: list[Any] | None = None
    """Answers provided in the application."""
    applied_at: str | None = None
    """Timestamp when the candidate applied."""
    attachments: list[Any] | None = None
    """Attachments uploaded with the application."""
    candidate_id: int | None = None
    """Unique identifier for the candidate."""
    credited_to: dict[str, Any] | None = None
    """Information about the employee who credited the application."""
    current_stage: dict[str, Any] | None = None
    """Current stage of the application process."""
    id: int | None = None
    """Unique identifier for the application."""
    job_post_id: int | None = None
    """"""
    jobs: list[Any] | None = None
    """Jobs applied for by the candidate."""
    last_activity_at: str | None = None
    """Timestamp of the last activity on the application."""
    location: str | None = None
    """Location related to the application."""
    prospect: bool | None = None
    """Status of the application prospect."""
    prospect_detail: dict[str, Any] | None = None
    """Details related to the application prospect."""
    prospective_department: str | None = None
    """Prospective department for the candidate."""
    prospective_office: str | None = None
    """Prospective office for the candidate."""
    rejected_at: str | None = None
    """Timestamp when the application was rejected."""
    rejection_details: dict[str, Any] | None = None
    """Details related to the application rejection."""
    rejection_reason: dict[str, Any] | None = None
    """Reason for the application rejection."""
    source: dict[str, Any] | None = None
    """Source of the application."""
    status: str | None = None
    """Status of the application."""


class CandidatesSearchData(BaseModel):
    """Search result data for candidates entity."""
    model_config = ConfigDict(extra="allow")

    addresses: list[Any] | None = None
    """Candidate's addresses"""
    application_ids: list[Any] | None = None
    """List of application IDs"""
    applications: list[Any] | None = None
    """An array of all applications made by candidates."""
    attachments: list[Any] | None = None
    """Attachments related to the candidate"""
    can_email: bool | None = None
    """Indicates if candidate can be emailed"""
    company: str | None = None
    """Company where the candidate is associated"""
    coordinator: str | None = None
    """Coordinator assigned to the candidate"""
    created_at: str | None = None
    """Date and time of creation"""
    custom_fields: dict[str, Any] | None = None
    """Custom fields associated with the candidate"""
    educations: list[Any] | None = None
    """List of candidate's educations"""
    email_addresses: list[Any] | None = None
    """Candidate's email addresses"""
    employments: list[Any] | None = None
    """List of candidate's employments"""
    first_name: str | None = None
    """Candidate's first name"""
    id: int | None = None
    """Candidate's ID"""
    is_private: bool | None = None
    """Indicates if the candidate's data is private"""
    keyed_custom_fields: dict[str, Any] | None = None
    """Keyed custom fields associated with the candidate"""
    last_activity: str | None = None
    """Details of the last activity related to the candidate"""
    last_name: str | None = None
    """Candidate's last name"""
    phone_numbers: list[Any] | None = None
    """Candidate's phone numbers"""
    photo_url: str | None = None
    """URL of the candidate's profile photo"""
    recruiter: str | None = None
    """Recruiter assigned to the candidate"""
    social_media_addresses: list[Any] | None = None
    """Candidate's social media addresses"""
    tags: list[Any] | None = None
    """Tags associated with the candidate"""
    title: str | None = None
    """Candidate's title (e.g., Mr., Mrs., Dr.)"""
    updated_at: str | None = None
    """Date and time of last update"""
    website_addresses: list[Any] | None = None
    """List of candidate's website addresses"""


class DepartmentsSearchData(BaseModel):
    """Search result data for departments entity."""
    model_config = ConfigDict(extra="allow")

    child_department_external_ids: list[Any] | None = None
    """External IDs of child departments associated with this department."""
    child_ids: list[Any] | None = None
    """Unique IDs of child departments associated with this department."""
    external_id: str | None = None
    """External ID of this department."""
    id: int | None = None
    """Unique ID of this department."""
    name: str | None = None
    """Name of the department."""
    parent_department_external_id: str | None = None
    """External ID of the parent department of this department."""
    parent_id: int | None = None
    """Unique ID of the parent department of this department."""


class JobPostsSearchData(BaseModel):
    """Search result data for job_posts entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Flag indicating if the job post is active or not."""
    content: str | None = None
    """Content or description of the job post."""
    created_at: str | None = None
    """Date and time when the job post was created."""
    demographic_question_set_id: int | None = None
    """ID of the demographic question set associated with the job post."""
    external: bool | None = None
    """Flag indicating if the job post is external or not."""
    first_published_at: str | None = None
    """Date and time when the job post was first published."""
    id: int | None = None
    """Unique identifier of the job post."""
    internal: bool | None = None
    """Flag indicating if the job post is internal or not."""
    internal_content: str | None = None
    """Internal content or description of the job post."""
    job_id: int | None = None
    """ID of the job associated with the job post."""
    live: bool | None = None
    """Flag indicating if the job post is live or not."""
    location: dict[str, Any] | None = None
    """Details about the job post location."""
    questions: list[Any] | None = None
    """List of questions related to the job post."""
    title: str | None = None
    """Title or headline of the job post."""
    updated_at: str | None = None
    """Date and time when the job post was last updated."""


class JobsSearchData(BaseModel):
    """Search result data for jobs entity."""
    model_config = ConfigDict(extra="allow")

    closed_at: str | None = None
    """The date and time the job was closed"""
    confidential: bool | None = None
    """Indicates if the job details are confidential"""
    copied_from_id: int | None = None
    """The ID of the job from which this job was copied"""
    created_at: str | None = None
    """The date and time the job was created"""
    custom_fields: dict[str, Any] | None = None
    """Custom fields related to the job"""
    departments: list[Any] | None = None
    """Departments associated with the job"""
    hiring_team: dict[str, Any] | None = None
    """Members of the hiring team for the job"""
    id: int | None = None
    """Unique ID of the job"""
    is_template: bool | None = None
    """Indicates if the job is a template"""
    keyed_custom_fields: dict[str, Any] | None = None
    """Keyed custom fields related to the job"""
    name: str | None = None
    """Name of the job"""
    notes: str | None = None
    """Additional notes or comments about the job"""
    offices: list[Any] | None = None
    """Offices associated with the job"""
    opened_at: str | None = None
    """The date and time the job was opened"""
    openings: list[Any] | None = None
    """Openings associated with the job"""
    requisition_id: str | None = None
    """ID associated with the job requisition"""
    status: str | None = None
    """Current status of the job"""
    updated_at: str | None = None
    """The date and time the job was last updated"""


class OffersSearchData(BaseModel):
    """Search result data for offers entity."""
    model_config = ConfigDict(extra="allow")

    application_id: int | None = None
    """Unique identifier for the application associated with the offer"""
    candidate_id: int | None = None
    """Unique identifier for the candidate associated with the offer"""
    created_at: str | None = None
    """Timestamp indicating when the offer was created"""
    custom_fields: dict[str, Any] | None = None
    """Additional custom fields related to the offer"""
    id: int | None = None
    """Unique identifier for the offer"""
    job_id: int | None = None
    """Unique identifier for the job associated with the offer"""
    keyed_custom_fields: dict[str, Any] | None = None
    """Keyed custom fields associated with the offer"""
    opening: dict[str, Any] | None = None
    """Details about the job opening"""
    resolved_at: str | None = None
    """Timestamp indicating when the offer was resolved"""
    sent_at: str | None = None
    """Timestamp indicating when the offer was sent"""
    starts_at: str | None = None
    """Timestamp indicating when the offer starts"""
    status: str | None = None
    """Status of the offer"""
    updated_at: str | None = None
    """Timestamp indicating when the offer was last updated"""
    version: int | None = None
    """Version of the offer data"""


class OfficesSearchData(BaseModel):
    """Search result data for offices entity."""
    model_config = ConfigDict(extra="allow")

    child_ids: list[Any] | None = None
    """IDs of child offices associated with this office"""
    child_office_external_ids: list[Any] | None = None
    """External IDs of child offices associated with this office"""
    external_id: str | None = None
    """Unique identifier for this office in the external system"""
    id: int | None = None
    """Unique identifier for this office in the API system"""
    location: dict[str, Any] | None = None
    """Location details of this office"""
    name: str | None = None
    """Name of the office"""
    parent_id: int | None = None
    """ID of the parent office, if this office is a branch office"""
    parent_office_external_id: str | None = None
    """External ID of the parent office in the external system"""
    primary_contact_user_id: int | None = None
    """User ID of the primary contact person for this office"""


class SourcesSearchData(BaseModel):
    """Search result data for sources entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """The unique identifier for the source."""
    name: str | None = None
    """The name of the source."""
    type: dict[str, Any] | None = None
    """Type of the data source"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """The date and time when the user account was created."""
    departments: list[Any] | None = None
    """List of departments associated with users"""
    disabled: bool | None = None
    """Indicates whether the user account is disabled."""
    emails: list[Any] | None = None
    """Email addresses of the users"""
    employee_id: str | None = None
    """Employee identifier for the user."""
    first_name: str | None = None
    """The first name of the user."""
    id: int | None = None
    """Unique identifier for the user."""
    last_name: str | None = None
    """The last name of the user."""
    linked_candidate_ids: list[Any] | None = None
    """IDs of candidates linked to the user."""
    name: str | None = None
    """The full name of the user."""
    offices: list[Any] | None = None
    """List of office locations where users are based"""
    primary_email_address: str | None = None
    """The primary email address of the user."""
    site_admin: bool | None = None
    """Indicates whether the user is a site administrator."""
    updated_at: str | None = None
    """The date and time when the user account was last updated."""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchHit(BaseModel, Generic[D]):
    """A single search result with typed data."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the record."""
    score: float | None = None
    """Relevance score for the match."""
    data: D
    """The matched record data."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed hits."""
    model_config = ConfigDict(extra="allow")

    hits: list[AirbyteSearchHit[D]] = Field(default_factory=list)
    """List of matching records."""
    next_cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

ApplicationsSearchResult = AirbyteSearchResult[ApplicationsSearchData]
"""Search result type for applications entity."""

CandidatesSearchResult = AirbyteSearchResult[CandidatesSearchData]
"""Search result type for candidates entity."""

DepartmentsSearchResult = AirbyteSearchResult[DepartmentsSearchData]
"""Search result type for departments entity."""

JobPostsSearchResult = AirbyteSearchResult[JobPostsSearchData]
"""Search result type for job_posts entity."""

JobsSearchResult = AirbyteSearchResult[JobsSearchData]
"""Search result type for jobs entity."""

OffersSearchResult = AirbyteSearchResult[OffersSearchData]
"""Search result type for offers entity."""

OfficesSearchResult = AirbyteSearchResult[OfficesSearchData]
"""Search result type for offices entity."""

SourcesSearchResult = AirbyteSearchResult[SourcesSearchData]
"""Search result type for sources entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CandidatesListResult = GreenhouseExecuteResult[list[Candidate]]
"""Result type for candidates.list operation."""

ApplicationsListResult = GreenhouseExecuteResult[list[Application]]
"""Result type for applications.list operation."""

JobsListResult = GreenhouseExecuteResult[list[Job]]
"""Result type for jobs.list operation."""

OffersListResult = GreenhouseExecuteResult[list[Offer]]
"""Result type for offers.list operation."""

UsersListResult = GreenhouseExecuteResult[list[User]]
"""Result type for users.list operation."""

DepartmentsListResult = GreenhouseExecuteResult[list[Department]]
"""Result type for departments.list operation."""

OfficesListResult = GreenhouseExecuteResult[list[Office]]
"""Result type for offices.list operation."""

JobPostsListResult = GreenhouseExecuteResult[list[JobPost]]
"""Result type for job_posts.list operation."""

SourcesListResult = GreenhouseExecuteResult[list[Source]]
"""Result type for sources.list operation."""

ScheduledInterviewsListResult = GreenhouseExecuteResult[list[ScheduledInterview]]
"""Result type for scheduled_interviews.list operation."""

