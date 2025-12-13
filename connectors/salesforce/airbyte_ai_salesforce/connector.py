"""
salesforce connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    AccountsGetParams,
    AccountsListParams,
    AccountsSearchParams,
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    AttachmentsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    CampaignsSearchParams,
    CasesGetParams,
    CasesListParams,
    CasesSearchParams,
    ContactsGetParams,
    ContactsListParams,
    ContactsSearchParams,
    ContentVersionsDownloadParams,
    ContentVersionsGetParams,
    ContentVersionsListParams,
    EventsGetParams,
    EventsListParams,
    EventsSearchParams,
    LeadsGetParams,
    LeadsListParams,
    LeadsSearchParams,
    NotesGetParams,
    NotesListParams,
    NotesSearchParams,
    OpportunitiesGetParams,
    OpportunitiesListParams,
    OpportunitiesSearchParams,
    QueryListParams,
    TasksGetParams,
    TasksListParams,
    TasksSearchParams,
)

if TYPE_CHECKING:
    from .models import SalesforceAuthConfig
# Import response models and envelope models at runtime
from .models import (
    SalesforceExecuteResult,
    SalesforceExecuteResultWithMeta,
    Account,
    AccountQueryResult,
    Attachment,
    AttachmentQueryResult,
    Campaign,
    CampaignQueryResult,
    Case,
    CaseQueryResult,
    Contact,
    ContactQueryResult,
    ContentVersion,
    ContentVersionQueryResult,
    Event,
    EventQueryResult,
    Lead,
    LeadQueryResult,
    Note,
    NoteQueryResult,
    Opportunity,
    OpportunityQueryResult,
    QueryResult,
    SearchResult,
    Task,
    TaskQueryResult,
)


class SalesforceConnector:
    """
    Type-safe Salesforce API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "salesforce"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("accounts", "list"): False,
        ("accounts", "get"): False,
        ("accounts", "search"): False,
        ("contacts", "list"): False,
        ("contacts", "get"): False,
        ("contacts", "search"): False,
        ("leads", "list"): False,
        ("leads", "get"): False,
        ("leads", "search"): False,
        ("opportunities", "list"): False,
        ("opportunities", "get"): False,
        ("opportunities", "search"): False,
        ("tasks", "list"): False,
        ("tasks", "get"): False,
        ("tasks", "search"): False,
        ("events", "list"): False,
        ("events", "get"): False,
        ("events", "search"): False,
        ("campaigns", "list"): False,
        ("campaigns", "get"): False,
        ("campaigns", "search"): False,
        ("cases", "list"): False,
        ("cases", "get"): False,
        ("cases", "search"): False,
        ("notes", "list"): False,
        ("notes", "get"): False,
        ("notes", "search"): False,
        ("content_versions", "list"): False,
        ("content_versions", "get"): False,
        ("content_versions", "download"): False,
        ("attachments", "list"): False,
        ("attachments", "get"): False,
        ("attachments", "download"): False,
        ("query", "list"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('accounts', 'list'): {'q': 'q'},
        ('accounts', 'get'): {'id': 'id', 'fields': 'fields'},
        ('accounts', 'search'): {'q': 'q'},
        ('contacts', 'list'): {'q': 'q'},
        ('contacts', 'get'): {'id': 'id', 'fields': 'fields'},
        ('contacts', 'search'): {'q': 'q'},
        ('leads', 'list'): {'q': 'q'},
        ('leads', 'get'): {'id': 'id', 'fields': 'fields'},
        ('leads', 'search'): {'q': 'q'},
        ('opportunities', 'list'): {'q': 'q'},
        ('opportunities', 'get'): {'id': 'id', 'fields': 'fields'},
        ('opportunities', 'search'): {'q': 'q'},
        ('tasks', 'list'): {'q': 'q'},
        ('tasks', 'get'): {'id': 'id', 'fields': 'fields'},
        ('tasks', 'search'): {'q': 'q'},
        ('events', 'list'): {'q': 'q'},
        ('events', 'get'): {'id': 'id', 'fields': 'fields'},
        ('events', 'search'): {'q': 'q'},
        ('campaigns', 'list'): {'q': 'q'},
        ('campaigns', 'get'): {'id': 'id', 'fields': 'fields'},
        ('campaigns', 'search'): {'q': 'q'},
        ('cases', 'list'): {'q': 'q'},
        ('cases', 'get'): {'id': 'id', 'fields': 'fields'},
        ('cases', 'search'): {'q': 'q'},
        ('notes', 'list'): {'q': 'q'},
        ('notes', 'get'): {'id': 'id', 'fields': 'fields'},
        ('notes', 'search'): {'q': 'q'},
        ('content_versions', 'list'): {'q': 'q'},
        ('content_versions', 'get'): {'id': 'id', 'fields': 'fields'},
        ('content_versions', 'download'): {'id': 'id', 'range_header': 'range_header'},
        ('attachments', 'list'): {'q': 'q'},
        ('attachments', 'get'): {'id': 'id', 'fields': 'fields'},
        ('attachments', 'download'): {'id': 'id', 'range_header': 'range_header'},
        ('query', 'list'): {'q': 'q'},
    }

    def __init__(
        self,
        auth_config: SalesforceAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None,
        instance_url: str | None = None    ):
        """
        Initialize a new salesforce connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            instance_url: Your Salesforce instance URL (e.g., https://na1.salesforce.com)
        Examples:
            # Local mode (direct API calls)
            connector = SalesforceConnector(auth_config=SalesforceAuthConfig(refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = SalesforceConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = SalesforceConnector(
                auth_config=SalesforceAuthConfig(access_token="...", refresh_token="..."),
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
            config_values: dict[str, str] = {}
            if instance_url:
                config_values["instance_url"] = instance_url

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if instance_url:
                base_url = base_url.replace("{instance_url}", instance_url)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.accounts = AccountsQuery(self)
        self.contacts = ContactsQuery(self)
        self.leads = LeadsQuery(self)
        self.opportunities = OpportunitiesQuery(self)
        self.tasks = TasksQuery(self)
        self.events = EventsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.cases = CasesQuery(self)
        self.notes = NotesQuery(self)
        self.content_versions = ContentVersionsQuery(self)
        self.attachments = AttachmentsQuery(self)
        self.query = QueryQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["list"],
        params: "AccountsListParams"
    ) -> "AccountQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams"
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["search"],
        params: "AccountsSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["list"],
        params: "ContactsListParams"
    ) -> "ContactQueryResult": ...

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
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["list"],
        params: "LeadsListParams"
    ) -> "LeadQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["get"],
        params: "LeadsGetParams"
    ) -> "Lead": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["search"],
        params: "LeadsSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["list"],
        params: "OpportunitiesListParams"
    ) -> "OpportunityQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["get"],
        params: "OpportunitiesGetParams"
    ) -> "Opportunity": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["search"],
        params: "OpportunitiesSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["list"],
        params: "TasksListParams"
    ) -> "TaskQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["get"],
        params: "TasksGetParams"
    ) -> "Task": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["search"],
        params: "TasksSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["list"],
        params: "EventsListParams"
    ) -> "EventQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["get"],
        params: "EventsGetParams"
    ) -> "Event": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["search"],
        params: "EventsSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams"
    ) -> "CampaignQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams"
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["search"],
        params: "CampaignsSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["list"],
        params: "CasesListParams"
    ) -> "CaseQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["get"],
        params: "CasesGetParams"
    ) -> "Case": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["search"],
        params: "CasesSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["list"],
        params: "NotesListParams"
    ) -> "NoteQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["get"],
        params: "NotesGetParams"
    ) -> "Note": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["search"],
        params: "NotesSearchParams"
    ) -> "SearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["list"],
        params: "ContentVersionsListParams"
    ) -> "ContentVersionQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["get"],
        params: "ContentVersionsGetParams"
    ) -> "ContentVersion": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["download"],
        params: "ContentVersionsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["list"],
        params: "AttachmentsListParams"
    ) -> "AttachmentQueryResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["get"],
        params: "AttachmentsGetParams"
    ) -> "Attachment": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["download"],
        params: "AttachmentsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["query"],
        action: Literal["list"],
        params: "QueryListParams"
    ) -> "QueryResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> SalesforceExecuteResult[Any] | SalesforceExecuteResultWithMeta[Any, Any] | Any: ...

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
                return SalesforceExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SalesforceExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> AccountQueryResult:
        """
        Returns a list of accounts via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for accounts. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Account ORDER BY LastModifiedDate DESC LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            AccountQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Account:
        """
        Get a single account by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Account ID (18-character ID starting with '001')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Industry,AnnualRevenue,Website"

            **kwargs: Additional parameters

        Returns:
            Account
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for accounts using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields and objects.
Use SOQL (list action) for structured queries with specific field conditions.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} IN scope RETURNING Object(fields) [LIMIT n]
Examples:
- "FIND {Acme} IN ALL FIELDS RETURNING Account(Id,Name)"
- "FIND {tech*} IN NAME FIELDS RETURNING Account(Id,Name,Industry) LIMIT 50"
- "FIND {\"exact phrase\"} RETURNING Account(Id,Name,Website)"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "search", params)
        return result



class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> ContactQueryResult:
        """
        Returns a list of contacts via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for contacts. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Contact WHERE AccountId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            ContactQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Contact ID (18-character ID starting with '003')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,FirstName,LastName,Email,Phone,AccountId"

            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for contacts using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Contact(fields) [LIMIT n]
