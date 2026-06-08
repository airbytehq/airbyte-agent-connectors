"""
Gong connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GongConnector
from .models import (
    GongAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    UsersSearchData,
    UsersSearchResult,
    CallsSearchData,
    CallsSearchResult,
    CallsExtensiveSearchData,
    CallsExtensiveSearchResult,
    SettingsScorecardsSearchData,
    SettingsScorecardsSearchResult,
    StatsActivityScorecardsSearchData,
    StatsActivityScorecardsSearchResult,
    CallTranscriptsSearchData,
    CallTranscriptsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "GongConnector",
    "AirbyteAuthConfig",
    "GongAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "UsersSearchData",
    "UsersSearchResult",
    "CallsSearchData",
    "CallsSearchResult",
    "CallsExtensiveSearchData",
    "CallsExtensiveSearchResult",
    "SettingsScorecardsSearchData",
    "SettingsScorecardsSearchResult",
    "StatsActivityScorecardsSearchData",
    "StatsActivityScorecardsSearchResult",
    "CallTranscriptsSearchData",
    "CallTranscriptsSearchResult",
]