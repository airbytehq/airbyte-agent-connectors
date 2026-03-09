"""
Pydantic models for chargebee connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class ChargebeeAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Chargebee API key (used as the HTTP Basic username)"""

# Replication configuration

class ChargebeeReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Chargebee."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ. Data before this date is excluded."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Customer(BaseModel):
    """Chargebee customer object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    first_name: Union[str, Any] = Field(default=None)
    last_name: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    phone: Union[str, Any] = Field(default=None)
    company: Union[str, Any] = Field(default=None)
    vat_number: Union[str, Any] = Field(default=None)
    auto_collection: Union[str, Any] = Field(default=None)
    offline_payment_method: Union[str, Any] = Field(default=None)
    net_term_days: Union[int, Any] = Field(default=None)
    vat_number_validated_time: Union[int, Any] = Field(default=None)
    vat_number_status: Union[str, Any] = Field(default=None)
    allow_direct_debit: Union[bool, Any] = Field(default=None)
    is_location_valid: Union[bool, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)
    created_from_ip: Union[str, Any] = Field(default=None)
    taxability: Union[str, Any] = Field(default=None)
    entity_code: Union[str, Any] = Field(default=None)
    exempt_number: Union[str, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    locale: Union[str, Any] = Field(default=None)
    billing_date: Union[int, Any] = Field(default=None)
    billing_date_mode: Union[str, Any] = Field(default=None)
    billing_day_of_week: Union[str, Any] = Field(default=None)
    billing_day_of_week_mode: Union[str, Any] = Field(default=None)
    billing_month: Union[int, Any] = Field(default=None)
    pii_cleared: Union[str, Any] = Field(default=None)
    auto_close_invoices: Union[bool, Any] = Field(default=None)
    channel: Union[str, Any] = Field(default=None)
    fraud_flag: Union[str, Any] = Field(default=None)
    primary_payment_source_id: Union[str, Any] = Field(default=None)
    backup_payment_source_id: Union[str, Any] = Field(default=None)
    invoice_notes: Union[str, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    preferred_currency_code: Union[str, Any] = Field(default=None)
    promotional_credits: Union[int, Any] = Field(default=None)
    unbilled_charges: Union[int, Any] = Field(default=None)
    refundable_credits: Union[int, Any] = Field(default=None)
    excess_payments: Union[int, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    registered_for_gst: Union[bool, Any] = Field(default=None)
    consolidated_invoicing: Union[bool, Any] = Field(default=None)
    customer_type: Union[str, Any] = Field(default=None)
    business_customer_without_vat_number: Union[bool, Any] = Field(default=None)
    client_profile_id: Union[str, Any] = Field(default=None)
    use_default_hierarchy_settings: Union[bool, Any] = Field(default=None)
    vat_number_prefix: Union[str, Any] = Field(default=None)
    billing_address: Union[dict[str, Any], Any] = Field(default=None)
    referral_urls: Union[list[dict[str, Any]], Any] = Field(default=None)
    contacts: Union[list[dict[str, Any]], Any] = Field(default=None)
    payment_method: Union[dict[str, Any], Any] = Field(default=None)
    balances: Union[list[dict[str, Any]], Any] = Field(default=None)
    relationship: Union[dict[str, Any], Any] = Field(default=None)
    parent_account_access: Union[dict[str, Any], Any] = Field(default=None)
    child_account_access: Union[dict[str, Any], Any] = Field(default=None)
    meta_data: Union[dict[str, Any], Any] = Field(default=None)
    mrr: Union[int, Any] = Field(default=None)
    exemption_details: Union[list[dict[str, Any]], Any] = Field(default=None)
    tax_providers_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    card_status: Union[str, Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)

class CustomerListListItem(BaseModel):
    """Nested schema for CustomerList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer: Union[Customer, Any] = Field(default=None)

