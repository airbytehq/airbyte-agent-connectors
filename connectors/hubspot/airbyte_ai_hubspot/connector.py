"""
Auto-generated hubspot connector. Do not edit manually.

Generated from OpenAPI specification.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from pathlib import Path

if TYPE_CHECKING:
    from .types import (
        CRMObject,
        CompaniesGetParams,
        CompaniesList,
        CompaniesListParams,
        Company,
        Contact,
        ContactsGetParams,
        ContactsList,
        ContactsListParams,
        Deal,
        DealsGetParams,
        DealsList,
        DealsListParams,
        ObjectsGetParams,
        ObjectsList,
        ObjectsListParams,
        SchemasList,
        SchemasListParams,
        Ticket,
        TicketsGetParams,
        TicketsList,
        TicketsListParams,
        HubspotAuthConfig,
    )


class HubspotConnector:
    """
    Type-safe Hubspot API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "hubspot"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

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
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = HubspotConnector(auth_config={"api_key": "sk_..."})
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
                auth_config={"access_token": "...", "refresh_token": "..."},
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
                auth_config=auth_config,
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
    ) -> "ContactsList": ...
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
        entity: Literal["companies"],
        action: Literal["list"],
        params: "CompaniesListParams"
    ) -> "CompaniesList": ...
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
        entity: Literal["deals"],
        action: Literal["list"],
        params: "DealsListParams"
    ) -> "DealsList": ...
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
        entity: Literal["tickets"],
        action: Literal["list"],
        params: "TicketsListParams"
    ) -> "TicketsList": ...
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
        entity: Literal["schemas"],
        action: Literal["list"],
        params: "SchemasListParams"
    ) -> "SchemasList": ...
    @overload
    async def execute(
        self,
        entity: Literal["objects"],
        action: Literal["list"],
        params: "ObjectsListParams"
    ) -> "ObjectsList": ...
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
    ) -> dict[str, Any]: ...

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

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

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
        properties: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> "ContactsList":
        """
        List contacts

        Args:
            limit: Number of items to return per page
            after: Pagination cursor for next page
            properties: Comma-separated list of properties to include
            archived: Whether to include archived contacts
            **kwargs: Additional parameters

        Returns:
            ContactsList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("contacts", "list", params)
    async def get(
        self,
        contactId: str,
        properties: str | None = None,
        **kwargs
    ) -> "Contact":
        """
        Get a contact

        Args:
            contactId: Contact ID
            properties: Comma-separated list of properties to include
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "contactId": contactId,
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("contacts", "get", params)
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
        properties: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> "CompaniesList":
        """
        List companies

        Args:
            limit: Number of items to return per page
            after: Pagination cursor for next page
            properties: Comma-separated list of properties to include
            archived: Whether to include archived companies
            **kwargs: Additional parameters

        Returns:
            CompaniesList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("companies", "list", params)
    async def get(
        self,
        companyId: str,
        properties: str | None = None,
        **kwargs
    ) -> "Company":
        """
        Get a company

        Args:
            companyId: Company ID
            properties: Comma-separated list of properties to include
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "companyId": companyId,
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("companies", "get", params)
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
        properties: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> "DealsList":
        """
        List deals

        Args:
            limit: Number of items to return per page
            after: Pagination cursor for next page
            properties: Comma-separated list of properties to include
            archived: Whether to include archived deals
            **kwargs: Additional parameters

        Returns:
            DealsList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("deals", "list", params)
    async def get(
        self,
        dealId: str,
        properties: str | None = None,
        **kwargs
    ) -> "Deal":
        """
        Get a deal

        Args:
            dealId: Deal ID
            properties: Comma-separated list of properties to include
            **kwargs: Additional parameters

        Returns:
            Deal
        """
        params = {k: v for k, v in {
            "dealId": dealId,
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("deals", "get", params)
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
        properties: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> "TicketsList":
        """
        List tickets

        Args:
            limit: Number of items to return per page
            after: Pagination cursor for next page
            properties: Comma-separated list of properties to include
            archived: Whether to include archived tickets
            **kwargs: Additional parameters

        Returns:
            TicketsList
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("tickets", "list", params)
    async def get(
        self,
        ticketId: str,
        properties: str | None = None,
        **kwargs
    ) -> "Ticket":
        """
        Get a ticket

        Args:
            ticketId: Ticket ID
            properties: Comma-separated list of properties to include
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "ticketId": ticketId,
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("tickets", "get", params)
class SchemasQuery:
    """
    Query class for Schemas entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> "SchemasList":
        """
        List custom object schemas

        Returns:
            SchemasList
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("schemas", "list", params)
class ObjectsQuery:
    """
    Query class for Objects entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        objectType: str,
        limit: int | None = None,
        after: str | None = None,
        properties: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> "ObjectsList":
        """
        List objects

        Args:
            objectType: Object type ID or fully qualified name (e.g., "cars" or "p12345_cars")
            limit: Number of items to return per page
            after: Pagination cursor for next page
            properties: Comma-separated list of properties to include
            archived: Whether to include archived objects
            **kwargs: Additional parameters

        Returns:
            ObjectsList
        """
        params = {k: v for k, v in {
            "objectType": objectType,
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("objects", "list", params)
    async def get(
        self,
        objectType: str,
        objectId: str,
        properties: str | None = None,
        **kwargs
    ) -> "CRMObject":
        """
        Get an object

        Args:
            objectType: Object type ID or fully qualified name
            objectId: Object record ID
            properties: Comma-separated list of properties to include
            **kwargs: Additional parameters

        Returns:
            CRMObject
        """
        params = {k: v for k, v in {
            "objectType": objectType,
            "objectId": objectId,
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("objects", "get", params)