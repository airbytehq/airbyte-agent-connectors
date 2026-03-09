"""
Type definitions for harvest connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    per_page: NotRequired[int]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class ClientsListParams(TypedDict):
    """Parameters for clients.list operation"""
    per_page: NotRequired[int]

class ClientsGetParams(TypedDict):
    """Parameters for clients.get operation"""
    id: str

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    per_page: NotRequired[int]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class CompanyGetParams(TypedDict):
    """Parameters for company.get operation"""
    pass

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    per_page: NotRequired[int]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    id: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    per_page: NotRequired[int]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    id: str

class TimeEntriesListParams(TypedDict):
    """Parameters for time_entries.list operation"""
    per_page: NotRequired[int]

class TimeEntriesGetParams(TypedDict):
    """Parameters for time_entries.get operation"""
    id: str

class InvoicesListParams(TypedDict):
    """Parameters for invoices.list operation"""
    per_page: NotRequired[int]

class InvoicesGetParams(TypedDict):
    """Parameters for invoices.get operation"""
    id: str

class InvoiceItemCategoriesListParams(TypedDict):
    """Parameters for invoice_item_categories.list operation"""
    per_page: NotRequired[int]

class InvoiceItemCategoriesGetParams(TypedDict):
    """Parameters for invoice_item_categories.get operation"""
    id: str

class EstimatesListParams(TypedDict):
    """Parameters for estimates.list operation"""
    per_page: NotRequired[int]

class EstimatesGetParams(TypedDict):
    """Parameters for estimates.get operation"""
    id: str

class EstimateItemCategoriesListParams(TypedDict):
    """Parameters for estimate_item_categories.list operation"""
    per_page: NotRequired[int]

class EstimateItemCategoriesGetParams(TypedDict):
    """Parameters for estimate_item_categories.get operation"""
    id: str

class ExpensesListParams(TypedDict):
    """Parameters for expenses.list operation"""
    per_page: NotRequired[int]

class ExpensesGetParams(TypedDict):
    """Parameters for expenses.get operation"""
    id: str

class ExpenseCategoriesListParams(TypedDict):
    """Parameters for expense_categories.list operation"""
    per_page: NotRequired[int]

class ExpenseCategoriesGetParams(TypedDict):
    """Parameters for expense_categories.get operation"""
    id: str

class RolesListParams(TypedDict):
    """Parameters for roles.list operation"""
    per_page: NotRequired[int]

class RolesGetParams(TypedDict):
    """Parameters for roles.get operation"""
    id: str

class UserAssignmentsListParams(TypedDict):
    """Parameters for user_assignments.list operation"""
    per_page: NotRequired[int]

class TaskAssignmentsListParams(TypedDict):
    """Parameters for task_assignments.list operation"""
    per_page: NotRequired[int]

class TimeProjectsListParams(TypedDict):
    """Parameters for time_projects.list operation"""
    from_: str
    to: str
    per_page: NotRequired[int]

class TimeTasksListParams(TypedDict):
    """Parameters for time_tasks.list operation"""
    from_: str
    to: str
    per_page: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CLIENTS SEARCH TYPES =====

class ClientsSearchFilter(TypedDict, total=False):
    """Available fields for filtering clients search queries."""
    address: str | None
    """The client's postal address"""
    created_at: str | None
    """When the client record was created"""
    currency: str | None
    """The currency used by the client"""
    id: int | None
    """Unique identifier for the client"""
    is_active: bool | None
    """Whether the client is active"""
    name: str | None
    """The client's name"""
    updated_at: str | None
    """When the client record was last updated"""


class ClientsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    address: list[str]
    """The client's postal address"""
    created_at: list[str]
    """When the client record was created"""
    currency: list[str]
    """The currency used by the client"""
    id: list[int]
    """Unique identifier for the client"""
    is_active: list[bool]
    """Whether the client is active"""
    name: list[str]
    """The client's name"""
    updated_at: list[str]
    """When the client record was last updated"""


class ClientsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    address: Any
    """The client's postal address"""
    created_at: Any
    """When the client record was created"""
    currency: Any
    """The currency used by the client"""
    id: Any
    """Unique identifier for the client"""
    is_active: Any
    """Whether the client is active"""
    name: Any
    """The client's name"""
    updated_at: Any
    """When the client record was last updated"""


class ClientsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    address: str
    """The client's postal address"""
    created_at: str
    """When the client record was created"""
    currency: str
    """The currency used by the client"""
    id: str
    """Unique identifier for the client"""
    is_active: str
    """Whether the client is active"""
    name: str
    """The client's name"""
    updated_at: str
    """When the client record was last updated"""


class ClientsSortFilter(TypedDict, total=False):
    """Available fields for sorting clients search results."""
    address: AirbyteSortOrder
    """The client's postal address"""
    created_at: AirbyteSortOrder
    """When the client record was created"""
    currency: AirbyteSortOrder
    """The currency used by the client"""
    id: AirbyteSortOrder
    """Unique identifier for the client"""
    is_active: AirbyteSortOrder
    """Whether the client is active"""
    name: AirbyteSortOrder
    """The client's name"""
    updated_at: AirbyteSortOrder
    """When the client record was last updated"""


# Entity-specific condition types for clients
class ClientsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ClientsSearchFilter


class ClientsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ClientsSearchFilter


class ClientsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ClientsSearchFilter


class ClientsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ClientsSearchFilter


class ClientsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ClientsSearchFilter


class ClientsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ClientsSearchFilter


class ClientsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ClientsStringFilter


class ClientsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ClientsStringFilter


class ClientsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ClientsStringFilter


class ClientsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ClientsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ClientsInCondition = TypedDict("ClientsInCondition", {"in": ClientsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ClientsNotCondition = TypedDict("ClientsNotCondition", {"not": "ClientsCondition"}, total=False)
"""Negates the nested condition."""

ClientsAndCondition = TypedDict("ClientsAndCondition", {"and": "list[ClientsCondition]"}, total=False)
"""True if all nested conditions are true."""

ClientsOrCondition = TypedDict("ClientsOrCondition", {"or": "list[ClientsCondition]"}, total=False)
"""True if any nested condition is true."""

ClientsAnyCondition = TypedDict("ClientsAnyCondition", {"any": ClientsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all clients condition types
ClientsCondition = (
    ClientsEqCondition
    | ClientsNeqCondition
    | ClientsGtCondition
    | ClientsGteCondition
    | ClientsLtCondition
    | ClientsLteCondition
    | ClientsInCondition
    | ClientsLikeCondition
    | ClientsFuzzyCondition
    | ClientsKeywordCondition
    | ClientsContainsCondition
    | ClientsNotCondition
    | ClientsAndCondition
    | ClientsOrCondition
    | ClientsAnyCondition
)


class ClientsSearchQuery(TypedDict, total=False):
    """Search query for clients entity."""
    filter: ClientsCondition
    sort: list[ClientsSortFilter]


# ===== COMPANY SEARCH TYPES =====

class CompanySearchFilter(TypedDict, total=False):
    """Available fields for filtering company search queries."""
    base_uri: str | None
    """The base URI"""
    currency: str | None
    """Currency used by the company"""
    full_domain: str | None
    """The full domain name"""
    is_active: bool | None
    """Whether the company is active"""
    name: str | None
    """The name of the company"""
    plan_type: str | None
    """The plan type"""
    weekly_capacity: int | None
    """Weekly capacity in seconds"""


class CompanyInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    base_uri: list[str]
    """The base URI"""
    currency: list[str]
    """Currency used by the company"""
    full_domain: list[str]
    """The full domain name"""
    is_active: list[bool]
    """Whether the company is active"""
    name: list[str]
    """The name of the company"""
    plan_type: list[str]
    """The plan type"""
    weekly_capacity: list[int]
    """Weekly capacity in seconds"""


class CompanyAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    base_uri: Any
    """The base URI"""
    currency: Any
    """Currency used by the company"""
    full_domain: Any
    """The full domain name"""
    is_active: Any
    """Whether the company is active"""
    name: Any
    """The name of the company"""
    plan_type: Any
    """The plan type"""
    weekly_capacity: Any
    """Weekly capacity in seconds"""


class CompanyStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    base_uri: str
    """The base URI"""
    currency: str
    """Currency used by the company"""
    full_domain: str
    """The full domain name"""
    is_active: str
    """Whether the company is active"""
    name: str
    """The name of the company"""
    plan_type: str
    """The plan type"""
    weekly_capacity: str
    """Weekly capacity in seconds"""


class CompanySortFilter(TypedDict, total=False):
    """Available fields for sorting company search results."""
    base_uri: AirbyteSortOrder
    """The base URI"""
    currency: AirbyteSortOrder
    """Currency used by the company"""
    full_domain: AirbyteSortOrder
    """The full domain name"""
    is_active: AirbyteSortOrder
    """Whether the company is active"""
    name: AirbyteSortOrder
    """The name of the company"""
    plan_type: AirbyteSortOrder
    """The plan type"""
    weekly_capacity: AirbyteSortOrder
    """Weekly capacity in seconds"""


# Entity-specific condition types for company
class CompanyEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CompanySearchFilter


class CompanyNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CompanySearchFilter


class CompanyGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CompanySearchFilter


class CompanyGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CompanySearchFilter


class CompanyLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CompanySearchFilter


class CompanyLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CompanySearchFilter


class CompanyLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CompanyStringFilter


class CompanyFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CompanyStringFilter


class CompanyKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CompanyStringFilter


class CompanyContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CompanyAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CompanyInCondition = TypedDict("CompanyInCondition", {"in": CompanyInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CompanyNotCondition = TypedDict("CompanyNotCondition", {"not": "CompanyCondition"}, total=False)
"""Negates the nested condition."""

CompanyAndCondition = TypedDict("CompanyAndCondition", {"and": "list[CompanyCondition]"}, total=False)
"""True if all nested conditions are true."""

CompanyOrCondition = TypedDict("CompanyOrCondition", {"or": "list[CompanyCondition]"}, total=False)
"""True if any nested condition is true."""

CompanyAnyCondition = TypedDict("CompanyAnyCondition", {"any": CompanyAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all company condition types
CompanyCondition = (
    CompanyEqCondition
    | CompanyNeqCondition
    | CompanyGtCondition
    | CompanyGteCondition
    | CompanyLtCondition
    | CompanyLteCondition
    | CompanyInCondition
    | CompanyLikeCondition
    | CompanyFuzzyCondition
    | CompanyKeywordCondition
    | CompanyContainsCondition
    | CompanyNotCondition
    | CompanyAndCondition
    | CompanyOrCondition
    | CompanyAnyCondition
)


class CompanySearchQuery(TypedDict, total=False):
    """Search query for company entity."""
    filter: CompanyCondition
    sort: list[CompanySortFilter]


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    client: dict[str, Any] | None
    """Client associated with the contact"""
    created_at: str | None
    """When created"""
    email: str | None
    """Email address"""
    first_name: str | None
    """First name"""
    id: int | None
    """Unique identifier"""
    last_name: str | None
    """Last name"""
    title: str | None
    """Job title"""
    updated_at: str | None
    """When last updated"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    client: list[dict[str, Any]]
    """Client associated with the contact"""
    created_at: list[str]
    """When created"""
    email: list[str]
    """Email address"""
    first_name: list[str]
    """First name"""
    id: list[int]
    """Unique identifier"""
    last_name: list[str]
    """Last name"""
    title: list[str]
    """Job title"""
    updated_at: list[str]
    """When last updated"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    client: Any
    """Client associated with the contact"""
    created_at: Any
    """When created"""
    email: Any
    """Email address"""
    first_name: Any
    """First name"""
    id: Any
    """Unique identifier"""
    last_name: Any
    """Last name"""
    title: Any
    """Job title"""
    updated_at: Any
    """When last updated"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    client: str
    """Client associated with the contact"""
    created_at: str
    """When created"""
    email: str
    """Email address"""
    first_name: str
    """First name"""
    id: str
    """Unique identifier"""
    last_name: str
    """Last name"""
    title: str
    """Job title"""
    updated_at: str
    """When last updated"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    client: AirbyteSortOrder
    """Client associated with the contact"""
    created_at: AirbyteSortOrder
    """When created"""
    email: AirbyteSortOrder
    """Email address"""
    first_name: AirbyteSortOrder
    """First name"""
    id: AirbyteSortOrder
    """Unique identifier"""
    last_name: AirbyteSortOrder
    """Last name"""
    title: AirbyteSortOrder
    """Job title"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for contacts
class ContactsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ContactsSearchFilter


class ContactsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ContactsSearchFilter


class ContactsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ContactsSearchFilter


class ContactsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ContactsSearchFilter


class ContactsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ContactsSearchFilter


class ContactsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ContactsSearchFilter


class ContactsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ContactsStringFilter


class ContactsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ContactsStringFilter


class ContactsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ContactsStringFilter


class ContactsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ContactsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ContactsInCondition = TypedDict("ContactsInCondition", {"in": ContactsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ContactsNotCondition = TypedDict("ContactsNotCondition", {"not": "ContactsCondition"}, total=False)
"""Negates the nested condition."""

ContactsAndCondition = TypedDict("ContactsAndCondition", {"and": "list[ContactsCondition]"}, total=False)
"""True if all nested conditions are true."""

ContactsOrCondition = TypedDict("ContactsOrCondition", {"or": "list[ContactsCondition]"}, total=False)
"""True if any nested condition is true."""

ContactsAnyCondition = TypedDict("ContactsAnyCondition", {"any": ContactsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all contacts condition types
ContactsCondition = (
    ContactsEqCondition
    | ContactsNeqCondition
    | ContactsGtCondition
    | ContactsGteCondition
    | ContactsLtCondition
    | ContactsLteCondition
    | ContactsInCondition
    | ContactsLikeCondition
    | ContactsFuzzyCondition
    | ContactsKeywordCondition
    | ContactsContainsCondition
    | ContactsNotCondition
    | ContactsAndCondition
    | ContactsOrCondition
    | ContactsAnyCondition
)


class ContactsSearchQuery(TypedDict, total=False):
    """Search query for contacts entity."""
    filter: ContactsCondition
    sort: list[ContactsSortFilter]


# ===== ESTIMATE_ITEM_CATEGORIES SEARCH TYPES =====

class EstimateItemCategoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering estimate_item_categories search queries."""
    created_at: str | None
    """When created"""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Category name"""
    updated_at: str | None
    """When last updated"""


class EstimateItemCategoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When created"""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Category name"""
    updated_at: list[str]
    """When last updated"""


class EstimateItemCategoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When created"""
    id: Any
    """Unique identifier"""
    name: Any
    """Category name"""
    updated_at: Any
    """When last updated"""


class EstimateItemCategoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When created"""
    id: str
    """Unique identifier"""
    name: str
    """Category name"""
    updated_at: str
    """When last updated"""


class EstimateItemCategoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting estimate_item_categories search results."""
    created_at: AirbyteSortOrder
    """When created"""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Category name"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for estimate_item_categories
class EstimateItemCategoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EstimateItemCategoriesSearchFilter


class EstimateItemCategoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EstimateItemCategoriesSearchFilter


class EstimateItemCategoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EstimateItemCategoriesSearchFilter


class EstimateItemCategoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EstimateItemCategoriesSearchFilter


class EstimateItemCategoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EstimateItemCategoriesSearchFilter


class EstimateItemCategoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EstimateItemCategoriesSearchFilter


class EstimateItemCategoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EstimateItemCategoriesStringFilter


class EstimateItemCategoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EstimateItemCategoriesStringFilter


class EstimateItemCategoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EstimateItemCategoriesStringFilter


class EstimateItemCategoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EstimateItemCategoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EstimateItemCategoriesInCondition = TypedDict("EstimateItemCategoriesInCondition", {"in": EstimateItemCategoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EstimateItemCategoriesNotCondition = TypedDict("EstimateItemCategoriesNotCondition", {"not": "EstimateItemCategoriesCondition"}, total=False)
"""Negates the nested condition."""

EstimateItemCategoriesAndCondition = TypedDict("EstimateItemCategoriesAndCondition", {"and": "list[EstimateItemCategoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

EstimateItemCategoriesOrCondition = TypedDict("EstimateItemCategoriesOrCondition", {"or": "list[EstimateItemCategoriesCondition]"}, total=False)
"""True if any nested condition is true."""

EstimateItemCategoriesAnyCondition = TypedDict("EstimateItemCategoriesAnyCondition", {"any": EstimateItemCategoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all estimate_item_categories condition types
EstimateItemCategoriesCondition = (
    EstimateItemCategoriesEqCondition
    | EstimateItemCategoriesNeqCondition
    | EstimateItemCategoriesGtCondition
    | EstimateItemCategoriesGteCondition
    | EstimateItemCategoriesLtCondition
    | EstimateItemCategoriesLteCondition
    | EstimateItemCategoriesInCondition
    | EstimateItemCategoriesLikeCondition
    | EstimateItemCategoriesFuzzyCondition
    | EstimateItemCategoriesKeywordCondition
    | EstimateItemCategoriesContainsCondition
    | EstimateItemCategoriesNotCondition
    | EstimateItemCategoriesAndCondition
    | EstimateItemCategoriesOrCondition
    | EstimateItemCategoriesAnyCondition
)


class EstimateItemCategoriesSearchQuery(TypedDict, total=False):
    """Search query for estimate_item_categories entity."""
    filter: EstimateItemCategoriesCondition
    sort: list[EstimateItemCategoriesSortFilter]


# ===== ESTIMATES SEARCH TYPES =====

class EstimatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering estimates search queries."""
    amount: float | None
    """Total amount"""
    client: dict[str, Any] | None
    """Client details"""
    created_at: str | None
    """When created"""
    currency: str | None
    """Currency"""
    id: int | None
    """Unique identifier"""
    issue_date: str | None
    """Issue date"""
    number: str | None
    """Estimate number"""
    state: str | None
    """Current state"""
    subject: str | None
    """Subject"""
    updated_at: str | None
    """When last updated"""


class EstimatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[float]
    """Total amount"""
    client: list[dict[str, Any]]
    """Client details"""
    created_at: list[str]
    """When created"""
    currency: list[str]
    """Currency"""
    id: list[int]
    """Unique identifier"""
    issue_date: list[str]
    """Issue date"""
    number: list[str]
    """Estimate number"""
    state: list[str]
    """Current state"""
    subject: list[str]
    """Subject"""
    updated_at: list[str]
    """When last updated"""


class EstimatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """Total amount"""
    client: Any
    """Client details"""
    created_at: Any
    """When created"""
    currency: Any
    """Currency"""
    id: Any
    """Unique identifier"""
    issue_date: Any
    """Issue date"""
    number: Any
    """Estimate number"""
    state: Any
    """Current state"""
    subject: Any
    """Subject"""
    updated_at: Any
    """When last updated"""


class EstimatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """Total amount"""
    client: str
    """Client details"""
    created_at: str
    """When created"""
    currency: str
    """Currency"""
    id: str
    """Unique identifier"""
    issue_date: str
    """Issue date"""
    number: str
    """Estimate number"""
    state: str
    """Current state"""
    subject: str
    """Subject"""
    updated_at: str
    """When last updated"""


class EstimatesSortFilter(TypedDict, total=False):
    """Available fields for sorting estimates search results."""
    amount: AirbyteSortOrder
    """Total amount"""
    client: AirbyteSortOrder
    """Client details"""
    created_at: AirbyteSortOrder
    """When created"""
    currency: AirbyteSortOrder
    """Currency"""
    id: AirbyteSortOrder
    """Unique identifier"""
    issue_date: AirbyteSortOrder
    """Issue date"""
    number: AirbyteSortOrder
    """Estimate number"""
    state: AirbyteSortOrder
    """Current state"""
    subject: AirbyteSortOrder
    """Subject"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for estimates
class EstimatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EstimatesSearchFilter


class EstimatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EstimatesSearchFilter


class EstimatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EstimatesSearchFilter


class EstimatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EstimatesSearchFilter


class EstimatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EstimatesSearchFilter


class EstimatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EstimatesSearchFilter


class EstimatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EstimatesStringFilter


class EstimatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EstimatesStringFilter


class EstimatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EstimatesStringFilter


class EstimatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EstimatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EstimatesInCondition = TypedDict("EstimatesInCondition", {"in": EstimatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EstimatesNotCondition = TypedDict("EstimatesNotCondition", {"not": "EstimatesCondition"}, total=False)
"""Negates the nested condition."""

EstimatesAndCondition = TypedDict("EstimatesAndCondition", {"and": "list[EstimatesCondition]"}, total=False)
"""True if all nested conditions are true."""

EstimatesOrCondition = TypedDict("EstimatesOrCondition", {"or": "list[EstimatesCondition]"}, total=False)
"""True if any nested condition is true."""

EstimatesAnyCondition = TypedDict("EstimatesAnyCondition", {"any": EstimatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all estimates condition types
EstimatesCondition = (
    EstimatesEqCondition
    | EstimatesNeqCondition
    | EstimatesGtCondition
    | EstimatesGteCondition
    | EstimatesLtCondition
    | EstimatesLteCondition
    | EstimatesInCondition
    | EstimatesLikeCondition
    | EstimatesFuzzyCondition
    | EstimatesKeywordCondition
    | EstimatesContainsCondition
    | EstimatesNotCondition
    | EstimatesAndCondition
    | EstimatesOrCondition
    | EstimatesAnyCondition
)


class EstimatesSearchQuery(TypedDict, total=False):
    """Search query for estimates entity."""
    filter: EstimatesCondition
    sort: list[EstimatesSortFilter]


# ===== EXPENSE_CATEGORIES SEARCH TYPES =====

class ExpenseCategoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering expense_categories search queries."""
    created_at: str | None
    """When created"""
    id: int | None
    """Unique identifier"""
    is_active: bool | None
    """Whether active"""
    name: str | None
    """Category name"""
    unit_name: str | None
    """Unit name"""
    unit_price: float | None
    """Unit price"""
    updated_at: str | None
    """When last updated"""


class ExpenseCategoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When created"""
    id: list[int]
    """Unique identifier"""
    is_active: list[bool]
    """Whether active"""
    name: list[str]
    """Category name"""
    unit_name: list[str]
    """Unit name"""
    unit_price: list[float]
    """Unit price"""
    updated_at: list[str]
    """When last updated"""


class ExpenseCategoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When created"""
    id: Any
    """Unique identifier"""
    is_active: Any
    """Whether active"""
    name: Any
    """Category name"""
    unit_name: Any
    """Unit name"""
    unit_price: Any
    """Unit price"""
    updated_at: Any
    """When last updated"""


class ExpenseCategoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When created"""
    id: str
    """Unique identifier"""
    is_active: str
    """Whether active"""
    name: str
    """Category name"""
    unit_name: str
    """Unit name"""
    unit_price: str
    """Unit price"""
    updated_at: str
    """When last updated"""


class ExpenseCategoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting expense_categories search results."""
    created_at: AirbyteSortOrder
    """When created"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_active: AirbyteSortOrder
    """Whether active"""
    name: AirbyteSortOrder
    """Category name"""
    unit_name: AirbyteSortOrder
    """Unit name"""
    unit_price: AirbyteSortOrder
    """Unit price"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for expense_categories
class ExpenseCategoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ExpenseCategoriesSearchFilter


class ExpenseCategoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ExpenseCategoriesSearchFilter


class ExpenseCategoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ExpenseCategoriesSearchFilter


class ExpenseCategoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ExpenseCategoriesSearchFilter


class ExpenseCategoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ExpenseCategoriesSearchFilter


class ExpenseCategoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ExpenseCategoriesSearchFilter


class ExpenseCategoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ExpenseCategoriesStringFilter


class ExpenseCategoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ExpenseCategoriesStringFilter


class ExpenseCategoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ExpenseCategoriesStringFilter


class ExpenseCategoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ExpenseCategoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ExpenseCategoriesInCondition = TypedDict("ExpenseCategoriesInCondition", {"in": ExpenseCategoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ExpenseCategoriesNotCondition = TypedDict("ExpenseCategoriesNotCondition", {"not": "ExpenseCategoriesCondition"}, total=False)
"""Negates the nested condition."""

ExpenseCategoriesAndCondition = TypedDict("ExpenseCategoriesAndCondition", {"and": "list[ExpenseCategoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

ExpenseCategoriesOrCondition = TypedDict("ExpenseCategoriesOrCondition", {"or": "list[ExpenseCategoriesCondition]"}, total=False)
"""True if any nested condition is true."""

ExpenseCategoriesAnyCondition = TypedDict("ExpenseCategoriesAnyCondition", {"any": ExpenseCategoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all expense_categories condition types
ExpenseCategoriesCondition = (
    ExpenseCategoriesEqCondition
    | ExpenseCategoriesNeqCondition
    | ExpenseCategoriesGtCondition
    | ExpenseCategoriesGteCondition
    | ExpenseCategoriesLtCondition
    | ExpenseCategoriesLteCondition
    | ExpenseCategoriesInCondition
    | ExpenseCategoriesLikeCondition
    | ExpenseCategoriesFuzzyCondition
    | ExpenseCategoriesKeywordCondition
    | ExpenseCategoriesContainsCondition
    | ExpenseCategoriesNotCondition
    | ExpenseCategoriesAndCondition
    | ExpenseCategoriesOrCondition
    | ExpenseCategoriesAnyCondition
)


class ExpenseCategoriesSearchQuery(TypedDict, total=False):
    """Search query for expense_categories entity."""
    filter: ExpenseCategoriesCondition
    sort: list[ExpenseCategoriesSortFilter]


# ===== EXPENSES SEARCH TYPES =====

class ExpensesSearchFilter(TypedDict, total=False):
    """Available fields for filtering expenses search queries."""
    billable: bool | None
    """Whether billable"""
    client: dict[str, Any] | None
    """Associated client"""
    created_at: str | None
    """When created"""
    expense_category: dict[str, Any] | None
    """Expense category"""
    id: int | None
    """Unique identifier"""
    is_billed: bool | None
    """Whether billed"""
    notes: str | None
    """Notes"""
    project: dict[str, Any] | None
    """Associated project"""
    spent_date: str | None
    """Date spent"""
    total_cost: float | None
    """Total cost"""
    updated_at: str | None
    """When last updated"""
    user: dict[str, Any] | None
    """Associated user"""


class ExpensesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billable: list[bool]
    """Whether billable"""
    client: list[dict[str, Any]]
    """Associated client"""
    created_at: list[str]
    """When created"""
    expense_category: list[dict[str, Any]]
    """Expense category"""
    id: list[int]
    """Unique identifier"""
    is_billed: list[bool]
    """Whether billed"""
    notes: list[str]
    """Notes"""
    project: list[dict[str, Any]]
    """Associated project"""
    spent_date: list[str]
    """Date spent"""
    total_cost: list[float]
    """Total cost"""
    updated_at: list[str]
    """When last updated"""
    user: list[dict[str, Any]]
    """Associated user"""


class ExpensesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billable: Any
    """Whether billable"""
    client: Any
    """Associated client"""
    created_at: Any
    """When created"""
    expense_category: Any
    """Expense category"""
    id: Any
    """Unique identifier"""
    is_billed: Any
    """Whether billed"""
    notes: Any
    """Notes"""
    project: Any
    """Associated project"""
    spent_date: Any
    """Date spent"""
    total_cost: Any
    """Total cost"""
    updated_at: Any
    """When last updated"""
    user: Any
    """Associated user"""


class ExpensesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billable: str
    """Whether billable"""
    client: str
    """Associated client"""
    created_at: str
    """When created"""
    expense_category: str
    """Expense category"""
    id: str
    """Unique identifier"""
    is_billed: str
    """Whether billed"""
    notes: str
    """Notes"""
    project: str
    """Associated project"""
    spent_date: str
    """Date spent"""
    total_cost: str
    """Total cost"""
    updated_at: str
    """When last updated"""
    user: str
    """Associated user"""


class ExpensesSortFilter(TypedDict, total=False):
    """Available fields for sorting expenses search results."""
    billable: AirbyteSortOrder
    """Whether billable"""
    client: AirbyteSortOrder
    """Associated client"""
    created_at: AirbyteSortOrder
    """When created"""
    expense_category: AirbyteSortOrder
    """Expense category"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_billed: AirbyteSortOrder
    """Whether billed"""
    notes: AirbyteSortOrder
    """Notes"""
    project: AirbyteSortOrder
    """Associated project"""
    spent_date: AirbyteSortOrder
    """Date spent"""
    total_cost: AirbyteSortOrder
    """Total cost"""
    updated_at: AirbyteSortOrder
    """When last updated"""
    user: AirbyteSortOrder
    """Associated user"""


# Entity-specific condition types for expenses
class ExpensesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ExpensesSearchFilter


class ExpensesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ExpensesSearchFilter


class ExpensesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ExpensesSearchFilter


class ExpensesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ExpensesSearchFilter


class ExpensesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ExpensesSearchFilter


class ExpensesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ExpensesSearchFilter


class ExpensesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ExpensesStringFilter


class ExpensesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ExpensesStringFilter


class ExpensesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ExpensesStringFilter


class ExpensesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ExpensesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ExpensesInCondition = TypedDict("ExpensesInCondition", {"in": ExpensesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ExpensesNotCondition = TypedDict("ExpensesNotCondition", {"not": "ExpensesCondition"}, total=False)
"""Negates the nested condition."""

ExpensesAndCondition = TypedDict("ExpensesAndCondition", {"and": "list[ExpensesCondition]"}, total=False)
"""True if all nested conditions are true."""

ExpensesOrCondition = TypedDict("ExpensesOrCondition", {"or": "list[ExpensesCondition]"}, total=False)
"""True if any nested condition is true."""

ExpensesAnyCondition = TypedDict("ExpensesAnyCondition", {"any": ExpensesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all expenses condition types
ExpensesCondition = (
    ExpensesEqCondition
    | ExpensesNeqCondition
    | ExpensesGtCondition
    | ExpensesGteCondition
    | ExpensesLtCondition
    | ExpensesLteCondition
    | ExpensesInCondition
    | ExpensesLikeCondition
    | ExpensesFuzzyCondition
    | ExpensesKeywordCondition
    | ExpensesContainsCondition
    | ExpensesNotCondition
    | ExpensesAndCondition
    | ExpensesOrCondition
    | ExpensesAnyCondition
)


class ExpensesSearchQuery(TypedDict, total=False):
    """Search query for expenses entity."""
    filter: ExpensesCondition
    sort: list[ExpensesSortFilter]


# ===== INVOICE_ITEM_CATEGORIES SEARCH TYPES =====

class InvoiceItemCategoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering invoice_item_categories search queries."""
    created_at: str | None
    """When created"""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Category name"""
    updated_at: str | None
    """When last updated"""
    use_as_expense: bool | None
    """Whether used as expense type"""
    use_as_service: bool | None
    """Whether used as service type"""


class InvoiceItemCategoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When created"""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Category name"""
    updated_at: list[str]
    """When last updated"""
    use_as_expense: list[bool]
    """Whether used as expense type"""
    use_as_service: list[bool]
    """Whether used as service type"""


class InvoiceItemCategoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When created"""
    id: Any
    """Unique identifier"""
    name: Any
    """Category name"""
    updated_at: Any
    """When last updated"""
    use_as_expense: Any
    """Whether used as expense type"""
    use_as_service: Any
    """Whether used as service type"""


class InvoiceItemCategoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When created"""
    id: str
    """Unique identifier"""
    name: str
    """Category name"""
    updated_at: str
    """When last updated"""
    use_as_expense: str
    """Whether used as expense type"""
    use_as_service: str
    """Whether used as service type"""


class InvoiceItemCategoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting invoice_item_categories search results."""
    created_at: AirbyteSortOrder
    """When created"""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Category name"""
    updated_at: AirbyteSortOrder
    """When last updated"""
    use_as_expense: AirbyteSortOrder
    """Whether used as expense type"""
    use_as_service: AirbyteSortOrder
    """Whether used as service type"""


# Entity-specific condition types for invoice_item_categories
class InvoiceItemCategoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InvoiceItemCategoriesSearchFilter


class InvoiceItemCategoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InvoiceItemCategoriesSearchFilter


class InvoiceItemCategoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InvoiceItemCategoriesSearchFilter


class InvoiceItemCategoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InvoiceItemCategoriesSearchFilter


class InvoiceItemCategoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InvoiceItemCategoriesSearchFilter


class InvoiceItemCategoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InvoiceItemCategoriesSearchFilter


class InvoiceItemCategoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InvoiceItemCategoriesStringFilter


class InvoiceItemCategoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InvoiceItemCategoriesStringFilter


class InvoiceItemCategoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InvoiceItemCategoriesStringFilter


class InvoiceItemCategoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InvoiceItemCategoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InvoiceItemCategoriesInCondition = TypedDict("InvoiceItemCategoriesInCondition", {"in": InvoiceItemCategoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InvoiceItemCategoriesNotCondition = TypedDict("InvoiceItemCategoriesNotCondition", {"not": "InvoiceItemCategoriesCondition"}, total=False)
"""Negates the nested condition."""

InvoiceItemCategoriesAndCondition = TypedDict("InvoiceItemCategoriesAndCondition", {"and": "list[InvoiceItemCategoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

InvoiceItemCategoriesOrCondition = TypedDict("InvoiceItemCategoriesOrCondition", {"or": "list[InvoiceItemCategoriesCondition]"}, total=False)
"""True if any nested condition is true."""

InvoiceItemCategoriesAnyCondition = TypedDict("InvoiceItemCategoriesAnyCondition", {"any": InvoiceItemCategoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all invoice_item_categories condition types
InvoiceItemCategoriesCondition = (
    InvoiceItemCategoriesEqCondition
    | InvoiceItemCategoriesNeqCondition
    | InvoiceItemCategoriesGtCondition
    | InvoiceItemCategoriesGteCondition
    | InvoiceItemCategoriesLtCondition
    | InvoiceItemCategoriesLteCondition
    | InvoiceItemCategoriesInCondition
    | InvoiceItemCategoriesLikeCondition
    | InvoiceItemCategoriesFuzzyCondition
    | InvoiceItemCategoriesKeywordCondition
    | InvoiceItemCategoriesContainsCondition
    | InvoiceItemCategoriesNotCondition
    | InvoiceItemCategoriesAndCondition
    | InvoiceItemCategoriesOrCondition
    | InvoiceItemCategoriesAnyCondition
)


class InvoiceItemCategoriesSearchQuery(TypedDict, total=False):
    """Search query for invoice_item_categories entity."""
    filter: InvoiceItemCategoriesCondition
    sort: list[InvoiceItemCategoriesSortFilter]


# ===== INVOICES SEARCH TYPES =====

class InvoicesSearchFilter(TypedDict, total=False):
    """Available fields for filtering invoices search queries."""
    amount: float | None
    """Total amount"""
    client: dict[str, Any] | None
    """Client details"""
    created_at: str | None
    """When created"""
    currency: str | None
    """Currency"""
    due_amount: float | None
    """Amount due"""
    due_date: str | None
    """Due date"""
    id: int | None
    """Unique identifier"""
    issue_date: str | None
    """Issue date"""
    number: str | None
    """Invoice number"""
    state: str | None
    """Current state"""
    subject: str | None
    """Subject"""
    updated_at: str | None
    """When last updated"""


class InvoicesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[float]
    """Total amount"""
    client: list[dict[str, Any]]
    """Client details"""
    created_at: list[str]
    """When created"""
    currency: list[str]
    """Currency"""
    due_amount: list[float]
    """Amount due"""
    due_date: list[str]
    """Due date"""
    id: list[int]
    """Unique identifier"""
    issue_date: list[str]
    """Issue date"""
    number: list[str]
    """Invoice number"""
    state: list[str]
    """Current state"""
    subject: list[str]
    """Subject"""
    updated_at: list[str]
    """When last updated"""


class InvoicesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """Total amount"""
    client: Any
    """Client details"""
    created_at: Any
    """When created"""
    currency: Any
    """Currency"""
    due_amount: Any
    """Amount due"""
    due_date: Any
    """Due date"""
    id: Any
    """Unique identifier"""
    issue_date: Any
    """Issue date"""
    number: Any
    """Invoice number"""
    state: Any
    """Current state"""
    subject: Any
    """Subject"""
    updated_at: Any
    """When last updated"""


class InvoicesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """Total amount"""
    client: str
    """Client details"""
    created_at: str
    """When created"""
    currency: str
    """Currency"""
    due_amount: str
    """Amount due"""
    due_date: str
    """Due date"""
    id: str
    """Unique identifier"""
    issue_date: str
    """Issue date"""
    number: str
    """Invoice number"""
    state: str
    """Current state"""
    subject: str
    """Subject"""
    updated_at: str
    """When last updated"""


class InvoicesSortFilter(TypedDict, total=False):
    """Available fields for sorting invoices search results."""
    amount: AirbyteSortOrder
    """Total amount"""
    client: AirbyteSortOrder
    """Client details"""
    created_at: AirbyteSortOrder
    """When created"""
    currency: AirbyteSortOrder
    """Currency"""
    due_amount: AirbyteSortOrder
    """Amount due"""
    due_date: AirbyteSortOrder
    """Due date"""
    id: AirbyteSortOrder
    """Unique identifier"""
    issue_date: AirbyteSortOrder
    """Issue date"""
    number: AirbyteSortOrder
    """Invoice number"""
    state: AirbyteSortOrder
    """Current state"""
    subject: AirbyteSortOrder
    """Subject"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for invoices
class InvoicesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InvoicesSearchFilter


class InvoicesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InvoicesSearchFilter


class InvoicesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InvoicesSearchFilter


class InvoicesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InvoicesSearchFilter


class InvoicesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InvoicesSearchFilter


class InvoicesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InvoicesSearchFilter


class InvoicesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InvoicesStringFilter


class InvoicesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InvoicesStringFilter


class InvoicesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InvoicesStringFilter


class InvoicesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InvoicesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InvoicesInCondition = TypedDict("InvoicesInCondition", {"in": InvoicesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InvoicesNotCondition = TypedDict("InvoicesNotCondition", {"not": "InvoicesCondition"}, total=False)
"""Negates the nested condition."""

InvoicesAndCondition = TypedDict("InvoicesAndCondition", {"and": "list[InvoicesCondition]"}, total=False)
"""True if all nested conditions are true."""

InvoicesOrCondition = TypedDict("InvoicesOrCondition", {"or": "list[InvoicesCondition]"}, total=False)
"""True if any nested condition is true."""

InvoicesAnyCondition = TypedDict("InvoicesAnyCondition", {"any": InvoicesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all invoices condition types
InvoicesCondition = (
    InvoicesEqCondition
    | InvoicesNeqCondition
    | InvoicesGtCondition
    | InvoicesGteCondition
    | InvoicesLtCondition
    | InvoicesLteCondition
    | InvoicesInCondition
    | InvoicesLikeCondition
    | InvoicesFuzzyCondition
    | InvoicesKeywordCondition
    | InvoicesContainsCondition
    | InvoicesNotCondition
    | InvoicesAndCondition
    | InvoicesOrCondition
    | InvoicesAnyCondition
)


class InvoicesSearchQuery(TypedDict, total=False):
    """Search query for invoices entity."""
    filter: InvoicesCondition
    sort: list[InvoicesSortFilter]


# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    budget: float | None
    """Budget amount"""
    client: dict[str, Any] | None
    """Client details"""
    code: str | None
    """Project code"""
    created_at: str | None
    """When created"""
    hourly_rate: float | None
    """Hourly rate"""
    id: int | None
    """Unique identifier"""
    is_active: bool | None
    """Whether active"""
    is_billable: bool | None
    """Whether billable"""
    name: str | None
    """Project name"""
    starts_on: str | None
    """Start date"""
    updated_at: str | None
    """When last updated"""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    budget: list[float]
    """Budget amount"""
    client: list[dict[str, Any]]
    """Client details"""
    code: list[str]
    """Project code"""
    created_at: list[str]
    """When created"""
    hourly_rate: list[float]
    """Hourly rate"""
    id: list[int]
    """Unique identifier"""
    is_active: list[bool]
    """Whether active"""
    is_billable: list[bool]
    """Whether billable"""
    name: list[str]
    """Project name"""
    starts_on: list[str]
    """Start date"""
    updated_at: list[str]
    """When last updated"""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    budget: Any
    """Budget amount"""
    client: Any
    """Client details"""
    code: Any
    """Project code"""
    created_at: Any
    """When created"""
    hourly_rate: Any
    """Hourly rate"""
    id: Any
    """Unique identifier"""
    is_active: Any
    """Whether active"""
    is_billable: Any
    """Whether billable"""
    name: Any
    """Project name"""
    starts_on: Any
    """Start date"""
    updated_at: Any
    """When last updated"""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    budget: str
    """Budget amount"""
    client: str
    """Client details"""
    code: str
    """Project code"""
    created_at: str
    """When created"""
    hourly_rate: str
    """Hourly rate"""
    id: str
    """Unique identifier"""
    is_active: str
    """Whether active"""
    is_billable: str
    """Whether billable"""
    name: str
    """Project name"""
    starts_on: str
    """Start date"""
    updated_at: str
    """When last updated"""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    budget: AirbyteSortOrder
    """Budget amount"""
    client: AirbyteSortOrder
    """Client details"""
    code: AirbyteSortOrder
    """Project code"""
    created_at: AirbyteSortOrder
    """When created"""
    hourly_rate: AirbyteSortOrder
    """Hourly rate"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_active: AirbyteSortOrder
    """Whether active"""
    is_billable: AirbyteSortOrder
    """Whether billable"""
    name: AirbyteSortOrder
    """Project name"""
    starts_on: AirbyteSortOrder
    """Start date"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for projects
class ProjectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectsSearchFilter


class ProjectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectsSearchFilter


class ProjectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectsSearchFilter


class ProjectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectsSearchFilter


class ProjectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectsSearchFilter


class ProjectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectsSearchFilter


class ProjectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectsStringFilter


class ProjectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectsStringFilter


class ProjectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectsStringFilter


class ProjectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectsInCondition = TypedDict("ProjectsInCondition", {"in": ProjectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectsNotCondition = TypedDict("ProjectsNotCondition", {"not": "ProjectsCondition"}, total=False)
"""Negates the nested condition."""

ProjectsAndCondition = TypedDict("ProjectsAndCondition", {"and": "list[ProjectsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectsOrCondition = TypedDict("ProjectsOrCondition", {"or": "list[ProjectsCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectsAnyCondition = TypedDict("ProjectsAnyCondition", {"any": ProjectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all projects condition types
ProjectsCondition = (
    ProjectsEqCondition
    | ProjectsNeqCondition
    | ProjectsGtCondition
    | ProjectsGteCondition
    | ProjectsLtCondition
    | ProjectsLteCondition
    | ProjectsInCondition
    | ProjectsLikeCondition
    | ProjectsFuzzyCondition
    | ProjectsKeywordCondition
    | ProjectsContainsCondition
    | ProjectsNotCondition
    | ProjectsAndCondition
    | ProjectsOrCondition
    | ProjectsAnyCondition
)


class ProjectsSearchQuery(TypedDict, total=False):
    """Search query for projects entity."""
    filter: ProjectsCondition
    sort: list[ProjectsSortFilter]


# ===== ROLES SEARCH TYPES =====

class RolesSearchFilter(TypedDict, total=False):
    """Available fields for filtering roles search queries."""
    created_at: str | None
    """When created"""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Role name"""
    updated_at: str | None
    """When last updated"""
    user_ids: list[Any] | None
    """User IDs with this role"""


class RolesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When created"""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Role name"""
    updated_at: list[str]
    """When last updated"""
    user_ids: list[list[Any]]
    """User IDs with this role"""


class RolesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When created"""
    id: Any
    """Unique identifier"""
    name: Any
    """Role name"""
    updated_at: Any
    """When last updated"""
    user_ids: Any
    """User IDs with this role"""


class RolesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When created"""
    id: str
    """Unique identifier"""
    name: str
    """Role name"""
    updated_at: str
    """When last updated"""
    user_ids: str
    """User IDs with this role"""


class RolesSortFilter(TypedDict, total=False):
    """Available fields for sorting roles search results."""
    created_at: AirbyteSortOrder
    """When created"""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Role name"""
    updated_at: AirbyteSortOrder
    """When last updated"""
    user_ids: AirbyteSortOrder
    """User IDs with this role"""


# Entity-specific condition types for roles
class RolesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RolesSearchFilter


class RolesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RolesSearchFilter


class RolesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RolesSearchFilter


class RolesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RolesSearchFilter


class RolesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RolesSearchFilter


class RolesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RolesSearchFilter


class RolesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: RolesStringFilter


class RolesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RolesStringFilter


class RolesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RolesStringFilter


class RolesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: RolesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RolesInCondition = TypedDict("RolesInCondition", {"in": RolesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RolesNotCondition = TypedDict("RolesNotCondition", {"not": "RolesCondition"}, total=False)
"""Negates the nested condition."""

RolesAndCondition = TypedDict("RolesAndCondition", {"and": "list[RolesCondition]"}, total=False)
"""True if all nested conditions are true."""

RolesOrCondition = TypedDict("RolesOrCondition", {"or": "list[RolesCondition]"}, total=False)
"""True if any nested condition is true."""

RolesAnyCondition = TypedDict("RolesAnyCondition", {"any": RolesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all roles condition types
RolesCondition = (
    RolesEqCondition
    | RolesNeqCondition
    | RolesGtCondition
    | RolesGteCondition
    | RolesLtCondition
    | RolesLteCondition
    | RolesInCondition
    | RolesLikeCondition
    | RolesFuzzyCondition
    | RolesKeywordCondition
    | RolesContainsCondition
    | RolesNotCondition
    | RolesAndCondition
    | RolesOrCondition
    | RolesAnyCondition
)


class RolesSearchQuery(TypedDict, total=False):
    """Search query for roles entity."""
    filter: RolesCondition
    sort: list[RolesSortFilter]


# ===== TASK_ASSIGNMENTS SEARCH TYPES =====

class TaskAssignmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering task_assignments search queries."""
    billable: bool | None
    """Whether billable"""
    created_at: str | None
    """When created"""
    hourly_rate: float | None
    """Hourly rate"""
    id: int | None
    """Unique identifier"""
    is_active: bool | None
    """Whether active"""
    project: dict[str, Any] | None
    """Associated project"""
    task: dict[str, Any] | None
    """Associated task"""
    updated_at: str | None
    """When last updated"""


class TaskAssignmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billable: list[bool]
    """Whether billable"""
    created_at: list[str]
    """When created"""
    hourly_rate: list[float]
    """Hourly rate"""
    id: list[int]
    """Unique identifier"""
    is_active: list[bool]
    """Whether active"""
    project: list[dict[str, Any]]
    """Associated project"""
    task: list[dict[str, Any]]
    """Associated task"""
    updated_at: list[str]
    """When last updated"""


class TaskAssignmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billable: Any
    """Whether billable"""
    created_at: Any
    """When created"""
    hourly_rate: Any
    """Hourly rate"""
    id: Any
    """Unique identifier"""
    is_active: Any
    """Whether active"""
    project: Any
    """Associated project"""
    task: Any
    """Associated task"""
    updated_at: Any
    """When last updated"""


class TaskAssignmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billable: str
    """Whether billable"""
    created_at: str
    """When created"""
    hourly_rate: str
    """Hourly rate"""
    id: str
    """Unique identifier"""
    is_active: str
    """Whether active"""
    project: str
    """Associated project"""
    task: str
    """Associated task"""
    updated_at: str
    """When last updated"""


class TaskAssignmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting task_assignments search results."""
    billable: AirbyteSortOrder
    """Whether billable"""
    created_at: AirbyteSortOrder
    """When created"""
    hourly_rate: AirbyteSortOrder
    """Hourly rate"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_active: AirbyteSortOrder
    """Whether active"""
    project: AirbyteSortOrder
    """Associated project"""
    task: AirbyteSortOrder
    """Associated task"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for task_assignments
class TaskAssignmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TaskAssignmentsSearchFilter


class TaskAssignmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TaskAssignmentsSearchFilter


class TaskAssignmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TaskAssignmentsSearchFilter


class TaskAssignmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TaskAssignmentsSearchFilter


class TaskAssignmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TaskAssignmentsSearchFilter


class TaskAssignmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TaskAssignmentsSearchFilter


class TaskAssignmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TaskAssignmentsStringFilter


class TaskAssignmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TaskAssignmentsStringFilter


class TaskAssignmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TaskAssignmentsStringFilter


class TaskAssignmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TaskAssignmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TaskAssignmentsInCondition = TypedDict("TaskAssignmentsInCondition", {"in": TaskAssignmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TaskAssignmentsNotCondition = TypedDict("TaskAssignmentsNotCondition", {"not": "TaskAssignmentsCondition"}, total=False)
"""Negates the nested condition."""

TaskAssignmentsAndCondition = TypedDict("TaskAssignmentsAndCondition", {"and": "list[TaskAssignmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

TaskAssignmentsOrCondition = TypedDict("TaskAssignmentsOrCondition", {"or": "list[TaskAssignmentsCondition]"}, total=False)
"""True if any nested condition is true."""

TaskAssignmentsAnyCondition = TypedDict("TaskAssignmentsAnyCondition", {"any": TaskAssignmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all task_assignments condition types
TaskAssignmentsCondition = (
    TaskAssignmentsEqCondition
    | TaskAssignmentsNeqCondition
    | TaskAssignmentsGtCondition
    | TaskAssignmentsGteCondition
    | TaskAssignmentsLtCondition
    | TaskAssignmentsLteCondition
    | TaskAssignmentsInCondition
    | TaskAssignmentsLikeCondition
    | TaskAssignmentsFuzzyCondition
    | TaskAssignmentsKeywordCondition
    | TaskAssignmentsContainsCondition
    | TaskAssignmentsNotCondition
    | TaskAssignmentsAndCondition
    | TaskAssignmentsOrCondition
    | TaskAssignmentsAnyCondition
)


class TaskAssignmentsSearchQuery(TypedDict, total=False):
    """Search query for task_assignments entity."""
    filter: TaskAssignmentsCondition
    sort: list[TaskAssignmentsSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    billable_by_default: bool | None
    """Whether billable by default"""
    created_at: str | None
    """When created"""
    default_hourly_rate: float | None
    """Default hourly rate"""
    id: int | None
    """Unique identifier"""
    is_active: bool | None
    """Whether active"""
    name: str | None
    """Task name"""
    updated_at: str | None
    """When last updated"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billable_by_default: list[bool]
    """Whether billable by default"""
    created_at: list[str]
    """When created"""
    default_hourly_rate: list[float]
    """Default hourly rate"""
    id: list[int]
    """Unique identifier"""
    is_active: list[bool]
    """Whether active"""
    name: list[str]
    """Task name"""
    updated_at: list[str]
    """When last updated"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billable_by_default: Any
    """Whether billable by default"""
    created_at: Any
    """When created"""
    default_hourly_rate: Any
    """Default hourly rate"""
    id: Any
    """Unique identifier"""
    is_active: Any
    """Whether active"""
    name: Any
    """Task name"""
    updated_at: Any
    """When last updated"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billable_by_default: str
    """Whether billable by default"""
    created_at: str
    """When created"""
    default_hourly_rate: str
    """Default hourly rate"""
    id: str
    """Unique identifier"""
    is_active: str
    """Whether active"""
    name: str
    """Task name"""
    updated_at: str
    """When last updated"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    billable_by_default: AirbyteSortOrder
    """Whether billable by default"""
    created_at: AirbyteSortOrder
    """When created"""
    default_hourly_rate: AirbyteSortOrder
    """Default hourly rate"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_active: AirbyteSortOrder
    """Whether active"""
    name: AirbyteSortOrder
    """Task name"""
    updated_at: AirbyteSortOrder
    """When last updated"""


# Entity-specific condition types for tasks
class TasksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TasksSearchFilter


class TasksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TasksSearchFilter


class TasksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TasksSearchFilter


class TasksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TasksSearchFilter


class TasksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TasksSearchFilter


class TasksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TasksSearchFilter


class TasksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TasksStringFilter


class TasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TasksStringFilter


class TasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TasksStringFilter


class TasksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TasksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TasksInCondition = TypedDict("TasksInCondition", {"in": TasksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TasksNotCondition = TypedDict("TasksNotCondition", {"not": "TasksCondition"}, total=False)
"""Negates the nested condition."""

TasksAndCondition = TypedDict("TasksAndCondition", {"and": "list[TasksCondition]"}, total=False)
"""True if all nested conditions are true."""

TasksOrCondition = TypedDict("TasksOrCondition", {"or": "list[TasksCondition]"}, total=False)
"""True if any nested condition is true."""

TasksAnyCondition = TypedDict("TasksAnyCondition", {"any": TasksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tasks condition types
TasksCondition = (
    TasksEqCondition
    | TasksNeqCondition
    | TasksGtCondition
    | TasksGteCondition
    | TasksLtCondition
    | TasksLteCondition
    | TasksInCondition
    | TasksLikeCondition
    | TasksFuzzyCondition
    | TasksKeywordCondition
    | TasksContainsCondition
    | TasksNotCondition
    | TasksAndCondition
    | TasksOrCondition
    | TasksAnyCondition
)


class TasksSearchQuery(TypedDict, total=False):
    """Search query for tasks entity."""
    filter: TasksCondition
    sort: list[TasksSortFilter]


# ===== TIME_ENTRIES SEARCH TYPES =====

class TimeEntriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering time_entries search queries."""
    billable: bool | None
    """Whether billable"""
    client: dict[str, Any] | None
    """Associated client"""
    created_at: str | None
    """When created"""
    hours: float | None
    """Hours logged"""
    id: int | None
    """Unique identifier"""
    is_billed: bool | None
    """Whether billed"""
    notes: str | None
    """Notes"""
    project: dict[str, Any] | None
    """Associated project"""
    spent_date: str | None
    """Date time was spent"""
    task: dict[str, Any] | None
    """Associated task"""
    updated_at: str | None
    """When last updated"""
    user: dict[str, Any] | None
    """Associated user"""


class TimeEntriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billable: list[bool]
    """Whether billable"""
    client: list[dict[str, Any]]
    """Associated client"""
    created_at: list[str]
    """When created"""
    hours: list[float]
    """Hours logged"""
    id: list[int]
    """Unique identifier"""
    is_billed: list[bool]
    """Whether billed"""
    notes: list[str]
    """Notes"""
    project: list[dict[str, Any]]
    """Associated project"""
    spent_date: list[str]
    """Date time was spent"""
    task: list[dict[str, Any]]
    """Associated task"""
    updated_at: list[str]
    """When last updated"""
    user: list[dict[str, Any]]
    """Associated user"""


class TimeEntriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billable: Any
    """Whether billable"""
    client: Any
    """Associated client"""
    created_at: Any
    """When created"""
    hours: Any
    """Hours logged"""
    id: Any
    """Unique identifier"""
    is_billed: Any
    """Whether billed"""
    notes: Any
    """Notes"""
    project: Any
    """Associated project"""
    spent_date: Any
    """Date time was spent"""
    task: Any
    """Associated task"""
    updated_at: Any
    """When last updated"""
    user: Any
    """Associated user"""


class TimeEntriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billable: str
    """Whether billable"""
    client: str
    """Associated client"""
    created_at: str
    """When created"""
    hours: str
    """Hours logged"""
    id: str
    """Unique identifier"""
    is_billed: str
    """Whether billed"""
    notes: str
    """Notes"""
    project: str
    """Associated project"""
    spent_date: str
    """Date time was spent"""
    task: str
    """Associated task"""
    updated_at: str
    """When last updated"""
    user: str
    """Associated user"""


class TimeEntriesSortFilter(TypedDict, total=False):
    """Available fields for sorting time_entries search results."""
    billable: AirbyteSortOrder
    """Whether billable"""
    client: AirbyteSortOrder
    """Associated client"""
    created_at: AirbyteSortOrder
    """When created"""
    hours: AirbyteSortOrder
    """Hours logged"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_billed: AirbyteSortOrder
    """Whether billed"""
    notes: AirbyteSortOrder
    """Notes"""
    project: AirbyteSortOrder
    """Associated project"""
    spent_date: AirbyteSortOrder
    """Date time was spent"""
    task: AirbyteSortOrder
    """Associated task"""
    updated_at: AirbyteSortOrder
    """When last updated"""
    user: AirbyteSortOrder
    """Associated user"""


# Entity-specific condition types for time_entries
class TimeEntriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TimeEntriesSearchFilter


class TimeEntriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TimeEntriesSearchFilter


class TimeEntriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TimeEntriesSearchFilter


class TimeEntriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TimeEntriesSearchFilter


class TimeEntriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TimeEntriesSearchFilter


class TimeEntriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TimeEntriesSearchFilter


class TimeEntriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TimeEntriesStringFilter


class TimeEntriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TimeEntriesStringFilter


class TimeEntriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TimeEntriesStringFilter


class TimeEntriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TimeEntriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TimeEntriesInCondition = TypedDict("TimeEntriesInCondition", {"in": TimeEntriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TimeEntriesNotCondition = TypedDict("TimeEntriesNotCondition", {"not": "TimeEntriesCondition"}, total=False)
"""Negates the nested condition."""

TimeEntriesAndCondition = TypedDict("TimeEntriesAndCondition", {"and": "list[TimeEntriesCondition]"}, total=False)
"""True if all nested conditions are true."""

TimeEntriesOrCondition = TypedDict("TimeEntriesOrCondition", {"or": "list[TimeEntriesCondition]"}, total=False)
"""True if any nested condition is true."""

TimeEntriesAnyCondition = TypedDict("TimeEntriesAnyCondition", {"any": TimeEntriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all time_entries condition types
TimeEntriesCondition = (
    TimeEntriesEqCondition
    | TimeEntriesNeqCondition
    | TimeEntriesGtCondition
    | TimeEntriesGteCondition
    | TimeEntriesLtCondition
    | TimeEntriesLteCondition
    | TimeEntriesInCondition
    | TimeEntriesLikeCondition
    | TimeEntriesFuzzyCondition
    | TimeEntriesKeywordCondition
    | TimeEntriesContainsCondition
    | TimeEntriesNotCondition
    | TimeEntriesAndCondition
    | TimeEntriesOrCondition
    | TimeEntriesAnyCondition
)


class TimeEntriesSearchQuery(TypedDict, total=False):
    """Search query for time_entries entity."""
    filter: TimeEntriesCondition
    sort: list[TimeEntriesSortFilter]


# ===== TIME_PROJECTS SEARCH TYPES =====

class TimeProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering time_projects search queries."""
    billable_amount: float | None
    """Total billable amount"""
    billable_hours: float | None
    """Number of billable hours"""
    client_id: int | None
    """Client identifier"""
    client_name: str | None
    """Client name"""
    currency: str | None
    """Currency code"""
    project_id: int | None
    """Project identifier"""
    project_name: str | None
    """Project name"""
    total_hours: float | None
    """Total hours spent"""


class TimeProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billable_amount: list[float]
    """Total billable amount"""
    billable_hours: list[float]
    """Number of billable hours"""
    client_id: list[int]
    """Client identifier"""
    client_name: list[str]
    """Client name"""
    currency: list[str]
    """Currency code"""
    project_id: list[int]
    """Project identifier"""
    project_name: list[str]
    """Project name"""
    total_hours: list[float]
    """Total hours spent"""


class TimeProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billable_amount: Any
    """Total billable amount"""
    billable_hours: Any
    """Number of billable hours"""
    client_id: Any
    """Client identifier"""
    client_name: Any
    """Client name"""
    currency: Any
    """Currency code"""
    project_id: Any
    """Project identifier"""
    project_name: Any
    """Project name"""
    total_hours: Any
    """Total hours spent"""


class TimeProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billable_amount: str
    """Total billable amount"""
    billable_hours: str
    """Number of billable hours"""
    client_id: str
    """Client identifier"""
    client_name: str
    """Client name"""
    currency: str
    """Currency code"""
    project_id: str
    """Project identifier"""
    project_name: str
    """Project name"""
    total_hours: str
    """Total hours spent"""


class TimeProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting time_projects search results."""
    billable_amount: AirbyteSortOrder
    """Total billable amount"""
    billable_hours: AirbyteSortOrder
    """Number of billable hours"""
    client_id: AirbyteSortOrder
    """Client identifier"""
    client_name: AirbyteSortOrder
    """Client name"""
    currency: AirbyteSortOrder
    """Currency code"""
    project_id: AirbyteSortOrder
    """Project identifier"""
    project_name: AirbyteSortOrder
    """Project name"""
    total_hours: AirbyteSortOrder
    """Total hours spent"""


# Entity-specific condition types for time_projects
class TimeProjectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TimeProjectsSearchFilter


class TimeProjectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TimeProjectsSearchFilter


class TimeProjectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TimeProjectsSearchFilter


class TimeProjectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TimeProjectsSearchFilter


class TimeProjectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TimeProjectsSearchFilter


class TimeProjectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TimeProjectsSearchFilter


class TimeProjectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TimeProjectsStringFilter


class TimeProjectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TimeProjectsStringFilter


class TimeProjectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TimeProjectsStringFilter


class TimeProjectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TimeProjectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TimeProjectsInCondition = TypedDict("TimeProjectsInCondition", {"in": TimeProjectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TimeProjectsNotCondition = TypedDict("TimeProjectsNotCondition", {"not": "TimeProjectsCondition"}, total=False)
"""Negates the nested condition."""

TimeProjectsAndCondition = TypedDict("TimeProjectsAndCondition", {"and": "list[TimeProjectsCondition]"}, total=False)
"""True if all nested conditions are true."""

TimeProjectsOrCondition = TypedDict("TimeProjectsOrCondition", {"or": "list[TimeProjectsCondition]"}, total=False)
"""True if any nested condition is true."""

TimeProjectsAnyCondition = TypedDict("TimeProjectsAnyCondition", {"any": TimeProjectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all time_projects condition types
TimeProjectsCondition = (
    TimeProjectsEqCondition
    | TimeProjectsNeqCondition
    | TimeProjectsGtCondition
    | TimeProjectsGteCondition
    | TimeProjectsLtCondition
    | TimeProjectsLteCondition
    | TimeProjectsInCondition
    | TimeProjectsLikeCondition
    | TimeProjectsFuzzyCondition
    | TimeProjectsKeywordCondition
    | TimeProjectsContainsCondition
    | TimeProjectsNotCondition
    | TimeProjectsAndCondition
    | TimeProjectsOrCondition
    | TimeProjectsAnyCondition
)


class TimeProjectsSearchQuery(TypedDict, total=False):
    """Search query for time_projects entity."""
    filter: TimeProjectsCondition
    sort: list[TimeProjectsSortFilter]


# ===== TIME_TASKS SEARCH TYPES =====

class TimeTasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering time_tasks search queries."""
    billable_amount: float | None
    """Total billable amount"""
    billable_hours: float | None
    """Number of billable hours"""
    currency: str | None
    """Currency code"""
    task_id: int | None
    """Task identifier"""
    task_name: str | None
    """Task name"""
    total_hours: float | None
    """Total hours spent"""


class TimeTasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billable_amount: list[float]
    """Total billable amount"""
    billable_hours: list[float]
    """Number of billable hours"""
    currency: list[str]
    """Currency code"""
    task_id: list[int]
    """Task identifier"""
    task_name: list[str]
    """Task name"""
    total_hours: list[float]
    """Total hours spent"""


class TimeTasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billable_amount: Any
    """Total billable amount"""
    billable_hours: Any
    """Number of billable hours"""
    currency: Any
    """Currency code"""
    task_id: Any
    """Task identifier"""
    task_name: Any
    """Task name"""
    total_hours: Any
    """Total hours spent"""


class TimeTasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billable_amount: str
    """Total billable amount"""
    billable_hours: str
    """Number of billable hours"""
    currency: str
    """Currency code"""
    task_id: str
    """Task identifier"""
    task_name: str
    """Task name"""
    total_hours: str
    """Total hours spent"""


class TimeTasksSortFilter(TypedDict, total=False):
    """Available fields for sorting time_tasks search results."""
    billable_amount: AirbyteSortOrder
    """Total billable amount"""
    billable_hours: AirbyteSortOrder
    """Number of billable hours"""
    currency: AirbyteSortOrder
    """Currency code"""
    task_id: AirbyteSortOrder
    """Task identifier"""
    task_name: AirbyteSortOrder
    """Task name"""
    total_hours: AirbyteSortOrder
    """Total hours spent"""


# Entity-specific condition types for time_tasks
class TimeTasksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TimeTasksSearchFilter


class TimeTasksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TimeTasksSearchFilter


class TimeTasksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TimeTasksSearchFilter


class TimeTasksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TimeTasksSearchFilter


class TimeTasksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TimeTasksSearchFilter


class TimeTasksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TimeTasksSearchFilter


class TimeTasksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TimeTasksStringFilter


class TimeTasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TimeTasksStringFilter


class TimeTasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TimeTasksStringFilter


class TimeTasksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TimeTasksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TimeTasksInCondition = TypedDict("TimeTasksInCondition", {"in": TimeTasksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TimeTasksNotCondition = TypedDict("TimeTasksNotCondition", {"not": "TimeTasksCondition"}, total=False)
"""Negates the nested condition."""

TimeTasksAndCondition = TypedDict("TimeTasksAndCondition", {"and": "list[TimeTasksCondition]"}, total=False)
"""True if all nested conditions are true."""

TimeTasksOrCondition = TypedDict("TimeTasksOrCondition", {"or": "list[TimeTasksCondition]"}, total=False)
"""True if any nested condition is true."""

TimeTasksAnyCondition = TypedDict("TimeTasksAnyCondition", {"any": TimeTasksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all time_tasks condition types
TimeTasksCondition = (
    TimeTasksEqCondition
    | TimeTasksNeqCondition
    | TimeTasksGtCondition
    | TimeTasksGteCondition
    | TimeTasksLtCondition
    | TimeTasksLteCondition
    | TimeTasksInCondition
    | TimeTasksLikeCondition
    | TimeTasksFuzzyCondition
    | TimeTasksKeywordCondition
    | TimeTasksContainsCondition
    | TimeTasksNotCondition
    | TimeTasksAndCondition
    | TimeTasksOrCondition
    | TimeTasksAnyCondition
)


class TimeTasksSearchQuery(TypedDict, total=False):
    """Search query for time_tasks entity."""
    filter: TimeTasksCondition
    sort: list[TimeTasksSortFilter]


# ===== USER_ASSIGNMENTS SEARCH TYPES =====

class UserAssignmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering user_assignments search queries."""
    budget: float | None
    """Budget"""
    created_at: str | None
    """When created"""
    hourly_rate: float | None
    """Hourly rate"""
    id: int | None
    """Unique identifier"""
    is_active: bool | None
    """Whether active"""
    is_project_manager: bool | None
    """Whether project manager"""
    project: dict[str, Any] | None
    """Associated project"""
    updated_at: str | None
    """When last updated"""
    user: dict[str, Any] | None
    """Associated user"""


class UserAssignmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    budget: list[float]
    """Budget"""
    created_at: list[str]
    """When created"""
    hourly_rate: list[float]
    """Hourly rate"""
    id: list[int]
    """Unique identifier"""
    is_active: list[bool]
    """Whether active"""
    is_project_manager: list[bool]
    """Whether project manager"""
    project: list[dict[str, Any]]
    """Associated project"""
    updated_at: list[str]
    """When last updated"""
    user: list[dict[str, Any]]
    """Associated user"""


class UserAssignmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    budget: Any
    """Budget"""
    created_at: Any
    """When created"""
    hourly_rate: Any
    """Hourly rate"""
    id: Any
    """Unique identifier"""
    is_active: Any
    """Whether active"""
    is_project_manager: Any
    """Whether project manager"""
    project: Any
    """Associated project"""
    updated_at: Any
    """When last updated"""
    user: Any
    """Associated user"""


class UserAssignmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    budget: str
    """Budget"""
    created_at: str
    """When created"""
    hourly_rate: str
    """Hourly rate"""
    id: str
    """Unique identifier"""
    is_active: str
    """Whether active"""
    is_project_manager: str
    """Whether project manager"""
    project: str
    """Associated project"""
    updated_at: str
    """When last updated"""
    user: str
    """Associated user"""


class UserAssignmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting user_assignments search results."""
    budget: AirbyteSortOrder
    """Budget"""
    created_at: AirbyteSortOrder
    """When created"""
    hourly_rate: AirbyteSortOrder
    """Hourly rate"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_active: AirbyteSortOrder
    """Whether active"""
    is_project_manager: AirbyteSortOrder
    """Whether project manager"""
    project: AirbyteSortOrder
    """Associated project"""
    updated_at: AirbyteSortOrder
    """When last updated"""
    user: AirbyteSortOrder
    """Associated user"""


# Entity-specific condition types for user_assignments
class UserAssignmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UserAssignmentsSearchFilter


class UserAssignmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UserAssignmentsSearchFilter


class UserAssignmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UserAssignmentsSearchFilter


class UserAssignmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UserAssignmentsSearchFilter


class UserAssignmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UserAssignmentsSearchFilter


class UserAssignmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UserAssignmentsSearchFilter


class UserAssignmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UserAssignmentsStringFilter


class UserAssignmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UserAssignmentsStringFilter


class UserAssignmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UserAssignmentsStringFilter


class UserAssignmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UserAssignmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UserAssignmentsInCondition = TypedDict("UserAssignmentsInCondition", {"in": UserAssignmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UserAssignmentsNotCondition = TypedDict("UserAssignmentsNotCondition", {"not": "UserAssignmentsCondition"}, total=False)
"""Negates the nested condition."""

UserAssignmentsAndCondition = TypedDict("UserAssignmentsAndCondition", {"and": "list[UserAssignmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

UserAssignmentsOrCondition = TypedDict("UserAssignmentsOrCondition", {"or": "list[UserAssignmentsCondition]"}, total=False)
"""True if any nested condition is true."""

UserAssignmentsAnyCondition = TypedDict("UserAssignmentsAnyCondition", {"any": UserAssignmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all user_assignments condition types
UserAssignmentsCondition = (
    UserAssignmentsEqCondition
    | UserAssignmentsNeqCondition
    | UserAssignmentsGtCondition
    | UserAssignmentsGteCondition
    | UserAssignmentsLtCondition
    | UserAssignmentsLteCondition
    | UserAssignmentsInCondition
    | UserAssignmentsLikeCondition
    | UserAssignmentsFuzzyCondition
    | UserAssignmentsKeywordCondition
    | UserAssignmentsContainsCondition
    | UserAssignmentsNotCondition
    | UserAssignmentsAndCondition
    | UserAssignmentsOrCondition
    | UserAssignmentsAnyCondition
)


class UserAssignmentsSearchQuery(TypedDict, total=False):
    """Search query for user_assignments entity."""
    filter: UserAssignmentsCondition
    sort: list[UserAssignmentsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    avatar_url: str | None
    """Avatar URL"""
    cost_rate: float | None
    """Cost rate"""
    created_at: str | None
    """When created"""
    default_hourly_rate: float | None
    """Default hourly rate"""
    email: str | None
    """Email address"""
    first_name: str | None
    """First name"""
    id: int | None
    """Unique identifier"""
    is_active: bool | None
    """Whether active"""
    is_contractor: bool | None
    """Whether contractor"""
    last_name: str | None
    """Last name"""
    roles: list[Any] | None
    """Assigned roles"""
    telephone: str | None
    """Phone number"""
    timezone: str | None
    """Timezone"""
    updated_at: str | None
    """When last updated"""
    weekly_capacity: int | None
    """Weekly capacity in seconds"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    avatar_url: list[str]
    """Avatar URL"""
    cost_rate: list[float]
    """Cost rate"""
    created_at: list[str]
    """When created"""
    default_hourly_rate: list[float]
    """Default hourly rate"""
    email: list[str]
    """Email address"""
    first_name: list[str]
    """First name"""
    id: list[int]
    """Unique identifier"""
    is_active: list[bool]
    """Whether active"""
    is_contractor: list[bool]
    """Whether contractor"""
    last_name: list[str]
    """Last name"""
    roles: list[list[Any]]
    """Assigned roles"""
    telephone: list[str]
    """Phone number"""
    timezone: list[str]
    """Timezone"""
    updated_at: list[str]
    """When last updated"""
    weekly_capacity: list[int]
    """Weekly capacity in seconds"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    avatar_url: Any
    """Avatar URL"""
    cost_rate: Any
    """Cost rate"""
    created_at: Any
    """When created"""
    default_hourly_rate: Any
    """Default hourly rate"""
    email: Any
    """Email address"""
    first_name: Any
    """First name"""
    id: Any
    """Unique identifier"""
    is_active: Any
    """Whether active"""
    is_contractor: Any
    """Whether contractor"""
    last_name: Any
    """Last name"""
    roles: Any
    """Assigned roles"""
    telephone: Any
    """Phone number"""
    timezone: Any
    """Timezone"""
    updated_at: Any
    """When last updated"""
    weekly_capacity: Any
    """Weekly capacity in seconds"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    avatar_url: str
    """Avatar URL"""
    cost_rate: str
    """Cost rate"""
    created_at: str
    """When created"""
    default_hourly_rate: str
    """Default hourly rate"""
    email: str
    """Email address"""
    first_name: str
    """First name"""
    id: str
    """Unique identifier"""
    is_active: str
    """Whether active"""
    is_contractor: str
    """Whether contractor"""
    last_name: str
    """Last name"""
    roles: str
    """Assigned roles"""
    telephone: str
    """Phone number"""
    timezone: str
    """Timezone"""
    updated_at: str
    """When last updated"""
    weekly_capacity: str
    """Weekly capacity in seconds"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    avatar_url: AirbyteSortOrder
    """Avatar URL"""
    cost_rate: AirbyteSortOrder
    """Cost rate"""
    created_at: AirbyteSortOrder
    """When created"""
    default_hourly_rate: AirbyteSortOrder
    """Default hourly rate"""
    email: AirbyteSortOrder
    """Email address"""
    first_name: AirbyteSortOrder
    """First name"""
    id: AirbyteSortOrder
    """Unique identifier"""
    is_active: AirbyteSortOrder
    """Whether active"""
    is_contractor: AirbyteSortOrder
    """Whether contractor"""
    last_name: AirbyteSortOrder
    """Last name"""
    roles: AirbyteSortOrder
    """Assigned roles"""
    telephone: AirbyteSortOrder
    """Phone number"""
    timezone: AirbyteSortOrder
    """Timezone"""
    updated_at: AirbyteSortOrder
    """When last updated"""
    weekly_capacity: AirbyteSortOrder
    """Weekly capacity in seconds"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
