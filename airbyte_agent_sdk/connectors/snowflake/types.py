"""
Type definitions for snowflake connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class DatabasesListParams(TypedDict):
    """Parameters for databases.list operation"""
    statement: NotRequired[str]
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class SchemasListParams(TypedDict):
    """Parameters for schemas.list operation"""
    statement: NotRequired[str]
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class TablesListParams(TypedDict):
    """Parameters for tables.list operation"""
    statement: NotRequired[str]
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class ViewsListParams(TypedDict):
    """Parameters for views.list operation"""
    statement: NotRequired[str]
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class WarehousesListParams(TypedDict):
    """Parameters for warehouses.list operation"""
    statement: NotRequired[str]
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class ColumnsListParams(TypedDict):
    """Parameters for columns.list operation"""
    statement: NotRequired[str]
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class RecordGetParams(TypedDict):
    """Parameters for record.get operation"""
    statement: str
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class RecordListParams(TypedDict):
    """Parameters for record.list operation"""
    statement: str
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]

class RecordCreateParams(TypedDict):
    """Parameters for record.create operation"""
    statement: str
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]
    request_id: NotRequired[str]
    retry: NotRequired[bool]

class RecordUpdateParams(TypedDict):
    """Parameters for record.update operation"""
    statement: str
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]
    request_id: NotRequired[str]
    retry: NotRequired[bool]

class RecordDeleteParams(TypedDict):
    """Parameters for record.delete operation"""
    statement: str
    database: NotRequired[str]
    schema: NotRequired[str]
    warehouse: NotRequired[str]
    role: NotRequired[str]
    timeout: NotRequired[int]
    parameters: NotRequired[dict[str, Any]]
    request_id: NotRequired[str]
    retry: NotRequired[bool]

class ResultPartitionsGetParams(TypedDict):
    """Parameters for result_partitions.get operation"""
    statement_handle: str
    partition: int
    request_id: NotRequired[str]

