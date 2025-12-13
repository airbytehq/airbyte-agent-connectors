"""
zendesk-support connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    ArticleAttachmentsDownloadParams,
    ArticleAttachmentsGetParams,
    ArticleAttachmentsListParams,
    ArticlesGetParams,
    ArticlesListParams,
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    AutomationsGetParams,
    AutomationsListParams,
    BrandsGetParams,
    BrandsListParams,
    GroupMembershipsListParams,
    GroupsGetParams,
    GroupsListParams,
    MacrosGetParams,
    MacrosListParams,
    OrganizationMembershipsListParams,
    OrganizationsGetParams,
    OrganizationsListParams,
    SatisfactionRatingsGetParams,
    SatisfactionRatingsListParams,
    SlaPoliciesGetParams,
    SlaPoliciesListParams,
    TagsListParams,
    TicketAuditsListParams,
    TicketCommentsListParams,
    TicketFieldsGetParams,
    TicketFieldsListParams,
    TicketFormsGetParams,
    TicketFormsListParams,
    TicketMetricsListParams,
    TicketsGetParams,
    TicketsListParams,
    TriggersGetParams,
    TriggersListParams,
    UsersGetParams,
    UsersListParams,
    ViewsGetParams,
    ViewsListParams,
)

if TYPE_CHECKING:
    from .models import ZendeskSupportAuthConfig
# Import specific auth config classes for multi-auth isinstance checks
from .models import ZendeskSupportOauth20AuthConfig, ZendeskSupportApiTokenAuthConfig
# Import response models and envelope models at runtime
from .models import (
    ZendeskSupportExecuteResult,
    ZendeskSupportExecuteResultWithMeta,
    TicketsListResult,
    TicketsGetResult,
    UsersListResult,
    UsersGetResult,
    OrganizationsListResult,
    OrganizationsGetResult,
    GroupsListResult,
    GroupsGetResult,
    TicketCommentsListResult,
    AttachmentsGetResult,
    TicketAuditsListResult,
    TicketAuditsListResult,
    TicketMetricsListResult,
    TicketFieldsListResult,
    TicketFieldsGetResult,
    BrandsListResult,
    BrandsGetResult,
    ViewsListResult,
    ViewsGetResult,
    MacrosListResult,
    MacrosGetResult,
    TriggersListResult,
    TriggersGetResult,
    AutomationsListResult,
    AutomationsGetResult,
    TagsListResult,
    SatisfactionRatingsListResult,
    SatisfactionRatingsGetResult,
    GroupMembershipsListResult,
    OrganizationMembershipsListResult,
    SlaPoliciesListResult,
    SlaPoliciesGetResult,
    TicketFormsListResult,
    TicketFormsGetResult,
    ArticlesListResult,
    ArticlesGetResult,
    ArticleAttachmentsListResult,
    ArticleAttachmentsGetResult,
)


class ZendeskSupportConnector:
    """
    Type-safe Zendesk-Support API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-support"
    connector_version = "0.1.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("tickets", "list"): True,
        ("tickets", "get"): True,
        ("users", "list"): True,
        ("users", "get"): True,
        ("organizations", "list"): True,
        ("organizations", "get"): True,
        ("groups", "list"): True,
        ("groups", "get"): True,
        ("ticket_comments", "list"): True,
        ("attachments", "get"): True,
        ("attachments", "download"): False,
        ("ticket_audits", "list"): True,
        ("ticket_audits", "list"): True,
        ("ticket_metrics", "list"): True,
        ("ticket_fields", "list"): True,
        ("ticket_fields", "get"): True,
        ("brands", "list"): True,
        ("brands", "get"): True,
        ("views", "list"): True,
        ("views", "get"): True,
        ("macros", "list"): True,
        ("macros", "get"): True,
        ("triggers", "list"): True,
        ("triggers", "get"): True,
        ("automations", "list"): True,
        ("automations", "get"): True,
        ("tags", "list"): True,
        ("satisfaction_ratings", "list"): True,
        ("satisfaction_ratings", "get"): True,
        ("group_memberships", "list"): True,
        ("organization_memberships", "list"): True,
        ("sla_policies", "list"): True,
        ("sla_policies", "get"): True,
        ("ticket_forms", "list"): True,
        ("ticket_forms", "get"): True,
        ("articles", "list"): True,
        ("articles", "get"): True,
        ("article_attachments", "list"): True,
        ("article_attachments", "get"): True,
        ("article_attachments", "download"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('tickets', 'list'): {'page': 'page', 'external_id': 'external_id', 'sort': 'sort'},
        ('tickets', 'get'): {'ticket_id': 'ticket_id'},
        ('users', 'list'): {'page': 'page', 'role': 'role', 'external_id': 'external_id'},
        ('users', 'get'): {'user_id': 'user_id'},
        ('organizations', 'list'): {'page': 'page'},
        ('organizations', 'get'): {'organization_id': 'organization_id'},
        ('groups', 'list'): {'page': 'page', 'exclude_deleted': 'exclude_deleted'},
        ('groups', 'get'): {'group_id': 'group_id'},
        ('ticket_comments', 'list'): {'ticket_id': 'ticket_id', 'page': 'page', 'include_inline_images': 'include_inline_images', 'sort': 'sort'},
        ('attachments', 'get'): {'attachment_id': 'attachment_id'},
        ('attachments', 'download'): {'attachment_id': 'attachment_id', 'range_header': 'range_header'},
        ('ticket_audits', 'list'): {'ticket_id': 'ticket_id', 'page': 'page'},
        ('ticket_metrics', 'list'): {'page': 'page'},
        ('ticket_fields', 'list'): {'page': 'page', 'locale': 'locale'},
        ('ticket_fields', 'get'): {'ticket_field_id': 'ticket_field_id'},
        ('brands', 'list'): {'page': 'page'},
        ('brands', 'get'): {'brand_id': 'brand_id'},
        ('views', 'list'): {'page': 'page', 'access': 'access', 'active': 'active', 'group_id': 'group_id', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('views', 'get'): {'view_id': 'view_id'},
        ('macros', 'list'): {'page': 'page', 'access': 'access', 'active': 'active', 'category': 'category', 'group_id': 'group_id', 'only_viewable': 'only_viewable', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('macros', 'get'): {'macro_id': 'macro_id'},
        ('triggers', 'list'): {'page': 'page', 'active': 'active', 'category_id': 'category_id', 'sort': 'sort'},
        ('triggers', 'get'): {'trigger_id': 'trigger_id'},
        ('automations', 'list'): {'page': 'page', 'active': 'active', 'sort': 'sort'},
        ('automations', 'get'): {'automation_id': 'automation_id'},
        ('tags', 'list'): {'page': 'page'},
        ('satisfaction_ratings', 'list'): {'page': 'page', 'score': 'score', 'start_time': 'start_time', 'end_time': 'end_time'},
        ('satisfaction_ratings', 'get'): {'satisfaction_rating_id': 'satisfaction_rating_id'},
        ('group_memberships', 'list'): {'page': 'page'},
        ('organization_memberships', 'list'): {'page': 'page'},
        ('sla_policies', 'list'): {'page': 'page'},
        ('sla_policies', 'get'): {'sla_policy_id': 'sla_policy_id'},
        ('ticket_forms', 'list'): {'page': 'page', 'active': 'active', 'end_user_visible': 'end_user_visible'},
        ('ticket_forms', 'get'): {'ticket_form_id': 'ticket_form_id'},
        ('articles', 'list'): {'page': 'page', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('articles', 'get'): {'id': 'id'},
        ('article_attachments', 'list'): {'article_id': 'article_id', 'page': 'page'},
        ('article_attachments', 'get'): {'article_id': 'article_id', 'attachment_id': 'attachment_id'},
        ('article_attachments', 'download'): {'article_id': 'article_id', 'attachment_id': 'attachment_id', 'range_header': 'range_header'},
    }

    def __init__(
        self,
        auth_config: ZendeskSupportAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new zendesk-support connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Zendesk subdomain
        Examples:
            # Local mode (direct API calls)
            connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = ZendeskSupportConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = ZendeskSupportConnector(
                auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="..."),
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
            if subdomain:
                config_values["subdomain"] = subdomain

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, ZendeskSupportOauth20AuthConfig):
                    auth_scheme = "zendeskOAuth"
                if isinstance(auth_config, ZendeskSupportApiTokenAuthConfig):
                    auth_scheme = "zendeskAPIToken"

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if subdomain:
                base_url = base_url.replace("{subdomain}", subdomain)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.tickets = TicketsQuery(self)
        self.users = UsersQuery(self)
        self.organizations = OrganizationsQuery(self)
        self.groups = GroupsQuery(self)
        self.ticket_comments = TicketCommentsQuery(self)
        self.attachments = AttachmentsQuery(self)
        self.ticket_audits = TicketAuditsQuery(self)
        self.ticket_metrics = TicketMetricsQuery(self)
        self.ticket_fields = TicketFieldsQuery(self)
        self.brands = BrandsQuery(self)
        self.views = ViewsQuery(self)
        self.macros = MacrosQuery(self)
        self.triggers = TriggersQuery(self)
        self.automations = AutomationsQuery(self)
        self.tags = TagsQuery(self)
        self.satisfaction_ratings = SatisfactionRatingsQuery(self)
        self.group_memberships = GroupMembershipsQuery(self)
        self.organization_memberships = OrganizationMembershipsQuery(self)
        self.sla_policies = SlaPoliciesQuery(self)
        self.ticket_forms = TicketFormsQuery(self)
        self.articles = ArticlesQuery(self)
        self.article_attachments = ArticleAttachmentsQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
    ) -> "TicketsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "UsersGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["list"],
        params: "OrganizationsListParams"
    ) -> "OrganizationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["get"],
        params: "OrganizationsGetParams"
    ) -> "OrganizationsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["list"],
        params: "GroupsListParams"
    ) -> "GroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["get"],
        params: "GroupsGetParams"
    ) -> "GroupsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_comments"],
        action: Literal["list"],
        params: "TicketCommentsListParams"
    ) -> "TicketCommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["get"],
        params: "AttachmentsGetParams"
    ) -> "AttachmentsGetResult": ...

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
        entity: Literal["ticket_audits"],
        action: Literal["list"],
        params: "TicketAuditsListParams"
    ) -> "TicketAuditsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_audits"],
        action: Literal["list"],
        params: "TicketAuditsListParams"
    ) -> "TicketAuditsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_metrics"],
        action: Literal["list"],
        params: "TicketMetricsListParams"
    ) -> "TicketMetricsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_fields"],
        action: Literal["list"],
        params: "TicketFieldsListParams"
    ) -> "TicketFieldsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_fields"],
        action: Literal["get"],
        params: "TicketFieldsGetParams"
    ) -> "TicketFieldsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["brands"],
        action: Literal["list"],
        params: "BrandsListParams"
    ) -> "BrandsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["brands"],
        action: Literal["get"],
        params: "BrandsGetParams"
    ) -> "BrandsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["list"],
        params: "ViewsListParams"
    ) -> "ViewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["views"],
        action: Literal["get"],
        params: "ViewsGetParams"
    ) -> "ViewsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["macros"],
        action: Literal["list"],
        params: "MacrosListParams"
    ) -> "MacrosListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["macros"],
        action: Literal["get"],
        params: "MacrosGetParams"
    ) -> "MacrosGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["triggers"],
        action: Literal["list"],
        params: "TriggersListParams"
    ) -> "TriggersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["triggers"],
        action: Literal["get"],
        params: "TriggersGetParams"
    ) -> "TriggersGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["automations"],
        action: Literal["list"],
        params: "AutomationsListParams"
    ) -> "AutomationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["automations"],
        action: Literal["get"],
        params: "AutomationsGetParams"
    ) -> "AutomationsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tags"],
        action: Literal["list"],
        params: "TagsListParams"
    ) -> "TagsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["satisfaction_ratings"],
        action: Literal["list"],
        params: "SatisfactionRatingsListParams"
    ) -> "SatisfactionRatingsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["satisfaction_ratings"],
        action: Literal["get"],
        params: "SatisfactionRatingsGetParams"
    ) -> "SatisfactionRatingsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["group_memberships"],
        action: Literal["list"],
        params: "GroupMembershipsListParams"
    ) -> "GroupMembershipsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["organization_memberships"],
        action: Literal["list"],
        params: "OrganizationMembershipsListParams"
    ) -> "OrganizationMembershipsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sla_policies"],
        action: Literal["list"],
        params: "SlaPoliciesListParams"
    ) -> "SlaPoliciesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sla_policies"],
        action: Literal["get"],
        params: "SlaPoliciesGetParams"
    ) -> "SlaPoliciesGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_forms"],
        action: Literal["list"],
        params: "TicketFormsListParams"
    ) -> "TicketFormsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_forms"],
        action: Literal["get"],
        params: "TicketFormsGetParams"
    ) -> "TicketFormsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["list"],
        params: "ArticlesListParams"
    ) -> "ArticlesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["get"],
        params: "ArticlesGetParams"
    ) -> "ArticlesGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["list"],
        params: "ArticleAttachmentsListParams"
    ) -> "ArticleAttachmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["get"],
        params: "ArticleAttachmentsGetParams"
    ) -> "ArticleAttachmentsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["download"],
        params: "ArticleAttachmentsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> ZendeskSupportExecuteResult[Any] | ZendeskSupportExecuteResultWithMeta[Any, Any] | Any: ...

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
                return ZendeskSupportExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ZendeskSupportExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class TicketsQuery:
    """
    Query class for Tickets entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        external_id: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> TicketsListResult:
        """
        Returns a list of all tickets in your account

        Args:
            page: Page number for pagination
            external_id: Lists tickets by external id
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            TicketsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "external_id": external_id,
            "sort": sort,
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
        **kwargs
    ) -> TicketsGetResult:
        """
        Returns a ticket by its ID

        Args:
            ticket_id: The ID of the ticket
            **kwargs: Additional parameters

        Returns:
            TicketsGetResult
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "get", params)
        # Cast generic envelope to concrete typed result
        return TicketsGetResult(
            data=result.data        )



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        role: str | None = None,
        external_id: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a list of all users in your account

        Args:
            page: Page number for pagination
            role: Filter by role
            external_id: Filter by external id
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "role": role,
            "external_id": external_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        user_id: str,
        **kwargs
    ) -> UsersGetResult:
        """
        Returns a user by their ID

        Args:
            user_id: The ID of the user
            **kwargs: Additional parameters

        Returns:
            UsersGetResult
        """
        params = {k: v for k, v in {
            "user_id": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        # Cast generic envelope to concrete typed result
        return UsersGetResult(
            data=result.data        )



class OrganizationsQuery:
    """
    Query class for Organizations entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> OrganizationsListResult:
        """
        Returns a list of all organizations in your account

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            OrganizationsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "list", params)
        # Cast generic envelope to concrete typed result
        return OrganizationsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        organization_id: str,
        **kwargs
    ) -> OrganizationsGetResult:
        """
        Returns an organization by its ID

        Args:
            organization_id: The ID of the organization
            **kwargs: Additional parameters

        Returns:
            OrganizationsGetResult
        """
        params = {k: v for k, v in {
            "organization_id": organization_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "get", params)
        # Cast generic envelope to concrete typed result
        return OrganizationsGetResult(
            data=result.data        )



class GroupsQuery:
    """
    Query class for Groups entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        exclude_deleted: bool | None = None,
        **kwargs
    ) -> GroupsListResult:
        """
        Returns a list of all groups in your account

        Args:
            page: Page number for pagination
            exclude_deleted: Exclude deleted groups
            **kwargs: Additional parameters

        Returns:
            GroupsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "exclude_deleted": exclude_deleted,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "list", params)
        # Cast generic envelope to concrete typed result
        return GroupsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        group_id: str,
        **kwargs
    ) -> GroupsGetResult:
        """
        Returns a group by its ID

        Args:
            group_id: The ID of the group
            **kwargs: Additional parameters

        Returns:
            GroupsGetResult
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "get", params)
        # Cast generic envelope to concrete typed result
        return GroupsGetResult(
            data=result.data        )



