"""
Hubspot connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import HubspotConnector
from .models import (
    HubspotAuthConfig,
    HubspotOAuthCredentials,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CompaniesSearchData,
    CompaniesSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    DealsSearchData,
    DealsSearchResult,
    TicketsSearchData,
    TicketsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "HubspotConnector",
    "AirbyteAuthConfig",
    "HubspotAuthConfig",
    "HubspotOAuthCredentials",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "CompaniesSearchData",
    "CompaniesSearchResult",
    "ContactsSearchData",
    "ContactsSearchResult",
    "DealsSearchData",
    "DealsSearchResult",
    "TicketsSearchData",
    "TicketsSearchResult",
]