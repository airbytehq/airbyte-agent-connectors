"""
Type definitions for confluence connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class SpacesListParams(TypedDict):
    """Parameters for spaces.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]
    type: NotRequired[str]
    status: NotRequired[str]
    keys: NotRequired[list[str]]
    sort: NotRequired[str]

class SpacesGetParams(TypedDict):
    """Parameters for spaces.get operation"""
    id: str
    description_format: NotRequired[str]

class PagesListParams(TypedDict):
    """Parameters for pages.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]
    space_id: NotRequired[list[int]]
    title: NotRequired[str]
    status: NotRequired[list[str]]
    sort: NotRequired[str]
    body_format: NotRequired[str]

class PagesGetParams(TypedDict):
    """Parameters for pages.get operation"""
    id: str
    body_format: NotRequired[str]
    version: NotRequired[int]

class BlogPostsListParams(TypedDict):
    """Parameters for blog_posts.list operation"""
    cursor: NotRequired[str]
    limit: NotRequired[int]
    space_id: NotRequired[list[int]]
    title: NotRequired[str]
    status: NotRequired[list[str]]
    sort: NotRequired[str]
    body_format: NotRequired[str]

class BlogPostsGetParams(TypedDict):
    """Parameters for blog_posts.get operation"""
    id: str
    body_format: NotRequired[str]
    version: NotRequired[int]

class GroupsListParams(TypedDict):
    """Parameters for groups.list operation"""
    start: NotRequired[int]
    limit: NotRequired[int]

class AuditListParams(TypedDict):
    """Parameters for audit.list operation"""
    start: NotRequired[int]
    limit: NotRequired[int]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    search_string: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== AUDIT SEARCH TYPES =====

class AuditSearchFilter(TypedDict, total=False):
    """Available fields for filtering audit search queries."""
    affected_object: dict[str, Any] | None
    """The object that was affected by the audit event."""
    associated_objects: list[Any] | None
    """Any associated objects related to the audit event."""
    author: dict[str, Any] | None
    """The user who triggered the audit event."""
    category: str | None
    """The category under which the audit event falls."""
    changed_values: list[Any] | None
    """Details of the values that were changed during the audit event."""
    creation_date: int | None
    """The date and time when the audit event was created."""
    description: str | None
    """A detailed description of the audit event."""
    remote_address: str | None
    """The IP address from which the audit event originated."""
    summary: str | None
    """A brief summary or title describing the audit event."""
    super_admin: bool | None
    """Indicates if the user triggering the audit event is a super admin."""
    sys_admin: bool | None
    """Indicates if the user triggering the audit event is a system admin."""


class AuditInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    affected_object: list[dict[str, Any]]
    """The object that was affected by the audit event."""
    associated_objects: list[list[Any]]
    """Any associated objects related to the audit event."""
    author: list[dict[str, Any]]
    """The user who triggered the audit event."""
    category: list[str]
    """The category under which the audit event falls."""
    changed_values: list[list[Any]]
    """Details of the values that were changed during the audit event."""
    creation_date: list[int]
    """The date and time when the audit event was created."""
    description: list[str]
    """A detailed description of the audit event."""
    remote_address: list[str]
    """The IP address from which the audit event originated."""
    summary: list[str]
    """A brief summary or title describing the audit event."""
    super_admin: list[bool]
    """Indicates if the user triggering the audit event is a super admin."""
    sys_admin: list[bool]
    """Indicates if the user triggering the audit event is a system admin."""


class AuditAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    affected_object: Any
    """The object that was affected by the audit event."""
    associated_objects: Any
    """Any associated objects related to the audit event."""
    author: Any
    """The user who triggered the audit event."""
    category: Any
    """The category under which the audit event falls."""
    changed_values: Any
    """Details of the values that were changed during the audit event."""
    creation_date: Any
    """The date and time when the audit event was created."""
    description: Any
    """A detailed description of the audit event."""
    remote_address: Any
    """The IP address from which the audit event originated."""
    summary: Any
    """A brief summary or title describing the audit event."""
    super_admin: Any
    """Indicates if the user triggering the audit event is a super admin."""
    sys_admin: Any
    """Indicates if the user triggering the audit event is a system admin."""


class AuditStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    affected_object: str
    """The object that was affected by the audit event."""
    associated_objects: str
    """Any associated objects related to the audit event."""
    author: str
    """The user who triggered the audit event."""
    category: str
    """The category under which the audit event falls."""
    changed_values: str
    """Details of the values that were changed during the audit event."""
    creation_date: str
    """The date and time when the audit event was created."""
    description: str
    """A detailed description of the audit event."""
    remote_address: str
    """The IP address from which the audit event originated."""
    summary: str
    """A brief summary or title describing the audit event."""
    super_admin: str
    """Indicates if the user triggering the audit event is a super admin."""
    sys_admin: str
    """Indicates if the user triggering the audit event is a system admin."""


class AuditSortFilter(TypedDict, total=False):
    """Available fields for sorting audit search results."""
    affected_object: AirbyteSortOrder
    """The object that was affected by the audit event."""
    associated_objects: AirbyteSortOrder
    """Any associated objects related to the audit event."""
    author: AirbyteSortOrder
    """The user who triggered the audit event."""
    category: AirbyteSortOrder
    """The category under which the audit event falls."""
    changed_values: AirbyteSortOrder
    """Details of the values that were changed during the audit event."""
    creation_date: AirbyteSortOrder
    """The date and time when the audit event was created."""
    description: AirbyteSortOrder
    """A detailed description of the audit event."""
    remote_address: AirbyteSortOrder
    """The IP address from which the audit event originated."""
    summary: AirbyteSortOrder
    """A brief summary or title describing the audit event."""
    super_admin: AirbyteSortOrder
    """Indicates if the user triggering the audit event is a super admin."""
    sys_admin: AirbyteSortOrder
    """Indicates if the user triggering the audit event is a system admin."""


# Entity-specific condition types for audit
class AuditEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AuditSearchFilter


class AuditNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AuditSearchFilter


class AuditGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AuditSearchFilter


class AuditGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AuditSearchFilter


class AuditLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AuditSearchFilter


class AuditLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AuditSearchFilter


class AuditLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AuditStringFilter


class AuditFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AuditStringFilter


class AuditKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AuditStringFilter


class AuditContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AuditAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AuditInCondition = TypedDict("AuditInCondition", {"in": AuditInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AuditNotCondition = TypedDict("AuditNotCondition", {"not": "AuditCondition"}, total=False)
"""Negates the nested condition."""

AuditAndCondition = TypedDict("AuditAndCondition", {"and": "list[AuditCondition]"}, total=False)
"""True if all nested conditions are true."""

AuditOrCondition = TypedDict("AuditOrCondition", {"or": "list[AuditCondition]"}, total=False)
"""True if any nested condition is true."""

AuditAnyCondition = TypedDict("AuditAnyCondition", {"any": AuditAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all audit condition types
AuditCondition = (
    AuditEqCondition
    | AuditNeqCondition
    | AuditGtCondition
    | AuditGteCondition
    | AuditLtCondition
    | AuditLteCondition
    | AuditInCondition
    | AuditLikeCondition
    | AuditFuzzyCondition
    | AuditKeywordCondition
    | AuditContainsCondition
    | AuditNotCondition
    | AuditAndCondition
    | AuditOrCondition
    | AuditAnyCondition
)


class AuditSearchQuery(TypedDict, total=False):
    """Search query for audit entity."""
    filter: AuditCondition
    sort: list[AuditSortFilter]


# ===== BLOG_POSTS SEARCH TYPES =====

class BlogPostsSearchFilter(TypedDict, total=False):
    """Available fields for filtering blog_posts search queries."""
    links: dict[str, Any] | None
    """Links related to the blog post"""
    author_id: str | None
    """ID of the user who created the blog post"""
    body: dict[str, Any] | None
    """Blog post body content"""
    created_at: str | None
    """Timestamp when the blog post was created"""
    id: str | None
    """Unique blog post identifier"""
    space_id: str | None
    """ID of the space containing this blog post"""
    status: str | None
    """Blog post status (current, draft, trashed)"""
    title: str | None
    """Blog post title"""
    version: dict[str, Any] | None
    """Version information"""


class BlogPostsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    links: list[dict[str, Any]]
    """Links related to the blog post"""
    author_id: list[str]
    """ID of the user who created the blog post"""
    body: list[dict[str, Any]]
    """Blog post body content"""
    created_at: list[str]
    """Timestamp when the blog post was created"""
    id: list[str]
    """Unique blog post identifier"""
    space_id: list[str]
    """ID of the space containing this blog post"""
    status: list[str]
    """Blog post status (current, draft, trashed)"""
    title: list[str]
    """Blog post title"""
    version: list[dict[str, Any]]
    """Version information"""


class BlogPostsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    links: Any
    """Links related to the blog post"""
    author_id: Any
    """ID of the user who created the blog post"""
    body: Any
    """Blog post body content"""
    created_at: Any
    """Timestamp when the blog post was created"""
    id: Any
    """Unique blog post identifier"""
    space_id: Any
    """ID of the space containing this blog post"""
    status: Any
    """Blog post status (current, draft, trashed)"""
    title: Any
    """Blog post title"""
    version: Any
    """Version information"""


class BlogPostsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    links: str
    """Links related to the blog post"""
    author_id: str
    """ID of the user who created the blog post"""
    body: str
    """Blog post body content"""
    created_at: str
    """Timestamp when the blog post was created"""
    id: str
    """Unique blog post identifier"""
    space_id: str
    """ID of the space containing this blog post"""
    status: str
    """Blog post status (current, draft, trashed)"""
    title: str
    """Blog post title"""
    version: str
    """Version information"""


class BlogPostsSortFilter(TypedDict, total=False):
    """Available fields for sorting blog_posts search results."""
    links: AirbyteSortOrder
    """Links related to the blog post"""
    author_id: AirbyteSortOrder
    """ID of the user who created the blog post"""
    body: AirbyteSortOrder
    """Blog post body content"""
    created_at: AirbyteSortOrder
    """Timestamp when the blog post was created"""
    id: AirbyteSortOrder
    """Unique blog post identifier"""
    space_id: AirbyteSortOrder
    """ID of the space containing this blog post"""
    status: AirbyteSortOrder
    """Blog post status (current, draft, trashed)"""
    title: AirbyteSortOrder
    """Blog post title"""
    version: AirbyteSortOrder
    """Version information"""


# Entity-specific condition types for blog_posts
class BlogPostsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BlogPostsSearchFilter


class BlogPostsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BlogPostsSearchFilter


class BlogPostsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BlogPostsSearchFilter


class BlogPostsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BlogPostsSearchFilter


class BlogPostsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BlogPostsSearchFilter


class BlogPostsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BlogPostsSearchFilter


class BlogPostsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BlogPostsStringFilter


class BlogPostsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BlogPostsStringFilter


class BlogPostsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BlogPostsStringFilter


class BlogPostsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BlogPostsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BlogPostsInCondition = TypedDict("BlogPostsInCondition", {"in": BlogPostsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BlogPostsNotCondition = TypedDict("BlogPostsNotCondition", {"not": "BlogPostsCondition"}, total=False)
"""Negates the nested condition."""

BlogPostsAndCondition = TypedDict("BlogPostsAndCondition", {"and": "list[BlogPostsCondition]"}, total=False)
"""True if all nested conditions are true."""

BlogPostsOrCondition = TypedDict("BlogPostsOrCondition", {"or": "list[BlogPostsCondition]"}, total=False)
"""True if any nested condition is true."""

BlogPostsAnyCondition = TypedDict("BlogPostsAnyCondition", {"any": BlogPostsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all blog_posts condition types
BlogPostsCondition = (
    BlogPostsEqCondition
    | BlogPostsNeqCondition
    | BlogPostsGtCondition
    | BlogPostsGteCondition
    | BlogPostsLtCondition
    | BlogPostsLteCondition
    | BlogPostsInCondition
    | BlogPostsLikeCondition
    | BlogPostsFuzzyCondition
    | BlogPostsKeywordCondition
    | BlogPostsContainsCondition
    | BlogPostsNotCondition
    | BlogPostsAndCondition
    | BlogPostsOrCondition
    | BlogPostsAnyCondition
)


class BlogPostsSearchQuery(TypedDict, total=False):
    """Search query for blog_posts entity."""
    filter: BlogPostsCondition
    sort: list[BlogPostsSortFilter]


# ===== GROUPS SEARCH TYPES =====

class GroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering groups search queries."""
    links: dict[str, Any] | None
    """Links related to the group"""
    id: str | None
    """The unique identifier of the group"""
    name: str | None
    """The name of the group"""
    type_: str | None
    """The type of group"""


class GroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    links: list[dict[str, Any]]
    """Links related to the group"""
    id: list[str]
    """The unique identifier of the group"""
    name: list[str]
    """The name of the group"""
    type_: list[str]
    """The type of group"""


class GroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    links: Any
    """Links related to the group"""
    id: Any
    """The unique identifier of the group"""
    name: Any
    """The name of the group"""
    type_: Any
    """The type of group"""


class GroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    links: str
    """Links related to the group"""
    id: str
    """The unique identifier of the group"""
    name: str
    """The name of the group"""
    type_: str
    """The type of group"""


class GroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting groups search results."""
    links: AirbyteSortOrder
    """Links related to the group"""
    id: AirbyteSortOrder
    """The unique identifier of the group"""
    name: AirbyteSortOrder
    """The name of the group"""
    type_: AirbyteSortOrder
    """The type of group"""


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


# ===== PAGES SEARCH TYPES =====

class PagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering pages search queries."""
    links: dict[str, Any] | None
    """Links related to the page"""
    author_id: str | None
    """ID of the user who created the page"""
    body: dict[str, Any] | None
    """Page body content"""
    created_at: str | None
    """Timestamp when the page was created"""
    id: str | None
    """Unique page identifier"""
    last_owner_id: str | None
    """ID of the previous page owner"""
    owner_id: str | None
    """ID of the current page owner"""
    parent_id: str | None
    """ID of the parent page"""
    parent_type: str | None
    """Type of the parent (page or space)"""
    position: int | None
    """Position of the page among siblings"""
    space_id: str | None
    """ID of the space containing this page"""
    status: str | None
    """Page status (current, archived, trashed, draft)"""
    title: str | None
    """Page title"""
    version: dict[str, Any] | None
    """Version information"""


class PagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    links: list[dict[str, Any]]
    """Links related to the page"""
    author_id: list[str]
    """ID of the user who created the page"""
    body: list[dict[str, Any]]
    """Page body content"""
    created_at: list[str]
    """Timestamp when the page was created"""
    id: list[str]
    """Unique page identifier"""
    last_owner_id: list[str]
    """ID of the previous page owner"""
    owner_id: list[str]
    """ID of the current page owner"""
    parent_id: list[str]
    """ID of the parent page"""
    parent_type: list[str]
    """Type of the parent (page or space)"""
    position: list[int]
    """Position of the page among siblings"""
    space_id: list[str]
    """ID of the space containing this page"""
    status: list[str]
    """Page status (current, archived, trashed, draft)"""
    title: list[str]
    """Page title"""
    version: list[dict[str, Any]]
    """Version information"""


class PagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    links: Any
    """Links related to the page"""
    author_id: Any
    """ID of the user who created the page"""
    body: Any
    """Page body content"""
    created_at: Any
    """Timestamp when the page was created"""
    id: Any
    """Unique page identifier"""
    last_owner_id: Any
    """ID of the previous page owner"""
    owner_id: Any
    """ID of the current page owner"""
    parent_id: Any
    """ID of the parent page"""
    parent_type: Any
    """Type of the parent (page or space)"""
    position: Any
    """Position of the page among siblings"""
    space_id: Any
    """ID of the space containing this page"""
    status: Any
    """Page status (current, archived, trashed, draft)"""
    title: Any
    """Page title"""
    version: Any
    """Version information"""


class PagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    links: str
    """Links related to the page"""
    author_id: str
    """ID of the user who created the page"""
    body: str
    """Page body content"""
    created_at: str
    """Timestamp when the page was created"""
    id: str
    """Unique page identifier"""
    last_owner_id: str
    """ID of the previous page owner"""
    owner_id: str
    """ID of the current page owner"""
    parent_id: str
    """ID of the parent page"""
    parent_type: str
    """Type of the parent (page or space)"""
    position: str
    """Position of the page among siblings"""
    space_id: str
    """ID of the space containing this page"""
    status: str
    """Page status (current, archived, trashed, draft)"""
    title: str
    """Page title"""
    version: str
    """Version information"""


class PagesSortFilter(TypedDict, total=False):
    """Available fields for sorting pages search results."""
    links: AirbyteSortOrder
    """Links related to the page"""
    author_id: AirbyteSortOrder
    """ID of the user who created the page"""
    body: AirbyteSortOrder
    """Page body content"""
    created_at: AirbyteSortOrder
    """Timestamp when the page was created"""
    id: AirbyteSortOrder
    """Unique page identifier"""
    last_owner_id: AirbyteSortOrder
    """ID of the previous page owner"""
    owner_id: AirbyteSortOrder
    """ID of the current page owner"""
    parent_id: AirbyteSortOrder
    """ID of the parent page"""
    parent_type: AirbyteSortOrder
    """Type of the parent (page or space)"""
    position: AirbyteSortOrder
    """Position of the page among siblings"""
    space_id: AirbyteSortOrder
    """ID of the space containing this page"""
    status: AirbyteSortOrder
    """Page status (current, archived, trashed, draft)"""
    title: AirbyteSortOrder
    """Page title"""
    version: AirbyteSortOrder
    """Version information"""


