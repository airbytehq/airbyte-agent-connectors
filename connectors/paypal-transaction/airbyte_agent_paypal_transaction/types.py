"""
Type definitions for paypal-transaction connector.
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

class SearchInvoicesListParamsCreationDateRange(TypedDict):
    """Filter by invoice creation date range."""
    start: NotRequired[str]
    end: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class BalancesListParams(TypedDict):
    """Parameters for balances.list operation"""
    as_of_time: NotRequired[str]
    currency_code: NotRequired[str]

class TransactionsListParams(TypedDict):
    """Parameters for transactions.list operation"""
    start_date: str
    end_date: str
    transaction_id: NotRequired[str]
    transaction_type: NotRequired[str]
    transaction_status: NotRequired[str]
    transaction_currency: NotRequired[str]
    fields: NotRequired[str]
    page_size: NotRequired[int]
    page: NotRequired[int]
    balance_affecting_records_only: NotRequired[str]

class ListPaymentsListParams(TypedDict):
    """Parameters for list_payments.list operation"""
    start_time: NotRequired[str]
    end_time: NotRequired[str]
    count: NotRequired[int]
    start_id: NotRequired[str]

class ListDisputesListParams(TypedDict):
    """Parameters for list_disputes.list operation"""
    update_time_after: NotRequired[str]
    update_time_before: NotRequired[str]
    page_size: NotRequired[int]
    next_page_token: NotRequired[str]

class ListProductsListParams(TypedDict):
    """Parameters for list_products.list operation"""
    page_size: NotRequired[int]
    page: NotRequired[int]

class ShowProductDetailsGetParams(TypedDict):
    """Parameters for show_product_details.get operation"""
    id: str

class SearchInvoicesListParams(TypedDict):
    """Parameters for search_invoices.list operation"""
    creation_date_range: NotRequired[SearchInvoicesListParamsCreationDateRange]
    page_size: NotRequired[int]
    page: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== TRANSACTIONS SEARCH TYPES =====

class TransactionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering transactions search queries."""
    auction_info: dict[str, Any] | None
    """Information related to an auction"""
    cart_info: dict[str, Any] | None
    """Details of items in the cart"""
    incentive_info: dict[str, Any] | None
    """Details of any incentives applied"""
    payer_info: dict[str, Any] | None
    """Information about the payer"""
    shipping_info: dict[str, Any] | None
    """Shipping information"""
    store_info: dict[str, Any] | None
    """Information about the store"""
    transaction_id: str | None
    """Unique ID of the transaction"""
    transaction_info: dict[str, Any] | None
    """Detailed information about the transaction"""
    transaction_initiation_date: str | None
    """Date and time when the transaction was initiated"""
    transaction_updated_date: str | None
    """Date and time when the transaction was last updated"""


class TransactionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    auction_info: list[dict[str, Any]]
    """Information related to an auction"""
    cart_info: list[dict[str, Any]]
    """Details of items in the cart"""
    incentive_info: list[dict[str, Any]]
    """Details of any incentives applied"""
    payer_info: list[dict[str, Any]]
    """Information about the payer"""
    shipping_info: list[dict[str, Any]]
    """Shipping information"""
    store_info: list[dict[str, Any]]
    """Information about the store"""
    transaction_id: list[str]
    """Unique ID of the transaction"""
    transaction_info: list[dict[str, Any]]
    """Detailed information about the transaction"""
    transaction_initiation_date: list[str]
    """Date and time when the transaction was initiated"""
    transaction_updated_date: list[str]
    """Date and time when the transaction was last updated"""


class TransactionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    auction_info: Any
    """Information related to an auction"""
    cart_info: Any
    """Details of items in the cart"""
    incentive_info: Any
    """Details of any incentives applied"""
    payer_info: Any
    """Information about the payer"""
    shipping_info: Any
    """Shipping information"""
    store_info: Any
    """Information about the store"""
    transaction_id: Any
    """Unique ID of the transaction"""
    transaction_info: Any
    """Detailed information about the transaction"""
    transaction_initiation_date: Any
    """Date and time when the transaction was initiated"""
    transaction_updated_date: Any
    """Date and time when the transaction was last updated"""


class TransactionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    auction_info: str
    """Information related to an auction"""
    cart_info: str
    """Details of items in the cart"""
    incentive_info: str
    """Details of any incentives applied"""
    payer_info: str
    """Information about the payer"""
    shipping_info: str
    """Shipping information"""
    store_info: str
    """Information about the store"""
    transaction_id: str
    """Unique ID of the transaction"""
    transaction_info: str
    """Detailed information about the transaction"""
    transaction_initiation_date: str
    """Date and time when the transaction was initiated"""
    transaction_updated_date: str
    """Date and time when the transaction was last updated"""


