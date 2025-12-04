"""Async HTTP client with connection pooling, auth injection, and metrics."""

from __future__ import annotations

import asyncio
from collections import defaultdict
from collections.abc import Awaitable, Callable
from datetime import datetime
from typing import Any

from .constants import (
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_MAX_CONNECTIONS,
    DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
    DEFAULT_REQUEST_TIMEOUT,
)
from .http import (
    AuthenticationError,
    ClientConfig,
    ConnectionLimits,
    HTTPClientError,
    HTTPClientProtocol,
    HTTPStatusError,
    NetworkError,
    RateLimitError,
    TimeoutConfig,
    TimeoutError,
)
from .http.adapters import HTTPXClient
from .secrets import SecretStr

from .auth_strategies import AuthStrategyFactory
from .logging import NullLogger
from .types import AuthConfig, AuthType

# Type alias for token refresh callback
# Supports both sync and async callbacks for flexibility
TokenRefreshCallback = (
    Callable[[dict[str, str]], None]
    | Callable[[dict[str, str]], Awaitable[None]]
    | None
)


class HTTPMetrics:
    """Metrics collector for HTTP requests."""

    def __init__(self):
        """Initialize metrics."""
        self.request_count = 0
        self.error_count = 0
        self.total_duration = 0.0
        self.status_counts: dict[int, int] = defaultdict(int)

    def record_request(self, duration: float, status_code: int, success: bool):
        """Record a request metric.

        Args:
            duration: Request duration in seconds
            status_code: HTTP status code
            success: Whether the request succeeded
        """
        self.request_count += 1
        self.total_duration += duration
        self.status_counts[status_code] += 1
        if not success:
            self.error_count += 1

    @property
    def avg_duration(self) -> float:
        """Get average request duration."""
        if self.request_count == 0:
            return 0.0
        return self.total_duration / self.request_count

    def get_stats(self) -> dict[str, Any]:
        """Get metrics as dictionary."""
        return {
            "request_count": self.request_count,
            "error_count": self.error_count,
            "avg_duration": self.avg_duration,
            "total_duration": self.total_duration,
            "status_counts": dict(self.status_counts),
        }


