"""
Blessed Airtable connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import AirtableConnector
from .models import (
    AirtableAuthConfig,
    Base,
    BasesList,
    TableField,
    View,
    Table,
    TablesList,
    Record,
    RecordsList,
    AirtableCheckResult,
    AirtableExecuteResult,
    AirtableExecuteResultWithMeta,
    BasesListResult,
    TablesListResult,
    RecordsListResult,
    AirbyteSearchHit,
    AirbyteSearchResult,
    BasesSearchData,
    BasesSearchResult,
    TablesSearchData,
    TablesSearchResult
)
from .types import (
    BasesListParams,
    TablesListParams,
    RecordsListParams,
    RecordsGetParams,
    AirbyteSearchParams,
    AirbyteSortOrder,
    BasesSearchFilter,
    BasesSearchQuery,
    BasesCondition,
    TablesSearchFilter,
    TablesSearchQuery,
    TablesCondition
)

__all__ = [
    "AirtableConnector",
    "AirtableAuthConfig",
    "Base",
    "BasesList",
    "TableField",
    "View",
    "Table",
    "TablesList",
    "Record",
    "RecordsList",
    "AirtableCheckResult",
    "AirtableExecuteResult",
    "AirtableExecuteResultWithMeta",
    "BasesListResult",
    "TablesListResult",
    "RecordsListResult",
    "AirbyteSearchHit",
    "AirbyteSearchResult",
    "BasesSearchData",
    "BasesSearchResult",
    "TablesSearchData",
    "TablesSearchResult",
    "BasesListParams",
    "TablesListParams",
    "RecordsListParams",
    "RecordsGetParams",
    "AirbyteSearchParams",
    "AirbyteSortOrder",
    "BasesSearchFilter",
    "BasesSearchQuery",
    "BasesCondition",
    "TablesSearchFilter",
    "TablesSearchQuery",
    "TablesCondition",
]