"""
Pydantic models for stripe connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class StripeAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Stripe API Key (starts with sk_test_ or sk_live_)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CustomerShippingAddress(BaseModel):
    """Customer shipping address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str | None, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    line1: Union[str | None, Any] = Field(default=None, description="Address line 1, such as the street, PO Box, or company name")
    """Address line 1, such as the street, PO Box, or company name"""
    line2: Union[str | None, Any] = Field(default=None, description="Address line 2, such as the apartment, suite, unit, or building")
    """Address line 2, such as the apartment, suite, unit, or building"""
    postal_code: Union[str | None, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    state: Union[str | None, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""

class CustomerShipping(BaseModel):
    """Mailing and shipping address for the customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address: Union[CustomerShippingAddress, Any] = Field(default=None, description="Customer shipping address")
    """Customer shipping address"""
    name: Union[str, Any] = Field(default=None, description="Customer name")
    """Customer name"""
    phone: Union[str | None, Any] = Field(default=None, description="Customer phone (including extension)")
    """Customer phone (including extension)"""

class CustomerSourcesDataItem(BaseModel):
    """Nested schema for CustomerSources.data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique identifier for the object")
    """Unique identifier for the object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    account: Union[str | None, Any] = Field(default=None, description="The account this bank account belongs to")
    """The account this bank account belongs to"""
    account_holder_name: Union[str | None, Any] = Field(default=None, description="The name of the person or business that owns the bank account")
    """The name of the person or business that owns the bank account"""
    account_holder_type: Union[str | None, Any] = Field(default=None, description="The type of entity that holds the account")
    """The type of entity that holds the account"""
    account_type: Union[str | None, Any] = Field(default=None, description="The bank account type")
    """The bank account type"""
    available_payout_methods: Union[list[str] | None, Any] = Field(default=None, description="A set of available payout methods for this bank account")
    """A set of available payout methods for this bank account"""
    bank_name: Union[str | None, Any] = Field(default=None, description="Name of the bank associated with the routing number")
    """Name of the bank associated with the routing number"""
    country: Union[str, Any] = Field(default=None, description="Two-letter ISO code representing the country the bank account is located in")
    """Two-letter ISO code representing the country the bank account is located in"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO code for the currency paid out to the bank account")
    """Three-letter ISO code for the currency paid out to the bank account"""
    customer: Union[str | None, Any] = Field(default=None, description="The ID of the customer that the bank account is associated with")
    """The ID of the customer that the bank account is associated with"""
    fingerprint: Union[str | None, Any] = Field(default=None, description="Uniquely identifies this particular bank account")
    """Uniquely identifies this particular bank account"""
    last4: Union[str, Any] = Field(default=None, description="The last four digits of the bank account number")
    """The last four digits of the bank account number"""
    metadata: Union[dict[str, str] | None, Any] = Field(default=None, description="Set of key-value pairs that you can attach to an object")
    """Set of key-value pairs that you can attach to an object"""
    routing_number: Union[str | None, Any] = Field(default=None, description="The routing transit number for the bank account")
    """The routing transit number for the bank account"""
    status: Union[str, Any] = Field(default=None, description="The status of the bank account")
    """The status of the bank account"""

class CustomerSources(BaseModel):
    """The customer's payment sources, if any"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    data: Union[list[CustomerSourcesDataItem], Any] = Field(default=None, description="Details about each object")
    """Details about each object"""
    has_more: Union[bool, Any] = Field(default=None, description="True if this list has another page of items after this one")
    """True if this list has another page of items after this one"""
    url: Union[str, Any] = Field(default=None, description="The URL where this list can be accessed")
    """The URL where this list can be accessed"""

class CustomerInvoiceSettingsRenderingOptions(BaseModel):
    """Default options for invoice PDF rendering for this customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_tax_display: Union[str | None, Any] = Field(default=None, description="How line-item prices and amounts will be displayed with respect to tax on invoice PDFs")
    """How line-item prices and amounts will be displayed with respect to tax on invoice PDFs"""
    template: Union[str | None, Any] = Field(default=None, description="ID of the invoice rendering template to be used for this customer's invoices")
    """ID of the invoice rendering template to be used for this customer's invoices"""

class CustomerInvoiceSettingsCustomFieldsItem(BaseModel):
    """Nested schema for CustomerInvoiceSettings.custom_fields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="The name of the custom field")
    """The name of the custom field"""
    value: Union[str, Any] = Field(default=None, description="The value of the custom field")
    """The value of the custom field"""

class CustomerInvoiceSettings(BaseModel):
    """The customer's default invoice settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    custom_fields: Union[list[CustomerInvoiceSettingsCustomFieldsItem] | None, Any] = Field(default=None, description="Default custom fields to be displayed on invoices for this customer")
    """Default custom fields to be displayed on invoices for this customer"""
    default_payment_method: Union[str | None, Any] = Field(default=None, description="ID of a payment method that's attached to the customer")
    """ID of a payment method that's attached to the customer"""
    footer: Union[str | None, Any] = Field(default=None, description="Default footer to be displayed on invoices for this customer")
    """Default footer to be displayed on invoices for this customer"""
    rendering_options: Union[CustomerInvoiceSettingsRenderingOptions | None, Any] = Field(default=None, description="Default options for invoice PDF rendering for this customer")
    """Default options for invoice PDF rendering for this customer"""

class CustomerDiscountSource(BaseModel):
    """The source of the discount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    coupon: Union[str | None, Any] = Field(default=None, description="The coupon that was redeemed to create this discount")
    """The coupon that was redeemed to create this discount"""
    type: Union[str, Any] = Field(default=None, description="The source type of the discount")
    """The source type of the discount"""

class CustomerDiscount(BaseModel):
    """Describes the current discount active on the customer, if there is one"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="The ID of the discount object")
    """The ID of the discount object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    checkout_session: Union[str | None, Any] = Field(default=None, description="The Checkout session that this coupon is applied to, if applicable")
    """The Checkout session that this coupon is applied to, if applicable"""
    customer: Union[str | None, Any] = Field(default=None, description="The ID of the customer associated with this discount")
    """The ID of the customer associated with this discount"""
    customer_account: Union[str | None, Any] = Field(default=None, description="The ID of the account associated with this discount")
    """The ID of the account associated with this discount"""
    end: Union[int | None, Any] = Field(default=None, description="If the coupon has a duration of repeating, the date that this discount will end")
    """If the coupon has a duration of repeating, the date that this discount will end"""
    invoice: Union[str | None, Any] = Field(default=None, description="The invoice that the discount's coupon was applied to")
    """The invoice that the discount's coupon was applied to"""
    invoice_item: Union[str | None, Any] = Field(default=None, description="The invoice item that the discount's coupon was applied to")
    """The invoice item that the discount's coupon was applied to"""
    promotion_code: Union[str | None, Any] = Field(default=None, description="The promotion code applied to create this discount")
    """The promotion code applied to create this discount"""
    source: Union[CustomerDiscountSource, Any] = Field(default=None, description="The source of the discount")
    """The source of the discount"""
    start: Union[int, Any] = Field(default=None, description="Date that the coupon was applied")
    """Date that the coupon was applied"""
    subscription: Union[str | None, Any] = Field(default=None, description="The subscription that this coupon is applied to")
    """The subscription that this coupon is applied to"""
    subscription_item: Union[str | None, Any] = Field(default=None, description="The subscription item that this coupon is applied to")
    """The subscription item that this coupon is applied to"""

class CustomerCashBalanceSettings(BaseModel):
    """A hash of settings for this cash balance"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reconciliation_mode: Union[str, Any] = Field(default=None, description="The configuration for how funds that land in the customer cash balance are reconciled")
    """The configuration for how funds that land in the customer cash balance are reconciled"""
    using_merchant_default: Union[bool, Any] = Field(default=None, description="A flag to indicate if reconciliation mode returned is the user's default or is specific to this customer cash balance")
    """A flag to indicate if reconciliation mode returned is the user's default or is specific to this customer cash balance"""

class CustomerCashBalance(BaseModel):
    """The current funds being held by Stripe on behalf of the customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    available: Union[dict[str, Any] | None, Any] = Field(default=None, description="A hash of all cash balances available to this customer")
    """A hash of all cash balances available to this customer"""
    customer: Union[str, Any] = Field(default=None, description="The ID of the customer whose cash balance this object represents")
    """The ID of the customer whose cash balance this object represents"""
    customer_account: Union[str | None, Any] = Field(default=None, description="The ID of the account whose cash balance this object represents")
    """The ID of the account whose cash balance this object represents"""
    livemode: Union[bool, Any] = Field(default=None, description="Has the value true if the object exists in live mode or false if in test mode")
    """Has the value true if the object exists in live mode or false if in test mode"""
    settings: Union[CustomerCashBalanceSettings, Any] = Field(default=None, description="A hash of settings for this cash balance")
    """A hash of settings for this cash balance"""

class CustomerAddress(BaseModel):
    """The customer's address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str | None, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    line1: Union[str | None, Any] = Field(default=None, description="Address line 1, such as the street, PO Box, or company name")
    """Address line 1, such as the street, PO Box, or company name"""
    line2: Union[str | None, Any] = Field(default=None, description="Address line 2, such as the apartment, suite, unit, or building")
    """Address line 2, such as the apartment, suite, unit, or building"""
    postal_code: Union[str | None, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    state: Union[str | None, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""

class SubscriptionBillingModeFlexible(BaseModel):
    """Configure behavior for flexible billing mode"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    proration_discounts: Union[str, Any] = Field(default=None, description="Controls how invoices and invoice items display proration amounts and discount amounts")
    """Controls how invoices and invoice items display proration amounts and discount amounts"""

class SubscriptionBillingMode(BaseModel):
    """Controls how prorations and invoices for subscriptions are calculated and orchestrated"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    flexible: Union[SubscriptionBillingModeFlexible | None, Any] = Field(default=None, description="Configure behavior for flexible billing mode")
    """Configure behavior for flexible billing mode"""
    type: Union[str, Any] = Field(default=None, description="Controls how prorations and invoices for subscriptions are calculated and orchestrated")
    """Controls how prorations and invoices for subscriptions are calculated and orchestrated"""
    updated_at: Union[int | None, Any] = Field(default=None, description="Details on when the current billing_mode was adopted")
    """Details on when the current billing_mode was adopted"""

class SubscriptionBillingThresholds(BaseModel):
    """Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_gte: Union[int | None, Any] = Field(default=None, description="Monetary threshold that triggers the subscription to create an invoice")
    """Monetary threshold that triggers the subscription to create an invoice"""
    reset_billing_cycle_anchor: Union[bool | None, Any] = Field(default=None, description="Indicates if the billing_cycle_anchor should be reset when a threshold is reached")
    """Indicates if the billing_cycle_anchor should be reset when a threshold is reached"""

class SubscriptionCancellationDetails(BaseModel):
    """Details about why this subscription was cancelled"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment: Union[str | None, Any] = Field(default=None, description="Additional comments about why the user canceled the subscription")
    """Additional comments about why the user canceled the subscription"""
    feedback: Union[str | None, Any] = Field(default=None, description="The customer submitted reason for why they canceled")
    """The customer submitted reason for why they canceled"""
    reason: Union[str | None, Any] = Field(default=None, description="Why this subscription was canceled")
    """Why this subscription was canceled"""

class SubscriptionItemsDataItemBillingThresholds(BaseModel):
    """Define thresholds at which an invoice will be sent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    usage_gte: Union[int | None, Any] = Field(default=None, description="Usage threshold that triggers the subscription to create an invoice")
    """Usage threshold that triggers the subscription to create an invoice"""

class SubscriptionItemsDataItem(BaseModel):
    """Nested schema for SubscriptionItems.data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique identifier for the object")
    """Unique identifier for the object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    billing_thresholds: Union[SubscriptionItemsDataItemBillingThresholds | None, Any] = Field(default=None, description="Define thresholds at which an invoice will be sent")
    """Define thresholds at which an invoice will be sent"""
    created: Union[int, Any] = Field(default=None, description="Time at which the object was created")
    """Time at which the object was created"""
    current_period_end: Union[int, Any] = Field(default=None, description="The end time of this subscription item's current billing period")
    """The end time of this subscription item's current billing period"""
    current_period_start: Union[int, Any] = Field(default=None, description="The start time of this subscription item's current billing period")
    """The start time of this subscription item's current billing period"""
    discounts: Union[list[str], Any] = Field(default=None, description="The discounts applied to the subscription item")
    """The discounts applied to the subscription item"""
    metadata: Union[dict[str, str], Any] = Field(default=None, description="Set of key-value pairs")
    """Set of key-value pairs"""
    plan: Union[dict[str, Any] | None, Any] = Field(default=None, description="The plan the customer is subscribed to (deprecated, use price instead)")
    """The plan the customer is subscribed to (deprecated, use price instead)"""
    price: Union[dict[str, Any], Any] = Field(default=None, description="The price the customer is subscribed to")
    """The price the customer is subscribed to"""
    quantity: Union[int | None, Any] = Field(default=None, description="The quantity of the plan to which the customer should be subscribed")
    """The quantity of the plan to which the customer should be subscribed"""
    subscription: Union[str, Any] = Field(default=None, description="The subscription this subscription_item belongs to")
    """The subscription this subscription_item belongs to"""
    tax_rates: Union[list[dict[str, Any]] | None, Any] = Field(default=None, description="The tax rates which apply to this subscription_item")
    """The tax rates which apply to this subscription_item"""

class SubscriptionItems(BaseModel):
    """List of subscription items, each with an attached price"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    data: Union[list[SubscriptionItemsDataItem], Any] = Field(default=None, description="Details about each object")
    """Details about each object"""
    has_more: Union[bool, Any] = Field(default=None, description="True if this list has another page of items after this one")
    """True if this list has another page of items after this one"""
    url: Union[str, Any] = Field(default=None, description="The URL where this list can be accessed")
    """The URL where this list can be accessed"""
    total_count: Union[int, Any] = Field(default=None, description="The total count of items in the list")
    """The total count of items in the list"""

class SubscriptionTrialSettingsEndBehavior(BaseModel):
    """Nested schema for SubscriptionTrialSettings.end_behavior"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    missing_payment_method: Union[str, Any] = Field(default=None, description="Behavior when the trial ends and payment method is missing")
    """Behavior when the trial ends and payment method is missing"""

class SubscriptionTrialSettings(BaseModel):
    """Settings related to subscription trials"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    end_behavior: Union[SubscriptionTrialSettingsEndBehavior, Any] = Field(default=None)

class SubscriptionPaymentSettings(BaseModel):
    """Payment settings passed on to invoices created by the subscription"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_method_options: Union[dict[str, Any] | None, Any] = Field(default=None, description="Payment-method-specific configuration to provide to invoices")
    """Payment-method-specific configuration to provide to invoices"""
    payment_method_types: Union[list[str] | None, Any] = Field(default=None, description="The list of payment method types to provide to every invoice")
    """The list of payment method types to provide to every invoice"""

class SubscriptionInvoiceSettingsIssuer(BaseModel):
    """The connected account that issues the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: Union[str | None, Any] = Field(default=None, description="The connected account being referenced when type is account")
    """The connected account being referenced when type is account"""
    type: Union[str, Any] = Field(default=None, description="Type of the account referenced")
    """Type of the account referenced"""

class SubscriptionInvoiceSettings(BaseModel):
    """All invoices will be billed using the specified settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_tax_ids: Union[list[str] | None, Any] = Field(default=None, description="The account tax IDs associated with the subscription")
    """The account tax IDs associated with the subscription"""
    issuer: Union[SubscriptionInvoiceSettingsIssuer, Any] = Field(default=None, description="The connected account that issues the invoice")
    """The connected account that issues the invoice"""

class SubscriptionDefaultTaxRatesItemFlatAmount(BaseModel):
    """The amount of the tax rate when the rate_type is flat_amount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Amount of the tax when the rate_type is flat_amount")
    """Amount of the tax when the rate_type is flat_amount"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code, in lowercase")
    """Three-letter ISO currency code, in lowercase"""

class SubscriptionDefaultTaxRatesItem(BaseModel):
    """Nested schema for Subscription.default_tax_rates_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique identifier for the object")
    """Unique identifier for the object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    active: Union[bool, Any] = Field(default=None, description="Defaults to true")
    """Defaults to true"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    created: Union[int, Any] = Field(default=None, description="Time at which the object was created")
    """Time at which the object was created"""
    description: Union[str | None, Any] = Field(default=None, description="An arbitrary string attached to the tax rate for your internal use only")
    """An arbitrary string attached to the tax rate for your internal use only"""
    display_name: Union[str, Any] = Field(default=None, description="The display name of the tax rates")
    """The display name of the tax rates"""
    effective_percentage: Union[float | None, Any] = Field(default=None, description="Actual/effective tax rate percentage out of 100")
    """Actual/effective tax rate percentage out of 100"""
    flat_amount: Union[SubscriptionDefaultTaxRatesItemFlatAmount | None, Any] = Field(default=None, description="The amount of the tax rate when the rate_type is flat_amount")
    """The amount of the tax rate when the rate_type is flat_amount"""
    inclusive: Union[bool, Any] = Field(default=None, description="This specifies if the tax rate is inclusive or exclusive")
    """This specifies if the tax rate is inclusive or exclusive"""
    jurisdiction: Union[str | None, Any] = Field(default=None, description="The jurisdiction for the tax rate")
    """The jurisdiction for the tax rate"""
    jurisdiction_level: Union[str | None, Any] = Field(default=None, description="The level of the jurisdiction that imposes this tax rate")
    """The level of the jurisdiction that imposes this tax rate"""
    livemode: Union[bool, Any] = Field(default=None, description="Has the value true if the object exists in live mode or false if in test mode")
    """Has the value true if the object exists in live mode or false if in test mode"""
    metadata: Union[dict[str, str] | None, Any] = Field(default=None, description="Set of key-value pairs")
    """Set of key-value pairs"""
    percentage: Union[float, Any] = Field(default=None, description="Tax rate percentage out of 100")
    """Tax rate percentage out of 100"""
    rate_type: Union[str | None, Any] = Field(default=None, description="Indicates the type of tax rate applied to the taxable amount")
    """Indicates the type of tax rate applied to the taxable amount"""
    state: Union[str | None, Any] = Field(default=None, description="ISO 3166-2 subdivision code, without country prefix")
    """ISO 3166-2 subdivision code, without country prefix"""
    tax_type: Union[str | None, Any] = Field(default=None, description="The high-level tax type")
    """The high-level tax type"""

class SubscriptionBillingCycleAnchorConfig(BaseModel):
    """The fixed values used to calculate the billing_cycle_anchor"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    day_of_month: Union[int, Any] = Field(default=None, description="The day of the month of the billing_cycle_anchor")
    """The day of the month of the billing_cycle_anchor"""
    hour: Union[int | None, Any] = Field(default=None, description="The hour of the day of the billing_cycle_anchor")
    """The hour of the day of the billing_cycle_anchor"""
    minute: Union[int | None, Any] = Field(default=None, description="The minute of the hour of the billing_cycle_anchor")
    """The minute of the hour of the billing_cycle_anchor"""
    month: Union[int | None, Any] = Field(default=None, description="The month to start full cycle billing periods")
    """The month to start full cycle billing periods"""
    second: Union[int | None, Any] = Field(default=None, description="The second of the minute of the billing_cycle_anchor")
    """The second of the minute of the billing_cycle_anchor"""

class SubscriptionPauseCollection(BaseModel):
    """If specified, payment collection for this subscription will be paused"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    behavior: Union[str, Any] = Field(default=None, description="The payment collection behavior for this subscription while paused")
    """The payment collection behavior for this subscription while paused"""
    resumes_at: Union[int | None, Any] = Field(default=None, description="The time after which the subscription will resume collecting payments")
    """The time after which the subscription will resume collecting payments"""

class SubscriptionAutomaticTaxLiability(BaseModel):
    """The account that's liable for tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: Union[str | None, Any] = Field(default=None, description="The connected account being referenced when type is account")
    """The connected account being referenced when type is account"""
    type: Union[str, Any] = Field(default=None, description="Type of the account referenced")
    """Type of the account referenced"""

class SubscriptionAutomaticTax(BaseModel):
    """Automatic tax settings for this subscription"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    disabled_reason: Union[str | None, Any] = Field(default=None, description="If Stripe disabled automatic tax, this enum describes why")
    """If Stripe disabled automatic tax, this enum describes why"""
    enabled: Union[bool, Any] = Field(default=None, description="Whether Stripe automatically computes tax on this subscription")
    """Whether Stripe automatically computes tax on this subscription"""
    liability: Union[SubscriptionAutomaticTaxLiability | None, Any] = Field(default=None, description="The account that's liable for tax")
    """The account that's liable for tax"""

class Subscription(BaseModel):
    """Subscription type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    application: Union[str | None, Any] = Field(default=None)
    application_fee_percent: Union[float | None, Any] = Field(default=None)
    automatic_tax: Union[SubscriptionAutomaticTax, Any] = Field(default=None)
    billing_cycle_anchor: Union[int, Any] = Field(default=None)
    billing_cycle_anchor_config: Union[SubscriptionBillingCycleAnchorConfig | None, Any] = Field(default=None)
    billing_mode: Union[SubscriptionBillingMode, Any] = Field(default=None)
    billing_thresholds: Union[SubscriptionBillingThresholds | None, Any] = Field(default=None)
    cancel_at: Union[int | None, Any] = Field(default=None)
    cancel_at_period_end: Union[bool, Any] = Field(default=None)
    canceled_at: Union[int | None, Any] = Field(default=None)
    cancellation_details: Union[SubscriptionCancellationDetails | None, Any] = Field(default=None)
    collection_method: Union[str, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    customer: Union[str, Any] = Field(default=None)
    customer_account: Union[str | None, Any] = Field(default=None)
    days_until_due: Union[int | None, Any] = Field(default=None)
    default_payment_method: Union[str | None, Any] = Field(default=None)
    default_source: Union[str | None, Any] = Field(default=None)
    default_tax_rates: Union[list[SubscriptionDefaultTaxRatesItem] | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    discounts: Union[list[str], Any] = Field(default=None)
    ended_at: Union[int | None, Any] = Field(default=None)
    invoice_settings: Union[SubscriptionInvoiceSettings, Any] = Field(default=None)
    items: Union[SubscriptionItems, Any] = Field(default=None)
    latest_invoice: Union[str | None, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    next_pending_invoice_item_invoice: Union[int | None, Any] = Field(default=None)
    on_behalf_of: Union[str | None, Any] = Field(default=None)
    pause_collection: Union[SubscriptionPauseCollection | None, Any] = Field(default=None)
    payment_settings: Union[SubscriptionPaymentSettings | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    current_period_start: Union[int, Any] = Field(default=None)
    current_period_end: Union[int, Any] = Field(default=None)
    start_date: Union[int, Any] = Field(default=None)
    trial_start: Union[int | None, Any] = Field(default=None)
    trial_end: Union[int | None, Any] = Field(default=None)
    discount: Union[dict[str, Any] | None, Any] = Field(default=None)
    plan: Union[dict[str, Any] | None, Any] = Field(default=None)
    quantity: Union[int | None, Any] = Field(default=None)
    schedule: Union[str | None, Any] = Field(default=None)
    test_clock: Union[str | None, Any] = Field(default=None)
    transfer_data: Union[dict[str, Any] | None, Any] = Field(default=None)
    trial_settings: Union[SubscriptionTrialSettings | None, Any] = Field(default=None)
    pending_invoice_item_interval: Union[dict[str, Any] | None, Any] = Field(default=None)
    pending_setup_intent: Union[str | None, Any] = Field(default=None)
    pending_update: Union[dict[str, Any] | None, Any] = Field(default=None)

class CustomerSubscriptions(BaseModel):
    """The customer's current subscriptions, if any"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    data: Union[list[Subscription], Any] = Field(default=None, description="Details about each subscription")
    """Details about each subscription"""
    has_more: Union[bool, Any] = Field(default=None, description="True if this list has another page of items after this one")
    """True if this list has another page of items after this one"""
    url: Union[str, Any] = Field(default=None, description="The URL where this list can be accessed")
    """The URL where this list can be accessed"""

class Customer(BaseModel):
    """Customer type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    address: Union[CustomerAddress | None, Any] = Field(default=None)
    balance: Union[int, Any] = Field(default=None)
    business_name: Union[str | None, Any] = Field(default=None)
    cash_balance: Union[CustomerCashBalance | None, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    customer_account: Union[str | None, Any] = Field(default=None)
    default_currency: Union[str | None, Any] = Field(default=None)
    default_source: Union[str | None, Any] = Field(default=None)
    delinquent: Union[bool | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    discount: Union[CustomerDiscount | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    individual_name: Union[str | None, Any] = Field(default=None)
    invoice_credit_balance: Union[dict[str, Any], Any] = Field(default=None)
    invoice_prefix: Union[str | None, Any] = Field(default=None)
    invoice_settings: Union[CustomerInvoiceSettings, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    next_invoice_sequence: Union[int | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    preferred_locales: Union[list[str] | None, Any] = Field(default=None)
    shipping: Union[CustomerShipping | None, Any] = Field(default=None)
    sources: Union[CustomerSources | None, Any] = Field(default=None)
    subscriptions: Union[CustomerSubscriptions | None, Any] = Field(default=None)
    tax_exempt: Union[str | None, Any] = Field(default=None)
    test_clock: Union[str | None, Any] = Field(default=None)

class CustomerList(BaseModel):
    """CustomerList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Customer], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class CustomerCreateParamsAddress(BaseModel):
    """The customer's address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line1: Union[str, Any] = Field(default=None, description="Address line 1")
    """Address line 1"""
    line2: Union[str, Any] = Field(default=None, description="Address line 2")
    """Address line 2"""
    city: Union[str, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    state: Union[str, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""
    postal_code: Union[str, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    country: Union[str, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""

class CustomerCreateParams(BaseModel):
    """CustomerCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    phone: Union[str, Any] = Field(default=None)
    address: Union[CustomerCreateParamsAddress, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)

class CustomerUpdateParamsAddress(BaseModel):
    """The customer's address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line1: Union[str, Any] = Field(default=None, description="Address line 1")
    """Address line 1"""
    line2: Union[str, Any] = Field(default=None, description="Address line 2")
    """Address line 2"""
    city: Union[str, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    state: Union[str, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""
    postal_code: Union[str, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    country: Union[str, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""

class CustomerUpdateParams(BaseModel):
    """CustomerUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    phone: Union[str, Any] = Field(default=None)
    address: Union[CustomerUpdateParamsAddress, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)

class CustomerDeletedResponse(BaseModel):
    """CustomerDeletedResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)

class InvoiceDefaultTaxRatesItemFlatAmount(BaseModel):
    """The amount of the tax rate when the rate_type is flat_amount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Amount of the tax when the rate_type is flat_amount")
    """Amount of the tax when the rate_type is flat_amount"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code")
    """Three-letter ISO currency code"""

class InvoiceDefaultTaxRatesItem(BaseModel):
    """Nested schema for Invoice.default_tax_rates_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique identifier for the object")
    """Unique identifier for the object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    active: Union[bool, Any] = Field(default=None, description="Defaults to true")
    """Defaults to true"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    created: Union[int, Any] = Field(default=None, description="Time at which the object was created")
    """Time at which the object was created"""
    description: Union[str | None, Any] = Field(default=None, description="An arbitrary string attached to the tax rate for your internal use only")
    """An arbitrary string attached to the tax rate for your internal use only"""
    display_name: Union[str, Any] = Field(default=None, description="The display name of the tax rate")
    """The display name of the tax rate"""
    effective_percentage: Union[float | None, Any] = Field(default=None, description="Actual/effective tax rate percentage out of 100")
    """Actual/effective tax rate percentage out of 100"""
    inclusive: Union[bool, Any] = Field(default=None, description="This specifies if the tax rate is inclusive or exclusive")
    """This specifies if the tax rate is inclusive or exclusive"""
    jurisdiction: Union[str | None, Any] = Field(default=None, description="The jurisdiction for the tax rate")
    """The jurisdiction for the tax rate"""
    livemode: Union[bool, Any] = Field(default=None, description="Has the value true if the object exists in live mode")
    """Has the value true if the object exists in live mode"""
    metadata: Union[dict[str, str] | None, Any] = Field(default=None, description="Set of key-value pairs")
    """Set of key-value pairs"""
    percentage: Union[float, Any] = Field(default=None, description="Tax rate percentage out of 100")
    """Tax rate percentage out of 100"""
    flat_amount: Union[InvoiceDefaultTaxRatesItemFlatAmount | None, Any] = Field(default=None, description="The amount of the tax rate when the rate_type is flat_amount")
    """The amount of the tax rate when the rate_type is flat_amount"""
    jurisdiction_level: Union[str | None, Any] = Field(default=None, description="The level of the jurisdiction that imposes this tax rate")
    """The level of the jurisdiction that imposes this tax rate"""
    rate_type: Union[str | None, Any] = Field(default=None, description="Indicates the type of tax rate applied to the taxable amount")
    """Indicates the type of tax rate applied to the taxable amount"""
    state: Union[str | None, Any] = Field(default=None, description="ISO 3166-2 subdivision code")
    """ISO 3166-2 subdivision code"""
    tax_type: Union[str | None, Any] = Field(default=None, description="The high-level tax type")
    """The high-level tax type"""

class InvoiceCustomFieldsItem(BaseModel):
    """Nested schema for Invoice.custom_fields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="The name of the custom field")
    """The name of the custom field"""
    value: Union[str, Any] = Field(default=None, description="The value of the custom field")
    """The value of the custom field"""

class InvoiceLastFinalizationError(BaseModel):
    """The error encountered during the last finalization attempt"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    advice_code: Union[str | None, Any] = Field(default=None, description="For card errors resulting from a card issuer decline")
    """For card errors resulting from a card issuer decline"""
    code: Union[str | None, Any] = Field(default=None, description="For some errors that could be handled programmatically, a short string indicating the error code")
    """For some errors that could be handled programmatically, a short string indicating the error code"""
    doc_url: Union[str | None, Any] = Field(default=None, description="A URL to more information about the error code reported")
    """A URL to more information about the error code reported"""
    message: Union[str | None, Any] = Field(default=None, description="A human-readable message providing more details about the error")
    """A human-readable message providing more details about the error"""
    network_advice_code: Union[str | None, Any] = Field(default=None, description="For card errors resulting from a card issuer decline")
    """For card errors resulting from a card issuer decline"""
    network_decline_code: Union[str | None, Any] = Field(default=None, description="For payments declined by the network")
    """For payments declined by the network"""
    param: Union[str | None, Any] = Field(default=None, description="If the error is parameter-specific, the parameter related to the error")
    """If the error is parameter-specific, the parameter related to the error"""
    payment_method_type: Union[str | None, Any] = Field(default=None, description="If the error is specific to the type of payment method")
    """If the error is specific to the type of payment method"""
    type: Union[str, Any] = Field(default=None, description="The type of error returned")
    """The type of error returned"""

class InvoiceConfirmationSecret(BaseModel):
    """The confirmation secret associated with this invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    client_secret: Union[str, Any] = Field(default=None, description="The client_secret of the payment that Stripe creates for the invoice after finalization")
    """The client_secret of the payment that Stripe creates for the invoice after finalization"""
    type: Union[str, Any] = Field(default=None, description="The type of client_secret")
    """The type of client_secret"""

class InvoiceFromInvoice(BaseModel):
    """Details of the invoice that was cloned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: Union[str, Any] = Field(default=None)
    invoice: Union[str, Any] = Field(default=None)

class InvoiceThresholdReasonItemReasonsItem(BaseModel):
    """Nested schema for InvoiceThresholdReason.item_reasons_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line_item_ids: Union[list[str], Any] = Field(default=None, description="The IDs of the line items that triggered the threshold invoice")
    """The IDs of the line items that triggered the threshold invoice"""
    usage_gte: Union[int, Any] = Field(default=None, description="The quantity threshold boundary that applied to the given line item")
    """The quantity threshold boundary that applied to the given line item"""

class InvoiceThresholdReason(BaseModel):
    """If billing_reason is set to subscription_threshold this returns more information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_gte: Union[int | None, Any] = Field(default=None, description="The total invoice amount threshold boundary if it triggered the threshold invoice")
    """The total invoice amount threshold boundary if it triggered the threshold invoice"""
    item_reasons: Union[list[InvoiceThresholdReasonItemReasonsItem], Any] = Field(default=None, description="Indicates which line items triggered a threshold invoice")
    """Indicates which line items triggered a threshold invoice"""

class InvoiceParentQuoteDetails(BaseModel):
    """Details about the quote that generated this invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    quote: Union[str, Any] = Field(default=None, description="The quote that generated this invoice")
    """The quote that generated this invoice"""

class InvoiceParentSubscriptionDetails(BaseModel):
    """Details about the subscription that generated this invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metadata: Union[dict[str, str] | None, Any] = Field(default=None, description="Set of key-value pairs defined as subscription metadata")
    """Set of key-value pairs defined as subscription metadata"""
    subscription: Union[str, Any] = Field(default=None, description="The subscription that generated this invoice")
    """The subscription that generated this invoice"""
    subscription_proration_date: Union[int | None, Any] = Field(default=None, description="Only set for upcoming invoices that preview prorations")
    """Only set for upcoming invoices that preview prorations"""

class InvoiceParent(BaseModel):
    """The parent that generated this invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    quote_details: Union[InvoiceParentQuoteDetails | None, Any] = Field(default=None, description="Details about the quote that generated this invoice")
    """Details about the quote that generated this invoice"""
    subscription_details: Union[InvoiceParentSubscriptionDetails | None, Any] = Field(default=None, description="Details about the subscription that generated this invoice")
    """Details about the subscription that generated this invoice"""
    type: Union[str, Any] = Field(default=None, description="The type of parent that generated this invoice")
    """The type of parent that generated this invoice"""

class InvoiceShippingDetailsAddress(BaseModel):
    """Shipping address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str | None, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    line1: Union[str | None, Any] = Field(default=None, description="Address line 1")
    """Address line 1"""
    line2: Union[str | None, Any] = Field(default=None, description="Address line 2")
    """Address line 2"""
    postal_code: Union[str | None, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    state: Union[str | None, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""

class InvoiceShippingDetails(BaseModel):
    """Shipping details for the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address: Union[InvoiceShippingDetailsAddress, Any] = Field(default=None, description="Shipping address")
    """Shipping address"""
    name: Union[str, Any] = Field(default=None, description="Recipient name")
    """Recipient name"""
    phone: Union[str | None, Any] = Field(default=None, description="Recipient phone")
    """Recipient phone"""

class InvoiceCustomerAddress(BaseModel):
    """The customer's address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str | None, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    line1: Union[str | None, Any] = Field(default=None, description="Address line 1")
    """Address line 1"""
    line2: Union[str | None, Any] = Field(default=None, description="Address line 2")
    """Address line 2"""
    postal_code: Union[str | None, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    state: Union[str | None, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""

class InvoiceAutomaticTaxLiability(BaseModel):
    """The account that's liable for tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: Union[str | None, Any] = Field(default=None, description="The connected account being referenced when type is account")
    """The connected account being referenced when type is account"""
    type: Union[str, Any] = Field(default=None, description="Type of the account referenced")
    """Type of the account referenced"""

class InvoiceAutomaticTax(BaseModel):
    """Settings and latest results for automatic tax lookup for this invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    disabled_reason: Union[str | None, Any] = Field(default=None, description="If Stripe disabled automatic tax, this enum describes why")
    """If Stripe disabled automatic tax, this enum describes why"""
    enabled: Union[bool, Any] = Field(default=None, description="Whether Stripe automatically computes tax on this invoice")
    """Whether Stripe automatically computes tax on this invoice"""
    liability: Union[InvoiceAutomaticTaxLiability | None, Any] = Field(default=None, description="The account that's liable for tax")
    """The account that's liable for tax"""
    provider: Union[str | None, Any] = Field(default=None, description="The tax provider powering automatic tax")
    """The tax provider powering automatic tax"""
    status: Union[str | None, Any] = Field(default=None, description="The status of the most recent automated tax calculation for this invoice")
    """The status of the most recent automated tax calculation for this invoice"""

class InvoiceStatusTransitions(BaseModel):
    """Status transition timestamps"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    finalized_at: Union[int | None, Any] = Field(default=None, description="The time that the invoice draft was finalized")
    """The time that the invoice draft was finalized"""
    marked_uncollectible_at: Union[int | None, Any] = Field(default=None, description="The time that the invoice was marked uncollectible")
    """The time that the invoice was marked uncollectible"""
    paid_at: Union[int | None, Any] = Field(default=None, description="The time that the invoice was paid")
    """The time that the invoice was paid"""
    voided_at: Union[int | None, Any] = Field(default=None, description="The time that the invoice was voided")
    """The time that the invoice was voided"""

class InvoiceTotalTaxAmountsItem(BaseModel):
    """Nested schema for Invoice.total_tax_amounts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="The amount of the tax")
    """The amount of the tax"""
    inclusive: Union[bool, Any] = Field(default=None, description="Whether the tax amount is included in the line item amount")
    """Whether the tax amount is included in the line item amount"""
    tax_rate: Union[str, Any] = Field(default=None, description="The tax rate applied")
    """The tax rate applied"""
    taxability_reason: Union[str | None, Any] = Field(default=None, description="The reasoning behind the tax")
    """The reasoning behind the tax"""
    taxable_amount: Union[int, Any] = Field(default=None, description="The amount on which tax is calculated")
    """The amount on which tax is calculated"""

class InvoiceTotalTaxesItem(BaseModel):
    """Nested schema for Invoice.total_taxes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="The amount of the tax")
    """The amount of the tax"""
    tax_behavior: Union[str, Any] = Field(default=None, description="Whether this tax is inclusive or exclusive")
    """Whether this tax is inclusive or exclusive"""
    tax_rate_details: Union[dict[str, Any] | None, Any] = Field(default=None, description="Additional details about the tax rate")
    """Additional details about the tax rate"""
    taxability_reason: Union[str, Any] = Field(default=None, description="The reasoning behind this tax")
    """The reasoning behind this tax"""
    taxable_amount: Union[int | None, Any] = Field(default=None, description="The amount on which tax is calculated")
    """The amount on which tax is calculated"""
    type: Union[str, Any] = Field(default=None, description="The type of tax information")
    """The type of tax information"""

class InvoicePaymentsDataItem(BaseModel):
    """Nested schema for InvoicePayments.data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique identifier for the object")
    """Unique identifier for the object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    amount_paid: Union[int | None, Any] = Field(default=None, description="Amount that was actually paid for this invoice")
    """Amount that was actually paid for this invoice"""
    amount_requested: Union[int, Any] = Field(default=None, description="Amount intended to be paid toward this invoice")
    """Amount intended to be paid toward this invoice"""
    created: Union[int, Any] = Field(default=None, description="Time at which the object was created")
    """Time at which the object was created"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code")
    """Three-letter ISO currency code"""
    invoice: Union[str, Any] = Field(default=None, description="The invoice that was paid")
    """The invoice that was paid"""
    is_default: Union[bool, Any] = Field(default=None, description="Whether this is the default payment created when the invoice was finalized")
    """Whether this is the default payment created when the invoice was finalized"""
    livemode: Union[bool, Any] = Field(default=None, description="Has the value true if the object exists in live mode")
    """Has the value true if the object exists in live mode"""
    status: Union[str, Any] = Field(default=None, description="The status of the payment")
    """The status of the payment"""

class InvoicePayments(BaseModel):
    """Payments for this invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    data: Union[list[InvoicePaymentsDataItem], Any] = Field(default=None, description="Details about each payment")
    """Details about each payment"""
    has_more: Union[bool, Any] = Field(default=None, description="True if this list has another page of items")
    """True if this list has another page of items"""
    url: Union[str, Any] = Field(default=None, description="The URL where this list can be accessed")
    """The URL where this list can be accessed"""

class InvoiceLinesDataItemDiscountAmountsItem(BaseModel):
    """Nested schema for InvoiceLinesDataItem.discount_amounts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="The amount of the discount")
    """The amount of the discount"""
    discount: Union[str, Any] = Field(default=None, description="The discount that was applied")
    """The discount that was applied"""

class InvoiceLinesDataItemPeriod(BaseModel):
    """The period this line_item covers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    end: Union[int, Any] = Field(default=None, description="The end of the period")
    """The end of the period"""
    start: Union[int, Any] = Field(default=None, description="The start of the period")
    """The start of the period"""

class InvoiceLinesDataItem(BaseModel):
    """Nested schema for InvoiceLines.data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique identifier for the object")
    """Unique identifier for the object"""
    object: Union[str, Any] = Field(default=None, description="String representing the object's type")
    """String representing the object's type"""
    amount: Union[int, Any] = Field(default=None, description="The amount in cents")
    """The amount in cents"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code")
    """Three-letter ISO currency code"""
    description: Union[str | None, Any] = Field(default=None, description="An arbitrary string attached to the object")
    """An arbitrary string attached to the object"""
    discount_amounts: Union[list[InvoiceLinesDataItemDiscountAmountsItem] | None, Any] = Field(default=None, description="The amount of discount calculated per discount for this line item")
    """The amount of discount calculated per discount for this line item"""
    discountable: Union[bool, Any] = Field(default=None, description="If true, discounts will apply to this line item")
    """If true, discounts will apply to this line item"""
    discounts: Union[list[str], Any] = Field(default=None, description="The discounts applied to the invoice line item")
    """The discounts applied to the invoice line item"""
    invoice: Union[str | None, Any] = Field(default=None, description="The ID of the invoice that contains this line item")
    """The ID of the invoice that contains this line item"""
    livemode: Union[bool, Any] = Field(default=None, description="Has the value true if the object exists in live mode")
    """Has the value true if the object exists in live mode"""
    metadata: Union[dict[str, str], Any] = Field(default=None, description="Set of key-value pairs")
    """Set of key-value pairs"""
    period: Union[InvoiceLinesDataItemPeriod, Any] = Field(default=None, description="The period this line_item covers")
    """The period this line_item covers"""
    proration: Union[bool, Any] = Field(default=None, description="Whether this is a proration")
    """Whether this is a proration"""
    quantity: Union[int | None, Any] = Field(default=None, description="The quantity of the subscription")
    """The quantity of the subscription"""

class InvoiceLines(BaseModel):
    """The individual line items that make up the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[InvoiceLinesDataItem], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    total_count: Union[int | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class InvoiceTotalPretaxCreditAmountsItem(BaseModel):
    """Nested schema for Invoice.total_pretax_credit_amounts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="The amount of the pretax credit amount")
    """The amount of the pretax credit amount"""
    credit_balance_transaction: Union[str | None, Any] = Field(default=None, description="The credit balance transaction that was applied")
    """The credit balance transaction that was applied"""
    discount: Union[str | None, Any] = Field(default=None, description="The discount that was applied")
    """The discount that was applied"""
    type: Union[str, Any] = Field(default=None, description="Type of the pretax credit amount referenced")
    """Type of the pretax credit amount referenced"""

class InvoiceIssuer(BaseModel):
    """The connected account that issues the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account: Union[str | None, Any] = Field(default=None, description="The connected account being referenced when type is account")
    """The connected account being referenced when type is account"""
    type: Union[str, Any] = Field(default=None, description="Type of the account referenced")
    """Type of the account referenced"""

class InvoiceSubscriptionDetails(BaseModel):
    """Details about the subscription that this invoice was prepared for, if any"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metadata: Union[dict[str, str] | None, Any] = Field(default=None, description="Set of key-value pairs defined as subscription metadata when the invoice is created")
    """Set of key-value pairs defined as subscription metadata when the invoice is created"""

class InvoiceDiscountCoupon(BaseModel):
    """Nested schema for InvoiceDiscount.coupon"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    amount_off: Union[int | None, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    duration: Union[str, Any] = Field(default=None)
    duration_in_months: Union[int | None, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    max_redemptions: Union[int | None, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    percent_off: Union[float | None, Any] = Field(default=None)
    redeem_by: Union[int | None, Any] = Field(default=None)
    times_redeemed: Union[int, Any] = Field(default=None)
    valid: Union[bool, Any] = Field(default=None)

class InvoiceDiscount(BaseModel):
    """The discount applied to the invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    checkout_session: Union[str | None, Any] = Field(default=None)
    coupon: Union[InvoiceDiscountCoupon | None, Any] = Field(default=None)
    customer: Union[str, Any] = Field(default=None)
    customer_account: Union[str | None, Any] = Field(default=None)
    end: Union[int | None, Any] = Field(default=None)
    invoice: Union[str | None, Any] = Field(default=None)
    invoice_item: Union[str | None, Any] = Field(default=None)
    promotion_code: Union[str | None, Any] = Field(default=None)
    start: Union[int, Any] = Field(default=None)
    subscription: Union[str | None, Any] = Field(default=None)
    subscription_item: Union[str | None, Any] = Field(default=None)

class InvoiceCustomerTaxIdsItem(BaseModel):
    """Nested schema for Invoice.customer_tax_ids_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="The type of the tax ID")
    """The type of the tax ID"""
    value: Union[str | None, Any] = Field(default=None, description="The value of the tax ID")
    """The value of the tax ID"""

class InvoiceTotalDiscountAmountsItem(BaseModel):
    """Nested schema for Invoice.total_discount_amounts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="The amount of the discount")
    """The amount of the discount"""
    discount: Union[str, Any] = Field(default=None, description="The discount that was applied")
    """The discount that was applied"""

class InvoicePaymentSettings(BaseModel):
    """Configuration settings for the PaymentIntent that is generated when the invoice is finalized"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    default_mandate: Union[str | None, Any] = Field(default=None, description="ID of the mandate to be used for this invoice")
    """ID of the mandate to be used for this invoice"""
    payment_method_options: Union[dict[str, Any] | None, Any] = Field(default=None, description="Payment-method-specific configuration to provide to the invoice's PaymentIntent")
    """Payment-method-specific configuration to provide to the invoice's PaymentIntent"""
    payment_method_types: Union[list[str] | None, Any] = Field(default=None, description="The list of payment method types to provide to the invoice's PaymentIntent")
    """The list of payment method types to provide to the invoice's PaymentIntent"""

class InvoiceCustomerShippingAddress(BaseModel):
    """Customer shipping address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str | None, Any] = Field(default=None, description="City, district, suburb, town, or village")
    """City, district, suburb, town, or village"""
    country: Union[str | None, Any] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    """Two-letter country code (ISO 3166-1 alpha-2)"""
    line1: Union[str | None, Any] = Field(default=None, description="Address line 1")
    """Address line 1"""
    line2: Union[str | None, Any] = Field(default=None, description="Address line 2")
    """Address line 2"""
    postal_code: Union[str | None, Any] = Field(default=None, description="ZIP or postal code")
    """ZIP or postal code"""
    state: Union[str | None, Any] = Field(default=None, description="State, county, province, or region")
    """State, county, province, or region"""

class InvoiceCustomerShipping(BaseModel):
    """The customer's shipping information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address: Union[InvoiceCustomerShippingAddress, Any] = Field(default=None, description="Customer shipping address")
    """Customer shipping address"""
    name: Union[str, Any] = Field(default=None, description="Customer name")
    """Customer name"""
    phone: Union[str | None, Any] = Field(default=None, description="Customer phone (including extension)")
    """Customer phone (including extension)"""

class InvoiceRenderingPdf(BaseModel):
    """Invoice pdf rendering options"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_size: Union[str | None, Any] = Field(default=None, description="Page size of invoice pdf")
    """Page size of invoice pdf"""

class InvoiceRendering(BaseModel):
    """The rendering-related settings that control how the invoice is displayed"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_tax_display: Union[str | None, Any] = Field(default=None, description="How line-item prices and amounts will be displayed with respect to tax")
    """How line-item prices and amounts will be displayed with respect to tax"""
    pdf: Union[InvoiceRenderingPdf | None, Any] = Field(default=None, description="Invoice pdf rendering options")
    """Invoice pdf rendering options"""
    template: Union[str | None, Any] = Field(default=None, description="ID of the rendering template that the invoice is formatted by")
    """ID of the rendering template that the invoice is formatted by"""
    template_version: Union[int | None, Any] = Field(default=None, description="Version of the rendering template that the invoice is using")
    """Version of the rendering template that the invoice is using"""

class InvoiceShippingCostTaxesItem(BaseModel):
    """Nested schema for InvoiceShippingCost.taxes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Amount of tax applied for this rate")
    """Amount of tax applied for this rate"""
    taxability_reason: Union[str | None, Any] = Field(default=None, description="The reasoning behind this tax")
    """The reasoning behind this tax"""
    taxable_amount: Union[int | None, Any] = Field(default=None, description="The amount on which tax is calculated")
    """The amount on which tax is calculated"""

class InvoiceShippingCost(BaseModel):
    """The details of the cost of shipping"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_subtotal: Union[int, Any] = Field(default=None, description="Total shipping cost before any taxes are applied")
    """Total shipping cost before any taxes are applied"""
    amount_tax: Union[int, Any] = Field(default=None, description="Total tax amount applied due to shipping costs")
    """Total tax amount applied due to shipping costs"""
    amount_total: Union[int, Any] = Field(default=None, description="Total shipping cost after taxes are applied")
    """Total shipping cost after taxes are applied"""
    shipping_rate: Union[str | None, Any] = Field(default=None, description="The ID of the ShippingRate for this invoice")
    """The ID of the ShippingRate for this invoice"""
    taxes: Union[list[InvoiceShippingCostTaxesItem] | None, Any] = Field(default=None, description="The taxes applied to the shipping rate")
    """The taxes applied to the shipping rate"""

class Invoice(BaseModel):
    """Invoice type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    account_country: Union[str | None, Any] = Field(default=None)
    account_name: Union[str | None, Any] = Field(default=None)
    account_tax_ids: Union[list[str] | None, Any] = Field(default=None)
    amount_due: Union[int, Any] = Field(default=None)
    amount_overpaid: Union[int, Any] = Field(default=None)
    amount_paid: Union[int, Any] = Field(default=None)
    amount_remaining: Union[int, Any] = Field(default=None)
    amount_shipping: Union[int, Any] = Field(default=None)
    application: Union[str | None, Any] = Field(default=None)
    application_fee_amount: Union[int | None, Any] = Field(default=None)
    attempt_count: Union[int, Any] = Field(default=None)
    attempted: Union[bool, Any] = Field(default=None)
    auto_advance: Union[bool, Any] = Field(default=None)
    automatic_tax: Union[InvoiceAutomaticTax, Any] = Field(default=None)
    automatically_finalizes_at: Union[int | None, Any] = Field(default=None)
    billing_reason: Union[str | None, Any] = Field(default=None)
    charge: Union[str | None, Any] = Field(default=None)
    collection_method: Union[str, Any] = Field(default=None)
    confirmation_secret: Union[InvoiceConfirmationSecret | None, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    custom_fields: Union[list[InvoiceCustomFieldsItem] | None, Any] = Field(default=None)
    customer: Union[str, Any] = Field(default=None)
    customer_account: Union[str | None, Any] = Field(default=None)
    customer_address: Union[InvoiceCustomerAddress | None, Any] = Field(default=None)
    customer_email: Union[str | None, Any] = Field(default=None)
    customer_name: Union[str | None, Any] = Field(default=None)
    customer_phone: Union[str | None, Any] = Field(default=None)
    customer_shipping: Union[InvoiceCustomerShipping | None, Any] = Field(default=None)
    customer_tax_exempt: Union[str | None, Any] = Field(default=None)
    customer_tax_ids: Union[list[InvoiceCustomerTaxIdsItem] | None, Any] = Field(default=None)
    default_payment_method: Union[str | None, Any] = Field(default=None)
    default_source: Union[str | None, Any] = Field(default=None)
    default_tax_rates: Union[list[InvoiceDefaultTaxRatesItem], Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    discount: Union[InvoiceDiscount | None, Any] = Field(default=None)
    discounts: Union[list[str], Any] = Field(default=None)
    due_date: Union[int | None, Any] = Field(default=None)
    effective_at: Union[int | None, Any] = Field(default=None)
    ending_balance: Union[int | None, Any] = Field(default=None)
    footer: Union[str | None, Any] = Field(default=None)
    from_invoice: Union[InvoiceFromInvoice | None, Any] = Field(default=None)
    hosted_invoice_url: Union[str | None, Any] = Field(default=None)
    invoice_pdf: Union[str | None, Any] = Field(default=None)
    issuer: Union[InvoiceIssuer, Any] = Field(default=None)
    last_finalization_error: Union[InvoiceLastFinalizationError | None, Any] = Field(default=None)
    latest_revision: Union[str | None, Any] = Field(default=None)
    lines: Union[InvoiceLines, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    next_payment_attempt: Union[int | None, Any] = Field(default=None)
    number: Union[str | None, Any] = Field(default=None)
    on_behalf_of: Union[str | None, Any] = Field(default=None)
    paid: Union[bool | None, Any] = Field(default=None)
    paid_out_of_band: Union[bool | None, Any] = Field(default=None)
    parent: Union[InvoiceParent | None, Any] = Field(default=None)
    payment_intent: Union[str | None, Any] = Field(default=None)
    payment_settings: Union[InvoicePaymentSettings, Any] = Field(default=None)
    payments: Union[InvoicePayments, Any] = Field(default=None)
    period_end: Union[int, Any] = Field(default=None)
    period_start: Union[int, Any] = Field(default=None)
    post_payment_credit_notes_amount: Union[int, Any] = Field(default=None)
    pre_payment_credit_notes_amount: Union[int, Any] = Field(default=None)
    quote: Union[str | None, Any] = Field(default=None)
    receipt_number: Union[str | None, Any] = Field(default=None)
    rendering: Union[InvoiceRendering | None, Any] = Field(default=None)
    rendering_options: Union[dict[str, Any] | None, Any] = Field(default=None)
    shipping_cost: Union[InvoiceShippingCost | None, Any] = Field(default=None)
    shipping_details: Union[InvoiceShippingDetails | None, Any] = Field(default=None)
    starting_balance: Union[int, Any] = Field(default=None)
    statement_descriptor: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    status_transitions: Union[InvoiceStatusTransitions, Any] = Field(default=None)
    subscription: Union[str | None, Any] = Field(default=None)
    subscription_details: Union[InvoiceSubscriptionDetails | None, Any] = Field(default=None)
    subtotal: Union[int, Any] = Field(default=None)
    subtotal_excluding_tax: Union[int | None, Any] = Field(default=None)
    tax: Union[int | None, Any] = Field(default=None)
    test_clock: Union[str | None, Any] = Field(default=None)
    threshold_reason: Union[InvoiceThresholdReason | None, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)
    total_discount_amounts: Union[list[InvoiceTotalDiscountAmountsItem] | None, Any] = Field(default=None)
    total_excluding_tax: Union[int | None, Any] = Field(default=None)
    total_pretax_credit_amounts: Union[list[InvoiceTotalPretaxCreditAmountsItem] | None, Any] = Field(default=None)
    total_tax_amounts: Union[list[InvoiceTotalTaxAmountsItem] | None, Any] = Field(default=None)
    total_taxes: Union[list[InvoiceTotalTaxesItem] | None, Any] = Field(default=None)
    transfer_data: Union[dict[str, Any] | None, Any] = Field(default=None)
    webhooks_delivered_at: Union[int | None, Any] = Field(default=None)

class InvoiceList(BaseModel):
    """InvoiceList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Invoice], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ChargeBillingDetailsAddress(BaseModel):
    """Nested schema for ChargeBillingDetails.address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    line1: Union[str | None, Any] = Field(default=None)
    line2: Union[str | None, Any] = Field(default=None)
    postal_code: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)

class ChargeBillingDetails(BaseModel):
    """Billing information associated with the payment method"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address: Union[ChargeBillingDetailsAddress | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    tax_id: Union[str | None, Any] = Field(default=None)

class ChargeRefunds(BaseModel):
    """A list of refunds that have been applied to the charge"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[dict[str, Any]], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None, description="Total number of refunds")
    """Total number of refunds"""
    url: Union[str, Any] = Field(default=None, description="URL to access the refunds list")
    """URL to access the refunds list"""

class ChargePaymentMethodDetailsCardIncrementalAuthorization(BaseModel):
    """Incremental authorization details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None)

class ChargePaymentMethodDetailsCardNetworkToken(BaseModel):
    """Network token details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    used: Union[bool, Any] = Field(default=None)

class ChargePaymentMethodDetailsCardChecks(BaseModel):
    """Check results by Card networks on Card address and CVC"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address_line1_check: Union[str | None, Any] = Field(default=None)
    address_postal_code_check: Union[str | None, Any] = Field(default=None)
    cvc_check: Union[str | None, Any] = Field(default=None)

class ChargePaymentMethodDetailsCardExtendedAuthorization(BaseModel):
    """Extended authorization details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None)

class ChargePaymentMethodDetailsCardMulticapture(BaseModel):
    """Multicapture details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None)

class ChargePaymentMethodDetailsCardOvercapture(BaseModel):
    """Overcapture details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    maximum_amount_capturable: Union[int, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)

class ChargePaymentMethodDetailsCard(BaseModel):
    """Nested schema for ChargePaymentMethodDetails.card"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_authorized: Union[int | None, Any] = Field(default=None, description="Amount authorized on the card")
    """Amount authorized on the card"""
    authorization_code: Union[str | None, Any] = Field(default=None, description="Authorization code on the charge")
    """Authorization code on the charge"""
    brand: Union[str, Any] = Field(default=None, description="Card brand")
    """Card brand"""
    checks: Union[ChargePaymentMethodDetailsCardChecks | None, Any] = Field(default=None, description="Check results by Card networks on Card address and CVC")
    """Check results by Card networks on Card address and CVC"""
    country: Union[str, Any] = Field(default=None, description="Two-letter ISO code representing the country of the card")
    """Two-letter ISO code representing the country of the card"""
    exp_month: Union[int, Any] = Field(default=None, description="Two-digit number representing the card's expiration month")
    """Two-digit number representing the card's expiration month"""
    exp_year: Union[int, Any] = Field(default=None, description="Four-digit number representing the card's expiration year")
    """Four-digit number representing the card's expiration year"""
    extended_authorization: Union[ChargePaymentMethodDetailsCardExtendedAuthorization | None, Any] = Field(default=None, description="Extended authorization details")
    """Extended authorization details"""
    fingerprint: Union[str, Any] = Field(default=None, description="Uniquely identifies this particular card number")
    """Uniquely identifies this particular card number"""
    funding: Union[str, Any] = Field(default=None, description="Card funding type")
    """Card funding type"""
    incremental_authorization: Union[ChargePaymentMethodDetailsCardIncrementalAuthorization | None, Any] = Field(default=None, description="Incremental authorization details")
    """Incremental authorization details"""
    installments: Union[dict[str, Any] | None, Any] = Field(default=None, description="Installment details")
    """Installment details"""
    last4: Union[str, Any] = Field(default=None, description="The last four digits of the card")
    """The last four digits of the card"""
    mandate: Union[str | None, Any] = Field(default=None, description="ID of the mandate used to make this payment")
    """ID of the mandate used to make this payment"""
    multicapture: Union[ChargePaymentMethodDetailsCardMulticapture | None, Any] = Field(default=None, description="Multicapture details")
    """Multicapture details"""
    network: Union[str, Any] = Field(default=None, description="Card network")
    """Card network"""
    network_token: Union[ChargePaymentMethodDetailsCardNetworkToken | None, Any] = Field(default=None, description="Network token details")
    """Network token details"""
    network_transaction_id: Union[str | None, Any] = Field(default=None, description="Network transaction identifier")
    """Network transaction identifier"""
    overcapture: Union[ChargePaymentMethodDetailsCardOvercapture | None, Any] = Field(default=None, description="Overcapture details")
    """Overcapture details"""
    regulated_status: Union[str | None, Any] = Field(default=None, description="Regulated status of the card")
    """Regulated status of the card"""
    three_d_secure: Union[dict[str, Any] | None, Any] = Field(default=None, description="3D Secure details")
    """3D Secure details"""
    wallet: Union[dict[str, Any] | None, Any] = Field(default=None, description="Digital wallet details if used")
    """Digital wallet details if used"""

class ChargePaymentMethodDetails(BaseModel):
    """Details about the payment method at the time of the transaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    card: Union[ChargePaymentMethodDetailsCard | None, Any] = Field(default=None)

class ChargePresentmentDetails(BaseModel):
    """Currency presentation information for multi-currency charges"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount_authorized: Union[int | None, Any] = Field(default=None, description="Amount authorized in the presentment currency")
    """Amount authorized in the presentment currency"""
    amount_charged: Union[int | None, Any] = Field(default=None, description="Amount charged in the presentment currency")
    """Amount charged in the presentment currency"""
    currency: Union[str | None, Any] = Field(default=None, description="Three-letter ISO currency code for presentment")
    """Three-letter ISO currency code for presentment"""

class ChargeFraudDetails(BaseModel):
    """Information on fraud assessments for the charge"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    stripe_report: Union[str | None, Any] = Field(default=None, description="Assessments from Stripe. If set, the value is `fraudulent`.")
    """Assessments from Stripe. If set, the value is `fraudulent`."""
    user_report: Union[str | None, Any] = Field(default=None, description="Assessments from you or your users. Possible values are `fraudulent` and `safe`")
    """Assessments from you or your users. Possible values are `fraudulent` and `safe`"""

class ChargeOutcome(BaseModel):
    """Details about whether the payment was accepted, and why"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    advice_code: Union[str | None, Any] = Field(default=None)
    network_advice_code: Union[str | None, Any] = Field(default=None)
    network_decline_code: Union[str | None, Any] = Field(default=None)
    network_status: Union[str, Any] = Field(default=None)
    reason: Union[str | None, Any] = Field(default=None)
    risk_level: Union[str, Any] = Field(default=None)
    risk_score: Union[int, Any] = Field(default=None)
    seller_message: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)