class HTTPClient:
    """Async HTTP client for making API requests with authentication and connection pooling."""

    def __init__(
        self,
        base_url: str,
        auth_config: AuthConfig,
        secrets: dict[str, SecretStr | str],
        config_values: dict[str, str] | None = None,
        client: HTTPClientProtocol | None = None,
        logger: Any | None = None,
        max_connections: int = DEFAULT_MAX_CONNECTIONS,
        max_keepalive_connections: int = DEFAULT_MAX_KEEPALIVE_CONNECTIONS,
        timeout: float = DEFAULT_REQUEST_TIMEOUT,
        connect_timeout: float | None = None,
        read_timeout: float | None = None,
        on_token_refresh: TokenRefreshCallback = None,
    ):
        """Initialize async HTTP client.

        Args:
            base_url: Base URL for API (e.g., https://api.stripe.com)
            auth_config: Authentication configuration from connector.yaml
            secrets: Secret credentials (SecretStr or plain str values)
            config_values: Non-secret configuration values (e.g., {"subdomain": "mycompany"})
                Used for server variables and template substitution in OAuth2 refresh URLs.
            client: Optional HTTPClientProtocol implementation. If None, creates HTTPXClient.
            logger: Optional RequestLogger instance for logging requests/responses
            max_connections: Maximum number of concurrent connections
            max_keepalive_connections: Maximum number of keepalive connections
            timeout: Default timeout in seconds (used if connect/read not specified)
            connect_timeout: Connection timeout in seconds
            read_timeout: Read timeout in seconds
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Signature: (new_tokens: dict[str, str]) -> None (sync or async).
                Called when tokens are refreshed. Use to persist updated tokens.
        """
        self.base_url = base_url.rstrip("/")
        self.config_values = config_values or {}

        # Substitute server variables in base_url (e.g., {subdomain} -> "mycompany")
        for var_name, var_value in self.config_values.items():
            self.base_url = self.base_url.replace(f"{{{var_name}}}", var_value)

        self.auth_config = auth_config
        self.secrets = secrets
        self.config_values = config_values or {}
        self.logger = logger or NullLogger()
        self.metrics = HTTPMetrics()
        self.on_token_refresh: TokenRefreshCallback = on_token_refresh

        # Auth error handling with refresh lock (for strategies that support refresh)
        self._refresh_lock = asyncio.Lock()

        # Validate base URL
        if not base_url:
            raise ValueError("base_url cannot be empty")

        if not base_url.startswith(("http://", "https://")):
            raise ValueError(
                f"base_url must start with http:// or https://, got: {base_url}"
            )

        # Create HTTP client if not provided
        if client is None:
            # Create default client configuration
            config = ClientConfig(
                base_url=None,  # We handle base_url ourselves
                limits=ConnectionLimits(
                    max_connections=max_connections,
                    max_keepalive_connections=max_keepalive_connections,
                ),
                timeout=TimeoutConfig(
                    connect=connect_timeout or DEFAULT_CONNECT_TIMEOUT,
                    read=read_timeout or timeout,
                    write=timeout,
                    pool=timeout,
                ),
            )
            client = HTTPXClient(config=config)

        self.client = client

    @classmethod
    def create_default(
        cls,
        base_url: str,
        auth_config: AuthConfig,
        secrets: dict[str, SecretStr | str],
        logger: Any | None = None,
        **kwargs: Any,
    ) -> HTTPClient:
        """Create an HTTPClient with default HTTP client (HTTPXClient).

        This is a convenience factory method for the common case of using httpx.

        Args:
            base_url: Base URL for API (e.g., https://api.stripe.com)
            auth_config: Authentication configuration from connector.yaml
            secrets: Secret credentials (SecretStr or plain str values)
            logger: Optional RequestLogger instance for logging requests/responses
            **kwargs: Additional arguments passed to __init__

        Returns:
            Configured HTTPClient instance with HTTPXClient
        """
        return cls(
            base_url=base_url,
            auth_config=auth_config,
            secrets=secrets,
            client=None,  # Will create default HTTPXClient
            logger=logger,
            **kwargs,
        )

    def _validate_auth_credentials(self) -> None:
        """Validate that required auth credentials are present.

        Raises:
            AuthenticationError: If required credentials are missing
        """
        if self.auth_config.type == AuthType.API_KEY:
            api_key = self.secrets.get("api_key")
            if not api_key:
                raise AuthenticationError(
                    "Missing required credential 'api_key' for API_KEY authentication"
                )

        elif self.auth_config.type == AuthType.BEARER:
            token = self.secrets.get("token") or self.secrets.get("api_key")
            if not token:
                raise AuthenticationError(
                    "Missing required credential 'token' or 'api_key' for BEARER authentication"
                )

        elif self.auth_config.type == AuthType.BASIC:
            username = self.secrets.get("username")
            password = self.secrets.get("password")
            if not username or not password:
                raise AuthenticationError(
                    "Missing required credentials 'username' and 'password' for BASIC authentication"
                )

    def _inject_auth(self, headers: dict[str, str]) -> dict[str, str]:
        """Inject authentication into request headers.

        Args:
            headers: Existing headers

        Returns:
            Headers with authentication added

        Raises:
            AuthenticationError: If required credentials are missing
        """
        strategy = AuthStrategyFactory.get_strategy(self.auth_config.type)
        return strategy.inject_auth(headers, self.auth_config.config, self.secrets)

    async def request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        *,
        stream: bool = False,
    ):
        """Make an async HTTP request with optional streaming.

        Args:
            method: HTTP method (GET, POST, etc.)
            path: API path or full URL
            params: Query parameters
            json: JSON body for POST/PUT
            data: Form-encoded body for POST/PUT (mutually exclusive with json)
            headers: Additional headers
            stream: If True, do not eagerly read the body (useful for downloads)

        Returns:
            - If stream=False: Parsed JSON (dict) or empty dict
            - If stream=True: Response object suitable for streaming

        Raises:
            HTTPStatusError: If request fails with 4xx/5xx status
            AuthenticationError: For 401 or 403 status codes
            RateLimitError: For 429 status codes
            TimeoutError: If request times out
            NetworkError: If network error occurs
            HTTPClientError: For other client errors
        """
        # Check if path is a full URL (for CDN/external URLs)
        is_external_url = path.startswith(
            ("http://", "https://")
        ) and not path.startswith(self.base_url)
        url = (
            path
            if path.startswith(("http://", "https://"))
            else f"{self.base_url}{path}"
        )

        # Prepare headers with auth (skip for external URLs like pre-signed S3)
        request_headers = headers or {}
        if not is_external_url:
            request_headers = self._inject_auth(request_headers)

        # Log request start
        request_id = self.logger.log_request(
            method=method.upper(),
            url=url,
            path=path,
            headers=request_headers,
            params=params,
            body=json or data,
        )

        # Track timing
        start_time = datetime.now()
        success = False
        status_code = 0

        try:
            # Make async request through HTTP client protocol
            response = await self.client.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json,
                data=data,
                headers=request_headers,
                stream=stream,
            )

            status_code = response.status_code

            # Streaming path: return response without reading body
            if stream:
                success = True

                # Log placeholder (without consuming stream)
                # Actual chunks will be logged via log_chunk_fetch() during iteration
                self.logger.log_response(
                    request_id=request_id,
                    status_code=status_code,
                    response_body=f"<binary content, {response.headers.get('content-length', 'unknown')} bytes>",
                )
                return response

            # Parse response - handle non-JSON responses gracefully
            content_type = response.headers.get("content-type", "")

            try:
                # Check if response has content first
                response_text = await response.text()

                if not response_text.strip():
                    # Empty response - return empty dict
                    response_data = {}
                elif "application/json" in content_type or not content_type:
                    # Try to parse as JSON
                    response_data = await response.json()
                else:
                    # Non-JSON response with content
                    error_msg = (
                        f"Expected JSON response for {method.upper()} {url}, "
                        f"got content-type: {content_type}"
                    )
                    raise HTTPClientError(error_msg)

            except ValueError as e:
                # Malformed JSON
                error_msg = f"Failed to parse JSON response for {method.upper()} {url}: {str(e)}"
                raise HTTPClientError(error_msg)

            success = True

            # Log successful response
            self.logger.log_response(
                request_id=request_id,
                status_code=status_code,
                response_body=response_data,
            )

            return response_data

        except RateLimitError as e:
            # Rate limit error (429) - already wrapped by adapter
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=429,
            )
            raise

        except AuthenticationError as e:
            # Auth error (401, 403) - already wrapped by adapter
            status_code = e.status_code if hasattr(e, "status_code") else 401

            # Attempt to handle auth error (e.g., token refresh for OAuth2)
            # Use lock to prevent concurrent refresh attempts
            async with self._refresh_lock:
                # Check if credentials were already refreshed by another
                # concurrent request while we were waiting for the lock
                current_token = self.secrets.get("access_token")

                # Get the current auth strategy
                strategy = AuthStrategyFactory.get_strategy(self.auth_config.type)

                # Ask strategy to handle the error (returns new tokens or None)
                try:
                    new_tokens = await strategy.handle_auth_error(
                        status_code=status_code,
                        config=self.auth_config.config,
                        secrets=self.secrets,
                        config_values=self.config_values,
                        http_client=self.client._client
                        if hasattr(self.client, "_client")
                        else None,
                    )

                    if new_tokens:
                        # Notify callback if provided (for persistence)
                        if self.on_token_refresh is not None:
                            try:
                                # Support both sync and async callbacks
                                result = self.on_token_refresh(new_tokens)
                                if hasattr(result, "__await__"):
                                    await result
                            except Exception as callback_error:
                                # Log but don't fail the refresh if callback fails
                                self.logger.log_error(
                                    request_id=request_id,
                                    error=f"Token refresh callback failed: {str(callback_error)}",
                                    status_code=status_code,
                                )

                        # Update secrets with new tokens (in-memory)
                        self.secrets.update(new_tokens)

                        # Retry request if credentials changed
                        if self.secrets.get("access_token") != current_token:
                            return await self.request(
                                method=method,
                                path=path,
                                params=params,
                                json=json,
                                data=data,
                                headers=headers,
                            )

                except Exception as refresh_error:
                    # Credential refresh failed, log and continue
                    self.logger.log_error(
                        request_id=request_id,
                        error=f"Credential refresh failed: {str(refresh_error)}",
                        status_code=status_code,
                    )
                    # Fall through to raise original auth error

            # Log and raise the authentication error
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=status_code,
            )
            raise

        except HTTPStatusError as e:
            # Other HTTP errors (4xx, 5xx) - already wrapped by adapter
            status_code = e.status_code if hasattr(e, "status_code") else 0
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=status_code,
            )
            raise

        except TimeoutError as e:
            # Timeout error - already wrapped by adapter
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=None,
            )
            raise

        except NetworkError as e:
            # Network error - already wrapped by adapter
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=None,
            )
            raise

        except HTTPClientError as e:
            # General HTTP client error
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=status_code if status_code else None,
            )
            raise

        except Exception as e:
            # Other unexpected errors
            error_msg = f"Unexpected error for {method.upper()} {url}: {str(e)}"
            self.logger.log_error(
                request_id=request_id,
                error=error_msg,
                status_code=status_code if status_code else None,
            )
            raise HTTPClientError(error_msg)

        finally:
            # Record metrics
            duration = (datetime.now() - start_time).total_seconds()
            self.metrics.record_request(duration, status_code, success)

    async def close(self):
        """Close the async HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
