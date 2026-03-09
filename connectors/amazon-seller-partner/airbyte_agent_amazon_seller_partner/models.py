"""
Pydantic models for amazon-seller-partner connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class AmazonSellerPartnerAuthConfig(BaseModel):
    """Login with Amazon OAuth 2.0"""

    model_config = ConfigDict(extra="forbid")

    lwa_app_id: str
    """Your Login with Amazon Client ID."""
    lwa_client_secret: str
    """Your Login with Amazon Client Secret."""
    refresh_token: str
    """The Refresh Token obtained via the OAuth authorization flow."""
    access_token: Optional[str] = None
    """Access token (optional if refresh_token is provided)."""

# Replication configuration

class AmazonSellerPartnerReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Amazon Seller Partner."""

    model_config = ConfigDict(extra="forbid")

    replication_start_date: str
    """UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class OrderShippingaddress(BaseModel):
    """Shipping address for the order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    city: Union[str, Any] = Field(default=None, alias="City")
    state_or_region: Union[str, Any] = Field(default=None, alias="StateOrRegion")
    postal_code: Union[str, Any] = Field(default=None, alias="PostalCode")
    country_code: Union[str, Any] = Field(default=None, alias="CountryCode")

class OrderOrdertotal(BaseModel):
    """Total amount of the order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderDefaultshipfromlocationaddress(BaseModel):
    """Default ship-from address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, alias="Name")
    address_line1: Union[str, Any] = Field(default=None, alias="AddressLine1")
    city: Union[str, Any] = Field(default=None, alias="City")
    state_or_region: Union[str, Any] = Field(default=None, alias="StateOrRegion")
    postal_code: Union[str, Any] = Field(default=None, alias="PostalCode")
    country_code: Union[str, Any] = Field(default=None, alias="CountryCode")

class OrderAutomatedshippingsettings(BaseModel):
    """Automated shipping settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_automated_shipping_settings: Union[bool, Any] = Field(default=None, alias="HasAutomatedShippingSettings")

class Order(BaseModel):
    """Amazon order object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amazon_order_id: Union[str, Any] = Field(default=None, alias="AmazonOrderId")
    seller_order_id: Union[str, Any] = Field(default=None, alias="SellerOrderId")
    purchase_date: Union[str, Any] = Field(default=None, alias="PurchaseDate")
    last_update_date: Union[str, Any] = Field(default=None, alias="LastUpdateDate")
    order_status: Union[str, Any] = Field(default=None, alias="OrderStatus")
    fulfillment_channel: Union[str, Any] = Field(default=None, alias="FulfillmentChannel")
    sales_channel: Union[str, Any] = Field(default=None, alias="SalesChannel")
    ship_service_level: Union[str, Any] = Field(default=None, alias="ShipServiceLevel")
    order_total: Union[OrderOrdertotal, Any] = Field(default=None, alias="OrderTotal")
    number_of_items_shipped: Union[int, Any] = Field(default=None, alias="NumberOfItemsShipped")
    number_of_items_unshipped: Union[int, Any] = Field(default=None, alias="NumberOfItemsUnshipped")
    payment_method: Union[str, Any] = Field(default=None, alias="PaymentMethod")
    payment_method_details: Union[list[str], Any] = Field(default=None, alias="PaymentMethodDetails")
    marketplace_id: Union[str, Any] = Field(default=None, alias="MarketplaceId")
    shipment_service_level_category: Union[str, Any] = Field(default=None, alias="ShipmentServiceLevelCategory")
    order_type: Union[str, Any] = Field(default=None, alias="OrderType")
    earliest_ship_date: Union[str, Any] = Field(default=None, alias="EarliestShipDate")
    latest_ship_date: Union[str, Any] = Field(default=None, alias="LatestShipDate")
    earliest_delivery_date: Union[str, Any] = Field(default=None, alias="EarliestDeliveryDate")
    latest_delivery_date: Union[str, Any] = Field(default=None, alias="LatestDeliveryDate")
    is_business_order: Union[bool, Any] = Field(default=None, alias="IsBusinessOrder")
    is_prime: Union[bool, Any] = Field(default=None, alias="IsPrime")
    is_global_express_enabled: Union[bool, Any] = Field(default=None, alias="IsGlobalExpressEnabled")
    is_premium_order: Union[bool, Any] = Field(default=None, alias="IsPremiumOrder")
    is_sold_by_ab: Union[bool, Any] = Field(default=None, alias="IsSoldByAB")
    is_replacement_order: Union[str, Any] = Field(default=None, alias="IsReplacementOrder")
    is_ispu: Union[bool, Any] = Field(default=None, alias="IsISPU")
    is_access_point_order: Union[bool, Any] = Field(default=None, alias="IsAccessPointOrder")
    has_regulated_items: Union[bool, Any] = Field(default=None, alias="HasRegulatedItems")
    shipping_address: Union[OrderShippingaddress, Any] = Field(default=None, alias="ShippingAddress")
    default_ship_from_location_address: Union[OrderDefaultshipfromlocationaddress, Any] = Field(default=None, alias="DefaultShipFromLocationAddress")
    automated_shipping_settings: Union[OrderAutomatedshippingsettings, Any] = Field(default=None, alias="AutomatedShippingSettings")
    buyer_info: Union[dict[str, Any], Any] = Field(default=None, alias="BuyerInfo")

