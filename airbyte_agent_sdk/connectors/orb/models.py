"""
Pydantic models for orb connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class OrbAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Orb API key"""

# Replication configuration

class OrbReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Orb."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Address(BaseModel):
    """Address object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: str | None = Field(default=None)
    country: str | None = Field(default=None)
    line1: str | None = Field(default=None)
    line2: str | None = Field(default=None)
    postal_code: str | None = Field(default=None)
    state: str | None = Field(default=None)

class CustomerTaxId(BaseModel):
    """Tax identification information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="The type of tax ID")
    """The type of tax ID"""
    value: str | None | None = Field(default=None, description="The value of the tax ID")
    """The value of the tax ID"""
    country: str | None | None = Field(default=None, description="The country of the tax ID")
    """The country of the tax ID"""

class Customer(BaseModel):
    """Customer object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    external_customer_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    payment_provider: str | None = Field(default=None)
    payment_provider_id: str | None = Field(default=None)
    timezone: str | None = Field(default=None)
    shipping_address: Any | None = Field(default=None)
    billing_address: Any | None = Field(default=None)
    balance: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    tax_id: CustomerTaxId | None = Field(default=None)
    auto_collection: bool | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)

class PaginationMetadata(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: bool | None = Field(default=None)
    next_cursor: str | None = Field(default=None)

class CustomersList(BaseModel):
    """Paginated list of customers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Customer] | None = Field(default=None)
    pagination_metadata: PaginationMetadata | None = Field(default=None)

class SubscriptionCustomer(BaseModel):
    """The customer associated with the subscription"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The customer ID")
    """The customer ID"""
    external_customer_id: str | None | None = Field(default=None, description="The external customer ID")
    """The external customer ID"""

class SubscriptionPlan(BaseModel):
    """The plan associated with the subscription"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The plan ID")
    """The plan ID"""
    name: str | None | None = Field(default=None, description="The plan name")
    """The plan name"""

class Subscription(BaseModel):
    """Subscription object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    created_at: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    status: str | None = Field(default=None)
    customer: SubscriptionCustomer | None = Field(default=None)
    plan: SubscriptionPlan | None = Field(default=None)
    current_billing_period_start_date: str | None = Field(default=None)
    current_billing_period_end_date: str | None = Field(default=None)
    active_plan_phase_order: int | None = Field(default=None)
    fixed_fee_quantity_schedule: list[dict[str, Any]] | None = Field(default=None)
    price_intervals: list[dict[str, Any]] | None = Field(default=None)
    redeemed_coupon: dict[str, Any] | None = Field(default=None)
    default_invoice_memo: str | None = Field(default=None)
    auto_collection: bool | None = Field(default=None)
    net_terms: int | None = Field(default=None)
    invoicing_threshold: str | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)

class SubscriptionsList(BaseModel):
    """Paginated list of subscriptions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Subscription] | None = Field(default=None)
    pagination_metadata: PaginationMetadata | None = Field(default=None)

class PlanProduct(BaseModel):
    """The product associated with the plan"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The product ID")
    """The product ID"""
    name: str | None | None = Field(default=None, description="The product name")
    """The product name"""

class PlanPricesItem(BaseModel):
    """Nested schema for Plan.prices_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The unique identifier of the price")
    """The unique identifier of the price"""
    name: str | None | None = Field(default=None, description="The name of the price")
    """The name of the price"""
    price_type: str | None | None = Field(default=None, description="The type of price")
    """The type of price"""
    model_type: str | None | None = Field(default=None, description="The model type of the price")
    """The model type of the price"""
    currency: str | None | None = Field(default=None, description="The currency of the price")
    """The currency of the price"""

