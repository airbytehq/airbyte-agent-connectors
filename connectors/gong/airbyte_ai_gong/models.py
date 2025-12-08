"""
Pydantic models for gong connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, SkipValidation
from typing import TypeVar, Generic

# Import types needed for result type aliases
from .types import (
    AnsweredScorecard,
    Call,
    CallTranscript,
    CallTranscriptsListResultMeta,
    CallsExtensiveListResultMeta,
    CallsListResultMeta,
    CoachingData,
    ExtensiveCall,
    FolderCall,
    LibraryFolder,
    LibraryFolderContentListResultMeta,
    Scorecard,
    StatsActivityAggregateListResultMeta,
    StatsActivityDayByDayListResultMeta,
    StatsActivityScorecardsListResultMeta,
    StatsInteractionListResultMeta,
    Tracker,
    User,
    UserAggregateActivity,
    UserDetailedActivity,
    UserInteractionStats,
    UsersListResultMeta,
    Workspace,
)

# Authentication configuration

class GongAuthConfig(BaseModel):
    """Access Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_key: str
    """Your Gong API Access Key"""
    access_key_secret: str
    """Your Gong API Access Key Secret"""

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class GongExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: SkipValidation[T]
    """Response data containing the result of the action."""


class GongExecuteResultWithMeta(GongExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: SkipValidation[S]
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = GongExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

UsersGetResult = GongExecuteResult[User]
"""Result type for users.get operation."""

CallsListResult = GongExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

CallsGetResult = GongExecuteResult[Call]
"""Result type for calls.get operation."""

CallsExtensiveListResult = GongExecuteResultWithMeta[list[ExtensiveCall], CallsExtensiveListResultMeta]
"""Result type for calls_extensive.list operation with data and metadata."""

WorkspacesListResult = GongExecuteResult[list[Workspace]]
"""Result type for workspaces.list operation."""

CallTranscriptsListResult = GongExecuteResultWithMeta[list[CallTranscript], CallTranscriptsListResultMeta]
"""Result type for call_transcripts.list operation with data and metadata."""

StatsActivityAggregateListResult = GongExecuteResultWithMeta[list[UserAggregateActivity], StatsActivityAggregateListResultMeta]
"""Result type for stats_activity_aggregate.list operation with data and metadata."""

StatsActivityDayByDayListResult = GongExecuteResultWithMeta[list[UserDetailedActivity], StatsActivityDayByDayListResultMeta]
"""Result type for stats_activity_day_by_day.list operation with data and metadata."""

StatsInteractionListResult = GongExecuteResultWithMeta[list[UserInteractionStats], StatsInteractionListResultMeta]
"""Result type for stats_interaction.list operation with data and metadata."""

SettingsScorecardsListResult = GongExecuteResult[list[Scorecard]]
"""Result type for settings_scorecards.list operation."""

SettingsTrackersListResult = GongExecuteResult[list[Tracker]]
"""Result type for settings_trackers.list operation."""

LibraryFoldersListResult = GongExecuteResult[list[LibraryFolder]]
"""Result type for library_folders.list operation."""

LibraryFolderContentListResult = GongExecuteResultWithMeta[list[FolderCall], LibraryFolderContentListResultMeta]
"""Result type for library_folder_content.list operation with data and metadata."""

CoachingListResult = GongExecuteResult[list[CoachingData]]
"""Result type for coaching.list operation."""

StatsActivityScorecardsListResult = GongExecuteResultWithMeta[list[AnsweredScorecard], StatsActivityScorecardsListResultMeta]
"""Result type for stats_activity_scorecards.list operation with data and metadata."""

