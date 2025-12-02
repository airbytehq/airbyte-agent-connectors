"""
Auto-generated zendesk-support connector. Do not edit manually.

Generated from OpenAPI specification.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Any, Dict, overload, Self
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from pathlib import Path

if TYPE_CHECKING:
    from ._vendored.connector_sdk.executor import ExecutorProtocol
    from .types import (
        ArticleAttachmentList,
        ArticleAttachmentsListParams,
        ArticleList,
        ArticlesGetParams,
        ArticlesListParams,
    )


class ZendeskSupportConnector:
    """
    Type-safe Zendesk-Support API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-support"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(self, executor: ExecutorProtocol):
        """Initialize connector with an executor."""
        self._executor = executor
        self.articles = ArticlesQuery(self)
        self.article_attachments = ArticleattachmentsQuery(self)

    @classmethod
    def create(
        cls,
        secrets: Optional[dict[str, str]] = None,
        config_path: Optional[str] = None,
        connector_id: Optional[str] = None,
        airbyte_client_id: Optional[str] = None,
        airbyte_client_secret: Optional[str] = None,
        airbyte_connector_api_url: Optional[str] = None,
        subdomain: Optional[str] = None    ) -> Self:
        """
        Create a new zendesk-support connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `secrets` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            secrets: API secrets/credentials (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)            subdomain: Your Zendesk subdomain
        Returns:
            Configured ZendeskSupportConnector instance

        Examples:
            # Local mode (direct API calls)
            connector = ZendeskSupportConnector.create(secrets={"api_key": "sk_..."})

            # Hosted mode (executed on Airbyte cloud)
            connector = ZendeskSupportConnector.create(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )
        """
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
            return cls(executor)

        # Local mode: secrets required
        if not secrets:
            raise ValueError(
                "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                "or secrets for local mode"
            )

        from ._vendored.connector_sdk.executor import LocalExecutor

        if not config_path:
            config_path = str(cls.get_default_config_path())

        executor = LocalExecutor(config_path=config_path, secrets=secrets)
        connector = cls(executor)

        # Update base_url with server variables if provided

        base_url = executor.http_client.base_url
        if subdomain:
            base_url = base_url.replace("{subdomain}", subdomain)
        executor.http_client.base_url = base_url

        return connector

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====
    @overload
    async def execute(
        self,
        resource: Literal["articles"],
        verb: Literal["list"],
        params: "ArticlesListParams"
    ) -> "ArticleList": ...
    @overload
    async def execute(
        self,
        resource: Literal["articles"],
        verb: Literal["get"],
        params: "ArticlesGetParams"
    ) -> "dict[str, Any]": ...
    @overload
    async def execute(
        self,
        resource: Literal["article_attachments"],
        verb: Literal["list"],
        params: "ArticleAttachmentsListParams"
    ) -> "ArticleAttachmentList": ...

    @overload
    async def execute(
        self,
        resource: str,
        verb: str,
        params: Dict[str, Any]
    ) -> Dict[str, Any]: ...

    async def execute(
        self,
        resource: str,
        verb: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Execute a resource operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for resource/verb/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            resource: Resource name (e.g., "customers")
            verb: Operation verb (e.g., "create", "get", "list")
            params: Operation parameters (typed based on resource+verb)

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                resource="customers",
                verb="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            resource=resource,
            verb=verb,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        return result.data



class ArticlesQuery:
    """
    Query class for Articles resource operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        **kwargs
    ) -> "ArticleList":
        """
        List all articles

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

        return await self._connector.execute("articles", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "dict[str, Any]":
        """
        Get an article by ID

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

        return await self._connector.execute("articles", "get", params)
class ArticleattachmentsQuery:
    """
    Query class for Articleattachments resource operations.
    """

    def __init__(self, connector: ZendeskSupportConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        article_id: str,
        **kwargs
    ) -> "ArticleAttachmentList":
        """
        List attachments for an article

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

        return await self._connector.execute("article_attachments", "list", params)