class OrdersListPayload(BaseModel):
    """Nested schema for OrdersList.payload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    orders: Union[list[Order], Any] = Field(default=None, alias="Orders")
    next_token: Union[str, Any] = Field(default=None, alias="NextToken", description="Pagination token for next page")
    """Pagination token for next page"""

class OrdersList(BaseModel):
    """Paginated list of orders"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payload: Union[OrdersListPayload, Any] = Field(default=None)

class OrderItemCodfee(BaseModel):
    """Cash on delivery fee"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemItemtax(BaseModel):
    """Item tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemProductinfo(BaseModel):
    """Product information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    number_of_items: Union[str, Any] = Field(default=None, alias="NumberOfItems")

class OrderItemBuyerrequestedcancel(BaseModel):
    """Buyer cancellation request information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    is_buyer_requested_cancel: Union[str, Any] = Field(default=None, alias="IsBuyerRequestedCancel")
    buyer_cancel_reason: Union[str, Any] = Field(default=None, alias="BuyerCancelReason")

class OrderItemCodfeediscount(BaseModel):
    """Cash on delivery fee discount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemShippingprice(BaseModel):
    """Shipping price"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemShippingdiscounttax(BaseModel):
    """Shipping discount tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemTaxcollection(BaseModel):
    """Tax collection information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    model: Union[str, Any] = Field(default=None, alias="Model")
    responsible_party: Union[str, Any] = Field(default=None, alias="ResponsibleParty")

class OrderItemBuyerinfoBuyercustomizedinfo(BaseModel):
    """Nested schema for OrderItemBuyerinfo.BuyerCustomizedInfo"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customized_url: Union[str, Any] = Field(default=None, alias="CustomizedURL")

class OrderItemBuyerinfoGiftwrapprice(BaseModel):
    """Nested schema for OrderItemBuyerinfo.GiftWrapPrice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemBuyerinfo(BaseModel):
    """Buyer information for the item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    buyer_customized_info: Union[OrderItemBuyerinfoBuyercustomizedinfo, Any] = Field(default=None, alias="BuyerCustomizedInfo")
    gift_message_text: Union[str, Any] = Field(default=None, alias="GiftMessageText")
    gift_wrap_price: Union[OrderItemBuyerinfoGiftwrapprice, Any] = Field(default=None, alias="GiftWrapPrice")
    gift_wrap_level: Union[str, Any] = Field(default=None, alias="GiftWrapLevel")

class OrderItemShippingtax(BaseModel):
    """Shipping tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemPromotiondiscount(BaseModel):
    """Promotion discount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemPointsgrantedPointsmonetaryvalue(BaseModel):
    """Nested schema for OrderItemPointsgranted.PointsMonetaryValue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemPointsgranted(BaseModel):
    """Points granted for the purchase"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    points_number: Union[int, Any] = Field(default=None, alias="PointsNumber")
    points_monetary_value: Union[OrderItemPointsgrantedPointsmonetaryvalue, Any] = Field(default=None, alias="PointsMonetaryValue")

class OrderItemItemprice(BaseModel):
    """Item price"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemPromotiondiscounttax(BaseModel):
    """Promotion discount tax"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItemShippingdiscount(BaseModel):
    """Shipping discount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    amount: Union[str, Any] = Field(default=None, alias="Amount")

