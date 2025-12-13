"""
stripe connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    BalanceGetParams,
    BalanceTransactionsGetParams,
    BalanceTransactionsListParams,
    BalanceTransactionsListParamsCreated,
    ChargesGetParams,
    ChargesListParams,
    ChargesListParamsCreated,
    ChargesSearchParams,
    CustomersGetParams,
    CustomersListParams,
    CustomersListParamsCreated,
    CustomersSearchParams,
    DisputesGetParams,
    DisputesListParams,
    DisputesListParamsCreated,
    InvoicesGetParams,
    InvoicesListParams,
    InvoicesListParamsCreated,
    InvoicesSearchParams,
    PaymentIntentsGetParams,
    PaymentIntentsListParams,
    PaymentIntentsListParamsCreated,
    PaymentIntentsSearchParams,
    PayoutsGetParams,
    PayoutsListParams,
    PayoutsListParamsArrivalDate,
    PayoutsListParamsCreated,
    ProductsGetParams,
    ProductsListParams,
    ProductsListParamsCreated,
    ProductsSearchParams,
    RefundsGetParams,
    RefundsListParams,
    RefundsListParamsCreated,
    SubscriptionsGetParams,
    SubscriptionsListParams,
    SubscriptionsListParamsAutomaticTax,
    SubscriptionsListParamsCreated,
    SubscriptionsListParamsCurrentPeriodEnd,
    SubscriptionsListParamsCurrentPeriodStart,
    SubscriptionsSearchParams,
)

if TYPE_CHECKING:
    from .models import StripeAuthConfig
# Import response models and envelope models at runtime
from .models import (
    StripeExecuteResult,
    StripeExecuteResultWithMeta,
    CustomersListResult,
    CustomersSearchResult,
    InvoicesListResult,
    ChargesListResult,
    SubscriptionsListResult,
    RefundsListResult,
    ProductsListResult,
    ProductsSearchResult,
    BalanceTransactionsListResult,
    PaymentIntentsListResult,
    PaymentIntentsSearchResult,
    DisputesListResult,
    PayoutsListResult,
    Balance,
    BalanceTransaction,
    Charge,
    ChargeSearchResult,
    Customer,
    Dispute,
    Invoice,
    InvoiceSearchResult,
    PaymentIntent,
    Payout,
    Product,
    Refund,
    Subscription,
    SubscriptionSearchResult,
)


class StripeConnector:
    """
    Type-safe Stripe API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "stripe"
    connector_version = "0.1.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("customers", "list"): True,
        ("customers", "get"): False,
        ("customers", "search"): True,
        ("invoices", "list"): True,
        ("invoices", "get"): False,
        ("invoices", "search"): False,
        ("charges", "list"): True,
        ("charges", "get"): False,
        ("charges", "search"): False,
        ("subscriptions", "list"): True,
        ("subscriptions", "get"): False,
        ("subscriptions", "search"): False,
        ("refunds", "list"): True,
        ("refunds", "get"): False,
        ("products", "list"): True,
        ("products", "get"): False,
        ("products", "search"): True,
        ("balance", "get"): False,
        ("balance_transactions", "list"): True,
        ("balance_transactions", "get"): False,
        ("payment_intents", "list"): True,
        ("payment_intents", "get"): False,
        ("payment_intents", "search"): True,
        ("disputes", "list"): True,
        ("disputes", "get"): False,
        ("payouts", "list"): True,
        ("payouts", "get"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('customers', 'list'): {'limit': 'limit', 'starting_after': 'starting_after', 'ending_before': 'ending_before', 'email': 'email', 'created': 'created'},
        ('customers', 'get'): {'id': 'id'},
        ('customers', 'search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('invoices', 'list'): {'collection_method': 'collection_method', 'created': 'created', 'customer': 'customer', 'customer_account': 'customer_account', 'ending_before': 'ending_before', 'limit': 'limit', 'starting_after': 'starting_after', 'status': 'status', 'subscription': 'subscription'},
        ('invoices', 'get'): {'id': 'id'},
        ('invoices', 'search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('charges', 'list'): {'created': 'created', 'customer': 'customer', 'ending_before': 'ending_before', 'limit': 'limit', 'payment_intent': 'payment_intent', 'starting_after': 'starting_after'},
        ('charges', 'get'): {'id': 'id'},
        ('charges', 'search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('subscriptions', 'list'): {'automatic_tax': 'automatic_tax', 'collection_method': 'collection_method', 'created': 'created', 'current_period_end': 'current_period_end', 'current_period_start': 'current_period_start', 'customer': 'customer', 'customer_account': 'customer_account', 'ending_before': 'ending_before', 'limit': 'limit', 'price': 'price', 'starting_after': 'starting_after', 'status': 'status'},
        ('subscriptions', 'get'): {'id': 'id'},
        ('subscriptions', 'search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('refunds', 'list'): {'charge': 'charge', 'created': 'created', 'ending_before': 'ending_before', 'limit': 'limit', 'payment_intent': 'payment_intent', 'starting_after': 'starting_after'},
        ('refunds', 'get'): {'id': 'id'},
        ('products', 'list'): {'active': 'active', 'created': 'created', 'ending_before': 'ending_before', 'ids': 'ids', 'limit': 'limit', 'shippable': 'shippable', 'starting_after': 'starting_after', 'url': 'url'},
        ('products', 'get'): {'id': 'id'},
        ('products', 'search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('balance_transactions', 'list'): {'created': 'created', 'currency': 'currency', 'ending_before': 'ending_before', 'limit': 'limit', 'payout': 'payout', 'source': 'source', 'starting_after': 'starting_after', 'type': 'type'},
        ('balance_transactions', 'get'): {'id': 'id'},
        ('payment_intents', 'list'): {'created': 'created', 'customer': 'customer', 'customer_account': 'customer_account', 'ending_before': 'ending_before', 'limit': 'limit', 'starting_after': 'starting_after'},
        ('payment_intents', 'get'): {'id': 'id'},
        ('payment_intents', 'search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('disputes', 'list'): {'charge': 'charge', 'created': 'created', 'ending_before': 'ending_before', 'limit': 'limit', 'payment_intent': 'payment_intent', 'starting_after': 'starting_after'},
        ('disputes', 'get'): {'id': 'id'},
        ('payouts', 'list'): {'arrival_date': 'arrival_date', 'created': 'created', 'destination': 'destination', 'ending_before': 'ending_before', 'limit': 'limit', 'starting_after': 'starting_after', 'status': 'status'},
        ('payouts', 'get'): {'id': 'id'},
    }

    def __init__(
        self,
        auth_config: StripeAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new stripe connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            airbyte_connector_api_url: Airbyte connector API URL (defaults to Airbyte Cloud API URL)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = StripeConnector(auth_config=StripeAuthConfig(api_key="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = StripeConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = StripeConnector(
                auth_config=StripeAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            if not config_path:
                config_path = str(self.get_default_config_path())

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.customers = CustomersQuery(self)
        self.invoices = InvoicesQuery(self)
        self.charges = ChargesQuery(self)
        self.subscriptions = SubscriptionsQuery(self)
        self.refunds = RefundsQuery(self)
        self.products = ProductsQuery(self)
        self.balance = BalanceQuery(self)
        self.balance_transactions = BalanceTransactionsQuery(self)
        self.payment_intents = PaymentIntentsQuery(self)
        self.disputes = DisputesQuery(self)
        self.payouts = PayoutsQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["list"],
        params: "CustomersListParams"
    ) -> "CustomersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["get"],
        params: "CustomersGetParams"
    ) -> "Customer": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["search"],
        params: "CustomersSearchParams"
    ) -> "CustomersSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoices"],
        action: Literal["list"],
        params: "InvoicesListParams"
    ) -> "InvoicesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoices"],
        action: Literal["get"],
        params: "InvoicesGetParams"
    ) -> "Invoice": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoices"],
        action: Literal["search"],
        params: "InvoicesSearchParams"
    ) -> "InvoiceSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["charges"],
        action: Literal["list"],
        params: "ChargesListParams"
    ) -> "ChargesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["charges"],
        action: Literal["get"],
        params: "ChargesGetParams"
    ) -> "Charge": ...

    @overload
    async def execute(
        self,
        entity: Literal["charges"],
        action: Literal["search"],
        params: "ChargesSearchParams"
    ) -> "ChargeSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["subscriptions"],
        action: Literal["list"],
        params: "SubscriptionsListParams"
    ) -> "SubscriptionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["subscriptions"],
        action: Literal["get"],
        params: "SubscriptionsGetParams"
    ) -> "Subscription": ...

    @overload
    async def execute(
        self,
        entity: Literal["subscriptions"],
        action: Literal["search"],
        params: "SubscriptionsSearchParams"
    ) -> "SubscriptionSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["refunds"],
        action: Literal["list"],
        params: "RefundsListParams"
    ) -> "RefundsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["refunds"],
        action: Literal["get"],
        params: "RefundsGetParams"
    ) -> "Refund": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["list"],
        params: "ProductsListParams"
    ) -> "ProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["get"],
        params: "ProductsGetParams"
    ) -> "Product": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["search"],
        params: "ProductsSearchParams"
    ) -> "ProductsSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["balance"],
        action: Literal["get"],
        params: "BalanceGetParams"
    ) -> "Balance": ...

    @overload
    async def execute(
        self,
        entity: Literal["balance_transactions"],
        action: Literal["list"],
        params: "BalanceTransactionsListParams"
    ) -> "BalanceTransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["balance_transactions"],
        action: Literal["get"],
        params: "BalanceTransactionsGetParams"
    ) -> "BalanceTransaction": ...

    @overload
    async def execute(
        self,
        entity: Literal["payment_intents"],
        action: Literal["list"],
        params: "PaymentIntentsListParams"
    ) -> "PaymentIntentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["payment_intents"],
        action: Literal["get"],
        params: "PaymentIntentsGetParams"
    ) -> "PaymentIntent": ...

    @overload
    async def execute(
        self,
        entity: Literal["payment_intents"],
        action: Literal["search"],
        params: "PaymentIntentsSearchParams"
    ) -> "PaymentIntentsSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["disputes"],
        action: Literal["list"],
        params: "DisputesListParams"
    ) -> "DisputesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["disputes"],
        action: Literal["get"],
        params: "DisputesGetParams"
    ) -> "Dispute": ...

    @overload
    async def execute(
        self,
        entity: Literal["payouts"],
        action: Literal["list"],
        params: "PayoutsListParams"
    ) -> "PayoutsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["payouts"],
        action: Literal["get"],
        params: "PayoutsGetParams"
    ) -> "Payout": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> StripeExecuteResult[Any] | StripeExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Remap parameter names from snake_case (TypedDict keys) to API parameter names
        if params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                params = {param_map.get(k, k): v for k, v in params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._EXTRACTOR_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return StripeExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return StripeExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class CustomersQuery:
    """
    Query class for Customers entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        starting_after: str | None = None,
        ending_before: str | None = None,
        email: str | None = None,
        created: CustomersListParamsCreated | None = None,
        **kwargs
    ) -> CustomersListResult:
        """
        Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.

        Args:
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.
            email: A case-sensitive filter on the list based on the customer's email field. The value must be a string.
            created: Only return customers that were created during the given date interval.
            **kwargs: Additional parameters

        Returns:
            CustomersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "starting_after": starting_after,
            "ending_before": ending_before,
            "email": email,
            "created": created,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomersListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Customer:
        """
        Retrieves a Customer object.

        Args:
            id: The customer ID
            **kwargs: Additional parameters

        Returns:
            Customer
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "get", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> CustomersSearchResult:
        """
        Search for customers using Stripe's Search Query Language.

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            CustomersSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "search", params)
        # Cast generic envelope to concrete typed result
        return CustomersSearchResult(
            data=result.data,
            meta=result.meta        )



