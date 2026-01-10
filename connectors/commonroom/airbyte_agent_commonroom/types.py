"""
Type definitions for commonroom connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict
except ImportError:
    from typing import TypedDict  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ApiTokenStatusListParams(TypedDict):
    """Parameters for api_token_status.list operation"""
    pass

class ContactCustomFieldsListParams(TypedDict):
    """Parameters for contact_custom_fields.list operation"""
    pass

class ActivityTypesListParams(TypedDict):
    """Parameters for activity_types.list operation"""
    pass

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    pass

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    pass