class OrderItem(BaseModel):
    """Amazon order item object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order_item_id: Union[str, Any] = Field(default=None, alias="OrderItemId")
    amazon_order_id: Union[str, Any] = Field(default=None, alias="AmazonOrderId")
    asin: Union[str, Any] = Field(default=None, alias="ASIN")
    seller_sku: Union[str, Any] = Field(default=None, alias="SellerSKU")
    title: Union[str, Any] = Field(default=None, alias="Title")
    quantity_ordered: Union[int, Any] = Field(default=None, alias="QuantityOrdered")
    quantity_shipped: Union[int, Any] = Field(default=None, alias="QuantityShipped")
    item_price: Union[OrderItemItemprice, Any] = Field(default=None, alias="ItemPrice")
    item_tax: Union[OrderItemItemtax, Any] = Field(default=None, alias="ItemTax")
    shipping_price: Union[OrderItemShippingprice, Any] = Field(default=None, alias="ShippingPrice")
    shipping_tax: Union[OrderItemShippingtax, Any] = Field(default=None, alias="ShippingTax")
    shipping_discount: Union[OrderItemShippingdiscount, Any] = Field(default=None, alias="ShippingDiscount")
    shipping_discount_tax: Union[OrderItemShippingdiscounttax, Any] = Field(default=None, alias="ShippingDiscountTax")
    promotion_discount: Union[OrderItemPromotiondiscount, Any] = Field(default=None, alias="PromotionDiscount")
    promotion_discount_tax: Union[OrderItemPromotiondiscounttax, Any] = Field(default=None, alias="PromotionDiscountTax")
    promotion_ids: Union[list[str], Any] = Field(default=None, alias="PromotionIds")
    cod_fee: Union[OrderItemCodfee, Any] = Field(default=None, alias="CODFee")
    cod_fee_discount: Union[OrderItemCodfeediscount, Any] = Field(default=None, alias="CODFeeDiscount")
    is_gift: Union[str, Any] = Field(default=None, alias="IsGift")
    condition_id: Union[str, Any] = Field(default=None, alias="ConditionId")
    condition_subtype_id: Union[str, Any] = Field(default=None, alias="ConditionSubtypeId")
    condition_note: Union[str, Any] = Field(default=None, alias="ConditionNote")
    is_transparency: Union[bool, Any] = Field(default=None, alias="IsTransparency")
    serial_number_required: Union[bool, Any] = Field(default=None, alias="SerialNumberRequired")
    ioss_number: Union[str, Any] = Field(default=None, alias="IossNumber")
    deemed_reseller_category: Union[str, Any] = Field(default=None, alias="DeemedResellerCategory")
    store_chain_store_id: Union[str, Any] = Field(default=None, alias="StoreChainStoreId")
    product_info: Union[OrderItemProductinfo, Any] = Field(default=None, alias="ProductInfo")
    buyer_info: Union[OrderItemBuyerinfo, Any] = Field(default=None, alias="BuyerInfo")
    buyer_requested_cancel: Union[OrderItemBuyerrequestedcancel, Any] = Field(default=None, alias="BuyerRequestedCancel")
    points_granted: Union[OrderItemPointsgranted, Any] = Field(default=None, alias="PointsGranted")
    tax_collection: Union[OrderItemTaxcollection, Any] = Field(default=None, alias="TaxCollection")
    price_designation: Union[str, Any] = Field(default=None, alias="PriceDesignation")

class OrderItemsListPayload(BaseModel):
    """Nested schema for OrderItemsList.payload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amazon_order_id: Union[str, Any] = Field(default=None, alias="AmazonOrderId")
    order_items: Union[list[OrderItem], Any] = Field(default=None, alias="OrderItems")
    next_token: Union[str, Any] = Field(default=None, alias="NextToken")

class OrderItemsList(BaseModel):
    """Paginated list of order items"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payload: Union[OrderItemsListPayload, Any] = Field(default=None)

class FinancialEventGroupConvertedtotal(BaseModel):
    """Converted total"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventGroupBeginningbalance(BaseModel):
    """Beginning balance"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventGroupOriginaltotal(BaseModel):
    """Original total in seller's currency"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventGroup(BaseModel):
    """A financial event group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    financial_event_group_id: Union[str, Any] = Field(default=None, alias="FinancialEventGroupId")
    processing_status: Union[str, Any] = Field(default=None, alias="ProcessingStatus")
    fund_transfer_status: Union[str, Any] = Field(default=None, alias="FundTransferStatus")
    original_total: Union[FinancialEventGroupOriginaltotal, Any] = Field(default=None, alias="OriginalTotal")
    converted_total: Union[FinancialEventGroupConvertedtotal, Any] = Field(default=None, alias="ConvertedTotal")
    fund_transfer_date: Union[str, Any] = Field(default=None, alias="FundTransferDate")
    trace_id: Union[str, Any] = Field(default=None, alias="TraceId")
    account_tail: Union[str, Any] = Field(default=None, alias="AccountTail")
    beginning_balance: Union[FinancialEventGroupBeginningbalance, Any] = Field(default=None, alias="BeginningBalance")
    financial_event_group_start: Union[str, Any] = Field(default=None, alias="FinancialEventGroupStart")
    financial_event_group_end: Union[str, Any] = Field(default=None, alias="FinancialEventGroupEnd")

class FinancialEventGroupListPayload(BaseModel):
    """Nested schema for FinancialEventGroupList.payload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    financial_event_group_list: Union[list[FinancialEventGroup], Any] = Field(default=None, alias="FinancialEventGroupList")
    next_token: Union[str, Any] = Field(default=None, alias="NextToken")

