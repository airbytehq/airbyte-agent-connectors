"""
Type definitions for zoho-crm connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class LeadsCreateParamsDataItem(TypedDict):
    """Nested schema for LeadsCreateParams.data_item"""
    First_Name: NotRequired[str]
    Last_Name: str
    Email: NotRequired[str]
    Phone: NotRequired[str]
    Mobile: NotRequired[str]
    Company: NotRequired[str]
    Title: NotRequired[str]
    Lead_Source: NotRequired[str]
    Industry: NotRequired[str]
    Annual_Revenue: NotRequired[float]
    No_of_Employees: NotRequired[int]
    Rating: NotRequired[str]
    Lead_Status: NotRequired[str]
    Website: NotRequired[str]
    Street: NotRequired[str]
    City: NotRequired[str]
    State: NotRequired[str]
    Zip_Code: NotRequired[str]
    Country: NotRequired[str]
    Description: NotRequired[str]

class LeadsUpdateParamsDataItem(TypedDict):
    """Nested schema for LeadsUpdateParams.data_item"""
    First_Name: NotRequired[str]
    Last_Name: NotRequired[str]
    Email: NotRequired[str]
    Phone: NotRequired[str]
    Mobile: NotRequired[str]
    Company: NotRequired[str]
    Title: NotRequired[str]
    Lead_Source: NotRequired[str]
    Industry: NotRequired[str]
    Annual_Revenue: NotRequired[float]
    No_of_Employees: NotRequired[int]
    Rating: NotRequired[str]
    Lead_Status: NotRequired[str]
    Website: NotRequired[str]
    Street: NotRequired[str]
    City: NotRequired[str]
    State: NotRequired[str]
    Zip_Code: NotRequired[str]
    Country: NotRequired[str]
    Description: NotRequired[str]

class ContactsCreateParamsDataItem(TypedDict):
    """Nested schema for ContactsCreateParams.data_item"""
    First_Name: NotRequired[str]
    Last_Name: str
    Email: NotRequired[str]
    Phone: NotRequired[str]
    Mobile: NotRequired[str]
    Title: NotRequired[str]
    Department: NotRequired[str]
    Lead_Source: NotRequired[str]
    Date_of_Birth: NotRequired[str]
    Mailing_Street: NotRequired[str]
    Mailing_City: NotRequired[str]
    Mailing_State: NotRequired[str]
    Mailing_Zip: NotRequired[str]
    Mailing_Country: NotRequired[str]
    Description: NotRequired[str]

class ContactsUpdateParamsDataItem(TypedDict):
    """Nested schema for ContactsUpdateParams.data_item"""
    First_Name: NotRequired[str]
    Last_Name: NotRequired[str]
    Email: NotRequired[str]
    Phone: NotRequired[str]
    Mobile: NotRequired[str]
    Title: NotRequired[str]
    Department: NotRequired[str]
    Lead_Source: NotRequired[str]
    Date_of_Birth: NotRequired[str]
    Mailing_Street: NotRequired[str]
    Mailing_City: NotRequired[str]
    Mailing_State: NotRequired[str]
    Mailing_Zip: NotRequired[str]
    Mailing_Country: NotRequired[str]
    Description: NotRequired[str]

class AccountsCreateParamsDataItem(TypedDict):
    """Nested schema for AccountsCreateParams.data_item"""
    Account_Name: str
    Account_Number: NotRequired[str]
    Account_Type: NotRequired[str]
    Industry: NotRequired[str]
    Annual_Revenue: NotRequired[float]
    Employees: NotRequired[int]
    Phone: NotRequired[str]
    Website: NotRequired[str]
    Ownership: NotRequired[str]
    Rating: NotRequired[str]
    Billing_Street: NotRequired[str]
    Billing_City: NotRequired[str]
    Billing_State: NotRequired[str]
    Billing_Code: NotRequired[str]
    Billing_Country: NotRequired[str]
    Shipping_Street: NotRequired[str]
    Shipping_City: NotRequired[str]
    Shipping_State: NotRequired[str]
    Shipping_Code: NotRequired[str]
    Shipping_Country: NotRequired[str]
    Description: NotRequired[str]

class AccountsUpdateParamsDataItem(TypedDict):
    """Nested schema for AccountsUpdateParams.data_item"""
    Account_Name: NotRequired[str]
    Account_Number: NotRequired[str]
    Account_Type: NotRequired[str]
    Industry: NotRequired[str]
    Annual_Revenue: NotRequired[float]
    Employees: NotRequired[int]
    Phone: NotRequired[str]
    Website: NotRequired[str]
    Ownership: NotRequired[str]
    Rating: NotRequired[str]
    Billing_Street: NotRequired[str]
    Billing_City: NotRequired[str]
    Billing_State: NotRequired[str]
    Billing_Code: NotRequired[str]
    Billing_Country: NotRequired[str]
    Shipping_Street: NotRequired[str]
    Shipping_City: NotRequired[str]
    Shipping_State: NotRequired[str]
    Shipping_Code: NotRequired[str]
    Shipping_Country: NotRequired[str]
    Description: NotRequired[str]

class DealsCreateParamsDataItem(TypedDict):
    """Nested schema for DealsCreateParams.data_item"""
    Deal_Name: str
    Amount: NotRequired[float]
    Stage: str
    Probability: NotRequired[int]
    Closing_Date: str
    Type: NotRequired[str]
    Next_Step: NotRequired[str]
    Lead_Source: NotRequired[str]
    Description: NotRequired[str]

class DealsUpdateParamsDataItem(TypedDict):
    """Nested schema for DealsUpdateParams.data_item"""
    Deal_Name: NotRequired[str]
    Amount: NotRequired[float]
    Stage: NotRequired[str]
    Probability: NotRequired[int]
    Closing_Date: NotRequired[str]
    Type: NotRequired[str]
    Next_Step: NotRequired[str]
    Lead_Source: NotRequired[str]
    Description: NotRequired[str]

class TasksCreateParamsDataItem(TypedDict):
    """Nested schema for TasksCreateParams.data_item"""
    Subject: str
    Due_Date: NotRequired[str]
    Status: NotRequired[str]
    Priority: NotRequired[str]
    Send_Notification_Email: NotRequired[bool]
    Description: NotRequired[str]

class TasksUpdateParamsDataItem(TypedDict):
    """Nested schema for TasksUpdateParams.data_item"""
    Subject: NotRequired[str]
    Due_Date: NotRequired[str]
    Status: NotRequired[str]
    Priority: NotRequired[str]
    Send_Notification_Email: NotRequired[bool]
    Description: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class LeadsListParams(TypedDict):
    """Parameters for leads.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class LeadsCreateParams(TypedDict):
    """Parameters for leads.create operation"""
    data: list[LeadsCreateParamsDataItem]

class LeadsGetParams(TypedDict):
    """Parameters for leads.get operation"""
    id: str

class LeadsUpdateParams(TypedDict):
    """Parameters for leads.update operation"""
    data: list[LeadsUpdateParamsDataItem]
    id: str

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ContactsCreateParams(TypedDict):
    """Parameters for contacts.create operation"""
    data: list[ContactsCreateParamsDataItem]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class ContactsUpdateParams(TypedDict):
    """Parameters for contacts.update operation"""
    data: list[ContactsUpdateParamsDataItem]
    id: str

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class AccountsCreateParams(TypedDict):
    """Parameters for accounts.create operation"""
    data: list[AccountsCreateParamsDataItem]

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str

class AccountsUpdateParams(TypedDict):
    """Parameters for accounts.update operation"""
    data: list[AccountsUpdateParamsDataItem]
    id: str

