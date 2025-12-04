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

class CallTranscriptTranscriptItemSentencesItem(TypedDict):
    """Nested schema for CallTranscriptTranscriptItem.sentences_item"""
    start: NotRequired[int]
    end: NotRequired[int]
    text: NotRequired[str]

class CallTranscriptTranscriptItem(TypedDict):
    """Nested schema for CallTranscript.transcript_item"""
    speakerId: NotRequired[str]
    topic: NotRequired[str | None]
    sentences: NotRequired[list[CallTranscriptTranscriptItemSentencesItem]]

class CallTranscript(TypedDict):
    """Call transcript object"""
    callId: NotRequired[str]
    transcript: NotRequired[list[CallTranscriptTranscriptItem]]

class TranscriptsResponse(TypedDict):
    """Response containing call transcripts"""
    callTranscripts: NotRequired[list[CallTranscript]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class ExtensiveCallMedia(TypedDict):
    """Media URLs"""
    audioUrl: NotRequired[str]
    videoUrl: NotRequired[str]

class ExtensiveCallInteractionQuestions(TypedDict):
    """Nested schema for ExtensiveCallInteraction.questions"""
    companyCount: NotRequired[int]
    nonCompanyCount: NotRequired[int]

class ExtensiveCallInteractionInteractionstatsItem(TypedDict):
    """Nested schema for ExtensiveCallInteraction.interactionStats_item"""
    speakerId: NotRequired[str]
    talkTime: NotRequired[float]

class ExtensiveCallInteraction(TypedDict):
    """Interaction statistics"""
    interactionStats: NotRequired[list[ExtensiveCallInteractionInteractionstatsItem]]
    questions: NotRequired[ExtensiveCallInteractionQuestions]

class ExtensiveCallPartiesItemContextItem(TypedDict):
    """Nested schema for ExtensiveCallPartiesItem.context_item"""
    system: NotRequired[str]
    objects: NotRequired[list[dict[str, Any]]]

class ExtensiveCallPartiesItem(TypedDict):
    """Nested schema for ExtensiveCall.parties_item"""
    id: NotRequired[str]
    emailAddress: NotRequired[str]
    name: NotRequired[str]
    title: NotRequired[str]
    userId: NotRequired[str]
    speakerId: NotRequired[str]
    context: NotRequired[list[ExtensiveCallPartiesItemContextItem]]

class ExtensiveCallCollaboration(TypedDict):
    """Collaboration data"""
    publicComments: NotRequired[list[dict[str, Any]]]

class ExtensiveCallContentTrackersItem(TypedDict):
    """Nested schema for ExtensiveCallContent.trackers_item"""
    id: NotRequired[str]
    name: NotRequired[str]
    count: NotRequired[int]
    type: NotRequired[str]
    occurrences: NotRequired[list[dict[str, Any]]]

class ExtensiveCallContentTopicsItem(TypedDict):
    """Nested schema for ExtensiveCallContent.topics_item"""
    name: NotRequired[str]
    duration: NotRequired[float]

class ExtensiveCallContent(TypedDict):
    """Content data including topics and trackers"""
    topics: NotRequired[list[ExtensiveCallContentTopicsItem]]
    trackers: NotRequired[list[ExtensiveCallContentTrackersItem]]
    pointsOfInterest: NotRequired[dict[str, Any]]

class ExtensiveCallMetadata(TypedDict):
    """Call metadata"""
    id: NotRequired[str]
    url: NotRequired[str]
    title: NotRequired[str]
    scheduled: NotRequired[str]
    started: NotRequired[str]
    duration: NotRequired[int]
    primaryUserId: NotRequired[str]
    direction: NotRequired[str]
    system: NotRequired[str]
    scope: NotRequired[str]
    media: NotRequired[str]
    language: NotRequired[str]
    workspaceId: NotRequired[str]
    isPrivate: NotRequired[bool]
    meetingUrl: NotRequired[str]

class ExtensiveCall(TypedDict):
    """Detailed call object with extended information"""
    metaData: NotRequired[ExtensiveCallMetadata]
    parties: NotRequired[list[ExtensiveCallPartiesItem]]
    interaction: NotRequired[ExtensiveCallInteraction]
    collaboration: NotRequired[ExtensiveCallCollaboration]
    content: NotRequired[ExtensiveCallContent]
    media: NotRequired[ExtensiveCallMedia]

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

# ===== ENVELOPE TYPE DEFINITIONS =====

class UsersListResultMeta(TypedDict):
    """Metadata for users.list operation"""
    pagination: PaginationRecords

class UsersListResult(TypedDict):
    """Result envelope for users.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[User]
    meta: UsersListResultMeta

class UsersGetResult(TypedDict):
    """Result envelope for users.get operation

    Contains extracted data from the API response.
    """
    data: User

class CallsListResultMeta(TypedDict):
    """Metadata for calls.list operation"""
    pagination: PaginationRecords

class CallsListResult(TypedDict):
    """Result envelope for calls.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[Call]
    meta: CallsListResultMeta

class CallsGetResult(TypedDict):
    """Result envelope for calls.get operation

    Contains extracted data from the API response.
    """
    data: Call

class CallsExtensiveListResultMeta(TypedDict):
    """Metadata for calls_extensive.list operation"""
    pagination: PaginationRecords

class CallsExtensiveListResult(TypedDict):
    """Result envelope for calls_extensive.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[ExtensiveCall]
    meta: CallsExtensiveListResultMeta

class WorkspacesListResult(TypedDict):
    """Result envelope for workspaces.list operation

    Contains extracted data from the API response.
    """
    data: list[Workspace]

class CallTranscriptsListResultMeta(TypedDict):
    """Metadata for call_transcripts.list operation"""
    pagination: PaginationRecords

class CallTranscriptsListResult(TypedDict):
    """Result envelope for call_transcripts.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[CallTranscript]
    meta: CallTranscriptsListResultMeta

class StatsActivityAggregateListResultMeta(TypedDict):
    """Metadata for stats_activity_aggregate.list operation"""
    pagination: PaginationRecords

class StatsActivityAggregateListResult(TypedDict):
    """Result envelope for stats_activity_aggregate.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[UserAggregateActivity]
    meta: StatsActivityAggregateListResultMeta

class StatsActivityDayByDayListResultMeta(TypedDict):
    """Metadata for stats_activity_day_by_day.list operation"""
    pagination: PaginationRecords

class StatsActivityDayByDayListResult(TypedDict):
    """Result envelope for stats_activity_day_by_day.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[UserDetailedActivity]
    meta: StatsActivityDayByDayListResultMeta

class StatsInteractionListResultMeta(TypedDict):
    """Metadata for stats_interaction.list operation"""
    pagination: PaginationRecords

class StatsInteractionListResult(TypedDict):
    """Result envelope for stats_interaction.list operation

    Contains extracted data and metadata from the API response.
    """
    data: list[UserInteractionStats]
    meta: StatsInteractionListResultMeta

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    cursor: NotRequired[str]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    id: str

class CallsExtensiveListParams(TypedDict):
    """Parameters for calls_extensive.list operation"""
    filter: NotRequired[CallsExtensiveListParamsFilter]
    contentSelector: NotRequired[CallsExtensiveListParamsContentselector]
    cursor: NotRequired[str]

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
