"""
Pydantic models for paypal-transaction connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
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

    currency_code: Union[str, Any] = Field(default=None)
    value: Union[str, Any] = Field(default=None)

class BalanceDetail(BaseModel):
    """Balance information for a single currency."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    primary: Union[bool, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    total_balance: Union[Money, Any] = Field(default=None)
    available_balance: Union[Money, Any] = Field(default=None)
    withheld_balance: Union[Money, Any] = Field(default=None)

class BalancesResponse(BaseModel):
    """Balances response with account balance details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    balances: Union[list[BalanceDetail], Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None)
    as_of_time: Union[str, Any] = Field(default=None)
    last_refresh_time: Union[str, Any] = Field(default=None)

class PayerName(BaseModel):
    """Payer name details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    given_name: Union[str, Any] = Field(default=None)
    surname: Union[str, Any] = Field(default=None)
    alternate_full_name: Union[str, Any] = Field(default=None)

class PayerInfo(BaseModel):
    """Information about the payer."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: Union[str, Any] = Field(default=None)
    email_address: Union[str, Any] = Field(default=None)
    address_status: Union[str, Any] = Field(default=None)
    payer_status: Union[str, Any] = Field(default=None)
    payer_name: Union[PayerName, Any] = Field(default=None)
    country_code: Union[str, Any] = Field(default=None)

class TransactionInfo(BaseModel):
    """Detailed transaction information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    paypal_account_id: Union[str, Any] = Field(default=None)
    transaction_id: Union[str, Any] = Field(default=None)
    paypal_reference_id: Union[str, Any] = Field(default=None)
    paypal_reference_id_type: Union[str, Any] = Field(default=None)
    transaction_event_code: Union[str, Any] = Field(default=None)
    transaction_initiation_date: Union[str, Any] = Field(default=None)
    transaction_updated_date: Union[str, Any] = Field(default=None)
    transaction_amount: Union[Money, Any] = Field(default=None)
    fee_amount: Union[Money, Any] = Field(default=None)
    insurance_amount: Union[Money, Any] = Field(default=None)
    shipping_amount: Union[Money, Any] = Field(default=None)
    shipping_discount_amount: Union[Money, Any] = Field(default=None)
    transaction_status: Union[str, Any] = Field(default=None)
    transaction_subject: Union[str, Any] = Field(default=None)
    transaction_note: Union[str, Any] = Field(default=None)
    invoice_id: Union[str, Any] = Field(default=None)
    custom_field: Union[str, Any] = Field(default=None)
    protection_eligibility: Union[str, Any] = Field(default=None)

class ShippingAddress(BaseModel):
    """Shipping address details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line1: Union[str, Any] = Field(default=None)
    line2: Union[str, Any] = Field(default=None)
    city: Union[str, Any] = Field(default=None)
    country_code: Union[str, Any] = Field(default=None)
    postal_code: Union[str, Any] = Field(default=None)

class ShippingInfo(BaseModel):
    """Shipping information for the transaction."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    address: Union[ShippingAddress, Any] = Field(default=None)

class ItemDetailTaxAmountsItem(BaseModel):
    """Nested schema for ItemDetail.tax_amounts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tax_amount: Union[Money, Any] = Field(default=None)

class ItemDetail(BaseModel):
    """Details for a single cart item."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_code: Union[str, Any] = Field(default=None)
    item_name: Union[str, Any] = Field(default=None)
    item_description: Union[str, Any] = Field(default=None)
    item_quantity: Union[str, Any] = Field(default=None)
    item_unit_price: Union[Money, Any] = Field(default=None)
    item_amount: Union[Money, Any] = Field(default=None)
    total_item_amount: Union[Money, Any] = Field(default=None)
    tax_amounts: Union[list[ItemDetailTaxAmountsItem], Any] = Field(default=None)
    invoice_number: Union[str, Any] = Field(default=None)

