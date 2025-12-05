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
    ArticleAttachment,
    ArticleAttachmentList,
    ArticleAttachmentsDownloadParams,
    ArticleAttachmentsGetParams,
    ArticleAttachmentsListParams,
    ArticleList,
    ArticlesGetParams,
    ArticlesListParams,
)

if TYPE_CHECKING:
    from .models import ZendeskSupportAuthConfig

# Import envelope models at runtime (needed for instantiation in action methods)
from .models import (
    ZendeskSupportExecuteResult,
    ZendeskSupportExecuteResultWithMeta,
)


class ZendeskSupportConnector:
    """
    Type-safe Zendesk-Support API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-support"
    connector_version = "0.1.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("articles", "list"): False,
        ("articles", "get"): False,
        ("article_attachments", "list"): False,
        ("article_attachments", "get"): False,
        ("article_attachments", "download"): False,
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
            connector = ZendeskSupportConnector(auth_config=ZendeskSupportAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
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

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if subdomain:
                base_url = base_url.replace("{subdomain}", subdomain)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
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
        entity: Literal["articles"],
        action: Literal["list"],
        params: "ArticlesListParams"
    ) -> "ArticleList": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["get"],
        params: "ArticlesGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["article_attachments"],
        action: Literal["list"],
        params: "ArticleAttachmentsListParams"
    ) -> "ArticleAttachmentList": ...

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



class ArticlesQuery:
    """
    Query class for Articles entity operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ArticleList:
        """
        Returns a list of all articles in the Help Center

        Args:
            per_page: Number of results per page
            page: Page number for pagination
            sort_by: Sort articles by field (created_at, updated_at, title, position)
            sort_order: Sort order (asc or desc)
            **kwargs: Additional parameters

        Returns:
            ArticleList
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Retrieves the details of a specific article

        Args:
            id: The unique ID of the article
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
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
        **kwargs
    ) -> ArticleAttachmentList:
        """
        Returns a list of all attachments for a specific article

        Args:
            article_id: The unique ID of the article
            **kwargs: Additional parameters

        Returns:
            ArticleAttachmentList
        """
        params = {k: v for k, v in {
            "article_id": article_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("article_attachments", "list", params)
        return result



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