class FinancialEventGroupList(BaseModel):
    """Paginated list of financial event groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payload: Union[FinancialEventGroupListPayload, Any] = Field(default=None)

class FinancialEventsDebtrecoveryeventlistItemChargeinstrumentlistItemAmount(BaseModel):
    """Nested schema for FinancialEventsDebtrecoveryeventlistItemChargeinstrumentlistItem.Amount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventsDebtrecoveryeventlistItemChargeinstrumentlistItem(BaseModel):
    """Nested schema for FinancialEventsDebtrecoveryeventlistItem.ChargeInstrumentList_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: Union[str, Any] = Field(default=None, alias="Description")
    tail: Union[str, Any] = Field(default=None, alias="Tail")
    amount: Union[FinancialEventsDebtrecoveryeventlistItemChargeinstrumentlistItemAmount, Any] = Field(default=None, alias="Amount")

class FinancialEventsDebtrecoveryeventlistItemRecoveryamount(BaseModel):
    """Nested schema for FinancialEventsDebtrecoveryeventlistItem.RecoveryAmount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItemOriginalamount(BaseModel):
    """Nested schema for FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItem.OriginalAmount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItemRecoveryamount(BaseModel):
    """Nested schema for FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItem.RecoveryAmount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItem(BaseModel):
    """Nested schema for FinancialEventsDebtrecoveryeventlistItem.DebtRecoveryItemList_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    recovery_amount: Union[FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItemRecoveryamount, Any] = Field(default=None, alias="RecoveryAmount")
    original_amount: Union[FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItemOriginalamount, Any] = Field(default=None, alias="OriginalAmount")
    group_begin_date: Union[str, Any] = Field(default=None, alias="GroupBeginDate")
    group_end_date: Union[str, Any] = Field(default=None, alias="GroupEndDate")

class FinancialEventsDebtrecoveryeventlistItem(BaseModel):
    """Nested schema for FinancialEvents.DebtRecoveryEventList_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    debt_recovery_type: Union[str, Any] = Field(default=None, alias="DebtRecoveryType")
    recovery_amount: Union[FinancialEventsDebtrecoveryeventlistItemRecoveryamount, Any] = Field(default=None, alias="RecoveryAmount")
    debt_recovery_item_list: Union[list[FinancialEventsDebtrecoveryeventlistItemDebtrecoveryitemlistItem], Any] = Field(default=None, alias="DebtRecoveryItemList")
    charge_instrument_list: Union[list[FinancialEventsDebtrecoveryeventlistItemChargeinstrumentlistItem], Any] = Field(default=None, alias="ChargeInstrumentList")

class FinancialEventsServicefeeeventlistItemFeelistItemFeeamount(BaseModel):
    """Nested schema for FinancialEventsServicefeeeventlistItemFeelistItem.FeeAmount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="CurrencyCode")
    currency_amount: Union[float, Any] = Field(default=None, alias="CurrencyAmount")

class FinancialEventsServicefeeeventlistItemFeelistItem(BaseModel):
    """Nested schema for FinancialEventsServicefeeeventlistItem.FeeList_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fee_type: Union[str, Any] = Field(default=None, alias="FeeType")
    fee_amount: Union[FinancialEventsServicefeeeventlistItemFeelistItemFeeamount, Any] = Field(default=None, alias="FeeAmount")

class FinancialEventsServicefeeeventlistItem(BaseModel):
    """Nested schema for FinancialEvents.ServiceFeeEventList_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fee_list: Union[list[FinancialEventsServicefeeeventlistItemFeelistItem], Any] = Field(default=None, alias="FeeList")

class FinancialEvents(BaseModel):
    """A collection of financial events grouped by type"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    shipment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ShipmentEventList")
    shipment_settle_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ShipmentSettleEventList")
    refund_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="RefundEventList")
    guarantee_claim_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="GuaranteeClaimEventList")
    chargeback_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ChargebackEventList")
    charge_refund_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ChargeRefundEventList")
    pay_with_amazon_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="PayWithAmazonEventList")
    service_provider_credit_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ServiceProviderCreditEventList")
    retrocharge_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="RetrochargeEventList")
    rental_transaction_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="RentalTransactionEventList")
    product_ads_payment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ProductAdsPaymentEventList")
    service_fee_event_list: Union[list[FinancialEventsServicefeeeventlistItem], Any] = Field(default=None, alias="ServiceFeeEventList")
    seller_deal_payment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="SellerDealPaymentEventList")
    debt_recovery_event_list: Union[list[FinancialEventsDebtrecoveryeventlistItem], Any] = Field(default=None, alias="DebtRecoveryEventList")
    loan_servicing_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="LoanServicingEventList")
    adjustment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="AdjustmentEventList")
    safet_reimbursement_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="SAFETReimbursementEventList")
    seller_review_enrollment_payment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="SellerReviewEnrollmentPaymentEventList")
    fba_liquidation_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="FBALiquidationEventList")
    coupon_payment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="CouponPaymentEventList")
    imaging_services_fee_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ImagingServicesFeeEventList")
    network_commingling_transaction_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="NetworkComminglingTransactionEventList")
    affordability_expense_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="AffordabilityExpenseEventList")
    affordability_expense_reversal_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="AffordabilityExpenseReversalEventList")
    trial_shipment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="TrialShipmentEventList")
    tds_reimbursement_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="TDSReimbursementEventList")
    tax_withholding_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="TaxWithholdingEventList")
    removal_shipment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="RemovalShipmentEventList")
    removal_shipment_adjustment_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="RemovalShipmentAdjustmentEventList")
    value_added_service_charge_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="ValueAddedServiceChargeEventList")
    capacity_reservation_billing_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="CapacityReservationBillingEventList")
    failed_adhoc_disbursement_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="FailedAdhocDisbursementEventList")
    adhoc_disbursement_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="AdhocDisbursementEventList")
    performance_bond_refund_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="PerformanceBondRefundEventList")
    ebt_refund_reimbursement_only_event_list: Union[list[dict[str, Any]], Any] = Field(default=None, alias="EBTRefundReimbursementOnlyEventList")