class DealsListParams(TypedDict):
    """Parameters for deals.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class DealsCreateParams(TypedDict):
    """Parameters for deals.create operation"""
    data: list[DealsCreateParamsDataItem]

class DealsGetParams(TypedDict):
    """Parameters for deals.get operation"""
    id: str

class DealsUpdateParams(TypedDict):
    """Parameters for deals.update operation"""
    data: list[DealsUpdateParamsDataItem]
    id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    id: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class TasksCreateParams(TypedDict):
    """Parameters for tasks.create operation"""
    data: list[TasksCreateParamsDataItem]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    id: str

class TasksUpdateParams(TypedDict):
    """Parameters for tasks.update operation"""
    data: list[TasksUpdateParamsDataItem]
    id: str

class EventsListParams(TypedDict):
    """Parameters for events.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class EventsGetParams(TypedDict):
    """Parameters for events.get operation"""
    id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    id: str

class ProductsListParams(TypedDict):
    """Parameters for products.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ProductsGetParams(TypedDict):
    """Parameters for products.get operation"""
    id: str

class QuotesListParams(TypedDict):
    """Parameters for quotes.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class QuotesGetParams(TypedDict):
    """Parameters for quotes.get operation"""
    id: str

class InvoicesListParams(TypedDict):
    """Parameters for invoices.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    page_token: NotRequired[str]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class InvoicesGetParams(TypedDict):
    """Parameters for invoices.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== LEADS SEARCH TYPES =====

