"""
Stripe connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import StripeConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    BalanceGetParams,
    BalanceTransactionsGetParams,
    BalanceTransactionsListParams,
    BalanceTransactionsListParamsCreated,
    ChargesApiSearchParams,
    ChargesGetParams,
    ChargesListParams,
    ChargesListParamsCreated,
    CustomersApiSearchParams,
    CustomersCreateParams,
    CustomersDeleteParams,
    CustomersGetParams,
    CustomersListParams,
    CustomersListParamsCreated,
    CustomersUpdateParams,
    DisputesGetParams,
    DisputesListParams,
    DisputesListParamsCreated,
    InvoicesApiSearchParams,
    InvoicesGetParams,
    InvoicesListParams,
    InvoicesListParamsCreated,
    PaymentIntentsApiSearchParams,
    PaymentIntentsGetParams,
    PaymentIntentsListParams,
    PaymentIntentsListParamsCreated,
    PayoutsGetParams,
    PayoutsListParams,
    PayoutsListParamsArrivalDate,
    PayoutsListParamsCreated,
    ProductsApiSearchParams,
    ProductsCreateParams,
    ProductsDeleteParams,
    ProductsGetParams,
    ProductsListParams,
    ProductsListParamsCreated,
    ProductsUpdateParams,
    RefundsCreateParams,
    RefundsGetParams,
    RefundsListParams,
    RefundsListParamsCreated,
    SubscriptionsApiSearchParams,
    SubscriptionsGetParams,
    SubscriptionsListParams,
    SubscriptionsListParamsAutomaticTax,
    SubscriptionsListParamsCreated,
    SubscriptionsListParamsCurrentPeriodEnd,
    SubscriptionsListParamsCurrentPeriodStart,
    AirbyteSearchParams,
    ChargesSearchFilter,
    ChargesSearchQuery,
    CustomersSearchFilter,
    CustomersSearchQuery,
    InvoicesSearchFilter,
    InvoicesSearchQuery,
    RefundsSearchFilter,
    RefundsSearchQuery,
    SubscriptionsSearchFilter,
    SubscriptionsSearchQuery,
)
if TYPE_CHECKING:
    from .models import StripeAuthConfig

# Import response models and envelope models at runtime
from .models import (
    StripeCheckResult,
    StripeExecuteResult,
    StripeExecuteResultWithMeta,
    CustomersListResult,
    CustomersApiSearchResult,
    InvoicesListResult,
    InvoicesApiSearchResult,
    ChargesListResult,
    ChargesApiSearchResult,
    SubscriptionsListResult,
    SubscriptionsApiSearchResult,
    RefundsListResult,
    ProductsListResult,
    ProductsApiSearchResult,
    BalanceTransactionsListResult,
    PaymentIntentsListResult,
    PaymentIntentsApiSearchResult,
    DisputesListResult,
    PayoutsListResult,
    Balance,
    BalanceTransaction,
    Charge,
    ChargeSearchResult,
    Customer,
    CustomerDeletedResponse,
    Dispute,
    Invoice,
    InvoiceSearchResult,
    PaymentIntent,
    Payout,
    Product,
    ProductDeletedResponse,
    Refund,
    Subscription,
    SubscriptionSearchResult,
    AirbyteSearchHit,
    AirbyteSearchResult,
    ChargesSearchData,
    ChargesSearchResult,
    CustomersSearchData,
    CustomersSearchResult,
    InvoicesSearchData,
    InvoicesSearchResult,
    RefundsSearchData,
    RefundsSearchResult,
    SubscriptionsSearchData,
    SubscriptionsSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 50_000  # ~50KB default, configurable per-tool


def _raise_output_too_large(message: str) -> None:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except Exception as exc:
        raise RuntimeError(message) from exc
    raise ModelRetry(message)


def _check_output_size(result: Any, max_chars: int | None, tool_name: str) -> Any:
    if max_chars is None or max_chars <= 0:
        return result

    try:
        serialized = json.dumps(result, default=str)
    except (TypeError, ValueError):
        return result

    if len(serialized) > max_chars:
        truncated_preview = serialized[:500] + "..." if len(serialized) > 500 else serialized
        _raise_output_too_large(
            f"Tool '{tool_name}' output too large ({len(serialized):,} chars, limit {max_chars:,}). "
            "Please narrow your query by: using the 'fields' parameter to select only needed fields, "
            "adding filters, or reducing the 'limit'. "
            f"Preview: {truncated_preview}"
        )

    return result




class StripeConnector:
    """
    Type-safe Stripe API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "stripe"
    connector_version = "0.1.6"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("customers", "list"): True,
        ("customers", "create"): None,
        ("customers", "get"): None,
        ("customers", "update"): None,
        ("customers", "delete"): None,
        ("customers", "api_search"): True,
        ("invoices", "list"): True,
        ("invoices", "get"): None,
        ("invoices", "api_search"): True,
        ("charges", "list"): True,
        ("charges", "get"): None,
        ("charges", "api_search"): True,
        ("subscriptions", "list"): True,
        ("subscriptions", "get"): None,
        ("subscriptions", "api_search"): True,
        ("refunds", "list"): True,
        ("refunds", "create"): None,
        ("refunds", "get"): None,
        ("products", "list"): True,
        ("products", "create"): None,
        ("products", "get"): None,
        ("products", "update"): None,
        ("products", "delete"): None,
        ("products", "api_search"): True,
        ("balance", "get"): None,
        ("balance_transactions", "list"): True,
        ("balance_transactions", "get"): None,
        ("payment_intents", "list"): True,
        ("payment_intents", "get"): None,
        ("payment_intents", "api_search"): True,
        ("disputes", "list"): True,
        ("disputes", "get"): None,
        ("payouts", "list"): True,
        ("payouts", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('customers', 'list'): {'limit': 'limit', 'starting_after': 'starting_after', 'ending_before': 'ending_before', 'email': 'email', 'created': 'created'},
        ('customers', 'get'): {'id': 'id'},
        ('customers', 'update'): {'id': 'id'},
        ('customers', 'delete'): {'id': 'id'},
        ('customers', 'api_search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('invoices', 'list'): {'collection_method': 'collection_method', 'created': 'created', 'customer': 'customer', 'customer_account': 'customer_account', 'ending_before': 'ending_before', 'limit': 'limit', 'starting_after': 'starting_after', 'status': 'status', 'subscription': 'subscription'},
        ('invoices', 'get'): {'id': 'id'},
        ('invoices', 'api_search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('charges', 'list'): {'created': 'created', 'customer': 'customer', 'ending_before': 'ending_before', 'limit': 'limit', 'payment_intent': 'payment_intent', 'starting_after': 'starting_after'},
        ('charges', 'get'): {'id': 'id'},
        ('charges', 'api_search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('subscriptions', 'list'): {'automatic_tax': 'automatic_tax', 'collection_method': 'collection_method', 'created': 'created', 'current_period_end': 'current_period_end', 'current_period_start': 'current_period_start', 'customer': 'customer', 'customer_account': 'customer_account', 'ending_before': 'ending_before', 'limit': 'limit', 'price': 'price', 'starting_after': 'starting_after', 'status': 'status'},
        ('subscriptions', 'get'): {'id': 'id'},
        ('subscriptions', 'api_search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('refunds', 'list'): {'charge': 'charge', 'created': 'created', 'ending_before': 'ending_before', 'limit': 'limit', 'payment_intent': 'payment_intent', 'starting_after': 'starting_after'},
        ('refunds', 'get'): {'id': 'id'},
        ('products', 'list'): {'active': 'active', 'created': 'created', 'ending_before': 'ending_before', 'ids': 'ids', 'limit': 'limit', 'shippable': 'shippable', 'starting_after': 'starting_after', 'url': 'url'},
        ('products', 'get'): {'id': 'id'},
        ('products', 'update'): {'id': 'id'},
        ('products', 'delete'): {'id': 'id'},
        ('products', 'api_search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('balance_transactions', 'list'): {'created': 'created', 'currency': 'currency', 'ending_before': 'ending_before', 'limit': 'limit', 'payout': 'payout', 'source': 'source', 'starting_after': 'starting_after', 'type': 'type'},
        ('balance_transactions', 'get'): {'id': 'id'},
        ('payment_intents', 'list'): {'created': 'created', 'customer': 'customer', 'customer_account': 'customer_account', 'ending_before': 'ending_before', 'limit': 'limit', 'starting_after': 'starting_after'},
        ('payment_intents', 'get'): {'id': 'id'},
        ('payment_intents', 'api_search'): {'query': 'query', 'limit': 'limit', 'page': 'page'},
        ('disputes', 'list'): {'charge': 'charge', 'created': 'created', 'ending_before': 'ending_before', 'limit': 'limit', 'payment_intent': 'payment_intent', 'starting_after': 'starting_after'},
        ('disputes', 'get'): {'id': 'id'},
        ('payouts', 'list'): {'arrival_date': 'arrival_date', 'created': 'created', 'destination': 'destination', 'ending_before': 'ending_before', 'limit': 'limit', 'starting_after': 'starting_after', 'status': 'status'},
        ('payouts', 'get'): {'id': 'id'},
    }

    def __init__(
        self,
        auth_config: StripeAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new stripe connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide Airbyte credentials with either `connector_id` or `external_user_id`

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (for hosted mode lookup)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            connector_id: Specific connector/source ID (for hosted mode, skips lookup)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = StripeConnector(auth_config=StripeAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = StripeConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = StripeConnector(
                external_user_id="user-123",
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
        # Hosted mode: Airbyte credentials + either connector_id OR external_user_id
        is_hosted = airbyte_client_id and airbyte_client_secret and (connector_id or external_user_id)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_id=connector_id,
                external_user_id=external_user_id,
                connector_definition_id=str(StripeConnectorModel.id) if not connector_id else None,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide Airbyte credentials (airbyte_client_id, airbyte_client_secret) with "
                    "connector_id or external_user_id for hosted mode, or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=StripeConnectorModel,
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
        action: Literal["create"],
        params: "CustomersCreateParams"
    ) -> "Customer": ...

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
        action: Literal["update"],
        params: "CustomersUpdateParams"
    ) -> "Customer": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["delete"],
        params: "CustomersDeleteParams"
    ) -> "CustomerDeletedResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["api_search"],
        params: "CustomersApiSearchParams"
    ) -> "CustomersApiSearchResult": ...

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
        action: Literal["api_search"],
        params: "InvoicesApiSearchParams"
    ) -> "InvoicesApiSearchResult": ...

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
        action: Literal["api_search"],
        params: "ChargesApiSearchParams"
    ) -> "ChargesApiSearchResult": ...

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
        action: Literal["api_search"],
        params: "SubscriptionsApiSearchParams"
    ) -> "SubscriptionsApiSearchResult": ...

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
        action: Literal["create"],
        params: "RefundsCreateParams"
    ) -> "Refund": ...

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
        action: Literal["create"],
        params: "ProductsCreateParams"
    ) -> "Product": ...

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
        action: Literal["update"],
        params: "ProductsUpdateParams"
    ) -> "Product": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["delete"],
        params: "ProductsDeleteParams"
    ) -> "ProductDeletedResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["api_search"],
        params: "ProductsApiSearchParams"
    ) -> "ProductsApiSearchResult": ...

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
        action: Literal["api_search"],
        params: "PaymentIntentsApiSearchParams"
    ) -> "PaymentIntentsApiSearchResult": ...

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
        action: Literal["list", "create", "get", "update", "delete", "api_search", "search"],
        params: Mapping[str, Any]
    ) -> StripeExecuteResult[Any] | StripeExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "delete", "api_search", "search"],
        params: Mapping[str, Any] | None = None
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
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

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

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> StripeCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            StripeCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return StripeCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return StripeCheckResult(
                status="unhealthy",
                error=result.error or "Unknown error during health check",
            )

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def tool_utils(
        cls,
        func: _F | None = None,
        *,
        update_docstring: bool = True,
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @StripeConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @StripeConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    StripeConnectorModel,
                    enable_hosted_mode_features=enable_hosted_mode_features,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            if inspect.iscoroutinefunction(inner):

                @wraps(inner)
                async def aw(*args: Any, **kwargs: Any) -> Any:
                    result = await inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = aw
            else:

                @wraps(inner)
                def sw(*args: Any, **kwargs: Any) -> Any:
                    result = inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = sw

            if update_docstring:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate

    def list_entities(self) -> list[dict[str, Any]]:
        """
        Get structured data about available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.list_entities()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(StripeConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """
        Get the JSON schema for an entity.

        Args:
            entity: Entity name (e.g., "contacts", "companies")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.

        Example:
            schema = connector.entity_schema("contacts")
            if schema:
                print(f"Contact properties: {list(schema.get('properties', {}).keys())}")
        """
        entity_def = next(
            (e for e in StripeConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in StripeConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await StripeConnector.create_hosted(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create_hosted(
        cls,
        *,
        external_user_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        auth_config: "StripeAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "StripeConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            external_user_id: Workspace identifier in Airbyte Cloud
            airbyte_client_id: Airbyte OAuth client ID
            airbyte_client_secret: Airbyte OAuth client secret
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).

        Returns:
            A StripeConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await StripeConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=StripeAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config
            credentials = auth_config.model_dump(exclude_none=True)
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(StripeConnectorModel.id),
                external_user_id=external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            airbyte_client_id=airbyte_client_id,
            airbyte_client_secret=airbyte_client_secret,
            connector_id=source_id,
        )



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
            meta=result.meta
        )



    async def create(
        self,
        **kwargs
    ) -> Customer:
        """
        Creates a new customer object.

        Returns:
            Customer
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "create", params)
        return result



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



    async def update(
        self,
        id: str | None = None,
        **kwargs
    ) -> Customer:
        """
        Updates the specified customer by setting the values of the parameters passed.

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

        result = await self._connector.execute("customers", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> CustomerDeletedResponse:
        """
        Permanently deletes a customer. It cannot be undone.

        Args:
            id: The customer ID
            **kwargs: Additional parameters

        Returns:
            CustomerDeletedResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "delete", params)
        return result



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> CustomersApiSearchResult:
        """
        Search for customers using Stripe's Search Query Language.

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            CustomersApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CustomersApiSearchResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CustomersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomersSearchResult:
        """
        Search customers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomersSearchFilter):
        - account_balance: Current balance value representing funds owed by or to the customer.
        - address: The customer's address information including line1, line2, city, state, postal code, and country.
        - balance: Current balance (positive or negative) that is automatically applied to the customer's next invoice.
        - cards: Card payment methods associated with the customer account.
        - created: Timestamp indicating when the customer object was created.
        - currency: Three-letter ISO currency code representing the customer's default currency.
        - default_card: The default card to be used for charges when no specific payment method is provided.
        - default_source: The default payment source (card or bank account) for the customer.
        - delinquent: Boolean indicating whether the customer is currently delinquent on payments.
        - description: An arbitrary string attached to the customer, often useful for displaying to users.
        - discount: Discount object describing any active discount applied to the customer.
        - email: The customer's email address for communication and tracking purposes.
        - id: Unique identifier for the customer object.
        - invoice_prefix: The prefix for invoice numbers generated for this customer.
        - invoice_settings: Customer's invoice-related settings including default payment method and custom fields.
        - is_deleted: Boolean indicating whether the customer has been deleted.
        - livemode: Boolean indicating whether the object exists in live mode or test mode.
        - metadata: Set of key-value pairs for storing additional structured information about the customer.
        - name: The customer's full name or business name.
        - next_invoice_sequence: The sequence number for the next invoice generated for this customer.
        - object: String representing the object type, always 'customer'.
        - phone: The customer's phone number.
        - preferred_locales: Array of preferred locales for the customer, used for invoice and receipt localization.
        - shipping: Mailing and shipping address for the customer, appears on invoices emailed to the customer.
        - sources: Payment sources (cards, bank accounts) attached to the customer for making payments.
        - subscriptions: List of active subscriptions associated with the customer.
        - tax_exempt: Describes the customer's tax exemption status (none, exempt, or reverse).
        - tax_info: Tax identification information for the customer.
        - tax_info_verification: Verification status of the customer's tax information.
        - test_clock: ID of the test clock associated with this customer for testing time-dependent scenarios.
        - updated: Timestamp indicating when the customer object was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomersSearchResult with hits (list of AirbyteSearchHit[CustomersSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("customers", "search", params)

        # Parse response into typed result
        return CustomersSearchResult(
            hits=[
                AirbyteSearchHit[CustomersSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CustomersSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



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



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> InvoicesApiSearchResult:
        """
        Search for invoices using Stripe's Search Query Language

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            InvoicesApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "api_search", params)
        # Cast generic envelope to concrete typed result
        return InvoicesApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: InvoicesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InvoicesSearchResult:
        """
        Search invoices records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InvoicesSearchFilter):
        - account_country: The country of the business associated with this invoice, commonly used to display localized content.
        - account_name: The public name of the business associated with this invoice.
        - account_tax_ids: Tax IDs of the account associated with this invoice.
        - amount_due: Total amount, in smallest currency unit, that is due and owed by the customer.
        - amount_paid: Total amount, in smallest currency unit, that has been paid by the customer.
        - amount_remaining: The difference between amount_due and amount_paid, representing the outstanding balance.
        - amount_shipping: Total amount of shipping costs on the invoice.
        - application: ID of the Connect application that created this invoice.
        - application_fee: Amount of application fee charged for this invoice in a Connect scenario.
        - application_fee_amount: The fee in smallest currency unit that is collected by the application in a Connect scenario.
        - attempt_count: Number of payment attempts made for this invoice.
        - attempted: Whether an attempt has been made to pay the invoice.
        - auto_advance: Controls whether Stripe performs automatic collection of the invoice.
        - automatic_tax: Settings and status for automatic tax calculation on this invoice.
        - billing: Billing method used for the invoice (charge_automatically or send_invoice).
        - billing_reason: Indicates the reason why the invoice was created (subscription_cycle, manual, etc.).
        - charge: ID of the latest charge generated for this invoice, if any.
        - closed: Whether the invoice has been marked as closed and no longer open for collection.
        - collection_method: Method by which the invoice is collected: charge_automatically or send_invoice.
        - created: Timestamp indicating when the invoice was created.
        - currency: Three-letter ISO currency code in which the invoice is denominated.
        - custom_fields: Custom fields displayed on the invoice as specified by the account.
        - customer: The customer object or ID associated with this invoice.
        - customer_address: The customer's address at the time the invoice was finalized.
        - customer_email: The customer's email address at the time the invoice was finalized.
        - customer_name: The customer's name at the time the invoice was finalized.
        - customer_phone: The customer's phone number at the time the invoice was finalized.
        - customer_shipping: The customer's shipping information at the time the invoice was finalized.
        - customer_tax_exempt: The customer's tax exempt status at the time the invoice was finalized.
        - customer_tax_ids: The customer's tax IDs at the time the invoice was finalized.
        - default_payment_method: Default payment method for the invoice, used if no other method is specified.
        - default_source: Default payment source for the invoice if no payment method is set.
        - default_tax_rates: The tax rates applied to the invoice by default.
        - description: An arbitrary string attached to the invoice, often displayed to customers.
        - discount: The discount object applied to the invoice, if any.
        - discounts: Array of discount IDs or objects currently applied to this invoice.
        - due_date: The date by which payment on this invoice is due, if the invoice is not auto-collected.
        - effective_at: Timestamp when the invoice becomes effective and finalized for payment.
        - ending_balance: The customer's ending account balance after this invoice is finalized.
        - footer: Footer text displayed on the invoice.
        - forgiven: Whether the invoice has been forgiven and is considered paid without actual payment.
        - from_invoice: Details about the invoice this invoice was created from, if applicable.
        - hosted_invoice_url: URL for the hosted invoice page where customers can view and pay the invoice.
        - id: Unique identifier for the invoice object.
        - invoice_pdf: URL for the PDF version of the invoice.
        - is_deleted: Indicates whether this invoice has been deleted.
        - issuer: Details about the entity issuing the invoice.
        - last_finalization_error: The error encountered during the last finalization attempt, if any.
        - latest_revision: The latest revision of the invoice, if revisions are enabled.
        - lines: The individual line items that make up the invoice, representing products, services, or fees.
        - livemode: Indicates whether the invoice exists in live mode (true) or test mode (false).
        - metadata: Key-value pairs for storing additional structured information about the invoice.
        - next_payment_attempt: Timestamp of the next automatic payment attempt for this invoice, if applicable.
        - number: A unique, human-readable identifier for this invoice, often shown to customers.
        - object: String representing the object type, always 'invoice'.
        - on_behalf_of: The account on behalf of which the invoice is being created, used in Connect scenarios.
        - paid: Whether the invoice has been paid in full.
        - paid_out_of_band: Whether payment was made outside of Stripe and manually marked as paid.
        - payment: ID of the payment associated with this invoice, if any.
        - payment_intent: The PaymentIntent associated with this invoice for processing payment.
        - payment_settings: Configuration settings for how payment should be collected on this invoice.
        - period_end: End date of the billing period covered by this invoice.
        - period_start: Start date of the billing period covered by this invoice.
        - post_payment_credit_notes_amount: Total amount of credit notes issued after the invoice was paid.
        - pre_payment_credit_notes_amount: Total amount of credit notes applied before payment was attempted.
        - quote: The quote from which this invoice was generated, if applicable.
        - receipt_number: The receipt number displayed on the invoice, if available.
        - rendering: Settings that control how the invoice is rendered for display.
        - rendering_options: Options for customizing the visual rendering of the invoice.
        - shipping_cost: Total cost of shipping charges included in the invoice.
        - shipping_details: Detailed shipping information for the invoice, including address and carrier.
        - starting_balance: The customer's starting account balance at the beginning of the billing period.
        - statement_description: Extra information about the invoice that appears on the customer's credit card statement.
        - statement_descriptor: A dynamic descriptor that appears on the customer's credit card statement for this invoice.
        - status: The status of the invoice: draft, open, paid, void, or uncollectible.
        - status_transitions: Timestamps tracking when the invoice transitioned between different statuses.
        - subscription: The subscription this invoice was generated for, if applicable.
        - subscription_details: Additional details about the subscription associated with this invoice.
        - subtotal: Total of all line items before discounts or tax are applied.
        - subtotal_excluding_tax: The subtotal amount excluding any tax calculations.
        - tax: Total tax amount applied to the invoice.
        - tax_percent: The percentage of tax applied to the invoice (deprecated, use total_tax_amounts instead).
        - test_clock: ID of the test clock this invoice belongs to, used for testing time-dependent billing.
        - total: Total amount of the invoice after all line items, discounts, and taxes are calculated.
        - total_discount_amounts: Array of the total discount amounts applied, broken down by discount.
        - total_excluding_tax: Total amount of the invoice excluding all tax calculations.
        - total_tax_amounts: Array of tax amounts applied to the invoice, broken down by tax rate.
        - transfer_data: Information about the transfer of funds associated with this invoice in Connect scenarios.
        - updated: Timestamp indicating when the invoice was last updated.
        - webhooks_delivered_at: Timestamp indicating when webhooks for this invoice were successfully delivered.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InvoicesSearchResult with hits (list of AirbyteSearchHit[InvoicesSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("invoices", "search", params)

        # Parse response into typed result
        return InvoicesSearchResult(
            hits=[
                AirbyteSearchHit[InvoicesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=InvoicesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



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



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> ChargesApiSearchResult:
        """
        Search for charges using Stripe's Search Query Language

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            ChargesApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("charges", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ChargesApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: ChargesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ChargesSearchResult:
        """
        Search charges records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ChargesSearchFilter):
        - amount: Amount intended to be collected by this payment in the smallest currency unit (e.g., 100 cents for $1.00), supporting up to eight digits.
        - amount_captured: Amount that was actually captured from this charge.
        - amount_refunded: Amount that has been refunded back to the customer.
        - amount_updates: Updates to the amount that have been made during the charge lifecycle.
        - application: ID of the application that created this charge (Connect only).
        - application_fee: ID of the application fee associated with this charge (Connect only).
        - application_fee_amount: The amount of the application fee deducted from this charge (Connect only).
        - balance_transaction: ID of the balance transaction that describes the impact of this charge on your account balance (excluding refunds or disputes).
        - billing_details: Billing information associated with the payment method at the time of the transaction, including name, email, phone, and address.
        - calculated_statement_descriptor: The full statement descriptor that appears on the customer's credit card statement, combining prefix and suffix.
        - captured: Whether the charge has been captured and funds transferred to your account.
        - card: Deprecated card object containing payment card details if a card was used.
        - created: Timestamp indicating when the charge was created.
        - currency: Three-letter ISO currency code in lowercase (e.g., 'usd', 'eur') for the charge amount.
        - customer: ID of the customer this charge is for, if one exists.
        - description: An arbitrary string attached to the charge, often useful for displaying to users or internal reference.
        - destination: ID of the destination account where funds are transferred (Connect only).
        - dispute: ID of the dispute object if the charge has been disputed.
        - disputed: Whether the charge has been disputed by the customer with their card issuer.
        - failure_balance_transaction: ID of the balance transaction that describes the reversal of funds if the charge failed.
        - failure_code: Error code explaining the reason for charge failure, if applicable.
        - failure_message: Human-readable message providing more details about why the charge failed.
        - fraud_details: Information about fraud assessments and user reports related to this charge.
        - id: Unique identifier for the charge, used to link transactions across other records.
        - invoice: ID of the invoice this charge is for, if the charge was created by invoicing.
        - livemode: Whether the charge occurred in live mode (true) or test mode (false).
        - metadata: Key-value pairs for storing additional structured information about the charge, useful for internal tracking.
        - object: String representing the object type, always 'charge' for charge objects.
        - on_behalf_of: ID of the account on whose behalf the charge was made (Connect only).
        - order: Deprecated field for order information associated with this charge.
        - outcome: Details about the outcome of the charge, including network status, risk assessment, and reason codes.
        - paid: Whether the charge succeeded and funds were successfully collected.
        - payment_intent: ID of the PaymentIntent associated with this charge, if one exists.
        - payment_method: ID of the payment method used for this charge.
        - payment_method_details: Details about the payment method at the time of the transaction, including card brand, network, and authentication results.
        - receipt_email: Email address to which the receipt for this charge was sent.
        - receipt_number: Receipt number that appears on email receipts sent for this charge.
        - receipt_url: URL to a hosted receipt page for this charge, viewable by the customer.
        - refunded: Whether the charge has been fully refunded (partial refunds will still show as false).
        - refunds: List of refunds that have been applied to this charge.
        - review: ID of the review object associated with this charge, if it was flagged for manual review.
        - shipping: Shipping information for the charge, including recipient name, address, and tracking details.
        - source: Deprecated payment source object used to create this charge.
        - source_transfer: ID of the transfer from a source account if funds came from another Stripe account (Connect only).
        - statement_description: Deprecated alias for statement_descriptor.
        - statement_descriptor: Statement descriptor that overrides the account default for card charges, appearing on the customer's statement.
        - statement_descriptor_suffix: Suffix concatenated to the account's statement descriptor prefix to form the complete descriptor on customer statements.
        - status: Current status of the payment: 'succeeded' (completed), 'pending' (processing), or 'failed' (unsuccessful).
        - transfer_data: Object containing destination and amount for transfers to connected accounts (Connect only).
        - transfer_group: String identifier for grouping related charges and transfers together (Connect only).
        - updated: Timestamp of the last update to this charge object.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ChargesSearchResult with hits (list of AirbyteSearchHit[ChargesSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("charges", "search", params)

        # Parse response into typed result
        return ChargesSearchResult(
            hits=[
                AirbyteSearchHit[ChargesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ChargesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



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



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> SubscriptionsApiSearchResult:
        """
        Search for subscriptions using Stripe's Search Query Language

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            SubscriptionsApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("subscriptions", "api_search", params)
        # Cast generic envelope to concrete typed result
        return SubscriptionsApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: SubscriptionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SubscriptionsSearchResult:
        """
        Search subscriptions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SubscriptionsSearchFilter):
        - application: For Connect platforms, the application associated with the subscription.
        - application_fee_percent: For Connect platforms, the percentage of the subscription amount taken as an application fee.
        - automatic_tax: Automatic tax calculation settings for the subscription.
        - billing: Billing mode configuration for the subscription.
        - billing_cycle_anchor: Timestamp determining when the billing cycle for the subscription starts.
        - billing_cycle_anchor_config: Configuration for the subscription's billing cycle anchor behavior.
        - billing_thresholds: Defines thresholds at which an invoice will be sent, controlling billing timing based on usage.
        - cancel_at: Timestamp indicating when the subscription is scheduled to be canceled.
        - cancel_at_period_end: Boolean indicating whether the subscription will be canceled at the end of the current billing period.
        - canceled_at: Timestamp indicating when the subscription was canceled, if applicable.
        - cancellation_details: Details about why and how the subscription was canceled.
        - collection_method: How invoices are collected (charge_automatically or send_invoice).
        - created: Timestamp indicating when the subscription was created.
        - currency: Three-letter ISO currency code in lowercase indicating the currency for the subscription.
        - current_period_end: Timestamp marking the end of the current billing period.
        - current_period_start: Timestamp marking the start of the current billing period.
        - customer: ID of the customer who owns the subscription, expandable to full customer object.
        - days_until_due: Number of days until the invoice is due for subscriptions using send_invoice collection method.
        - default_payment_method: ID of the default payment method for the subscription, taking precedence over default_source.
        - default_source: ID of the default payment source for the subscription.
        - default_tax_rates: Tax rates that apply to the subscription by default.
        - description: Human-readable description of the subscription, displayable to the customer.
        - discount: Describes any discount currently applied to the subscription.
        - ended_at: Timestamp indicating when the subscription ended, if applicable.
        - id: Unique identifier for the subscription object.
        - invoice_settings: Settings for invoices generated by this subscription, such as custom fields and footer.
        - is_deleted: Indicates whether the subscription has been deleted.
        - items: List of subscription items, each with an attached price defining what the customer is subscribed to.
        - latest_invoice: The most recent invoice this subscription has generated, expandable to full invoice object.
        - livemode: Indicates whether the subscription exists in live mode (true) or test mode (false).
        - metadata: Set of key-value pairs that you can attach to the subscription for storing additional structured information.
        - next_pending_invoice_item_invoice: Timestamp when the next invoice for pending invoice items will be created.
        - object: String representing the object type, always 'subscription'.
        - on_behalf_of: For Connect platforms, the account for which the subscription is being created or managed.
        - pause_collection: Configuration for pausing collection on the subscription while retaining the subscription structure.
        - payment_settings: Payment settings for invoices generated by this subscription.
        - pending_invoice_item_interval: Specifies an interval for aggregating usage records into pending invoice items.
        - pending_setup_intent: SetupIntent used for collecting user authentication when updating payment methods without immediate payment.
        - pending_update: If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid.
        - plan: The plan associated with the subscription (deprecated, use items instead).
        - quantity: Quantity of the plan subscribed to (deprecated, use items instead).
        - schedule: ID of the subscription schedule managing this subscription's lifecycle, if applicable.
        - start_date: Timestamp indicating when the subscription started.
        - status: Current status of the subscription (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused).
        - tax_percent: The percentage of tax applied to the subscription (deprecated, use default_tax_rates instead).
        - test_clock: ID of the test clock associated with this subscription for simulating time-based scenarios.
        - transfer_data: For Connect platforms, the account receiving funds from the subscription and optional percentage transferred.
        - trial_end: Timestamp indicating when the trial period ends, if applicable.
        - trial_settings: Settings related to trial periods, including conditions for ending trials.
        - trial_start: Timestamp indicating when the trial period began, if applicable.
        - updated: Timestamp indicating when the subscription was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SubscriptionsSearchResult with hits (list of AirbyteSearchHit[SubscriptionsSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("subscriptions", "search", params)

        # Parse response into typed result
        return SubscriptionsSearchResult(
            hits=[
                AirbyteSearchHit[SubscriptionsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=SubscriptionsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def create(
        self,
        **kwargs
    ) -> Refund:
        """
        When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it. Creating a new refund will refund a charge that has previously been created but not yet refunded.

        Returns:
            Refund
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("refunds", "create", params)
        return result



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



    async def search(
        self,
        query: RefundsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> RefundsSearchResult:
        """
        Search refunds records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (RefundsSearchFilter):
        - amount: Amount refunded, in cents (the smallest currency unit).
        - balance_transaction: ID of the balance transaction that describes the impact of this refund on your account balance.
        - charge: ID of the charge that was refunded.
        - created: Timestamp indicating when the refund was created.
        - currency: Three-letter ISO currency code in lowercase representing the currency of the refund.
        - destination_details: Details about the destination where the refunded funds should be sent.
        - id: Unique identifier for the refund object.
        - metadata: Set of key-value pairs that you can attach to an object for storing additional structured information.
        - object: String representing the object type, always 'refund'.
        - payment_intent: ID of the PaymentIntent that was refunded.
        - reason: Reason for the refund, either user-provided (duplicate, fraudulent, or requested_by_customer) or generated by Stripe internally (expired_uncaptured_charge).
        - receipt_number: The transaction number that appears on email receipts sent for this refund.
        - source_transfer_reversal: ID of the transfer reversal that was created as a result of refunding a transfer (Connect only).
        - status: Status of the refund (pending, requires_action, succeeded, failed, or canceled).
        - transfer_reversal: ID of the reversal of the transfer that funded the charge being refunded (Connect only).
        - updated: Timestamp indicating when the refund was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            RefundsSearchResult with hits (list of AirbyteSearchHit[RefundsSearchData]) and pagination info

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("refunds", "search", params)

        # Parse response into typed result
        return RefundsSearchResult(
            hits=[
                AirbyteSearchHit[RefundsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=RefundsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def create(
        self,
        **kwargs
    ) -> Product:
        """
        Creates a new product object. Your product's name, description, and other information will be displayed in all product and invoice displays.

        Returns:
            Product
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "create", params)
        return result



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



    async def update(
        self,
        id: str | None = None,
        **kwargs
    ) -> Product:
        """
        Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

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

        result = await self._connector.execute("products", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProductDeletedResponse:
        """
        Deletes a product. Deleting a product is only possible if it has no prices associated with it.

        Args:
            id: The product ID
            **kwargs: Additional parameters

        Returns:
            ProductDeletedResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "delete", params)
        return result



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> ProductsApiSearchResult:
        """
        Search for products using Stripe's Search Query Language.

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            ProductsApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ProductsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



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
            meta=result.meta
        )



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
            meta=result.meta
        )



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



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        page: str | None = None,
        **kwargs
    ) -> PaymentIntentsApiSearchResult:
        """
        Search for payment intents using Stripe's Search Query Language.

        Args:
            query: The search query string using Stripe's Search Query Language
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            **kwargs: Additional parameters

        Returns:
            PaymentIntentsApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payment_intents", "api_search", params)
        # Cast generic envelope to concrete typed result
        return PaymentIntentsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



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
            meta=result.meta
        )



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
            meta=result.meta
        )



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


