"""
Zendesk-Support connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import ZendeskSupportConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
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
    AirbyteSearchParams,
    BrandsSearchFilter,
    BrandsSearchQuery,
    GroupsSearchFilter,
    GroupsSearchQuery,
    OrganizationsSearchFilter,
    OrganizationsSearchQuery,
    SatisfactionRatingsSearchFilter,
    SatisfactionRatingsSearchQuery,
    TagsSearchFilter,
    TagsSearchQuery,
    TicketAuditsSearchFilter,
    TicketAuditsSearchQuery,
    TicketCommentsSearchFilter,
    TicketCommentsSearchQuery,
    TicketFieldsSearchFilter,
    TicketFieldsSearchQuery,
    TicketFormsSearchFilter,
    TicketFormsSearchQuery,
    TicketMetricsSearchFilter,
    TicketMetricsSearchQuery,
    TicketsSearchFilter,
    TicketsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
)
if TYPE_CHECKING:
    from .models import ZendeskSupportAuthConfig
# Import specific auth config classes for multi-auth isinstance checks
from .models import ZendeskSupportOauth20AuthConfig, ZendeskSupportApiTokenAuthConfig
# Import response models and envelope models at runtime
from .models import (
    ZendeskSupportCheckResult,
    ZendeskSupportExecuteResult,
    ZendeskSupportExecuteResultWithMeta,
    TicketsListResult,
    UsersListResult,
    OrganizationsListResult,
    GroupsListResult,
    TicketCommentsListResult,
    TicketAuditsListResult,
    TicketAuditsListResult,
    TicketMetricsListResult,
    TicketFieldsListResult,
    BrandsListResult,
    ViewsListResult,
    MacrosListResult,
    TriggersListResult,
    AutomationsListResult,
    TagsListResult,
    SatisfactionRatingsListResult,
    GroupMembershipsListResult,
    OrganizationMembershipsListResult,
    SlaPoliciesListResult,
    TicketFormsListResult,
    ArticlesListResult,
    ArticleAttachmentsListResult,
    Article,
    ArticleAttachment,
    Attachment,
    Automation,
    Brand,
    Group,
    GroupMembership,
    Macro,
    Organization,
    OrganizationMembership,
    SLAPolicy,
    SatisfactionRating,
    Tag,
    Ticket,
    TicketAudit,
    TicketComment,
    TicketField,
    TicketForm,
    TicketMetric,
    Trigger,
    User,
    View,
    AirbyteSearchHit,
    AirbyteSearchResult,
    BrandsSearchData,
    BrandsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
    OrganizationsSearchData,
    OrganizationsSearchResult,
    SatisfactionRatingsSearchData,
    SatisfactionRatingsSearchResult,
    TagsSearchData,
    TagsSearchResult,
    TicketAuditsSearchData,
    TicketAuditsSearchResult,
    TicketCommentsSearchData,
    TicketCommentsSearchResult,
    TicketFieldsSearchData,
    TicketFieldsSearchResult,
    TicketFormsSearchData,
    TicketFormsSearchResult,
    TicketMetricsSearchData,
    TicketMetricsSearchResult,
    TicketsSearchData,
    TicketsSearchResult,
    UsersSearchData,
    UsersSearchResult,
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




class ZendeskSupportConnector:
    """
    Type-safe Zendesk-Support API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-support"
    connector_version = "0.1.10"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("tickets", "list"): True,
        ("tickets", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("organizations", "list"): True,
        ("organizations", "get"): None,
        ("groups", "list"): True,
        ("groups", "get"): None,
        ("ticket_comments", "list"): True,
        ("attachments", "get"): None,
        ("attachments", "download"): None,
        ("ticket_audits", "list"): True,
        ("ticket_audits", "list"): True,
        ("ticket_metrics", "list"): True,
        ("ticket_fields", "list"): True,
        ("ticket_fields", "get"): None,
        ("brands", "list"): True,
        ("brands", "get"): None,
        ("views", "list"): True,
        ("views", "get"): None,
        ("macros", "list"): True,
        ("macros", "get"): None,
        ("triggers", "list"): True,
        ("triggers", "get"): None,
        ("automations", "list"): True,
        ("automations", "get"): None,
        ("tags", "list"): True,
        ("satisfaction_ratings", "list"): True,
        ("satisfaction_ratings", "get"): None,
        ("group_memberships", "list"): True,
        ("organization_memberships", "list"): True,
        ("sla_policies", "list"): True,
        ("sla_policies", "get"): None,
        ("ticket_forms", "list"): True,
        ("ticket_forms", "get"): None,
        ("articles", "list"): True,
        ("articles", "get"): None,
        ("article_attachments", "list"): True,
        ("article_attachments", "get"): None,
        ("article_attachments", "download"): None,
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
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new zendesk-support connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `external_user_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Zendesk subdomain
        Examples:
            # Local mode (direct API calls)
            connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = ZendeskSupportConnector(
                external_user_id="user-123",
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
        # Hosted mode: external_user_id, airbyte_client_id, and airbyte_client_secret provided
        if external_user_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                external_user_id=external_user_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_definition_id=str(ZendeskSupportConnectorModel.id),
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (external_user_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

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
                model=ZendeskSupportConnectorModel,
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
    ) -> "Ticket": ...

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
    ) -> "User": ...

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
    ) -> "Organization": ...

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
    ) -> "Group": ...

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
    ) -> "TicketField": ...

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
    ) -> "Brand": ...

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
    ) -> "View": ...

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
    ) -> "Macro": ...

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
    ) -> "Trigger": ...

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
    ) -> "Automation": ...

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
    ) -> "SatisfactionRating": ...

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
    ) -> "SLAPolicy": ...

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
    ) -> "TicketForm": ...

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
    ) -> "Article": ...

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
    ) -> "ArticleAttachment": ...

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
        action: Literal["list", "get", "download", "search"],
        params: Mapping[str, Any]
    ) -> ZendeskSupportExecuteResult[Any] | ZendeskSupportExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download", "search"],
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
                return ZendeskSupportExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ZendeskSupportExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ZendeskSupportCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ZendeskSupportCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ZendeskSupportCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ZendeskSupportCheckResult(
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
            @ZendeskSupportConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @ZendeskSupportConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    ZendeskSupportConnectorModel,
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
        return describe_entities(ZendeskSupportConnectorModel)

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
            (e for e in ZendeskSupportConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ZendeskSupportConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



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
            meta=result.meta
        )



    async def get(
        self,
        ticket_id: str,
        **kwargs
    ) -> Ticket:
        """
        Returns a ticket by its ID

        Args:
            ticket_id: The ID of the ticket
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "ticket_id": ticket_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "get", params)
        return result



    async def search(
        self,
        query: TicketsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketsSearchResult:
        """
        Search tickets records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketsSearchFilter):
        - allow_attachments: Boolean indicating whether attachments are allowed on the ticket
        - allow_channelback: Boolean indicating whether agents can reply to the ticket through the original channel
        - assignee_id: Unique identifier of the agent currently assigned to the ticket
        - brand_id: Unique identifier of the brand associated with the ticket in multi-brand accounts
        - collaborator_ids: Array of user identifiers who are collaborating on the ticket
        - created_at: Timestamp indicating when the ticket was created
        - custom_fields: Array of custom field values specific to the account's ticket configuration
        - custom_status_id: Unique identifier of the custom status applied to the ticket
        - deleted_ticket_form_id: The ID of the ticket form that was previously associated with this ticket but has since been deleted
        - description: Initial description or content of the ticket when it was created
        - due_at: Timestamp indicating when the ticket is due for completion or resolution
        - email_cc_ids: Array of user identifiers who are CC'd on ticket email notifications
        - external_id: External identifier for the ticket, used for integrations with other systems
        - fields: Array of ticket field values including both system and custom fields
        - follower_ids: Array of user identifiers who are following the ticket for updates
        - followup_ids: Array of identifiers for follow-up tickets related to this ticket
        - forum_topic_id: Unique identifier linking the ticket to a forum topic if applicable
        - from_messaging_channel: Boolean indicating whether the ticket originated from a messaging channel
        - generated_timestamp: Timestamp updated for all ticket updates including system changes, used for incremental export
        - group_id: Unique identifier of the agent group assigned to handle the ticket
        - has_incidents: Boolean indicating whether this problem ticket has related incident tickets
        - id: Unique identifier for the ticket
        - is_public: Boolean indicating whether the ticket is publicly visible
        - organization_id: Unique identifier of the organization associated with the ticket
        - priority: Priority level assigned to the ticket (e.g., urgent, high, normal, low)
        - problem_id: Unique identifier of the problem ticket if this is an incident ticket
        - raw_subject: Original unprocessed subject line before any system modifications
        - recipient: Email address or identifier of the ticket recipient
        - requester_id: Unique identifier of the user who requested or created the ticket
        - satisfaction_rating: Object containing customer satisfaction rating data for the ticket
        - sharing_agreement_ids: Array of sharing agreement identifiers if the ticket is shared across Zendesk instances
        - status: Current status of the ticket (e.g., new, open, pending, solved, closed)
        - subject: Subject line of the ticket describing the issue or request
        - submitter_id: Unique identifier of the user who submitted the ticket on behalf of the requester
        - tags: Array of tags applied to the ticket for categorization and filtering
        - ticket_form_id: Unique identifier of the ticket form used when creating the ticket
        - type: Type of ticket (e.g., problem, incident, question, task)
        - updated_at: Timestamp indicating when the ticket was last updated with a ticket event
        - url: API URL to access the full ticket resource
        - via: Object describing the channel and method through which the ticket was created

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketsSearchResult with hits (list of AirbyteSearchHit[TicketsSearchData]) and pagination info

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

        result = await self._connector.execute("tickets", "search", params)

        # Parse response into typed result
        return TicketsSearchResult(
            hits=[
                AirbyteSearchHit[TicketsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TicketsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        user_id: str,
        **kwargs
    ) -> User:
        """
        Returns a user by their ID

        Args:
            user_id: The ID of the user
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "user_id": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



    async def search(
        self,
        query: UsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> UsersSearchResult:
        """
        Search users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (UsersSearchFilter):
        - active: Indicates if the user account is currently active
        - alias: Alternative name or nickname for the user
        - chat_only: Indicates if the user can only interact via chat
        - created_at: Timestamp indicating when the user was created
        - custom_role_id: Identifier for a custom role assigned to the user
        - default_group_id: Identifier of the default group assigned to the user
        - details: Additional descriptive information about the user
        - email: Email address of the user
        - external_id: External system identifier for the user, used for integrations
        - iana_time_zone: IANA standard time zone identifier for the user
        - id: Unique identifier for the user
        - last_login_at: Timestamp of the user's most recent login
        - locale: Locale setting determining language and regional format preferences
        - locale_id: Identifier for the user's locale preference
        - moderator: Indicates if the user has moderator privileges
        - name: Display name of the user
        - notes: Internal notes about the user, visible only to agents
        - only_private_comments: Indicates if the user can only make private comments on tickets
        - organization_id: Identifier of the organization the user belongs to
        - permanently_deleted: Indicates if the user has been permanently deleted from the system
        - phone: Phone number of the user
        - photo: Profile photo or avatar of the user
        - report_csv: Indicates if the user receives reports in CSV format
        - restricted_agent: Indicates if the agent has restricted access permissions
        - role: Role assigned to the user defining their permissions level
        - role_type: Type classification of the user's role
        - shared: Indicates if the user is shared across multiple accounts
        - shared_agent: Indicates if the user is a shared agent across multiple brands or accounts
        - shared_phone_number: Indicates if the phone number is shared with other users
        - signature: Email signature text for the user
        - suspended: Indicates if the user account is suspended
        - tags: Labels or tags associated with the user for categorization
        - ticket_restriction: Defines which tickets the user can access based on restrictions
        - time_zone: Time zone setting for the user
        - two_factor_auth_enabled: Indicates if two-factor authentication is enabled for the user
        - updated_at: Timestamp indicating when the user was last updated
        - url: API endpoint URL for accessing the user's detailed information
        - user_fields: Custom field values specific to the user, stored as key-value pairs
        - verified: Indicates if the user's identity has been verified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UsersSearchResult with hits (list of AirbyteSearchHit[UsersSearchData]) and pagination info

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

        result = await self._connector.execute("users", "search", params)

        # Parse response into typed result
        return UsersSearchResult(
            hits=[
                AirbyteSearchHit[UsersSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=UsersSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        organization_id: str,
        **kwargs
    ) -> Organization:
        """
        Returns an organization by its ID

        Args:
            organization_id: The ID of the organization
            **kwargs: Additional parameters

        Returns:
            Organization
        """
        params = {k: v for k, v in {
            "organization_id": organization_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "get", params)
        return result



    async def search(
        self,
        query: OrganizationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrganizationsSearchResult:
        """
        Search organizations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrganizationsSearchFilter):
        - created_at: Timestamp when the organization was created
        - deleted_at: Timestamp when the organization was deleted
        - details: Details about the organization, such as the address
        - domain_names: Array of domain names associated with this organization for automatic user assignment
        - external_id: Unique external identifier to associate the organization to an external record (case-insensitive)
        - group_id: ID of the group where new tickets from users in this organization are automatically assigned
        - id: Unique identifier automatically assigned when the organization is created
        - name: Unique name for the organization (mandatory field)
        - notes: Notes about the organization
        - organization_fields: Key-value object for custom organization fields
        - shared_comments: Boolean indicating whether end users in this organization can comment on each other's tickets
        - shared_tickets: Boolean indicating whether end users in this organization can see each other's tickets
        - tags: Array of tags associated with the organization
        - updated_at: Timestamp of the last update to the organization
        - url: The API URL of this organization

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrganizationsSearchResult with hits (list of AirbyteSearchHit[OrganizationsSearchData]) and pagination info

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

        result = await self._connector.execute("organizations", "search", params)

        # Parse response into typed result
        return OrganizationsSearchResult(
            hits=[
                AirbyteSearchHit[OrganizationsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=OrganizationsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        group_id: str,
        **kwargs
    ) -> Group:
        """
        Returns a group by its ID

        Args:
            group_id: The ID of the group
            **kwargs: Additional parameters

        Returns:
            Group
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "get", params)
        return result



    async def search(
        self,
        query: GroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GroupsSearchResult:
        """
        Search groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GroupsSearchFilter):
        - created_at: Timestamp indicating when the group was created
        - default: Indicates if the group is the default one for the account
        - deleted: Indicates whether the group has been deleted
        - description: The description of the group
        - id: Unique identifier automatically assigned when creating groups
        - is_public: Indicates if the group is public (true) or private (false)
        - name: The name of the group
        - updated_at: Timestamp indicating when the group was last updated
        - url: The API URL of the group

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GroupsSearchResult with hits (list of AirbyteSearchHit[GroupsSearchData]) and pagination info

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

        result = await self._connector.execute("groups", "search", params)

        # Parse response into typed result
        return GroupsSearchResult(
            hits=[
                AirbyteSearchHit[GroupsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=GroupsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def search(
        self,
        query: TicketCommentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketCommentsSearchResult:
        """
        Search ticket_comments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketCommentsSearchFilter):
        - attachments: List of files or media attached to the comment
        - audit_id: Identifier of the audit record associated with this comment event
        - author_id: Identifier of the user who created the comment
        - body: Content of the comment in its original format
        - created_at: Timestamp when the comment was created
        - event_type: Specific classification of the event within the ticket event stream
        - html_body: HTML-formatted content of the comment
        - id: Unique identifier for the comment event
        - metadata: Additional structured information about the comment not covered by standard fields
        - plain_body: Plain text content of the comment without formatting
        - public: Boolean indicating whether the comment is visible to end users or is an internal note
        - ticket_id: Identifier of the ticket to which this comment belongs
        - timestamp: Timestamp of when the event occurred in the incremental export stream
        - type: Type of event, typically indicating this is a comment event
        - uploads: Array of upload tokens or identifiers for files being attached to the comment
        - via: Channel or method through which the comment was submitted
        - via_reference_id: Reference identifier for the channel through which the comment was created

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketCommentsSearchResult with hits (list of AirbyteSearchHit[TicketCommentsSearchData]) and pagination info

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

        result = await self._connector.execute("ticket_comments", "search", params)

        # Parse response into typed result
        return TicketCommentsSearchResult(
            hits=[
                AirbyteSearchHit[TicketCommentsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TicketCommentsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
    ) -> Attachment:
        """
        Returns an attachment by its ID

        Args:
            attachment_id: The ID of the attachment
            **kwargs: Additional parameters

        Returns:
            Attachment
        """
        params = {k: v for k, v in {
            "attachment_id": attachment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        return result



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
            meta=result.meta
        )



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
            meta=result.meta
        )



    async def search(
        self,
        query: TicketAuditsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketAuditsSearchResult:
        """
        Search ticket_audits records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketAuditsSearchFilter):
        - attachments: Files or documents attached to the audit
        - author_id: The unique identifier of the user who created the audit
        - created_at: Timestamp indicating when the audit was created
        - events: Array of events that occurred in this audit, such as field changes, comments, or tag updates
        - id: Unique identifier for the audit record, automatically assigned when the audit is created
        - metadata: Custom and system data associated with the audit
        - ticket_id: The unique identifier of the ticket associated with this audit
        - via: Describes how the audit was created, providing context about the creation source

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketAuditsSearchResult with hits (list of AirbyteSearchHit[TicketAuditsSearchData]) and pagination info

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

        result = await self._connector.execute("ticket_audits", "search", params)

        # Parse response into typed result
        return TicketAuditsSearchResult(
            hits=[
                AirbyteSearchHit[TicketAuditsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TicketAuditsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def search(
        self,
        query: TicketMetricsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketMetricsSearchResult:
        """
        Search ticket_metrics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketMetricsSearchFilter):
        - agent_wait_time_in_minutes: Number of minutes the agent spent waiting during calendar and business hours
        - assigned_at: Timestamp when the ticket was assigned
        - assignee_stations: Number of assignees the ticket had
        - assignee_updated_at: Timestamp when the assignee last updated the ticket
        - created_at: Timestamp when the metric record was created
        - custom_status_updated_at: Timestamp when the ticket's custom status was last updated
        - first_resolution_time_in_minutes: Number of minutes to the first resolution time during calendar and business hours
        - full_resolution_time_in_minutes: Number of minutes to the full resolution during calendar and business hours
        - generated_timestamp: Timestamp of when record was last updated
        - group_stations: Number of groups the ticket passed through
        - id: Unique identifier for the ticket metric record
        - initially_assigned_at: Timestamp when the ticket was initially assigned
        - instance_id: ID of the Zendesk instance associated with the ticket
        - latest_comment_added_at: Timestamp when the latest comment was added
        - metric: Ticket metrics data
        - on_hold_time_in_minutes: Number of minutes on hold
        - reopens: Total number of times the ticket was reopened
        - replies: The number of public replies added to a ticket by an agent
        - reply_time_in_minutes: Number of minutes to the first reply during calendar and business hours
        - reply_time_in_seconds: Number of seconds to the first reply during calendar hours, only available for Messaging tickets
        - requester_updated_at: Timestamp when the requester last updated the ticket
        - requester_wait_time_in_minutes: Number of minutes the requester spent waiting during calendar and business hours
        - solved_at: Timestamp when the ticket was solved
        - status: The current status of the ticket (open, pending, solved, etc.).
        - status_updated_at: Timestamp when the status of the ticket was last updated
        - ticket_id: Identifier of the associated ticket
        - time: Time related to the ticket
        - type: Type of ticket
        - updated_at: Timestamp when the metric record was last updated
        - url: The API url of the ticket metric

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketMetricsSearchResult with hits (list of AirbyteSearchHit[TicketMetricsSearchData]) and pagination info

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

        result = await self._connector.execute("ticket_metrics", "search", params)

        # Parse response into typed result
        return TicketMetricsSearchResult(
            hits=[
                AirbyteSearchHit[TicketMetricsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TicketMetricsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        ticket_field_id: str,
        **kwargs
    ) -> TicketField:
        """
        Returns a ticket field by its ID

        Args:
            ticket_field_id: The ID of the ticket field
            **kwargs: Additional parameters

        Returns:
            TicketField
        """
        params = {k: v for k, v in {
            "ticket_field_id": ticket_field_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_fields", "get", params)
        return result



    async def search(
        self,
        query: TicketFieldsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketFieldsSearchResult:
        """
        Search ticket_fields records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketFieldsSearchFilter):
        - active: Whether this field is currently available for use
        - agent_description: A description of the ticket field that only agents can see
        - collapsed_for_agents: If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields
        - created_at: Timestamp when the custom ticket field was created
        - custom_field_options: Array of option objects for custom ticket fields of type multiselect or tagger
        - custom_statuses: List of customized ticket statuses, only present for system ticket fields of type custom_status
        - description: Text describing the purpose of the ticket field to users
        - editable_in_portal: Whether this field is editable by end users in Help Center
        - id: Unique identifier for the ticket field, automatically assigned when created
        - key: Internal identifier or reference key for the field
        - position: The relative position of the ticket field on a ticket, controlling display order
        - raw_description: The dynamic content placeholder if present, or the description value if not
        - raw_title: The dynamic content placeholder if present, or the title value if not
        - raw_title_in_portal: The dynamic content placeholder if present, or the title_in_portal value if not
        - regexp_for_validation: For regexp fields only, the validation pattern for a field value to be deemed valid
        - removable: If false, this field is a system field that must be present on all tickets
        - required: If true, agents must enter a value in the field to change the ticket status to solved
        - required_in_portal: If true, end users must enter a value in the field to create a request
        - sub_type_id: For system ticket fields of type priority and status, controlling available options
        - system_field_options: Array of options for system ticket fields of type tickettype, priority, or status
        - tag: For checkbox fields only, a tag added to tickets when the checkbox field is selected
        - title: The title of the ticket field displayed to agents
        - title_in_portal: The title of the ticket field displayed to end users in Help Center
        - type: Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger
        - updated_at: Timestamp when the custom ticket field was last updated
        - url: The API URL for this ticket field resource
        - visible_in_portal: Whether this field is visible to end users in Help Center

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketFieldsSearchResult with hits (list of AirbyteSearchHit[TicketFieldsSearchData]) and pagination info

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

        result = await self._connector.execute("ticket_fields", "search", params)

        # Parse response into typed result
        return TicketFieldsSearchResult(
            hits=[
                AirbyteSearchHit[TicketFieldsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TicketFieldsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        brand_id: str,
        **kwargs
    ) -> Brand:
        """
        Returns a brand by its ID

        Args:
            brand_id: The ID of the brand
            **kwargs: Additional parameters

        Returns:
            Brand
        """
        params = {k: v for k, v in {
            "brand_id": brand_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("brands", "get", params)
        return result



    async def search(
        self,
        query: BrandsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BrandsSearchResult:
        """
        Search brands records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BrandsSearchFilter):
        - active: Indicates whether the brand is set as active
        - brand_url: The public URL of the brand
        - created_at: Timestamp when the brand was created
        - default: Indicates whether the brand is the default brand for tickets generated from non-branded channels
        - has_help_center: Indicates whether the brand has a Help Center enabled
        - help_center_state: The state of the Help Center, with allowed values of enabled, disabled, or restricted
        - host_mapping: The host mapping configuration for the brand, visible only to administrators
        - id: Unique identifier automatically assigned when the brand is created
        - is_deleted: Indicates whether the brand has been deleted
        - logo: Brand logo image file represented as an Attachment object
        - name: The name of the brand
        - signature_template: The signature template used for the brand
        - subdomain: The subdomain associated with the brand
        - ticket_form_ids: Array of ticket form IDs that are available for use by this brand
        - updated_at: Timestamp when the brand was last updated
        - url: The API URL for accessing this brand resource

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BrandsSearchResult with hits (list of AirbyteSearchHit[BrandsSearchData]) and pagination info

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

        result = await self._connector.execute("brands", "search", params)

        # Parse response into typed result
        return BrandsSearchResult(
            hits=[
                AirbyteSearchHit[BrandsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=BrandsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        view_id: str,
        **kwargs
    ) -> View:
        """
        Returns a view by its ID

        Args:
            view_id: The ID of the view
            **kwargs: Additional parameters

        Returns:
            View
        """
        params = {k: v for k, v in {
            "view_id": view_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("views", "get", params)
        return result



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
            meta=result.meta
        )



    async def get(
        self,
        macro_id: str,
        **kwargs
    ) -> Macro:
        """
        Returns a macro by its ID

        Args:
            macro_id: The ID of the macro
            **kwargs: Additional parameters

        Returns:
            Macro
        """
        params = {k: v for k, v in {
            "macro_id": macro_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("macros", "get", params)
        return result



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
            meta=result.meta
        )



    async def get(
        self,
        trigger_id: str,
        **kwargs
    ) -> Trigger:
        """
        Returns a trigger by its ID

        Args:
            trigger_id: The ID of the trigger
            **kwargs: Additional parameters

        Returns:
            Trigger
        """
        params = {k: v for k, v in {
            "trigger_id": trigger_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("triggers", "get", params)
        return result



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
            meta=result.meta
        )



    async def get(
        self,
        automation_id: str,
        **kwargs
    ) -> Automation:
        """
        Returns an automation by its ID

        Args:
            automation_id: The ID of the automation
            **kwargs: Additional parameters

        Returns:
            Automation
        """
        params = {k: v for k, v in {
            "automation_id": automation_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("automations", "get", params)
        return result



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
            meta=result.meta
        )



    async def search(
        self,
        query: TagsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TagsSearchResult:
        """
        Search tags records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TagsSearchFilter):
        - count: The number of times this tag has been used across resources
        - name: The tag name string used to label and categorize resources

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TagsSearchResult with hits (list of AirbyteSearchHit[TagsSearchData]) and pagination info

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

        result = await self._connector.execute("tags", "search", params)

        # Parse response into typed result
        return TagsSearchResult(
            hits=[
                AirbyteSearchHit[TagsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TagsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        satisfaction_rating_id: str,
        **kwargs
    ) -> SatisfactionRating:
        """
        Returns a satisfaction rating by its ID

        Args:
            satisfaction_rating_id: The ID of the satisfaction rating
            **kwargs: Additional parameters

        Returns:
            SatisfactionRating
        """
        params = {k: v for k, v in {
            "satisfaction_rating_id": satisfaction_rating_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("satisfaction_ratings", "get", params)
        return result



    async def search(
        self,
        query: SatisfactionRatingsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SatisfactionRatingsSearchResult:
        """
        Search satisfaction_ratings records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SatisfactionRatingsSearchFilter):
        - assignee_id: The identifier of the agent assigned to the ticket at the time the rating was submitted
        - comment: Optional comment provided by the requester with the rating
        - created_at: Timestamp indicating when the satisfaction rating was created
        - group_id: The identifier of the group assigned to the ticket at the time the rating was submitted
        - id: Unique identifier for the satisfaction rating, automatically assigned upon creation
        - reason: Free-text reason for a bad rating provided by the requester in a follow-up question
        - reason_id: Identifier for the predefined reason given for a negative rating
        - requester_id: The identifier of the ticket requester who submitted the satisfaction rating
        - score: The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'
        - ticket_id: The identifier of the ticket being rated
        - updated_at: Timestamp indicating when the satisfaction rating was last updated
        - url: The API URL of this satisfaction rating resource

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SatisfactionRatingsSearchResult with hits (list of AirbyteSearchHit[SatisfactionRatingsSearchData]) and pagination info

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

        result = await self._connector.execute("satisfaction_ratings", "search", params)

        # Parse response into typed result
        return SatisfactionRatingsSearchResult(
            hits=[
                AirbyteSearchHit[SatisfactionRatingsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=SatisfactionRatingsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



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
            meta=result.meta
        )



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
            meta=result.meta
        )



    async def get(
        self,
        sla_policy_id: str,
        **kwargs
    ) -> SLAPolicy:
        """
        Returns an SLA policy by its ID

        Args:
            sla_policy_id: The ID of the SLA policy
            **kwargs: Additional parameters

        Returns:
            SLAPolicy
        """
        params = {k: v for k, v in {
            "sla_policy_id": sla_policy_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sla_policies", "get", params)
        return result



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
            meta=result.meta
        )



    async def get(
        self,
        ticket_form_id: str,
        **kwargs
    ) -> TicketForm:
        """
        Returns a ticket form by its ID

        Args:
            ticket_form_id: The ID of the ticket form
            **kwargs: Additional parameters

        Returns:
            TicketForm
        """
        params = {k: v for k, v in {
            "ticket_form_id": ticket_form_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_forms", "get", params)
        return result



    async def search(
        self,
        query: TicketFormsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketFormsSearchResult:
        """
        Search ticket_forms records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketFormsSearchFilter):
        - active: Indicates if the form is set as active
        - agent_conditions: Array of condition sets for agent workspaces
        - created_at: Timestamp when the ticket form was created
        - default: Indicates if the form is the default form for this account
        - display_name: The name of the form that is displayed to an end user
        - end_user_conditions: Array of condition sets for end user products
        - end_user_visible: Indicates if the form is visible to the end user
        - id: Unique identifier for the ticket form, automatically assigned when creating the form
        - in_all_brands: Indicates if the form is available for use in all brands on this account
        - name: The name of the ticket form
        - position: The position of this form among other forms in the account, such as in a dropdown
        - raw_display_name: The dynamic content placeholder if present, or the display_name value if not
        - raw_name: The dynamic content placeholder if present, or the name value if not
        - restricted_brand_ids: IDs of all brands that this ticket form is restricted to
        - ticket_field_ids: IDs of all ticket fields included in this ticket form
        - updated_at: Timestamp of the last update to the ticket form
        - url: URL of the ticket form

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketFormsSearchResult with hits (list of AirbyteSearchHit[TicketFormsSearchData]) and pagination info

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

        result = await self._connector.execute("ticket_forms", "search", params)

        # Parse response into typed result
        return TicketFormsSearchResult(
            hits=[
                AirbyteSearchHit[TicketFormsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TicketFormsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Article:
        """
        Retrieves the details of a specific article

        Args:
            id: The unique ID of the article
            **kwargs: Additional parameters

        Returns:
            Article
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "get", params)
        return result



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
            meta=result.meta
        )



    async def get(
        self,
        article_id: str,
        attachment_id: str,
        **kwargs
    ) -> ArticleAttachment:
        """
        Retrieves the metadata of a specific attachment for a specific article

        Args:
            article_id: The unique ID of the article
            attachment_id: The unique ID of the attachment
            **kwargs: Additional parameters

        Returns:
            ArticleAttachment
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            "attachment_id": attachment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "get", params)
        return result



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

