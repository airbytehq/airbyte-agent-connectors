"""
Salesforce connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import SalesforceConnector
from .models import (
    SalesforceAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    LeadsSearchData,
    LeadsSearchResult,
    OpportunitiesSearchData,
    OpportunitiesSearchResult,
    TasksSearchData,
    TasksSearchResult,
    UsersSearchData,
    UsersSearchResult,
    OpportunityStagesSearchData,
    OpportunityStagesSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "SalesforceConnector",
    "AirbyteAuthConfig",
    "SalesforceAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "AccountsSearchData",
    "AccountsSearchResult",
    "ContactsSearchData",
    "ContactsSearchResult",
    "LeadsSearchData",
    "LeadsSearchResult",
    "OpportunitiesSearchData",
    "OpportunitiesSearchResult",
    "TasksSearchData",
    "TasksSearchResult",
    "UsersSearchData",
    "UsersSearchResult",
    "OpportunityStagesSearchData",
    "OpportunityStagesSearchResult",
]