Examples:
- "FIND {John} IN NAME FIELDS RETURNING Contact(Id,FirstName,LastName,Email)"
- "FIND {*@example.com} IN EMAIL FIELDS RETURNING Contact(Id,Name,Email) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "search", params)
        return result



class LeadsQuery:
    """
    Query class for Leads entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> LeadQueryResult:
        """
        Returns a list of leads via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for leads. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Lead WHERE Status = 'Open' LIMIT 100"

            **kwargs: Additional parameters

        Returns:
            LeadQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Lead:
        """
        Get a single lead by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Lead ID (18-character ID starting with '00Q')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,FirstName,LastName,Email,Company,Status,LeadSource"

            **kwargs: Additional parameters

        Returns:
            Lead
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for leads using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Lead(fields) [LIMIT n]
Examples:
- "FIND {Smith} IN NAME FIELDS RETURNING Lead(Id,FirstName,LastName,Company,Status)"
- "FIND {marketing} IN ALL FIELDS RETURNING Lead(Id,Name,LeadSource) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "search", params)
        return result



class OpportunitiesQuery:
    """
    Query class for Opportunities entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> OpportunityQueryResult:
        """
        Returns a list of opportunities via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for opportunities. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Opportunity WHERE StageName = 'Closed Won' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            OpportunityQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Opportunity:
        """
        Get a single opportunity by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Opportunity ID (18-character ID starting with '006')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Amount,StageName,CloseDate,AccountId"

            **kwargs: Additional parameters

        Returns:
            Opportunity
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for opportunities using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Opportunity(fields) [LIMIT n]
Examples:
- "FIND {Enterprise} IN NAME FIELDS RETURNING Opportunity(Id,Name,Amount,StageName)"
- "FIND {renewal} IN ALL FIELDS RETURNING Opportunity(Id,Name,CloseDate) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "search", params)
        return result



