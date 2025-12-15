"""
Type definitions for zendesk-support connector.
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

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    page: NotRequired[int]
    external_id: NotRequired[str]
    sort: NotRequired[str]

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticket_id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    page: NotRequired[int]
    role: NotRequired[str]
    external_id: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_id: str

class OrganizationsListParams(TypedDict):
    """Parameters for organizations.list operation"""
    page: NotRequired[int]

class OrganizationsGetParams(TypedDict):
    """Parameters for organizations.get operation"""
    organization_id: str

class GroupsListParams(TypedDict):
    """Parameters for groups.list operation"""
    page: NotRequired[int]
    exclude_deleted: NotRequired[bool]

class GroupsGetParams(TypedDict):
    """Parameters for groups.get operation"""
    group_id: str

class TicketCommentsListParams(TypedDict):
    """Parameters for ticket_comments.list operation"""
    ticket_id: str
    page: NotRequired[int]
    include_inline_images: NotRequired[bool]
    sort: NotRequired[str]

class AttachmentsGetParams(TypedDict):
    """Parameters for attachments.get operation"""
    attachment_id: str

class AttachmentsDownloadParams(TypedDict):
    """Parameters for attachments.download operation"""
    attachment_id: str
    range_header: NotRequired[str]

class TicketAuditsListParams(TypedDict):
    """Parameters for ticket_audits.list operation"""
    page: NotRequired[int]

class TicketAuditsListParams(TypedDict):
    """Parameters for ticket_audits.list operation"""
    ticket_id: str
    page: NotRequired[int]

class TicketMetricsListParams(TypedDict):
    """Parameters for ticket_metrics.list operation"""
    page: NotRequired[int]

class TicketFieldsListParams(TypedDict):
    """Parameters for ticket_fields.list operation"""
    page: NotRequired[int]
    locale: NotRequired[str]

class TicketFieldsGetParams(TypedDict):
    """Parameters for ticket_fields.get operation"""
    ticket_field_id: str

class BrandsListParams(TypedDict):
    """Parameters for brands.list operation"""
    page: NotRequired[int]

class BrandsGetParams(TypedDict):
    """Parameters for brands.get operation"""
    brand_id: str

class ViewsListParams(TypedDict):
    """Parameters for views.list operation"""
    page: NotRequired[int]
    access: NotRequired[str]
    active: NotRequired[bool]
    group_id: NotRequired[int]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ViewsGetParams(TypedDict):
    """Parameters for views.get operation"""
    view_id: str

class MacrosListParams(TypedDict):
    """Parameters for macros.list operation"""
    page: NotRequired[int]
    access: NotRequired[str]
    active: NotRequired[bool]
    category: NotRequired[int]
    group_id: NotRequired[int]
    only_viewable: NotRequired[bool]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class MacrosGetParams(TypedDict):
    """Parameters for macros.get operation"""
    macro_id: str

class TriggersListParams(TypedDict):
    """Parameters for triggers.list operation"""
    page: NotRequired[int]
    active: NotRequired[bool]
    category_id: NotRequired[str]
    sort: NotRequired[str]

class TriggersGetParams(TypedDict):
    """Parameters for triggers.get operation"""
    trigger_id: str

class AutomationsListParams(TypedDict):
    """Parameters for automations.list operation"""
    page: NotRequired[int]
    active: NotRequired[bool]
    sort: NotRequired[str]

class AutomationsGetParams(TypedDict):
    """Parameters for automations.get operation"""
    automation_id: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    page: NotRequired[int]

class SatisfactionRatingsListParams(TypedDict):
    """Parameters for satisfaction_ratings.list operation"""
    page: NotRequired[int]
    score: NotRequired[str]
    start_time: NotRequired[int]
    end_time: NotRequired[int]

class SatisfactionRatingsGetParams(TypedDict):
    """Parameters for satisfaction_ratings.get operation"""
    satisfaction_rating_id: str

class GroupMembershipsListParams(TypedDict):
    """Parameters for group_memberships.list operation"""
    page: NotRequired[int]

class OrganizationMembershipsListParams(TypedDict):
    """Parameters for organization_memberships.list operation"""
    page: NotRequired[int]

class SlaPoliciesListParams(TypedDict):
    """Parameters for sla_policies.list operation"""
    page: NotRequired[int]

class SlaPoliciesGetParams(TypedDict):
    """Parameters for sla_policies.get operation"""
    sla_policy_id: str

class TicketFormsListParams(TypedDict):
    """Parameters for ticket_forms.list operation"""
    page: NotRequired[int]
    active: NotRequired[bool]
    end_user_visible: NotRequired[bool]

class TicketFormsGetParams(TypedDict):
    """Parameters for ticket_forms.get operation"""
    ticket_form_id: str

class ArticlesListParams(TypedDict):
    """Parameters for articles.list operation"""
    page: NotRequired[int]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ArticlesGetParams(TypedDict):
    """Parameters for articles.get operation"""
    id: str

class ArticleAttachmentsListParams(TypedDict):
    """Parameters for article_attachments.list operation"""
    article_id: str
    page: NotRequired[int]

class ArticleAttachmentsGetParams(TypedDict):
    """Parameters for article_attachments.get operation"""
    article_id: str
    attachment_id: str

class ArticleAttachmentsDownloadParams(TypedDict):
    """Parameters for article_attachments.download operation"""
    article_id: str
    attachment_id: str
    range_header: NotRequired[str]