class FinancialEventsResponsePayload(BaseModel):
    """Nested schema for FinancialEventsResponse.payload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    financial_events: Union[FinancialEvents, Any] = Field(default=None, alias="FinancialEvents")
    next_token: Union[str, Any] = Field(default=None, alias="NextToken")

class FinancialEventsResponse(BaseModel):
    """Response wrapper for financial events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payload: Union[FinancialEventsResponsePayload, Any] = Field(default=None)

class CatalogItemSummariesItemBrowseclassification(BaseModel):
    """Nested schema for CatalogItemSummariesItem.browseClassification"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    classification_id: Union[str, Any] = Field(default=None, alias="classificationId")

class CatalogItemSummariesItem(BaseModel):
    """Nested schema for CatalogItem.summaries_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    marketplace_id: Union[str, Any] = Field(default=None, alias="marketplaceId")
    adult_product: Union[bool, Any] = Field(default=None, alias="adultProduct")
    autographed: Union[bool, Any] = Field(default=None)
    brand: Union[str, Any] = Field(default=None)
    browse_classification: Union[CatalogItemSummariesItemBrowseclassification, Any] = Field(default=None, alias="browseClassification")
    color: Union[str, Any] = Field(default=None)
    item_classification: Union[str, Any] = Field(default=None, alias="itemClassification")
    item_name: Union[str, Any] = Field(default=None, alias="itemName")
    manufacturer: Union[str, Any] = Field(default=None)
    memorabilia: Union[bool, Any] = Field(default=None)
    model_number: Union[str, Any] = Field(default=None, alias="modelNumber")
    package_quantity: Union[int, Any] = Field(default=None, alias="packageQuantity")
    part_number: Union[str, Any] = Field(default=None, alias="partNumber")
    size: Union[str, Any] = Field(default=None)
    style: Union[str, Any] = Field(default=None)
    trade_in_eligible: Union[bool, Any] = Field(default=None, alias="tradeInEligible")
    website_display_group: Union[str, Any] = Field(default=None, alias="websiteDisplayGroup")
    website_display_group_name: Union[str, Any] = Field(default=None, alias="websiteDisplayGroupName")

class CatalogItem(BaseModel):
    """Amazon catalog item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    asin: Union[str, Any] = Field(default=None)
    attributes: Union[dict[str, Any], Any] = Field(default=None)
    classifications: Union[list[dict[str, Any]], Any] = Field(default=None)
    dimensions: Union[list[dict[str, Any]], Any] = Field(default=None)
    identifiers: Union[list[dict[str, Any]], Any] = Field(default=None)
    images: Union[list[dict[str, Any]], Any] = Field(default=None)
    product_types: Union[list[dict[str, Any]], Any] = Field(default=None, alias="productTypes")
    relationships: Union[list[dict[str, Any]], Any] = Field(default=None)
    sales_ranks: Union[list[dict[str, Any]], Any] = Field(default=None, alias="salesRanks")
    summaries: Union[list[CatalogItemSummariesItem], Any] = Field(default=None)
    vendor_details: Union[list[dict[str, Any]], Any] = Field(default=None, alias="vendorDetails")

class CatalogItemsListPagination(BaseModel):
    """Nested schema for CatalogItemsList.pagination"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None, alias="nextToken")
    previous_token: Union[str, Any] = Field(default=None, alias="previousToken")

class CatalogItemsListRefinementsClassificationsItem(BaseModel):
    """Nested schema for CatalogItemsListRefinements.classifications_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    number_of_results: Union[int, Any] = Field(default=None, alias="numberOfResults")
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    classification_id: Union[str, Any] = Field(default=None, alias="classificationId")

class CatalogItemsListRefinementsBrandsItem(BaseModel):
    """Nested schema for CatalogItemsListRefinements.brands_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    number_of_results: Union[int, Any] = Field(default=None, alias="numberOfResults")
    brand_name: Union[str, Any] = Field(default=None, alias="brandName")

