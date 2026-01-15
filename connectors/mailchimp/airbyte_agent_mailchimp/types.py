"""
Type definitions for mailchimp connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    type: NotRequired[str]
    status: NotRequired[str]
    before_send_time: NotRequired[str]
    since_send_time: NotRequired[str]
    before_create_time: NotRequired[str]
    since_create_time: NotRequired[str]
    list_id: NotRequired[str]
    folder_id: NotRequired[str]
    sort_field: NotRequired[str]
    sort_dir: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    campaign_id: str

class ListsListParams(TypedDict):
    """Parameters for lists.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    before_date_created: NotRequired[str]
    since_date_created: NotRequired[str]
    before_campaign_last_sent: NotRequired[str]
    since_campaign_last_sent: NotRequired[str]
    email: NotRequired[str]
    sort_field: NotRequired[str]
    sort_dir: NotRequired[str]

class ListsGetParams(TypedDict):
    """Parameters for lists.get operation"""
    list_id: str

class ListMembersListParams(TypedDict):
    """Parameters for list_members.list operation"""
    list_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
    email_type: NotRequired[str]
    status: NotRequired[str]
    since_timestamp_opt: NotRequired[str]
    before_timestamp_opt: NotRequired[str]
    since_last_changed: NotRequired[str]
    before_last_changed: NotRequired[str]
    unique_email_id: NotRequired[str]
    vip_only: NotRequired[bool]
    interest_category_id: NotRequired[str]
    interest_ids: NotRequired[str]
    interest_match: NotRequired[str]
    sort_field: NotRequired[str]
    sort_dir: NotRequired[str]

class ListMembersGetParams(TypedDict):
    """Parameters for list_members.get operation"""
    list_id: str
    subscriber_hash: str

class ReportsListParams(TypedDict):
    """Parameters for reports.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    type: NotRequired[str]
    before_send_time: NotRequired[str]
    since_send_time: NotRequired[str]

class ReportsGetParams(TypedDict):
    """Parameters for reports.get operation"""
    campaign_id: str

class EmailActivityListParams(TypedDict):
    """Parameters for email_activity.list operation"""
    campaign_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
    since: NotRequired[str]

class AutomationsListParams(TypedDict):
    """Parameters for automations.list operation"""
    count: NotRequired[int]
    offset: NotRequired[int]
    before_create_time: NotRequired[str]
    since_create_time: NotRequired[str]
    before_start_time: NotRequired[str]
    since_start_time: NotRequired[str]
    status: NotRequired[str]

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    list_id: str
    name: NotRequired[str]

class InterestCategoriesListParams(TypedDict):
    """Parameters for interest_categories.list operation"""
    list_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

class InterestCategoriesGetParams(TypedDict):
    """Parameters for interest_categories.get operation"""
    list_id: str
    interest_category_id: str

class InterestsListParams(TypedDict):
    """Parameters for interests.list operation"""
    list_id: str
    interest_category_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

class InterestsGetParams(TypedDict):
    """Parameters for interests.get operation"""
    list_id: str
    interest_category_id: str
    interest_id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    list_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
    type: NotRequired[str]
    since_created_at: NotRequired[str]
    before_created_at: NotRequired[str]
    since_updated_at: NotRequired[str]
    before_updated_at: NotRequired[str]

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    list_id: str
    segment_id: str

class SegmentMembersListParams(TypedDict):
    """Parameters for segment_members.list operation"""
    list_id: str
    segment_id: str
    count: NotRequired[int]
    offset: NotRequired[int]

class UnsubscribesListParams(TypedDict):
    """Parameters for unsubscribes.list operation"""
    campaign_id: str
    count: NotRequired[int]
    offset: NotRequired[int]
