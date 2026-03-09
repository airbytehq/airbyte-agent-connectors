"""
Type definitions for chargebee connector.
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

class CustomerListParams(TypedDict):
    """Parameters for customer.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class CustomerGetParams(TypedDict):
    """Parameters for customer.get operation"""
    id: str

class SubscriptionListParams(TypedDict):
    """Parameters for subscription.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class SubscriptionGetParams(TypedDict):
    """Parameters for subscription.get operation"""
    id: str

class InvoiceListParams(TypedDict):
    """Parameters for invoice.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class InvoiceGetParams(TypedDict):
    """Parameters for invoice.get operation"""
    id: str

class CreditNoteListParams(TypedDict):
    """Parameters for credit_note.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class CreditNoteGetParams(TypedDict):
    """Parameters for credit_note.get operation"""
    id: str

class CouponListParams(TypedDict):
    """Parameters for coupon.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class CouponGetParams(TypedDict):
    """Parameters for coupon.get operation"""
    id: str

class TransactionListParams(TypedDict):
    """Parameters for transaction.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class TransactionGetParams(TypedDict):
    """Parameters for transaction.get operation"""
    id: str

class EventListParams(TypedDict):
    """Parameters for event.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class EventGetParams(TypedDict):
    """Parameters for event.get operation"""
    id: str

class OrderListParams(TypedDict):
    """Parameters for order.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class OrderGetParams(TypedDict):
    """Parameters for order.get operation"""
    id: str

class ItemListParams(TypedDict):
    """Parameters for item.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class ItemGetParams(TypedDict):
    """Parameters for item.get operation"""
    id: str

class ItemPriceListParams(TypedDict):
    """Parameters for item_price.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class ItemPriceGetParams(TypedDict):
    """Parameters for item_price.get operation"""
    id: str

class PaymentSourceListParams(TypedDict):
    """Parameters for payment_source.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class PaymentSourceGetParams(TypedDict):
    """Parameters for payment_source.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== SUBSCRIPTION SEARCH TYPES =====

class SubscriptionSearchFilter(TypedDict, total=False):
    """Available fields for filtering subscription search queries."""
    activated_at: int | None
    """The date and time when the subscription was activated."""
    addons: list[Any] | None
    """Represents any additional features or services added to the subscription"""
    affiliate_token: str | None
    """The affiliate token associated with the subscription."""
    auto_close_invoices: bool | None
    """Defines if the invoices are automatically closed or not."""
    auto_collection: str | None
    """Indicates if auto-collection is enabled for the subscription."""
    base_currency_code: str | None
    """The base currency code used for the subscription."""
    billing_period: int | None
    """The billing period duration for the subscription."""
    billing_period_unit: str | None
    """The unit of the billing period."""
    business_entity_id: str | None
    """The ID of the business entity to which the subscription belongs."""
    cancel_reason: str | None
    """The reason for the cancellation of the subscription."""
    cancel_reason_code: str | None
    """The code associated with the cancellation reason."""
    cancel_schedule_created_at: int | None
    """The date and time when the cancellation schedule was created."""
    cancelled_at: int | None
    """The date and time when the subscription was cancelled."""
    channel: str | None
    """The channel through which the subscription was acquired."""
    charged_event_based_addons: list[Any] | None
    """Details of addons charged based on events"""
    charged_items: list[Any] | None
    """Lists the items that have been charged as part of the subscription"""
    contract_term: dict[str, Any] | None
    """Contains details about the contract term of the subscription"""
    contract_term_billing_cycle_on_renewal: int | None
    """Indicates if the contract term billing cycle is applied on renewal."""
    coupon: str | None
    """The coupon applied to the subscription."""
    coupons: list[Any] | None
    """Details of applied coupons"""
    create_pending_invoices: bool | None
    """Indicates if pending invoices are created."""
    created_at: int | None
    """The date and time of the creation of the subscription."""
    created_from_ip: str | None
    """The IP address from which the subscription was created."""
    currency_code: str | None
    """The currency code used for the subscription."""
    current_term_end: int | None
    """The end date of the current term for the subscription."""
    current_term_start: int | None
    """The start date of the current term for the subscription."""
    custom_fields: list[Any] | None
    """"""
    customer_id: str | None
    """The ID of the customer associated with the subscription."""
    deleted: bool | None
    """Indicates if the subscription has been deleted."""
    discounts: list[Any] | None
    """Includes any discounts applied to the subscription"""
    due_invoices_count: int | None
    """The count of due invoices for the subscription."""
    due_since: int | None
    """The date since which the invoices are due."""
    event_based_addons: list[Any] | None
    """Specifies any event-based addons associated with the subscription"""
    exchange_rate: float | None
    """The exchange rate used for currency conversion."""
    free_period: int | None
    """The duration of the free period for the subscription."""
    free_period_unit: str | None
    """The unit of the free period duration."""
    gift_id: str | None
    """The ID of the gift associated with the subscription."""
    has_scheduled_advance_invoices: bool | None
    """Indicates if there are scheduled advance invoices for the subscription."""
    has_scheduled_changes: bool | None
    """Indicates if there are scheduled changes for the subscription."""
    id: str | None
    """The unique ID of the subscription."""
    invoice_notes: str | None
    """Any notes added to the invoices of the subscription."""
    item_tiers: list[Any] | None
    """Provides information about tiers or levels for specific subscription items"""
    meta_data: dict[str, Any] | None
    """Additional metadata associated with subscription"""
    metadata: dict[str, Any] | None
    """Additional metadata associated with subscription"""
    mrr: int | None
    """The monthly recurring revenue generated by the subscription."""
    next_billing_at: int | None
    """The date and time of the next billing event for the subscription."""
    object_: str | None
    """The type of object (subscription)."""
    offline_payment_method: str | None
    """The offline payment method used for the subscription."""
    override_relationship: bool | None
    """Indicates if the existing relationship is overridden by this subscription."""
    pause_date: int | None
    """The date on which the subscription was paused."""
    payment_source_id: str | None
    """The ID of the payment source used for the subscription."""
    plan_amount: int | None
    """The total amount charged for the plan of the subscription."""
    plan_amount_in_decimal: str | None
    """The total amount charged for the plan in decimal format."""
    plan_free_quantity: int | None
    """The free quantity included in the plan of the subscription."""
    plan_free_quantity_in_decimal: str | None
    """The free quantity included in the plan in decimal format."""
    plan_id: str | None
    """The ID of the plan associated with the subscription."""
    plan_quantity: int | None
    """The quantity of the plan included in the subscription."""
    plan_quantity_in_decimal: str | None
    """The quantity of the plan in decimal format."""
    plan_unit_price: int | None
    """The unit price of the plan for the subscription."""
    plan_unit_price_in_decimal: str | None
    """The unit price of the plan in decimal format."""
    po_number: str | None
    """The purchase order number associated with the subscription."""
    referral_info: dict[str, Any] | None
    """Contains details related to any referral information associated with the subscription"""
    remaining_billing_cycles: int | None
    """The count of remaining billing cycles for the subscription."""
    resource_version: int | None
    """The version of the resource (subscription)."""
    resume_date: int | None
    """The date on which the subscription was resumed."""
    setup_fee: int | None
    """The setup fee charged for the subscription."""
    shipping_address: dict[str, Any] | None
    """Stores the shipping address related to the subscription"""
    start_date: int | None
    """The start date of the subscription."""
    started_at: int | None
    """The date and time when the subscription started."""
    status: str | None
    """The current status of the subscription."""
    subscription_items: list[Any] | None
    """Lists individual items included in the subscription"""
    total_dues: int | None
    """The total amount of dues for the subscription."""
    trial_end: int | None
    """The end date of the trial period for the subscription."""
    trial_end_action: str | None
    """The action to be taken at the end of the trial period."""
    trial_start: int | None
    """The start date of the trial period for the subscription."""
    updated_at: int | None
    """The date and time when the subscription was last updated."""


class SubscriptionInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    activated_at: list[int]
    """The date and time when the subscription was activated."""
    addons: list[list[Any]]
    """Represents any additional features or services added to the subscription"""
    affiliate_token: list[str]
    """The affiliate token associated with the subscription."""
    auto_close_invoices: list[bool]
    """Defines if the invoices are automatically closed or not."""
    auto_collection: list[str]
    """Indicates if auto-collection is enabled for the subscription."""
    base_currency_code: list[str]
    """The base currency code used for the subscription."""
    billing_period: list[int]
    """The billing period duration for the subscription."""
    billing_period_unit: list[str]
    """The unit of the billing period."""
    business_entity_id: list[str]
    """The ID of the business entity to which the subscription belongs."""
    cancel_reason: list[str]
    """The reason for the cancellation of the subscription."""
    cancel_reason_code: list[str]
    """The code associated with the cancellation reason."""
    cancel_schedule_created_at: list[int]
    """The date and time when the cancellation schedule was created."""
    cancelled_at: list[int]
    """The date and time when the subscription was cancelled."""
    channel: list[str]
    """The channel through which the subscription was acquired."""
    charged_event_based_addons: list[list[Any]]
    """Details of addons charged based on events"""
    charged_items: list[list[Any]]
    """Lists the items that have been charged as part of the subscription"""
    contract_term: list[dict[str, Any]]
    """Contains details about the contract term of the subscription"""
    contract_term_billing_cycle_on_renewal: list[int]
    """Indicates if the contract term billing cycle is applied on renewal."""
    coupon: list[str]
    """The coupon applied to the subscription."""
    coupons: list[list[Any]]
    """Details of applied coupons"""
    create_pending_invoices: list[bool]
    """Indicates if pending invoices are created."""
    created_at: list[int]
    """The date and time of the creation of the subscription."""
    created_from_ip: list[str]
    """The IP address from which the subscription was created."""
    currency_code: list[str]
    """The currency code used for the subscription."""
    current_term_end: list[int]
    """The end date of the current term for the subscription."""
    current_term_start: list[int]
    """The start date of the current term for the subscription."""
    custom_fields: list[list[Any]]
    """"""
    customer_id: list[str]
    """The ID of the customer associated with the subscription."""
    deleted: list[bool]
    """Indicates if the subscription has been deleted."""
    discounts: list[list[Any]]
    """Includes any discounts applied to the subscription"""
    due_invoices_count: list[int]
    """The count of due invoices for the subscription."""
    due_since: list[int]
    """The date since which the invoices are due."""
    event_based_addons: list[list[Any]]
    """Specifies any event-based addons associated with the subscription"""
    exchange_rate: list[float]
    """The exchange rate used for currency conversion."""
    free_period: list[int]
    """The duration of the free period for the subscription."""
    free_period_unit: list[str]
    """The unit of the free period duration."""
    gift_id: list[str]
    """The ID of the gift associated with the subscription."""
    has_scheduled_advance_invoices: list[bool]
    """Indicates if there are scheduled advance invoices for the subscription."""
    has_scheduled_changes: list[bool]
    """Indicates if there are scheduled changes for the subscription."""
    id: list[str]
    """The unique ID of the subscription."""
    invoice_notes: list[str]
    """Any notes added to the invoices of the subscription."""
    item_tiers: list[list[Any]]
    """Provides information about tiers or levels for specific subscription items"""
    meta_data: list[dict[str, Any]]
    """Additional metadata associated with subscription"""
    metadata: list[dict[str, Any]]
    """Additional metadata associated with subscription"""
    mrr: list[int]
    """The monthly recurring revenue generated by the subscription."""
    next_billing_at: list[int]
    """The date and time of the next billing event for the subscription."""
    object_: list[str]
    """The type of object (subscription)."""
    offline_payment_method: list[str]
    """The offline payment method used for the subscription."""
    override_relationship: list[bool]
    """Indicates if the existing relationship is overridden by this subscription."""
    pause_date: list[int]
    """The date on which the subscription was paused."""
    payment_source_id: list[str]
    """The ID of the payment source used for the subscription."""
    plan_amount: list[int]
    """The total amount charged for the plan of the subscription."""
    plan_amount_in_decimal: list[str]
    """The total amount charged for the plan in decimal format."""
    plan_free_quantity: list[int]
    """The free quantity included in the plan of the subscription."""
    plan_free_quantity_in_decimal: list[str]
    """The free quantity included in the plan in decimal format."""
    plan_id: list[str]
    """The ID of the plan associated with the subscription."""
    plan_quantity: list[int]
    """The quantity of the plan included in the subscription."""
    plan_quantity_in_decimal: list[str]
    """The quantity of the plan in decimal format."""
    plan_unit_price: list[int]
    """The unit price of the plan for the subscription."""
    plan_unit_price_in_decimal: list[str]
    """The unit price of the plan in decimal format."""
    po_number: list[str]
    """The purchase order number associated with the subscription."""
    referral_info: list[dict[str, Any]]
    """Contains details related to any referral information associated with the subscription"""
    remaining_billing_cycles: list[int]
    """The count of remaining billing cycles for the subscription."""
    resource_version: list[int]
    """The version of the resource (subscription)."""
    resume_date: list[int]
    """The date on which the subscription was resumed."""
    setup_fee: list[int]
    """The setup fee charged for the subscription."""
    shipping_address: list[dict[str, Any]]
    """Stores the shipping address related to the subscription"""
    start_date: list[int]
    """The start date of the subscription."""
    started_at: list[int]
    """The date and time when the subscription started."""
    status: list[str]
    """The current status of the subscription."""
    subscription_items: list[list[Any]]
    """Lists individual items included in the subscription"""
    total_dues: list[int]
    """The total amount of dues for the subscription."""
    trial_end: list[int]
    """The end date of the trial period for the subscription."""
    trial_end_action: list[str]
    """The action to be taken at the end of the trial period."""
    trial_start: list[int]
    """The start date of the trial period for the subscription."""
    updated_at: list[int]
    """The date and time when the subscription was last updated."""


class SubscriptionAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    activated_at: Any
    """The date and time when the subscription was activated."""
    addons: Any
    """Represents any additional features or services added to the subscription"""
    affiliate_token: Any
    """The affiliate token associated with the subscription."""
    auto_close_invoices: Any
    """Defines if the invoices are automatically closed or not."""
    auto_collection: Any
    """Indicates if auto-collection is enabled for the subscription."""
    base_currency_code: Any
    """The base currency code used for the subscription."""
    billing_period: Any
    """The billing period duration for the subscription."""
    billing_period_unit: Any
    """The unit of the billing period."""
    business_entity_id: Any
    """The ID of the business entity to which the subscription belongs."""
    cancel_reason: Any
    """The reason for the cancellation of the subscription."""
    cancel_reason_code: Any
    """The code associated with the cancellation reason."""
    cancel_schedule_created_at: Any
    """The date and time when the cancellation schedule was created."""
    cancelled_at: Any
    """The date and time when the subscription was cancelled."""
    channel: Any
    """The channel through which the subscription was acquired."""
    charged_event_based_addons: Any
    """Details of addons charged based on events"""
    charged_items: Any
    """Lists the items that have been charged as part of the subscription"""
    contract_term: Any
    """Contains details about the contract term of the subscription"""
    contract_term_billing_cycle_on_renewal: Any
    """Indicates if the contract term billing cycle is applied on renewal."""
    coupon: Any
    """The coupon applied to the subscription."""
    coupons: Any
    """Details of applied coupons"""
    create_pending_invoices: Any
    """Indicates if pending invoices are created."""
    created_at: Any
    """The date and time of the creation of the subscription."""
    created_from_ip: Any
    """The IP address from which the subscription was created."""
    currency_code: Any
    """The currency code used for the subscription."""
    current_term_end: Any
    """The end date of the current term for the subscription."""
    current_term_start: Any
    """The start date of the current term for the subscription."""
    custom_fields: Any
    """"""
    customer_id: Any
    """The ID of the customer associated with the subscription."""
    deleted: Any
    """Indicates if the subscription has been deleted."""
    discounts: Any
    """Includes any discounts applied to the subscription"""
    due_invoices_count: Any
    """The count of due invoices for the subscription."""
    due_since: Any
    """The date since which the invoices are due."""
    event_based_addons: Any
    """Specifies any event-based addons associated with the subscription"""
    exchange_rate: Any
    """The exchange rate used for currency conversion."""
    free_period: Any
    """The duration of the free period for the subscription."""
    free_period_unit: Any
    """The unit of the free period duration."""
    gift_id: Any
    """The ID of the gift associated with the subscription."""
    has_scheduled_advance_invoices: Any
    """Indicates if there are scheduled advance invoices for the subscription."""
    has_scheduled_changes: Any
    """Indicates if there are scheduled changes for the subscription."""
    id: Any
    """The unique ID of the subscription."""
    invoice_notes: Any
    """Any notes added to the invoices of the subscription."""
    item_tiers: Any
    """Provides information about tiers or levels for specific subscription items"""
    meta_data: Any
    """Additional metadata associated with subscription"""
    metadata: Any
    """Additional metadata associated with subscription"""
    mrr: Any
    """The monthly recurring revenue generated by the subscription."""
    next_billing_at: Any
    """The date and time of the next billing event for the subscription."""
    object_: Any
    """The type of object (subscription)."""
    offline_payment_method: Any
    """The offline payment method used for the subscription."""
    override_relationship: Any
    """Indicates if the existing relationship is overridden by this subscription."""
    pause_date: Any
    """The date on which the subscription was paused."""
    payment_source_id: Any
    """The ID of the payment source used for the subscription."""
    plan_amount: Any
    """The total amount charged for the plan of the subscription."""
    plan_amount_in_decimal: Any
    """The total amount charged for the plan in decimal format."""
    plan_free_quantity: Any
    """The free quantity included in the plan of the subscription."""
    plan_free_quantity_in_decimal: Any
    """The free quantity included in the plan in decimal format."""
    plan_id: Any
    """The ID of the plan associated with the subscription."""
    plan_quantity: Any
    """The quantity of the plan included in the subscription."""
    plan_quantity_in_decimal: Any
    """The quantity of the plan in decimal format."""
    plan_unit_price: Any
    """The unit price of the plan for the subscription."""
    plan_unit_price_in_decimal: Any
    """The unit price of the plan in decimal format."""
    po_number: Any
    """The purchase order number associated with the subscription."""
    referral_info: Any
    """Contains details related to any referral information associated with the subscription"""
    remaining_billing_cycles: Any
    """The count of remaining billing cycles for the subscription."""
    resource_version: Any
    """The version of the resource (subscription)."""
    resume_date: Any
    """The date on which the subscription was resumed."""
    setup_fee: Any
    """The setup fee charged for the subscription."""
    shipping_address: Any
    """Stores the shipping address related to the subscription"""
    start_date: Any
    """The start date of the subscription."""
    started_at: Any
    """The date and time when the subscription started."""
    status: Any
    """The current status of the subscription."""
    subscription_items: Any
    """Lists individual items included in the subscription"""
    total_dues: Any
    """The total amount of dues for the subscription."""
    trial_end: Any
    """The end date of the trial period for the subscription."""
    trial_end_action: Any
    """The action to be taken at the end of the trial period."""
    trial_start: Any
    """The start date of the trial period for the subscription."""
    updated_at: Any
    """The date and time when the subscription was last updated."""


class SubscriptionStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    activated_at: str
    """The date and time when the subscription was activated."""
    addons: str
    """Represents any additional features or services added to the subscription"""
    affiliate_token: str
    """The affiliate token associated with the subscription."""
    auto_close_invoices: str
    """Defines if the invoices are automatically closed or not."""
    auto_collection: str
    """Indicates if auto-collection is enabled for the subscription."""
    base_currency_code: str
    """The base currency code used for the subscription."""
    billing_period: str
    """The billing period duration for the subscription."""
    billing_period_unit: str
    """The unit of the billing period."""
    business_entity_id: str
    """The ID of the business entity to which the subscription belongs."""
    cancel_reason: str
    """The reason for the cancellation of the subscription."""
    cancel_reason_code: str
    """The code associated with the cancellation reason."""
    cancel_schedule_created_at: str
    """The date and time when the cancellation schedule was created."""
    cancelled_at: str
    """The date and time when the subscription was cancelled."""
    channel: str
    """The channel through which the subscription was acquired."""
    charged_event_based_addons: str
    """Details of addons charged based on events"""
    charged_items: str
    """Lists the items that have been charged as part of the subscription"""
    contract_term: str
    """Contains details about the contract term of the subscription"""
    contract_term_billing_cycle_on_renewal: str
    """Indicates if the contract term billing cycle is applied on renewal."""
    coupon: str
    """The coupon applied to the subscription."""
    coupons: str
    """Details of applied coupons"""
    create_pending_invoices: str
    """Indicates if pending invoices are created."""
    created_at: str
    """The date and time of the creation of the subscription."""
    created_from_ip: str
    """The IP address from which the subscription was created."""
    currency_code: str
    """The currency code used for the subscription."""
    current_term_end: str
    """The end date of the current term for the subscription."""
    current_term_start: str
    """The start date of the current term for the subscription."""
    custom_fields: str
    """"""
    customer_id: str
    """The ID of the customer associated with the subscription."""
    deleted: str
    """Indicates if the subscription has been deleted."""
    discounts: str
    """Includes any discounts applied to the subscription"""
    due_invoices_count: str
    """The count of due invoices for the subscription."""
    due_since: str
    """The date since which the invoices are due."""
    event_based_addons: str
    """Specifies any event-based addons associated with the subscription"""
    exchange_rate: str
    """The exchange rate used for currency conversion."""
    free_period: str
    """The duration of the free period for the subscription."""
    free_period_unit: str
    """The unit of the free period duration."""
    gift_id: str
    """The ID of the gift associated with the subscription."""
    has_scheduled_advance_invoices: str
    """Indicates if there are scheduled advance invoices for the subscription."""
    has_scheduled_changes: str
    """Indicates if there are scheduled changes for the subscription."""
    id: str
    """The unique ID of the subscription."""
    invoice_notes: str
    """Any notes added to the invoices of the subscription."""
    item_tiers: str
    """Provides information about tiers or levels for specific subscription items"""
    meta_data: str
    """Additional metadata associated with subscription"""
    metadata: str
    """Additional metadata associated with subscription"""
    mrr: str
    """The monthly recurring revenue generated by the subscription."""
    next_billing_at: str
    """The date and time of the next billing event for the subscription."""
    object_: str
    """The type of object (subscription)."""
    offline_payment_method: str
    """The offline payment method used for the subscription."""
    override_relationship: str
    """Indicates if the existing relationship is overridden by this subscription."""
    pause_date: str
    """The date on which the subscription was paused."""
    payment_source_id: str
    """The ID of the payment source used for the subscription."""
    plan_amount: str
    """The total amount charged for the plan of the subscription."""
    plan_amount_in_decimal: str
    """The total amount charged for the plan in decimal format."""
    plan_free_quantity: str
    """The free quantity included in the plan of the subscription."""
    plan_free_quantity_in_decimal: str
    """The free quantity included in the plan in decimal format."""
    plan_id: str
    """The ID of the plan associated with the subscription."""
    plan_quantity: str
    """The quantity of the plan included in the subscription."""
    plan_quantity_in_decimal: str
    """The quantity of the plan in decimal format."""
    plan_unit_price: str
    """The unit price of the plan for the subscription."""
    plan_unit_price_in_decimal: str
    """The unit price of the plan in decimal format."""
    po_number: str
    """The purchase order number associated with the subscription."""
    referral_info: str
    """Contains details related to any referral information associated with the subscription"""
    remaining_billing_cycles: str
    """The count of remaining billing cycles for the subscription."""
    resource_version: str
    """The version of the resource (subscription)."""
    resume_date: str
    """The date on which the subscription was resumed."""
    setup_fee: str
    """The setup fee charged for the subscription."""
    shipping_address: str
    """Stores the shipping address related to the subscription"""
    start_date: str
    """The start date of the subscription."""
    started_at: str
    """The date and time when the subscription started."""
    status: str
    """The current status of the subscription."""
    subscription_items: str
    """Lists individual items included in the subscription"""
    total_dues: str
    """The total amount of dues for the subscription."""
    trial_end: str
    """The end date of the trial period for the subscription."""
    trial_end_action: str
    """The action to be taken at the end of the trial period."""
    trial_start: str
    """The start date of the trial period for the subscription."""
    updated_at: str
    """The date and time when the subscription was last updated."""


class SubscriptionSortFilter(TypedDict, total=False):
    """Available fields for sorting subscription search results."""
    activated_at: AirbyteSortOrder
    """The date and time when the subscription was activated."""
    addons: AirbyteSortOrder
    """Represents any additional features or services added to the subscription"""
    affiliate_token: AirbyteSortOrder
    """The affiliate token associated with the subscription."""
    auto_close_invoices: AirbyteSortOrder
    """Defines if the invoices are automatically closed or not."""
    auto_collection: AirbyteSortOrder
    """Indicates if auto-collection is enabled for the subscription."""
    base_currency_code: AirbyteSortOrder
    """The base currency code used for the subscription."""
    billing_period: AirbyteSortOrder
    """The billing period duration for the subscription."""
    billing_period_unit: AirbyteSortOrder
    """The unit of the billing period."""
    business_entity_id: AirbyteSortOrder
    """The ID of the business entity to which the subscription belongs."""
    cancel_reason: AirbyteSortOrder
    """The reason for the cancellation of the subscription."""
    cancel_reason_code: AirbyteSortOrder
    """The code associated with the cancellation reason."""
    cancel_schedule_created_at: AirbyteSortOrder
    """The date and time when the cancellation schedule was created."""
    cancelled_at: AirbyteSortOrder
    """The date and time when the subscription was cancelled."""
    channel: AirbyteSortOrder
    """The channel through which the subscription was acquired."""
    charged_event_based_addons: AirbyteSortOrder
    """Details of addons charged based on events"""
    charged_items: AirbyteSortOrder
    """Lists the items that have been charged as part of the subscription"""
    contract_term: AirbyteSortOrder
    """Contains details about the contract term of the subscription"""
    contract_term_billing_cycle_on_renewal: AirbyteSortOrder
    """Indicates if the contract term billing cycle is applied on renewal."""
    coupon: AirbyteSortOrder
    """The coupon applied to the subscription."""
    coupons: AirbyteSortOrder
    """Details of applied coupons"""
    create_pending_invoices: AirbyteSortOrder
    """Indicates if pending invoices are created."""
    created_at: AirbyteSortOrder
    """The date and time of the creation of the subscription."""
    created_from_ip: AirbyteSortOrder
    """The IP address from which the subscription was created."""
    currency_code: AirbyteSortOrder
    """The currency code used for the subscription."""
    current_term_end: AirbyteSortOrder
    """The end date of the current term for the subscription."""
    current_term_start: AirbyteSortOrder
    """The start date of the current term for the subscription."""
    custom_fields: AirbyteSortOrder
    """"""
    customer_id: AirbyteSortOrder
    """The ID of the customer associated with the subscription."""
    deleted: AirbyteSortOrder
    """Indicates if the subscription has been deleted."""
    discounts: AirbyteSortOrder
    """Includes any discounts applied to the subscription"""
    due_invoices_count: AirbyteSortOrder
    """The count of due invoices for the subscription."""
    due_since: AirbyteSortOrder
    """The date since which the invoices are due."""
    event_based_addons: AirbyteSortOrder
    """Specifies any event-based addons associated with the subscription"""
    exchange_rate: AirbyteSortOrder
    """The exchange rate used for currency conversion."""
    free_period: AirbyteSortOrder
    """The duration of the free period for the subscription."""
    free_period_unit: AirbyteSortOrder
    """The unit of the free period duration."""
    gift_id: AirbyteSortOrder
    """The ID of the gift associated with the subscription."""
    has_scheduled_advance_invoices: AirbyteSortOrder
    """Indicates if there are scheduled advance invoices for the subscription."""
    has_scheduled_changes: AirbyteSortOrder
    """Indicates if there are scheduled changes for the subscription."""
    id: AirbyteSortOrder
    """The unique ID of the subscription."""
    invoice_notes: AirbyteSortOrder
    """Any notes added to the invoices of the subscription."""
    item_tiers: AirbyteSortOrder
    """Provides information about tiers or levels for specific subscription items"""
    meta_data: AirbyteSortOrder
    """Additional metadata associated with subscription"""
    metadata: AirbyteSortOrder
    """Additional metadata associated with subscription"""
    mrr: AirbyteSortOrder
    """The monthly recurring revenue generated by the subscription."""
    next_billing_at: AirbyteSortOrder
    """The date and time of the next billing event for the subscription."""
    object_: AirbyteSortOrder
    """The type of object (subscription)."""
    offline_payment_method: AirbyteSortOrder
    """The offline payment method used for the subscription."""
    override_relationship: AirbyteSortOrder
    """Indicates if the existing relationship is overridden by this subscription."""
    pause_date: AirbyteSortOrder
    """The date on which the subscription was paused."""
    payment_source_id: AirbyteSortOrder
    """The ID of the payment source used for the subscription."""
    plan_amount: AirbyteSortOrder
    """The total amount charged for the plan of the subscription."""
    plan_amount_in_decimal: AirbyteSortOrder
    """The total amount charged for the plan in decimal format."""
    plan_free_quantity: AirbyteSortOrder
    """The free quantity included in the plan of the subscription."""
    plan_free_quantity_in_decimal: AirbyteSortOrder
    """The free quantity included in the plan in decimal format."""
    plan_id: AirbyteSortOrder
    """The ID of the plan associated with the subscription."""
    plan_quantity: AirbyteSortOrder
    """The quantity of the plan included in the subscription."""
    plan_quantity_in_decimal: AirbyteSortOrder
    """The quantity of the plan in decimal format."""
    plan_unit_price: AirbyteSortOrder
    """The unit price of the plan for the subscription."""
    plan_unit_price_in_decimal: AirbyteSortOrder
    """The unit price of the plan in decimal format."""
    po_number: AirbyteSortOrder
    """The purchase order number associated with the subscription."""
    referral_info: AirbyteSortOrder
    """Contains details related to any referral information associated with the subscription"""
    remaining_billing_cycles: AirbyteSortOrder
    """The count of remaining billing cycles for the subscription."""
    resource_version: AirbyteSortOrder
    """The version of the resource (subscription)."""
    resume_date: AirbyteSortOrder
    """The date on which the subscription was resumed."""
    setup_fee: AirbyteSortOrder
    """The setup fee charged for the subscription."""
    shipping_address: AirbyteSortOrder
    """Stores the shipping address related to the subscription"""
    start_date: AirbyteSortOrder
    """The start date of the subscription."""
    started_at: AirbyteSortOrder
    """The date and time when the subscription started."""
    status: AirbyteSortOrder
    """The current status of the subscription."""
    subscription_items: AirbyteSortOrder
    """Lists individual items included in the subscription"""
    total_dues: AirbyteSortOrder
    """The total amount of dues for the subscription."""
    trial_end: AirbyteSortOrder
    """The end date of the trial period for the subscription."""
    trial_end_action: AirbyteSortOrder
    """The action to be taken at the end of the trial period."""
    trial_start: AirbyteSortOrder
    """The start date of the trial period for the subscription."""
    updated_at: AirbyteSortOrder
    """The date and time when the subscription was last updated."""


# Entity-specific condition types for subscription
class SubscriptionEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SubscriptionSearchFilter


class SubscriptionNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SubscriptionSearchFilter


class SubscriptionGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SubscriptionSearchFilter


class SubscriptionGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SubscriptionSearchFilter


class SubscriptionLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SubscriptionSearchFilter


class SubscriptionLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SubscriptionSearchFilter


class SubscriptionLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SubscriptionStringFilter


class SubscriptionFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SubscriptionStringFilter


class SubscriptionKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SubscriptionStringFilter


class SubscriptionContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SubscriptionAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SubscriptionInCondition = TypedDict("SubscriptionInCondition", {"in": SubscriptionInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SubscriptionNotCondition = TypedDict("SubscriptionNotCondition", {"not": "SubscriptionCondition"}, total=False)
"""Negates the nested condition."""

SubscriptionAndCondition = TypedDict("SubscriptionAndCondition", {"and": "list[SubscriptionCondition]"}, total=False)
"""True if all nested conditions are true."""

SubscriptionOrCondition = TypedDict("SubscriptionOrCondition", {"or": "list[SubscriptionCondition]"}, total=False)
"""True if any nested condition is true."""

SubscriptionAnyCondition = TypedDict("SubscriptionAnyCondition", {"any": SubscriptionAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all subscription condition types
SubscriptionCondition = (
    SubscriptionEqCondition
    | SubscriptionNeqCondition
    | SubscriptionGtCondition
    | SubscriptionGteCondition
    | SubscriptionLtCondition
    | SubscriptionLteCondition
    | SubscriptionInCondition
    | SubscriptionLikeCondition
    | SubscriptionFuzzyCondition
    | SubscriptionKeywordCondition
    | SubscriptionContainsCondition
    | SubscriptionNotCondition
    | SubscriptionAndCondition
    | SubscriptionOrCondition
    | SubscriptionAnyCondition
)


class SubscriptionSearchQuery(TypedDict, total=False):
    """Search query for subscription entity."""
    filter: SubscriptionCondition
    sort: list[SubscriptionSortFilter]


# ===== CUSTOMER SEARCH TYPES =====

class CustomerSearchFilter(TypedDict, total=False):
    """Available fields for filtering customer search queries."""
    allow_direct_debit: bool | None
    """Indicates if direct debit is allowed for the customer."""
    auto_close_invoices: bool | None
    """Flag to automatically close invoices for the customer."""
    auto_collection: str | None
    """Configures the automatic collection settings for the customer."""
    backup_payment_source_id: str | None
    """ID of the backup payment source for the customer."""
    balances: list[Any] | None
    """Customer's balance information related to their account."""
    billing_address: dict[str, Any] | None
    """Customer's billing address details."""
    billing_date: int | None
    """Date for billing cycle."""
    billing_date_mode: str | None
    """Mode for billing date calculation."""
    billing_day_of_week: str | None
    """Day of the week for billing cycle."""
    billing_day_of_week_mode: str | None
    """Mode for billing day of the week calculation."""
    billing_month: int | None
    """Month for billing cycle."""
    business_customer_without_vat_number: bool | None
    """Flag indicating business customer without a VAT number."""
    business_entity_id: str | None
    """ID of the business entity."""
    card_status: str | None
    """Status of payment card associated with the customer."""
    channel: str | None
    """Channel through which the customer was acquired."""
    child_account_access: dict[str, Any] | None
    """Information regarding the access rights of child accounts linked to the customer's account."""
    client_profile_id: str | None
    """Client profile ID of the customer."""
    company: str | None
    """Company or organization name."""
    consolidated_invoicing: bool | None
    """Flag for consolidated invoicing setting."""
    contacts: list[Any] | None
    """List of contact details associated with the customer."""
    created_at: int | None
    """Date and time when the customer was created."""
    created_from_ip: str | None
    """IP address from which the customer was created."""
    custom_fields: list[Any] | None
    """"""
    customer_type: str | None
    """Type of customer (e.g., individual, business)."""
    deleted: bool | None
    """Flag indicating if the customer is deleted."""
    email: str | None
    """Email address of the customer."""
    entity_code: str | None
    """Code for the customer entity."""
    excess_payments: int | None
    """Total amount of excess payments by the customer."""
    exempt_number: str | None
    """Exemption number for tax purposes."""
    exemption_details: list[Any] | None
    """Details about any exemptions applicable to the customer's account."""
    first_name: str | None
    """First name of the customer."""
    fraud_flag: str | None
    """Flag indicating if fraud is associated with the customer."""
    id: str | None
    """Unique ID of the customer."""
    invoice_notes: str | None
    """Notes added to the customer's invoices."""
    is_location_valid: bool | None
    """Flag indicating if the customer location is valid."""
    last_name: str | None
    """Last name of the customer."""
    locale: str | None
    """Locale setting for the customer."""
    meta_data: dict[str, Any] | None
    """Additional metadata associated with the customer."""
    mrr: int | None
    """Monthly recurring revenue generated from the customer."""
    net_term_days: int | None
    """Number of days for net terms."""
    object_: str | None
    """Object type for the customer."""
    offline_payment_method: str | None
    """Offline payment method used by the customer."""
    parent_account_access: dict[str, Any] | None
    """Information regarding the access rights of the parent account, if applicable."""
    payment_method: dict[str, Any] | None
    """Customer's preferred payment method details."""
    phone: str | None
    """Phone number of the customer."""
    pii_cleared: str | None
    """Flag indicating if PII (Personally Identifiable Information) is cleared."""
    preferred_currency_code: str | None
    """Preferred currency code for transactions."""
    primary_payment_source_id: str | None
    """ID of the primary payment source for the customer."""
    promotional_credits: int | None
    """Total amount of promotional credits used."""
    referral_urls: list[Any] | None
    """List of referral URLs associated with the customer."""
    refundable_credits: int | None
    """Total amount of refundable credits."""
    registered_for_gst: bool | None
    """Flag indicating if the customer is registered for GST."""
    relationship: dict[str, Any] | None
    """Details about the relationship of the customer to other entities, if any."""
    resource_version: int | None
    """Version of the customer's resource."""
    tax_providers_fields: list[Any] | None
    """Fields related to tax providers."""
    taxability: str | None
    """Taxability status of the customer."""
    unbilled_charges: int | None
    """Total amount of unbilled charges."""
    updated_at: int | None
    """Date and time when the customer record was last updated."""
    use_default_hierarchy_settings: bool | None
    """Flag indicating if default hierarchy settings are used."""
    vat_number: str | None
    """VAT number associated with the customer."""
    vat_number_prefix: str | None
    """Prefix for the VAT number."""
    vat_number_status: str | None
    """Status of the VAT number validation."""
    vat_number_validated_time: int | None
    """Date and time when the VAT number was validated."""


class CustomerInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    allow_direct_debit: list[bool]
    """Indicates if direct debit is allowed for the customer."""
    auto_close_invoices: list[bool]
    """Flag to automatically close invoices for the customer."""
    auto_collection: list[str]
    """Configures the automatic collection settings for the customer."""
    backup_payment_source_id: list[str]
    """ID of the backup payment source for the customer."""
    balances: list[list[Any]]
    """Customer's balance information related to their account."""
    billing_address: list[dict[str, Any]]
    """Customer's billing address details."""
    billing_date: list[int]
    """Date for billing cycle."""
    billing_date_mode: list[str]
    """Mode for billing date calculation."""
    billing_day_of_week: list[str]
    """Day of the week for billing cycle."""
    billing_day_of_week_mode: list[str]
    """Mode for billing day of the week calculation."""
    billing_month: list[int]
    """Month for billing cycle."""
    business_customer_without_vat_number: list[bool]
    """Flag indicating business customer without a VAT number."""
    business_entity_id: list[str]
    """ID of the business entity."""
    card_status: list[str]
    """Status of payment card associated with the customer."""
    channel: list[str]
    """Channel through which the customer was acquired."""
    child_account_access: list[dict[str, Any]]
    """Information regarding the access rights of child accounts linked to the customer's account."""
    client_profile_id: list[str]
    """Client profile ID of the customer."""
    company: list[str]
    """Company or organization name."""
    consolidated_invoicing: list[bool]
    """Flag for consolidated invoicing setting."""
    contacts: list[list[Any]]
    """List of contact details associated with the customer."""
    created_at: list[int]
    """Date and time when the customer was created."""
    created_from_ip: list[str]
    """IP address from which the customer was created."""
    custom_fields: list[list[Any]]
    """"""
    customer_type: list[str]
    """Type of customer (e.g., individual, business)."""
    deleted: list[bool]
    """Flag indicating if the customer is deleted."""
    email: list[str]
    """Email address of the customer."""
    entity_code: list[str]
    """Code for the customer entity."""
    excess_payments: list[int]
    """Total amount of excess payments by the customer."""
    exempt_number: list[str]
    """Exemption number for tax purposes."""
    exemption_details: list[list[Any]]
    """Details about any exemptions applicable to the customer's account."""
    first_name: list[str]
    """First name of the customer."""
    fraud_flag: list[str]
    """Flag indicating if fraud is associated with the customer."""
    id: list[str]
    """Unique ID of the customer."""
    invoice_notes: list[str]
    """Notes added to the customer's invoices."""
    is_location_valid: list[bool]
    """Flag indicating if the customer location is valid."""
    last_name: list[str]
    """Last name of the customer."""
    locale: list[str]
    """Locale setting for the customer."""
    meta_data: list[dict[str, Any]]
    """Additional metadata associated with the customer."""
    mrr: list[int]
    """Monthly recurring revenue generated from the customer."""
    net_term_days: list[int]
    """Number of days for net terms."""
    object_: list[str]
    """Object type for the customer."""
    offline_payment_method: list[str]
    """Offline payment method used by the customer."""
    parent_account_access: list[dict[str, Any]]
    """Information regarding the access rights of the parent account, if applicable."""
    payment_method: list[dict[str, Any]]
    """Customer's preferred payment method details."""
    phone: list[str]
    """Phone number of the customer."""
    pii_cleared: list[str]
    """Flag indicating if PII (Personally Identifiable Information) is cleared."""
    preferred_currency_code: list[str]
    """Preferred currency code for transactions."""
    primary_payment_source_id: list[str]
    """ID of the primary payment source for the customer."""
    promotional_credits: list[int]
    """Total amount of promotional credits used."""
    referral_urls: list[list[Any]]
    """List of referral URLs associated with the customer."""
    refundable_credits: list[int]
    """Total amount of refundable credits."""
    registered_for_gst: list[bool]
    """Flag indicating if the customer is registered for GST."""
    relationship: list[dict[str, Any]]
    """Details about the relationship of the customer to other entities, if any."""
    resource_version: list[int]
    """Version of the customer's resource."""
    tax_providers_fields: list[list[Any]]
    """Fields related to tax providers."""
    taxability: list[str]
    """Taxability status of the customer."""
    unbilled_charges: list[int]
    """Total amount of unbilled charges."""
    updated_at: list[int]
    """Date and time when the customer record was last updated."""
    use_default_hierarchy_settings: list[bool]
    """Flag indicating if default hierarchy settings are used."""
    vat_number: list[str]
    """VAT number associated with the customer."""
    vat_number_prefix: list[str]
    """Prefix for the VAT number."""
    vat_number_status: list[str]
    """Status of the VAT number validation."""
    vat_number_validated_time: list[int]
    """Date and time when the VAT number was validated."""


class CustomerAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    allow_direct_debit: Any
    """Indicates if direct debit is allowed for the customer."""
    auto_close_invoices: Any
    """Flag to automatically close invoices for the customer."""
    auto_collection: Any
    """Configures the automatic collection settings for the customer."""
    backup_payment_source_id: Any
    """ID of the backup payment source for the customer."""
    balances: Any
    """Customer's balance information related to their account."""
    billing_address: Any
    """Customer's billing address details."""
    billing_date: Any
    """Date for billing cycle."""
    billing_date_mode: Any
    """Mode for billing date calculation."""
    billing_day_of_week: Any
    """Day of the week for billing cycle."""
    billing_day_of_week_mode: Any
    """Mode for billing day of the week calculation."""
    billing_month: Any
    """Month for billing cycle."""
    business_customer_without_vat_number: Any
    """Flag indicating business customer without a VAT number."""
    business_entity_id: Any
    """ID of the business entity."""
    card_status: Any
    """Status of payment card associated with the customer."""
    channel: Any
    """Channel through which the customer was acquired."""
    child_account_access: Any
    """Information regarding the access rights of child accounts linked to the customer's account."""
    client_profile_id: Any
    """Client profile ID of the customer."""
    company: Any
    """Company or organization name."""
    consolidated_invoicing: Any
    """Flag for consolidated invoicing setting."""
    contacts: Any
    """List of contact details associated with the customer."""
    created_at: Any
    """Date and time when the customer was created."""
    created_from_ip: Any
    """IP address from which the customer was created."""
    custom_fields: Any
    """"""
    customer_type: Any
    """Type of customer (e.g., individual, business)."""
    deleted: Any
    """Flag indicating if the customer is deleted."""
    email: Any
    """Email address of the customer."""
    entity_code: Any
    """Code for the customer entity."""
    excess_payments: Any
    """Total amount of excess payments by the customer."""
    exempt_number: Any
    """Exemption number for tax purposes."""
    exemption_details: Any
    """Details about any exemptions applicable to the customer's account."""
    first_name: Any
    """First name of the customer."""
    fraud_flag: Any
    """Flag indicating if fraud is associated with the customer."""
    id: Any
    """Unique ID of the customer."""
    invoice_notes: Any
    """Notes added to the customer's invoices."""
    is_location_valid: Any
    """Flag indicating if the customer location is valid."""
    last_name: Any
    """Last name of the customer."""
    locale: Any
    """Locale setting for the customer."""
    meta_data: Any
    """Additional metadata associated with the customer."""
    mrr: Any
    """Monthly recurring revenue generated from the customer."""
    net_term_days: Any
    """Number of days for net terms."""
    object_: Any
    """Object type for the customer."""
    offline_payment_method: Any
    """Offline payment method used by the customer."""
    parent_account_access: Any
    """Information regarding the access rights of the parent account, if applicable."""
    payment_method: Any
    """Customer's preferred payment method details."""
    phone: Any
    """Phone number of the customer."""
    pii_cleared: Any
    """Flag indicating if PII (Personally Identifiable Information) is cleared."""
    preferred_currency_code: Any
    """Preferred currency code for transactions."""
    primary_payment_source_id: Any
    """ID of the primary payment source for the customer."""
    promotional_credits: Any
    """Total amount of promotional credits used."""
    referral_urls: Any
    """List of referral URLs associated with the customer."""
    refundable_credits: Any
    """Total amount of refundable credits."""
    registered_for_gst: Any
    """Flag indicating if the customer is registered for GST."""
    relationship: Any
    """Details about the relationship of the customer to other entities, if any."""
    resource_version: Any
    """Version of the customer's resource."""
    tax_providers_fields: Any
    """Fields related to tax providers."""
    taxability: Any
    """Taxability status of the customer."""
    unbilled_charges: Any
    """Total amount of unbilled charges."""
    updated_at: Any
    """Date and time when the customer record was last updated."""
    use_default_hierarchy_settings: Any
    """Flag indicating if default hierarchy settings are used."""
    vat_number: Any
    """VAT number associated with the customer."""
    vat_number_prefix: Any
    """Prefix for the VAT number."""
    vat_number_status: Any
    """Status of the VAT number validation."""
    vat_number_validated_time: Any
    """Date and time when the VAT number was validated."""


class CustomerStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    allow_direct_debit: str
    """Indicates if direct debit is allowed for the customer."""
    auto_close_invoices: str
    """Flag to automatically close invoices for the customer."""
    auto_collection: str
    """Configures the automatic collection settings for the customer."""
    backup_payment_source_id: str
    """ID of the backup payment source for the customer."""
    balances: str
    """Customer's balance information related to their account."""
    billing_address: str
    """Customer's billing address details."""
    billing_date: str
    """Date for billing cycle."""
    billing_date_mode: str
    """Mode for billing date calculation."""
    billing_day_of_week: str
    """Day of the week for billing cycle."""
    billing_day_of_week_mode: str
    """Mode for billing day of the week calculation."""
    billing_month: str
    """Month for billing cycle."""
    business_customer_without_vat_number: str
    """Flag indicating business customer without a VAT number."""
    business_entity_id: str
    """ID of the business entity."""
    card_status: str
    """Status of payment card associated with the customer."""
    channel: str
    """Channel through which the customer was acquired."""
    child_account_access: str
    """Information regarding the access rights of child accounts linked to the customer's account."""
    client_profile_id: str
    """Client profile ID of the customer."""
    company: str
    """Company or organization name."""
    consolidated_invoicing: str
    """Flag for consolidated invoicing setting."""
    contacts: str
    """List of contact details associated with the customer."""
    created_at: str
    """Date and time when the customer was created."""
    created_from_ip: str
    """IP address from which the customer was created."""
    custom_fields: str
    """"""
    customer_type: str
    """Type of customer (e.g., individual, business)."""
    deleted: str
    """Flag indicating if the customer is deleted."""
    email: str
    """Email address of the customer."""
    entity_code: str
    """Code for the customer entity."""
    excess_payments: str
    """Total amount of excess payments by the customer."""
    exempt_number: str
    """Exemption number for tax purposes."""
    exemption_details: str
    """Details about any exemptions applicable to the customer's account."""
    first_name: str
    """First name of the customer."""
    fraud_flag: str
    """Flag indicating if fraud is associated with the customer."""
    id: str
    """Unique ID of the customer."""
    invoice_notes: str
    """Notes added to the customer's invoices."""
    is_location_valid: str
    """Flag indicating if the customer location is valid."""
    last_name: str
    """Last name of the customer."""
    locale: str
    """Locale setting for the customer."""
    meta_data: str
    """Additional metadata associated with the customer."""
    mrr: str
    """Monthly recurring revenue generated from the customer."""
    net_term_days: str
    """Number of days for net terms."""
    object_: str
    """Object type for the customer."""
    offline_payment_method: str
    """Offline payment method used by the customer."""
    parent_account_access: str
    """Information regarding the access rights of the parent account, if applicable."""
    payment_method: str
    """Customer's preferred payment method details."""
    phone: str
    """Phone number of the customer."""
    pii_cleared: str
    """Flag indicating if PII (Personally Identifiable Information) is cleared."""
    preferred_currency_code: str
    """Preferred currency code for transactions."""
    primary_payment_source_id: str
    """ID of the primary payment source for the customer."""
    promotional_credits: str
    """Total amount of promotional credits used."""
    referral_urls: str
    """List of referral URLs associated with the customer."""
    refundable_credits: str
    """Total amount of refundable credits."""
    registered_for_gst: str
    """Flag indicating if the customer is registered for GST."""
    relationship: str
    """Details about the relationship of the customer to other entities, if any."""
    resource_version: str
    """Version of the customer's resource."""
    tax_providers_fields: str
    """Fields related to tax providers."""
    taxability: str
    """Taxability status of the customer."""
    unbilled_charges: str
    """Total amount of unbilled charges."""
    updated_at: str
    """Date and time when the customer record was last updated."""
    use_default_hierarchy_settings: str
    """Flag indicating if default hierarchy settings are used."""
    vat_number: str
    """VAT number associated with the customer."""
    vat_number_prefix: str
    """Prefix for the VAT number."""
    vat_number_status: str
    """Status of the VAT number validation."""
    vat_number_validated_time: str
    """Date and time when the VAT number was validated."""


