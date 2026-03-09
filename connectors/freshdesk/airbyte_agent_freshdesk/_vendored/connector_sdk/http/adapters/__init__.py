"""HTTP client adapter implementations.

This package contains implementations of HTTPClientProtocol for different
HTTP client libraries.
"""

from .httpx_adapter import HTTPXClient

__all__ = ["HTTPXClient"]
