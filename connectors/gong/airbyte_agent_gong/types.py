"""
Type definitions for gong connector.
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

class CallsExtensiveListParamsFilter(TypedDict):
    """Nested schema for CallsExtensiveListParams.filter"""
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    callIds: NotRequired[list[str]]
    workspaceId: NotRequired[str]

class CallsExtensiveListParamsContentselectorExposedfieldsCollaboration(TypedDict):
    """Nested schema for CallsExtensiveListParamsContentselectorExposedfields.collaboration"""
    publicComments: NotRequired[bool]

class CallsExtensiveListParamsContentselectorExposedfieldsContent(TypedDict):
    """Nested schema for CallsExtensiveListParamsContentselectorExposedfields.content"""
    pointsOfInterest: NotRequired[bool]
    structure: NotRequired[bool]
    topics: NotRequired[bool]
    trackers: NotRequired[bool]
    trackerOccurrences: NotRequired[bool]
    brief: NotRequired[bool]
    outline: NotRequired[bool]
    highlights: NotRequired[bool]
    callOutcome: NotRequired[bool]
    keyPoints: NotRequired[bool]

class CallsExtensiveListParamsContentselectorExposedfieldsInteraction(TypedDict):
    """Nested schema for CallsExtensiveListParamsContentselectorExposedfields.interaction"""
    personInteractionStats: NotRequired[bool]
    questions: NotRequired[bool]
    speakers: NotRequired[bool]
    video: NotRequired[bool]

class CallsExtensiveListParamsContentselectorExposedfields(TypedDict):
    """Specify which fields to include in the response"""
    collaboration: NotRequired[CallsExtensiveListParamsContentselectorExposedfieldsCollaboration]
    content: NotRequired[CallsExtensiveListParamsContentselectorExposedfieldsContent]
    interaction: NotRequired[CallsExtensiveListParamsContentselectorExposedfieldsInteraction]
    media: NotRequired[bool]
    parties: NotRequired[bool]

class CallsExtensiveListParamsContentselector(TypedDict):
    """Select which content to include in the response"""
    context: NotRequired[str]
    contextTiming: NotRequired[list[str]]
    exposedFields: NotRequired[CallsExtensiveListParamsContentselectorExposedfields]

class CallAudioDownloadParamsFilter(TypedDict):
    """Nested schema for CallAudioDownloadParams.filter"""
    callIds: NotRequired[list[str]]

class CallAudioDownloadParamsContentselectorExposedfields(TypedDict):
    """Nested schema for CallAudioDownloadParamsContentselector.exposedFields"""
    media: NotRequired[bool]

class CallAudioDownloadParamsContentselector(TypedDict):
    """Nested schema for CallAudioDownloadParams.contentSelector"""
    exposedFields: NotRequired[CallAudioDownloadParamsContentselectorExposedfields]

class CallVideoDownloadParamsFilter(TypedDict):
    """Nested schema for CallVideoDownloadParams.filter"""
    callIds: NotRequired[list[str]]

class CallVideoDownloadParamsContentselectorExposedfields(TypedDict):
    """Nested schema for CallVideoDownloadParamsContentselector.exposedFields"""
    media: NotRequired[bool]

class CallVideoDownloadParamsContentselector(TypedDict):
    """Nested schema for CallVideoDownloadParams.contentSelector"""
    exposedFields: NotRequired[CallVideoDownloadParamsContentselectorExposedfields]

class CallTranscriptsListParamsFilter(TypedDict):
    """Nested schema for CallTranscriptsListParams.filter"""
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    callIds: NotRequired[list[str]]

class StatsActivityAggregateListParamsFilter(TypedDict):
    """Nested schema for StatsActivityAggregateListParams.filter"""
    fromDate: NotRequired[str]
    toDate: NotRequired[str]
    userIds: NotRequired[list[str]]

class StatsActivityDayByDayListParamsFilter(TypedDict):
    """Nested schema for StatsActivityDayByDayListParams.filter"""
    fromDate: NotRequired[str]
    toDate: NotRequired[str]
    userIds: NotRequired[list[str]]

class StatsInteractionListParamsFilter(TypedDict):
    """Nested schema for StatsInteractionListParams.filter"""
    fromDate: NotRequired[str]
    toDate: NotRequired[str]
    userIds: NotRequired[list[str]]

class StatsActivityScorecardsListParamsFilter(TypedDict):
    """Nested schema for StatsActivityScorecardsListParams.filter"""
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    scorecardIds: NotRequired[list[str]]
    reviewedUserIds: NotRequired[list[str]]
    reviewerUserIds: NotRequired[list[str]]
    callIds: NotRequired[list[str]]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    from_date_time: NotRequired[str]
    to_date_time: NotRequired[str]
    cursor: NotRequired[str]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    id: str

class CallsExtensiveListParams(TypedDict):
    """Parameters for calls_extensive.list operation"""
    filter: CallsExtensiveListParamsFilter
    content_selector: NotRequired[CallsExtensiveListParamsContentselector]
    cursor: NotRequired[str]

class CallAudioDownloadParams(TypedDict):
    """Parameters for call_audio.download operation"""
    filter: NotRequired[CallAudioDownloadParamsFilter]
    content_selector: NotRequired[CallAudioDownloadParamsContentselector]
    range_header: NotRequired[str]

class CallVideoDownloadParams(TypedDict):
    """Parameters for call_video.download operation"""
    filter: NotRequired[CallVideoDownloadParamsFilter]
    content_selector: NotRequired[CallVideoDownloadParamsContentselector]
    range_header: NotRequired[str]

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    pass

class CallTranscriptsListParams(TypedDict):
    """Parameters for call_transcripts.list operation"""
    filter: NotRequired[CallTranscriptsListParamsFilter]
    cursor: NotRequired[str]

class StatsActivityAggregateListParams(TypedDict):
    """Parameters for stats_activity_aggregate.list operation"""
    filter: NotRequired[StatsActivityAggregateListParamsFilter]

class StatsActivityDayByDayListParams(TypedDict):
    """Parameters for stats_activity_day_by_day.list operation"""
    filter: NotRequired[StatsActivityDayByDayListParamsFilter]

class StatsInteractionListParams(TypedDict):
    """Parameters for stats_interaction.list operation"""
    filter: NotRequired[StatsInteractionListParamsFilter]

class SettingsScorecardsListParams(TypedDict):
    """Parameters for settings_scorecards.list operation"""
    workspace_id: NotRequired[str]

class SettingsTrackersListParams(TypedDict):
    """Parameters for settings_trackers.list operation"""
    workspace_id: NotRequired[str]

class LibraryFoldersListParams(TypedDict):
    """Parameters for library_folders.list operation"""
    workspace_id: str

class LibraryFolderContentListParams(TypedDict):
    """Parameters for library_folder_content.list operation"""
    folder_id: str
    cursor: NotRequired[str]

class CoachingListParams(TypedDict):
    """Parameters for coaching.list operation"""
    workspace_id: str
    manager_id: str
    from_: str
    to: str

class StatsActivityScorecardsListParams(TypedDict):
    """Parameters for stats_activity_scorecards.list operation"""
    filter: NotRequired[StatsActivityScorecardsListParamsFilter]
    cursor: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    active: bool | None
    """Indicates if the user is currently active or not"""
    created: str | None
    """The timestamp denoting when the user account was created"""
    email_address: str | None
    """The primary email address associated with the user"""
    email_aliases: list[Any] | None
    """Additional email addresses that can be used to reach the user"""
    extension: str | None
    """The phone extension number for the user"""
    first_name: str | None
    """The first name of the user"""
    id: str | None
    """Unique identifier for the user"""
    last_name: str | None
    """The last name of the user"""
    manager_id: str | None
    """The ID of the user's manager"""
    meeting_consent_page_url: str | None
    """URL for the consent page related to meetings"""
    personal_meeting_urls: list[Any] | None
    """URLs for personal meeting rooms assigned to the user"""
    phone_number: str | None
    """The phone number associated with the user"""
    settings: dict[str, Any] | None
    """User-specific settings and configurations"""
    spoken_languages: list[Any] | None
    """Languages spoken by the user"""
    title: str | None
    """The job title or position of the user"""
    trusted_email_address: str | None
    """An email address that is considered trusted for the user"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Indicates if the user is currently active or not"""
    created: list[str]
    """The timestamp denoting when the user account was created"""
    email_address: list[str]
    """The primary email address associated with the user"""
    email_aliases: list[list[Any]]
    """Additional email addresses that can be used to reach the user"""
    extension: list[str]
    """The phone extension number for the user"""
    first_name: list[str]
    """The first name of the user"""
    id: list[str]
    """Unique identifier for the user"""
    last_name: list[str]
    """The last name of the user"""
    manager_id: list[str]
    """The ID of the user's manager"""
    meeting_consent_page_url: list[str]
    """URL for the consent page related to meetings"""
    personal_meeting_urls: list[list[Any]]
    """URLs for personal meeting rooms assigned to the user"""
    phone_number: list[str]
    """The phone number associated with the user"""
    settings: list[dict[str, Any]]
    """User-specific settings and configurations"""
    spoken_languages: list[list[Any]]
    """Languages spoken by the user"""
    title: list[str]
    """The job title or position of the user"""
    trusted_email_address: list[str]
    """An email address that is considered trusted for the user"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Indicates if the user is currently active or not"""
    created: Any
    """The timestamp denoting when the user account was created"""
    email_address: Any
    """The primary email address associated with the user"""
    email_aliases: Any
    """Additional email addresses that can be used to reach the user"""
    extension: Any
    """The phone extension number for the user"""
    first_name: Any
    """The first name of the user"""
    id: Any
    """Unique identifier for the user"""
    last_name: Any
    """The last name of the user"""
    manager_id: Any
    """The ID of the user's manager"""
    meeting_consent_page_url: Any
    """URL for the consent page related to meetings"""
    personal_meeting_urls: Any
    """URLs for personal meeting rooms assigned to the user"""
    phone_number: Any
    """The phone number associated with the user"""
    settings: Any
    """User-specific settings and configurations"""
    spoken_languages: Any
    """Languages spoken by the user"""
    title: Any
    """The job title or position of the user"""
    trusted_email_address: Any
    """An email address that is considered trusted for the user"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Indicates if the user is currently active or not"""
    created: str
    """The timestamp denoting when the user account was created"""
    email_address: str
    """The primary email address associated with the user"""
    email_aliases: str
    """Additional email addresses that can be used to reach the user"""
    extension: str
    """The phone extension number for the user"""
    first_name: str
    """The first name of the user"""
    id: str
    """Unique identifier for the user"""
    last_name: str
    """The last name of the user"""
    manager_id: str
    """The ID of the user's manager"""
    meeting_consent_page_url: str
    """URL for the consent page related to meetings"""
    personal_meeting_urls: str
    """URLs for personal meeting rooms assigned to the user"""
    phone_number: str
    """The phone number associated with the user"""
    settings: str
    """User-specific settings and configurations"""
    spoken_languages: str
    """Languages spoken by the user"""
    title: str
    """The job title or position of the user"""
    trusted_email_address: str
    """An email address that is considered trusted for the user"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    active: AirbyteSortOrder
    """Indicates if the user is currently active or not"""
    created: AirbyteSortOrder
    """The timestamp denoting when the user account was created"""
    email_address: AirbyteSortOrder
    """The primary email address associated with the user"""
    email_aliases: AirbyteSortOrder
    """Additional email addresses that can be used to reach the user"""
    extension: AirbyteSortOrder
    """The phone extension number for the user"""
    first_name: AirbyteSortOrder
    """The first name of the user"""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    last_name: AirbyteSortOrder
    """The last name of the user"""
    manager_id: AirbyteSortOrder
    """The ID of the user's manager"""
    meeting_consent_page_url: AirbyteSortOrder
    """URL for the consent page related to meetings"""
    personal_meeting_urls: AirbyteSortOrder
    """URLs for personal meeting rooms assigned to the user"""
    phone_number: AirbyteSortOrder
    """The phone number associated with the user"""
    settings: AirbyteSortOrder
    """User-specific settings and configurations"""
    spoken_languages: AirbyteSortOrder
    """Languages spoken by the user"""
    title: AirbyteSortOrder
    """The job title or position of the user"""
    trusted_email_address: AirbyteSortOrder
    """An email address that is considered trusted for the user"""


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


