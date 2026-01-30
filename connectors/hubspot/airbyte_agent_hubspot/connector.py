"""
Hubspot connector.
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

from .connector_model import HubspotConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    CompaniesApiSearchParams,
    CompaniesApiSearchParamsFiltergroupsItem,
    CompaniesApiSearchParamsSortsItem,
    CompaniesGetParams,
    CompaniesListParams,
    ContactsApiSearchParams,
    ContactsApiSearchParamsFiltergroupsItem,
    ContactsApiSearchParamsSortsItem,
    ContactsGetParams,
    ContactsListParams,
    DealsApiSearchParams,
    DealsApiSearchParamsFiltergroupsItem,
    DealsApiSearchParamsSortsItem,
    DealsGetParams,
    DealsListParams,
    ObjectsGetParams,
    ObjectsListParams,
    SchemasGetParams,
    SchemasListParams,
    TicketsApiSearchParams,
    TicketsApiSearchParamsFiltergroupsItem,
    TicketsApiSearchParamsSortsItem,
    TicketsGetParams,
    TicketsListParams,
    AirbyteSearchParams,
    CompaniesSearchFilter,
    CompaniesSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    DealsSearchFilter,
    DealsSearchQuery,
)
if TYPE_CHECKING:
    from .models import HubspotAuthConfig

# Import response models and envelope models at runtime
from .models import (
    HubspotCheckResult,
    HubspotExecuteResult,
    HubspotExecuteResultWithMeta,
    ContactsListResult,
    ContactsApiSearchResult,
    CompaniesListResult,
    CompaniesApiSearchResult,
    DealsListResult,
    DealsApiSearchResult,
    TicketsListResult,
    TicketsApiSearchResult,
    SchemasListResult,
    ObjectsListResult,
    CRMObject,
    Company,
    Contact,
    Deal,
    Schema,
    Ticket,
    AirbyteSearchHit,
    AirbyteSearchResult,
    CompaniesSearchData,
    CompaniesSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    DealsSearchData,
    DealsSearchResult,
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




class HubspotConnector:
    """
    Type-safe Hubspot API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "hubspot"
    connector_version = "0.1.9"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("contacts", "api_search"): True,
        ("companies", "list"): True,
        ("companies", "get"): None,
        ("companies", "api_search"): True,
        ("deals", "list"): True,
        ("deals", "get"): None,
        ("deals", "api_search"): True,
        ("tickets", "list"): True,
        ("tickets", "get"): None,
        ("tickets", "api_search"): True,
        ("schemas", "list"): True,
        ("schemas", "get"): None,
        ("objects", "list"): True,
        ("objects", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('contacts', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('contacts', 'get'): {'contact_id': 'contactId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('contacts', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('companies', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('companies', 'get'): {'company_id': 'companyId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('companies', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('deals', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('deals', 'get'): {'deal_id': 'dealId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('deals', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('tickets', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('tickets', 'get'): {'ticket_id': 'ticketId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('tickets', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('schemas', 'list'): {'archived': 'archived'},
        ('schemas', 'get'): {'object_type': 'objectType'},
        ('objects', 'list'): {'object_type': 'objectType', 'limit': 'limit', 'after': 'after', 'properties': 'properties', 'archived': 'archived', 'associations': 'associations', 'properties_with_history': 'propertiesWithHistory'},
        ('objects', 'get'): {'object_type': 'objectType', 'object_id': 'objectId', 'properties': 'properties', 'archived': 'archived', 'associations': 'associations', 'id_property': 'idProperty', 'properties_with_history': 'propertiesWithHistory'},
    }

    def __init__(
        self,
        auth_config: HubspotAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new hubspot connector instance.

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
            connector = HubspotConnector(auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = HubspotConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = HubspotConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = HubspotConnector(
                auth_config=HubspotAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(HubspotConnectorModel.id) if not connector_id else None,
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
                model=HubspotConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.contacts = ContactsQuery(self)
        self.companies = CompaniesQuery(self)
        self.deals = DealsQuery(self)
        self.tickets = TicketsQuery(self)
        self.schemas = SchemasQuery(self)
        self.objects = ObjectsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["list"],
        params: "ContactsListParams"
    ) -> "ContactsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["get"],
        params: "ContactsGetParams"
    ) -> "Contact": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["api_search"],
        params: "ContactsApiSearchParams"
    ) -> "ContactsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["list"],
        params: "CompaniesListParams"
    ) -> "CompaniesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["get"],
        params: "CompaniesGetParams"
    ) -> "Company": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["api_search"],
        params: "CompaniesApiSearchParams"
    ) -> "CompaniesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["list"],
        params: "DealsListParams"
    ) -> "DealsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["get"],
        params: "DealsGetParams"
    ) -> "Deal": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["api_search"],
        params: "DealsApiSearchParams"
    ) -> "DealsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["list"],
        params: "TicketsListParams"
    ) -> "TicketsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["get"],
        params: "TicketsGetParams"
    ) -> "Ticket": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["api_search"],
        params: "TicketsApiSearchParams"
    ) -> "TicketsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["schemas"],
        action: Literal["list"],
        params: "SchemasListParams"
    ) -> "SchemasListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["schemas"],
        action: Literal["get"],
        params: "SchemasGetParams"
    ) -> "Schema": ...

    @overload
    async def execute(
        self,
        entity: Literal["objects"],
        action: Literal["list"],
        params: "ObjectsListParams"
    ) -> "ObjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["objects"],
        action: Literal["get"],
        params: "ObjectsGetParams"
    ) -> "CRMObject": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "api_search", "search"],
        params: Mapping[str, Any]
    ) -> HubspotExecuteResult[Any] | HubspotExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "api_search", "search"],
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
                return HubspotExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return HubspotExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> HubspotCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            HubspotCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return HubspotCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return HubspotCheckResult(
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
            @HubspotConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @HubspotConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    HubspotConnectorModel,
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
        return describe_entities(HubspotConnectorModel)

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
            (e for e in HubspotConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in HubspotConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await HubspotConnector.create_hosted(...)
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
        auth_config: "HubspotAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "HubspotConnector":
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
            A HubspotConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await HubspotConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."),
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
                connector_definition_id=str(HubspotConnectorModel.id),
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



class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a paginated list of contacts

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        contact_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID

        Args:
            contact_id: Contact ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "contactId": contact_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



    async def api_search(
        self,
        filter_groups: list[ContactsApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[ContactsApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> ContactsApiSearchResult:
        """
        Search for contacts by filtering on properties, searching through associations, and sorting results.

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            ContactsApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ContactsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ContactsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ContactsSearchResult:
        """
        Search contacts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ContactsSearchFilter):
        - archived: Boolean flag indicating whether the contact has been archived or deleted.
        - companies: Associated company records linked to this contact.
        - created_at: Timestamp indicating when the contact was first created in the system.
        - id: Unique identifier for the contact record.
        - properties: Key-value object storing all contact properties and their values.
        - updated_at: Timestamp indicating when the contact record was last modified.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ContactsSearchResult with hits (list of AirbyteSearchHit[ContactsSearchData]) and pagination info

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

        result = await self._connector.execute("contacts", "search", params)

        # Parse response into typed result
        return ContactsSearchResult(
            hits=[
                AirbyteSearchHit[ContactsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ContactsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class CompaniesQuery:
    """
    Query class for Companies entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> CompaniesListResult:
        """
        Retrieve all companies, using query parameters to control the information that gets returned.

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            CompaniesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "list", params)
        # Cast generic envelope to concrete typed result
        return CompaniesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        company_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Company:
        """
        Get a single company by ID

        Args:
            company_id: Company ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "companyId": company_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "get", params)
        return result



    async def api_search(
        self,
        filter_groups: list[CompaniesApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[CompaniesApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> CompaniesApiSearchResult:
        """
        Search for companies by filtering on properties, searching through associations, and sorting results.

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            CompaniesApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CompaniesApiSearchResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CompaniesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CompaniesSearchResult:
        """
        Search companies records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CompaniesSearchFilter):
        - archived: Indicates whether the company has been deleted and moved to the recycling bin
        - contacts: Associated contact records linked to this company
        - created_at: Timestamp when the company record was created
        - id: Unique identifier for the company record
        - properties: Object containing all property values for the company
        - updated_at: Timestamp when the company record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CompaniesSearchResult with hits (list of AirbyteSearchHit[CompaniesSearchData]) and pagination info

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

        result = await self._connector.execute("companies", "search", params)

        # Parse response into typed result
        return CompaniesSearchResult(
            hits=[
                AirbyteSearchHit[CompaniesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CompaniesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class DealsQuery:
    """
    Query class for Deals entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> DealsListResult:
        """
        Returns a paginated list of deals

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            DealsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "list", params)
        # Cast generic envelope to concrete typed result
        return DealsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        deal_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Deal:
        """
        Get a single deal by ID

        Args:
            deal_id: Deal ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Deal
        """
        params = {k: v for k, v in {
            "dealId": deal_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "get", params)
        return result



    async def api_search(
        self,
        filter_groups: list[DealsApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[DealsApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> DealsApiSearchResult:
        """
        Search deals with filters and sorting

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            DealsApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "api_search", params)
        # Cast generic envelope to concrete typed result
        return DealsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: DealsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DealsSearchResult:
        """
        Search deals records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DealsSearchFilter):
        - archived: Indicates whether the deal has been deleted and moved to the recycling bin
        - companies: Collection of company records associated with the deal
        - contacts: Collection of contact records associated with the deal
        - created_at: Timestamp when the deal record was originally created
        - id: Unique identifier for the deal record
        - line_items: Collection of product line items associated with the deal
        - properties: Key-value object containing all deal properties and custom fields
        - updated_at: Timestamp when the deal record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DealsSearchResult with hits (list of AirbyteSearchHit[DealsSearchData]) and pagination info

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

        result = await self._connector.execute("deals", "search", params)

        # Parse response into typed result
        return DealsSearchResult(
            hits=[
                AirbyteSearchHit[DealsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=DealsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class TicketsQuery:
    """
    Query class for Tickets entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> TicketsListResult:
        """
        Returns a paginated list of tickets

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            TicketsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        ticket_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Ticket:
        """
        Get a single ticket by ID

        Args:
            ticket_id: Ticket ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "ticketId": ticket_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "get", params)
        return result



    async def api_search(
        self,
        filter_groups: list[TicketsApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[TicketsApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> TicketsApiSearchResult:
        """
        Search for tickets by filtering on properties, searching through associations, and sorting results.

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            TicketsApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "api_search", params)
        # Cast generic envelope to concrete typed result
        return TicketsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



class SchemasQuery:
    """
    Query class for Schemas entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        archived: bool | None = None,
        **kwargs
    ) -> SchemasListResult:
        """
        Returns all custom object schemas to discover available custom objects

        Args:
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            SchemasListResult
        """
        params = {k: v for k, v in {
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schemas", "list", params)
        # Cast generic envelope to concrete typed result
        return SchemasListResult(
            data=result.data
        )



    async def get(
        self,
        object_type: str,
        **kwargs
    ) -> Schema:
        """
        Get the schema for a specific custom object type

        Args:
            object_type: Fully qualified name or object type ID of your schema.
            **kwargs: Additional parameters

        Returns:
            Schema
        """
        params = {k: v for k, v in {
            "objectType": object_type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schemas", "get", params)
        return result



class ObjectsQuery:
    """
    Query class for Objects entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        object_type: str,
        limit: int | None = None,
        after: str | None = None,
        properties: str | None = None,
        archived: bool | None = None,
        associations: str | None = None,
        properties_with_history: str | None = None,
        **kwargs
    ) -> ObjectsListResult:
        """
        Read a page of objects. Control what is returned via the properties query param.

        Args:
            object_type: Object type ID or fully qualified name (e.g., "cars" or "p12345_cars")
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            **kwargs: Additional parameters

        Returns:
            ObjectsListResult
        """
        params = {k: v for k, v in {
            "objectType": object_type,
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            "associations": associations,
            "propertiesWithHistory": properties_with_history,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("objects", "list", params)
        # Cast generic envelope to concrete typed result
        return ObjectsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        object_type: str,
        object_id: str,
        properties: str | None = None,
        archived: bool | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        properties_with_history: str | None = None,
        **kwargs
    ) -> CRMObject:
        """
        Read an Object identified by {objectId}. {objectId} refers to the internal object ID by default, or optionally any unique property value as specified by the idProperty query param. Control what is returned via the properties query param.

        Args:
            object_type: Object type ID or fully qualified name
            object_id: Object record ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            **kwargs: Additional parameters

        Returns:
            CRMObject
        """
        params = {k: v for k, v in {
            "objectType": object_type,
            "objectId": object_id,
            "properties": properties,
            "archived": archived,
            "associations": associations,
            "idProperty": id_property,
            "propertiesWithHistory": properties_with_history,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("objects", "get", params)
        return result


