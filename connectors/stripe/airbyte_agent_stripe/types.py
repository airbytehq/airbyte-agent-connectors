"""
Type definitions for stripe connector.
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

class CustomersListParamsCreated(TypedDict):
    """Nested schema for CustomersListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class InvoicesListParamsCreated(TypedDict):
    """Nested schema for InvoicesListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class ChargesListParamsCreated(TypedDict):
    """Nested schema for ChargesListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class SubscriptionsListParamsAutomaticTax(TypedDict):
    """Nested schema for SubscriptionsListParams.automatic_tax"""
    enabled: NotRequired[bool]

class SubscriptionsListParamsCreated(TypedDict):
    """Nested schema for SubscriptionsListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class SubscriptionsListParamsCurrentPeriodEnd(TypedDict):
    """Nested schema for SubscriptionsListParams.current_period_end"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class SubscriptionsListParamsCurrentPeriodStart(TypedDict):
    """Nested schema for SubscriptionsListParams.current_period_start"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class RefundsListParamsCreated(TypedDict):
    """Nested schema for RefundsListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class ProductsListParamsCreated(TypedDict):
    """Nested schema for ProductsListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class BalanceTransactionsListParamsCreated(TypedDict):
    """Nested schema for BalanceTransactionsListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class PaymentIntentsListParamsCreated(TypedDict):
    """Nested schema for PaymentIntentsListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class DisputesListParamsCreated(TypedDict):
    """Nested schema for DisputesListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class PayoutsListParamsArrivalDate(TypedDict):
    """Nested schema for PayoutsListParams.arrival_date"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

class PayoutsListParamsCreated(TypedDict):
    """Nested schema for PayoutsListParams.created"""
    gt: NotRequired[int]
    gte: NotRequired[int]
    lt: NotRequired[int]
    lte: NotRequired[int]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    limit: NotRequired[int]
    starting_after: NotRequired[str]
    ending_before: NotRequired[str]
    email: NotRequired[str]
    created: NotRequired[CustomersListParamsCreated]

class CustomersCreateParams(TypedDict):
    """Parameters for customers.create operation"""
    pass

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    id: str

class CustomersUpdateParams(TypedDict):
    """Parameters for customers.update operation"""
    id: str

class CustomersDeleteParams(TypedDict):
    """Parameters for customers.delete operation"""
    id: str

class CustomersApiSearchParams(TypedDict):
    """Parameters for customers.api_search operation"""
    query: str
    limit: NotRequired[int]
    page: NotRequired[str]

class InvoicesListParams(TypedDict):
    """Parameters for invoices.list operation"""
    collection_method: NotRequired[str]
    created: NotRequired[InvoicesListParamsCreated]
    customer: NotRequired[str]
    customer_account: NotRequired[str]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    starting_after: NotRequired[str]
    status: NotRequired[str]
    subscription: NotRequired[str]

class InvoicesGetParams(TypedDict):
    """Parameters for invoices.get operation"""
    id: str

class InvoicesApiSearchParams(TypedDict):
    """Parameters for invoices.api_search operation"""
    query: str
    limit: NotRequired[int]
    page: NotRequired[str]

class ChargesListParams(TypedDict):
    """Parameters for charges.list operation"""
    created: NotRequired[ChargesListParamsCreated]
    customer: NotRequired[str]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    payment_intent: NotRequired[str]
    starting_after: NotRequired[str]

class ChargesGetParams(TypedDict):
    """Parameters for charges.get operation"""
    id: str

class ChargesApiSearchParams(TypedDict):
    """Parameters for charges.api_search operation"""
    query: str
    limit: NotRequired[int]
    page: NotRequired[str]

class SubscriptionsListParams(TypedDict):
    """Parameters for subscriptions.list operation"""
    automatic_tax: NotRequired[SubscriptionsListParamsAutomaticTax]
    collection_method: NotRequired[str]
    created: NotRequired[SubscriptionsListParamsCreated]
    current_period_end: NotRequired[SubscriptionsListParamsCurrentPeriodEnd]
    current_period_start: NotRequired[SubscriptionsListParamsCurrentPeriodStart]
    customer: NotRequired[str]
    customer_account: NotRequired[str]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    price: NotRequired[str]
    starting_after: NotRequired[str]
    status: NotRequired[str]

class SubscriptionsGetParams(TypedDict):
    """Parameters for subscriptions.get operation"""
    id: str

class SubscriptionsApiSearchParams(TypedDict):
    """Parameters for subscriptions.api_search operation"""
    query: str
    limit: NotRequired[int]
    page: NotRequired[str]

class RefundsListParams(TypedDict):
    """Parameters for refunds.list operation"""
    charge: NotRequired[str]
    created: NotRequired[RefundsListParamsCreated]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    payment_intent: NotRequired[str]
    starting_after: NotRequired[str]

class RefundsCreateParams(TypedDict):
    """Parameters for refunds.create operation"""
    pass

class RefundsGetParams(TypedDict):
    """Parameters for refunds.get operation"""
    id: str

class ProductsListParams(TypedDict):
    """Parameters for products.list operation"""
    active: NotRequired[bool]
    created: NotRequired[ProductsListParamsCreated]
    ending_before: NotRequired[str]
    ids: NotRequired[list[str]]
    limit: NotRequired[int]
    shippable: NotRequired[bool]
    starting_after: NotRequired[str]
    url: NotRequired[str]

class ProductsCreateParams(TypedDict):
    """Parameters for products.create operation"""
    pass

class ProductsGetParams(TypedDict):
    """Parameters for products.get operation"""
    id: str

class ProductsUpdateParams(TypedDict):
    """Parameters for products.update operation"""
    id: str

class ProductsDeleteParams(TypedDict):
    """Parameters for products.delete operation"""
    id: str

class ProductsApiSearchParams(TypedDict):
    """Parameters for products.api_search operation"""
    query: str
    limit: NotRequired[int]
    page: NotRequired[str]

class BalanceGetParams(TypedDict):
    """Parameters for balance.get operation"""
    pass

class BalanceTransactionsListParams(TypedDict):
    """Parameters for balance_transactions.list operation"""
    created: NotRequired[BalanceTransactionsListParamsCreated]
    currency: NotRequired[str]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    payout: NotRequired[str]
    source: NotRequired[str]
    starting_after: NotRequired[str]
    type: NotRequired[str]

class BalanceTransactionsGetParams(TypedDict):
    """Parameters for balance_transactions.get operation"""
    id: str

class PaymentIntentsListParams(TypedDict):
    """Parameters for payment_intents.list operation"""
    created: NotRequired[PaymentIntentsListParamsCreated]
    customer: NotRequired[str]
    customer_account: NotRequired[str]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    starting_after: NotRequired[str]

class PaymentIntentsGetParams(TypedDict):
    """Parameters for payment_intents.get operation"""
    id: str

class PaymentIntentsApiSearchParams(TypedDict):
    """Parameters for payment_intents.api_search operation"""
    query: str
    limit: NotRequired[int]
    page: NotRequired[str]

class DisputesListParams(TypedDict):
    """Parameters for disputes.list operation"""
    charge: NotRequired[str]
    created: NotRequired[DisputesListParamsCreated]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    payment_intent: NotRequired[str]
    starting_after: NotRequired[str]

class DisputesGetParams(TypedDict):
    """Parameters for disputes.get operation"""
    id: str

class PayoutsListParams(TypedDict):
    """Parameters for payouts.list operation"""
    arrival_date: NotRequired[PayoutsListParamsArrivalDate]
    created: NotRequired[PayoutsListParamsCreated]
    destination: NotRequired[str]
    ending_before: NotRequired[str]
    limit: NotRequired[int]
    starting_after: NotRequired[str]
    status: NotRequired[str]

class PayoutsGetParams(TypedDict):
    """Parameters for payouts.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CHARGES SEARCH TYPES =====

class ChargesSearchFilter(TypedDict, total=False):
    """Available fields for filtering charges search queries."""
    amount: int | None
    """Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits."""
    amount_captured: int | None
    """Amount that was actually captured from this charge."""
    amount_refunded: int | None
    """Amount that has been refunded back to the customer."""
    amount_updates: list[Any] | None
    """Updates to the amount that have been made during the charge lifecycle."""
    application: str | None
    """ID of the application that created this charge (Connect only)."""
    application_fee: str | None
    """ID of the application fee associated with this charge (Connect only)."""
    application_fee_amount: int | None
    """The amount of the application fee deducted from this charge (Connect only)."""
    balance_transaction: str | None
    """ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes)."""
    billing_details: dict[str, Any] | None
    """Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address."""
    calculated_statement_descriptor: str | None
    """The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix."""
    captured: bool | None
    """Whether the charge has been captured and funds transferred to your account."""
    card: dict[str, Any] | None
    """Deprecated card object containing payment card details if a card was used."""
    created: int | None
    """Timestamp indicating when the charge was created."""
    currency: str | None
    """Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount."""
    customer: str | None
    """ID of the customer this charge is for, if one exists."""
    description: str | None
    """An arbitrary string attached to the charge, often useful for displaying to users or internal reference."""
    destination: str | None
    """ID of the destination account where funds are transferred (Connect only)."""
    dispute: str | None
    """ID of the dispute object if the charge has been disputed."""
    disputed: bool | None
    """Whether the charge has been disputed by the customer with their card issuer."""
    failure_balance_transaction: str | None
    """ID of the balance transaction that describes the reversal of funds if the charge failed."""
    failure_code: str | None
    """Error code explaining the reason for charge failure, if applicable."""
    failure_message: str | None
    """Human-readable message providing more details about why the charge failed."""
    fraud_details: dict[str, Any] | None
    """Information about fraud assessments and user reports related to this charge."""
    id: str
    """Unique identifier for the charge, used to link transactions across other records."""
    invoice: str | None
    """ID of the invoice this charge is for, if the charge was created by invoicing."""
    livemode: bool | None
    """Whether the charge occurred in live mode (true) or test mode (false)."""
    metadata: dict[str, Any] | None
    """Key-value pairs for storing additional structured information about the charge, useful for internal tracking."""
    object: str | None
    """String representing the object type, always 'charge' for charge objects."""
    on_behalf_of: str | None
    """ID of the account on whose behalf the charge was made (Connect only)."""
    order: str | None
    """Deprecated field for order information associated with this charge."""
    outcome: dict[str, Any] | None
    """Details about the outcome of the charge, including network status, risk assessment, and reason codes."""
    paid: bool | None
    """Whether the charge succeeded and funds were successfully collected."""
    payment_intent: str | None
    """ID of the PaymentIntent associated with this charge, if one exists."""
    payment_method: str | None
    """ID of the payment method used for this charge."""
    payment_method_details: dict[str, Any] | None
    """Details about the payment method at the time of the transaction, including card brand, network, and authentication results."""
    receipt_email: str | None
    """Email address to which the receipt for this charge was sent."""
    receipt_number: str | None
    """Receipt number that appears on email receipts sent for this charge."""
    receipt_url: str | None
    """URL to a hosted receipt page for this charge, viewable by the customer."""
    refunded: bool | None
    """Whether the charge has been fully refunded (partial refunds will still show as false)."""
    refunds: dict[str, Any] | None
    """List of refunds that have been applied to this charge."""
    review: str | None
    """ID of the review object associated with this charge, if it was flagged for manual review."""
    shipping: dict[str, Any] | None
    """Shipping information for the charge, including recipient name, address, and tracking details."""
    source: dict[str, Any] | None
    """Deprecated payment source object used to create this charge."""
    source_transfer: str | None
    """ID of the transfer from a source account if funds came from another Stripe account (Connect only)."""
    statement_description: str | None
    """Deprecated alias for statement_descriptor."""
    statement_descriptor: str | None
    """Statement descriptor that overrides the account default for card charges, appearing on the customer's statement."""
    statement_descriptor_suffix: str | None
    """Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements."""
    status: str | None
    """Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful)."""
    transfer_data: dict[str, Any] | None
    """Object containing destination and amount for transfers to connected accounts (Connect only)."""
    transfer_group: str | None
    """String identifier for grouping related charges and transfers together (Connect only)."""
    updated: int | None
    """Timestamp of the last update to this charge object."""


class ChargesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[int]
    """Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits."""
    amount_captured: list[int]
    """Amount that was actually captured from this charge."""
    amount_refunded: list[int]
    """Amount that has been refunded back to the customer."""
    amount_updates: list[list[Any]]
    """Updates to the amount that have been made during the charge lifecycle."""
    application: list[str]
    """ID of the application that created this charge (Connect only)."""
    application_fee: list[str]
    """ID of the application fee associated with this charge (Connect only)."""
    application_fee_amount: list[int]
    """The amount of the application fee deducted from this charge (Connect only)."""
    balance_transaction: list[str]
    """ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes)."""
    billing_details: list[dict[str, Any]]
    """Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address."""
    calculated_statement_descriptor: list[str]
    """The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix."""
    captured: list[bool]
    """Whether the charge has been captured and funds transferred to your account."""
    card: list[dict[str, Any]]
    """Deprecated card object containing payment card details if a card was used."""
    created: list[int]
    """Timestamp indicating when the charge was created."""
    currency: list[str]
    """Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount."""
    customer: list[str]
    """ID of the customer this charge is for, if one exists."""
    description: list[str]
    """An arbitrary string attached to the charge, often useful for displaying to users or internal reference."""
    destination: list[str]
    """ID of the destination account where funds are transferred (Connect only)."""
    dispute: list[str]
    """ID of the dispute object if the charge has been disputed."""
    disputed: list[bool]
    """Whether the charge has been disputed by the customer with their card issuer."""
    failure_balance_transaction: list[str]
    """ID of the balance transaction that describes the reversal of funds if the charge failed."""
    failure_code: list[str]
    """Error code explaining the reason for charge failure, if applicable."""
    failure_message: list[str]
    """Human-readable message providing more details about why the charge failed."""
    fraud_details: list[dict[str, Any]]
    """Information about fraud assessments and user reports related to this charge."""
    id: list[str]
    """Unique identifier for the charge, used to link transactions across other records."""
    invoice: list[str]
    """ID of the invoice this charge is for, if the charge was created by invoicing."""
    livemode: list[bool]
    """Whether the charge occurred in live mode (true) or test mode (false)."""
    metadata: list[dict[str, Any]]
    """Key-value pairs for storing additional structured information about the charge, useful for internal tracking."""
    object: list[str]
    """String representing the object type, always 'charge' for charge objects."""
    on_behalf_of: list[str]
    """ID of the account on whose behalf the charge was made (Connect only)."""
    order: list[str]
    """Deprecated field for order information associated with this charge."""
    outcome: list[dict[str, Any]]
    """Details about the outcome of the charge, including network status, risk assessment, and reason codes."""
    paid: list[bool]
    """Whether the charge succeeded and funds were successfully collected."""
    payment_intent: list[str]
    """ID of the PaymentIntent associated with this charge, if one exists."""
    payment_method: list[str]
    """ID of the payment method used for this charge."""
    payment_method_details: list[dict[str, Any]]
    """Details about the payment method at the time of the transaction, including card brand, network, and authentication results."""
    receipt_email: list[str]
    """Email address to which the receipt for this charge was sent."""
    receipt_number: list[str]
    """Receipt number that appears on email receipts sent for this charge."""
    receipt_url: list[str]
    """URL to a hosted receipt page for this charge, viewable by the customer."""
    refunded: list[bool]
    """Whether the charge has been fully refunded (partial refunds will still show as false)."""
    refunds: list[dict[str, Any]]
    """List of refunds that have been applied to this charge."""
    review: list[str]
    """ID of the review object associated with this charge, if it was flagged for manual review."""
    shipping: list[dict[str, Any]]
    """Shipping information for the charge, including recipient name, address, and tracking details."""
    source: list[dict[str, Any]]
    """Deprecated payment source object used to create this charge."""
    source_transfer: list[str]
    """ID of the transfer from a source account if funds came from another Stripe account (Connect only)."""
    statement_description: list[str]
    """Deprecated alias for statement_descriptor."""
    statement_descriptor: list[str]
    """Statement descriptor that overrides the account default for card charges, appearing on the customer's statement."""
    statement_descriptor_suffix: list[str]
    """Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements."""
    status: list[str]
    """Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful)."""
    transfer_data: list[dict[str, Any]]
    """Object containing destination and amount for transfers to connected accounts (Connect only)."""
    transfer_group: list[str]
    """String identifier for grouping related charges and transfers together (Connect only)."""
    updated: list[int]
    """Timestamp of the last update to this charge object."""


class ChargesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits."""
    amount_captured: Any
    """Amount that was actually captured from this charge."""
    amount_refunded: Any
    """Amount that has been refunded back to the customer."""
    amount_updates: Any
    """Updates to the amount that have been made during the charge lifecycle."""
    application: Any
    """ID of the application that created this charge (Connect only)."""
    application_fee: Any
    """ID of the application fee associated with this charge (Connect only)."""
    application_fee_amount: Any
    """The amount of the application fee deducted from this charge (Connect only)."""
    balance_transaction: Any
    """ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes)."""
    billing_details: Any
    """Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address."""
    calculated_statement_descriptor: Any
    """The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix."""
    captured: Any
    """Whether the charge has been captured and funds transferred to your account."""
    card: Any
    """Deprecated card object containing payment card details if a card was used."""
    created: Any
    """Timestamp indicating when the charge was created."""
    currency: Any
    """Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount."""
    customer: Any
    """ID of the customer this charge is for, if one exists."""
    description: Any
    """An arbitrary string attached to the charge, often useful for displaying to users or internal reference."""
    destination: Any
    """ID of the destination account where funds are transferred (Connect only)."""
    dispute: Any
    """ID of the dispute object if the charge has been disputed."""
    disputed: Any
    """Whether the charge has been disputed by the customer with their card issuer."""
    failure_balance_transaction: Any
    """ID of the balance transaction that describes the reversal of funds if the charge failed."""
    failure_code: Any
    """Error code explaining the reason for charge failure, if applicable."""
    failure_message: Any
    """Human-readable message providing more details about why the charge failed."""
    fraud_details: Any
    """Information about fraud assessments and user reports related to this charge."""
    id: Any
    """Unique identifier for the charge, used to link transactions across other records."""
    invoice: Any
    """ID of the invoice this charge is for, if the charge was created by invoicing."""
    livemode: Any
    """Whether the charge occurred in live mode (true) or test mode (false)."""
    metadata: Any
    """Key-value pairs for storing additional structured information about the charge, useful for internal tracking."""
    object: Any
    """String representing the object type, always 'charge' for charge objects."""
    on_behalf_of: Any
    """ID of the account on whose behalf the charge was made (Connect only)."""
    order: Any
    """Deprecated field for order information associated with this charge."""
    outcome: Any
    """Details about the outcome of the charge, including network status, risk assessment, and reason codes."""
    paid: Any
    """Whether the charge succeeded and funds were successfully collected."""
    payment_intent: Any
    """ID of the PaymentIntent associated with this charge, if one exists."""
    payment_method: Any
    """ID of the payment method used for this charge."""
    payment_method_details: Any
    """Details about the payment method at the time of the transaction, including card brand, network, and authentication results."""
    receipt_email: Any
    """Email address to which the receipt for this charge was sent."""
    receipt_number: Any
    """Receipt number that appears on email receipts sent for this charge."""
    receipt_url: Any
    """URL to a hosted receipt page for this charge, viewable by the customer."""
    refunded: Any
    """Whether the charge has been fully refunded (partial refunds will still show as false)."""
    refunds: Any
    """List of refunds that have been applied to this charge."""
    review: Any
    """ID of the review object associated with this charge, if it was flagged for manual review."""
    shipping: Any
    """Shipping information for the charge, including recipient name, address, and tracking details."""
    source: Any
    """Deprecated payment source object used to create this charge."""
    source_transfer: Any
    """ID of the transfer from a source account if funds came from another Stripe account (Connect only)."""
    statement_description: Any
    """Deprecated alias for statement_descriptor."""
    statement_descriptor: Any
    """Statement descriptor that overrides the account default for card charges, appearing on the customer's statement."""
    statement_descriptor_suffix: Any
    """Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements."""
    status: Any
    """Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful)."""
    transfer_data: Any
    """Object containing destination and amount for transfers to connected accounts (Connect only)."""
    transfer_group: Any
    """String identifier for grouping related charges and transfers together (Connect only)."""
    updated: Any
    """Timestamp of the last update to this charge object."""


class ChargesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits."""
    amount_captured: str
    """Amount that was actually captured from this charge."""
    amount_refunded: str
    """Amount that has been refunded back to the customer."""
    amount_updates: str
    """Updates to the amount that have been made during the charge lifecycle."""
    application: str
    """ID of the application that created this charge (Connect only)."""
    application_fee: str
    """ID of the application fee associated with this charge (Connect only)."""
    application_fee_amount: str
    """The amount of the application fee deducted from this charge (Connect only)."""
    balance_transaction: str
    """ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes)."""
    billing_details: str
    """Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address."""
    calculated_statement_descriptor: str
    """The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix."""
    captured: str
    """Whether the charge has been captured and funds transferred to your account."""
    card: str
    """Deprecated card object containing payment card details if a card was used."""
    created: str
    """Timestamp indicating when the charge was created."""
    currency: str
    """Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount."""
    customer: str
    """ID of the customer this charge is for, if one exists."""
    description: str
    """An arbitrary string attached to the charge, often useful for displaying to users or internal reference."""
    destination: str
    """ID of the destination account where funds are transferred (Connect only)."""
    dispute: str
    """ID of the dispute object if the charge has been disputed."""
    disputed: str
    """Whether the charge has been disputed by the customer with their card issuer."""
    failure_balance_transaction: str
    """ID of the balance transaction that describes the reversal of funds if the charge failed."""
    failure_code: str
    """Error code explaining the reason for charge failure, if applicable."""
    failure_message: str
    """Human-readable message providing more details about why the charge failed."""
    fraud_details: str
    """Information about fraud assessments and user reports related to this charge."""
    id: str
    """Unique identifier for the charge, used to link transactions across other records."""
    invoice: str
    """ID of the invoice this charge is for, if the charge was created by invoicing."""
    livemode: str
    """Whether the charge occurred in live mode (true) or test mode (false)."""
    metadata: str
    """Key-value pairs for storing additional structured information about the charge, useful for internal tracking."""
    object: str
    """String representing the object type, always 'charge' for charge objects."""
    on_behalf_of: str
    """ID of the account on whose behalf the charge was made (Connect only)."""
    order: str
    """Deprecated field for order information associated with this charge."""
    outcome: str
    """Details about the outcome of the charge, including network status, risk assessment, and reason codes."""
    paid: str
    """Whether the charge succeeded and funds were successfully collected."""
    payment_intent: str
    """ID of the PaymentIntent associated with this charge, if one exists."""
    payment_method: str
    """ID of the payment method used for this charge."""
    payment_method_details: str
    """Details about the payment method at the time of the transaction, including card brand, network, and authentication results."""
    receipt_email: str
    """Email address to which the receipt for this charge was sent."""
    receipt_number: str
    """Receipt number that appears on email receipts sent for this charge."""
    receipt_url: str
    """URL to a hosted receipt page for this charge, viewable by the customer."""
    refunded: str
    """Whether the charge has been fully refunded (partial refunds will still show as false)."""
    refunds: str
    """List of refunds that have been applied to this charge."""
    review: str
    """ID of the review object associated with this charge, if it was flagged for manual review."""
    shipping: str
    """Shipping information for the charge, including recipient name, address, and tracking details."""
    source: str
    """Deprecated payment source object used to create this charge."""
    source_transfer: str
    """ID of the transfer from a source account if funds came from another Stripe account (Connect only)."""
    statement_description: str
    """Deprecated alias for statement_descriptor."""
    statement_descriptor: str
    """Statement descriptor that overrides the account default for card charges, appearing on the customer's statement."""
    statement_descriptor_suffix: str
    """Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements."""
    status: str
    """Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful)."""
    transfer_data: str
    """Object containing destination and amount for transfers to connected accounts (Connect only)."""
    transfer_group: str
    """String identifier for grouping related charges and transfers together (Connect only)."""
    updated: str
    """Timestamp of the last update to this charge object."""


class ChargesSortFilter(TypedDict, total=False):
    """Available fields for sorting charges search results."""
    amount: AirbyteSortOrder
    """Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits."""
    amount_captured: AirbyteSortOrder
    """Amount that was actually captured from this charge."""
    amount_refunded: AirbyteSortOrder
    """Amount that has been refunded back to the customer."""
    amount_updates: AirbyteSortOrder
    """Updates to the amount that have been made during the charge lifecycle."""
    application: AirbyteSortOrder
    """ID of the application that created this charge (Connect only)."""
    application_fee: AirbyteSortOrder
    """ID of the application fee associated with this charge (Connect only)."""
    application_fee_amount: AirbyteSortOrder
    """The amount of the application fee deducted from this charge (Connect only)."""
    balance_transaction: AirbyteSortOrder
    """ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes)."""
    billing_details: AirbyteSortOrder
    """Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address."""
    calculated_statement_descriptor: AirbyteSortOrder
    """The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix."""
    captured: AirbyteSortOrder
    """Whether the charge has been captured and funds transferred to your account."""
    card: AirbyteSortOrder
    """Deprecated card object containing payment card details if a card was used."""
    created: AirbyteSortOrder
    """Timestamp indicating when the charge was created."""
    currency: AirbyteSortOrder
    """Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount."""
    customer: AirbyteSortOrder
    """ID of the customer this charge is for, if one exists."""
    description: AirbyteSortOrder
    """An arbitrary string attached to the charge, often useful for displaying to users or internal reference."""
    destination: AirbyteSortOrder
    """ID of the destination account where funds are transferred (Connect only)."""
    dispute: AirbyteSortOrder
    """ID of the dispute object if the charge has been disputed."""
    disputed: AirbyteSortOrder
    """Whether the charge has been disputed by the customer with their card issuer."""
    failure_balance_transaction: AirbyteSortOrder
    """ID of the balance transaction that describes the reversal of funds if the charge failed."""
    failure_code: AirbyteSortOrder
    """Error code explaining the reason for charge failure, if applicable."""
    failure_message: AirbyteSortOrder
    """Human-readable message providing more details about why the charge failed."""
    fraud_details: AirbyteSortOrder
    """Information about fraud assessments and user reports related to this charge."""
    id: AirbyteSortOrder
    """Unique identifier for the charge, used to link transactions across other records."""
    invoice: AirbyteSortOrder
    """ID of the invoice this charge is for, if the charge was created by invoicing."""
    livemode: AirbyteSortOrder
    """Whether the charge occurred in live mode (true) or test mode (false)."""
    metadata: AirbyteSortOrder
    """Key-value pairs for storing additional structured information about the charge, useful for internal tracking."""
    object: AirbyteSortOrder
    """String representing the object type, always 'charge' for charge objects."""
    on_behalf_of: AirbyteSortOrder
    """ID of the account on whose behalf the charge was made (Connect only)."""
    order: AirbyteSortOrder
    """Deprecated field for order information associated with this charge."""
    outcome: AirbyteSortOrder
    """Details about the outcome of the charge, including network status, risk assessment, and reason codes."""
    paid: AirbyteSortOrder
    """Whether the charge succeeded and funds were successfully collected."""
    payment_intent: AirbyteSortOrder
    """ID of the PaymentIntent associated with this charge, if one exists."""
    payment_method: AirbyteSortOrder
    """ID of the payment method used for this charge."""
    payment_method_details: AirbyteSortOrder
    """Details about the payment method at the time of the transaction, including card brand, network, and authentication results."""
    receipt_email: AirbyteSortOrder
    """Email address to which the receipt for this charge was sent."""
    receipt_number: AirbyteSortOrder
    """Receipt number that appears on email receipts sent for this charge."""
    receipt_url: AirbyteSortOrder
    """URL to a hosted receipt page for this charge, viewable by the customer."""
    refunded: AirbyteSortOrder
    """Whether the charge has been fully refunded (partial refunds will still show as false)."""
    refunds: AirbyteSortOrder
    """List of refunds that have been applied to this charge."""
    review: AirbyteSortOrder
    """ID of the review object associated with this charge, if it was flagged for manual review."""
    shipping: AirbyteSortOrder
    """Shipping information for the charge, including recipient name, address, and tracking details."""
    source: AirbyteSortOrder
    """Deprecated payment source object used to create this charge."""
    source_transfer: AirbyteSortOrder
    """ID of the transfer from a source account if funds came from another Stripe account (Connect only)."""
    statement_description: AirbyteSortOrder
    """Deprecated alias for statement_descriptor."""
    statement_descriptor: AirbyteSortOrder
    """Statement descriptor that overrides the account default for card charges, appearing on the customer's statement."""
    statement_descriptor_suffix: AirbyteSortOrder
    """Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements."""
    status: AirbyteSortOrder
    """Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful)."""
    transfer_data: AirbyteSortOrder
    """Object containing destination and amount for transfers to connected accounts (Connect only)."""
    transfer_group: AirbyteSortOrder
    """String identifier for grouping related charges and transfers together (Connect only)."""
    updated: AirbyteSortOrder
    """Timestamp of the last update to this charge object."""