class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> TaskQueryResult:
        """
        Returns a list of tasks via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for tasks. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Task WHERE Status = 'Not Started' LIMIT 100"

            **kwargs: Additional parameters

        Returns:
            TaskQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Task:
        """
        Get a single task by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Task ID (18-character ID starting with '00T')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Subject,Status,Priority,ActivityDate,WhoId,WhatId"

            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for tasks using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Task(fields) [LIMIT n]
Examples:
- "FIND {follow up} IN ALL FIELDS RETURNING Task(Id,Subject,Status,Priority)"
- "FIND {call} IN NAME FIELDS RETURNING Task(Id,Subject,ActivityDate) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "search", params)
        return result



class EventsQuery:
    """
    Query class for Events entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> EventQueryResult:
        """
        Returns a list of events via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for events. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Event WHERE StartDateTime > TODAY LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            EventQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Event:
        """
        Get a single event by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Event ID (18-character ID starting with '00U')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Subject,StartDateTime,EndDateTime,Location,WhoId,WhatId"

            **kwargs: Additional parameters

        Returns:
            Event
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for events using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Event(fields) [LIMIT n]
Examples:
- "FIND {meeting} IN ALL FIELDS RETURNING Event(Id,Subject,StartDateTime,Location)"
- "FIND {demo} IN NAME FIELDS RETURNING Event(Id,Subject,EndDateTime) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "search", params)
        return result



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> CampaignQueryResult:
        """
        Returns a list of campaigns via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for campaigns. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Campaign WHERE IsActive = true LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            CampaignQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Campaign:
        """
        Get a single campaign by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Campaign ID (18-character ID starting with '701')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Type,Status,StartDate,EndDate,IsActive"

            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for campaigns using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Campaign(fields) [LIMIT n]
Examples:
- "FIND {webinar} IN ALL FIELDS RETURNING Campaign(Id,Name,Type,Status)"
- "FIND {2024} IN NAME FIELDS RETURNING Campaign(Id,Name,StartDate,IsActive) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "search", params)
        return result



class CasesQuery:
    """
    Query class for Cases entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> CaseQueryResult:
        """
        Returns a list of cases via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for cases. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Case WHERE Status = 'New' LIMIT 100"

            **kwargs: Additional parameters

        Returns:
            CaseQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Case:
        """
        Get a single case by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Case ID (18-character ID starting with '500')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,CaseNumber,Subject,Status,Priority,ContactId,AccountId"

            **kwargs: Additional parameters

        Returns:
            Case
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for cases using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Case(fields) [LIMIT n]
Examples:
- "FIND {login issue} IN ALL FIELDS RETURNING Case(Id,CaseNumber,Subject,Status)"
- "FIND {urgent} IN NAME FIELDS RETURNING Case(Id,Subject,Priority) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "search", params)
        return result



