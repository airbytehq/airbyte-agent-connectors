"""
Pydantic models for paypal-transaction connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration

class PaypalTransactionAuthConfig(BaseModel):
    """PayPal OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The Client ID of your PayPal developer application."""
    client_secret: str
    """The Client Secret of your PayPal developer application."""
    access_token: Optional[str] = None
    """OAuth2 access token obtained via client credentials grant. Use the PayPal token endpoint with your client_id and client_secret to obtain this.
"""

# Replication configuration

class PaypalTransactionReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from PayPal."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """Start date for data extraction in ISO 8601 format. Date must be in range from 3 years till 12 hours before present time.
"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Money(BaseModel):
    """Currency amount with code and value."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: str | None = Field(default=None)
    value: str | None = Field(default=None)

class BalanceDetail(BaseModel):
    """Balance information for a single currency."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    primary: bool | None = Field(default=None)
    currency: str | None = Field(default=None)
    total_balance: Money | None = Field(default=None)
    available_balance: Money | None = Field(default=None)
    withheld_balance: Money | None = Field(default=None)

class BalancesResponse(BaseModel):
    """Balances response with account balance details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    balances: list[BalanceDetail] | None = Field(default=None)
    account_id: str | None = Field(default=None)
    as_of_time: str | None = Field(default=None)
    last_refresh_time: str | None = Field(default=None)

class PayerName(BaseModel):
    """Payer name details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    given_name: str | None = Field(default=None)
    surname: str | None = Field(default=None)
    alternate_full_name: str | None = Field(default=None)

class PayerInfo(BaseModel):
    """Information about the payer."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: str | None = Field(default=None)
    email_address: str | None = Field(default=None)
    address_status: str | None = Field(default=None)
    payer_status: str | None = Field(default=None)
    payer_name: PayerName | None = Field(default=None)
    country_code: str | None = Field(default=None)

class TransactionInfo(BaseModel):
    """Detailed transaction information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    paypal_account_id: str | None = Field(default=None)
    transaction_id: str | None = Field(default=None)
    paypal_reference_id: str | None = Field(default=None)
    paypal_reference_id_type: str | None = Field(default=None)
    transaction_event_code: str | None = Field(default=None)
    transaction_initiation_date: str | None = Field(default=None)
    transaction_updated_date: str | None = Field(default=None)
    transaction_amount: Money | None = Field(default=None)
    fee_amount: Money | None = Field(default=None)
    insurance_amount: Money | None = Field(default=None)
    shipping_amount: Money | None = Field(default=None)
    shipping_discount_amount: Money | None = Field(default=None)
    transaction_status: str | None = Field(default=None)
    transaction_subject: str | None = Field(default=None)
    transaction_note: str | None = Field(default=None)
    invoice_id: str | None = Field(default=None)
    custom_field: str | None = Field(default=None)
    protection_eligibility: str | None = Field(default=None)

class ShippingAddress(BaseModel):
    """Shipping address details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line1: str | None = Field(default=None)
    line2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    postal_code: str | None = Field(default=None)

class ShippingInfo(BaseModel):
    """Shipping information for the transaction."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    address: ShippingAddress | None = Field(default=None)

class ItemDetailTaxAmountsItem(BaseModel):
    """Nested schema for ItemDetail.tax_amounts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tax_amount: Money | None = Field(default=None)

class ItemDetail(BaseModel):
    """Details for a single cart item."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_code: str | None = Field(default=None)
    item_name: str | None = Field(default=None)
    item_description: str | None = Field(default=None)
    item_quantity: str | None = Field(default=None)
    item_unit_price: Money | None = Field(default=None)
    item_amount: Money | None = Field(default=None)
    total_item_amount: Money | None = Field(default=None)
    tax_amounts: list[ItemDetailTaxAmountsItem] | None = Field(default=None)
    invoice_number: str | None = Field(default=None)

class CartInfo(BaseModel):
    """Cart information for the transaction."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_details: list[ItemDetail] | None = Field(default=None)
    tax_inclusive: bool | None = Field(default=None)
    paypal_invoice_id: str | None = Field(default=None)

class AuctionInfo(BaseModel):
    """Auction information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auction_site: str | None = Field(default=None)
    auction_item_site: str | None = Field(default=None)
    auction_buyer_id: str | None = Field(default=None)
    auction_closing_date: str | None = Field(default=None)