class Charge(BaseModel):
    """Charge type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    amount_captured: Union[int, Any] = Field(default=None)
    amount_refunded: Union[int, Any] = Field(default=None)
    amount_updates: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    application: Union[str | None, Any] = Field(default=None)
    application_fee: Union[str | None, Any] = Field(default=None)
    application_fee_amount: Union[int | None, Any] = Field(default=None)
    calculated_statement_descriptor: Union[str | None, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    customer: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    destination: Union[str | None, Any] = Field(default=None)
    dispute: Union[str | None, Any] = Field(default=None)
    disputed: Union[bool, Any] = Field(default=None)
    failure_balance_transaction: Union[str | None, Any] = Field(default=None)
    failure_code: Union[str | None, Any] = Field(default=None)
    failure_message: Union[str | None, Any] = Field(default=None)
    fraud_details: Union[ChargeFraudDetails | None, Any] = Field(default=None)
    invoice: Union[str | None, Any] = Field(default=None)
    on_behalf_of: Union[str | None, Any] = Field(default=None)
    order: Union[str | None, Any] = Field(default=None)
    outcome: Union[ChargeOutcome | None, Any] = Field(default=None)
    paid: Union[bool, Any] = Field(default=None)
    payment_intent: Union[str | None, Any] = Field(default=None)
    payment_method: Union[str | None, Any] = Field(default=None)
    payment_method_details: Union[ChargePaymentMethodDetails | None, Any] = Field(default=None)
    presentment_details: Union[ChargePresentmentDetails | None, Any] = Field(default=None)
    receipt_email: Union[str | None, Any] = Field(default=None)
    receipt_number: Union[str | None, Any] = Field(default=None)
    receipt_url: Union[str | None, Any] = Field(default=None)
    refunded: Union[bool, Any] = Field(default=None)
    refunds: Union[ChargeRefunds | None, Any] = Field(default=None)
    review: Union[str | None, Any] = Field(default=None)
    shipping: Union[dict[str, Any] | None, Any] = Field(default=None)
    source: Union[dict[str, Any] | None, Any] = Field(default=None)
    source_transfer: Union[str | None, Any] = Field(default=None)
    statement_descriptor: Union[str | None, Any] = Field(default=None)
    statement_descriptor_suffix: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    transfer_data: Union[dict[str, Any] | None, Any] = Field(default=None)
    transfer_group: Union[str | None, Any] = Field(default=None)
    captured: Union[bool, Any] = Field(default=None)
    balance_transaction: Union[str | None, Any] = Field(default=None)
    billing_details: Union[ChargeBillingDetails, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    radar_options: Union[dict[str, Any] | None, Any] = Field(default=None)

class ChargeList(BaseModel):
    """ChargeList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Charge], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class SubscriptionList(BaseModel):
    """SubscriptionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Subscription], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class RefundNextActionDisplayDetailsEmailSent(BaseModel):
    """Contains information about the email sent to the customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email_sent_at: Union[int, Any] = Field(default=None, description="The timestamp when the email was sent")
    """The timestamp when the email was sent"""
    email_sent_to: Union[str, Any] = Field(default=None, description="The recipient's email address")
    """The recipient's email address"""

