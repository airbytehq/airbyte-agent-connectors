"""
Type definitions for stripe connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    limit: NotRequired[int]
    starting_after: NotRequired[str]
    ending_before: NotRequired[str]
    email: NotRequired[str]

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    id: str
