"""
Type definitions for airtable connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class BasesListParams(TypedDict):
    """Parameters for bases.list operation"""
    offset: NotRequired[str]

class TablesListParams(TypedDict):
    """Parameters for tables.list operation"""
    base_id: str

class RecordsListParams(TypedDict):
    """Parameters for records.list operation"""
    base_id: str
    table_id_or_name: str
    offset: NotRequired[str]
    page_size: NotRequired[int]
    view: NotRequired[str]
    filter_by_formula: NotRequired[str]
    sort: NotRequired[str]

class RecordsGetParams(TypedDict):
    """Parameters for records.get operation"""
    base_id: str
    table_id_or_name: str
    record_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== BASES SEARCH TYPES =====

class BasesSearchFilter(TypedDict, total=False):
    """Available fields for filtering bases search queries."""
    id: str | None
    """Unique identifier for the base"""
    name: str | None
    """Name of the base"""
    permission_level: str | None
    """Permission level for the base"""


class BasesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the base"""
    name: list[str]
    """Name of the base"""
    permission_level: list[str]
    """Permission level for the base"""


class BasesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the base"""
    name: Any
    """Name of the base"""
    permission_level: Any
    """Permission level for the base"""


class BasesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the base"""
    name: str
    """Name of the base"""
    permission_level: str
    """Permission level for the base"""


class BasesSortFilter(TypedDict, total=False):
    """Available fields for sorting bases search results."""
    id: AirbyteSortOrder
    """Unique identifier for the base"""
    name: AirbyteSortOrder
    """Name of the base"""
    permission_level: AirbyteSortOrder
    """Permission level for the base"""


# Entity-specific condition types for bases
class BasesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BasesSearchFilter


class BasesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BasesSearchFilter


class BasesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BasesSearchFilter


class BasesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BasesSearchFilter


class BasesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BasesSearchFilter


class BasesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BasesSearchFilter


class BasesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BasesStringFilter


class BasesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BasesStringFilter


class BasesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BasesStringFilter


class BasesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BasesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BasesInCondition = TypedDict("BasesInCondition", {"in": BasesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BasesNotCondition = TypedDict("BasesNotCondition", {"not": "BasesCondition"}, total=False)
"""Negates the nested condition."""

BasesAndCondition = TypedDict("BasesAndCondition", {"and": "list[BasesCondition]"}, total=False)
"""True if all nested conditions are true."""

BasesOrCondition = TypedDict("BasesOrCondition", {"or": "list[BasesCondition]"}, total=False)
"""True if any nested condition is true."""

BasesAnyCondition = TypedDict("BasesAnyCondition", {"any": BasesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all bases condition types
BasesCondition = (
    BasesEqCondition
    | BasesNeqCondition
    | BasesGtCondition
    | BasesGteCondition
    | BasesLtCondition
    | BasesLteCondition
    | BasesInCondition
    | BasesLikeCondition
    | BasesFuzzyCondition
    | BasesKeywordCondition
    | BasesContainsCondition
    | BasesNotCondition
    | BasesAndCondition
    | BasesOrCondition
    | BasesAnyCondition
)


class BasesSearchQuery(TypedDict, total=False):
    """Search query for bases entity."""
    filter: BasesCondition
    sort: list[BasesSortFilter]


# ===== TABLES SEARCH TYPES =====

class TablesSearchFilter(TypedDict, total=False):
    """Available fields for filtering tables search queries."""
    id: str | None
    """Unique identifier for the table"""
    name: str | None
    """Name of the table"""
    primary_field_id: str | None
    """ID of the primary field"""
    fields: list[Any] | None
    """List of fields in the table"""
    views: list[Any] | None
    """List of views in the table"""


class TablesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the table"""
    name: list[str]
    """Name of the table"""
    primary_field_id: list[str]
    """ID of the primary field"""
    fields: list[list[Any]]
    """List of fields in the table"""
    views: list[list[Any]]
    """List of views in the table"""


class TablesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the table"""
    name: Any
    """Name of the table"""
    primary_field_id: Any
    """ID of the primary field"""
    fields: Any
    """List of fields in the table"""
    views: Any
    """List of views in the table"""


class TablesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the table"""
    name: str
    """Name of the table"""
    primary_field_id: str
    """ID of the primary field"""
    fields: str
    """List of fields in the table"""
    views: str
    """List of views in the table"""


class TablesSortFilter(TypedDict, total=False):
    """Available fields for sorting tables search results."""
    id: AirbyteSortOrder
    """Unique identifier for the table"""
    name: AirbyteSortOrder
    """Name of the table"""
    primary_field_id: AirbyteSortOrder
    """ID of the primary field"""
    fields: AirbyteSortOrder
    """List of fields in the table"""
    views: AirbyteSortOrder
    """List of views in the table"""


# Entity-specific condition types for tables
class TablesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TablesSearchFilter


class TablesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TablesSearchFilter


class TablesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TablesSearchFilter


class TablesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TablesSearchFilter


class TablesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TablesSearchFilter


class TablesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TablesSearchFilter


class TablesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TablesStringFilter


class TablesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TablesStringFilter


class TablesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TablesStringFilter


class TablesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TablesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TablesInCondition = TypedDict("TablesInCondition", {"in": TablesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TablesNotCondition = TypedDict("TablesNotCondition", {"not": "TablesCondition"}, total=False)
"""Negates the nested condition."""

TablesAndCondition = TypedDict("TablesAndCondition", {"and": "list[TablesCondition]"}, total=False)
"""True if all nested conditions are true."""

TablesOrCondition = TypedDict("TablesOrCondition", {"or": "list[TablesCondition]"}, total=False)
"""True if any nested condition is true."""

TablesAnyCondition = TypedDict("TablesAnyCondition", {"any": TablesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tables condition types
TablesCondition = (
    TablesEqCondition
    | TablesNeqCondition
    | TablesGtCondition
    | TablesGteCondition
    | TablesLtCondition
    | TablesLteCondition
    | TablesInCondition
    | TablesLikeCondition
    | TablesFuzzyCondition
    | TablesKeywordCondition
    | TablesContainsCondition
    | TablesNotCondition
    | TablesAndCondition
    | TablesOrCondition
    | TablesAnyCondition
)


class TablesSearchQuery(TypedDict, total=False):
    """Search query for tables entity."""
    filter: TablesCondition
    sort: list[TablesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