class TicketCommentsQuery:
    """
    Query class for TicketComments entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ticket_id: str,
        page: int | None = None,
        include_inline_images: bool | None = None,
        sort: str | None = None,
        **kwargs
    ) -> TicketCommentsListResult:
        """
        Returns a list of comments for a specific ticket

        Args:
            ticket_id: The ID of the ticket
            page: Page number for pagination
            include_inline_images: Include inline images in the response
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            TicketCommentsListResult
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            "page": page,
            "include_inline_images": include_inline_images,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_comments", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketCommentsListResult(
            data=result.data,
            meta=result.meta        )



class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        attachment_id: str,
        **kwargs
    ) -> AttachmentsGetResult:
        """
        Returns an attachment by its ID

        Args:
            attachment_id: The ID of the attachment
            **kwargs: Additional parameters

        Returns:
            AttachmentsGetResult
        """
        params = {k: v for k, v in {
            "attachment_id": attachment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        # Cast generic envelope to concrete typed result
        return AttachmentsGetResult(
            data=result.data        )



    async def download(
        self,
        attachment_id: str,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the file content of a ticket attachment

        Args:
            attachment_id: The ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "attachment_id": attachment_id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_local(
        self,
        attachment_id: str,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the file content of a ticket attachment and save to file.

        Args:
            attachment_id: The ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            attachment_id=attachment_id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class TicketAuditsQuery:
    """
    Query class for TicketAudits entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> TicketAuditsListResult:
        """
        Returns a list of all ticket audits

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            TicketAuditsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_audits", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketAuditsListResult(
            data=result.data,
            meta=result.meta        )



    async def list(
        self,
        ticket_id: str,
        page: int | None = None,
        **kwargs
    ) -> TicketAuditsListResult:
        """
        Returns a list of audits for a specific ticket

        Args:
            ticket_id: The ID of the ticket
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            TicketAuditsListResult
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_audits", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketAuditsListResult(
            data=result.data,
            meta=result.meta        )



class TicketMetricsQuery:
    """
    Query class for TicketMetrics entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> TicketMetricsListResult:
        """
        Returns a list of all ticket metrics

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            TicketMetricsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_metrics", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketMetricsListResult(
            data=result.data,
            meta=result.meta        )



class TicketFieldsQuery:
    """
    Query class for TicketFields entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        locale: str | None = None,
        **kwargs
    ) -> TicketFieldsListResult:
        """
        Returns a list of all ticket fields

        Args:
            page: Page number for pagination
            locale: Locale for the results
            **kwargs: Additional parameters

        Returns:
            TicketFieldsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "locale": locale,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketFieldsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        ticket_field_id: str,
        **kwargs
    ) -> TicketFieldsGetResult:
        """
        Returns a ticket field by its ID

        Args:
            ticket_field_id: The ID of the ticket field
            **kwargs: Additional parameters

        Returns:
            TicketFieldsGetResult
        """
        params = {k: v for k, v in {
            "ticket_field_id": ticket_field_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_fields", "get", params)
        # Cast generic envelope to concrete typed result
        return TicketFieldsGetResult(
            data=result.data        )



class BrandsQuery:
    """
    Query class for Brands entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> BrandsListResult:
        """
        Returns a list of all brands for the account

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            BrandsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("brands", "list", params)
        # Cast generic envelope to concrete typed result
        return BrandsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        brand_id: str,
        **kwargs
    ) -> BrandsGetResult:
        """
        Returns a brand by its ID

        Args:
            brand_id: The ID of the brand
            **kwargs: Additional parameters

        Returns:
            BrandsGetResult
        """
        params = {k: v for k, v in {
            "brand_id": brand_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("brands", "get", params)
        # Cast generic envelope to concrete typed result
        return BrandsGetResult(
            data=result.data        )



class ViewsQuery:
    """
    Query class for Views entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        access: str | None = None,
        active: bool | None = None,
        group_id: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ViewsListResult:
        """
        Returns a list of all views for the account

        Args:
            page: Page number for pagination
            access: Filter by access level
            active: Filter by active status
            group_id: Filter by group ID
            sort_by: Sort results
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ViewsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "access": access,
            "active": active,
            "group_id": group_id,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "list", params)
        # Cast generic envelope to concrete typed result
        return ViewsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        view_id: str,
        **kwargs
    ) -> ViewsGetResult:
        """
        Returns a view by its ID

        Args:
            view_id: The ID of the view
            **kwargs: Additional parameters

        Returns:
            ViewsGetResult
        """
        params = {k: v for k, v in {
            "view_id": view_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "get", params)
        # Cast generic envelope to concrete typed result
        return ViewsGetResult(
            data=result.data        )



class MacrosQuery:
    """
    Query class for Macros entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        access: str | None = None,
        active: bool | None = None,
        category: int | None = None,
        group_id: int | None = None,
        only_viewable: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> MacrosListResult:
        """
        Returns a list of all macros for the account

        Args:
            page: Page number for pagination
            access: Filter by access level
            active: Filter by active status
            category: Filter by category
            group_id: Filter by group ID
            only_viewable: Return only viewable macros
            sort_by: Sort results
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            MacrosListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "access": access,
            "active": active,
            "category": category,
            "group_id": group_id,
            "only_viewable": only_viewable,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("macros", "list", params)
        # Cast generic envelope to concrete typed result
        return MacrosListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        macro_id: str,
        **kwargs
    ) -> MacrosGetResult:
        """
        Returns a macro by its ID

        Args:
            macro_id: The ID of the macro
            **kwargs: Additional parameters

        Returns:
            MacrosGetResult
        """
        params = {k: v for k, v in {
            "macro_id": macro_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("macros", "get", params)
        # Cast generic envelope to concrete typed result
        return MacrosGetResult(
            data=result.data        )



class TriggersQuery:
    """
    Query class for Triggers entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        active: bool | None = None,
        category_id: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> TriggersListResult:
        """
        Returns a list of all triggers for the account

        Args:
            page: Page number for pagination
            active: Filter by active status
            category_id: Filter by category ID
            sort: Sort results
            **kwargs: Additional parameters

        Returns:
            TriggersListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "active": active,
            "category_id": category_id,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("triggers", "list", params)
        # Cast generic envelope to concrete typed result
        return TriggersListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        trigger_id: str,
        **kwargs
    ) -> TriggersGetResult:
        """
        Returns a trigger by its ID

        Args:
            trigger_id: The ID of the trigger
            **kwargs: Additional parameters

        Returns:
            TriggersGetResult
        """
        params = {k: v for k, v in {
            "trigger_id": trigger_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("triggers", "get", params)
        # Cast generic envelope to concrete typed result
        return TriggersGetResult(
            data=result.data        )



class AutomationsQuery:
    """
    Query class for Automations entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        active: bool | None = None,
        sort: str | None = None,
        **kwargs
    ) -> AutomationsListResult:
        """
        Returns a list of all automations for the account

        Args:
            page: Page number for pagination
            active: Filter by active status
            sort: Sort results
            **kwargs: Additional parameters

        Returns:
            AutomationsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "active": active,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("automations", "list", params)
        # Cast generic envelope to concrete typed result
        return AutomationsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        automation_id: str,
        **kwargs
    ) -> AutomationsGetResult:
        """
        Returns an automation by its ID

        Args:
            automation_id: The ID of the automation
            **kwargs: Additional parameters

        Returns:
            AutomationsGetResult
        """
        params = {k: v for k, v in {
            "automation_id": automation_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("automations", "get", params)
        # Cast generic envelope to concrete typed result
        return AutomationsGetResult(
            data=result.data        )



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> TagsListResult:
        """
        Returns a list of all tags used in the account

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            TagsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to concrete typed result
        return TagsListResult(
            data=result.data,
            meta=result.meta        )



class SatisfactionRatingsQuery:
    """
    Query class for SatisfactionRatings entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        score: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs
    ) -> SatisfactionRatingsListResult:
        """
        Returns a list of all satisfaction ratings

        Args:
            page: Page number for pagination
            score: Filter by score
            start_time: Start time (Unix epoch)
            end_time: End time (Unix epoch)
            **kwargs: Additional parameters

        Returns:
            SatisfactionRatingsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "score": score,
            "start_time": start_time,
            "end_time": end_time,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("satisfaction_ratings", "list", params)
        # Cast generic envelope to concrete typed result
        return SatisfactionRatingsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        satisfaction_rating_id: str,
        **kwargs
    ) -> SatisfactionRatingsGetResult:
        """
        Returns a satisfaction rating by its ID

        Args:
            satisfaction_rating_id: The ID of the satisfaction rating
            **kwargs: Additional parameters

        Returns:
            SatisfactionRatingsGetResult
        """
        params = {k: v for k, v in {
            "satisfaction_rating_id": satisfaction_rating_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("satisfaction_ratings", "get", params)
        # Cast generic envelope to concrete typed result
        return SatisfactionRatingsGetResult(
            data=result.data        )



class GroupMembershipsQuery:
    """
    Query class for GroupMemberships entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> GroupMembershipsListResult:
        """
        Returns a list of all group memberships

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            GroupMembershipsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("group_memberships", "list", params)
        # Cast generic envelope to concrete typed result
        return GroupMembershipsListResult(
            data=result.data,
            meta=result.meta        )



class OrganizationMembershipsQuery:
    """
    Query class for OrganizationMemberships entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> OrganizationMembershipsListResult:
        """
        Returns a list of all organization memberships

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            OrganizationMembershipsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organization_memberships", "list", params)
        # Cast generic envelope to concrete typed result
        return OrganizationMembershipsListResult(
            data=result.data,
            meta=result.meta        )



class SlaPoliciesQuery:
    """
    Query class for SlaPolicies entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        **kwargs
    ) -> SlaPoliciesListResult:
        """
        Returns a list of all SLA policies

        Args:
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            SlaPoliciesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sla_policies", "list", params)
        # Cast generic envelope to concrete typed result
        return SlaPoliciesListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        sla_policy_id: str,
        **kwargs
    ) -> SlaPoliciesGetResult:
        """
        Returns an SLA policy by its ID

        Args:
            sla_policy_id: The ID of the SLA policy
            **kwargs: Additional parameters

        Returns:
            SlaPoliciesGetResult
        """
        params = {k: v for k, v in {
            "sla_policy_id": sla_policy_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sla_policies", "get", params)
        # Cast generic envelope to concrete typed result
        return SlaPoliciesGetResult(
            data=result.data        )



class TicketFormsQuery:
    """
    Query class for TicketForms entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        active: bool | None = None,
        end_user_visible: bool | None = None,
        **kwargs
    ) -> TicketFormsListResult:
        """
        Returns a list of all ticket forms for the account

        Args:
            page: Page number for pagination
            active: Filter by active status
            end_user_visible: Filter by end user visibility
            **kwargs: Additional parameters

        Returns:
            TicketFormsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "active": active,
            "end_user_visible": end_user_visible,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_forms", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketFormsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        ticket_form_id: str,
        **kwargs
    ) -> TicketFormsGetResult:
        """
        Returns a ticket form by its ID

        Args:
            ticket_form_id: The ID of the ticket form
            **kwargs: Additional parameters

        Returns:
            TicketFormsGetResult
        """
        params = {k: v for k, v in {
            "ticket_form_id": ticket_form_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_forms", "get", params)
        # Cast generic envelope to concrete typed result
        return TicketFormsGetResult(
            data=result.data        )



class ArticlesQuery:
    """
    Query class for Articles entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ArticlesListResult:
        """
        Returns a list of all articles in the Help Center

        Args:
            page: Page number for pagination
            sort_by: Sort articles by field
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ArticlesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "list", params)
        # Cast generic envelope to concrete typed result
        return ArticlesListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ArticlesGetResult:
        """
        Retrieves the details of a specific article

        Args:
            id: The unique ID of the article
            **kwargs: Additional parameters

        Returns:
            ArticlesGetResult
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "get", params)
        # Cast generic envelope to concrete typed result
        return ArticlesGetResult(
            data=result.data        )



class ArticleAttachmentsQuery:
    """
    Query class for ArticleAttachments entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        article_id: str,
        page: int | None = None,
        **kwargs
    ) -> ArticleAttachmentsListResult:
        """
        Returns a list of all attachments for a specific article

        Args:
            article_id: The unique ID of the article
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            ArticleAttachmentsListResult
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "list", params)
        # Cast generic envelope to concrete typed result
        return ArticleAttachmentsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        article_id: str,
        attachment_id: str,
        **kwargs
    ) -> ArticleAttachmentsGetResult:
        """
        Retrieves the metadata of a specific attachment for a specific article

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            **kwargs: Additional parameters

        Returns:
            ArticleAttachmentsGetResult
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "attachment_id": attachment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "get", params)
        # Cast generic envelope to concrete typed result
        return ArticleAttachmentsGetResult(
            data=result.data        )



    async def download(
        self,
        article_id: str,
        attachment_id: str,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the file content of a specific attachment

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "attachment_id": attachment_id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "download", params)
        return result


    async def download_local(
        self,
        article_id: str,
        attachment_id: str,
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the file content of a specific attachment and save to file.

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            article_id=article_id,
            attachment_id=attachment_id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)