class CartInfo(BaseModel):
    """Cart information for the transaction."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_details: Union[list[ItemDetail], Any] = Field(default=None)
    tax_inclusive: Union[bool, Any] = Field(default=None)
    paypal_invoice_id: Union[str, Any] = Field(default=None)

class AuctionInfo(BaseModel):
    """Auction information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auction_site: Union[str, Any] = Field(default=None)
    auction_item_site: Union[str, Any] = Field(default=None)
    auction_buyer_id: Union[str, Any] = Field(default=None)
    auction_closing_date: Union[str, Any] = Field(default=None)

class IncentiveDetail(BaseModel):
    """Incentive detail."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incentive_type: Union[str, Any] = Field(default=None)
    incentive_code: Union[str, Any] = Field(default=None)
    incentive_amount: Union[Money, Any] = Field(default=None)
    incentive_program_code: Union[str, Any] = Field(default=None)

class IncentiveInfo(BaseModel):
    """Incentive information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incentive_details: Union[list[IncentiveDetail], Any] = Field(default=None)

class StoreInfo(BaseModel):
    """Store information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    store_id: Union[str, Any] = Field(default=None)
    terminal_id: Union[str, Any] = Field(default=None)

class Transaction(BaseModel):
    """A single PayPal transaction with full details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transaction_info: Union[TransactionInfo, Any] = Field(default=None)
    payer_info: Union[PayerInfo, Any] = Field(default=None)
    shipping_info: Union[ShippingInfo, Any] = Field(default=None)
    cart_info: Union[CartInfo, Any] = Field(default=None)
    auction_info: Union[AuctionInfo, Any] = Field(default=None)
    incentive_info: Union[IncentiveInfo, Any] = Field(default=None)
    store_info: Union[StoreInfo, Any] = Field(default=None)
    transaction_id: Union[str, Any] = Field(default=None)
    transaction_updated_date: Union[str, Any] = Field(default=None)