# Entity-specific condition types for charges
class ChargesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ChargesSearchFilter


class ChargesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ChargesSearchFilter


class ChargesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ChargesSearchFilter


class ChargesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ChargesSearchFilter


class ChargesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ChargesSearchFilter


class ChargesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ChargesSearchFilter


class ChargesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ChargesStringFilter


class ChargesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ChargesStringFilter


class ChargesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ChargesStringFilter


class ChargesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ChargesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ChargesInCondition = TypedDict("ChargesInCondition", {"in": ChargesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ChargesNotCondition = TypedDict("ChargesNotCondition", {"not": "ChargesCondition"}, total=False)
"""Negates the nested condition."""

ChargesAndCondition = TypedDict("ChargesAndCondition", {"and": "list[ChargesCondition]"}, total=False)
"""True if all nested conditions are true."""

ChargesOrCondition = TypedDict("ChargesOrCondition", {"or": "list[ChargesCondition]"}, total=False)
"""True if any nested condition is true."""

ChargesAnyCondition = TypedDict("ChargesAnyCondition", {"any": ChargesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all charges condition types
ChargesCondition = (
    ChargesEqCondition
    | ChargesNeqCondition
    | ChargesGtCondition
    | ChargesGteCondition
    | ChargesLtCondition
    | ChargesLteCondition
    | ChargesInCondition
    | ChargesLikeCondition
    | ChargesFuzzyCondition
    | ChargesKeywordCondition
    | ChargesContainsCondition
    | ChargesNotCondition
    | ChargesAndCondition
    | ChargesOrCondition
    | ChargesAnyCondition
)


class ChargesSearchQuery(TypedDict, total=False):
    """Search query for charges entity."""
    filter: ChargesCondition
    sort: list[ChargesSortFilter]


# ===== CUSTOMERS SEARCH TYPES =====

class CustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering customers search queries."""
    account_balance: int | None
    """Current balance value representing funds owed by or to the customer."""
    address: dict[str, Any] | None
    """The customer's address information including line1, line2, city, state, postal code, and country."""
    balance: int | None
    """Current balance (positive or negative) that is automatically applied to the customer's next invoice."""
    cards: list[Any] | None
    """Card payment methods associated with the customer account."""
    created: int | None
    """Timestamp indicating when the customer object was created."""
    currency: str | None
    """Three-letter ISO currency code representing the customer's default currency."""
    default_card: str | None
    """The default card to be used for charges when no specific payment method is provided."""
    default_source: str | None
    """The default payment source (card or bank account) for the customer."""
    delinquent: bool | None
    """Boolean indicating whether the customer is currently delinquent on payments."""
    description: str | None
    """An arbitrary string attached to the customer, often useful for displaying to users."""
    discount: dict[str, Any] | None
    """Discount object describing any active discount applied to the customer."""
    email: str | None
    """The customer's email address for communication and tracking purposes."""
    id: str | None
    """Unique identifier for the customer object."""
    invoice_prefix: str | None
    """The prefix for invoice numbers generated for this customer."""
    invoice_settings: dict[str, Any] | None
    """Customer's invoice-related settings including default payment method and custom fields."""
    is_deleted: bool | None
    """Boolean indicating whether the customer has been deleted."""
    livemode: bool | None
    """Boolean indicating whether the object exists in live mode or test mode."""
    metadata: dict[str, Any] | None
    """Set of key-value pairs for storing additional structured information about the customer."""
    name: str | None
    """The customer's full name or business name."""
    next_invoice_sequence: int | None
    """The sequence number for the next invoice generated for this customer."""
    object: str | None
    """String representing the object type, always 'customer'."""
    phone: str | None
    """The customer's phone number."""
    preferred_locales: list[Any] | None
    """Array of preferred locales for the customer, used for invoice and receipt localization."""
    shipping: dict[str, Any] | None
    """Mailing and shipping address for the customer, appears on invoices emailed to the customer."""
    sources: str
    """Payment sources (cards, bank accounts) attached to the customer for making payments."""
    subscriptions: dict[str, Any] | None
    """List of active subscriptions associated with the customer."""
    tax_exempt: str | None
    """Describes the customer's tax exemption status (none, exempt, or reverse)."""
    tax_info: str | None
    """Tax identification information for the customer."""
    tax_info_verification: str | None
    """Verification status of the customer's tax information."""
    test_clock: str | None
    """ID of the test clock associated with this customer for testing time-dependent scenarios."""
    updated: int | None
    """Timestamp indicating when the customer object was last updated."""


class CustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_balance: list[int]
    """Current balance value representing funds owed by or to the customer."""
    address: list[dict[str, Any]]
    """The customer's address information including line1, line2, city, state, postal code, and country."""
    balance: list[int]
    """Current balance (positive or negative) that is automatically applied to the customer's next invoice."""
    cards: list[list[Any]]
    """Card payment methods associated with the customer account."""
    created: list[int]
    """Timestamp indicating when the customer object was created."""
    currency: list[str]
    """Three-letter ISO currency code representing the customer's default currency."""
    default_card: list[str]
    """The default card to be used for charges when no specific payment method is provided."""
    default_source: list[str]
    """The default payment source (card or bank account) for the customer."""
    delinquent: list[bool]
    """Boolean indicating whether the customer is currently delinquent on payments."""
    description: list[str]
    """An arbitrary string attached to the customer, often useful for displaying to users."""
    discount: list[dict[str, Any]]
    """Discount object describing any active discount applied to the customer."""
    email: list[str]
    """The customer's email address for communication and tracking purposes."""
    id: list[str]
    """Unique identifier for the customer object."""
    invoice_prefix: list[str]
    """The prefix for invoice numbers generated for this customer."""
    invoice_settings: list[dict[str, Any]]
    """Customer's invoice-related settings including default payment method and custom fields."""
    is_deleted: list[bool]
    """Boolean indicating whether the customer has been deleted."""
    livemode: list[bool]
    """Boolean indicating whether the object exists in live mode or test mode."""
    metadata: list[dict[str, Any]]
    """Set of key-value pairs for storing additional structured information about the customer."""
    name: list[str]
    """The customer's full name or business name."""
    next_invoice_sequence: list[int]
    """The sequence number for the next invoice generated for this customer."""
    object: list[str]
    """String representing the object type, always 'customer'."""
    phone: list[str]
    """The customer's phone number."""
    preferred_locales: list[list[Any]]
    """Array of preferred locales for the customer, used for invoice and receipt localization."""
    shipping: list[dict[str, Any]]
    """Mailing and shipping address for the customer, appears on invoices emailed to the customer."""
    sources: list[str]
    """Payment sources (cards, bank accounts) attached to the customer for making payments."""
    subscriptions: list[dict[str, Any]]
    """List of active subscriptions associated with the customer."""
    tax_exempt: list[str]
    """Describes the customer's tax exemption status (none, exempt, or reverse)."""
    tax_info: list[str]
    """Tax identification information for the customer."""
    tax_info_verification: list[str]
    """Verification status of the customer's tax information."""
    test_clock: list[str]
    """ID of the test clock associated with this customer for testing time-dependent scenarios."""
    updated: list[int]
    """Timestamp indicating when the customer object was last updated."""


class CustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_balance: Any
    """Current balance value representing funds owed by or to the customer."""
    address: Any
    """The customer's address information including line1, line2, city, state, postal code, and country."""
    balance: Any
    """Current balance (positive or negative) that is automatically applied to the customer's next invoice."""
    cards: Any
    """Card payment methods associated with the customer account."""
    created: Any
    """Timestamp indicating when the customer object was created."""
    currency: Any
    """Three-letter ISO currency code representing the customer's default currency."""
    default_card: Any
    """The default card to be used for charges when no specific payment method is provided."""
    default_source: Any
    """The default payment source (card or bank account) for the customer."""
    delinquent: Any
    """Boolean indicating whether the customer is currently delinquent on payments."""
    description: Any
    """An arbitrary string attached to the customer, often useful for displaying to users."""
    discount: Any
    """Discount object describing any active discount applied to the customer."""
    email: Any
    """The customer's email address for communication and tracking purposes."""
    id: Any
    """Unique identifier for the customer object."""
    invoice_prefix: Any
    """The prefix for invoice numbers generated for this customer."""
    invoice_settings: Any
    """Customer's invoice-related settings including default payment method and custom fields."""
    is_deleted: Any
    """Boolean indicating whether the customer has been deleted."""
    livemode: Any
    """Boolean indicating whether the object exists in live mode or test mode."""
    metadata: Any
    """Set of key-value pairs for storing additional structured information about the customer."""
    name: Any
    """The customer's full name or business name."""
    next_invoice_sequence: Any
    """The sequence number for the next invoice generated for this customer."""
    object: Any
    """String representing the object type, always 'customer'."""
    phone: Any
    """The customer's phone number."""
    preferred_locales: Any
    """Array of preferred locales for the customer, used for invoice and receipt localization."""
    shipping: Any
    """Mailing and shipping address for the customer, appears on invoices emailed to the customer."""
    sources: Any
    """Payment sources (cards, bank accounts) attached to the customer for making payments."""
    subscriptions: Any
    """List of active subscriptions associated with the customer."""
    tax_exempt: Any
    """Describes the customer's tax exemption status (none, exempt, or reverse)."""
    tax_info: Any
    """Tax identification information for the customer."""
    tax_info_verification: Any
    """Verification status of the customer's tax information."""
    test_clock: Any
    """ID of the test clock associated with this customer for testing time-dependent scenarios."""
    updated: Any
    """Timestamp indicating when the customer object was last updated."""


class CustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_balance: str
    """Current balance value representing funds owed by or to the customer."""
    address: str
    """The customer's address information including line1, line2, city, state, postal code, and country."""
    balance: str
    """Current balance (positive or negative) that is automatically applied to the customer's next invoice."""
    cards: str
    """Card payment methods associated with the customer account."""
    created: str
    """Timestamp indicating when the customer object was created."""
    currency: str
    """Three-letter ISO currency code representing the customer's default currency."""
    default_card: str
    """The default card to be used for charges when no specific payment method is provided."""
    default_source: str
    """The default payment source (card or bank account) for the customer."""
    delinquent: str
    """Boolean indicating whether the customer is currently delinquent on payments."""
    description: str
    """An arbitrary string attached to the customer, often useful for displaying to users."""
    discount: str
    """Discount object describing any active discount applied to the customer."""
    email: str
    """The customer's email address for communication and tracking purposes."""
    id: str
    """Unique identifier for the customer object."""
    invoice_prefix: str
    """The prefix for invoice numbers generated for this customer."""
    invoice_settings: str
    """Customer's invoice-related settings including default payment method and custom fields."""
    is_deleted: str
    """Boolean indicating whether the customer has been deleted."""
    livemode: str
    """Boolean indicating whether the object exists in live mode or test mode."""
    metadata: str
    """Set of key-value pairs for storing additional structured information about the customer."""
    name: str
    """The customer's full name or business name."""
    next_invoice_sequence: str
    """The sequence number for the next invoice generated for this customer."""
    object: str
    """String representing the object type, always 'customer'."""
    phone: str
    """The customer's phone number."""
    preferred_locales: str
    """Array of preferred locales for the customer, used for invoice and receipt localization."""
    shipping: str
    """Mailing and shipping address for the customer, appears on invoices emailed to the customer."""
    sources: str
    """Payment sources (cards, bank accounts) attached to the customer for making payments."""
    subscriptions: str
    """List of active subscriptions associated with the customer."""
    tax_exempt: str
    """Describes the customer's tax exemption status (none, exempt, or reverse)."""
    tax_info: str
    """Tax identification information for the customer."""
    tax_info_verification: str
    """Verification status of the customer's tax information."""
    test_clock: str
    """ID of the test clock associated with this customer for testing time-dependent scenarios."""
    updated: str
    """Timestamp indicating when the customer object was last updated."""


class CustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting customers search results."""
    account_balance: AirbyteSortOrder
    """Current balance value representing funds owed by or to the customer."""
    address: AirbyteSortOrder
    """The customer's address information including line1, line2, city, state, postal code, and country."""
    balance: AirbyteSortOrder
    """Current balance (positive or negative) that is automatically applied to the customer's next invoice."""
    cards: AirbyteSortOrder
    """Card payment methods associated with the customer account."""
    created: AirbyteSortOrder
    """Timestamp indicating when the customer object was created."""
    currency: AirbyteSortOrder
    """Three-letter ISO currency code representing the customer's default currency."""
    default_card: AirbyteSortOrder
    """The default card to be used for charges when no specific payment method is provided."""
    default_source: AirbyteSortOrder
    """The default payment source (card or bank account) for the customer."""
    delinquent: AirbyteSortOrder
    """Boolean indicating whether the customer is currently delinquent on payments."""
    description: AirbyteSortOrder
    """An arbitrary string attached to the customer, often useful for displaying to users."""
    discount: AirbyteSortOrder
    """Discount object describing any active discount applied to the customer."""
    email: AirbyteSortOrder
    """The customer's email address for communication and tracking purposes."""
    id: AirbyteSortOrder
    """Unique identifier for the customer object."""
    invoice_prefix: AirbyteSortOrder
    """The prefix for invoice numbers generated for this customer."""
    invoice_settings: AirbyteSortOrder
    """Customer's invoice-related settings including default payment method and custom fields."""
    is_deleted: AirbyteSortOrder
    """Boolean indicating whether the customer has been deleted."""
    livemode: AirbyteSortOrder
    """Boolean indicating whether the object exists in live mode or test mode."""
    metadata: AirbyteSortOrder
    """Set of key-value pairs for storing additional structured information about the customer."""
    name: AirbyteSortOrder
    """The customer's full name or business name."""
    next_invoice_sequence: AirbyteSortOrder
    """The sequence number for the next invoice generated for this customer."""
    object: AirbyteSortOrder
    """String representing the object type, always 'customer'."""
    phone: AirbyteSortOrder
    """The customer's phone number."""
    preferred_locales: AirbyteSortOrder
    """Array of preferred locales for the customer, used for invoice and receipt localization."""
    shipping: AirbyteSortOrder
    """Mailing and shipping address for the customer, appears on invoices emailed to the customer."""
    sources: AirbyteSortOrder
    """Payment sources (cards, bank accounts) attached to the customer for making payments."""
    subscriptions: AirbyteSortOrder
    """List of active subscriptions associated with the customer."""
    tax_exempt: AirbyteSortOrder
    """Describes the customer's tax exemption status (none, exempt, or reverse)."""
    tax_info: AirbyteSortOrder
    """Tax identification information for the customer."""
    tax_info_verification: AirbyteSortOrder
    """Verification status of the customer's tax information."""
    test_clock: AirbyteSortOrder
    """ID of the test clock associated with this customer for testing time-dependent scenarios."""
    updated: AirbyteSortOrder
    """Timestamp indicating when the customer object was last updated."""


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


# ===== INVOICES SEARCH TYPES =====

class InvoicesSearchFilter(TypedDict, total=False):
    """Available fields for filtering invoices search queries."""
    account_country: str | None
    """The country of the business associated with this invoice, commonly used to display localized content."""
    account_name: str | None
    """The public name of the business associated with this invoice."""
    account_tax_ids: list[Any] | None
    """Tax IDs of the account associated with this invoice."""
    amount_due: int | None
    """Total amount, in smallest currency unit, that is due and owed by the customer."""
    amount_paid: int | None
    """Total amount, in smallest currency unit, that has been paid by the customer."""
    amount_remaining: int | None
    """The difference between amount_due and amount_paid, representing the outstanding balance."""
    amount_shipping: int | None
    """Total amount of shipping costs on the invoice."""
    application: str | None
    """ID of the Connect application that created this invoice."""
    application_fee: int | None
    """Amount of application fee charged for this invoice in a Connect scenario."""
    application_fee_amount: int | None
    """The fee in smallest currency unit that is collected by the application in a Connect scenario."""
    attempt_count: int | None
    """Number of payment attempts made for this invoice."""
    attempted: bool | None
    """Whether an attempt has been made to pay the invoice."""
    auto_advance: bool | None
    """Controls whether Stripe performs automatic collection of the invoice."""
    automatic_tax: dict[str, Any] | None
    """Settings and status for automatic tax calculation on this invoice."""
    billing: str | None
    """Billing method used for the invoice (charge_automatically or send_invoice)."""
    billing_reason: str | None
    """Indicates the reason why the invoice was created (subscription_cycle, manual, etc.)."""
    charge: str | None
    """ID of the latest charge generated for this invoice, if any."""
    closed: bool | None
    """Whether the invoice has been marked as closed and no longer open for collection."""
    collection_method: str | None
    """Method by which the invoice is collected: charge_automatically or send_invoice."""
    created: int | None
    """Timestamp indicating when the invoice was created."""
    currency: str | None
    """Three-letter ISO currency code in which the invoice is denominated."""
    custom_fields: list[Any] | None
    """Custom fields displayed on the invoice as specified by the account."""
    customer: str | None
    """The customer object or ID associated with this invoice."""
    customer_address: dict[str, Any] | None
    """The customer's address at the time the invoice was finalized."""
    customer_email: str | None
    """The customer's email address at the time the invoice was finalized."""
    customer_name: str | None
    """The customer's name at the time the invoice was finalized."""
    customer_phone: str | None
    """The customer's phone number at the time the invoice was finalized."""
    customer_shipping: dict[str, Any] | None
    """The customer's shipping information at the time the invoice was finalized."""
    customer_tax_exempt: str | None
    """The customer's tax exempt status at the time the invoice was finalized."""
    customer_tax_ids: list[Any] | None
    """The customer's tax IDs at the time the invoice was finalized."""
    default_payment_method: str | None
    """Default payment method for the invoice, used if no other method is specified."""
    default_source: str | None
    """Default payment source for the invoice if no payment method is set."""
    default_tax_rates: list[Any] | None
    """The tax rates applied to the invoice by default."""
    description: str | None
    """An arbitrary string attached to the invoice, often displayed to customers."""
    discount: dict[str, Any] | None
    """The discount object applied to the invoice, if any."""
    discounts: list[Any] | None
    """Array of discount IDs or objects currently applied to this invoice."""
    due_date: float | None
    """The date by which payment on this invoice is due, if the invoice is not auto-collected."""
    effective_at: int | None
    """Timestamp when the invoice becomes effective and finalized for payment."""
    ending_balance: int | None
    """The customer's ending account balance after this invoice is finalized."""
    footer: str | None
    """Footer text displayed on the invoice."""
    forgiven: bool | None
    """Whether the invoice has been forgiven and is considered paid without actual payment."""
    from_invoice: dict[str, Any] | None
    """Details about the invoice this invoice was created from, if applicable."""
    hosted_invoice_url: str | None
    """URL for the hosted invoice page where customers can view and pay the invoice."""
    id: str | None
    """Unique identifier for the invoice object."""
    invoice_pdf: str | None
    """URL for the PDF version of the invoice."""
    is_deleted: bool | None
    """Indicates whether this invoice has been deleted."""
    issuer: dict[str, Any] | None
    """Details about the entity issuing the invoice."""
    last_finalization_error: dict[str, Any] | None
    """The error encountered during the last finalization attempt, if any."""
    latest_revision: str | None
    """The latest revision of the invoice, if revisions are enabled."""
    lines: dict[str, Any] | None
    """The individual line items that make up the invoice, representing products, services, or fees."""
    livemode: bool | None
    """Indicates whether the invoice exists in live mode (true) or test mode (false)."""
    metadata: dict[str, Any] | None
    """Key-value pairs for storing additional structured information about the invoice."""
    next_payment_attempt: float | None
    """Timestamp of the next automatic payment attempt for this invoice, if applicable."""
    number: str | None
    """A unique, human-readable identifier for this invoice, often shown to customers."""
    object: str | None
    """String representing the object type, always 'invoice'."""
    on_behalf_of: str | None
    """The account on behalf of which the invoice is being created, used in Connect scenarios."""
    paid: bool | None
    """Whether the invoice has been paid in full."""
    paid_out_of_band: bool | None
    """Whether payment was made outside of Stripe and manually marked as paid."""
    payment: str | None
    """ID of the payment associated with this invoice, if any."""
    payment_intent: str | None
    """The PaymentIntent associated with this invoice for processing payment."""
    payment_settings: dict[str, Any] | None
    """Configuration settings for how payment should be collected on this invoice."""
    period_end: float | None
    """End date of the billing period covered by this invoice."""
    period_start: float | None
    """Start date of the billing period covered by this invoice."""
    post_payment_credit_notes_amount: int | None
    """Total amount of credit notes issued after the invoice was paid."""
    pre_payment_credit_notes_amount: int | None
    """Total amount of credit notes applied before payment was attempted."""
    quote: str | None
    """The quote from which this invoice was generated, if applicable."""
    receipt_number: str | None
    """The receipt number displayed on the invoice, if available."""
    rendering: dict[str, Any] | None
    """Settings that control how the invoice is rendered for display."""
    rendering_options: dict[str, Any] | None
    """Options for customizing the visual rendering of the invoice."""
    shipping_cost: dict[str, Any] | None
    """Total cost of shipping charges included in the invoice."""
    shipping_details: dict[str, Any] | None
    """Detailed shipping information for the invoice, including address and carrier."""
    starting_balance: int | None
    """The customer's starting account balance at the beginning of the billing period."""
    statement_description: str | None
    """Extra information about the invoice that appears on the customer's credit card statement."""
    statement_descriptor: str | None
    """A dynamic descriptor that appears on the customer's credit card statement for this invoice."""
    status: str | None
    """The status of the invoice: draft, open, paid, void, or uncollectible."""
    status_transitions: dict[str, Any]
    """Timestamps tracking when the invoice transitioned between different statuses."""
    subscription: str | None
    """The subscription this invoice was generated for, if applicable."""
    subscription_details: dict[str, Any] | None
    """Additional details about the subscription associated with this invoice."""
    subtotal: int | None
    """Total of all line items before discounts or tax are applied."""
    subtotal_excluding_tax: int | None
    """The subtotal amount excluding any tax calculations."""
    tax: int | None
    """Total tax amount applied to the invoice."""
    tax_percent: float | None
    """The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead)."""
    test_clock: str | None
    """ID of the test clock this invoice belongs to, used for testing time-dependent billing."""
    total: int | None
    """Total amount of the invoice after all line items, discounts, and taxes are calculated."""
    total_discount_amounts: list[Any] | None
    """Array of the total discount amounts applied, broken down by discount."""
    total_excluding_tax: int | None
    """Total amount of the invoice excluding all tax calculations."""
    total_tax_amounts: list[Any] | None
    """Array of tax amounts applied to the invoice, broken down by tax rate."""
    transfer_data: dict[str, Any] | None
    """Information about the transfer of funds associated with this invoice in Connect scenarios."""
    updated: int | None
    """Timestamp indicating when the invoice was last updated."""
    webhooks_delivered_at: float | None
    """Timestamp indicating when webhooks for this invoice were successfully delivered."""


class InvoicesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_country: list[str]
    """The country of the business associated with this invoice, commonly used to display localized content."""
    account_name: list[str]
    """The public name of the business associated with this invoice."""
    account_tax_ids: list[list[Any]]
    """Tax IDs of the account associated with this invoice."""
    amount_due: list[int]
    """Total amount, in smallest currency unit, that is due and owed by the customer."""
    amount_paid: list[int]
    """Total amount, in smallest currency unit, that has been paid by the customer."""
    amount_remaining: list[int]
    """The difference between amount_due and amount_paid, representing the outstanding balance."""
    amount_shipping: list[int]
    """Total amount of shipping costs on the invoice."""
    application: list[str]
    """ID of the Connect application that created this invoice."""
    application_fee: list[int]
    """Amount of application fee charged for this invoice in a Connect scenario."""
    application_fee_amount: list[int]
    """The fee in smallest currency unit that is collected by the application in a Connect scenario."""
    attempt_count: list[int]
    """Number of payment attempts made for this invoice."""
    attempted: list[bool]
    """Whether an attempt has been made to pay the invoice."""
    auto_advance: list[bool]
    """Controls whether Stripe performs automatic collection of the invoice."""
    automatic_tax: list[dict[str, Any]]
    """Settings and status for automatic tax calculation on this invoice."""
    billing: list[str]
    """Billing method used for the invoice (charge_automatically or send_invoice)."""
    billing_reason: list[str]
    """Indicates the reason why the invoice was created (subscription_cycle, manual, etc.)."""
    charge: list[str]
    """ID of the latest charge generated for this invoice, if any."""
    closed: list[bool]
    """Whether the invoice has been marked as closed and no longer open for collection."""
    collection_method: list[str]
    """Method by which the invoice is collected: charge_automatically or send_invoice."""
    created: list[int]
    """Timestamp indicating when the invoice was created."""
    currency: list[str]
    """Three-letter ISO currency code in which the invoice is denominated."""
    custom_fields: list[list[Any]]
    """Custom fields displayed on the invoice as specified by the account."""
    customer: list[str]
    """The customer object or ID associated with this invoice."""
    customer_address: list[dict[str, Any]]
    """The customer's address at the time the invoice was finalized."""
    customer_email: list[str]
    """The customer's email address at the time the invoice was finalized."""
    customer_name: list[str]
    """The customer's name at the time the invoice was finalized."""
    customer_phone: list[str]
    """The customer's phone number at the time the invoice was finalized."""
    customer_shipping: list[dict[str, Any]]
    """The customer's shipping information at the time the invoice was finalized."""
    customer_tax_exempt: list[str]
    """The customer's tax exempt status at the time the invoice was finalized."""
    customer_tax_ids: list[list[Any]]
    """The customer's tax IDs at the time the invoice was finalized."""
    default_payment_method: list[str]
    """Default payment method for the invoice, used if no other method is specified."""
    default_source: list[str]
    """Default payment source for the invoice if no payment method is set."""
    default_tax_rates: list[list[Any]]
    """The tax rates applied to the invoice by default."""
    description: list[str]
    """An arbitrary string attached to the invoice, often displayed to customers."""
    discount: list[dict[str, Any]]
    """The discount object applied to the invoice, if any."""
    discounts: list[list[Any]]
    """Array of discount IDs or objects currently applied to this invoice."""
    due_date: list[float]
    """The date by which payment on this invoice is due, if the invoice is not auto-collected."""
    effective_at: list[int]
    """Timestamp when the invoice becomes effective and finalized for payment."""
    ending_balance: list[int]
    """The customer's ending account balance after this invoice is finalized."""
    footer: list[str]
    """Footer text displayed on the invoice."""
    forgiven: list[bool]
    """Whether the invoice has been forgiven and is considered paid without actual payment."""
    from_invoice: list[dict[str, Any]]
    """Details about the invoice this invoice was created from, if applicable."""
    hosted_invoice_url: list[str]
    """URL for the hosted invoice page where customers can view and pay the invoice."""
    id: list[str]
    """Unique identifier for the invoice object."""
    invoice_pdf: list[str]
    """URL for the PDF version of the invoice."""
    is_deleted: list[bool]
    """Indicates whether this invoice has been deleted."""
    issuer: list[dict[str, Any]]
    """Details about the entity issuing the invoice."""
    last_finalization_error: list[dict[str, Any]]
    """The error encountered during the last finalization attempt, if any."""
    latest_revision: list[str]
    """The latest revision of the invoice, if revisions are enabled."""
    lines: list[dict[str, Any]]
    """The individual line items that make up the invoice, representing products, services, or fees."""
    livemode: list[bool]
    """Indicates whether the invoice exists in live mode (true) or test mode (false)."""
    metadata: list[dict[str, Any]]
    """Key-value pairs for storing additional structured information about the invoice."""
    next_payment_attempt: list[float]
    """Timestamp of the next automatic payment attempt for this invoice, if applicable."""
    number: list[str]
    """A unique, human-readable identifier for this invoice, often shown to customers."""
    object: list[str]
    """String representing the object type, always 'invoice'."""
    on_behalf_of: list[str]
    """The account on behalf of which the invoice is being created, used in Connect scenarios."""
    paid: list[bool]
    """Whether the invoice has been paid in full."""
    paid_out_of_band: list[bool]
    """Whether payment was made outside of Stripe and manually marked as paid."""
    payment: list[str]
    """ID of the payment associated with this invoice, if any."""
    payment_intent: list[str]
    """The PaymentIntent associated with this invoice for processing payment."""
    payment_settings: list[dict[str, Any]]
    """Configuration settings for how payment should be collected on this invoice."""
    period_end: list[float]
    """End date of the billing period covered by this invoice."""
    period_start: list[float]
    """Start date of the billing period covered by this invoice."""
    post_payment_credit_notes_amount: list[int]
    """Total amount of credit notes issued after the invoice was paid."""
    pre_payment_credit_notes_amount: list[int]
    """Total amount of credit notes applied before payment was attempted."""
    quote: list[str]
    """The quote from which this invoice was generated, if applicable."""
    receipt_number: list[str]
    """The receipt number displayed on the invoice, if available."""
    rendering: list[dict[str, Any]]
    """Settings that control how the invoice is rendered for display."""
    rendering_options: list[dict[str, Any]]
    """Options for customizing the visual rendering of the invoice."""
    shipping_cost: list[dict[str, Any]]
    """Total cost of shipping charges included in the invoice."""
    shipping_details: list[dict[str, Any]]
    """Detailed shipping information for the invoice, including address and carrier."""
    starting_balance: list[int]
    """The customer's starting account balance at the beginning of the billing period."""
    statement_description: list[str]
    """Extra information about the invoice that appears on the customer's credit card statement."""
    statement_descriptor: list[str]
    """A dynamic descriptor that appears on the customer's credit card statement for this invoice."""
    status: list[str]
    """The status of the invoice: draft, open, paid, void, or uncollectible."""
    status_transitions: list[dict[str, Any]]
    """Timestamps tracking when the invoice transitioned between different statuses."""
    subscription: list[str]
    """The subscription this invoice was generated for, if applicable."""
    subscription_details: list[dict[str, Any]]
    """Additional details about the subscription associated with this invoice."""
    subtotal: list[int]
    """Total of all line items before discounts or tax are applied."""
    subtotal_excluding_tax: list[int]
    """The subtotal amount excluding any tax calculations."""
    tax: list[int]
    """Total tax amount applied to the invoice."""
    tax_percent: list[float]
    """The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead)."""
    test_clock: list[str]
    """ID of the test clock this invoice belongs to, used for testing time-dependent billing."""
    total: list[int]
    """Total amount of the invoice after all line items, discounts, and taxes are calculated."""
    total_discount_amounts: list[list[Any]]
    """Array of the total discount amounts applied, broken down by discount."""
    total_excluding_tax: list[int]
    """Total amount of the invoice excluding all tax calculations."""
    total_tax_amounts: list[list[Any]]
    """Array of tax amounts applied to the invoice, broken down by tax rate."""
    transfer_data: list[dict[str, Any]]
    """Information about the transfer of funds associated with this invoice in Connect scenarios."""
    updated: list[int]
    """Timestamp indicating when the invoice was last updated."""
    webhooks_delivered_at: list[float]
    """Timestamp indicating when webhooks for this invoice were successfully delivered."""


class InvoicesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_country: Any
    """The country of the business associated with this invoice, commonly used to display localized content."""
    account_name: Any
    """The public name of the business associated with this invoice."""
    account_tax_ids: Any
    """Tax IDs of the account associated with this invoice."""
    amount_due: Any
    """Total amount, in smallest currency unit, that is due and owed by the customer."""
    amount_paid: Any
    """Total amount, in smallest currency unit, that has been paid by the customer."""
    amount_remaining: Any
    """The difference between amount_due and amount_paid, representing the outstanding balance."""
    amount_shipping: Any
    """Total amount of shipping costs on the invoice."""
    application: Any
    """ID of the Connect application that created this invoice."""
    application_fee: Any
    """Amount of application fee charged for this invoice in a Connect scenario."""
    application_fee_amount: Any
    """The fee in smallest currency unit that is collected by the application in a Connect scenario."""
    attempt_count: Any
    """Number of payment attempts made for this invoice."""
    attempted: Any
    """Whether an attempt has been made to pay the invoice."""
    auto_advance: Any
    """Controls whether Stripe performs automatic collection of the invoice."""
    automatic_tax: Any
    """Settings and status for automatic tax calculation on this invoice."""
    billing: Any
    """Billing method used for the invoice (charge_automatically or send_invoice)."""
    billing_reason: Any
    """Indicates the reason why the invoice was created (subscription_cycle, manual, etc.)."""
    charge: Any
    """ID of the latest charge generated for this invoice, if any."""
    closed: Any
    """Whether the invoice has been marked as closed and no longer open for collection."""
    collection_method: Any
    """Method by which the invoice is collected: charge_automatically or send_invoice."""
    created: Any
    """Timestamp indicating when the invoice was created."""
    currency: Any
    """Three-letter ISO currency code in which the invoice is denominated."""
    custom_fields: Any
    """Custom fields displayed on the invoice as specified by the account."""
    customer: Any
    """The customer object or ID associated with this invoice."""
    customer_address: Any
    """The customer's address at the time the invoice was finalized."""
    customer_email: Any
    """The customer's email address at the time the invoice was finalized."""
    customer_name: Any
    """The customer's name at the time the invoice was finalized."""
    customer_phone: Any
    """The customer's phone number at the time the invoice was finalized."""
    customer_shipping: Any
    """The customer's shipping information at the time the invoice was finalized."""
    customer_tax_exempt: Any
    """The customer's tax exempt status at the time the invoice was finalized."""
    customer_tax_ids: Any
    """The customer's tax IDs at the time the invoice was finalized."""
    default_payment_method: Any
    """Default payment method for the invoice, used if no other method is specified."""
    default_source: Any
    """Default payment source for the invoice if no payment method is set."""
    default_tax_rates: Any
    """The tax rates applied to the invoice by default."""
    description: Any
    """An arbitrary string attached to the invoice, often displayed to customers."""
    discount: Any
    """The discount object applied to the invoice, if any."""
    discounts: Any
    """Array of discount IDs or objects currently applied to this invoice."""
    due_date: Any
    """The date by which payment on this invoice is due, if the invoice is not auto-collected."""
    effective_at: Any
    """Timestamp when the invoice becomes effective and finalized for payment."""
    ending_balance: Any
    """The customer's ending account balance after this invoice is finalized."""
    footer: Any
    """Footer text displayed on the invoice."""
    forgiven: Any
    """Whether the invoice has been forgiven and is considered paid without actual payment."""
    from_invoice: Any
    """Details about the invoice this invoice was created from, if applicable."""
    hosted_invoice_url: Any
    """URL for the hosted invoice page where customers can view and pay the invoice."""
    id: Any
    """Unique identifier for the invoice object."""
    invoice_pdf: Any
    """URL for the PDF version of the invoice."""
    is_deleted: Any
    """Indicates whether this invoice has been deleted."""
    issuer: Any
    """Details about the entity issuing the invoice."""
    last_finalization_error: Any
    """The error encountered during the last finalization attempt, if any."""
    latest_revision: Any
    """The latest revision of the invoice, if revisions are enabled."""
    lines: Any
    """The individual line items that make up the invoice, representing products, services, or fees."""
    livemode: Any
    """Indicates whether the invoice exists in live mode (true) or test mode (false)."""
    metadata: Any
    """Key-value pairs for storing additional structured information about the invoice."""
    next_payment_attempt: Any
    """Timestamp of the next automatic payment attempt for this invoice, if applicable."""
    number: Any
    """A unique, human-readable identifier for this invoice, often shown to customers."""
    object: Any
    """String representing the object type, always 'invoice'."""
    on_behalf_of: Any
    """The account on behalf of which the invoice is being created, used in Connect scenarios."""
    paid: Any
    """Whether the invoice has been paid in full."""
    paid_out_of_band: Any
    """Whether payment was made outside of Stripe and manually marked as paid."""
    payment: Any
    """ID of the payment associated with this invoice, if any."""
    payment_intent: Any
    """The PaymentIntent associated with this invoice for processing payment."""
    payment_settings: Any
    """Configuration settings for how payment should be collected on this invoice."""
    period_end: Any
    """End date of the billing period covered by this invoice."""
    period_start: Any
    """Start date of the billing period covered by this invoice."""
    post_payment_credit_notes_amount: Any
    """Total amount of credit notes issued after the invoice was paid."""
    pre_payment_credit_notes_amount: Any
    """Total amount of credit notes applied before payment was attempted."""
    quote: Any
    """The quote from which this invoice was generated, if applicable."""
    receipt_number: Any
    """The receipt number displayed on the invoice, if available."""
    rendering: Any
    """Settings that control how the invoice is rendered for display."""
    rendering_options: Any
    """Options for customizing the visual rendering of the invoice."""
    shipping_cost: Any
    """Total cost of shipping charges included in the invoice."""
    shipping_details: Any
    """Detailed shipping information for the invoice, including address and carrier."""
    starting_balance: Any
    """The customer's starting account balance at the beginning of the billing period."""
    statement_description: Any
    """Extra information about the invoice that appears on the customer's credit card statement."""
    statement_descriptor: Any
    """A dynamic descriptor that appears on the customer's credit card statement for this invoice."""
    status: Any
    """The status of the invoice: draft, open, paid, void, or uncollectible."""
    status_transitions: Any
    """Timestamps tracking when the invoice transitioned between different statuses."""
    subscription: Any
    """The subscription this invoice was generated for, if applicable."""
    subscription_details: Any
    """Additional details about the subscription associated with this invoice."""
    subtotal: Any
    """Total of all line items before discounts or tax are applied."""
    subtotal_excluding_tax: Any
    """The subtotal amount excluding any tax calculations."""
    tax: Any
    """Total tax amount applied to the invoice."""
    tax_percent: Any
    """The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead)."""
    test_clock: Any
    """ID of the test clock this invoice belongs to, used for testing time-dependent billing."""
    total: Any
    """Total amount of the invoice after all line items, discounts, and taxes are calculated."""
    total_discount_amounts: Any
    """Array of the total discount amounts applied, broken down by discount."""
    total_excluding_tax: Any
    """Total amount of the invoice excluding all tax calculations."""
    total_tax_amounts: Any
    """Array of tax amounts applied to the invoice, broken down by tax rate."""
    transfer_data: Any
    """Information about the transfer of funds associated with this invoice in Connect scenarios."""
    updated: Any
    """Timestamp indicating when the invoice was last updated."""
    webhooks_delivered_at: Any
    """Timestamp indicating when webhooks for this invoice were successfully delivered."""


class InvoicesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_country: str
    """The country of the business associated with this invoice, commonly used to display localized content."""
    account_name: str
    """The public name of the business associated with this invoice."""
    account_tax_ids: str
    """Tax IDs of the account associated with this invoice."""
    amount_due: str
    """Total amount, in smallest currency unit, that is due and owed by the customer."""
    amount_paid: str
    """Total amount, in smallest currency unit, that has been paid by the customer."""
    amount_remaining: str
    """The difference between amount_due and amount_paid, representing the outstanding balance."""
    amount_shipping: str
    """Total amount of shipping costs on the invoice."""
    application: str
    """ID of the Connect application that created this invoice."""
    application_fee: str
    """Amount of application fee charged for this invoice in a Connect scenario."""
    application_fee_amount: str
    """The fee in smallest currency unit that is collected by the application in a Connect scenario."""
    attempt_count: str
    """Number of payment attempts made for this invoice."""
    attempted: str
    """Whether an attempt has been made to pay the invoice."""
    auto_advance: str
    """Controls whether Stripe performs automatic collection of the invoice."""
    automatic_tax: str
    """Settings and status for automatic tax calculation on this invoice."""
    billing: str
    """Billing method used for the invoice (charge_automatically or send_invoice)."""
    billing_reason: str
    """Indicates the reason why the invoice was created (subscription_cycle, manual, etc.)."""
    charge: str
    """ID of the latest charge generated for this invoice, if any."""
    closed: str
    """Whether the invoice has been marked as closed and no longer open for collection."""
    collection_method: str
    """Method by which the invoice is collected: charge_automatically or send_invoice."""
    created: str
    """Timestamp indicating when the invoice was created."""
    currency: str
    """Three-letter ISO currency code in which the invoice is denominated."""
    custom_fields: str
    """Custom fields displayed on the invoice as specified by the account."""
    customer: str
    """The customer object or ID associated with this invoice."""
    customer_address: str
    """The customer's address at the time the invoice was finalized."""
    customer_email: str
    """The customer's email address at the time the invoice was finalized."""
    customer_name: str
    """The customer's name at the time the invoice was finalized."""
    customer_phone: str
    """The customer's phone number at the time the invoice was finalized."""
    customer_shipping: str
    """The customer's shipping information at the time the invoice was finalized."""
    customer_tax_exempt: str
    """The customer's tax exempt status at the time the invoice was finalized."""
    customer_tax_ids: str
    """The customer's tax IDs at the time the invoice was finalized."""
    default_payment_method: str
    """Default payment method for the invoice, used if no other method is specified."""
    default_source: str
    """Default payment source for the invoice if no payment method is set."""
    default_tax_rates: str
    """The tax rates applied to the invoice by default."""
    description: str
    """An arbitrary string attached to the invoice, often displayed to customers."""
    discount: str
    """The discount object applied to the invoice, if any."""
    discounts: str
    """Array of discount IDs or objects currently applied to this invoice."""
    due_date: str
    """The date by which payment on this invoice is due, if the invoice is not auto-collected."""
    effective_at: str
    """Timestamp when the invoice becomes effective and finalized for payment."""
    ending_balance: str
    """The customer's ending account balance after this invoice is finalized."""
    footer: str
    """Footer text displayed on the invoice."""
    forgiven: str
    """Whether the invoice has been forgiven and is considered paid without actual payment."""
    from_invoice: str
    """Details about the invoice this invoice was created from, if applicable."""
    hosted_invoice_url: str
    """URL for the hosted invoice page where customers can view and pay the invoice."""
    id: str
    """Unique identifier for the invoice object."""
    invoice_pdf: str
    """URL for the PDF version of the invoice."""
    is_deleted: str
    """Indicates whether this invoice has been deleted."""
    issuer: str
    """Details about the entity issuing the invoice."""
    last_finalization_error: str
    """The error encountered during the last finalization attempt, if any."""
    latest_revision: str
    """The latest revision of the invoice, if revisions are enabled."""
    lines: str
    """The individual line items that make up the invoice, representing products, services, or fees."""
    livemode: str
    """Indicates whether the invoice exists in live mode (true) or test mode (false)."""
    metadata: str
    """Key-value pairs for storing additional structured information about the invoice."""
    next_payment_attempt: str
    """Timestamp of the next automatic payment attempt for this invoice, if applicable."""
    number: str
    """A unique, human-readable identifier for this invoice, often shown to customers."""
    object: str
    """String representing the object type, always 'invoice'."""
    on_behalf_of: str
    """The account on behalf of which the invoice is being created, used in Connect scenarios."""
    paid: str
    """Whether the invoice has been paid in full."""
    paid_out_of_band: str
    """Whether payment was made outside of Stripe and manually marked as paid."""
    payment: str
    """ID of the payment associated with this invoice, if any."""
    payment_intent: str
    """The PaymentIntent associated with this invoice for processing payment."""
    payment_settings: str
    """Configuration settings for how payment should be collected on this invoice."""
    period_end: str
    """End date of the billing period covered by this invoice."""
    period_start: str
    """Start date of the billing period covered by this invoice."""
    post_payment_credit_notes_amount: str
    """Total amount of credit notes issued after the invoice was paid."""
    pre_payment_credit_notes_amount: str
    """Total amount of credit notes applied before payment was attempted."""
    quote: str
    """The quote from which this invoice was generated, if applicable."""
    receipt_number: str
    """The receipt number displayed on the invoice, if available."""
    rendering: str
    """Settings that control how the invoice is rendered for display."""
    rendering_options: str
    """Options for customizing the visual rendering of the invoice."""
    shipping_cost: str
    """Total cost of shipping charges included in the invoice."""
    shipping_details: str
    """Detailed shipping information for the invoice, including address and carrier."""
    starting_balance: str
    """The customer's starting account balance at the beginning of the billing period."""
    statement_description: str
    """Extra information about the invoice that appears on the customer's credit card statement."""
    statement_descriptor: str
    """A dynamic descriptor that appears on the customer's credit card statement for this invoice."""
    status: str
    """The status of the invoice: draft, open, paid, void, or uncollectible."""
    status_transitions: str
    """Timestamps tracking when the invoice transitioned between different statuses."""
    subscription: str
    """The subscription this invoice was generated for, if applicable."""
    subscription_details: str
    """Additional details about the subscription associated with this invoice."""
    subtotal: str
    """Total of all line items before discounts or tax are applied."""
    subtotal_excluding_tax: str
    """The subtotal amount excluding any tax calculations."""
    tax: str
    """Total tax amount applied to the invoice."""
    tax_percent: str
    """The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead)."""
    test_clock: str
    """ID of the test clock this invoice belongs to, used for testing time-dependent billing."""
    total: str
    """Total amount of the invoice after all line items, discounts, and taxes are calculated."""
    total_discount_amounts: str
    """Array of the total discount amounts applied, broken down by discount."""
    total_excluding_tax: str
    """Total amount of the invoice excluding all tax calculations."""
    total_tax_amounts: str
    """Array of tax amounts applied to the invoice, broken down by tax rate."""
    transfer_data: str
    """Information about the transfer of funds associated with this invoice in Connect scenarios."""
    updated: str
    """Timestamp indicating when the invoice was last updated."""
    webhooks_delivered_at: str
    """Timestamp indicating when webhooks for this invoice were successfully delivered."""


class InvoicesSortFilter(TypedDict, total=False):
    """Available fields for sorting invoices search results."""
    account_country: AirbyteSortOrder
    """The country of the business associated with this invoice, commonly used to display localized content."""
    account_name: AirbyteSortOrder
    """The public name of the business associated with this invoice."""
    account_tax_ids: AirbyteSortOrder
    """Tax IDs of the account associated with this invoice."""
    amount_due: AirbyteSortOrder
    """Total amount, in smallest currency unit, that is due and owed by the customer."""
    amount_paid: AirbyteSortOrder
    """Total amount, in smallest currency unit, that has been paid by the customer."""
    amount_remaining: AirbyteSortOrder
    """The difference between amount_due and amount_paid, representing the outstanding balance."""
    amount_shipping: AirbyteSortOrder
    """Total amount of shipping costs on the invoice."""
    application: AirbyteSortOrder
    """ID of the Connect application that created this invoice."""
    application_fee: AirbyteSortOrder
    """Amount of application fee charged for this invoice in a Connect scenario."""
    application_fee_amount: AirbyteSortOrder
    """The fee in smallest currency unit that is collected by the application in a Connect scenario."""
    attempt_count: AirbyteSortOrder
    """Number of payment attempts made for this invoice."""
    attempted: AirbyteSortOrder
    """Whether an attempt has been made to pay the invoice."""
    auto_advance: AirbyteSortOrder
    """Controls whether Stripe performs automatic collection of the invoice."""
    automatic_tax: AirbyteSortOrder
    """Settings and status for automatic tax calculation on this invoice."""
    billing: AirbyteSortOrder
    """Billing method used for the invoice (charge_automatically or send_invoice)."""
    billing_reason: AirbyteSortOrder
    """Indicates the reason why the invoice was created (subscription_cycle, manual, etc.)."""
    charge: AirbyteSortOrder
    """ID of the latest charge generated for this invoice, if any."""
    closed: AirbyteSortOrder
    """Whether the invoice has been marked as closed and no longer open for collection."""
    collection_method: AirbyteSortOrder
    """Method by which the invoice is collected: charge_automatically or send_invoice."""
    created: AirbyteSortOrder
    """Timestamp indicating when the invoice was created."""
    currency: AirbyteSortOrder
    """Three-letter ISO currency code in which the invoice is denominated."""
    custom_fields: AirbyteSortOrder
    """Custom fields displayed on the invoice as specified by the account."""
    customer: AirbyteSortOrder
    """The customer object or ID associated with this invoice."""
    customer_address: AirbyteSortOrder
    """The customer's address at the time the invoice was finalized."""
    customer_email: AirbyteSortOrder
    """The customer's email address at the time the invoice was finalized."""
    customer_name: AirbyteSortOrder
    """The customer's name at the time the invoice was finalized."""
    customer_phone: AirbyteSortOrder
    """The customer's phone number at the time the invoice was finalized."""
    customer_shipping: AirbyteSortOrder
    """The customer's shipping information at the time the invoice was finalized."""
    customer_tax_exempt: AirbyteSortOrder
    """The customer's tax exempt status at the time the invoice was finalized."""
    customer_tax_ids: AirbyteSortOrder
    """The customer's tax IDs at the time the invoice was finalized."""
    default_payment_method: AirbyteSortOrder
    """Default payment method for the invoice, used if no other method is specified."""
    default_source: AirbyteSortOrder
    """Default payment source for the invoice if no payment method is set."""
    default_tax_rates: AirbyteSortOrder
    """The tax rates applied to the invoice by default."""
    description: AirbyteSortOrder
    """An arbitrary string attached to the invoice, often displayed to customers."""
    discount: AirbyteSortOrder
    """The discount object applied to the invoice, if any."""
    discounts: AirbyteSortOrder
    """Array of discount IDs or objects currently applied to this invoice."""
    due_date: AirbyteSortOrder
    """The date by which payment on this invoice is due, if the invoice is not auto-collected."""
    effective_at: AirbyteSortOrder
    """Timestamp when the invoice becomes effective and finalized for payment."""
    ending_balance: AirbyteSortOrder
    """The customer's ending account balance after this invoice is finalized."""
    footer: AirbyteSortOrder
    """Footer text displayed on the invoice."""
    forgiven: AirbyteSortOrder
    """Whether the invoice has been forgiven and is considered paid without actual payment."""
    from_invoice: AirbyteSortOrder
    """Details about the invoice this invoice was created from, if applicable."""
    hosted_invoice_url: AirbyteSortOrder
    """URL for the hosted invoice page where customers can view and pay the invoice."""
    id: AirbyteSortOrder
    """Unique identifier for the invoice object."""
    invoice_pdf: AirbyteSortOrder
    """URL for the PDF version of the invoice."""
    is_deleted: AirbyteSortOrder
    """Indicates whether this invoice has been deleted."""
    issuer: AirbyteSortOrder
    """Details about the entity issuing the invoice."""
    last_finalization_error: AirbyteSortOrder
    """The error encountered during the last finalization attempt, if any."""
    latest_revision: AirbyteSortOrder
    """The latest revision of the invoice, if revisions are enabled."""
    lines: AirbyteSortOrder
    """The individual line items that make up the invoice, representing products, services, or fees."""
    livemode: AirbyteSortOrder
    """Indicates whether the invoice exists in live mode (true) or test mode (false)."""
    metadata: AirbyteSortOrder
    """Key-value pairs for storing additional structured information about the invoice."""
    next_payment_attempt: AirbyteSortOrder
    """Timestamp of the next automatic payment attempt for this invoice, if applicable."""
    number: AirbyteSortOrder
    """A unique, human-readable identifier for this invoice, often shown to customers."""
    object: AirbyteSortOrder
    """String representing the object type, always 'invoice'."""
    on_behalf_of: AirbyteSortOrder
    """The account on behalf of which the invoice is being created, used in Connect scenarios."""
    paid: AirbyteSortOrder
    """Whether the invoice has been paid in full."""
    paid_out_of_band: AirbyteSortOrder
    """Whether payment was made outside of Stripe and manually marked as paid."""
    payment: AirbyteSortOrder
    """ID of the payment associated with this invoice, if any."""
    payment_intent: AirbyteSortOrder
    """The PaymentIntent associated with this invoice for processing payment."""
    payment_settings: AirbyteSortOrder
    """Configuration settings for how payment should be collected on this invoice."""
    period_end: AirbyteSortOrder
    """End date of the billing period covered by this invoice."""
    period_start: AirbyteSortOrder
    """Start date of the billing period covered by this invoice."""
    post_payment_credit_notes_amount: AirbyteSortOrder
    """Total amount of credit notes issued after the invoice was paid."""
    pre_payment_credit_notes_amount: AirbyteSortOrder
    """Total amount of credit notes applied before payment was attempted."""
    quote: AirbyteSortOrder
    """The quote from which this invoice was generated, if applicable."""
    receipt_number: AirbyteSortOrder
    """The receipt number displayed on the invoice, if available."""
    rendering: AirbyteSortOrder
    """Settings that control how the invoice is rendered for display."""
    rendering_options: AirbyteSortOrder
    """Options for customizing the visual rendering of the invoice."""
    shipping_cost: AirbyteSortOrder
    """Total cost of shipping charges included in the invoice."""
    shipping_details: AirbyteSortOrder
    """Detailed shipping information for the invoice, including address and carrier."""
    starting_balance: AirbyteSortOrder
    """The customer's starting account balance at the beginning of the billing period."""
    statement_description: AirbyteSortOrder
    """Extra information about the invoice that appears on the customer's credit card statement."""
    statement_descriptor: AirbyteSortOrder
    """A dynamic descriptor that appears on the customer's credit card statement for this invoice."""
    status: AirbyteSortOrder
    """The status of the invoice: draft, open, paid, void, or uncollectible."""
    status_transitions: AirbyteSortOrder
    """Timestamps tracking when the invoice transitioned between different statuses."""
    subscription: AirbyteSortOrder
    """The subscription this invoice was generated for, if applicable."""
    subscription_details: AirbyteSortOrder
    """Additional details about the subscription associated with this invoice."""
    subtotal: AirbyteSortOrder
    """Total of all line items before discounts or tax are applied."""
    subtotal_excluding_tax: AirbyteSortOrder
    """The subtotal amount excluding any tax calculations."""
    tax: AirbyteSortOrder
    """Total tax amount applied to the invoice."""
    tax_percent: AirbyteSortOrder
    """The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead)."""
    test_clock: AirbyteSortOrder
    """ID of the test clock this invoice belongs to, used for testing time-dependent billing."""
    total: AirbyteSortOrder
    """Total amount of the invoice after all line items, discounts, and taxes are calculated."""
    total_discount_amounts: AirbyteSortOrder
    """Array of the total discount amounts applied, broken down by discount."""
    total_excluding_tax: AirbyteSortOrder
    """Total amount of the invoice excluding all tax calculations."""
    total_tax_amounts: AirbyteSortOrder
    """Array of tax amounts applied to the invoice, broken down by tax rate."""
    transfer_data: AirbyteSortOrder
    """Information about the transfer of funds associated with this invoice in Connect scenarios."""
    updated: AirbyteSortOrder
    """Timestamp indicating when the invoice was last updated."""
    webhooks_delivered_at: AirbyteSortOrder
    """Timestamp indicating when webhooks for this invoice were successfully delivered."""


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


# ===== REFUNDS SEARCH TYPES =====

class RefundsSearchFilter(TypedDict, total=False):
    """Available fields for filtering refunds search queries."""
    amount: int | None
    """Amount refunded, in cents (the smallest currency unit)."""
    balance_transaction: str | None
    """ID of the balance transaction that describes the impact of this refund on your account balance."""
    charge: str | None
    """ID of the charge that was refunded."""
    created: int | None
    """Timestamp indicating when the refund was created."""
    currency: str | None
    """Three-letter ISO currency code in lowercase representing the currency of the refund."""
    destination_details: dict[str, Any] | None
    """Details about the destination where the refunded funds should be sent."""
    id: str | None
    """Unique identifier for the refund object."""
    metadata: dict[str, Any] | None
    """Set of key-value pairs that you can attach to an object for storing additional structured information."""
    object: str | None
    """String representing the object type, always 'refund'."""
    payment_intent: str | None
    """ID of the PaymentIntent that was refunded."""
    reason: str | None
    """Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge)."""
    receipt_number: str | None
    """The transaction number that appears on email receipts sent for this refund."""
    source_transfer_reversal: str | None
    """ID of the transfer reversal that was created as a result of refunding a transfer (Connect only)."""
    status: str | None
    """Status of the refund (pending, requires_action, succeeded, failed, or canceled)."""
    transfer_reversal: str | None
    """ID of the reversal of the transfer that funded the charge being refunded (Connect only)."""
    updated: int | None
    """Timestamp indicating when the refund was last updated."""


class RefundsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[int]
    """Amount refunded, in cents (the smallest currency unit)."""
    balance_transaction: list[str]
    """ID of the balance transaction that describes the impact of this refund on your account balance."""
    charge: list[str]
    """ID of the charge that was refunded."""
    created: list[int]
    """Timestamp indicating when the refund was created."""
    currency: list[str]
    """Three-letter ISO currency code in lowercase representing the currency of the refund."""
    destination_details: list[dict[str, Any]]
    """Details about the destination where the refunded funds should be sent."""
    id: list[str]
    """Unique identifier for the refund object."""
    metadata: list[dict[str, Any]]
    """Set of key-value pairs that you can attach to an object for storing additional structured information."""
    object: list[str]
    """String representing the object type, always 'refund'."""
    payment_intent: list[str]
    """ID of the PaymentIntent that was refunded."""
    reason: list[str]
    """Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge)."""
    receipt_number: list[str]
    """The transaction number that appears on email receipts sent for this refund."""
    source_transfer_reversal: list[str]
    """ID of the transfer reversal that was created as a result of refunding a transfer (Connect only)."""
    status: list[str]
    """Status of the refund (pending, requires_action, succeeded, failed, or canceled)."""
    transfer_reversal: list[str]
    """ID of the reversal of the transfer that funded the charge being refunded (Connect only)."""
    updated: list[int]
    """Timestamp indicating when the refund was last updated."""


class RefundsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """Amount refunded, in cents (the smallest currency unit)."""
    balance_transaction: Any
    """ID of the balance transaction that describes the impact of this refund on your account balance."""
    charge: Any
    """ID of the charge that was refunded."""
    created: Any
    """Timestamp indicating when the refund was created."""
    currency: Any
    """Three-letter ISO currency code in lowercase representing the currency of the refund."""
    destination_details: Any
    """Details about the destination where the refunded funds should be sent."""
    id: Any
    """Unique identifier for the refund object."""
    metadata: Any
    """Set of key-value pairs that you can attach to an object for storing additional structured information."""
    object: Any
    """String representing the object type, always 'refund'."""
    payment_intent: Any
    """ID of the PaymentIntent that was refunded."""
    reason: Any
    """Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge)."""
    receipt_number: Any
    """The transaction number that appears on email receipts sent for this refund."""
    source_transfer_reversal: Any
    """ID of the transfer reversal that was created as a result of refunding a transfer (Connect only)."""
    status: Any
    """Status of the refund (pending, requires_action, succeeded, failed, or canceled)."""
    transfer_reversal: Any
    """ID of the reversal of the transfer that funded the charge being refunded (Connect only)."""
    updated: Any
    """Timestamp indicating when the refund was last updated."""


class RefundsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """Amount refunded, in cents (the smallest currency unit)."""
    balance_transaction: str
    """ID of the balance transaction that describes the impact of this refund on your account balance."""
    charge: str
    """ID of the charge that was refunded."""
    created: str
    """Timestamp indicating when the refund was created."""
    currency: str
    """Three-letter ISO currency code in lowercase representing the currency of the refund."""
    destination_details: str
    """Details about the destination where the refunded funds should be sent."""
    id: str
    """Unique identifier for the refund object."""
    metadata: str
    """Set of key-value pairs that you can attach to an object for storing additional structured information."""
    object: str
    """String representing the object type, always 'refund'."""
    payment_intent: str
    """ID of the PaymentIntent that was refunded."""
    reason: str
    """Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge)."""
    receipt_number: str
    """The transaction number that appears on email receipts sent for this refund."""
    source_transfer_reversal: str
    """ID of the transfer reversal that was created as a result of refunding a transfer (Connect only)."""
    status: str
    """Status of the refund (pending, requires_action, succeeded, failed, or canceled)."""
    transfer_reversal: str
    """ID of the reversal of the transfer that funded the charge being refunded (Connect only)."""
    updated: str
    """Timestamp indicating when the refund was last updated."""


class RefundsSortFilter(TypedDict, total=False):
    """Available fields for sorting refunds search results."""
    amount: AirbyteSortOrder
    """Amount refunded, in cents (the smallest currency unit)."""
    balance_transaction: AirbyteSortOrder
    """ID of the balance transaction that describes the impact of this refund on your account balance."""
    charge: AirbyteSortOrder
    """ID of the charge that was refunded."""
    created: AirbyteSortOrder
    """Timestamp indicating when the refund was created."""
    currency: AirbyteSortOrder
    """Three-letter ISO currency code in lowercase representing the currency of the refund."""
    destination_details: AirbyteSortOrder
    """Details about the destination where the refunded funds should be sent."""
    id: AirbyteSortOrder
    """Unique identifier for the refund object."""
    metadata: AirbyteSortOrder
    """Set of key-value pairs that you can attach to an object for storing additional structured information."""
    object: AirbyteSortOrder
    """String representing the object type, always 'refund'."""
    payment_intent: AirbyteSortOrder
    """ID of the PaymentIntent that was refunded."""
    reason: AirbyteSortOrder
    """Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge)."""
    receipt_number: AirbyteSortOrder
    """The transaction number that appears on email receipts sent for this refund."""
    source_transfer_reversal: AirbyteSortOrder
    """ID of the transfer reversal that was created as a result of refunding a transfer (Connect only)."""
    status: AirbyteSortOrder
    """Status of the refund (pending, requires_action, succeeded, failed, or canceled)."""
    transfer_reversal: AirbyteSortOrder
    """ID of the reversal of the transfer that funded the charge being refunded (Connect only)."""
    updated: AirbyteSortOrder
    """Timestamp indicating when the refund was last updated."""


# Entity-specific condition types for refunds
class RefundsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RefundsSearchFilter


class RefundsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RefundsSearchFilter


class RefundsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RefundsSearchFilter


class RefundsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RefundsSearchFilter


class RefundsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RefundsSearchFilter


class RefundsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RefundsSearchFilter


class RefundsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: RefundsStringFilter


class RefundsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RefundsStringFilter


class RefundsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RefundsStringFilter


class RefundsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: RefundsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RefundsInCondition = TypedDict("RefundsInCondition", {"in": RefundsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RefundsNotCondition = TypedDict("RefundsNotCondition", {"not": "RefundsCondition"}, total=False)
"""Negates the nested condition."""

RefundsAndCondition = TypedDict("RefundsAndCondition", {"and": "list[RefundsCondition]"}, total=False)
"""True if all nested conditions are true."""

RefundsOrCondition = TypedDict("RefundsOrCondition", {"or": "list[RefundsCondition]"}, total=False)
"""True if any nested condition is true."""

RefundsAnyCondition = TypedDict("RefundsAnyCondition", {"any": RefundsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all refunds condition types
RefundsCondition = (
    RefundsEqCondition
    | RefundsNeqCondition
    | RefundsGtCondition
    | RefundsGteCondition
    | RefundsLtCondition
    | RefundsLteCondition
    | RefundsInCondition
    | RefundsLikeCondition
    | RefundsFuzzyCondition
    | RefundsKeywordCondition
    | RefundsContainsCondition
    | RefundsNotCondition
    | RefundsAndCondition
    | RefundsOrCondition
    | RefundsAnyCondition
)


class RefundsSearchQuery(TypedDict, total=False):
    """Search query for refunds entity."""
    filter: RefundsCondition
    sort: list[RefundsSortFilter]


# ===== SUBSCRIPTIONS SEARCH TYPES =====

class SubscriptionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering subscriptions search queries."""
    application: str | None
    """For Connect platforms, the application associated with the subscription."""
    application_fee_percent: float | None
    """For Connect platforms, the percentage of the subscription amount taken as an application fee."""
    automatic_tax: dict[str, Any] | None
    """Automatic tax calculation settings for the subscription."""
    billing: str | None
    """Billing mode configuration for the subscription."""
    billing_cycle_anchor: float | None
    """Timestamp determining when the billing cycle for the subscription starts."""
    billing_cycle_anchor_config: dict[str, Any] | None
    """Configuration for the subscription's billing cycle anchor behavior."""
    billing_thresholds: dict[str, Any] | None
    """Defines thresholds at which an invoice will be sent, controlling billing timing based on usage."""
    cancel_at: float | None
    """Timestamp indicating when the subscription is scheduled to be canceled."""
    cancel_at_period_end: bool | None
    """Boolean indicating whether the subscription will be canceled at the end of the current billing period."""
    canceled_at: float | None
    """Timestamp indicating when the subscription was canceled, if applicable."""
    cancellation_details: dict[str, Any] | None
    """Details about why and how the subscription was canceled."""
    collection_method: str | None
    """How invoices are collected (charge_automatically or send_invoice)."""
    created: int | None
    """Timestamp indicating when the subscription was created."""
    currency: str | None
    """Three-letter ISO currency code in lowercase indicating the currency for the subscription."""
    current_period_end: float | None
    """Timestamp marking the end of the current billing period."""
    current_period_start: int | None
    """Timestamp marking the start of the current billing period."""
    customer: str | None
    """ID of the customer who owns the subscription, expandable to full customer object."""
    days_until_due: int | None
    """Number of days until the invoice is due for subscriptions using send_invoice collection method."""
    default_payment_method: str | None
    """ID of the default payment method for the subscription, taking precedence over default_source."""
    default_source: str | None
    """ID of the default payment source for the subscription."""
    default_tax_rates: list[Any] | None
    """Tax rates that apply to the subscription by default."""
    description: str | None
    """Human-readable description of the subscription, displayable to the customer."""
    discount: dict[str, Any] | None
    """Describes any discount currently applied to the subscription."""
    ended_at: float | None
    """Timestamp indicating when the subscription ended, if applicable."""
    id: str | None
    """Unique identifier for the subscription object."""
    invoice_settings: dict[str, Any] | None
    """Settings for invoices generated by this subscription, such as custom fields and footer."""
    is_deleted: bool | None
    """Indicates whether the subscription has been deleted."""
    items: dict[str, Any] | None
    """List of subscription items, each with an attached price defining what the customer is subscribed to."""
    latest_invoice: str | None
    """The most recent invoice this subscription has generated, expandable to full invoice object."""
    livemode: bool | None
    """Indicates whether the subscription exists in live mode (true) or test mode (false)."""
    metadata: dict[str, Any] | None
    """Set of key-value pairs that you can attach to the subscription for storing additional structured information."""
    next_pending_invoice_item_invoice: int | None
    """Timestamp when the next invoice for pending invoice items will be created."""
    object: str | None
    """String representing the object type, always 'subscription'."""
    on_behalf_of: str | None
    """For Connect platforms, the account for which the subscription is being created or managed."""
    pause_collection: dict[str, Any] | None
    """Configuration for pausing collection on the subscription while retaining the subscription structure."""
    payment_settings: dict[str, Any] | None
    """Payment settings for invoices generated by this subscription."""
    pending_invoice_item_interval: dict[str, Any] | None
    """Specifies an interval for aggregating usage records into pending invoice items."""
    pending_setup_intent: str | None
    """SetupIntent used for collecting user authentication when updating payment methods without immediate payment."""
    pending_update: dict[str, Any] | None
    """If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid."""
    plan: dict[str, Any] | None
    """The plan associated with the subscription (deprecated, use items instead)."""
    quantity: int | None
    """Quantity of the plan subscribed to (deprecated, use items instead)."""
    schedule: str | None
    """ID of the subscription schedule managing this subscription's lifecycle, if applicable."""
    start_date: int | None
    """Timestamp indicating when the subscription started."""
    status: str | None
    """Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)."""
    tax_percent: float | None
    """The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead)."""
    test_clock: str | None
    """ID of the test clock associated with this subscription for simulating time-based scenarios."""
    transfer_data: dict[str, Any] | None
    """For Connect platforms, the account receiving funds from the subscription and optional percentage transferred."""
    trial_end: float | None
    """Timestamp indicating when the trial period ends, if applicable."""
    trial_settings: dict[str, Any] | None
    """Settings related to trial periods, including conditions for ending trials."""
    trial_start: int | None
    """Timestamp indicating when the trial period began, if applicable."""
    updated: int | None
    """Timestamp indicating when the subscription was last updated."""


class SubscriptionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    application: list[str]
    """For Connect platforms, the application associated with the subscription."""
    application_fee_percent: list[float]
    """For Connect platforms, the percentage of the subscription amount taken as an application fee."""
    automatic_tax: list[dict[str, Any]]
    """Automatic tax calculation settings for the subscription."""
    billing: list[str]
    """Billing mode configuration for the subscription."""
    billing_cycle_anchor: list[float]
    """Timestamp determining when the billing cycle for the subscription starts."""
    billing_cycle_anchor_config: list[dict[str, Any]]
    """Configuration for the subscription's billing cycle anchor behavior."""
    billing_thresholds: list[dict[str, Any]]
    """Defines thresholds at which an invoice will be sent, controlling billing timing based on usage."""
    cancel_at: list[float]
    """Timestamp indicating when the subscription is scheduled to be canceled."""
    cancel_at_period_end: list[bool]
    """Boolean indicating whether the subscription will be canceled at the end of the current billing period."""
    canceled_at: list[float]
    """Timestamp indicating when the subscription was canceled, if applicable."""
    cancellation_details: list[dict[str, Any]]
    """Details about why and how the subscription was canceled."""
    collection_method: list[str]
    """How invoices are collected (charge_automatically or send_invoice)."""
    created: list[int]
    """Timestamp indicating when the subscription was created."""
    currency: list[str]
    """Three-letter ISO currency code in lowercase indicating the currency for the subscription."""
    current_period_end: list[float]
    """Timestamp marking the end of the current billing period."""
    current_period_start: list[int]
    """Timestamp marking the start of the current billing period."""
    customer: list[str]
    """ID of the customer who owns the subscription, expandable to full customer object."""
    days_until_due: list[int]
    """Number of days until the invoice is due for subscriptions using send_invoice collection method."""
    default_payment_method: list[str]
    """ID of the default payment method for the subscription, taking precedence over default_source."""
    default_source: list[str]
    """ID of the default payment source for the subscription."""
    default_tax_rates: list[list[Any]]
    """Tax rates that apply to the subscription by default."""
    description: list[str]
    """Human-readable description of the subscription, displayable to the customer."""
    discount: list[dict[str, Any]]
    """Describes any discount currently applied to the subscription."""
    ended_at: list[float]
    """Timestamp indicating when the subscription ended, if applicable."""
    id: list[str]
    """Unique identifier for the subscription object."""
    invoice_settings: list[dict[str, Any]]
    """Settings for invoices generated by this subscription, such as custom fields and footer."""
    is_deleted: list[bool]
    """Indicates whether the subscription has been deleted."""
    items: list[dict[str, Any]]
    """List of subscription items, each with an attached price defining what the customer is subscribed to."""
    latest_invoice: list[str]
    """The most recent invoice this subscription has generated, expandable to full invoice object."""
    livemode: list[bool]
    """Indicates whether the subscription exists in live mode (true) or test mode (false)."""
    metadata: list[dict[str, Any]]
    """Set of key-value pairs that you can attach to the subscription for storing additional structured information."""
    next_pending_invoice_item_invoice: list[int]
    """Timestamp when the next invoice for pending invoice items will be created."""
    object: list[str]
    """String representing the object type, always 'subscription'."""
    on_behalf_of: list[str]
    """For Connect platforms, the account for which the subscription is being created or managed."""
    pause_collection: list[dict[str, Any]]
    """Configuration for pausing collection on the subscription while retaining the subscription structure."""
    payment_settings: list[dict[str, Any]]
    """Payment settings for invoices generated by this subscription."""
    pending_invoice_item_interval: list[dict[str, Any]]
    """Specifies an interval for aggregating usage records into pending invoice items."""
    pending_setup_intent: list[str]
    """SetupIntent used for collecting user authentication when updating payment methods without immediate payment."""
    pending_update: list[dict[str, Any]]
    """If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid."""
    plan: list[dict[str, Any]]
    """The plan associated with the subscription (deprecated, use items instead)."""
    quantity: list[int]
    """Quantity of the plan subscribed to (deprecated, use items instead)."""
    schedule: list[str]
    """ID of the subscription schedule managing this subscription's lifecycle, if applicable."""
    start_date: list[int]
    """Timestamp indicating when the subscription started."""
    status: list[str]
    """Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)."""
    tax_percent: list[float]
    """The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead)."""
    test_clock: list[str]
    """ID of the test clock associated with this subscription for simulating time-based scenarios."""
    transfer_data: list[dict[str, Any]]
    """For Connect platforms, the account receiving funds from the subscription and optional percentage transferred."""
    trial_end: list[float]
    """Timestamp indicating when the trial period ends, if applicable."""
    trial_settings: list[dict[str, Any]]
    """Settings related to trial periods, including conditions for ending trials."""
    trial_start: list[int]
    """Timestamp indicating when the trial period began, if applicable."""
    updated: list[int]
    """Timestamp indicating when the subscription was last updated."""


class SubscriptionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    application: Any
    """For Connect platforms, the application associated with the subscription."""
    application_fee_percent: Any
    """For Connect platforms, the percentage of the subscription amount taken as an application fee."""
    automatic_tax: Any
    """Automatic tax calculation settings for the subscription."""
    billing: Any
    """Billing mode configuration for the subscription."""
    billing_cycle_anchor: Any
    """Timestamp determining when the billing cycle for the subscription starts."""
    billing_cycle_anchor_config: Any
    """Configuration for the subscription's billing cycle anchor behavior."""
    billing_thresholds: Any
    """Defines thresholds at which an invoice will be sent, controlling billing timing based on usage."""
    cancel_at: Any
    """Timestamp indicating when the subscription is scheduled to be canceled."""
    cancel_at_period_end: Any
    """Boolean indicating whether the subscription will be canceled at the end of the current billing period."""
    canceled_at: Any
    """Timestamp indicating when the subscription was canceled, if applicable."""
    cancellation_details: Any
    """Details about why and how the subscription was canceled."""
    collection_method: Any
    """How invoices are collected (charge_automatically or send_invoice)."""
    created: Any
    """Timestamp indicating when the subscription was created."""
    currency: Any
    """Three-letter ISO currency code in lowercase indicating the currency for the subscription."""
    current_period_end: Any
    """Timestamp marking the end of the current billing period."""
    current_period_start: Any
    """Timestamp marking the start of the current billing period."""
    customer: Any
    """ID of the customer who owns the subscription, expandable to full customer object."""
    days_until_due: Any
    """Number of days until the invoice is due for subscriptions using send_invoice collection method."""
    default_payment_method: Any
    """ID of the default payment method for the subscription, taking precedence over default_source."""
    default_source: Any
    """ID of the default payment source for the subscription."""
    default_tax_rates: Any
    """Tax rates that apply to the subscription by default."""
    description: Any
    """Human-readable description of the subscription, displayable to the customer."""
    discount: Any
    """Describes any discount currently applied to the subscription."""
    ended_at: Any
    """Timestamp indicating when the subscription ended, if applicable."""
    id: Any
    """Unique identifier for the subscription object."""
    invoice_settings: Any
    """Settings for invoices generated by this subscription, such as custom fields and footer."""
    is_deleted: Any
    """Indicates whether the subscription has been deleted."""
    items: Any
    """List of subscription items, each with an attached price defining what the customer is subscribed to."""
    latest_invoice: Any
    """The most recent invoice this subscription has generated, expandable to full invoice object."""
    livemode: Any
    """Indicates whether the subscription exists in live mode (true) or test mode (false)."""
    metadata: Any
    """Set of key-value pairs that you can attach to the subscription for storing additional structured information."""
    next_pending_invoice_item_invoice: Any
    """Timestamp when the next invoice for pending invoice items will be created."""
    object: Any
    """String representing the object type, always 'subscription'."""
    on_behalf_of: Any
    """For Connect platforms, the account for which the subscription is being created or managed."""
    pause_collection: Any
    """Configuration for pausing collection on the subscription while retaining the subscription structure."""
    payment_settings: Any
    """Payment settings for invoices generated by this subscription."""
    pending_invoice_item_interval: Any
    """Specifies an interval for aggregating usage records into pending invoice items."""
    pending_setup_intent: Any
    """SetupIntent used for collecting user authentication when updating payment methods without immediate payment."""
    pending_update: Any
    """If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid."""
    plan: Any
    """The plan associated with the subscription (deprecated, use items instead)."""
    quantity: Any
    """Quantity of the plan subscribed to (deprecated, use items instead)."""
    schedule: Any
    """ID of the subscription schedule managing this subscription's lifecycle, if applicable."""
    start_date: Any
    """Timestamp indicating when the subscription started."""
    status: Any
    """Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)."""
    tax_percent: Any
    """The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead)."""
    test_clock: Any
    """ID of the test clock associated with this subscription for simulating time-based scenarios."""
    transfer_data: Any
    """For Connect platforms, the account receiving funds from the subscription and optional percentage transferred."""
    trial_end: Any
    """Timestamp indicating when the trial period ends, if applicable."""
    trial_settings: Any
    """Settings related to trial periods, including conditions for ending trials."""
    trial_start: Any
    """Timestamp indicating when the trial period began, if applicable."""
    updated: Any
    """Timestamp indicating when the subscription was last updated."""


class SubscriptionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    application: str
    """For Connect platforms, the application associated with the subscription."""
    application_fee_percent: str
    """For Connect platforms, the percentage of the subscription amount taken as an application fee."""
    automatic_tax: str
    """Automatic tax calculation settings for the subscription."""
    billing: str
    """Billing mode configuration for the subscription."""
    billing_cycle_anchor: str
    """Timestamp determining when the billing cycle for the subscription starts."""
    billing_cycle_anchor_config: str
    """Configuration for the subscription's billing cycle anchor behavior."""
    billing_thresholds: str
    """Defines thresholds at which an invoice will be sent, controlling billing timing based on usage."""
    cancel_at: str
    """Timestamp indicating when the subscription is scheduled to be canceled."""
    cancel_at_period_end: str
    """Boolean indicating whether the subscription will be canceled at the end of the current billing period."""
    canceled_at: str
    """Timestamp indicating when the subscription was canceled, if applicable."""
    cancellation_details: str
    """Details about why and how the subscription was canceled."""
    collection_method: str
    """How invoices are collected (charge_automatically or send_invoice)."""
    created: str
    """Timestamp indicating when the subscription was created."""
    currency: str
    """Three-letter ISO currency code in lowercase indicating the currency for the subscription."""
    current_period_end: str
    """Timestamp marking the end of the current billing period."""
    current_period_start: str
    """Timestamp marking the start of the current billing period."""
    customer: str
    """ID of the customer who owns the subscription, expandable to full customer object."""
    days_until_due: str
    """Number of days until the invoice is due for subscriptions using send_invoice collection method."""
    default_payment_method: str
    """ID of the default payment method for the subscription, taking precedence over default_source."""
    default_source: str
    """ID of the default payment source for the subscription."""
    default_tax_rates: str
    """Tax rates that apply to the subscription by default."""
    description: str
    """Human-readable description of the subscription, displayable to the customer."""
    discount: str
    """Describes any discount currently applied to the subscription."""
    ended_at: str
    """Timestamp indicating when the subscription ended, if applicable."""
    id: str
    """Unique identifier for the subscription object."""
    invoice_settings: str
    """Settings for invoices generated by this subscription, such as custom fields and footer."""
    is_deleted: str
    """Indicates whether the subscription has been deleted."""
    items: str
    """List of subscription items, each with an attached price defining what the customer is subscribed to."""
    latest_invoice: str
    """The most recent invoice this subscription has generated, expandable to full invoice object."""
    livemode: str
    """Indicates whether the subscription exists in live mode (true) or test mode (false)."""
    metadata: str
    """Set of key-value pairs that you can attach to the subscription for storing additional structured information."""
    next_pending_invoice_item_invoice: str
    """Timestamp when the next invoice for pending invoice items will be created."""
    object: str
    """String representing the object type, always 'subscription'."""
    on_behalf_of: str
    """For Connect platforms, the account for which the subscription is being created or managed."""
    pause_collection: str
    """Configuration for pausing collection on the subscription while retaining the subscription structure."""
    payment_settings: str
    """Payment settings for invoices generated by this subscription."""
    pending_invoice_item_interval: str
    """Specifies an interval for aggregating usage records into pending invoice items."""
    pending_setup_intent: str
    """SetupIntent used for collecting user authentication when updating payment methods without immediate payment."""
    pending_update: str
    """If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid."""
    plan: str
    """The plan associated with the subscription (deprecated, use items instead)."""
    quantity: str
    """Quantity of the plan subscribed to (deprecated, use items instead)."""
    schedule: str
    """ID of the subscription schedule managing this subscription's lifecycle, if applicable."""
    start_date: str
    """Timestamp indicating when the subscription started."""
    status: str
    """Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)."""
    tax_percent: str
    """The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead)."""
    test_clock: str
    """ID of the test clock associated with this subscription for simulating time-based scenarios."""
    transfer_data: str
    """For Connect platforms, the account receiving funds from the subscription and optional percentage transferred."""
    trial_end: str
    """Timestamp indicating when the trial period ends, if applicable."""
    trial_settings: str
    """Settings related to trial periods, including conditions for ending trials."""
    trial_start: str
    """Timestamp indicating when the trial period began, if applicable."""
    updated: str
    """Timestamp indicating when the subscription was last updated."""


class SubscriptionsSortFilter(TypedDict, total=False):
    """Available fields for sorting subscriptions search results."""
    application: AirbyteSortOrder
    """For Connect platforms, the application associated with the subscription."""
    application_fee_percent: AirbyteSortOrder
    """For Connect platforms, the percentage of the subscription amount taken as an application fee."""
    automatic_tax: AirbyteSortOrder
    """Automatic tax calculation settings for the subscription."""
    billing: AirbyteSortOrder
    """Billing mode configuration for the subscription."""
    billing_cycle_anchor: AirbyteSortOrder
    """Timestamp determining when the billing cycle for the subscription starts."""
    billing_cycle_anchor_config: AirbyteSortOrder
    """Configuration for the subscription's billing cycle anchor behavior."""
    billing_thresholds: AirbyteSortOrder
    """Defines thresholds at which an invoice will be sent, controlling billing timing based on usage."""
    cancel_at: AirbyteSortOrder
    """Timestamp indicating when the subscription is scheduled to be canceled."""
    cancel_at_period_end: AirbyteSortOrder
    """Boolean indicating whether the subscription will be canceled at the end of the current billing period."""
    canceled_at: AirbyteSortOrder
    """Timestamp indicating when the subscription was canceled, if applicable."""
    cancellation_details: AirbyteSortOrder
    """Details about why and how the subscription was canceled."""
    collection_method: AirbyteSortOrder
    """How invoices are collected (charge_automatically or send_invoice)."""
    created: AirbyteSortOrder
    """Timestamp indicating when the subscription was created."""
    currency: AirbyteSortOrder
    """Three-letter ISO currency code in lowercase indicating the currency for the subscription."""
    current_period_end: AirbyteSortOrder
    """Timestamp marking the end of the current billing period."""
    current_period_start: AirbyteSortOrder
    """Timestamp marking the start of the current billing period."""
    customer: AirbyteSortOrder
    """ID of the customer who owns the subscription, expandable to full customer object."""
    days_until_due: AirbyteSortOrder
    """Number of days until the invoice is due for subscriptions using send_invoice collection method."""
    default_payment_method: AirbyteSortOrder
    """ID of the default payment method for the subscription, taking precedence over default_source."""
    default_source: AirbyteSortOrder
    """ID of the default payment source for the subscription."""
    default_tax_rates: AirbyteSortOrder
    """Tax rates that apply to the subscription by default."""
    description: AirbyteSortOrder
    """Human-readable description of the subscription, displayable to the customer."""
    discount: AirbyteSortOrder
    """Describes any discount currently applied to the subscription."""
    ended_at: AirbyteSortOrder
    """Timestamp indicating when the subscription ended, if applicable."""
    id: AirbyteSortOrder
    """Unique identifier for the subscription object."""
    invoice_settings: AirbyteSortOrder
    """Settings for invoices generated by this subscription, such as custom fields and footer."""
    is_deleted: AirbyteSortOrder
    """Indicates whether the subscription has been deleted."""
    items: AirbyteSortOrder
    """List of subscription items, each with an attached price defining what the customer is subscribed to."""
    latest_invoice: AirbyteSortOrder
    """The most recent invoice this subscription has generated, expandable to full invoice object."""
    livemode: AirbyteSortOrder
    """Indicates whether the subscription exists in live mode (true) or test mode (false)."""
    metadata: AirbyteSortOrder
    """Set of key-value pairs that you can attach to the subscription for storing additional structured information."""
    next_pending_invoice_item_invoice: AirbyteSortOrder
    """Timestamp when the next invoice for pending invoice items will be created."""
    object: AirbyteSortOrder
    """String representing the object type, always 'subscription'."""
    on_behalf_of: AirbyteSortOrder
    """For Connect platforms, the account for which the subscription is being created or managed."""
    pause_collection: AirbyteSortOrder
    """Configuration for pausing collection on the subscription while retaining the subscription structure."""
    payment_settings: AirbyteSortOrder
    """Payment settings for invoices generated by this subscription."""
    pending_invoice_item_interval: AirbyteSortOrder
    """Specifies an interval for aggregating usage records into pending invoice items."""
    pending_setup_intent: AirbyteSortOrder
    """SetupIntent used for collecting user authentication when updating payment methods without immediate payment."""
    pending_update: AirbyteSortOrder
    """If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid."""
    plan: AirbyteSortOrder
    """The plan associated with the subscription (deprecated, use items instead)."""
    quantity: AirbyteSortOrder
    """Quantity of the plan subscribed to (deprecated, use items instead)."""
    schedule: AirbyteSortOrder
    """ID of the subscription schedule managing this subscription's lifecycle, if applicable."""
    start_date: AirbyteSortOrder
    """Timestamp indicating when the subscription started."""
    status: AirbyteSortOrder
    """Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)."""
    tax_percent: AirbyteSortOrder
    """The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead)."""
    test_clock: AirbyteSortOrder
    """ID of the test clock associated with this subscription for simulating time-based scenarios."""
    transfer_data: AirbyteSortOrder
    """For Connect platforms, the account receiving funds from the subscription and optional percentage transferred."""
    trial_end: AirbyteSortOrder
    """Timestamp indicating when the trial period ends, if applicable."""
    trial_settings: AirbyteSortOrder
    """Settings related to trial periods, including conditions for ending trials."""
    trial_start: AirbyteSortOrder
    """Timestamp indicating when the trial period began, if applicable."""
    updated: AirbyteSortOrder
    """Timestamp indicating when the subscription was last updated."""


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



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