class InvoicesQuery:
    """
    Query class for Invoices entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        collection_method: str | None = None,
        created: InvoicesListParamsCreated | None = None,
        customer: str | None = None,
        customer_account: str | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        starting_after: str | None = None,
        status: str | None = None,
        subscription: str | None = None,
        **kwargs
    ) -> InvoicesListResult:
        """
        Returns a list of invoices

        Args:
            collection_method: The collection method of the invoices to retrieve
            created: Only return customers that were created during the given date interval.
            customer: Only return invoices for the customer specified by this customer ID.
            customer_account: Only return invoices for the account specified by this account ID
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.
            status: The status of the invoices to retrieve
            subscription: Only return invoices for the subscription specified by this subscription ID.
            **kwargs: Additional parameters

        Returns:
            InvoicesListResult
        """
        params = {k: v for k, v in {
            "collection_method": collection_method,
            "created": created,
            "customer": customer,
            "customer_account": customer_account,
            "ending_before": ending_before,
            "limit": limit,
            "starting_after": starting_after,
            "status": status,
            "subscription": subscription,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "list", params)
        # Cast generic envelope to concrete typed result
        return InvoicesListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Invoice:
        """
        Retrieves the invoice with the given ID

        Args:
            id: The invoice ID
            **kwargs: Additional parameters

        Returns:
            Invoice
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "get", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> InvoiceSearchResult:
        """
        Search for invoices using Stripe's Search Query Language

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            InvoiceSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "search", params)
        return result



class ChargesQuery:
    """
    Query class for Charges entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        created: ChargesListParamsCreated | None = None,
        customer: str | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        payment_intent: str | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> ChargesListResult:
        """
        Returns a list of charges you've previously created. The charges are returned in sorted order, with the most recent charges appearing first.

        Args:
            created: Only return customers that were created during the given date interval.
            customer: Only return charges for the customer specified by this customer ID
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return charges that were created by the PaymentIntent specified by this ID
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.
            **kwargs: Additional parameters

        Returns:
            ChargesListResult
        """
        params = {k: v for k, v in {
            "created": created,
            "customer": customer,
            "ending_before": ending_before,
            "limit": limit,
            "payment_intent": payment_intent,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("charges", "list", params)
        # Cast generic envelope to concrete typed result
        return ChargesListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Charge:
        """
        Retrieves the details of a charge that has previously been created

        Args:
            id: The charge ID
            **kwargs: Additional parameters

        Returns:
            Charge
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("charges", "get", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> ChargeSearchResult:
        """
        Search for charges using Stripe's Search Query Language

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            ChargeSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("charges", "search", params)
        return result



class SubscriptionsQuery:
    """
    Query class for Subscriptions entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        automatic_tax: SubscriptionsListParamsAutomaticTax | None = None,
        collection_method: str | None = None,
        created: SubscriptionsListParamsCreated | None = None,
        current_period_end: SubscriptionsListParamsCurrentPeriodEnd | None = None,
        current_period_start: SubscriptionsListParamsCurrentPeriodStart | None = None,
        customer: str | None = None,
        customer_account: str | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        price: str | None = None,
        starting_after: str | None = None,
        status: str | None = None,
        **kwargs
    ) -> SubscriptionsListResult:
        """
        By default, returns a list of subscriptions that have not been canceled

        Args:
            automatic_tax: Filter subscriptions by their automatic tax settings.
            collection_method: The collection method of the subscriptions to retrieve
            created: Only return customers that were created during the given date interval.
            current_period_end: Only return subscriptions whose minimum item current_period_end falls within the given date interval.
            current_period_start: Only return subscriptions whose maximum item current_period_start falls within the given date interval.
            customer: Only return subscriptions for the customer specified by this customer ID
            customer_account: The ID of the account whose subscriptions will be retrieved.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            price: Filter for subscriptions that contain this recurring price ID.
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.
            status: The status of the subscriptions to retrieve. Passing in a value of canceled will return all canceled subscriptions, including those belonging to deleted customers. Pass ended to find subscriptions that are canceled and subscriptions that are expired due to incomplete payment. Passing in a value of all will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.
            **kwargs: Additional parameters

        Returns:
            SubscriptionsListResult
        """
        params = {k: v for k, v in {
            "automatic_tax": automatic_tax,
            "collection_method": collection_method,
            "created": created,
            "current_period_end": current_period_end,
            "current_period_start": current_period_start,
            "customer": customer,
            "customer_account": customer_account,
            "ending_before": ending_before,
            "limit": limit,
            "price": price,
            "starting_after": starting_after,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("subscriptions", "list", params)
        # Cast generic envelope to concrete typed result
        return SubscriptionsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Subscription:
        """
        Retrieves the subscription with the given ID

        Args:
            id: The subscription ID
            **kwargs: Additional parameters

        Returns:
            Subscription
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("subscriptions", "get", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> SubscriptionSearchResult:
        """
        Search for subscriptions using Stripe's Search Query Language

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            SubscriptionSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("subscriptions", "search", params)
        return result



class RefundsQuery:
    """
    Query class for Refunds entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        charge: str | None = None,
        created: RefundsListParamsCreated | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        payment_intent: str | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> RefundsListResult:
        """
        Returns a list of all refunds you've previously created. The refunds are returned in sorted order, with the most recent refunds appearing first.

        Args:
            charge: Only return refunds for the charge specified by this charge ID
            created: Only return customers that were created during the given date interval.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return refunds for the PaymentIntent specified by this ID
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.
            **kwargs: Additional parameters

        Returns:
            RefundsListResult
        """
        params = {k: v for k, v in {
            "charge": charge,
            "created": created,
            "ending_before": ending_before,
            "limit": limit,
            "payment_intent": payment_intent,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("refunds", "list", params)
        # Cast generic envelope to concrete typed result
        return RefundsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Refund:
        """
        Retrieves the details of an existing refund

        Args:
            id: The refund ID
            **kwargs: Additional parameters

        Returns:
            Refund
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("refunds", "get", params)
        return result



class ProductsQuery:
    """
    Query class for Products entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        active: bool | None = None,
        created: ProductsListParamsCreated | None = None,
        ending_before: str | None = None,
        ids: list[str] | None = None,
        limit: int | None = None,
        shippable: bool | None = None,
        starting_after: str | None = None,
        url: str | None = None,
        **kwargs
    ) -> ProductsListResult:
        """
        Returns a list of your products. The products are returned sorted by creation date, with the most recent products appearing first.

        Args:
            active: Only return products that are active or inactive
            created: Only return products that were created during the given date interval.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.
            ids: Only return products with the given IDs
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            shippable: Only return products that can be shipped
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.
            url: Only return products with the given url
            **kwargs: Additional parameters

        Returns:
            ProductsListResult
        """
        params = {k: v for k, v in {
            "active": active,
            "created": created,
            "ending_before": ending_before,
            "ids": ids,
            "limit": limit,
            "shippable": shippable,
            "starting_after": starting_after,
            "url": url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Product:
        """
        Retrieves the details of an existing product. Supply the unique product ID and Stripe will return the corresponding product information.

        Args:
            id: The product ID
            **kwargs: Additional parameters

        Returns:
            Product
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "get", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> ProductsSearchResult:
        """
        Search for products using Stripe's Search Query Language.

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            ProductsSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "search", params)
        # Cast generic envelope to concrete typed result
        return ProductsSearchResult(
            data=result.data,
            meta=result.meta        )



class BalanceQuery:
    """
    Query class for Balance entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> Balance:
        """
        Retrieves the current account balance, based on the authentication that was used to make the request.

        Returns:
            Balance
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("balance", "get", params)
        return result



class BalanceTransactionsQuery:
    """
    Query class for BalanceTransactions entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        created: BalanceTransactionsListParamsCreated | None = None,
        currency: str | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        payout: str | None = None,
        source: str | None = None,
        starting_after: str | None = None,
        type: str | None = None,
        **kwargs
    ) -> BalanceTransactionsListResult:
        """
        Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.

        Args:
            created: Only return transactions that were created during the given date interval.
            currency: Only return transactions in a certain currency. Three-letter ISO currency code, in lowercase.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payout: For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.
            source: Only returns the original transaction.
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list.
            type: Only returns transactions of the given type.
            **kwargs: Additional parameters

        Returns:
            BalanceTransactionsListResult
        """
        params = {k: v for k, v in {
            "created": created,
            "currency": currency,
            "ending_before": ending_before,
            "limit": limit,
            "payout": payout,
            "source": source,
            "starting_after": starting_after,
            "type": type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("balance_transactions", "list", params)
        # Cast generic envelope to concrete typed result
        return BalanceTransactionsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> BalanceTransaction:
        """
        Retrieves the balance transaction with the given ID.

        Args:
            id: The ID of the desired balance transaction
            **kwargs: Additional parameters

        Returns:
            BalanceTransaction
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("balance_transactions", "get", params)
        return result



class PaymentIntentsQuery:
    """
    Query class for PaymentIntents entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        created: PaymentIntentsListParamsCreated | None = None,
        customer: str | None = None,
        customer_account: str | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> PaymentIntentsListResult:
        """
        Returns a list of PaymentIntents. The payment intents are returned sorted by creation date, with the most recent payment intents appearing first.

        Args:
            created: Only return payment intents that were created during the given date interval.
            customer: Only return payment intents for the customer specified by this customer ID
            customer_account: Only return payment intents for the account specified by this account ID
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list.
            **kwargs: Additional parameters

        Returns:
            PaymentIntentsListResult
        """
        params = {k: v for k, v in {
            "created": created,
            "customer": customer,
            "customer_account": customer_account,
            "ending_before": ending_before,
            "limit": limit,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payment_intents", "list", params)
        # Cast generic envelope to concrete typed result
        return PaymentIntentsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> PaymentIntent:
        """
        Retrieves the details of a PaymentIntent that has previously been created.

        Args:
            id: The ID of the payment intent
            **kwargs: Additional parameters

        Returns:
            PaymentIntent
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payment_intents", "get", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> PaymentIntentsSearchResult:
        """
        Search for payment intents using Stripe's Search Query Language.

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            PaymentIntentsSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payment_intents", "search", params)
        # Cast generic envelope to concrete typed result
        return PaymentIntentsSearchResult(
            data=result.data,
            meta=result.meta        )



class DisputesQuery:
    """
    Query class for Disputes entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        charge: str | None = None,
        created: DisputesListParamsCreated | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        payment_intent: str | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> DisputesListResult:
        """
        Returns a list of your disputes. The disputes are returned sorted by creation date, with the most recent disputes appearing first.

        Args:
            charge: Only return disputes associated to the charge specified by this charge ID
            created: Only return disputes that were created during the given date interval.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list.
            **kwargs: Additional parameters

        Returns:
            DisputesListResult
        """
        params = {k: v for k, v in {
            "charge": charge,
            "created": created,
            "ending_before": ending_before,
            "limit": limit,
            "payment_intent": payment_intent,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("disputes", "list", params)
        # Cast generic envelope to concrete typed result
        return DisputesListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Dispute:
        """
        Retrieves the dispute with the given ID.

        Args:
            id: The ID of the dispute
            **kwargs: Additional parameters

        Returns:
            Dispute
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("disputes", "get", params)
        return result



class PayoutsQuery:
    """
    Query class for Payouts entity operations.
    """

    def __init__(self, connector: StripeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        arrival_date: PayoutsListParamsArrivalDate | None = None,
        created: PayoutsListParamsCreated | None = None,
        destination: str | None = None,
        ending_before: str | None = None,
        limit: int | None = None,
        starting_after: str | None = None,
        status: str | None = None,
        **kwargs
    ) -> PayoutsListResult:
        """
        Returns a list of existing payouts sent to third-party bank accounts or payouts that Stripe sent to you. The payouts return in sorted order, with the most recently created payouts appearing first.

        Args:
            arrival_date: Filter payouts by expected arrival date range.
            created: Only return payouts that were created during the given date interval.
            destination: The ID of the external account the payout was sent to.
            ending_before: A cursor for use in pagination. ending_before is an object ID that defines your place in the list.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. starting_after is an object ID that defines your place in the list.
            status: Only return payouts that have the given status
            **kwargs: Additional parameters

        Returns:
            PayoutsListResult
        """
        params = {k: v for k, v in {
            "arrival_date": arrival_date,
            "created": created,
            "destination": destination,
            "ending_before": ending_before,
            "limit": limit,
            "starting_after": starting_after,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payouts", "list", params)
        # Cast generic envelope to concrete typed result
        return PayoutsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Payout:
        """
        Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list, and Stripe will return the corresponding payout information.

        Args:
            id: The ID of the payout
            **kwargs: Additional parameters

        Returns:
            Payout
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payouts", "get", params)
        return result


