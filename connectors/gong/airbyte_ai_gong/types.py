"""
Type definitions for gong connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any


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

class CallsAiContentListParamsFilter(TypedDict):
    """Nested schema for CallsAiContentListParams.filter"""
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    callIds: NotRequired[list[str]]

class CallsAiContentListParamsContentselector(TypedDict):
    """Select which AI content to include in the response"""
    brief: NotRequired[bool]
    outline: NotRequired[bool]
    highlights: NotRequired[bool]
    callOutcome: NotRequired[bool]

class StatsActivityScorecardsListParamsFilter(TypedDict):
    """Nested schema for StatsActivityScorecardsListParams.filter"""
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]
    scorecardIds: NotRequired[list[str]]
    reviewedUserIds: NotRequired[list[str]]
    reviewerUserIds: NotRequired[list[str]]
    callIds: NotRequired[list[str]]

class UserSettings(TypedDict):
    """User settings"""
    webConferencesRecorded: NotRequired[bool]
    preventWebConferenceRecording: NotRequired[bool]
    telephonyCallsImported: NotRequired[bool]
    emailsImported: NotRequired[bool]
    preventEmailImport: NotRequired[bool]
    nonRecordedMeetingsImported: NotRequired[bool]
    gongConnectEnabled: NotRequired[bool]

class UserSpokenlanguagesItem(TypedDict):
    """Nested schema for User.spokenLanguages_item"""
    language: NotRequired[str]
    primary: NotRequired[bool]

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
    sdrDisposition: NotRequired[str | None]
    clientUniqueId: NotRequired[str | None]
    customData: NotRequired[str | None]
    purpose: NotRequired[str | None]
    isPrivate: NotRequired[bool]
    meetingUrl: NotRequired[str]
    calendarEventId: NotRequired[str | None]

class ExtensiveCallPartiesItemContextItemObjectsItemFieldsItem(TypedDict):
    """Nested schema for ExtensiveCallPartiesItemContextItemObjectsItem.fields_item"""
    name: NotRequired[str]
    value: NotRequired[Any]

class ExtensiveCallPartiesItemContextItemObjectsItem(TypedDict):
    """Nested schema for ExtensiveCallPartiesItemContextItem.objects_item"""
    objectType: NotRequired[str]
    objectId: NotRequired[str]
    fields: NotRequired[list[ExtensiveCallPartiesItemContextItemObjectsItemFieldsItem]]

class ExtensiveCallPartiesItemContextItem(TypedDict):
    """Nested schema for ExtensiveCallPartiesItem.context_item"""
    system: NotRequired[str]
    objects: NotRequired[list[ExtensiveCallPartiesItemContextItemObjectsItem]]

class ExtensiveCallPartiesItem(TypedDict):
    """Nested schema for ExtensiveCall.parties_item"""
    id: NotRequired[str]
    emailAddress: NotRequired[str]
    name: NotRequired[str]
    title: NotRequired[str]
    userId: NotRequired[str]
    speakerId: NotRequired[str | None]
    affiliation: NotRequired[str]
    methods: NotRequired[list[str]]
    phoneNumber: NotRequired[str]
    context: NotRequired[list[ExtensiveCallPartiesItemContextItem]]

class ExtensiveCallInteractionInteractionstatsItem(TypedDict):
    """Nested schema for ExtensiveCallInteraction.interactionStats_item"""
    name: NotRequired[str]
    value: NotRequired[float]

class ExtensiveCallInteractionQuestions(TypedDict):
    """Nested schema for ExtensiveCallInteraction.questions"""
    companyCount: NotRequired[int]
    nonCompanyCount: NotRequired[int]

class ExtensiveCallInteraction(TypedDict):
    """Interaction statistics"""
    interactionStats: NotRequired[list[ExtensiveCallInteractionInteractionstatsItem]]
    questions: NotRequired[ExtensiveCallInteractionQuestions]

class ExtensiveCallCollaboration(TypedDict):
    """Collaboration data"""
    publicComments: NotRequired[list[dict[str, Any]]]

class ExtensiveCallContentTopicsItem(TypedDict):
    """Nested schema for ExtensiveCallContent.topics_item"""
    name: NotRequired[str]
    duration: NotRequired[float]

class ExtensiveCallContentTrackersItem(TypedDict):
    """Nested schema for ExtensiveCallContent.trackers_item"""
    id: NotRequired[str]
    name: NotRequired[str]
    count: NotRequired[int]
    type: NotRequired[str]
    occurrences: NotRequired[list[dict[str, Any]]]

class ExtensiveCallContent(TypedDict):
    """Content data including topics and trackers"""
    topics: NotRequired[list[ExtensiveCallContentTopicsItem]]
    trackers: NotRequired[list[ExtensiveCallContentTrackersItem]]
    pointsOfInterest: NotRequired[dict[str, Any]]

class ExtensiveCallMedia(TypedDict):
    """Media URLs"""
    audioUrl: NotRequired[str]
    videoUrl: NotRequired[str]

class ScorecardQuestionAnsweroptionsItem(TypedDict):
    """Nested schema for ScorecardQuestion.answerOptions_item"""
    optionId: NotRequired[str]
    optionText: NotRequired[str]
    score: NotRequired[float]

class TrackerKeywordsItem(TypedDict):
    """Nested schema for Tracker.keywords_item"""
    keyword: NotRequired[str]
    aliases: NotRequired[list[str]]

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
    filter: NotRequired[CallsExtensiveListParamsFilter]
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
    workspace_id: NotRequired[str]

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

class CallsAiContentListParams(TypedDict):
    """Parameters for calls_ai_content.list operation"""
    filter: NotRequired[CallsAiContentListParamsFilter]
    content_selector: NotRequired[CallsAiContentListParamsContentselector]
    cursor: NotRequired[str]

class StatsActivityScorecardsListParams(TypedDict):
    """Parameters for stats_activity_scorecards.list operation"""
    filter: NotRequired[StatsActivityScorecardsListParamsFilter]
    cursor: NotRequired[str]