class CatalogItemsListRefinements(BaseModel):
    """Nested schema for CatalogItemsList.refinements"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    brands: Union[list[CatalogItemsListRefinementsBrandsItem], Any] = Field(default=None)
    classifications: Union[list[CatalogItemsListRefinementsClassificationsItem], Any] = Field(default=None)

class CatalogItemsList(BaseModel):
    """Catalog items search results"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    number_of_results: Union[int, Any] = Field(default=None, alias="numberOfResults")
    pagination: Union[CatalogItemsListPagination, Any] = Field(default=None)
    refinements: Union[CatalogItemsListRefinements, Any] = Field(default=None)
    items: Union[list[CatalogItem], Any] = Field(default=None)

class Report(BaseModel):
    """Amazon SP-API report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    report_id: Union[str, Any] = Field(default=None, alias="reportId")
    report_type: Union[str, Any] = Field(default=None, alias="reportType")
    created_time: Union[str, Any] = Field(default=None, alias="createdTime")
    processing_status: Union[str, Any] = Field(default=None, alias="processingStatus")
    data_start_time: Union[str, Any] = Field(default=None, alias="dataStartTime")
    data_end_time: Union[str, Any] = Field(default=None, alias="dataEndTime")
    report_schedule_id: Union[str, Any] = Field(default=None, alias="reportScheduleId")
    processing_start_time: Union[str, Any] = Field(default=None, alias="processingStartTime")
    processing_end_time: Union[str, Any] = Field(default=None, alias="processingEndTime")
    report_document_id: Union[str, Any] = Field(default=None, alias="reportDocumentId")
    marketplace_ids: Union[list[str], Any] = Field(default=None, alias="marketplaceIds")

class ReportsList(BaseModel):
    """Paginated list of reports"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reports: Union[list[Report], Any] = Field(default=None)
    next_token: Union[str, Any] = Field(default=None, alias="nextToken")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class OrdersListResultMeta(BaseModel):
    """Metadata for orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None)

class OrderItemsListResultMeta(BaseModel):
    """Metadata for order_items.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None)

class ListFinancialEventGroupsListResultMeta(BaseModel):
    """Metadata for list_financial_event_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None)

class ListFinancialEventsListResultMeta(BaseModel):
    """Metadata for list_financial_events.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None)

