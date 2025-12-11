"""
Type definitions for gong connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



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
