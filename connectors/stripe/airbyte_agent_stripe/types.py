"""
Type definitions for stripe connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



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

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    id: str

class CustomersSearchParams(TypedDict):
    """Parameters for customers.search operation"""
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

class InvoicesSearchParams(TypedDict):
    """Parameters for invoices.search operation"""
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

class ChargesSearchParams(TypedDict):
    """Parameters for charges.search operation"""
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

class SubscriptionsSearchParams(TypedDict):
    """Parameters for subscriptions.search operation"""
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

class ProductsGetParams(TypedDict):
    """Parameters for products.get operation"""
    id: str

class ProductsSearchParams(TypedDict):
    """Parameters for products.search operation"""
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

class PaymentIntentsSearchParams(TypedDict):
    """Parameters for payment_intents.search operation"""
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
