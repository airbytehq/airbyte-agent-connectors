"""
Pydantic models for airtable connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class AirtableAuthConfig(BaseModel):
    """Personal Access Token"""

    model_config = ConfigDict(extra="forbid")

    personal_access_token: str
    """Airtable Personal Access Token. See https://airtable.com/developers/web/guides/personal-access-tokens"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Base(BaseModel):
    """An Airtable base (workspace)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str | None = Field(default=None)
    permission_level: str | None = Field(default=None, alias="permissionLevel")

class BasesList(BaseModel):
    """Paginated list of bases"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bases: list[Base] | None = Field(default=None)
    offset: str | None = Field(default=None)

class View(BaseModel):
    """A view in a table"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")

class TableField(BaseModel):
    """A field (column) in a table"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    options: dict[str, Any] | None = Field(default=None)

class Table(BaseModel):
    """A table within an Airtable base"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str | None = Field(default=None)
    primary_field_id: str | None = Field(default=None, alias="primaryFieldId")
    fields: list[TableField] | None = Field(default=None)
    views: list[View] | None = Field(default=None)

class TablesList(BaseModel):
    """List of tables in a base"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tables: list[Table] | None = Field(default=None)

class Record(BaseModel):
    """A record (row) in an Airtable table"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    created_time: str | None = Field(default=None, alias="createdTime")
    fields: dict[str, Any] | None = Field(default=None)

class RecordsList(BaseModel):
    """Paginated list of records"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    records: list[Record] | None = Field(default=None)
    offset: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class BasesListResultMeta(BaseModel):
    """Metadata for bases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)

class RecordsListResultMeta(BaseModel):
    """Metadata for records.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class AirtableCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class AirtableExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AirtableExecuteResultWithMeta(AirtableExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class BasesSearchData(BaseModel):
    """Search result data for bases entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the base"""
    name: str | None = None
    """Name of the base"""
    permission_level: str | None = None
    """Permission level for the base"""


class TablesSearchData(BaseModel):
    """Search result data for tables entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the table"""
    name: str | None = None
    """Name of the table"""
    primary_field_id: str | None = None
    """ID of the primary field"""
    fields: list[Any] | None = None
    """List of fields in the table"""
    views: list[Any] | None = None
    """List of views in the table"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

BasesSearchResult = AirbyteSearchResult[BasesSearchData]
"""Search result type for bases entity."""

TablesSearchResult = AirbyteSearchResult[TablesSearchData]
"""Search result type for tables entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

BasesListResult = AirtableExecuteResultWithMeta[list[Base], BasesListResultMeta]
"""Result type for bases.list operation with data and metadata."""

TablesListResult = AirtableExecuteResult[list[Table]]
"""Result type for tables.list operation."""

RecordsListResult = AirtableExecuteResultWithMeta[list[Record], RecordsListResultMeta]
"""Result type for records.list operation with data and metadata."""

