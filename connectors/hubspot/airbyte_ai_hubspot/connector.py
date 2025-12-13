"""
hubspot connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    CompaniesGetParams,
    CompaniesListParams,
    CompaniesSearchParams,
    CompaniesSearchParamsFiltergroupsItem,
    CompaniesSearchParamsSortsItem,
    ContactsGetParams,
    ContactsListParams,
    ContactsSearchParams,
    ContactsSearchParamsFiltergroupsItem,
    ContactsSearchParamsSortsItem,
    DealsGetParams,
    DealsListParams,
    DealsSearchParams,
    DealsSearchParamsFiltergroupsItem,
    DealsSearchParamsSortsItem,
    ObjectsGetParams,
    ObjectsListParams,
    SchemasGetParams,
    SchemasListParams,
    TicketsGetParams,
    TicketsListParams,
    TicketsSearchParams,
    TicketsSearchParamsFiltergroupsItem,
    TicketsSearchParamsSortsItem,
)

if TYPE_CHECKING:
    from .models import HubspotAuthConfig
# Import response models and envelope models at runtime
from .models import (
    HubspotExecuteResult,
    HubspotExecuteResultWithMeta,
    ContactsListResult,
    ContactsSearchResult,
    CompaniesListResult,
    CompaniesSearchResult,
    DealsListResult,
    DealsSearchResult,
    TicketsListResult,
    TicketsSearchResult,
    SchemasListResult,
    ObjectsListResult,
    CRMObject,
    Company,
    Contact,
    Deal,
    Schema,
    Ticket,
)


class HubspotConnector:
    """
    Type-safe Hubspot API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "hubspot"
    connector_version = "0.1.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("contacts", "list"): True,
        ("contacts", "get"): False,
        ("contacts", "search"): True,
        ("companies", "list"): True,
        ("companies", "get"): False,
        ("companies", "search"): True,
        ("deals", "list"): True,
        ("deals", "get"): False,
        ("deals", "search"): True,
        ("tickets", "list"): True,
        ("tickets", "get"): False,
        ("tickets", "search"): True,
        ("schemas", "list"): True,
        ("schemas", "get"): False,
        ("objects", "list"): True,
        ("objects", "get"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('contacts', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('contacts', 'get'): {'contact_id': 'contactId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('contacts', 'search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('companies', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('companies', 'get'): {'company_id': 'companyId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('companies', 'search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('deals', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('deals', 'get'): {'deal_id': 'dealId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('deals', 'search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('tickets', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('tickets', 'get'): {'ticket_id': 'ticketId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('tickets', 'search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('schemas', 'list'): {'archived': 'archived'},
        ('schemas', 'get'): {'object_type': 'objectType'},
        ('objects', 'list'): {'object_type': 'objectType', 'limit': 'limit', 'after': 'after', 'properties': 'properties', 'archived': 'archived', 'associations': 'associations', 'properties_with_history': 'propertiesWithHistory'},
        ('objects', 'get'): {'object_type': 'objectType', 'object_id': 'objectId', 'properties': 'properties', 'archived': 'archived', 'associations': 'associations', 'id_property': 'idProperty', 'properties_with_history': 'propertiesWithHistory'},
    }

    def __init__(
        self,
        auth_config: HubspotAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new hubspot connector instance.

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
            connector = HubspotConnector(auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = HubspotConnector(
                connector_id="connector-456",
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
        self.contacts = ContactsQuery(self)
        self.companies = CompaniesQuery(self)
        self.deals = DealsQuery(self)
        self.tickets = TicketsQuery(self)
        self.schemas = SchemasQuery(self)
        self.objects = ObjectsQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

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
        action: Literal["search"],
        params: "ContactsSearchParams"
    ) -> "ContactsSearchResult": ...

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
        action: Literal["search"],
        params: "CompaniesSearchParams"
    ) -> "CompaniesSearchResult": ...

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
        action: Literal["search"],
        params: "DealsSearchParams"
    ) -> "DealsSearchResult": ...

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
        action: Literal["search"],
        params: "TicketsSearchParams"
    ) -> "TicketsSearchResult": ...

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
        action: str,
        params: dict[str, Any]
    ) -> HubspotExecuteResult[Any] | HubspotExecuteResultWithMeta[Any, Any] | Any: ...

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
                return HubspotExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return HubspotExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



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
            meta=result.meta        )



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



    async def search(
        self,
        filter_groups: list[ContactsSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[ContactsSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> ContactsSearchResult:
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
            ContactsSearchResult
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

        result = await self._connector.execute("contacts", "search", params)
        # Cast generic envelope to concrete typed result
        return ContactsSearchResult(
            data=result.data,
            meta=result.meta        )



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
            meta=result.meta        )



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



    async def search(
        self,
        filter_groups: list[CompaniesSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[CompaniesSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> CompaniesSearchResult:
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
            CompaniesSearchResult
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

        result = await self._connector.execute("companies", "search", params)
        # Cast generic envelope to concrete typed result
        return CompaniesSearchResult(
            data=result.data,
            meta=result.meta        )



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
            meta=result.meta        )



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



    async def search(
        self,
        filter_groups: list[DealsSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[DealsSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> DealsSearchResult:
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
            DealsSearchResult
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

        result = await self._connector.execute("deals", "search", params)
        # Cast generic envelope to concrete typed result
        return DealsSearchResult(
            data=result.data,
            meta=result.meta        )



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
            meta=result.meta        )



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



    async def search(
        self,
        filter_groups: list[TicketsSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[TicketsSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> TicketsSearchResult:
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
            TicketsSearchResult
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

        result = await self._connector.execute("tickets", "search", params)
        # Cast generic envelope to concrete typed result
        return TicketsSearchResult(
            data=result.data,
            meta=result.meta        )



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
            data=result.data        )



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
            meta=result.meta        )



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