class RefundNextActionDisplayDetails(BaseModel):
    """Contains the refund details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email_sent: Union[RefundNextActionDisplayDetailsEmailSent, Any] = Field(default=None, description="Contains information about the email sent to the customer")
    """Contains information about the email sent to the customer"""
    expires_at: Union[int, Any] = Field(default=None, description="The expiry timestamp")
    """The expiry timestamp"""

class RefundNextAction(BaseModel):
    """If the refund has a status of requires_action, this property describes what the refund needs to continue processing"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display_details: Union[RefundNextActionDisplayDetails | None, Any] = Field(default=None, description="Contains the refund details")
    """Contains the refund details"""
    type: Union[str, Any] = Field(default=None, description="Type of the next action to perform")
    """Type of the next action to perform"""

class RefundDestinationDetailsBlik(BaseModel):
    """If this is a blik refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    network_decline_code: Union[str | None, Any] = Field(default=None, description="For refunds declined by the network, a decline code provided by the network")
    """For refunds declined by the network, a decline code provided by the network"""
    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsThBankTransfer(BaseModel):
    """If this is a th_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsGbBankTransfer(BaseModel):
    """If this is a gb_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsSwish(BaseModel):
    """If this is a swish refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    network_decline_code: Union[str | None, Any] = Field(default=None, description="For refunds declined by the network, a decline code provided by the network")
    """For refunds declined by the network, a decline code provided by the network"""
    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsMbWay(BaseModel):
    """If this is a mb_way refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsCrypto(BaseModel):
    """If this is a crypto refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The transaction hash of the refund")
    """The transaction hash of the refund"""