# Entity-specific condition types for pages
class PagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PagesSearchFilter


class PagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PagesSearchFilter


class PagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PagesSearchFilter


class PagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PagesSearchFilter


class PagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PagesSearchFilter


class PagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PagesSearchFilter


class PagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PagesStringFilter


class PagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PagesStringFilter


class PagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PagesStringFilter


class PagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PagesInCondition = TypedDict("PagesInCondition", {"in": PagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PagesNotCondition = TypedDict("PagesNotCondition", {"not": "PagesCondition"}, total=False)
"""Negates the nested condition."""

PagesAndCondition = TypedDict("PagesAndCondition", {"and": "list[PagesCondition]"}, total=False)
"""True if all nested conditions are true."""

PagesOrCondition = TypedDict("PagesOrCondition", {"or": "list[PagesCondition]"}, total=False)
"""True if any nested condition is true."""

PagesAnyCondition = TypedDict("PagesAnyCondition", {"any": PagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pages condition types
PagesCondition = (
    PagesEqCondition
    | PagesNeqCondition
    | PagesGtCondition
    | PagesGteCondition
    | PagesLtCondition
    | PagesLteCondition
    | PagesInCondition
    | PagesLikeCondition
    | PagesFuzzyCondition
    | PagesKeywordCondition
    | PagesContainsCondition
    | PagesNotCondition
    | PagesAndCondition
    | PagesOrCondition
    | PagesAnyCondition
)


class PagesSearchQuery(TypedDict, total=False):
    """Search query for pages entity."""
    filter: PagesCondition
    sort: list[PagesSortFilter]


# ===== SPACES SEARCH TYPES =====

class SpacesSearchFilter(TypedDict, total=False):
    """Available fields for filtering spaces search queries."""
    links: dict[str, Any] | None
    """Links related to the space"""
    author_id: str | None
    """ID of the user who created the space"""
    created_at: str | None
    """Timestamp when the space was created"""
    description: dict[str, Any] | None
    """Space description in various formats"""
    homepage_id: str | None
    """ID of the space homepage"""
    icon: dict[str, Any] | None
    """Space icon information"""
    id: str | None
    """Unique space identifier"""
    key: str | None
    """Space key"""
    name: str | None
    """Space name"""
    status: str | None
    """Space status (current or archived)"""
    type_: str | None
    """Space type (global or personal)"""


class SpacesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    links: list[dict[str, Any]]
    """Links related to the space"""
    author_id: list[str]
    """ID of the user who created the space"""
    created_at: list[str]
    """Timestamp when the space was created"""
    description: list[dict[str, Any]]
    """Space description in various formats"""
    homepage_id: list[str]
    """ID of the space homepage"""
    icon: list[dict[str, Any]]
    """Space icon information"""
    id: list[str]
    """Unique space identifier"""
    key: list[str]
    """Space key"""
    name: list[str]
    """Space name"""
    status: list[str]
    """Space status (current or archived)"""
    type_: list[str]
    """Space type (global or personal)"""


class SpacesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    links: Any
    """Links related to the space"""
    author_id: Any
    """ID of the user who created the space"""
    created_at: Any
    """Timestamp when the space was created"""
    description: Any
    """Space description in various formats"""
    homepage_id: Any
    """ID of the space homepage"""
    icon: Any
    """Space icon information"""
    id: Any
    """Unique space identifier"""
    key: Any
    """Space key"""
    name: Any
    """Space name"""
    status: Any
    """Space status (current or archived)"""
    type_: Any
    """Space type (global or personal)"""


class SpacesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    links: str
    """Links related to the space"""
    author_id: str
    """ID of the user who created the space"""
    created_at: str
    """Timestamp when the space was created"""
    description: str
    """Space description in various formats"""
    homepage_id: str
    """ID of the space homepage"""
    icon: str
    """Space icon information"""
    id: str
    """Unique space identifier"""
    key: str
    """Space key"""
    name: str
    """Space name"""
    status: str
    """Space status (current or archived)"""
    type_: str
    """Space type (global or personal)"""


class SpacesSortFilter(TypedDict, total=False):
    """Available fields for sorting spaces search results."""
    links: AirbyteSortOrder
    """Links related to the space"""
    author_id: AirbyteSortOrder
    """ID of the user who created the space"""
    created_at: AirbyteSortOrder
    """Timestamp when the space was created"""
    description: AirbyteSortOrder
    """Space description in various formats"""
    homepage_id: AirbyteSortOrder
    """ID of the space homepage"""
    icon: AirbyteSortOrder
    """Space icon information"""
    id: AirbyteSortOrder
    """Unique space identifier"""
    key: AirbyteSortOrder
    """Space key"""
    name: AirbyteSortOrder
    """Space name"""
    status: AirbyteSortOrder
    """Space status (current or archived)"""
    type_: AirbyteSortOrder
    """Space type (global or personal)"""


# Entity-specific condition types for spaces
class SpacesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SpacesSearchFilter


class SpacesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SpacesSearchFilter


class SpacesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SpacesSearchFilter


class SpacesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SpacesSearchFilter


class SpacesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SpacesSearchFilter


class SpacesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SpacesSearchFilter


class SpacesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SpacesStringFilter


class SpacesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SpacesStringFilter


class SpacesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SpacesStringFilter


class SpacesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SpacesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SpacesInCondition = TypedDict("SpacesInCondition", {"in": SpacesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SpacesNotCondition = TypedDict("SpacesNotCondition", {"not": "SpacesCondition"}, total=False)
"""Negates the nested condition."""

SpacesAndCondition = TypedDict("SpacesAndCondition", {"and": "list[SpacesCondition]"}, total=False)
"""True if all nested conditions are true."""

SpacesOrCondition = TypedDict("SpacesOrCondition", {"or": "list[SpacesCondition]"}, total=False)
"""True if any nested condition is true."""

SpacesAnyCondition = TypedDict("SpacesAnyCondition", {"any": SpacesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all spaces condition types
SpacesCondition = (
    SpacesEqCondition
    | SpacesNeqCondition
    | SpacesGtCondition
    | SpacesGteCondition
    | SpacesLtCondition
    | SpacesLteCondition
    | SpacesInCondition
    | SpacesLikeCondition
    | SpacesFuzzyCondition
    | SpacesKeywordCondition
    | SpacesContainsCondition
    | SpacesNotCondition
    | SpacesAndCondition
    | SpacesOrCondition
    | SpacesAnyCondition
)


class SpacesSearchQuery(TypedDict, total=False):
    """Search query for spaces entity."""
    filter: SpacesCondition
    sort: list[SpacesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
