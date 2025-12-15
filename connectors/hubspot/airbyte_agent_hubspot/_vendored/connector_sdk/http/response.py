"""HTTP response wrapper providing a consistent interface across HTTP clients."""

import json as json_module
from typing import Any


class HTTPResponse:
    """Wrapper for HTTP responses that provides a consistent interface.

    This class wraps responses from any HTTP client (httpx, aiohttp, etc.) and
    provides a standard interface that the SDK can rely on.
    """

    def __init__(
        self,
        status_code: int,
        headers: dict[str, str],
        content: bytes,
        _original_response: Any | None = None,
    ) -> None:
        """Initialize an HTTP response wrapper.

        Args:
            status_code: The HTTP status code (e.g., 200, 404, 500)
            headers: Response headers as a dictionary
            content: Raw response body as bytes
            _original_response: Optional original response object from the underlying client
        """
        self._status_code = status_code
        self._headers = headers
        self._content = content
        self._original_response = _original_response
        self._text_cache: str | None = None
        self._json_cache: Any | None = None
        self._json_parsed = False

    @property
    def status_code(self) -> int:
        """The HTTP status code of the response."""
        return self._status_code

    @property
    def headers(self) -> dict[str, str]:
        """The response headers as a dictionary."""
        return self._headers

    async def text(self) -> str:
        """Get the response body as text.

        Returns:
            The response body decoded as a string.
        """
        if self._text_cache is None:
            self._text_cache = self._content.decode("utf-8", errors="replace")
        return self._text_cache

    async def json(self) -> Any:
        """Parse the response body as JSON.

        Returns:
            The parsed JSON data (dict, list, or primitive).

        Raises:
            ValueError: If the response body is not valid JSON.
        """
        if not self._json_parsed:
            try:
                text = await self.text()
                self._json_cache = json_module.loads(text)
            except json_module.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON in response: {e}") from e
            finally:
                self._json_parsed = True
        return self._json_cache

    def raise_for_status(self) -> None:
        """Raise an exception if the response status indicates an error.

        Raises:
            HTTPStatusError: For 4xx or 5xx status codes.
        """
        if 400 <= self._status_code < 600:
            from .exceptions import HTTPStatusError

            raise HTTPStatusError(
                status_code=self._status_code,
                message=f"HTTP {self._status_code} error",
                response=self,
            )

    @property
    def original_response(self) -> Any | None:
        """Get the original response object from the underlying HTTP client.

        This is provided for advanced use cases but should generally not be needed.
        Returns None if the original response was not provided.
        """
        return self._original_response

    def __repr__(self) -> str:
        """String representation of the response."""
        return f"HTTPResponse(status_code={self.status_code})"