class RefundDestinationDetailsCard(BaseModel):
    """If this is a card refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="Value of the reference number assigned to the refund")
    """Value of the reference number assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference number on the refund")
    """Status of the reference number on the refund"""
    reference_type: Union[str | None, Any] = Field(default=None, description="Type of the reference number assigned to the refund")
    """Type of the reference number assigned to the refund"""
    type: Union[str, Any] = Field(default=None, description="The type of refund")
    """The type of refund"""

class RefundDestinationDetailsMxBankTransfer(BaseModel):
    """If this is a mx_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsP24(BaseModel):
    """If this is a p24 refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsPaypal(BaseModel):
    """If this is a paypal refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    network_decline_code: Union[str | None, Any] = Field(default=None, description="For refunds declined by the network, a decline code provided by the network")
    """For refunds declined by the network, a decline code provided by the network"""

class RefundDestinationDetailsJpBankTransfer(BaseModel):
    """If this is a jp_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsMultibanco(BaseModel):
    """If this is a multibanco refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsUsBankTransfer(BaseModel):
    """If this is a us_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsEuBankTransfer(BaseModel):
    """If this is a eu_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetailsBrBankTransfer(BaseModel):
    """If this is a br_bank_transfer refund, this hash contains the transaction specific details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reference: Union[str | None, Any] = Field(default=None, description="The reference assigned to the refund")
    """The reference assigned to the refund"""
    reference_status: Union[str | None, Any] = Field(default=None, description="Status of the reference on the refund")
    """Status of the reference on the refund"""

