"""Async HTTP client with connection pooling, auth injection, metrics, and retry support."""

from __future__ import annotations

import asyncio
import random
import time
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
from .schema.extensions import RetryConfig
from .secrets import SecretStr

from .auth_strategies import AuthStrategyFactory
from .logging import NullLogger
from .types import AuthConfig, AuthType

# Type alias for token refresh callback
# Supports both sync and async callbacks for flexibility
TokenRefreshCallback = Callable[[dict[str, str]], None] | Callable[[dict[str, str]], Awaitable[None]] | None


class HTTPMetrics:
    """Metrics collector for HTTP requests."""

    def __init__(self):
        """Initialize metrics."""
        self.request_count = 0
        self.error_count = 0
        self.total_duration = 0.0
        self.status_counts: dict[int, int] = defaultdict(int)
        # Retry metrics
        self.retry_count = 0
        self.total_retry_delay = 0.0

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

    def record_retry(self, delay: float):
        """Record a retry attempt.

        Args:
            delay: Delay in seconds before the retry
        """
        self.retry_count += 1
        self.total_retry_delay += delay

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
            "retry_count": self.retry_count,
            "total_retry_delay": self.total_retry_delay,
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
        retry_config: RetryConfig | None = None,
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
            retry_config: Optional retry configuration for transient errors.
                If None, uses default RetryConfig with sensible defaults.
        """
        # Store original base_url template for re-rendering after token extraction
        self._base_url_template = base_url.rstrip("/")
        self.config_values = config_values or {}

        # Substitute server variables in base_url (e.g., {subdomain} -> "mycompany")
        self.base_url = self._base_url_template
        for var_name, var_value in self.config_values.items():
            self.base_url = self.base_url.replace(f"{{{var_name}}}", var_value)

        self.auth_config = auth_config
        assert (
            self.auth_config.type is not None
        ), "auth_config.type cannot be None"  # Should never be None when instantiated via the local executor flow
        self.secrets = secrets
        self.logger = logger or NullLogger()
        self.metrics = HTTPMetrics()
        self.on_token_refresh: TokenRefreshCallback = on_token_refresh
        self.retry_config = retry_config or RetryConfig()

        # Auth error handling with refresh lock (for strategies that support refresh)
        self._refresh_lock = asyncio.Lock()
        # Track whether proactive credential initialization has been performed
        self._credentials_initialized = False

        # Validate base URL template
        if not base_url:
            raise ValueError("base_url cannot be empty")

        # Check if base_url has unresolved template variables (e.g., {instance_url})
        # These will be resolved later from token_extract in OAuth2 flows
        has_unresolved_variables = "{" in self.base_url and "}" in self.base_url

        # Only validate URL format if there are no unresolved variables
        if not has_unresolved_variables and not self.base_url.startswith(("http://", "https://")):
            raise ValueError(f"base_url must start with http:// or https://, got: {self.base_url}")

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
                raise AuthenticationError("Missing required credential 'api_key' for API_KEY authentication")

        elif self.auth_config.type == AuthType.BEARER:
            token = self.secrets.get("token") or self.secrets.get("api_key")
            if not token:
                raise AuthenticationError("Missing required credential 'token' or 'api_key' for BEARER authentication")

        elif self.auth_config.type == AuthType.BASIC:
            username = self.secrets.get("username")
            password = self.secrets.get("password")
            if not username or not password:
                raise AuthenticationError("Missing required credentials 'username' and 'password' for BASIC authentication")

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

    async def _ensure_auth_initialized(self) -> None:
        """Ensure authentication credentials are initialized.

        For auth strategies that support proactive credential acquisition
        (e.g., OAuth2 refresh-token-only mode), this method is called
        before the first request to obtain necessary credentials.

        Thread-safe via _refresh_lock. Only runs once per HTTPClient instance.
        """
        if self._credentials_initialized:
            return

        async with self._refresh_lock:
            # Double-check after acquiring lock (another request may have initialized)
            if self._credentials_initialized:
                return

            strategy = AuthStrategyFactory.get_strategy(self.auth_config.type)

            result = await strategy.ensure_credentials(
                config=self.auth_config.config,
                secrets=self.secrets,
                config_values=self.config_values,
                http_client=None,  # Let strategy create its own client
            )

            if result:
                # Notify callback if provided (for persistence)
                if self.on_token_refresh is not None:
                    try:
                        # Build callback data with both tokens and extracted values
                        callback_data = dict(result.tokens)
                        if result.extracted_values:
                            callback_data.update(result.extracted_values)

                        # Support both sync and async callbacks
                        callback_result = self.on_token_refresh(callback_data)
                        if callback_result is not None and hasattr(callback_result, "__await__"):
                            await callback_result
                    except Exception as callback_error:
                        self.logger.log_error(
                            request_id=None,
                            error=(f"Token refresh callback failed during initialization: {callback_error!s}"),
                            status_code=None,
                        )

                # Update secrets with new tokens (in-memory)
                self.secrets.update(result.tokens)

                # Update config_values and re-render base_url with extracted values
                if result.extracted_values:
                    self._apply_token_extract(result.extracted_values)

            self._credentials_initialized = True

    def _apply_token_extract(self, extracted_values: dict[str, str]) -> None:
        """Apply extracted token values to config_values and re-render base_url.

        This method is called after OAuth2 token refresh when the token response
        includes values specified by x-airbyte-token-extract (e.g., instance_url
        for Salesforce).

        Args:
            extracted_values: Dictionary of field name -> value extracted from
                the token response
        """
        # Update config_values with extracted values
        self.config_values.update(extracted_values)

        # Re-render base_url with updated config_values
        self.base_url = self._base_url_template
        for var_name, var_value in self.config_values.items():
            self.base_url = self.base_url.replace(f"{{{var_name}}}", var_value)

    def _should_retry(
        self,
        exception: Exception,
        status_code: int | None,
        attempt: int,
    ) -> bool:
        """Determine if a request should be retried.

        Args:
            exception: The exception that was raised
            status_code: HTTP status code if available
            attempt: Current attempt number (0-indexed)

        Returns:
            True if the request should be retried
        """
        # Check if we have retries remaining
        if attempt >= self.retry_config.max_attempts - 1:
            return False

        # Check status code-based retries
        if status_code and status_code in self.retry_config.retry_on_status_codes:
            return True

        # Check timeout retries
        if self.retry_config.retry_on_timeout and isinstance(exception, TimeoutError):
            return True

        # Check network error retries
        if self.retry_config.retry_on_network_error and isinstance(exception, NetworkError):
            return True

        return False

    def _calculate_delay(self, attempt: int, response_headers: dict[str, str]) -> float:
        """Calculate delay before the next retry attempt.

        Prefers Retry-After header if present, otherwise uses exponential backoff
        with optional jitter.

        Args:
            attempt: The current attempt number (0-indexed)
            response_headers: Response headers from the failed request

        Returns:
            Delay in seconds before the next retry
        """
        # Try Retry-After header first
        header_name = self.retry_config.retry_after_header
        header_value = response_headers.get(header_name) or response_headers.get(header_name.lower())

        if header_value:
            try:
                value = float(header_value)
                if self.retry_config.retry_after_format == "milliseconds":
                    delay = value / 1000.0
                elif self.retry_config.retry_after_format == "unix_timestamp":
                    delay = max(0.0, value - time.time())
                else:
                    delay = value
                return min(delay, self.retry_config.max_delay_seconds)
            except (ValueError, TypeError):
                pass  # Fall through to exponential backoff

        # Exponential backoff: initial_delay * (base ^ attempt)
        delay = self.retry_config.initial_delay_seconds * (self.retry_config.exponential_base**attempt)
        delay = min(delay, self.retry_config.max_delay_seconds)

        # Apply full jitter to prevent thundering herd
        # See: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
        if self.retry_config.jitter:
            delay = random.random() * delay

        return delay

    async def _execute_request(
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
        """Execute a single HTTP request attempt (no retries).

        This is the core request logic, separated from retry handling.
        """
        # Ensure auth credentials are initialized (proactive refresh if needed)
        await self._ensure_auth_initialized()

        # Check if path is a full URL (for CDN/external URLs)
        is_external_url = path.startswith(("http://", "https://")) and not path.startswith(self.base_url)
        url = path if path.startswith(("http://", "https://")) else f"{self.base_url}{path}"

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
                self.logger.log_response(
                    request_id=request_id,
                    status_code=status_code,
                    response_body=f"<binary content, {response.headers.get('content-length', 'unknown')} bytes>",
                )
                return response

            # Parse response - handle non-JSON responses gracefully
            content_type = response.headers.get("content-type", "")

            try:
                response_text = await response.text()

                if not response_text.strip():
                    response_data = {}
                elif "application/json" in content_type or not content_type:
                    response_data = await response.json()
                else:
                    error_msg = f"Expected JSON response for {method.upper()} {url}, got content-type: {content_type}"
                    raise HTTPClientError(error_msg)

            except ValueError as e:
                error_msg = f"Failed to parse JSON response for {method.upper()} {url}: {str(e)}"
                raise HTTPClientError(error_msg)

            success = True
            self.logger.log_response(
                request_id=request_id,
                status_code=status_code,
                response_body=response_data,
            )
            return response_data

        except AuthenticationError as e:
            # Auth error (401, 403) - handle token refresh
            status_code = e.status_code if hasattr(e, "status_code") else 401
            result = await self._handle_auth_error(e, request_id, method, path, params, json, data, headers)
            if result is not None:
                return result  # Token refresh succeeded, return the retry result
            raise  # Token refresh failed or not applicable

        except (RateLimitError, HTTPStatusError, TimeoutError, NetworkError) as e:
            # These may be retried by the caller
            status_code = getattr(e, "status_code", 0) or 0
            self.logger.log_error(request_id=request_id, error=str(e), status_code=status_code or None)
            raise

        except HTTPClientError as e:
            self.logger.log_error(
                request_id=request_id,
                error=str(e),
                status_code=status_code if status_code else None,
            )
            raise

        except Exception as e:
            error_msg = f"Unexpected error for {method.upper()} {url}: {str(e)}"
            self.logger.log_error(
                request_id=request_id,
                error=error_msg,
                status_code=status_code if status_code else None,
            )
            raise HTTPClientError(error_msg)

        finally:
            duration = (datetime.now() - start_time).total_seconds()
            self.metrics.record_request(duration, status_code, success)

    async def _handle_auth_error(
        self,
        error: AuthenticationError,
        request_id: str,
        method: str,
        path: str,
        params: dict[str, Any] | None,
        json: dict[str, Any] | None,
        data: dict[str, Any] | None,
        headers: dict[str, str] | None,
    ):
        """Handle authentication error with potential token refresh.

        Raises the original error if refresh fails or is not applicable.
        """
        status_code = error.status_code if hasattr(error, "status_code") else 401

        async with self._refresh_lock:
            current_token = self.secrets.get("access_token")
            strategy = AuthStrategyFactory.get_strategy(self.auth_config.type)

            # Try to refresh credentials
            try:
                result = await strategy.handle_auth_error(
                    status_code=status_code,
                    config=self.auth_config.config,
                    secrets=self.secrets,
                    config_values=self.config_values,
                    http_client=None,  # Let strategy create its own client
                )
            except Exception as refresh_error:
                self.logger.log_error(
                    request_id=request_id,
                    error=f"Credential refresh failed: {str(refresh_error)}",
                    status_code=status_code,
                )
                result = None

            # If refresh succeeded, update tokens and retry
            if result:
                # Notify callback if provided (for persistence)
                # Include both tokens AND extracted values for full persistence
                if self.on_token_refresh is not None:
                    try:
                        # Build callback data with both tokens and extracted values
                        callback_data = dict(result.tokens)
                        if result.extracted_values:
                            callback_data.update(result.extracted_values)

                        # Support both sync and async callbacks
                        callback_result = self.on_token_refresh(callback_data)
                        if callback_result is not None and hasattr(callback_result, "__await__"):
                            await callback_result
                    except Exception as callback_error:
                        self.logger.log_error(
                            request_id=request_id,
                            error=f"Token refresh callback failed: {str(callback_error)}",
                            status_code=status_code,
                        )

                # Update secrets with new tokens (in-memory)
                self.secrets.update(result.tokens)

                # Update config_values and re-render base_url with extracted values
                if result.extracted_values:
                    self._apply_token_extract(result.extracted_values)

                if self.secrets.get("access_token") != current_token:
                    # Retry with new token - this will go through full retry logic
                    # Any errors from this retry will propagate to the caller
                    return await self.request(
                        method=method,
                        path=path,
                        params=params,
                        json=json,
                        data=data,
                        headers=headers,
                    )

        # Refresh failed or token didn't change, log and let original error propagate
        self.logger.log_error(request_id=request_id, error=str(error), status_code=status_code)

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
        _auth_retry_attempted: bool = False,
    ):
        """Make an async HTTP request with optional streaming and automatic retries.

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
            HTTPStatusError: If request fails with 4xx/5xx status after all retries
            AuthenticationError: For 401 or 403 status codes
            RateLimitError: For 429 status codes (after all retries if configured)
            TimeoutError: If request times out (after all retries if configured)
            NetworkError: If network error occurs (after all retries if configured)
            HTTPClientError: For other client errors
        """
        for attempt in range(self.retry_config.max_attempts):
            try:
                return await self._execute_request(method, path, params, json, data, headers, stream=stream)
            except (RateLimitError, HTTPStatusError, TimeoutError, NetworkError) as e:
                status_code = getattr(e, "status_code", None)
                headers_from_error = getattr(e, "headers", {}) or {}

                if not self._should_retry(e, status_code, attempt):
                    raise

                delay = self._calculate_delay(attempt, headers_from_error)
                self.metrics.record_retry(delay)
                await asyncio.sleep(delay)
            # AuthenticationError, HTTPClientError, and other exceptions propagate immediately

        # Should not reach here, but just in case
        raise HTTPClientError("Exhausted all retry attempts")

    async def close(self):
        """Close the async HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