class CatalogItemsListResultMeta(BaseModel):
    """Metadata for catalog_items.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None)
    number_of_results: Union[int, Any] = Field(default=None)

class ReportsListResultMeta(BaseModel):
    """Metadata for reports.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: Union[str, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class AmazonSellerPartnerCheckResult(BaseModel):
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


class AmazonSellerPartnerExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AmazonSellerPartnerExecuteResultWithMeta(AmazonSellerPartnerExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class OrdersSearchData(BaseModel):
    """Search result data for orders entity."""
    model_config = ConfigDict(extra="allow")

    amazon_order_id: str | None = None
    """Unique identifier for the Amazon order"""
    automated_shipping_settings: dict[str, Any] | None = None
    """Settings related to automated shipping processes"""
    buyer_info: dict[str, Any] | None = None
    """Information about the buyer"""
    default_ship_from_location_address: dict[str, Any] | None = None
    """The default address from which orders are shipped"""
    earliest_delivery_date: str | None = None
    """Earliest estimated delivery date of the order"""
    earliest_ship_date: str | None = None
    """Earliest shipment date for the order"""
    fulfillment_channel: str | None = None
    """Channel through which the order is fulfilled"""
    has_regulated_items: bool | None = None
    """Indicates if the order has regulated items"""
    is_access_point_order: bool | None = None
    """Indicates if the order is an Amazon Hub Counter order"""
    is_business_order: bool | None = None
    """Indicates if the order is a business order"""
    is_global_express_enabled: bool | None = None
    """Indicates if global express is enabled for the order"""
    is_ispu: bool | None = None
    """Indicates if the order is for In-Store Pickup"""
    is_premium_order: bool | None = None
    """Indicates if the order is a premium order"""
    is_prime: bool | None = None
    """Indicates if the order is a Prime order"""
    is_replacement_order: str | None = None
    """Indicates if the order is a replacement order"""
    is_sold_by_ab: bool | None = None
    """Indicates if the order is sold by Amazon Business"""
    last_update_date: str | None = None
    """Date and time when the order was last updated"""
    latest_delivery_date: str | None = None
    """Latest estimated delivery date of the order"""
    latest_ship_date: str | None = None
    """Latest shipment date for the order"""
    marketplace_id: str | None = None
    """Identifier for the marketplace where the order was placed"""
    number_of_items_shipped: int | None = None
    """Number of items shipped in the order"""
    number_of_items_unshipped: int | None = None
    """Number of items yet to be shipped in the order"""
    order_status: str | None = None
    """Status of the order"""
    order_total: dict[str, Any] | None = None
    """Total amount of the order"""
    order_type: str | None = None
    """Type of the order"""
    payment_method: str | None = None
    """Payment method used for the order"""
    payment_method_details: list[Any] | None = None
    """Details of the payment method used for the order"""
    purchase_date: str | None = None
    """Date and time when the order was purchased"""
    sales_channel: str | None = None
    """Channel through which the order was sold"""
    seller_order_id: str | None = None
    """Unique identifier given by the seller for the order"""
    ship_service_level: str | None = None
    """Service level for shipping the order"""
    shipment_service_level_category: str | None = None
    """Service level category for shipping the order"""
    shipping_address: dict[str, Any] | None = None
    """The address to which the order will be shipped"""
    seller_id: str | None = None
    """Identifier for the seller associated with the order"""


class OrderItemsSearchData(BaseModel):
    """Search result data for order_items entity."""
    model_config = ConfigDict(extra="allow")

    asin: str | None = None
    """Amazon Standard Identification Number of the product"""
    amazon_order_id: str | None = None
    """ID of the Amazon order"""
    buyer_info: dict[str, Any] | None = None
    """Information about the buyer"""
    buyer_requested_cancel: dict[str, Any] | None = None
    """Information about buyer's request for cancellation"""
    cod_fee: dict[str, Any] | None = None
    """Cash on delivery fee"""
    cod_fee_discount: dict[str, Any] | None = None
    """Discount on cash on delivery fee"""
    condition_id: str | None = None
    """Condition ID of the product"""
    condition_note: str | None = None
    """Additional notes on the condition of the product"""
    condition_subtype_id: str | None = None
    """Subtype ID of the product condition"""
    deemed_reseller_category: str | None = None
    """Category indicating if the seller is considered a reseller"""
    ioss_number: str | None = None
    """Import One Stop Shop number"""
    is_gift: str | None = None
    """Flag indicating if the order is a gift"""
    is_transparency: bool | None = None
    """Flag indicating if transparency is applied"""
    item_price: dict[str, Any] | None = None
    """Price of the item"""
    item_tax: dict[str, Any] | None = None
    """Tax applied on the item"""
    last_update_date: str | None = None
    """Date and time of the last update"""
    order_item_id: str | None = None
    """ID of the order item"""
    points_granted: dict[str, Any] | None = None
    """Points granted for the purchase"""
    price_designation: str | None = None
    """Designation of the price"""
    product_info: dict[str, Any] | None = None
    """Information about the product"""
    promotion_discount: dict[str, Any] | None = None
    """Discount applied due to promotion"""
    promotion_discount_tax: dict[str, Any] | None = None
    """Tax applied on the promotion discount"""
    promotion_ids: list[Any] | None = None
    """IDs of promotions applied"""
    quantity_ordered: int | None = None
    """Quantity of the item ordered"""
    quantity_shipped: int | None = None
    """Quantity of the item shipped"""
    scheduled_delivery_end_date: str | None = None
    """End date for scheduled delivery"""
    scheduled_delivery_start_date: str | None = None
    """Start date for scheduled delivery"""
    seller_sku: str | None = None
    """SKU of the seller"""
    serial_number_required: bool | None = None
    """Flag indicating if serial number is required"""
    serial_numbers: list[Any] | None = None
    """List of serial numbers"""
    shipping_discount: dict[str, Any] | None = None
    """Discount applied on shipping"""
    shipping_discount_tax: dict[str, Any] | None = None
    """Tax applied on the shipping discount"""
    shipping_price: dict[str, Any] | None = None
    """Price of shipping"""
    shipping_tax: dict[str, Any] | None = None
    """Tax applied on shipping"""
    store_chain_store_id: str | None = None
    """ID of the store chain"""
    tax_collection: dict[str, Any] | None = None
    """Information about tax collection"""
    title: str | None = None
    """Title of the product"""


class ListFinancialEventGroupsSearchData(BaseModel):
    """Search result data for list_financial_event_groups entity."""
    model_config = ConfigDict(extra="allow")

    account_tail: str | None = None
    """The last digits of the account number"""
    beginning_balance: dict[str, Any] | None = None
    """Beginning balance"""
    converted_total: dict[str, Any] | None = None
    """Converted total"""
    financial_event_group_end: str | None = None
    """End datetime of the financial event group"""
    financial_event_group_id: str | None = None
    """Unique identifier for the financial event group"""
    financial_event_group_start: str | None = None
    """Start datetime of the financial event group"""
    fund_transfer_date: str | None = None
    """Date the fund transfer occurred"""
    fund_transfer_status: str | None = None
    """Status of the fund transfer"""
    original_total: dict[str, Any] | None = None
    """Original total amount"""
    processing_status: str | None = None
    """Processing status of the financial event group"""
    trace_id: str | None = None
    """Unique identifier for tracing"""


class ListFinancialEventsSearchData(BaseModel):
    """Search result data for list_financial_events entity."""
    model_config = ConfigDict(extra="allow")

    adhoc_disbursement_event_list: list[Any] | None = None
    """List of adhoc disbursement events"""
    adjustment_event_list: list[Any] | None = None
    """List of adjustment events"""
    affordability_expense_event_list: list[Any] | None = None
    """List of affordability expense events"""
    affordability_expense_reversal_event_list: list[Any] | None = None
    """List of affordability expense reversal events"""
    capacity_reservation_billing_event_list: list[Any] | None = None
    """List of capacity reservation billing events"""
    charge_refund_event_list: list[Any] | None = None
    """List of charge refund events"""
    chargeback_event_list: list[Any] | None = None
    """List of chargeback events"""
    coupon_payment_event_list: list[Any] | None = None
    """List of coupon payment events"""
    debt_recovery_event_list: list[Any] | None = None
    """List of debt recovery events"""
    fba_liquidation_event_list: list[Any] | None = None
    """List of FBA liquidation events"""
    failed_adhoc_disbursement_event_list: list[Any] | None = None
    """List of failed adhoc disbursement events"""
    guarantee_claim_event_list: list[Any] | None = None
    """List of guarantee claim events"""
    imaging_services_fee_event_list: list[Any] | None = None
    """List of imaging services fee events"""
    loan_servicing_event_list: list[Any] | None = None
    """List of loan servicing events"""
    network_commingling_transaction_event_list: list[Any] | None = None
    """List of network commingling events"""
    pay_with_amazon_event_list: list[Any] | None = None
    """List of Pay with Amazon events"""
    performance_bond_refund_event_list: list[Any] | None = None
    """List of performance bond refund events"""
    posted_before: str | None = None
    """Date filter for events posted before"""
    product_ads_payment_event_list: list[Any] | None = None
    """List of product ads payment events"""
    refund_event_list: list[Any] | None = None
    """List of refund events"""
    removal_shipment_adjustment_event_list: list[Any] | None = None
    """List of removal shipment adjustment events"""
    removal_shipment_event_list: list[Any] | None = None
    """List of removal shipment events"""
    rental_transaction_event_list: list[Any] | None = None
    """List of rental transaction events"""
    retrocharge_event_list: list[Any] | None = None
    """List of retrocharge events"""
    safet_reimbursement_event_list: list[Any] | None = None
    """List of SAFET reimbursement events"""
    seller_deal_payment_event_list: list[Any] | None = None
    """List of seller deal payment events"""
    seller_review_enrollment_payment_event_list: list[Any] | None = None
    """List of seller review enrollment events"""
    service_fee_event_list: list[Any] | None = None
    """List of service fee events"""
    service_provider_credit_event_list: list[Any] | None = None
    """List of service provider credit events"""
    shipment_event_list: list[Any] | None = None
    """List of shipment events"""
    shipment_settle_event_list: list[Any] | None = None
    """List of shipment settlement events"""
    tds_reimbursement_event_list: list[Any] | None = None
    """List of TDS reimbursement events"""
    tax_withholding_event_list: list[Any] | None = None
    """List of tax withholding events"""
    trial_shipment_event_list: list[Any] | None = None
    """List of trial shipment events"""
    value_added_service_charge_event_list: list[Any] | None = None
    """List of value-added service charge events"""


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

OrdersSearchResult = AirbyteSearchResult[OrdersSearchData]
"""Search result type for orders entity."""

OrderItemsSearchResult = AirbyteSearchResult[OrderItemsSearchData]
"""Search result type for order_items entity."""

ListFinancialEventGroupsSearchResult = AirbyteSearchResult[ListFinancialEventGroupsSearchData]
"""Search result type for list_financial_event_groups entity."""

ListFinancialEventsSearchResult = AirbyteSearchResult[ListFinancialEventsSearchData]
"""Search result type for list_financial_events entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

OrdersListResult = AmazonSellerPartnerExecuteResultWithMeta[list[Order], OrdersListResultMeta]
"""Result type for orders.list operation with data and metadata."""

OrderItemsListResult = AmazonSellerPartnerExecuteResultWithMeta[list[OrderItem], OrderItemsListResultMeta]
"""Result type for order_items.list operation with data and metadata."""

ListFinancialEventGroupsListResult = AmazonSellerPartnerExecuteResultWithMeta[list[FinancialEventGroup], ListFinancialEventGroupsListResultMeta]
"""Result type for list_financial_event_groups.list operation with data and metadata."""

ListFinancialEventsListResult = AmazonSellerPartnerExecuteResultWithMeta[FinancialEvents, ListFinancialEventsListResultMeta]
"""Result type for list_financial_events.list operation with data and metadata."""

CatalogItemsListResult = AmazonSellerPartnerExecuteResultWithMeta[list[CatalogItem], CatalogItemsListResultMeta]
"""Result type for catalog_items.list operation with data and metadata."""

ReportsListResult = AmazonSellerPartnerExecuteResultWithMeta[list[Report], ReportsListResultMeta]
"""Result type for reports.list operation with data and metadata."""