class IncentiveDetail(BaseModel):
    """Incentive detail."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incentive_type: str | None = Field(default=None)
    incentive_code: str | None = Field(default=None)
    incentive_amount: Money | None = Field(default=None)
    incentive_program_code: str | None = Field(default=None)

class IncentiveInfo(BaseModel):
    """Incentive information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incentive_details: list[IncentiveDetail] | None = Field(default=None)

class StoreInfo(BaseModel):
    """Store information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    store_id: str | None = Field(default=None)
    terminal_id: str | None = Field(default=None)

class Transaction(BaseModel):
    """A single PayPal transaction with full details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transaction_info: TransactionInfo | None = Field(default=None)
    payer_info: PayerInfo | None = Field(default=None)
    shipping_info: ShippingInfo | None = Field(default=None)
    cart_info: CartInfo | None = Field(default=None)
    auction_info: AuctionInfo | None = Field(default=None)
    incentive_info: IncentiveInfo | None = Field(default=None)
    store_info: StoreInfo | None = Field(default=None)
    transaction_id: str | None = Field(default=None)
    transaction_updated_date: str | None = Field(default=None)

class TransactionsListLinksItem(BaseModel):
    """Nested schema for TransactionsList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class TransactionsList(BaseModel):
    """Paginated list of transactions."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transaction_details: list[Transaction] | None = Field(default=None)
    account_number: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    last_refreshed_datetime: str | None = Field(default=None)
    page: int | None = Field(default=None)
    total_items: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    links: list[TransactionsListLinksItem] | None = Field(default=None)

class PaymentPayerPayerInfo(BaseModel):
    """Nested schema for PaymentPayer.payer_info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None, description="Payer email.")
    """Payer email."""
    first_name: str | None = Field(default=None, description="Payer first name.")
    """Payer first name."""
    last_name: str | None = Field(default=None, description="Payer last name.")
    """Payer last name."""
    payer_id: str | None = Field(default=None, description="Payer ID.")
    """Payer ID."""
    country_code: str | None = Field(default=None, description="Payer country code.")
    """Payer country code."""

class PaymentPayer(BaseModel):
    """Payer information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_method: str | None = Field(default=None, description="Payment method.")
    """Payment method."""
    status: str | None = Field(default=None, description="Payer status.")
    """Payer status."""
    payer_info: PaymentPayerPayerInfo | None = Field(default=None)

class PaymentTransactionsItemAmountDetails(BaseModel):
    """Nested schema for PaymentTransactionsItemAmount.details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subtotal: str | None = Field(default=None)
    shipping: str | None = Field(default=None)
    insurance: str | None = Field(default=None)
    handling_fee: str | None = Field(default=None)
    shipping_discount: str | None = Field(default=None)

class PaymentTransactionsItemAmount(BaseModel):
    """Nested schema for PaymentTransactionsItem.amount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: str | None = Field(default=None, description="Total amount.")
    """Total amount."""
    currency: str | None = Field(default=None, description="Currency code.")
    """Currency code."""
    details: PaymentTransactionsItemAmountDetails | None = Field(default=None)

class PaymentTransactionsItem(BaseModel):
    """Nested schema for Payment.transactions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: PaymentTransactionsItemAmount | None = Field(default=None)
    description: str | None = Field(default=None, description="Transaction description.")
    """Transaction description."""
    related_resources: list[dict[str, Any]] | None = Field(default=None)

class PaymentLinksItem(BaseModel):
    """Nested schema for Payment.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class Payment(BaseModel):
    """A PayPal payment object."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    intent: str | None = Field(default=None)
    state: str | None = Field(default=None)
    cart: str | None = Field(default=None)
    payer: PaymentPayer | None = Field(default=None)
    transactions: list[PaymentTransactionsItem] | None = Field(default=None)
    create_time: str | None = Field(default=None)
    update_time: str | None = Field(default=None)
    links: list[PaymentLinksItem] | None = Field(default=None)

class PaymentsList(BaseModel):
    """List of payments."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payments: list[Payment] | None = Field(default=None)
    count: int | None = Field(default=None)
    next_id: str | None = Field(default=None)

class DisputeLinksItem(BaseModel):
    """Nested schema for Dispute.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class DisputeDisputedTransactionsItemSeller(BaseModel):
    """Nested schema for DisputeDisputedTransactionsItem.seller"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    merchant_id: str | None = Field(default=None, description="Seller's merchant ID.")
    """Seller's merchant ID."""

class DisputeDisputedTransactionsItem(BaseModel):
    """Nested schema for Dispute.disputed_transactions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    buyer_transaction_id: str | None = Field(default=None, description="Buyer's transaction ID.")
    """Buyer's transaction ID."""
    seller: DisputeDisputedTransactionsItemSeller | None = Field(default=None)

