"""
Google-Drive connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GoogleDriveConnector
from .models import (
    GoogleDriveAuthConfig,
    GoogleDriveReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    FilesSearchData,
    FilesSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "GoogleDriveConnector",
    "AirbyteAuthConfig",
    "GoogleDriveAuthConfig",
    "GoogleDriveReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "FilesSearchData",
    "FilesSearchResult",
]