class TransactionsListLinksItem(BaseModel):
    """Nested schema for TransactionsList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class TransactionsList(BaseModel):
    """Paginated list of transactions."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transaction_details: Union[list[Transaction], Any] = Field(default=None)
    account_number: Union[str, Any] = Field(default=None)
    start_date: Union[str, Any] = Field(default=None)
    end_date: Union[str, Any] = Field(default=None)
    last_refreshed_datetime: Union[str, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    total_items: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    links: Union[list[TransactionsListLinksItem], Any] = Field(default=None)

class PaymentPayerPayerInfo(BaseModel):
    """Nested schema for PaymentPayer.payer_info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str, Any] = Field(default=None, description="Payer email.")
    """Payer email."""
    first_name: Union[str, Any] = Field(default=None, description="Payer first name.")
    """Payer first name."""
    last_name: Union[str, Any] = Field(default=None, description="Payer last name.")
    """Payer last name."""
    payer_id: Union[str, Any] = Field(default=None, description="Payer ID.")
    """Payer ID."""
    country_code: Union[str, Any] = Field(default=None, description="Payer country code.")
    """Payer country code."""

class PaymentPayer(BaseModel):
    """Payer information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_method: Union[str, Any] = Field(default=None, description="Payment method.")
    """Payment method."""
    status: Union[str, Any] = Field(default=None, description="Payer status.")
    """Payer status."""
    payer_info: Union[PaymentPayerPayerInfo, Any] = Field(default=None)

class PaymentLinksItem(BaseModel):
    """Nested schema for Payment.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class PaymentTransactionsItemAmountDetails(BaseModel):
    """Nested schema for PaymentTransactionsItemAmount.details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subtotal: Union[str, Any] = Field(default=None)
    shipping: Union[str, Any] = Field(default=None)
    insurance: Union[str, Any] = Field(default=None)
    handling_fee: Union[str, Any] = Field(default=None)
    shipping_discount: Union[str, Any] = Field(default=None)

class PaymentTransactionsItemAmount(BaseModel):
    """Nested schema for PaymentTransactionsItem.amount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[str, Any] = Field(default=None, description="Total amount.")
    """Total amount."""
    currency: Union[str, Any] = Field(default=None, description="Currency code.")
    """Currency code."""
    details: Union[PaymentTransactionsItemAmountDetails, Any] = Field(default=None)

class PaymentTransactionsItem(BaseModel):
    """Nested schema for Payment.transactions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[PaymentTransactionsItemAmount, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None, description="Transaction description.")
    """Transaction description."""
    related_resources: Union[list[dict[str, Any]], Any] = Field(default=None)

class Payment(BaseModel):
    """A PayPal payment object."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    intent: Union[str, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    cart: Union[str, Any] = Field(default=None)
    payer: Union[PaymentPayer, Any] = Field(default=None)
    transactions: Union[list[PaymentTransactionsItem], Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    update_time: Union[str, Any] = Field(default=None)
    links: Union[list[PaymentLinksItem], Any] = Field(default=None)

class PaymentsList(BaseModel):
    """List of payments."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payments: Union[list[Payment], Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)
    next_id: Union[str, Any] = Field(default=None)

class DisputeLinksItem(BaseModel):
    """Nested schema for Dispute.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class DisputeDisputedTransactionsItemSeller(BaseModel):
    """Nested schema for DisputeDisputedTransactionsItem.seller"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    merchant_id: Union[str, Any] = Field(default=None, description="Seller's merchant ID.")
    """Seller's merchant ID."""

class DisputeDisputedTransactionsItem(BaseModel):
    """Nested schema for Dispute.disputed_transactions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    buyer_transaction_id: Union[str, Any] = Field(default=None, description="Buyer's transaction ID.")
    """Buyer's transaction ID."""
    seller: Union[DisputeDisputedTransactionsItemSeller, Any] = Field(default=None)

class Dispute(BaseModel):
    """A PayPal dispute object."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    dispute_id: Union[str, Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    update_time: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    reason: Union[str, Any] = Field(default=None)
    dispute_state: Union[str, Any] = Field(default=None)
    dispute_life_cycle_stage: Union[str, Any] = Field(default=None)
    dispute_channel: Union[str, Any] = Field(default=None)
    dispute_amount: Union[Money, Any] = Field(default=None)
    outcome: Union[str, Any] = Field(default=None)
    disputed_transactions: Union[list[DisputeDisputedTransactionsItem], Any] = Field(default=None)
    links: Union[list[DisputeLinksItem], Any] = Field(default=None)

class DisputesListLinksItem(BaseModel):
    """Nested schema for DisputesList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class DisputesList(BaseModel):
    """List of disputes."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Dispute], Any] = Field(default=None)
    links: Union[list[DisputesListLinksItem], Any] = Field(default=None)

class ProductLinksItem(BaseModel):
    """Nested schema for Product.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class Product(BaseModel):
    """A PayPal catalog product (summary)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    links: Union[list[ProductLinksItem], Any] = Field(default=None)

class ProductsListLinksItem(BaseModel):
    """Nested schema for ProductsList.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class ProductsList(BaseModel):
    """List of catalog products."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    products: Union[list[Product], Any] = Field(default=None)
    links: Union[list[ProductsListLinksItem], Any] = Field(default=None)

class ProductDetailsLinksItem(BaseModel):
    """Nested schema for ProductDetails.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class ProductDetails(BaseModel):
    """Detailed catalog product information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    category: Union[str, Any] = Field(default=None)
    image_url: Union[str, Any] = Field(default=None)
    home_url: Union[str, Any] = Field(default=None)
    create_time: Union[str, Any] = Field(default=None)
    update_time: Union[str, Any] = Field(default=None)
    links: Union[list[ProductDetailsLinksItem], Any] = Field(default=None)

class InvoiceSearchParamsCreationDateRange(BaseModel):
    """Filter by invoice creation date range."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: Union[str, Any] = Field(default=None, description="Start date in ISO 8601 format.")
    """Start date in ISO 8601 format."""
    end: Union[str, Any] = Field(default=None, description="End date in ISO 8601 format.")
    """End date in ISO 8601 format."""

class InvoiceSearchParams(BaseModel):
    """Parameters for searching invoices."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    creation_date_range: Union[InvoiceSearchParamsCreationDateRange, Any] = Field(default=None)

class InvoiceLinksItem(BaseModel):
    """Nested schema for Invoice.links_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: Union[str, Any] = Field(default=None)
    rel: Union[str, Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)

class InvoiceDetailMetadata(BaseModel):
    """Nested schema for InvoiceDetail.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    create_time: Union[str, Any] = Field(default=None, description="Invoice creation time.")
    """Invoice creation time."""
    created_by: Union[str, Any] = Field(default=None, description="Creator of the invoice.")
    """Creator of the invoice."""
    last_update_time: Union[str, Any] = Field(default=None, description="Last update time.")
    """Last update time."""
    last_updated_by: Union[str, Any] = Field(default=None, description="Last updater.")
    """Last updater."""
    first_sent_time: Union[str, Any] = Field(default=None, description="First sent time.")
    """First sent time."""
    last_sent_time: Union[str, Any] = Field(default=None, description="Last sent time.")
    """Last sent time."""
    created_by_flow: Union[str, Any] = Field(default=None, description="Flow that created the invoice.")
    """Flow that created the invoice."""
    invoicer_view_url: Union[str, Any] = Field(default=None, description="Invoicer view URL.")
    """Invoicer view URL."""
    recipient_view_url: Union[str, Any] = Field(default=None, description="Recipient view URL.")
    """Recipient view URL."""
    cancel_time: Union[str, Any] = Field(default=None, description="Cancellation time.")
    """Cancellation time."""
    cancelled_by: Union[str, Any] = Field(default=None, description="Canceller.")
    """Canceller."""

class InvoiceDetailPaymentTerm(BaseModel):
    """Nested schema for InvoiceDetail.payment_term"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    term_type: Union[str, Any] = Field(default=None, description="Payment term type.")
    """Payment term type."""
    due_date: Union[str, Any] = Field(default=None, description="Due date.")
    """Due date."""

class InvoiceDetail(BaseModel):
    """Invoice detail information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str, Any] = Field(default=None, description="Reference for the invoice.")
    """Reference for the invoice."""
    currency_code: Union[str, Any] = Field(default=None, description="Currency code.")
    """Currency code."""
    note: Union[str, Any] = Field(default=None, description="Note to the recipient.")
    """Note to the recipient."""
    terms_and_conditions: Union[str, Any] = Field(default=None, description="Terms and conditions.")
    """Terms and conditions."""
    memo: Union[str, Any] = Field(default=None, description="Memo for the invoice.")
    """Memo for the invoice."""
    invoice_number: Union[str, Any] = Field(default=None, description="Invoice number.")
    """Invoice number."""
    invoice_date: Union[str, Any] = Field(default=None, description="Invoice date.")
    """Invoice date."""
    payment_term: Union[InvoiceDetailPaymentTerm, Any] = Field(default=None)
    metadata: Union[InvoiceDetailMetadata, Any] = Field(default=None)

class InvoicePrimaryRecipientsItemBillingInfoName(BaseModel):
    """Nested schema for InvoicePrimaryRecipientsItemBillingInfo.name"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    given_name: Union[str, Any] = Field(default=None)
    surname: Union[str, Any] = Field(default=None)
    full_name: Union[str, Any] = Field(default=None)

class InvoicePrimaryRecipientsItemBillingInfo(BaseModel):
    """Nested schema for InvoicePrimaryRecipientsItem.billing_info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[InvoicePrimaryRecipientsItemBillingInfoName, Any] = Field(default=None)
    email_address: Union[str, Any] = Field(default=None)
    additional_info_value: Union[str, Any] = Field(default=None)

class InvoicePrimaryRecipientsItem(BaseModel):
    """Nested schema for Invoice.primary_recipients_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    billing_info: Union[InvoicePrimaryRecipientsItemBillingInfo, Any] = Field(default=None)

class InvoicePayments(BaseModel):
    """Payment records for this invoice."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    paid_amount: Union[Money, Any] = Field(default=None)
    transactions: Union[list[dict[str, Any]], Any] = Field(default=None)

class InvoiceInvoicerName(BaseModel):
    """Nested schema for InvoiceInvoicer.name"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    given_name: Union[str, Any] = Field(default=None)
    surname: Union[str, Any] = Field(default=None)
    full_name: Union[str, Any] = Field(default=None)

class InvoiceInvoicer(BaseModel):
    """Invoicer details."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[InvoiceInvoicerName, Any] = Field(default=None)
    address: Union[dict[str, Any], Any] = Field(default=None)
    email_address: Union[str, Any] = Field(default=None, description="Invoicer email.")
    """Invoicer email."""

class InvoiceAmountBreakdown(BaseModel):
    """Nested schema for InvoiceAmount.breakdown"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    item_total: Union[Money, Any] = Field(default=None)
    discount: Union[dict[str, Any], Any] = Field(default=None)
    tax_total: Union[Money, Any] = Field(default=None)
    shipping: Union[Money, Any] = Field(default=None)
    custom: Union[dict[str, Any], Any] = Field(default=None)

class InvoiceAmount(BaseModel):
    """Total invoice amount."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None)
    value: Union[str, Any] = Field(default=None)
    breakdown: Union[InvoiceAmountBreakdown, Any] = Field(default=None)

class InvoiceRefunds(BaseModel):
    """Refund records for this invoice."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    refund_amount: Union[Money, Any] = Field(default=None)
    transactions: Union[list[dict[str, Any]], Any] = Field(default=None)

class InvoiceConfigurationPartialPayment(BaseModel):
    """Nested schema for InvoiceConfiguration.partial_payment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_partial_payment: Union[str, Any] = Field(default=None)
    minimum_amount_due: Union[Money, Any] = Field(default=None)

class InvoiceConfiguration(BaseModel):
    """Invoice configuration."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tax_calculated_after_discount: Union[str, Any] = Field(default=None)
    tax_inclusive: Union[str, Any] = Field(default=None)
    allow_tip: Union[str, Any] = Field(default=None)
    template_id: Union[str, Any] = Field(default=None)
    partial_payment: Union[InvoiceConfigurationPartialPayment, Any] = Field(default=None)

class InvoiceItemsItemTax(BaseModel):
    """Nested schema for InvoiceItemsItem.tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    percent: Union[str, Any] = Field(default=None)
    amount: Union[Money, Any] = Field(default=None)

class InvoiceItemsItem(BaseModel):
    """Nested schema for Invoice.items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    quantity: Union[str, Any] = Field(default=None)
    unit_amount: Union[Money, Any] = Field(default=None)
    tax: Union[InvoiceItemsItemTax, Any] = Field(default=None)
    unit_of_measure: Union[str, Any] = Field(default=None)

class Invoice(BaseModel):
    """A PayPal invoice object."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    detail: Union[InvoiceDetail, Any] = Field(default=None)
    invoicer: Union[InvoiceInvoicer, Any] = Field(default=None)
    primary_recipients: Union[list[InvoicePrimaryRecipientsItem], Any] = Field(default=None)
    additional_recipients: Union[list[str], Any] = Field(default=None)
    items: Union[list[InvoiceItemsItem], Any] = Field(default=None)
    amount: Union[InvoiceAmount, Any] = Field(default=None)
    configuration: Union[InvoiceConfiguration, Any] = Field(default=None)
    due_amount: Union[Money, Any] = Field(default=None)
    payments: Union[InvoicePayments, Any] = Field(default=None)
    refunds: Union[InvoiceRefunds, Any] = Field(default=None)
    links: Union[list[InvoiceLinksItem], Any] = Field(default=None)

class InvoicesList(BaseModel):
    """Paginated list of invoices from search."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: Union[list[Invoice], Any] = Field(default=None)
    total_items: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TransactionsListResultMeta(BaseModel):
    """Metadata for transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)

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

ListPaymentsListResult = PaypalTransactionExecuteResult[list[Payment]]
"""Result type for list_payments.list operation."""

ListDisputesListResult = PaypalTransactionExecuteResult[list[Dispute]]
"""Result type for list_disputes.list operation."""

ListProductsListResult = PaypalTransactionExecuteResult[list[Product]]
"""Result type for list_products.list operation."""

SearchInvoicesListResult = PaypalTransactionExecuteResult[list[Invoice]]
"""Result type for search_invoices.list operation."""