class Dispute(BaseModel):
    """A PayPal dispute object."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    dispute_id: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    update_time: str | None = Field(default=None)
    status: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    dispute_state: str | None = Field(default=None)
    dispute_life_cycle_stage: str | None = Field(default=None)
    dispute_channel: str | None = Field(default=None)
    dispute_amount: Money | None = Field(default=None)
    outcome: str | None = Field(default=None)
    disputed_transactions: list[DisputeDisputedTransactionsItem] | None = Field(default=None)
    links: list[DisputeLinksItem] | None = Field(default=None)

class DisputesListLinksItem(BaseModel):
    """Nested schema for DisputesList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class DisputesList(BaseModel):
    """List of disputes."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: list[Dispute] | None = Field(default=None)
    links: list[DisputesListLinksItem] | None = Field(default=None)

class ProductLinksItem(BaseModel):
    """Nested schema for Product.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class Product(BaseModel):
    """A PayPal catalog product (summary)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    links: list[ProductLinksItem] | None = Field(default=None)

class ProductsListLinksItem(BaseModel):
    """Nested schema for ProductsList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class ProductsList(BaseModel):
    """List of catalog products."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    products: list[Product] | None = Field(default=None)
    links: list[ProductsListLinksItem] | None = Field(default=None)

class ProductDetailsLinksItem(BaseModel):
    """Nested schema for ProductDetails.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class ProductDetails(BaseModel):
    """Detailed catalog product information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    category: str | None = Field(default=None)
    image_url: str | None = Field(default=None)
    home_url: str | None = Field(default=None)
    create_time: str | None = Field(default=None)
    update_time: str | None = Field(default=None)
    links: list[ProductDetailsLinksItem] | None = Field(default=None)

class InvoiceSearchParamsCreationDateRange(BaseModel):
    """Filter by invoice creation date range."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: str | None = Field(default=None, description="Start date in ISO 8601 format.")
    """Start date in ISO 8601 format."""
    end: str | None = Field(default=None, description="End date in ISO 8601 format.")
    """End date in ISO 8601 format."""

class InvoiceSearchParams(BaseModel):
    """Parameters for searching invoices."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    creation_date_range: InvoiceSearchParamsCreationDateRange | None = Field(default=None)

class InvoiceRefunds(BaseModel):
    """Refund records for this invoice."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    refund_amount: Money | None = Field(default=None)
    transactions: list[dict[str, Any]] | None = Field(default=None)

class InvoiceDetailPaymentTerm(BaseModel):
    """Nested schema for InvoiceDetail.payment_term"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    term_type: str | None = Field(default=None, description="Payment term type.")
    """Payment term type."""
    due_date: str | None = Field(default=None, description="Due date.")
    """Due date."""

class InvoiceDetailMetadata(BaseModel):
    """Nested schema for InvoiceDetail.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    create_time: str | None = Field(default=None, description="Invoice creation time.")
    """Invoice creation time."""
    created_by: str | None = Field(default=None, description="Creator of the invoice.")
    """Creator of the invoice."""
    last_update_time: str | None = Field(default=None, description="Last update time.")
    """Last update time."""
    last_updated_by: str | None = Field(default=None, description="Last updater.")
    """Last updater."""
    first_sent_time: str | None = Field(default=None, description="First sent time.")
    """First sent time."""
    last_sent_time: str | None = Field(default=None, description="Last sent time.")
    """Last sent time."""
    created_by_flow: str | None = Field(default=None, description="Flow that created the invoice.")
    """Flow that created the invoice."""
    invoicer_view_url: str | None = Field(default=None, description="Invoicer view URL.")
    """Invoicer view URL."""
    recipient_view_url: str | None = Field(default=None, description="Recipient view URL.")
    """Recipient view URL."""
    cancel_time: str | None = Field(default=None, description="Cancellation time.")
    """Cancellation time."""
    cancelled_by: str | None = Field(default=None, description="Canceller.")
    """Canceller."""