# ===== CALLS SEARCH TYPES =====

class CallsSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls search queries."""
    calendar_event_id: str | None
    """Unique identifier for the calendar event associated with the call."""
    client_unique_id: str | None
    """Unique identifier for the client related to the call."""
    custom_data: str | None
    """Custom data associated with the call."""
    direction: str | None
    """Direction of the call (inbound/outbound)."""
    duration: int | None
    """Duration of the call in seconds."""
    id: str | None
    """Unique identifier for the call."""
    is_private: bool | None
    """Indicates if the call is private or not."""
    language: str | None
    """Language used in the call."""
    media: str | None
    """Media type used for communication (voice, video, etc.)."""
    meeting_url: str | None
    """URL for accessing the meeting associated with the call."""
    primary_user_id: str | None
    """Unique identifier for the primary user involved in the call."""
    purpose: str | None
    """Purpose or topic of the call."""
    scheduled: str | None
    """Scheduled date and time of the call."""
    scope: str | None
    """Scope or extent of the call."""
    sdr_disposition: str | None
    """Disposition set by the sales development representative."""
    started: str | None
    """Start date and time of the call."""
    system: str | None
    """System information related to the call."""
    title: str | None
    """Title or headline of the call."""
    url: str | None
    """URL associated with the call."""
    workspace_id: str | None
    """Identifier for the workspace to which the call belongs."""


class CallsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    calendar_event_id: list[str]
    """Unique identifier for the calendar event associated with the call."""
    client_unique_id: list[str]
    """Unique identifier for the client related to the call."""
    custom_data: list[str]
    """Custom data associated with the call."""
    direction: list[str]
    """Direction of the call (inbound/outbound)."""
    duration: list[int]
    """Duration of the call in seconds."""
    id: list[str]
    """Unique identifier for the call."""
    is_private: list[bool]
    """Indicates if the call is private or not."""
    language: list[str]
    """Language used in the call."""
    media: list[str]
    """Media type used for communication (voice, video, etc.)."""
    meeting_url: list[str]
    """URL for accessing the meeting associated with the call."""
    primary_user_id: list[str]
    """Unique identifier for the primary user involved in the call."""
    purpose: list[str]
    """Purpose or topic of the call."""
    scheduled: list[str]
    """Scheduled date and time of the call."""
    scope: list[str]
    """Scope or extent of the call."""
    sdr_disposition: list[str]
    """Disposition set by the sales development representative."""
    started: list[str]
    """Start date and time of the call."""
    system: list[str]
    """System information related to the call."""
    title: list[str]
    """Title or headline of the call."""
    url: list[str]
    """URL associated with the call."""
    workspace_id: list[str]
    """Identifier for the workspace to which the call belongs."""


class CallsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    calendar_event_id: Any
    """Unique identifier for the calendar event associated with the call."""
    client_unique_id: Any
    """Unique identifier for the client related to the call."""
    custom_data: Any
    """Custom data associated with the call."""
    direction: Any
    """Direction of the call (inbound/outbound)."""
    duration: Any
    """Duration of the call in seconds."""
    id: Any
    """Unique identifier for the call."""
    is_private: Any
    """Indicates if the call is private or not."""
    language: Any
    """Language used in the call."""
    media: Any
    """Media type used for communication (voice, video, etc.)."""
    meeting_url: Any
    """URL for accessing the meeting associated with the call."""
    primary_user_id: Any
    """Unique identifier for the primary user involved in the call."""
    purpose: Any
    """Purpose or topic of the call."""
    scheduled: Any
    """Scheduled date and time of the call."""
    scope: Any
    """Scope or extent of the call."""
    sdr_disposition: Any
    """Disposition set by the sales development representative."""
    started: Any
    """Start date and time of the call."""
    system: Any
    """System information related to the call."""
    title: Any
    """Title or headline of the call."""
    url: Any
    """URL associated with the call."""
    workspace_id: Any
    """Identifier for the workspace to which the call belongs."""


class CallsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    calendar_event_id: str
    """Unique identifier for the calendar event associated with the call."""
    client_unique_id: str
    """Unique identifier for the client related to the call."""
    custom_data: str
    """Custom data associated with the call."""
    direction: str
    """Direction of the call (inbound/outbound)."""
    duration: str
    """Duration of the call in seconds."""
    id: str
    """Unique identifier for the call."""
    is_private: str
    """Indicates if the call is private or not."""
    language: str
    """Language used in the call."""
    media: str
    """Media type used for communication (voice, video, etc.)."""
    meeting_url: str
    """URL for accessing the meeting associated with the call."""
    primary_user_id: str
    """Unique identifier for the primary user involved in the call."""
    purpose: str
    """Purpose or topic of the call."""
    scheduled: str
    """Scheduled date and time of the call."""
    scope: str
    """Scope or extent of the call."""
    sdr_disposition: str
    """Disposition set by the sales development representative."""
    started: str
    """Start date and time of the call."""
    system: str
    """System information related to the call."""
    title: str
    """Title or headline of the call."""
    url: str
    """URL associated with the call."""
    workspace_id: str
    """Identifier for the workspace to which the call belongs."""


class CallsSortFilter(TypedDict, total=False):
    """Available fields for sorting calls search results."""
    calendar_event_id: AirbyteSortOrder
    """Unique identifier for the calendar event associated with the call."""
    client_unique_id: AirbyteSortOrder
    """Unique identifier for the client related to the call."""
    custom_data: AirbyteSortOrder
    """Custom data associated with the call."""
    direction: AirbyteSortOrder
    """Direction of the call (inbound/outbound)."""
    duration: AirbyteSortOrder
    """Duration of the call in seconds."""
    id: AirbyteSortOrder
    """Unique identifier for the call."""
    is_private: AirbyteSortOrder
    """Indicates if the call is private or not."""
    language: AirbyteSortOrder
    """Language used in the call."""
    media: AirbyteSortOrder
    """Media type used for communication (voice, video, etc.)."""
    meeting_url: AirbyteSortOrder
    """URL for accessing the meeting associated with the call."""
    primary_user_id: AirbyteSortOrder
    """Unique identifier for the primary user involved in the call."""
    purpose: AirbyteSortOrder
    """Purpose or topic of the call."""
    scheduled: AirbyteSortOrder
    """Scheduled date and time of the call."""
    scope: AirbyteSortOrder
    """Scope or extent of the call."""
    sdr_disposition: AirbyteSortOrder
    """Disposition set by the sales development representative."""
    started: AirbyteSortOrder
    """Start date and time of the call."""
    system: AirbyteSortOrder
    """System information related to the call."""
    title: AirbyteSortOrder
    """Title or headline of the call."""
    url: AirbyteSortOrder
    """URL associated with the call."""
    workspace_id: AirbyteSortOrder
    """Identifier for the workspace to which the call belongs."""


# Entity-specific condition types for calls
class CallsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallsSearchFilter


class CallsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallsSearchFilter


class CallsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallsSearchFilter


class CallsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallsSearchFilter


class CallsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallsSearchFilter


class CallsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallsSearchFilter


class CallsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CallsStringFilter


class CallsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallsStringFilter


class CallsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallsStringFilter


class CallsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CallsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallsInCondition = TypedDict("CallsInCondition", {"in": CallsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallsNotCondition = TypedDict("CallsNotCondition", {"not": "CallsCondition"}, total=False)
"""Negates the nested condition."""

CallsAndCondition = TypedDict("CallsAndCondition", {"and": "list[CallsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallsOrCondition = TypedDict("CallsOrCondition", {"or": "list[CallsCondition]"}, total=False)
"""True if any nested condition is true."""

CallsAnyCondition = TypedDict("CallsAnyCondition", {"any": CallsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all calls condition types
CallsCondition = (
    CallsEqCondition
    | CallsNeqCondition
    | CallsGtCondition
    | CallsGteCondition
    | CallsLtCondition
    | CallsLteCondition
    | CallsInCondition
    | CallsLikeCondition
    | CallsFuzzyCondition
    | CallsKeywordCondition
    | CallsContainsCondition
    | CallsNotCondition
    | CallsAndCondition
    | CallsOrCondition
    | CallsAnyCondition
)


class CallsSearchQuery(TypedDict, total=False):
    """Search query for calls entity."""
    filter: CallsCondition
    sort: list[CallsSortFilter]


# ===== CALLS_EXTENSIVE SEARCH TYPES =====

class CallsExtensiveSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls_extensive search queries."""
    id: int | None
    """Unique identifier for the call (from metaData.id)."""
    startdatetime: str | None
    """Datetime for extensive calls."""
    collaboration: dict[str, Any] | None
    """Collaboration information added to the call"""
    content: dict[str, Any] | None
    """Analysis of the interaction content."""
    context: dict[str, Any] | None
    """A list of the agenda of each part of the call."""
    interaction: dict[str, Any] | None
    """Metrics collected around the interaction during the call."""
    media: dict[str, Any] | None
    """The media urls of the call."""
    meta_data: dict[str, Any] | None
    """call's metadata."""
    parties: list[Any] | None
    """A list of the call's participants"""


class CallsExtensiveInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the call (from metaData.id)."""
    startdatetime: list[str]
    """Datetime for extensive calls."""
    collaboration: list[dict[str, Any]]
    """Collaboration information added to the call"""
    content: list[dict[str, Any]]
    """Analysis of the interaction content."""
    context: list[dict[str, Any]]
    """A list of the agenda of each part of the call."""
    interaction: list[dict[str, Any]]
    """Metrics collected around the interaction during the call."""
    media: list[dict[str, Any]]
    """The media urls of the call."""
    meta_data: list[dict[str, Any]]
    """call's metadata."""
    parties: list[list[Any]]
    """A list of the call's participants"""


class CallsExtensiveAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the call (from metaData.id)."""
    startdatetime: Any
    """Datetime for extensive calls."""
    collaboration: Any
    """Collaboration information added to the call"""
    content: Any
    """Analysis of the interaction content."""
    context: Any
    """A list of the agenda of each part of the call."""
    interaction: Any
    """Metrics collected around the interaction during the call."""
    media: Any
    """The media urls of the call."""
    meta_data: Any
    """call's metadata."""
    parties: Any
    """A list of the call's participants"""


class CallsExtensiveStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the call (from metaData.id)."""
    startdatetime: str
    """Datetime for extensive calls."""
    collaboration: str
    """Collaboration information added to the call"""
    content: str
    """Analysis of the interaction content."""
    context: str
    """A list of the agenda of each part of the call."""
    interaction: str
    """Metrics collected around the interaction during the call."""
    media: str
    """The media urls of the call."""
    meta_data: str
    """call's metadata."""
    parties: str
    """A list of the call's participants"""