class TransactionsSortFilter(TypedDict, total=False):
    """Available fields for sorting transactions search results."""
    auction_info: AirbyteSortOrder
    """Information related to an auction"""
    cart_info: AirbyteSortOrder
    """Details of items in the cart"""
    incentive_info: AirbyteSortOrder
    """Details of any incentives applied"""
    payer_info: AirbyteSortOrder
    """Information about the payer"""
    shipping_info: AirbyteSortOrder
    """Shipping information"""
    store_info: AirbyteSortOrder
    """Information about the store"""
    transaction_id: AirbyteSortOrder
    """Unique ID of the transaction"""
    transaction_info: AirbyteSortOrder
    """Detailed information about the transaction"""
    transaction_initiation_date: AirbyteSortOrder
    """Date and time when the transaction was initiated"""
    transaction_updated_date: AirbyteSortOrder
    """Date and time when the transaction was last updated"""


# Entity-specific condition types for transactions
class TransactionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TransactionsSearchFilter


class TransactionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TransactionsSearchFilter


class TransactionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TransactionsSearchFilter


class TransactionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TransactionsSearchFilter


class TransactionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TransactionsSearchFilter


class TransactionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TransactionsSearchFilter


class TransactionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TransactionsStringFilter


class TransactionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TransactionsStringFilter


class TransactionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TransactionsStringFilter


class TransactionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TransactionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TransactionsInCondition = TypedDict("TransactionsInCondition", {"in": TransactionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TransactionsNotCondition = TypedDict("TransactionsNotCondition", {"not": "TransactionsCondition"}, total=False)
"""Negates the nested condition."""

TransactionsAndCondition = TypedDict("TransactionsAndCondition", {"and": "list[TransactionsCondition]"}, total=False)
"""True if all nested conditions are true."""

TransactionsOrCondition = TypedDict("TransactionsOrCondition", {"or": "list[TransactionsCondition]"}, total=False)
"""True if any nested condition is true."""

TransactionsAnyCondition = TypedDict("TransactionsAnyCondition", {"any": TransactionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all transactions condition types
TransactionsCondition = (
    TransactionsEqCondition
    | TransactionsNeqCondition
    | TransactionsGtCondition
    | TransactionsGteCondition
    | TransactionsLtCondition
    | TransactionsLteCondition
    | TransactionsInCondition
    | TransactionsLikeCondition
    | TransactionsFuzzyCondition
    | TransactionsKeywordCondition
    | TransactionsContainsCondition
    | TransactionsNotCondition
    | TransactionsAndCondition
    | TransactionsOrCondition
    | TransactionsAnyCondition
)


class TransactionsSearchQuery(TypedDict, total=False):
    """Search query for transactions entity."""
    filter: TransactionsCondition
    sort: list[TransactionsSortFilter]


# ===== BALANCES SEARCH TYPES =====

class BalancesSearchFilter(TypedDict, total=False):
    """Available fields for filtering balances search queries."""
    account_id: str | None
    """The unique identifier of the account."""
    as_of_time: str | None
    """The timestamp when the balances data was reported."""
    balances: list[Any] | None
    """Object containing information about the account balances."""
    last_refresh_time: str | None
    """The timestamp when the balances data was last refreshed."""


class BalancesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_id: list[str]
    """The unique identifier of the account."""
    as_of_time: list[str]
    """The timestamp when the balances data was reported."""
    balances: list[list[Any]]
    """Object containing information about the account balances."""
    last_refresh_time: list[str]
    """The timestamp when the balances data was last refreshed."""


class BalancesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_id: Any
    """The unique identifier of the account."""
    as_of_time: Any
    """The timestamp when the balances data was reported."""
    balances: Any
    """Object containing information about the account balances."""
    last_refresh_time: Any
    """The timestamp when the balances data was last refreshed."""


class BalancesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_id: str
    """The unique identifier of the account."""
    as_of_time: str
    """The timestamp when the balances data was reported."""
    balances: str
    """Object containing information about the account balances."""
    last_refresh_time: str
    """The timestamp when the balances data was last refreshed."""


class BalancesSortFilter(TypedDict, total=False):
    """Available fields for sorting balances search results."""
    account_id: AirbyteSortOrder
    """The unique identifier of the account."""
    as_of_time: AirbyteSortOrder
    """The timestamp when the balances data was reported."""
    balances: AirbyteSortOrder
    """Object containing information about the account balances."""
    last_refresh_time: AirbyteSortOrder
    """The timestamp when the balances data was last refreshed."""


# Entity-specific condition types for balances
class BalancesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BalancesSearchFilter


class BalancesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BalancesSearchFilter


class BalancesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BalancesSearchFilter


class BalancesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BalancesSearchFilter


class BalancesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BalancesSearchFilter


class BalancesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BalancesSearchFilter


class BalancesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BalancesStringFilter


class BalancesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BalancesStringFilter


class BalancesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BalancesStringFilter


class BalancesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BalancesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BalancesInCondition = TypedDict("BalancesInCondition", {"in": BalancesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BalancesNotCondition = TypedDict("BalancesNotCondition", {"not": "BalancesCondition"}, total=False)
"""Negates the nested condition."""

BalancesAndCondition = TypedDict("BalancesAndCondition", {"and": "list[BalancesCondition]"}, total=False)
"""True if all nested conditions are true."""

BalancesOrCondition = TypedDict("BalancesOrCondition", {"or": "list[BalancesCondition]"}, total=False)
"""True if any nested condition is true."""

BalancesAnyCondition = TypedDict("BalancesAnyCondition", {"any": BalancesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all balances condition types
BalancesCondition = (
    BalancesEqCondition
    | BalancesNeqCondition
    | BalancesGtCondition
    | BalancesGteCondition
    | BalancesLtCondition
    | BalancesLteCondition
    | BalancesInCondition
    | BalancesLikeCondition
    | BalancesFuzzyCondition
    | BalancesKeywordCondition
    | BalancesContainsCondition
    | BalancesNotCondition
    | BalancesAndCondition
    | BalancesOrCondition
    | BalancesAnyCondition
)


class BalancesSearchQuery(TypedDict, total=False):
    """Search query for balances entity."""
    filter: BalancesCondition
    sort: list[BalancesSortFilter]


# ===== LIST_PRODUCTS SEARCH TYPES =====

class ListProductsSearchFilter(TypedDict, total=False):
    """Available fields for filtering list_products search queries."""
    create_time: str | None
    """The time when the product was created"""
    description: str | None
    """Detailed information or features of the product"""
    id: str | None
    """Unique identifier for the product"""
    links: list[Any] | None
    """List of links related to the fetched products."""
    name: str | None
    """The name or title of the product"""


class ListProductsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    create_time: list[str]
    """The time when the product was created"""
    description: list[str]
    """Detailed information or features of the product"""
    id: list[str]
    """Unique identifier for the product"""
    links: list[list[Any]]
    """List of links related to the fetched products."""
    name: list[str]
    """The name or title of the product"""


class ListProductsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    create_time: Any
    """The time when the product was created"""
    description: Any
    """Detailed information or features of the product"""
    id: Any
    """Unique identifier for the product"""
    links: Any
    """List of links related to the fetched products."""
    name: Any
    """The name or title of the product"""


class ListProductsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    create_time: str
    """The time when the product was created"""
    description: str
    """Detailed information or features of the product"""
    id: str
    """Unique identifier for the product"""
    links: str
    """List of links related to the fetched products."""
    name: str
    """The name or title of the product"""


class ListProductsSortFilter(TypedDict, total=False):
    """Available fields for sorting list_products search results."""
    create_time: AirbyteSortOrder
    """The time when the product was created"""
    description: AirbyteSortOrder
    """Detailed information or features of the product"""
    id: AirbyteSortOrder
    """Unique identifier for the product"""
    links: AirbyteSortOrder
    """List of links related to the fetched products."""
    name: AirbyteSortOrder
    """The name or title of the product"""


# Entity-specific condition types for list_products
class ListProductsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListProductsSearchFilter


class ListProductsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListProductsSearchFilter


class ListProductsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListProductsSearchFilter


class ListProductsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListProductsSearchFilter


class ListProductsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListProductsSearchFilter


class ListProductsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListProductsSearchFilter


class ListProductsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ListProductsStringFilter


class ListProductsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListProductsStringFilter


class ListProductsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListProductsStringFilter


class ListProductsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ListProductsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListProductsInCondition = TypedDict("ListProductsInCondition", {"in": ListProductsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListProductsNotCondition = TypedDict("ListProductsNotCondition", {"not": "ListProductsCondition"}, total=False)
"""Negates the nested condition."""

ListProductsAndCondition = TypedDict("ListProductsAndCondition", {"and": "list[ListProductsCondition]"}, total=False)
"""True if all nested conditions are true."""

ListProductsOrCondition = TypedDict("ListProductsOrCondition", {"or": "list[ListProductsCondition]"}, total=False)
"""True if any nested condition is true."""

ListProductsAnyCondition = TypedDict("ListProductsAnyCondition", {"any": ListProductsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all list_products condition types
ListProductsCondition = (
    ListProductsEqCondition
    | ListProductsNeqCondition
    | ListProductsGtCondition
    | ListProductsGteCondition
    | ListProductsLtCondition
    | ListProductsLteCondition
    | ListProductsInCondition
    | ListProductsLikeCondition
    | ListProductsFuzzyCondition
    | ListProductsKeywordCondition
    | ListProductsContainsCondition
    | ListProductsNotCondition
    | ListProductsAndCondition
    | ListProductsOrCondition
    | ListProductsAnyCondition
)


class ListProductsSearchQuery(TypedDict, total=False):
    """Search query for list_products entity."""
    filter: ListProductsCondition
    sort: list[ListProductsSortFilter]


# ===== SHOW_PRODUCT_DETAILS SEARCH TYPES =====

class ShowProductDetailsSearchFilter(TypedDict, total=False):
    """Available fields for filtering show_product_details search queries."""
    category: str | None
    """The category to which the product belongs"""
    create_time: str | None
    """The date and time when the product was created"""
    description: str | None
    """The detailed description of the product"""
    home_url: str | None
    """The URL for the home page of the product"""
    id: str | None
    """The unique identifier for the product"""
    image_url: str | None
    """The URL to the image representing the product"""
    links: list[Any] | None
    """Contains links related to the product details."""
    name: str | None
    """The name of the product"""
    type_: str | None
    """The type or category of the product"""
    update_time: str | None
    """The date and time when the product was last updated"""


class ShowProductDetailsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    category: list[str]
    """The category to which the product belongs"""
    create_time: list[str]
    """The date and time when the product was created"""
    description: list[str]
    """The detailed description of the product"""
    home_url: list[str]
    """The URL for the home page of the product"""
    id: list[str]
    """The unique identifier for the product"""
    image_url: list[str]
    """The URL to the image representing the product"""
    links: list[list[Any]]
    """Contains links related to the product details."""
    name: list[str]
    """The name of the product"""
    type_: list[str]
    """The type or category of the product"""
    update_time: list[str]
    """The date and time when the product was last updated"""


class ShowProductDetailsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    category: Any
    """The category to which the product belongs"""
    create_time: Any
    """The date and time when the product was created"""
    description: Any
    """The detailed description of the product"""
    home_url: Any
    """The URL for the home page of the product"""
    id: Any
    """The unique identifier for the product"""
    image_url: Any
    """The URL to the image representing the product"""
    links: Any
    """Contains links related to the product details."""
    name: Any
    """The name of the product"""
    type_: Any
    """The type or category of the product"""
    update_time: Any
    """The date and time when the product was last updated"""


class ShowProductDetailsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    category: str
    """The category to which the product belongs"""
    create_time: str
    """The date and time when the product was created"""
    description: str
    """The detailed description of the product"""
    home_url: str
    """The URL for the home page of the product"""
    id: str
    """The unique identifier for the product"""
    image_url: str
    """The URL to the image representing the product"""
    links: str
    """Contains links related to the product details."""
    name: str
    """The name of the product"""
    type_: str
    """The type or category of the product"""
    update_time: str
    """The date and time when the product was last updated"""


class ShowProductDetailsSortFilter(TypedDict, total=False):
    """Available fields for sorting show_product_details search results."""
    category: AirbyteSortOrder
    """The category to which the product belongs"""
    create_time: AirbyteSortOrder
    """The date and time when the product was created"""
    description: AirbyteSortOrder
    """The detailed description of the product"""
    home_url: AirbyteSortOrder
    """The URL for the home page of the product"""
    id: AirbyteSortOrder
    """The unique identifier for the product"""
    image_url: AirbyteSortOrder
    """The URL to the image representing the product"""
    links: AirbyteSortOrder
    """Contains links related to the product details."""
    name: AirbyteSortOrder
    """The name of the product"""
    type_: AirbyteSortOrder
    """The type or category of the product"""
    update_time: AirbyteSortOrder
    """The date and time when the product was last updated"""


# Entity-specific condition types for show_product_details
class ShowProductDetailsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ShowProductDetailsSearchFilter


class ShowProductDetailsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ShowProductDetailsSearchFilter


class ShowProductDetailsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ShowProductDetailsSearchFilter


class ShowProductDetailsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ShowProductDetailsSearchFilter


class ShowProductDetailsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ShowProductDetailsSearchFilter


class ShowProductDetailsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ShowProductDetailsSearchFilter


class ShowProductDetailsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ShowProductDetailsStringFilter


class ShowProductDetailsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ShowProductDetailsStringFilter


class ShowProductDetailsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ShowProductDetailsStringFilter


class ShowProductDetailsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ShowProductDetailsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ShowProductDetailsInCondition = TypedDict("ShowProductDetailsInCondition", {"in": ShowProductDetailsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ShowProductDetailsNotCondition = TypedDict("ShowProductDetailsNotCondition", {"not": "ShowProductDetailsCondition"}, total=False)
"""Negates the nested condition."""

ShowProductDetailsAndCondition = TypedDict("ShowProductDetailsAndCondition", {"and": "list[ShowProductDetailsCondition]"}, total=False)
"""True if all nested conditions are true."""

ShowProductDetailsOrCondition = TypedDict("ShowProductDetailsOrCondition", {"or": "list[ShowProductDetailsCondition]"}, total=False)
"""True if any nested condition is true."""

ShowProductDetailsAnyCondition = TypedDict("ShowProductDetailsAnyCondition", {"any": ShowProductDetailsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all show_product_details condition types
ShowProductDetailsCondition = (
    ShowProductDetailsEqCondition
    | ShowProductDetailsNeqCondition
    | ShowProductDetailsGtCondition
    | ShowProductDetailsGteCondition
    | ShowProductDetailsLtCondition
    | ShowProductDetailsLteCondition
    | ShowProductDetailsInCondition
    | ShowProductDetailsLikeCondition
    | ShowProductDetailsFuzzyCondition
    | ShowProductDetailsKeywordCondition
    | ShowProductDetailsContainsCondition
    | ShowProductDetailsNotCondition
    | ShowProductDetailsAndCondition
    | ShowProductDetailsOrCondition
    | ShowProductDetailsAnyCondition
)


class ShowProductDetailsSearchQuery(TypedDict, total=False):
    """Search query for show_product_details entity."""
    filter: ShowProductDetailsCondition
    sort: list[ShowProductDetailsSortFilter]


# ===== LIST_DISPUTES SEARCH TYPES =====

class ListDisputesSearchFilter(TypedDict, total=False):
    """Available fields for filtering list_disputes search queries."""
    create_time: str | None
    """The timestamp when the dispute was created."""
    dispute_amount: dict[str, Any] | None
    """Details about the disputed amount."""
    dispute_channel: str | None
    """The channel through which the dispute was initiated."""
    dispute_id: str | None
    """The unique identifier for the dispute."""
    dispute_life_cycle_stage: str | None
    """The stage in the life cycle of the dispute."""
    dispute_state: str | None
    """The current state of the dispute."""
    disputed_transactions: list[Any] | None
    """Details of transactions involved in the dispute."""
    links: list[Any] | None
    """Links related to the dispute."""
    outcome: str | None
    """The outcome of the dispute resolution."""
    reason: str | None
    """The reason for the dispute."""
    status: str | None
    """The current status of the dispute."""
    update_time: str | None
    """The timestamp when the dispute was last updated."""
    updated_time_cut: str | None
    """The cut-off timestamp for the last update."""


class ListDisputesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    create_time: list[str]
    """The timestamp when the dispute was created."""
    dispute_amount: list[dict[str, Any]]
    """Details about the disputed amount."""
    dispute_channel: list[str]
    """The channel through which the dispute was initiated."""
    dispute_id: list[str]
    """The unique identifier for the dispute."""
    dispute_life_cycle_stage: list[str]
    """The stage in the life cycle of the dispute."""
    dispute_state: list[str]
    """The current state of the dispute."""
    disputed_transactions: list[list[Any]]
    """Details of transactions involved in the dispute."""
    links: list[list[Any]]
    """Links related to the dispute."""
    outcome: list[str]
    """The outcome of the dispute resolution."""
    reason: list[str]
    """The reason for the dispute."""
    status: list[str]
    """The current status of the dispute."""
    update_time: list[str]
    """The timestamp when the dispute was last updated."""
    updated_time_cut: list[str]
    """The cut-off timestamp for the last update."""


class ListDisputesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    create_time: Any
    """The timestamp when the dispute was created."""
    dispute_amount: Any
    """Details about the disputed amount."""
    dispute_channel: Any
    """The channel through which the dispute was initiated."""
    dispute_id: Any
    """The unique identifier for the dispute."""
    dispute_life_cycle_stage: Any
    """The stage in the life cycle of the dispute."""
    dispute_state: Any
    """The current state of the dispute."""
    disputed_transactions: Any
    """Details of transactions involved in the dispute."""
    links: Any
    """Links related to the dispute."""
    outcome: Any
    """The outcome of the dispute resolution."""
    reason: Any
    """The reason for the dispute."""
    status: Any
    """The current status of the dispute."""
    update_time: Any
    """The timestamp when the dispute was last updated."""
    updated_time_cut: Any
    """The cut-off timestamp for the last update."""


class ListDisputesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    create_time: str
    """The timestamp when the dispute was created."""
    dispute_amount: str
    """Details about the disputed amount."""
    dispute_channel: str
    """The channel through which the dispute was initiated."""
    dispute_id: str
    """The unique identifier for the dispute."""
    dispute_life_cycle_stage: str
    """The stage in the life cycle of the dispute."""
    dispute_state: str
    """The current state of the dispute."""
    disputed_transactions: str
    """Details of transactions involved in the dispute."""
    links: str
    """Links related to the dispute."""
    outcome: str
    """The outcome of the dispute resolution."""
    reason: str
    """The reason for the dispute."""
    status: str
    """The current status of the dispute."""
    update_time: str
    """The timestamp when the dispute was last updated."""
    updated_time_cut: str
    """The cut-off timestamp for the last update."""


class ListDisputesSortFilter(TypedDict, total=False):
    """Available fields for sorting list_disputes search results."""
    create_time: AirbyteSortOrder
    """The timestamp when the dispute was created."""
    dispute_amount: AirbyteSortOrder
    """Details about the disputed amount."""
    dispute_channel: AirbyteSortOrder
    """The channel through which the dispute was initiated."""
    dispute_id: AirbyteSortOrder
    """The unique identifier for the dispute."""
    dispute_life_cycle_stage: AirbyteSortOrder
    """The stage in the life cycle of the dispute."""
    dispute_state: AirbyteSortOrder
    """The current state of the dispute."""
    disputed_transactions: AirbyteSortOrder
    """Details of transactions involved in the dispute."""
    links: AirbyteSortOrder
    """Links related to the dispute."""
    outcome: AirbyteSortOrder
    """The outcome of the dispute resolution."""
    reason: AirbyteSortOrder
    """The reason for the dispute."""
    status: AirbyteSortOrder
    """The current status of the dispute."""
    update_time: AirbyteSortOrder
    """The timestamp when the dispute was last updated."""
    updated_time_cut: AirbyteSortOrder
    """The cut-off timestamp for the last update."""


# Entity-specific condition types for list_disputes
class ListDisputesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListDisputesSearchFilter


class ListDisputesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListDisputesSearchFilter


class ListDisputesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListDisputesSearchFilter


class ListDisputesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListDisputesSearchFilter


class ListDisputesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListDisputesSearchFilter


class ListDisputesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListDisputesSearchFilter


class ListDisputesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ListDisputesStringFilter


class ListDisputesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListDisputesStringFilter


class ListDisputesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListDisputesStringFilter


class ListDisputesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ListDisputesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListDisputesInCondition = TypedDict("ListDisputesInCondition", {"in": ListDisputesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListDisputesNotCondition = TypedDict("ListDisputesNotCondition", {"not": "ListDisputesCondition"}, total=False)
"""Negates the nested condition."""

ListDisputesAndCondition = TypedDict("ListDisputesAndCondition", {"and": "list[ListDisputesCondition]"}, total=False)
"""True if all nested conditions are true."""

ListDisputesOrCondition = TypedDict("ListDisputesOrCondition", {"or": "list[ListDisputesCondition]"}, total=False)
"""True if any nested condition is true."""

ListDisputesAnyCondition = TypedDict("ListDisputesAnyCondition", {"any": ListDisputesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all list_disputes condition types
ListDisputesCondition = (
    ListDisputesEqCondition
    | ListDisputesNeqCondition
    | ListDisputesGtCondition
    | ListDisputesGteCondition
    | ListDisputesLtCondition
    | ListDisputesLteCondition
    | ListDisputesInCondition
    | ListDisputesLikeCondition
    | ListDisputesFuzzyCondition
    | ListDisputesKeywordCondition
    | ListDisputesContainsCondition
    | ListDisputesNotCondition
    | ListDisputesAndCondition
    | ListDisputesOrCondition
    | ListDisputesAnyCondition
)


class ListDisputesSearchQuery(TypedDict, total=False):
    """Search query for list_disputes entity."""
    filter: ListDisputesCondition
    sort: list[ListDisputesSortFilter]


# ===== SEARCH_INVOICES SEARCH TYPES =====

class SearchInvoicesSearchFilter(TypedDict, total=False):
    """Available fields for filtering search_invoices search queries."""
    additional_recipients: list[Any] | None
    """List of additional recipients associated with the invoice"""
    amount: dict[str, Any] | None
    """Detailed breakdown of the invoice amount"""
    configuration: dict[str, Any] | None
    """Configuration settings related to the invoice"""
    detail: dict[str, Any] | None
    """Detailed information about the invoice"""
    due_amount: dict[str, Any] | None
    """Due amount remaining to be paid for the invoice"""
    gratuity: dict[str, Any] | None
    """Gratuity amount included in the invoice"""
    id: str | None
    """Unique identifier of the invoice"""
    invoicer: dict[str, Any] | None
    """Information about the invoicer associated with the invoice"""
    last_update_time: str | None
    """Date and time of the last update made to the invoice"""
    links: list[Any] | None
    """Links associated with the invoice"""
    payments: dict[str, Any] | None
    """Payment transactions associated with the invoice"""
    primary_recipients: list[Any] | None
    """Primary recipients associated with the invoice"""
    refunds: dict[str, Any] | None
    """Refund transactions associated with the invoice"""
    status: str | None
    """Current status of the invoice"""


class SearchInvoicesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    additional_recipients: list[list[Any]]
    """List of additional recipients associated with the invoice"""
    amount: list[dict[str, Any]]
    """Detailed breakdown of the invoice amount"""
    configuration: list[dict[str, Any]]
    """Configuration settings related to the invoice"""
    detail: list[dict[str, Any]]
    """Detailed information about the invoice"""
    due_amount: list[dict[str, Any]]
    """Due amount remaining to be paid for the invoice"""
    gratuity: list[dict[str, Any]]
    """Gratuity amount included in the invoice"""
    id: list[str]
    """Unique identifier of the invoice"""
    invoicer: list[dict[str, Any]]
    """Information about the invoicer associated with the invoice"""
    last_update_time: list[str]
    """Date and time of the last update made to the invoice"""
    links: list[list[Any]]
    """Links associated with the invoice"""
    payments: list[dict[str, Any]]
    """Payment transactions associated with the invoice"""
    primary_recipients: list[list[Any]]
    """Primary recipients associated with the invoice"""
    refunds: list[dict[str, Any]]
    """Refund transactions associated with the invoice"""
    status: list[str]
    """Current status of the invoice"""


class SearchInvoicesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    additional_recipients: Any
    """List of additional recipients associated with the invoice"""
    amount: Any
    """Detailed breakdown of the invoice amount"""
    configuration: Any
    """Configuration settings related to the invoice"""
    detail: Any
    """Detailed information about the invoice"""
    due_amount: Any
    """Due amount remaining to be paid for the invoice"""
    gratuity: Any
    """Gratuity amount included in the invoice"""
    id: Any
    """Unique identifier of the invoice"""
    invoicer: Any
    """Information about the invoicer associated with the invoice"""
    last_update_time: Any
    """Date and time of the last update made to the invoice"""
    links: Any
    """Links associated with the invoice"""
    payments: Any
    """Payment transactions associated with the invoice"""
    primary_recipients: Any
    """Primary recipients associated with the invoice"""
    refunds: Any
    """Refund transactions associated with the invoice"""
    status: Any
    """Current status of the invoice"""


class SearchInvoicesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    additional_recipients: str
    """List of additional recipients associated with the invoice"""
    amount: str
    """Detailed breakdown of the invoice amount"""
    configuration: str
    """Configuration settings related to the invoice"""
    detail: str
    """Detailed information about the invoice"""
    due_amount: str
    """Due amount remaining to be paid for the invoice"""
    gratuity: str
    """Gratuity amount included in the invoice"""
    id: str
    """Unique identifier of the invoice"""
    invoicer: str
    """Information about the invoicer associated with the invoice"""
    last_update_time: str
    """Date and time of the last update made to the invoice"""
    links: str
    """Links associated with the invoice"""
    payments: str
    """Payment transactions associated with the invoice"""
    primary_recipients: str
    """Primary recipients associated with the invoice"""
    refunds: str
    """Refund transactions associated with the invoice"""
    status: str
    """Current status of the invoice"""


class SearchInvoicesSortFilter(TypedDict, total=False):
    """Available fields for sorting search_invoices search results."""
    additional_recipients: AirbyteSortOrder
    """List of additional recipients associated with the invoice"""
    amount: AirbyteSortOrder
    """Detailed breakdown of the invoice amount"""
    configuration: AirbyteSortOrder
    """Configuration settings related to the invoice"""
    detail: AirbyteSortOrder
    """Detailed information about the invoice"""
    due_amount: AirbyteSortOrder
    """Due amount remaining to be paid for the invoice"""
    gratuity: AirbyteSortOrder
    """Gratuity amount included in the invoice"""
    id: AirbyteSortOrder
    """Unique identifier of the invoice"""
    invoicer: AirbyteSortOrder
    """Information about the invoicer associated with the invoice"""
    last_update_time: AirbyteSortOrder
    """Date and time of the last update made to the invoice"""
    links: AirbyteSortOrder
    """Links associated with the invoice"""
    payments: AirbyteSortOrder
    """Payment transactions associated with the invoice"""
    primary_recipients: AirbyteSortOrder
    """Primary recipients associated with the invoice"""
    refunds: AirbyteSortOrder
    """Refund transactions associated with the invoice"""
    status: AirbyteSortOrder
    """Current status of the invoice"""


# Entity-specific condition types for search_invoices
class SearchInvoicesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchInvoicesSearchFilter


class SearchInvoicesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchInvoicesSearchFilter


class SearchInvoicesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchInvoicesSearchFilter


class SearchInvoicesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchInvoicesSearchFilter


class SearchInvoicesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchInvoicesSearchFilter


class SearchInvoicesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchInvoicesSearchFilter


class SearchInvoicesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchInvoicesStringFilter


class SearchInvoicesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchInvoicesStringFilter


class SearchInvoicesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchInvoicesStringFilter


class SearchInvoicesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchInvoicesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchInvoicesInCondition = TypedDict("SearchInvoicesInCondition", {"in": SearchInvoicesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchInvoicesNotCondition = TypedDict("SearchInvoicesNotCondition", {"not": "SearchInvoicesCondition"}, total=False)
"""Negates the nested condition."""

SearchInvoicesAndCondition = TypedDict("SearchInvoicesAndCondition", {"and": "list[SearchInvoicesCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchInvoicesOrCondition = TypedDict("SearchInvoicesOrCondition", {"or": "list[SearchInvoicesCondition]"}, total=False)
"""True if any nested condition is true."""

SearchInvoicesAnyCondition = TypedDict("SearchInvoicesAnyCondition", {"any": SearchInvoicesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_invoices condition types
SearchInvoicesCondition = (
    SearchInvoicesEqCondition
    | SearchInvoicesNeqCondition
    | SearchInvoicesGtCondition
    | SearchInvoicesGteCondition
    | SearchInvoicesLtCondition
    | SearchInvoicesLteCondition
    | SearchInvoicesInCondition
    | SearchInvoicesLikeCondition
    | SearchInvoicesFuzzyCondition
    | SearchInvoicesKeywordCondition
    | SearchInvoicesContainsCondition
    | SearchInvoicesNotCondition
    | SearchInvoicesAndCondition
    | SearchInvoicesOrCondition
    | SearchInvoicesAnyCondition
)


class SearchInvoicesSearchQuery(TypedDict, total=False):
    """Search query for search_invoices entity."""
    filter: SearchInvoicesCondition
    sort: list[SearchInvoicesSortFilter]


# ===== LIST_PAYMENTS SEARCH TYPES =====

class ListPaymentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering list_payments search queries."""
    cart: str | None
    """Details of the cart associated with the payment."""
    create_time: str | None
    """The date and time when the payment was created."""
    id: str | None
    """Unique identifier for the payment."""
    intent: str | None
    """The intention or purpose behind the payment."""
    links: list[Any] | None
    """Collection of links related to the payment"""
    payer: dict[str, Any] | None
    """Details of the payer who made the payment"""
    state: str | None
    """The state of the payment."""
    transactions: list[Any] | None
    """List of transactions associated with the payment"""
    update_time: str | None
    """The date and time when the payment was last updated."""


class ListPaymentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    cart: list[str]
    """Details of the cart associated with the payment."""
    create_time: list[str]
    """The date and time when the payment was created."""
    id: list[str]
    """Unique identifier for the payment."""
    intent: list[str]
    """The intention or purpose behind the payment."""
    links: list[list[Any]]
    """Collection of links related to the payment"""
    payer: list[dict[str, Any]]
    """Details of the payer who made the payment"""
    state: list[str]
    """The state of the payment."""
    transactions: list[list[Any]]
    """List of transactions associated with the payment"""
    update_time: list[str]
    """The date and time when the payment was last updated."""


class ListPaymentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    cart: Any
    """Details of the cart associated with the payment."""
    create_time: Any
    """The date and time when the payment was created."""
    id: Any
    """Unique identifier for the payment."""
    intent: Any
    """The intention or purpose behind the payment."""
    links: Any
    """Collection of links related to the payment"""
    payer: Any
    """Details of the payer who made the payment"""
    state: Any
    """The state of the payment."""
    transactions: Any
    """List of transactions associated with the payment"""
    update_time: Any
    """The date and time when the payment was last updated."""


class ListPaymentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    cart: str
    """Details of the cart associated with the payment."""
    create_time: str
    """The date and time when the payment was created."""
    id: str
    """Unique identifier for the payment."""
    intent: str
    """The intention or purpose behind the payment."""
    links: str
    """Collection of links related to the payment"""
    payer: str
    """Details of the payer who made the payment"""
    state: str
    """The state of the payment."""
    transactions: str
    """List of transactions associated with the payment"""
    update_time: str
    """The date and time when the payment was last updated."""


class ListPaymentsSortFilter(TypedDict, total=False):
    """Available fields for sorting list_payments search results."""
    cart: AirbyteSortOrder
    """Details of the cart associated with the payment."""
    create_time: AirbyteSortOrder
    """The date and time when the payment was created."""
    id: AirbyteSortOrder
    """Unique identifier for the payment."""
    intent: AirbyteSortOrder
    """The intention or purpose behind the payment."""
    links: AirbyteSortOrder
    """Collection of links related to the payment"""
    payer: AirbyteSortOrder
    """Details of the payer who made the payment"""
    state: AirbyteSortOrder
    """The state of the payment."""
    transactions: AirbyteSortOrder
    """List of transactions associated with the payment"""
    update_time: AirbyteSortOrder
    """The date and time when the payment was last updated."""


# Entity-specific condition types for list_payments
class ListPaymentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListPaymentsSearchFilter


class ListPaymentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListPaymentsSearchFilter


class ListPaymentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListPaymentsSearchFilter


class ListPaymentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListPaymentsSearchFilter


class ListPaymentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListPaymentsSearchFilter


class ListPaymentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListPaymentsSearchFilter


class ListPaymentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ListPaymentsStringFilter


class ListPaymentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListPaymentsStringFilter


class ListPaymentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListPaymentsStringFilter


class ListPaymentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ListPaymentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListPaymentsInCondition = TypedDict("ListPaymentsInCondition", {"in": ListPaymentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListPaymentsNotCondition = TypedDict("ListPaymentsNotCondition", {"not": "ListPaymentsCondition"}, total=False)
"""Negates the nested condition."""

ListPaymentsAndCondition = TypedDict("ListPaymentsAndCondition", {"and": "list[ListPaymentsCondition]"}, total=False)
"""True if all nested conditions are true."""

ListPaymentsOrCondition = TypedDict("ListPaymentsOrCondition", {"or": "list[ListPaymentsCondition]"}, total=False)
"""True if any nested condition is true."""

ListPaymentsAnyCondition = TypedDict("ListPaymentsAnyCondition", {"any": ListPaymentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all list_payments condition types
ListPaymentsCondition = (
    ListPaymentsEqCondition
    | ListPaymentsNeqCondition
    | ListPaymentsGtCondition
    | ListPaymentsGteCondition
    | ListPaymentsLtCondition
    | ListPaymentsLteCondition
    | ListPaymentsInCondition
    | ListPaymentsLikeCondition
    | ListPaymentsFuzzyCondition
    | ListPaymentsKeywordCondition
    | ListPaymentsContainsCondition
    | ListPaymentsNotCondition
    | ListPaymentsAndCondition
    | ListPaymentsOrCondition
    | ListPaymentsAnyCondition
)


class ListPaymentsSearchQuery(TypedDict, total=False):
    """Search query for list_payments entity."""
    filter: ListPaymentsCondition
    sort: list[ListPaymentsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
