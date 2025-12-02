"""
Auto-generated type definitions for gong connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

# ===== AUTH CONFIG TYPE DEFINITIONS =====

class GongAuthConfig(TypedDict):
    """Access Key Authentication"""
    access_key: str  # Your Gong API Access Key
    access_key_secret: str  # Your Gong API Access Key Secret

# ===== RESPONSE TYPE DEFINITIONS =====

class PaginationRecords(TypedDict):
    """Pagination metadata"""
    totalRecords: NotRequired[int]
    currentPageSize: NotRequired[int]
    currentPageNumber: NotRequired[int]
    cursor: NotRequired[str]

class User(TypedDict):
    """User object"""
    id: NotRequired[str]
    emailAddress: NotRequired[str]
    firstName: NotRequired[str]
    lastName: NotRequired[str]
    active: NotRequired[bool]
    createdDate: NotRequired[str]

class UsersResponse(TypedDict):
    """Response containing list of users"""
    users: NotRequired[list[User]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class UserResponse(TypedDict):
    """Response containing single user"""
    user: NotRequired[User]
    requestId: NotRequired[str]

class Call(TypedDict):
    """Call object"""
    id: NotRequired[str]
    url: NotRequired[str]
    title: NotRequired[str]
    started: NotRequired[str]
    duration: NotRequired[int]
    primaryUserId: NotRequired[str]
    direction: NotRequired[str]
    system: NotRequired[str]
    scope: NotRequired[str]
    language: NotRequired[str]

class CallsResponse(TypedDict):
    """Response containing list of calls"""
    calls: NotRequired[list[Call]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class CallResponse(TypedDict):
    """Response containing single call"""
    call: NotRequired[Call]
    requestId: NotRequired[str]

class Workspace(TypedDict):
    """Workspace object"""
    workspaceId: NotRequired[str]
    name: NotRequired[str]

class WorkspacesResponse(TypedDict):
    """Response containing list of workspaces"""
    workspaces: NotRequired[list[Workspace]]
    requestId: NotRequired[str]

class CallTranscript(TypedDict):
    """Call transcript object"""
    callId: NotRequired[str]
    transcript: NotRequired[list[dict[str, Any]]]

class TranscriptsResponse(TypedDict):
    """Response containing call transcripts"""
    callTranscripts: NotRequired[list[CallTranscript]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class ExtensiveCall(TypedDict):
    """Detailed call object with extended information"""
    metaData: NotRequired[dict[str, Any]]
    parties: NotRequired[list[dict[str, Any]]]
    interaction: NotRequired[dict[str, Any]]
    collaboration: NotRequired[dict[str, Any]]
    content: NotRequired[dict[str, Any]]
    media: NotRequired[dict[str, Any]]

class ExtensiveCallsResponse(TypedDict):
    """Response containing detailed call data"""
    calls: NotRequired[list[ExtensiveCall]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class UserAggregateActivityStats(TypedDict):
    """Aggregated activity statistics for a user"""
    callsAsHost: NotRequired[int]
    callsGaveFeedback: NotRequired[int]
    callsRequestedFeedback: NotRequired[int]
    callsReceivedFeedback: NotRequired[int]
    ownCallsListenedTo: NotRequired[int]
    othersCallsListenedTo: NotRequired[int]
    callsSharedInternally: NotRequired[int]
    callsSharedExternally: NotRequired[int]
    callsScorecardsFilled: NotRequired[int]
    callsScorecardsReceived: NotRequired[int]
    callsAttended: NotRequired[int]
    callsCommentsGiven: NotRequired[int]
    callsCommentsReceived: NotRequired[int]
    callsMarkedAsFeedbackGiven: NotRequired[int]
    callsMarkedAsFeedbackReceived: NotRequired[int]

class UserAggregateActivity(TypedDict):
    """User with aggregated activity statistics"""
    userId: NotRequired[str]
    userEmailAddress: NotRequired[str]
    userAggregateActivityStats: NotRequired[UserAggregateActivityStats]

class ActivityAggregateResponse(TypedDict):
    """Response containing aggregated activity statistics"""
    requestId: NotRequired[str]
    records: NotRequired[PaginationRecords]
    usersAggregateActivityStats: NotRequired[list[UserAggregateActivity]]
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    timeZone: NotRequired[str]

class DailyActivityStats(TypedDict):
    """Daily activity statistics with call IDs"""
    callsAsHost: NotRequired[list[str]]
    callsGaveFeedback: NotRequired[list[str]]
    callsRequestedFeedback: NotRequired[list[str]]
    callsReceivedFeedback: NotRequired[list[str]]
    ownCallsListenedTo: NotRequired[list[str]]
    othersCallsListenedTo: NotRequired[list[str]]
    callsSharedInternally: NotRequired[list[str]]
    callsSharedExternally: NotRequired[list[str]]
    callsAttended: NotRequired[list[str]]
    callsCommentsGiven: NotRequired[list[str]]
    callsCommentsReceived: NotRequired[list[str]]
    callsMarkedAsFeedbackGiven: NotRequired[list[str]]
    callsMarkedAsFeedbackReceived: NotRequired[list[str]]
    callsScorecardsFilled: NotRequired[list[str]]
    callsScorecardsReceived: NotRequired[list[str]]
    fromDate: NotRequired[str]
    toDate: NotRequired[str]

class UserDetailedActivity(TypedDict):
    """User with detailed daily activity statistics"""
    userId: NotRequired[str]
    userEmailAddress: NotRequired[str]
    userDailyActivityStats: NotRequired[list[DailyActivityStats]]

class ActivityDayByDayResponse(TypedDict):
    """Response containing daily activity statistics"""
    requestId: NotRequired[str]
    records: NotRequired[PaginationRecords]
    usersDetailedActivities: NotRequired[list[UserDetailedActivity]]

class PersonInteractionStat(TypedDict):
    """Individual interaction statistic"""
    name: NotRequired[str]
    value: NotRequired[float]

class UserInteractionStats(TypedDict):
    """User with interaction statistics"""
    userId: NotRequired[str]
    userEmailAddress: NotRequired[str]
    personInteractionStats: NotRequired[list[PersonInteractionStat]]

class InteractionStatsResponse(TypedDict):
    """Response containing interaction statistics"""
    requestId: NotRequired[str]
    records: NotRequired[PaginationRecords]
    peopleInteractionStats: NotRequired[list[UserInteractionStats]]
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    timeZone: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    fromDateTime: str
    toDateTime: str
    cursor: NotRequired[str]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    id: str

class CallsExtensiveListParams(TypedDict):
    """Parameters for calls_extensive.list operation"""
    pass

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    pass

class CallTranscriptsListParams(TypedDict):
    """Parameters for call_transcripts.list operation"""
    pass

class StatsActivityAggregateListParams(TypedDict):
    """Parameters for stats_activity_aggregate.list operation"""
    pass

class StatsActivityDayByDayListParams(TypedDict):
    """Parameters for stats_activity_day_by_day.list operation"""
    pass

class StatsInteractionListParams(TypedDict):
    """Parameters for stats_interaction.list operation"""
    pass
