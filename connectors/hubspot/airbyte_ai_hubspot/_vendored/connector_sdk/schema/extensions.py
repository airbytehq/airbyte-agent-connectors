"""
Extension models for future features.

These models are defined but NOT yet added to the main schema models.
They serve as:
1. Type hints for future use
2. Documentation of planned extensions
3. Ready-to-use structures when features are implemented

NOTE: These are not currently active in the schema. They will be added
to Operation, Schema, or other models when their respective features
are implemented.
"""

from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict


class PaginationConfig(BaseModel):
    """
    Configuration for pagination support.

    NOT YET USED - Defined for future implementation.

    When active, will be added to Operation model as:
        x_pagination: Optional[PaginationConfig] = Field(None, alias="x-pagination")
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    style: Literal["cursor", "offset", "page", "link"]
    limit_param: str = "limit"

    # Cursor-based pagination
    cursor_param: Optional[str] = None
    cursor_source: Optional[Literal["body", "headers"]] = "body"
    cursor_path: Optional[str] = None

    # Offset-based pagination
    offset_param: Optional[str] = None

    # Page-based pagination
    page_param: Optional[str] = None

    # Response parsing
    data_path: str = "data"
    has_more_path: Optional[str] = None

    # Limits
    max_page_size: Optional[int] = None
    default_page_size: int = 100


class RateLimitConfig(BaseModel):
    """
    Configuration for rate limiting.

    NOT YET USED - Defined for future implementation.

    When active, might be added to Server or root OpenAPIConnector as:
        x_rate_limit: Optional[RateLimitConfig] = Field(None, alias="x-rate-limit")
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    max_requests: int
    time_window_seconds: int
    retry_after_header: Optional[str] = "Retry-After"
    respect_retry_after: bool = True


class RetryConfig(BaseModel):
    """
    Configuration for retry strategy.

    NOT YET USED - Defined for future implementation.

    When active, might be added to Server or root OpenAPIConnector as:
        x_retry: Optional[RetryConfig] = Field(None, alias="x-retry")
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    max_attempts: int = 3
    backoff_strategy: Literal["exponential", "linear", "constant"] = "exponential"
    initial_delay_seconds: float = 1.0
    max_delay_seconds: float = 60.0
    retry_on_status_codes: Optional[list[int]] = None  # e.g., [429, 503]
