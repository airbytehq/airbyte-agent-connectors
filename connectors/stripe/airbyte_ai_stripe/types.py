"""
Auto-generated type definitions for stripe connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

# ===== AUTH CONFIG TYPE DEFINITIONS =====

class StripeAuthConfig(TypedDict):
    """Authentication"""
    token: str  # Authentication bearer token

# ===== RESPONSE TYPE DEFINITIONS =====

class Customer(TypedDict):
    """Customer type definition"""
    id: str
    object: str
    email: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    phone: NotRequired[str]
    address: NotRequired[dict[str, Any]]
    metadata: NotRequired[dict[str, str]]
    created: NotRequired[int]
    balance: NotRequired[int]
    delinquent: NotRequired[bool]

class CustomerList(TypedDict):
    """CustomerList type definition"""
    object: NotRequired[str]
    data: NotRequired[list[Customer]]
    has_more: NotRequired[bool]
    url: NotRequired[str]

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