class NotesQuery:
    """
    Query class for Notes entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> NoteQueryResult:
        """
        Returns a list of notes via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for notes. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Note WHERE ParentId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            NoteQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Note:
        """
        Get a single note by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Note ID (18-character ID starting with '002')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Title,Body,ParentId,OwnerId"

            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "get", params)
        return result



    async def search(
        self,
        q: str,
        **kwargs
    ) -> SearchResult:
        """
        Search for notes using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Note(fields) [LIMIT n]
Examples:
- "FIND {important} IN ALL FIELDS RETURNING Note(Id,Title,ParentId)"
- "FIND {action items} IN NAME FIELDS RETURNING Note(Id,Title,Body) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            SearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "search", params)
        return result



class ContentVersionsQuery:
    """
    Query class for ContentVersions entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> ContentVersionQueryResult:
        """
        Returns a list of content versions (file metadata) via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
Note: ContentVersion does not support FIELDS(STANDARD), so specific fields must be listed.


        Args:
            q: SOQL query for content versions. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT Id, Title, FileExtension, ContentSize FROM ContentVersion WHERE IsLatest = true LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            ContentVersionQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> ContentVersion:
        """
        Get a single content version's metadata by ID. Returns file metadata, not the file content.
Use the download action to retrieve the actual file binary.


        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Title,FileExtension,ContentSize,ContentDocumentId,IsLatest"

            **kwargs: Additional parameters

        Returns:
            ContentVersion
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "get", params)
        return result



    async def download(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.


        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "download", params)
        return result


    async def download_local(
        self,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.
 and save to file.

        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> AttachmentQueryResult:
        """
        Returns a list of attachments (legacy) via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
Note: Attachments are a legacy feature; consider using ContentVersion (Salesforce Files) for new implementations.


        Args:
            q: SOQL query for attachments. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT Id, Name, ContentType, BodyLength, ParentId FROM Attachment WHERE ParentId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            AttachmentQueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Attachment:
        """
        Get a single attachment's metadata by ID. Returns file metadata, not the file content.
Use the download action to retrieve the actual file binary.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.


        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,ContentType,BodyLength,ParentId"

            **kwargs: Additional parameters

        Returns:
            Attachment
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        return result



    async def download(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.


        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_local(
        self,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.
 and save to file.

        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class QueryQuery:
    """
    Query class for Query entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> QueryResult:
        """
        Execute a custom SOQL query and return results. Use this for querying any Salesforce object.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query string. Include LIMIT clause to control the number of records returned.
Examples:
- "SELECT Id, Name FROM Account LIMIT 100"
- "SELECT FIELDS(STANDARD) FROM Contact WHERE AccountId = '001xx...' LIMIT 50"
- "SELECT Id, Subject, Status FROM Case WHERE CreatedDate = TODAY"

            **kwargs: Additional parameters

        Returns:
            QueryResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("query", "list", params)
        return result


