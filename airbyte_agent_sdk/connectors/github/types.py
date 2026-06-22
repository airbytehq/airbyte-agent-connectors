"""
Type definitions for github connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class RepositoriesGetParams(TypedDict):
    """Parameters for repositories.get operation"""
    owner: str
    repo: str
    fields: NotRequired[list[str]]

class RepositoriesListParams(TypedDict):
    """Parameters for repositories.list operation"""
    username: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class RepositoriesApiSearchParams(TypedDict):
    """Parameters for repositories.api_search operation"""
    query: str
    limit: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class OrgRepositoriesListParams(TypedDict):
    """Parameters for org_repositories.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class BranchesListParams(TypedDict):
    """Parameters for branches.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class BranchesGetParams(TypedDict):
    """Parameters for branches.get operation"""
    owner: str
    repo: str
    branch: str
    fields: NotRequired[list[str]]

class CommitsListParams(TypedDict):
    """Parameters for commits.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    path: NotRequired[str]
    fields: NotRequired[list[str]]

class CommitsGetParams(TypedDict):
    """Parameters for commits.get operation"""
    owner: str
    repo: str
    sha: str
    fields: NotRequired[list[str]]

class ReleasesListParams(TypedDict):
    """Parameters for releases.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ReleasesGetParams(TypedDict):
    """Parameters for releases.get operation"""
    owner: str
    repo: str
    tag: str
    fields: NotRequired[list[str]]

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class IssuesApiSearchParams(TypedDict):
    """Parameters for issues.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class IssuesCreateParams(TypedDict):
    """Parameters for issues.create operation"""
    title: str
    body: NotRequired[str]
    labels: NotRequired[list[str]]
    assignees: NotRequired[list[str]]
    milestone: NotRequired[int | None]
    owner: str
    repo: str

class IssuesUpdateParams(TypedDict):
    """Parameters for issues.update operation"""
    title: NotRequired[str]
    body: NotRequired[str]
    state: NotRequired[str]
    state_reason: NotRequired[str | None]
    labels: NotRequired[list[str]]
    assignees: NotRequired[list[str]]
    milestone: NotRequired[int | None]
    owner: str
    repo: str
    issue_number: str

class CommentsCreateParams(TypedDict):
    """Parameters for comments.create operation"""
    body: str
    owner: str
    repo: str
    issue_number: str

class PullRequestsCreateParams(TypedDict):
    """Parameters for pull_requests.create operation"""
    title: str
    head: str
    base: str
    body: NotRequired[str]
    draft: NotRequired[bool]
    maintainer_can_modify: NotRequired[bool]
    owner: str
    repo: str

class PullRequestsListParams(TypedDict):
    """Parameters for pull_requests.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PullRequestsGetParams(TypedDict):
    """Parameters for pull_requests.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class PullRequestsApiSearchParams(TypedDict):
    """Parameters for pull_requests.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ReviewsListParams(TypedDict):
    """Parameters for reviews.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommentsGetParams(TypedDict):
    """Parameters for comments.get operation"""
    id: str
    fields: NotRequired[list[str]]

class PrCommentsListParams(TypedDict):
    """Parameters for pr_comments.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PrCommentsGetParams(TypedDict):
    """Parameters for pr_comments.get operation"""
    id: str
    fields: NotRequired[list[str]]

class LabelsListParams(TypedDict):
    """Parameters for labels.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class LabelsGetParams(TypedDict):
    """Parameters for labels.get operation"""
    owner: str
    repo: str
    name: str
    fields: NotRequired[list[str]]

class MilestonesListParams(TypedDict):
    """Parameters for milestones.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class MilestonesGetParams(TypedDict):
    """Parameters for milestones.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class OrganizationsGetParams(TypedDict):
    """Parameters for organizations.get operation"""
    org: str
    fields: NotRequired[list[str]]

class OrganizationsListParams(TypedDict):
    """Parameters for organizations.list operation"""
    username: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    username: str
    fields: NotRequired[list[str]]

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class UsersApiSearchParams(TypedDict):
    """Parameters for users.api_search operation"""
    query: str
    limit: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    org: str
    team_slug: str
    fields: NotRequired[list[str]]

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    owner: str
    repo: str
    tag: str
    fields: NotRequired[list[str]]

class StargazersListParams(TypedDict):
    """Parameters for stargazers.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ViewerGetParams(TypedDict):
    """Parameters for viewer.get operation"""
    fields: NotRequired[list[str]]

class ViewerRepositoriesListParams(TypedDict):
    """Parameters for viewer_repositories.list operation"""
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    org: str
    project_number: int
    fields: NotRequired[list[str]]

class ProjectItemsListParams(TypedDict):
    """Parameters for project_items.list operation"""
    org: str
    project_number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class DiscussionsListParams(TypedDict):
    """Parameters for discussions.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    answered: NotRequired[bool]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class DiscussionsGetParams(TypedDict):
    """Parameters for discussions.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class DiscussionsApiSearchParams(TypedDict):
    """Parameters for discussions.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class FileContentGetParams(TypedDict):
    """Parameters for file_content.get operation"""
    owner: str
    repo: str
    path: str
    ref: NotRequired[str]
    fields: NotRequired[list[str]]

class DirectoryContentListParams(TypedDict):
    """Parameters for directory_content.list operation"""
    owner: str
    repo: str
    path: str
    ref: NotRequired[str]
    fields: NotRequired[list[str]]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== BRANCHES SEARCH TYPES =====

class BranchesSearchFilter(TypedDict, total=False):
    """Available fields for filtering branches search queries."""
    name: str | None
    """Branch name (e.g. `main`, `feature/foo`)"""


class BranchesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Branch name (e.g. `main`, `feature/foo`)"""


class BranchesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Branch name (e.g. `main`, `feature/foo`)"""


class BranchesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Branch name (e.g. `main`, `feature/foo`)"""


class BranchesSortFilter(TypedDict, total=False):
    """Available fields for sorting branches search results."""
    name: AirbyteSortOrder
    """Branch name (e.g. `main`, `feature/foo`)"""


# Entity-specific condition types for branches
class BranchesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BranchesSearchFilter


class BranchesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BranchesSearchFilter


class BranchesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BranchesSearchFilter


class BranchesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BranchesSearchFilter


class BranchesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BranchesSearchFilter


class BranchesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BranchesSearchFilter


class BranchesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BranchesStringFilter


class BranchesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BranchesStringFilter


class BranchesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BranchesStringFilter


class BranchesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BranchesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BranchesInCondition = TypedDict("BranchesInCondition", {"in": BranchesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BranchesNotCondition = TypedDict("BranchesNotCondition", {"not": "BranchesCondition"}, total=False)
"""Negates the nested condition."""

BranchesAndCondition = TypedDict("BranchesAndCondition", {"and": "list[BranchesCondition]"}, total=False)
"""True if all nested conditions are true."""

BranchesOrCondition = TypedDict("BranchesOrCondition", {"or": "list[BranchesCondition]"}, total=False)
"""True if any nested condition is true."""

BranchesAnyCondition = TypedDict("BranchesAnyCondition", {"any": BranchesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all branches condition types
BranchesCondition = (
    BranchesEqCondition
    | BranchesNeqCondition
    | BranchesGtCondition
    | BranchesGteCondition
    | BranchesLtCondition
    | BranchesLteCondition
    | BranchesInCondition
    | BranchesLikeCondition
    | BranchesFuzzyCondition
    | BranchesKeywordCondition
    | BranchesContainsCondition
    | BranchesNotCondition
    | BranchesAndCondition
    | BranchesOrCondition
    | BranchesAnyCondition
)


class BranchesSearchQuery(TypedDict, total=False):
    """Search query for branches entity."""
    filter: BranchesCondition
    sort: list[BranchesSortFilter]


# ===== COMMENTS SEARCH TYPES =====

class CommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering comments search queries."""
    id: str | None
    """GraphQL node ID of the comment"""
    database_id: int | None
    """REST API numeric identifier for the comment"""
    body: str | None
    """Markdown body of the comment"""
    created_at: str | None
    """ISO 8601 timestamp when the comment was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the comment was last updated"""
    url: str | None
    """Permalink to the comment on GitHub"""


class CommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the comment"""
    database_id: list[int]
    """REST API numeric identifier for the comment"""
    body: list[str]
    """Markdown body of the comment"""
    created_at: list[str]
    """ISO 8601 timestamp when the comment was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the comment was last updated"""
    url: list[str]
    """Permalink to the comment on GitHub"""


class CommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the comment"""
    database_id: Any
    """REST API numeric identifier for the comment"""
    body: Any
    """Markdown body of the comment"""
    created_at: Any
    """ISO 8601 timestamp when the comment was created"""
    updated_at: Any
    """ISO 8601 timestamp when the comment was last updated"""
    url: Any
    """Permalink to the comment on GitHub"""


class CommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the comment"""
    database_id: str
    """REST API numeric identifier for the comment"""
    body: str
    """Markdown body of the comment"""
    created_at: str
    """ISO 8601 timestamp when the comment was created"""
    updated_at: str
    """ISO 8601 timestamp when the comment was last updated"""
    url: str
    """Permalink to the comment on GitHub"""


class CommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting comments search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the comment"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the comment"""
    body: AirbyteSortOrder
    """Markdown body of the comment"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the comment was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the comment was last updated"""
    url: AirbyteSortOrder
    """Permalink to the comment on GitHub"""


# Entity-specific condition types for comments
class CommentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CommentsSearchFilter


class CommentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CommentsSearchFilter


class CommentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CommentsSearchFilter


class CommentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CommentsSearchFilter


class CommentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CommentsSearchFilter


class CommentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CommentsSearchFilter


class CommentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CommentsStringFilter


class CommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CommentsStringFilter


class CommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CommentsStringFilter


class CommentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CommentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CommentsInCondition = TypedDict("CommentsInCondition", {"in": CommentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CommentsNotCondition = TypedDict("CommentsNotCondition", {"not": "CommentsCondition"}, total=False)
"""Negates the nested condition."""

CommentsAndCondition = TypedDict("CommentsAndCondition", {"and": "list[CommentsCondition]"}, total=False)
"""True if all nested conditions are true."""

CommentsOrCondition = TypedDict("CommentsOrCondition", {"or": "list[CommentsCondition]"}, total=False)
"""True if any nested condition is true."""

CommentsAnyCondition = TypedDict("CommentsAnyCondition", {"any": CommentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all comments condition types
CommentsCondition = (
    CommentsEqCondition
    | CommentsNeqCondition
    | CommentsGtCondition
    | CommentsGteCondition
    | CommentsLtCondition
    | CommentsLteCondition
    | CommentsInCondition
    | CommentsLikeCondition
    | CommentsFuzzyCondition
    | CommentsKeywordCondition
    | CommentsContainsCondition
    | CommentsNotCondition
    | CommentsAndCondition
    | CommentsOrCondition
    | CommentsAnyCondition
)


class CommentsSearchQuery(TypedDict, total=False):
    """Search query for comments entity."""
    filter: CommentsCondition
    sort: list[CommentsSortFilter]


# ===== COMMITS SEARCH TYPES =====

class CommitsSearchFilter(TypedDict, total=False):
    """Available fields for filtering commits search queries."""
    sha: str | None
    """Full Git commit SHA"""
    url: str | None
    """Permalink to the commit on GitHub"""
    created_at: str | None
    """ISO 8601 timestamp of the commit"""


class CommitsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    sha: list[str]
    """Full Git commit SHA"""
    url: list[str]
    """Permalink to the commit on GitHub"""
    created_at: list[str]
    """ISO 8601 timestamp of the commit"""


class CommitsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    sha: Any
    """Full Git commit SHA"""
    url: Any
    """Permalink to the commit on GitHub"""
    created_at: Any
    """ISO 8601 timestamp of the commit"""


class CommitsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    sha: str
    """Full Git commit SHA"""
    url: str
    """Permalink to the commit on GitHub"""
    created_at: str
    """ISO 8601 timestamp of the commit"""


class CommitsSortFilter(TypedDict, total=False):
    """Available fields for sorting commits search results."""
    sha: AirbyteSortOrder
    """Full Git commit SHA"""
    url: AirbyteSortOrder
    """Permalink to the commit on GitHub"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp of the commit"""


# Entity-specific condition types for commits
class CommitsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CommitsSearchFilter


class CommitsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CommitsSearchFilter


class CommitsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CommitsSearchFilter


class CommitsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CommitsSearchFilter


class CommitsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CommitsSearchFilter


class CommitsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CommitsSearchFilter


class CommitsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CommitsStringFilter


class CommitsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CommitsStringFilter


class CommitsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CommitsStringFilter


class CommitsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CommitsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CommitsInCondition = TypedDict("CommitsInCondition", {"in": CommitsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CommitsNotCondition = TypedDict("CommitsNotCondition", {"not": "CommitsCondition"}, total=False)
"""Negates the nested condition."""

CommitsAndCondition = TypedDict("CommitsAndCondition", {"and": "list[CommitsCondition]"}, total=False)
"""True if all nested conditions are true."""

CommitsOrCondition = TypedDict("CommitsOrCondition", {"or": "list[CommitsCondition]"}, total=False)
"""True if any nested condition is true."""

CommitsAnyCondition = TypedDict("CommitsAnyCondition", {"any": CommitsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all commits condition types
CommitsCondition = (
    CommitsEqCondition
    | CommitsNeqCondition
    | CommitsGtCondition
    | CommitsGteCondition
    | CommitsLtCondition
    | CommitsLteCondition
    | CommitsInCondition
    | CommitsLikeCondition
    | CommitsFuzzyCondition
    | CommitsKeywordCondition
    | CommitsContainsCondition
    | CommitsNotCondition
    | CommitsAndCondition
    | CommitsOrCondition
    | CommitsAnyCondition
)


class CommitsSearchQuery(TypedDict, total=False):
    """Search query for commits entity."""
    filter: CommitsCondition
    sort: list[CommitsSortFilter]


# ===== DIRECTORY_CONTENT SEARCH TYPES =====

class DirectoryContentSearchFilter(TypedDict, total=False):
    """Available fields for filtering directory_content search queries."""


class DirectoryContentInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class DirectoryContentAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class DirectoryContentStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class DirectoryContentSortFilter(TypedDict, total=False):
    """Available fields for sorting directory_content search results."""


# Entity-specific condition types for directory_content
class DirectoryContentEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DirectoryContentSearchFilter


class DirectoryContentNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DirectoryContentSearchFilter


class DirectoryContentGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DirectoryContentSearchFilter


class DirectoryContentGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DirectoryContentSearchFilter


class DirectoryContentLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DirectoryContentSearchFilter


class DirectoryContentLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DirectoryContentSearchFilter


class DirectoryContentLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DirectoryContentStringFilter


class DirectoryContentFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DirectoryContentStringFilter


class DirectoryContentKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DirectoryContentStringFilter


class DirectoryContentContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DirectoryContentAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DirectoryContentInCondition = TypedDict("DirectoryContentInCondition", {"in": DirectoryContentInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DirectoryContentNotCondition = TypedDict("DirectoryContentNotCondition", {"not": "DirectoryContentCondition"}, total=False)
"""Negates the nested condition."""

DirectoryContentAndCondition = TypedDict("DirectoryContentAndCondition", {"and": "list[DirectoryContentCondition]"}, total=False)
"""True if all nested conditions are true."""

DirectoryContentOrCondition = TypedDict("DirectoryContentOrCondition", {"or": "list[DirectoryContentCondition]"}, total=False)
"""True if any nested condition is true."""

DirectoryContentAnyCondition = TypedDict("DirectoryContentAnyCondition", {"any": DirectoryContentAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all directory_content condition types
DirectoryContentCondition = (
    DirectoryContentEqCondition
    | DirectoryContentNeqCondition
    | DirectoryContentGtCondition
    | DirectoryContentGteCondition
    | DirectoryContentLtCondition
    | DirectoryContentLteCondition
    | DirectoryContentInCondition
    | DirectoryContentLikeCondition
    | DirectoryContentFuzzyCondition
    | DirectoryContentKeywordCondition
    | DirectoryContentContainsCondition
    | DirectoryContentNotCondition
    | DirectoryContentAndCondition
    | DirectoryContentOrCondition
    | DirectoryContentAnyCondition
)


class DirectoryContentSearchQuery(TypedDict, total=False):
    """Search query for directory_content entity."""
    filter: DirectoryContentCondition
    sort: list[DirectoryContentSortFilter]


# ===== DISCUSSIONS SEARCH TYPES =====

class DiscussionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering discussions search queries."""


class DiscussionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class DiscussionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class DiscussionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class DiscussionsSortFilter(TypedDict, total=False):
    """Available fields for sorting discussions search results."""


# Entity-specific condition types for discussions
class DiscussionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DiscussionsSearchFilter


class DiscussionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DiscussionsSearchFilter


class DiscussionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DiscussionsSearchFilter


class DiscussionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DiscussionsSearchFilter


class DiscussionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DiscussionsSearchFilter


class DiscussionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DiscussionsSearchFilter


class DiscussionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DiscussionsStringFilter


class DiscussionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DiscussionsStringFilter


class DiscussionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DiscussionsStringFilter


class DiscussionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DiscussionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DiscussionsInCondition = TypedDict("DiscussionsInCondition", {"in": DiscussionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DiscussionsNotCondition = TypedDict("DiscussionsNotCondition", {"not": "DiscussionsCondition"}, total=False)
"""Negates the nested condition."""

DiscussionsAndCondition = TypedDict("DiscussionsAndCondition", {"and": "list[DiscussionsCondition]"}, total=False)
"""True if all nested conditions are true."""

DiscussionsOrCondition = TypedDict("DiscussionsOrCondition", {"or": "list[DiscussionsCondition]"}, total=False)
"""True if any nested condition is true."""

DiscussionsAnyCondition = TypedDict("DiscussionsAnyCondition", {"any": DiscussionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all discussions condition types
DiscussionsCondition = (
    DiscussionsEqCondition
    | DiscussionsNeqCondition
    | DiscussionsGtCondition
    | DiscussionsGteCondition
    | DiscussionsLtCondition
    | DiscussionsLteCondition
    | DiscussionsInCondition
    | DiscussionsLikeCondition
    | DiscussionsFuzzyCondition
    | DiscussionsKeywordCondition
    | DiscussionsContainsCondition
    | DiscussionsNotCondition
    | DiscussionsAndCondition
    | DiscussionsOrCondition
    | DiscussionsAnyCondition
)


class DiscussionsSearchQuery(TypedDict, total=False):
    """Search query for discussions entity."""
    filter: DiscussionsCondition
    sort: list[DiscussionsSortFilter]


# ===== FILE_CONTENT SEARCH TYPES =====

class FileContentSearchFilter(TypedDict, total=False):
    """Available fields for filtering file_content search queries."""


class FileContentInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class FileContentAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class FileContentStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class FileContentSortFilter(TypedDict, total=False):
    """Available fields for sorting file_content search results."""


# Entity-specific condition types for file_content
class FileContentEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FileContentSearchFilter


class FileContentNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FileContentSearchFilter


class FileContentGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FileContentSearchFilter


class FileContentGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FileContentSearchFilter


class FileContentLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FileContentSearchFilter


class FileContentLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FileContentSearchFilter


class FileContentLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FileContentStringFilter


class FileContentFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FileContentStringFilter


class FileContentKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FileContentStringFilter


class FileContentContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FileContentAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FileContentInCondition = TypedDict("FileContentInCondition", {"in": FileContentInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FileContentNotCondition = TypedDict("FileContentNotCondition", {"not": "FileContentCondition"}, total=False)
"""Negates the nested condition."""

FileContentAndCondition = TypedDict("FileContentAndCondition", {"and": "list[FileContentCondition]"}, total=False)
"""True if all nested conditions are true."""

FileContentOrCondition = TypedDict("FileContentOrCondition", {"or": "list[FileContentCondition]"}, total=False)
"""True if any nested condition is true."""

FileContentAnyCondition = TypedDict("FileContentAnyCondition", {"any": FileContentAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all file_content condition types
FileContentCondition = (
    FileContentEqCondition
    | FileContentNeqCondition
    | FileContentGtCondition
    | FileContentGteCondition
    | FileContentLtCondition
    | FileContentLteCondition
    | FileContentInCondition
    | FileContentLikeCondition
    | FileContentFuzzyCondition
    | FileContentKeywordCondition
    | FileContentContainsCondition
    | FileContentNotCondition
    | FileContentAndCondition
    | FileContentOrCondition
    | FileContentAnyCondition
)


class FileContentSearchQuery(TypedDict, total=False):
    """Search query for file_content entity."""
    filter: FileContentCondition
    sort: list[FileContentSortFilter]


# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    id: str | None
    """GraphQL node ID of the issue"""
    database_id: int | None
    """REST API numeric identifier for the issue"""
    number: int | None
    """Repository-scoped issue number"""
    title: str | None
    """Issue title"""
    state: str | None
    """Issue state in the cache: lowercase `open` or `closed`"""
    state_reason: str | None
    """Reason the issue is in its current state (e.g. `completed`, `not_planned`, `reopened`). Cached values are lowercase."""
    created_at: str | None
    """ISO 8601 timestamp when the issue was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: str | None
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: bool | None
    """Whether the conversation on the issue is locked"""
    url: str | None
    """Permalink to the issue on GitHub"""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the issue"""
    database_id: list[int]
    """REST API numeric identifier for the issue"""
    number: list[int]
    """Repository-scoped issue number"""
    title: list[str]
    """Issue title"""
    state: list[str]
    """Issue state in the cache: lowercase `open` or `closed`"""
    state_reason: list[str]
    """Reason the issue is in its current state (e.g. `completed`, `not_planned`, `reopened`). Cached values are lowercase."""
    created_at: list[str]
    """ISO 8601 timestamp when the issue was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: list[str]
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: list[bool]
    """Whether the conversation on the issue is locked"""
    url: list[str]
    """Permalink to the issue on GitHub"""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the issue"""
    database_id: Any
    """REST API numeric identifier for the issue"""
    number: Any
    """Repository-scoped issue number"""
    title: Any
    """Issue title"""
    state: Any
    """Issue state in the cache: lowercase `open` or `closed`"""
    state_reason: Any
    """Reason the issue is in its current state (e.g. `completed`, `not_planned`, `reopened`). Cached values are lowercase."""
    created_at: Any
    """ISO 8601 timestamp when the issue was created"""
    updated_at: Any
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: Any
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: Any
    """Whether the conversation on the issue is locked"""
    url: Any
    """Permalink to the issue on GitHub"""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the issue"""
    database_id: str
    """REST API numeric identifier for the issue"""
    number: str
    """Repository-scoped issue number"""
    title: str
    """Issue title"""
    state: str
    """Issue state in the cache: lowercase `open` or `closed`"""
    state_reason: str
    """Reason the issue is in its current state (e.g. `completed`, `not_planned`, `reopened`). Cached values are lowercase."""
    created_at: str
    """ISO 8601 timestamp when the issue was created"""
    updated_at: str
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: str
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: str
    """Whether the conversation on the issue is locked"""
    url: str
    """Permalink to the issue on GitHub"""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the issue"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the issue"""
    number: AirbyteSortOrder
    """Repository-scoped issue number"""
    title: AirbyteSortOrder
    """Issue title"""
    state: AirbyteSortOrder
    """Issue state in the cache: lowercase `open` or `closed`"""
    state_reason: AirbyteSortOrder
    """Reason the issue is in its current state (e.g. `completed`, `not_planned`, `reopened`). Cached values are lowercase."""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the issue was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: AirbyteSortOrder
    """Whether the conversation on the issue is locked"""
    url: AirbyteSortOrder
    """Permalink to the issue on GitHub"""


# Entity-specific condition types for issues
class IssuesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssuesSearchFilter


class IssuesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssuesSearchFilter


class IssuesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssuesSearchFilter


class IssuesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssuesSearchFilter


class IssuesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssuesSearchFilter


class IssuesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssuesSearchFilter


class IssuesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssuesStringFilter


class IssuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssuesStringFilter


class IssuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssuesStringFilter


class IssuesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssuesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssuesInCondition = TypedDict("IssuesInCondition", {"in": IssuesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssuesNotCondition = TypedDict("IssuesNotCondition", {"not": "IssuesCondition"}, total=False)
"""Negates the nested condition."""

IssuesAndCondition = TypedDict("IssuesAndCondition", {"and": "list[IssuesCondition]"}, total=False)
"""True if all nested conditions are true."""

IssuesOrCondition = TypedDict("IssuesOrCondition", {"or": "list[IssuesCondition]"}, total=False)
"""True if any nested condition is true."""

IssuesAnyCondition = TypedDict("IssuesAnyCondition", {"any": IssuesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issues condition types
IssuesCondition = (
    IssuesEqCondition
    | IssuesNeqCondition
    | IssuesGtCondition
    | IssuesGteCondition
    | IssuesLtCondition
    | IssuesLteCondition
    | IssuesInCondition
    | IssuesLikeCondition
    | IssuesFuzzyCondition
    | IssuesKeywordCondition
    | IssuesContainsCondition
    | IssuesNotCondition
    | IssuesAndCondition
    | IssuesOrCondition
    | IssuesAnyCondition
)


class IssuesSearchQuery(TypedDict, total=False):
    """Search query for issues entity."""
    filter: IssuesCondition
    sort: list[IssuesSortFilter]


# ===== LABELS SEARCH TYPES =====

class LabelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering labels search queries."""
    id: str | None
    """GraphQL node ID of the label"""
    name: str | None
    """Label name"""
    color: str | None
    """Label color as a 6-character hex string without a leading `#`"""
    description: str | None
    """Short description of what the label is used for"""
    url: str | None
    """API URL to the label resource"""


class LabelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the label"""
    name: list[str]
    """Label name"""
    color: list[str]
    """Label color as a 6-character hex string without a leading `#`"""
    description: list[str]
    """Short description of what the label is used for"""
    url: list[str]
    """API URL to the label resource"""


class LabelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the label"""
    name: Any
    """Label name"""
    color: Any
    """Label color as a 6-character hex string without a leading `#`"""
    description: Any
    """Short description of what the label is used for"""
    url: Any
    """API URL to the label resource"""


class LabelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the label"""
    name: str
    """Label name"""
    color: str
    """Label color as a 6-character hex string without a leading `#`"""
    description: str
    """Short description of what the label is used for"""
    url: str
    """API URL to the label resource"""


class LabelsSortFilter(TypedDict, total=False):
    """Available fields for sorting labels search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the label"""
    name: AirbyteSortOrder
    """Label name"""
    color: AirbyteSortOrder
    """Label color as a 6-character hex string without a leading `#`"""
    description: AirbyteSortOrder
    """Short description of what the label is used for"""
    url: AirbyteSortOrder
    """API URL to the label resource"""


# Entity-specific condition types for labels
class LabelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LabelsSearchFilter


class LabelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LabelsSearchFilter


class LabelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LabelsSearchFilter


class LabelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LabelsSearchFilter


class LabelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LabelsSearchFilter


class LabelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LabelsSearchFilter


class LabelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LabelsStringFilter


class LabelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LabelsStringFilter


class LabelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LabelsStringFilter


class LabelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LabelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LabelsInCondition = TypedDict("LabelsInCondition", {"in": LabelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LabelsNotCondition = TypedDict("LabelsNotCondition", {"not": "LabelsCondition"}, total=False)
"""Negates the nested condition."""

LabelsAndCondition = TypedDict("LabelsAndCondition", {"and": "list[LabelsCondition]"}, total=False)
"""True if all nested conditions are true."""

LabelsOrCondition = TypedDict("LabelsOrCondition", {"or": "list[LabelsCondition]"}, total=False)
"""True if any nested condition is true."""

LabelsAnyCondition = TypedDict("LabelsAnyCondition", {"any": LabelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all labels condition types
LabelsCondition = (
    LabelsEqCondition
    | LabelsNeqCondition
    | LabelsGtCondition
    | LabelsGteCondition
    | LabelsLtCondition
    | LabelsLteCondition
    | LabelsInCondition
    | LabelsLikeCondition
    | LabelsFuzzyCondition
    | LabelsKeywordCondition
    | LabelsContainsCondition
    | LabelsNotCondition
    | LabelsAndCondition
    | LabelsOrCondition
    | LabelsAnyCondition
)


class LabelsSearchQuery(TypedDict, total=False):
    """Search query for labels entity."""
    filter: LabelsCondition
    sort: list[LabelsSortFilter]


# ===== MILESTONES SEARCH TYPES =====

class MilestonesSearchFilter(TypedDict, total=False):
    """Available fields for filtering milestones search queries."""
    id: str | None
    """GraphQL node ID of the milestone"""
    number: int | None
    """Repository-scoped milestone number"""
    title: str | None
    """Milestone title"""
    description: str | None
    """Milestone description"""
    state: str | None
    """Milestone state in the cache: lowercase `open` or `closed`"""
    due_on: str | None
    """ISO 8601 timestamp for the milestone's due date, if set"""
    closed_at: str | None
    """ISO 8601 timestamp when the milestone was closed, if applicable"""
    created_at: str | None
    """ISO 8601 timestamp when the milestone was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the milestone was last updated"""


class MilestonesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the milestone"""
    number: list[int]
    """Repository-scoped milestone number"""
    title: list[str]
    """Milestone title"""
    description: list[str]
    """Milestone description"""
    state: list[str]
    """Milestone state in the cache: lowercase `open` or `closed`"""
    due_on: list[str]
    """ISO 8601 timestamp for the milestone's due date, if set"""
    closed_at: list[str]
    """ISO 8601 timestamp when the milestone was closed, if applicable"""
    created_at: list[str]
    """ISO 8601 timestamp when the milestone was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the milestone was last updated"""


class MilestonesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the milestone"""
    number: Any
    """Repository-scoped milestone number"""
    title: Any
    """Milestone title"""
    description: Any
    """Milestone description"""
    state: Any
    """Milestone state in the cache: lowercase `open` or `closed`"""
    due_on: Any
    """ISO 8601 timestamp for the milestone's due date, if set"""
    closed_at: Any
    """ISO 8601 timestamp when the milestone was closed, if applicable"""
    created_at: Any
    """ISO 8601 timestamp when the milestone was created"""
    updated_at: Any
    """ISO 8601 timestamp when the milestone was last updated"""


class MilestonesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the milestone"""
    number: str
    """Repository-scoped milestone number"""
    title: str
    """Milestone title"""
    description: str
    """Milestone description"""
    state: str
    """Milestone state in the cache: lowercase `open` or `closed`"""
    due_on: str
    """ISO 8601 timestamp for the milestone's due date, if set"""
    closed_at: str
    """ISO 8601 timestamp when the milestone was closed, if applicable"""
    created_at: str
    """ISO 8601 timestamp when the milestone was created"""
    updated_at: str
    """ISO 8601 timestamp when the milestone was last updated"""


class MilestonesSortFilter(TypedDict, total=False):
    """Available fields for sorting milestones search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the milestone"""
    number: AirbyteSortOrder
    """Repository-scoped milestone number"""
    title: AirbyteSortOrder
    """Milestone title"""
    description: AirbyteSortOrder
    """Milestone description"""
    state: AirbyteSortOrder
    """Milestone state in the cache: lowercase `open` or `closed`"""
    due_on: AirbyteSortOrder
    """ISO 8601 timestamp for the milestone's due date, if set"""
    closed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the milestone was closed, if applicable"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the milestone was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the milestone was last updated"""


# Entity-specific condition types for milestones
class MilestonesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MilestonesSearchFilter


class MilestonesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MilestonesSearchFilter


class MilestonesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MilestonesSearchFilter


class MilestonesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MilestonesSearchFilter


class MilestonesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MilestonesSearchFilter


class MilestonesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MilestonesSearchFilter


class MilestonesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MilestonesStringFilter


class MilestonesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MilestonesStringFilter


class MilestonesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MilestonesStringFilter


class MilestonesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MilestonesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MilestonesInCondition = TypedDict("MilestonesInCondition", {"in": MilestonesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MilestonesNotCondition = TypedDict("MilestonesNotCondition", {"not": "MilestonesCondition"}, total=False)
"""Negates the nested condition."""

MilestonesAndCondition = TypedDict("MilestonesAndCondition", {"and": "list[MilestonesCondition]"}, total=False)
"""True if all nested conditions are true."""

MilestonesOrCondition = TypedDict("MilestonesOrCondition", {"or": "list[MilestonesCondition]"}, total=False)
"""True if any nested condition is true."""

MilestonesAnyCondition = TypedDict("MilestonesAnyCondition", {"any": MilestonesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all milestones condition types
MilestonesCondition = (
    MilestonesEqCondition
    | MilestonesNeqCondition
    | MilestonesGtCondition
    | MilestonesGteCondition
    | MilestonesLtCondition
    | MilestonesLteCondition
    | MilestonesInCondition
    | MilestonesLikeCondition
    | MilestonesFuzzyCondition
    | MilestonesKeywordCondition
    | MilestonesContainsCondition
    | MilestonesNotCondition
    | MilestonesAndCondition
    | MilestonesOrCondition
    | MilestonesAnyCondition
)


class MilestonesSearchQuery(TypedDict, total=False):
    """Search query for milestones entity."""
    filter: MilestonesCondition
    sort: list[MilestonesSortFilter]


# ===== ORGANIZATIONS SEARCH TYPES =====

class OrganizationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering organizations search queries."""
    id: str | None
    """GraphQL node ID of the organization"""
    database_id: int | None
    """REST API numeric identifier for the organization"""
    login: str | None
    """Organization login/handle (unique URL slug)"""
    name: str | None
    """Display name of the organization"""
    description: str | None
    """Short public description of the organization"""
    email: str | None
    """Public contact email for the organization, if set"""
    location: str | None
    """Public location of the organization, if set"""
    is_verified: bool | None
    """Whether the organization has a verified domain"""
    created_at: str | None
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the organization"""
    database_id: list[int]
    """REST API numeric identifier for the organization"""
    login: list[str]
    """Organization login/handle (unique URL slug)"""
    name: list[str]
    """Display name of the organization"""
    description: list[str]
    """Short public description of the organization"""
    email: list[str]
    """Public contact email for the organization, if set"""
    location: list[str]
    """Public location of the organization, if set"""
    is_verified: list[bool]
    """Whether the organization has a verified domain"""
    created_at: list[str]
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the organization"""
    database_id: Any
    """REST API numeric identifier for the organization"""
    login: Any
    """Organization login/handle (unique URL slug)"""
    name: Any
    """Display name of the organization"""
    description: Any
    """Short public description of the organization"""
    email: Any
    """Public contact email for the organization, if set"""
    location: Any
    """Public location of the organization, if set"""
    is_verified: Any
    """Whether the organization has a verified domain"""
    created_at: Any
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the organization"""
    database_id: str
    """REST API numeric identifier for the organization"""
    login: str
    """Organization login/handle (unique URL slug)"""
    name: str
    """Display name of the organization"""
    description: str
    """Short public description of the organization"""
    email: str
    """Public contact email for the organization, if set"""
    location: str
    """Public location of the organization, if set"""
    is_verified: str
    """Whether the organization has a verified domain"""
    created_at: str
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsSortFilter(TypedDict, total=False):
    """Available fields for sorting organizations search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the organization"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the organization"""
    login: AirbyteSortOrder
    """Organization login/handle (unique URL slug)"""
    name: AirbyteSortOrder
    """Display name of the organization"""
    description: AirbyteSortOrder
    """Short public description of the organization"""
    email: AirbyteSortOrder
    """Public contact email for the organization, if set"""
    location: AirbyteSortOrder
    """Public location of the organization, if set"""
    is_verified: AirbyteSortOrder
    """Whether the organization has a verified domain"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the organization was created"""


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


# ===== ORG_REPOSITORIES SEARCH TYPES =====

class OrgRepositoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering org_repositories search queries."""


class OrgRepositoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class OrgRepositoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class OrgRepositoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class OrgRepositoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting org_repositories search results."""


# Entity-specific condition types for org_repositories
class OrgRepositoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrgRepositoriesSearchFilter


class OrgRepositoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrgRepositoriesSearchFilter


class OrgRepositoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrgRepositoriesSearchFilter


class OrgRepositoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrgRepositoriesSearchFilter


class OrgRepositoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrgRepositoriesSearchFilter


class OrgRepositoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrgRepositoriesSearchFilter


class OrgRepositoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrgRepositoriesStringFilter


class OrgRepositoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrgRepositoriesStringFilter


class OrgRepositoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrgRepositoriesStringFilter


class OrgRepositoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrgRepositoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrgRepositoriesInCondition = TypedDict("OrgRepositoriesInCondition", {"in": OrgRepositoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrgRepositoriesNotCondition = TypedDict("OrgRepositoriesNotCondition", {"not": "OrgRepositoriesCondition"}, total=False)
"""Negates the nested condition."""

OrgRepositoriesAndCondition = TypedDict("OrgRepositoriesAndCondition", {"and": "list[OrgRepositoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

OrgRepositoriesOrCondition = TypedDict("OrgRepositoriesOrCondition", {"or": "list[OrgRepositoriesCondition]"}, total=False)
"""True if any nested condition is true."""

OrgRepositoriesAnyCondition = TypedDict("OrgRepositoriesAnyCondition", {"any": OrgRepositoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all org_repositories condition types
OrgRepositoriesCondition = (
    OrgRepositoriesEqCondition
    | OrgRepositoriesNeqCondition
    | OrgRepositoriesGtCondition
    | OrgRepositoriesGteCondition
    | OrgRepositoriesLtCondition
    | OrgRepositoriesLteCondition
    | OrgRepositoriesInCondition
    | OrgRepositoriesLikeCondition
    | OrgRepositoriesFuzzyCondition
    | OrgRepositoriesKeywordCondition
    | OrgRepositoriesContainsCondition
    | OrgRepositoriesNotCondition
    | OrgRepositoriesAndCondition
    | OrgRepositoriesOrCondition
    | OrgRepositoriesAnyCondition
)


class OrgRepositoriesSearchQuery(TypedDict, total=False):
    """Search query for org_repositories entity."""
    filter: OrgRepositoriesCondition
    sort: list[OrgRepositoriesSortFilter]


# ===== PR_COMMENTS SEARCH TYPES =====

class PrCommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering pr_comments search queries."""


class PrCommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class PrCommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class PrCommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class PrCommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting pr_comments search results."""


# Entity-specific condition types for pr_comments
class PrCommentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PrCommentsSearchFilter


class PrCommentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PrCommentsSearchFilter


class PrCommentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PrCommentsSearchFilter


class PrCommentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PrCommentsSearchFilter


class PrCommentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PrCommentsSearchFilter


class PrCommentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PrCommentsSearchFilter


class PrCommentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PrCommentsStringFilter


class PrCommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PrCommentsStringFilter


class PrCommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PrCommentsStringFilter


class PrCommentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PrCommentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PrCommentsInCondition = TypedDict("PrCommentsInCondition", {"in": PrCommentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PrCommentsNotCondition = TypedDict("PrCommentsNotCondition", {"not": "PrCommentsCondition"}, total=False)
"""Negates the nested condition."""

PrCommentsAndCondition = TypedDict("PrCommentsAndCondition", {"and": "list[PrCommentsCondition]"}, total=False)
"""True if all nested conditions are true."""

PrCommentsOrCondition = TypedDict("PrCommentsOrCondition", {"or": "list[PrCommentsCondition]"}, total=False)
"""True if any nested condition is true."""

PrCommentsAnyCondition = TypedDict("PrCommentsAnyCondition", {"any": PrCommentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pr_comments condition types
PrCommentsCondition = (
    PrCommentsEqCondition
    | PrCommentsNeqCondition
    | PrCommentsGtCondition
    | PrCommentsGteCondition
    | PrCommentsLtCondition
    | PrCommentsLteCondition
    | PrCommentsInCondition
    | PrCommentsLikeCondition
    | PrCommentsFuzzyCondition
    | PrCommentsKeywordCondition
    | PrCommentsContainsCondition
    | PrCommentsNotCondition
    | PrCommentsAndCondition
    | PrCommentsOrCondition
    | PrCommentsAnyCondition
)


class PrCommentsSearchQuery(TypedDict, total=False):
    """Search query for pr_comments entity."""
    filter: PrCommentsCondition
    sort: list[PrCommentsSortFilter]


# ===== PROJECT_ITEMS SEARCH TYPES =====

class ProjectItemsSearchFilter(TypedDict, total=False):
    """Available fields for filtering project_items search queries."""


class ProjectItemsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class ProjectItemsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class ProjectItemsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class ProjectItemsSortFilter(TypedDict, total=False):
    """Available fields for sorting project_items search results."""


# Entity-specific condition types for project_items
class ProjectItemsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectItemsSearchFilter


class ProjectItemsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectItemsSearchFilter


class ProjectItemsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectItemsSearchFilter


class ProjectItemsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectItemsSearchFilter


class ProjectItemsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectItemsSearchFilter


class ProjectItemsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectItemsSearchFilter


class ProjectItemsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectItemsStringFilter


class ProjectItemsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectItemsStringFilter


class ProjectItemsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectItemsStringFilter


class ProjectItemsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectItemsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectItemsInCondition = TypedDict("ProjectItemsInCondition", {"in": ProjectItemsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectItemsNotCondition = TypedDict("ProjectItemsNotCondition", {"not": "ProjectItemsCondition"}, total=False)
"""Negates the nested condition."""

ProjectItemsAndCondition = TypedDict("ProjectItemsAndCondition", {"and": "list[ProjectItemsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectItemsOrCondition = TypedDict("ProjectItemsOrCondition", {"or": "list[ProjectItemsCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectItemsAnyCondition = TypedDict("ProjectItemsAnyCondition", {"any": ProjectItemsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all project_items condition types
ProjectItemsCondition = (
    ProjectItemsEqCondition
    | ProjectItemsNeqCondition
    | ProjectItemsGtCondition
    | ProjectItemsGteCondition
    | ProjectItemsLtCondition
    | ProjectItemsLteCondition
    | ProjectItemsInCondition
    | ProjectItemsLikeCondition
    | ProjectItemsFuzzyCondition
    | ProjectItemsKeywordCondition
    | ProjectItemsContainsCondition
    | ProjectItemsNotCondition
    | ProjectItemsAndCondition
    | ProjectItemsOrCondition
    | ProjectItemsAnyCondition
)


class ProjectItemsSearchQuery(TypedDict, total=False):
    """Search query for project_items entity."""
    filter: ProjectItemsCondition
    sort: list[ProjectItemsSortFilter]


# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    id: str | None
    """GraphQL node ID of the project"""
    number: int | None
    """Organization- or user-scoped project number"""
    title: str | None
    """Project title"""
    short_description: str | None
    """Short description displayed on the project summary"""
    url: str | None
    """Permalink to the project on GitHub"""
    closed: bool | None
    """Whether the project has been closed"""
    public: bool | None
    """Whether the project is publicly visible"""
    created_at: str | None
    """ISO 8601 timestamp when the project was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the project was last updated"""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the project"""
    number: list[int]
    """Organization- or user-scoped project number"""
    title: list[str]
    """Project title"""
    short_description: list[str]
    """Short description displayed on the project summary"""
    url: list[str]
    """Permalink to the project on GitHub"""
    closed: list[bool]
    """Whether the project has been closed"""
    public: list[bool]
    """Whether the project is publicly visible"""
    created_at: list[str]
    """ISO 8601 timestamp when the project was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the project was last updated"""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the project"""
    number: Any
    """Organization- or user-scoped project number"""
    title: Any
    """Project title"""
    short_description: Any
    """Short description displayed on the project summary"""
    url: Any
    """Permalink to the project on GitHub"""
    closed: Any
    """Whether the project has been closed"""
    public: Any
    """Whether the project is publicly visible"""
    created_at: Any
    """ISO 8601 timestamp when the project was created"""
    updated_at: Any
    """ISO 8601 timestamp when the project was last updated"""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the project"""
    number: str
    """Organization- or user-scoped project number"""
    title: str
    """Project title"""
    short_description: str
    """Short description displayed on the project summary"""
    url: str
    """Permalink to the project on GitHub"""
    closed: str
    """Whether the project has been closed"""
    public: str
    """Whether the project is publicly visible"""
    created_at: str
    """ISO 8601 timestamp when the project was created"""
    updated_at: str
    """ISO 8601 timestamp when the project was last updated"""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the project"""
    number: AirbyteSortOrder
    """Organization- or user-scoped project number"""
    title: AirbyteSortOrder
    """Project title"""
    short_description: AirbyteSortOrder
    """Short description displayed on the project summary"""
    url: AirbyteSortOrder
    """Permalink to the project on GitHub"""
    closed: AirbyteSortOrder
    """Whether the project has been closed"""
    public: AirbyteSortOrder
    """Whether the project is publicly visible"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the project was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the project was last updated"""


# Entity-specific condition types for projects
class ProjectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectsSearchFilter


class ProjectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectsSearchFilter


class ProjectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectsSearchFilter


class ProjectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectsSearchFilter


class ProjectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectsSearchFilter


class ProjectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectsSearchFilter


class ProjectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectsStringFilter


class ProjectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectsStringFilter


class ProjectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectsStringFilter


class ProjectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectsInCondition = TypedDict("ProjectsInCondition", {"in": ProjectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectsNotCondition = TypedDict("ProjectsNotCondition", {"not": "ProjectsCondition"}, total=False)
"""Negates the nested condition."""

ProjectsAndCondition = TypedDict("ProjectsAndCondition", {"and": "list[ProjectsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectsOrCondition = TypedDict("ProjectsOrCondition", {"or": "list[ProjectsCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectsAnyCondition = TypedDict("ProjectsAnyCondition", {"any": ProjectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all projects condition types
ProjectsCondition = (
    ProjectsEqCondition
    | ProjectsNeqCondition
    | ProjectsGtCondition
    | ProjectsGteCondition
    | ProjectsLtCondition
    | ProjectsLteCondition
    | ProjectsInCondition
    | ProjectsLikeCondition
    | ProjectsFuzzyCondition
    | ProjectsKeywordCondition
    | ProjectsContainsCondition
    | ProjectsNotCondition
    | ProjectsAndCondition
    | ProjectsOrCondition
    | ProjectsAnyCondition
)


class ProjectsSearchQuery(TypedDict, total=False):
    """Search query for projects entity."""
    filter: ProjectsCondition
    sort: list[ProjectsSortFilter]


# ===== PULL_REQUESTS SEARCH TYPES =====

class PullRequestsSearchFilter(TypedDict, total=False):
    """Available fields for filtering pull_requests search queries."""
    id: str | None
    """GraphQL node ID of the pull request"""
    database_id: int | None
    """REST API numeric identifier for the pull request"""
    number: int | None
    """Repository-scoped pull request number"""
    title: str | None
    """Pull request title"""
    state: str | None
    """Pull request state in the cache: lowercase `open` or `closed` (REST API has no `merged` state; check `mergedAt` to distinguish merged PRs)"""
    is_draft: bool | None
    """Whether the pull request is still a draft"""
    created_at: str | None
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: str | None
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: str | None
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    url: str | None
    """Permalink to the pull request on GitHub"""


class PullRequestsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the pull request"""
    database_id: list[int]
    """REST API numeric identifier for the pull request"""
    number: list[int]
    """Repository-scoped pull request number"""
    title: list[str]
    """Pull request title"""
    state: list[str]
    """Pull request state in the cache: lowercase `open` or `closed` (REST API has no `merged` state; check `mergedAt` to distinguish merged PRs)"""
    is_draft: list[bool]
    """Whether the pull request is still a draft"""
    created_at: list[str]
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: list[str]
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: list[str]
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    url: list[str]
    """Permalink to the pull request on GitHub"""


class PullRequestsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the pull request"""
    database_id: Any
    """REST API numeric identifier for the pull request"""
    number: Any
    """Repository-scoped pull request number"""
    title: Any
    """Pull request title"""
    state: Any
    """Pull request state in the cache: lowercase `open` or `closed` (REST API has no `merged` state; check `mergedAt` to distinguish merged PRs)"""
    is_draft: Any
    """Whether the pull request is still a draft"""
    created_at: Any
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: Any
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: Any
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: Any
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    url: Any
    """Permalink to the pull request on GitHub"""


class PullRequestsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the pull request"""
    database_id: str
    """REST API numeric identifier for the pull request"""
    number: str
    """Repository-scoped pull request number"""
    title: str
    """Pull request title"""
    state: str
    """Pull request state in the cache: lowercase `open` or `closed` (REST API has no `merged` state; check `mergedAt` to distinguish merged PRs)"""
    is_draft: str
    """Whether the pull request is still a draft"""
    created_at: str
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: str
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: str
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: str
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    url: str
    """Permalink to the pull request on GitHub"""


class PullRequestsSortFilter(TypedDict, total=False):
    """Available fields for sorting pull_requests search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the pull request"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the pull request"""
    number: AirbyteSortOrder
    """Repository-scoped pull request number"""
    title: AirbyteSortOrder
    """Pull request title"""
    state: AirbyteSortOrder
    """Pull request state in the cache: lowercase `open` or `closed` (REST API has no `merged` state; check `mergedAt` to distinguish merged PRs)"""
    is_draft: AirbyteSortOrder
    """Whether the pull request is still a draft"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    url: AirbyteSortOrder
    """Permalink to the pull request on GitHub"""


# Entity-specific condition types for pull_requests
class PullRequestsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PullRequestsSearchFilter


class PullRequestsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PullRequestsSearchFilter


class PullRequestsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PullRequestsSearchFilter


class PullRequestsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PullRequestsSearchFilter


class PullRequestsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PullRequestsSearchFilter


class PullRequestsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PullRequestsSearchFilter


class PullRequestsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PullRequestsStringFilter


class PullRequestsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PullRequestsStringFilter


class PullRequestsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PullRequestsStringFilter


class PullRequestsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PullRequestsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PullRequestsInCondition = TypedDict("PullRequestsInCondition", {"in": PullRequestsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PullRequestsNotCondition = TypedDict("PullRequestsNotCondition", {"not": "PullRequestsCondition"}, total=False)
"""Negates the nested condition."""

PullRequestsAndCondition = TypedDict("PullRequestsAndCondition", {"and": "list[PullRequestsCondition]"}, total=False)
"""True if all nested conditions are true."""

PullRequestsOrCondition = TypedDict("PullRequestsOrCondition", {"or": "list[PullRequestsCondition]"}, total=False)
"""True if any nested condition is true."""

PullRequestsAnyCondition = TypedDict("PullRequestsAnyCondition", {"any": PullRequestsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pull_requests condition types
PullRequestsCondition = (
    PullRequestsEqCondition
    | PullRequestsNeqCondition
    | PullRequestsGtCondition
    | PullRequestsGteCondition
    | PullRequestsLtCondition
    | PullRequestsLteCondition
    | PullRequestsInCondition
    | PullRequestsLikeCondition
    | PullRequestsFuzzyCondition
    | PullRequestsKeywordCondition
    | PullRequestsContainsCondition
    | PullRequestsNotCondition
    | PullRequestsAndCondition
    | PullRequestsOrCondition
    | PullRequestsAnyCondition
)


class PullRequestsSearchQuery(TypedDict, total=False):
    """Search query for pull_requests entity."""
    filter: PullRequestsCondition
    sort: list[PullRequestsSortFilter]


# ===== RELEASES SEARCH TYPES =====

class ReleasesSearchFilter(TypedDict, total=False):
    """Available fields for filtering releases search queries."""
    id: str | None
    """GraphQL node ID of the release"""
    database_id: int | None
    """REST API numeric identifier for the release"""
    name: str | None
    """Display name of the release"""
    tag_name: str | None
    """Git tag the release points at (e.g. `v1.2.3`)"""
    description: str | None
    """Markdown body / release notes"""
    published_at: str | None
    """ISO 8601 timestamp when the release was published"""
    created_at: str | None
    """ISO 8601 timestamp when the release was created"""
    is_prerelease: bool | None
    """Whether the release is marked as a pre-release"""
    is_draft: bool | None
    """Whether the release is still a draft and not published"""
    url: str | None
    """Permalink to the release on GitHub"""


class ReleasesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the release"""
    database_id: list[int]
    """REST API numeric identifier for the release"""
    name: list[str]
    """Display name of the release"""
    tag_name: list[str]
    """Git tag the release points at (e.g. `v1.2.3`)"""
    description: list[str]
    """Markdown body / release notes"""
    published_at: list[str]
    """ISO 8601 timestamp when the release was published"""
    created_at: list[str]
    """ISO 8601 timestamp when the release was created"""
    is_prerelease: list[bool]
    """Whether the release is marked as a pre-release"""
    is_draft: list[bool]
    """Whether the release is still a draft and not published"""
    url: list[str]
    """Permalink to the release on GitHub"""


class ReleasesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the release"""
    database_id: Any
    """REST API numeric identifier for the release"""
    name: Any
    """Display name of the release"""
    tag_name: Any
    """Git tag the release points at (e.g. `v1.2.3`)"""
    description: Any
    """Markdown body / release notes"""
    published_at: Any
    """ISO 8601 timestamp when the release was published"""
    created_at: Any
    """ISO 8601 timestamp when the release was created"""
    is_prerelease: Any
    """Whether the release is marked as a pre-release"""
    is_draft: Any
    """Whether the release is still a draft and not published"""
    url: Any
    """Permalink to the release on GitHub"""


class ReleasesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the release"""
    database_id: str
    """REST API numeric identifier for the release"""
    name: str
    """Display name of the release"""
    tag_name: str
    """Git tag the release points at (e.g. `v1.2.3`)"""
    description: str
    """Markdown body / release notes"""
    published_at: str
    """ISO 8601 timestamp when the release was published"""
    created_at: str
    """ISO 8601 timestamp when the release was created"""
    is_prerelease: str
    """Whether the release is marked as a pre-release"""
    is_draft: str
    """Whether the release is still a draft and not published"""
    url: str
    """Permalink to the release on GitHub"""


class ReleasesSortFilter(TypedDict, total=False):
    """Available fields for sorting releases search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the release"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the release"""
    name: AirbyteSortOrder
    """Display name of the release"""
    tag_name: AirbyteSortOrder
    """Git tag the release points at (e.g. `v1.2.3`)"""
    description: AirbyteSortOrder
    """Markdown body / release notes"""
    published_at: AirbyteSortOrder
    """ISO 8601 timestamp when the release was published"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the release was created"""
    is_prerelease: AirbyteSortOrder
    """Whether the release is marked as a pre-release"""
    is_draft: AirbyteSortOrder
    """Whether the release is still a draft and not published"""
    url: AirbyteSortOrder
    """Permalink to the release on GitHub"""


# Entity-specific condition types for releases
class ReleasesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ReleasesSearchFilter


class ReleasesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ReleasesSearchFilter


class ReleasesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ReleasesSearchFilter


class ReleasesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ReleasesSearchFilter


class ReleasesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ReleasesSearchFilter


class ReleasesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ReleasesSearchFilter


class ReleasesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ReleasesStringFilter


class ReleasesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ReleasesStringFilter


class ReleasesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ReleasesStringFilter


class ReleasesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ReleasesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ReleasesInCondition = TypedDict("ReleasesInCondition", {"in": ReleasesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ReleasesNotCondition = TypedDict("ReleasesNotCondition", {"not": "ReleasesCondition"}, total=False)
"""Negates the nested condition."""

ReleasesAndCondition = TypedDict("ReleasesAndCondition", {"and": "list[ReleasesCondition]"}, total=False)
"""True if all nested conditions are true."""

ReleasesOrCondition = TypedDict("ReleasesOrCondition", {"or": "list[ReleasesCondition]"}, total=False)
"""True if any nested condition is true."""

ReleasesAnyCondition = TypedDict("ReleasesAnyCondition", {"any": ReleasesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all releases condition types
ReleasesCondition = (
    ReleasesEqCondition
    | ReleasesNeqCondition
    | ReleasesGtCondition
    | ReleasesGteCondition
    | ReleasesLtCondition
    | ReleasesLteCondition
    | ReleasesInCondition
    | ReleasesLikeCondition
    | ReleasesFuzzyCondition
    | ReleasesKeywordCondition
    | ReleasesContainsCondition
    | ReleasesNotCondition
    | ReleasesAndCondition
    | ReleasesOrCondition
    | ReleasesAnyCondition
)


class ReleasesSearchQuery(TypedDict, total=False):
    """Search query for releases entity."""
    filter: ReleasesCondition
    sort: list[ReleasesSortFilter]


# ===== REPOSITORIES SEARCH TYPES =====

class RepositoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering repositories search queries."""
    id: str | None
    """GraphQL node ID of the repository"""
    name: str | None
    """Short repository name (without owner)"""
    name_with_owner: str | None
    """Fully-qualified `owner/name` identifier for the repository"""
    description: str | None
    """Short description of the repository"""
    url: str | None
    """Canonical GitHub URL for the repository"""
    created_at: str | None
    """ISO 8601 timestamp when the repository was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: str | None
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: int | None
    """Number of forks of the repository"""
    stargazer_count: int | None
    """Number of users who have starred the repository"""
    is_private: bool | None
    """Whether the repository is private"""
    is_fork: bool | None
    """Whether the repository is a fork of another repository"""
    is_archived: bool | None
    """Whether the repository has been archived"""


class RepositoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the repository"""
    name: list[str]
    """Short repository name (without owner)"""
    name_with_owner: list[str]
    """Fully-qualified `owner/name` identifier for the repository"""
    description: list[str]
    """Short description of the repository"""
    url: list[str]
    """Canonical GitHub URL for the repository"""
    created_at: list[str]
    """ISO 8601 timestamp when the repository was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: list[str]
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: list[int]
    """Number of forks of the repository"""
    stargazer_count: list[int]
    """Number of users who have starred the repository"""
    is_private: list[bool]
    """Whether the repository is private"""
    is_fork: list[bool]
    """Whether the repository is a fork of another repository"""
    is_archived: list[bool]
    """Whether the repository has been archived"""


class RepositoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the repository"""
    name: Any
    """Short repository name (without owner)"""
    name_with_owner: Any
    """Fully-qualified `owner/name` identifier for the repository"""
    description: Any
    """Short description of the repository"""
    url: Any
    """Canonical GitHub URL for the repository"""
    created_at: Any
    """ISO 8601 timestamp when the repository was created"""
    updated_at: Any
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: Any
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: Any
    """Number of forks of the repository"""
    stargazer_count: Any
    """Number of users who have starred the repository"""
    is_private: Any
    """Whether the repository is private"""
    is_fork: Any
    """Whether the repository is a fork of another repository"""
    is_archived: Any
    """Whether the repository has been archived"""


class RepositoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the repository"""
    name: str
    """Short repository name (without owner)"""
    name_with_owner: str
    """Fully-qualified `owner/name` identifier for the repository"""
    description: str
    """Short description of the repository"""
    url: str
    """Canonical GitHub URL for the repository"""
    created_at: str
    """ISO 8601 timestamp when the repository was created"""
    updated_at: str
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: str
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: str
    """Number of forks of the repository"""
    stargazer_count: str
    """Number of users who have starred the repository"""
    is_private: str
    """Whether the repository is private"""
    is_fork: str
    """Whether the repository is a fork of another repository"""
    is_archived: str
    """Whether the repository has been archived"""


class RepositoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting repositories search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the repository"""
    name: AirbyteSortOrder
    """Short repository name (without owner)"""
    name_with_owner: AirbyteSortOrder
    """Fully-qualified `owner/name` identifier for the repository"""
    description: AirbyteSortOrder
    """Short description of the repository"""
    url: AirbyteSortOrder
    """Canonical GitHub URL for the repository"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the repository was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: AirbyteSortOrder
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: AirbyteSortOrder
    """Number of forks of the repository"""
    stargazer_count: AirbyteSortOrder
    """Number of users who have starred the repository"""
    is_private: AirbyteSortOrder
    """Whether the repository is private"""
    is_fork: AirbyteSortOrder
    """Whether the repository is a fork of another repository"""
    is_archived: AirbyteSortOrder
    """Whether the repository has been archived"""


# Entity-specific condition types for repositories
class RepositoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RepositoriesSearchFilter


class RepositoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RepositoriesSearchFilter


class RepositoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RepositoriesSearchFilter


class RepositoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RepositoriesSearchFilter


class RepositoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RepositoriesSearchFilter


class RepositoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RepositoriesSearchFilter


class RepositoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: RepositoriesStringFilter


class RepositoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RepositoriesStringFilter


class RepositoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RepositoriesStringFilter


class RepositoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: RepositoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RepositoriesInCondition = TypedDict("RepositoriesInCondition", {"in": RepositoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RepositoriesNotCondition = TypedDict("RepositoriesNotCondition", {"not": "RepositoriesCondition"}, total=False)
"""Negates the nested condition."""

RepositoriesAndCondition = TypedDict("RepositoriesAndCondition", {"and": "list[RepositoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

RepositoriesOrCondition = TypedDict("RepositoriesOrCondition", {"or": "list[RepositoriesCondition]"}, total=False)
"""True if any nested condition is true."""

RepositoriesAnyCondition = TypedDict("RepositoriesAnyCondition", {"any": RepositoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all repositories condition types
RepositoriesCondition = (
    RepositoriesEqCondition
    | RepositoriesNeqCondition
    | RepositoriesGtCondition
    | RepositoriesGteCondition
    | RepositoriesLtCondition
    | RepositoriesLteCondition
    | RepositoriesInCondition
    | RepositoriesLikeCondition
    | RepositoriesFuzzyCondition
    | RepositoriesKeywordCondition
    | RepositoriesContainsCondition
    | RepositoriesNotCondition
    | RepositoriesAndCondition
    | RepositoriesOrCondition
    | RepositoriesAnyCondition
)


class RepositoriesSearchQuery(TypedDict, total=False):
    """Search query for repositories entity."""
    filter: RepositoriesCondition
    sort: list[RepositoriesSortFilter]


# ===== REVIEWS SEARCH TYPES =====

class ReviewsSearchFilter(TypedDict, total=False):
    """Available fields for filtering reviews search queries."""
    id: str | None
    """GraphQL node ID of the review"""
    database_id: int | None
    """REST API numeric identifier for the review"""
    state: str | None
    """Review state in the cache: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`"""
    body: str | None
    """Review body text"""
    submitted_at: str | None
    """ISO 8601 timestamp when the review was submitted"""
    created_at: str | None
    """ISO 8601 timestamp when the review was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the review was last updated"""
    url: str | None
    """Permalink to the review on GitHub"""


class ReviewsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the review"""
    database_id: list[int]
    """REST API numeric identifier for the review"""
    state: list[str]
    """Review state in the cache: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`"""
    body: list[str]
    """Review body text"""
    submitted_at: list[str]
    """ISO 8601 timestamp when the review was submitted"""
    created_at: list[str]
    """ISO 8601 timestamp when the review was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the review was last updated"""
    url: list[str]
    """Permalink to the review on GitHub"""


class ReviewsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the review"""
    database_id: Any
    """REST API numeric identifier for the review"""
    state: Any
    """Review state in the cache: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`"""
    body: Any
    """Review body text"""
    submitted_at: Any
    """ISO 8601 timestamp when the review was submitted"""
    created_at: Any
    """ISO 8601 timestamp when the review was created"""
    updated_at: Any
    """ISO 8601 timestamp when the review was last updated"""
    url: Any
    """Permalink to the review on GitHub"""


class ReviewsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the review"""
    database_id: str
    """REST API numeric identifier for the review"""
    state: str
    """Review state in the cache: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`"""
    body: str
    """Review body text"""
    submitted_at: str
    """ISO 8601 timestamp when the review was submitted"""
    created_at: str
    """ISO 8601 timestamp when the review was created"""
    updated_at: str
    """ISO 8601 timestamp when the review was last updated"""
    url: str
    """Permalink to the review on GitHub"""


class ReviewsSortFilter(TypedDict, total=False):
    """Available fields for sorting reviews search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the review"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the review"""
    state: AirbyteSortOrder
    """Review state in the cache: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`"""
    body: AirbyteSortOrder
    """Review body text"""
    submitted_at: AirbyteSortOrder
    """ISO 8601 timestamp when the review was submitted"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the review was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the review was last updated"""
    url: AirbyteSortOrder
    """Permalink to the review on GitHub"""


# Entity-specific condition types for reviews
class ReviewsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ReviewsSearchFilter


class ReviewsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ReviewsSearchFilter


class ReviewsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ReviewsSearchFilter


class ReviewsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ReviewsSearchFilter


class ReviewsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ReviewsSearchFilter


class ReviewsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ReviewsSearchFilter


class ReviewsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ReviewsStringFilter


class ReviewsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ReviewsStringFilter


class ReviewsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ReviewsStringFilter


class ReviewsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ReviewsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ReviewsInCondition = TypedDict("ReviewsInCondition", {"in": ReviewsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ReviewsNotCondition = TypedDict("ReviewsNotCondition", {"not": "ReviewsCondition"}, total=False)
"""Negates the nested condition."""

ReviewsAndCondition = TypedDict("ReviewsAndCondition", {"and": "list[ReviewsCondition]"}, total=False)
"""True if all nested conditions are true."""

ReviewsOrCondition = TypedDict("ReviewsOrCondition", {"or": "list[ReviewsCondition]"}, total=False)
"""True if any nested condition is true."""

ReviewsAnyCondition = TypedDict("ReviewsAnyCondition", {"any": ReviewsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all reviews condition types
ReviewsCondition = (
    ReviewsEqCondition
    | ReviewsNeqCondition
    | ReviewsGtCondition
    | ReviewsGteCondition
    | ReviewsLtCondition
    | ReviewsLteCondition
    | ReviewsInCondition
    | ReviewsLikeCondition
    | ReviewsFuzzyCondition
    | ReviewsKeywordCondition
    | ReviewsContainsCondition
    | ReviewsNotCondition
    | ReviewsAndCondition
    | ReviewsOrCondition
    | ReviewsAnyCondition
)


class ReviewsSearchQuery(TypedDict, total=False):
    """Search query for reviews entity."""
    filter: ReviewsCondition
    sort: list[ReviewsSortFilter]


# ===== STARGAZERS SEARCH TYPES =====

class StargazersSearchFilter(TypedDict, total=False):
    """Available fields for filtering stargazers search queries."""
    starred_at: str | None
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    starred_at: list[str]
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    starred_at: Any
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    starred_at: str
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersSortFilter(TypedDict, total=False):
    """Available fields for sorting stargazers search results."""
    starred_at: AirbyteSortOrder
    """ISO 8601 timestamp when the user starred the repository"""


# Entity-specific condition types for stargazers
class StargazersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: StargazersSearchFilter


class StargazersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: StargazersSearchFilter


class StargazersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: StargazersSearchFilter


class StargazersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: StargazersSearchFilter


class StargazersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: StargazersSearchFilter


class StargazersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: StargazersSearchFilter


class StargazersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: StargazersStringFilter


class StargazersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: StargazersStringFilter


class StargazersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: StargazersStringFilter


class StargazersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: StargazersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
StargazersInCondition = TypedDict("StargazersInCondition", {"in": StargazersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

StargazersNotCondition = TypedDict("StargazersNotCondition", {"not": "StargazersCondition"}, total=False)
"""Negates the nested condition."""

StargazersAndCondition = TypedDict("StargazersAndCondition", {"and": "list[StargazersCondition]"}, total=False)
"""True if all nested conditions are true."""

StargazersOrCondition = TypedDict("StargazersOrCondition", {"or": "list[StargazersCondition]"}, total=False)
"""True if any nested condition is true."""

StargazersAnyCondition = TypedDict("StargazersAnyCondition", {"any": StargazersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all stargazers condition types
StargazersCondition = (
    StargazersEqCondition
    | StargazersNeqCondition
    | StargazersGtCondition
    | StargazersGteCondition
    | StargazersLtCondition
    | StargazersLteCondition
    | StargazersInCondition
    | StargazersLikeCondition
    | StargazersFuzzyCondition
    | StargazersKeywordCondition
    | StargazersContainsCondition
    | StargazersNotCondition
    | StargazersAndCondition
    | StargazersOrCondition
    | StargazersAnyCondition
)


class StargazersSearchQuery(TypedDict, total=False):
    """Search query for stargazers entity."""
    filter: StargazersCondition
    sort: list[StargazersSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    name: str | None
    """Tag name (e.g. `v1.2.3`)"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Tag name (e.g. `v1.2.3`)"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Tag name (e.g. `v1.2.3`)"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Tag name (e.g. `v1.2.3`)"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    name: AirbyteSortOrder
    """Tag name (e.g. `v1.2.3`)"""


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


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    id: str | None
    """GraphQL node ID of the team"""
    database_id: int | None
    """REST API numeric identifier for the team"""
    slug: str | None
    """URL-friendly slug for the team within its organization"""
    name: str | None
    """Display name of the team"""
    description: str | None
    """Short description of the team"""
    privacy: str | None
    """Team visibility: `secret` or `closed` (REST API values)"""
    url: str | None
    """Permalink to the team on GitHub"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the team"""
    database_id: list[int]
    """REST API numeric identifier for the team"""
    slug: list[str]
    """URL-friendly slug for the team within its organization"""
    name: list[str]
    """Display name of the team"""
    description: list[str]
    """Short description of the team"""
    privacy: list[str]
    """Team visibility: `secret` or `closed` (REST API values)"""
    url: list[str]
    """Permalink to the team on GitHub"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the team"""
    database_id: Any
    """REST API numeric identifier for the team"""
    slug: Any
    """URL-friendly slug for the team within its organization"""
    name: Any
    """Display name of the team"""
    description: Any
    """Short description of the team"""
    privacy: Any
    """Team visibility: `secret` or `closed` (REST API values)"""
    url: Any
    """Permalink to the team on GitHub"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the team"""
    database_id: str
    """REST API numeric identifier for the team"""
    slug: str
    """URL-friendly slug for the team within its organization"""
    name: str
    """Display name of the team"""
    description: str
    """Short description of the team"""
    privacy: str
    """Team visibility: `secret` or `closed` (REST API values)"""
    url: str
    """Permalink to the team on GitHub"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the team"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the team"""
    slug: AirbyteSortOrder
    """URL-friendly slug for the team within its organization"""
    name: AirbyteSortOrder
    """Display name of the team"""
    description: AirbyteSortOrder
    """Short description of the team"""
    privacy: AirbyteSortOrder
    """Team visibility: `secret` or `closed` (REST API values)"""
    url: AirbyteSortOrder
    """Permalink to the team on GitHub"""


# Entity-specific condition types for teams
class TeamsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TeamsSearchFilter


class TeamsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TeamsSearchFilter


class TeamsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TeamsSearchFilter


class TeamsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TeamsSearchFilter


class TeamsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TeamsSearchFilter


class TeamsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TeamsSearchFilter


class TeamsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TeamsStringFilter


class TeamsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TeamsStringFilter


class TeamsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TeamsStringFilter


class TeamsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TeamsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TeamsInCondition = TypedDict("TeamsInCondition", {"in": TeamsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TeamsNotCondition = TypedDict("TeamsNotCondition", {"not": "TeamsCondition"}, total=False)
"""Negates the nested condition."""

TeamsAndCondition = TypedDict("TeamsAndCondition", {"and": "list[TeamsCondition]"}, total=False)
"""True if all nested conditions are true."""

TeamsOrCondition = TypedDict("TeamsOrCondition", {"or": "list[TeamsCondition]"}, total=False)
"""True if any nested condition is true."""

TeamsAnyCondition = TypedDict("TeamsAnyCondition", {"any": TeamsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all teams condition types
TeamsCondition = (
    TeamsEqCondition
    | TeamsNeqCondition
    | TeamsGtCondition
    | TeamsGteCondition
    | TeamsLtCondition
    | TeamsLteCondition
    | TeamsInCondition
    | TeamsLikeCondition
    | TeamsFuzzyCondition
    | TeamsKeywordCondition
    | TeamsContainsCondition
    | TeamsNotCondition
    | TeamsAndCondition
    | TeamsOrCondition
    | TeamsAnyCondition
)


class TeamsSearchQuery(TypedDict, total=False):
    """Search query for teams entity."""
    filter: TeamsCondition
    sort: list[TeamsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    id: str | None
    """GraphQL node ID of the user"""
    database_id: int | None
    """REST API numeric identifier for the user"""
    login: str | None
    """User login/handle"""
    url: str | None
    """Permalink to the user's profile on GitHub"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the user"""
    database_id: list[int]
    """REST API numeric identifier for the user"""
    login: list[str]
    """User login/handle"""
    url: list[str]
    """Permalink to the user's profile on GitHub"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the user"""
    database_id: Any
    """REST API numeric identifier for the user"""
    login: Any
    """User login/handle"""
    url: Any
    """Permalink to the user's profile on GitHub"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the user"""
    database_id: str
    """REST API numeric identifier for the user"""
    login: str
    """User login/handle"""
    url: str
    """Permalink to the user's profile on GitHub"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the user"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the user"""
    login: AirbyteSortOrder
    """User login/handle"""
    url: AirbyteSortOrder
    """Permalink to the user's profile on GitHub"""


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


# ===== VIEWER SEARCH TYPES =====

class ViewerSearchFilter(TypedDict, total=False):
    """Available fields for filtering viewer search queries."""


class ViewerInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class ViewerAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class ViewerStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class ViewerSortFilter(TypedDict, total=False):
    """Available fields for sorting viewer search results."""


# Entity-specific condition types for viewer
class ViewerEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ViewerSearchFilter


class ViewerNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ViewerSearchFilter


class ViewerGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ViewerSearchFilter


class ViewerGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ViewerSearchFilter


class ViewerLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ViewerSearchFilter


class ViewerLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ViewerSearchFilter


class ViewerLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ViewerStringFilter


class ViewerFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ViewerStringFilter


class ViewerKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ViewerStringFilter


class ViewerContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ViewerAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ViewerInCondition = TypedDict("ViewerInCondition", {"in": ViewerInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ViewerNotCondition = TypedDict("ViewerNotCondition", {"not": "ViewerCondition"}, total=False)
"""Negates the nested condition."""

ViewerAndCondition = TypedDict("ViewerAndCondition", {"and": "list[ViewerCondition]"}, total=False)
"""True if all nested conditions are true."""

ViewerOrCondition = TypedDict("ViewerOrCondition", {"or": "list[ViewerCondition]"}, total=False)
"""True if any nested condition is true."""

ViewerAnyCondition = TypedDict("ViewerAnyCondition", {"any": ViewerAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all viewer condition types
ViewerCondition = (
    ViewerEqCondition
    | ViewerNeqCondition
    | ViewerGtCondition
    | ViewerGteCondition
    | ViewerLtCondition
    | ViewerLteCondition
    | ViewerInCondition
    | ViewerLikeCondition
    | ViewerFuzzyCondition
    | ViewerKeywordCondition
    | ViewerContainsCondition
    | ViewerNotCondition
    | ViewerAndCondition
    | ViewerOrCondition
    | ViewerAnyCondition
)


class ViewerSearchQuery(TypedDict, total=False):
    """Search query for viewer entity."""
    filter: ViewerCondition
    sort: list[ViewerSortFilter]


# ===== VIEWER_REPOSITORIES SEARCH TYPES =====

class ViewerRepositoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering viewer_repositories search queries."""


class ViewerRepositoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class ViewerRepositoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class ViewerRepositoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class ViewerRepositoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting viewer_repositories search results."""


# Entity-specific condition types for viewer_repositories
class ViewerRepositoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ViewerRepositoriesSearchFilter


class ViewerRepositoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ViewerRepositoriesSearchFilter


class ViewerRepositoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ViewerRepositoriesSearchFilter


class ViewerRepositoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ViewerRepositoriesSearchFilter


class ViewerRepositoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ViewerRepositoriesSearchFilter


class ViewerRepositoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ViewerRepositoriesSearchFilter


class ViewerRepositoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ViewerRepositoriesStringFilter


class ViewerRepositoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ViewerRepositoriesStringFilter


class ViewerRepositoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ViewerRepositoriesStringFilter


class ViewerRepositoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ViewerRepositoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ViewerRepositoriesInCondition = TypedDict("ViewerRepositoriesInCondition", {"in": ViewerRepositoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ViewerRepositoriesNotCondition = TypedDict("ViewerRepositoriesNotCondition", {"not": "ViewerRepositoriesCondition"}, total=False)
"""Negates the nested condition."""

ViewerRepositoriesAndCondition = TypedDict("ViewerRepositoriesAndCondition", {"and": "list[ViewerRepositoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

ViewerRepositoriesOrCondition = TypedDict("ViewerRepositoriesOrCondition", {"or": "list[ViewerRepositoriesCondition]"}, total=False)
"""True if any nested condition is true."""

ViewerRepositoriesAnyCondition = TypedDict("ViewerRepositoriesAnyCondition", {"any": ViewerRepositoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all viewer_repositories condition types
ViewerRepositoriesCondition = (
    ViewerRepositoriesEqCondition
    | ViewerRepositoriesNeqCondition
    | ViewerRepositoriesGtCondition
    | ViewerRepositoriesGteCondition
    | ViewerRepositoriesLtCondition
    | ViewerRepositoriesLteCondition
    | ViewerRepositoriesInCondition
    | ViewerRepositoriesLikeCondition
    | ViewerRepositoriesFuzzyCondition
    | ViewerRepositoriesKeywordCondition
    | ViewerRepositoriesContainsCondition
    | ViewerRepositoriesNotCondition
    | ViewerRepositoriesAndCondition
    | ViewerRepositoriesOrCondition
    | ViewerRepositoriesAnyCondition
)


class ViewerRepositoriesSearchQuery(TypedDict, total=False):
    """Search query for viewer_repositories entity."""
    filter: ViewerRepositoriesCondition
    sort: list[ViewerRepositoriesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
