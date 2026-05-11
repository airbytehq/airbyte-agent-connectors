"""
Customer-Io connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import CustomerIoConnector
from .models import (
    CustomerIoAuthConfig,
    CustomerIoReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    CampaignActionsSearchData,
    CampaignActionsSearchResult,
    NewslettersSearchData,
    NewslettersSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "CustomerIoConnector",
    "AirbyteAuthConfig",
    "CustomerIoAuthConfig",
    "CustomerIoReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "CampaignsSearchData",
    "CampaignsSearchResult",
    "CampaignActionsSearchData",
    "CampaignActionsSearchResult",
    "NewslettersSearchData",
    "NewslettersSearchResult",
]