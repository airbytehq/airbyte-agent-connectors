"""HTTPX adapter implementing the HTTP client protocol."""

from typing import Any

import httpx

from ..config import ClientConfig, ConnectionLimits, TimeoutConfig
from ..exceptions import (
    AuthenticationError,
    HTTPStatusError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)
from ..protocols import HTTPResponseProtocol
from ..response import HTTPResponse


class HTTPXClient:
    """HTTPX-based implementation of the HTTP client protocol.

    This adapter wraps httpx.AsyncClient and provides the HTTPClientProtocol interface,
    allowing httpx to be swapped out for a different HTTP client in the future.
    """

    def __init__(self, config: ClientConfig | None = None) -> None:
        """Initialize the HTTPX client adapter.

        Args:
            config: Client configuration. If None, uses default configuration.
        """
        self.config = config or ClientConfig()
        self._client: httpx.AsyncClient | None = None

    def _create_client(self) -> httpx.AsyncClient:
        """Create and configure the httpx AsyncClient.

        Returns:
            Configured httpx.AsyncClient instance.
        """
        # Convert SDK config to httpx config
        limits = self._convert_limits(self.config.limits)  # type: ignore
        timeout = self._convert_timeout(self.config.timeout)  # type: ignore

        return httpx.AsyncClient(
            base_url=self.config.base_url or "",
            timeout=timeout,
            limits=limits,
            follow_redirects=self.config.follow_redirects,
        )

    def _convert_limits(self, limits: ConnectionLimits) -> httpx.Limits:
        """Convert SDK ConnectionLimits to httpx.Limits.

        Args:
            limits: SDK connection limits configuration

        Returns:
            httpx.Limits instance
        """
        return httpx.Limits(
            max_connections=limits.max_connections,
            max_keepalive_connections=limits.max_keepalive_connections,
        )

    def _convert_timeout(self, timeout: TimeoutConfig) -> httpx.Timeout:
        """Convert SDK TimeoutConfig to httpx.Timeout.

        Args:
            timeout: SDK timeout configuration

        Returns:
            httpx.Timeout instance
        """
        return httpx.Timeout(
            connect=timeout.connect,
            read=timeout.read,
            write=timeout.write,
            pool=timeout.pool,
        )

    def _convert_response(self, httpx_response: httpx.Response, *, stream: bool = False) -> HTTPResponse:
        """Convert httpx.Response to SDK HTTPResponse.

        Args:
            httpx_response: The httpx response object
            stream: Whether the response should be treated as streaming (do not eagerly read body)

        Returns:
            HTTPResponse wrapping the httpx response
        """
        return HTTPResponse(
            status_code=httpx_response.status_code,
            headers=dict(httpx_response.headers),
            # When streaming, avoid eagerly reading the body
            content=b"" if stream else httpx_response.content,
            _original_response=httpx_response,
        )

    async def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | str | None = None,
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> HTTPResponseProtocol:
        """Execute an HTTP request using httpx.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            url: The URL to request
            params: Query parameters to append to the URL
            json: JSON data to send in the request body
            data: Form data or raw string to send in the request body
            headers: HTTP headers to include in the request
            **kwargs: Additional httpx-specific parameters

        Returns:
            HTTPResponse with the response data.

        Raises:
            HTTPStatusError: For 4xx or 5xx HTTP status codes
            AuthenticationError: For 401 or 403 status codes
            RateLimitError: For 429 status codes
            TimeoutError: For timeout errors
            NetworkError: For network/connection errors
        """
        if self._client is None:
            self._client = self._create_client()

        # Extract stream parameter (not supported by httpx.request directly)
        stream = kwargs.pop("stream", False)

        try:
            # Execute the request
            httpx_response = await self._client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                data=data,
                headers=headers,
                **kwargs,
            )

            # Convert to SDK response
            response = self._convert_response(httpx_response, stream=stream)

            # Check for HTTP errors and wrap them
            if httpx_response.status_code >= 400:
                await self._handle_http_error(httpx_response, response)

            return response

        except httpx.TimeoutException as e:
            raise TimeoutError(
                message=f"Request timed out: {e}",
                timeout_type=None,  # httpx doesn't provide specific timeout type
                original_error=e,
            ) from e

        except (httpx.ConnectError, httpx.NetworkError) as e:
            raise NetworkError(
                message=f"Network error: {e}",
                original_error=e,
            ) from e

    async def _handle_http_error(self, httpx_response: httpx.Response, sdk_response: HTTPResponse) -> None:
        """Handle HTTP error responses by raising appropriate SDK exceptions.

        Args:
            httpx_response: The original httpx response
            sdk_response: The converted SDK response

        Raises:
            AuthenticationError: For 401 or 403 status codes
            RateLimitError: For 429 status codes
            HTTPStatusError: For other 4xx or 5xx status codes
        """
        status_code = httpx_response.status_code

        # Try to get error message from response
        try:
            error_data = httpx_response.json()
            error_message = error_data.get("message") or error_data.get("error") or str(error_data)
        except Exception:
            error_message = httpx_response.text or f"HTTP {status_code} error"

        # Raise specific exceptions based on status code
        if status_code in (401, 403):
            raise AuthenticationError(
                message=f"Authentication failed: {error_message} (HTTP {status_code})",
                status_code=status_code,
                response=sdk_response,
            )

        if status_code == 429:
            # Try to parse Retry-After header
            retry_after = None
            if "retry-after" in httpx_response.headers:
                try:
                    retry_after = int(httpx_response.headers["retry-after"])
                except ValueError:
                    pass

            error_msg = f"Rate limit exceeded: {error_message}"
            if retry_after:
                error_msg += f" (retry after {retry_after}s)"

            raise RateLimitError(
                message=error_msg,
                retry_after=retry_after,
                response=sdk_response,
            )

        # Generic HTTP error
        raise HTTPStatusError(
            status_code=status_code,
            message=error_message,
            response=sdk_response,
        )

    async def aclose(self) -> None:
        """Close the HTTP client and cleanup resources."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "HTTPXClient":
        """Enter async context manager.

        Returns:
            The client instance.
        """
        if self._client is None:
            self._client = self._create_client()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit async context manager and cleanup resources.

        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        """
        await self.aclose()