class CallsExtensiveSortFilter(TypedDict, total=False):
    """Available fields for sorting calls_extensive search results."""
    id: AirbyteSortOrder
    """Unique identifier for the call (from metaData.id)."""
    startdatetime: AirbyteSortOrder
    """Datetime for extensive calls."""
    collaboration: AirbyteSortOrder
    """Collaboration information added to the call"""
    content: AirbyteSortOrder
    """Analysis of the interaction content."""
    context: AirbyteSortOrder
    """A list of the agenda of each part of the call."""
    interaction: AirbyteSortOrder
    """Metrics collected around the interaction during the call."""
    media: AirbyteSortOrder
    """The media urls of the call."""
    meta_data: AirbyteSortOrder
    """call's metadata."""
    parties: AirbyteSortOrder
    """A list of the call's participants"""


# Entity-specific condition types for calls_extensive
class CallsExtensiveEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallsExtensiveSearchFilter


class CallsExtensiveNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallsExtensiveSearchFilter


class CallsExtensiveGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallsExtensiveSearchFilter


class CallsExtensiveGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallsExtensiveSearchFilter


class CallsExtensiveLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallsExtensiveSearchFilter


class CallsExtensiveLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallsExtensiveSearchFilter


class CallsExtensiveLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CallsExtensiveStringFilter


class CallsExtensiveFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallsExtensiveStringFilter


class CallsExtensiveKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallsExtensiveStringFilter


class CallsExtensiveContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CallsExtensiveAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallsExtensiveInCondition = TypedDict("CallsExtensiveInCondition", {"in": CallsExtensiveInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallsExtensiveNotCondition = TypedDict("CallsExtensiveNotCondition", {"not": "CallsExtensiveCondition"}, total=False)
"""Negates the nested condition."""

CallsExtensiveAndCondition = TypedDict("CallsExtensiveAndCondition", {"and": "list[CallsExtensiveCondition]"}, total=False)
"""True if all nested conditions are true."""

CallsExtensiveOrCondition = TypedDict("CallsExtensiveOrCondition", {"or": "list[CallsExtensiveCondition]"}, total=False)
"""True if any nested condition is true."""

CallsExtensiveAnyCondition = TypedDict("CallsExtensiveAnyCondition", {"any": CallsExtensiveAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all calls_extensive condition types
CallsExtensiveCondition = (
    CallsExtensiveEqCondition
    | CallsExtensiveNeqCondition
    | CallsExtensiveGtCondition
    | CallsExtensiveGteCondition
    | CallsExtensiveLtCondition
    | CallsExtensiveLteCondition
    | CallsExtensiveInCondition
    | CallsExtensiveLikeCondition
    | CallsExtensiveFuzzyCondition
    | CallsExtensiveKeywordCondition
    | CallsExtensiveContainsCondition
    | CallsExtensiveNotCondition
    | CallsExtensiveAndCondition
    | CallsExtensiveOrCondition
    | CallsExtensiveAnyCondition
)


class CallsExtensiveSearchQuery(TypedDict, total=False):
    """Search query for calls_extensive entity."""
    filter: CallsExtensiveCondition
    sort: list[CallsExtensiveSortFilter]


# ===== SETTINGS_SCORECARDS SEARCH TYPES =====

class SettingsScorecardsSearchFilter(TypedDict, total=False):
    """Available fields for filtering settings_scorecards search queries."""
    created: str | None
    """The timestamp when the scorecard was created"""
    enabled: bool | None
    """Indicates if the scorecard is enabled or disabled"""
    questions: list[Any] | None
    """An array of questions related to the scorecard"""
    scorecard_id: str | None
    """The unique identifier of the scorecard"""
    scorecard_name: str | None
    """The name of the scorecard"""
    updated: str | None
    """The timestamp when the scorecard was last updated"""
    updater_user_id: str | None
    """The user ID of the person who last updated the scorecard"""
    workspace_id: str | None
    """The unique identifier of the workspace associated with the scorecard"""


class SettingsScorecardsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created: list[str]
    """The timestamp when the scorecard was created"""
    enabled: list[bool]
    """Indicates if the scorecard is enabled or disabled"""
    questions: list[list[Any]]
    """An array of questions related to the scorecard"""
    scorecard_id: list[str]
    """The unique identifier of the scorecard"""
    scorecard_name: list[str]
    """The name of the scorecard"""
    updated: list[str]
    """The timestamp when the scorecard was last updated"""
    updater_user_id: list[str]
    """The user ID of the person who last updated the scorecard"""
    workspace_id: list[str]
    """The unique identifier of the workspace associated with the scorecard"""


class SettingsScorecardsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created: Any
    """The timestamp when the scorecard was created"""
    enabled: Any
    """Indicates if the scorecard is enabled or disabled"""
    questions: Any
    """An array of questions related to the scorecard"""
    scorecard_id: Any
    """The unique identifier of the scorecard"""
    scorecard_name: Any
    """The name of the scorecard"""
    updated: Any
    """The timestamp when the scorecard was last updated"""
    updater_user_id: Any
    """The user ID of the person who last updated the scorecard"""
    workspace_id: Any
    """The unique identifier of the workspace associated with the scorecard"""


class SettingsScorecardsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created: str
    """The timestamp when the scorecard was created"""
    enabled: str
    """Indicates if the scorecard is enabled or disabled"""
    questions: str
    """An array of questions related to the scorecard"""
    scorecard_id: str
    """The unique identifier of the scorecard"""
    scorecard_name: str
    """The name of the scorecard"""
    updated: str
    """The timestamp when the scorecard was last updated"""
    updater_user_id: str
    """The user ID of the person who last updated the scorecard"""
    workspace_id: str
    """The unique identifier of the workspace associated with the scorecard"""


class SettingsScorecardsSortFilter(TypedDict, total=False):
    """Available fields for sorting settings_scorecards search results."""
    created: AirbyteSortOrder
    """The timestamp when the scorecard was created"""
    enabled: AirbyteSortOrder
    """Indicates if the scorecard is enabled or disabled"""
    questions: AirbyteSortOrder
    """An array of questions related to the scorecard"""
    scorecard_id: AirbyteSortOrder
    """The unique identifier of the scorecard"""
    scorecard_name: AirbyteSortOrder
    """The name of the scorecard"""
    updated: AirbyteSortOrder
    """The timestamp when the scorecard was last updated"""
    updater_user_id: AirbyteSortOrder
    """The user ID of the person who last updated the scorecard"""
    workspace_id: AirbyteSortOrder
    """The unique identifier of the workspace associated with the scorecard"""


# Entity-specific condition types for settings_scorecards
class SettingsScorecardsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SettingsScorecardsSearchFilter


class SettingsScorecardsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SettingsScorecardsSearchFilter


class SettingsScorecardsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SettingsScorecardsSearchFilter


class SettingsScorecardsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SettingsScorecardsSearchFilter


class SettingsScorecardsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SettingsScorecardsSearchFilter


class SettingsScorecardsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SettingsScorecardsSearchFilter


class SettingsScorecardsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SettingsScorecardsStringFilter


class SettingsScorecardsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SettingsScorecardsStringFilter


class SettingsScorecardsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SettingsScorecardsStringFilter


class SettingsScorecardsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SettingsScorecardsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SettingsScorecardsInCondition = TypedDict("SettingsScorecardsInCondition", {"in": SettingsScorecardsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SettingsScorecardsNotCondition = TypedDict("SettingsScorecardsNotCondition", {"not": "SettingsScorecardsCondition"}, total=False)
"""Negates the nested condition."""

SettingsScorecardsAndCondition = TypedDict("SettingsScorecardsAndCondition", {"and": "list[SettingsScorecardsCondition]"}, total=False)
"""True if all nested conditions are true."""

SettingsScorecardsOrCondition = TypedDict("SettingsScorecardsOrCondition", {"or": "list[SettingsScorecardsCondition]"}, total=False)
"""True if any nested condition is true."""

SettingsScorecardsAnyCondition = TypedDict("SettingsScorecardsAnyCondition", {"any": SettingsScorecardsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all settings_scorecards condition types
SettingsScorecardsCondition = (
    SettingsScorecardsEqCondition
    | SettingsScorecardsNeqCondition
    | SettingsScorecardsGtCondition
    | SettingsScorecardsGteCondition
    | SettingsScorecardsLtCondition
    | SettingsScorecardsLteCondition
    | SettingsScorecardsInCondition
    | SettingsScorecardsLikeCondition
    | SettingsScorecardsFuzzyCondition
    | SettingsScorecardsKeywordCondition
    | SettingsScorecardsContainsCondition
    | SettingsScorecardsNotCondition
    | SettingsScorecardsAndCondition
    | SettingsScorecardsOrCondition
    | SettingsScorecardsAnyCondition
)


class SettingsScorecardsSearchQuery(TypedDict, total=False):
    """Search query for settings_scorecards entity."""
    filter: SettingsScorecardsCondition
    sort: list[SettingsScorecardsSortFilter]


# ===== STATS_ACTIVITY_SCORECARDS SEARCH TYPES =====

class StatsActivityScorecardsSearchFilter(TypedDict, total=False):
    """Available fields for filtering stats_activity_scorecards search queries."""
    answered_scorecard_id: str | None
    """Unique identifier for the answered scorecard instance."""
    answers: list[Any] | None
    """Contains the answered questions in the scorecards"""
    call_id: str | None
    """Unique identifier for the call associated with the answered scorecard."""
    call_start_time: str | None
    """Timestamp indicating the start time of the call."""
    review_time: str | None
    """Timestamp indicating when the review of the answered scorecard was completed."""
    reviewed_user_id: str | None
    """Unique identifier for the user whose performance was reviewed."""
    reviewer_user_id: str | None
    """Unique identifier for the user who performed the review."""
    scorecard_id: str | None
    """Unique identifier for the scorecard template used."""
    scorecard_name: str | None
    """Name or title of the scorecard template used."""
    visibility_type: str | None
    """Type indicating the visibility permissions for the answered scorecard."""


class StatsActivityScorecardsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    answered_scorecard_id: list[str]
    """Unique identifier for the answered scorecard instance."""
    answers: list[list[Any]]
    """Contains the answered questions in the scorecards"""
    call_id: list[str]
    """Unique identifier for the call associated with the answered scorecard."""
    call_start_time: list[str]
    """Timestamp indicating the start time of the call."""
    review_time: list[str]
    """Timestamp indicating when the review of the answered scorecard was completed."""
    reviewed_user_id: list[str]
    """Unique identifier for the user whose performance was reviewed."""
    reviewer_user_id: list[str]
    """Unique identifier for the user who performed the review."""
    scorecard_id: list[str]
    """Unique identifier for the scorecard template used."""
    scorecard_name: list[str]
    """Name or title of the scorecard template used."""
    visibility_type: list[str]
    """Type indicating the visibility permissions for the answered scorecard."""


class StatsActivityScorecardsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    answered_scorecard_id: Any
    """Unique identifier for the answered scorecard instance."""
    answers: Any
    """Contains the answered questions in the scorecards"""
    call_id: Any
    """Unique identifier for the call associated with the answered scorecard."""
    call_start_time: Any
    """Timestamp indicating the start time of the call."""
    review_time: Any
    """Timestamp indicating when the review of the answered scorecard was completed."""
    reviewed_user_id: Any
    """Unique identifier for the user whose performance was reviewed."""
    reviewer_user_id: Any
    """Unique identifier for the user who performed the review."""
    scorecard_id: Any
    """Unique identifier for the scorecard template used."""
    scorecard_name: Any
    """Name or title of the scorecard template used."""
    visibility_type: Any
    """Type indicating the visibility permissions for the answered scorecard."""


class StatsActivityScorecardsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    answered_scorecard_id: str
    """Unique identifier for the answered scorecard instance."""
    answers: str
    """Contains the answered questions in the scorecards"""
    call_id: str
    """Unique identifier for the call associated with the answered scorecard."""
    call_start_time: str
    """Timestamp indicating the start time of the call."""
    review_time: str
    """Timestamp indicating when the review of the answered scorecard was completed."""
    reviewed_user_id: str
    """Unique identifier for the user whose performance was reviewed."""
    reviewer_user_id: str
    """Unique identifier for the user who performed the review."""
    scorecard_id: str
    """Unique identifier for the scorecard template used."""
    scorecard_name: str
    """Name or title of the scorecard template used."""
    visibility_type: str
    """Type indicating the visibility permissions for the answered scorecard."""


class StatsActivityScorecardsSortFilter(TypedDict, total=False):
    """Available fields for sorting stats_activity_scorecards search results."""
    answered_scorecard_id: AirbyteSortOrder
    """Unique identifier for the answered scorecard instance."""
    answers: AirbyteSortOrder
    """Contains the answered questions in the scorecards"""
    call_id: AirbyteSortOrder
    """Unique identifier for the call associated with the answered scorecard."""
    call_start_time: AirbyteSortOrder
    """Timestamp indicating the start time of the call."""
    review_time: AirbyteSortOrder
    """Timestamp indicating when the review of the answered scorecard was completed."""
    reviewed_user_id: AirbyteSortOrder
    """Unique identifier for the user whose performance was reviewed."""
    reviewer_user_id: AirbyteSortOrder
    """Unique identifier for the user who performed the review."""
    scorecard_id: AirbyteSortOrder
    """Unique identifier for the scorecard template used."""
    scorecard_name: AirbyteSortOrder
    """Name or title of the scorecard template used."""
    visibility_type: AirbyteSortOrder
    """Type indicating the visibility permissions for the answered scorecard."""


# Entity-specific condition types for stats_activity_scorecards
class StatsActivityScorecardsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: StatsActivityScorecardsSearchFilter


class StatsActivityScorecardsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: StatsActivityScorecardsSearchFilter


class StatsActivityScorecardsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: StatsActivityScorecardsSearchFilter


class StatsActivityScorecardsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: StatsActivityScorecardsSearchFilter


class StatsActivityScorecardsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: StatsActivityScorecardsSearchFilter


class StatsActivityScorecardsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: StatsActivityScorecardsSearchFilter


class StatsActivityScorecardsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: StatsActivityScorecardsStringFilter


class StatsActivityScorecardsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: StatsActivityScorecardsStringFilter


class StatsActivityScorecardsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: StatsActivityScorecardsStringFilter


class StatsActivityScorecardsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: StatsActivityScorecardsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
StatsActivityScorecardsInCondition = TypedDict("StatsActivityScorecardsInCondition", {"in": StatsActivityScorecardsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

StatsActivityScorecardsNotCondition = TypedDict("StatsActivityScorecardsNotCondition", {"not": "StatsActivityScorecardsCondition"}, total=False)
"""Negates the nested condition."""

StatsActivityScorecardsAndCondition = TypedDict("StatsActivityScorecardsAndCondition", {"and": "list[StatsActivityScorecardsCondition]"}, total=False)
"""True if all nested conditions are true."""

StatsActivityScorecardsOrCondition = TypedDict("StatsActivityScorecardsOrCondition", {"or": "list[StatsActivityScorecardsCondition]"}, total=False)
"""True if any nested condition is true."""

StatsActivityScorecardsAnyCondition = TypedDict("StatsActivityScorecardsAnyCondition", {"any": StatsActivityScorecardsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all stats_activity_scorecards condition types
StatsActivityScorecardsCondition = (
    StatsActivityScorecardsEqCondition
    | StatsActivityScorecardsNeqCondition
    | StatsActivityScorecardsGtCondition
    | StatsActivityScorecardsGteCondition
    | StatsActivityScorecardsLtCondition
    | StatsActivityScorecardsLteCondition
    | StatsActivityScorecardsInCondition
    | StatsActivityScorecardsLikeCondition
    | StatsActivityScorecardsFuzzyCondition
    | StatsActivityScorecardsKeywordCondition
    | StatsActivityScorecardsContainsCondition
    | StatsActivityScorecardsNotCondition
    | StatsActivityScorecardsAndCondition
    | StatsActivityScorecardsOrCondition
    | StatsActivityScorecardsAnyCondition
)


class StatsActivityScorecardsSearchQuery(TypedDict, total=False):
    """Search query for stats_activity_scorecards entity."""
    filter: StatsActivityScorecardsCondition
    sort: list[StatsActivityScorecardsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