class Plan(BaseModel):
    """Plan object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    created_at: str | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    status: str | None = Field(default=None)
    default_invoice_memo: str | None = Field(default=None)
    net_terms: int | None = Field(default=None)
    currency: str | None = Field(default=None)
    prices: list[PlanPricesItem] | None = Field(default=None)
    product: PlanProduct | None = Field(default=None)
    minimum: dict[str, Any] | None = Field(default=None)
    maximum: dict[str, Any] | None = Field(default=None)
    discount: dict[str, Any] | None = Field(default=None)
    trial_config: dict[str, Any] | None = Field(default=None)
    plan_phases: list[dict[str, Any]] | None = Field(default=None)
    external_plan_id: str | None = Field(default=None)
    invoicing_currency: str | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)

class PlansList(BaseModel):
    """Paginated list of plans"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Plan] | None = Field(default=None)
    pagination_metadata: PaginationMetadata | None = Field(default=None)

class InvoiceSubscription(BaseModel):
    """The subscription associated with the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The subscription ID")
    """The subscription ID"""

class InvoiceLineItemsItem(BaseModel):
    """Nested schema for Invoice.line_items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The unique identifier of the line item")
    """The unique identifier of the line item"""
    quantity: float | None | None = Field(default=None, description="The quantity of the line item")
    """The quantity of the line item"""
    amount: str | None | None = Field(default=None, description="The amount of the line item")
    """The amount of the line item"""
    name: str | None | None = Field(default=None, description="The name of the line item")
    """The name of the line item"""
    start_date: str | None | None = Field(default=None, description="The start date of the line item")
    """The start date of the line item"""
    end_date: str | None | None = Field(default=None, description="The end date of the line item")
    """The end date of the line item"""

class InvoiceCustomer(BaseModel):
    """The customer associated with the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="The customer ID")
    """The customer ID"""
    external_customer_id: str | None | None = Field(default=None, description="The external customer ID")
    """The external customer ID"""

class Invoice(BaseModel):
    """Invoice object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    created_at: str | None = Field(default=None)
    invoice_date: str | None = Field(default=None)
    due_date: str | None = Field(default=None)
    invoice_pdf: str | None = Field(default=None)
    subtotal: str | None = Field(default=None)
    total: str | None = Field(default=None)
    amount_due: str | None = Field(default=None)
    status: str | None = Field(default=None)
    memo: str | None = Field(default=None)
    issue_failed_at: str | None = Field(default=None)
    sync_failed_at: str | None = Field(default=None)
    payment_failed_at: str | None = Field(default=None)
    payment_started_at: str | None = Field(default=None)
    voided_at: str | None = Field(default=None)
    paid_at: str | None = Field(default=None)
    issued_at: str | None = Field(default=None)
    hosted_invoice_url: str | None = Field(default=None)
    line_items: list[InvoiceLineItemsItem] | None = Field(default=None)
    subscription: InvoiceSubscription | None = Field(default=None)
    customer: InvoiceCustomer | None = Field(default=None)
    currency: str | None = Field(default=None)
    discount: dict[str, Any] | None = Field(default=None)
    minimum: dict[str, Any] | None = Field(default=None)
    maximum: dict[str, Any] | None = Field(default=None)
    credit_notes: list[dict[str, Any]] | None = Field(default=None)
    will_auto_issue: bool | None = Field(default=None)
    eligible_to_issue_at: str | None = Field(default=None)
    customer_balance_transactions: list[dict[str, Any]] | None = Field(default=None)
    auto_collection: dict[str, Any] | None = Field(default=None)
    invoice_number: str | None = Field(default=None)
    billing_address: Any | None = Field(default=None)
    shipping_address: Any | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)

class InvoicesList(BaseModel):
    """Paginated list of invoices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Invoice] | None = Field(default=None)
    pagination_metadata: PaginationMetadata | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CustomersListResultMeta(BaseModel):
    """Metadata for customers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

class SubscriptionsListResultMeta(BaseModel):
    """Metadata for subscriptions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

class PlansListResultMeta(BaseModel):
    """Metadata for plans.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

