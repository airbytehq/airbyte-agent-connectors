"""
Customer-Io connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import CustomerIoConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    ActivitiesListParams,
    BroadcastTriggerCreateParams,
    CampaignActionsGetParams,
    CampaignActionsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    CollectionsCreateParams,
    CollectionsGetParams,
    CollectionsListParams,
    CollectionsUpdateParams,
    ExportsCreateParams,
    ExportsGetParams,
    ExportsListParams,
    MessagesGetParams,
    MessagesListParams,
    NewslettersGetParams,
    NewslettersListParams,
    ReportingWebhooksCreateParams,
    ReportingWebhooksGetParams,
    ReportingWebhooksListParams,
    ReportingWebhooksUpdateParams,
    SegmentsCreateParams,
    SegmentsCreateParamsSegment,
    SegmentsGetParams,
    SegmentsListParams,
    SenderIdentitiesGetParams,
    SenderIdentitiesListParams,
    SnippetsCreateParams,
    SnippetsListParams,
    SnippetsUpdateParams,
    TransactionalEmailCreateParams,
    TransactionalInboxMessageCreateParams,
    TransactionalMessageContentsListParams,
    TransactionalMessageContentsUpdateParams,
    TransactionalMessageContentsUpdateParamsHeadersItem,
    TransactionalMessagesGetParams,
    TransactionalMessagesListParams,
    TransactionalPushCreateParams,
    TransactionalSmsCreateParams,
    AirbyteSearchParams,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    CampaignActionsSearchFilter,
    CampaignActionsSearchQuery,
    NewslettersSearchFilter,
    NewslettersSearchQuery,
)
from .models import CustomerIoAuthConfig
if TYPE_CHECKING:
    from .models import CustomerIoReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    CustomerIoCheckResult,
    CustomerIoExecuteResult,
    CustomerIoExecuteResultWithMeta,
    CampaignsListResult,
    CampaignActionsListResult,
    NewslettersListResult,
    SegmentsListResult,
    MessagesListResult,
    ActivitiesListResult,
    SenderIdentitiesListResult,
    SnippetsListResult,
    CollectionsListResult,
    ReportingWebhooksListResult,
    ExportsListResult,
    TransactionalMessagesListResult,
    TransactionalMessageContentsListResult,
    Activity,
    BroadcastTriggerResponse,
    Campaign,
    CampaignAction,
    Collection,
    Export,
    Message,
    Newsletter,
    ReportingWebhook,
    Segment,
    SenderIdentity,
    Snippet,
    TransactionalMessage,
    TransactionalMessageContent,
    TransactionalSendResponse,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    CampaignActionsSearchData,
    CampaignActionsSearchResult,
    NewslettersSearchData,
    NewslettersSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class CustomerIoConnector:
    """
    Type-safe Customer-Io API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "customer-io"
    connector_version = "1.0.0"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("campaign_actions", "list"): True,
        ("campaign_actions", "get"): None,
        ("newsletters", "list"): True,
        ("newsletters", "get"): None,
        ("segments", "list"): True,
        ("segments", "create"): None,
        ("segments", "get"): None,
        ("messages", "list"): True,
        ("messages", "get"): None,
        ("activities", "list"): True,
        ("sender_identities", "list"): True,
        ("sender_identities", "get"): None,
        ("snippets", "list"): True,
        ("snippets", "create"): None,
        ("snippets", "update"): None,
        ("collections", "list"): True,
        ("collections", "create"): None,
        ("collections", "get"): None,
        ("collections", "update"): None,
        ("reporting_webhooks", "list"): True,
        ("reporting_webhooks", "create"): None,
        ("reporting_webhooks", "get"): None,
        ("reporting_webhooks", "update"): None,
        ("exports", "list"): True,
        ("exports", "create"): None,
        ("exports", "get"): None,
        ("transactional_messages", "list"): True,
        ("transactional_messages", "get"): None,
        ("transactional_message_contents", "list"): True,
        ("transactional_message_contents", "update"): None,
        ("transactional_email", "create"): None,
        ("transactional_sms", "create"): None,
        ("transactional_push", "create"): None,
        ("transactional_inbox_message", "create"): None,
        ("broadcast_trigger", "create"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('campaigns', 'get'): {'campaign_id': 'campaign_id'},
        ('campaign_actions', 'list'): {'campaign_id': 'campaign_id', 'start': 'start'},
        ('campaign_actions', 'get'): {'campaign_id': 'campaign_id', 'action_id': 'action_id'},
        ('newsletters', 'list'): {'start': 'start', 'limit': 'limit', 'sort': 'sort'},
        ('newsletters', 'get'): {'newsletter_id': 'newsletter_id'},
        ('segments', 'create'): {'segment': 'segment'},
        ('segments', 'get'): {'segment_id': 'segment_id'},
        ('messages', 'list'): {'start': 'start', 'limit': 'limit', 'type': 'type', 'metric': 'metric', 'campaign_id': 'campaign_id', 'newsletter_id': 'newsletter_id'},
        ('messages', 'get'): {'message_id': 'message_id'},
        ('activities', 'list'): {'start': 'start', 'limit': 'limit', 'type': 'type', 'name': 'name'},
        ('sender_identities', 'list'): {'start': 'start', 'limit': 'limit', 'sort': 'sort'},
        ('sender_identities', 'get'): {'sender_id': 'sender_id'},
        ('snippets', 'create'): {'name': 'name', 'value': 'value'},
        ('snippets', 'update'): {'name': 'name', 'value': 'value'},
        ('collections', 'create'): {'name': 'name', 'data': 'data', 'url': 'url'},
        ('collections', 'get'): {'collection_id': 'collection_id'},
        ('collections', 'update'): {'name': 'name', 'data': 'data', 'url': 'url', 'collection_id': 'collection_id'},
        ('reporting_webhooks', 'create'): {'name': 'name', 'endpoint': 'endpoint', 'events': 'events', 'disabled': 'disabled', 'full_resolution': 'full_resolution', 'with_content': 'with_content'},
        ('reporting_webhooks', 'get'): {'webhook_id': 'webhook_id'},
        ('reporting_webhooks', 'update'): {'name': 'name', 'endpoint': 'endpoint', 'events': 'events', 'disabled': 'disabled', 'full_resolution': 'full_resolution', 'with_content': 'with_content', 'webhook_id': 'webhook_id'},
        ('exports', 'create'): {'filters': 'filters'},
        ('exports', 'get'): {'export_id': 'export_id'},
        ('transactional_messages', 'get'): {'transactional_id': 'transactional_id'},
        ('transactional_message_contents', 'list'): {'transactional_id': 'transactional_id'},
        ('transactional_message_contents', 'update'): {'body': 'body', 'from_id': 'from_id', 'reply_to_id': 'reply_to_id', 'recipient': 'recipient', 'subject': 'subject', 'preheader_text': 'preheader_text', 'body_amp': 'body_amp', 'headers': 'headers', 'transactional_id': 'transactional_id', 'content_id': 'content_id'},
        ('transactional_email', 'create'): {'transactional_message_id': 'transactional_message_id', 'to': 'to', 'identifiers': 'identifiers', 'message_data': 'message_data', 'from_': 'from', 'subject': 'subject', 'body': 'body', 'body_plain': 'body_plain', 'reply_to': 'reply_to', 'bcc': 'bcc', 'headers': 'headers', 'preheader_text': 'preheader_text', 'attachments': 'attachments', 'disable_message_retention': 'disable_message_retention', 'send_to_unsubscribed': 'send_to_unsubscribed', 'tracked': 'tracked', 'queue_draft': 'queue_draft', 'send_at': 'send_at'},
        ('transactional_sms', 'create'): {'transactional_message_id': 'transactional_message_id', 'to': 'to', 'identifiers': 'identifiers', 'message_data': 'message_data', 'from_': 'from', 'send_to_unsubscribed': 'send_to_unsubscribed', 'tracked': 'tracked', 'queue_draft': 'queue_draft', 'disable_message_retention': 'disable_message_retention'},
        ('transactional_push', 'create'): {'transactional_message_id': 'transactional_message_id', 'to': 'to', 'identifiers': 'identifiers', 'message_data': 'message_data', 'title': 'title', 'message': 'message', 'link': 'link', 'image_url': 'image_url', 'custom_data': 'custom_data', 'custom_payload': 'custom_payload', 'sound': 'sound', 'send_to_unsubscribed': 'send_to_unsubscribed', 'queue_draft': 'queue_draft', 'disable_message_retention': 'disable_message_retention', 'send_at': 'send_at'},
        ('transactional_inbox_message', 'create'): {'transactional_message_id': 'transactional_message_id', 'identifiers': 'identifiers', 'message_data': 'message_data'},
        ('broadcast_trigger', 'create'): {'data': 'data', 'recipients': 'recipients', 'ids': 'ids', 'emails': 'emails', 'per_user_data': 'per_user_data', 'data_file_url': 'data_file_url', 'id_ignore_missing': 'id_ignore_missing', 'email_ignore_missing': 'email_ignore_missing', 'email_add_duplicates': 'email_add_duplicates', 'campaign_id': 'campaign_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (CustomerIoAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: CustomerIoAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new customer-io connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., CustomerIoAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = CustomerIoConnector(auth_config=CustomerIoAuthConfig(app_api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = CustomerIoConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = CustomerIoConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
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
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(CustomerIoConnectorModel.id),
                model=CustomerIoConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or CustomerIoAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=CustomerIoConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.campaigns = CampaignsQuery(self)
        self.campaign_actions = CampaignActionsQuery(self)
        self.newsletters = NewslettersQuery(self)
        self.segments = SegmentsQuery(self)
        self.messages = MessagesQuery(self)
        self.activities = ActivitiesQuery(self)
        self.sender_identities = SenderIdentitiesQuery(self)
        self.snippets = SnippetsQuery(self)
        self.collections = CollectionsQuery(self)
        self.reporting_webhooks = ReportingWebhooksQuery(self)
        self.exports = ExportsQuery(self)
        self.transactional_messages = TransactionalMessagesQuery(self)
        self.transactional_message_contents = TransactionalMessageContentsQuery(self)
        self.transactional_email = TransactionalEmailQuery(self)
        self.transactional_sms = TransactionalSmsQuery(self)
        self.transactional_push = TransactionalPushQuery(self)
        self.transactional_inbox_message = TransactionalInboxMessageQuery(self)
        self.broadcast_trigger = BroadcastTriggerQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_actions"],
        action: Literal["list"],
        params: "CampaignActionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignActionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_actions"],
        action: Literal["get"],
        params: "CampaignActionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignAction": ...

    @overload
    async def execute(
        self,
        entity: Literal["newsletters"],
        action: Literal["list"],
        params: "NewslettersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "NewslettersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["newsletters"],
        action: Literal["get"],
        params: "NewslettersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Newsletter": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["list"],
        params: "SegmentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SegmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["create"],
        params: "SegmentsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["get"],
        params: "SegmentsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Segment": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["list"],
        params: "MessagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MessagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["get"],
        params: "MessagesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Message": ...

    @overload
    async def execute(
        self,
        entity: Literal["activities"],
        action: Literal["list"],
        params: "ActivitiesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ActivitiesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sender_identities"],
        action: Literal["list"],
        params: "SenderIdentitiesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SenderIdentitiesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sender_identities"],
        action: Literal["get"],
        params: "SenderIdentitiesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SenderIdentity": ...

    @overload
    async def execute(
        self,
        entity: Literal["snippets"],
        action: Literal["list"],
        params: "SnippetsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SnippetsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["snippets"],
        action: Literal["create"],
        params: "SnippetsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["snippets"],
        action: Literal["update"],
        params: "SnippetsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["collections"],
        action: Literal["list"],
        params: "CollectionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["collections"],
        action: Literal["create"],
        params: "CollectionsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["collections"],
        action: Literal["get"],
        params: "CollectionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Collection": ...

    @overload
    async def execute(
        self,
        entity: Literal["collections"],
        action: Literal["update"],
        params: "CollectionsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["reporting_webhooks"],
        action: Literal["list"],
        params: "ReportingWebhooksListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ReportingWebhooksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["reporting_webhooks"],
        action: Literal["create"],
        params: "ReportingWebhooksCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ReportingWebhook": ...

    @overload
    async def execute(
        self,
        entity: Literal["reporting_webhooks"],
        action: Literal["get"],
        params: "ReportingWebhooksGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ReportingWebhook": ...

    @overload
    async def execute(
        self,
        entity: Literal["reporting_webhooks"],
        action: Literal["update"],
        params: "ReportingWebhooksUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ReportingWebhook": ...

    @overload
    async def execute(
        self,
        entity: Literal["exports"],
        action: Literal["list"],
        params: "ExportsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ExportsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["exports"],
        action: Literal["create"],
        params: "ExportsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["exports"],
        action: Literal["get"],
        params: "ExportsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Export": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_messages"],
        action: Literal["list"],
        params: "TransactionalMessagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalMessagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_messages"],
        action: Literal["get"],
        params: "TransactionalMessagesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalMessage": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_message_contents"],
        action: Literal["list"],
        params: "TransactionalMessageContentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalMessageContentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_message_contents"],
        action: Literal["update"],
        params: "TransactionalMessageContentsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalMessageContent": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_email"],
        action: Literal["create"],
        params: "TransactionalEmailCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalSendResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_sms"],
        action: Literal["create"],
        params: "TransactionalSmsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalSendResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_push"],
        action: Literal["create"],
        params: "TransactionalPushCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalSendResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactional_inbox_message"],
        action: Literal["create"],
        params: "TransactionalInboxMessageCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionalSendResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["broadcast_trigger"],
        action: Literal["create"],
        params: "BroadcastTriggerCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BroadcastTriggerResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> CustomerIoExecuteResult[Any] | CustomerIoExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "context_store_search"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
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
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

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
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return CustomerIoExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return CustomerIoExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> CustomerIoCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            CustomerIoCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return CustomerIoCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return CustomerIoCheckResult(
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
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = CustomerIoConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @CustomerIoConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @CustomerIoConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @CustomerIoConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    CustomerIoConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

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
        return describe_entities(CustomerIoConnectorModel)

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
            (e for e in CustomerIoConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in CustomerIoConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a list of all campaigns in the workspace.

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data
        )



    async def get(
        self,
        campaign_id: str,
        **kwargs
    ) -> Campaign:
        """
        Returns a single campaign by ID.

        Args:
            campaign_id: The campaign identifier
            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def context_store_search(
        self,
        query: CampaignsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsSearchResult:
        """
        Search campaigns records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsSearchFilter):
        - actions: Actions defined in this campaign
        - active: Whether the campaign is active
        - created: Creation timestamp (Unix)
        - created_by: Who created the campaign
        - date_attribute: Date attribute used for date-triggered campaigns
        - deduplicate_id: Deduplication identifier
        - event_name: Event name that triggers the campaign
        - first_started: When the campaign was first started (Unix)
        - frequency: How frequently a person can receive this campaign
        - id: Unique campaign identifier
        - msg_templates: Message templates used in the campaign
        - name: Campaign name
        - start_hour: Hour of the day to trigger
        - start_minutes: Minute of the hour to trigger
        - state: Campaign status (draft, active, stopped)
        - tags: Tags associated with the campaign
        - timezone: Timezone for trigger scheduling
        - trigger_segment_ids: Segment IDs that trigger this campaign
        - type_: Campaign trigger type
        - updated: Last update timestamp (Unix)
        - use_customer_timezone: Whether to use the customer's timezone

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaigns", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignsSearchResult(
            data=[
                CampaignsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CampaignActionsQuery:
    """
    Query class for CampaignActions entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        campaign_id: str,
        start: str | None = None,
        **kwargs
    ) -> CampaignActionsListResult:
        """
        Returns a paginated list of actions for a campaign.

        Args:
            campaign_id: The campaign identifier
            start: Pagination cursor for the next page
            **kwargs: Additional parameters

        Returns:
            CampaignActionsListResult
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            "start": start,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_actions", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignActionsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        campaign_id: str,
        action_id: str,
        **kwargs
    ) -> CampaignAction:
        """
        Returns a single campaign action by ID.

        Args:
            campaign_id: The campaign identifier
            action_id: The action identifier
            **kwargs: Additional parameters

        Returns:
            CampaignAction
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            "action_id": action_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_actions", "get", params)
        return result



    async def context_store_search(
        self,
        query: CampaignActionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignActionsSearchResult:
        """
        Search campaign_actions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignActionsSearchFilter):
        - bcc: BCC addresses
        - body: Action body content (HTML for emails)
        - campaign_id: Parent campaign ID
        - created: Creation timestamp (Unix)
        - deduplicate_id: Deduplication identifier
        - editor: Editor used to create the action
        - fake_bcc: Whether to use fake BCC
        - from_: From address
        - from_id: Sender identity ID
        - headers: Custom email headers as JSON
        - id: Unique action identifier
        - language: Language variant
        - layout: Layout template used
        - name: Action name
        - parent_action_id: Parent action ID for language variants
        - preheader_text: Email preheader/preview text
        - preprocessor: CSS preprocessor setting
        - recipient: Recipient address
        - recipient_environment_id: Recipient environment ID
        - reply_to: Reply-to address
        - reply_to_id: Reply-to sender identity ID
        - request_method: HTTP request method for webhook actions
        - sending_state: Sending behavior (automatic or draft)
        - subject: Email subject line
        - type_: Action type (email, webhook, twilio, push, slack, in_app, whatsapp)
        - updated: Last update timestamp (Unix)
        - url: Webhook URL (for webhook actions)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignActionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaign_actions", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignActionsSearchResult(
            data=[
                CampaignActionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class NewslettersQuery:
    """
    Query class for Newsletters entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        **kwargs
    ) -> NewslettersListResult:
        """
        Returns a paginated list of newsletters.

        Args:
            start: Pagination cursor for the next page
            limit: Maximum number of newsletters to return
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            NewslettersListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "limit": limit,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("newsletters", "list", params)
        # Cast generic envelope to concrete typed result
        return NewslettersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        newsletter_id: str,
        **kwargs
    ) -> Newsletter:
        """
        Returns a single newsletter by ID.

        Args:
            newsletter_id: The newsletter identifier
            **kwargs: Additional parameters

        Returns:
            Newsletter
        """
        params = {k: v for k, v in {
            "newsletter_id": newsletter_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("newsletters", "get", params)
        return result



    async def context_store_search(
        self,
        query: NewslettersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> NewslettersSearchResult:
        """
        Search newsletters records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (NewslettersSearchFilter):
        - content_ids: Content variant IDs for this newsletter
        - created: Creation timestamp (Unix)
        - deduplicate_id: Deduplication identifier
        - id: Unique newsletter identifier
        - name: Newsletter name
        - sent_at: When the newsletter was last sent (Unix)
        - tags: Tags associated with the newsletter
        - type_: Channel type (email, webhook, twilio, push, in_app, inbox)
        - updated: Last update timestamp (Unix)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            NewslettersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("newsletters", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return NewslettersSearchResult(
            data=[
                NewslettersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SegmentsQuery:
    """
    Query class for Segments entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SegmentsListResult:
        """
        Returns all segments in the workspace.

        Returns:
            SegmentsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "list", params)
        # Cast generic envelope to concrete typed result
        return SegmentsListResult(
            data=result.data
        )



    async def create(
        self,
        segment: SegmentsCreateParamsSegment,
        **kwargs
    ) -> dict[str, Any]:
        """
        Creates a new empty manual segment. People can be added to it separately.

        Args:
            segment: Parameter segment
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "segment": segment,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "create", params)
        return result



    async def get(
        self,
        segment_id: str,
        **kwargs
    ) -> Segment:
        """
        Returns a single segment by ID.

        Args:
            segment_id: The segment identifier
            **kwargs: Additional parameters

        Returns:
            Segment
        """
        params = {k: v for k, v in {
            "segment_id": segment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "get", params)
        return result



class MessagesQuery:
    """
    Query class for Messages entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: str | None = None,
        limit: int | None = None,
        type: str | None = None,
        metric: str | None = None,
        campaign_id: int | None = None,
        newsletter_id: int | None = None,
        **kwargs
    ) -> MessagesListResult:
        """
        Returns a paginated list of message deliveries.

        Args:
            start: Pagination cursor for the next page
            limit: Maximum number of messages to return
            type: Filter messages by channel type
            metric: Filter messages by delivery metric
            campaign_id: Filter by campaign ID
            newsletter_id: Filter by newsletter ID
            **kwargs: Additional parameters

        Returns:
            MessagesListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "limit": limit,
            "type": type,
            "metric": metric,
            "campaign_id": campaign_id,
            "newsletter_id": newsletter_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "list", params)
        # Cast generic envelope to concrete typed result
        return MessagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        message_id: str,
        **kwargs
    ) -> Message:
        """
        Returns a single message delivery by ID. Untested because the test workspace has no message deliveries to retrieve.


        Args:
            message_id: The message delivery identifier
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "message_id": message_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "get", params)
        return result



class ActivitiesQuery:
    """
    Query class for Activities entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: str | None = None,
        limit: int | None = None,
        type: str | None = None,
        name: str | None = None,
        **kwargs
    ) -> ActivitiesListResult:
        """
        Returns a paginated list of activities in the workspace.

        Args:
            start: Pagination cursor for the next page
            limit: Maximum number of activities to return
            type: Filter by activity type
            name: Filter by event name
            **kwargs: Additional parameters

        Returns:
            ActivitiesListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "limit": limit,
            "type": type,
            "name": name,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("activities", "list", params)
        # Cast generic envelope to concrete typed result
        return ActivitiesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class SenderIdentitiesQuery:
    """
    Query class for SenderIdentities entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        **kwargs
    ) -> SenderIdentitiesListResult:
        """
        Returns a paginated list of sender identities.

        Args:
            start: Pagination cursor for the next page
            limit: Maximum number of sender identities to return
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            SenderIdentitiesListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "limit": limit,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sender_identities", "list", params)
        # Cast generic envelope to concrete typed result
        return SenderIdentitiesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        sender_id: str,
        **kwargs
    ) -> SenderIdentity:
        """
        Returns a single sender identity by ID.

        Args:
            sender_id: The sender identity identifier
            **kwargs: Additional parameters

        Returns:
            SenderIdentity
        """
        params = {k: v for k, v in {
            "sender_id": sender_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sender_identities", "get", params)
        return result



class SnippetsQuery:
    """
    Query class for Snippets entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SnippetsListResult:
        """
        Returns all snippets in the workspace.

        Returns:
            SnippetsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("snippets", "list", params)
        # Cast generic envelope to concrete typed result
        return SnippetsListResult(
            data=result.data
        )



    async def create(
        self,
        name: str,
        value: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Creates a new reusable content snippet. Returns 422 if a snippet with the same name already exists.

        Args:
            name: Unique snippet name (used as the liquid tag identifier)
            value: Snippet content (plain text, HTML, or Liquid)
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "name": name,
            "value": value,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("snippets", "create", params)
        return result



    async def update(
        self,
        name: str,
        value: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Updates an existing snippet by name, or creates it if it does not exist (upsert behavior).

        Args:
            name: Snippet name to update (or create if it does not exist)
            value: New snippet content (plain text, HTML, or Liquid)
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "name": name,
            "value": value,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("snippets", "update", params)
        return result



class CollectionsQuery:
    """
    Query class for Collections entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> CollectionsListResult:
        """
        Returns all collections in the workspace.

        Returns:
            CollectionsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collections", "list", params)
        # Cast generic envelope to concrete typed result
        return CollectionsListResult(
            data=result.data
        )



    async def create(
        self,
        name: str,
        data: list[dict[str, Any]] | None = None,
        url: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Creates a new data collection with inline data or a URL source.

        Args:
            name: Collection name, referenced in Liquid as collection_name.property
            data: Inline collection data (array of objects). Provide either data or url, not both.
            url: URL to a CSV or JSON file containing collection data. Provide either data or url, not both.
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "name": name,
            "data": data,
            "url": url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collections", "create", params)
        return result



    async def get(
        self,
        collection_id: str,
        **kwargs
    ) -> Collection:
        """
        Returns a single collection by ID.

        Args:
            collection_id: The collection identifier
            **kwargs: Additional parameters

        Returns:
            Collection
        """
        params = {k: v for k, v in {
            "collection_id": collection_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collections", "get", params)
        return result



    async def update(
        self,
        collection_id: str,
        name: str | None = None,
        data: list[dict[str, Any]] | None = None,
        url: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Updates an existing collection's name, data, or URL source.

        Args:
            name: Rename the collection
            data: Replace collection data entirely (array of objects). Provide either data or url, not both.
            url: Replace the URL source for collection data. Provide either data or url, not both.
            collection_id: The collection identifier
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "name": name,
            "data": data,
            "url": url,
            "collection_id": collection_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collections", "update", params)
        return result



class ReportingWebhooksQuery:
    """
    Query class for ReportingWebhooks entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ReportingWebhooksListResult:
        """
        Returns all reporting webhooks in the workspace.

        Returns:
            ReportingWebhooksListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reporting_webhooks", "list", params)
        # Cast generic envelope to concrete typed result
        return ReportingWebhooksListResult(
            data=result.data
        )



    async def create(
        self,
        name: str,
        endpoint: str,
        events: list[str],
        disabled: bool | None = None,
        full_resolution: bool | None = None,
        with_content: bool | None = None,
        **kwargs
    ) -> ReportingWebhook:
        """
        Creates a new reporting webhook to receive event notifications at the specified endpoint.

        Args:
            name: Webhook display name
            endpoint: The URL to receive webhook notifications
            events: Event types to report (e.g. customer_subscribed, email_sent, email_opened, email_clicked, email_bounced, email_converted, email_unsubscribed, sms_sent, sms_delivered, push_sent)

            disabled: Whether the webhook should be disabled initially
            full_resolution: Send all events instead of only unique events
            with_content: Include the message body in sent events
            **kwargs: Additional parameters

        Returns:
            ReportingWebhook
        """
        params = {k: v for k, v in {
            "name": name,
            "endpoint": endpoint,
            "events": events,
            "disabled": disabled,
            "full_resolution": full_resolution,
            "with_content": with_content,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reporting_webhooks", "create", params)
        return result



    async def get(
        self,
        webhook_id: str,
        **kwargs
    ) -> ReportingWebhook:
        """
        Returns a single reporting webhook by ID.

        Args:
            webhook_id: The reporting webhook identifier
            **kwargs: Additional parameters

        Returns:
            ReportingWebhook
        """
        params = {k: v for k, v in {
            "webhook_id": webhook_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reporting_webhooks", "get", params)
        return result



    async def update(
        self,
        name: str,
        endpoint: str,
        events: list[str],
        webhook_id: str,
        disabled: bool | None = None,
        full_resolution: bool | None = None,
        with_content: bool | None = None,
        **kwargs
    ) -> ReportingWebhook:
        """
        Updates an existing reporting webhook's configuration.

        Args:
            name: Webhook display name
            endpoint: The URL to receive webhook notifications
            events: Event types to report
            disabled: Whether the webhook is disabled
            full_resolution: Send all events instead of only unique events
            with_content: Include the message body in sent events
            webhook_id: The reporting webhook identifier
            **kwargs: Additional parameters

        Returns:
            ReportingWebhook
        """
        params = {k: v for k, v in {
            "name": name,
            "endpoint": endpoint,
            "events": events,
            "disabled": disabled,
            "full_resolution": full_resolution,
            "with_content": with_content,
            "webhook_id": webhook_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reporting_webhooks", "update", params)
        return result



class ExportsQuery:
    """
    Query class for Exports entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ExportsListResult:
        """
        Returns all exports in the workspace.

        Returns:
            ExportsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("exports", "list", params)
        # Cast generic envelope to concrete typed result
        return ExportsListResult(
            data=result.data
        )



    async def create(
        self,
        filters: dict[str, Any],
        **kwargs
    ) -> dict[str, Any]:
        """
        Triggers a new export of customer data. Use filters to select which customers to export.

        Args:
            filters: Audience filter conditions to select which customers to export. Uses boolean logic with "and", "or", "not" arrays of conditions, "segment" objects with an "id" field, and "attribute" objects with "field", "operator", and "value" fields. Example: {"and": [{"segment": {"id": 3}}, {"attribute": {"field": "plan", "operator": "eq", "value": "premium"}}]}

            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "filters": filters,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("exports", "create", params)
        return result



    async def get(
        self,
        export_id: str,
        **kwargs
    ) -> Export:
        """
        Returns a single export by ID.

        Args:
            export_id: The export identifier
            **kwargs: Additional parameters

        Returns:
            Export
        """
        params = {k: v for k, v in {
            "export_id": export_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("exports", "get", params)
        return result



class TransactionalMessagesQuery:
    """
    Query class for TransactionalMessages entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TransactionalMessagesListResult:
        """
        Returns a list of all transactional message templates in the workspace.

        Returns:
            TransactionalMessagesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_messages", "list", params)
        # Cast generic envelope to concrete typed result
        return TransactionalMessagesListResult(
            data=result.data
        )



    async def get(
        self,
        transactional_id: str,
        **kwargs
    ) -> TransactionalMessage:
        """
        Returns a single transactional message template by ID.

        Args:
            transactional_id: The transactional message identifier
            **kwargs: Additional parameters

        Returns:
            TransactionalMessage
        """
        params = {k: v for k, v in {
            "transactional_id": transactional_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_messages", "get", params)
        return result



class TransactionalMessageContentsQuery:
    """
    Query class for TransactionalMessageContents entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        transactional_id: str,
        **kwargs
    ) -> TransactionalMessageContentsListResult:
        """
        Returns all content variants (including language translations) for a transactional message template.

        Args:
            transactional_id: The transactional message identifier
            **kwargs: Additional parameters

        Returns:
            TransactionalMessageContentsListResult
        """
        params = {k: v for k, v in {
            "transactional_id": transactional_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_message_contents", "list", params)
        # Cast generic envelope to concrete typed result
        return TransactionalMessageContentsListResult(
            data=result.data
        )



    async def update(
        self,
        transactional_id: str,
        content_id: str,
        body: str | None = None,
        from_id: int | None = None,
        reply_to_id: int | None | None = None,
        recipient: str | None = None,
        subject: str | None = None,
        preheader_text: str | None = None,
        body_amp: str | None = None,
        headers: list[TransactionalMessageContentsUpdateParamsHeadersItem] | None = None,
        **kwargs
    ) -> TransactionalMessageContent:
        """
        Updates the content of a specific variant of a transactional message template by content ID.

        Args:
            body: HTML body content of the message
            from_id: Sender identity ID
            reply_to_id: Reply-to sender identity ID
            recipient: Recipient expression (e.g. "{{customer.email}}")
            subject: Email subject line
            preheader_text: Email preheader/preview text
            body_amp: AMP HTML body content
            headers: Custom email headers as an array of name-value objects
            transactional_id: The transactional message identifier
            content_id: The content variant identifier
            **kwargs: Additional parameters

        Returns:
            TransactionalMessageContent
        """
        params = {k: v for k, v in {
            "body": body,
            "from_id": from_id,
            "reply_to_id": reply_to_id,
            "recipient": recipient,
            "subject": subject,
            "preheader_text": preheader_text,
            "body_amp": body_amp,
            "headers": headers,
            "transactional_id": transactional_id,
            "content_id": content_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_message_contents", "update", params)
        return result



class TransactionalEmailQuery:
    """
    Query class for TransactionalEmail entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        to: str,
        identifiers: dict[str, Any],
        transactional_message_id: Any | None = None,
        message_data: dict[str, Any] | None = None,
        from_: str | None = None,
        subject: str | None = None,
        body: str | None = None,
        body_plain: str | None = None,
        reply_to: str | None = None,
        bcc: str | None = None,
        headers: dict[str, Any] | None = None,
        preheader_text: str | None = None,
        attachments: dict[str, Any] | None = None,
        disable_message_retention: bool | None = None,
        send_to_unsubscribed: bool | None = None,
        tracked: bool | None = None,
        queue_draft: bool | None = None,
        send_at: int | None = None,
        **kwargs
    ) -> TransactionalSendResponse:
        """
        Sends a transactional email to a single recipient. Can use a pre-built template (via transactional_message_id) or provide inline content (subject, body, from). Creates the recipient profile if it does not already exist.


        Args:
            transactional_message_id: Template ID (number) or trigger name (string). Required if not providing inline body/subject/from.
            to: Recipient email address. Supports display name format: "Name <email>"
            identifiers: Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}
            message_data: Key-value pairs available as {{trigger.<key>}} in templates
            from_: Sender address (must be verified domain). Overrides template if provided.
            subject: Email subject line. Overrides template if provided.
            body: HTML email body. Overrides template if provided.
            body_plain: Plaintext email body
            reply_to: Reply-to email address
            bcc: BCC address(es), comma-separated. Max 15 total recipients.
            headers: Custom email headers (ASCII only)
            preheader_text: Email preview text
            attachments: Map of filename to base64 content: {"file.pdf": "<base64>"}. Max 2MB total.
            disable_message_retention: Do not store message body (for sensitive data)
            send_to_unsubscribed: Send even if person is unsubscribed
            tracked: Enable open and click tracking
            queue_draft: Queue as draft instead of sending immediately
            send_at: Unix timestamp for scheduled delivery (up to 90 days in the future)
            **kwargs: Additional parameters

        Returns:
            TransactionalSendResponse
        """
        params = {k: v for k, v in {
            "transactional_message_id": transactional_message_id,
            "to": to,
            "identifiers": identifiers,
            "message_data": message_data,
            "from": from_,
            "subject": subject,
            "body": body,
            "body_plain": body_plain,
            "reply_to": reply_to,
            "bcc": bcc,
            "headers": headers,
            "preheader_text": preheader_text,
            "attachments": attachments,
            "disable_message_retention": disable_message_retention,
            "send_to_unsubscribed": send_to_unsubscribed,
            "tracked": tracked,
            "queue_draft": queue_draft,
            "send_at": send_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_email", "create", params)
        return result



class TransactionalSmsQuery:
    """
    Query class for TransactionalSms entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        transactional_message_id: Any,
        to: str,
        identifiers: dict[str, Any],
        message_data: dict[str, Any] | None = None,
        from_: str | None = None,
        send_to_unsubscribed: bool | None = None,
        tracked: bool | None = None,
        queue_draft: bool | None = None,
        disable_message_retention: bool | None = None,
        **kwargs
    ) -> TransactionalSendResponse:
        """
        Sends a transactional SMS to a single recipient. Always requires a pre-built template (transactional_message_id). Requires Twilio integration to be configured in the workspace.


        Args:
            transactional_message_id: Template ID (number) or trigger name (string). Always required for SMS.
            to: Phone number in E.164 format (e.g. +15551234567)
            identifiers: Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}
            message_data: Key-value pairs available as {{trigger.<key>}} in templates
            from_: Override sender phone number (must be verified in Twilio)
            send_to_unsubscribed: Send even if person is unsubscribed
            tracked: Enable link tracking
            queue_draft: Queue as draft instead of sending immediately
            disable_message_retention: Do not store message content
            **kwargs: Additional parameters

        Returns:
            TransactionalSendResponse
        """
        params = {k: v for k, v in {
            "transactional_message_id": transactional_message_id,
            "to": to,
            "identifiers": identifiers,
            "message_data": message_data,
            "from": from_,
            "send_to_unsubscribed": send_to_unsubscribed,
            "tracked": tracked,
            "queue_draft": queue_draft,
            "disable_message_retention": disable_message_retention,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_sms", "create", params)
        return result



class TransactionalPushQuery:
    """
    Query class for TransactionalPush entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        identifiers: dict[str, Any],
        transactional_message_id: Any | None = None,
        to: str | None = None,
        message_data: dict[str, Any] | None = None,
        title: str | None = None,
        message: str | None = None,
        link: str | None = None,
        image_url: str | None = None,
        custom_data: dict[str, Any] | None = None,
        custom_payload: dict[str, Any] | None = None,
        sound: str | None = None,
        send_to_unsubscribed: bool | None = None,
        queue_draft: bool | None = None,
        disable_message_retention: bool | None = None,
        send_at: int | None = None,
        **kwargs
    ) -> TransactionalSendResponse:
        """
        Sends a transactional push notification to a single recipient. Can use a template or provide inline title and message. Requires push notifications to be configured in the workspace.


        Args:
            transactional_message_id: Template ID or trigger name. Required if not providing inline title/message.
            to: Device target: "last_used" for most recent device, or a specific device token. Defaults to all devices.
            identifiers: Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}
            message_data: Key-value pairs available as {{trigger.<key>}} in templates
            title: Push notification title (overrides template)
            message: Push notification body (overrides template)
            link: Deep link URL
            image_url: Image URL to display in the notification
            custom_data: Custom key-value data included in the push payload
            custom_payload: Platform-specific payload overrides (iOS/Android)
            sound: Notification sound name
            send_to_unsubscribed: Send even if person is unsubscribed
            queue_draft: Queue as draft instead of sending immediately
            disable_message_retention: Do not store message content
            send_at: Unix timestamp for scheduled delivery
            **kwargs: Additional parameters

        Returns:
            TransactionalSendResponse
        """
        params = {k: v for k, v in {
            "transactional_message_id": transactional_message_id,
            "to": to,
            "identifiers": identifiers,
            "message_data": message_data,
            "title": title,
            "message": message,
            "link": link,
            "image_url": image_url,
            "custom_data": custom_data,
            "custom_payload": custom_payload,
            "sound": sound,
            "send_to_unsubscribed": send_to_unsubscribed,
            "queue_draft": queue_draft,
            "disable_message_retention": disable_message_retention,
            "send_at": send_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_push", "create", params)
        return result



class TransactionalInboxMessageQuery:
    """
    Query class for TransactionalInboxMessage entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        transactional_message_id: Any,
        identifiers: dict[str, Any],
        message_data: dict[str, Any] | None = None,
        **kwargs
    ) -> TransactionalSendResponse:
        """
        Sends a transactional in-app inbox message to a single recipient. Always requires a pre-built Inbox-type transactional message template (transactional_message_id). Messages appear in the recipient's notification inbox via the Customer.io SDK.


        Args:
            transactional_message_id: Template ID or trigger name. Must reference an Inbox-type transactional message.
            identifiers: Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}
            message_data: Key-value pairs available as {{trigger.<key>}} in the inbox message template
            **kwargs: Additional parameters

        Returns:
            TransactionalSendResponse
        """
        params = {k: v for k, v in {
            "transactional_message_id": transactional_message_id,
            "identifiers": identifiers,
            "message_data": message_data,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactional_inbox_message", "create", params)
        return result



class BroadcastTriggerQuery:
    """
    Query class for BroadcastTrigger entity operations.
    """

    def __init__(self, connector: CustomerIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        campaign_id: str,
        data: dict[str, Any] | None = None,
        recipients: dict[str, Any] | None = None,
        ids: list[str] | None = None,
        emails: list[str] | None = None,
        per_user_data: list[dict[str, Any]] | None = None,
        data_file_url: str | None = None,
        id_ignore_missing: bool | None = None,
        email_ignore_missing: bool | None = None,
        email_add_duplicates: bool | None = None,
        **kwargs
    ) -> BroadcastTriggerResponse:
        """
        Triggers an API-triggered broadcast campaign. The broadcast must be configured as API-triggered in the Customer.io UI. Cannot be triggered more than once every 10 seconds, with a maximum of 5 queued broadcasts per campaign. Recipients must already exist in the workspace.


        Args:
            data: Global data available as {{trigger.<key>}} in broadcast messages
            recipients: Filter object to define audience (overrides UI-defined recipients). Supports and/or/not/segment/attribute conditions.
            ids: List of profile IDs to target (max 10,000)
            emails: List of email addresses to target (max 10,000)
            per_user_data: Per-recipient custom data: [{"id": "user1", "data": {...}}, ...]
            data_file_url: URL to a JSON Lines file with per-user data
            id_ignore_missing: Ignore IDs that do not match existing profiles (default false)
            email_ignore_missing: Ignore emails that do not match existing profiles
            email_add_duplicates: Send to all profiles sharing an email address
            campaign_id: The broadcast campaign identifier (found in Triggering Details)
            **kwargs: Additional parameters

        Returns:
            BroadcastTriggerResponse
        """
        params = {k: v for k, v in {
            "data": data,
            "recipients": recipients,
            "ids": ids,
            "emails": emails,
            "per_user_data": per_user_data,
            "data_file_url": data_file_url,
            "id_ignore_missing": id_ignore_missing,
            "email_ignore_missing": email_ignore_missing,
            "email_add_duplicates": email_add_duplicates,
            "campaign_id": campaign_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("broadcast_trigger", "create", params)
        return result


