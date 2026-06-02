"""
Pydantic models for snowflake connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class SnowflakeAuthConfig(BaseModel):
    """PAT Authentication"""

    model_config = ConfigDict(extra="forbid")

    programmatic_access_token: str
    """Snowflake Programmatic Access Token (PAT) for authentication. Generate one via ALTER USER ADD PROGRAMMATIC ACCESS TOKEN in Snowflake."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class RowType(BaseModel):
    """Column metadata describing a single column in the result set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    database: str | None = Field(default=None)
    schema_: str | None = Field(default=None, alias="schema")
    table: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    scale: Any | None = Field(default=None)
    precision: Any | None = Field(default=None)
    length: Any | None = Field(default=None)
    nullable: bool | None = Field(default=None)
    byte_length: Any | None = Field(default=None, alias="byteLength")
    collation: Any | None = Field(default=None)

class PartitionInfo(BaseModel):
    """Information about a result partition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    row_count: int | None = Field(default=None, alias="rowCount")
    uncompressed_size: int | None = Field(default=None, alias="uncompressedSize")
    compressed_size: int | None = Field(default=None, alias="compressedSize")

class ResultSetMetaData(BaseModel):
    """Metadata about the result set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    num_rows: int | None = Field(default=None, alias="numRows")
    format: str | None = Field(default=None)
    row_type: list[RowType] | None = Field(default=None, alias="rowType")
    partition_info: list[PartitionInfo] | None = Field(default=None, alias="partitionInfo")

class StatementResponse(BaseModel):
    """Response from the Snowflake SQL API containing result set metadata and data rows. Used by all SHOW statement operations."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class DatabasesResponse(BaseModel):
    """DatabasesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class SchemasResponse(BaseModel):
    """SchemasResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class TablesResponse(BaseModel):
    """TablesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class ViewsResponse(BaseModel):
    """ViewsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class WarehousesResponse(BaseModel):
    """WarehousesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class ColumnsResponse(BaseModel):
    """ColumnsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

class ResultPartitionResponse(BaseModel):
    """ResultPartitionResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    result_set_meta_data: ResultSetMetaData | None = Field(default=None, alias="resultSetMetaData")
    data: list[list[Any]] | None = Field(default=None)
    code: str | None = Field(default=None)
    statement_status_url: str | None = Field(default=None, alias="statementStatusUrl")
    sql_state: str | None = Field(default=None, alias="sqlState")
    statement_handle: str | None = Field(default=None, alias="statementHandle")
    message: str | None = Field(default=None)
    created_on: int | None = Field(default=None, alias="createdOn")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class DatabasesListResultMeta(BaseModel):
    """Metadata for databases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)
    statement_handle: str | None = Field(default=None)
    partition_info: list[PartitionInfo] | None = Field(default=None)

class SchemasListResultMeta(BaseModel):
    """Metadata for schemas.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)
    statement_handle: str | None = Field(default=None)
    partition_info: list[PartitionInfo] | None = Field(default=None)

class TablesListResultMeta(BaseModel):
    """Metadata for tables.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)
    statement_handle: str | None = Field(default=None)
    partition_info: list[PartitionInfo] | None = Field(default=None)

class ViewsListResultMeta(BaseModel):
    """Metadata for views.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)
    statement_handle: str | None = Field(default=None)
    partition_info: list[PartitionInfo] | None = Field(default=None)

class WarehousesListResultMeta(BaseModel):
    """Metadata for warehouses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)
    statement_handle: str | None = Field(default=None)
    partition_info: list[PartitionInfo] | None = Field(default=None)

class ColumnsListResultMeta(BaseModel):
    """Metadata for columns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)
    statement_handle: str | None = Field(default=None)
    partition_info: list[PartitionInfo] | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class SnowflakeCheckResult(BaseModel):
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


class SnowflakeExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class SnowflakeExecuteResultWithMeta(SnowflakeExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

DatabasesListResult = SnowflakeExecuteResultWithMeta[DatabasesResponse, DatabasesListResultMeta]
"""Result type for databases.list operation with data and metadata."""

SchemasListResult = SnowflakeExecuteResultWithMeta[SchemasResponse, SchemasListResultMeta]
"""Result type for schemas.list operation with data and metadata."""

TablesListResult = SnowflakeExecuteResultWithMeta[TablesResponse, TablesListResultMeta]
"""Result type for tables.list operation with data and metadata."""

ViewsListResult = SnowflakeExecuteResultWithMeta[ViewsResponse, ViewsListResultMeta]
"""Result type for views.list operation with data and metadata."""

WarehousesListResult = SnowflakeExecuteResultWithMeta[WarehousesResponse, WarehousesListResultMeta]
"""Result type for warehouses.list operation with data and metadata."""

ColumnsListResult = SnowflakeExecuteResultWithMeta[ColumnsResponse, ColumnsListResultMeta]
"""Result type for columns.list operation with data and metadata."""