class InvoicesListResultMeta(BaseModel):
    """Metadata for invoices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class OrbCheckResult(BaseModel):
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


class OrbExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class OrbExecuteResultWithMeta(OrbExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CustomersSearchData(BaseModel):
    """Search result data for customers entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """The unique identifier of the customer"""
    external_customer_id: str | None = None
    """The ID of the customer in an external system"""
    name: str | None = None
    """The name of the customer"""
    email: str | None = None
    """The email address of the customer"""
    created_at: str | None = None
    """The date and time when the customer was created"""
    payment_provider: str | None = None
    """The payment provider used by the customer"""
    payment_provider_id: str | None = None
    """The ID of the customer in the payment provider's system"""
    timezone: str | None = None
    """The timezone setting of the customer"""
    shipping_address: dict[str, Any] | None = None
    """The shipping address of the customer"""
    billing_address: dict[str, Any] | None = None
    """The billing address of the customer"""


class SubscriptionsSearchData(BaseModel):
    """Search result data for subscriptions entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """The unique identifier of the subscription"""
    created_at: str | None = None
    """The date and time when the subscription was created"""
    start_date: str | None = None
    """The date and time when the subscription starts"""
    end_date: str | None = None
    """The date and time when the subscription ends"""
    status: str | None = None
    """The current status of the subscription"""


class PlansSearchData(BaseModel):
    """Search result data for plans entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """The unique identifier of the plan"""
    created_at: str | None = None
    """The date and time when the plan was created"""
    name: str | None = None
    """The name of the plan"""
    description: str | None = None
    """A description of the plan"""
    prices: list[Any] | None = None
    """The pricing options for the plan"""
    product: dict[str, Any] | None = None
    """The product associated with the plan"""


class InvoicesSearchData(BaseModel):
    """Search result data for invoices entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """The unique identifier of the invoice"""
    created_at: str | None = None
    """The date and time when the invoice was created"""
    invoice_date: str | None = None
    """The date of the invoice"""
    due_date: str | None = None
    """The due date for the invoice"""
    invoice_pdf: str | None = None
    """The URL to download the PDF version of the invoice"""
    subtotal: str | None = None
    """The subtotal amount of the invoice"""
    total: str | None = None
    """The total amount of the invoice"""
    amount_due: str | None = None
    """The amount due on the invoice"""
    status: str | None = None
    """The current status of the invoice"""
    memo: str | None = None
    """Any additional notes or comments on the invoice"""
    paid_at: str | None = None
    """The date and time when the invoice was paid"""
    issued_at: str | None = None
    """The date and time when the invoice was issued"""
    hosted_invoice_url: str | None = None
    """The URL to view the hosted invoice"""
    line_items: list[Any] | None = None
    """The line items on the invoice"""
    subscription: dict[str, Any] | None = None
    """The subscription associated with the invoice"""


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

CustomersSearchResult = AirbyteSearchResult[CustomersSearchData]
"""Search result type for customers entity."""

SubscriptionsSearchResult = AirbyteSearchResult[SubscriptionsSearchData]
"""Search result type for subscriptions entity."""

PlansSearchResult = AirbyteSearchResult[PlansSearchData]
"""Search result type for plans entity."""

InvoicesSearchResult = AirbyteSearchResult[InvoicesSearchData]
"""Search result type for invoices entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CustomersListResult = OrbExecuteResultWithMeta[list[Customer], CustomersListResultMeta]
"""Result type for customers.list operation with data and metadata."""

SubscriptionsListResult = OrbExecuteResultWithMeta[list[Subscription], SubscriptionsListResultMeta]
"""Result type for subscriptions.list operation with data and metadata."""

PlansListResult = OrbExecuteResultWithMeta[list[Plan], PlansListResultMeta]
"""Result type for plans.list operation with data and metadata."""

InvoicesListResult = OrbExecuteResultWithMeta[list[Invoice], InvoicesListResultMeta]
"""Result type for invoices.list operation with data and metadata."""