class InvoiceDetail(BaseModel):
    """Invoice detail information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: str | None = Field(default=None, description="Reference for the invoice.")
    """Reference for the invoice."""
    currency_code: str | None = Field(default=None, description="Currency code.")
    """Currency code."""
    note: str | None = Field(default=None, description="Note to the recipient.")
    """Note to the recipient."""
    terms_and_conditions: str | None = Field(default=None, description="Terms and conditions.")
    """Terms and conditions."""
    memo: str | None = Field(default=None, description="Memo for the invoice.")
    """Memo for the invoice."""
    invoice_number: str | None = Field(default=None, description="Invoice number.")
    """Invoice number."""
    invoice_date: str | None = Field(default=None, description="Invoice date.")
    """Invoice date."""
    payment_term: InvoiceDetailPaymentTerm | None = Field(default=None)
    metadata: InvoiceDetailMetadata | None = Field(default=None)

class InvoiceItemsItemTax(BaseModel):
    """Nested schema for InvoiceItemsItem.tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    percent: str | None = Field(default=None)
    amount: Money | None = Field(default=None)

class InvoiceItemsItem(BaseModel):
    """Nested schema for Invoice.items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    quantity: str | None = Field(default=None)
    unit_amount: Money | None = Field(default=None)
    tax: InvoiceItemsItemTax | None = Field(default=None)
    unit_of_measure: str | None = Field(default=None)

class InvoiceAmountBreakdown(BaseModel):
    """Nested schema for InvoiceAmount.breakdown"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_total: Money | None = Field(default=None)
    discount: dict[str, Any] | None = Field(default=None)
    tax_total: Money | None = Field(default=None)
    shipping: Money | None = Field(default=None)
    custom: dict[str, Any] | None = Field(default=None)

class InvoiceAmount(BaseModel):
    """Total invoice amount."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: str | None = Field(default=None)
    value: str | None = Field(default=None)
    breakdown: InvoiceAmountBreakdown | None = Field(default=None)

class InvoiceInvoicerName(BaseModel):
    """Nested schema for InvoiceInvoicer.name"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    given_name: str | None = Field(default=None)
    surname: str | None = Field(default=None)
    full_name: str | None = Field(default=None)

class InvoiceInvoicer(BaseModel):
    """Invoicer details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: InvoiceInvoicerName | None = Field(default=None)
    address: dict[str, Any] | None = Field(default=None)
    email_address: str | None = Field(default=None, description="Invoicer email.")
    """Invoicer email."""

class InvoiceConfigurationPartialPayment(BaseModel):
    """Nested schema for InvoiceConfiguration.partial_payment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_partial_payment: str | None = Field(default=None)
    minimum_amount_due: Money | None = Field(default=None)

class InvoiceConfiguration(BaseModel):
    """Invoice configuration."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tax_calculated_after_discount: str | None = Field(default=None)
    tax_inclusive: str | None = Field(default=None)
    allow_tip: str | None = Field(default=None)
    template_id: str | None = Field(default=None)
    partial_payment: InvoiceConfigurationPartialPayment | None = Field(default=None)

class InvoicePayments(BaseModel):
    """Payment records for this invoice."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    paid_amount: Money | None = Field(default=None)
    transactions: list[dict[str, Any]] | None = Field(default=None)

class InvoicePrimaryRecipientsItemBillingInfoName(BaseModel):
    """Nested schema for InvoicePrimaryRecipientsItemBillingInfo.name"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    given_name: str | None = Field(default=None)
    surname: str | None = Field(default=None)
    full_name: str | None = Field(default=None)

class InvoicePrimaryRecipientsItemBillingInfo(BaseModel):
    """Nested schema for InvoicePrimaryRecipientsItem.billing_info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: InvoicePrimaryRecipientsItemBillingInfoName | None = Field(default=None)
    email_address: str | None = Field(default=None)
    additional_info_value: str | None = Field(default=None)

class InvoicePrimaryRecipientsItem(BaseModel):
    """Nested schema for Invoice.primary_recipients_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    billing_info: InvoicePrimaryRecipientsItemBillingInfo | None = Field(default=None)

class InvoiceLinksItem(BaseModel):
    """Nested schema for Invoice.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class Invoice(BaseModel):
    """A PayPal invoice object."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    status: str | None = Field(default=None)
    detail: InvoiceDetail | None = Field(default=None)
    invoicer: InvoiceInvoicer | None = Field(default=None)
    primary_recipients: list[InvoicePrimaryRecipientsItem] | None = Field(default=None)
    additional_recipients: list[str] | None = Field(default=None)
    items: list[InvoiceItemsItem] | None = Field(default=None)
    amount: InvoiceAmount | None = Field(default=None)
    configuration: InvoiceConfiguration | None = Field(default=None)
    due_amount: Money | None = Field(default=None)
    payments: InvoicePayments | None = Field(default=None)
    refunds: InvoiceRefunds | None = Field(default=None)
    links: list[InvoiceLinksItem] | None = Field(default=None)

class InvoicesListLinksItem(BaseModel):
    """Nested schema for InvoicesList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None = Field(default=None)
    rel: str | None = Field(default=None)
    method: str | None = Field(default=None)