class CustomerSortFilter(TypedDict, total=False):
    """Available fields for sorting customer search results."""
    allow_direct_debit: AirbyteSortOrder
    """Indicates if direct debit is allowed for the customer."""
    auto_close_invoices: AirbyteSortOrder
    """Flag to automatically close invoices for the customer."""
    auto_collection: AirbyteSortOrder
    """Configures the automatic collection settings for the customer."""
    backup_payment_source_id: AirbyteSortOrder
    """ID of the backup payment source for the customer."""
    balances: AirbyteSortOrder
    """Customer's balance information related to their account."""
    billing_address: AirbyteSortOrder
    """Customer's billing address details."""
    billing_date: AirbyteSortOrder
    """Date for billing cycle."""
    billing_date_mode: AirbyteSortOrder
    """Mode for billing date calculation."""
    billing_day_of_week: AirbyteSortOrder
    """Day of the week for billing cycle."""
    billing_day_of_week_mode: AirbyteSortOrder
    """Mode for billing day of the week calculation."""
    billing_month: AirbyteSortOrder
    """Month for billing cycle."""
    business_customer_without_vat_number: AirbyteSortOrder
    """Flag indicating business customer without a VAT number."""
    business_entity_id: AirbyteSortOrder
    """ID of the business entity."""
    card_status: AirbyteSortOrder
    """Status of payment card associated with the customer."""
    channel: AirbyteSortOrder
    """Channel through which the customer was acquired."""
    child_account_access: AirbyteSortOrder
    """Information regarding the access rights of child accounts linked to the customer's account."""
    client_profile_id: AirbyteSortOrder
    """Client profile ID of the customer."""
    company: AirbyteSortOrder
    """Company or organization name."""
    consolidated_invoicing: AirbyteSortOrder
    """Flag for consolidated invoicing setting."""
    contacts: AirbyteSortOrder
    """List of contact details associated with the customer."""
    created_at: AirbyteSortOrder
    """Date and time when the customer was created."""
    created_from_ip: AirbyteSortOrder
    """IP address from which the customer was created."""
    custom_fields: AirbyteSortOrder
    """"""
    customer_type: AirbyteSortOrder
    """Type of customer (e.g., individual, business)."""
    deleted: AirbyteSortOrder
    """Flag indicating if the customer is deleted."""
    email: AirbyteSortOrder
    """Email address of the customer."""
    entity_code: AirbyteSortOrder
    """Code for the customer entity."""
    excess_payments: AirbyteSortOrder
    """Total amount of excess payments by the customer."""
    exempt_number: AirbyteSortOrder
    """Exemption number for tax purposes."""
    exemption_details: AirbyteSortOrder
    """Details about any exemptions applicable to the customer's account."""
    first_name: AirbyteSortOrder
    """First name of the customer."""
    fraud_flag: AirbyteSortOrder
    """Flag indicating if fraud is associated with the customer."""
    id: AirbyteSortOrder
    """Unique ID of the customer."""
    invoice_notes: AirbyteSortOrder
    """Notes added to the customer's invoices."""
    is_location_valid: AirbyteSortOrder
    """Flag indicating if the customer location is valid."""
    last_name: AirbyteSortOrder
    """Last name of the customer."""
    locale: AirbyteSortOrder
    """Locale setting for the customer."""
    meta_data: AirbyteSortOrder
    """Additional metadata associated with the customer."""
    mrr: AirbyteSortOrder
    """Monthly recurring revenue generated from the customer."""
    net_term_days: AirbyteSortOrder
    """Number of days for net terms."""
    object_: AirbyteSortOrder
    """Object type for the customer."""
    offline_payment_method: AirbyteSortOrder
    """Offline payment method used by the customer."""
    parent_account_access: AirbyteSortOrder
    """Information regarding the access rights of the parent account, if applicable."""
    payment_method: AirbyteSortOrder
    """Customer's preferred payment method details."""
    phone: AirbyteSortOrder
    """Phone number of the customer."""
    pii_cleared: AirbyteSortOrder
    """Flag indicating if PII (Personally Identifiable Information) is cleared."""
    preferred_currency_code: AirbyteSortOrder
    """Preferred currency code for transactions."""
    primary_payment_source_id: AirbyteSortOrder
    """ID of the primary payment source for the customer."""
    promotional_credits: AirbyteSortOrder
    """Total amount of promotional credits used."""
    referral_urls: AirbyteSortOrder
    """List of referral URLs associated with the customer."""
    refundable_credits: AirbyteSortOrder
    """Total amount of refundable credits."""
    registered_for_gst: AirbyteSortOrder
    """Flag indicating if the customer is registered for GST."""
    relationship: AirbyteSortOrder
    """Details about the relationship of the customer to other entities, if any."""
    resource_version: AirbyteSortOrder
    """Version of the customer's resource."""
    tax_providers_fields: AirbyteSortOrder
    """Fields related to tax providers."""
    taxability: AirbyteSortOrder
    """Taxability status of the customer."""
    unbilled_charges: AirbyteSortOrder
    """Total amount of unbilled charges."""
    updated_at: AirbyteSortOrder
    """Date and time when the customer record was last updated."""
    use_default_hierarchy_settings: AirbyteSortOrder
    """Flag indicating if default hierarchy settings are used."""
    vat_number: AirbyteSortOrder
    """VAT number associated with the customer."""
    vat_number_prefix: AirbyteSortOrder
    """Prefix for the VAT number."""
    vat_number_status: AirbyteSortOrder
    """Status of the VAT number validation."""
    vat_number_validated_time: AirbyteSortOrder
    """Date and time when the VAT number was validated."""


# Entity-specific condition types for customer
class CustomerEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomerSearchFilter


class CustomerNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomerSearchFilter


class CustomerGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomerSearchFilter


class CustomerGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomerSearchFilter


class CustomerLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomerSearchFilter


class CustomerLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomerSearchFilter


class CustomerLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomerStringFilter


class CustomerFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomerStringFilter


class CustomerKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomerStringFilter


class CustomerContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomerAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomerInCondition = TypedDict("CustomerInCondition", {"in": CustomerInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomerNotCondition = TypedDict("CustomerNotCondition", {"not": "CustomerCondition"}, total=False)
"""Negates the nested condition."""

CustomerAndCondition = TypedDict("CustomerAndCondition", {"and": "list[CustomerCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomerOrCondition = TypedDict("CustomerOrCondition", {"or": "list[CustomerCondition]"}, total=False)
"""True if any nested condition is true."""

CustomerAnyCondition = TypedDict("CustomerAnyCondition", {"any": CustomerAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all customer condition types
CustomerCondition = (
    CustomerEqCondition
    | CustomerNeqCondition
    | CustomerGtCondition
    | CustomerGteCondition
    | CustomerLtCondition
    | CustomerLteCondition
    | CustomerInCondition
    | CustomerLikeCondition
    | CustomerFuzzyCondition
    | CustomerKeywordCondition
    | CustomerContainsCondition
    | CustomerNotCondition
    | CustomerAndCondition
    | CustomerOrCondition
    | CustomerAnyCondition
)


class CustomerSearchQuery(TypedDict, total=False):
    """Search query for customer entity."""
    filter: CustomerCondition
    sort: list[CustomerSortFilter]


# ===== INVOICE SEARCH TYPES =====

class InvoiceSearchFilter(TypedDict, total=False):
    """Available fields for filtering invoice search queries."""
    adjustment_credit_notes: list[Any] | None
    """Details of adjustment credit notes applied to the invoice"""
    amount_adjusted: int | None
    """Total amount adjusted in the invoice"""
    amount_due: int | None
    """Amount due for payment"""
    amount_paid: int | None
    """Amount already paid"""
    amount_to_collect: int | None
    """Amount yet to be collected"""
    applied_credits: list[Any] | None
    """Details of credits applied to the invoice"""
    base_currency_code: str | None
    """Currency code used as base for the invoice"""
    billing_address: dict[str, Any] | None
    """Details of the billing address associated with the invoice"""
    business_entity_id: str | None
    """ID of the business entity"""
    channel: str | None
    """Channel through which the invoice was generated"""
    credits_applied: int | None
    """Total credits applied to the invoice"""
    currency_code: str | None
    """Currency code of the invoice"""
    custom_fields: list[Any] | None
    """"""
    customer_id: str | None
    """ID of the customer"""
    date: int | None
    """Date of the invoice"""
    deleted: bool | None
    """Flag indicating if the invoice is deleted"""
    discounts: list[Any] | None
    """Discount details applied to the invoice"""
    due_date: int | None
    """Due date for payment"""
    dunning_attempts: list[Any] | None
    """Details of dunning attempts made"""
    dunning_status: str | None
    """Status of dunning for the invoice"""
    einvoice: dict[str, Any] | None
    """Details of electronic invoice"""
    exchange_rate: float | None
    """Exchange rate used for currency conversion"""
    expected_payment_date: int | None
    """Expected date of payment"""
    first_invoice: bool | None
    """Flag indicating whether it's the first invoice"""
    generated_at: int | None
    """Date when the invoice was generated"""
    has_advance_charges: bool | None
    """Flag indicating if there are advance charges"""
    id: str | None
    """Unique ID of the invoice"""
    is_digital: bool | None
    """Flag indicating if the invoice is digital"""
    is_gifted: bool | None
    """Flag indicating if the invoice is gifted"""
    issued_credit_notes: list[Any] | None
    """Details of credit notes issued"""
    line_item_discounts: list[Any] | None
    """Details of line item discounts"""
    line_item_taxes: list[Any] | None
    """Tax details applied to each line item in the invoice"""
    line_item_tiers: list[Any] | None
    """Tiers information for each line item in the invoice"""
    line_items: list[Any] | None
    """Details of individual line items in the invoice"""
    linked_orders: list[Any] | None
    """Details of linked orders to the invoice"""
    linked_payments: list[Any] | None
    """Details of linked payments"""
    linked_taxes_withheld: list[Any] | None
    """Details of linked taxes withheld on the invoice"""
    local_currency_code: str | None
    """Local currency code of the invoice"""
    local_currency_exchange_rate: float | None
    """Exchange rate for local currency conversion"""
    net_term_days: int | None
    """Net term days for payment"""
    new_sales_amount: int | None
    """New sales amount in the invoice"""
    next_retry_at: int | None
    """Date of the next payment retry"""
    notes: list[Any] | None
    """Notes associated with the invoice"""
    object_: str | None
    """Type of object"""
    paid_at: int | None
    """Date when the invoice was paid"""
    payment_owner: str | None
    """Owner of the payment"""
    po_number: str | None
    """Purchase order number"""
    price_type: str | None
    """Type of pricing"""
    recurring: bool | None
    """Flag indicating if it's a recurring invoice"""
    resource_version: int | None
    """Resource version of the invoice"""
    round_off_amount: int | None
    """Amount rounded off"""
    shipping_address: dict[str, Any] | None
    """Details of the shipping address associated with the invoice"""
    statement_descriptor: dict[str, Any] | None
    """Descriptor for the statement"""
    status: str | None
    """Status of the invoice"""
    sub_total: int | None
    """Subtotal amount"""
    sub_total_in_local_currency: int | None
    """Subtotal amount in local currency"""
    subscription_id: str | None
    """ID of the subscription associated"""
    tax: int | None
    """Total tax amount"""
    tax_category: str | None
    """Tax category"""
    taxes: list[Any] | None
    """Details of taxes applied"""
    term_finalized: bool | None
    """Flag indicating if the term is finalized"""
    total: int | None
    """Total amount of the invoice"""
    total_in_local_currency: int | None
    """Total amount in local currency"""
    updated_at: int | None
    """Date of last update"""
    vat_number: str | None
    """VAT number"""
    vat_number_prefix: str | None
    """Prefix for the VAT number"""
    void_reason_code: str | None
    """Reason code for voiding the invoice"""
    voided_at: int | None
    """Date when the invoice was voided"""
    write_off_amount: int | None
    """Amount written off"""


class InvoiceInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    adjustment_credit_notes: list[list[Any]]
    """Details of adjustment credit notes applied to the invoice"""
    amount_adjusted: list[int]
    """Total amount adjusted in the invoice"""
    amount_due: list[int]
    """Amount due for payment"""
    amount_paid: list[int]
    """Amount already paid"""
    amount_to_collect: list[int]
    """Amount yet to be collected"""
    applied_credits: list[list[Any]]
    """Details of credits applied to the invoice"""
    base_currency_code: list[str]
    """Currency code used as base for the invoice"""
    billing_address: list[dict[str, Any]]
    """Details of the billing address associated with the invoice"""
    business_entity_id: list[str]
    """ID of the business entity"""
    channel: list[str]
    """Channel through which the invoice was generated"""
    credits_applied: list[int]
    """Total credits applied to the invoice"""
    currency_code: list[str]
    """Currency code of the invoice"""
    custom_fields: list[list[Any]]
    """"""
    customer_id: list[str]
    """ID of the customer"""
    date: list[int]
    """Date of the invoice"""
    deleted: list[bool]
    """Flag indicating if the invoice is deleted"""
    discounts: list[list[Any]]
    """Discount details applied to the invoice"""
    due_date: list[int]
    """Due date for payment"""
    dunning_attempts: list[list[Any]]
    """Details of dunning attempts made"""
    dunning_status: list[str]
    """Status of dunning for the invoice"""
    einvoice: list[dict[str, Any]]
    """Details of electronic invoice"""
    exchange_rate: list[float]
    """Exchange rate used for currency conversion"""
    expected_payment_date: list[int]
    """Expected date of payment"""
    first_invoice: list[bool]
    """Flag indicating whether it's the first invoice"""
    generated_at: list[int]
    """Date when the invoice was generated"""
    has_advance_charges: list[bool]
    """Flag indicating if there are advance charges"""
    id: list[str]
    """Unique ID of the invoice"""
    is_digital: list[bool]
    """Flag indicating if the invoice is digital"""
    is_gifted: list[bool]
    """Flag indicating if the invoice is gifted"""
    issued_credit_notes: list[list[Any]]
    """Details of credit notes issued"""
    line_item_discounts: list[list[Any]]
    """Details of line item discounts"""
    line_item_taxes: list[list[Any]]
    """Tax details applied to each line item in the invoice"""
    line_item_tiers: list[list[Any]]
    """Tiers information for each line item in the invoice"""
    line_items: list[list[Any]]
    """Details of individual line items in the invoice"""
    linked_orders: list[list[Any]]
    """Details of linked orders to the invoice"""
    linked_payments: list[list[Any]]
    """Details of linked payments"""
    linked_taxes_withheld: list[list[Any]]
    """Details of linked taxes withheld on the invoice"""
    local_currency_code: list[str]
    """Local currency code of the invoice"""
    local_currency_exchange_rate: list[float]
    """Exchange rate for local currency conversion"""
    net_term_days: list[int]
    """Net term days for payment"""
    new_sales_amount: list[int]
    """New sales amount in the invoice"""
    next_retry_at: list[int]
    """Date of the next payment retry"""
    notes: list[list[Any]]
    """Notes associated with the invoice"""
    object_: list[str]
    """Type of object"""
    paid_at: list[int]
    """Date when the invoice was paid"""
    payment_owner: list[str]
    """Owner of the payment"""
    po_number: list[str]
    """Purchase order number"""
    price_type: list[str]
    """Type of pricing"""
    recurring: list[bool]
    """Flag indicating if it's a recurring invoice"""
    resource_version: list[int]
    """Resource version of the invoice"""
    round_off_amount: list[int]
    """Amount rounded off"""
    shipping_address: list[dict[str, Any]]
    """Details of the shipping address associated with the invoice"""
    statement_descriptor: list[dict[str, Any]]
    """Descriptor for the statement"""
    status: list[str]
    """Status of the invoice"""
    sub_total: list[int]
    """Subtotal amount"""
    sub_total_in_local_currency: list[int]
    """Subtotal amount in local currency"""
    subscription_id: list[str]
    """ID of the subscription associated"""
    tax: list[int]
    """Total tax amount"""
    tax_category: list[str]
    """Tax category"""
    taxes: list[list[Any]]
    """Details of taxes applied"""
    term_finalized: list[bool]
    """Flag indicating if the term is finalized"""
    total: list[int]
    """Total amount of the invoice"""
    total_in_local_currency: list[int]
    """Total amount in local currency"""
    updated_at: list[int]
    """Date of last update"""
    vat_number: list[str]
    """VAT number"""
    vat_number_prefix: list[str]
    """Prefix for the VAT number"""
    void_reason_code: list[str]
    """Reason code for voiding the invoice"""
    voided_at: list[int]
    """Date when the invoice was voided"""
    write_off_amount: list[int]
    """Amount written off"""


class InvoiceAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    adjustment_credit_notes: Any
    """Details of adjustment credit notes applied to the invoice"""
    amount_adjusted: Any
    """Total amount adjusted in the invoice"""
    amount_due: Any
    """Amount due for payment"""
    amount_paid: Any
    """Amount already paid"""
    amount_to_collect: Any
    """Amount yet to be collected"""
    applied_credits: Any
    """Details of credits applied to the invoice"""
    base_currency_code: Any
    """Currency code used as base for the invoice"""
    billing_address: Any
    """Details of the billing address associated with the invoice"""
    business_entity_id: Any
    """ID of the business entity"""
    channel: Any
    """Channel through which the invoice was generated"""
    credits_applied: Any
    """Total credits applied to the invoice"""
    currency_code: Any
    """Currency code of the invoice"""
    custom_fields: Any
    """"""
    customer_id: Any
    """ID of the customer"""
    date: Any
    """Date of the invoice"""
    deleted: Any
    """Flag indicating if the invoice is deleted"""
    discounts: Any
    """Discount details applied to the invoice"""
    due_date: Any
    """Due date for payment"""
    dunning_attempts: Any
    """Details of dunning attempts made"""
    dunning_status: Any
    """Status of dunning for the invoice"""
    einvoice: Any
    """Details of electronic invoice"""
    exchange_rate: Any
    """Exchange rate used for currency conversion"""
    expected_payment_date: Any
    """Expected date of payment"""
    first_invoice: Any
    """Flag indicating whether it's the first invoice"""
    generated_at: Any
    """Date when the invoice was generated"""
    has_advance_charges: Any
    """Flag indicating if there are advance charges"""
    id: Any
    """Unique ID of the invoice"""
    is_digital: Any
    """Flag indicating if the invoice is digital"""
    is_gifted: Any
    """Flag indicating if the invoice is gifted"""
    issued_credit_notes: Any
    """Details of credit notes issued"""
    line_item_discounts: Any
    """Details of line item discounts"""
    line_item_taxes: Any
    """Tax details applied to each line item in the invoice"""
    line_item_tiers: Any
    """Tiers information for each line item in the invoice"""
    line_items: Any
    """Details of individual line items in the invoice"""
    linked_orders: Any
    """Details of linked orders to the invoice"""
    linked_payments: Any
    """Details of linked payments"""
    linked_taxes_withheld: Any
    """Details of linked taxes withheld on the invoice"""
    local_currency_code: Any
    """Local currency code of the invoice"""
    local_currency_exchange_rate: Any
    """Exchange rate for local currency conversion"""
    net_term_days: Any
    """Net term days for payment"""
    new_sales_amount: Any
    """New sales amount in the invoice"""
    next_retry_at: Any
    """Date of the next payment retry"""
    notes: Any
    """Notes associated with the invoice"""
    object_: Any
    """Type of object"""
    paid_at: Any
    """Date when the invoice was paid"""
    payment_owner: Any
    """Owner of the payment"""
    po_number: Any
    """Purchase order number"""
    price_type: Any
    """Type of pricing"""
    recurring: Any
    """Flag indicating if it's a recurring invoice"""
    resource_version: Any
    """Resource version of the invoice"""
    round_off_amount: Any
    """Amount rounded off"""
    shipping_address: Any
    """Details of the shipping address associated with the invoice"""
    statement_descriptor: Any
    """Descriptor for the statement"""
    status: Any
    """Status of the invoice"""
    sub_total: Any
    """Subtotal amount"""
    sub_total_in_local_currency: Any
    """Subtotal amount in local currency"""
    subscription_id: Any
    """ID of the subscription associated"""
    tax: Any
    """Total tax amount"""
    tax_category: Any
    """Tax category"""
    taxes: Any
    """Details of taxes applied"""
    term_finalized: Any
    """Flag indicating if the term is finalized"""
    total: Any
    """Total amount of the invoice"""
    total_in_local_currency: Any
    """Total amount in local currency"""
    updated_at: Any
    """Date of last update"""
    vat_number: Any
    """VAT number"""
    vat_number_prefix: Any
    """Prefix for the VAT number"""
    void_reason_code: Any
    """Reason code for voiding the invoice"""
    voided_at: Any
    """Date when the invoice was voided"""
    write_off_amount: Any
    """Amount written off"""


class InvoiceStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    adjustment_credit_notes: str
    """Details of adjustment credit notes applied to the invoice"""
    amount_adjusted: str
    """Total amount adjusted in the invoice"""
    amount_due: str
    """Amount due for payment"""
    amount_paid: str
    """Amount already paid"""
    amount_to_collect: str
    """Amount yet to be collected"""
    applied_credits: str
    """Details of credits applied to the invoice"""
    base_currency_code: str
    """Currency code used as base for the invoice"""
    billing_address: str
    """Details of the billing address associated with the invoice"""
    business_entity_id: str
    """ID of the business entity"""
    channel: str
    """Channel through which the invoice was generated"""
    credits_applied: str
    """Total credits applied to the invoice"""
    currency_code: str
    """Currency code of the invoice"""
    custom_fields: str
    """"""
    customer_id: str
    """ID of the customer"""
    date: str
    """Date of the invoice"""
    deleted: str
    """Flag indicating if the invoice is deleted"""
    discounts: str
    """Discount details applied to the invoice"""
    due_date: str
    """Due date for payment"""
    dunning_attempts: str
    """Details of dunning attempts made"""
    dunning_status: str
    """Status of dunning for the invoice"""
    einvoice: str
    """Details of electronic invoice"""
    exchange_rate: str
    """Exchange rate used for currency conversion"""
    expected_payment_date: str
    """Expected date of payment"""
    first_invoice: str
    """Flag indicating whether it's the first invoice"""
    generated_at: str
    """Date when the invoice was generated"""
    has_advance_charges: str
    """Flag indicating if there are advance charges"""
    id: str
    """Unique ID of the invoice"""
    is_digital: str
    """Flag indicating if the invoice is digital"""
    is_gifted: str
    """Flag indicating if the invoice is gifted"""
    issued_credit_notes: str
    """Details of credit notes issued"""
    line_item_discounts: str
    """Details of line item discounts"""
    line_item_taxes: str
    """Tax details applied to each line item in the invoice"""
    line_item_tiers: str
    """Tiers information for each line item in the invoice"""
    line_items: str
    """Details of individual line items in the invoice"""
    linked_orders: str
    """Details of linked orders to the invoice"""
    linked_payments: str
    """Details of linked payments"""
    linked_taxes_withheld: str
    """Details of linked taxes withheld on the invoice"""
    local_currency_code: str
    """Local currency code of the invoice"""
    local_currency_exchange_rate: str
    """Exchange rate for local currency conversion"""
    net_term_days: str
    """Net term days for payment"""
    new_sales_amount: str
    """New sales amount in the invoice"""
    next_retry_at: str
    """Date of the next payment retry"""
    notes: str
    """Notes associated with the invoice"""
    object_: str
    """Type of object"""
    paid_at: str
    """Date when the invoice was paid"""
    payment_owner: str
    """Owner of the payment"""
    po_number: str
    """Purchase order number"""
    price_type: str
    """Type of pricing"""
    recurring: str
    """Flag indicating if it's a recurring invoice"""
    resource_version: str
    """Resource version of the invoice"""
    round_off_amount: str
    """Amount rounded off"""
    shipping_address: str
    """Details of the shipping address associated with the invoice"""
    statement_descriptor: str
    """Descriptor for the statement"""
    status: str
    """Status of the invoice"""
    sub_total: str
    """Subtotal amount"""
    sub_total_in_local_currency: str
    """Subtotal amount in local currency"""
    subscription_id: str
    """ID of the subscription associated"""
    tax: str
    """Total tax amount"""
    tax_category: str
    """Tax category"""
    taxes: str
    """Details of taxes applied"""
    term_finalized: str
    """Flag indicating if the term is finalized"""
    total: str
    """Total amount of the invoice"""
    total_in_local_currency: str
    """Total amount in local currency"""
    updated_at: str
    """Date of last update"""
    vat_number: str
    """VAT number"""
    vat_number_prefix: str
    """Prefix for the VAT number"""
    void_reason_code: str
    """Reason code for voiding the invoice"""
    voided_at: str
    """Date when the invoice was voided"""
    write_off_amount: str
    """Amount written off"""


class InvoiceSortFilter(TypedDict, total=False):
    """Available fields for sorting invoice search results."""
    adjustment_credit_notes: AirbyteSortOrder
    """Details of adjustment credit notes applied to the invoice"""
    amount_adjusted: AirbyteSortOrder
    """Total amount adjusted in the invoice"""
    amount_due: AirbyteSortOrder
    """Amount due for payment"""
    amount_paid: AirbyteSortOrder
    """Amount already paid"""
    amount_to_collect: AirbyteSortOrder
    """Amount yet to be collected"""
    applied_credits: AirbyteSortOrder
    """Details of credits applied to the invoice"""
    base_currency_code: AirbyteSortOrder
    """Currency code used as base for the invoice"""
    billing_address: AirbyteSortOrder
    """Details of the billing address associated with the invoice"""
    business_entity_id: AirbyteSortOrder
    """ID of the business entity"""
    channel: AirbyteSortOrder
    """Channel through which the invoice was generated"""
    credits_applied: AirbyteSortOrder
    """Total credits applied to the invoice"""
    currency_code: AirbyteSortOrder
    """Currency code of the invoice"""
    custom_fields: AirbyteSortOrder
    """"""
    customer_id: AirbyteSortOrder
    """ID of the customer"""
    date: AirbyteSortOrder
    """Date of the invoice"""
    deleted: AirbyteSortOrder
    """Flag indicating if the invoice is deleted"""
    discounts: AirbyteSortOrder
    """Discount details applied to the invoice"""
    due_date: AirbyteSortOrder
    """Due date for payment"""
    dunning_attempts: AirbyteSortOrder
    """Details of dunning attempts made"""
    dunning_status: AirbyteSortOrder
    """Status of dunning for the invoice"""
    einvoice: AirbyteSortOrder
    """Details of electronic invoice"""
    exchange_rate: AirbyteSortOrder
    """Exchange rate used for currency conversion"""
    expected_payment_date: AirbyteSortOrder
    """Expected date of payment"""
    first_invoice: AirbyteSortOrder
    """Flag indicating whether it's the first invoice"""
    generated_at: AirbyteSortOrder
    """Date when the invoice was generated"""
    has_advance_charges: AirbyteSortOrder
    """Flag indicating if there are advance charges"""
    id: AirbyteSortOrder
    """Unique ID of the invoice"""
    is_digital: AirbyteSortOrder
    """Flag indicating if the invoice is digital"""
    is_gifted: AirbyteSortOrder
    """Flag indicating if the invoice is gifted"""
    issued_credit_notes: AirbyteSortOrder
    """Details of credit notes issued"""
    line_item_discounts: AirbyteSortOrder
    """Details of line item discounts"""
    line_item_taxes: AirbyteSortOrder
    """Tax details applied to each line item in the invoice"""
    line_item_tiers: AirbyteSortOrder
    """Tiers information for each line item in the invoice"""
    line_items: AirbyteSortOrder
    """Details of individual line items in the invoice"""
    linked_orders: AirbyteSortOrder
    """Details of linked orders to the invoice"""
    linked_payments: AirbyteSortOrder
    """Details of linked payments"""
    linked_taxes_withheld: AirbyteSortOrder
    """Details of linked taxes withheld on the invoice"""
    local_currency_code: AirbyteSortOrder
    """Local currency code of the invoice"""
    local_currency_exchange_rate: AirbyteSortOrder
    """Exchange rate for local currency conversion"""
    net_term_days: AirbyteSortOrder
    """Net term days for payment"""
    new_sales_amount: AirbyteSortOrder
    """New sales amount in the invoice"""
    next_retry_at: AirbyteSortOrder
    """Date of the next payment retry"""
    notes: AirbyteSortOrder
    """Notes associated with the invoice"""
    object_: AirbyteSortOrder
    """Type of object"""
    paid_at: AirbyteSortOrder
    """Date when the invoice was paid"""
    payment_owner: AirbyteSortOrder
    """Owner of the payment"""
    po_number: AirbyteSortOrder
    """Purchase order number"""
    price_type: AirbyteSortOrder
    """Type of pricing"""
    recurring: AirbyteSortOrder
    """Flag indicating if it's a recurring invoice"""
    resource_version: AirbyteSortOrder
    """Resource version of the invoice"""
    round_off_amount: AirbyteSortOrder
    """Amount rounded off"""
    shipping_address: AirbyteSortOrder
    """Details of the shipping address associated with the invoice"""
    statement_descriptor: AirbyteSortOrder
    """Descriptor for the statement"""
    status: AirbyteSortOrder
    """Status of the invoice"""
    sub_total: AirbyteSortOrder
    """Subtotal amount"""
    sub_total_in_local_currency: AirbyteSortOrder
    """Subtotal amount in local currency"""
    subscription_id: AirbyteSortOrder
    """ID of the subscription associated"""
    tax: AirbyteSortOrder
    """Total tax amount"""
    tax_category: AirbyteSortOrder
    """Tax category"""
    taxes: AirbyteSortOrder
    """Details of taxes applied"""
    term_finalized: AirbyteSortOrder
    """Flag indicating if the term is finalized"""
    total: AirbyteSortOrder
    """Total amount of the invoice"""
    total_in_local_currency: AirbyteSortOrder
    """Total amount in local currency"""
    updated_at: AirbyteSortOrder
    """Date of last update"""
    vat_number: AirbyteSortOrder
    """VAT number"""
    vat_number_prefix: AirbyteSortOrder
    """Prefix for the VAT number"""
    void_reason_code: AirbyteSortOrder
    """Reason code for voiding the invoice"""
    voided_at: AirbyteSortOrder
    """Date when the invoice was voided"""
    write_off_amount: AirbyteSortOrder
    """Amount written off"""


# Entity-specific condition types for invoice
class InvoiceEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InvoiceSearchFilter


class InvoiceNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InvoiceSearchFilter


class InvoiceGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InvoiceSearchFilter


class InvoiceGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InvoiceSearchFilter


class InvoiceLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InvoiceSearchFilter


class InvoiceLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InvoiceSearchFilter


class InvoiceLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InvoiceStringFilter


class InvoiceFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InvoiceStringFilter


class InvoiceKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InvoiceStringFilter


class InvoiceContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InvoiceAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InvoiceInCondition = TypedDict("InvoiceInCondition", {"in": InvoiceInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InvoiceNotCondition = TypedDict("InvoiceNotCondition", {"not": "InvoiceCondition"}, total=False)
"""Negates the nested condition."""

InvoiceAndCondition = TypedDict("InvoiceAndCondition", {"and": "list[InvoiceCondition]"}, total=False)
"""True if all nested conditions are true."""

InvoiceOrCondition = TypedDict("InvoiceOrCondition", {"or": "list[InvoiceCondition]"}, total=False)
"""True if any nested condition is true."""

InvoiceAnyCondition = TypedDict("InvoiceAnyCondition", {"any": InvoiceAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all invoice condition types
InvoiceCondition = (
    InvoiceEqCondition
    | InvoiceNeqCondition
    | InvoiceGtCondition
    | InvoiceGteCondition
    | InvoiceLtCondition
    | InvoiceLteCondition
    | InvoiceInCondition
    | InvoiceLikeCondition
    | InvoiceFuzzyCondition
    | InvoiceKeywordCondition
    | InvoiceContainsCondition
    | InvoiceNotCondition
    | InvoiceAndCondition
    | InvoiceOrCondition
    | InvoiceAnyCondition
)


class InvoiceSearchQuery(TypedDict, total=False):
    """Search query for invoice entity."""
    filter: InvoiceCondition
    sort: list[InvoiceSortFilter]


# ===== CREDIT_NOTE SEARCH TYPES =====

class CreditNoteSearchFilter(TypedDict, total=False):
    """Available fields for filtering credit_note search queries."""
    allocations: list[Any] | None
    """Details of allocations associated with the credit note"""
    amount_allocated: int | None
    """The amount of credits allocated."""
    amount_available: int | None
    """The amount of credits available."""
    amount_refunded: int | None
    """The amount of credits refunded."""
    base_currency_code: str | None
    """The base currency code for the credit note."""
    billing_address: dict[str, Any] | None
    """Details of the billing address associated with the credit note"""
    business_entity_id: str | None
    """The ID of the business entity associated with the credit note."""
    channel: str | None
    """The channel through which the credit note was created."""
    create_reason_code: str | None
    """The reason code for creating the credit note."""
    currency_code: str | None
    """The currency code for the credit note."""
    custom_fields: list[Any] | None
    """"""
    customer_id: str | None
    """The ID of the customer associated with the credit note."""
    customer_notes: str | None
    """Notes provided by the customer for the credit note."""
    date: int | None
    """The date when the credit note was created."""
    deleted: bool | None
    """Indicates if the credit note has been deleted."""
    discounts: list[Any] | None
    """Details of discounts applied to the credit note"""
    exchange_rate: float | None
    """The exchange rate used for currency conversion."""
    fractional_correction: int | None
    """Fractional correction for rounding off decimals."""
    generated_at: int | None
    """The date when the credit note was generated."""
    id: str | None
    """The unique identifier for the credit note."""
    is_digital: bool | None
    """Indicates if the credit note is in digital format."""
    is_vat_moss_registered: bool | None
    """Indicates if VAT MOSS registration applies."""
    line_item_discounts: list[Any] | None
    """Details of discounts applied at the line item level in the credit note"""
    line_item_taxes: list[Any] | None
    """Details of taxes applied at the line item level in the credit note"""
    line_item_tiers: list[Any] | None
    """Details of tiers applied to line items in the credit note"""
    line_items: list[Any] | None
    """Details of line items in the credit note"""
    linked_refunds: list[Any] | None
    """Details of linked refunds to the credit note"""
    linked_tax_withheld_refunds: list[Any] | None
    """Details of linked tax withheld refunds to the credit note"""
    local_currency_code: str | None
    """The local currency code for the credit note."""
    object_: str | None
    """The object type of the credit note."""
    price_type: str | None
    """The type of pricing used for the credit note."""
    reason_code: str | None
    """The reason code for creating the credit note."""
    reference_invoice_id: str | None
    """The ID of the invoice this credit note references."""
    refunded_at: int | None
    """The date when the credit note was refunded."""
    resource_version: int | None
    """The version of the credit note resource."""
    round_off_amount: int | None
    """Amount rounded off for currency conversions."""
    shipping_address: dict[str, Any] | None
    """Details of the shipping address associated with the credit note"""
    status: str | None
    """The status of the credit note."""
    sub_total: int | None
    """The subtotal amount of the credit note."""
    sub_total_in_local_currency: int | None
    """The subtotal amount in local currency."""
    subscription_id: str | None
    """The ID of the subscription associated with the credit note."""
    taxes: list[Any] | None
    """List of taxes applied to the credit note"""
    total: int | None
    """The total amount of the credit note."""
    total_in_local_currency: int | None
    """The total amount in local currency."""
    type_: str | None
    """The type of credit note."""
    updated_at: int | None
    """The date when the credit note was last updated."""
    vat_number: str | None
    """VAT number associated with the credit note."""
    vat_number_prefix: str | None
    """Prefix for the VAT number."""
    voided_at: int | None
    """The date when the credit note was voided."""


class CreditNoteInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    allocations: list[list[Any]]
    """Details of allocations associated with the credit note"""
    amount_allocated: list[int]
    """The amount of credits allocated."""
    amount_available: list[int]
    """The amount of credits available."""
    amount_refunded: list[int]
    """The amount of credits refunded."""
    base_currency_code: list[str]
    """The base currency code for the credit note."""
    billing_address: list[dict[str, Any]]
    """Details of the billing address associated with the credit note"""
    business_entity_id: list[str]
    """The ID of the business entity associated with the credit note."""
    channel: list[str]
    """The channel through which the credit note was created."""
    create_reason_code: list[str]
    """The reason code for creating the credit note."""
    currency_code: list[str]
    """The currency code for the credit note."""
    custom_fields: list[list[Any]]
    """"""
    customer_id: list[str]
    """The ID of the customer associated with the credit note."""
    customer_notes: list[str]
    """Notes provided by the customer for the credit note."""
    date: list[int]
    """The date when the credit note was created."""
    deleted: list[bool]
    """Indicates if the credit note has been deleted."""
    discounts: list[list[Any]]
    """Details of discounts applied to the credit note"""
    exchange_rate: list[float]
    """The exchange rate used for currency conversion."""
    fractional_correction: list[int]
    """Fractional correction for rounding off decimals."""
    generated_at: list[int]
    """The date when the credit note was generated."""
    id: list[str]
    """The unique identifier for the credit note."""
    is_digital: list[bool]
    """Indicates if the credit note is in digital format."""
    is_vat_moss_registered: list[bool]
    """Indicates if VAT MOSS registration applies."""
    line_item_discounts: list[list[Any]]
    """Details of discounts applied at the line item level in the credit note"""
    line_item_taxes: list[list[Any]]
    """Details of taxes applied at the line item level in the credit note"""
    line_item_tiers: list[list[Any]]
    """Details of tiers applied to line items in the credit note"""
    line_items: list[list[Any]]
    """Details of line items in the credit note"""
    linked_refunds: list[list[Any]]
    """Details of linked refunds to the credit note"""
    linked_tax_withheld_refunds: list[list[Any]]
    """Details of linked tax withheld refunds to the credit note"""
    local_currency_code: list[str]
    """The local currency code for the credit note."""
    object_: list[str]
    """The object type of the credit note."""
    price_type: list[str]
    """The type of pricing used for the credit note."""
    reason_code: list[str]
    """The reason code for creating the credit note."""
    reference_invoice_id: list[str]
    """The ID of the invoice this credit note references."""
    refunded_at: list[int]
    """The date when the credit note was refunded."""
    resource_version: list[int]
    """The version of the credit note resource."""
    round_off_amount: list[int]
    """Amount rounded off for currency conversions."""
    shipping_address: list[dict[str, Any]]
    """Details of the shipping address associated with the credit note"""
    status: list[str]
    """The status of the credit note."""
    sub_total: list[int]
    """The subtotal amount of the credit note."""
    sub_total_in_local_currency: list[int]
    """The subtotal amount in local currency."""
    subscription_id: list[str]
    """The ID of the subscription associated with the credit note."""
    taxes: list[list[Any]]
    """List of taxes applied to the credit note"""
    total: list[int]
    """The total amount of the credit note."""
    total_in_local_currency: list[int]
    """The total amount in local currency."""
    type_: list[str]
    """The type of credit note."""
    updated_at: list[int]
    """The date when the credit note was last updated."""
    vat_number: list[str]
    """VAT number associated with the credit note."""
    vat_number_prefix: list[str]
    """Prefix for the VAT number."""
    voided_at: list[int]
    """The date when the credit note was voided."""


class CreditNoteAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    allocations: Any
    """Details of allocations associated with the credit note"""
    amount_allocated: Any
    """The amount of credits allocated."""
    amount_available: Any
    """The amount of credits available."""
    amount_refunded: Any
    """The amount of credits refunded."""
    base_currency_code: Any
    """The base currency code for the credit note."""
    billing_address: Any
    """Details of the billing address associated with the credit note"""
    business_entity_id: Any
    """The ID of the business entity associated with the credit note."""
    channel: Any
    """The channel through which the credit note was created."""
    create_reason_code: Any
    """The reason code for creating the credit note."""
    currency_code: Any
    """The currency code for the credit note."""
    custom_fields: Any
    """"""
    customer_id: Any
    """The ID of the customer associated with the credit note."""
    customer_notes: Any
    """Notes provided by the customer for the credit note."""
    date: Any
    """The date when the credit note was created."""
    deleted: Any
    """Indicates if the credit note has been deleted."""
    discounts: Any
    """Details of discounts applied to the credit note"""
    exchange_rate: Any
    """The exchange rate used for currency conversion."""
    fractional_correction: Any
    """Fractional correction for rounding off decimals."""
    generated_at: Any
    """The date when the credit note was generated."""
    id: Any
    """The unique identifier for the credit note."""
    is_digital: Any
    """Indicates if the credit note is in digital format."""
    is_vat_moss_registered: Any
    """Indicates if VAT MOSS registration applies."""
    line_item_discounts: Any
    """Details of discounts applied at the line item level in the credit note"""
    line_item_taxes: Any
    """Details of taxes applied at the line item level in the credit note"""
    line_item_tiers: Any
    """Details of tiers applied to line items in the credit note"""
    line_items: Any
    """Details of line items in the credit note"""
    linked_refunds: Any
    """Details of linked refunds to the credit note"""
    linked_tax_withheld_refunds: Any
    """Details of linked tax withheld refunds to the credit note"""
    local_currency_code: Any
    """The local currency code for the credit note."""
    object_: Any
    """The object type of the credit note."""
    price_type: Any
    """The type of pricing used for the credit note."""
    reason_code: Any
    """The reason code for creating the credit note."""
    reference_invoice_id: Any
    """The ID of the invoice this credit note references."""
    refunded_at: Any
    """The date when the credit note was refunded."""
    resource_version: Any
    """The version of the credit note resource."""
    round_off_amount: Any
    """Amount rounded off for currency conversions."""
    shipping_address: Any
    """Details of the shipping address associated with the credit note"""
    status: Any
    """The status of the credit note."""
    sub_total: Any
    """The subtotal amount of the credit note."""
    sub_total_in_local_currency: Any
    """The subtotal amount in local currency."""
    subscription_id: Any
    """The ID of the subscription associated with the credit note."""
    taxes: Any
    """List of taxes applied to the credit note"""
    total: Any
    """The total amount of the credit note."""
    total_in_local_currency: Any
    """The total amount in local currency."""
    type_: Any
    """The type of credit note."""
    updated_at: Any
    """The date when the credit note was last updated."""
    vat_number: Any
    """VAT number associated with the credit note."""
    vat_number_prefix: Any
    """Prefix for the VAT number."""
    voided_at: Any
    """The date when the credit note was voided."""


class CreditNoteStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    allocations: str
    """Details of allocations associated with the credit note"""
    amount_allocated: str
    """The amount of credits allocated."""
    amount_available: str
    """The amount of credits available."""
    amount_refunded: str
    """The amount of credits refunded."""
    base_currency_code: str
    """The base currency code for the credit note."""
    billing_address: str
    """Details of the billing address associated with the credit note"""
    business_entity_id: str
    """The ID of the business entity associated with the credit note."""
    channel: str
    """The channel through which the credit note was created."""
    create_reason_code: str
    """The reason code for creating the credit note."""
    currency_code: str
    """The currency code for the credit note."""
    custom_fields: str
    """"""
    customer_id: str
    """The ID of the customer associated with the credit note."""
    customer_notes: str
    """Notes provided by the customer for the credit note."""
    date: str
    """The date when the credit note was created."""
    deleted: str
    """Indicates if the credit note has been deleted."""
    discounts: str
    """Details of discounts applied to the credit note"""
    exchange_rate: str
    """The exchange rate used for currency conversion."""
    fractional_correction: str
    """Fractional correction for rounding off decimals."""
    generated_at: str
    """The date when the credit note was generated."""
    id: str
    """The unique identifier for the credit note."""
    is_digital: str
    """Indicates if the credit note is in digital format."""
    is_vat_moss_registered: str
    """Indicates if VAT MOSS registration applies."""
    line_item_discounts: str
    """Details of discounts applied at the line item level in the credit note"""
    line_item_taxes: str
    """Details of taxes applied at the line item level in the credit note"""
    line_item_tiers: str
    """Details of tiers applied to line items in the credit note"""
    line_items: str
    """Details of line items in the credit note"""
    linked_refunds: str
    """Details of linked refunds to the credit note"""
    linked_tax_withheld_refunds: str
    """Details of linked tax withheld refunds to the credit note"""
    local_currency_code: str
    """The local currency code for the credit note."""
    object_: str
    """The object type of the credit note."""
    price_type: str
    """The type of pricing used for the credit note."""
    reason_code: str
    """The reason code for creating the credit note."""
    reference_invoice_id: str
    """The ID of the invoice this credit note references."""
    refunded_at: str
    """The date when the credit note was refunded."""
    resource_version: str
    """The version of the credit note resource."""
    round_off_amount: str
    """Amount rounded off for currency conversions."""
    shipping_address: str
    """Details of the shipping address associated with the credit note"""
    status: str
    """The status of the credit note."""
    sub_total: str
    """The subtotal amount of the credit note."""
    sub_total_in_local_currency: str
    """The subtotal amount in local currency."""
    subscription_id: str
    """The ID of the subscription associated with the credit note."""
    taxes: str
    """List of taxes applied to the credit note"""
    total: str
    """The total amount of the credit note."""
    total_in_local_currency: str
    """The total amount in local currency."""
    type_: str
    """The type of credit note."""
    updated_at: str
    """The date when the credit note was last updated."""
    vat_number: str
    """VAT number associated with the credit note."""
    vat_number_prefix: str
    """Prefix for the VAT number."""
    voided_at: str
    """The date when the credit note was voided."""


class CreditNoteSortFilter(TypedDict, total=False):
    """Available fields for sorting credit_note search results."""
    allocations: AirbyteSortOrder
    """Details of allocations associated with the credit note"""
    amount_allocated: AirbyteSortOrder
    """The amount of credits allocated."""
    amount_available: AirbyteSortOrder
    """The amount of credits available."""
    amount_refunded: AirbyteSortOrder
    """The amount of credits refunded."""
    base_currency_code: AirbyteSortOrder
    """The base currency code for the credit note."""
    billing_address: AirbyteSortOrder
    """Details of the billing address associated with the credit note"""
    business_entity_id: AirbyteSortOrder
    """The ID of the business entity associated with the credit note."""
    channel: AirbyteSortOrder
    """The channel through which the credit note was created."""
    create_reason_code: AirbyteSortOrder
    """The reason code for creating the credit note."""
    currency_code: AirbyteSortOrder
    """The currency code for the credit note."""
    custom_fields: AirbyteSortOrder
    """"""
    customer_id: AirbyteSortOrder
    """The ID of the customer associated with the credit note."""
    customer_notes: AirbyteSortOrder
    """Notes provided by the customer for the credit note."""
    date: AirbyteSortOrder
    """The date when the credit note was created."""
    deleted: AirbyteSortOrder
    """Indicates if the credit note has been deleted."""
    discounts: AirbyteSortOrder
    """Details of discounts applied to the credit note"""
    exchange_rate: AirbyteSortOrder
    """The exchange rate used for currency conversion."""
    fractional_correction: AirbyteSortOrder
    """Fractional correction for rounding off decimals."""
    generated_at: AirbyteSortOrder
    """The date when the credit note was generated."""
    id: AirbyteSortOrder
    """The unique identifier for the credit note."""
    is_digital: AirbyteSortOrder
    """Indicates if the credit note is in digital format."""
    is_vat_moss_registered: AirbyteSortOrder
    """Indicates if VAT MOSS registration applies."""
    line_item_discounts: AirbyteSortOrder
    """Details of discounts applied at the line item level in the credit note"""
    line_item_taxes: AirbyteSortOrder
    """Details of taxes applied at the line item level in the credit note"""
    line_item_tiers: AirbyteSortOrder
    """Details of tiers applied to line items in the credit note"""
    line_items: AirbyteSortOrder
    """Details of line items in the credit note"""
    linked_refunds: AirbyteSortOrder
    """Details of linked refunds to the credit note"""
    linked_tax_withheld_refunds: AirbyteSortOrder
    """Details of linked tax withheld refunds to the credit note"""
    local_currency_code: AirbyteSortOrder
    """The local currency code for the credit note."""
    object_: AirbyteSortOrder
    """The object type of the credit note."""
    price_type: AirbyteSortOrder
    """The type of pricing used for the credit note."""
    reason_code: AirbyteSortOrder
    """The reason code for creating the credit note."""
    reference_invoice_id: AirbyteSortOrder
    """The ID of the invoice this credit note references."""
    refunded_at: AirbyteSortOrder
    """The date when the credit note was refunded."""
    resource_version: AirbyteSortOrder
    """The version of the credit note resource."""
    round_off_amount: AirbyteSortOrder
    """Amount rounded off for currency conversions."""
    shipping_address: AirbyteSortOrder
    """Details of the shipping address associated with the credit note"""
    status: AirbyteSortOrder
    """The status of the credit note."""
    sub_total: AirbyteSortOrder
    """The subtotal amount of the credit note."""
    sub_total_in_local_currency: AirbyteSortOrder
    """The subtotal amount in local currency."""
    subscription_id: AirbyteSortOrder
    """The ID of the subscription associated with the credit note."""
    taxes: AirbyteSortOrder
    """List of taxes applied to the credit note"""
    total: AirbyteSortOrder
    """The total amount of the credit note."""
    total_in_local_currency: AirbyteSortOrder
    """The total amount in local currency."""
    type_: AirbyteSortOrder
    """The type of credit note."""
    updated_at: AirbyteSortOrder
    """The date when the credit note was last updated."""
    vat_number: AirbyteSortOrder
    """VAT number associated with the credit note."""
    vat_number_prefix: AirbyteSortOrder
    """Prefix for the VAT number."""
    voided_at: AirbyteSortOrder
    """The date when the credit note was voided."""


# Entity-specific condition types for credit_note
class CreditNoteEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CreditNoteSearchFilter


class CreditNoteNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CreditNoteSearchFilter


class CreditNoteGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CreditNoteSearchFilter


class CreditNoteGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CreditNoteSearchFilter


class CreditNoteLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CreditNoteSearchFilter


class CreditNoteLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CreditNoteSearchFilter


class CreditNoteLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CreditNoteStringFilter


class CreditNoteFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CreditNoteStringFilter


class CreditNoteKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CreditNoteStringFilter


class CreditNoteContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CreditNoteAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CreditNoteInCondition = TypedDict("CreditNoteInCondition", {"in": CreditNoteInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CreditNoteNotCondition = TypedDict("CreditNoteNotCondition", {"not": "CreditNoteCondition"}, total=False)
"""Negates the nested condition."""

CreditNoteAndCondition = TypedDict("CreditNoteAndCondition", {"and": "list[CreditNoteCondition]"}, total=False)
"""True if all nested conditions are true."""

CreditNoteOrCondition = TypedDict("CreditNoteOrCondition", {"or": "list[CreditNoteCondition]"}, total=False)
"""True if any nested condition is true."""

CreditNoteAnyCondition = TypedDict("CreditNoteAnyCondition", {"any": CreditNoteAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all credit_note condition types
CreditNoteCondition = (
    CreditNoteEqCondition
    | CreditNoteNeqCondition
    | CreditNoteGtCondition
    | CreditNoteGteCondition
    | CreditNoteLtCondition
    | CreditNoteLteCondition
    | CreditNoteInCondition
    | CreditNoteLikeCondition
    | CreditNoteFuzzyCondition
    | CreditNoteKeywordCondition
    | CreditNoteContainsCondition
    | CreditNoteNotCondition
    | CreditNoteAndCondition
    | CreditNoteOrCondition
    | CreditNoteAnyCondition
)


class CreditNoteSearchQuery(TypedDict, total=False):
    """Search query for credit_note entity."""
    filter: CreditNoteCondition
    sort: list[CreditNoteSortFilter]


# ===== COUPON SEARCH TYPES =====

class CouponSearchFilter(TypedDict, total=False):
    """Available fields for filtering coupon search queries."""
    apply_discount_on: str | None
    """Determines where the discount is applied on (e.g. subtotal, total)."""
    apply_on: str | None
    """Specify on what type of items the coupon applies (e.g. subscription, addon)."""
    archived_at: int | None
    """Timestamp when the coupon was archived."""
    coupon_constraints: list[Any] | None
    """Represents the constraints associated with the coupon"""
    created_at: int | None
    """Timestamp of the coupon creation."""
    currency_code: str | None
    """The currency code for the coupon (e.g. USD, EUR)."""
    custom_fields: list[Any] | None
    """"""
    discount_amount: int | None
    """The fixed discount amount applied by the coupon."""
    discount_percentage: float | None
    """Percentage discount applied by the coupon."""
    discount_quantity: int | None
    """Specifies the number of free units provided for the item price, without affecting the total quantity sold. This parameter is applicable only when the discount_type is set to offer_quantity."""
    discount_type: str | None
    """Type of discount (e.g. fixed, percentage)."""
    duration_month: int | None
    """Duration of the coupon in months."""
    duration_type: str | None
    """Type of duration (e.g. forever, one-time)."""
    id: str | None
    """Unique identifier for the coupon."""
    invoice_name: str | None
    """Name displayed on invoices when the coupon is used."""
    invoice_notes: str | None
    """Additional notes displayed on invoices when the coupon is used."""
    item_constraint_criteria: list[Any] | None
    """Criteria for item constraints"""
    item_constraints: list[Any] | None
    """Constraints related to the items"""
    max_redemptions: int | None
    """Maximum number of times the coupon can be redeemed."""
    name: str | None
    """Name of the coupon."""
    object_: str | None
    """Type of object (usually 'coupon')."""
    period: int | None
    """Duration or frequency for which the coupon is valid."""
    period_unit: str | None
    """Unit of the period (e.g. days, weeks)."""
    redemptions: int | None
    """Number of times the coupon has been redeemed."""
    resource_version: int | None
    """Version of the resource."""
    status: str | None
    """Current status of the coupon (e.g. active, inactive)."""
    updated_at: int | None
    """Timestamp when the coupon was last updated."""
    valid_till: int | None
    """Date until which the coupon is valid for use."""


class CouponInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    apply_discount_on: list[str]
    """Determines where the discount is applied on (e.g. subtotal, total)."""
    apply_on: list[str]
    """Specify on what type of items the coupon applies (e.g. subscription, addon)."""
    archived_at: list[int]
    """Timestamp when the coupon was archived."""
    coupon_constraints: list[list[Any]]
    """Represents the constraints associated with the coupon"""
    created_at: list[int]
    """Timestamp of the coupon creation."""
    currency_code: list[str]
    """The currency code for the coupon (e.g. USD, EUR)."""
    custom_fields: list[list[Any]]
    """"""
    discount_amount: list[int]
    """The fixed discount amount applied by the coupon."""
    discount_percentage: list[float]
    """Percentage discount applied by the coupon."""
    discount_quantity: list[int]
    """Specifies the number of free units provided for the item price, without affecting the total quantity sold. This parameter is applicable only when the discount_type is set to offer_quantity."""
    discount_type: list[str]
    """Type of discount (e.g. fixed, percentage)."""
    duration_month: list[int]
    """Duration of the coupon in months."""
    duration_type: list[str]
    """Type of duration (e.g. forever, one-time)."""
    id: list[str]
    """Unique identifier for the coupon."""
    invoice_name: list[str]
    """Name displayed on invoices when the coupon is used."""
    invoice_notes: list[str]
    """Additional notes displayed on invoices when the coupon is used."""
    item_constraint_criteria: list[list[Any]]
    """Criteria for item constraints"""
    item_constraints: list[list[Any]]
    """Constraints related to the items"""
    max_redemptions: list[int]
    """Maximum number of times the coupon can be redeemed."""
    name: list[str]
    """Name of the coupon."""
    object_: list[str]
    """Type of object (usually 'coupon')."""
    period: list[int]
    """Duration or frequency for which the coupon is valid."""
    period_unit: list[str]
    """Unit of the period (e.g. days, weeks)."""
    redemptions: list[int]
    """Number of times the coupon has been redeemed."""
    resource_version: list[int]
    """Version of the resource."""
    status: list[str]
    """Current status of the coupon (e.g. active, inactive)."""
    updated_at: list[int]
    """Timestamp when the coupon was last updated."""
    valid_till: list[int]
    """Date until which the coupon is valid for use."""


class CouponAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    apply_discount_on: Any
    """Determines where the discount is applied on (e.g. subtotal, total)."""
    apply_on: Any
    """Specify on what type of items the coupon applies (e.g. subscription, addon)."""
    archived_at: Any
    """Timestamp when the coupon was archived."""
    coupon_constraints: Any
    """Represents the constraints associated with the coupon"""
    created_at: Any
    """Timestamp of the coupon creation."""
    currency_code: Any
    """The currency code for the coupon (e.g. USD, EUR)."""
    custom_fields: Any
    """"""
    discount_amount: Any
    """The fixed discount amount applied by the coupon."""
    discount_percentage: Any
    """Percentage discount applied by the coupon."""
    discount_quantity: Any
    """Specifies the number of free units provided for the item price, without affecting the total quantity sold. This parameter is applicable only when the discount_type is set to offer_quantity."""
    discount_type: Any
    """Type of discount (e.g. fixed, percentage)."""
    duration_month: Any
    """Duration of the coupon in months."""
    duration_type: Any
    """Type of duration (e.g. forever, one-time)."""
    id: Any
    """Unique identifier for the coupon."""
    invoice_name: Any
    """Name displayed on invoices when the coupon is used."""
    invoice_notes: Any
    """Additional notes displayed on invoices when the coupon is used."""
    item_constraint_criteria: Any
    """Criteria for item constraints"""
    item_constraints: Any
    """Constraints related to the items"""
    max_redemptions: Any
    """Maximum number of times the coupon can be redeemed."""
    name: Any
    """Name of the coupon."""
    object_: Any
    """Type of object (usually 'coupon')."""
    period: Any
    """Duration or frequency for which the coupon is valid."""
    period_unit: Any
    """Unit of the period (e.g. days, weeks)."""
    redemptions: Any
    """Number of times the coupon has been redeemed."""
    resource_version: Any
    """Version of the resource."""
    status: Any
    """Current status of the coupon (e.g. active, inactive)."""
    updated_at: Any
    """Timestamp when the coupon was last updated."""
    valid_till: Any
    """Date until which the coupon is valid for use."""


class CouponStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    apply_discount_on: str
    """Determines where the discount is applied on (e.g. subtotal, total)."""
    apply_on: str
    """Specify on what type of items the coupon applies (e.g. subscription, addon)."""
    archived_at: str
    """Timestamp when the coupon was archived."""
    coupon_constraints: str
    """Represents the constraints associated with the coupon"""
    created_at: str
    """Timestamp of the coupon creation."""
    currency_code: str
    """The currency code for the coupon (e.g. USD, EUR)."""
    custom_fields: str
    """"""
    discount_amount: str
    """The fixed discount amount applied by the coupon."""
    discount_percentage: str
    """Percentage discount applied by the coupon."""
    discount_quantity: str
    """Specifies the number of free units provided for the item price, without affecting the total quantity sold. This parameter is applicable only when the discount_type is set to offer_quantity."""
    discount_type: str
    """Type of discount (e.g. fixed, percentage)."""
    duration_month: str
    """Duration of the coupon in months."""
    duration_type: str
    """Type of duration (e.g. forever, one-time)."""
    id: str
    """Unique identifier for the coupon."""
    invoice_name: str
    """Name displayed on invoices when the coupon is used."""
    invoice_notes: str
    """Additional notes displayed on invoices when the coupon is used."""
    item_constraint_criteria: str
    """Criteria for item constraints"""
    item_constraints: str
    """Constraints related to the items"""
    max_redemptions: str
    """Maximum number of times the coupon can be redeemed."""
    name: str
    """Name of the coupon."""
    object_: str
    """Type of object (usually 'coupon')."""
    period: str
    """Duration or frequency for which the coupon is valid."""
    period_unit: str
    """Unit of the period (e.g. days, weeks)."""
    redemptions: str
    """Number of times the coupon has been redeemed."""
    resource_version: str
    """Version of the resource."""
    status: str
    """Current status of the coupon (e.g. active, inactive)."""
    updated_at: str
    """Timestamp when the coupon was last updated."""
    valid_till: str
    """Date until which the coupon is valid for use."""


class CouponSortFilter(TypedDict, total=False):
    """Available fields for sorting coupon search results."""
    apply_discount_on: AirbyteSortOrder
    """Determines where the discount is applied on (e.g. subtotal, total)."""
    apply_on: AirbyteSortOrder
    """Specify on what type of items the coupon applies (e.g. subscription, addon)."""
    archived_at: AirbyteSortOrder
    """Timestamp when the coupon was archived."""
    coupon_constraints: AirbyteSortOrder
    """Represents the constraints associated with the coupon"""
    created_at: AirbyteSortOrder
    """Timestamp of the coupon creation."""
    currency_code: AirbyteSortOrder
    """The currency code for the coupon (e.g. USD, EUR)."""
    custom_fields: AirbyteSortOrder
    """"""
    discount_amount: AirbyteSortOrder
    """The fixed discount amount applied by the coupon."""
    discount_percentage: AirbyteSortOrder
    """Percentage discount applied by the coupon."""
    discount_quantity: AirbyteSortOrder
    """Specifies the number of free units provided for the item price, without affecting the total quantity sold. This parameter is applicable only when the discount_type is set to offer_quantity."""
    discount_type: AirbyteSortOrder
    """Type of discount (e.g. fixed, percentage)."""
    duration_month: AirbyteSortOrder
    """Duration of the coupon in months."""
    duration_type: AirbyteSortOrder
    """Type of duration (e.g. forever, one-time)."""
    id: AirbyteSortOrder
    """Unique identifier for the coupon."""
    invoice_name: AirbyteSortOrder
    """Name displayed on invoices when the coupon is used."""
    invoice_notes: AirbyteSortOrder
    """Additional notes displayed on invoices when the coupon is used."""
    item_constraint_criteria: AirbyteSortOrder
    """Criteria for item constraints"""
    item_constraints: AirbyteSortOrder
    """Constraints related to the items"""
    max_redemptions: AirbyteSortOrder
    """Maximum number of times the coupon can be redeemed."""
    name: AirbyteSortOrder
    """Name of the coupon."""
    object_: AirbyteSortOrder
    """Type of object (usually 'coupon')."""
    period: AirbyteSortOrder
    """Duration or frequency for which the coupon is valid."""
    period_unit: AirbyteSortOrder
    """Unit of the period (e.g. days, weeks)."""
    redemptions: AirbyteSortOrder
    """Number of times the coupon has been redeemed."""
    resource_version: AirbyteSortOrder
    """Version of the resource."""
    status: AirbyteSortOrder
    """Current status of the coupon (e.g. active, inactive)."""
    updated_at: AirbyteSortOrder
    """Timestamp when the coupon was last updated."""
    valid_till: AirbyteSortOrder
    """Date until which the coupon is valid for use."""


# Entity-specific condition types for coupon
class CouponEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CouponSearchFilter


class CouponNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CouponSearchFilter


class CouponGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CouponSearchFilter


class CouponGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CouponSearchFilter


class CouponLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CouponSearchFilter


class CouponLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CouponSearchFilter


class CouponLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CouponStringFilter


class CouponFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CouponStringFilter


class CouponKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CouponStringFilter


class CouponContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CouponAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CouponInCondition = TypedDict("CouponInCondition", {"in": CouponInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CouponNotCondition = TypedDict("CouponNotCondition", {"not": "CouponCondition"}, total=False)
"""Negates the nested condition."""

CouponAndCondition = TypedDict("CouponAndCondition", {"and": "list[CouponCondition]"}, total=False)
"""True if all nested conditions are true."""

CouponOrCondition = TypedDict("CouponOrCondition", {"or": "list[CouponCondition]"}, total=False)
"""True if any nested condition is true."""

CouponAnyCondition = TypedDict("CouponAnyCondition", {"any": CouponAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all coupon condition types
CouponCondition = (
    CouponEqCondition
    | CouponNeqCondition
    | CouponGtCondition
    | CouponGteCondition
    | CouponLtCondition
    | CouponLteCondition
    | CouponInCondition
    | CouponLikeCondition
    | CouponFuzzyCondition
    | CouponKeywordCondition
    | CouponContainsCondition
    | CouponNotCondition
    | CouponAndCondition
    | CouponOrCondition
    | CouponAnyCondition
)


class CouponSearchQuery(TypedDict, total=False):
    """Search query for coupon entity."""
    filter: CouponCondition
    sort: list[CouponSortFilter]


# ===== TRANSACTION SEARCH TYPES =====

class TransactionSearchFilter(TypedDict, total=False):
    """Available fields for filtering transaction search queries."""
    amount: int | None
    """The total amount of the transaction."""
    amount_capturable: int | None
    """The remaining amount that can be captured in the transaction."""
    amount_unused: int | None
    """The amount in the transaction that remains unused."""
    authorization_reason: str | None
    """Reason for authorization of the transaction."""
    base_currency_code: str | None
    """The base currency code of the transaction."""
    business_entity_id: str | None
    """The ID of the business entity related to the transaction."""
    cn_create_reason_code: str | None
    """Reason code for creating a credit note."""
    cn_date: int | None
    """Date of the credit note."""
    cn_reference_invoice_id: str | None
    """ID of the invoice referenced in the credit note."""
    cn_status: str | None
    """Status of the credit note."""
    cn_total: int | None
    """Total amount of the credit note."""
    currency_code: str | None
    """The currency code of the transaction."""
    custom_fields: list[Any] | None
    """"""
    customer_id: str | None
    """The ID of the customer associated with the transaction."""
    date: int | None
    """Date of the transaction."""
    deleted: bool | None
    """Flag indicating if the transaction is deleted."""
    error_code: str | None
    """Error code associated with the transaction."""
    error_detail: str | None
    """Detailed error information related to the transaction."""
    error_text: str | None
    """Error message text of the transaction."""
    exchange_rate: float | None
    """Exchange rate used in the transaction."""
    fraud_flag: str | None
    """Flag indicating if the transaction is flagged for fraud."""
    fraud_reason: str | None
    """Reason for flagging the transaction as fraud."""
    gateway: str | None
    """The payment gateway used in the transaction."""
    gateway_account_id: str | None
    """ID of the gateway account used in the transaction."""
    id: str | None
    """Unique identifier of the transaction."""
    id_at_gateway: str | None
    """Transaction ID assigned by the gateway."""
    iin: str | None
    """Bank identification number of the transaction."""
    initiator_type: str | None
    """Type of initiator involved in the transaction."""
    last4: str | None
    """Last 4 digits of the card used in the transaction."""
    linked_credit_notes: list[Any] | None
    """Linked credit notes associated with the transaction."""
    linked_invoices: list[Any] | None
    """Linked invoices associated with the transaction."""
    linked_payments: list[Any] | None
    """Linked payments associated with the transaction."""
    linked_refunds: list[Any] | None
    """Linked refunds associated with the transaction."""
    masked_card_number: str | None
    """Masked card number used in the transaction."""
    merchant_reference_id: str | None
    """Merchant reference ID of the transaction."""
    object_: str | None
    """Type of object representing the transaction."""
    payment_method: str | None
    """Payment method used in the transaction."""
    payment_method_details: str | None
    """Details of the payment method used in the transaction."""
    payment_source_id: str | None
    """ID of the payment source used in the transaction."""
    reference_authorization_id: str | None
    """Reference authorization ID of the transaction."""
    reference_number: str | None
    """Reference number associated with the transaction."""
    reference_transaction_id: str | None
    """ID of the reference transaction."""
    refrence_number: str | None
    """Reference number of the transaction."""
    refunded_txn_id: str | None
    """ID of the refunded transaction."""
    resource_version: int | None
    """Resource version of the transaction."""
    reversal_transaction_id: str | None
    """ID of the reversal transaction, if any."""
    settled_at: int | None
    """Date when the transaction was settled."""
    status: str | None
    """Status of the transaction."""
    subscription_id: str | None
    """ID of the subscription related to the transaction."""
    three_d_secure: bool | None
    """Flag indicating if 3D secure was used in the transaction."""
    txn_amount: int | None
    """Amount of the transaction."""
    txn_date: int | None
    """Date of the transaction."""
    type_: str | None
    """Type of the transaction."""
    updated_at: int | None
    """Date when the transaction was last updated."""
    voided_at: int | None
    """Date when the transaction was voided."""


class TransactionInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[int]
    """The total amount of the transaction."""
    amount_capturable: list[int]
    """The remaining amount that can be captured in the transaction."""
    amount_unused: list[int]
    """The amount in the transaction that remains unused."""
    authorization_reason: list[str]
    """Reason for authorization of the transaction."""
    base_currency_code: list[str]
    """The base currency code of the transaction."""
    business_entity_id: list[str]
    """The ID of the business entity related to the transaction."""
    cn_create_reason_code: list[str]
    """Reason code for creating a credit note."""
    cn_date: list[int]
    """Date of the credit note."""
    cn_reference_invoice_id: list[str]
    """ID of the invoice referenced in the credit note."""
    cn_status: list[str]
    """Status of the credit note."""
    cn_total: list[int]
    """Total amount of the credit note."""
    currency_code: list[str]
    """The currency code of the transaction."""
    custom_fields: list[list[Any]]
    """"""
    customer_id: list[str]
    """The ID of the customer associated with the transaction."""
    date: list[int]
    """Date of the transaction."""
    deleted: list[bool]
    """Flag indicating if the transaction is deleted."""
    error_code: list[str]
    """Error code associated with the transaction."""
    error_detail: list[str]
    """Detailed error information related to the transaction."""
    error_text: list[str]
    """Error message text of the transaction."""
    exchange_rate: list[float]
    """Exchange rate used in the transaction."""
    fraud_flag: list[str]
    """Flag indicating if the transaction is flagged for fraud."""
    fraud_reason: list[str]
    """Reason for flagging the transaction as fraud."""
    gateway: list[str]
    """The payment gateway used in the transaction."""
    gateway_account_id: list[str]
    """ID of the gateway account used in the transaction."""
    id: list[str]
    """Unique identifier of the transaction."""
    id_at_gateway: list[str]
    """Transaction ID assigned by the gateway."""
    iin: list[str]
    """Bank identification number of the transaction."""
    initiator_type: list[str]
    """Type of initiator involved in the transaction."""
    last4: list[str]
    """Last 4 digits of the card used in the transaction."""
    linked_credit_notes: list[list[Any]]
    """Linked credit notes associated with the transaction."""
    linked_invoices: list[list[Any]]
    """Linked invoices associated with the transaction."""
    linked_payments: list[list[Any]]
    """Linked payments associated with the transaction."""
    linked_refunds: list[list[Any]]
    """Linked refunds associated with the transaction."""
    masked_card_number: list[str]
    """Masked card number used in the transaction."""
    merchant_reference_id: list[str]
    """Merchant reference ID of the transaction."""
    object_: list[str]
    """Type of object representing the transaction."""
    payment_method: list[str]
    """Payment method used in the transaction."""
    payment_method_details: list[str]
    """Details of the payment method used in the transaction."""
    payment_source_id: list[str]
    """ID of the payment source used in the transaction."""
    reference_authorization_id: list[str]
    """Reference authorization ID of the transaction."""
    reference_number: list[str]
    """Reference number associated with the transaction."""
    reference_transaction_id: list[str]
    """ID of the reference transaction."""
    refrence_number: list[str]
    """Reference number of the transaction."""
    refunded_txn_id: list[str]
    """ID of the refunded transaction."""
    resource_version: list[int]
    """Resource version of the transaction."""
    reversal_transaction_id: list[str]
    """ID of the reversal transaction, if any."""
    settled_at: list[int]
    """Date when the transaction was settled."""
    status: list[str]
    """Status of the transaction."""
    subscription_id: list[str]
    """ID of the subscription related to the transaction."""
    three_d_secure: list[bool]
    """Flag indicating if 3D secure was used in the transaction."""
    txn_amount: list[int]
    """Amount of the transaction."""
    txn_date: list[int]
    """Date of the transaction."""
    type_: list[str]
    """Type of the transaction."""
    updated_at: list[int]
    """Date when the transaction was last updated."""
    voided_at: list[int]
    """Date when the transaction was voided."""


class TransactionAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """The total amount of the transaction."""
    amount_capturable: Any
    """The remaining amount that can be captured in the transaction."""
    amount_unused: Any
    """The amount in the transaction that remains unused."""
    authorization_reason: Any
    """Reason for authorization of the transaction."""
    base_currency_code: Any
    """The base currency code of the transaction."""
    business_entity_id: Any
    """The ID of the business entity related to the transaction."""
    cn_create_reason_code: Any
    """Reason code for creating a credit note."""
    cn_date: Any
    """Date of the credit note."""
    cn_reference_invoice_id: Any
    """ID of the invoice referenced in the credit note."""
    cn_status: Any
    """Status of the credit note."""
    cn_total: Any
    """Total amount of the credit note."""
    currency_code: Any
    """The currency code of the transaction."""
    custom_fields: Any
    """"""
    customer_id: Any
    """The ID of the customer associated with the transaction."""
    date: Any
    """Date of the transaction."""
    deleted: Any
    """Flag indicating if the transaction is deleted."""
    error_code: Any
    """Error code associated with the transaction."""
    error_detail: Any
    """Detailed error information related to the transaction."""
    error_text: Any
    """Error message text of the transaction."""
    exchange_rate: Any
    """Exchange rate used in the transaction."""
    fraud_flag: Any
    """Flag indicating if the transaction is flagged for fraud."""
    fraud_reason: Any
    """Reason for flagging the transaction as fraud."""
    gateway: Any
    """The payment gateway used in the transaction."""
    gateway_account_id: Any
    """ID of the gateway account used in the transaction."""
    id: Any
    """Unique identifier of the transaction."""
    id_at_gateway: Any
    """Transaction ID assigned by the gateway."""
    iin: Any
    """Bank identification number of the transaction."""
    initiator_type: Any
    """Type of initiator involved in the transaction."""
    last4: Any
    """Last 4 digits of the card used in the transaction."""
    linked_credit_notes: Any
    """Linked credit notes associated with the transaction."""
    linked_invoices: Any
    """Linked invoices associated with the transaction."""
    linked_payments: Any
    """Linked payments associated with the transaction."""
    linked_refunds: Any
    """Linked refunds associated with the transaction."""
    masked_card_number: Any
    """Masked card number used in the transaction."""
    merchant_reference_id: Any
    """Merchant reference ID of the transaction."""
    object_: Any
    """Type of object representing the transaction."""
    payment_method: Any
    """Payment method used in the transaction."""
    payment_method_details: Any
    """Details of the payment method used in the transaction."""
    payment_source_id: Any
    """ID of the payment source used in the transaction."""
    reference_authorization_id: Any
    """Reference authorization ID of the transaction."""
    reference_number: Any
    """Reference number associated with the transaction."""
    reference_transaction_id: Any
    """ID of the reference transaction."""
    refrence_number: Any
    """Reference number of the transaction."""
    refunded_txn_id: Any
    """ID of the refunded transaction."""
    resource_version: Any
    """Resource version of the transaction."""
    reversal_transaction_id: Any
    """ID of the reversal transaction, if any."""
    settled_at: Any
    """Date when the transaction was settled."""
    status: Any
    """Status of the transaction."""
    subscription_id: Any
    """ID of the subscription related to the transaction."""
    three_d_secure: Any
    """Flag indicating if 3D secure was used in the transaction."""
    txn_amount: Any
    """Amount of the transaction."""
    txn_date: Any
    """Date of the transaction."""
    type_: Any
    """Type of the transaction."""
    updated_at: Any
    """Date when the transaction was last updated."""
    voided_at: Any
    """Date when the transaction was voided."""


class TransactionStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """The total amount of the transaction."""
    amount_capturable: str
    """The remaining amount that can be captured in the transaction."""
    amount_unused: str
    """The amount in the transaction that remains unused."""
    authorization_reason: str
    """Reason for authorization of the transaction."""
    base_currency_code: str
    """The base currency code of the transaction."""
    business_entity_id: str
    """The ID of the business entity related to the transaction."""
    cn_create_reason_code: str
    """Reason code for creating a credit note."""
    cn_date: str
    """Date of the credit note."""
    cn_reference_invoice_id: str
    """ID of the invoice referenced in the credit note."""
    cn_status: str
    """Status of the credit note."""
    cn_total: str
    """Total amount of the credit note."""
    currency_code: str
    """The currency code of the transaction."""
    custom_fields: str
    """"""
    customer_id: str
    """The ID of the customer associated with the transaction."""
    date: str
    """Date of the transaction."""
    deleted: str
    """Flag indicating if the transaction is deleted."""
    error_code: str
    """Error code associated with the transaction."""
    error_detail: str
    """Detailed error information related to the transaction."""
    error_text: str
    """Error message text of the transaction."""
    exchange_rate: str
    """Exchange rate used in the transaction."""
    fraud_flag: str
    """Flag indicating if the transaction is flagged for fraud."""
    fraud_reason: str
    """Reason for flagging the transaction as fraud."""
    gateway: str
    """The payment gateway used in the transaction."""
    gateway_account_id: str
    """ID of the gateway account used in the transaction."""
    id: str
    """Unique identifier of the transaction."""
    id_at_gateway: str
    """Transaction ID assigned by the gateway."""
    iin: str
    """Bank identification number of the transaction."""
    initiator_type: str
    """Type of initiator involved in the transaction."""
    last4: str
    """Last 4 digits of the card used in the transaction."""
    linked_credit_notes: str
    """Linked credit notes associated with the transaction."""
    linked_invoices: str
    """Linked invoices associated with the transaction."""
    linked_payments: str
    """Linked payments associated with the transaction."""
    linked_refunds: str
    """Linked refunds associated with the transaction."""
    masked_card_number: str
    """Masked card number used in the transaction."""
    merchant_reference_id: str
    """Merchant reference ID of the transaction."""
    object_: str
    """Type of object representing the transaction."""
    payment_method: str
    """Payment method used in the transaction."""
    payment_method_details: str
    """Details of the payment method used in the transaction."""
    payment_source_id: str
    """ID of the payment source used in the transaction."""
    reference_authorization_id: str
    """Reference authorization ID of the transaction."""
    reference_number: str
    """Reference number associated with the transaction."""
    reference_transaction_id: str
    """ID of the reference transaction."""
    refrence_number: str
    """Reference number of the transaction."""
    refunded_txn_id: str
    """ID of the refunded transaction."""
    resource_version: str
    """Resource version of the transaction."""
    reversal_transaction_id: str
    """ID of the reversal transaction, if any."""
    settled_at: str
    """Date when the transaction was settled."""
    status: str
    """Status of the transaction."""
    subscription_id: str
    """ID of the subscription related to the transaction."""
    three_d_secure: str
    """Flag indicating if 3D secure was used in the transaction."""
    txn_amount: str
    """Amount of the transaction."""
    txn_date: str
    """Date of the transaction."""
    type_: str
    """Type of the transaction."""
    updated_at: str
    """Date when the transaction was last updated."""
    voided_at: str
    """Date when the transaction was voided."""


class TransactionSortFilter(TypedDict, total=False):
    """Available fields for sorting transaction search results."""
    amount: AirbyteSortOrder
    """The total amount of the transaction."""
    amount_capturable: AirbyteSortOrder
    """The remaining amount that can be captured in the transaction."""
    amount_unused: AirbyteSortOrder
    """The amount in the transaction that remains unused."""
    authorization_reason: AirbyteSortOrder
    """Reason for authorization of the transaction."""
    base_currency_code: AirbyteSortOrder
    """The base currency code of the transaction."""
    business_entity_id: AirbyteSortOrder
    """The ID of the business entity related to the transaction."""
    cn_create_reason_code: AirbyteSortOrder
    """Reason code for creating a credit note."""
    cn_date: AirbyteSortOrder
    """Date of the credit note."""
    cn_reference_invoice_id: AirbyteSortOrder
    """ID of the invoice referenced in the credit note."""
    cn_status: AirbyteSortOrder
    """Status of the credit note."""
    cn_total: AirbyteSortOrder
    """Total amount of the credit note."""
    currency_code: AirbyteSortOrder
    """The currency code of the transaction."""
    custom_fields: AirbyteSortOrder
    """"""
    customer_id: AirbyteSortOrder
    """The ID of the customer associated with the transaction."""
    date: AirbyteSortOrder
    """Date of the transaction."""
    deleted: AirbyteSortOrder
    """Flag indicating if the transaction is deleted."""
    error_code: AirbyteSortOrder
    """Error code associated with the transaction."""
    error_detail: AirbyteSortOrder
    """Detailed error information related to the transaction."""
    error_text: AirbyteSortOrder
    """Error message text of the transaction."""
    exchange_rate: AirbyteSortOrder
    """Exchange rate used in the transaction."""
    fraud_flag: AirbyteSortOrder
    """Flag indicating if the transaction is flagged for fraud."""
    fraud_reason: AirbyteSortOrder
    """Reason for flagging the transaction as fraud."""
    gateway: AirbyteSortOrder
    """The payment gateway used in the transaction."""
    gateway_account_id: AirbyteSortOrder
    """ID of the gateway account used in the transaction."""
    id: AirbyteSortOrder
    """Unique identifier of the transaction."""
    id_at_gateway: AirbyteSortOrder
    """Transaction ID assigned by the gateway."""
    iin: AirbyteSortOrder
    """Bank identification number of the transaction."""
    initiator_type: AirbyteSortOrder
    """Type of initiator involved in the transaction."""
    last4: AirbyteSortOrder
    """Last 4 digits of the card used in the transaction."""
    linked_credit_notes: AirbyteSortOrder
    """Linked credit notes associated with the transaction."""
    linked_invoices: AirbyteSortOrder
    """Linked invoices associated with the transaction."""
    linked_payments: AirbyteSortOrder
    """Linked payments associated with the transaction."""
    linked_refunds: AirbyteSortOrder
    """Linked refunds associated with the transaction."""
    masked_card_number: AirbyteSortOrder
    """Masked card number used in the transaction."""
    merchant_reference_id: AirbyteSortOrder
    """Merchant reference ID of the transaction."""
    object_: AirbyteSortOrder
    """Type of object representing the transaction."""
    payment_method: AirbyteSortOrder
    """Payment method used in the transaction."""
    payment_method_details: AirbyteSortOrder
    """Details of the payment method used in the transaction."""
    payment_source_id: AirbyteSortOrder
    """ID of the payment source used in the transaction."""
    reference_authorization_id: AirbyteSortOrder
    """Reference authorization ID of the transaction."""
    reference_number: AirbyteSortOrder
    """Reference number associated with the transaction."""
    reference_transaction_id: AirbyteSortOrder
    """ID of the reference transaction."""
    refrence_number: AirbyteSortOrder
    """Reference number of the transaction."""
    refunded_txn_id: AirbyteSortOrder
    """ID of the refunded transaction."""
    resource_version: AirbyteSortOrder
    """Resource version of the transaction."""
    reversal_transaction_id: AirbyteSortOrder
    """ID of the reversal transaction, if any."""
    settled_at: AirbyteSortOrder
    """Date when the transaction was settled."""
    status: AirbyteSortOrder
    """Status of the transaction."""
    subscription_id: AirbyteSortOrder
    """ID of the subscription related to the transaction."""
    three_d_secure: AirbyteSortOrder
    """Flag indicating if 3D secure was used in the transaction."""
    txn_amount: AirbyteSortOrder
    """Amount of the transaction."""
    txn_date: AirbyteSortOrder
    """Date of the transaction."""
    type_: AirbyteSortOrder
    """Type of the transaction."""
    updated_at: AirbyteSortOrder
    """Date when the transaction was last updated."""
    voided_at: AirbyteSortOrder
    """Date when the transaction was voided."""


# Entity-specific condition types for transaction
class TransactionEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TransactionSearchFilter


class TransactionNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TransactionSearchFilter


class TransactionGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TransactionSearchFilter


class TransactionGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TransactionSearchFilter


class TransactionLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TransactionSearchFilter


class TransactionLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TransactionSearchFilter


class TransactionLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TransactionStringFilter


class TransactionFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TransactionStringFilter


class TransactionKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TransactionStringFilter


class TransactionContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TransactionAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TransactionInCondition = TypedDict("TransactionInCondition", {"in": TransactionInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TransactionNotCondition = TypedDict("TransactionNotCondition", {"not": "TransactionCondition"}, total=False)
"""Negates the nested condition."""

TransactionAndCondition = TypedDict("TransactionAndCondition", {"and": "list[TransactionCondition]"}, total=False)
"""True if all nested conditions are true."""

TransactionOrCondition = TypedDict("TransactionOrCondition", {"or": "list[TransactionCondition]"}, total=False)
"""True if any nested condition is true."""

TransactionAnyCondition = TypedDict("TransactionAnyCondition", {"any": TransactionAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all transaction condition types
TransactionCondition = (
    TransactionEqCondition
    | TransactionNeqCondition
    | TransactionGtCondition
    | TransactionGteCondition
    | TransactionLtCondition
    | TransactionLteCondition
    | TransactionInCondition
    | TransactionLikeCondition
    | TransactionFuzzyCondition
    | TransactionKeywordCondition
    | TransactionContainsCondition
    | TransactionNotCondition
    | TransactionAndCondition
    | TransactionOrCondition
    | TransactionAnyCondition
)


class TransactionSearchQuery(TypedDict, total=False):
    """Search query for transaction entity."""
    filter: TransactionCondition
    sort: list[TransactionSortFilter]


# ===== EVENT SEARCH TYPES =====

class EventSearchFilter(TypedDict, total=False):
    """Available fields for filtering event search queries."""
    api_version: str | None
    """The version of the Chargebee API being used to fetch the event data."""
    content: dict[str, Any] | None
    """The specific content or information associated with the event."""
    custom_fields: list[Any] | None
    """"""
    event_type: str | None
    """The type or category of the event."""
    id: str | None
    """Unique identifier for the event data record."""
    object_: str | None
    """The object or entity that the event is triggered for."""
    occurred_at: int | None
    """The datetime when the event occurred."""
    source: str | None
    """The source or origin of the event data."""
    user: str | None
    """Information about the user or entity associated with the event."""
    webhook_status: str | None
    """The status of the webhook execution for the event."""
    webhooks: list[Any] | None
    """List of webhooks associated with the event."""


class EventInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    api_version: list[str]
    """The version of the Chargebee API being used to fetch the event data."""
    content: list[dict[str, Any]]
    """The specific content or information associated with the event."""
    custom_fields: list[list[Any]]
    """"""
    event_type: list[str]
    """The type or category of the event."""
    id: list[str]
    """Unique identifier for the event data record."""
    object_: list[str]
    """The object or entity that the event is triggered for."""
    occurred_at: list[int]
    """The datetime when the event occurred."""
    source: list[str]
    """The source or origin of the event data."""
    user: list[str]
    """Information about the user or entity associated with the event."""
    webhook_status: list[str]
    """The status of the webhook execution for the event."""
    webhooks: list[list[Any]]
    """List of webhooks associated with the event."""


class EventAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    api_version: Any
    """The version of the Chargebee API being used to fetch the event data."""
    content: Any
    """The specific content or information associated with the event."""
    custom_fields: Any
    """"""
    event_type: Any
    """The type or category of the event."""
    id: Any
    """Unique identifier for the event data record."""
    object_: Any
    """The object or entity that the event is triggered for."""
    occurred_at: Any
    """The datetime when the event occurred."""
    source: Any
    """The source or origin of the event data."""
    user: Any
    """Information about the user or entity associated with the event."""
    webhook_status: Any
    """The status of the webhook execution for the event."""
    webhooks: Any
    """List of webhooks associated with the event."""


class EventStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    api_version: str
    """The version of the Chargebee API being used to fetch the event data."""
    content: str
    """The specific content or information associated with the event."""
    custom_fields: str
    """"""
    event_type: str
    """The type or category of the event."""
    id: str
    """Unique identifier for the event data record."""
    object_: str
    """The object or entity that the event is triggered for."""
    occurred_at: str
    """The datetime when the event occurred."""
    source: str
    """The source or origin of the event data."""
    user: str
    """Information about the user or entity associated with the event."""
    webhook_status: str
    """The status of the webhook execution for the event."""
    webhooks: str
    """List of webhooks associated with the event."""


class EventSortFilter(TypedDict, total=False):
    """Available fields for sorting event search results."""
    api_version: AirbyteSortOrder
    """The version of the Chargebee API being used to fetch the event data."""
    content: AirbyteSortOrder
    """The specific content or information associated with the event."""
    custom_fields: AirbyteSortOrder
    """"""
    event_type: AirbyteSortOrder
    """The type or category of the event."""
    id: AirbyteSortOrder
    """Unique identifier for the event data record."""
    object_: AirbyteSortOrder
    """The object or entity that the event is triggered for."""
    occurred_at: AirbyteSortOrder
    """The datetime when the event occurred."""
    source: AirbyteSortOrder
    """The source or origin of the event data."""
    user: AirbyteSortOrder
    """Information about the user or entity associated with the event."""
    webhook_status: AirbyteSortOrder
    """The status of the webhook execution for the event."""
    webhooks: AirbyteSortOrder
    """List of webhooks associated with the event."""


# Entity-specific condition types for event
class EventEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EventSearchFilter


class EventNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EventSearchFilter


class EventGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EventSearchFilter


class EventGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EventSearchFilter


class EventLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EventSearchFilter


class EventLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EventSearchFilter


class EventLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EventStringFilter


class EventFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EventStringFilter


class EventKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EventStringFilter


class EventContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EventAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EventInCondition = TypedDict("EventInCondition", {"in": EventInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EventNotCondition = TypedDict("EventNotCondition", {"not": "EventCondition"}, total=False)
"""Negates the nested condition."""

EventAndCondition = TypedDict("EventAndCondition", {"and": "list[EventCondition]"}, total=False)
"""True if all nested conditions are true."""

EventOrCondition = TypedDict("EventOrCondition", {"or": "list[EventCondition]"}, total=False)
"""True if any nested condition is true."""

EventAnyCondition = TypedDict("EventAnyCondition", {"any": EventAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all event condition types
EventCondition = (
    EventEqCondition
    | EventNeqCondition
    | EventGtCondition
    | EventGteCondition
    | EventLtCondition
    | EventLteCondition
    | EventInCondition
    | EventLikeCondition
    | EventFuzzyCondition
    | EventKeywordCondition
    | EventContainsCondition
    | EventNotCondition
    | EventAndCondition
    | EventOrCondition
    | EventAnyCondition
)


class EventSearchQuery(TypedDict, total=False):
    """Search query for event entity."""
    filter: EventCondition
    sort: list[EventSortFilter]


# ===== ORDER SEARCH TYPES =====

class OrderSearchFilter(TypedDict, total=False):
    """Available fields for filtering order search queries."""
    amount_adjusted: int | None
    """Adjusted amount for the order."""
    amount_paid: int | None
    """Amount paid for the order."""
    base_currency_code: str | None
    """The base currency code used for the order."""
    batch_id: str | None
    """Unique identifier for the batch the order belongs to."""
    billing_address: dict[str, Any] | None
    """The billing address associated with the order"""
    business_entity_id: str | None
    """Identifier for the business entity associated with the order."""
    cancellation_reason: str | None
    """Reason for order cancellation."""
    cancelled_at: int | None
    """Timestamp when the order was cancelled."""
    created_at: int | None
    """Timestamp when the order was created."""
    created_by: str | None
    """User or system that created the order."""
    currency_code: str | None
    """Currency code used for the order."""
    custom_fields: list[Any] | None
    """"""
    customer_id: str | None
    """Identifier for the customer placing the order."""
    deleted: bool | None
    """Flag indicating if the order has been deleted."""
    delivered_at: int | None
    """Timestamp when the order was delivered."""
    discount: int | None
    """Discount amount applied to the order."""
    document_number: str | None
    """Unique document number associated with the order."""
    exchange_rate: float | None
    """Rate used for currency exchange in the order."""
    fulfillment_status: str | None
    """Status of fulfillment for the order."""
    gift_id: str | None
    """Identifier for any gift associated with the order."""
    gift_note: str | None
    """Note attached to any gift in the order."""
    id: str | None
    """Unique identifier for the order."""
    invoice_id: str | None
    """Identifier for the invoice associated with the order."""
    invoice_round_off_amount: int | None
    """Round-off amount applied to the invoice."""
    is_gifted: bool | None
    """Flag indicating if the order is a gift."""
    is_resent: bool | None
    """Flag indicating if the order has been resent."""
    line_item_discounts: list[Any] | None
    """Discounts applied to individual line items"""
    line_item_taxes: list[Any] | None
    """Taxes applied to individual line items"""
    linked_credit_notes: list[Any] | None
    """Credit notes linked to the order"""
    note: str | None
    """Additional notes or comments for the order."""
    object_: str | None
    """Type of object representing an order in the system."""
    order_date: int | None
    """Date when the order was created."""
    order_line_items: list[Any] | None
    """List of line items in the order"""
    order_type: str | None
    """Type of order such as purchase order or sales order."""
    original_order_id: str | None
    """Identifier for the original order if this is a modified order."""
    paid_on: int | None
    """Timestamp when the order was paid for."""
    payment_status: str | None
    """Status of payment for the order."""
    price_type: str | None
    """Type of pricing used for the order."""
    reference_id: str | None
    """Reference identifier for the order."""
    refundable_credits: int | None
    """Credits that can be refunded for the whole order."""
    refundable_credits_issued: int | None
    """Credits already issued for refund for the whole order."""
    resend_reason: str | None
    """Reason for resending the order."""
    resent_orders: list[Any] | None
    """Orders that were resent to the customer"""
    resent_status: str | None
    """Status of the resent order."""
    resource_version: int | None
    """Version of the resource or order data."""
    rounding_adjustement: int | None
    """Adjustment made for rounding off the order amount."""
    shipment_carrier: str | None
    """Carrier for shipping the order."""
    shipped_at: int | None
    """Timestamp when the order was shipped."""
    shipping_address: dict[str, Any] | None
    """The shipping address for the order"""
    shipping_cut_off_date: int | None
    """Date indicating the shipping cut-off for the order."""
    shipping_date: int | None
    """Date when the order is scheduled for shipping."""
    status: str | None
    """Current status of the order."""
    status_update_at: int | None
    """Timestamp when the status of the order was last updated."""
    sub_total: int | None
    """Sub-total amount for the order before applying taxes or discounts."""
    subscription_id: str | None
    """Identifier for the subscription associated with the order."""
    tax: int | None
    """Total tax amount for the order."""
    total: int | None
    """Total amount including taxes and discounts for the order."""
    tracking_id: str | None
    """Tracking identifier for the order shipment."""
    tracking_url: str | None
    """URL for tracking the order shipment."""
    updated_at: int | None
    """Timestamp when the order data was last updated."""


class OrderInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount_adjusted: list[int]
    """Adjusted amount for the order."""
    amount_paid: list[int]
    """Amount paid for the order."""
    base_currency_code: list[str]
    """The base currency code used for the order."""
    batch_id: list[str]
    """Unique identifier for the batch the order belongs to."""
    billing_address: list[dict[str, Any]]
    """The billing address associated with the order"""
    business_entity_id: list[str]
    """Identifier for the business entity associated with the order."""
    cancellation_reason: list[str]
    """Reason for order cancellation."""
    cancelled_at: list[int]
    """Timestamp when the order was cancelled."""
    created_at: list[int]
    """Timestamp when the order was created."""
    created_by: list[str]
    """User or system that created the order."""
    currency_code: list[str]
    """Currency code used for the order."""
    custom_fields: list[list[Any]]
    """"""
    customer_id: list[str]
    """Identifier for the customer placing the order."""
    deleted: list[bool]
    """Flag indicating if the order has been deleted."""
    delivered_at: list[int]
    """Timestamp when the order was delivered."""
    discount: list[int]
    """Discount amount applied to the order."""
    document_number: list[str]
    """Unique document number associated with the order."""
    exchange_rate: list[float]
    """Rate used for currency exchange in the order."""
    fulfillment_status: list[str]
    """Status of fulfillment for the order."""
    gift_id: list[str]
    """Identifier for any gift associated with the order."""
    gift_note: list[str]
    """Note attached to any gift in the order."""
    id: list[str]
    """Unique identifier for the order."""
    invoice_id: list[str]
    """Identifier for the invoice associated with the order."""
    invoice_round_off_amount: list[int]
    """Round-off amount applied to the invoice."""
    is_gifted: list[bool]
    """Flag indicating if the order is a gift."""
    is_resent: list[bool]
    """Flag indicating if the order has been resent."""
    line_item_discounts: list[list[Any]]
    """Discounts applied to individual line items"""
    line_item_taxes: list[list[Any]]
    """Taxes applied to individual line items"""
    linked_credit_notes: list[list[Any]]
    """Credit notes linked to the order"""
    note: list[str]
    """Additional notes or comments for the order."""
    object_: list[str]
    """Type of object representing an order in the system."""
    order_date: list[int]
    """Date when the order was created."""
    order_line_items: list[list[Any]]
    """List of line items in the order"""
    order_type: list[str]
    """Type of order such as purchase order or sales order."""
    original_order_id: list[str]
    """Identifier for the original order if this is a modified order."""
    paid_on: list[int]
    """Timestamp when the order was paid for."""
    payment_status: list[str]
    """Status of payment for the order."""
    price_type: list[str]
    """Type of pricing used for the order."""
    reference_id: list[str]
    """Reference identifier for the order."""
    refundable_credits: list[int]
    """Credits that can be refunded for the whole order."""
    refundable_credits_issued: list[int]
    """Credits already issued for refund for the whole order."""
    resend_reason: list[str]
    """Reason for resending the order."""
    resent_orders: list[list[Any]]
    """Orders that were resent to the customer"""
    resent_status: list[str]
    """Status of the resent order."""
    resource_version: list[int]
    """Version of the resource or order data."""
    rounding_adjustement: list[int]
    """Adjustment made for rounding off the order amount."""
    shipment_carrier: list[str]
    """Carrier for shipping the order."""
    shipped_at: list[int]
    """Timestamp when the order was shipped."""
    shipping_address: list[dict[str, Any]]
    """The shipping address for the order"""
    shipping_cut_off_date: list[int]
    """Date indicating the shipping cut-off for the order."""
    shipping_date: list[int]
    """Date when the order is scheduled for shipping."""
    status: list[str]
    """Current status of the order."""
    status_update_at: list[int]
    """Timestamp when the status of the order was last updated."""
    sub_total: list[int]
    """Sub-total amount for the order before applying taxes or discounts."""
    subscription_id: list[str]
    """Identifier for the subscription associated with the order."""
    tax: list[int]
    """Total tax amount for the order."""
    total: list[int]
    """Total amount including taxes and discounts for the order."""
    tracking_id: list[str]
    """Tracking identifier for the order shipment."""
    tracking_url: list[str]
    """URL for tracking the order shipment."""
    updated_at: list[int]
    """Timestamp when the order data was last updated."""


class OrderAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount_adjusted: Any
    """Adjusted amount for the order."""
    amount_paid: Any
    """Amount paid for the order."""
    base_currency_code: Any
    """The base currency code used for the order."""
    batch_id: Any
    """Unique identifier for the batch the order belongs to."""
    billing_address: Any
    """The billing address associated with the order"""
    business_entity_id: Any
    """Identifier for the business entity associated with the order."""
    cancellation_reason: Any
    """Reason for order cancellation."""
    cancelled_at: Any
    """Timestamp when the order was cancelled."""
    created_at: Any
    """Timestamp when the order was created."""
    created_by: Any
    """User or system that created the order."""
    currency_code: Any
    """Currency code used for the order."""
    custom_fields: Any
    """"""
    customer_id: Any
    """Identifier for the customer placing the order."""
    deleted: Any
    """Flag indicating if the order has been deleted."""
    delivered_at: Any
    """Timestamp when the order was delivered."""
    discount: Any
    """Discount amount applied to the order."""
    document_number: Any
    """Unique document number associated with the order."""
    exchange_rate: Any
    """Rate used for currency exchange in the order."""
    fulfillment_status: Any
    """Status of fulfillment for the order."""
    gift_id: Any
    """Identifier for any gift associated with the order."""
    gift_note: Any
    """Note attached to any gift in the order."""
    id: Any
    """Unique identifier for the order."""
    invoice_id: Any
    """Identifier for the invoice associated with the order."""
    invoice_round_off_amount: Any
    """Round-off amount applied to the invoice."""
    is_gifted: Any
    """Flag indicating if the order is a gift."""
    is_resent: Any
    """Flag indicating if the order has been resent."""
    line_item_discounts: Any
    """Discounts applied to individual line items"""
    line_item_taxes: Any
    """Taxes applied to individual line items"""
    linked_credit_notes: Any
    """Credit notes linked to the order"""
    note: Any
    """Additional notes or comments for the order."""
    object_: Any
    """Type of object representing an order in the system."""
    order_date: Any
    """Date when the order was created."""
    order_line_items: Any
    """List of line items in the order"""
    order_type: Any
    """Type of order such as purchase order or sales order."""
    original_order_id: Any
    """Identifier for the original order if this is a modified order."""
    paid_on: Any
    """Timestamp when the order was paid for."""
    payment_status: Any
    """Status of payment for the order."""
    price_type: Any
    """Type of pricing used for the order."""
    reference_id: Any
    """Reference identifier for the order."""
    refundable_credits: Any
    """Credits that can be refunded for the whole order."""
    refundable_credits_issued: Any
    """Credits already issued for refund for the whole order."""
    resend_reason: Any
    """Reason for resending the order."""
    resent_orders: Any
    """Orders that were resent to the customer"""
    resent_status: Any
    """Status of the resent order."""
    resource_version: Any
    """Version of the resource or order data."""
    rounding_adjustement: Any
    """Adjustment made for rounding off the order amount."""
    shipment_carrier: Any
    """Carrier for shipping the order."""
    shipped_at: Any
    """Timestamp when the order was shipped."""
    shipping_address: Any
    """The shipping address for the order"""
    shipping_cut_off_date: Any
    """Date indicating the shipping cut-off for the order."""
    shipping_date: Any
    """Date when the order is scheduled for shipping."""
    status: Any
    """Current status of the order."""
    status_update_at: Any
    """Timestamp when the status of the order was last updated."""
    sub_total: Any
    """Sub-total amount for the order before applying taxes or discounts."""
    subscription_id: Any
    """Identifier for the subscription associated with the order."""
    tax: Any
    """Total tax amount for the order."""
    total: Any
    """Total amount including taxes and discounts for the order."""
    tracking_id: Any
    """Tracking identifier for the order shipment."""
    tracking_url: Any
    """URL for tracking the order shipment."""
    updated_at: Any
    """Timestamp when the order data was last updated."""


class OrderStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount_adjusted: str
    """Adjusted amount for the order."""
    amount_paid: str
    """Amount paid for the order."""
    base_currency_code: str
    """The base currency code used for the order."""
    batch_id: str
    """Unique identifier for the batch the order belongs to."""
    billing_address: str
    """The billing address associated with the order"""
    business_entity_id: str
    """Identifier for the business entity associated with the order."""
    cancellation_reason: str
    """Reason for order cancellation."""
    cancelled_at: str
    """Timestamp when the order was cancelled."""
    created_at: str
    """Timestamp when the order was created."""
    created_by: str
    """User or system that created the order."""
    currency_code: str
    """Currency code used for the order."""
    custom_fields: str
    """"""
    customer_id: str
    """Identifier for the customer placing the order."""
    deleted: str
    """Flag indicating if the order has been deleted."""
    delivered_at: str
    """Timestamp when the order was delivered."""
    discount: str
    """Discount amount applied to the order."""
    document_number: str
    """Unique document number associated with the order."""
    exchange_rate: str
    """Rate used for currency exchange in the order."""
    fulfillment_status: str
    """Status of fulfillment for the order."""
    gift_id: str
    """Identifier for any gift associated with the order."""
    gift_note: str
    """Note attached to any gift in the order."""
    id: str
    """Unique identifier for the order."""
    invoice_id: str
    """Identifier for the invoice associated with the order."""
    invoice_round_off_amount: str
    """Round-off amount applied to the invoice."""
    is_gifted: str
    """Flag indicating if the order is a gift."""
    is_resent: str
    """Flag indicating if the order has been resent."""
    line_item_discounts: str
    """Discounts applied to individual line items"""
    line_item_taxes: str
    """Taxes applied to individual line items"""
    linked_credit_notes: str
    """Credit notes linked to the order"""
    note: str
    """Additional notes or comments for the order."""
    object_: str
    """Type of object representing an order in the system."""
    order_date: str
    """Date when the order was created."""
    order_line_items: str
    """List of line items in the order"""
    order_type: str
    """Type of order such as purchase order or sales order."""
    original_order_id: str
    """Identifier for the original order if this is a modified order."""
    paid_on: str
    """Timestamp when the order was paid for."""
    payment_status: str
    """Status of payment for the order."""
    price_type: str
    """Type of pricing used for the order."""
    reference_id: str
    """Reference identifier for the order."""
    refundable_credits: str
    """Credits that can be refunded for the whole order."""
    refundable_credits_issued: str
    """Credits already issued for refund for the whole order."""
    resend_reason: str
    """Reason for resending the order."""
    resent_orders: str
    """Orders that were resent to the customer"""
    resent_status: str
    """Status of the resent order."""
    resource_version: str
    """Version of the resource or order data."""
    rounding_adjustement: str
    """Adjustment made for rounding off the order amount."""
    shipment_carrier: str
    """Carrier for shipping the order."""
    shipped_at: str
    """Timestamp when the order was shipped."""
    shipping_address: str
    """The shipping address for the order"""
    shipping_cut_off_date: str
    """Date indicating the shipping cut-off for the order."""
    shipping_date: str
    """Date when the order is scheduled for shipping."""
    status: str
    """Current status of the order."""
    status_update_at: str
    """Timestamp when the status of the order was last updated."""
    sub_total: str
    """Sub-total amount for the order before applying taxes or discounts."""
    subscription_id: str
    """Identifier for the subscription associated with the order."""
    tax: str
    """Total tax amount for the order."""
    total: str
    """Total amount including taxes and discounts for the order."""
    tracking_id: str
    """Tracking identifier for the order shipment."""
    tracking_url: str
    """URL for tracking the order shipment."""
    updated_at: str
    """Timestamp when the order data was last updated."""


class OrderSortFilter(TypedDict, total=False):
    """Available fields for sorting order search results."""
    amount_adjusted: AirbyteSortOrder
    """Adjusted amount for the order."""
    amount_paid: AirbyteSortOrder
    """Amount paid for the order."""
    base_currency_code: AirbyteSortOrder
    """The base currency code used for the order."""
    batch_id: AirbyteSortOrder
    """Unique identifier for the batch the order belongs to."""
    billing_address: AirbyteSortOrder
    """The billing address associated with the order"""
    business_entity_id: AirbyteSortOrder
    """Identifier for the business entity associated with the order."""
    cancellation_reason: AirbyteSortOrder
    """Reason for order cancellation."""
    cancelled_at: AirbyteSortOrder
    """Timestamp when the order was cancelled."""
    created_at: AirbyteSortOrder
    """Timestamp when the order was created."""
    created_by: AirbyteSortOrder
    """User or system that created the order."""
    currency_code: AirbyteSortOrder
    """Currency code used for the order."""
    custom_fields: AirbyteSortOrder
    """"""
    customer_id: AirbyteSortOrder
    """Identifier for the customer placing the order."""
    deleted: AirbyteSortOrder
    """Flag indicating if the order has been deleted."""
    delivered_at: AirbyteSortOrder
    """Timestamp when the order was delivered."""
    discount: AirbyteSortOrder
    """Discount amount applied to the order."""
    document_number: AirbyteSortOrder
    """Unique document number associated with the order."""
    exchange_rate: AirbyteSortOrder
    """Rate used for currency exchange in the order."""
    fulfillment_status: AirbyteSortOrder
    """Status of fulfillment for the order."""
    gift_id: AirbyteSortOrder
    """Identifier for any gift associated with the order."""
    gift_note: AirbyteSortOrder
    """Note attached to any gift in the order."""
    id: AirbyteSortOrder
    """Unique identifier for the order."""
    invoice_id: AirbyteSortOrder
    """Identifier for the invoice associated with the order."""
    invoice_round_off_amount: AirbyteSortOrder
    """Round-off amount applied to the invoice."""
    is_gifted: AirbyteSortOrder
    """Flag indicating if the order is a gift."""
    is_resent: AirbyteSortOrder
    """Flag indicating if the order has been resent."""
    line_item_discounts: AirbyteSortOrder
    """Discounts applied to individual line items"""
    line_item_taxes: AirbyteSortOrder
    """Taxes applied to individual line items"""
    linked_credit_notes: AirbyteSortOrder
    """Credit notes linked to the order"""
    note: AirbyteSortOrder
    """Additional notes or comments for the order."""
    object_: AirbyteSortOrder
    """Type of object representing an order in the system."""
    order_date: AirbyteSortOrder
    """Date when the order was created."""
    order_line_items: AirbyteSortOrder
    """List of line items in the order"""
    order_type: AirbyteSortOrder
    """Type of order such as purchase order or sales order."""
    original_order_id: AirbyteSortOrder
    """Identifier for the original order if this is a modified order."""
    paid_on: AirbyteSortOrder
    """Timestamp when the order was paid for."""
    payment_status: AirbyteSortOrder
    """Status of payment for the order."""
    price_type: AirbyteSortOrder
    """Type of pricing used for the order."""
    reference_id: AirbyteSortOrder
    """Reference identifier for the order."""
    refundable_credits: AirbyteSortOrder
    """Credits that can be refunded for the whole order."""
    refundable_credits_issued: AirbyteSortOrder
    """Credits already issued for refund for the whole order."""
    resend_reason: AirbyteSortOrder
    """Reason for resending the order."""
    resent_orders: AirbyteSortOrder
    """Orders that were resent to the customer"""
    resent_status: AirbyteSortOrder
    """Status of the resent order."""
    resource_version: AirbyteSortOrder
    """Version of the resource or order data."""
    rounding_adjustement: AirbyteSortOrder
    """Adjustment made for rounding off the order amount."""
    shipment_carrier: AirbyteSortOrder
    """Carrier for shipping the order."""
    shipped_at: AirbyteSortOrder
    """Timestamp when the order was shipped."""
    shipping_address: AirbyteSortOrder
    """The shipping address for the order"""
    shipping_cut_off_date: AirbyteSortOrder
    """Date indicating the shipping cut-off for the order."""
    shipping_date: AirbyteSortOrder
    """Date when the order is scheduled for shipping."""
    status: AirbyteSortOrder
    """Current status of the order."""
    status_update_at: AirbyteSortOrder
    """Timestamp when the status of the order was last updated."""
    sub_total: AirbyteSortOrder
    """Sub-total amount for the order before applying taxes or discounts."""
    subscription_id: AirbyteSortOrder
    """Identifier for the subscription associated with the order."""
    tax: AirbyteSortOrder
    """Total tax amount for the order."""
    total: AirbyteSortOrder
    """Total amount including taxes and discounts for the order."""
    tracking_id: AirbyteSortOrder
    """Tracking identifier for the order shipment."""
    tracking_url: AirbyteSortOrder
    """URL for tracking the order shipment."""
    updated_at: AirbyteSortOrder
    """Timestamp when the order data was last updated."""


# Entity-specific condition types for order
class OrderEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrderSearchFilter


class OrderNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrderSearchFilter


class OrderGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrderSearchFilter


class OrderGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrderSearchFilter


class OrderLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrderSearchFilter


class OrderLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrderSearchFilter


class OrderLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrderStringFilter


class OrderFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrderStringFilter


class OrderKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrderStringFilter


class OrderContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrderAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrderInCondition = TypedDict("OrderInCondition", {"in": OrderInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrderNotCondition = TypedDict("OrderNotCondition", {"not": "OrderCondition"}, total=False)
"""Negates the nested condition."""

OrderAndCondition = TypedDict("OrderAndCondition", {"and": "list[OrderCondition]"}, total=False)
"""True if all nested conditions are true."""

OrderOrCondition = TypedDict("OrderOrCondition", {"or": "list[OrderCondition]"}, total=False)
"""True if any nested condition is true."""

OrderAnyCondition = TypedDict("OrderAnyCondition", {"any": OrderAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all order condition types
OrderCondition = (
    OrderEqCondition
    | OrderNeqCondition
    | OrderGtCondition
    | OrderGteCondition
    | OrderLtCondition
    | OrderLteCondition
    | OrderInCondition
    | OrderLikeCondition
    | OrderFuzzyCondition
    | OrderKeywordCondition
    | OrderContainsCondition
    | OrderNotCondition
    | OrderAndCondition
    | OrderOrCondition
    | OrderAnyCondition
)


class OrderSearchQuery(TypedDict, total=False):
    """Search query for order entity."""
    filter: OrderCondition
    sort: list[OrderSortFilter]


# ===== PAYMENT_SOURCE SEARCH TYPES =====

class PaymentSourceSearchFilter(TypedDict, total=False):
    """Available fields for filtering payment_source search queries."""
    amazon_payment: dict[str, Any] | None
    """Data related to Amazon Pay payment source"""
    bank_account: dict[str, Any] | None
    """Data related to bank account payment source"""
    business_entity_id: str | None
    """Identifier for the business entity associated with the payment source"""
    card: dict[str, Any] | None
    """Data related to card payment source"""
    created_at: int | None
    """Timestamp indicating when the payment source was created"""
    custom_fields: list[Any] | None
    """"""
    customer_id: str | None
    """Unique identifier for the customer associated with the payment source"""
    deleted: bool | None
    """Indicates if the payment source has been deleted"""
    gateway: str | None
    """Name of the payment gateway used for the payment source"""
    gateway_account_id: str | None
    """Identifier for the gateway account tied to the payment source"""
    id: str | None
    """Unique identifier for the payment source"""
    ip_address: str | None
    """IP address associated with the payment source"""
    issuing_country: str | None
    """Country where the payment source was issued"""
    mandates: dict[str, Any] | None
    """Data related to mandates for payments"""
    object_: str | None
    """Type of object, e.g., payment_source"""
    paypal: dict[str, Any] | None
    """Data related to PayPal payment source"""
    reference_id: str | None
    """Reference identifier for the payment source"""
    resource_version: int | None
    """Version of the payment source resource"""
    status: str | None
    """Status of the payment source, e.g., active or inactive"""
    type_: str | None
    """Type of payment source, e.g., card, bank_account"""
    updated_at: int | None
    """Timestamp indicating when the payment source was last updated"""
    upi: dict[str, Any] | None
    """Data related to UPI payment source"""


class PaymentSourceInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amazon_payment: list[dict[str, Any]]
    """Data related to Amazon Pay payment source"""
    bank_account: list[dict[str, Any]]
    """Data related to bank account payment source"""
    business_entity_id: list[str]
    """Identifier for the business entity associated with the payment source"""
    card: list[dict[str, Any]]
    """Data related to card payment source"""
    created_at: list[int]
    """Timestamp indicating when the payment source was created"""
    custom_fields: list[list[Any]]
    """"""
    customer_id: list[str]
    """Unique identifier for the customer associated with the payment source"""
    deleted: list[bool]
    """Indicates if the payment source has been deleted"""
    gateway: list[str]
    """Name of the payment gateway used for the payment source"""
    gateway_account_id: list[str]
    """Identifier for the gateway account tied to the payment source"""
    id: list[str]
    """Unique identifier for the payment source"""
    ip_address: list[str]
    """IP address associated with the payment source"""
    issuing_country: list[str]
    """Country where the payment source was issued"""
    mandates: list[dict[str, Any]]
    """Data related to mandates for payments"""
    object_: list[str]
    """Type of object, e.g., payment_source"""
    paypal: list[dict[str, Any]]
    """Data related to PayPal payment source"""
    reference_id: list[str]
    """Reference identifier for the payment source"""
    resource_version: list[int]
    """Version of the payment source resource"""
    status: list[str]
    """Status of the payment source, e.g., active or inactive"""
    type_: list[str]
    """Type of payment source, e.g., card, bank_account"""
    updated_at: list[int]
    """Timestamp indicating when the payment source was last updated"""
    upi: list[dict[str, Any]]
    """Data related to UPI payment source"""


class PaymentSourceAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amazon_payment: Any
    """Data related to Amazon Pay payment source"""
    bank_account: Any
    """Data related to bank account payment source"""
    business_entity_id: Any
    """Identifier for the business entity associated with the payment source"""
    card: Any
    """Data related to card payment source"""
    created_at: Any
    """Timestamp indicating when the payment source was created"""
    custom_fields: Any
    """"""
    customer_id: Any
    """Unique identifier for the customer associated with the payment source"""
    deleted: Any
    """Indicates if the payment source has been deleted"""
    gateway: Any
    """Name of the payment gateway used for the payment source"""
    gateway_account_id: Any
    """Identifier for the gateway account tied to the payment source"""
    id: Any
    """Unique identifier for the payment source"""
    ip_address: Any
    """IP address associated with the payment source"""
    issuing_country: Any
    """Country where the payment source was issued"""
    mandates: Any
    """Data related to mandates for payments"""
    object_: Any
    """Type of object, e.g., payment_source"""
    paypal: Any
    """Data related to PayPal payment source"""
    reference_id: Any
    """Reference identifier for the payment source"""
    resource_version: Any
    """Version of the payment source resource"""
    status: Any
    """Status of the payment source, e.g., active or inactive"""
    type_: Any
    """Type of payment source, e.g., card, bank_account"""
    updated_at: Any
    """Timestamp indicating when the payment source was last updated"""
    upi: Any
    """Data related to UPI payment source"""


class PaymentSourceStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amazon_payment: str
    """Data related to Amazon Pay payment source"""
    bank_account: str
    """Data related to bank account payment source"""
    business_entity_id: str
    """Identifier for the business entity associated with the payment source"""
    card: str
    """Data related to card payment source"""
    created_at: str
    """Timestamp indicating when the payment source was created"""
    custom_fields: str
    """"""
    customer_id: str
    """Unique identifier for the customer associated with the payment source"""
    deleted: str
    """Indicates if the payment source has been deleted"""
    gateway: str
    """Name of the payment gateway used for the payment source"""
    gateway_account_id: str
    """Identifier for the gateway account tied to the payment source"""
    id: str
    """Unique identifier for the payment source"""
    ip_address: str
    """IP address associated with the payment source"""
    issuing_country: str
    """Country where the payment source was issued"""
    mandates: str
    """Data related to mandates for payments"""
    object_: str
    """Type of object, e.g., payment_source"""
    paypal: str
    """Data related to PayPal payment source"""
    reference_id: str
    """Reference identifier for the payment source"""
    resource_version: str
    """Version of the payment source resource"""
    status: str
    """Status of the payment source, e.g., active or inactive"""
    type_: str
    """Type of payment source, e.g., card, bank_account"""
    updated_at: str
    """Timestamp indicating when the payment source was last updated"""
    upi: str
    """Data related to UPI payment source"""


class PaymentSourceSortFilter(TypedDict, total=False):
    """Available fields for sorting payment_source search results."""
    amazon_payment: AirbyteSortOrder
    """Data related to Amazon Pay payment source"""
    bank_account: AirbyteSortOrder
    """Data related to bank account payment source"""
    business_entity_id: AirbyteSortOrder
    """Identifier for the business entity associated with the payment source"""
    card: AirbyteSortOrder
    """Data related to card payment source"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the payment source was created"""
    custom_fields: AirbyteSortOrder
    """"""
    customer_id: AirbyteSortOrder
    """Unique identifier for the customer associated with the payment source"""
    deleted: AirbyteSortOrder
    """Indicates if the payment source has been deleted"""
    gateway: AirbyteSortOrder
    """Name of the payment gateway used for the payment source"""
    gateway_account_id: AirbyteSortOrder
    """Identifier for the gateway account tied to the payment source"""
    id: AirbyteSortOrder
    """Unique identifier for the payment source"""
    ip_address: AirbyteSortOrder
    """IP address associated with the payment source"""
    issuing_country: AirbyteSortOrder
    """Country where the payment source was issued"""
    mandates: AirbyteSortOrder
    """Data related to mandates for payments"""
    object_: AirbyteSortOrder
    """Type of object, e.g., payment_source"""
    paypal: AirbyteSortOrder
    """Data related to PayPal payment source"""
    reference_id: AirbyteSortOrder
    """Reference identifier for the payment source"""
    resource_version: AirbyteSortOrder
    """Version of the payment source resource"""
    status: AirbyteSortOrder
    """Status of the payment source, e.g., active or inactive"""
    type_: AirbyteSortOrder
    """Type of payment source, e.g., card, bank_account"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the payment source was last updated"""
    upi: AirbyteSortOrder
    """Data related to UPI payment source"""


# Entity-specific condition types for payment_source
class PaymentSourceEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PaymentSourceSearchFilter


class PaymentSourceNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PaymentSourceSearchFilter


class PaymentSourceGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PaymentSourceSearchFilter


class PaymentSourceGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PaymentSourceSearchFilter


class PaymentSourceLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PaymentSourceSearchFilter


class PaymentSourceLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PaymentSourceSearchFilter


class PaymentSourceLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PaymentSourceStringFilter


class PaymentSourceFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PaymentSourceStringFilter


class PaymentSourceKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PaymentSourceStringFilter


class PaymentSourceContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PaymentSourceAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PaymentSourceInCondition = TypedDict("PaymentSourceInCondition", {"in": PaymentSourceInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PaymentSourceNotCondition = TypedDict("PaymentSourceNotCondition", {"not": "PaymentSourceCondition"}, total=False)
"""Negates the nested condition."""

PaymentSourceAndCondition = TypedDict("PaymentSourceAndCondition", {"and": "list[PaymentSourceCondition]"}, total=False)
"""True if all nested conditions are true."""

PaymentSourceOrCondition = TypedDict("PaymentSourceOrCondition", {"or": "list[PaymentSourceCondition]"}, total=False)
"""True if any nested condition is true."""

PaymentSourceAnyCondition = TypedDict("PaymentSourceAnyCondition", {"any": PaymentSourceAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all payment_source condition types
PaymentSourceCondition = (
    PaymentSourceEqCondition
    | PaymentSourceNeqCondition
    | PaymentSourceGtCondition
    | PaymentSourceGteCondition
    | PaymentSourceLtCondition
    | PaymentSourceLteCondition
    | PaymentSourceInCondition
    | PaymentSourceLikeCondition
    | PaymentSourceFuzzyCondition
    | PaymentSourceKeywordCondition
    | PaymentSourceContainsCondition
    | PaymentSourceNotCondition
    | PaymentSourceAndCondition
    | PaymentSourceOrCondition
    | PaymentSourceAnyCondition
)


class PaymentSourceSearchQuery(TypedDict, total=False):
    """Search query for payment_source entity."""
    filter: PaymentSourceCondition
    sort: list[PaymentSourceSortFilter]


# ===== ITEM SEARCH TYPES =====

class ItemSearchFilter(TypedDict, total=False):
    """Available fields for filtering item search queries."""
    applicable_items: list[Any] | None
    """Items associated with the item"""
    archived_at: int | None
    """Date and time when the item was archived"""
    channel: str | None
    """Channel the item belongs to"""
    custom_fields: list[Any] | None
    """Custom field entries for the item"""
    description: str | None
    """Description of the item"""
    enabled_for_checkout: bool | None
    """Flag indicating if the item is enabled for checkout"""
    enabled_in_portal: bool | None
    """Flag indicating if the item is enabled in the portal"""
    external_name: str | None
    """Name of the item in an external system"""
    gift_claim_redirect_url: str | None
    """URL to redirect for gift claim"""
    id: str | None
    """Unique identifier for the item"""
    included_in_mrr: bool | None
    """Flag indicating if the item is included in Monthly Recurring Revenue"""
    is_giftable: bool | None
    """Flag indicating if the item is giftable"""
    is_shippable: bool | None
    """Flag indicating if the item is shippable"""
    item_applicability: str | None
    """Applicability of the item"""
    item_family_id: str | None
    """ID of the item's family"""
    metadata: dict[str, Any] | None
    """Additional data associated with the item"""
    metered: bool | None
    """Flag indicating if the item is metered"""
    name: str | None
    """Name of the item"""
    object_: str | None
    """Type of object"""
    redirect_url: str | None
    """URL to redirect for the item"""
    resource_version: int | None
    """Version of the resource"""
    status: str | None
    """Status of the item"""
    type_: str | None
    """Type of the item"""
    unit: str | None
    """Unit associated with the item"""
    updated_at: int | None
    """Date and time when the item was last updated"""
    usage_calculation: str | None
    """Calculation method used for item usage"""


class ItemInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    applicable_items: list[list[Any]]
    """Items associated with the item"""
    archived_at: list[int]
    """Date and time when the item was archived"""
    channel: list[str]
    """Channel the item belongs to"""
    custom_fields: list[list[Any]]
    """Custom field entries for the item"""
    description: list[str]
    """Description of the item"""
    enabled_for_checkout: list[bool]
    """Flag indicating if the item is enabled for checkout"""
    enabled_in_portal: list[bool]
    """Flag indicating if the item is enabled in the portal"""
    external_name: list[str]
    """Name of the item in an external system"""
    gift_claim_redirect_url: list[str]
    """URL to redirect for gift claim"""
    id: list[str]
    """Unique identifier for the item"""
    included_in_mrr: list[bool]
    """Flag indicating if the item is included in Monthly Recurring Revenue"""
    is_giftable: list[bool]
    """Flag indicating if the item is giftable"""
    is_shippable: list[bool]
    """Flag indicating if the item is shippable"""
    item_applicability: list[str]
    """Applicability of the item"""
    item_family_id: list[str]
    """ID of the item's family"""
    metadata: list[dict[str, Any]]
    """Additional data associated with the item"""
    metered: list[bool]
    """Flag indicating if the item is metered"""
    name: list[str]
    """Name of the item"""
    object_: list[str]
    """Type of object"""
    redirect_url: list[str]
    """URL to redirect for the item"""
    resource_version: list[int]
    """Version of the resource"""
    status: list[str]
    """Status of the item"""
    type_: list[str]
    """Type of the item"""
    unit: list[str]
    """Unit associated with the item"""
    updated_at: list[int]
    """Date and time when the item was last updated"""
    usage_calculation: list[str]
    """Calculation method used for item usage"""


class ItemAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    applicable_items: Any
    """Items associated with the item"""
    archived_at: Any
    """Date and time when the item was archived"""
    channel: Any
    """Channel the item belongs to"""
    custom_fields: Any
    """Custom field entries for the item"""
    description: Any
    """Description of the item"""
    enabled_for_checkout: Any
    """Flag indicating if the item is enabled for checkout"""
    enabled_in_portal: Any
    """Flag indicating if the item is enabled in the portal"""
    external_name: Any
    """Name of the item in an external system"""
    gift_claim_redirect_url: Any
    """URL to redirect for gift claim"""
    id: Any
    """Unique identifier for the item"""
    included_in_mrr: Any
    """Flag indicating if the item is included in Monthly Recurring Revenue"""
    is_giftable: Any
    """Flag indicating if the item is giftable"""
    is_shippable: Any
    """Flag indicating if the item is shippable"""
    item_applicability: Any
    """Applicability of the item"""
    item_family_id: Any
    """ID of the item's family"""
    metadata: Any
    """Additional data associated with the item"""
    metered: Any
    """Flag indicating if the item is metered"""
    name: Any
    """Name of the item"""
    object_: Any
    """Type of object"""
    redirect_url: Any
    """URL to redirect for the item"""
    resource_version: Any
    """Version of the resource"""
    status: Any
    """Status of the item"""
    type_: Any
    """Type of the item"""
    unit: Any
    """Unit associated with the item"""
    updated_at: Any
    """Date and time when the item was last updated"""
    usage_calculation: Any
    """Calculation method used for item usage"""


class ItemStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    applicable_items: str
    """Items associated with the item"""
    archived_at: str
    """Date and time when the item was archived"""
    channel: str
    """Channel the item belongs to"""
    custom_fields: str
    """Custom field entries for the item"""
    description: str
    """Description of the item"""
    enabled_for_checkout: str
    """Flag indicating if the item is enabled for checkout"""
    enabled_in_portal: str
    """Flag indicating if the item is enabled in the portal"""
    external_name: str
    """Name of the item in an external system"""
    gift_claim_redirect_url: str
    """URL to redirect for gift claim"""
    id: str
    """Unique identifier for the item"""
    included_in_mrr: str
    """Flag indicating if the item is included in Monthly Recurring Revenue"""
    is_giftable: str
    """Flag indicating if the item is giftable"""
    is_shippable: str
    """Flag indicating if the item is shippable"""
    item_applicability: str
    """Applicability of the item"""
    item_family_id: str
    """ID of the item's family"""
    metadata: str
    """Additional data associated with the item"""
    metered: str
    """Flag indicating if the item is metered"""
    name: str
    """Name of the item"""
    object_: str
    """Type of object"""
    redirect_url: str
    """URL to redirect for the item"""
    resource_version: str
    """Version of the resource"""
    status: str
    """Status of the item"""
    type_: str
    """Type of the item"""
    unit: str
    """Unit associated with the item"""
    updated_at: str
    """Date and time when the item was last updated"""
    usage_calculation: str
    """Calculation method used for item usage"""


class ItemSortFilter(TypedDict, total=False):
    """Available fields for sorting item search results."""
    applicable_items: AirbyteSortOrder
    """Items associated with the item"""
    archived_at: AirbyteSortOrder
    """Date and time when the item was archived"""
    channel: AirbyteSortOrder
    """Channel the item belongs to"""
    custom_fields: AirbyteSortOrder
    """Custom field entries for the item"""
    description: AirbyteSortOrder
    """Description of the item"""
    enabled_for_checkout: AirbyteSortOrder
    """Flag indicating if the item is enabled for checkout"""
    enabled_in_portal: AirbyteSortOrder
    """Flag indicating if the item is enabled in the portal"""
    external_name: AirbyteSortOrder
    """Name of the item in an external system"""
    gift_claim_redirect_url: AirbyteSortOrder
    """URL to redirect for gift claim"""
    id: AirbyteSortOrder
    """Unique identifier for the item"""
    included_in_mrr: AirbyteSortOrder
    """Flag indicating if the item is included in Monthly Recurring Revenue"""
    is_giftable: AirbyteSortOrder
    """Flag indicating if the item is giftable"""
    is_shippable: AirbyteSortOrder
    """Flag indicating if the item is shippable"""
    item_applicability: AirbyteSortOrder
    """Applicability of the item"""
    item_family_id: AirbyteSortOrder
    """ID of the item's family"""
    metadata: AirbyteSortOrder
    """Additional data associated with the item"""
    metered: AirbyteSortOrder
    """Flag indicating if the item is metered"""
    name: AirbyteSortOrder
    """Name of the item"""
    object_: AirbyteSortOrder
    """Type of object"""
    redirect_url: AirbyteSortOrder
    """URL to redirect for the item"""
    resource_version: AirbyteSortOrder
    """Version of the resource"""
    status: AirbyteSortOrder
    """Status of the item"""
    type_: AirbyteSortOrder
    """Type of the item"""
    unit: AirbyteSortOrder
    """Unit associated with the item"""
    updated_at: AirbyteSortOrder
    """Date and time when the item was last updated"""
    usage_calculation: AirbyteSortOrder
    """Calculation method used for item usage"""


# Entity-specific condition types for item
class ItemEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ItemSearchFilter


class ItemNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ItemSearchFilter


class ItemGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ItemSearchFilter


class ItemGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ItemSearchFilter


class ItemLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ItemSearchFilter


class ItemLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ItemSearchFilter


class ItemLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ItemStringFilter


class ItemFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ItemStringFilter


class ItemKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ItemStringFilter


class ItemContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ItemAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ItemInCondition = TypedDict("ItemInCondition", {"in": ItemInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ItemNotCondition = TypedDict("ItemNotCondition", {"not": "ItemCondition"}, total=False)
"""Negates the nested condition."""

ItemAndCondition = TypedDict("ItemAndCondition", {"and": "list[ItemCondition]"}, total=False)
"""True if all nested conditions are true."""

ItemOrCondition = TypedDict("ItemOrCondition", {"or": "list[ItemCondition]"}, total=False)
"""True if any nested condition is true."""

ItemAnyCondition = TypedDict("ItemAnyCondition", {"any": ItemAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all item condition types
ItemCondition = (
    ItemEqCondition
    | ItemNeqCondition
    | ItemGtCondition
    | ItemGteCondition
    | ItemLtCondition
    | ItemLteCondition
    | ItemInCondition
    | ItemLikeCondition
    | ItemFuzzyCondition
    | ItemKeywordCondition
    | ItemContainsCondition
    | ItemNotCondition
    | ItemAndCondition
    | ItemOrCondition
    | ItemAnyCondition
)


class ItemSearchQuery(TypedDict, total=False):
    """Search query for item entity."""
    filter: ItemCondition
    sort: list[ItemSortFilter]


# ===== ITEM_PRICE SEARCH TYPES =====

class ItemPriceSearchFilter(TypedDict, total=False):
    """Available fields for filtering item_price search queries."""
    accounting_detail: dict[str, Any] | None
    """Details related to accounting such as cost, revenue, expenses, etc."""
    archived_at: int | None
    """Date and time when the item was archived."""
    billing_cycles: int | None
    """Number of billing cycles for the item."""
    channel: str | None
    """The channel through which the item is sold."""
    created_at: int | None
    """Date and time when the item was created."""
    currency_code: str | None
    """The currency code used for pricing the item."""
    custom_fields: list[Any] | None
    """Custom field entries for the item price."""
    description: str | None
    """Description of the item."""
    external_name: str | None
    """External name of the item."""
    free_quantity: int | None
    """Free quantity allowed for the item."""
    free_quantity_in_decimal: str | None
    """Free quantity allowed represented in decimal format."""
    id: str | None
    """Unique identifier for the item price."""
    invoice_notes: str | None
    """Notes to be included in the invoice for the item."""
    is_taxable: bool | None
    """Flag indicating whether the item is taxable."""
    item_family_id: str | None
    """Identifier for the item family to which the item belongs."""
    item_id: str | None
    """Unique identifier for the parent item."""
    item_type: str | None
    """Type of the item (e.g., product, service)."""
    metadata: dict[str, Any] | None
    """Additional metadata associated with the item."""
    name: str | None
    """Name of the item price."""
    object_: str | None
    """Object type representing the item price."""
    period: int | None
    """Duration of the item's billing period."""
    period_unit: str | None
    """Unit of measurement for the billing period duration."""
    price: int | None
    """Price of the item."""
    price_in_decimal: str | None
    """Price of the item represented in decimal format."""
    pricing_model: str | None
    """The pricing model used for the item (e.g., flat fee, usage-based)."""
    resource_version: int | None
    """Version of the item price resource."""
    shipping_period: int | None
    """Duration of the item's shipping period."""
    shipping_period_unit: str | None
    """Unit of measurement for the shipping period duration."""
    show_description_in_invoices: bool | None
    """Flag indicating whether to show the description in invoices."""
    show_description_in_quotes: bool | None
    """Flag indicating whether to show the description in quotes."""
    status: str | None
    """Current status of the item price (e.g., active, inactive)."""
    tax_detail: dict[str, Any] | None
    """Information about taxes associated with the item price."""
    tiers: list[Any] | None
    """Different pricing tiers for the item."""
    trial_end_action: str | None
    """Action to be taken at the end of the trial period."""
    trial_period: int | None
    """Duration of the trial period."""
    trial_period_unit: str | None
    """Unit of measurement for the trial period duration."""
    updated_at: int | None
    """Date and time when the item price was last updated."""


class ItemPriceInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    accounting_detail: list[dict[str, Any]]
    """Details related to accounting such as cost, revenue, expenses, etc."""
    archived_at: list[int]
    """Date and time when the item was archived."""
    billing_cycles: list[int]
    """Number of billing cycles for the item."""
    channel: list[str]
    """The channel through which the item is sold."""
    created_at: list[int]
    """Date and time when the item was created."""
    currency_code: list[str]
    """The currency code used for pricing the item."""
    custom_fields: list[list[Any]]
    """Custom field entries for the item price."""
    description: list[str]
    """Description of the item."""
    external_name: list[str]
    """External name of the item."""
    free_quantity: list[int]
    """Free quantity allowed for the item."""
    free_quantity_in_decimal: list[str]
    """Free quantity allowed represented in decimal format."""
    id: list[str]
    """Unique identifier for the item price."""
    invoice_notes: list[str]
    """Notes to be included in the invoice for the item."""
    is_taxable: list[bool]
    """Flag indicating whether the item is taxable."""
    item_family_id: list[str]
    """Identifier for the item family to which the item belongs."""
    item_id: list[str]
    """Unique identifier for the parent item."""
    item_type: list[str]
    """Type of the item (e.g., product, service)."""
    metadata: list[dict[str, Any]]
    """Additional metadata associated with the item."""
    name: list[str]
    """Name of the item price."""
    object_: list[str]
    """Object type representing the item price."""
    period: list[int]
    """Duration of the item's billing period."""
    period_unit: list[str]
    """Unit of measurement for the billing period duration."""
    price: list[int]
    """Price of the item."""
    price_in_decimal: list[str]
    """Price of the item represented in decimal format."""
    pricing_model: list[str]
    """The pricing model used for the item (e.g., flat fee, usage-based)."""
    resource_version: list[int]
    """Version of the item price resource."""
    shipping_period: list[int]
    """Duration of the item's shipping period."""
    shipping_period_unit: list[str]
    """Unit of measurement for the shipping period duration."""
    show_description_in_invoices: list[bool]
    """Flag indicating whether to show the description in invoices."""
    show_description_in_quotes: list[bool]
    """Flag indicating whether to show the description in quotes."""
    status: list[str]
    """Current status of the item price (e.g., active, inactive)."""
    tax_detail: list[dict[str, Any]]
    """Information about taxes associated with the item price."""
    tiers: list[list[Any]]
    """Different pricing tiers for the item."""
    trial_end_action: list[str]
    """Action to be taken at the end of the trial period."""
    trial_period: list[int]
    """Duration of the trial period."""
    trial_period_unit: list[str]
    """Unit of measurement for the trial period duration."""
    updated_at: list[int]
    """Date and time when the item price was last updated."""


class ItemPriceAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    accounting_detail: Any
    """Details related to accounting such as cost, revenue, expenses, etc."""
    archived_at: Any
    """Date and time when the item was archived."""
    billing_cycles: Any
    """Number of billing cycles for the item."""
    channel: Any
    """The channel through which the item is sold."""
    created_at: Any
    """Date and time when the item was created."""
    currency_code: Any
    """The currency code used for pricing the item."""
    custom_fields: Any
    """Custom field entries for the item price."""
    description: Any
    """Description of the item."""
    external_name: Any
    """External name of the item."""
    free_quantity: Any
    """Free quantity allowed for the item."""
    free_quantity_in_decimal: Any
    """Free quantity allowed represented in decimal format."""
    id: Any
    """Unique identifier for the item price."""
    invoice_notes: Any
    """Notes to be included in the invoice for the item."""
    is_taxable: Any
    """Flag indicating whether the item is taxable."""
    item_family_id: Any
    """Identifier for the item family to which the item belongs."""
    item_id: Any
    """Unique identifier for the parent item."""
    item_type: Any
    """Type of the item (e.g., product, service)."""
    metadata: Any
    """Additional metadata associated with the item."""
    name: Any
    """Name of the item price."""
    object_: Any
    """Object type representing the item price."""
    period: Any
    """Duration of the item's billing period."""
    period_unit: Any
    """Unit of measurement for the billing period duration."""
    price: Any
    """Price of the item."""
    price_in_decimal: Any
    """Price of the item represented in decimal format."""
    pricing_model: Any
    """The pricing model used for the item (e.g., flat fee, usage-based)."""
    resource_version: Any
    """Version of the item price resource."""
    shipping_period: Any
    """Duration of the item's shipping period."""
    shipping_period_unit: Any
    """Unit of measurement for the shipping period duration."""
    show_description_in_invoices: Any
    """Flag indicating whether to show the description in invoices."""
    show_description_in_quotes: Any
    """Flag indicating whether to show the description in quotes."""
    status: Any
    """Current status of the item price (e.g., active, inactive)."""
    tax_detail: Any
    """Information about taxes associated with the item price."""
    tiers: Any
    """Different pricing tiers for the item."""
    trial_end_action: Any
    """Action to be taken at the end of the trial period."""
    trial_period: Any
    """Duration of the trial period."""
    trial_period_unit: Any
    """Unit of measurement for the trial period duration."""
    updated_at: Any
    """Date and time when the item price was last updated."""


class ItemPriceStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    accounting_detail: str
    """Details related to accounting such as cost, revenue, expenses, etc."""
    archived_at: str
    """Date and time when the item was archived."""
    billing_cycles: str
    """Number of billing cycles for the item."""
    channel: str
    """The channel through which the item is sold."""
    created_at: str
    """Date and time when the item was created."""
    currency_code: str
    """The currency code used for pricing the item."""
    custom_fields: str
    """Custom field entries for the item price."""
    description: str
    """Description of the item."""
    external_name: str
    """External name of the item."""
    free_quantity: str
    """Free quantity allowed for the item."""
    free_quantity_in_decimal: str
    """Free quantity allowed represented in decimal format."""
    id: str
    """Unique identifier for the item price."""
    invoice_notes: str
    """Notes to be included in the invoice for the item."""
    is_taxable: str
    """Flag indicating whether the item is taxable."""
    item_family_id: str
    """Identifier for the item family to which the item belongs."""
    item_id: str
    """Unique identifier for the parent item."""
    item_type: str
    """Type of the item (e.g., product, service)."""
    metadata: str
    """Additional metadata associated with the item."""
    name: str
    """Name of the item price."""
    object_: str
    """Object type representing the item price."""
    period: str
    """Duration of the item's billing period."""
    period_unit: str
    """Unit of measurement for the billing period duration."""
    price: str
    """Price of the item."""
    price_in_decimal: str
    """Price of the item represented in decimal format."""
    pricing_model: str
    """The pricing model used for the item (e.g., flat fee, usage-based)."""
    resource_version: str
    """Version of the item price resource."""
    shipping_period: str
    """Duration of the item's shipping period."""
    shipping_period_unit: str
    """Unit of measurement for the shipping period duration."""
    show_description_in_invoices: str
    """Flag indicating whether to show the description in invoices."""
    show_description_in_quotes: str
    """Flag indicating whether to show the description in quotes."""
    status: str
    """Current status of the item price (e.g., active, inactive)."""
    tax_detail: str
    """Information about taxes associated with the item price."""
    tiers: str
    """Different pricing tiers for the item."""
    trial_end_action: str
    """Action to be taken at the end of the trial period."""
    trial_period: str
    """Duration of the trial period."""
    trial_period_unit: str
    """Unit of measurement for the trial period duration."""
    updated_at: str
    """Date and time when the item price was last updated."""


class ItemPriceSortFilter(TypedDict, total=False):
    """Available fields for sorting item_price search results."""
    accounting_detail: AirbyteSortOrder
    """Details related to accounting such as cost, revenue, expenses, etc."""
    archived_at: AirbyteSortOrder
    """Date and time when the item was archived."""
    billing_cycles: AirbyteSortOrder
    """Number of billing cycles for the item."""
    channel: AirbyteSortOrder
    """The channel through which the item is sold."""
    created_at: AirbyteSortOrder
    """Date and time when the item was created."""
    currency_code: AirbyteSortOrder
    """The currency code used for pricing the item."""
    custom_fields: AirbyteSortOrder
    """Custom field entries for the item price."""
    description: AirbyteSortOrder
    """Description of the item."""
    external_name: AirbyteSortOrder
    """External name of the item."""
    free_quantity: AirbyteSortOrder
    """Free quantity allowed for the item."""
    free_quantity_in_decimal: AirbyteSortOrder
    """Free quantity allowed represented in decimal format."""
    id: AirbyteSortOrder
    """Unique identifier for the item price."""
    invoice_notes: AirbyteSortOrder
    """Notes to be included in the invoice for the item."""
    is_taxable: AirbyteSortOrder
    """Flag indicating whether the item is taxable."""
    item_family_id: AirbyteSortOrder
    """Identifier for the item family to which the item belongs."""
    item_id: AirbyteSortOrder
    """Unique identifier for the parent item."""
    item_type: AirbyteSortOrder
    """Type of the item (e.g., product, service)."""
    metadata: AirbyteSortOrder
    """Additional metadata associated with the item."""
    name: AirbyteSortOrder
    """Name of the item price."""
    object_: AirbyteSortOrder
    """Object type representing the item price."""
    period: AirbyteSortOrder
    """Duration of the item's billing period."""
    period_unit: AirbyteSortOrder
    """Unit of measurement for the billing period duration."""
    price: AirbyteSortOrder
    """Price of the item."""
    price_in_decimal: AirbyteSortOrder
    """Price of the item represented in decimal format."""
    pricing_model: AirbyteSortOrder
    """The pricing model used for the item (e.g., flat fee, usage-based)."""
    resource_version: AirbyteSortOrder
    """Version of the item price resource."""
    shipping_period: AirbyteSortOrder
    """Duration of the item's shipping period."""
    shipping_period_unit: AirbyteSortOrder
    """Unit of measurement for the shipping period duration."""
    show_description_in_invoices: AirbyteSortOrder
    """Flag indicating whether to show the description in invoices."""
    show_description_in_quotes: AirbyteSortOrder
    """Flag indicating whether to show the description in quotes."""
    status: AirbyteSortOrder
    """Current status of the item price (e.g., active, inactive)."""
    tax_detail: AirbyteSortOrder
    """Information about taxes associated with the item price."""
    tiers: AirbyteSortOrder
    """Different pricing tiers for the item."""
    trial_end_action: AirbyteSortOrder
    """Action to be taken at the end of the trial period."""
    trial_period: AirbyteSortOrder
    """Duration of the trial period."""
    trial_period_unit: AirbyteSortOrder
    """Unit of measurement for the trial period duration."""
    updated_at: AirbyteSortOrder
    """Date and time when the item price was last updated."""


# Entity-specific condition types for item_price
class ItemPriceEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ItemPriceSearchFilter


class ItemPriceNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ItemPriceSearchFilter


class ItemPriceGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ItemPriceSearchFilter


class ItemPriceGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ItemPriceSearchFilter


class ItemPriceLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ItemPriceSearchFilter


class ItemPriceLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ItemPriceSearchFilter


class ItemPriceLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ItemPriceStringFilter


class ItemPriceFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ItemPriceStringFilter


class ItemPriceKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ItemPriceStringFilter


class ItemPriceContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ItemPriceAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ItemPriceInCondition = TypedDict("ItemPriceInCondition", {"in": ItemPriceInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ItemPriceNotCondition = TypedDict("ItemPriceNotCondition", {"not": "ItemPriceCondition"}, total=False)
"""Negates the nested condition."""

ItemPriceAndCondition = TypedDict("ItemPriceAndCondition", {"and": "list[ItemPriceCondition]"}, total=False)
"""True if all nested conditions are true."""

ItemPriceOrCondition = TypedDict("ItemPriceOrCondition", {"or": "list[ItemPriceCondition]"}, total=False)
"""True if any nested condition is true."""

ItemPriceAnyCondition = TypedDict("ItemPriceAnyCondition", {"any": ItemPriceAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all item_price condition types
ItemPriceCondition = (
    ItemPriceEqCondition
    | ItemPriceNeqCondition
    | ItemPriceGtCondition
    | ItemPriceGteCondition
    | ItemPriceLtCondition
    | ItemPriceLteCondition
    | ItemPriceInCondition
    | ItemPriceLikeCondition
    | ItemPriceFuzzyCondition
    | ItemPriceKeywordCondition
    | ItemPriceContainsCondition
    | ItemPriceNotCondition
    | ItemPriceAndCondition
    | ItemPriceOrCondition
    | ItemPriceAnyCondition
)


class ItemPriceSearchQuery(TypedDict, total=False):
    """Search query for item_price entity."""
    filter: ItemPriceCondition
    sort: list[ItemPriceSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
