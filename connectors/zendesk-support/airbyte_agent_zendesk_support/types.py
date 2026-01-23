"""
Type definitions for zendesk-support connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


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

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== BRANDS SEARCH TYPES =====

class BrandsSearchFilter(TypedDict, total=False):
    """Available fields for filtering brands search queries."""
    active: bool | None
    """Indicates whether the brand is set as active"""
    brand_url: str | None
    """The public URL of the brand"""
    created_at: str | None
    """Timestamp when the brand was created"""
    default: bool | None
    """Indicates whether the brand is the default brand for tickets generated from non-branded channels"""
    has_help_center: bool | None
    """Indicates whether the brand has a Help Center enabled"""
    help_center_state: str | None
    """The state of the Help Center, with allowed values of enabled, disabled, or restricted"""
    host_mapping: str | None
    """The host mapping configuration for the brand, visible only to administrators"""
    id: int | None
    """Unique identifier automatically assigned when the brand is created"""
    is_deleted: bool | None
    """Indicates whether the brand has been deleted"""
    logo: str | None
    """Brand logo image file represented as an Attachment object"""
    name: str | None
    """The name of the brand"""
    signature_template: str | None
    """The signature template used for the brand"""
    subdomain: str | None
    """The subdomain associated with the brand"""
    ticket_form_ids: list[Any] | None
    """Array of ticket form IDs that are available for use by this brand"""
    updated_at: str | None
    """Timestamp when the brand was last updated"""
    url: str | None
    """The API URL for accessing this brand resource"""


class BrandsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Indicates whether the brand is set as active"""
    brand_url: list[str]
    """The public URL of the brand"""
    created_at: list[str]
    """Timestamp when the brand was created"""
    default: list[bool]
    """Indicates whether the brand is the default brand for tickets generated from non-branded channels"""
    has_help_center: list[bool]
    """Indicates whether the brand has a Help Center enabled"""
    help_center_state: list[str]
    """The state of the Help Center, with allowed values of enabled, disabled, or restricted"""
    host_mapping: list[str]
    """The host mapping configuration for the brand, visible only to administrators"""
    id: list[int]
    """Unique identifier automatically assigned when the brand is created"""
    is_deleted: list[bool]
    """Indicates whether the brand has been deleted"""
    logo: list[str]
    """Brand logo image file represented as an Attachment object"""
    name: list[str]
    """The name of the brand"""
    signature_template: list[str]
    """The signature template used for the brand"""
    subdomain: list[str]
    """The subdomain associated with the brand"""
    ticket_form_ids: list[list[Any]]
    """Array of ticket form IDs that are available for use by this brand"""
    updated_at: list[str]
    """Timestamp when the brand was last updated"""
    url: list[str]
    """The API URL for accessing this brand resource"""


class BrandsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Indicates whether the brand is set as active"""
    brand_url: Any
    """The public URL of the brand"""
    created_at: Any
    """Timestamp when the brand was created"""
    default: Any
    """Indicates whether the brand is the default brand for tickets generated from non-branded channels"""
    has_help_center: Any
    """Indicates whether the brand has a Help Center enabled"""
    help_center_state: Any
    """The state of the Help Center, with allowed values of enabled, disabled, or restricted"""
    host_mapping: Any
    """The host mapping configuration for the brand, visible only to administrators"""
    id: Any
    """Unique identifier automatically assigned when the brand is created"""
    is_deleted: Any
    """Indicates whether the brand has been deleted"""
    logo: Any
    """Brand logo image file represented as an Attachment object"""
    name: Any
    """The name of the brand"""
    signature_template: Any
    """The signature template used for the brand"""
    subdomain: Any
    """The subdomain associated with the brand"""
    ticket_form_ids: Any
    """Array of ticket form IDs that are available for use by this brand"""
    updated_at: Any
    """Timestamp when the brand was last updated"""
    url: Any
    """The API URL for accessing this brand resource"""


class BrandsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Indicates whether the brand is set as active"""
    brand_url: str
    """The public URL of the brand"""
    created_at: str
    """Timestamp when the brand was created"""
    default: str
    """Indicates whether the brand is the default brand for tickets generated from non-branded channels"""
    has_help_center: str
    """Indicates whether the brand has a Help Center enabled"""
    help_center_state: str
    """The state of the Help Center, with allowed values of enabled, disabled, or restricted"""
    host_mapping: str
    """The host mapping configuration for the brand, visible only to administrators"""
    id: str
    """Unique identifier automatically assigned when the brand is created"""
    is_deleted: str
    """Indicates whether the brand has been deleted"""
    logo: str
    """Brand logo image file represented as an Attachment object"""
    name: str
    """The name of the brand"""
    signature_template: str
    """The signature template used for the brand"""
    subdomain: str
    """The subdomain associated with the brand"""
    ticket_form_ids: str
    """Array of ticket form IDs that are available for use by this brand"""
    updated_at: str
    """Timestamp when the brand was last updated"""
    url: str
    """The API URL for accessing this brand resource"""


class BrandsSortFilter(TypedDict, total=False):
    """Available fields for sorting brands search results."""
    active: AirbyteSortOrder
    """Indicates whether the brand is set as active"""
    brand_url: AirbyteSortOrder
    """The public URL of the brand"""
    created_at: AirbyteSortOrder
    """Timestamp when the brand was created"""
    default: AirbyteSortOrder
    """Indicates whether the brand is the default brand for tickets generated from non-branded channels"""
    has_help_center: AirbyteSortOrder
    """Indicates whether the brand has a Help Center enabled"""
    help_center_state: AirbyteSortOrder
    """The state of the Help Center, with allowed values of enabled, disabled, or restricted"""
    host_mapping: AirbyteSortOrder
    """The host mapping configuration for the brand, visible only to administrators"""
    id: AirbyteSortOrder
    """Unique identifier automatically assigned when the brand is created"""
    is_deleted: AirbyteSortOrder
    """Indicates whether the brand has been deleted"""
    logo: AirbyteSortOrder
    """Brand logo image file represented as an Attachment object"""
    name: AirbyteSortOrder
    """The name of the brand"""
    signature_template: AirbyteSortOrder
    """The signature template used for the brand"""
    subdomain: AirbyteSortOrder
    """The subdomain associated with the brand"""
    ticket_form_ids: AirbyteSortOrder
    """Array of ticket form IDs that are available for use by this brand"""
    updated_at: AirbyteSortOrder
    """Timestamp when the brand was last updated"""
    url: AirbyteSortOrder
    """The API URL for accessing this brand resource"""


# Entity-specific condition types for brands
class BrandsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BrandsSearchFilter


class BrandsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BrandsSearchFilter


class BrandsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BrandsSearchFilter


class BrandsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BrandsSearchFilter


class BrandsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BrandsSearchFilter


class BrandsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BrandsSearchFilter


class BrandsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BrandsStringFilter


class BrandsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BrandsStringFilter


class BrandsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BrandsStringFilter


class BrandsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BrandsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BrandsInCondition = TypedDict("BrandsInCondition", {"in": BrandsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BrandsNotCondition = TypedDict("BrandsNotCondition", {"not": "BrandsCondition"}, total=False)
"""Negates the nested condition."""

BrandsAndCondition = TypedDict("BrandsAndCondition", {"and": "list[BrandsCondition]"}, total=False)
"""True if all nested conditions are true."""

BrandsOrCondition = TypedDict("BrandsOrCondition", {"or": "list[BrandsCondition]"}, total=False)
"""True if any nested condition is true."""

BrandsAnyCondition = TypedDict("BrandsAnyCondition", {"any": BrandsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all brands condition types
BrandsCondition = (
    BrandsEqCondition
    | BrandsNeqCondition
    | BrandsGtCondition
    | BrandsGteCondition
    | BrandsLtCondition
    | BrandsLteCondition
    | BrandsInCondition
    | BrandsLikeCondition
    | BrandsFuzzyCondition
    | BrandsKeywordCondition
    | BrandsContainsCondition
    | BrandsNotCondition
    | BrandsAndCondition
    | BrandsOrCondition
    | BrandsAnyCondition
)


class BrandsSearchQuery(TypedDict, total=False):
    """Search query for brands entity."""
    filter: BrandsCondition
    sort: list[BrandsSortFilter]


# ===== GROUPS SEARCH TYPES =====

class GroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering groups search queries."""
    created_at: str | None
    """Timestamp indicating when the group was created"""
    default: bool | None
    """Indicates if the group is the default one for the account"""
    deleted: bool | None
    """Indicates whether the group has been deleted"""
    description: str | None
    """The description of the group"""
    id: int | None
    """Unique identifier automatically assigned when creating groups"""
    is_public: bool | None
    """Indicates if the group is public (true) or private (false)"""
    name: str | None
    """The name of the group"""
    updated_at: str | None
    """Timestamp indicating when the group was last updated"""
    url: str | None
    """The API URL of the group"""


class GroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Timestamp indicating when the group was created"""
    default: list[bool]
    """Indicates if the group is the default one for the account"""
    deleted: list[bool]
    """Indicates whether the group has been deleted"""
    description: list[str]
    """The description of the group"""
    id: list[int]
    """Unique identifier automatically assigned when creating groups"""
    is_public: list[bool]
    """Indicates if the group is public (true) or private (false)"""
    name: list[str]
    """The name of the group"""
    updated_at: list[str]
    """Timestamp indicating when the group was last updated"""
    url: list[str]
    """The API URL of the group"""


class GroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Timestamp indicating when the group was created"""
    default: Any
    """Indicates if the group is the default one for the account"""
    deleted: Any
    """Indicates whether the group has been deleted"""
    description: Any
    """The description of the group"""
    id: Any
    """Unique identifier automatically assigned when creating groups"""
    is_public: Any
    """Indicates if the group is public (true) or private (false)"""
    name: Any
    """The name of the group"""
    updated_at: Any
    """Timestamp indicating when the group was last updated"""
    url: Any
    """The API URL of the group"""


class GroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """Timestamp indicating when the group was created"""
    default: str
    """Indicates if the group is the default one for the account"""
    deleted: str
    """Indicates whether the group has been deleted"""
    description: str
    """The description of the group"""
    id: str
    """Unique identifier automatically assigned when creating groups"""
    is_public: str
    """Indicates if the group is public (true) or private (false)"""
    name: str
    """The name of the group"""
    updated_at: str
    """Timestamp indicating when the group was last updated"""
    url: str
    """The API URL of the group"""


class GroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting groups search results."""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the group was created"""
    default: AirbyteSortOrder
    """Indicates if the group is the default one for the account"""
    deleted: AirbyteSortOrder
    """Indicates whether the group has been deleted"""
    description: AirbyteSortOrder
    """The description of the group"""
    id: AirbyteSortOrder
    """Unique identifier automatically assigned when creating groups"""
    is_public: AirbyteSortOrder
    """Indicates if the group is public (true) or private (false)"""
    name: AirbyteSortOrder
    """The name of the group"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the group was last updated"""
    url: AirbyteSortOrder
    """The API URL of the group"""


# Entity-specific condition types for groups
class GroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GroupsSearchFilter


class GroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GroupsSearchFilter


class GroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GroupsSearchFilter


class GroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GroupsSearchFilter


class GroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GroupsSearchFilter


class GroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GroupsSearchFilter


class GroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GroupsStringFilter


class GroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GroupsStringFilter


class GroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GroupsStringFilter


class GroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GroupsInCondition = TypedDict("GroupsInCondition", {"in": GroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GroupsNotCondition = TypedDict("GroupsNotCondition", {"not": "GroupsCondition"}, total=False)
"""Negates the nested condition."""

GroupsAndCondition = TypedDict("GroupsAndCondition", {"and": "list[GroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

GroupsOrCondition = TypedDict("GroupsOrCondition", {"or": "list[GroupsCondition]"}, total=False)
"""True if any nested condition is true."""

GroupsAnyCondition = TypedDict("GroupsAnyCondition", {"any": GroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all groups condition types
GroupsCondition = (
    GroupsEqCondition
    | GroupsNeqCondition
    | GroupsGtCondition
    | GroupsGteCondition
    | GroupsLtCondition
    | GroupsLteCondition
    | GroupsInCondition
    | GroupsLikeCondition
    | GroupsFuzzyCondition
    | GroupsKeywordCondition
    | GroupsContainsCondition
    | GroupsNotCondition
    | GroupsAndCondition
    | GroupsOrCondition
    | GroupsAnyCondition
)


class GroupsSearchQuery(TypedDict, total=False):
    """Search query for groups entity."""
    filter: GroupsCondition
    sort: list[GroupsSortFilter]


# ===== ORGANIZATIONS SEARCH TYPES =====

class OrganizationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering organizations search queries."""
    created_at: str | None
    """Timestamp when the organization was created"""
    deleted_at: str | None
    """Timestamp when the organization was deleted"""
    details: str | None
    """Details about the organization, such as the address"""
    domain_names: list[Any] | None
    """Array of domain names associated with this organization for automatic user assignment"""
    external_id: str | None
    """Unique external identifier to associate the organization to an external record (case-insensitive)"""
    group_id: int | None
    """ID of the group where new tickets from users in this organization are automatically assigned"""
    id: int | None
    """Unique identifier automatically assigned when the organization is created"""
    name: str | None
    """Unique name for the organization (mandatory field)"""
    notes: str | None
    """Notes about the organization"""
    organization_fields: dict[str, Any] | None
    """Key-value object for custom organization fields"""
    shared_comments: bool | None
    """Boolean indicating whether end users in this organization can comment on each other's tickets"""
    shared_tickets: bool | None
    """Boolean indicating whether end users in this organization can see each other's tickets"""
    tags: list[Any] | None
    """Array of tags associated with the organization"""
    updated_at: str | None
    """Timestamp of the last update to the organization"""
    url: str | None
    """The API URL of this organization"""


class OrganizationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Timestamp when the organization was created"""
    deleted_at: list[str]
    """Timestamp when the organization was deleted"""
    details: list[str]
    """Details about the organization, such as the address"""
    domain_names: list[list[Any]]
    """Array of domain names associated with this organization for automatic user assignment"""
    external_id: list[str]
    """Unique external identifier to associate the organization to an external record (case-insensitive)"""
    group_id: list[int]
    """ID of the group where new tickets from users in this organization are automatically assigned"""
    id: list[int]
    """Unique identifier automatically assigned when the organization is created"""
    name: list[str]
    """Unique name for the organization (mandatory field)"""
    notes: list[str]
    """Notes about the organization"""
    organization_fields: list[dict[str, Any]]
    """Key-value object for custom organization fields"""
    shared_comments: list[bool]
    """Boolean indicating whether end users in this organization can comment on each other's tickets"""
    shared_tickets: list[bool]
    """Boolean indicating whether end users in this organization can see each other's tickets"""
    tags: list[list[Any]]
    """Array of tags associated with the organization"""
    updated_at: list[str]
    """Timestamp of the last update to the organization"""
    url: list[str]
    """The API URL of this organization"""


class OrganizationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Timestamp when the organization was created"""
    deleted_at: Any
    """Timestamp when the organization was deleted"""
    details: Any
    """Details about the organization, such as the address"""
    domain_names: Any
    """Array of domain names associated with this organization for automatic user assignment"""
    external_id: Any
    """Unique external identifier to associate the organization to an external record (case-insensitive)"""
    group_id: Any
    """ID of the group where new tickets from users in this organization are automatically assigned"""
    id: Any
    """Unique identifier automatically assigned when the organization is created"""
    name: Any
    """Unique name for the organization (mandatory field)"""
    notes: Any
    """Notes about the organization"""
    organization_fields: Any
    """Key-value object for custom organization fields"""
    shared_comments: Any
    """Boolean indicating whether end users in this organization can comment on each other's tickets"""
    shared_tickets: Any
    """Boolean indicating whether end users in this organization can see each other's tickets"""
    tags: Any
    """Array of tags associated with the organization"""
    updated_at: Any
    """Timestamp of the last update to the organization"""
    url: Any
    """The API URL of this organization"""


class OrganizationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """Timestamp when the organization was created"""
    deleted_at: str
    """Timestamp when the organization was deleted"""
    details: str
    """Details about the organization, such as the address"""
    domain_names: str
    """Array of domain names associated with this organization for automatic user assignment"""
    external_id: str
    """Unique external identifier to associate the organization to an external record (case-insensitive)"""
    group_id: str
    """ID of the group where new tickets from users in this organization are automatically assigned"""
    id: str
    """Unique identifier automatically assigned when the organization is created"""
    name: str
    """Unique name for the organization (mandatory field)"""
    notes: str
    """Notes about the organization"""
    organization_fields: str
    """Key-value object for custom organization fields"""
    shared_comments: str
    """Boolean indicating whether end users in this organization can comment on each other's tickets"""
    shared_tickets: str
    """Boolean indicating whether end users in this organization can see each other's tickets"""
    tags: str
    """Array of tags associated with the organization"""
    updated_at: str
    """Timestamp of the last update to the organization"""
    url: str
    """The API URL of this organization"""


class OrganizationsSortFilter(TypedDict, total=False):
    """Available fields for sorting organizations search results."""
    created_at: AirbyteSortOrder
    """Timestamp when the organization was created"""
    deleted_at: AirbyteSortOrder
    """Timestamp when the organization was deleted"""
    details: AirbyteSortOrder
    """Details about the organization, such as the address"""
    domain_names: AirbyteSortOrder
    """Array of domain names associated with this organization for automatic user assignment"""
    external_id: AirbyteSortOrder
    """Unique external identifier to associate the organization to an external record (case-insensitive)"""
    group_id: AirbyteSortOrder
    """ID of the group where new tickets from users in this organization are automatically assigned"""
    id: AirbyteSortOrder
    """Unique identifier automatically assigned when the organization is created"""
    name: AirbyteSortOrder
    """Unique name for the organization (mandatory field)"""
    notes: AirbyteSortOrder
    """Notes about the organization"""
    organization_fields: AirbyteSortOrder
    """Key-value object for custom organization fields"""
    shared_comments: AirbyteSortOrder
    """Boolean indicating whether end users in this organization can comment on each other's tickets"""
    shared_tickets: AirbyteSortOrder
    """Boolean indicating whether end users in this organization can see each other's tickets"""
    tags: AirbyteSortOrder
    """Array of tags associated with the organization"""
    updated_at: AirbyteSortOrder
    """Timestamp of the last update to the organization"""
    url: AirbyteSortOrder
    """The API URL of this organization"""


# Entity-specific condition types for organizations
class OrganizationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrganizationsSearchFilter


class OrganizationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrganizationsSearchFilter


class OrganizationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrganizationsSearchFilter


class OrganizationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrganizationsSearchFilter


class OrganizationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrganizationsSearchFilter


class OrganizationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrganizationsSearchFilter


class OrganizationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrganizationsStringFilter


class OrganizationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrganizationsStringFilter


class OrganizationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrganizationsStringFilter


class OrganizationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrganizationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrganizationsInCondition = TypedDict("OrganizationsInCondition", {"in": OrganizationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrganizationsNotCondition = TypedDict("OrganizationsNotCondition", {"not": "OrganizationsCondition"}, total=False)
"""Negates the nested condition."""

OrganizationsAndCondition = TypedDict("OrganizationsAndCondition", {"and": "list[OrganizationsCondition]"}, total=False)
"""True if all nested conditions are true."""

OrganizationsOrCondition = TypedDict("OrganizationsOrCondition", {"or": "list[OrganizationsCondition]"}, total=False)
"""True if any nested condition is true."""

OrganizationsAnyCondition = TypedDict("OrganizationsAnyCondition", {"any": OrganizationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all organizations condition types
OrganizationsCondition = (
    OrganizationsEqCondition
    | OrganizationsNeqCondition
    | OrganizationsGtCondition
    | OrganizationsGteCondition
    | OrganizationsLtCondition
    | OrganizationsLteCondition
    | OrganizationsInCondition
    | OrganizationsLikeCondition
    | OrganizationsFuzzyCondition
    | OrganizationsKeywordCondition
    | OrganizationsContainsCondition
    | OrganizationsNotCondition
    | OrganizationsAndCondition
    | OrganizationsOrCondition
    | OrganizationsAnyCondition
)


class OrganizationsSearchQuery(TypedDict, total=False):
    """Search query for organizations entity."""
    filter: OrganizationsCondition
    sort: list[OrganizationsSortFilter]


# ===== SATISFACTION_RATINGS SEARCH TYPES =====

class SatisfactionRatingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering satisfaction_ratings search queries."""
    assignee_id: int | None
    """The identifier of the agent assigned to the ticket at the time the rating was submitted"""
    comment: str | None
    """Optional comment provided by the requester with the rating"""
    created_at: str | None
    """Timestamp indicating when the satisfaction rating was created"""
    group_id: int | None
    """The identifier of the group assigned to the ticket at the time the rating was submitted"""
    id: int | None
    """Unique identifier for the satisfaction rating, automatically assigned upon creation"""
    reason: str | None
    """Free-text reason for a bad rating provided by the requester in a follow-up question"""
    reason_id: int | None
    """Identifier for the predefined reason given for a negative rating"""
    requester_id: int | None
    """The identifier of the ticket requester who submitted the satisfaction rating"""
    score: str | None
    """The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'"""
    ticket_id: int | None
    """The identifier of the ticket being rated"""
    updated_at: str | None
    """Timestamp indicating when the satisfaction rating was last updated"""
    url: str | None
    """The API URL of this satisfaction rating resource"""


class SatisfactionRatingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    assignee_id: list[int]
    """The identifier of the agent assigned to the ticket at the time the rating was submitted"""
    comment: list[str]
    """Optional comment provided by the requester with the rating"""
    created_at: list[str]
    """Timestamp indicating when the satisfaction rating was created"""
    group_id: list[int]
    """The identifier of the group assigned to the ticket at the time the rating was submitted"""
    id: list[int]
    """Unique identifier for the satisfaction rating, automatically assigned upon creation"""
    reason: list[str]
    """Free-text reason for a bad rating provided by the requester in a follow-up question"""
    reason_id: list[int]
    """Identifier for the predefined reason given for a negative rating"""
    requester_id: list[int]
    """The identifier of the ticket requester who submitted the satisfaction rating"""
    score: list[str]
    """The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'"""
    ticket_id: list[int]
    """The identifier of the ticket being rated"""
    updated_at: list[str]
    """Timestamp indicating when the satisfaction rating was last updated"""
    url: list[str]
    """The API URL of this satisfaction rating resource"""


class SatisfactionRatingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    assignee_id: Any
    """The identifier of the agent assigned to the ticket at the time the rating was submitted"""
    comment: Any
    """Optional comment provided by the requester with the rating"""
    created_at: Any
    """Timestamp indicating when the satisfaction rating was created"""
    group_id: Any
    """The identifier of the group assigned to the ticket at the time the rating was submitted"""
    id: Any
    """Unique identifier for the satisfaction rating, automatically assigned upon creation"""
    reason: Any
    """Free-text reason for a bad rating provided by the requester in a follow-up question"""
    reason_id: Any
    """Identifier for the predefined reason given for a negative rating"""
    requester_id: Any
    """The identifier of the ticket requester who submitted the satisfaction rating"""
    score: Any
    """The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'"""
    ticket_id: Any
    """The identifier of the ticket being rated"""
    updated_at: Any
    """Timestamp indicating when the satisfaction rating was last updated"""
    url: Any
    """The API URL of this satisfaction rating resource"""


class SatisfactionRatingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    assignee_id: str
    """The identifier of the agent assigned to the ticket at the time the rating was submitted"""
    comment: str
    """Optional comment provided by the requester with the rating"""
    created_at: str
    """Timestamp indicating when the satisfaction rating was created"""
    group_id: str
    """The identifier of the group assigned to the ticket at the time the rating was submitted"""
    id: str
    """Unique identifier for the satisfaction rating, automatically assigned upon creation"""
    reason: str
    """Free-text reason for a bad rating provided by the requester in a follow-up question"""
    reason_id: str
    """Identifier for the predefined reason given for a negative rating"""
    requester_id: str
    """The identifier of the ticket requester who submitted the satisfaction rating"""
    score: str
    """The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'"""
    ticket_id: str
    """The identifier of the ticket being rated"""
    updated_at: str
    """Timestamp indicating when the satisfaction rating was last updated"""
    url: str
    """The API URL of this satisfaction rating resource"""


class SatisfactionRatingsSortFilter(TypedDict, total=False):
    """Available fields for sorting satisfaction_ratings search results."""
    assignee_id: AirbyteSortOrder
    """The identifier of the agent assigned to the ticket at the time the rating was submitted"""
    comment: AirbyteSortOrder
    """Optional comment provided by the requester with the rating"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the satisfaction rating was created"""
    group_id: AirbyteSortOrder
    """The identifier of the group assigned to the ticket at the time the rating was submitted"""
    id: AirbyteSortOrder
    """Unique identifier for the satisfaction rating, automatically assigned upon creation"""
    reason: AirbyteSortOrder
    """Free-text reason for a bad rating provided by the requester in a follow-up question"""
    reason_id: AirbyteSortOrder
    """Identifier for the predefined reason given for a negative rating"""
    requester_id: AirbyteSortOrder
    """The identifier of the ticket requester who submitted the satisfaction rating"""
    score: AirbyteSortOrder
    """The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'"""
    ticket_id: AirbyteSortOrder
    """The identifier of the ticket being rated"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the satisfaction rating was last updated"""
    url: AirbyteSortOrder
    """The API URL of this satisfaction rating resource"""


# Entity-specific condition types for satisfaction_ratings
class SatisfactionRatingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SatisfactionRatingsSearchFilter


class SatisfactionRatingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SatisfactionRatingsSearchFilter


class SatisfactionRatingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SatisfactionRatingsSearchFilter


class SatisfactionRatingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SatisfactionRatingsSearchFilter


class SatisfactionRatingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SatisfactionRatingsSearchFilter


class SatisfactionRatingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SatisfactionRatingsSearchFilter


class SatisfactionRatingsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SatisfactionRatingsStringFilter


class SatisfactionRatingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SatisfactionRatingsStringFilter


class SatisfactionRatingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SatisfactionRatingsStringFilter


class SatisfactionRatingsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SatisfactionRatingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SatisfactionRatingsInCondition = TypedDict("SatisfactionRatingsInCondition", {"in": SatisfactionRatingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SatisfactionRatingsNotCondition = TypedDict("SatisfactionRatingsNotCondition", {"not": "SatisfactionRatingsCondition"}, total=False)
"""Negates the nested condition."""

SatisfactionRatingsAndCondition = TypedDict("SatisfactionRatingsAndCondition", {"and": "list[SatisfactionRatingsCondition]"}, total=False)
"""True if all nested conditions are true."""

SatisfactionRatingsOrCondition = TypedDict("SatisfactionRatingsOrCondition", {"or": "list[SatisfactionRatingsCondition]"}, total=False)
"""True if any nested condition is true."""

SatisfactionRatingsAnyCondition = TypedDict("SatisfactionRatingsAnyCondition", {"any": SatisfactionRatingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all satisfaction_ratings condition types
SatisfactionRatingsCondition = (
    SatisfactionRatingsEqCondition
    | SatisfactionRatingsNeqCondition
    | SatisfactionRatingsGtCondition
    | SatisfactionRatingsGteCondition
    | SatisfactionRatingsLtCondition
    | SatisfactionRatingsLteCondition
    | SatisfactionRatingsInCondition
    | SatisfactionRatingsLikeCondition
    | SatisfactionRatingsFuzzyCondition
    | SatisfactionRatingsKeywordCondition
    | SatisfactionRatingsContainsCondition
    | SatisfactionRatingsNotCondition
    | SatisfactionRatingsAndCondition
    | SatisfactionRatingsOrCondition
    | SatisfactionRatingsAnyCondition
)


class SatisfactionRatingsSearchQuery(TypedDict, total=False):
    """Search query for satisfaction_ratings entity."""
    filter: SatisfactionRatingsCondition
    sort: list[SatisfactionRatingsSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    count: int | None
    """The number of times this tag has been used across resources"""
    name: str | None
    """The tag name string used to label and categorize resources"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    count: list[int]
    """The number of times this tag has been used across resources"""
    name: list[str]
    """The tag name string used to label and categorize resources"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    count: Any
    """The number of times this tag has been used across resources"""
    name: Any
    """The tag name string used to label and categorize resources"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    count: str
    """The number of times this tag has been used across resources"""
    name: str
    """The tag name string used to label and categorize resources"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    count: AirbyteSortOrder
    """The number of times this tag has been used across resources"""
    name: AirbyteSortOrder
    """The tag name string used to label and categorize resources"""


# Entity-specific condition types for tags
class TagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TagsSearchFilter


class TagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TagsSearchFilter


class TagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TagsSearchFilter


class TagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TagsSearchFilter


class TagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TagsSearchFilter


class TagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TagsSearchFilter


class TagsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TagsStringFilter


class TagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TagsStringFilter


class TagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TagsStringFilter


class TagsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TagsInCondition = TypedDict("TagsInCondition", {"in": TagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TagsNotCondition = TypedDict("TagsNotCondition", {"not": "TagsCondition"}, total=False)
"""Negates the nested condition."""

TagsAndCondition = TypedDict("TagsAndCondition", {"and": "list[TagsCondition]"}, total=False)
"""True if all nested conditions are true."""

TagsOrCondition = TypedDict("TagsOrCondition", {"or": "list[TagsCondition]"}, total=False)
"""True if any nested condition is true."""

TagsAnyCondition = TypedDict("TagsAnyCondition", {"any": TagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tags condition types
TagsCondition = (
    TagsEqCondition
    | TagsNeqCondition
    | TagsGtCondition
    | TagsGteCondition
    | TagsLtCondition
    | TagsLteCondition
    | TagsInCondition
    | TagsLikeCondition
    | TagsFuzzyCondition
    | TagsKeywordCondition
    | TagsContainsCondition
    | TagsNotCondition
    | TagsAndCondition
    | TagsOrCondition
    | TagsAnyCondition
)


class TagsSearchQuery(TypedDict, total=False):
    """Search query for tags entity."""
    filter: TagsCondition
    sort: list[TagsSortFilter]


# ===== TICKET_AUDITS SEARCH TYPES =====

class TicketAuditsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_audits search queries."""
    attachments: list[Any] | None
    """Files or documents attached to the audit"""
    author_id: int | None
    """The unique identifier of the user who created the audit"""
    created_at: str | None
    """Timestamp indicating when the audit was created"""
    events: list[Any] | None
    """Array of events that occurred in this audit, such as field changes, comments, or tag updates"""
    id: int | None
    """Unique identifier for the audit record, automatically assigned when the audit is created"""
    metadata: dict[str, Any] | None
    """Custom and system data associated with the audit"""
    ticket_id: int | None
    """The unique identifier of the ticket associated with this audit"""
    via: dict[str, Any] | None
    """Describes how the audit was created, providing context about the creation source"""


class TicketAuditsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attachments: list[list[Any]]
    """Files or documents attached to the audit"""
    author_id: list[int]
    """The unique identifier of the user who created the audit"""
    created_at: list[str]
    """Timestamp indicating when the audit was created"""
    events: list[list[Any]]
    """Array of events that occurred in this audit, such as field changes, comments, or tag updates"""
    id: list[int]
    """Unique identifier for the audit record, automatically assigned when the audit is created"""
    metadata: list[dict[str, Any]]
    """Custom and system data associated with the audit"""
    ticket_id: list[int]
    """The unique identifier of the ticket associated with this audit"""
    via: list[dict[str, Any]]
    """Describes how the audit was created, providing context about the creation source"""


class TicketAuditsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attachments: Any
    """Files or documents attached to the audit"""
    author_id: Any
    """The unique identifier of the user who created the audit"""
    created_at: Any
    """Timestamp indicating when the audit was created"""
    events: Any
    """Array of events that occurred in this audit, such as field changes, comments, or tag updates"""
    id: Any
    """Unique identifier for the audit record, automatically assigned when the audit is created"""
    metadata: Any
    """Custom and system data associated with the audit"""
    ticket_id: Any
    """The unique identifier of the ticket associated with this audit"""
    via: Any
    """Describes how the audit was created, providing context about the creation source"""


class TicketAuditsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attachments: str
    """Files or documents attached to the audit"""
    author_id: str
    """The unique identifier of the user who created the audit"""
    created_at: str
    """Timestamp indicating when the audit was created"""
    events: str
    """Array of events that occurred in this audit, such as field changes, comments, or tag updates"""
    id: str
    """Unique identifier for the audit record, automatically assigned when the audit is created"""
    metadata: str
    """Custom and system data associated with the audit"""
    ticket_id: str
    """The unique identifier of the ticket associated with this audit"""
    via: str
    """Describes how the audit was created, providing context about the creation source"""


class TicketAuditsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_audits search results."""
    attachments: AirbyteSortOrder
    """Files or documents attached to the audit"""
    author_id: AirbyteSortOrder
    """The unique identifier of the user who created the audit"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the audit was created"""
    events: AirbyteSortOrder
    """Array of events that occurred in this audit, such as field changes, comments, or tag updates"""
    id: AirbyteSortOrder
    """Unique identifier for the audit record, automatically assigned when the audit is created"""
    metadata: AirbyteSortOrder
    """Custom and system data associated with the audit"""
    ticket_id: AirbyteSortOrder
    """The unique identifier of the ticket associated with this audit"""
    via: AirbyteSortOrder
    """Describes how the audit was created, providing context about the creation source"""


# Entity-specific condition types for ticket_audits
class TicketAuditsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketAuditsSearchFilter


class TicketAuditsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketAuditsSearchFilter


class TicketAuditsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketAuditsSearchFilter


class TicketAuditsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketAuditsSearchFilter


class TicketAuditsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketAuditsSearchFilter


class TicketAuditsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketAuditsSearchFilter


class TicketAuditsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketAuditsStringFilter


class TicketAuditsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketAuditsStringFilter


class TicketAuditsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketAuditsStringFilter


class TicketAuditsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketAuditsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketAuditsInCondition = TypedDict("TicketAuditsInCondition", {"in": TicketAuditsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketAuditsNotCondition = TypedDict("TicketAuditsNotCondition", {"not": "TicketAuditsCondition"}, total=False)
"""Negates the nested condition."""

TicketAuditsAndCondition = TypedDict("TicketAuditsAndCondition", {"and": "list[TicketAuditsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketAuditsOrCondition = TypedDict("TicketAuditsOrCondition", {"or": "list[TicketAuditsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketAuditsAnyCondition = TypedDict("TicketAuditsAnyCondition", {"any": TicketAuditsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_audits condition types
TicketAuditsCondition = (
    TicketAuditsEqCondition
    | TicketAuditsNeqCondition
    | TicketAuditsGtCondition
    | TicketAuditsGteCondition
    | TicketAuditsLtCondition
    | TicketAuditsLteCondition
    | TicketAuditsInCondition
    | TicketAuditsLikeCondition
    | TicketAuditsFuzzyCondition
    | TicketAuditsKeywordCondition
    | TicketAuditsContainsCondition
    | TicketAuditsNotCondition
    | TicketAuditsAndCondition
    | TicketAuditsOrCondition
    | TicketAuditsAnyCondition
)


class TicketAuditsSearchQuery(TypedDict, total=False):
    """Search query for ticket_audits entity."""
    filter: TicketAuditsCondition
    sort: list[TicketAuditsSortFilter]


# ===== TICKET_COMMENTS SEARCH TYPES =====

class TicketCommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_comments search queries."""
    attachments: list[Any] | None
    """List of files or media attached to the comment"""
    audit_id: int | None
    """Identifier of the audit record associated with this comment event"""
    author_id: int | None
    """Identifier of the user who created the comment"""
    body: str | None
    """Content of the comment in its original format"""
    created_at: str | None
    """Timestamp when the comment was created"""
    event_type: str | None
    """Specific classification of the event within the ticket event stream"""
    html_body: str | None
    """HTML-formatted content of the comment"""
    id: int | None
    """Unique identifier for the comment event"""
    metadata: dict[str, Any] | None
    """Additional structured information about the comment not covered by standard fields"""
    plain_body: str | None
    """Plain text content of the comment without formatting"""
    public: bool | None
    """Boolean indicating whether the comment is visible to end users or is an internal note"""
    ticket_id: int | None
    """Identifier of the ticket to which this comment belongs"""
    timestamp: int | None
    """Timestamp of when the event occurred in the incremental export stream"""
    type: str | None
    """Type of event, typically indicating this is a comment event"""
    uploads: list[Any] | None
    """Array of upload tokens or identifiers for files being attached to the comment"""
    via: dict[str, Any] | None
    """Channel or method through which the comment was submitted"""
    via_reference_id: int | None
    """Reference identifier for the channel through which the comment was created"""


class TicketCommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attachments: list[list[Any]]
    """List of files or media attached to the comment"""
    audit_id: list[int]
    """Identifier of the audit record associated with this comment event"""
    author_id: list[int]
    """Identifier of the user who created the comment"""
    body: list[str]
    """Content of the comment in its original format"""
    created_at: list[str]
    """Timestamp when the comment was created"""
    event_type: list[str]
    """Specific classification of the event within the ticket event stream"""
    html_body: list[str]
    """HTML-formatted content of the comment"""
    id: list[int]
    """Unique identifier for the comment event"""
    metadata: list[dict[str, Any]]
    """Additional structured information about the comment not covered by standard fields"""
    plain_body: list[str]
    """Plain text content of the comment without formatting"""
    public: list[bool]
    """Boolean indicating whether the comment is visible to end users or is an internal note"""
    ticket_id: list[int]
    """Identifier of the ticket to which this comment belongs"""
    timestamp: list[int]
    """Timestamp of when the event occurred in the incremental export stream"""
    type: list[str]
    """Type of event, typically indicating this is a comment event"""
    uploads: list[list[Any]]
    """Array of upload tokens or identifiers for files being attached to the comment"""
    via: list[dict[str, Any]]
    """Channel or method through which the comment was submitted"""
    via_reference_id: list[int]
    """Reference identifier for the channel through which the comment was created"""


class TicketCommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attachments: Any
    """List of files or media attached to the comment"""
    audit_id: Any
    """Identifier of the audit record associated with this comment event"""
    author_id: Any
    """Identifier of the user who created the comment"""
    body: Any
    """Content of the comment in its original format"""
    created_at: Any
    """Timestamp when the comment was created"""
    event_type: Any
    """Specific classification of the event within the ticket event stream"""
    html_body: Any
    """HTML-formatted content of the comment"""
    id: Any
    """Unique identifier for the comment event"""
    metadata: Any
    """Additional structured information about the comment not covered by standard fields"""
    plain_body: Any
    """Plain text content of the comment without formatting"""
    public: Any
    """Boolean indicating whether the comment is visible to end users or is an internal note"""
    ticket_id: Any
    """Identifier of the ticket to which this comment belongs"""
    timestamp: Any
    """Timestamp of when the event occurred in the incremental export stream"""
    type: Any
    """Type of event, typically indicating this is a comment event"""
    uploads: Any
    """Array of upload tokens or identifiers for files being attached to the comment"""
    via: Any
    """Channel or method through which the comment was submitted"""
    via_reference_id: Any
    """Reference identifier for the channel through which the comment was created"""


class TicketCommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attachments: str
    """List of files or media attached to the comment"""
    audit_id: str
    """Identifier of the audit record associated with this comment event"""
    author_id: str
    """Identifier of the user who created the comment"""
    body: str
    """Content of the comment in its original format"""
    created_at: str
    """Timestamp when the comment was created"""
    event_type: str
    """Specific classification of the event within the ticket event stream"""
    html_body: str
    """HTML-formatted content of the comment"""
    id: str
    """Unique identifier for the comment event"""
    metadata: str
    """Additional structured information about the comment not covered by standard fields"""
    plain_body: str
    """Plain text content of the comment without formatting"""
    public: str
    """Boolean indicating whether the comment is visible to end users or is an internal note"""
    ticket_id: str
    """Identifier of the ticket to which this comment belongs"""
    timestamp: str
    """Timestamp of when the event occurred in the incremental export stream"""
    type: str
    """Type of event, typically indicating this is a comment event"""
    uploads: str
    """Array of upload tokens or identifiers for files being attached to the comment"""
    via: str
    """Channel or method through which the comment was submitted"""
    via_reference_id: str
    """Reference identifier for the channel through which the comment was created"""


class TicketCommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_comments search results."""
    attachments: AirbyteSortOrder
    """List of files or media attached to the comment"""
    audit_id: AirbyteSortOrder
    """Identifier of the audit record associated with this comment event"""
    author_id: AirbyteSortOrder
    """Identifier of the user who created the comment"""
    body: AirbyteSortOrder
    """Content of the comment in its original format"""
    created_at: AirbyteSortOrder
    """Timestamp when the comment was created"""
    event_type: AirbyteSortOrder
    """Specific classification of the event within the ticket event stream"""
    html_body: AirbyteSortOrder
    """HTML-formatted content of the comment"""
    id: AirbyteSortOrder
    """Unique identifier for the comment event"""
    metadata: AirbyteSortOrder
    """Additional structured information about the comment not covered by standard fields"""
    plain_body: AirbyteSortOrder
    """Plain text content of the comment without formatting"""
    public: AirbyteSortOrder
    """Boolean indicating whether the comment is visible to end users or is an internal note"""
    ticket_id: AirbyteSortOrder
    """Identifier of the ticket to which this comment belongs"""
    timestamp: AirbyteSortOrder
    """Timestamp of when the event occurred in the incremental export stream"""
    type: AirbyteSortOrder
    """Type of event, typically indicating this is a comment event"""
    uploads: AirbyteSortOrder
    """Array of upload tokens or identifiers for files being attached to the comment"""
    via: AirbyteSortOrder
    """Channel or method through which the comment was submitted"""
    via_reference_id: AirbyteSortOrder
    """Reference identifier for the channel through which the comment was created"""


# Entity-specific condition types for ticket_comments
class TicketCommentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketCommentsSearchFilter


class TicketCommentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketCommentsSearchFilter


class TicketCommentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketCommentsSearchFilter


class TicketCommentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketCommentsSearchFilter


class TicketCommentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketCommentsSearchFilter


class TicketCommentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketCommentsSearchFilter


class TicketCommentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketCommentsStringFilter


class TicketCommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketCommentsStringFilter


class TicketCommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketCommentsStringFilter


class TicketCommentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketCommentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketCommentsInCondition = TypedDict("TicketCommentsInCondition", {"in": TicketCommentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketCommentsNotCondition = TypedDict("TicketCommentsNotCondition", {"not": "TicketCommentsCondition"}, total=False)
"""Negates the nested condition."""

TicketCommentsAndCondition = TypedDict("TicketCommentsAndCondition", {"and": "list[TicketCommentsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketCommentsOrCondition = TypedDict("TicketCommentsOrCondition", {"or": "list[TicketCommentsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketCommentsAnyCondition = TypedDict("TicketCommentsAnyCondition", {"any": TicketCommentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_comments condition types
TicketCommentsCondition = (
    TicketCommentsEqCondition
    | TicketCommentsNeqCondition
    | TicketCommentsGtCondition
    | TicketCommentsGteCondition
    | TicketCommentsLtCondition
    | TicketCommentsLteCondition
    | TicketCommentsInCondition
    | TicketCommentsLikeCondition
    | TicketCommentsFuzzyCondition
    | TicketCommentsKeywordCondition
    | TicketCommentsContainsCondition
    | TicketCommentsNotCondition
    | TicketCommentsAndCondition
    | TicketCommentsOrCondition
    | TicketCommentsAnyCondition
)


class TicketCommentsSearchQuery(TypedDict, total=False):
    """Search query for ticket_comments entity."""
    filter: TicketCommentsCondition
    sort: list[TicketCommentsSortFilter]


# ===== TICKET_FIELDS SEARCH TYPES =====

class TicketFieldsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_fields search queries."""
    active: bool | None
    """Whether this field is currently available for use"""
    agent_description: str | None
    """A description of the ticket field that only agents can see"""
    collapsed_for_agents: bool | None
    """If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields"""
    created_at: str | None
    """Timestamp when the custom ticket field was created"""
    custom_field_options: list[Any] | None
    """Array of option objects for custom ticket fields of type multiselect or tagger"""
    custom_statuses: list[Any] | None
    """List of customized ticket statuses, only present for system ticket fields of type custom_status"""
    description: str | None
    """Text describing the purpose of the ticket field to users"""
    editable_in_portal: bool | None
    """Whether this field is editable by end users in Help Center"""
    id: int | None
    """Unique identifier for the ticket field, automatically assigned when created"""
    key: str | None
    """Internal identifier or reference key for the field"""
    position: int | None
    """The relative position of the ticket field on a ticket, controlling display order"""
    raw_description: str | None
    """The dynamic content placeholder if present, or the description value if not"""
    raw_title: str | None
    """The dynamic content placeholder if present, or the title value if not"""
    raw_title_in_portal: str | None
    """The dynamic content placeholder if present, or the title_in_portal value if not"""
    regexp_for_validation: str | None
    """For regexp fields only, the validation pattern for a field value to be deemed valid"""
    removable: bool | None
    """If false, this field is a system field that must be present on all tickets"""
    required: bool | None
    """If true, agents must enter a value in the field to change the ticket status to solved"""
    required_in_portal: bool | None
    """If true, end users must enter a value in the field to create a request"""
    sub_type_id: int | None
    """For system ticket fields of type priority and status, controlling available options"""
    system_field_options: list[Any] | None
    """Array of options for system ticket fields of type tickettype, priority, or status"""
    tag: str | None
    """For checkbox fields only, a tag added to tickets when the checkbox field is selected"""
    title: str | None
    """The title of the ticket field displayed to agents"""
    title_in_portal: str | None
    """The title of the ticket field displayed to end users in Help Center"""
    type: str | None
    """Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger"""
    updated_at: str | None
    """Timestamp when the custom ticket field was last updated"""
    url: str | None
    """The API URL for this ticket field resource"""
    visible_in_portal: bool | None
    """Whether this field is visible to end users in Help Center"""


class TicketFieldsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Whether this field is currently available for use"""
    agent_description: list[str]
    """A description of the ticket field that only agents can see"""
    collapsed_for_agents: list[bool]
    """If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields"""
    created_at: list[str]
    """Timestamp when the custom ticket field was created"""
    custom_field_options: list[list[Any]]
    """Array of option objects for custom ticket fields of type multiselect or tagger"""
    custom_statuses: list[list[Any]]
    """List of customized ticket statuses, only present for system ticket fields of type custom_status"""
    description: list[str]
    """Text describing the purpose of the ticket field to users"""
    editable_in_portal: list[bool]
    """Whether this field is editable by end users in Help Center"""
    id: list[int]
    """Unique identifier for the ticket field, automatically assigned when created"""
    key: list[str]
    """Internal identifier or reference key for the field"""
    position: list[int]
    """The relative position of the ticket field on a ticket, controlling display order"""
    raw_description: list[str]
    """The dynamic content placeholder if present, or the description value if not"""
    raw_title: list[str]
    """The dynamic content placeholder if present, or the title value if not"""
    raw_title_in_portal: list[str]
    """The dynamic content placeholder if present, or the title_in_portal value if not"""
    regexp_for_validation: list[str]
    """For regexp fields only, the validation pattern for a field value to be deemed valid"""
    removable: list[bool]
    """If false, this field is a system field that must be present on all tickets"""
    required: list[bool]
    """If true, agents must enter a value in the field to change the ticket status to solved"""
    required_in_portal: list[bool]
    """If true, end users must enter a value in the field to create a request"""
    sub_type_id: list[int]
    """For system ticket fields of type priority and status, controlling available options"""
    system_field_options: list[list[Any]]
    """Array of options for system ticket fields of type tickettype, priority, or status"""
    tag: list[str]
    """For checkbox fields only, a tag added to tickets when the checkbox field is selected"""
    title: list[str]
    """The title of the ticket field displayed to agents"""
    title_in_portal: list[str]
    """The title of the ticket field displayed to end users in Help Center"""
    type: list[str]
    """Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger"""
    updated_at: list[str]
    """Timestamp when the custom ticket field was last updated"""
    url: list[str]
    """The API URL for this ticket field resource"""
    visible_in_portal: list[bool]
    """Whether this field is visible to end users in Help Center"""


class TicketFieldsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Whether this field is currently available for use"""
    agent_description: Any
    """A description of the ticket field that only agents can see"""
    collapsed_for_agents: Any
    """If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields"""
    created_at: Any
    """Timestamp when the custom ticket field was created"""
    custom_field_options: Any
    """Array of option objects for custom ticket fields of type multiselect or tagger"""
    custom_statuses: Any
    """List of customized ticket statuses, only present for system ticket fields of type custom_status"""
    description: Any
    """Text describing the purpose of the ticket field to users"""
    editable_in_portal: Any
    """Whether this field is editable by end users in Help Center"""
    id: Any
    """Unique identifier for the ticket field, automatically assigned when created"""
    key: Any
    """Internal identifier or reference key for the field"""
    position: Any
    """The relative position of the ticket field on a ticket, controlling display order"""
    raw_description: Any
    """The dynamic content placeholder if present, or the description value if not"""
    raw_title: Any
    """The dynamic content placeholder if present, or the title value if not"""
    raw_title_in_portal: Any
    """The dynamic content placeholder if present, or the title_in_portal value if not"""
    regexp_for_validation: Any
    """For regexp fields only, the validation pattern for a field value to be deemed valid"""
    removable: Any
    """If false, this field is a system field that must be present on all tickets"""
    required: Any
    """If true, agents must enter a value in the field to change the ticket status to solved"""
    required_in_portal: Any
    """If true, end users must enter a value in the field to create a request"""
    sub_type_id: Any
    """For system ticket fields of type priority and status, controlling available options"""
    system_field_options: Any
    """Array of options for system ticket fields of type tickettype, priority, or status"""
    tag: Any
    """For checkbox fields only, a tag added to tickets when the checkbox field is selected"""
    title: Any
    """The title of the ticket field displayed to agents"""
    title_in_portal: Any
    """The title of the ticket field displayed to end users in Help Center"""
    type: Any
    """Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger"""
    updated_at: Any
    """Timestamp when the custom ticket field was last updated"""
    url: Any
    """The API URL for this ticket field resource"""
    visible_in_portal: Any
    """Whether this field is visible to end users in Help Center"""


class TicketFieldsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Whether this field is currently available for use"""
    agent_description: str
    """A description of the ticket field that only agents can see"""
    collapsed_for_agents: str
    """If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields"""
    created_at: str
    """Timestamp when the custom ticket field was created"""
    custom_field_options: str
    """Array of option objects for custom ticket fields of type multiselect or tagger"""
    custom_statuses: str
    """List of customized ticket statuses, only present for system ticket fields of type custom_status"""
    description: str
    """Text describing the purpose of the ticket field to users"""
    editable_in_portal: str
    """Whether this field is editable by end users in Help Center"""
    id: str
    """Unique identifier for the ticket field, automatically assigned when created"""
    key: str
    """Internal identifier or reference key for the field"""
    position: str
    """The relative position of the ticket field on a ticket, controlling display order"""
    raw_description: str
    """The dynamic content placeholder if present, or the description value if not"""
    raw_title: str
    """The dynamic content placeholder if present, or the title value if not"""
    raw_title_in_portal: str
    """The dynamic content placeholder if present, or the title_in_portal value if not"""
    regexp_for_validation: str
    """For regexp fields only, the validation pattern for a field value to be deemed valid"""
    removable: str
    """If false, this field is a system field that must be present on all tickets"""
    required: str
    """If true, agents must enter a value in the field to change the ticket status to solved"""
    required_in_portal: str
    """If true, end users must enter a value in the field to create a request"""
    sub_type_id: str
    """For system ticket fields of type priority and status, controlling available options"""
    system_field_options: str
    """Array of options for system ticket fields of type tickettype, priority, or status"""
    tag: str
    """For checkbox fields only, a tag added to tickets when the checkbox field is selected"""
    title: str
    """The title of the ticket field displayed to agents"""
    title_in_portal: str
    """The title of the ticket field displayed to end users in Help Center"""
    type: str
    """Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger"""
    updated_at: str
    """Timestamp when the custom ticket field was last updated"""
    url: str
    """The API URL for this ticket field resource"""
    visible_in_portal: str
    """Whether this field is visible to end users in Help Center"""


class TicketFieldsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_fields search results."""
    active: AirbyteSortOrder
    """Whether this field is currently available for use"""
    agent_description: AirbyteSortOrder
    """A description of the ticket field that only agents can see"""
    collapsed_for_agents: AirbyteSortOrder
    """If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields"""
    created_at: AirbyteSortOrder
    """Timestamp when the custom ticket field was created"""
    custom_field_options: AirbyteSortOrder
    """Array of option objects for custom ticket fields of type multiselect or tagger"""
    custom_statuses: AirbyteSortOrder
    """List of customized ticket statuses, only present for system ticket fields of type custom_status"""
    description: AirbyteSortOrder
    """Text describing the purpose of the ticket field to users"""
    editable_in_portal: AirbyteSortOrder
    """Whether this field is editable by end users in Help Center"""
    id: AirbyteSortOrder
    """Unique identifier for the ticket field, automatically assigned when created"""
    key: AirbyteSortOrder
    """Internal identifier or reference key for the field"""
    position: AirbyteSortOrder
    """The relative position of the ticket field on a ticket, controlling display order"""
    raw_description: AirbyteSortOrder
    """The dynamic content placeholder if present, or the description value if not"""
    raw_title: AirbyteSortOrder
    """The dynamic content placeholder if present, or the title value if not"""
    raw_title_in_portal: AirbyteSortOrder
    """The dynamic content placeholder if present, or the title_in_portal value if not"""
    regexp_for_validation: AirbyteSortOrder
    """For regexp fields only, the validation pattern for a field value to be deemed valid"""
    removable: AirbyteSortOrder
    """If false, this field is a system field that must be present on all tickets"""
    required: AirbyteSortOrder
    """If true, agents must enter a value in the field to change the ticket status to solved"""
    required_in_portal: AirbyteSortOrder
    """If true, end users must enter a value in the field to create a request"""
    sub_type_id: AirbyteSortOrder
    """For system ticket fields of type priority and status, controlling available options"""
    system_field_options: AirbyteSortOrder
    """Array of options for system ticket fields of type tickettype, priority, or status"""
    tag: AirbyteSortOrder
    """For checkbox fields only, a tag added to tickets when the checkbox field is selected"""
    title: AirbyteSortOrder
    """The title of the ticket field displayed to agents"""
    title_in_portal: AirbyteSortOrder
    """The title of the ticket field displayed to end users in Help Center"""
    type: AirbyteSortOrder
    """Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger"""
    updated_at: AirbyteSortOrder
    """Timestamp when the custom ticket field was last updated"""
    url: AirbyteSortOrder
    """The API URL for this ticket field resource"""
    visible_in_portal: AirbyteSortOrder
    """Whether this field is visible to end users in Help Center"""


# Entity-specific condition types for ticket_fields
class TicketFieldsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketFieldsSearchFilter


class TicketFieldsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketFieldsSearchFilter


class TicketFieldsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketFieldsSearchFilter


class TicketFieldsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketFieldsSearchFilter


class TicketFieldsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketFieldsSearchFilter


class TicketFieldsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketFieldsSearchFilter


class TicketFieldsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketFieldsStringFilter


class TicketFieldsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketFieldsStringFilter


class TicketFieldsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketFieldsStringFilter


class TicketFieldsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketFieldsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketFieldsInCondition = TypedDict("TicketFieldsInCondition", {"in": TicketFieldsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketFieldsNotCondition = TypedDict("TicketFieldsNotCondition", {"not": "TicketFieldsCondition"}, total=False)
"""Negates the nested condition."""

TicketFieldsAndCondition = TypedDict("TicketFieldsAndCondition", {"and": "list[TicketFieldsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketFieldsOrCondition = TypedDict("TicketFieldsOrCondition", {"or": "list[TicketFieldsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketFieldsAnyCondition = TypedDict("TicketFieldsAnyCondition", {"any": TicketFieldsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_fields condition types
TicketFieldsCondition = (
    TicketFieldsEqCondition
    | TicketFieldsNeqCondition
    | TicketFieldsGtCondition
    | TicketFieldsGteCondition
    | TicketFieldsLtCondition
    | TicketFieldsLteCondition
    | TicketFieldsInCondition
    | TicketFieldsLikeCondition
    | TicketFieldsFuzzyCondition
    | TicketFieldsKeywordCondition
    | TicketFieldsContainsCondition
    | TicketFieldsNotCondition
    | TicketFieldsAndCondition
    | TicketFieldsOrCondition
    | TicketFieldsAnyCondition
)


class TicketFieldsSearchQuery(TypedDict, total=False):
    """Search query for ticket_fields entity."""
    filter: TicketFieldsCondition
    sort: list[TicketFieldsSortFilter]


# ===== TICKET_FORMS SEARCH TYPES =====

class TicketFormsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_forms search queries."""
    active: bool | None
    """Indicates if the form is set as active"""
    agent_conditions: list[Any] | None
    """Array of condition sets for agent workspaces"""
    created_at: str | None
    """Timestamp when the ticket form was created"""
    default: bool | None
    """Indicates if the form is the default form for this account"""
    display_name: str | None
    """The name of the form that is displayed to an end user"""
    end_user_conditions: list[Any] | None
    """Array of condition sets for end user products"""
    end_user_visible: bool | None
    """Indicates if the form is visible to the end user"""
    id: int | None
    """Unique identifier for the ticket form, automatically assigned when creating the form"""
    in_all_brands: bool | None
    """Indicates if the form is available for use in all brands on this account"""
    name: str | None
    """The name of the ticket form"""
    position: int | None
    """The position of this form among other forms in the account, such as in a dropdown"""
    raw_display_name: str | None
    """The dynamic content placeholder if present, or the display_name value if not"""
    raw_name: str | None
    """The dynamic content placeholder if present, or the name value if not"""
    restricted_brand_ids: list[Any] | None
    """IDs of all brands that this ticket form is restricted to"""
    ticket_field_ids: list[Any] | None
    """IDs of all ticket fields included in this ticket form"""
    updated_at: str | None
    """Timestamp of the last update to the ticket form"""
    url: str | None
    """URL of the ticket form"""


class TicketFormsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Indicates if the form is set as active"""
    agent_conditions: list[list[Any]]
    """Array of condition sets for agent workspaces"""
    created_at: list[str]
    """Timestamp when the ticket form was created"""
    default: list[bool]
    """Indicates if the form is the default form for this account"""
    display_name: list[str]
    """The name of the form that is displayed to an end user"""
    end_user_conditions: list[list[Any]]
    """Array of condition sets for end user products"""
    end_user_visible: list[bool]
    """Indicates if the form is visible to the end user"""
    id: list[int]
    """Unique identifier for the ticket form, automatically assigned when creating the form"""
    in_all_brands: list[bool]
    """Indicates if the form is available for use in all brands on this account"""
    name: list[str]
    """The name of the ticket form"""
    position: list[int]
    """The position of this form among other forms in the account, such as in a dropdown"""
    raw_display_name: list[str]
    """The dynamic content placeholder if present, or the display_name value if not"""
    raw_name: list[str]
    """The dynamic content placeholder if present, or the name value if not"""
    restricted_brand_ids: list[list[Any]]
    """IDs of all brands that this ticket form is restricted to"""
    ticket_field_ids: list[list[Any]]
    """IDs of all ticket fields included in this ticket form"""
    updated_at: list[str]
    """Timestamp of the last update to the ticket form"""
    url: list[str]
    """URL of the ticket form"""


class TicketFormsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Indicates if the form is set as active"""
    agent_conditions: Any
    """Array of condition sets for agent workspaces"""
    created_at: Any
    """Timestamp when the ticket form was created"""
    default: Any
    """Indicates if the form is the default form for this account"""
    display_name: Any
    """The name of the form that is displayed to an end user"""
    end_user_conditions: Any
    """Array of condition sets for end user products"""
    end_user_visible: Any
    """Indicates if the form is visible to the end user"""
    id: Any
    """Unique identifier for the ticket form, automatically assigned when creating the form"""
    in_all_brands: Any
    """Indicates if the form is available for use in all brands on this account"""
    name: Any
    """The name of the ticket form"""
    position: Any
    """The position of this form among other forms in the account, such as in a dropdown"""
    raw_display_name: Any
    """The dynamic content placeholder if present, or the display_name value if not"""
    raw_name: Any
    """The dynamic content placeholder if present, or the name value if not"""
    restricted_brand_ids: Any
    """IDs of all brands that this ticket form is restricted to"""
    ticket_field_ids: Any
    """IDs of all ticket fields included in this ticket form"""
    updated_at: Any
    """Timestamp of the last update to the ticket form"""
    url: Any
    """URL of the ticket form"""


class TicketFormsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Indicates if the form is set as active"""
    agent_conditions: str
    """Array of condition sets for agent workspaces"""
    created_at: str
    """Timestamp when the ticket form was created"""
    default: str
    """Indicates if the form is the default form for this account"""
    display_name: str
    """The name of the form that is displayed to an end user"""
    end_user_conditions: str
    """Array of condition sets for end user products"""
    end_user_visible: str
    """Indicates if the form is visible to the end user"""
    id: str
    """Unique identifier for the ticket form, automatically assigned when creating the form"""
    in_all_brands: str
    """Indicates if the form is available for use in all brands on this account"""
    name: str
    """The name of the ticket form"""
    position: str
    """The position of this form among other forms in the account, such as in a dropdown"""
    raw_display_name: str
    """The dynamic content placeholder if present, or the display_name value if not"""
    raw_name: str
    """The dynamic content placeholder if present, or the name value if not"""
    restricted_brand_ids: str
    """IDs of all brands that this ticket form is restricted to"""
    ticket_field_ids: str
    """IDs of all ticket fields included in this ticket form"""
    updated_at: str
    """Timestamp of the last update to the ticket form"""
    url: str
    """URL of the ticket form"""


class TicketFormsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_forms search results."""
    active: AirbyteSortOrder
    """Indicates if the form is set as active"""
    agent_conditions: AirbyteSortOrder
    """Array of condition sets for agent workspaces"""
    created_at: AirbyteSortOrder
    """Timestamp when the ticket form was created"""
    default: AirbyteSortOrder
    """Indicates if the form is the default form for this account"""
    display_name: AirbyteSortOrder
    """The name of the form that is displayed to an end user"""
    end_user_conditions: AirbyteSortOrder
    """Array of condition sets for end user products"""
    end_user_visible: AirbyteSortOrder
    """Indicates if the form is visible to the end user"""
    id: AirbyteSortOrder
    """Unique identifier for the ticket form, automatically assigned when creating the form"""
    in_all_brands: AirbyteSortOrder
    """Indicates if the form is available for use in all brands on this account"""
    name: AirbyteSortOrder
    """The name of the ticket form"""
    position: AirbyteSortOrder
    """The position of this form among other forms in the account, such as in a dropdown"""
    raw_display_name: AirbyteSortOrder
    """The dynamic content placeholder if present, or the display_name value if not"""
    raw_name: AirbyteSortOrder
    """The dynamic content placeholder if present, or the name value if not"""
    restricted_brand_ids: AirbyteSortOrder
    """IDs of all brands that this ticket form is restricted to"""
    ticket_field_ids: AirbyteSortOrder
    """IDs of all ticket fields included in this ticket form"""
    updated_at: AirbyteSortOrder
    """Timestamp of the last update to the ticket form"""
    url: AirbyteSortOrder
    """URL of the ticket form"""


# Entity-specific condition types for ticket_forms
class TicketFormsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketFormsSearchFilter


class TicketFormsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketFormsSearchFilter


class TicketFormsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketFormsSearchFilter


class TicketFormsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketFormsSearchFilter


class TicketFormsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketFormsSearchFilter


class TicketFormsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketFormsSearchFilter


class TicketFormsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketFormsStringFilter


class TicketFormsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketFormsStringFilter


class TicketFormsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketFormsStringFilter


class TicketFormsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketFormsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketFormsInCondition = TypedDict("TicketFormsInCondition", {"in": TicketFormsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketFormsNotCondition = TypedDict("TicketFormsNotCondition", {"not": "TicketFormsCondition"}, total=False)
"""Negates the nested condition."""

TicketFormsAndCondition = TypedDict("TicketFormsAndCondition", {"and": "list[TicketFormsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketFormsOrCondition = TypedDict("TicketFormsOrCondition", {"or": "list[TicketFormsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketFormsAnyCondition = TypedDict("TicketFormsAnyCondition", {"any": TicketFormsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_forms condition types
TicketFormsCondition = (
    TicketFormsEqCondition
    | TicketFormsNeqCondition
    | TicketFormsGtCondition
    | TicketFormsGteCondition
    | TicketFormsLtCondition
    | TicketFormsLteCondition
    | TicketFormsInCondition
    | TicketFormsLikeCondition
    | TicketFormsFuzzyCondition
    | TicketFormsKeywordCondition
    | TicketFormsContainsCondition
    | TicketFormsNotCondition
    | TicketFormsAndCondition
    | TicketFormsOrCondition
    | TicketFormsAnyCondition
)


class TicketFormsSearchQuery(TypedDict, total=False):
    """Search query for ticket_forms entity."""
    filter: TicketFormsCondition
    sort: list[TicketFormsSortFilter]


# ===== TICKET_METRICS SEARCH TYPES =====

class TicketMetricsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_metrics search queries."""
    agent_wait_time_in_minutes: dict[str, Any] | None
    """Number of minutes the agent spent waiting during calendar and business hours"""
    assigned_at: str | None
    """Timestamp when the ticket was assigned"""
    assignee_stations: int | None
    """Number of assignees the ticket had"""
    assignee_updated_at: str | None
    """Timestamp when the assignee last updated the ticket"""
    created_at: str | None
    """Timestamp when the metric record was created"""
    custom_status_updated_at: str | None
    """Timestamp when the ticket's custom status was last updated"""
    first_resolution_time_in_minutes: dict[str, Any] | None
    """Number of minutes to the first resolution time during calendar and business hours"""
    full_resolution_time_in_minutes: dict[str, Any] | None
    """Number of minutes to the full resolution during calendar and business hours"""
    generated_timestamp: int | None
    """Timestamp of when record was last updated"""
    group_stations: int | None
    """Number of groups the ticket passed through"""
    id: int | None
    """Unique identifier for the ticket metric record"""
    initially_assigned_at: str | None
    """Timestamp when the ticket was initially assigned"""
    instance_id: int | None
    """ID of the Zendesk instance associated with the ticket"""
    latest_comment_added_at: str | None
    """Timestamp when the latest comment was added"""
    metric: str | None
    """Ticket metrics data"""
    on_hold_time_in_minutes: dict[str, Any] | None
    """Number of minutes on hold"""
    reopens: int | None
    """Total number of times the ticket was reopened"""
    replies: int | None
    """The number of public replies added to a ticket by an agent"""
    reply_time_in_minutes: dict[str, Any] | None
    """Number of minutes to the first reply during calendar and business hours"""
    reply_time_in_seconds: dict[str, Any] | None
    """Number of seconds to the first reply during calendar hours, only available for Messaging tickets"""
    requester_updated_at: str | None
    """Timestamp when the requester last updated the ticket"""
    requester_wait_time_in_minutes: dict[str, Any] | None
    """Number of minutes the requester spent waiting during calendar and business hours"""
    solved_at: str | None
    """Timestamp when the ticket was solved"""
    status: dict[str, Any] | None
    """The current status of the ticket (open, pending, solved, etc.)."""
    status_updated_at: str | None
    """Timestamp when the status of the ticket was last updated"""
    ticket_id: int | None
    """Identifier of the associated ticket"""
    time: str | None
    """Time related to the ticket"""
    type: str | None
    """Type of ticket"""
    updated_at: str | None
    """Timestamp when the metric record was last updated"""
    url: str | None
    """The API url of the ticket metric"""


class TicketMetricsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    agent_wait_time_in_minutes: list[dict[str, Any]]
    """Number of minutes the agent spent waiting during calendar and business hours"""
    assigned_at: list[str]
    """Timestamp when the ticket was assigned"""
    assignee_stations: list[int]
    """Number of assignees the ticket had"""
    assignee_updated_at: list[str]
    """Timestamp when the assignee last updated the ticket"""
    created_at: list[str]
    """Timestamp when the metric record was created"""
    custom_status_updated_at: list[str]
    """Timestamp when the ticket's custom status was last updated"""
    first_resolution_time_in_minutes: list[dict[str, Any]]
    """Number of minutes to the first resolution time during calendar and business hours"""
    full_resolution_time_in_minutes: list[dict[str, Any]]
    """Number of minutes to the full resolution during calendar and business hours"""
    generated_timestamp: list[int]
    """Timestamp of when record was last updated"""
    group_stations: list[int]
    """Number of groups the ticket passed through"""
    id: list[int]
    """Unique identifier for the ticket metric record"""
    initially_assigned_at: list[str]
    """Timestamp when the ticket was initially assigned"""
    instance_id: list[int]
    """ID of the Zendesk instance associated with the ticket"""
    latest_comment_added_at: list[str]
    """Timestamp when the latest comment was added"""
    metric: list[str]
    """Ticket metrics data"""
    on_hold_time_in_minutes: list[dict[str, Any]]
    """Number of minutes on hold"""
    reopens: list[int]
    """Total number of times the ticket was reopened"""
    replies: list[int]
    """The number of public replies added to a ticket by an agent"""
    reply_time_in_minutes: list[dict[str, Any]]
    """Number of minutes to the first reply during calendar and business hours"""
    reply_time_in_seconds: list[dict[str, Any]]
    """Number of seconds to the first reply during calendar hours, only available for Messaging tickets"""
    requester_updated_at: list[str]
    """Timestamp when the requester last updated the ticket"""
    requester_wait_time_in_minutes: list[dict[str, Any]]
    """Number of minutes the requester spent waiting during calendar and business hours"""
    solved_at: list[str]
    """Timestamp when the ticket was solved"""
    status: list[dict[str, Any]]
    """The current status of the ticket (open, pending, solved, etc.)."""
    status_updated_at: list[str]
    """Timestamp when the status of the ticket was last updated"""
    ticket_id: list[int]
    """Identifier of the associated ticket"""
    time: list[str]
    """Time related to the ticket"""
    type: list[str]
    """Type of ticket"""
    updated_at: list[str]
    """Timestamp when the metric record was last updated"""
    url: list[str]
    """The API url of the ticket metric"""


class TicketMetricsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    agent_wait_time_in_minutes: Any
    """Number of minutes the agent spent waiting during calendar and business hours"""
    assigned_at: Any
    """Timestamp when the ticket was assigned"""
    assignee_stations: Any
    """Number of assignees the ticket had"""
    assignee_updated_at: Any
    """Timestamp when the assignee last updated the ticket"""
    created_at: Any
    """Timestamp when the metric record was created"""
    custom_status_updated_at: Any
    """Timestamp when the ticket's custom status was last updated"""
    first_resolution_time_in_minutes: Any
    """Number of minutes to the first resolution time during calendar and business hours"""
    full_resolution_time_in_minutes: Any
    """Number of minutes to the full resolution during calendar and business hours"""
    generated_timestamp: Any
    """Timestamp of when record was last updated"""
    group_stations: Any
    """Number of groups the ticket passed through"""
    id: Any
    """Unique identifier for the ticket metric record"""
    initially_assigned_at: Any
    """Timestamp when the ticket was initially assigned"""
    instance_id: Any
    """ID of the Zendesk instance associated with the ticket"""
    latest_comment_added_at: Any
    """Timestamp when the latest comment was added"""
    metric: Any
    """Ticket metrics data"""
    on_hold_time_in_minutes: Any
    """Number of minutes on hold"""
    reopens: Any
    """Total number of times the ticket was reopened"""
    replies: Any
    """The number of public replies added to a ticket by an agent"""
    reply_time_in_minutes: Any
    """Number of minutes to the first reply during calendar and business hours"""
    reply_time_in_seconds: Any
    """Number of seconds to the first reply during calendar hours, only available for Messaging tickets"""
    requester_updated_at: Any
    """Timestamp when the requester last updated the ticket"""
    requester_wait_time_in_minutes: Any
    """Number of minutes the requester spent waiting during calendar and business hours"""
    solved_at: Any
    """Timestamp when the ticket was solved"""
    status: Any
    """The current status of the ticket (open, pending, solved, etc.)."""
    status_updated_at: Any
    """Timestamp when the status of the ticket was last updated"""
    ticket_id: Any
    """Identifier of the associated ticket"""
    time: Any
    """Time related to the ticket"""
    type: Any
    """Type of ticket"""
    updated_at: Any
    """Timestamp when the metric record was last updated"""
    url: Any
    """The API url of the ticket metric"""


class TicketMetricsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    agent_wait_time_in_minutes: str
    """Number of minutes the agent spent waiting during calendar and business hours"""
    assigned_at: str
    """Timestamp when the ticket was assigned"""
    assignee_stations: str
    """Number of assignees the ticket had"""
    assignee_updated_at: str
    """Timestamp when the assignee last updated the ticket"""
    created_at: str
    """Timestamp when the metric record was created"""
    custom_status_updated_at: str
    """Timestamp when the ticket's custom status was last updated"""
    first_resolution_time_in_minutes: str
    """Number of minutes to the first resolution time during calendar and business hours"""
    full_resolution_time_in_minutes: str
    """Number of minutes to the full resolution during calendar and business hours"""
    generated_timestamp: str
    """Timestamp of when record was last updated"""
    group_stations: str
    """Number of groups the ticket passed through"""
    id: str
    """Unique identifier for the ticket metric record"""
    initially_assigned_at: str
    """Timestamp when the ticket was initially assigned"""
    instance_id: str
    """ID of the Zendesk instance associated with the ticket"""
    latest_comment_added_at: str
    """Timestamp when the latest comment was added"""
    metric: str
    """Ticket metrics data"""
    on_hold_time_in_minutes: str
    """Number of minutes on hold"""
    reopens: str
    """Total number of times the ticket was reopened"""
    replies: str
    """The number of public replies added to a ticket by an agent"""
    reply_time_in_minutes: str
    """Number of minutes to the first reply during calendar and business hours"""
    reply_time_in_seconds: str
    """Number of seconds to the first reply during calendar hours, only available for Messaging tickets"""
    requester_updated_at: str
    """Timestamp when the requester last updated the ticket"""
    requester_wait_time_in_minutes: str
    """Number of minutes the requester spent waiting during calendar and business hours"""
    solved_at: str
    """Timestamp when the ticket was solved"""
    status: str
    """The current status of the ticket (open, pending, solved, etc.)."""
    status_updated_at: str
    """Timestamp when the status of the ticket was last updated"""
    ticket_id: str
    """Identifier of the associated ticket"""
    time: str
    """Time related to the ticket"""
    type: str
    """Type of ticket"""
    updated_at: str
    """Timestamp when the metric record was last updated"""
    url: str
    """The API url of the ticket metric"""


class TicketMetricsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_metrics search results."""
    agent_wait_time_in_minutes: AirbyteSortOrder
    """Number of minutes the agent spent waiting during calendar and business hours"""
    assigned_at: AirbyteSortOrder
    """Timestamp when the ticket was assigned"""
    assignee_stations: AirbyteSortOrder
    """Number of assignees the ticket had"""
    assignee_updated_at: AirbyteSortOrder
    """Timestamp when the assignee last updated the ticket"""
    created_at: AirbyteSortOrder
    """Timestamp when the metric record was created"""
    custom_status_updated_at: AirbyteSortOrder
    """Timestamp when the ticket's custom status was last updated"""
    first_resolution_time_in_minutes: AirbyteSortOrder
    """Number of minutes to the first resolution time during calendar and business hours"""
    full_resolution_time_in_minutes: AirbyteSortOrder
    """Number of minutes to the full resolution during calendar and business hours"""
    generated_timestamp: AirbyteSortOrder
    """Timestamp of when record was last updated"""
    group_stations: AirbyteSortOrder
    """Number of groups the ticket passed through"""
    id: AirbyteSortOrder
    """Unique identifier for the ticket metric record"""
    initially_assigned_at: AirbyteSortOrder
    """Timestamp when the ticket was initially assigned"""
    instance_id: AirbyteSortOrder
    """ID of the Zendesk instance associated with the ticket"""
    latest_comment_added_at: AirbyteSortOrder
    """Timestamp when the latest comment was added"""
    metric: AirbyteSortOrder
    """Ticket metrics data"""
    on_hold_time_in_minutes: AirbyteSortOrder
    """Number of minutes on hold"""
    reopens: AirbyteSortOrder
    """Total number of times the ticket was reopened"""
    replies: AirbyteSortOrder
    """The number of public replies added to a ticket by an agent"""
    reply_time_in_minutes: AirbyteSortOrder
    """Number of minutes to the first reply during calendar and business hours"""
    reply_time_in_seconds: AirbyteSortOrder
    """Number of seconds to the first reply during calendar hours, only available for Messaging tickets"""
    requester_updated_at: AirbyteSortOrder
    """Timestamp when the requester last updated the ticket"""
    requester_wait_time_in_minutes: AirbyteSortOrder
    """Number of minutes the requester spent waiting during calendar and business hours"""
    solved_at: AirbyteSortOrder
    """Timestamp when the ticket was solved"""
    status: AirbyteSortOrder
    """The current status of the ticket (open, pending, solved, etc.)."""
    status_updated_at: AirbyteSortOrder
    """Timestamp when the status of the ticket was last updated"""
    ticket_id: AirbyteSortOrder
    """Identifier of the associated ticket"""
    time: AirbyteSortOrder
    """Time related to the ticket"""
    type: AirbyteSortOrder
    """Type of ticket"""
    updated_at: AirbyteSortOrder
    """Timestamp when the metric record was last updated"""
    url: AirbyteSortOrder
    """The API url of the ticket metric"""


# Entity-specific condition types for ticket_metrics
class TicketMetricsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketMetricsSearchFilter


class TicketMetricsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketMetricsSearchFilter


class TicketMetricsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketMetricsSearchFilter


class TicketMetricsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketMetricsSearchFilter


class TicketMetricsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketMetricsSearchFilter


class TicketMetricsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketMetricsSearchFilter


class TicketMetricsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketMetricsStringFilter


class TicketMetricsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketMetricsStringFilter


class TicketMetricsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketMetricsStringFilter


class TicketMetricsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketMetricsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketMetricsInCondition = TypedDict("TicketMetricsInCondition", {"in": TicketMetricsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketMetricsNotCondition = TypedDict("TicketMetricsNotCondition", {"not": "TicketMetricsCondition"}, total=False)
"""Negates the nested condition."""

TicketMetricsAndCondition = TypedDict("TicketMetricsAndCondition", {"and": "list[TicketMetricsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketMetricsOrCondition = TypedDict("TicketMetricsOrCondition", {"or": "list[TicketMetricsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketMetricsAnyCondition = TypedDict("TicketMetricsAnyCondition", {"any": TicketMetricsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_metrics condition types
TicketMetricsCondition = (
    TicketMetricsEqCondition
    | TicketMetricsNeqCondition
    | TicketMetricsGtCondition
    | TicketMetricsGteCondition
    | TicketMetricsLtCondition
    | TicketMetricsLteCondition
    | TicketMetricsInCondition
    | TicketMetricsLikeCondition
    | TicketMetricsFuzzyCondition
    | TicketMetricsKeywordCondition
    | TicketMetricsContainsCondition
    | TicketMetricsNotCondition
    | TicketMetricsAndCondition
    | TicketMetricsOrCondition
    | TicketMetricsAnyCondition
)


class TicketMetricsSearchQuery(TypedDict, total=False):
    """Search query for ticket_metrics entity."""
    filter: TicketMetricsCondition
    sort: list[TicketMetricsSortFilter]


# ===== TICKETS SEARCH TYPES =====

class TicketsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tickets search queries."""
    allow_attachments: bool | None
    """Boolean indicating whether attachments are allowed on the ticket"""
    allow_channelback: bool | None
    """Boolean indicating whether agents can reply to the ticket through the original channel"""
    assignee_id: int | None
    """Unique identifier of the agent currently assigned to the ticket"""
    brand_id: int | None
    """Unique identifier of the brand associated with the ticket in multi-brand accounts"""
    collaborator_ids: list[Any] | None
    """Array of user identifiers who are collaborating on the ticket"""
    created_at: str | None
    """Timestamp indicating when the ticket was created"""
    custom_fields: list[Any] | None
    """Array of custom field values specific to the account's ticket configuration"""
    custom_status_id: int | None
    """Unique identifier of the custom status applied to the ticket"""
    deleted_ticket_form_id: int | None
    """The ID of the ticket form that was previously associated with this ticket but has since been deleted"""
    description: str | None
    """Initial description or content of the ticket when it was created"""
    due_at: str | None
    """Timestamp indicating when the ticket is due for completion or resolution"""
    email_cc_ids: list[Any] | None
    """Array of user identifiers who are CC'd on ticket email notifications"""
    external_id: str | None
    """External identifier for the ticket, used for integrations with other systems"""
    fields: list[Any] | None
    """Array of ticket field values including both system and custom fields"""
    follower_ids: list[Any] | None
    """Array of user identifiers who are following the ticket for updates"""
    followup_ids: list[Any] | None
    """Array of identifiers for follow-up tickets related to this ticket"""
    forum_topic_id: int | None
    """Unique identifier linking the ticket to a forum topic if applicable"""
    from_messaging_channel: bool | None
    """Boolean indicating whether the ticket originated from a messaging channel"""
    generated_timestamp: int | None
    """Timestamp updated for all ticket updates including system changes, used for incremental export"""
    group_id: int | None
    """Unique identifier of the agent group assigned to handle the ticket"""
    has_incidents: bool | None
    """Boolean indicating whether this problem ticket has related incident tickets"""
    id: int | None
    """Unique identifier for the ticket"""
    is_public: bool | None
    """Boolean indicating whether the ticket is publicly visible"""
    organization_id: int | None
    """Unique identifier of the organization associated with the ticket"""
    priority: str | None
    """Priority level assigned to the ticket (e.g., urgent, high, normal, low)"""
    problem_id: int | None
    """Unique identifier of the problem ticket if this is an incident ticket"""
    raw_subject: str | None
    """Original unprocessed subject line before any system modifications"""
    recipient: str | None
    """Email address or identifier of the ticket recipient"""
    requester_id: int | None
    """Unique identifier of the user who requested or created the ticket"""
    satisfaction_rating: Any
    """Object containing customer satisfaction rating data for the ticket"""
    sharing_agreement_ids: list[Any] | None
    """Array of sharing agreement identifiers if the ticket is shared across Zendesk instances"""
    status: str | None
    """Current status of the ticket (e.g., new, open, pending, solved, closed)"""
    subject: str | None
    """Subject line of the ticket describing the issue or request"""
    submitter_id: int | None
    """Unique identifier of the user who submitted the ticket on behalf of the requester"""
    tags: list[Any] | None
    """Array of tags applied to the ticket for categorization and filtering"""
    ticket_form_id: int | None
    """Unique identifier of the ticket form used when creating the ticket"""
    type: str | None
    """Type of ticket (e.g., problem, incident, question, task)"""
    updated_at: str | None
    """Timestamp indicating when the ticket was last updated with a ticket event"""
    url: str | None
    """API URL to access the full ticket resource"""
    via: dict[str, Any] | None
    """Object describing the channel and method through which the ticket was created"""


class TicketsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    allow_attachments: list[bool]
    """Boolean indicating whether attachments are allowed on the ticket"""
    allow_channelback: list[bool]
    """Boolean indicating whether agents can reply to the ticket through the original channel"""
    assignee_id: list[int]
    """Unique identifier of the agent currently assigned to the ticket"""
    brand_id: list[int]
    """Unique identifier of the brand associated with the ticket in multi-brand accounts"""
    collaborator_ids: list[list[Any]]
    """Array of user identifiers who are collaborating on the ticket"""
    created_at: list[str]
    """Timestamp indicating when the ticket was created"""
    custom_fields: list[list[Any]]
    """Array of custom field values specific to the account's ticket configuration"""
    custom_status_id: list[int]
    """Unique identifier of the custom status applied to the ticket"""
    deleted_ticket_form_id: list[int]
    """The ID of the ticket form that was previously associated with this ticket but has since been deleted"""
    description: list[str]
    """Initial description or content of the ticket when it was created"""
    due_at: list[str]
    """Timestamp indicating when the ticket is due for completion or resolution"""
    email_cc_ids: list[list[Any]]
    """Array of user identifiers who are CC'd on ticket email notifications"""
    external_id: list[str]
    """External identifier for the ticket, used for integrations with other systems"""
    fields: list[list[Any]]
    """Array of ticket field values including both system and custom fields"""
    follower_ids: list[list[Any]]
    """Array of user identifiers who are following the ticket for updates"""
    followup_ids: list[list[Any]]
    """Array of identifiers for follow-up tickets related to this ticket"""
    forum_topic_id: list[int]
    """Unique identifier linking the ticket to a forum topic if applicable"""
    from_messaging_channel: list[bool]
    """Boolean indicating whether the ticket originated from a messaging channel"""
    generated_timestamp: list[int]
    """Timestamp updated for all ticket updates including system changes, used for incremental export"""
    group_id: list[int]
    """Unique identifier of the agent group assigned to handle the ticket"""
    has_incidents: list[bool]
    """Boolean indicating whether this problem ticket has related incident tickets"""
    id: list[int]
    """Unique identifier for the ticket"""
    is_public: list[bool]
    """Boolean indicating whether the ticket is publicly visible"""
    organization_id: list[int]
    """Unique identifier of the organization associated with the ticket"""
    priority: list[str]
    """Priority level assigned to the ticket (e.g., urgent, high, normal, low)"""
    problem_id: list[int]
    """Unique identifier of the problem ticket if this is an incident ticket"""
    raw_subject: list[str]
    """Original unprocessed subject line before any system modifications"""
    recipient: list[str]
    """Email address or identifier of the ticket recipient"""
    requester_id: list[int]
    """Unique identifier of the user who requested or created the ticket"""
    satisfaction_rating: list[Any]
    """Object containing customer satisfaction rating data for the ticket"""
    sharing_agreement_ids: list[list[Any]]
    """Array of sharing agreement identifiers if the ticket is shared across Zendesk instances"""
    status: list[str]
    """Current status of the ticket (e.g., new, open, pending, solved, closed)"""
    subject: list[str]
    """Subject line of the ticket describing the issue or request"""
    submitter_id: list[int]
    """Unique identifier of the user who submitted the ticket on behalf of the requester"""
    tags: list[list[Any]]
    """Array of tags applied to the ticket for categorization and filtering"""
    ticket_form_id: list[int]
    """Unique identifier of the ticket form used when creating the ticket"""
    type: list[str]
    """Type of ticket (e.g., problem, incident, question, task)"""
    updated_at: list[str]
    """Timestamp indicating when the ticket was last updated with a ticket event"""
    url: list[str]
    """API URL to access the full ticket resource"""
    via: list[dict[str, Any]]
    """Object describing the channel and method through which the ticket was created"""


class TicketsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    allow_attachments: Any
    """Boolean indicating whether attachments are allowed on the ticket"""
    allow_channelback: Any
    """Boolean indicating whether agents can reply to the ticket through the original channel"""
    assignee_id: Any
    """Unique identifier of the agent currently assigned to the ticket"""
    brand_id: Any
    """Unique identifier of the brand associated with the ticket in multi-brand accounts"""
    collaborator_ids: Any
    """Array of user identifiers who are collaborating on the ticket"""
    created_at: Any
    """Timestamp indicating when the ticket was created"""
    custom_fields: Any
    """Array of custom field values specific to the account's ticket configuration"""
    custom_status_id: Any
    """Unique identifier of the custom status applied to the ticket"""
    deleted_ticket_form_id: Any
    """The ID of the ticket form that was previously associated with this ticket but has since been deleted"""
    description: Any
    """Initial description or content of the ticket when it was created"""
    due_at: Any
    """Timestamp indicating when the ticket is due for completion or resolution"""
    email_cc_ids: Any
    """Array of user identifiers who are CC'd on ticket email notifications"""
    external_id: Any
    """External identifier for the ticket, used for integrations with other systems"""
    fields: Any
    """Array of ticket field values including both system and custom fields"""
    follower_ids: Any
    """Array of user identifiers who are following the ticket for updates"""
    followup_ids: Any
    """Array of identifiers for follow-up tickets related to this ticket"""
    forum_topic_id: Any
    """Unique identifier linking the ticket to a forum topic if applicable"""
    from_messaging_channel: Any
    """Boolean indicating whether the ticket originated from a messaging channel"""
    generated_timestamp: Any
    """Timestamp updated for all ticket updates including system changes, used for incremental export"""
    group_id: Any
    """Unique identifier of the agent group assigned to handle the ticket"""
    has_incidents: Any
    """Boolean indicating whether this problem ticket has related incident tickets"""
    id: Any
    """Unique identifier for the ticket"""
    is_public: Any
    """Boolean indicating whether the ticket is publicly visible"""
    organization_id: Any
    """Unique identifier of the organization associated with the ticket"""
    priority: Any
    """Priority level assigned to the ticket (e.g., urgent, high, normal, low)"""
    problem_id: Any
    """Unique identifier of the problem ticket if this is an incident ticket"""
    raw_subject: Any
    """Original unprocessed subject line before any system modifications"""
    recipient: Any
    """Email address or identifier of the ticket recipient"""
    requester_id: Any
    """Unique identifier of the user who requested or created the ticket"""
    satisfaction_rating: Any
    """Object containing customer satisfaction rating data for the ticket"""
    sharing_agreement_ids: Any
    """Array of sharing agreement identifiers if the ticket is shared across Zendesk instances"""
    status: Any
    """Current status of the ticket (e.g., new, open, pending, solved, closed)"""
    subject: Any
    """Subject line of the ticket describing the issue or request"""
    submitter_id: Any
    """Unique identifier of the user who submitted the ticket on behalf of the requester"""
    tags: Any
    """Array of tags applied to the ticket for categorization and filtering"""
    ticket_form_id: Any
    """Unique identifier of the ticket form used when creating the ticket"""
    type: Any
    """Type of ticket (e.g., problem, incident, question, task)"""
    updated_at: Any
    """Timestamp indicating when the ticket was last updated with a ticket event"""
    url: Any
    """API URL to access the full ticket resource"""
    via: Any
    """Object describing the channel and method through which the ticket was created"""


class TicketsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    allow_attachments: str
    """Boolean indicating whether attachments are allowed on the ticket"""
    allow_channelback: str
    """Boolean indicating whether agents can reply to the ticket through the original channel"""
    assignee_id: str
    """Unique identifier of the agent currently assigned to the ticket"""
    brand_id: str
    """Unique identifier of the brand associated with the ticket in multi-brand accounts"""
    collaborator_ids: str
    """Array of user identifiers who are collaborating on the ticket"""
    created_at: str
    """Timestamp indicating when the ticket was created"""
    custom_fields: str
    """Array of custom field values specific to the account's ticket configuration"""
    custom_status_id: str
    """Unique identifier of the custom status applied to the ticket"""
    deleted_ticket_form_id: str
    """The ID of the ticket form that was previously associated with this ticket but has since been deleted"""
    description: str
    """Initial description or content of the ticket when it was created"""
    due_at: str
    """Timestamp indicating when the ticket is due for completion or resolution"""
    email_cc_ids: str
    """Array of user identifiers who are CC'd on ticket email notifications"""
    external_id: str
    """External identifier for the ticket, used for integrations with other systems"""
    fields: str
    """Array of ticket field values including both system and custom fields"""
    follower_ids: str
    """Array of user identifiers who are following the ticket for updates"""
    followup_ids: str
    """Array of identifiers for follow-up tickets related to this ticket"""
    forum_topic_id: str
    """Unique identifier linking the ticket to a forum topic if applicable"""
    from_messaging_channel: str
    """Boolean indicating whether the ticket originated from a messaging channel"""
    generated_timestamp: str
    """Timestamp updated for all ticket updates including system changes, used for incremental export"""
    group_id: str
    """Unique identifier of the agent group assigned to handle the ticket"""
    has_incidents: str
    """Boolean indicating whether this problem ticket has related incident tickets"""
    id: str
    """Unique identifier for the ticket"""
    is_public: str
    """Boolean indicating whether the ticket is publicly visible"""
    organization_id: str
    """Unique identifier of the organization associated with the ticket"""
    priority: str
    """Priority level assigned to the ticket (e.g., urgent, high, normal, low)"""
    problem_id: str
    """Unique identifier of the problem ticket if this is an incident ticket"""
    raw_subject: str
    """Original unprocessed subject line before any system modifications"""
    recipient: str
    """Email address or identifier of the ticket recipient"""
    requester_id: str
    """Unique identifier of the user who requested or created the ticket"""
    satisfaction_rating: str
    """Object containing customer satisfaction rating data for the ticket"""
    sharing_agreement_ids: str
    """Array of sharing agreement identifiers if the ticket is shared across Zendesk instances"""
    status: str
    """Current status of the ticket (e.g., new, open, pending, solved, closed)"""
    subject: str
    """Subject line of the ticket describing the issue or request"""
    submitter_id: str
    """Unique identifier of the user who submitted the ticket on behalf of the requester"""
    tags: str
    """Array of tags applied to the ticket for categorization and filtering"""
    ticket_form_id: str
    """Unique identifier of the ticket form used when creating the ticket"""
    type: str
    """Type of ticket (e.g., problem, incident, question, task)"""
    updated_at: str
    """Timestamp indicating when the ticket was last updated with a ticket event"""
    url: str
    """API URL to access the full ticket resource"""
    via: str
    """Object describing the channel and method through which the ticket was created"""


class TicketsSortFilter(TypedDict, total=False):
    """Available fields for sorting tickets search results."""
    allow_attachments: AirbyteSortOrder
    """Boolean indicating whether attachments are allowed on the ticket"""
    allow_channelback: AirbyteSortOrder
    """Boolean indicating whether agents can reply to the ticket through the original channel"""
    assignee_id: AirbyteSortOrder
    """Unique identifier of the agent currently assigned to the ticket"""
    brand_id: AirbyteSortOrder
    """Unique identifier of the brand associated with the ticket in multi-brand accounts"""
    collaborator_ids: AirbyteSortOrder
    """Array of user identifiers who are collaborating on the ticket"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the ticket was created"""
    custom_fields: AirbyteSortOrder
    """Array of custom field values specific to the account's ticket configuration"""
    custom_status_id: AirbyteSortOrder
    """Unique identifier of the custom status applied to the ticket"""
    deleted_ticket_form_id: AirbyteSortOrder
    """The ID of the ticket form that was previously associated with this ticket but has since been deleted"""
    description: AirbyteSortOrder
    """Initial description or content of the ticket when it was created"""
    due_at: AirbyteSortOrder
    """Timestamp indicating when the ticket is due for completion or resolution"""
    email_cc_ids: AirbyteSortOrder
    """Array of user identifiers who are CC'd on ticket email notifications"""
    external_id: AirbyteSortOrder
    """External identifier for the ticket, used for integrations with other systems"""
    fields: AirbyteSortOrder
    """Array of ticket field values including both system and custom fields"""
    follower_ids: AirbyteSortOrder
    """Array of user identifiers who are following the ticket for updates"""
    followup_ids: AirbyteSortOrder
    """Array of identifiers for follow-up tickets related to this ticket"""
    forum_topic_id: AirbyteSortOrder
    """Unique identifier linking the ticket to a forum topic if applicable"""
    from_messaging_channel: AirbyteSortOrder
    """Boolean indicating whether the ticket originated from a messaging channel"""
    generated_timestamp: AirbyteSortOrder
    """Timestamp updated for all ticket updates including system changes, used for incremental export"""
    group_id: AirbyteSortOrder
    """Unique identifier of the agent group assigned to handle the ticket"""
    has_incidents: AirbyteSortOrder
    """Boolean indicating whether this problem ticket has related incident tickets"""
    id: AirbyteSortOrder
    """Unique identifier for the ticket"""
    is_public: AirbyteSortOrder
    """Boolean indicating whether the ticket is publicly visible"""
    organization_id: AirbyteSortOrder
    """Unique identifier of the organization associated with the ticket"""
    priority: AirbyteSortOrder
    """Priority level assigned to the ticket (e.g., urgent, high, normal, low)"""
    problem_id: AirbyteSortOrder
    """Unique identifier of the problem ticket if this is an incident ticket"""
    raw_subject: AirbyteSortOrder
    """Original unprocessed subject line before any system modifications"""
    recipient: AirbyteSortOrder
    """Email address or identifier of the ticket recipient"""
    requester_id: AirbyteSortOrder
    """Unique identifier of the user who requested or created the ticket"""
    satisfaction_rating: AirbyteSortOrder
    """Object containing customer satisfaction rating data for the ticket"""
    sharing_agreement_ids: AirbyteSortOrder
    """Array of sharing agreement identifiers if the ticket is shared across Zendesk instances"""
    status: AirbyteSortOrder
    """Current status of the ticket (e.g., new, open, pending, solved, closed)"""
    subject: AirbyteSortOrder
    """Subject line of the ticket describing the issue or request"""
    submitter_id: AirbyteSortOrder
    """Unique identifier of the user who submitted the ticket on behalf of the requester"""
    tags: AirbyteSortOrder
    """Array of tags applied to the ticket for categorization and filtering"""
    ticket_form_id: AirbyteSortOrder
    """Unique identifier of the ticket form used when creating the ticket"""
    type: AirbyteSortOrder
    """Type of ticket (e.g., problem, incident, question, task)"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the ticket was last updated with a ticket event"""
    url: AirbyteSortOrder
    """API URL to access the full ticket resource"""
    via: AirbyteSortOrder
    """Object describing the channel and method through which the ticket was created"""


# Entity-specific condition types for tickets
class TicketsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketsSearchFilter


class TicketsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketsSearchFilter


class TicketsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketsSearchFilter


class TicketsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketsSearchFilter


class TicketsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketsSearchFilter


class TicketsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketsSearchFilter


class TicketsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketsStringFilter


class TicketsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketsStringFilter


class TicketsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketsStringFilter


class TicketsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketsInCondition = TypedDict("TicketsInCondition", {"in": TicketsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketsNotCondition = TypedDict("TicketsNotCondition", {"not": "TicketsCondition"}, total=False)
"""Negates the nested condition."""

TicketsAndCondition = TypedDict("TicketsAndCondition", {"and": "list[TicketsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketsOrCondition = TypedDict("TicketsOrCondition", {"or": "list[TicketsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketsAnyCondition = TypedDict("TicketsAnyCondition", {"any": TicketsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tickets condition types
TicketsCondition = (
    TicketsEqCondition
    | TicketsNeqCondition
    | TicketsGtCondition
    | TicketsGteCondition
    | TicketsLtCondition
    | TicketsLteCondition
    | TicketsInCondition
    | TicketsLikeCondition
    | TicketsFuzzyCondition
    | TicketsKeywordCondition
    | TicketsContainsCondition
    | TicketsNotCondition
    | TicketsAndCondition
    | TicketsOrCondition
    | TicketsAnyCondition
)


class TicketsSearchQuery(TypedDict, total=False):
    """Search query for tickets entity."""
    filter: TicketsCondition
    sort: list[TicketsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    active: bool | None
    """Indicates if the user account is currently active"""
    alias: str | None
    """Alternative name or nickname for the user"""
    chat_only: bool | None
    """Indicates if the user can only interact via chat"""
    created_at: str | None
    """Timestamp indicating when the user was created"""
    custom_role_id: int | None
    """Identifier for a custom role assigned to the user"""
    default_group_id: int | None
    """Identifier of the default group assigned to the user"""
    details: str | None
    """Additional descriptive information about the user"""
    email: str | None
    """Email address of the user"""
    external_id: str | None
    """External system identifier for the user, used for integrations"""
    iana_time_zone: str | None
    """IANA standard time zone identifier for the user"""
    id: int | None
    """Unique identifier for the user"""
    last_login_at: str | None
    """Timestamp of the user's most recent login"""
    locale: str | None
    """Locale setting determining language and regional format preferences"""
    locale_id: int | None
    """Identifier for the user's locale preference"""
    moderator: bool | None
    """Indicates if the user has moderator privileges"""
    name: str | None
    """Display name of the user"""
    notes: str | None
    """Internal notes about the user, visible only to agents"""
    only_private_comments: bool | None
    """Indicates if the user can only make private comments on tickets"""
    organization_id: int | None
    """Identifier of the organization the user belongs to"""
    permanently_deleted: bool | None
    """Indicates if the user has been permanently deleted from the system"""
    phone: str | None
    """Phone number of the user"""
    photo: dict[str, Any] | None
    """Profile photo or avatar of the user"""
    report_csv: bool | None
    """Indicates if the user receives reports in CSV format"""
    restricted_agent: bool | None
    """Indicates if the agent has restricted access permissions"""
    role: str | None
    """Role assigned to the user defining their permissions level"""
    role_type: int | None
    """Type classification of the user's role"""
    shared: bool | None
    """Indicates if the user is shared across multiple accounts"""
    shared_agent: bool | None
    """Indicates if the user is a shared agent across multiple brands or accounts"""
    shared_phone_number: bool | None
    """Indicates if the phone number is shared with other users"""
    signature: str | None
    """Email signature text for the user"""
    suspended: bool | None
    """Indicates if the user account is suspended"""
    tags: list[Any] | None
    """Labels or tags associated with the user for categorization"""
    ticket_restriction: str | None
    """Defines which tickets the user can access based on restrictions"""
    time_zone: str | None
    """Time zone setting for the user"""
    two_factor_auth_enabled: bool | None
    """Indicates if two-factor authentication is enabled for the user"""
    updated_at: str | None
    """Timestamp indicating when the user was last updated"""
    url: str | None
    """API endpoint URL for accessing the user's detailed information"""
    user_fields: dict[str, Any] | None
    """Custom field values specific to the user, stored as key-value pairs"""
    verified: bool | None
    """Indicates if the user's identity has been verified"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """Indicates if the user account is currently active"""
    alias: list[str]
    """Alternative name or nickname for the user"""
    chat_only: list[bool]
    """Indicates if the user can only interact via chat"""
    created_at: list[str]
    """Timestamp indicating when the user was created"""
    custom_role_id: list[int]
    """Identifier for a custom role assigned to the user"""
    default_group_id: list[int]
    """Identifier of the default group assigned to the user"""
    details: list[str]
    """Additional descriptive information about the user"""
    email: list[str]
    """Email address of the user"""
    external_id: list[str]
    """External system identifier for the user, used for integrations"""
    iana_time_zone: list[str]
    """IANA standard time zone identifier for the user"""
    id: list[int]
    """Unique identifier for the user"""
    last_login_at: list[str]
    """Timestamp of the user's most recent login"""
    locale: list[str]
    """Locale setting determining language and regional format preferences"""
    locale_id: list[int]
    """Identifier for the user's locale preference"""
    moderator: list[bool]
    """Indicates if the user has moderator privileges"""
    name: list[str]
    """Display name of the user"""
    notes: list[str]
    """Internal notes about the user, visible only to agents"""
    only_private_comments: list[bool]
    """Indicates if the user can only make private comments on tickets"""
    organization_id: list[int]
    """Identifier of the organization the user belongs to"""
    permanently_deleted: list[bool]
    """Indicates if the user has been permanently deleted from the system"""
    phone: list[str]
    """Phone number of the user"""
    photo: list[dict[str, Any]]
    """Profile photo or avatar of the user"""
    report_csv: list[bool]
    """Indicates if the user receives reports in CSV format"""
    restricted_agent: list[bool]
    """Indicates if the agent has restricted access permissions"""
    role: list[str]
    """Role assigned to the user defining their permissions level"""
    role_type: list[int]
    """Type classification of the user's role"""
    shared: list[bool]
    """Indicates if the user is shared across multiple accounts"""
    shared_agent: list[bool]
    """Indicates if the user is a shared agent across multiple brands or accounts"""
    shared_phone_number: list[bool]
    """Indicates if the phone number is shared with other users"""
    signature: list[str]
    """Email signature text for the user"""
    suspended: list[bool]
    """Indicates if the user account is suspended"""
    tags: list[list[Any]]
    """Labels or tags associated with the user for categorization"""
    ticket_restriction: list[str]
    """Defines which tickets the user can access based on restrictions"""
    time_zone: list[str]
    """Time zone setting for the user"""
    two_factor_auth_enabled: list[bool]
    """Indicates if two-factor authentication is enabled for the user"""
    updated_at: list[str]
    """Timestamp indicating when the user was last updated"""
    url: list[str]
    """API endpoint URL for accessing the user's detailed information"""
    user_fields: list[dict[str, Any]]
    """Custom field values specific to the user, stored as key-value pairs"""
    verified: list[bool]
    """Indicates if the user's identity has been verified"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """Indicates if the user account is currently active"""
    alias: Any
    """Alternative name or nickname for the user"""
    chat_only: Any
    """Indicates if the user can only interact via chat"""
    created_at: Any
    """Timestamp indicating when the user was created"""
    custom_role_id: Any
    """Identifier for a custom role assigned to the user"""
    default_group_id: Any
    """Identifier of the default group assigned to the user"""
    details: Any
    """Additional descriptive information about the user"""
    email: Any
    """Email address of the user"""
    external_id: Any
    """External system identifier for the user, used for integrations"""
    iana_time_zone: Any
    """IANA standard time zone identifier for the user"""
    id: Any
    """Unique identifier for the user"""
    last_login_at: Any
    """Timestamp of the user's most recent login"""
    locale: Any
    """Locale setting determining language and regional format preferences"""
    locale_id: Any
    """Identifier for the user's locale preference"""
    moderator: Any
    """Indicates if the user has moderator privileges"""
    name: Any
    """Display name of the user"""
    notes: Any
    """Internal notes about the user, visible only to agents"""
    only_private_comments: Any
    """Indicates if the user can only make private comments on tickets"""
    organization_id: Any
    """Identifier of the organization the user belongs to"""
    permanently_deleted: Any
    """Indicates if the user has been permanently deleted from the system"""
    phone: Any
    """Phone number of the user"""
    photo: Any
    """Profile photo or avatar of the user"""
    report_csv: Any
    """Indicates if the user receives reports in CSV format"""
    restricted_agent: Any
    """Indicates if the agent has restricted access permissions"""
    role: Any
    """Role assigned to the user defining their permissions level"""
    role_type: Any
    """Type classification of the user's role"""
    shared: Any
    """Indicates if the user is shared across multiple accounts"""
    shared_agent: Any
    """Indicates if the user is a shared agent across multiple brands or accounts"""
    shared_phone_number: Any
    """Indicates if the phone number is shared with other users"""
    signature: Any
    """Email signature text for the user"""
    suspended: Any
    """Indicates if the user account is suspended"""
    tags: Any
    """Labels or tags associated with the user for categorization"""
    ticket_restriction: Any
    """Defines which tickets the user can access based on restrictions"""
    time_zone: Any
    """Time zone setting for the user"""
    two_factor_auth_enabled: Any
    """Indicates if two-factor authentication is enabled for the user"""
    updated_at: Any
    """Timestamp indicating when the user was last updated"""
    url: Any
    """API endpoint URL for accessing the user's detailed information"""
    user_fields: Any
    """Custom field values specific to the user, stored as key-value pairs"""
    verified: Any
    """Indicates if the user's identity has been verified"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """Indicates if the user account is currently active"""
    alias: str
    """Alternative name or nickname for the user"""
    chat_only: str
    """Indicates if the user can only interact via chat"""
    created_at: str
    """Timestamp indicating when the user was created"""
    custom_role_id: str
    """Identifier for a custom role assigned to the user"""
    default_group_id: str
    """Identifier of the default group assigned to the user"""
    details: str
    """Additional descriptive information about the user"""
    email: str
    """Email address of the user"""
    external_id: str
    """External system identifier for the user, used for integrations"""
    iana_time_zone: str
    """IANA standard time zone identifier for the user"""
    id: str
    """Unique identifier for the user"""
    last_login_at: str
    """Timestamp of the user's most recent login"""
    locale: str
    """Locale setting determining language and regional format preferences"""
    locale_id: str
    """Identifier for the user's locale preference"""
    moderator: str
    """Indicates if the user has moderator privileges"""
    name: str
    """Display name of the user"""
    notes: str
    """Internal notes about the user, visible only to agents"""
    only_private_comments: str
    """Indicates if the user can only make private comments on tickets"""
    organization_id: str
    """Identifier of the organization the user belongs to"""
    permanently_deleted: str
    """Indicates if the user has been permanently deleted from the system"""
    phone: str
    """Phone number of the user"""
    photo: str
    """Profile photo or avatar of the user"""
    report_csv: str
    """Indicates if the user receives reports in CSV format"""
    restricted_agent: str
    """Indicates if the agent has restricted access permissions"""
    role: str
    """Role assigned to the user defining their permissions level"""
    role_type: str
    """Type classification of the user's role"""
    shared: str
    """Indicates if the user is shared across multiple accounts"""
    shared_agent: str
    """Indicates if the user is a shared agent across multiple brands or accounts"""
    shared_phone_number: str
    """Indicates if the phone number is shared with other users"""
    signature: str
    """Email signature text for the user"""
    suspended: str
    """Indicates if the user account is suspended"""
    tags: str
    """Labels or tags associated with the user for categorization"""
    ticket_restriction: str
    """Defines which tickets the user can access based on restrictions"""
    time_zone: str
    """Time zone setting for the user"""
    two_factor_auth_enabled: str
    """Indicates if two-factor authentication is enabled for the user"""
    updated_at: str
    """Timestamp indicating when the user was last updated"""
    url: str
    """API endpoint URL for accessing the user's detailed information"""
    user_fields: str
    """Custom field values specific to the user, stored as key-value pairs"""
    verified: str
    """Indicates if the user's identity has been verified"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    active: AirbyteSortOrder
    """Indicates if the user account is currently active"""
    alias: AirbyteSortOrder
    """Alternative name or nickname for the user"""
    chat_only: AirbyteSortOrder
    """Indicates if the user can only interact via chat"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the user was created"""
    custom_role_id: AirbyteSortOrder
    """Identifier for a custom role assigned to the user"""
    default_group_id: AirbyteSortOrder
    """Identifier of the default group assigned to the user"""
    details: AirbyteSortOrder
    """Additional descriptive information about the user"""
    email: AirbyteSortOrder
    """Email address of the user"""
    external_id: AirbyteSortOrder
    """External system identifier for the user, used for integrations"""
    iana_time_zone: AirbyteSortOrder
    """IANA standard time zone identifier for the user"""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    last_login_at: AirbyteSortOrder
    """Timestamp of the user's most recent login"""
    locale: AirbyteSortOrder
    """Locale setting determining language and regional format preferences"""
    locale_id: AirbyteSortOrder
    """Identifier for the user's locale preference"""
    moderator: AirbyteSortOrder
    """Indicates if the user has moderator privileges"""
    name: AirbyteSortOrder
    """Display name of the user"""
    notes: AirbyteSortOrder
    """Internal notes about the user, visible only to agents"""
    only_private_comments: AirbyteSortOrder
    """Indicates if the user can only make private comments on tickets"""
    organization_id: AirbyteSortOrder
    """Identifier of the organization the user belongs to"""
    permanently_deleted: AirbyteSortOrder
    """Indicates if the user has been permanently deleted from the system"""
    phone: AirbyteSortOrder
    """Phone number of the user"""
    photo: AirbyteSortOrder
    """Profile photo or avatar of the user"""
    report_csv: AirbyteSortOrder
    """Indicates if the user receives reports in CSV format"""
    restricted_agent: AirbyteSortOrder
    """Indicates if the agent has restricted access permissions"""
    role: AirbyteSortOrder
    """Role assigned to the user defining their permissions level"""
    role_type: AirbyteSortOrder
    """Type classification of the user's role"""
    shared: AirbyteSortOrder
    """Indicates if the user is shared across multiple accounts"""
    shared_agent: AirbyteSortOrder
    """Indicates if the user is a shared agent across multiple brands or accounts"""
    shared_phone_number: AirbyteSortOrder
    """Indicates if the phone number is shared with other users"""
    signature: AirbyteSortOrder
    """Email signature text for the user"""
    suspended: AirbyteSortOrder
    """Indicates if the user account is suspended"""
    tags: AirbyteSortOrder
    """Labels or tags associated with the user for categorization"""
    ticket_restriction: AirbyteSortOrder
    """Defines which tickets the user can access based on restrictions"""
    time_zone: AirbyteSortOrder
    """Time zone setting for the user"""
    two_factor_auth_enabled: AirbyteSortOrder
    """Indicates if two-factor authentication is enabled for the user"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the user was last updated"""
    url: AirbyteSortOrder
    """API endpoint URL for accessing the user's detailed information"""
    user_fields: AirbyteSortOrder
    """Custom field values specific to the user, stored as key-value pairs"""
    verified: AirbyteSortOrder
    """Indicates if the user's identity has been verified"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