class LeadsSearchFilter(TypedDict, total=False):
    """Available fields for filtering leads search queries."""
    id: str
    """Unique record identifier"""
    first_name: str | None
    """Lead's first name"""
    last_name: str | None
    """Lead's last name"""
    full_name: str | None
    """Lead's full name"""
    email: str | None
    """Lead's email address"""
    phone: str | None
    """Lead's phone number"""
    mobile: str | None
    """Lead's mobile number"""
    company: str | None
    """Company the lead is associated with"""
    title: str | None
    """Lead's job title"""
    lead_source: str | None
    """Source from which the lead was generated"""
    industry: str | None
    """Industry the lead belongs to"""
    annual_revenue: float | None
    """Annual revenue of the lead's company"""
    no_of_employees: int | None
    """Number of employees in the lead's company"""
    rating: str | None
    """Lead rating"""
    lead_status: str | None
    """Current status of the lead"""
    website: str | None
    """Lead's website URL"""
    city: str | None
    """Lead's city"""
    state: str | None
    """Lead's state or province"""
    country: str | None
    """Lead's country"""
    description: str | None
    """Description or notes about the lead"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class LeadsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    first_name: list[str]
    """Lead's first name"""
    last_name: list[str]
    """Lead's last name"""
    full_name: list[str]
    """Lead's full name"""
    email: list[str]
    """Lead's email address"""
    phone: list[str]
    """Lead's phone number"""
    mobile: list[str]
    """Lead's mobile number"""
    company: list[str]
    """Company the lead is associated with"""
    title: list[str]
    """Lead's job title"""
    lead_source: list[str]
    """Source from which the lead was generated"""
    industry: list[str]
    """Industry the lead belongs to"""
    annual_revenue: list[float]
    """Annual revenue of the lead's company"""
    no_of_employees: list[int]
    """Number of employees in the lead's company"""
    rating: list[str]
    """Lead rating"""
    lead_status: list[str]
    """Current status of the lead"""
    website: list[str]
    """Lead's website URL"""
    city: list[str]
    """Lead's city"""
    state: list[str]
    """Lead's state or province"""
    country: list[str]
    """Lead's country"""
    description: list[str]
    """Description or notes about the lead"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class LeadsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    first_name: Any
    """Lead's first name"""
    last_name: Any
    """Lead's last name"""
    full_name: Any
    """Lead's full name"""
    email: Any
    """Lead's email address"""
    phone: Any
    """Lead's phone number"""
    mobile: Any
    """Lead's mobile number"""
    company: Any
    """Company the lead is associated with"""
    title: Any
    """Lead's job title"""
    lead_source: Any
    """Source from which the lead was generated"""
    industry: Any
    """Industry the lead belongs to"""
    annual_revenue: Any
    """Annual revenue of the lead's company"""
    no_of_employees: Any
    """Number of employees in the lead's company"""
    rating: Any
    """Lead rating"""
    lead_status: Any
    """Current status of the lead"""
    website: Any
    """Lead's website URL"""
    city: Any
    """Lead's city"""
    state: Any
    """Lead's state or province"""
    country: Any
    """Lead's country"""
    description: Any
    """Description or notes about the lead"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class LeadsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    first_name: str
    """Lead's first name"""
    last_name: str
    """Lead's last name"""
    full_name: str
    """Lead's full name"""
    email: str
    """Lead's email address"""
    phone: str
    """Lead's phone number"""
    mobile: str
    """Lead's mobile number"""
    company: str
    """Company the lead is associated with"""
    title: str
    """Lead's job title"""
    lead_source: str
    """Source from which the lead was generated"""
    industry: str
    """Industry the lead belongs to"""
    annual_revenue: str
    """Annual revenue of the lead's company"""
    no_of_employees: str
    """Number of employees in the lead's company"""
    rating: str
    """Lead rating"""
    lead_status: str
    """Current status of the lead"""
    website: str
    """Lead's website URL"""
    city: str
    """Lead's city"""
    state: str
    """Lead's state or province"""
    country: str
    """Lead's country"""
    description: str
    """Description or notes about the lead"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class LeadsSortFilter(TypedDict, total=False):
    """Available fields for sorting leads search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    first_name: AirbyteSortOrder
    """Lead's first name"""
    last_name: AirbyteSortOrder
    """Lead's last name"""
    full_name: AirbyteSortOrder
    """Lead's full name"""
    email: AirbyteSortOrder
    """Lead's email address"""
    phone: AirbyteSortOrder
    """Lead's phone number"""
    mobile: AirbyteSortOrder
    """Lead's mobile number"""
    company: AirbyteSortOrder
    """Company the lead is associated with"""
    title: AirbyteSortOrder
    """Lead's job title"""
    lead_source: AirbyteSortOrder
    """Source from which the lead was generated"""
    industry: AirbyteSortOrder
    """Industry the lead belongs to"""
    annual_revenue: AirbyteSortOrder
    """Annual revenue of the lead's company"""
    no_of_employees: AirbyteSortOrder
    """Number of employees in the lead's company"""
    rating: AirbyteSortOrder
    """Lead rating"""
    lead_status: AirbyteSortOrder
    """Current status of the lead"""
    website: AirbyteSortOrder
    """Lead's website URL"""
    city: AirbyteSortOrder
    """Lead's city"""
    state: AirbyteSortOrder
    """Lead's state or province"""
    country: AirbyteSortOrder
    """Lead's country"""
    description: AirbyteSortOrder
    """Description or notes about the lead"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for leads
class LeadsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LeadsSearchFilter


class LeadsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LeadsSearchFilter


class LeadsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LeadsSearchFilter


class LeadsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LeadsSearchFilter


class LeadsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LeadsSearchFilter


class LeadsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LeadsSearchFilter


class LeadsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LeadsStringFilter


class LeadsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LeadsStringFilter


class LeadsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LeadsStringFilter


class LeadsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LeadsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LeadsInCondition = TypedDict("LeadsInCondition", {"in": LeadsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LeadsNotCondition = TypedDict("LeadsNotCondition", {"not": "LeadsCondition"}, total=False)
"""Negates the nested condition."""

LeadsAndCondition = TypedDict("LeadsAndCondition", {"and": "list[LeadsCondition]"}, total=False)
"""True if all nested conditions are true."""

LeadsOrCondition = TypedDict("LeadsOrCondition", {"or": "list[LeadsCondition]"}, total=False)
"""True if any nested condition is true."""

LeadsAnyCondition = TypedDict("LeadsAnyCondition", {"any": LeadsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all leads condition types
LeadsCondition = (
    LeadsEqCondition
    | LeadsNeqCondition
    | LeadsGtCondition
    | LeadsGteCondition
    | LeadsLtCondition
    | LeadsLteCondition
    | LeadsInCondition
    | LeadsLikeCondition
    | LeadsFuzzyCondition
    | LeadsKeywordCondition
    | LeadsContainsCondition
    | LeadsNotCondition
    | LeadsAndCondition
    | LeadsOrCondition
    | LeadsAnyCondition
)


class LeadsSearchQuery(TypedDict, total=False):
    """Search query for leads entity."""
    filter: LeadsCondition
    sort: list[LeadsSortFilter]


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    id: str
    """Unique record identifier"""
    first_name: str | None
    """Contact's first name"""
    last_name: str | None
    """Contact's last name"""
    full_name: str | None
    """Contact's full name"""
    email: str | None
    """Contact's email address"""
    phone: str | None
    """Contact's phone number"""
    mobile: str | None
    """Contact's mobile number"""
    title: str | None
    """Contact's job title"""
    department: str | None
    """Department the contact belongs to"""
    lead_source: str | None
    """Source from which the contact was generated"""
    date_of_birth: str | None
    """Contact's date of birth"""
    mailing_city: str | None
    """Mailing address city"""
    mailing_state: str | None
    """Mailing address state or province"""
    mailing_country: str | None
    """Mailing address country"""
    description: str | None
    """Description or notes about the contact"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    first_name: list[str]
    """Contact's first name"""
    last_name: list[str]
    """Contact's last name"""
    full_name: list[str]
    """Contact's full name"""
    email: list[str]
    """Contact's email address"""
    phone: list[str]
    """Contact's phone number"""
    mobile: list[str]
    """Contact's mobile number"""
    title: list[str]
    """Contact's job title"""
    department: list[str]
    """Department the contact belongs to"""
    lead_source: list[str]
    """Source from which the contact was generated"""
    date_of_birth: list[str]
    """Contact's date of birth"""
    mailing_city: list[str]
    """Mailing address city"""
    mailing_state: list[str]
    """Mailing address state or province"""
    mailing_country: list[str]
    """Mailing address country"""
    description: list[str]
    """Description or notes about the contact"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    first_name: Any
    """Contact's first name"""
    last_name: Any
    """Contact's last name"""
    full_name: Any
    """Contact's full name"""
    email: Any
    """Contact's email address"""
    phone: Any
    """Contact's phone number"""
    mobile: Any
    """Contact's mobile number"""
    title: Any
    """Contact's job title"""
    department: Any
    """Department the contact belongs to"""
    lead_source: Any
    """Source from which the contact was generated"""
    date_of_birth: Any
    """Contact's date of birth"""
    mailing_city: Any
    """Mailing address city"""
    mailing_state: Any
    """Mailing address state or province"""
    mailing_country: Any
    """Mailing address country"""
    description: Any
    """Description or notes about the contact"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    first_name: str
    """Contact's first name"""
    last_name: str
    """Contact's last name"""
    full_name: str
    """Contact's full name"""
    email: str
    """Contact's email address"""
    phone: str
    """Contact's phone number"""
    mobile: str
    """Contact's mobile number"""
    title: str
    """Contact's job title"""
    department: str
    """Department the contact belongs to"""
    lead_source: str
    """Source from which the contact was generated"""
    date_of_birth: str
    """Contact's date of birth"""
    mailing_city: str
    """Mailing address city"""
    mailing_state: str
    """Mailing address state or province"""
    mailing_country: str
    """Mailing address country"""
    description: str
    """Description or notes about the contact"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    first_name: AirbyteSortOrder
    """Contact's first name"""
    last_name: AirbyteSortOrder
    """Contact's last name"""
    full_name: AirbyteSortOrder
    """Contact's full name"""
    email: AirbyteSortOrder
    """Contact's email address"""
    phone: AirbyteSortOrder
    """Contact's phone number"""
    mobile: AirbyteSortOrder
    """Contact's mobile number"""
    title: AirbyteSortOrder
    """Contact's job title"""
    department: AirbyteSortOrder
    """Department the contact belongs to"""
    lead_source: AirbyteSortOrder
    """Source from which the contact was generated"""
    date_of_birth: AirbyteSortOrder
    """Contact's date of birth"""
    mailing_city: AirbyteSortOrder
    """Mailing address city"""
    mailing_state: AirbyteSortOrder
    """Mailing address state or province"""
    mailing_country: AirbyteSortOrder
    """Mailing address country"""
    description: AirbyteSortOrder
    """Description or notes about the contact"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


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


# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    id: str
    """Unique record identifier"""
    account_name: str | None
    """Name of the account or company"""
    account_number: str | None
    """Account number"""
    account_type: str | None
    """Type of account (e.g., Analyst, Competitor, Customer)"""
    industry: str | None
    """Industry the account belongs to"""
    annual_revenue: float | None
    """Annual revenue of the account"""
    employees: int | None
    """Number of employees"""
    phone: str | None
    """Account phone number"""
    website: str | None
    """Account website URL"""
    ownership: str | None
    """Ownership type (e.g., Public, Private)"""
    rating: str | None
    """Account rating"""
    billing_city: str | None
    """Billing address city"""
    billing_state: str | None
    """Billing address state or province"""
    billing_country: str | None
    """Billing address country"""
    description: str | None
    """Description or notes about the account"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    account_name: list[str]
    """Name of the account or company"""
    account_number: list[str]
    """Account number"""
    account_type: list[str]
    """Type of account (e.g., Analyst, Competitor, Customer)"""
    industry: list[str]
    """Industry the account belongs to"""
    annual_revenue: list[float]
    """Annual revenue of the account"""
    employees: list[int]
    """Number of employees"""
    phone: list[str]
    """Account phone number"""
    website: list[str]
    """Account website URL"""
    ownership: list[str]
    """Ownership type (e.g., Public, Private)"""
    rating: list[str]
    """Account rating"""
    billing_city: list[str]
    """Billing address city"""
    billing_state: list[str]
    """Billing address state or province"""
    billing_country: list[str]
    """Billing address country"""
    description: list[str]
    """Description or notes about the account"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    account_name: Any
    """Name of the account or company"""
    account_number: Any
    """Account number"""
    account_type: Any
    """Type of account (e.g., Analyst, Competitor, Customer)"""
    industry: Any
    """Industry the account belongs to"""
    annual_revenue: Any
    """Annual revenue of the account"""
    employees: Any
    """Number of employees"""
    phone: Any
    """Account phone number"""
    website: Any
    """Account website URL"""
    ownership: Any
    """Ownership type (e.g., Public, Private)"""
    rating: Any
    """Account rating"""
    billing_city: Any
    """Billing address city"""
    billing_state: Any
    """Billing address state or province"""
    billing_country: Any
    """Billing address country"""
    description: Any
    """Description or notes about the account"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    account_name: str
    """Name of the account or company"""
    account_number: str
    """Account number"""
    account_type: str
    """Type of account (e.g., Analyst, Competitor, Customer)"""
    industry: str
    """Industry the account belongs to"""
    annual_revenue: str
    """Annual revenue of the account"""
    employees: str
    """Number of employees"""
    phone: str
    """Account phone number"""
    website: str
    """Account website URL"""
    ownership: str
    """Ownership type (e.g., Public, Private)"""
    rating: str
    """Account rating"""
    billing_city: str
    """Billing address city"""
    billing_state: str
    """Billing address state or province"""
    billing_country: str
    """Billing address country"""
    description: str
    """Description or notes about the account"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    account_name: AirbyteSortOrder
    """Name of the account or company"""
    account_number: AirbyteSortOrder
    """Account number"""
    account_type: AirbyteSortOrder
    """Type of account (e.g., Analyst, Competitor, Customer)"""
    industry: AirbyteSortOrder
    """Industry the account belongs to"""
    annual_revenue: AirbyteSortOrder
    """Annual revenue of the account"""
    employees: AirbyteSortOrder
    """Number of employees"""
    phone: AirbyteSortOrder
    """Account phone number"""
    website: AirbyteSortOrder
    """Account website URL"""
    ownership: AirbyteSortOrder
    """Ownership type (e.g., Public, Private)"""
    rating: AirbyteSortOrder
    """Account rating"""
    billing_city: AirbyteSortOrder
    """Billing address city"""
    billing_state: AirbyteSortOrder
    """Billing address state or province"""
    billing_country: AirbyteSortOrder
    """Billing address country"""
    description: AirbyteSortOrder
    """Description or notes about the account"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for accounts
class AccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountsSearchFilter


class AccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountsSearchFilter


class AccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountsSearchFilter


class AccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountsSearchFilter


class AccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountsSearchFilter


class AccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountsSearchFilter


class AccountsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AccountsStringFilter


class AccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountsStringFilter


class AccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountsStringFilter


class AccountsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountsInCondition = TypedDict("AccountsInCondition", {"in": AccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountsNotCondition = TypedDict("AccountsNotCondition", {"not": "AccountsCondition"}, total=False)
"""Negates the nested condition."""

AccountsAndCondition = TypedDict("AccountsAndCondition", {"and": "list[AccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountsOrCondition = TypedDict("AccountsOrCondition", {"or": "list[AccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AccountsAnyCondition = TypedDict("AccountsAnyCondition", {"any": AccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all accounts condition types
AccountsCondition = (
    AccountsEqCondition
    | AccountsNeqCondition
    | AccountsGtCondition
    | AccountsGteCondition
    | AccountsLtCondition
    | AccountsLteCondition
    | AccountsInCondition
    | AccountsLikeCondition
    | AccountsFuzzyCondition
    | AccountsKeywordCondition
    | AccountsContainsCondition
    | AccountsNotCondition
    | AccountsAndCondition
    | AccountsOrCondition
    | AccountsAnyCondition
)


class AccountsSearchQuery(TypedDict, total=False):
    """Search query for accounts entity."""
    filter: AccountsCondition
    sort: list[AccountsSortFilter]


# ===== DEALS SEARCH TYPES =====

class DealsSearchFilter(TypedDict, total=False):
    """Available fields for filtering deals search queries."""
    id: str
    """Unique record identifier"""
    deal_name: str | None
    """Name of the deal"""
    amount: float | None
    """Monetary value of the deal"""
    stage: str | None
    """Current stage of the deal in the pipeline"""
    probability: int | None
    """Probability of closing the deal (percentage)"""
    closing_date: str | None
    """Expected closing date"""
    type_: str | None
    """Type of deal (e.g., New Business, Existing Business)"""
    next_step: str | None
    """Next step in the deal process"""
    lead_source: str | None
    """Source from which the deal originated"""
    description: str | None
    """Description or notes about the deal"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class DealsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    deal_name: list[str]
    """Name of the deal"""
    amount: list[float]
    """Monetary value of the deal"""
    stage: list[str]
    """Current stage of the deal in the pipeline"""
    probability: list[int]
    """Probability of closing the deal (percentage)"""
    closing_date: list[str]
    """Expected closing date"""
    type_: list[str]
    """Type of deal (e.g., New Business, Existing Business)"""
    next_step: list[str]
    """Next step in the deal process"""
    lead_source: list[str]
    """Source from which the deal originated"""
    description: list[str]
    """Description or notes about the deal"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class DealsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    deal_name: Any
    """Name of the deal"""
    amount: Any
    """Monetary value of the deal"""
    stage: Any
    """Current stage of the deal in the pipeline"""
    probability: Any
    """Probability of closing the deal (percentage)"""
    closing_date: Any
    """Expected closing date"""
    type_: Any
    """Type of deal (e.g., New Business, Existing Business)"""
    next_step: Any
    """Next step in the deal process"""
    lead_source: Any
    """Source from which the deal originated"""
    description: Any
    """Description or notes about the deal"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class DealsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    deal_name: str
    """Name of the deal"""
    amount: str
    """Monetary value of the deal"""
    stage: str
    """Current stage of the deal in the pipeline"""
    probability: str
    """Probability of closing the deal (percentage)"""
    closing_date: str
    """Expected closing date"""
    type_: str
    """Type of deal (e.g., New Business, Existing Business)"""
    next_step: str
    """Next step in the deal process"""
    lead_source: str
    """Source from which the deal originated"""
    description: str
    """Description or notes about the deal"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class DealsSortFilter(TypedDict, total=False):
    """Available fields for sorting deals search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    deal_name: AirbyteSortOrder
    """Name of the deal"""
    amount: AirbyteSortOrder
    """Monetary value of the deal"""
    stage: AirbyteSortOrder
    """Current stage of the deal in the pipeline"""
    probability: AirbyteSortOrder
    """Probability of closing the deal (percentage)"""
    closing_date: AirbyteSortOrder
    """Expected closing date"""
    type_: AirbyteSortOrder
    """Type of deal (e.g., New Business, Existing Business)"""
    next_step: AirbyteSortOrder
    """Next step in the deal process"""
    lead_source: AirbyteSortOrder
    """Source from which the deal originated"""
    description: AirbyteSortOrder
    """Description or notes about the deal"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for deals
class DealsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DealsSearchFilter


class DealsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DealsSearchFilter


class DealsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DealsSearchFilter


class DealsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DealsSearchFilter


class DealsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DealsSearchFilter


class DealsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DealsSearchFilter


class DealsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DealsStringFilter


class DealsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DealsStringFilter


class DealsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DealsStringFilter


class DealsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DealsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DealsInCondition = TypedDict("DealsInCondition", {"in": DealsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DealsNotCondition = TypedDict("DealsNotCondition", {"not": "DealsCondition"}, total=False)
"""Negates the nested condition."""

DealsAndCondition = TypedDict("DealsAndCondition", {"and": "list[DealsCondition]"}, total=False)
"""True if all nested conditions are true."""

DealsOrCondition = TypedDict("DealsOrCondition", {"or": "list[DealsCondition]"}, total=False)
"""True if any nested condition is true."""

DealsAnyCondition = TypedDict("DealsAnyCondition", {"any": DealsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all deals condition types
DealsCondition = (
    DealsEqCondition
    | DealsNeqCondition
    | DealsGtCondition
    | DealsGteCondition
    | DealsLtCondition
    | DealsLteCondition
    | DealsInCondition
    | DealsLikeCondition
    | DealsFuzzyCondition
    | DealsKeywordCondition
    | DealsContainsCondition
    | DealsNotCondition
    | DealsAndCondition
    | DealsOrCondition
    | DealsAnyCondition
)


class DealsSearchQuery(TypedDict, total=False):
    """Search query for deals entity."""
    filter: DealsCondition
    sort: list[DealsSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    id: str
    """Unique record identifier"""
    campaign_name: str | None
    """Name of the campaign"""
    type_: str | None
    """Type of campaign (e.g., Email, Webinar, Conference)"""
    status: str | None
    """Current status of the campaign"""
    start_date: str | None
    """Campaign start date"""
    end_date: str | None
    """Campaign end date"""
    expected_revenue: float | None
    """Expected revenue from the campaign"""
    budgeted_cost: float | None
    """Budget allocated for the campaign"""
    actual_cost: float | None
    """Actual cost incurred"""
    num_sent: str | None
    """Number of campaign messages sent"""
    expected_response: int | None
    """Expected response count"""
    description: str | None
    """Description or notes about the campaign"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    campaign_name: list[str]
    """Name of the campaign"""
    type_: list[str]
    """Type of campaign (e.g., Email, Webinar, Conference)"""
    status: list[str]
    """Current status of the campaign"""
    start_date: list[str]
    """Campaign start date"""
    end_date: list[str]
    """Campaign end date"""
    expected_revenue: list[float]
    """Expected revenue from the campaign"""
    budgeted_cost: list[float]
    """Budget allocated for the campaign"""
    actual_cost: list[float]
    """Actual cost incurred"""
    num_sent: list[str]
    """Number of campaign messages sent"""
    expected_response: list[int]
    """Expected response count"""
    description: list[str]
    """Description or notes about the campaign"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    campaign_name: Any
    """Name of the campaign"""
    type_: Any
    """Type of campaign (e.g., Email, Webinar, Conference)"""
    status: Any
    """Current status of the campaign"""
    start_date: Any
    """Campaign start date"""
    end_date: Any
    """Campaign end date"""
    expected_revenue: Any
    """Expected revenue from the campaign"""
    budgeted_cost: Any
    """Budget allocated for the campaign"""
    actual_cost: Any
    """Actual cost incurred"""
    num_sent: Any
    """Number of campaign messages sent"""
    expected_response: Any
    """Expected response count"""
    description: Any
    """Description or notes about the campaign"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    campaign_name: str
    """Name of the campaign"""
    type_: str
    """Type of campaign (e.g., Email, Webinar, Conference)"""
    status: str
    """Current status of the campaign"""
    start_date: str
    """Campaign start date"""
    end_date: str
    """Campaign end date"""
    expected_revenue: str
    """Expected revenue from the campaign"""
    budgeted_cost: str
    """Budget allocated for the campaign"""
    actual_cost: str
    """Actual cost incurred"""
    num_sent: str
    """Number of campaign messages sent"""
    expected_response: str
    """Expected response count"""
    description: str
    """Description or notes about the campaign"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    campaign_name: AirbyteSortOrder
    """Name of the campaign"""
    type_: AirbyteSortOrder
    """Type of campaign (e.g., Email, Webinar, Conference)"""
    status: AirbyteSortOrder
    """Current status of the campaign"""
    start_date: AirbyteSortOrder
    """Campaign start date"""
    end_date: AirbyteSortOrder
    """Campaign end date"""
    expected_revenue: AirbyteSortOrder
    """Expected revenue from the campaign"""
    budgeted_cost: AirbyteSortOrder
    """Budget allocated for the campaign"""
    actual_cost: AirbyteSortOrder
    """Actual cost incurred"""
    num_sent: AirbyteSortOrder
    """Number of campaign messages sent"""
    expected_response: AirbyteSortOrder
    """Expected response count"""
    description: AirbyteSortOrder
    """Description or notes about the campaign"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for campaigns
class CampaignsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignsSearchFilter


class CampaignsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignsSearchFilter


class CampaignsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignsSearchFilter


class CampaignsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignsSearchFilter


class CampaignsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignsSearchFilter


class CampaignsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignsSearchFilter


class CampaignsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignsInCondition = TypedDict("CampaignsInCondition", {"in": CampaignsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignsNotCondition = TypedDict("CampaignsNotCondition", {"not": "CampaignsCondition"}, total=False)
"""Negates the nested condition."""

CampaignsAndCondition = TypedDict("CampaignsAndCondition", {"and": "list[CampaignsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignsOrCondition = TypedDict("CampaignsOrCondition", {"or": "list[CampaignsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignsAnyCondition = TypedDict("CampaignsAnyCondition", {"any": CampaignsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaigns condition types
CampaignsCondition = (
    CampaignsEqCondition
    | CampaignsNeqCondition
    | CampaignsGtCondition
    | CampaignsGteCondition
    | CampaignsLtCondition
    | CampaignsLteCondition
    | CampaignsInCondition
    | CampaignsLikeCondition
    | CampaignsFuzzyCondition
    | CampaignsKeywordCondition
    | CampaignsContainsCondition
    | CampaignsNotCondition
    | CampaignsAndCondition
    | CampaignsOrCondition
    | CampaignsAnyCondition
)


class CampaignsSearchQuery(TypedDict, total=False):
    """Search query for campaigns entity."""
    filter: CampaignsCondition
    sort: list[CampaignsSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    id: str
    """Unique record identifier"""
    subject: str | None
    """Subject or title of the task"""
    due_date: str | None
    """Due date for the task"""
    status: str | None
    """Current status (e.g., Not Started, In Progress, Completed)"""
    priority: str | None
    """Priority level (e.g., High, Highest, Low, Lowest, Normal)"""
    send_notification_email: bool | None
    """Whether to send a notification email"""
    description: str | None
    """Description or notes about the task"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""
    closed_time: str | None
    """Time the task was closed"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    subject: list[str]
    """Subject or title of the task"""
    due_date: list[str]
    """Due date for the task"""
    status: list[str]
    """Current status (e.g., Not Started, In Progress, Completed)"""
    priority: list[str]
    """Priority level (e.g., High, Highest, Low, Lowest, Normal)"""
    send_notification_email: list[bool]
    """Whether to send a notification email"""
    description: list[str]
    """Description or notes about the task"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""
    closed_time: list[str]
    """Time the task was closed"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    subject: Any
    """Subject or title of the task"""
    due_date: Any
    """Due date for the task"""
    status: Any
    """Current status (e.g., Not Started, In Progress, Completed)"""
    priority: Any
    """Priority level (e.g., High, Highest, Low, Lowest, Normal)"""
    send_notification_email: Any
    """Whether to send a notification email"""
    description: Any
    """Description or notes about the task"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""
    closed_time: Any
    """Time the task was closed"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    subject: str
    """Subject or title of the task"""
    due_date: str
    """Due date for the task"""
    status: str
    """Current status (e.g., Not Started, In Progress, Completed)"""
    priority: str
    """Priority level (e.g., High, Highest, Low, Lowest, Normal)"""
    send_notification_email: str
    """Whether to send a notification email"""
    description: str
    """Description or notes about the task"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""
    closed_time: str
    """Time the task was closed"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    subject: AirbyteSortOrder
    """Subject or title of the task"""
    due_date: AirbyteSortOrder
    """Due date for the task"""
    status: AirbyteSortOrder
    """Current status (e.g., Not Started, In Progress, Completed)"""
    priority: AirbyteSortOrder
    """Priority level (e.g., High, Highest, Low, Lowest, Normal)"""
    send_notification_email: AirbyteSortOrder
    """Whether to send a notification email"""
    description: AirbyteSortOrder
    """Description or notes about the task"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""
    closed_time: AirbyteSortOrder
    """Time the task was closed"""


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


# ===== EVENTS SEARCH TYPES =====

class EventsSearchFilter(TypedDict, total=False):
    """Available fields for filtering events search queries."""
    id: str
    """Unique record identifier"""
    event_title: str | None
    """Title of the event"""
    start_date_time: str | None
    """Event start date and time"""
    end_date_time: str | None
    """Event end date and time"""
    all_day: bool | None
    """Whether this is an all-day event"""
    location: str | None
    """Event location"""
    description: str | None
    """Description or notes about the event"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class EventsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    event_title: list[str]
    """Title of the event"""
    start_date_time: list[str]
    """Event start date and time"""
    end_date_time: list[str]
    """Event end date and time"""
    all_day: list[bool]
    """Whether this is an all-day event"""
    location: list[str]
    """Event location"""
    description: list[str]
    """Description or notes about the event"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class EventsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    event_title: Any
    """Title of the event"""
    start_date_time: Any
    """Event start date and time"""
    end_date_time: Any
    """Event end date and time"""
    all_day: Any
    """Whether this is an all-day event"""
    location: Any
    """Event location"""
    description: Any
    """Description or notes about the event"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class EventsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    event_title: str
    """Title of the event"""
    start_date_time: str
    """Event start date and time"""
    end_date_time: str
    """Event end date and time"""
    all_day: str
    """Whether this is an all-day event"""
    location: str
    """Event location"""
    description: str
    """Description or notes about the event"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class EventsSortFilter(TypedDict, total=False):
    """Available fields for sorting events search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    event_title: AirbyteSortOrder
    """Title of the event"""
    start_date_time: AirbyteSortOrder
    """Event start date and time"""
    end_date_time: AirbyteSortOrder
    """Event end date and time"""
    all_day: AirbyteSortOrder
    """Whether this is an all-day event"""
    location: AirbyteSortOrder
    """Event location"""
    description: AirbyteSortOrder
    """Description or notes about the event"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for events
class EventsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EventsSearchFilter


class EventsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EventsSearchFilter


class EventsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EventsSearchFilter


class EventsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EventsSearchFilter


class EventsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EventsSearchFilter


class EventsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EventsSearchFilter


class EventsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EventsStringFilter


class EventsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EventsStringFilter


class EventsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EventsStringFilter


class EventsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EventsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EventsInCondition = TypedDict("EventsInCondition", {"in": EventsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EventsNotCondition = TypedDict("EventsNotCondition", {"not": "EventsCondition"}, total=False)
"""Negates the nested condition."""

EventsAndCondition = TypedDict("EventsAndCondition", {"and": "list[EventsCondition]"}, total=False)
"""True if all nested conditions are true."""

EventsOrCondition = TypedDict("EventsOrCondition", {"or": "list[EventsCondition]"}, total=False)
"""True if any nested condition is true."""

EventsAnyCondition = TypedDict("EventsAnyCondition", {"any": EventsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all events condition types
EventsCondition = (
    EventsEqCondition
    | EventsNeqCondition
    | EventsGtCondition
    | EventsGteCondition
    | EventsLtCondition
    | EventsLteCondition
    | EventsInCondition
    | EventsLikeCondition
    | EventsFuzzyCondition
    | EventsKeywordCondition
    | EventsContainsCondition
    | EventsNotCondition
    | EventsAndCondition
    | EventsOrCondition
    | EventsAnyCondition
)


class EventsSearchQuery(TypedDict, total=False):
    """Search query for events entity."""
    filter: EventsCondition
    sort: list[EventsSortFilter]


# ===== CALLS SEARCH TYPES =====

class CallsSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls search queries."""
    id: str
    """Unique record identifier"""
    subject: str | None
    """Subject of the call"""
    call_type: str | None
    """Type of call (Inbound or Outbound)"""
    call_start_time: str | None
    """Start time of the call"""
    call_duration: str | None
    """Duration of the call as a formatted string"""
    call_duration_in_seconds: float | None
    """Duration of the call in seconds"""
    call_purpose: str | None
    """Purpose of the call"""
    call_result: str | None
    """Result or outcome of the call"""
    caller_id: str | None
    """Caller ID number"""
    outgoing_call_status: str | None
    """Status of outgoing calls"""
    description: str | None
    """Description or notes about the call"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class CallsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    subject: list[str]
    """Subject of the call"""
    call_type: list[str]
    """Type of call (Inbound or Outbound)"""
    call_start_time: list[str]
    """Start time of the call"""
    call_duration: list[str]
    """Duration of the call as a formatted string"""
    call_duration_in_seconds: list[float]
    """Duration of the call in seconds"""
    call_purpose: list[str]
    """Purpose of the call"""
    call_result: list[str]
    """Result or outcome of the call"""
    caller_id: list[str]
    """Caller ID number"""
    outgoing_call_status: list[str]
    """Status of outgoing calls"""
    description: list[str]
    """Description or notes about the call"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class CallsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    subject: Any
    """Subject of the call"""
    call_type: Any
    """Type of call (Inbound or Outbound)"""
    call_start_time: Any
    """Start time of the call"""
    call_duration: Any
    """Duration of the call as a formatted string"""
    call_duration_in_seconds: Any
    """Duration of the call in seconds"""
    call_purpose: Any
    """Purpose of the call"""
    call_result: Any
    """Result or outcome of the call"""
    caller_id: Any
    """Caller ID number"""
    outgoing_call_status: Any
    """Status of outgoing calls"""
    description: Any
    """Description or notes about the call"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class CallsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    subject: str
    """Subject of the call"""
    call_type: str
    """Type of call (Inbound or Outbound)"""
    call_start_time: str
    """Start time of the call"""
    call_duration: str
    """Duration of the call as a formatted string"""
    call_duration_in_seconds: str
    """Duration of the call in seconds"""
    call_purpose: str
    """Purpose of the call"""
    call_result: str
    """Result or outcome of the call"""
    caller_id: str
    """Caller ID number"""
    outgoing_call_status: str
    """Status of outgoing calls"""
    description: str
    """Description or notes about the call"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class CallsSortFilter(TypedDict, total=False):
    """Available fields for sorting calls search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    subject: AirbyteSortOrder
    """Subject of the call"""
    call_type: AirbyteSortOrder
    """Type of call (Inbound or Outbound)"""
    call_start_time: AirbyteSortOrder
    """Start time of the call"""
    call_duration: AirbyteSortOrder
    """Duration of the call as a formatted string"""
    call_duration_in_seconds: AirbyteSortOrder
    """Duration of the call in seconds"""
    call_purpose: AirbyteSortOrder
    """Purpose of the call"""
    call_result: AirbyteSortOrder
    """Result or outcome of the call"""
    caller_id: AirbyteSortOrder
    """Caller ID number"""
    outgoing_call_status: AirbyteSortOrder
    """Status of outgoing calls"""
    description: AirbyteSortOrder
    """Description or notes about the call"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for calls
class CallsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallsSearchFilter


class CallsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallsSearchFilter


class CallsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallsSearchFilter


class CallsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallsSearchFilter


class CallsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallsSearchFilter


class CallsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallsSearchFilter


class CallsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CallsStringFilter


class CallsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallsStringFilter


class CallsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallsStringFilter


class CallsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CallsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallsInCondition = TypedDict("CallsInCondition", {"in": CallsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallsNotCondition = TypedDict("CallsNotCondition", {"not": "CallsCondition"}, total=False)
"""Negates the nested condition."""

CallsAndCondition = TypedDict("CallsAndCondition", {"and": "list[CallsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallsOrCondition = TypedDict("CallsOrCondition", {"or": "list[CallsCondition]"}, total=False)
"""True if any nested condition is true."""

CallsAnyCondition = TypedDict("CallsAnyCondition", {"any": CallsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all calls condition types
CallsCondition = (
    CallsEqCondition
    | CallsNeqCondition
    | CallsGtCondition
    | CallsGteCondition
    | CallsLtCondition
    | CallsLteCondition
    | CallsInCondition
    | CallsLikeCondition
    | CallsFuzzyCondition
    | CallsKeywordCondition
    | CallsContainsCondition
    | CallsNotCondition
    | CallsAndCondition
    | CallsOrCondition
    | CallsAnyCondition
)


class CallsSearchQuery(TypedDict, total=False):
    """Search query for calls entity."""
    filter: CallsCondition
    sort: list[CallsSortFilter]


# ===== PRODUCTS SEARCH TYPES =====

class ProductsSearchFilter(TypedDict, total=False):
    """Available fields for filtering products search queries."""
    id: str
    """Unique record identifier"""
    product_name: str | None
    """Name of the product"""
    product_code: str | None
    """Product code or SKU"""
    product_category: str | None
    """Category of the product"""
    product_active: bool | None
    """Whether the product is active"""
    unit_price: float | None
    """Unit price of the product"""
    commission_rate: float | None
    """Commission rate for the product"""
    manufacturer: str | None
    """Product manufacturer"""
    sales_start_date: str | None
    """Date when sales begin"""
    sales_end_date: str | None
    """Date when sales end"""
    qty_in_stock: float | None
    """Quantity currently in stock"""
    qty_in_demand: float | None
    """Quantity in demand"""
    qty_ordered: float | None
    """Quantity on order"""
    description: str | None
    """Description of the product"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class ProductsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    product_name: list[str]
    """Name of the product"""
    product_code: list[str]
    """Product code or SKU"""
    product_category: list[str]
    """Category of the product"""
    product_active: list[bool]
    """Whether the product is active"""
    unit_price: list[float]
    """Unit price of the product"""
    commission_rate: list[float]
    """Commission rate for the product"""
    manufacturer: list[str]
    """Product manufacturer"""
    sales_start_date: list[str]
    """Date when sales begin"""
    sales_end_date: list[str]
    """Date when sales end"""
    qty_in_stock: list[float]
    """Quantity currently in stock"""
    qty_in_demand: list[float]
    """Quantity in demand"""
    qty_ordered: list[float]
    """Quantity on order"""
    description: list[str]
    """Description of the product"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class ProductsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    product_name: Any
    """Name of the product"""
    product_code: Any
    """Product code or SKU"""
    product_category: Any
    """Category of the product"""
    product_active: Any
    """Whether the product is active"""
    unit_price: Any
    """Unit price of the product"""
    commission_rate: Any
    """Commission rate for the product"""
    manufacturer: Any
    """Product manufacturer"""
    sales_start_date: Any
    """Date when sales begin"""
    sales_end_date: Any
    """Date when sales end"""
    qty_in_stock: Any
    """Quantity currently in stock"""
    qty_in_demand: Any
    """Quantity in demand"""
    qty_ordered: Any
    """Quantity on order"""
    description: Any
    """Description of the product"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class ProductsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    product_name: str
    """Name of the product"""
    product_code: str
    """Product code or SKU"""
    product_category: str
    """Category of the product"""
    product_active: str
    """Whether the product is active"""
    unit_price: str
    """Unit price of the product"""
    commission_rate: str
    """Commission rate for the product"""
    manufacturer: str
    """Product manufacturer"""
    sales_start_date: str
    """Date when sales begin"""
    sales_end_date: str
    """Date when sales end"""
    qty_in_stock: str
    """Quantity currently in stock"""
    qty_in_demand: str
    """Quantity in demand"""
    qty_ordered: str
    """Quantity on order"""
    description: str
    """Description of the product"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class ProductsSortFilter(TypedDict, total=False):
    """Available fields for sorting products search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    product_name: AirbyteSortOrder
    """Name of the product"""
    product_code: AirbyteSortOrder
    """Product code or SKU"""
    product_category: AirbyteSortOrder
    """Category of the product"""
    product_active: AirbyteSortOrder
    """Whether the product is active"""
    unit_price: AirbyteSortOrder
    """Unit price of the product"""
    commission_rate: AirbyteSortOrder
    """Commission rate for the product"""
    manufacturer: AirbyteSortOrder
    """Product manufacturer"""
    sales_start_date: AirbyteSortOrder
    """Date when sales begin"""
    sales_end_date: AirbyteSortOrder
    """Date when sales end"""
    qty_in_stock: AirbyteSortOrder
    """Quantity currently in stock"""
    qty_in_demand: AirbyteSortOrder
    """Quantity in demand"""
    qty_ordered: AirbyteSortOrder
    """Quantity on order"""
    description: AirbyteSortOrder
    """Description of the product"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for products
class ProductsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductsSearchFilter


class ProductsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductsSearchFilter


class ProductsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductsSearchFilter


class ProductsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductsSearchFilter


class ProductsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductsSearchFilter


class ProductsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductsSearchFilter


class ProductsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductsStringFilter


class ProductsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductsStringFilter


class ProductsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductsStringFilter


class ProductsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductsInCondition = TypedDict("ProductsInCondition", {"in": ProductsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductsNotCondition = TypedDict("ProductsNotCondition", {"not": "ProductsCondition"}, total=False)
"""Negates the nested condition."""

ProductsAndCondition = TypedDict("ProductsAndCondition", {"and": "list[ProductsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductsOrCondition = TypedDict("ProductsOrCondition", {"or": "list[ProductsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductsAnyCondition = TypedDict("ProductsAnyCondition", {"any": ProductsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all products condition types
ProductsCondition = (
    ProductsEqCondition
    | ProductsNeqCondition
    | ProductsGtCondition
    | ProductsGteCondition
    | ProductsLtCondition
    | ProductsLteCondition
    | ProductsInCondition
    | ProductsLikeCondition
    | ProductsFuzzyCondition
    | ProductsKeywordCondition
    | ProductsContainsCondition
    | ProductsNotCondition
    | ProductsAndCondition
    | ProductsOrCondition
    | ProductsAnyCondition
)


class ProductsSearchQuery(TypedDict, total=False):
    """Search query for products entity."""
    filter: ProductsCondition
    sort: list[ProductsSortFilter]


# ===== QUOTES SEARCH TYPES =====

class QuotesSearchFilter(TypedDict, total=False):
    """Available fields for filtering quotes search queries."""
    id: str
    """Unique record identifier"""
    subject: str | None
    """Subject or title of the quote"""
    quote_stage: str | None
    """Current stage of the quote"""
    valid_till: str | None
    """Date until which the quote is valid"""
    carrier: str | None
    """Shipping carrier"""
    sub_total: float | None
    """Subtotal before tax and adjustments"""
    tax: float | None
    """Tax amount"""
    adjustment: float | None
    """Adjustment amount"""
    grand_total: float | None
    """Total amount including tax and adjustments"""
    discount: float | None
    """Discount amount"""
    terms_and_conditions: str | None
    """Terms and conditions text"""
    description: str | None
    """Description or notes about the quote"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class QuotesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    subject: list[str]
    """Subject or title of the quote"""
    quote_stage: list[str]
    """Current stage of the quote"""
    valid_till: list[str]
    """Date until which the quote is valid"""
    carrier: list[str]
    """Shipping carrier"""
    sub_total: list[float]
    """Subtotal before tax and adjustments"""
    tax: list[float]
    """Tax amount"""
    adjustment: list[float]
    """Adjustment amount"""
    grand_total: list[float]
    """Total amount including tax and adjustments"""
    discount: list[float]
    """Discount amount"""
    terms_and_conditions: list[str]
    """Terms and conditions text"""
    description: list[str]
    """Description or notes about the quote"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class QuotesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    subject: Any
    """Subject or title of the quote"""
    quote_stage: Any
    """Current stage of the quote"""
    valid_till: Any
    """Date until which the quote is valid"""
    carrier: Any
    """Shipping carrier"""
    sub_total: Any
    """Subtotal before tax and adjustments"""
    tax: Any
    """Tax amount"""
    adjustment: Any
    """Adjustment amount"""
    grand_total: Any
    """Total amount including tax and adjustments"""
    discount: Any
    """Discount amount"""
    terms_and_conditions: Any
    """Terms and conditions text"""
    description: Any
    """Description or notes about the quote"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class QuotesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    subject: str
    """Subject or title of the quote"""
    quote_stage: str
    """Current stage of the quote"""
    valid_till: str
    """Date until which the quote is valid"""
    carrier: str
    """Shipping carrier"""
    sub_total: str
    """Subtotal before tax and adjustments"""
    tax: str
    """Tax amount"""
    adjustment: str
    """Adjustment amount"""
    grand_total: str
    """Total amount including tax and adjustments"""
    discount: str
    """Discount amount"""
    terms_and_conditions: str
    """Terms and conditions text"""
    description: str
    """Description or notes about the quote"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class QuotesSortFilter(TypedDict, total=False):
    """Available fields for sorting quotes search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    subject: AirbyteSortOrder
    """Subject or title of the quote"""
    quote_stage: AirbyteSortOrder
    """Current stage of the quote"""
    valid_till: AirbyteSortOrder
    """Date until which the quote is valid"""
    carrier: AirbyteSortOrder
    """Shipping carrier"""
    sub_total: AirbyteSortOrder
    """Subtotal before tax and adjustments"""
    tax: AirbyteSortOrder
    """Tax amount"""
    adjustment: AirbyteSortOrder
    """Adjustment amount"""
    grand_total: AirbyteSortOrder
    """Total amount including tax and adjustments"""
    discount: AirbyteSortOrder
    """Discount amount"""
    terms_and_conditions: AirbyteSortOrder
    """Terms and conditions text"""
    description: AirbyteSortOrder
    """Description or notes about the quote"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


# Entity-specific condition types for quotes
class QuotesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: QuotesSearchFilter


class QuotesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: QuotesSearchFilter


class QuotesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: QuotesSearchFilter


class QuotesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: QuotesSearchFilter


class QuotesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: QuotesSearchFilter


class QuotesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: QuotesSearchFilter


class QuotesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: QuotesStringFilter


class QuotesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: QuotesStringFilter


class QuotesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: QuotesStringFilter


class QuotesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: QuotesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
QuotesInCondition = TypedDict("QuotesInCondition", {"in": QuotesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

QuotesNotCondition = TypedDict("QuotesNotCondition", {"not": "QuotesCondition"}, total=False)
"""Negates the nested condition."""

QuotesAndCondition = TypedDict("QuotesAndCondition", {"and": "list[QuotesCondition]"}, total=False)
"""True if all nested conditions are true."""

QuotesOrCondition = TypedDict("QuotesOrCondition", {"or": "list[QuotesCondition]"}, total=False)
"""True if any nested condition is true."""

QuotesAnyCondition = TypedDict("QuotesAnyCondition", {"any": QuotesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all quotes condition types
QuotesCondition = (
    QuotesEqCondition
    | QuotesNeqCondition
    | QuotesGtCondition
    | QuotesGteCondition
    | QuotesLtCondition
    | QuotesLteCondition
    | QuotesInCondition
    | QuotesLikeCondition
    | QuotesFuzzyCondition
    | QuotesKeywordCondition
    | QuotesContainsCondition
    | QuotesNotCondition
    | QuotesAndCondition
    | QuotesOrCondition
    | QuotesAnyCondition
)


class QuotesSearchQuery(TypedDict, total=False):
    """Search query for quotes entity."""
    filter: QuotesCondition
    sort: list[QuotesSortFilter]


# ===== INVOICES SEARCH TYPES =====

class InvoicesSearchFilter(TypedDict, total=False):
    """Available fields for filtering invoices search queries."""
    id: str
    """Unique record identifier"""
    subject: str | None
    """Subject or title of the invoice"""
    invoice_number: str | None
    """Invoice number"""
    invoice_date: str | None
    """Date the invoice was issued"""
    due_date: str | None
    """Payment due date"""
    status: str | None
    """Current status of the invoice"""
    purchase_order: str | None
    """Associated purchase order number"""
    sub_total: float | None
    """Subtotal before tax and adjustments"""
    tax: float | None
    """Tax amount"""
    adjustment: float | None
    """Adjustment amount"""
    grand_total: float | None
    """Total amount including tax and adjustments"""
    discount: float | None
    """Discount amount"""
    excise_duty: float | None
    """Excise duty amount"""
    terms_and_conditions: str | None
    """Terms and conditions text"""
    description: str | None
    """Description or notes about the invoice"""
    created_time: str | None
    """Time the record was created"""
    modified_time: str | None
    """Time the record was last modified"""


class InvoicesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique record identifier"""
    subject: list[str]
    """Subject or title of the invoice"""
    invoice_number: list[str]
    """Invoice number"""
    invoice_date: list[str]
    """Date the invoice was issued"""
    due_date: list[str]
    """Payment due date"""
    status: list[str]
    """Current status of the invoice"""
    purchase_order: list[str]
    """Associated purchase order number"""
    sub_total: list[float]
    """Subtotal before tax and adjustments"""
    tax: list[float]
    """Tax amount"""
    adjustment: list[float]
    """Adjustment amount"""
    grand_total: list[float]
    """Total amount including tax and adjustments"""
    discount: list[float]
    """Discount amount"""
    excise_duty: list[float]
    """Excise duty amount"""
    terms_and_conditions: list[str]
    """Terms and conditions text"""
    description: list[str]
    """Description or notes about the invoice"""
    created_time: list[str]
    """Time the record was created"""
    modified_time: list[str]
    """Time the record was last modified"""


class InvoicesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique record identifier"""
    subject: Any
    """Subject or title of the invoice"""
    invoice_number: Any
    """Invoice number"""
    invoice_date: Any
    """Date the invoice was issued"""
    due_date: Any
    """Payment due date"""
    status: Any
    """Current status of the invoice"""
    purchase_order: Any
    """Associated purchase order number"""
    sub_total: Any
    """Subtotal before tax and adjustments"""
    tax: Any
    """Tax amount"""
    adjustment: Any
    """Adjustment amount"""
    grand_total: Any
    """Total amount including tax and adjustments"""
    discount: Any
    """Discount amount"""
    excise_duty: Any
    """Excise duty amount"""
    terms_and_conditions: Any
    """Terms and conditions text"""
    description: Any
    """Description or notes about the invoice"""
    created_time: Any
    """Time the record was created"""
    modified_time: Any
    """Time the record was last modified"""


class InvoicesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique record identifier"""
    subject: str
    """Subject or title of the invoice"""
    invoice_number: str
    """Invoice number"""
    invoice_date: str
    """Date the invoice was issued"""
    due_date: str
    """Payment due date"""
    status: str
    """Current status of the invoice"""
    purchase_order: str
    """Associated purchase order number"""
    sub_total: str
    """Subtotal before tax and adjustments"""
    tax: str
    """Tax amount"""
    adjustment: str
    """Adjustment amount"""
    grand_total: str
    """Total amount including tax and adjustments"""
    discount: str
    """Discount amount"""
    excise_duty: str
    """Excise duty amount"""
    terms_and_conditions: str
    """Terms and conditions text"""
    description: str
    """Description or notes about the invoice"""
    created_time: str
    """Time the record was created"""
    modified_time: str
    """Time the record was last modified"""


class InvoicesSortFilter(TypedDict, total=False):
    """Available fields for sorting invoices search results."""
    id: AirbyteSortOrder
    """Unique record identifier"""
    subject: AirbyteSortOrder
    """Subject or title of the invoice"""
    invoice_number: AirbyteSortOrder
    """Invoice number"""
    invoice_date: AirbyteSortOrder
    """Date the invoice was issued"""
    due_date: AirbyteSortOrder
    """Payment due date"""
    status: AirbyteSortOrder
    """Current status of the invoice"""
    purchase_order: AirbyteSortOrder
    """Associated purchase order number"""
    sub_total: AirbyteSortOrder
    """Subtotal before tax and adjustments"""
    tax: AirbyteSortOrder
    """Tax amount"""
    adjustment: AirbyteSortOrder
    """Adjustment amount"""
    grand_total: AirbyteSortOrder
    """Total amount including tax and adjustments"""
    discount: AirbyteSortOrder
    """Discount amount"""
    excise_duty: AirbyteSortOrder
    """Excise duty amount"""
    terms_and_conditions: AirbyteSortOrder
    """Terms and conditions text"""
    description: AirbyteSortOrder
    """Description or notes about the invoice"""
    created_time: AirbyteSortOrder
    """Time the record was created"""
    modified_time: AirbyteSortOrder
    """Time the record was last modified"""


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



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