class InvoicesList(BaseModel):
    """Paginated list of invoices from search."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: list[Invoice] | None = Field(default=None)
    total_items: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    links: list[InvoicesListLinksItem] | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TransactionsListResultMeta(BaseModel):
    """Metadata for transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    page: int | None = Field(default=None)

class ListPaymentsListResultMeta(BaseModel):
    """Metadata for list_payments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_id: str | None = Field(default=None)

class ListDisputesListResultMeta(BaseModel):
    """Metadata for list_disputes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: list[dict[str, Any]] | None = Field(default=None)

class ListProductsListResultMeta(BaseModel):
    """Metadata for list_products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: list[dict[str, Any]] | None = Field(default=None)

class SearchInvoicesListResultMeta(BaseModel):
    """Metadata for search_invoices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: list[dict[str, Any]] | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class PaypalTransactionCheckResult(BaseModel):
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


class PaypalTransactionExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class PaypalTransactionExecuteResultWithMeta(PaypalTransactionExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class TransactionsSearchData(BaseModel):
    """Search result data for transactions entity."""
    model_config = ConfigDict(extra="allow")

    auction_info: dict[str, Any] | None = None
    """Information related to an auction"""
    cart_info: dict[str, Any] | None = None
    """Details of items in the cart"""
    incentive_info: dict[str, Any] | None = None
    """Details of any incentives applied"""
    payer_info: dict[str, Any] | None = None
    """Information about the payer"""
    shipping_info: dict[str, Any] | None = None
    """Shipping information"""
    store_info: dict[str, Any] | None = None
    """Information about the store"""
    transaction_id: str | None = None
    """Unique ID of the transaction"""
    transaction_info: dict[str, Any] | None = None
    """Detailed information about the transaction"""
    transaction_initiation_date: str | None = None
    """Date and time when the transaction was initiated"""
    transaction_updated_date: str | None = None
    """Date and time when the transaction was last updated"""


class BalancesSearchData(BaseModel):
    """Search result data for balances entity."""
    model_config = ConfigDict(extra="allow")

    account_id: str | None = None
    """The unique identifier of the account."""
    as_of_time: str | None = None
    """The timestamp when the balances data was reported."""
    balances: list[Any] | None = None
    """Object containing information about the account balances."""
    last_refresh_time: str | None = None
    """The timestamp when the balances data was last refreshed."""


class ListProductsSearchData(BaseModel):
    """Search result data for list_products entity."""
    model_config = ConfigDict(extra="allow")

    create_time: str | None = None
    """The time when the product was created"""
    description: str | None = None
    """Detailed information or features of the product"""
    id: str | None = None
    """Unique identifier for the product"""
    links: list[Any] | None = None
    """List of links related to the fetched products."""
    name: str | None = None
    """The name or title of the product"""


class ShowProductDetailsSearchData(BaseModel):
    """Search result data for show_product_details entity."""
    model_config = ConfigDict(extra="allow")

    category: str | None = None
    """The category to which the product belongs"""
    create_time: str | None = None
    """The date and time when the product was created"""
    description: str | None = None
    """The detailed description of the product"""
    home_url: str | None = None
    """The URL for the home page of the product"""
    id: str | None = None
    """The unique identifier for the product"""
    image_url: str | None = None
    """The URL to the image representing the product"""
    links: list[Any] | None = None
    """Contains links related to the product details."""
    name: str | None = None
    """The name of the product"""
    type_: str | None = None
    """The type or category of the product"""
    update_time: str | None = None
    """The date and time when the product was last updated"""


class ListDisputesSearchData(BaseModel):
    """Search result data for list_disputes entity."""
    model_config = ConfigDict(extra="allow")

    create_time: str | None = None
    """The timestamp when the dispute was created."""
    dispute_amount: dict[str, Any] | None = None
    """Details about the disputed amount."""
    dispute_channel: str | None = None
    """The channel through which the dispute was initiated."""
    dispute_id: str | None = None
    """The unique identifier for the dispute."""
    dispute_life_cycle_stage: str | None = None
    """The stage in the life cycle of the dispute."""
    dispute_state: str | None = None
    """The current state of the dispute."""
    disputed_transactions: list[Any] | None = None
    """Details of transactions involved in the dispute."""
    links: list[Any] | None = None
    """Links related to the dispute."""
    outcome: str | None = None
    """The outcome of the dispute resolution."""
    reason: str | None = None
    """The reason for the dispute."""
    status: str | None = None
    """The current status of the dispute."""
    update_time: str | None = None
    """The timestamp when the dispute was last updated."""
    updated_time_cut: str | None = None
    """The cut-off timestamp for the last update."""


class SearchInvoicesSearchData(BaseModel):
    """Search result data for search_invoices entity."""
    model_config = ConfigDict(extra="allow")

    additional_recipients: list[Any] | None = None
    """List of additional recipients associated with the invoice"""
    amount: dict[str, Any] | None = None
    """Detailed breakdown of the invoice amount"""
    configuration: dict[str, Any] | None = None
    """Configuration settings related to the invoice"""
    detail: dict[str, Any] | None = None
    """Detailed information about the invoice"""
    due_amount: dict[str, Any] | None = None
    """Due amount remaining to be paid for the invoice"""
    gratuity: dict[str, Any] | None = None
    """Gratuity amount included in the invoice"""
    id: str | None = None
    """Unique identifier of the invoice"""
    invoicer: dict[str, Any] | None = None
    """Information about the invoicer associated with the invoice"""
    last_update_time: str | None = None
    """Date and time of the last update made to the invoice"""
    links: list[Any] | None = None
    """Links associated with the invoice"""
    payments: dict[str, Any] | None = None
    """Payment transactions associated with the invoice"""
    primary_recipients: list[Any] | None = None
    """Primary recipients associated with the invoice"""
    refunds: dict[str, Any] | None = None
    """Refund transactions associated with the invoice"""
    status: str | None = None
    """Current status of the invoice"""


class ListPaymentsSearchData(BaseModel):
    """Search result data for list_payments entity."""
    model_config = ConfigDict(extra="allow")

    cart: str | None = None
    """Details of the cart associated with the payment."""
    create_time: str | None = None
    """The date and time when the payment was created."""
    id: str | None = None
    """Unique identifier for the payment."""
    intent: str | None = None
    """The intention or purpose behind the payment."""
    links: list[Any] | None = None
    """Collection of links related to the payment"""
    payer: dict[str, Any] | None = None
    """Details of the payer who made the payment"""
    state: str | None = None
    """The state of the payment."""
    transactions: list[Any] | None = None
    """List of transactions associated with the payment"""
    update_time: str | None = None
    """The date and time when the payment was last updated."""


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

TransactionsSearchResult = AirbyteSearchResult[TransactionsSearchData]
"""Search result type for transactions entity."""

BalancesSearchResult = AirbyteSearchResult[BalancesSearchData]
"""Search result type for balances entity."""

ListProductsSearchResult = AirbyteSearchResult[ListProductsSearchData]
"""Search result type for list_products entity."""

ShowProductDetailsSearchResult = AirbyteSearchResult[ShowProductDetailsSearchData]
"""Search result type for show_product_details entity."""

ListDisputesSearchResult = AirbyteSearchResult[ListDisputesSearchData]
"""Search result type for list_disputes entity."""

SearchInvoicesSearchResult = AirbyteSearchResult[SearchInvoicesSearchData]
"""Search result type for search_invoices entity."""

ListPaymentsSearchResult = AirbyteSearchResult[ListPaymentsSearchData]
"""Search result type for list_payments entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

BalancesListResult = PaypalTransactionExecuteResult[BalancesResponse]
"""Result type for balances.list operation."""

TransactionsListResult = PaypalTransactionExecuteResultWithMeta[list[Transaction], TransactionsListResultMeta]
"""Result type for transactions.list operation with data and metadata."""

ListPaymentsListResult = PaypalTransactionExecuteResultWithMeta[list[Payment], ListPaymentsListResultMeta]
"""Result type for list_payments.list operation with data and metadata."""

ListDisputesListResult = PaypalTransactionExecuteResultWithMeta[list[Dispute], ListDisputesListResultMeta]
"""Result type for list_disputes.list operation with data and metadata."""

ListProductsListResult = PaypalTransactionExecuteResultWithMeta[list[Product], ListProductsListResultMeta]
"""Result type for list_products.list operation with data and metadata."""

SearchInvoicesListResult = PaypalTransactionExecuteResultWithMeta[list[Invoice], SearchInvoicesListResultMeta]
"""Result type for search_invoices.list operation with data and metadata."""

