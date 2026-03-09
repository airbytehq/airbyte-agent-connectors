"""Shared redaction logic for both logging and telemetry."""

from typing import Any, Dict
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


class DataRedactor:
    """Shared redaction logic for both logging and telemetry."""

    SENSITIVE_HEADER_PATTERNS = [
        "authorization",
        "api-key",
        "x-api-key",
        "token",
        "bearer",
        "secret",
        "password",
        "credential",
    ]

    SENSITIVE_PARAM_PATTERNS = [
        "password",
        "secret",
        "api_key",
        "apikey",
        "token",
        "credentials",
        "auth",
        "key",
    ]

    @staticmethod
    def redact_headers(headers: Dict[str, str]) -> Dict[str, str]:
        """Redact sensitive headers."""
        redacted = {}
        for key, value in headers.items():
            if any(pattern in key.lower() for pattern in DataRedactor.SENSITIVE_HEADER_PATTERNS):
                redacted[key] = "***REDACTED***"
            else:
                redacted[key] = value
        return redacted

    @staticmethod
    def redact_params(params: Dict[str, Any]) -> Dict[str, Any]:
        """Redact sensitive parameters."""
        redacted = {}
        for key, value in params.items():
            if any(pattern in key.lower() for pattern in DataRedactor.SENSITIVE_PARAM_PATTERNS):
                redacted[key] = "***REDACTED***"
            else:
                redacted[key] = value
        return redacted

    @staticmethod
    def redact_url(url: str) -> str:
        """Redact sensitive query params from URL."""
        parsed = urlparse(url)
        if not parsed.query:
            return url

        params = parse_qs(parsed.query)
        redacted_params = {}

        for key, values in params.items():
            if any(pattern in key.lower() for pattern in DataRedactor.SENSITIVE_PARAM_PATTERNS):
                redacted_params[key] = ["***REDACTED***"] * len(values)
            else:
                redacted_params[key] = values

        # Reconstruct URL with redacted params
        new_query = urlencode(redacted_params, doseq=True)
        return urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                parsed.path,
                parsed.params,
                new_query,
                parsed.fragment,
            )
        )