class RefundDestinationDetails(BaseModel):
    """Transaction-specific details for the refund"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    affirm: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a affirm refund, this hash contains the transaction specific details")
    """If this is a affirm refund, this hash contains the transaction specific details"""
    afterpay_clearpay: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a afterpay_clearpay refund, this hash contains the transaction specific details")
    """If this is a afterpay_clearpay refund, this hash contains the transaction specific details"""
    alipay: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a alipay refund, this hash contains the transaction specific details")
    """If this is a alipay refund, this hash contains the transaction specific details"""
    alma: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a alma refund, this hash contains the transaction specific details")
    """If this is a alma refund, this hash contains the transaction specific details"""
    amazon_pay: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a amazon_pay refund, this hash contains the transaction specific details")
    """If this is a amazon_pay refund, this hash contains the transaction specific details"""
    au_bank_transfer: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a au_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a au_bank_transfer refund, this hash contains the transaction specific details"""
    blik: Union[RefundDestinationDetailsBlik | None, Any] = Field(default=None, description="If this is a blik refund, this hash contains the transaction specific details")
    """If this is a blik refund, this hash contains the transaction specific details"""
    br_bank_transfer: Union[RefundDestinationDetailsBrBankTransfer | None, Any] = Field(default=None, description="If this is a br_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a br_bank_transfer refund, this hash contains the transaction specific details"""
    card: Union[RefundDestinationDetailsCard | None, Any] = Field(default=None, description="If this is a card refund, this hash contains the transaction specific details")
    """If this is a card refund, this hash contains the transaction specific details"""
    cashapp: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a cashapp refund, this hash contains the transaction specific details")
    """If this is a cashapp refund, this hash contains the transaction specific details"""
    crypto: Union[RefundDestinationDetailsCrypto | None, Any] = Field(default=None, description="If this is a crypto refund, this hash contains the transaction specific details")
    """If this is a crypto refund, this hash contains the transaction specific details"""
    customer_cash_balance: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a customer_cash_balance refund, this hash contains the transaction specific details")
    """If this is a customer_cash_balance refund, this hash contains the transaction specific details"""
    eps: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a eps refund, this hash contains the transaction specific details")
    """If this is a eps refund, this hash contains the transaction specific details"""
    eu_bank_transfer: Union[RefundDestinationDetailsEuBankTransfer | None, Any] = Field(default=None, description="If this is a eu_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a eu_bank_transfer refund, this hash contains the transaction specific details"""
    gb_bank_transfer: Union[RefundDestinationDetailsGbBankTransfer | None, Any] = Field(default=None, description="If this is a gb_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a gb_bank_transfer refund, this hash contains the transaction specific details"""
    giropay: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a giropay refund, this hash contains the transaction specific details")
    """If this is a giropay refund, this hash contains the transaction specific details"""
    grabpay: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a grabpay refund, this hash contains the transaction specific details")
    """If this is a grabpay refund, this hash contains the transaction specific details"""
    jp_bank_transfer: Union[RefundDestinationDetailsJpBankTransfer | None, Any] = Field(default=None, description="If this is a jp_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a jp_bank_transfer refund, this hash contains the transaction specific details"""
    klarna: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a klarna refund, this hash contains the transaction specific details")
    """If this is a klarna refund, this hash contains the transaction specific details"""
    mb_way: Union[RefundDestinationDetailsMbWay | None, Any] = Field(default=None, description="If this is a mb_way refund, this hash contains the transaction specific details")
    """If this is a mb_way refund, this hash contains the transaction specific details"""
    multibanco: Union[RefundDestinationDetailsMultibanco | None, Any] = Field(default=None, description="If this is a multibanco refund, this hash contains the transaction specific details")
    """If this is a multibanco refund, this hash contains the transaction specific details"""
    mx_bank_transfer: Union[RefundDestinationDetailsMxBankTransfer | None, Any] = Field(default=None, description="If this is a mx_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a mx_bank_transfer refund, this hash contains the transaction specific details"""
    nz_bank_transfer: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a nz_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a nz_bank_transfer refund, this hash contains the transaction specific details"""
    p24: Union[RefundDestinationDetailsP24 | None, Any] = Field(default=None, description="If this is a p24 refund, this hash contains the transaction specific details")
    """If this is a p24 refund, this hash contains the transaction specific details"""
    paynow: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a paynow refund, this hash contains the transaction specific details")
    """If this is a paynow refund, this hash contains the transaction specific details"""
    paypal: Union[RefundDestinationDetailsPaypal | None, Any] = Field(default=None, description="If this is a paypal refund, this hash contains the transaction specific details")
    """If this is a paypal refund, this hash contains the transaction specific details"""
    pix: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a pix refund, this hash contains the transaction specific details")
    """If this is a pix refund, this hash contains the transaction specific details"""
    revolut: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a revolut refund, this hash contains the transaction specific details")
    """If this is a revolut refund, this hash contains the transaction specific details"""
    sofort: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a sofort refund, this hash contains the transaction specific details")
    """If this is a sofort refund, this hash contains the transaction specific details"""
    swish: Union[RefundDestinationDetailsSwish | None, Any] = Field(default=None, description="If this is a swish refund, this hash contains the transaction specific details")
    """If this is a swish refund, this hash contains the transaction specific details"""
    th_bank_transfer: Union[RefundDestinationDetailsThBankTransfer | None, Any] = Field(default=None, description="If this is a th_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a th_bank_transfer refund, this hash contains the transaction specific details"""
    twint: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a twint refund, this hash contains the transaction specific details")
    """If this is a twint refund, this hash contains the transaction specific details"""
    type: Union[str, Any] = Field(default=None, description="The type of transaction-specific details of the payment method used in the refund")
    """The type of transaction-specific details of the payment method used in the refund"""
    us_bank_transfer: Union[RefundDestinationDetailsUsBankTransfer | None, Any] = Field(default=None, description="If this is a us_bank_transfer refund, this hash contains the transaction specific details")
    """If this is a us_bank_transfer refund, this hash contains the transaction specific details"""
    wechat_pay: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a wechat_pay refund, this hash contains the transaction specific details")
    """If this is a wechat_pay refund, this hash contains the transaction specific details"""
    zip: Union[dict[str, Any] | None, Any] = Field(default=None, description="If this is a zip refund, this hash contains the transaction specific details")
    """If this is a zip refund, this hash contains the transaction specific details"""

class Refund(BaseModel):
    """Refund type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    balance_transaction: Union[str | None, Any] = Field(default=None)
    charge: Union[str | None, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    destination_details: Union[RefundDestinationDetails | None, Any] = Field(default=None)
    failure_balance_transaction: Union[str | None, Any] = Field(default=None)
    failure_reason: Union[str | None, Any] = Field(default=None)
    instructions_email: Union[str | None, Any] = Field(default=None)
    metadata: Union[dict[str, str] | None, Any] = Field(default=None)
    next_action: Union[RefundNextAction | None, Any] = Field(default=None)
    payment_intent: Union[str | None, Any] = Field(default=None)
    pending_reason: Union[str | None, Any] = Field(default=None)
    reason: Union[str | None, Any] = Field(default=None)
    receipt_number: Union[str | None, Any] = Field(default=None)
    source_transfer_reversal: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    transfer_reversal: Union[str | None, Any] = Field(default=None)

class RefundList(BaseModel):
    """RefundList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)
    data: Union[list[Refund], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class RefundCreateParams(BaseModel):
    """RefundCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    charge: Union[str, Any] = Field(default=None)
    payment_intent: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    reason: Union[str, Any] = Field(default=None)
    refund_application_fee: Union[bool, Any] = Field(default=None)
    reverse_transfer: Union[bool, Any] = Field(default=None)

class ProductMarketingFeaturesItem(BaseModel):
    """Nested schema for Product.marketing_features_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None, description="The marketing feature name. Up to 80 characters long")
    """The marketing feature name. Up to 80 characters long"""

class ProductFeaturesItem(BaseModel):
    """Nested schema for Product.features_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="The feature name")
    """The feature name"""

class ProductPackageDimensions(BaseModel):
    """The dimensions of this product for shipping purposes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    height: Union[float, Any] = Field(default=None, description="Height, in inches")
    """Height, in inches"""
    length: Union[float, Any] = Field(default=None, description="Length, in inches")
    """Length, in inches"""
    weight: Union[float, Any] = Field(default=None, description="Weight, in ounces")
    """Weight, in ounces"""
    width: Union[float, Any] = Field(default=None, description="Width, in inches")
    """Width, in inches"""

class Product(BaseModel):
    """Product type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    attributes: Union[list[str], Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    default_price: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    features: Union[list[ProductFeaturesItem], Any] = Field(default=None)
    images: Union[list[str], Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    marketing_features: Union[list[ProductMarketingFeaturesItem], Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    package_dimensions: Union[ProductPackageDimensions | None, Any] = Field(default=None)
    shippable: Union[bool | None, Any] = Field(default=None)
    statement_descriptor: Union[str | None, Any] = Field(default=None)
    tax_code: Union[str | None, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    unit_label: Union[str | None, Any] = Field(default=None)
    updated: Union[int, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class ProductList(BaseModel):
    """ProductList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Product], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ProductSearchResult(BaseModel):
    """ProductSearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Product], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ProductCreateParamsMarketingFeaturesItem(BaseModel):
    """Nested schema for ProductCreateParams.marketing_features_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="The marketing feature name. Up to 80 characters long")
    """The marketing feature name. Up to 80 characters long"""

class ProductCreateParamsPackageDimensions(BaseModel):
    """The dimensions of this product for shipping purposes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    height: Union[float, Any] = Field(default=None, description="Height, in inches")
    """Height, in inches"""
    length: Union[float, Any] = Field(default=None, description="Length, in inches")
    """Length, in inches"""
    weight: Union[float, Any] = Field(default=None, description="Weight, in ounces")
    """Weight, in ounces"""
    width: Union[float, Any] = Field(default=None, description="Width, in inches")
    """Width, in inches"""

class ProductCreateParams(BaseModel):
    """ProductCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    images: Union[list[str], Any] = Field(default=None)
    marketing_features: Union[list[ProductCreateParamsMarketingFeaturesItem], Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    package_dimensions: Union[ProductCreateParamsPackageDimensions, Any] = Field(default=None)
    shippable: Union[bool, Any] = Field(default=None)
    statement_descriptor: Union[str, Any] = Field(default=None)
    tax_code: Union[str, Any] = Field(default=None)
    unit_label: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ProductUpdateParamsPackageDimensions(BaseModel):
    """The dimensions of this product for shipping purposes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    height: Union[float, Any] = Field(default=None, description="Height, in inches")
    """Height, in inches"""
    length: Union[float, Any] = Field(default=None, description="Length, in inches")
    """Length, in inches"""
    weight: Union[float, Any] = Field(default=None, description="Weight, in ounces")
    """Weight, in ounces"""
    width: Union[float, Any] = Field(default=None, description="Width, in inches")
    """Width, in inches"""

class ProductUpdateParamsMarketingFeaturesItem(BaseModel):
    """Nested schema for ProductUpdateParams.marketing_features_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="The marketing feature name. Up to 80 characters long")
    """The marketing feature name. Up to 80 characters long"""

class ProductUpdateParams(BaseModel):
    """ProductUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: Union[bool, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    default_price: Union[str, Any] = Field(default=None)
    images: Union[list[str], Any] = Field(default=None)
    marketing_features: Union[list[ProductUpdateParamsMarketingFeaturesItem], Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    package_dimensions: Union[ProductUpdateParamsPackageDimensions, Any] = Field(default=None)
    shippable: Union[bool, Any] = Field(default=None)
    statement_descriptor: Union[str, Any] = Field(default=None)
    tax_code: Union[str, Any] = Field(default=None)
    unit_label: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ProductDeletedResponse(BaseModel):
    """ProductDeletedResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)

class BalanceConnectReservedItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceConnectReservedItem(BaseModel):
    """Nested schema for Balance.connect_reserved_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount in the smallest currency unit")
    """Balance amount in the smallest currency unit"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code, in lowercase")
    """Three-letter ISO currency code, in lowercase"""
    source_types: Union[BalanceConnectReservedItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalanceAvailableItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceAvailableItem(BaseModel):
    """Nested schema for Balance.available_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount in the smallest currency unit (e.g., cents)")
    """Balance amount in the smallest currency unit (e.g., cents)"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code, in lowercase")
    """Three-letter ISO currency code, in lowercase"""
    source_types: Union[BalanceAvailableItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalancePendingItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalancePendingItem(BaseModel):
    """Nested schema for Balance.pending_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount in the smallest currency unit")
    """Balance amount in the smallest currency unit"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code, in lowercase")
    """Three-letter ISO currency code, in lowercase"""
    source_types: Union[BalancePendingItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalanceRefundAndDisputePrefundingPendingItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceRefundAndDisputePrefundingPendingItem(BaseModel):
    """Nested schema for BalanceRefundAndDisputePrefunding.pending_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount")
    """Balance amount"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code")
    """Three-letter ISO currency code"""
    source_types: Union[BalanceRefundAndDisputePrefundingPendingItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalanceRefundAndDisputePrefundingAvailableItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceRefundAndDisputePrefundingAvailableItem(BaseModel):
    """Nested schema for BalanceRefundAndDisputePrefunding.available_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount")
    """Balance amount"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code")
    """Three-letter ISO currency code"""
    source_types: Union[BalanceRefundAndDisputePrefundingAvailableItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalanceRefundAndDisputePrefunding(BaseModel):
    """Funds reserved for covering future refunds or disputes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    available: Union[list[BalanceRefundAndDisputePrefundingAvailableItem], Any] = Field(default=None, description="Available funds for refunds and disputes")
    """Available funds for refunds and disputes"""
    pending: Union[list[BalanceRefundAndDisputePrefundingPendingItem], Any] = Field(default=None, description="Pending funds for refunds and disputes")
    """Pending funds for refunds and disputes"""

class BalanceInstantAvailableItemNetAvailableItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceInstantAvailableItemNetAvailableItem(BaseModel):
    """Nested schema for BalanceInstantAvailableItem.net_available_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Net balance amount")
    """Net balance amount"""
    destination: Union[str, Any] = Field(default=None, description="ID of the external account")
    """ID of the external account"""
    source_types: Union[BalanceInstantAvailableItemNetAvailableItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalanceInstantAvailableItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceInstantAvailableItem(BaseModel):
    """Nested schema for Balance.instant_available_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount in the smallest currency unit")
    """Balance amount in the smallest currency unit"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code, in lowercase")
    """Three-letter ISO currency code, in lowercase"""
    source_types: Union[BalanceInstantAvailableItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""
    net_available: Union[list[BalanceInstantAvailableItemNetAvailableItem] | None, Any] = Field(default=None, description="Net balance amount available after deducting fees")
    """Net balance amount available after deducting fees"""

class BalanceIssuingAvailableItemSourceTypes(BaseModel):
    """Breakdown of balance by source types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bank_account: Union[int | None, Any] = Field(default=None, description="Amount for bank_account")
    """Amount for bank_account"""
    card: Union[int | None, Any] = Field(default=None, description="Amount for card")
    """Amount for card"""
    fpx: Union[int | None, Any] = Field(default=None, description="Amount for fpx")
    """Amount for fpx"""

class BalanceIssuingAvailableItem(BaseModel):
    """Nested schema for BalanceIssuing.available_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Balance amount")
    """Balance amount"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code")
    """Three-letter ISO currency code"""
    source_types: Union[BalanceIssuingAvailableItemSourceTypes | None, Any] = Field(default=None, description="Breakdown of balance by source types")
    """Breakdown of balance by source types"""

class BalanceIssuing(BaseModel):
    """Funds that are available for use with Issuing cards"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    available: Union[list[BalanceIssuingAvailableItem], Any] = Field(default=None, description="Funds available for issuing")
    """Funds available for issuing"""

class Balance(BaseModel):
    """Balance type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    available: Union[list[BalanceAvailableItem], Any] = Field(default=None)
    connect_reserved: Union[list[BalanceConnectReservedItem] | None, Any] = Field(default=None)
    instant_available: Union[list[BalanceInstantAvailableItem] | None, Any] = Field(default=None)
    issuing: Union[BalanceIssuing | None, Any] = Field(default=None)
    pending: Union[list[BalancePendingItem], Any] = Field(default=None)
    refund_and_dispute_prefunding: Union[BalanceRefundAndDisputePrefunding | None, Any] = Field(default=None)

class BalanceTransactionFeeDetailsItem(BaseModel):
    """Nested schema for BalanceTransaction.fee_details_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[int, Any] = Field(default=None, description="Amount of the fee, in cents")
    """Amount of the fee, in cents"""
    application: Union[str | None, Any] = Field(default=None, description="ID of the Connect application that earned the fee")
    """ID of the Connect application that earned the fee"""
    currency: Union[str, Any] = Field(default=None, description="Three-letter ISO currency code, in lowercase")
    """Three-letter ISO currency code, in lowercase"""
    description: Union[str | None, Any] = Field(default=None, description="An arbitrary string attached to the object")
    """An arbitrary string attached to the object"""
    type: Union[str, Any] = Field(default=None, description="Type of the fee")
    """Type of the fee"""

class BalanceTransaction(BaseModel):
    """BalanceTransaction type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    available_on: Union[int, Any] = Field(default=None)
    balance_type: Union[str, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    exchange_rate: Union[float | None, Any] = Field(default=None)
    fee: Union[int, Any] = Field(default=None)
    fee_details: Union[list[BalanceTransactionFeeDetailsItem], Any] = Field(default=None)
    net: Union[int, Any] = Field(default=None)
    reporting_category: Union[str, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)

class BalanceTransactionList(BaseModel):
    """BalanceTransactionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[BalanceTransaction], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class PaymentIntent(BaseModel):
    """PaymentIntent type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    amount_capturable: Union[int, Any] = Field(default=None)
    amount_received: Union[int, Any] = Field(default=None)
    application: Union[str | None, Any] = Field(default=None)
    application_fee_amount: Union[int | None, Any] = Field(default=None)
    capture_method: Union[str, Any] = Field(default=None)
    client_secret: Union[str | None, Any] = Field(default=None)
    confirmation_method: Union[str, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    customer: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    payment_method: Union[str | None, Any] = Field(default=None)
    payment_method_types: Union[list[str], Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)

class PaymentIntentList(BaseModel):
    """PaymentIntentList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[PaymentIntent], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class PaymentIntentSearchResult(BaseModel):
    """PaymentIntentSearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[PaymentIntent], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class DisputeEvidenceDetails(BaseModel):
    """Information about the evidence submission"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    due_by: Union[int | None, Any] = Field(default=None, description="Date by which evidence must be submitted, measured in seconds since the Unix epoch")
    """Date by which evidence must be submitted, measured in seconds since the Unix epoch"""
    has_evidence: Union[bool, Any] = Field(default=None, description="Whether evidence has been staged for this dispute")
    """Whether evidence has been staged for this dispute"""
    past_due: Union[bool, Any] = Field(default=None, description="Whether the last evidence submission was submitted past the due date")
    """Whether the last evidence submission was submitted past the due date"""
    submission_count: Union[int, Any] = Field(default=None, description="The number of times evidence has been submitted")
    """The number of times evidence has been submitted"""

class Dispute(BaseModel):
    """Dispute type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    balance_transactions: Union[list[dict[str, Any]], Any] = Field(default=None)
    charge: Union[str, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    enhanced_eligibility_types: Union[list[str], Any] = Field(default=None)
    evidence: Union[dict[str, Any], Any] = Field(default=None)
    evidence_details: Union[DisputeEvidenceDetails, Any] = Field(default=None)
    is_charge_refundable: Union[bool, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    payment_intent: Union[str | None, Any] = Field(default=None)
    payment_method_details: Union[dict[str, Any] | None, Any] = Field(default=None)
    reason: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)

class DisputeList(BaseModel):
    """DisputeList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Dispute], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class PayoutTraceId(BaseModel):
    """A string that identifies this payout as part of a group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None, description="The status of the trace ID")
    """The status of the trace ID"""
    value: Union[str | None, Any] = Field(default=None, description="The trace ID value")
    """The trace ID value"""

class Payout(BaseModel):
    """Payout type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    amount: Union[int, Any] = Field(default=None)
    application_fee: Union[str | None, Any] = Field(default=None)
    application_fee_amount: Union[int | None, Any] = Field(default=None)
    arrival_date: Union[int, Any] = Field(default=None)
    automatic: Union[bool, Any] = Field(default=None)
    balance_transaction: Union[str | None, Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    currency: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    destination: Union[str | None, Any] = Field(default=None)
    failure_balance_transaction: Union[str | None, Any] = Field(default=None)
    failure_code: Union[str | None, Any] = Field(default=None)
    failure_message: Union[str | None, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    method: Union[str, Any] = Field(default=None)
    original_payout: Union[str | None, Any] = Field(default=None)
    payout_method: Union[str | None, Any] = Field(default=None)
    reconciliation_status: Union[str, Any] = Field(default=None)
    reversed_by: Union[str | None, Any] = Field(default=None)
    source_balance: Union[str | None, Any] = Field(default=None)
    source_type: Union[str, Any] = Field(default=None)
    statement_descriptor: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    trace_id: Union[PayoutTraceId | None, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)

class PayoutList(BaseModel):
    """PayoutList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Payout], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class CustomerSearchResult(BaseModel):
    """CustomerSearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Customer], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class InvoiceSearchResult(BaseModel):
    """InvoiceSearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Invoice], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ChargeSearchResult(BaseModel):
    """ChargeSearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Charge], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class SubscriptionSearchResult(BaseModel):
    """SubscriptionSearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Subscription], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CustomersListResultMeta(BaseModel):
    """Metadata for customers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class CustomersApiSearchResultMeta(BaseModel):
    """Metadata for customers.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class InvoicesListResultMeta(BaseModel):
    """Metadata for invoices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class ChargesListResultMeta(BaseModel):
    """Metadata for charges.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class SubscriptionsListResultMeta(BaseModel):
    """Metadata for subscriptions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class RefundsListResultMeta(BaseModel):
    """Metadata for refunds.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class ProductsListResultMeta(BaseModel):
    """Metadata for products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class ProductsApiSearchResultMeta(BaseModel):
    """Metadata for products.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class BalanceTransactionsListResultMeta(BaseModel):
    """Metadata for balance_transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class PaymentIntentsListResultMeta(BaseModel):
    """Metadata for payment_intents.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class PaymentIntentsApiSearchResultMeta(BaseModel):
    """Metadata for payment_intents.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class DisputesListResultMeta(BaseModel):
    """Metadata for disputes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

class PayoutsListResultMeta(BaseModel):
    """Metadata for payouts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_more: Union[bool, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class StripeCheckResult(BaseModel):
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


class StripeExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class StripeExecuteResultWithMeta(StripeExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ChargesSearchData(BaseModel):
    """Search result data for charges entity."""
    model_config = ConfigDict(extra="allow")

    amount: int | None = None
    """Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits."""
    amount_captured: int | None = None
    """Amount that was actually captured from this charge."""
    amount_refunded: int | None = None
    """Amount that has been refunded back to the customer."""
    amount_updates: list[Any] | None = None
    """Updates to the amount that have been made during the charge lifecycle."""
    application: str | None = None
    """ID of the application that created this charge (Connect only)."""
    application_fee: str | None = None
    """ID of the application fee associated with this charge (Connect only)."""
    application_fee_amount: int | None = None
    """The amount of the application fee deducted from this charge (Connect only)."""
    balance_transaction: str | None = None
    """ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes)."""
    billing_details: dict[str, Any] | None = None
    """Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address."""
    calculated_statement_descriptor: str | None = None
    """The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix."""
    captured: bool | None = None
    """Whether the charge has been captured and funds transferred to your account."""
    card: dict[str, Any] | None = None
    """Deprecated card object containing payment card details if a card was used."""
    created: int | None = None
    """Timestamp indicating when the charge was created."""
    currency: str | None = None
    """Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount."""
    customer: str | None = None
    """ID of the customer this charge is for, if one exists."""
    description: str | None = None
    """An arbitrary string attached to the charge, often useful for displaying to users or internal reference."""
    destination: str | None = None
    """ID of the destination account where funds are transferred (Connect only)."""
    dispute: str | None = None
    """ID of the dispute object if the charge has been disputed."""
    disputed: bool | None = None
    """Whether the charge has been disputed by the customer with their card issuer."""
    failure_balance_transaction: str | None = None
    """ID of the balance transaction that describes the reversal of funds if the charge failed."""
    failure_code: str | None = None
    """Error code explaining the reason for charge failure, if applicable."""
    failure_message: str | None = None
    """Human-readable message providing more details about why the charge failed."""
    fraud_details: dict[str, Any] | None = None
    """Information about fraud assessments and user reports related to this charge."""
    id: str = None
    """Unique identifier for the charge, used to link transactions across other records."""
    invoice: str | None = None
    """ID of the invoice this charge is for, if the charge was created by invoicing."""
    livemode: bool | None = None
    """Whether the charge occurred in live mode (true) or test mode (false)."""
    metadata: dict[str, Any] | None = None
    """Key-value pairs for storing additional structured information about the charge, useful for internal tracking."""
    object: str | None = None
    """String representing the object type, always 'charge' for charge objects."""
    on_behalf_of: str | None = None
    """ID of the account on whose behalf the charge was made (Connect only)."""
    order: str | None = None
    """Deprecated field for order information associated with this charge."""
    outcome: dict[str, Any] | None = None
    """Details about the outcome of the charge, including network status, risk assessment, and reason codes."""
    paid: bool | None = None
    """Whether the charge succeeded and funds were successfully collected."""
    payment_intent: str | None = None
    """ID of the PaymentIntent associated with this charge, if one exists."""
    payment_method: str | None = None
    """ID of the payment method used for this charge."""
    payment_method_details: dict[str, Any] | None = None
    """Details about the payment method at the time of the transaction, including card brand, network, and authentication results."""
    receipt_email: str | None = None
    """Email address to which the receipt for this charge was sent."""
    receipt_number: str | None = None
    """Receipt number that appears on email receipts sent for this charge."""
    receipt_url: str | None = None
    """URL to a hosted receipt page for this charge, viewable by the customer."""
    refunded: bool | None = None
    """Whether the charge has been fully refunded (partial refunds will still show as false)."""
    refunds: dict[str, Any] | None = None
    """List of refunds that have been applied to this charge."""
    review: str | None = None
    """ID of the review object associated with this charge, if it was flagged for manual review."""
    shipping: dict[str, Any] | None = None
    """Shipping information for the charge, including recipient name, address, and tracking details."""
    source: dict[str, Any] | None = None
    """Deprecated payment source object used to create this charge."""
    source_transfer: str | None = None
    """ID of the transfer from a source account if funds came from another Stripe account (Connect only)."""
    statement_description: str | None = None
    """Deprecated alias for statement_descriptor."""
    statement_descriptor: str | None = None
    """Statement descriptor that overrides the account default for card charges, appearing on the customer's statement."""
    statement_descriptor_suffix: str | None = None
    """Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements."""
    status: str | None = None
    """Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful)."""
    transfer_data: dict[str, Any] | None = None
    """Object containing destination and amount for transfers to connected accounts (Connect only)."""
    transfer_group: str | None = None
    """String identifier for grouping related charges and transfers together (Connect only)."""
    updated: int | None = None
    """Timestamp of the last update to this charge object."""


class CustomersSearchData(BaseModel):
    """Search result data for customers entity."""
    model_config = ConfigDict(extra="allow")

    account_balance: int | None = None
    """Current balance value representing funds owed by or to the customer."""
    address: dict[str, Any] | None = None
    """The customer's address information including line1, line2, city, state, postal code, and country."""
    balance: int | None = None
    """Current balance (positive or negative) that is automatically applied to the customer's next invoice."""
    cards: list[Any] | None = None
    """Card payment methods associated with the customer account."""
    created: int | None = None
    """Timestamp indicating when the customer object was created."""
    currency: str | None = None
    """Three-letter ISO currency code representing the customer's default currency."""
    default_card: str | None = None
    """The default card to be used for charges when no specific payment method is provided."""
    default_source: str | None = None
    """The default payment source (card or bank account) for the customer."""
    delinquent: bool | None = None
    """Boolean indicating whether the customer is currently delinquent on payments."""
    description: str | None = None
    """An arbitrary string attached to the customer, often useful for displaying to users."""
    discount: dict[str, Any] | None = None
    """Discount object describing any active discount applied to the customer."""
    email: str | None = None
    """The customer's email address for communication and tracking purposes."""
    id: str | None = None
    """Unique identifier for the customer object."""
    invoice_prefix: str | None = None
    """The prefix for invoice numbers generated for this customer."""
    invoice_settings: dict[str, Any] | None = None
    """Customer's invoice-related settings including default payment method and custom fields."""
    is_deleted: bool | None = None
    """Boolean indicating whether the customer has been deleted."""
    livemode: bool | None = None
    """Boolean indicating whether the object exists in live mode or test mode."""
    metadata: dict[str, Any] | None = None
    """Set of key-value pairs for storing additional structured information about the customer."""
    name: str | None = None
    """The customer's full name or business name."""
    next_invoice_sequence: int | None = None
    """The sequence number for the next invoice generated for this customer."""
    object: str | None = None
    """String representing the object type, always 'customer'."""
    phone: str | None = None
    """The customer's phone number."""
    preferred_locales: list[Any] | None = None
    """Array of preferred locales for the customer, used for invoice and receipt localization."""
    shipping: dict[str, Any] | None = None
    """Mailing and shipping address for the customer, appears on invoices emailed to the customer."""
    sources: str = None
    """Payment sources (cards, bank accounts) attached to the customer for making payments."""
    subscriptions: dict[str, Any] | None = None
    """List of active subscriptions associated with the customer."""
    tax_exempt: str | None = None
    """Describes the customer's tax exemption status (none, exempt, or reverse)."""
    tax_info: str | None = None
    """Tax identification information for the customer."""
    tax_info_verification: str | None = None
    """Verification status of the customer's tax information."""
    test_clock: str | None = None
    """ID of the test clock associated with this customer for testing time-dependent scenarios."""
    updated: int | None = None
    """Timestamp indicating when the customer object was last updated."""


class InvoicesSearchData(BaseModel):
    """Search result data for invoices entity."""
    model_config = ConfigDict(extra="allow")

    account_country: str | None = None
    """The country of the business associated with this invoice, commonly used to display localized content."""
    account_name: str | None = None
    """The public name of the business associated with this invoice."""
    account_tax_ids: list[Any] | None = None
    """Tax IDs of the account associated with this invoice."""
    amount_due: int | None = None
    """Total amount, in smallest currency unit, that is due and owed by the customer."""
    amount_paid: int | None = None
    """Total amount, in smallest currency unit, that has been paid by the customer."""
    amount_remaining: int | None = None
    """The difference between amount_due and amount_paid, representing the outstanding balance."""
    amount_shipping: int | None = None
    """Total amount of shipping costs on the invoice."""
    application: str | None = None
    """ID of the Connect application that created this invoice."""
    application_fee: int | None = None
    """Amount of application fee charged for this invoice in a Connect scenario."""
    application_fee_amount: int | None = None
    """The fee in smallest currency unit that is collected by the application in a Connect scenario."""
    attempt_count: int | None = None
    """Number of payment attempts made for this invoice."""
    attempted: bool | None = None
    """Whether an attempt has been made to pay the invoice."""
    auto_advance: bool | None = None
    """Controls whether Stripe performs automatic collection of the invoice."""
    automatic_tax: dict[str, Any] | None = None
    """Settings and status for automatic tax calculation on this invoice."""
    billing: str | None = None
    """Billing method used for the invoice (charge_automatically or send_invoice)."""
    billing_reason: str | None = None
    """Indicates the reason why the invoice was created (subscription_cycle, manual, etc.)."""
    charge: str | None = None
    """ID of the latest charge generated for this invoice, if any."""
    closed: bool | None = None
    """Whether the invoice has been marked as closed and no longer open for collection."""
    collection_method: str | None = None
    """Method by which the invoice is collected: charge_automatically or send_invoice."""
    created: int | None = None
    """Timestamp indicating when the invoice was created."""
    currency: str | None = None
    """Three-letter ISO currency code in which the invoice is denominated."""
    custom_fields: list[Any] | None = None
    """Custom fields displayed on the invoice as specified by the account."""
    customer: str | None = None
    """The customer object or ID associated with this invoice."""
    customer_address: dict[str, Any] | None = None
    """The customer's address at the time the invoice was finalized."""
    customer_email: str | None = None
    """The customer's email address at the time the invoice was finalized."""
    customer_name: str | None = None
    """The customer's name at the time the invoice was finalized."""
    customer_phone: str | None = None
    """The customer's phone number at the time the invoice was finalized."""
    customer_shipping: dict[str, Any] | None = None
    """The customer's shipping information at the time the invoice was finalized."""
    customer_tax_exempt: str | None = None
    """The customer's tax exempt status at the time the invoice was finalized."""
    customer_tax_ids: list[Any] | None = None
    """The customer's tax IDs at the time the invoice was finalized."""
    default_payment_method: str | None = None
    """Default payment method for the invoice, used if no other method is specified."""
    default_source: str | None = None
    """Default payment source for the invoice if no payment method is set."""
    default_tax_rates: list[Any] | None = None
    """The tax rates applied to the invoice by default."""
    description: str | None = None
    """An arbitrary string attached to the invoice, often displayed to customers."""
    discount: dict[str, Any] | None = None
    """The discount object applied to the invoice, if any."""
    discounts: list[Any] | None = None
    """Array of discount IDs or objects currently applied to this invoice."""
    due_date: float | None = None
    """The date by which payment on this invoice is due, if the invoice is not auto-collected."""
    effective_at: int | None = None
    """Timestamp when the invoice becomes effective and finalized for payment."""
    ending_balance: int | None = None
    """The customer's ending account balance after this invoice is finalized."""
    footer: str | None = None
    """Footer text displayed on the invoice."""
    forgiven: bool | None = None
    """Whether the invoice has been forgiven and is considered paid without actual payment."""
    from_invoice: dict[str, Any] | None = None
    """Details about the invoice this invoice was created from, if applicable."""
    hosted_invoice_url: str | None = None
    """URL for the hosted invoice page where customers can view and pay the invoice."""
    id: str | None = None
    """Unique identifier for the invoice object."""
    invoice_pdf: str | None = None
    """URL for the PDF version of the invoice."""
    is_deleted: bool | None = None
    """Indicates whether this invoice has been deleted."""
    issuer: dict[str, Any] | None = None
    """Details about the entity issuing the invoice."""
    last_finalization_error: dict[str, Any] | None = None
    """The error encountered during the last finalization attempt, if any."""
    latest_revision: str | None = None
    """The latest revision of the invoice, if revisions are enabled."""
    lines: dict[str, Any] | None = None
    """The individual line items that make up the invoice, representing products, services, or fees."""
    livemode: bool | None = None
    """Indicates whether the invoice exists in live mode (true) or test mode (false)."""
    metadata: dict[str, Any] | None = None
    """Key-value pairs for storing additional structured information about the invoice."""
    next_payment_attempt: float | None = None
    """Timestamp of the next automatic payment attempt for this invoice, if applicable."""
    number: str | None = None
    """A unique, human-readable identifier for this invoice, often shown to customers."""
    object: str | None = None
    """String representing the object type, always 'invoice'."""
    on_behalf_of: str | None = None
    """The account on behalf of which the invoice is being created, used in Connect scenarios."""
    paid: bool | None = None
    """Whether the invoice has been paid in full."""
    paid_out_of_band: bool | None = None
    """Whether payment was made outside of Stripe and manually marked as paid."""
    payment: str | None = None
    """ID of the payment associated with this invoice, if any."""
    payment_intent: str | None = None
    """The PaymentIntent associated with this invoice for processing payment."""
    payment_settings: dict[str, Any] | None = None
    """Configuration settings for how payment should be collected on this invoice."""
    period_end: float | None = None
    """End date of the billing period covered by this invoice."""
    period_start: float | None = None
    """Start date of the billing period covered by this invoice."""
    post_payment_credit_notes_amount: int | None = None
    """Total amount of credit notes issued after the invoice was paid."""
    pre_payment_credit_notes_amount: int | None = None
    """Total amount of credit notes applied before payment was attempted."""
    quote: str | None = None
    """The quote from which this invoice was generated, if applicable."""
    receipt_number: str | None = None
    """The receipt number displayed on the invoice, if available."""
    rendering: dict[str, Any] | None = None
    """Settings that control how the invoice is rendered for display."""
    rendering_options: dict[str, Any] | None = None
    """Options for customizing the visual rendering of the invoice."""
    shipping_cost: dict[str, Any] | None = None
    """Total cost of shipping charges included in the invoice."""
    shipping_details: dict[str, Any] | None = None
    """Detailed shipping information for the invoice, including address and carrier."""
    starting_balance: int | None = None
    """The customer's starting account balance at the beginning of the billing period."""
    statement_description: str | None = None
    """Extra information about the invoice that appears on the customer's credit card statement."""
    statement_descriptor: str | None = None
    """A dynamic descriptor that appears on the customer's credit card statement for this invoice."""
    status: str | None = None
    """The status of the invoice: draft, open, paid, void, or uncollectible."""
    status_transitions: dict[str, Any] = None
    """Timestamps tracking when the invoice transitioned between different statuses."""
    subscription: str | None = None
    """The subscription this invoice was generated for, if applicable."""
    subscription_details: dict[str, Any] | None = None
    """Additional details about the subscription associated with this invoice."""
    subtotal: int | None = None
    """Total of all line items before discounts or tax are applied."""
    subtotal_excluding_tax: int | None = None
    """The subtotal amount excluding any tax calculations."""
    tax: int | None = None
    """Total tax amount applied to the invoice."""
    tax_percent: float | None = None
    """The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead)."""
    test_clock: str | None = None
    """ID of the test clock this invoice belongs to, used for testing time-dependent billing."""
    total: int | None = None
    """Total amount of the invoice after all line items, discounts, and taxes are calculated."""
    total_discount_amounts: list[Any] | None = None
    """Array of the total discount amounts applied, broken down by discount."""
    total_excluding_tax: int | None = None
    """Total amount of the invoice excluding all tax calculations."""
    total_tax_amounts: list[Any] | None = None
    """Array of tax amounts applied to the invoice, broken down by tax rate."""
    transfer_data: dict[str, Any] | None = None
    """Information about the transfer of funds associated with this invoice in Connect scenarios."""
    updated: int | None = None
    """Timestamp indicating when the invoice was last updated."""
    webhooks_delivered_at: float | None = None
    """Timestamp indicating when webhooks for this invoice were successfully delivered."""


class RefundsSearchData(BaseModel):
    """Search result data for refunds entity."""
    model_config = ConfigDict(extra="allow")

    amount: int | None = None
    """Amount refunded, in cents (the smallest currency unit)."""
    balance_transaction: str | None = None
    """ID of the balance transaction that describes the impact of this refund on your account balance."""
    charge: str | None = None
    """ID of the charge that was refunded."""
    created: int | None = None
    """Timestamp indicating when the refund was created."""
    currency: str | None = None
    """Three-letter ISO currency code in lowercase representing the currency of the refund."""
    destination_details: dict[str, Any] | None = None
    """Details about the destination where the refunded funds should be sent."""
    id: str | None = None
    """Unique identifier for the refund object."""
    metadata: dict[str, Any] | None = None
    """Set of key-value pairs that you can attach to an object for storing additional structured information."""
    object: str | None = None
    """String representing the object type, always 'refund'."""
    payment_intent: str | None = None
    """ID of the PaymentIntent that was refunded."""
    reason: str | None = None
    """Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge)."""
    receipt_number: str | None = None
    """The transaction number that appears on email receipts sent for this refund."""
    source_transfer_reversal: str | None = None
    """ID of the transfer reversal that was created as a result of refunding a transfer (Connect only)."""
    status: str | None = None
    """Status of the refund (pending, requires_action, succeeded, failed, or canceled)."""
    transfer_reversal: str | None = None
    """ID of the reversal of the transfer that funded the charge being refunded (Connect only)."""
    updated: int | None = None
    """Timestamp indicating when the refund was last updated."""


class SubscriptionsSearchData(BaseModel):
    """Search result data for subscriptions entity."""
    model_config = ConfigDict(extra="allow")

    application: str | None = None
    """For Connect platforms, the application associated with the subscription."""
    application_fee_percent: float | None = None
    """For Connect platforms, the percentage of the subscription amount taken as an application fee."""
    automatic_tax: dict[str, Any] | None = None
    """Automatic tax calculation settings for the subscription."""
    billing: str | None = None
    """Billing mode configuration for the subscription."""
    billing_cycle_anchor: float | None = None
    """Timestamp determining when the billing cycle for the subscription starts."""
    billing_cycle_anchor_config: dict[str, Any] | None = None
    """Configuration for the subscription's billing cycle anchor behavior."""
    billing_thresholds: dict[str, Any] | None = None
    """Defines thresholds at which an invoice will be sent, controlling billing timing based on usage."""
    cancel_at: float | None = None
    """Timestamp indicating when the subscription is scheduled to be canceled."""
    cancel_at_period_end: bool | None = None
    """Boolean indicating whether the subscription will be canceled at the end of the current billing period."""
    canceled_at: float | None = None
    """Timestamp indicating when the subscription was canceled, if applicable."""
    cancellation_details: dict[str, Any] | None = None
    """Details about why and how the subscription was canceled."""
    collection_method: str | None = None
    """How invoices are collected (charge_automatically or send_invoice)."""
    created: int | None = None
    """Timestamp indicating when the subscription was created."""
    currency: str | None = None
    """Three-letter ISO currency code in lowercase indicating the currency for the subscription."""
    current_period_end: float | None = None
    """Timestamp marking the end of the current billing period."""
    current_period_start: int | None = None
    """Timestamp marking the start of the current billing period."""
    customer: str | None = None
    """ID of the customer who owns the subscription, expandable to full customer object."""
    days_until_due: int | None = None
    """Number of days until the invoice is due for subscriptions using send_invoice collection method."""
    default_payment_method: str | None = None
    """ID of the default payment method for the subscription, taking precedence over default_source."""
    default_source: str | None = None
    """ID of the default payment source for the subscription."""
    default_tax_rates: list[Any] | None = None
    """Tax rates that apply to the subscription by default."""
    description: str | None = None
    """Human-readable description of the subscription, displayable to the customer."""
    discount: dict[str, Any] | None = None
    """Describes any discount currently applied to the subscription."""
    ended_at: float | None = None
    """Timestamp indicating when the subscription ended, if applicable."""
    id: str | None = None
    """Unique identifier for the subscription object."""
    invoice_settings: dict[str, Any] | None = None
    """Settings for invoices generated by this subscription, such as custom fields and footer."""
    is_deleted: bool | None = None
    """Indicates whether the subscription has been deleted."""
    items: dict[str, Any] | None = None
    """List of subscription items, each with an attached price defining what the customer is subscribed to."""
    latest_invoice: str | None = None
    """The most recent invoice this subscription has generated, expandable to full invoice object."""
    livemode: bool | None = None
    """Indicates whether the subscription exists in live mode (true) or test mode (false)."""
    metadata: dict[str, Any] | None = None
    """Set of key-value pairs that you can attach to the subscription for storing additional structured information."""
    next_pending_invoice_item_invoice: int | None = None
    """Timestamp when the next invoice for pending invoice items will be created."""
    object: str | None = None
    """String representing the object type, always 'subscription'."""
    on_behalf_of: str | None = None
    """For Connect platforms, the account for which the subscription is being created or managed."""
    pause_collection: dict[str, Any] | None = None
    """Configuration for pausing collection on the subscription while retaining the subscription structure."""
    payment_settings: dict[str, Any] | None = None
    """Payment settings for invoices generated by this subscription."""
    pending_invoice_item_interval: dict[str, Any] | None = None
    """Specifies an interval for aggregating usage records into pending invoice items."""
    pending_setup_intent: str | None = None
    """SetupIntent used for collecting user authentication when updating payment methods without immediate payment."""
    pending_update: dict[str, Any] | None = None
    """If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid."""
    plan: dict[str, Any] | None = None
    """The plan associated with the subscription (deprecated, use items instead)."""
    quantity: int | None = None
    """Quantity of the plan subscribed to (deprecated, use items instead)."""
    schedule: str | None = None
    """ID of the subscription schedule managing this subscription's lifecycle, if applicable."""
    start_date: int | None = None
    """Timestamp indicating when the subscription started."""
    status: str | None = None
    """Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)."""
    tax_percent: float | None = None
    """The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead)."""
    test_clock: str | None = None
    """ID of the test clock associated with this subscription for simulating time-based scenarios."""
    transfer_data: dict[str, Any] | None = None
    """For Connect platforms, the account receiving funds from the subscription and optional percentage transferred."""
    trial_end: float | None = None
    """Timestamp indicating when the trial period ends, if applicable."""
    trial_settings: dict[str, Any] | None = None
    """Settings related to trial periods, including conditions for ending trials."""
    trial_start: int | None = None
    """Timestamp indicating when the trial period began, if applicable."""
    updated: int | None = None
    """Timestamp indicating when the subscription was last updated."""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchHit(BaseModel, Generic[D]):
    """A single search result with typed data."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the record."""
    score: float | None = None
    """Relevance score for the match."""
    data: D
    """The matched record data."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed hits."""
    model_config = ConfigDict(extra="allow")

    hits: list[AirbyteSearchHit[D]] = Field(default_factory=list)
    """List of matching records."""
    next_cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

ChargesSearchResult = AirbyteSearchResult[ChargesSearchData]
"""Search result type for charges entity."""

CustomersSearchResult = AirbyteSearchResult[CustomersSearchData]
"""Search result type for customers entity."""

InvoicesSearchResult = AirbyteSearchResult[InvoicesSearchData]
"""Search result type for invoices entity."""

RefundsSearchResult = AirbyteSearchResult[RefundsSearchData]
"""Search result type for refunds entity."""

SubscriptionsSearchResult = AirbyteSearchResult[SubscriptionsSearchData]
"""Search result type for subscriptions entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CustomersListResult = StripeExecuteResultWithMeta[list[Customer], CustomersListResultMeta]
"""Result type for customers.list operation with data and metadata."""

CustomersApiSearchResult = StripeExecuteResultWithMeta[list[Customer], CustomersApiSearchResultMeta]
"""Result type for customers.api_search operation with data and metadata."""

InvoicesListResult = StripeExecuteResultWithMeta[list[Invoice], InvoicesListResultMeta]
"""Result type for invoices.list operation with data and metadata."""

InvoicesApiSearchResult = StripeExecuteResult[InvoiceSearchResult]
"""Result type for invoices.api_search operation."""

ChargesListResult = StripeExecuteResultWithMeta[list[Charge], ChargesListResultMeta]
"""Result type for charges.list operation with data and metadata."""

ChargesApiSearchResult = StripeExecuteResult[ChargeSearchResult]
"""Result type for charges.api_search operation."""

SubscriptionsListResult = StripeExecuteResultWithMeta[list[Subscription], SubscriptionsListResultMeta]
"""Result type for subscriptions.list operation with data and metadata."""

SubscriptionsApiSearchResult = StripeExecuteResult[SubscriptionSearchResult]
"""Result type for subscriptions.api_search operation."""

RefundsListResult = StripeExecuteResultWithMeta[list[Refund], RefundsListResultMeta]
"""Result type for refunds.list operation with data and metadata."""

ProductsListResult = StripeExecuteResultWithMeta[list[Product], ProductsListResultMeta]
"""Result type for products.list operation with data and metadata."""

ProductsApiSearchResult = StripeExecuteResultWithMeta[list[Product], ProductsApiSearchResultMeta]
"""Result type for products.api_search operation with data and metadata."""

BalanceTransactionsListResult = StripeExecuteResultWithMeta[list[BalanceTransaction], BalanceTransactionsListResultMeta]
"""Result type for balance_transactions.list operation with data and metadata."""

PaymentIntentsListResult = StripeExecuteResultWithMeta[list[PaymentIntent], PaymentIntentsListResultMeta]
"""Result type for payment_intents.list operation with data and metadata."""

PaymentIntentsApiSearchResult = StripeExecuteResultWithMeta[list[PaymentIntent], PaymentIntentsApiSearchResultMeta]
"""Result type for payment_intents.api_search operation with data and metadata."""

DisputesListResult = StripeExecuteResultWithMeta[list[Dispute], DisputesListResultMeta]
"""Result type for disputes.list operation with data and metadata."""

PayoutsListResult = StripeExecuteResultWithMeta[list[Payout], PayoutsListResultMeta]
"""Result type for payouts.list operation with data and metadata."""

