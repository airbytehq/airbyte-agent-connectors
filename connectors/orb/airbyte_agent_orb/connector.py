"""
Orb connector.
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

from .connector_model import OrbConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    CustomersGetParams,
    CustomersListParams,
    InvoicesGetParams,
    InvoicesListParams,
    PlansGetParams,
    PlansListParams,
    SubscriptionsGetParams,
    SubscriptionsListParams,
    AirbyteSearchParams,
    CustomersSearchFilter,
    CustomersSearchQuery,
    SubscriptionsSearchFilter,
    SubscriptionsSearchQuery,
    PlansSearchFilter,
    PlansSearchQuery,
    InvoicesSearchFilter,
    InvoicesSearchQuery,
)
if TYPE_CHECKING:
    from .models import OrbAuthConfig

# Import response models and envelope models at runtime
from .models import (
    OrbCheckResult,
    OrbExecuteResult,
    OrbExecuteResultWithMeta,
    CustomersListResult,
    SubscriptionsListResult,
    PlansListResult,
    InvoicesListResult,
    Customer,
    Invoice,
    Plan,
    Subscription,
    AirbyteSearchHit,
    AirbyteSearchResult,
    CustomersSearchData,
    CustomersSearchResult,
    SubscriptionsSearchData,
    SubscriptionsSearchResult,
    PlansSearchData,
    PlansSearchResult,
    InvoicesSearchData,
    InvoicesSearchResult,
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




class OrbConnector:
    """
    Type-safe Orb API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "orb"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("customers", "list"): True,
        ("customers", "get"): None,
        ("subscriptions", "list"): True,
        ("subscriptions", "get"): None,
        ("plans", "list"): True,
        ("plans", "get"): None,
        ("invoices", "list"): True,
        ("invoices", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('customers', 'list'): {'limit': 'limit', 'cursor': 'cursor'},
        ('customers', 'get'): {'customer_id': 'customer_id'},
        ('subscriptions', 'list'): {'limit': 'limit', 'cursor': 'cursor', 'customer_id': 'customer_id', 'external_customer_id': 'external_customer_id', 'status': 'status'},
        ('subscriptions', 'get'): {'subscription_id': 'subscription_id'},
        ('plans', 'list'): {'limit': 'limit', 'cursor': 'cursor'},
        ('plans', 'get'): {'plan_id': 'plan_id'},
        ('invoices', 'list'): {'limit': 'limit', 'cursor': 'cursor', 'customer_id': 'customer_id', 'external_customer_id': 'external_customer_id', 'subscription_id': 'subscription_id', 'invoice_date_gt': 'invoice_date_gt', 'invoice_date_gte': 'invoice_date_gte', 'invoice_date_lt': 'invoice_date_lt', 'invoice_date_lte': 'invoice_date_lte', 'status': 'status'},
        ('invoices', 'get'): {'invoice_id': 'invoice_id'},
    }

    def __init__(
        self,
        auth_config: OrbAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new orb connector instance.

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
            connector = OrbConnector(auth_config=OrbAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = OrbConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = OrbConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = OrbConnector(
                auth_config=OrbAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(OrbConnectorModel.id) if not connector_id else None,
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
                model=OrbConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.customers = CustomersQuery(self)
        self.subscriptions = SubscriptionsQuery(self)
        self.plans = PlansQuery(self)
        self.invoices = InvoicesQuery(self)

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
        entity: Literal["plans"],
        action: Literal["list"],
        params: "PlansListParams"
    ) -> "PlansListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["plans"],
        action: Literal["get"],
        params: "PlansGetParams"
    ) -> "Plan": ...

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
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> OrbExecuteResult[Any] | OrbExecuteResultWithMeta[Any, Any] | Any: ...

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
                return OrbExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return OrbExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> OrbCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            OrbCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return OrbCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return OrbCheckResult(
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
            @OrbConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @OrbConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    OrbConnectorModel,
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
        return describe_entities(OrbConnectorModel)

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
            (e for e in OrbConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in OrbConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await OrbConnector.create_hosted(...)
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
        auth_config: "OrbAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "OrbConnector":
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
            A OrbConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await OrbConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=OrbAuthConfig(api_key="..."),
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
                connector_definition_id=str(OrbConnectorModel.id),
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

    def __init__(self, connector: OrbConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> CustomersListResult:
        """
        Returns a paginated list of customers

        Args:
            limit: Number of items to return per page
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CustomersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        customer_id: str,
        **kwargs
    ) -> Customer:
        """
        Get a single customer by ID

        Args:
            customer_id: Customer ID
            **kwargs: Additional parameters

        Returns:
            Customer
        """
        params = {k: v for k, v in {
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "get", params)
        return result



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
        - id: The unique identifier of the customer
        - external_customer_id: The ID of the customer in an external system
        - name: The name of the customer
        - email: The email address of the customer
        - created_at: The date and time when the customer was created
        - payment_provider: The payment provider used by the customer
        - payment_provider_id: The ID of the customer in the payment provider's system
        - timezone: The timezone setting of the customer
        - shipping_address: The shipping address of the customer
        - billing_address: The billing address of the customer
        - balance: The current balance of the customer
        - currency: The currency of the customer
        - auto_collection: Whether auto collection is enabled
        - metadata: Additional metadata for the customer

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

class SubscriptionsQuery:
    """
    Query class for Subscriptions entity operations.
    """

    def __init__(self, connector: OrbConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        external_customer_id: str | None = None,
        status: str | None = None,
        **kwargs
    ) -> SubscriptionsListResult:
        """
        Returns a paginated list of subscriptions

        Args:
            limit: Number of items to return per page
            cursor: Cursor for pagination
            customer_id: Filter subscriptions by customer ID
            external_customer_id: Filter subscriptions by external customer ID
            status: Filter subscriptions by status
            **kwargs: Additional parameters

        Returns:
            SubscriptionsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "cursor": cursor,
            "customer_id": customer_id,
            "external_customer_id": external_customer_id,
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
        subscription_id: str,
        **kwargs
    ) -> Subscription:
        """
        Get a single subscription by ID

        Args:
            subscription_id: Subscription ID
            **kwargs: Additional parameters

        Returns:
            Subscription
        """
        params = {k: v for k, v in {
            "subscription_id": subscription_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("subscriptions", "get", params)
        return result



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
        - id: The unique identifier of the subscription
        - created_at: The date and time when the subscription was created
        - start_date: The date and time when the subscription starts
        - end_date: The date and time when the subscription ends
        - status: The current status of the subscription
        - customer: The customer associated with the subscription
        - plan: The plan associated with the subscription
        - current_billing_period_start_date: The start date of the current billing period
        - current_billing_period_end_date: The end date of the current billing period
        - auto_collection: Whether auto collection is enabled
        - net_terms: The net terms for the subscription
        - metadata: Additional metadata for the subscription

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

class PlansQuery:
    """
    Query class for Plans entity operations.
    """

    def __init__(self, connector: OrbConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> PlansListResult:
        """
        Returns a paginated list of plans

        Args:
            limit: Number of items to return per page
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            PlansListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("plans", "list", params)
        # Cast generic envelope to concrete typed result
        return PlansListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        plan_id: str,
        **kwargs
    ) -> Plan:
        """
        Get a single plan by ID

        Args:
            plan_id: Plan ID
            **kwargs: Additional parameters

        Returns:
            Plan
        """
        params = {k: v for k, v in {
            "plan_id": plan_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("plans", "get", params)
        return result



    async def search(
        self,
        query: PlansSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PlansSearchResult:
        """
        Search plans records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PlansSearchFilter):
        - id: The unique identifier of the plan
        - created_at: The date and time when the plan was created
        - name: The name of the plan
        - description: A description of the plan
        - status: The status of the plan
        - currency: The currency of the plan
        - prices: The pricing options for the plan
        - product: The product associated with the plan
        - external_plan_id: The external plan ID
        - metadata: Additional metadata for the plan

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PlansSearchResult with hits (list of AirbyteSearchHit[PlansSearchData]) and pagination info

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

        result = await self._connector.execute("plans", "search", params)

        # Parse response into typed result
        return PlansSearchResult(
            hits=[
                AirbyteSearchHit[PlansSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=PlansSearchData(**hit.get("data", {}))
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

    def __init__(self, connector: OrbConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        external_customer_id: str | None = None,
        subscription_id: str | None = None,
        invoice_date_gt: str | None = None,
        invoice_date_gte: str | None = None,
        invoice_date_lt: str | None = None,
        invoice_date_lte: str | None = None,
        status: str | None = None,
        **kwargs
    ) -> InvoicesListResult:
        """
        Returns a paginated list of invoices

        Args:
            limit: Number of items to return per page
            cursor: Cursor for pagination
            customer_id: Filter invoices by customer ID
            external_customer_id: Filter invoices by external customer ID
            subscription_id: Filter invoices by subscription ID
            invoice_date_gt: Filter invoices with invoice date greater than this value (ISO 8601 format)
            invoice_date_gte: Filter invoices with invoice date greater than or equal to this value (ISO 8601 format)
            invoice_date_lt: Filter invoices with invoice date less than this value (ISO 8601 format)
            invoice_date_lte: Filter invoices with invoice date less than or equal to this value (ISO 8601 format)
            status: Filter invoices by status
            **kwargs: Additional parameters

        Returns:
            InvoicesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "cursor": cursor,
            "customer_id": customer_id,
            "external_customer_id": external_customer_id,
            "subscription_id": subscription_id,
            "invoice_date_gt": invoice_date_gt,
            "invoice_date_gte": invoice_date_gte,
            "invoice_date_lt": invoice_date_lt,
            "invoice_date_lte": invoice_date_lte,
            "status": status,
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
        invoice_id: str,
        **kwargs
    ) -> Invoice:
        """
        Get a single invoice by ID

        Args:
            invoice_id: Invoice ID
            **kwargs: Additional parameters

        Returns:
            Invoice
        """
        params = {k: v for k, v in {
            "invoice_id": invoice_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "get", params)
        return result



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
        - id: The unique identifier of the invoice
        - created_at: The date and time when the invoice was created
        - invoice_date: The date of the invoice
        - due_date: The due date for the invoice
        - invoice_pdf: The URL to download the PDF version of the invoice
        - subtotal: The subtotal amount of the invoice
        - total: The total amount of the invoice
        - amount_due: The amount due on the invoice
        - status: The current status of the invoice
        - memo: Any additional notes or comments on the invoice
        - paid_at: The date and time when the invoice was paid
        - issued_at: The date and time when the invoice was issued
        - hosted_invoice_url: The URL to view the hosted invoice
        - line_items: The line items on the invoice
        - subscription: The subscription associated with the invoice
        - customer: The customer associated with the invoice
        - currency: The currency of the invoice
        - invoice_number: The invoice number
        - metadata: Additional metadata for the invoice

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