class CustomerList(BaseModel):
    """Paginated list of customers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[CustomerListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Subscription(BaseModel):
    """Chargebee subscription object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    customer_id: Union[str, Any] = Field(default=None)
    plan_id: Union[str, Any] = Field(default=None)
    plan_quantity: Union[int, Any] = Field(default=None)
    plan_unit_price: Union[int, Any] = Field(default=None)
    plan_amount: Union[int, Any] = Field(default=None)
    plan_free_quantity: Union[int, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    trial_start: Union[int, Any] = Field(default=None)
    trial_end: Union[int, Any] = Field(default=None)
    current_term_start: Union[int, Any] = Field(default=None)
    current_term_end: Union[int, Any] = Field(default=None)
    next_billing_at: Union[int, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)
    started_at: Union[int, Any] = Field(default=None)
    activated_at: Union[int, Any] = Field(default=None)
    cancelled_at: Union[int, Any] = Field(default=None)
    cancel_reason: Union[str, Any] = Field(default=None)
    channel: Union[str, Any] = Field(default=None)
    billing_period: Union[int, Any] = Field(default=None)
    billing_period_unit: Union[str, Any] = Field(default=None)
    auto_collection: Union[str, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    remaining_billing_cycles: Union[int, Any] = Field(default=None)
    po_number: Union[str, Any] = Field(default=None)
    created_from_ip: Union[str, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    has_scheduled_changes: Union[bool, Any] = Field(default=None)
    payment_source_id: Union[str, Any] = Field(default=None)
    plan_free_quantity_in_decimal: Union[str, Any] = Field(default=None)
    plan_quantity_in_decimal: Union[str, Any] = Field(default=None)
    plan_unit_price_in_decimal: Union[str, Any] = Field(default=None)
    plan_amount_in_decimal: Union[str, Any] = Field(default=None)
    due_invoices_count: Union[int, Any] = Field(default=None)
    due_since: Union[int, Any] = Field(default=None)
    total_dues: Union[int, Any] = Field(default=None)
    mrr: Union[int, Any] = Field(default=None)
    exchange_rate: Union[float, Any] = Field(default=None)
    base_currency_code: Union[str, Any] = Field(default=None)
    override_relationship: Union[bool, Any] = Field(default=None)
    trial_end_action: Union[str, Any] = Field(default=None)
    pause_date: Union[int, Any] = Field(default=None)
    resume_date: Union[int, Any] = Field(default=None)
    cancelled_at_term_end: Union[bool, Any] = Field(default=None)
    has_scheduled_advance_invoices: Union[bool, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    addons: Union[list[dict[str, Any]], Any] = Field(default=None)
    coupons: Union[list[dict[str, Any]], Any] = Field(default=None)
    discounts: Union[list[dict[str, Any]], Any] = Field(default=None)
    subscription_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    item_tiers: Union[list[dict[str, Any]], Any] = Field(default=None)
    charged_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    shipping_address: Union[dict[str, Any], Any] = Field(default=None)
    contract_term: Union[dict[str, Any], Any] = Field(default=None)
    meta_data: Union[dict[str, Any], Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    free_period: Union[int, Any] = Field(default=None)
    free_period_unit: Union[str, Any] = Field(default=None)
    cf_mandate_id: Union[str, Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    changes_scheduled_at: Union[int, Any] = Field(default=None)
    invoice_notes: Union[str, Any] = Field(default=None)
    auto_close_invoices: Union[bool, Any] = Field(default=None)
    offline_payment_method: Union[str, Any] = Field(default=None)

class SubscriptionListListItem(BaseModel):
    """Nested schema for SubscriptionList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subscription: Union[Subscription, Any] = Field(default=None)

class SubscriptionList(BaseModel):
    """Paginated list of subscriptions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[SubscriptionListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Invoice(BaseModel):
    """Chargebee invoice object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    customer_id: Union[str, Any] = Field(default=None)
    subscription_id: Union[str, Any] = Field(default=None)
    recurring: Union[bool, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    price_type: Union[str, Any] = Field(default=None)
    date: Union[int, Any] = Field(default=None)
    due_date: Union[int, Any] = Field(default=None)
    net_term_days: Union[int, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)
    amount_paid: Union[int, Any] = Field(default=None)
    amount_adjusted: Union[int, Any] = Field(default=None)
    write_off_amount: Union[int, Any] = Field(default=None)
    credits_applied: Union[int, Any] = Field(default=None)
    amount_due: Union[int, Any] = Field(default=None)
    paid_at: Union[int, Any] = Field(default=None)
    dunning_status: Union[str, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    first_invoice: Union[bool, Any] = Field(default=None)
    amount_to_collect: Union[int, Any] = Field(default=None)
    round_off_amount: Union[int, Any] = Field(default=None)
    new_sales_amount: Union[int, Any] = Field(default=None)
    has_advance_charges: Union[bool, Any] = Field(default=None)
    tax: Union[int, Any] = Field(default=None)
    sub_total: Union[int, Any] = Field(default=None)
    sub_total_in_local_currency: Union[int, Any] = Field(default=None)
    total_in_local_currency: Union[int, Any] = Field(default=None)
    exchange_rate: Union[float, Any] = Field(default=None)
    base_currency_code: Union[str, Any] = Field(default=None)
    is_gifted: Union[bool, Any] = Field(default=None)
    generated_at: Union[int, Any] = Field(default=None)
    expected_payment_date: Union[int, Any] = Field(default=None)
    channel: Union[str, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    line_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    discounts: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_discounts: Union[list[dict[str, Any]], Any] = Field(default=None)
    taxes: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_taxes: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_tiers: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_payments: Union[list[dict[str, Any]], Any] = Field(default=None)
    dunning_attempts: Union[list[dict[str, Any]], Any] = Field(default=None)
    applied_credits: Union[list[dict[str, Any]], Any] = Field(default=None)
    adjustment_credit_notes: Union[list[dict[str, Any]], Any] = Field(default=None)
    issued_credit_notes: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_orders: Union[list[dict[str, Any]], Any] = Field(default=None)
    notes: Union[list[dict[str, Any]], Any] = Field(default=None)
    billing_address: Union[dict[str, Any], Any] = Field(default=None)
    shipping_address: Union[dict[str, Any], Any] = Field(default=None)
    linked_taxes_withheld: Union[list[dict[str, Any]], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    void_reason_code: Union[str, Any] = Field(default=None)
    voided_at: Union[int, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)

class InvoiceListListItem(BaseModel):
    """Nested schema for InvoiceList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invoice: Union[Invoice, Any] = Field(default=None)

class InvoiceList(BaseModel):
    """Paginated list of invoices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[InvoiceListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class CreditNote(BaseModel):
    """Chargebee credit note object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    customer_id: Union[str, Any] = Field(default=None)
    subscription_id: Union[str, Any] = Field(default=None)
    reference_invoice_id: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    reason_code: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    date: Union[int, Any] = Field(default=None)
    price_type: Union[str, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)
    amount_allocated: Union[int, Any] = Field(default=None)
    amount_refunded: Union[int, Any] = Field(default=None)
    amount_available: Union[int, Any] = Field(default=None)
    refunded_at: Union[int, Any] = Field(default=None)
    voided_at: Union[int, Any] = Field(default=None)
    generated_at: Union[int, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    sub_total: Union[int, Any] = Field(default=None)
    sub_total_in_local_currency: Union[int, Any] = Field(default=None)
    total_in_local_currency: Union[int, Any] = Field(default=None)
    round_off_amount: Union[int, Any] = Field(default=None)
    channel: Union[str, Any] = Field(default=None)
    exchange_rate: Union[float, Any] = Field(default=None)
    base_currency_code: Union[str, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    create_reason_code: Union[str, Any] = Field(default=None)
    void_reason_code: Union[str, Any] = Field(default=None)
    fractional_correction: Union[int, Any] = Field(default=None)
    line_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    discounts: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_discounts: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_tiers: Union[list[dict[str, Any]], Any] = Field(default=None)
    taxes: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_taxes: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_refunds: Union[list[dict[str, Any]], Any] = Field(default=None)
    allocations: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_tax_withheld_refunds: Union[list[dict[str, Any]], Any] = Field(default=None)
    shipping_address: Union[dict[str, Any], Any] = Field(default=None)
    billing_address: Union[dict[str, Any], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)

class CreditNoteListListItem(BaseModel):
    """Nested schema for CreditNoteList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    credit_note: Union[CreditNote, Any] = Field(default=None)

class CreditNoteList(BaseModel):
    """Paginated list of credit notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[CreditNoteListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Coupon(BaseModel):
    """Chargebee coupon object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    invoice_name: Union[str, Any] = Field(default=None)
    discount_type: Union[str, Any] = Field(default=None)
    discount_percentage: Union[float, Any] = Field(default=None)
    discount_amount: Union[int, Any] = Field(default=None)
    discount_quantity: Union[int, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    duration_type: Union[str, Any] = Field(default=None)
    duration_month: Union[int, Any] = Field(default=None)
    valid_till: Union[int, Any] = Field(default=None)
    max_redemptions: Union[int, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    apply_discount_on: Union[str, Any] = Field(default=None)
    apply_on: Union[str, Any] = Field(default=None)
    plan_constraint: Union[str, Any] = Field(default=None)
    addon_constraint: Union[str, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)
    archived_at: Union[int, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    redemptions: Union[int, Any] = Field(default=None)
    invoice_notes: Union[str, Any] = Field(default=None)
    period: Union[int, Any] = Field(default=None)
    period_unit: Union[str, Any] = Field(default=None)
    item_constraints: Union[list[dict[str, Any]], Any] = Field(default=None)
    item_constraint_criteria: Union[list[dict[str, Any]], Any] = Field(default=None)
    coupon_constraints: Union[list[dict[str, Any]], Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)

class CouponListListItem(BaseModel):
    """Nested schema for CouponList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    coupon: Union[Coupon, Any] = Field(default=None)

class CouponList(BaseModel):
    """Paginated list of coupons"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[CouponListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Transaction(BaseModel):
    """Chargebee transaction object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    customer_id: Union[str, Any] = Field(default=None)
    subscription_id: Union[str, Any] = Field(default=None)
    gateway_account_id: Union[str, Any] = Field(default=None)
    payment_source_id: Union[str, Any] = Field(default=None)
    payment_method: Union[str, Any] = Field(default=None)
    reference_number: Union[str, Any] = Field(default=None)
    gateway: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    date: Union[int, Any] = Field(default=None)
    settled_at: Union[int, Any] = Field(default=None)
    exchange_rate: Union[float, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    id_at_gateway: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    fraud_flag: Union[str, Any] = Field(default=None)
    initiator_type: Union[str, Any] = Field(default=None)
    three_d_secure: Union[bool, Any] = Field(default=None)
    authorization_reason: Union[str, Any] = Field(default=None)
    error_code: Union[str, Any] = Field(default=None)
    error_text: Union[str, Any] = Field(default=None)
    voided_at: Union[int, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    fraud_reason: Union[str, Any] = Field(default=None)
    amount_unused: Union[int, Any] = Field(default=None)
    masked_card_number: Union[str, Any] = Field(default=None)
    reference_transaction_id: Union[str, Any] = Field(default=None)
    refunded_txn_id: Union[str, Any] = Field(default=None)
    reference_authorization_id: Union[str, Any] = Field(default=None)
    amount_capturable: Union[int, Any] = Field(default=None)
    reversal_transaction_id: Union[str, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    iin: Union[str, Any] = Field(default=None)
    last4: Union[str, Any] = Field(default=None)
    merchant_reference_id: Union[str, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    payment_method_details: Union[Any, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    base_currency_code: Union[str, Any] = Field(default=None)
    linked_invoices: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_credit_notes: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_refunds: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_payments: Union[list[dict[str, Any]], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)

class TransactionListListItem(BaseModel):
    """Nested schema for TransactionList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transaction: Union[Transaction, Any] = Field(default=None)

class TransactionList(BaseModel):
    """Paginated list of transactions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[TransactionListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Event(BaseModel):
    """Chargebee event object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    occurred_at: Union[int, Any] = Field(default=None)
    source: Union[str, Any] = Field(default=None)
    user: Union[str, Any] = Field(default=None)
    event_type: Union[str, Any] = Field(default=None)
    api_version: Union[str, Any] = Field(default=None)
    content: Union[dict[str, Any], Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    webhook_status: Union[str, Any] = Field(default=None)
    webhooks: Union[list[dict[str, Any]], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)

class EventListListItem(BaseModel):
    """Nested schema for EventList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    event: Union[Event, Any] = Field(default=None)

class EventList(BaseModel):
    """Paginated list of events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[EventListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Order(BaseModel):
    """Chargebee order object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    document_number: Union[str, Any] = Field(default=None)
    invoice_id: Union[str, Any] = Field(default=None)
    subscription_id: Union[str, Any] = Field(default=None)
    customer_id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    cancellation_reason: Union[str, Any] = Field(default=None)
    payment_status: Union[str, Any] = Field(default=None)
    order_type: Union[str, Any] = Field(default=None)
    price_type: Union[str, Any] = Field(default=None)
    reference_id: Union[str, Any] = Field(default=None)
    fulfillment_status: Union[str, Any] = Field(default=None)
    order_date: Union[int, Any] = Field(default=None)
    shipping_date: Union[int, Any] = Field(default=None)
    note: Union[str, Any] = Field(default=None)
    tracking_id: Union[str, Any] = Field(default=None)
    tracking_url: Union[str, Any] = Field(default=None)
    batch_id: Union[str, Any] = Field(default=None)
    created_by: Union[str, Any] = Field(default=None)
    shipment_carrier: Union[str, Any] = Field(default=None)
    invoice_round_off_amount: Union[int, Any] = Field(default=None)
    tax: Union[int, Any] = Field(default=None)
    amount_paid: Union[int, Any] = Field(default=None)
    amount_adjusted: Union[int, Any] = Field(default=None)
    refundable_credits_issued: Union[int, Any] = Field(default=None)
    refundable_credits: Union[int, Any] = Field(default=None)
    rounding_adjustement: Union[int, Any] = Field(default=None)
    paid_on: Union[int, Any] = Field(default=None)
    shipping_cut_off_date: Union[int, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)
    status_update_at: Union[int, Any] = Field(default=None)
    delivered_at: Union[int, Any] = Field(default=None)
    shipped_at: Union[int, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    cancelled_at: Union[int, Any] = Field(default=None)
    resent_status: Union[str, Any] = Field(default=None)
    is_resent: Union[bool, Any] = Field(default=None)
    original_order_id: Union[str, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    is_gifted: Union[bool, Any] = Field(default=None)
    gift_note: Union[str, Any] = Field(default=None)
    gift_id: Union[str, Any] = Field(default=None)
    resend_reason: Union[str, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    discount: Union[int, Any] = Field(default=None)
    sub_total: Union[int, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)
    order_line_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    shipping_address: Union[dict[str, Any], Any] = Field(default=None)
    billing_address: Union[dict[str, Any], Any] = Field(default=None)
    line_item_taxes: Union[list[dict[str, Any]], Any] = Field(default=None)
    line_item_discounts: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_credit_notes: Union[list[dict[str, Any]], Any] = Field(default=None)
    resent_orders: Union[list[dict[str, Any]], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)

class OrderListListItem(BaseModel):
    """Nested schema for OrderList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order: Union[Order, Any] = Field(default=None)

class OrderList(BaseModel):
    """Paginated list of orders"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[OrderListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class Item(BaseModel):
    """Chargebee item object (Product Catalog 2.0)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    external_name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    item_family_id: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    is_shippable: Union[bool, Any] = Field(default=None)
    is_giftable: Union[bool, Any] = Field(default=None)
    redirect_url: Union[str, Any] = Field(default=None)
    enabled_for_checkout: Union[bool, Any] = Field(default=None)
    enabled_in_portal: Union[bool, Any] = Field(default=None)
    included_in_mrr: Union[bool, Any] = Field(default=None)
    item_applicability: Union[str, Any] = Field(default=None)
    gift_claim_redirect_url: Union[str, Any] = Field(default=None)
    unit: Union[str, Any] = Field(default=None)
    metered: Union[bool, Any] = Field(default=None)
    usage_calculation: Union[str, Any] = Field(default=None)
    archived_at: Union[int, Any] = Field(default=None)
    channel: Union[str, Any] = Field(default=None)
    metadata: Union[dict[str, Any], Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    applicable_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    bundle_items: Union[list[dict[str, Any]], Any] = Field(default=None)
    bundle_configuration: Union[dict[str, Any], Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    is_percentage_pricing: Union[bool, Any] = Field(default=None)

class ItemListListItem(BaseModel):
    """Nested schema for ItemList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item: Union[Item, Any] = Field(default=None)

class ItemList(BaseModel):
    """Paginated list of items"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[ItemListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class ItemPrice(BaseModel):
    """Chargebee item price object (Product Catalog 2.0)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    item_family_id: Union[str, Any] = Field(default=None)
    item_id: Union[str, Any] = Field(default=None)
    item_type: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    external_name: Union[str, Any] = Field(default=None)
    pricing_model: Union[str, Any] = Field(default=None)
    price: Union[int, Any] = Field(default=None)
    price_in_decimal: Union[str, Any] = Field(default=None)
    period: Union[int, Any] = Field(default=None)
    period_unit: Union[str, Any] = Field(default=None)
    trial_period: Union[int, Any] = Field(default=None)
    trial_period_unit: Union[str, Any] = Field(default=None)
    trial_end_action: Union[str, Any] = Field(default=None)
    shipping_period: Union[int, Any] = Field(default=None)
    shipping_period_unit: Union[str, Any] = Field(default=None)
    billing_cycles: Union[int, Any] = Field(default=None)
    free_quantity: Union[int, Any] = Field(default=None)
    free_quantity_in_decimal: Union[str, Any] = Field(default=None)
    currency_code: Union[str, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)
    archived_at: Union[int, Any] = Field(default=None)
    invoice_notes: Union[str, Any] = Field(default=None)
    is_taxable: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, Any], Any] = Field(default=None)
    tax_detail: Union[dict[str, Any], Any] = Field(default=None)
    accounting_detail: Union[dict[str, Any], Any] = Field(default=None)
    tiers: Union[list[dict[str, Any]], Any] = Field(default=None)
    tax_providers_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    channel: Union[str, Any] = Field(default=None)
    show_description_in_invoices: Union[bool, Any] = Field(default=None)
    show_description_in_quotes: Union[bool, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)

class ItemPriceListListItem(BaseModel):
    """Nested schema for ItemPriceList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_price: Union[ItemPrice, Any] = Field(default=None)

class ItemPriceList(BaseModel):
    """Paginated list of item prices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[ItemPriceListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class PaymentSource(BaseModel):
    """Chargebee payment source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    customer_id: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    reference_id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    gateway: Union[str, Any] = Field(default=None)
    gateway_account_id: Union[str, Any] = Field(default=None)
    ip_address: Union[str, Any] = Field(default=None)
    issuing_country: Union[str, Any] = Field(default=None)
    created_at: Union[int, Any] = Field(default=None)
    updated_at: Union[int, Any] = Field(default=None)
    resource_version: Union[int, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    business_entity_id: Union[str, Any] = Field(default=None)
    object_: Union[str, Any] = Field(default=None, alias="object")
    card: Union[dict[str, Any], Any] = Field(default=None)
    bank_account: Union[dict[str, Any], Any] = Field(default=None)
    amazon_payment: Union[dict[str, Any], Any] = Field(default=None)
    paypal: Union[dict[str, Any], Any] = Field(default=None)
    upi: Union[dict[str, Any], Any] = Field(default=None)
    mandates: Union[dict[str, Any], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)

class PaymentSourceListListItem(BaseModel):
    """Nested schema for PaymentSourceList.list_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_source: Union[PaymentSource, Any] = Field(default=None)

class PaymentSourceList(BaseModel):
    """Paginated list of payment sources"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    list_: Union[list[PaymentSourceListListItem], Any] = Field(default=None, alias="list")
    next_offset: Union[str, Any] = Field(default=None)

class CustomerWrapper(BaseModel):
    """CustomerWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer: Union[Customer, Any] = Field(default=None)

class SubscriptionWrapper(BaseModel):
    """SubscriptionWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subscription: Union[Subscription, Any] = Field(default=None)

class InvoiceWrapper(BaseModel):
    """InvoiceWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invoice: Union[Invoice, Any] = Field(default=None)

class CreditNoteWrapper(BaseModel):
    """CreditNoteWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    credit_note: Union[CreditNote, Any] = Field(default=None)

class CouponWrapper(BaseModel):
    """CouponWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    coupon: Union[Coupon, Any] = Field(default=None)

class TransactionWrapper(BaseModel):
    """TransactionWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transaction: Union[Transaction, Any] = Field(default=None)

class EventWrapper(BaseModel):
    """EventWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    event: Union[Event, Any] = Field(default=None)

class OrderWrapper(BaseModel):
    """OrderWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order: Union[Order, Any] = Field(default=None)

class ItemWrapper(BaseModel):
    """ItemWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item: Union[Item, Any] = Field(default=None)

class ItemPriceWrapper(BaseModel):
    """ItemPriceWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_price: Union[ItemPrice, Any] = Field(default=None)

class PaymentSourceWrapper(BaseModel):
    """PaymentSourceWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_source: Union[PaymentSource, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CustomerListResultMeta(BaseModel):
    """Metadata for customer.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class SubscriptionListResultMeta(BaseModel):
    """Metadata for subscription.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class InvoiceListResultMeta(BaseModel):
    """Metadata for invoice.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class CreditNoteListResultMeta(BaseModel):
    """Metadata for credit_note.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class CouponListResultMeta(BaseModel):
    """Metadata for coupon.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class TransactionListResultMeta(BaseModel):
    """Metadata for transaction.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class EventListResultMeta(BaseModel):
    """Metadata for event.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class OrderListResultMeta(BaseModel):
    """Metadata for order.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class ItemListResultMeta(BaseModel):
    """Metadata for item.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class ItemPriceListResultMeta(BaseModel):
    """Metadata for item_price.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

class PaymentSourceListResultMeta(BaseModel):
    """Metadata for payment_source.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_offset: Union[str, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ChargebeeCheckResult(BaseModel):
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


class ChargebeeExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ChargebeeExecuteResultWithMeta(ChargebeeExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class SubscriptionSearchData(BaseModel):
    """Search result data for subscription entity."""
    model_config = ConfigDict(extra="allow")

    activated_at: int | None = None
    """The date and time when the subscription was activated."""
    addons: list[Any] | None = None
    """Represents any additional features or services added to the subscription"""
    affiliate_token: str | None = None
    """The affiliate token associated with the subscription."""
    auto_close_invoices: bool | None = None
    """Defines if the invoices are automatically closed or not."""
    auto_collection: str | None = None
    """Indicates if auto-collection is enabled for the subscription."""
    base_currency_code: str | None = None
    """The base currency code used for the subscription."""
    billing_period: int | None = None
    """The billing period duration for the subscription."""
    billing_period_unit: str | None = None
    """The unit of the billing period."""
    business_entity_id: str | None = None
    """The ID of the business entity to which the subscription belongs."""
    cancel_reason: str | None = None
    """The reason for the cancellation of the subscription."""
    cancel_reason_code: str | None = None
    """The code associated with the cancellation reason."""
    cancel_schedule_created_at: int | None = None
    """The date and time when the cancellation schedule was created."""
    cancelled_at: int | None = None
    """The date and time when the subscription was cancelled."""
    channel: str | None = None
    """The channel through which the subscription was acquired."""
    charged_event_based_addons: list[Any] | None = None
    """Details of addons charged based on events"""
    charged_items: list[Any] | None = None
    """Lists the items that have been charged as part of the subscription"""
    contract_term: dict[str, Any] | None = None
    """Contains details about the contract term of the subscription"""
    contract_term_billing_cycle_on_renewal: int | None = None
    """Indicates if the contract term billing cycle is applied on renewal."""
    coupon: str | None = None
    """The coupon applied to the subscription."""
    coupons: list[Any] | None = None
    """Details of applied coupons"""
    create_pending_invoices: bool | None = None
    """Indicates if pending invoices are created."""
    created_at: int | None = None
    """The date and time of the creation of the subscription."""
    created_from_ip: str | None = None
    """The IP address from which the subscription was created."""
    currency_code: str | None = None
    """The currency code used for the subscription."""
    current_term_end: int | None = None
    """The end date of the current term for the subscription."""
    current_term_start: int | None = None
    """The start date of the current term for the subscription."""
    custom_fields: list[Any] | None = None
    """"""
    customer_id: str | None = None
    """The ID of the customer associated with the subscription."""
    deleted: bool | None = None
    """Indicates if the subscription has been deleted."""
    discounts: list[Any] | None = None
    """Includes any discounts applied to the subscription"""
    due_invoices_count: int | None = None
    """The count of due invoices for the subscription."""
    due_since: int | None = None
    """The date since which the invoices are due."""
    event_based_addons: list[Any] | None = None
    """Specifies any event-based addons associated with the subscription"""
    exchange_rate: float | None = None
    """The exchange rate used for currency conversion."""
    free_period: int | None = None
    """The duration of the free period for the subscription."""
    free_period_unit: str | None = None
    """The unit of the free period duration."""
    gift_id: str | None = None
    """The ID of the gift associated with the subscription."""
    has_scheduled_advance_invoices: bool | None = None
    """Indicates if there are scheduled advance invoices for the subscription."""
    has_scheduled_changes: bool | None = None
    """Indicates if there are scheduled changes for the subscription."""
    id: str | None = None
    """The unique ID of the subscription."""
    invoice_notes: str | None = None
    """Any notes added to the invoices of the subscription."""
    item_tiers: list[Any] | None = None
    """Provides information about tiers or levels for specific subscription items"""
    meta_data: dict[str, Any] | None = None
    """Additional metadata associated with subscription"""
    metadata: dict[str, Any] | None = None
    """Additional metadata associated with subscription"""
    mrr: int | None = None
    """The monthly recurring revenue generated by the subscription."""
    next_billing_at: int | None = None
    """The date and time of the next billing event for the subscription."""
    object_: str | None = None
    """The type of object (subscription)."""
    offline_payment_method: str | None = None
    """The offline payment method used for the subscription."""
    override_relationship: bool | None = None
    """Indicates if the existing relationship is overridden by this subscription."""
    pause_date: int | None = None
    """The date on which the subscription was paused."""
    payment_source_id: str | None = None
    """The ID of the payment source used for the subscription."""
    plan_amount: int | None = None
    """The total amount charged for the plan of the subscription."""
    plan_amount_in_decimal: str | None = None
    """The total amount charged for the plan in decimal format."""
    plan_free_quantity: int | None = None
    """The free quantity included in the plan of the subscription."""
    plan_free_quantity_in_decimal: str | None = None
    """The free quantity included in the plan in decimal format."""
    plan_id: str | None = None
    """The ID of the plan associated with the subscription."""
    plan_quantity: int | None = None
    """The quantity of the plan included in the subscription."""
    plan_quantity_in_decimal: str | None = None
    """The quantity of the plan in decimal format."""
    plan_unit_price: int | None = None
    """The unit price of the plan for the subscription."""
    plan_unit_price_in_decimal: str | None = None
    """The unit price of the plan in decimal format."""
    po_number: str | None = None
    """The purchase order number associated with the subscription."""
    referral_info: dict[str, Any] | None = None
    """Contains details related to any referral information associated with the subscription"""
    remaining_billing_cycles: int | None = None
    """The count of remaining billing cycles for the subscription."""
    resource_version: int | None = None
    """The version of the resource (subscription)."""
    resume_date: int | None = None
    """The date on which the subscription was resumed."""
    setup_fee: int | None = None
    """The setup fee charged for the subscription."""
    shipping_address: dict[str, Any] | None = None
    """Stores the shipping address related to the subscription"""
    start_date: int | None = None
    """The start date of the subscription."""
    started_at: int | None = None
    """The date and time when the subscription started."""
    status: str | None = None
    """The current status of the subscription."""
    subscription_items: list[Any] | None = None
    """Lists individual items included in the subscription"""
    total_dues: int | None = None
    """The total amount of dues for the subscription."""
    trial_end: int | None = None
    """The end date of the trial period for the subscription."""
    trial_end_action: str | None = None
    """The action to be taken at the end of the trial period."""
    trial_start: int | None = None
    """The start date of the trial period for the subscription."""
    updated_at: int | None = None
    """The date and time when the subscription was last updated."""


class CustomerSearchData(BaseModel):
    """Search result data for customer entity."""
    model_config = ConfigDict(extra="allow")

    allow_direct_debit: bool | None = None
    """Indicates if direct debit is allowed for the customer."""
    auto_close_invoices: bool | None = None
    """Flag to automatically close invoices for the customer."""
    auto_collection: str | None = None
    """Configures the automatic collection settings for the customer."""
    backup_payment_source_id: str | None = None
    """ID of the backup payment source for the customer."""
    balances: list[Any] | None = None
    """Customer's balance information related to their account."""
    billing_address: dict[str, Any] | None = None
    """Customer's billing address details."""
    billing_date: int | None = None
    """Date for billing cycle."""
    billing_date_mode: str | None = None
    """Mode for billing date calculation."""
    billing_day_of_week: str | None = None
    """Day of the week for billing cycle."""
    billing_day_of_week_mode: str | None = None
    """Mode for billing day of the week calculation."""
    billing_month: int | None = None
    """Month for billing cycle."""
    business_customer_without_vat_number: bool | None = None
    """Flag indicating business customer without a VAT number."""
    business_entity_id: str | None = None
    """ID of the business entity."""
    card_status: str | None = None
    """Status of payment card associated with the customer."""
    channel: str | None = None
    """Channel through which the customer was acquired."""
    child_account_access: dict[str, Any] | None = None
    """Information regarding the access rights of child accounts linked to the customer's account."""
    client_profile_id: str | None = None
    """Client profile ID of the customer."""
    company: str | None = None
    """Company or organization name."""
    consolidated_invoicing: bool | None = None
    """Flag for consolidated invoicing setting."""
    contacts: list[Any] | None = None
    """List of contact details associated with the customer."""
    created_at: int | None = None
    """Date and time when the customer was created."""
    created_from_ip: str | None = None
    """IP address from which the customer was created."""
    custom_fields: list[Any] | None = None
    """"""
    customer_type: str | None = None
    """Type of customer (e.g., individual, business)."""
    deleted: bool | None = None
    """Flag indicating if the customer is deleted."""
    email: str | None = None
    """Email address of the customer."""
    entity_code: str | None = None
    """Code for the customer entity."""
    excess_payments: int | None = None
    """Total amount of excess payments by the customer."""
    exempt_number: str | None = None
    """Exemption number for tax purposes."""
    exemption_details: list[Any] | None = None
    """Details about any exemptions applicable to the customer's account."""
    first_name: str | None = None
    """First name of the customer."""
    fraud_flag: str | None = None
    """Flag indicating if fraud is associated with the customer."""
    id: str | None = None
    """Unique ID of the customer."""
    invoice_notes: str | None = None
    """Notes added to the customer's invoices."""
    is_location_valid: bool | None = None
    """Flag indicating if the customer location is valid."""
    last_name: str | None = None
    """Last name of the customer."""
    locale: str | None = None
    """Locale setting for the customer."""
    meta_data: dict[str, Any] | None = None
    """Additional metadata associated with the customer."""
    mrr: int | None = None
    """Monthly recurring revenue generated from the customer."""
    net_term_days: int | None = None
    """Number of days for net terms."""
    object_: str | None = None
    """Object type for the customer."""
    offline_payment_method: str | None = None
    """Offline payment method used by the customer."""
    parent_account_access: dict[str, Any] | None = None
    """Information regarding the access rights of the parent account, if applicable."""
    payment_method: dict[str, Any] | None = None
    """Customer's preferred payment method details."""
    phone: str | None = None
    """Phone number of the customer."""
    pii_cleared: str | None = None
    """Flag indicating if PII (Personally Identifiable Information) is cleared."""
    preferred_currency_code: str | None = None
    """Preferred currency code for transactions."""
    primary_payment_source_id: str | None = None
    """ID of the primary payment source for the customer."""
    promotional_credits: int | None = None
    """Total amount of promotional credits used."""
    referral_urls: list[Any] | None = None
    """List of referral URLs associated with the customer."""
    refundable_credits: int | None = None
    """Total amount of refundable credits."""
    registered_for_gst: bool | None = None
    """Flag indicating if the customer is registered for GST."""
    relationship: dict[str, Any] | None = None
    """Details about the relationship of the customer to other entities, if any."""
    resource_version: int | None = None
    """Version of the customer's resource."""
    tax_providers_fields: list[Any] | None = None
    """Fields related to tax providers."""
    taxability: str | None = None
    """Taxability status of the customer."""
    unbilled_charges: int | None = None
    """Total amount of unbilled charges."""
    updated_at: int | None = None
    """Date and time when the customer record was last updated."""
    use_default_hierarchy_settings: bool | None = None
    """Flag indicating if default hierarchy settings are used."""
    vat_number: str | None = None
    """VAT number associated with the customer."""
    vat_number_prefix: str | None = None
    """Prefix for the VAT number."""
    vat_number_status: str | None = None
    """Status of the VAT number validation."""
    vat_number_validated_time: int | None = None
    """Date and time when the VAT number was validated."""


class InvoiceSearchData(BaseModel):
    """Search result data for invoice entity."""
    model_config = ConfigDict(extra="allow")

    adjustment_credit_notes: list[Any] | None = None
    """Details of adjustment credit notes applied to the invoice"""
    amount_adjusted: int | None = None
    """Total amount adjusted in the invoice"""
    amount_due: int | None = None
    """Amount due for payment"""
    amount_paid: int | None = None
    """Amount already paid"""
    amount_to_collect: int | None = None
    """Amount yet to be collected"""
    applied_credits: list[Any] | None = None
    """Details of credits applied to the invoice"""
    base_currency_code: str | None = None
    """Currency code used as base for the invoice"""
    billing_address: dict[str, Any] | None = None
    """Details of the billing address associated with the invoice"""
    business_entity_id: str | None = None
    """ID of the business entity"""
    channel: str | None = None
    """Channel through which the invoice was generated"""
    credits_applied: int | None = None
    """Total credits applied to the invoice"""
    currency_code: str | None = None
    """Currency code of the invoice"""
    custom_fields: list[Any] | None = None
    """"""
    customer_id: str | None = None
    """ID of the customer"""
    date: int | None = None
    """Date of the invoice"""
    deleted: bool | None = None
    """Flag indicating if the invoice is deleted"""
    discounts: list[Any] | None = None
    """Discount details applied to the invoice"""
    due_date: int | None = None
    """Due date for payment"""
    dunning_attempts: list[Any] | None = None
    """Details of dunning attempts made"""
    dunning_status: str | None = None
    """Status of dunning for the invoice"""
    einvoice: dict[str, Any] | None = None
    """Details of electronic invoice"""
    exchange_rate: float | None = None
    """Exchange rate used for currency conversion"""
    expected_payment_date: int | None = None
    """Expected date of payment"""
    first_invoice: bool | None = None
    """Flag indicating whether it's the first invoice"""
    generated_at: int | None = None
    """Date when the invoice was generated"""
    has_advance_charges: bool | None = None
    """Flag indicating if there are advance charges"""
    id: str | None = None
    """Unique ID of the invoice"""
    is_digital: bool | None = None
    """Flag indicating if the invoice is digital"""
    is_gifted: bool | None = None
    """Flag indicating if the invoice is gifted"""
    issued_credit_notes: list[Any] | None = None
    """Details of credit notes issued"""
    line_item_discounts: list[Any] | None = None
    """Details of line item discounts"""
    line_item_taxes: list[Any] | None = None
    """Tax details applied to each line item in the invoice"""
    line_item_tiers: list[Any] | None = None
    """Tiers information for each line item in the invoice"""
    line_items: list[Any] | None = None
    """Details of individual line items in the invoice"""
    linked_orders: list[Any] | None = None
    """Details of linked orders to the invoice"""
    linked_payments: list[Any] | None = None
    """Details of linked payments"""
    linked_taxes_withheld: list[Any] | None = None
    """Details of linked taxes withheld on the invoice"""
    local_currency_code: str | None = None
    """Local currency code of the invoice"""
    local_currency_exchange_rate: float | None = None
    """Exchange rate for local currency conversion"""
    net_term_days: int | None = None
    """Net term days for payment"""
    new_sales_amount: int | None = None
    """New sales amount in the invoice"""
    next_retry_at: int | None = None
    """Date of the next payment retry"""
    notes: list[Any] | None = None
    """Notes associated with the invoice"""
    object_: str | None = None
    """Type of object"""
    paid_at: int | None = None
    """Date when the invoice was paid"""
    payment_owner: str | None = None
    """Owner of the payment"""
    po_number: str | None = None
    """Purchase order number"""
    price_type: str | None = None
    """Type of pricing"""
    recurring: bool | None = None
    """Flag indicating if it's a recurring invoice"""
    resource_version: int | None = None
    """Resource version of the invoice"""
    round_off_amount: int | None = None
    """Amount rounded off"""
    shipping_address: dict[str, Any] | None = None
    """Details of the shipping address associated with the invoice"""
    statement_descriptor: dict[str, Any] | None = None
    """Descriptor for the statement"""
    status: str | None = None
    """Status of the invoice"""
    sub_total: int | None = None
    """Subtotal amount"""
    sub_total_in_local_currency: int | None = None
    """Subtotal amount in local currency"""
    subscription_id: str | None = None
    """ID of the subscription associated"""
    tax: int | None = None
    """Total tax amount"""
    tax_category: str | None = None
    """Tax category"""
    taxes: list[Any] | None = None
    """Details of taxes applied"""
    term_finalized: bool | None = None
    """Flag indicating if the term is finalized"""
    total: int | None = None
    """Total amount of the invoice"""
    total_in_local_currency: int | None = None
    """Total amount in local currency"""
    updated_at: int | None = None
    """Date of last update"""
    vat_number: str | None = None
    """VAT number"""
    vat_number_prefix: str | None = None
    """Prefix for the VAT number"""
    void_reason_code: str | None = None
    """Reason code for voiding the invoice"""
    voided_at: int | None = None
    """Date when the invoice was voided"""
    write_off_amount: int | None = None
    """Amount written off"""


class CreditNoteSearchData(BaseModel):
    """Search result data for credit_note entity."""
    model_config = ConfigDict(extra="allow")

    allocations: list[Any] | None = None
    """Details of allocations associated with the credit note"""
    amount_allocated: int | None = None
    """The amount of credits allocated."""
    amount_available: int | None = None
    """The amount of credits available."""
    amount_refunded: int | None = None
    """The amount of credits refunded."""
    base_currency_code: str | None = None
    """The base currency code for the credit note."""
    billing_address: dict[str, Any] | None = None
    """Details of the billing address associated with the credit note"""
    business_entity_id: str | None = None
    """The ID of the business entity associated with the credit note."""
    channel: str | None = None
    """The channel through which the credit note was created."""
    create_reason_code: str | None = None
    """The reason code for creating the credit note."""
    currency_code: str | None = None
    """The currency code for the credit note."""
    custom_fields: list[Any] | None = None
    """"""
    customer_id: str | None = None
    """The ID of the customer associated with the credit note."""
    customer_notes: str | None = None
    """Notes provided by the customer for the credit note."""
    date: int | None = None
    """The date when the credit note was created."""
    deleted: bool | None = None
    """Indicates if the credit note has been deleted."""
    discounts: list[Any] | None = None
    """Details of discounts applied to the credit note"""
    exchange_rate: float | None = None
    """The exchange rate used for currency conversion."""
    fractional_correction: int | None = None
    """Fractional correction for rounding off decimals."""
    generated_at: int | None = None
    """The date when the credit note was generated."""
    id: str | None = None
    """The unique identifier for the credit note."""
    is_digital: bool | None = None
    """Indicates if the credit note is in digital format."""
    is_vat_moss_registered: bool | None = None
    """Indicates if VAT MOSS registration applies."""
    line_item_discounts: list[Any] | None = None
    """Details of discounts applied at the line item level in the credit note"""
    line_item_taxes: list[Any] | None = None
    """Details of taxes applied at the line item level in the credit note"""
    line_item_tiers: list[Any] | None = None
    """Details of tiers applied to line items in the credit note"""
    line_items: list[Any] | None = None
    """Details of line items in the credit note"""
    linked_refunds: list[Any] | None = None
    """Details of linked refunds to the credit note"""
    linked_tax_withheld_refunds: list[Any] | None = None
    """Details of linked tax withheld refunds to the credit note"""
    local_currency_code: str | None = None
    """The local currency code for the credit note."""
    object_: str | None = None
    """The object type of the credit note."""
    price_type: str | None = None
    """The type of pricing used for the credit note."""
    reason_code: str | None = None
    """The reason code for creating the credit note."""
    reference_invoice_id: str | None = None
    """The ID of the invoice this credit note references."""
    refunded_at: int | None = None
    """The date when the credit note was refunded."""
    resource_version: int | None = None
    """The version of the credit note resource."""
    round_off_amount: int | None = None
    """Amount rounded off for currency conversions."""
    shipping_address: dict[str, Any] | None = None
    """Details of the shipping address associated with the credit note"""
    status: str | None = None
    """The status of the credit note."""
    sub_total: int | None = None
    """The subtotal amount of the credit note."""
    sub_total_in_local_currency: int | None = None
    """The subtotal amount in local currency."""
    subscription_id: str | None = None
    """The ID of the subscription associated with the credit note."""
    taxes: list[Any] | None = None
    """List of taxes applied to the credit note"""
    total: int | None = None
    """The total amount of the credit note."""
    total_in_local_currency: int | None = None
    """The total amount in local currency."""
    type_: str | None = None
    """The type of credit note."""
    updated_at: int | None = None
    """The date when the credit note was last updated."""
    vat_number: str | None = None
    """VAT number associated with the credit note."""
    vat_number_prefix: str | None = None
    """Prefix for the VAT number."""
    voided_at: int | None = None
    """The date when the credit note was voided."""


class CouponSearchData(BaseModel):
    """Search result data for coupon entity."""
    model_config = ConfigDict(extra="allow")

    apply_discount_on: str | None = None
    """Determines where the discount is applied on (e.g. subtotal, total)."""
    apply_on: str | None = None
    """Specify on what type of items the coupon applies (e.g. subscription, addon)."""
    archived_at: int | None = None
    """Timestamp when the coupon was archived."""
    coupon_constraints: list[Any] | None = None
    """Represents the constraints associated with the coupon"""
    created_at: int | None = None
    """Timestamp of the coupon creation."""
    currency_code: str | None = None
    """The currency code for the coupon (e.g. USD, EUR)."""
    custom_fields: list[Any] | None = None
    """"""
    discount_amount: int | None = None
    """The fixed discount amount applied by the coupon."""
    discount_percentage: float | None = None
    """Percentage discount applied by the coupon."""
    discount_quantity: int | None = None
    """Specifies the number of free units provided for the item price, without affecting the total quantity sold. This parameter is applicable only when the discount_type is set to offer_quantity."""
    discount_type: str | None = None
    """Type of discount (e.g. fixed, percentage)."""
    duration_month: int | None = None
    """Duration of the coupon in months."""
    duration_type: str | None = None
    """Type of duration (e.g. forever, one-time)."""
    id: str | None = None
    """Unique identifier for the coupon."""
    invoice_name: str | None = None
    """Name displayed on invoices when the coupon is used."""
    invoice_notes: str | None = None
    """Additional notes displayed on invoices when the coupon is used."""
    item_constraint_criteria: list[Any] | None = None
    """Criteria for item constraints"""
    item_constraints: list[Any] | None = None
    """Constraints related to the items"""
    max_redemptions: int | None = None
    """Maximum number of times the coupon can be redeemed."""
    name: str | None = None
    """Name of the coupon."""
    object_: str | None = None
    """Type of object (usually 'coupon')."""
    period: int | None = None
    """Duration or frequency for which the coupon is valid."""
    period_unit: str | None = None
    """Unit of the period (e.g. days, weeks)."""
    redemptions: int | None = None
    """Number of times the coupon has been redeemed."""
    resource_version: int | None = None
    """Version of the resource."""
    status: str | None = None
    """Current status of the coupon (e.g. active, inactive)."""
    updated_at: int | None = None
    """Timestamp when the coupon was last updated."""
    valid_till: int | None = None
    """Date until which the coupon is valid for use."""


class TransactionSearchData(BaseModel):
    """Search result data for transaction entity."""
    model_config = ConfigDict(extra="allow")

    amount: int | None = None
    """The total amount of the transaction."""
    amount_capturable: int | None = None
    """The remaining amount that can be captured in the transaction."""
    amount_unused: int | None = None
    """The amount in the transaction that remains unused."""
    authorization_reason: str | None = None
    """Reason for authorization of the transaction."""
    base_currency_code: str | None = None
    """The base currency code of the transaction."""
    business_entity_id: str | None = None
    """The ID of the business entity related to the transaction."""
    cn_create_reason_code: str | None = None
    """Reason code for creating a credit note."""
    cn_date: int | None = None
    """Date of the credit note."""
    cn_reference_invoice_id: str | None = None
    """ID of the invoice referenced in the credit note."""
    cn_status: str | None = None
    """Status of the credit note."""
    cn_total: int | None = None
    """Total amount of the credit note."""
    currency_code: str | None = None
    """The currency code of the transaction."""
    custom_fields: list[Any] | None = None
    """"""
    customer_id: str | None = None
    """The ID of the customer associated with the transaction."""
    date: int | None = None
    """Date of the transaction."""
    deleted: bool | None = None
    """Flag indicating if the transaction is deleted."""
    error_code: str | None = None
    """Error code associated with the transaction."""
    error_detail: str | None = None
    """Detailed error information related to the transaction."""
    error_text: str | None = None
    """Error message text of the transaction."""
    exchange_rate: float | None = None
    """Exchange rate used in the transaction."""
    fraud_flag: str | None = None
    """Flag indicating if the transaction is flagged for fraud."""
    fraud_reason: str | None = None
    """Reason for flagging the transaction as fraud."""
    gateway: str | None = None
    """The payment gateway used in the transaction."""
    gateway_account_id: str | None = None
    """ID of the gateway account used in the transaction."""
    id: str | None = None
    """Unique identifier of the transaction."""
    id_at_gateway: str | None = None
    """Transaction ID assigned by the gateway."""
    iin: str | None = None
    """Bank identification number of the transaction."""
    initiator_type: str | None = None
    """Type of initiator involved in the transaction."""
    last4: str | None = None
    """Last 4 digits of the card used in the transaction."""
    linked_credit_notes: list[Any] | None = None
    """Linked credit notes associated with the transaction."""
    linked_invoices: list[Any] | None = None
    """Linked invoices associated with the transaction."""
    linked_payments: list[Any] | None = None
    """Linked payments associated with the transaction."""
    linked_refunds: list[Any] | None = None
    """Linked refunds associated with the transaction."""
    masked_card_number: str | None = None
    """Masked card number used in the transaction."""
    merchant_reference_id: str | None = None
    """Merchant reference ID of the transaction."""
    object_: str | None = None
    """Type of object representing the transaction."""
    payment_method: str | None = None
    """Payment method used in the transaction."""
    payment_method_details: str | None = None
    """Details of the payment method used in the transaction."""
    payment_source_id: str | None = None
    """ID of the payment source used in the transaction."""
    reference_authorization_id: str | None = None
    """Reference authorization ID of the transaction."""
    reference_number: str | None = None
    """Reference number associated with the transaction."""
    reference_transaction_id: str | None = None
    """ID of the reference transaction."""
    refrence_number: str | None = None
    """Reference number of the transaction."""
    refunded_txn_id: str | None = None
    """ID of the refunded transaction."""
    resource_version: int | None = None
    """Resource version of the transaction."""
    reversal_transaction_id: str | None = None
    """ID of the reversal transaction, if any."""
    settled_at: int | None = None
    """Date when the transaction was settled."""
    status: str | None = None
    """Status of the transaction."""
    subscription_id: str | None = None
    """ID of the subscription related to the transaction."""
    three_d_secure: bool | None = None
    """Flag indicating if 3D secure was used in the transaction."""
    txn_amount: int | None = None
    """Amount of the transaction."""
    txn_date: int | None = None
    """Date of the transaction."""
    type_: str | None = None
    """Type of the transaction."""
    updated_at: int | None = None
    """Date when the transaction was last updated."""
    voided_at: int | None = None
    """Date when the transaction was voided."""


class EventSearchData(BaseModel):
    """Search result data for event entity."""
    model_config = ConfigDict(extra="allow")

    api_version: str | None = None
    """The version of the Chargebee API being used to fetch the event data."""
    content: dict[str, Any] | None = None
    """The specific content or information associated with the event."""
    custom_fields: list[Any] | None = None
    """"""
    event_type: str | None = None
    """The type or category of the event."""
    id: str | None = None
    """Unique identifier for the event data record."""
    object_: str | None = None
    """The object or entity that the event is triggered for."""
    occurred_at: int | None = None
    """The datetime when the event occurred."""
    source: str | None = None
    """The source or origin of the event data."""
    user: str | None = None
    """Information about the user or entity associated with the event."""
    webhook_status: str | None = None
    """The status of the webhook execution for the event."""
    webhooks: list[Any] | None = None
    """List of webhooks associated with the event."""


class OrderSearchData(BaseModel):
    """Search result data for order entity."""
    model_config = ConfigDict(extra="allow")

    amount_adjusted: int | None = None
    """Adjusted amount for the order."""
    amount_paid: int | None = None
    """Amount paid for the order."""
    base_currency_code: str | None = None
    """The base currency code used for the order."""
    batch_id: str | None = None
    """Unique identifier for the batch the order belongs to."""
    billing_address: dict[str, Any] | None = None
    """The billing address associated with the order"""
    business_entity_id: str | None = None
    """Identifier for the business entity associated with the order."""
    cancellation_reason: str | None = None
    """Reason for order cancellation."""
    cancelled_at: int | None = None
    """Timestamp when the order was cancelled."""
    created_at: int | None = None
    """Timestamp when the order was created."""
    created_by: str | None = None
    """User or system that created the order."""
    currency_code: str | None = None
    """Currency code used for the order."""
    custom_fields: list[Any] | None = None
    """"""
    customer_id: str | None = None
    """Identifier for the customer placing the order."""
    deleted: bool | None = None
    """Flag indicating if the order has been deleted."""
    delivered_at: int | None = None
    """Timestamp when the order was delivered."""
    discount: int | None = None
    """Discount amount applied to the order."""
    document_number: str | None = None
    """Unique document number associated with the order."""
    exchange_rate: float | None = None
    """Rate used for currency exchange in the order."""
    fulfillment_status: str | None = None
    """Status of fulfillment for the order."""
    gift_id: str | None = None
    """Identifier for any gift associated with the order."""
    gift_note: str | None = None
    """Note attached to any gift in the order."""
    id: str | None = None
    """Unique identifier for the order."""
    invoice_id: str | None = None
    """Identifier for the invoice associated with the order."""
    invoice_round_off_amount: int | None = None
    """Round-off amount applied to the invoice."""
    is_gifted: bool | None = None
    """Flag indicating if the order is a gift."""
    is_resent: bool | None = None
    """Flag indicating if the order has been resent."""
    line_item_discounts: list[Any] | None = None
    """Discounts applied to individual line items"""
    line_item_taxes: list[Any] | None = None
    """Taxes applied to individual line items"""
    linked_credit_notes: list[Any] | None = None
    """Credit notes linked to the order"""
    note: str | None = None
    """Additional notes or comments for the order."""
    object_: str | None = None
    """Type of object representing an order in the system."""
    order_date: int | None = None
    """Date when the order was created."""
    order_line_items: list[Any] | None = None
    """List of line items in the order"""
    order_type: str | None = None
    """Type of order such as purchase order or sales order."""
    original_order_id: str | None = None
    """Identifier for the original order if this is a modified order."""
    paid_on: int | None = None
    """Timestamp when the order was paid for."""
    payment_status: str | None = None
    """Status of payment for the order."""
    price_type: str | None = None
    """Type of pricing used for the order."""
    reference_id: str | None = None
    """Reference identifier for the order."""
    refundable_credits: int | None = None
    """Credits that can be refunded for the whole order."""
    refundable_credits_issued: int | None = None
    """Credits already issued for refund for the whole order."""
    resend_reason: str | None = None
    """Reason for resending the order."""
    resent_orders: list[Any] | None = None
    """Orders that were resent to the customer"""
    resent_status: str | None = None
    """Status of the resent order."""
    resource_version: int | None = None
    """Version of the resource or order data."""
    rounding_adjustement: int | None = None
    """Adjustment made for rounding off the order amount."""
    shipment_carrier: str | None = None
    """Carrier for shipping the order."""
    shipped_at: int | None = None
    """Timestamp when the order was shipped."""
    shipping_address: dict[str, Any] | None = None
    """The shipping address for the order"""
    shipping_cut_off_date: int | None = None
    """Date indicating the shipping cut-off for the order."""
    shipping_date: int | None = None
    """Date when the order is scheduled for shipping."""
    status: str | None = None
    """Current status of the order."""
    status_update_at: int | None = None
    """Timestamp when the status of the order was last updated."""
    sub_total: int | None = None
    """Sub-total amount for the order before applying taxes or discounts."""
    subscription_id: str | None = None
    """Identifier for the subscription associated with the order."""
    tax: int | None = None
    """Total tax amount for the order."""
    total: int | None = None
    """Total amount including taxes and discounts for the order."""
    tracking_id: str | None = None
    """Tracking identifier for the order shipment."""
    tracking_url: str | None = None
    """URL for tracking the order shipment."""
    updated_at: int | None = None
    """Timestamp when the order data was last updated."""


class PaymentSourceSearchData(BaseModel):
    """Search result data for payment_source entity."""
    model_config = ConfigDict(extra="allow")

    amazon_payment: dict[str, Any] | None = None
    """Data related to Amazon Pay payment source"""
    bank_account: dict[str, Any] | None = None
    """Data related to bank account payment source"""
    business_entity_id: str | None = None
    """Identifier for the business entity associated with the payment source"""
    card: dict[str, Any] | None = None
    """Data related to card payment source"""
    created_at: int | None = None
    """Timestamp indicating when the payment source was created"""
    custom_fields: list[Any] | None = None
    """"""
    customer_id: str | None = None
    """Unique identifier for the customer associated with the payment source"""
    deleted: bool | None = None
    """Indicates if the payment source has been deleted"""
    gateway: str | None = None
    """Name of the payment gateway used for the payment source"""
    gateway_account_id: str | None = None
    """Identifier for the gateway account tied to the payment source"""
    id: str | None = None
    """Unique identifier for the payment source"""
    ip_address: str | None = None
    """IP address associated with the payment source"""
    issuing_country: str | None = None
    """Country where the payment source was issued"""
    mandates: dict[str, Any] | None = None
    """Data related to mandates for payments"""
    object_: str | None = None
    """Type of object, e.g., payment_source"""
    paypal: dict[str, Any] | None = None
    """Data related to PayPal payment source"""
    reference_id: str | None = None
    """Reference identifier for the payment source"""
    resource_version: int | None = None
    """Version of the payment source resource"""
    status: str | None = None
    """Status of the payment source, e.g., active or inactive"""
    type_: str | None = None
    """Type of payment source, e.g., card, bank_account"""
    updated_at: int | None = None
    """Timestamp indicating when the payment source was last updated"""
    upi: dict[str, Any] | None = None
    """Data related to UPI payment source"""


class ItemSearchData(BaseModel):
    """Search result data for item entity."""
    model_config = ConfigDict(extra="allow")

    applicable_items: list[Any] | None = None
    """Items associated with the item"""
    archived_at: int | None = None
    """Date and time when the item was archived"""
    channel: str | None = None
    """Channel the item belongs to"""
    custom_fields: list[Any] | None = None
    """Custom field entries for the item"""
    description: str | None = None
    """Description of the item"""
    enabled_for_checkout: bool | None = None
    """Flag indicating if the item is enabled for checkout"""
    enabled_in_portal: bool | None = None
    """Flag indicating if the item is enabled in the portal"""
    external_name: str | None = None
    """Name of the item in an external system"""
    gift_claim_redirect_url: str | None = None
    """URL to redirect for gift claim"""
    id: str | None = None
    """Unique identifier for the item"""
    included_in_mrr: bool | None = None
    """Flag indicating if the item is included in Monthly Recurring Revenue"""
    is_giftable: bool | None = None
    """Flag indicating if the item is giftable"""
    is_shippable: bool | None = None
    """Flag indicating if the item is shippable"""
    item_applicability: str | None = None
    """Applicability of the item"""
    item_family_id: str | None = None
    """ID of the item's family"""
    metadata: dict[str, Any] | None = None
    """Additional data associated with the item"""
    metered: bool | None = None
    """Flag indicating if the item is metered"""
    name: str | None = None
    """Name of the item"""
    object_: str | None = None
    """Type of object"""
    redirect_url: str | None = None
    """URL to redirect for the item"""
    resource_version: int | None = None
    """Version of the resource"""
    status: str | None = None
    """Status of the item"""
    type_: str | None = None
    """Type of the item"""
    unit: str | None = None
    """Unit associated with the item"""
    updated_at: int | None = None
    """Date and time when the item was last updated"""
    usage_calculation: str | None = None
    """Calculation method used for item usage"""


class ItemPriceSearchData(BaseModel):
    """Search result data for item_price entity."""
    model_config = ConfigDict(extra="allow")

    accounting_detail: dict[str, Any] | None = None
    """Details related to accounting such as cost, revenue, expenses, etc."""
    archived_at: int | None = None
    """Date and time when the item was archived."""
    billing_cycles: int | None = None
    """Number of billing cycles for the item."""
    channel: str | None = None
    """The channel through which the item is sold."""
    created_at: int | None = None
    """Date and time when the item was created."""
    currency_code: str | None = None
    """The currency code used for pricing the item."""
    custom_fields: list[Any] | None = None
    """Custom field entries for the item price."""
    description: str | None = None
    """Description of the item."""
    external_name: str | None = None
    """External name of the item."""
    free_quantity: int | None = None
    """Free quantity allowed for the item."""
    free_quantity_in_decimal: str | None = None
    """Free quantity allowed represented in decimal format."""
    id: str | None = None
    """Unique identifier for the item price."""
    invoice_notes: str | None = None
    """Notes to be included in the invoice for the item."""
    is_taxable: bool | None = None
    """Flag indicating whether the item is taxable."""
    item_family_id: str | None = None
    """Identifier for the item family to which the item belongs."""
    item_id: str | None = None
    """Unique identifier for the parent item."""
    item_type: str | None = None
    """Type of the item (e.g., product, service)."""
    metadata: dict[str, Any] | None = None
    """Additional metadata associated with the item."""
    name: str | None = None
    """Name of the item price."""
    object_: str | None = None
    """Object type representing the item price."""
    period: int | None = None
    """Duration of the item's billing period."""
    period_unit: str | None = None
    """Unit of measurement for the billing period duration."""
    price: int | None = None
    """Price of the item."""
    price_in_decimal: str | None = None
    """Price of the item represented in decimal format."""
    pricing_model: str | None = None
    """The pricing model used for the item (e.g., flat fee, usage-based)."""
    resource_version: int | None = None
    """Version of the item price resource."""
    shipping_period: int | None = None
    """Duration of the item's shipping period."""
    shipping_period_unit: str | None = None
    """Unit of measurement for the shipping period duration."""
    show_description_in_invoices: bool | None = None
    """Flag indicating whether to show the description in invoices."""
    show_description_in_quotes: bool | None = None
    """Flag indicating whether to show the description in quotes."""
    status: str | None = None
    """Current status of the item price (e.g., active, inactive)."""
    tax_detail: dict[str, Any] | None = None
    """Information about taxes associated with the item price."""
    tiers: list[Any] | None = None
    """Different pricing tiers for the item."""
    trial_end_action: str | None = None
    """Action to be taken at the end of the trial period."""
    trial_period: int | None = None
    """Duration of the trial period."""
    trial_period_unit: str | None = None
    """Unit of measurement for the trial period duration."""
    updated_at: int | None = None
    """Date and time when the item price was last updated."""


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

SubscriptionSearchResult = AirbyteSearchResult[SubscriptionSearchData]
"""Search result type for subscription entity."""

CustomerSearchResult = AirbyteSearchResult[CustomerSearchData]
"""Search result type for customer entity."""

InvoiceSearchResult = AirbyteSearchResult[InvoiceSearchData]
"""Search result type for invoice entity."""

CreditNoteSearchResult = AirbyteSearchResult[CreditNoteSearchData]
"""Search result type for credit_note entity."""

CouponSearchResult = AirbyteSearchResult[CouponSearchData]
"""Search result type for coupon entity."""

TransactionSearchResult = AirbyteSearchResult[TransactionSearchData]
"""Search result type for transaction entity."""

EventSearchResult = AirbyteSearchResult[EventSearchData]
"""Search result type for event entity."""

OrderSearchResult = AirbyteSearchResult[OrderSearchData]
"""Search result type for order entity."""

PaymentSourceSearchResult = AirbyteSearchResult[PaymentSourceSearchData]
"""Search result type for payment_source entity."""

ItemSearchResult = AirbyteSearchResult[ItemSearchData]
"""Search result type for item entity."""

ItemPriceSearchResult = AirbyteSearchResult[ItemPriceSearchData]
"""Search result type for item_price entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CustomerListResult = ChargebeeExecuteResultWithMeta[list[Customer], CustomerListResultMeta]
"""Result type for customer.list operation with data and metadata."""

SubscriptionListResult = ChargebeeExecuteResultWithMeta[list[Subscription], SubscriptionListResultMeta]
"""Result type for subscription.list operation with data and metadata."""

InvoiceListResult = ChargebeeExecuteResultWithMeta[list[Invoice], InvoiceListResultMeta]
"""Result type for invoice.list operation with data and metadata."""

CreditNoteListResult = ChargebeeExecuteResultWithMeta[list[CreditNote], CreditNoteListResultMeta]
"""Result type for credit_note.list operation with data and metadata."""

CouponListResult = ChargebeeExecuteResultWithMeta[list[Coupon], CouponListResultMeta]
"""Result type for coupon.list operation with data and metadata."""

TransactionListResult = ChargebeeExecuteResultWithMeta[list[Transaction], TransactionListResultMeta]
"""Result type for transaction.list operation with data and metadata."""

EventListResult = ChargebeeExecuteResultWithMeta[list[Event], EventListResultMeta]
"""Result type for event.list operation with data and metadata."""

OrderListResult = ChargebeeExecuteResultWithMeta[list[Order], OrderListResultMeta]
"""Result type for order.list operation with data and metadata."""

ItemListResult = ChargebeeExecuteResultWithMeta[list[Item], ItemListResultMeta]
"""Result type for item.list operation with data and metadata."""

ItemPriceListResult = ChargebeeExecuteResultWithMeta[list[ItemPrice], ItemPriceListResultMeta]
"""Result type for item_price.list operation with data and metadata."""

PaymentSourceListResult = ChargebeeExecuteResultWithMeta[list[PaymentSource], PaymentSourceListResultMeta]
"""Result type for payment_source.list operation with data and metadata."""

