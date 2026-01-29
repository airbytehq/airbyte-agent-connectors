"""
Type definitions for orb connector.
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

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    limit: NotRequired[int]
    cursor: NotRequired[str]

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    customer_id: str

class SubscriptionsListParams(TypedDict):
    """Parameters for subscriptions.list operation"""
    limit: NotRequired[int]
    cursor: NotRequired[str]
    customer_id: NotRequired[str]
    external_customer_id: NotRequired[str]
    status: NotRequired[str]

class SubscriptionsGetParams(TypedDict):
    """Parameters for subscriptions.get operation"""
    subscription_id: str

class PlansListParams(TypedDict):
    """Parameters for plans.list operation"""
    limit: NotRequired[int]
    cursor: NotRequired[str]

class PlansGetParams(TypedDict):
    """Parameters for plans.get operation"""
    plan_id: str

class InvoicesListParams(TypedDict):
    """Parameters for invoices.list operation"""
    limit: NotRequired[int]
    cursor: NotRequired[str]
    customer_id: NotRequired[str]
    external_customer_id: NotRequired[str]
    subscription_id: NotRequired[str]
    invoice_date_gt: NotRequired[str]
    invoice_date_gte: NotRequired[str]
    invoice_date_lt: NotRequired[str]
    invoice_date_lte: NotRequired[str]
    status: NotRequired[str]

class InvoicesGetParams(TypedDict):
    """Parameters for invoices.get operation"""
    invoice_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CUSTOMERS SEARCH TYPES =====

class CustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering customers search queries."""
    id: str
    """The unique identifier of the customer"""
    external_customer_id: str | None
    """The ID of the customer in an external system"""
    name: str | None
    """The name of the customer"""
    email: str | None
    """The email address of the customer"""
    created_at: str | None
    """The date and time when the customer was created"""
    payment_provider: str | None
    """The payment provider used by the customer"""
    payment_provider_id: str | None
    """The ID of the customer in the payment provider's system"""
    timezone: str | None
    """The timezone setting of the customer"""
    shipping_address: dict[str, Any] | None
    """The shipping address of the customer"""
    billing_address: dict[str, Any] | None
    """The billing address of the customer"""
    balance: str | None
    """The current balance of the customer"""
    currency: str | None
    """The currency of the customer"""
    auto_collection: bool | None
    """Whether auto collection is enabled"""
    metadata: dict[str, Any] | None
    """Additional metadata for the customer"""


class CustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """The unique identifier of the customer"""
    external_customer_id: list[str]
    """The ID of the customer in an external system"""
    name: list[str]
    """The name of the customer"""
    email: list[str]
    """The email address of the customer"""
    created_at: list[str]
    """The date and time when the customer was created"""
    payment_provider: list[str]
    """The payment provider used by the customer"""
    payment_provider_id: list[str]
    """The ID of the customer in the payment provider's system"""
    timezone: list[str]
    """The timezone setting of the customer"""
    shipping_address: list[dict[str, Any]]
    """The shipping address of the customer"""
    billing_address: list[dict[str, Any]]
    """The billing address of the customer"""
    balance: list[str]
    """The current balance of the customer"""
    currency: list[str]
    """The currency of the customer"""
    auto_collection: list[bool]
    """Whether auto collection is enabled"""
    metadata: list[dict[str, Any]]
    """Additional metadata for the customer"""


class CustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique identifier of the customer"""
    external_customer_id: Any
    """The ID of the customer in an external system"""
    name: Any
    """The name of the customer"""
    email: Any
    """The email address of the customer"""
    created_at: Any
    """The date and time when the customer was created"""
    payment_provider: Any
    """The payment provider used by the customer"""
    payment_provider_id: Any
    """The ID of the customer in the payment provider's system"""
    timezone: Any
    """The timezone setting of the customer"""
    shipping_address: Any
    """The shipping address of the customer"""
    billing_address: Any
    """The billing address of the customer"""
    balance: Any
    """The current balance of the customer"""
    currency: Any
    """The currency of the customer"""
    auto_collection: Any
    """Whether auto collection is enabled"""
    metadata: Any
    """Additional metadata for the customer"""


class CustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """The unique identifier of the customer"""
    external_customer_id: str
    """The ID of the customer in an external system"""
    name: str
    """The name of the customer"""
    email: str
    """The email address of the customer"""
    created_at: str
    """The date and time when the customer was created"""
    payment_provider: str
    """The payment provider used by the customer"""
    payment_provider_id: str
    """The ID of the customer in the payment provider's system"""
    timezone: str
    """The timezone setting of the customer"""
    shipping_address: str
    """The shipping address of the customer"""
    billing_address: str
    """The billing address of the customer"""
    balance: str
    """The current balance of the customer"""
    currency: str
    """The currency of the customer"""
    auto_collection: str
    """Whether auto collection is enabled"""
    metadata: str
    """Additional metadata for the customer"""


class CustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting customers search results."""
    id: AirbyteSortOrder
    """The unique identifier of the customer"""
    external_customer_id: AirbyteSortOrder
    """The ID of the customer in an external system"""
    name: AirbyteSortOrder
    """The name of the customer"""
    email: AirbyteSortOrder
    """The email address of the customer"""
    created_at: AirbyteSortOrder
    """The date and time when the customer was created"""
    payment_provider: AirbyteSortOrder
    """The payment provider used by the customer"""
    payment_provider_id: AirbyteSortOrder
    """The ID of the customer in the payment provider's system"""
    timezone: AirbyteSortOrder
    """The timezone setting of the customer"""
    shipping_address: AirbyteSortOrder
    """The shipping address of the customer"""
    billing_address: AirbyteSortOrder
    """The billing address of the customer"""
    balance: AirbyteSortOrder
    """The current balance of the customer"""
    currency: AirbyteSortOrder
    """The currency of the customer"""
    auto_collection: AirbyteSortOrder
    """Whether auto collection is enabled"""
    metadata: AirbyteSortOrder
    """Additional metadata for the customer"""


# Entity-specific condition types for customers
class CustomersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomersSearchFilter


class CustomersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomersSearchFilter


class CustomersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomersSearchFilter


class CustomersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomersSearchFilter


class CustomersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomersSearchFilter


class CustomersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomersSearchFilter


class CustomersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomersStringFilter


class CustomersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomersStringFilter


class CustomersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomersStringFilter


class CustomersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomersInCondition = TypedDict("CustomersInCondition", {"in": CustomersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomersNotCondition = TypedDict("CustomersNotCondition", {"not": "CustomersCondition"}, total=False)
"""Negates the nested condition."""

CustomersAndCondition = TypedDict("CustomersAndCondition", {"and": "list[CustomersCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomersOrCondition = TypedDict("CustomersOrCondition", {"or": "list[CustomersCondition]"}, total=False)
"""True if any nested condition is true."""

CustomersAnyCondition = TypedDict("CustomersAnyCondition", {"any": CustomersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all customers condition types
CustomersCondition = (
    CustomersEqCondition
    | CustomersNeqCondition
    | CustomersGtCondition
    | CustomersGteCondition
    | CustomersLtCondition
    | CustomersLteCondition
    | CustomersInCondition
    | CustomersLikeCondition
    | CustomersFuzzyCondition
    | CustomersKeywordCondition
    | CustomersContainsCondition
    | CustomersNotCondition
    | CustomersAndCondition
    | CustomersOrCondition
    | CustomersAnyCondition
)


class CustomersSearchQuery(TypedDict, total=False):
    """Search query for customers entity."""
    filter: CustomersCondition
    sort: list[CustomersSortFilter]


# ===== SUBSCRIPTIONS SEARCH TYPES =====

class SubscriptionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering subscriptions search queries."""
    id: str
    """The unique identifier of the subscription"""
    created_at: str | None
    """The date and time when the subscription was created"""
    start_date: str | None
    """The date and time when the subscription starts"""
    end_date: str | None
    """The date and time when the subscription ends"""
    status: str | None
    """The current status of the subscription"""
    customer: dict[str, Any] | None
    """The customer associated with the subscription"""
    plan: dict[str, Any] | None
    """The plan associated with the subscription"""
    current_billing_period_start_date: str | None
    """The start date of the current billing period"""
    current_billing_period_end_date: str | None
    """The end date of the current billing period"""
    auto_collection: bool | None
    """Whether auto collection is enabled"""
    net_terms: int | None
    """The net terms for the subscription"""
    metadata: dict[str, Any] | None
    """Additional metadata for the subscription"""


class SubscriptionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """The unique identifier of the subscription"""
    created_at: list[str]
    """The date and time when the subscription was created"""
    start_date: list[str]
    """The date and time when the subscription starts"""
    end_date: list[str]
    """The date and time when the subscription ends"""
    status: list[str]
    """The current status of the subscription"""
    customer: list[dict[str, Any]]
    """The customer associated with the subscription"""
    plan: list[dict[str, Any]]
    """The plan associated with the subscription"""
    current_billing_period_start_date: list[str]
    """The start date of the current billing period"""
    current_billing_period_end_date: list[str]
    """The end date of the current billing period"""
    auto_collection: list[bool]
    """Whether auto collection is enabled"""
    net_terms: list[int]
    """The net terms for the subscription"""
    metadata: list[dict[str, Any]]
    """Additional metadata for the subscription"""


class SubscriptionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique identifier of the subscription"""
    created_at: Any
    """The date and time when the subscription was created"""
    start_date: Any
    """The date and time when the subscription starts"""
    end_date: Any
    """The date and time when the subscription ends"""
    status: Any
    """The current status of the subscription"""
    customer: Any
    """The customer associated with the subscription"""
    plan: Any
    """The plan associated with the subscription"""
    current_billing_period_start_date: Any
    """The start date of the current billing period"""
    current_billing_period_end_date: Any
    """The end date of the current billing period"""
    auto_collection: Any
    """Whether auto collection is enabled"""
    net_terms: Any
    """The net terms for the subscription"""
    metadata: Any
    """Additional metadata for the subscription"""


class SubscriptionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """The unique identifier of the subscription"""
    created_at: str
    """The date and time when the subscription was created"""
    start_date: str
    """The date and time when the subscription starts"""
    end_date: str
    """The date and time when the subscription ends"""
    status: str
    """The current status of the subscription"""
    customer: str
    """The customer associated with the subscription"""
    plan: str
    """The plan associated with the subscription"""
    current_billing_period_start_date: str
    """The start date of the current billing period"""
    current_billing_period_end_date: str
    """The end date of the current billing period"""
    auto_collection: str
    """Whether auto collection is enabled"""
    net_terms: str
    """The net terms for the subscription"""
    metadata: str
    """Additional metadata for the subscription"""


class SubscriptionsSortFilter(TypedDict, total=False):
    """Available fields for sorting subscriptions search results."""
    id: AirbyteSortOrder
    """The unique identifier of the subscription"""
    created_at: AirbyteSortOrder
    """The date and time when the subscription was created"""
    start_date: AirbyteSortOrder
    """The date and time when the subscription starts"""
    end_date: AirbyteSortOrder
    """The date and time when the subscription ends"""
    status: AirbyteSortOrder
    """The current status of the subscription"""
    customer: AirbyteSortOrder
    """The customer associated with the subscription"""
    plan: AirbyteSortOrder
    """The plan associated with the subscription"""
    current_billing_period_start_date: AirbyteSortOrder
    """The start date of the current billing period"""
    current_billing_period_end_date: AirbyteSortOrder
    """The end date of the current billing period"""
    auto_collection: AirbyteSortOrder
    """Whether auto collection is enabled"""
    net_terms: AirbyteSortOrder
    """The net terms for the subscription"""
    metadata: AirbyteSortOrder
    """Additional metadata for the subscription"""


# Entity-specific condition types for subscriptions
class SubscriptionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SubscriptionsSearchFilter


class SubscriptionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SubscriptionsSearchFilter


class SubscriptionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SubscriptionsSearchFilter


class SubscriptionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SubscriptionsSearchFilter


class SubscriptionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SubscriptionsSearchFilter


class SubscriptionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SubscriptionsSearchFilter


class SubscriptionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SubscriptionsStringFilter


class SubscriptionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SubscriptionsStringFilter


class SubscriptionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SubscriptionsStringFilter


class SubscriptionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SubscriptionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SubscriptionsInCondition = TypedDict("SubscriptionsInCondition", {"in": SubscriptionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SubscriptionsNotCondition = TypedDict("SubscriptionsNotCondition", {"not": "SubscriptionsCondition"}, total=False)
"""Negates the nested condition."""

SubscriptionsAndCondition = TypedDict("SubscriptionsAndCondition", {"and": "list[SubscriptionsCondition]"}, total=False)
"""True if all nested conditions are true."""

SubscriptionsOrCondition = TypedDict("SubscriptionsOrCondition", {"or": "list[SubscriptionsCondition]"}, total=False)
"""True if any nested condition is true."""

SubscriptionsAnyCondition = TypedDict("SubscriptionsAnyCondition", {"any": SubscriptionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all subscriptions condition types
SubscriptionsCondition = (
    SubscriptionsEqCondition
    | SubscriptionsNeqCondition
    | SubscriptionsGtCondition
    | SubscriptionsGteCondition
    | SubscriptionsLtCondition
    | SubscriptionsLteCondition
    | SubscriptionsInCondition
    | SubscriptionsLikeCondition
    | SubscriptionsFuzzyCondition
    | SubscriptionsKeywordCondition
    | SubscriptionsContainsCondition
    | SubscriptionsNotCondition
    | SubscriptionsAndCondition
    | SubscriptionsOrCondition
    | SubscriptionsAnyCondition
)


class SubscriptionsSearchQuery(TypedDict, total=False):
    """Search query for subscriptions entity."""
    filter: SubscriptionsCondition
    sort: list[SubscriptionsSortFilter]


# ===== PLANS SEARCH TYPES =====

class PlansSearchFilter(TypedDict, total=False):
    """Available fields for filtering plans search queries."""
    id: str
    """The unique identifier of the plan"""
    created_at: str | None
    """The date and time when the plan was created"""
    name: str | None
    """The name of the plan"""
    description: str | None
    """A description of the plan"""
    status: str | None
    """The status of the plan"""
    currency: str | None
    """The currency of the plan"""
    prices: list[Any] | None
    """The pricing options for the plan"""
    product: dict[str, Any] | None
    """The product associated with the plan"""
    external_plan_id: str | None
    """The external plan ID"""
    metadata: dict[str, Any] | None
    """Additional metadata for the plan"""


class PlansInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """The unique identifier of the plan"""
    created_at: list[str]
    """The date and time when the plan was created"""
    name: list[str]
    """The name of the plan"""
    description: list[str]
    """A description of the plan"""
    status: list[str]
    """The status of the plan"""
    currency: list[str]
    """The currency of the plan"""
    prices: list[list[Any]]
    """The pricing options for the plan"""
    product: list[dict[str, Any]]
    """The product associated with the plan"""
    external_plan_id: list[str]
    """The external plan ID"""
    metadata: list[dict[str, Any]]
    """Additional metadata for the plan"""


class PlansAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique identifier of the plan"""
    created_at: Any
    """The date and time when the plan was created"""
    name: Any
    """The name of the plan"""
    description: Any
    """A description of the plan"""
    status: Any
    """The status of the plan"""
    currency: Any
    """The currency of the plan"""
    prices: Any
    """The pricing options for the plan"""
    product: Any
    """The product associated with the plan"""
    external_plan_id: Any
    """The external plan ID"""
    metadata: Any
    """Additional metadata for the plan"""


class PlansStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """The unique identifier of the plan"""
    created_at: str
    """The date and time when the plan was created"""
    name: str
    """The name of the plan"""
    description: str
    """A description of the plan"""
    status: str
    """The status of the plan"""
    currency: str
    """The currency of the plan"""
    prices: str
    """The pricing options for the plan"""
    product: str
    """The product associated with the plan"""
    external_plan_id: str
    """The external plan ID"""
    metadata: str
    """Additional metadata for the plan"""


class PlansSortFilter(TypedDict, total=False):
    """Available fields for sorting plans search results."""
    id: AirbyteSortOrder
    """The unique identifier of the plan"""
    created_at: AirbyteSortOrder
    """The date and time when the plan was created"""
    name: AirbyteSortOrder
    """The name of the plan"""
    description: AirbyteSortOrder
    """A description of the plan"""
    status: AirbyteSortOrder
    """The status of the plan"""
    currency: AirbyteSortOrder
    """The currency of the plan"""
    prices: AirbyteSortOrder
    """The pricing options for the plan"""
    product: AirbyteSortOrder
    """The product associated with the plan"""
    external_plan_id: AirbyteSortOrder
    """The external plan ID"""
    metadata: AirbyteSortOrder
    """Additional metadata for the plan"""


# Entity-specific condition types for plans
class PlansEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PlansSearchFilter


class PlansNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PlansSearchFilter


class PlansGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PlansSearchFilter


class PlansGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PlansSearchFilter


class PlansLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PlansSearchFilter


class PlansLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PlansSearchFilter


class PlansLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PlansStringFilter


class PlansFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PlansStringFilter


class PlansKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PlansStringFilter


class PlansContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PlansAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PlansInCondition = TypedDict("PlansInCondition", {"in": PlansInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PlansNotCondition = TypedDict("PlansNotCondition", {"not": "PlansCondition"}, total=False)
"""Negates the nested condition."""

PlansAndCondition = TypedDict("PlansAndCondition", {"and": "list[PlansCondition]"}, total=False)
"""True if all nested conditions are true."""

PlansOrCondition = TypedDict("PlansOrCondition", {"or": "list[PlansCondition]"}, total=False)
"""True if any nested condition is true."""

PlansAnyCondition = TypedDict("PlansAnyCondition", {"any": PlansAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all plans condition types
PlansCondition = (
    PlansEqCondition
    | PlansNeqCondition
    | PlansGtCondition
    | PlansGteCondition
    | PlansLtCondition
    | PlansLteCondition
    | PlansInCondition
    | PlansLikeCondition
    | PlansFuzzyCondition
    | PlansKeywordCondition
    | PlansContainsCondition
    | PlansNotCondition
    | PlansAndCondition
    | PlansOrCondition
    | PlansAnyCondition
)


class PlansSearchQuery(TypedDict, total=False):
    """Search query for plans entity."""
    filter: PlansCondition
    sort: list[PlansSortFilter]


# ===== INVOICES SEARCH TYPES =====

class InvoicesSearchFilter(TypedDict, total=False):
    """Available fields for filtering invoices search queries."""
    id: str
    """The unique identifier of the invoice"""
    created_at: str | None
    """The date and time when the invoice was created"""
    invoice_date: str | None
    """The date of the invoice"""
    due_date: str | None
    """The due date for the invoice"""
    invoice_pdf: str | None
    """The URL to download the PDF version of the invoice"""
    subtotal: str | None
    """The subtotal amount of the invoice"""
    total: str | None
    """The total amount of the invoice"""
    amount_due: str | None
    """The amount due on the invoice"""
    status: str | None
    """The current status of the invoice"""
    memo: str | None
    """Any additional notes or comments on the invoice"""
    paid_at: str | None
    """The date and time when the invoice was paid"""
    issued_at: str | None
    """The date and time when the invoice was issued"""
    hosted_invoice_url: str | None
    """The URL to view the hosted invoice"""
    line_items: list[Any] | None
    """The line items on the invoice"""
    subscription: dict[str, Any] | None
    """The subscription associated with the invoice"""
    customer: dict[str, Any] | None
    """The customer associated with the invoice"""
    currency: str | None
    """The currency of the invoice"""
    invoice_number: str | None
    """The invoice number"""
    metadata: dict[str, Any] | None
    """Additional metadata for the invoice"""


class InvoicesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """The unique identifier of the invoice"""
    created_at: list[str]
    """The date and time when the invoice was created"""
    invoice_date: list[str]
    """The date of the invoice"""
    due_date: list[str]
    """The due date for the invoice"""
    invoice_pdf: list[str]
    """The URL to download the PDF version of the invoice"""
    subtotal: list[str]
    """The subtotal amount of the invoice"""
    total: list[str]
    """The total amount of the invoice"""
    amount_due: list[str]
    """The amount due on the invoice"""
    status: list[str]
    """The current status of the invoice"""
    memo: list[str]
    """Any additional notes or comments on the invoice"""
    paid_at: list[str]
    """The date and time when the invoice was paid"""
    issued_at: list[str]
    """The date and time when the invoice was issued"""
    hosted_invoice_url: list[str]
    """The URL to view the hosted invoice"""
    line_items: list[list[Any]]
    """The line items on the invoice"""
    subscription: list[dict[str, Any]]
    """The subscription associated with the invoice"""
    customer: list[dict[str, Any]]
    """The customer associated with the invoice"""
    currency: list[str]
    """The currency of the invoice"""
    invoice_number: list[str]
    """The invoice number"""
    metadata: list[dict[str, Any]]
    """Additional metadata for the invoice"""


class InvoicesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """The unique identifier of the invoice"""
    created_at: Any
    """The date and time when the invoice was created"""
    invoice_date: Any
    """The date of the invoice"""
    due_date: Any
    """The due date for the invoice"""
    invoice_pdf: Any
    """The URL to download the PDF version of the invoice"""
    subtotal: Any
    """The subtotal amount of the invoice"""
    total: Any
    """The total amount of the invoice"""
    amount_due: Any
    """The amount due on the invoice"""
    status: Any
    """The current status of the invoice"""
    memo: Any
    """Any additional notes or comments on the invoice"""
    paid_at: Any
    """The date and time when the invoice was paid"""
    issued_at: Any
    """The date and time when the invoice was issued"""
    hosted_invoice_url: Any
    """The URL to view the hosted invoice"""
    line_items: Any
    """The line items on the invoice"""
    subscription: Any
    """The subscription associated with the invoice"""
    customer: Any
    """The customer associated with the invoice"""
    currency: Any
    """The currency of the invoice"""
    invoice_number: Any
    """The invoice number"""
    metadata: Any
    """Additional metadata for the invoice"""


class InvoicesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """The unique identifier of the invoice"""
    created_at: str
    """The date and time when the invoice was created"""
    invoice_date: str
    """The date of the invoice"""
    due_date: str
    """The due date for the invoice"""
    invoice_pdf: str
    """The URL to download the PDF version of the invoice"""
    subtotal: str
    """The subtotal amount of the invoice"""
    total: str
    """The total amount of the invoice"""
    amount_due: str
    """The amount due on the invoice"""
    status: str
    """The current status of the invoice"""
    memo: str
    """Any additional notes or comments on the invoice"""
    paid_at: str
    """The date and time when the invoice was paid"""
    issued_at: str
    """The date and time when the invoice was issued"""
    hosted_invoice_url: str
    """The URL to view the hosted invoice"""
    line_items: str
    """The line items on the invoice"""
    subscription: str
    """The subscription associated with the invoice"""
    customer: str
    """The customer associated with the invoice"""
    currency: str
    """The currency of the invoice"""
    invoice_number: str
    """The invoice number"""
    metadata: str
    """Additional metadata for the invoice"""


class InvoicesSortFilter(TypedDict, total=False):
    """Available fields for sorting invoices search results."""
    id: AirbyteSortOrder
    """The unique identifier of the invoice"""
    created_at: AirbyteSortOrder
    """The date and time when the invoice was created"""
    invoice_date: AirbyteSortOrder
    """The date of the invoice"""
    due_date: AirbyteSortOrder
    """The due date for the invoice"""
    invoice_pdf: AirbyteSortOrder
    """The URL to download the PDF version of the invoice"""
    subtotal: AirbyteSortOrder
    """The subtotal amount of the invoice"""
    total: AirbyteSortOrder
    """The total amount of the invoice"""
    amount_due: AirbyteSortOrder
    """The amount due on the invoice"""
    status: AirbyteSortOrder
    """The current status of the invoice"""
    memo: AirbyteSortOrder
    """Any additional notes or comments on the invoice"""
    paid_at: AirbyteSortOrder
    """The date and time when the invoice was paid"""
    issued_at: AirbyteSortOrder
    """The date and time when the invoice was issued"""
    hosted_invoice_url: AirbyteSortOrder
    """The URL to view the hosted invoice"""
    line_items: AirbyteSortOrder
    """The line items on the invoice"""
    subscription: AirbyteSortOrder
    """The subscription associated with the invoice"""
    customer: AirbyteSortOrder
    """The customer associated with the invoice"""
    currency: AirbyteSortOrder
    """The currency of the invoice"""
    invoice_number: AirbyteSortOrder
    """The invoice number"""
    metadata: AirbyteSortOrder
    """Additional metadata for the invoice"""


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
