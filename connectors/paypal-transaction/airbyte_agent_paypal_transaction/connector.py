"""
Paypal-Transaction connector.
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

from pydantic import BaseModel

from .connector_model import PaypalTransactionConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    BalancesListParams,
    ListDisputesListParams,
    ListPaymentsListParams,
    ListProductsListParams,
    SearchInvoicesListParams,
    SearchInvoicesListParamsCreationDateRange,
    ShowProductDetailsGetParams,
    TransactionsListParams,
    AirbyteSearchParams,
    TransactionsSearchFilter,
    TransactionsSearchQuery,
    BalancesSearchFilter,
    BalancesSearchQuery,
    ListProductsSearchFilter,
    ListProductsSearchQuery,
    ShowProductDetailsSearchFilter,
    ShowProductDetailsSearchQuery,
    ListDisputesSearchFilter,
    ListDisputesSearchQuery,
    SearchInvoicesSearchFilter,
    SearchInvoicesSearchQuery,
    ListPaymentsSearchFilter,
    ListPaymentsSearchQuery,
)
from .models import PaypalTransactionAuthConfig
if TYPE_CHECKING:
    from .models import PaypalTransactionReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    PaypalTransactionCheckResult,
    PaypalTransactionExecuteResult,
    PaypalTransactionExecuteResultWithMeta,
    BalancesListResult,
    TransactionsListResult,
    ListPaymentsListResult,
    ListDisputesListResult,
    ListProductsListResult,
    SearchInvoicesListResult,
    BalancesResponse,
    Dispute,
    Invoice,
    Payment,
    Product,
    ProductDetails,
    Transaction,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    TransactionsSearchData,
    TransactionsSearchResult,
    BalancesSearchData,
    BalancesSearchResult,
    ListProductsSearchData,
    ListProductsSearchResult,
    ShowProductDetailsSearchData,
    ShowProductDetailsSearchResult,
    ListDisputesSearchData,
    ListDisputesSearchResult,
    SearchInvoicesSearchData,
    SearchInvoicesSearchResult,
    ListPaymentsSearchData,
    ListPaymentsSearchResult,
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




class PaypalTransactionConnector:
    """
    Type-safe Paypal-Transaction API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "paypal-transaction"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("balances", "list"): True,
        ("transactions", "list"): True,
        ("list_payments", "list"): True,
        ("list_disputes", "list"): True,
        ("list_products", "list"): True,
        ("show_product_details", "get"): None,
        ("search_invoices", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('balances', 'list'): {'as_of_time': 'as_of_time', 'currency_code': 'currency_code'},
        ('transactions', 'list'): {'start_date': 'start_date', 'end_date': 'end_date', 'transaction_id': 'transaction_id', 'transaction_type': 'transaction_type', 'transaction_status': 'transaction_status', 'transaction_currency': 'transaction_currency', 'fields': 'fields', 'page_size': 'page_size', 'page': 'page', 'balance_affecting_records_only': 'balance_affecting_records_only'},
        ('list_payments', 'list'): {'start_time': 'start_time', 'end_time': 'end_time', 'count': 'count', 'start_id': 'start_id'},
        ('list_disputes', 'list'): {'update_time_after': 'update_time_after', 'update_time_before': 'update_time_before', 'page_size': 'page_size', 'next_page_token': 'next_page_token'},
        ('list_products', 'list'): {'page_size': 'page_size', 'page': 'page'},
        ('show_product_details', 'get'): {'id': 'id'},
        ('search_invoices', 'list'): {'creation_date_range': 'creation_date_range', 'page_size': 'page_size', 'page': 'page'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (PaypalTransactionAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: PaypalTransactionAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new paypal-transaction connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., PaypalTransactionAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = PaypalTransactionConnector(auth_config=PaypalTransactionAuthConfig(client_id="...", client_secret="...", access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = PaypalTransactionConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = PaypalTransactionConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                customer_name=auth_config.customer_name,
                organization_id=auth_config.organization_id,
                connector_definition_id=str(PaypalTransactionConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or PaypalTransactionAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=PaypalTransactionConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.balances = BalancesQuery(self)
        self.transactions = TransactionsQuery(self)
        self.list_payments = ListPaymentsQuery(self)
        self.list_disputes = ListDisputesQuery(self)
        self.list_products = ListProductsQuery(self)
        self.show_product_details = ShowProductDetailsQuery(self)
        self.search_invoices = SearchInvoicesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["balances"],
        action: Literal["list"],
        params: "BalancesListParams"
    ) -> "BalancesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactions"],
        action: Literal["list"],
        params: "TransactionsListParams"
    ) -> "TransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["list_payments"],
        action: Literal["list"],
        params: "ListPaymentsListParams"
    ) -> "ListPaymentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["list_disputes"],
        action: Literal["list"],
        params: "ListDisputesListParams"
    ) -> "ListDisputesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["list_products"],
        action: Literal["list"],
        params: "ListProductsListParams"
    ) -> "ListProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["show_product_details"],
        action: Literal["get"],
        params: "ShowProductDetailsGetParams"
    ) -> "ProductDetails": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_invoices"],
        action: Literal["list"],
        params: "SearchInvoicesListParams"
    ) -> "SearchInvoicesListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> PaypalTransactionExecuteResult[Any] | PaypalTransactionExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
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
                return PaypalTransactionExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return PaypalTransactionExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> PaypalTransactionCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            PaypalTransactionCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return PaypalTransactionCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return PaypalTransactionCheckResult(
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
            @PaypalTransactionConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @PaypalTransactionConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    PaypalTransactionConnectorModel,
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
        return describe_entities(PaypalTransactionConnectorModel)

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
            (e for e in PaypalTransactionConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in PaypalTransactionConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await PaypalTransactionConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def get_consent_url(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        redirect_url: str,
        name: str | None = None,
        replication_config: "PaypalTransactionReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + customer_name.
            replication_config: Typed replication settings. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await PaypalTransactionConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Paypal-Transaction Source",
                replication_config=PaypalTransactionReplicationConfig(start_date="..."),
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for get_consent_url()")

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(PaypalTransactionConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                redirect_url=redirect_url,
                name=name,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        return consent_url

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "PaypalTransactionAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "PaypalTransactionReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "PaypalTransactionConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A PaypalTransactionConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await PaypalTransactionConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=PaypalTransactionAuthConfig(client_id="...", client_secret="...", access_token="..."),
            )

            # With replication config (required for this connector):
            connector = await PaypalTransactionConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=PaypalTransactionAuthConfig(client_id="...", client_secret="...", access_token="..."),
                replication_config=PaypalTransactionReplicationConfig(start_date="..."),
            )

            # With server-side OAuth:
            connector = await PaypalTransactionConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=PaypalTransactionReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")

        # Validate: exactly one of auth_config or server_side_oauth_secret_id required
        if auth_config is None and server_side_oauth_secret_id is None:
            raise ValueError(
                "Either auth_config or server_side_oauth_secret_id must be provided"
            )
        if auth_config is not None and server_side_oauth_secret_id is not None:
            raise ValueError(
                "Cannot provide both auth_config and server_side_oauth_secret_id"
            )

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(PaypalTransactionConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
                replication_config=replication_config_dict,
                server_side_oauth_secret_id=server_side_oauth_secret_id,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )




class BalancesQuery:
    """
    Query class for Balances entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        as_of_time: str | None = None,
        currency_code: str | None = None,
        **kwargs
    ) -> BalancesListResult:
        """
        List all balances for a PayPal account. Specify date time to list balances for that time. It takes a maximum of three hours for balances to appear. Lists balances up to the previous three years.


        Args:
            as_of_time: List balances at the date time provided in ISO 8601 format. Returns the last refreshed balance when not provided.

            currency_code: Three-character ISO-4217 currency code to filter balances.

            **kwargs: Additional parameters

        Returns:
            BalancesListResult
        """
        params = {k: v for k, v in {
            "as_of_time": as_of_time,
            "currency_code": currency_code,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("balances", "list", params)
        # Cast generic envelope to concrete typed result
        return BalancesListResult(
            data=result.data
        )



    async def search(
        self,
        query: BalancesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BalancesSearchResult:
        """
        Search balances records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BalancesSearchFilter):
        - account_id: The unique identifier of the account.
        - as_of_time: The timestamp when the balances data was reported.
        - balances: Object containing information about the account balances.
        - last_refresh_time: The timestamp when the balances data was last refreshed.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BalancesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("balances", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BalancesSearchResult(
            data=[
                BalancesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TransactionsQuery:
    """
    Query class for Transactions entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        transaction_id: str | None = None,
        transaction_type: str | None = None,
        transaction_status: str | None = None,
        transaction_currency: str | None = None,
        fields: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        balance_affecting_records_only: str | None = None,
        **kwargs
    ) -> TransactionsListResult:
        """
        Lists transactions for a PayPal account. Specify one or more query parameters to filter the transactions. Requires start_date and end_date parameters. The maximum supported date range is 31 days. It takes a maximum of three hours for executed transactions to appear.


        Args:
            start_date: Start date and time in ISO 8601 format. Seconds are required.

            end_date: End date and time in ISO 8601 format. Seconds are required. Maximum supported range is 31 days.

            transaction_id: Filters by PayPal transaction ID (17-19 characters).
            transaction_type: Filters by PayPal transaction event code.
            transaction_status: Filters by PayPal transaction status code. D=Denied, P=Pending, S=Successful, V=Reversed.

            transaction_currency: Three-character ISO-4217 currency code.
            fields: Fields to include in the response. Comma-separated list. Use 'all' to include all fields. Default is transaction_info.

            page_size: Number of items per page (1-500).
            page: Page number to return.
            balance_affecting_records_only: Y to include only balance-impacting transactions (default). N to include all transactions.

            **kwargs: Additional parameters

        Returns:
            TransactionsListResult
        """
        params = {k: v for k, v in {
            "start_date": start_date,
            "end_date": end_date,
            "transaction_id": transaction_id,
            "transaction_type": transaction_type,
            "transaction_status": transaction_status,
            "transaction_currency": transaction_currency,
            "fields": fields,
            "page_size": page_size,
            "page": page,
            "balance_affecting_records_only": balance_affecting_records_only,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactions", "list", params)
        # Cast generic envelope to concrete typed result
        return TransactionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: TransactionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TransactionsSearchResult:
        """
        Search transactions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TransactionsSearchFilter):
        - auction_info: Information related to an auction
        - cart_info: Details of items in the cart
        - incentive_info: Details of any incentives applied
        - payer_info: Information about the payer
        - shipping_info: Shipping information
        - store_info: Information about the store
        - transaction_id: Unique ID of the transaction
        - transaction_info: Detailed information about the transaction
        - transaction_initiation_date: Date and time when the transaction was initiated
        - transaction_updated_date: Date and time when the transaction was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TransactionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("transactions", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TransactionsSearchResult(
            data=[
                TransactionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ListPaymentsQuery:
    """
    Query class for ListPayments entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_time: str | None = None,
        end_time: str | None = None,
        count: int | None = None,
        start_id: str | None = None,
        **kwargs
    ) -> ListPaymentsListResult:
        """
        Lists payments for the PayPal account. Supports filtering by start and end times.


        Args:
            start_time: Start time in ISO 8601 format.
            end_time: End time in ISO 8601 format.
            count: Number of items per page (max 20).
            start_id: Starting resource ID for pagination.
            **kwargs: Additional parameters

        Returns:
            ListPaymentsListResult
        """
        params = {k: v for k, v in {
            "start_time": start_time,
            "end_time": end_time,
            "count": count,
            "start_id": start_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_payments", "list", params)
        # Cast generic envelope to concrete typed result
        return ListPaymentsListResult(
            data=result.data
        )



    async def search(
        self,
        query: ListPaymentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListPaymentsSearchResult:
        """
        Search list_payments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListPaymentsSearchFilter):
        - cart: Details of the cart associated with the payment.
        - create_time: The date and time when the payment was created.
        - id: Unique identifier for the payment.
        - intent: The intention or purpose behind the payment.
        - links: Collection of links related to the payment
        - payer: Details of the payer who made the payment
        - state: The state of the payment.
        - transactions: List of transactions associated with the payment
        - update_time: The date and time when the payment was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListPaymentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("list_payments", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ListPaymentsSearchResult(
            data=[
                ListPaymentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ListDisputesQuery:
    """
    Query class for ListDisputes entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        update_time_after: str | None = None,
        update_time_before: str | None = None,
        page_size: int | None = None,
        next_page_token: str | None = None,
        **kwargs
    ) -> ListDisputesListResult:
        """
        Lists disputes for the PayPal account. Supports filtering by update time range.


        Args:
            update_time_after: Filter disputes updated after this time in ISO 8601 format.
            update_time_before: Filter disputes updated before this time in ISO 8601 format.
            page_size: Number of items per page (max 50).
            next_page_token: Token for retrieving the next page of results.
            **kwargs: Additional parameters

        Returns:
            ListDisputesListResult
        """
        params = {k: v for k, v in {
            "update_time_after": update_time_after,
            "update_time_before": update_time_before,
            "page_size": page_size,
            "next_page_token": next_page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_disputes", "list", params)
        # Cast generic envelope to concrete typed result
        return ListDisputesListResult(
            data=result.data
        )



    async def search(
        self,
        query: ListDisputesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListDisputesSearchResult:
        """
        Search list_disputes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListDisputesSearchFilter):
        - create_time: The timestamp when the dispute was created.
        - dispute_amount: Details about the disputed amount.
        - dispute_channel: The channel through which the dispute was initiated.
        - dispute_id: The unique identifier for the dispute.
        - dispute_life_cycle_stage: The stage in the life cycle of the dispute.
        - dispute_state: The current state of the dispute.
        - disputed_transactions: Details of transactions involved in the dispute.
        - links: Links related to the dispute.
        - outcome: The outcome of the dispute resolution.
        - reason: The reason for the dispute.
        - status: The current status of the dispute.
        - update_time: The timestamp when the dispute was last updated.
        - updated_time_cut: The cut-off timestamp for the last update.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListDisputesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("list_disputes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ListDisputesSearchResult(
            data=[
                ListDisputesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ListProductsQuery:
    """
    Query class for ListProducts entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> ListProductsListResult:
        """
        Lists all catalog products for the PayPal account.

        Args:
            page_size: Number of items per page (max 20).
            page: Page number starting from 1.
            **kwargs: Additional parameters

        Returns:
            ListProductsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_products", "list", params)
        # Cast generic envelope to concrete typed result
        return ListProductsListResult(
            data=result.data
        )



    async def search(
        self,
        query: ListProductsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListProductsSearchResult:
        """
        Search list_products records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListProductsSearchFilter):
        - create_time: The time when the product was created
        - description: Detailed information or features of the product
        - id: Unique identifier for the product
        - links: List of links related to the fetched products.
        - name: The name or title of the product

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListProductsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("list_products", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ListProductsSearchResult(
            data=[
                ListProductsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ShowProductDetailsQuery:
    """
    Query class for ShowProductDetails entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProductDetails:
        """
        Shows details for a catalog product by ID.

        Args:
            id: Product ID.
            **kwargs: Additional parameters

        Returns:
            ProductDetails
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("show_product_details", "get", params)
        return result



    async def search(
        self,
        query: ShowProductDetailsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ShowProductDetailsSearchResult:
        """
        Search show_product_details records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ShowProductDetailsSearchFilter):
        - category: The category to which the product belongs
        - create_time: The date and time when the product was created
        - description: The detailed description of the product
        - home_url: The URL for the home page of the product
        - id: The unique identifier for the product
        - image_url: The URL to the image representing the product
        - links: Contains links related to the product details.
        - name: The name of the product
        - type_: The type or category of the product
        - update_time: The date and time when the product was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ShowProductDetailsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("show_product_details", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ShowProductDetailsSearchResult(
            data=[
                ShowProductDetailsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchInvoicesQuery:
    """
    Query class for SearchInvoices entity operations.
    """

    def __init__(self, connector: PaypalTransactionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        creation_date_range: SearchInvoicesListParamsCreationDateRange | None = None,
        page_size: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> SearchInvoicesListResult:
        """
        Searches for invoices matching the specified criteria. Uses POST with a JSON body for filtering.


        Args:
            creation_date_range: Filter by invoice creation date range.
            page_size: Number of items per page (max 100).
            page: Page number starting from 1.
            **kwargs: Additional parameters

        Returns:
            SearchInvoicesListResult
        """
        params = {k: v for k, v in {
            "creation_date_range": creation_date_range,
            "page_size": page_size,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_invoices", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchInvoicesListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchInvoicesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchInvoicesSearchResult:
        """
        Search search_invoices records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchInvoicesSearchFilter):
        - additional_recipients: List of additional recipients associated with the invoice
        - amount: Detailed breakdown of the invoice amount
        - configuration: Configuration settings related to the invoice
        - detail: Detailed information about the invoice
        - due_amount: Due amount remaining to be paid for the invoice
        - gratuity: Gratuity amount included in the invoice
        - id: Unique identifier of the invoice
        - invoicer: Information about the invoicer associated with the invoice
        - last_update_time: Date and time of the last update made to the invoice
        - links: Links associated with the invoice
        - payments: Payment transactions associated with the invoice
        - primary_recipients: Primary recipients associated with the invoice
        - refunds: Refund transactions associated with the invoice
        - status: Current status of the invoice

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchInvoicesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_invoices", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchInvoicesSearchResult(
            data=[
                SearchInvoicesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
