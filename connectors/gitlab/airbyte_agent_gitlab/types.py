"""
Type definitions for gitlab connector.
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

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    membership: NotRequired[bool]
    owned: NotRequired[bool]
    search: NotRequired[str]
    order_by: NotRequired[str]
    sort: NotRequired[str]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    id: str
    statistics: NotRequired[bool]

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    state: NotRequired[str]
    scope: NotRequired[str]
    order_by: NotRequired[str]
    sort: NotRequired[str]
    created_after: NotRequired[str]
    created_before: NotRequired[str]
    updated_after: NotRequired[str]
    updated_before: NotRequired[str]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    project_id: str
    issue_iid: str

class MergeRequestsListParams(TypedDict):
    """Parameters for merge_requests.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    state: NotRequired[str]
    scope: NotRequired[str]
    order_by: NotRequired[str]
    sort: NotRequired[str]
    created_after: NotRequired[str]
    created_before: NotRequired[str]
    updated_after: NotRequired[str]
    updated_before: NotRequired[str]

class MergeRequestsGetParams(TypedDict):
    """Parameters for merge_requests.get operation"""
    project_id: str
    merge_request_iid: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    active: NotRequired[bool]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CommitsListParams(TypedDict):
    """Parameters for commits.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    ref_name: NotRequired[str]
    since: NotRequired[str]
    until: NotRequired[str]
    with_stats: NotRequired[bool]

class CommitsGetParams(TypedDict):
    """Parameters for commits.get operation"""
    project_id: str
    sha: str
    stats: NotRequired[bool]

class GroupsListParams(TypedDict):
    """Parameters for groups.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    owned: NotRequired[bool]
    order_by: NotRequired[str]
    sort: NotRequired[str]

class GroupsGetParams(TypedDict):
    """Parameters for groups.get operation"""
    id: str

class BranchesListParams(TypedDict):
    """Parameters for branches.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]

class BranchesGetParams(TypedDict):
    """Parameters for branches.get operation"""
    project_id: str
    branch: str

class PipelinesListParams(TypedDict):
    """Parameters for pipelines.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    status: NotRequired[str]
    ref: NotRequired[str]
    order_by: NotRequired[str]
    sort: NotRequired[str]

class PipelinesGetParams(TypedDict):
    """Parameters for pipelines.get operation"""
    project_id: str
    pipeline_id: str

class GroupMembersListParams(TypedDict):
    """Parameters for group_members.list operation"""
    group_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    query: NotRequired[str]

class GroupMembersGetParams(TypedDict):
    """Parameters for group_members.get operation"""
    group_id: str
    user_id: str

class ProjectMembersListParams(TypedDict):
    """Parameters for project_members.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    query: NotRequired[str]

class ProjectMembersGetParams(TypedDict):
    """Parameters for project_members.get operation"""
    project_id: str
    user_id: str

class ReleasesListParams(TypedDict):
    """Parameters for releases.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    order_by: NotRequired[str]
    sort: NotRequired[str]

class ReleasesGetParams(TypedDict):
    """Parameters for releases.get operation"""
    project_id: str
    tag_name: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    order_by: NotRequired[str]
    sort: NotRequired[str]

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    project_id: str
    tag_name: str

class GroupMilestonesListParams(TypedDict):
    """Parameters for group_milestones.list operation"""
    group_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    state: NotRequired[str]
    search: NotRequired[str]

class GroupMilestonesGetParams(TypedDict):
    """Parameters for group_milestones.get operation"""
    group_id: str
    milestone_id: str

class ProjectMilestonesListParams(TypedDict):
    """Parameters for project_milestones.list operation"""
    project_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    state: NotRequired[str]
    search: NotRequired[str]

class ProjectMilestonesGetParams(TypedDict):
    """Parameters for project_milestones.get operation"""
    project_id: str
    milestone_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    id: int | None
    """ID of the project"""
    description: str | None
    """Description of the project"""
    description_html: str | None
    """HTML-rendered description of the project"""
    name: str | None
    """Name of the project"""
    name_with_namespace: str | None
    """Full name including namespace"""
    path: str | None
    """URL path of the project"""
    path_with_namespace: str | None
    """Full path including namespace"""
    created_at: str | None
    """Timestamp when the project was created"""
    updated_at: str | None
    """Timestamp when the project was last updated"""
    default_branch: str | None
    """Default branch of the project"""
    tag_list: list[Any] | None
    """List of tags for the project"""
    topics: list[Any] | None
    """List of topics for the project"""
    ssh_url_to_repo: str | None
    """SSH URL to the repository"""
    http_url_to_repo: str | None
    """HTTP URL to the repository"""
    web_url: str | None
    """Web URL of the project"""
    readme_url: str | None
    """URL to the project README"""
    avatar_url: str | None
    """URL of the project avatar"""
    forks_count: int | None
    """Number of forks"""
    star_count: int | None
    """Number of stars"""
    last_activity_at: str | None
    """Timestamp of last activity"""
    namespace: dict[str, Any] | None
    """Namespace the project belongs to"""
    container_registry_image_prefix: str | None
    """Prefix for container registry images"""
    links: dict[str, Any] | None
    """Related resource links"""
    packages_enabled: bool | None
    """Whether packages are enabled"""
    empty_repo: bool | None
    """Whether the repository is empty"""
    archived: bool | None
    """Whether the project is archived"""
    visibility: str | None
    """Visibility level of the project"""
    resolve_outdated_diff_discussions: bool | None
    """Whether outdated diff discussions are auto-resolved"""
    container_registry_enabled: bool | None
    """Whether container registry is enabled"""
    container_expiration_policy: dict[str, Any] | None
    """Container expiration policy settings"""
    issues_enabled: bool | None
    """Whether issues are enabled"""
    merge_requests_enabled: bool | None
    """Whether merge requests are enabled"""
    wiki_enabled: bool | None
    """Whether wiki is enabled"""
    jobs_enabled: bool | None
    """Whether jobs are enabled"""
    snippets_enabled: bool | None
    """Whether snippets are enabled"""
    service_desk_enabled: bool | None
    """Whether service desk is enabled"""
    service_desk_address: str | None
    """Email address for the service desk"""
    can_create_merge_request_in: bool | None
    """Whether user can create merge requests"""
    issues_access_level: str | None
    """Access level for issues"""
    repository_access_level: str | None
    """Access level for the repository"""
    merge_requests_access_level: str | None
    """Access level for merge requests"""
    forking_access_level: str | None
    """Access level for forking"""
    wiki_access_level: str | None
    """Access level for the wiki"""
    builds_access_level: str | None
    """Access level for builds"""
    snippets_access_level: str | None
    """Access level for snippets"""
    pages_access_level: str | None
    """Access level for pages"""
    operations_access_level: str | None
    """Access level for operations"""
    analytics_access_level: str | None
    """Access level for analytics"""
    emails_disabled: bool | None
    """Whether emails are disabled"""
    shared_runners_enabled: bool | None
    """Whether shared runners are enabled"""
    lfs_enabled: bool | None
    """Whether Git LFS is enabled"""
    creator_id: int | None
    """ID of the project creator"""
    import_status: str | None
    """Import status of the project"""
    open_issues_count: int | None
    """Number of open issues"""
    ci_default_git_depth: int | None
    """Default git depth for CI pipelines"""
    ci_forward_deployment_enabled: bool | None
    """Whether CI forward deployment is enabled"""
    public_jobs: bool | None
    """Whether jobs are public"""
    build_timeout: int | None
    """Build timeout in seconds"""
    auto_cancel_pending_pipelines: str | None
    """Auto-cancel pending pipelines setting"""
    ci_config_path: str | None
    """Path to the CI configuration file"""
    shared_with_groups: list[Any] | None
    """Groups the project is shared with"""
    only_allow_merge_if_pipeline_succeeds: bool | None
    """Whether merge requires pipeline success"""
    allow_merge_on_skipped_pipeline: bool | None
    """Whether merge is allowed on skipped pipeline"""
    restrict_user_defined_variables: bool | None
    """Whether user-defined variables are restricted"""
    request_access_enabled: bool | None
    """Whether access requests are enabled"""
    only_allow_merge_if_all_discussions_are_resolved: bool | None
    """Whether merge requires all discussions resolved"""
    remove_source_branch_after_merge: bool | None
    """Whether source branch is removed after merge"""
    printing_merge_request_link_enabled: bool | None
    """Whether MR link printing is enabled"""
    merge_method: str | None
    """Merge method used for the project"""
    statistics: dict[str, Any] | None
    """Project statistics"""
    auto_devops_enabled: bool | None
    """Whether Auto DevOps is enabled"""
    auto_devops_deploy_strategy: str | None
    """Auto DevOps deployment strategy"""
    autoclose_referenced_issues: bool | None
    """Whether referenced issues are auto-closed"""
    external_authorization_classification_label: str | None
    """External authorization classification label"""
    requirements_enabled: bool | None
    """Whether requirements are enabled"""
    security_and_compliance_enabled: bool | None
    """Whether security and compliance is enabled"""
    compliance_frameworks: list[Any] | None
    """Compliance frameworks for the project"""
    permissions: dict[str, Any] | None
    """User permissions for the project"""
    keep_latest_artifact: bool | None
    """Whether the latest artifact is kept"""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the project"""
    description: list[str]
    """Description of the project"""
    description_html: list[str]
    """HTML-rendered description of the project"""
    name: list[str]
    """Name of the project"""
    name_with_namespace: list[str]
    """Full name including namespace"""
    path: list[str]
    """URL path of the project"""
    path_with_namespace: list[str]
    """Full path including namespace"""
    created_at: list[str]
    """Timestamp when the project was created"""
    updated_at: list[str]
    """Timestamp when the project was last updated"""
    default_branch: list[str]
    """Default branch of the project"""
    tag_list: list[list[Any]]
    """List of tags for the project"""
    topics: list[list[Any]]
    """List of topics for the project"""
    ssh_url_to_repo: list[str]
    """SSH URL to the repository"""
    http_url_to_repo: list[str]
    """HTTP URL to the repository"""
    web_url: list[str]
    """Web URL of the project"""
    readme_url: list[str]
    """URL to the project README"""
    avatar_url: list[str]
    """URL of the project avatar"""
    forks_count: list[int]
    """Number of forks"""
    star_count: list[int]
    """Number of stars"""
    last_activity_at: list[str]
    """Timestamp of last activity"""
    namespace: list[dict[str, Any]]
    """Namespace the project belongs to"""
    container_registry_image_prefix: list[str]
    """Prefix for container registry images"""
    links: list[dict[str, Any]]
    """Related resource links"""
    packages_enabled: list[bool]
    """Whether packages are enabled"""
    empty_repo: list[bool]
    """Whether the repository is empty"""
    archived: list[bool]
    """Whether the project is archived"""
    visibility: list[str]
    """Visibility level of the project"""
    resolve_outdated_diff_discussions: list[bool]
    """Whether outdated diff discussions are auto-resolved"""
    container_registry_enabled: list[bool]
    """Whether container registry is enabled"""
    container_expiration_policy: list[dict[str, Any]]
    """Container expiration policy settings"""
    issues_enabled: list[bool]
    """Whether issues are enabled"""
    merge_requests_enabled: list[bool]
    """Whether merge requests are enabled"""
    wiki_enabled: list[bool]
    """Whether wiki is enabled"""
    jobs_enabled: list[bool]
    """Whether jobs are enabled"""
    snippets_enabled: list[bool]
    """Whether snippets are enabled"""
    service_desk_enabled: list[bool]
    """Whether service desk is enabled"""
    service_desk_address: list[str]
    """Email address for the service desk"""
    can_create_merge_request_in: list[bool]
    """Whether user can create merge requests"""
    issues_access_level: list[str]
    """Access level for issues"""
    repository_access_level: list[str]
    """Access level for the repository"""
    merge_requests_access_level: list[str]
    """Access level for merge requests"""
    forking_access_level: list[str]
    """Access level for forking"""
    wiki_access_level: list[str]
    """Access level for the wiki"""
    builds_access_level: list[str]
    """Access level for builds"""
    snippets_access_level: list[str]
    """Access level for snippets"""
    pages_access_level: list[str]
    """Access level for pages"""
    operations_access_level: list[str]
    """Access level for operations"""
    analytics_access_level: list[str]
    """Access level for analytics"""
    emails_disabled: list[bool]
    """Whether emails are disabled"""
    shared_runners_enabled: list[bool]
    """Whether shared runners are enabled"""
    lfs_enabled: list[bool]
    """Whether Git LFS is enabled"""
    creator_id: list[int]
    """ID of the project creator"""
    import_status: list[str]
    """Import status of the project"""
    open_issues_count: list[int]
    """Number of open issues"""
    ci_default_git_depth: list[int]
    """Default git depth for CI pipelines"""
    ci_forward_deployment_enabled: list[bool]
    """Whether CI forward deployment is enabled"""
    public_jobs: list[bool]
    """Whether jobs are public"""
    build_timeout: list[int]
    """Build timeout in seconds"""
    auto_cancel_pending_pipelines: list[str]
    """Auto-cancel pending pipelines setting"""
    ci_config_path: list[str]
    """Path to the CI configuration file"""
    shared_with_groups: list[list[Any]]
    """Groups the project is shared with"""
    only_allow_merge_if_pipeline_succeeds: list[bool]
    """Whether merge requires pipeline success"""
    allow_merge_on_skipped_pipeline: list[bool]
    """Whether merge is allowed on skipped pipeline"""
    restrict_user_defined_variables: list[bool]
    """Whether user-defined variables are restricted"""
    request_access_enabled: list[bool]
    """Whether access requests are enabled"""
    only_allow_merge_if_all_discussions_are_resolved: list[bool]
    """Whether merge requires all discussions resolved"""
    remove_source_branch_after_merge: list[bool]
    """Whether source branch is removed after merge"""
    printing_merge_request_link_enabled: list[bool]
    """Whether MR link printing is enabled"""
    merge_method: list[str]
    """Merge method used for the project"""
    statistics: list[dict[str, Any]]
    """Project statistics"""
    auto_devops_enabled: list[bool]
    """Whether Auto DevOps is enabled"""
    auto_devops_deploy_strategy: list[str]
    """Auto DevOps deployment strategy"""
    autoclose_referenced_issues: list[bool]
    """Whether referenced issues are auto-closed"""
    external_authorization_classification_label: list[str]
    """External authorization classification label"""
    requirements_enabled: list[bool]
    """Whether requirements are enabled"""
    security_and_compliance_enabled: list[bool]
    """Whether security and compliance is enabled"""
    compliance_frameworks: list[list[Any]]
    """Compliance frameworks for the project"""
    permissions: list[dict[str, Any]]
    """User permissions for the project"""
    keep_latest_artifact: list[bool]
    """Whether the latest artifact is kept"""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the project"""
    description: Any
    """Description of the project"""
    description_html: Any
    """HTML-rendered description of the project"""
    name: Any
    """Name of the project"""
    name_with_namespace: Any
    """Full name including namespace"""
    path: Any
    """URL path of the project"""
    path_with_namespace: Any
    """Full path including namespace"""
    created_at: Any
    """Timestamp when the project was created"""
    updated_at: Any
    """Timestamp when the project was last updated"""
    default_branch: Any
    """Default branch of the project"""
    tag_list: Any
    """List of tags for the project"""
    topics: Any
    """List of topics for the project"""
    ssh_url_to_repo: Any
    """SSH URL to the repository"""
    http_url_to_repo: Any
    """HTTP URL to the repository"""
    web_url: Any
    """Web URL of the project"""
    readme_url: Any
    """URL to the project README"""
    avatar_url: Any
    """URL of the project avatar"""
    forks_count: Any
    """Number of forks"""
    star_count: Any
    """Number of stars"""
    last_activity_at: Any
    """Timestamp of last activity"""
    namespace: Any
    """Namespace the project belongs to"""
    container_registry_image_prefix: Any
    """Prefix for container registry images"""
    links: Any
    """Related resource links"""
    packages_enabled: Any
    """Whether packages are enabled"""
    empty_repo: Any
    """Whether the repository is empty"""
    archived: Any
    """Whether the project is archived"""
    visibility: Any
    """Visibility level of the project"""
    resolve_outdated_diff_discussions: Any
    """Whether outdated diff discussions are auto-resolved"""
    container_registry_enabled: Any
    """Whether container registry is enabled"""
    container_expiration_policy: Any
    """Container expiration policy settings"""
    issues_enabled: Any
    """Whether issues are enabled"""
    merge_requests_enabled: Any
    """Whether merge requests are enabled"""
    wiki_enabled: Any
    """Whether wiki is enabled"""
    jobs_enabled: Any
    """Whether jobs are enabled"""
    snippets_enabled: Any
    """Whether snippets are enabled"""
    service_desk_enabled: Any
    """Whether service desk is enabled"""
    service_desk_address: Any
    """Email address for the service desk"""
    can_create_merge_request_in: Any
    """Whether user can create merge requests"""
    issues_access_level: Any
    """Access level for issues"""
    repository_access_level: Any
    """Access level for the repository"""
    merge_requests_access_level: Any
    """Access level for merge requests"""
    forking_access_level: Any
    """Access level for forking"""
    wiki_access_level: Any
    """Access level for the wiki"""
    builds_access_level: Any
    """Access level for builds"""
    snippets_access_level: Any
    """Access level for snippets"""
    pages_access_level: Any
    """Access level for pages"""
    operations_access_level: Any
    """Access level for operations"""
    analytics_access_level: Any
    """Access level for analytics"""
    emails_disabled: Any
    """Whether emails are disabled"""
    shared_runners_enabled: Any
    """Whether shared runners are enabled"""
    lfs_enabled: Any
    """Whether Git LFS is enabled"""
    creator_id: Any
    """ID of the project creator"""
    import_status: Any
    """Import status of the project"""
    open_issues_count: Any
    """Number of open issues"""
    ci_default_git_depth: Any
    """Default git depth for CI pipelines"""
    ci_forward_deployment_enabled: Any
    """Whether CI forward deployment is enabled"""
    public_jobs: Any
    """Whether jobs are public"""
    build_timeout: Any
    """Build timeout in seconds"""
    auto_cancel_pending_pipelines: Any
    """Auto-cancel pending pipelines setting"""
    ci_config_path: Any
    """Path to the CI configuration file"""
    shared_with_groups: Any
    """Groups the project is shared with"""
    only_allow_merge_if_pipeline_succeeds: Any
    """Whether merge requires pipeline success"""
    allow_merge_on_skipped_pipeline: Any
    """Whether merge is allowed on skipped pipeline"""
    restrict_user_defined_variables: Any
    """Whether user-defined variables are restricted"""
    request_access_enabled: Any
    """Whether access requests are enabled"""
    only_allow_merge_if_all_discussions_are_resolved: Any
    """Whether merge requires all discussions resolved"""
    remove_source_branch_after_merge: Any
    """Whether source branch is removed after merge"""
    printing_merge_request_link_enabled: Any
    """Whether MR link printing is enabled"""
    merge_method: Any
    """Merge method used for the project"""
    statistics: Any
    """Project statistics"""
    auto_devops_enabled: Any
    """Whether Auto DevOps is enabled"""
    auto_devops_deploy_strategy: Any
    """Auto DevOps deployment strategy"""
    autoclose_referenced_issues: Any
    """Whether referenced issues are auto-closed"""
    external_authorization_classification_label: Any
    """External authorization classification label"""
    requirements_enabled: Any
    """Whether requirements are enabled"""
    security_and_compliance_enabled: Any
    """Whether security and compliance is enabled"""
    compliance_frameworks: Any
    """Compliance frameworks for the project"""
    permissions: Any
    """User permissions for the project"""
    keep_latest_artifact: Any
    """Whether the latest artifact is kept"""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the project"""
    description: str
    """Description of the project"""
    description_html: str
    """HTML-rendered description of the project"""
    name: str
    """Name of the project"""
    name_with_namespace: str
    """Full name including namespace"""
    path: str
    """URL path of the project"""
    path_with_namespace: str
    """Full path including namespace"""
    created_at: str
    """Timestamp when the project was created"""
    updated_at: str
    """Timestamp when the project was last updated"""
    default_branch: str
    """Default branch of the project"""
    tag_list: str
    """List of tags for the project"""
    topics: str
    """List of topics for the project"""
    ssh_url_to_repo: str
    """SSH URL to the repository"""
    http_url_to_repo: str
    """HTTP URL to the repository"""
    web_url: str
    """Web URL of the project"""
    readme_url: str
    """URL to the project README"""
    avatar_url: str
    """URL of the project avatar"""
    forks_count: str
    """Number of forks"""
    star_count: str
    """Number of stars"""
    last_activity_at: str
    """Timestamp of last activity"""
    namespace: str
    """Namespace the project belongs to"""
    container_registry_image_prefix: str
    """Prefix for container registry images"""
    links: str
    """Related resource links"""
    packages_enabled: str
    """Whether packages are enabled"""
    empty_repo: str
    """Whether the repository is empty"""
    archived: str
    """Whether the project is archived"""
    visibility: str
    """Visibility level of the project"""
    resolve_outdated_diff_discussions: str
    """Whether outdated diff discussions are auto-resolved"""
    container_registry_enabled: str
    """Whether container registry is enabled"""
    container_expiration_policy: str
    """Container expiration policy settings"""
    issues_enabled: str
    """Whether issues are enabled"""
    merge_requests_enabled: str
    """Whether merge requests are enabled"""
    wiki_enabled: str
    """Whether wiki is enabled"""
    jobs_enabled: str
    """Whether jobs are enabled"""
    snippets_enabled: str
    """Whether snippets are enabled"""
    service_desk_enabled: str
    """Whether service desk is enabled"""
    service_desk_address: str
    """Email address for the service desk"""
    can_create_merge_request_in: str
    """Whether user can create merge requests"""
    issues_access_level: str
    """Access level for issues"""
    repository_access_level: str
    """Access level for the repository"""
    merge_requests_access_level: str
    """Access level for merge requests"""
    forking_access_level: str
    """Access level for forking"""
    wiki_access_level: str
    """Access level for the wiki"""
    builds_access_level: str
    """Access level for builds"""
    snippets_access_level: str
    """Access level for snippets"""
    pages_access_level: str
    """Access level for pages"""
    operations_access_level: str
    """Access level for operations"""
    analytics_access_level: str
    """Access level for analytics"""
    emails_disabled: str
    """Whether emails are disabled"""
    shared_runners_enabled: str
    """Whether shared runners are enabled"""
    lfs_enabled: str
    """Whether Git LFS is enabled"""
    creator_id: str
    """ID of the project creator"""
    import_status: str
    """Import status of the project"""
    open_issues_count: str
    """Number of open issues"""
    ci_default_git_depth: str
    """Default git depth for CI pipelines"""
    ci_forward_deployment_enabled: str
    """Whether CI forward deployment is enabled"""
    public_jobs: str
    """Whether jobs are public"""
    build_timeout: str
    """Build timeout in seconds"""
    auto_cancel_pending_pipelines: str
    """Auto-cancel pending pipelines setting"""
    ci_config_path: str
    """Path to the CI configuration file"""
    shared_with_groups: str
    """Groups the project is shared with"""
    only_allow_merge_if_pipeline_succeeds: str
    """Whether merge requires pipeline success"""
    allow_merge_on_skipped_pipeline: str
    """Whether merge is allowed on skipped pipeline"""
    restrict_user_defined_variables: str
    """Whether user-defined variables are restricted"""
    request_access_enabled: str
    """Whether access requests are enabled"""
    only_allow_merge_if_all_discussions_are_resolved: str
    """Whether merge requires all discussions resolved"""
    remove_source_branch_after_merge: str
    """Whether source branch is removed after merge"""
    printing_merge_request_link_enabled: str
    """Whether MR link printing is enabled"""
    merge_method: str
    """Merge method used for the project"""
    statistics: str
    """Project statistics"""
    auto_devops_enabled: str
    """Whether Auto DevOps is enabled"""
    auto_devops_deploy_strategy: str
    """Auto DevOps deployment strategy"""
    autoclose_referenced_issues: str
    """Whether referenced issues are auto-closed"""
    external_authorization_classification_label: str
    """External authorization classification label"""
    requirements_enabled: str
    """Whether requirements are enabled"""
    security_and_compliance_enabled: str
    """Whether security and compliance is enabled"""
    compliance_frameworks: str
    """Compliance frameworks for the project"""
    permissions: str
    """User permissions for the project"""
    keep_latest_artifact: str
    """Whether the latest artifact is kept"""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    id: AirbyteSortOrder
    """ID of the project"""
    description: AirbyteSortOrder
    """Description of the project"""
    description_html: AirbyteSortOrder
    """HTML-rendered description of the project"""
    name: AirbyteSortOrder
    """Name of the project"""
    name_with_namespace: AirbyteSortOrder
    """Full name including namespace"""
    path: AirbyteSortOrder
    """URL path of the project"""
    path_with_namespace: AirbyteSortOrder
    """Full path including namespace"""
    created_at: AirbyteSortOrder
    """Timestamp when the project was created"""
    updated_at: AirbyteSortOrder
    """Timestamp when the project was last updated"""
    default_branch: AirbyteSortOrder
    """Default branch of the project"""
    tag_list: AirbyteSortOrder
    """List of tags for the project"""
    topics: AirbyteSortOrder
    """List of topics for the project"""
    ssh_url_to_repo: AirbyteSortOrder
    """SSH URL to the repository"""
    http_url_to_repo: AirbyteSortOrder
    """HTTP URL to the repository"""
    web_url: AirbyteSortOrder
    """Web URL of the project"""
    readme_url: AirbyteSortOrder
    """URL to the project README"""
    avatar_url: AirbyteSortOrder
    """URL of the project avatar"""
    forks_count: AirbyteSortOrder
    """Number of forks"""
    star_count: AirbyteSortOrder
    """Number of stars"""
    last_activity_at: AirbyteSortOrder
    """Timestamp of last activity"""
    namespace: AirbyteSortOrder
    """Namespace the project belongs to"""
    container_registry_image_prefix: AirbyteSortOrder
    """Prefix for container registry images"""
    links: AirbyteSortOrder
    """Related resource links"""
    packages_enabled: AirbyteSortOrder
    """Whether packages are enabled"""
    empty_repo: AirbyteSortOrder
    """Whether the repository is empty"""
    archived: AirbyteSortOrder
    """Whether the project is archived"""
    visibility: AirbyteSortOrder
    """Visibility level of the project"""
    resolve_outdated_diff_discussions: AirbyteSortOrder
    """Whether outdated diff discussions are auto-resolved"""
    container_registry_enabled: AirbyteSortOrder
    """Whether container registry is enabled"""
    container_expiration_policy: AirbyteSortOrder
    """Container expiration policy settings"""
    issues_enabled: AirbyteSortOrder
    """Whether issues are enabled"""
    merge_requests_enabled: AirbyteSortOrder
    """Whether merge requests are enabled"""
    wiki_enabled: AirbyteSortOrder
    """Whether wiki is enabled"""
    jobs_enabled: AirbyteSortOrder
    """Whether jobs are enabled"""
    snippets_enabled: AirbyteSortOrder
    """Whether snippets are enabled"""
    service_desk_enabled: AirbyteSortOrder
    """Whether service desk is enabled"""
    service_desk_address: AirbyteSortOrder
    """Email address for the service desk"""
    can_create_merge_request_in: AirbyteSortOrder
    """Whether user can create merge requests"""
    issues_access_level: AirbyteSortOrder
    """Access level for issues"""
    repository_access_level: AirbyteSortOrder
    """Access level for the repository"""
    merge_requests_access_level: AirbyteSortOrder
    """Access level for merge requests"""
    forking_access_level: AirbyteSortOrder
    """Access level for forking"""
    wiki_access_level: AirbyteSortOrder
    """Access level for the wiki"""
    builds_access_level: AirbyteSortOrder
    """Access level for builds"""
    snippets_access_level: AirbyteSortOrder
    """Access level for snippets"""
    pages_access_level: AirbyteSortOrder
    """Access level for pages"""
    operations_access_level: AirbyteSortOrder
    """Access level for operations"""
    analytics_access_level: AirbyteSortOrder
    """Access level for analytics"""
    emails_disabled: AirbyteSortOrder
    """Whether emails are disabled"""
    shared_runners_enabled: AirbyteSortOrder
    """Whether shared runners are enabled"""
    lfs_enabled: AirbyteSortOrder
    """Whether Git LFS is enabled"""
    creator_id: AirbyteSortOrder
    """ID of the project creator"""
    import_status: AirbyteSortOrder
    """Import status of the project"""
    open_issues_count: AirbyteSortOrder
    """Number of open issues"""
    ci_default_git_depth: AirbyteSortOrder
    """Default git depth for CI pipelines"""
    ci_forward_deployment_enabled: AirbyteSortOrder
    """Whether CI forward deployment is enabled"""
    public_jobs: AirbyteSortOrder
    """Whether jobs are public"""
    build_timeout: AirbyteSortOrder
    """Build timeout in seconds"""
    auto_cancel_pending_pipelines: AirbyteSortOrder
    """Auto-cancel pending pipelines setting"""
    ci_config_path: AirbyteSortOrder
    """Path to the CI configuration file"""
    shared_with_groups: AirbyteSortOrder
    """Groups the project is shared with"""
    only_allow_merge_if_pipeline_succeeds: AirbyteSortOrder
    """Whether merge requires pipeline success"""
    allow_merge_on_skipped_pipeline: AirbyteSortOrder
    """Whether merge is allowed on skipped pipeline"""
    restrict_user_defined_variables: AirbyteSortOrder
    """Whether user-defined variables are restricted"""
    request_access_enabled: AirbyteSortOrder
    """Whether access requests are enabled"""
    only_allow_merge_if_all_discussions_are_resolved: AirbyteSortOrder
    """Whether merge requires all discussions resolved"""
    remove_source_branch_after_merge: AirbyteSortOrder
    """Whether source branch is removed after merge"""
    printing_merge_request_link_enabled: AirbyteSortOrder
    """Whether MR link printing is enabled"""
    merge_method: AirbyteSortOrder
    """Merge method used for the project"""
    statistics: AirbyteSortOrder
    """Project statistics"""
    auto_devops_enabled: AirbyteSortOrder
    """Whether Auto DevOps is enabled"""
    auto_devops_deploy_strategy: AirbyteSortOrder
    """Auto DevOps deployment strategy"""
    autoclose_referenced_issues: AirbyteSortOrder
    """Whether referenced issues are auto-closed"""
    external_authorization_classification_label: AirbyteSortOrder
    """External authorization classification label"""
    requirements_enabled: AirbyteSortOrder
    """Whether requirements are enabled"""
    security_and_compliance_enabled: AirbyteSortOrder
    """Whether security and compliance is enabled"""
    compliance_frameworks: AirbyteSortOrder
    """Compliance frameworks for the project"""
    permissions: AirbyteSortOrder
    """User permissions for the project"""
    keep_latest_artifact: AirbyteSortOrder
    """Whether the latest artifact is kept"""


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


# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    id: int | None
    """ID of the issue"""
    iid: int | None
    """Internal ID of the issue within the project"""
    project_id: int | None
    """ID of the project the issue belongs to"""
    title: str | None
    """Title of the issue"""
    description: str | None
    """Description of the issue"""
    state: str | None
    """State of the issue"""
    created_at: str | None
    """Timestamp when the issue was created"""
    updated_at: str | None
    """Timestamp when the issue was last updated"""
    closed_at: str | None
    """Timestamp when the issue was closed"""
    labels: list[Any] | None
    """Labels assigned to the issue"""
    assignees: list[Any] | None
    """Users assigned to the issue"""
    type_: str | None
    """Type of the issue"""
    user_notes_count: int | None
    """Number of user notes on the issue"""
    merge_requests_count: int | None
    """Number of related merge requests"""
    upvotes: int | None
    """Number of upvotes"""
    downvotes: int | None
    """Number of downvotes"""
    due_date: str | None
    """Due date for the issue"""
    confidential: bool | None
    """Whether the issue is confidential"""
    discussion_locked: bool | None
    """Whether discussion is locked"""
    issue_type: str | None
    """Type classification of the issue"""
    web_url: str | None
    """Web URL of the issue"""
    time_stats: dict[str, Any] | None
    """Time tracking statistics"""
    task_completion_status: dict[str, Any] | None
    """Task completion status"""
    blocking_issues_count: int | None
    """Number of blocking issues"""
    has_tasks: bool | None
    """Whether the issue has tasks"""
    links: dict[str, Any] | None
    """Related resource links"""
    references: dict[str, Any] | None
    """Issue references"""
    author: dict[str, Any] | None
    """Author of the issue"""
    author_id: int | None
    """ID of the author"""
    assignee: dict[str, Any] | None
    """Primary assignee of the issue"""
    assignee_id: int | None
    """ID of the primary assignee"""
    closed_by: dict[str, Any] | None
    """User who closed the issue"""
    closed_by_id: int | None
    """ID of the user who closed the issue"""
    milestone: dict[str, Any] | None
    """Milestone the issue belongs to"""
    milestone_id: int | None
    """ID of the milestone"""
    weight: int | None
    """Weight of the issue"""
    severity: str | None
    """Severity level of the issue"""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the issue"""
    iid: list[int]
    """Internal ID of the issue within the project"""
    project_id: list[int]
    """ID of the project the issue belongs to"""
    title: list[str]
    """Title of the issue"""
    description: list[str]
    """Description of the issue"""
    state: list[str]
    """State of the issue"""
    created_at: list[str]
    """Timestamp when the issue was created"""
    updated_at: list[str]
    """Timestamp when the issue was last updated"""
    closed_at: list[str]
    """Timestamp when the issue was closed"""
    labels: list[list[Any]]
    """Labels assigned to the issue"""
    assignees: list[list[Any]]
    """Users assigned to the issue"""
    type_: list[str]
    """Type of the issue"""
    user_notes_count: list[int]
    """Number of user notes on the issue"""
    merge_requests_count: list[int]
    """Number of related merge requests"""
    upvotes: list[int]
    """Number of upvotes"""
    downvotes: list[int]
    """Number of downvotes"""
    due_date: list[str]
    """Due date for the issue"""
    confidential: list[bool]
    """Whether the issue is confidential"""
    discussion_locked: list[bool]
    """Whether discussion is locked"""
    issue_type: list[str]
    """Type classification of the issue"""
    web_url: list[str]
    """Web URL of the issue"""
    time_stats: list[dict[str, Any]]
    """Time tracking statistics"""
    task_completion_status: list[dict[str, Any]]
    """Task completion status"""
    blocking_issues_count: list[int]
    """Number of blocking issues"""
    has_tasks: list[bool]
    """Whether the issue has tasks"""
    links: list[dict[str, Any]]
    """Related resource links"""
    references: list[dict[str, Any]]
    """Issue references"""
    author: list[dict[str, Any]]
    """Author of the issue"""
    author_id: list[int]
    """ID of the author"""
    assignee: list[dict[str, Any]]
    """Primary assignee of the issue"""
    assignee_id: list[int]
    """ID of the primary assignee"""
    closed_by: list[dict[str, Any]]
    """User who closed the issue"""
    closed_by_id: list[int]
    """ID of the user who closed the issue"""
    milestone: list[dict[str, Any]]
    """Milestone the issue belongs to"""
    milestone_id: list[int]
    """ID of the milestone"""
    weight: list[int]
    """Weight of the issue"""
    severity: list[str]
    """Severity level of the issue"""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the issue"""
    iid: Any
    """Internal ID of the issue within the project"""
    project_id: Any
    """ID of the project the issue belongs to"""
    title: Any
    """Title of the issue"""
    description: Any
    """Description of the issue"""
    state: Any
    """State of the issue"""
    created_at: Any
    """Timestamp when the issue was created"""
    updated_at: Any
    """Timestamp when the issue was last updated"""
    closed_at: Any
    """Timestamp when the issue was closed"""
    labels: Any
    """Labels assigned to the issue"""
    assignees: Any
    """Users assigned to the issue"""
    type_: Any
    """Type of the issue"""
    user_notes_count: Any
    """Number of user notes on the issue"""
    merge_requests_count: Any
    """Number of related merge requests"""
    upvotes: Any
    """Number of upvotes"""
    downvotes: Any
    """Number of downvotes"""
    due_date: Any
    """Due date for the issue"""
    confidential: Any
    """Whether the issue is confidential"""
    discussion_locked: Any
    """Whether discussion is locked"""
    issue_type: Any
    """Type classification of the issue"""
    web_url: Any
    """Web URL of the issue"""
    time_stats: Any
    """Time tracking statistics"""
    task_completion_status: Any
    """Task completion status"""
    blocking_issues_count: Any
    """Number of blocking issues"""
    has_tasks: Any
    """Whether the issue has tasks"""
    links: Any
    """Related resource links"""
    references: Any
    """Issue references"""
    author: Any
    """Author of the issue"""
    author_id: Any
    """ID of the author"""
    assignee: Any
    """Primary assignee of the issue"""
    assignee_id: Any
    """ID of the primary assignee"""
    closed_by: Any
    """User who closed the issue"""
    closed_by_id: Any
    """ID of the user who closed the issue"""
    milestone: Any
    """Milestone the issue belongs to"""
    milestone_id: Any
    """ID of the milestone"""
    weight: Any
    """Weight of the issue"""
    severity: Any
    """Severity level of the issue"""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the issue"""
    iid: str
    """Internal ID of the issue within the project"""
    project_id: str
    """ID of the project the issue belongs to"""
    title: str
    """Title of the issue"""
    description: str
    """Description of the issue"""
    state: str
    """State of the issue"""
    created_at: str
    """Timestamp when the issue was created"""
    updated_at: str
    """Timestamp when the issue was last updated"""
    closed_at: str
    """Timestamp when the issue was closed"""
    labels: str
    """Labels assigned to the issue"""
    assignees: str
    """Users assigned to the issue"""
    type_: str
    """Type of the issue"""
    user_notes_count: str
    """Number of user notes on the issue"""
    merge_requests_count: str
    """Number of related merge requests"""
    upvotes: str
    """Number of upvotes"""
    downvotes: str
    """Number of downvotes"""
    due_date: str
    """Due date for the issue"""
    confidential: str
    """Whether the issue is confidential"""
    discussion_locked: str
    """Whether discussion is locked"""
    issue_type: str
    """Type classification of the issue"""
    web_url: str
    """Web URL of the issue"""
    time_stats: str
    """Time tracking statistics"""
    task_completion_status: str
    """Task completion status"""
    blocking_issues_count: str
    """Number of blocking issues"""
    has_tasks: str
    """Whether the issue has tasks"""
    links: str
    """Related resource links"""
    references: str
    """Issue references"""
    author: str
    """Author of the issue"""
    author_id: str
    """ID of the author"""
    assignee: str
    """Primary assignee of the issue"""
    assignee_id: str
    """ID of the primary assignee"""
    closed_by: str
    """User who closed the issue"""
    closed_by_id: str
    """ID of the user who closed the issue"""
    milestone: str
    """Milestone the issue belongs to"""
    milestone_id: str
    """ID of the milestone"""
    weight: str
    """Weight of the issue"""
    severity: str
    """Severity level of the issue"""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    id: AirbyteSortOrder
    """ID of the issue"""
    iid: AirbyteSortOrder
    """Internal ID of the issue within the project"""
    project_id: AirbyteSortOrder
    """ID of the project the issue belongs to"""
    title: AirbyteSortOrder
    """Title of the issue"""
    description: AirbyteSortOrder
    """Description of the issue"""
    state: AirbyteSortOrder
    """State of the issue"""
    created_at: AirbyteSortOrder
    """Timestamp when the issue was created"""
    updated_at: AirbyteSortOrder
    """Timestamp when the issue was last updated"""
    closed_at: AirbyteSortOrder
    """Timestamp when the issue was closed"""
    labels: AirbyteSortOrder
    """Labels assigned to the issue"""
    assignees: AirbyteSortOrder
    """Users assigned to the issue"""
    type_: AirbyteSortOrder
    """Type of the issue"""
    user_notes_count: AirbyteSortOrder
    """Number of user notes on the issue"""
    merge_requests_count: AirbyteSortOrder
    """Number of related merge requests"""
    upvotes: AirbyteSortOrder
    """Number of upvotes"""
    downvotes: AirbyteSortOrder
    """Number of downvotes"""
    due_date: AirbyteSortOrder
    """Due date for the issue"""
    confidential: AirbyteSortOrder
    """Whether the issue is confidential"""
    discussion_locked: AirbyteSortOrder
    """Whether discussion is locked"""
    issue_type: AirbyteSortOrder
    """Type classification of the issue"""
    web_url: AirbyteSortOrder
    """Web URL of the issue"""
    time_stats: AirbyteSortOrder
    """Time tracking statistics"""
    task_completion_status: AirbyteSortOrder
    """Task completion status"""
    blocking_issues_count: AirbyteSortOrder
    """Number of blocking issues"""
    has_tasks: AirbyteSortOrder
    """Whether the issue has tasks"""
    links: AirbyteSortOrder
    """Related resource links"""
    references: AirbyteSortOrder
    """Issue references"""
    author: AirbyteSortOrder
    """Author of the issue"""
    author_id: AirbyteSortOrder
    """ID of the author"""
    assignee: AirbyteSortOrder
    """Primary assignee of the issue"""
    assignee_id: AirbyteSortOrder
    """ID of the primary assignee"""
    closed_by: AirbyteSortOrder
    """User who closed the issue"""
    closed_by_id: AirbyteSortOrder
    """ID of the user who closed the issue"""
    milestone: AirbyteSortOrder
    """Milestone the issue belongs to"""
    milestone_id: AirbyteSortOrder
    """ID of the milestone"""
    weight: AirbyteSortOrder
    """Weight of the issue"""
    severity: AirbyteSortOrder
    """Severity level of the issue"""


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


# ===== MERGE_REQUESTS SEARCH TYPES =====

class MergeRequestsSearchFilter(TypedDict, total=False):
    """Available fields for filtering merge_requests search queries."""
    id: int | None
    """ID of the merge request"""
    iid: int | None
    """Internal ID of the merge request within the project"""
    project_id: int | None
    """ID of the project"""
    title: str | None
    """Title of the merge request"""
    description: str | None
    """Description of the merge request"""
    state: str | None
    """State of the merge request"""
    created_at: str | None
    """Timestamp when the merge request was created"""
    updated_at: str | None
    """Timestamp when the merge request was last updated"""
    merged_at: str | None
    """Timestamp when the merge request was merged"""
    closed_at: str | None
    """Timestamp when the merge request was closed"""
    target_branch: str | None
    """Target branch for the merge request"""
    source_branch: str | None
    """Source branch for the merge request"""
    user_notes_count: int | None
    """Number of user notes"""
    upvotes: int | None
    """Number of upvotes"""
    downvotes: int | None
    """Number of downvotes"""
    assignees: list[Any] | None
    """Users assigned to the merge request"""
    reviewers: list[Any] | None
    """Users assigned as reviewers"""
    source_project_id: int | None
    """ID of the source project"""
    target_project_id: int | None
    """ID of the target project"""
    labels: list[Any] | None
    """Labels assigned to the merge request"""
    work_in_progress: bool | None
    """Whether the merge request is a work in progress"""
    merge_when_pipeline_succeeds: bool | None
    """Whether to merge when pipeline succeeds"""
    merge_status: str | None
    """Merge status of the merge request"""
    sha: str | None
    """SHA of the head commit"""
    merge_commit_sha: str | None
    """SHA of the merge commit"""
    squash_commit_sha: str | None
    """SHA of the squash commit"""
    discussion_locked: bool | None
    """Whether discussion is locked"""
    should_remove_source_branch: bool | None
    """Whether source branch should be removed"""
    force_remove_source_branch: bool | None
    """Whether to force remove source branch"""
    reference: str | None
    """Short reference for the merge request"""
    references: dict[str, Any] | None
    """Merge request references"""
    web_url: str | None
    """Web URL of the merge request"""
    time_stats: dict[str, Any] | None
    """Time tracking statistics"""
    squash: bool | None
    """Whether to squash commits on merge"""
    task_completion_status: dict[str, Any] | None
    """Task completion status"""
    has_conflicts: bool | None
    """Whether the merge request has conflicts"""
    blocking_discussions_resolved: bool | None
    """Whether blocking discussions are resolved"""
    author: dict[str, Any] | None
    """Author of the merge request"""
    author_id: int | None
    """ID of the author"""
    assignee: dict[str, Any] | None
    """Primary assignee of the merge request"""
    assignee_id: int | None
    """ID of the primary assignee"""
    closed_by: dict[str, Any] | None
    """User who closed the merge request"""
    closed_by_id: int | None
    """ID of the user who closed it"""
    milestone: dict[str, Any] | None
    """Milestone the merge request belongs to"""
    milestone_id: int | None
    """ID of the milestone"""
    merged_by: dict[str, Any] | None
    """User who merged the merge request"""
    merged_by_id: int | None
    """ID of the user who merged it"""
    draft: bool | None
    """Whether the merge request is a draft"""
    detailed_merge_status: str | None
    """Detailed merge status"""
    merge_user: dict[str, Any] | None
    """User who performed the merge"""


class MergeRequestsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the merge request"""
    iid: list[int]
    """Internal ID of the merge request within the project"""
    project_id: list[int]
    """ID of the project"""
    title: list[str]
    """Title of the merge request"""
    description: list[str]
    """Description of the merge request"""
    state: list[str]
    """State of the merge request"""
    created_at: list[str]
    """Timestamp when the merge request was created"""
    updated_at: list[str]
    """Timestamp when the merge request was last updated"""
    merged_at: list[str]
    """Timestamp when the merge request was merged"""
    closed_at: list[str]
    """Timestamp when the merge request was closed"""
    target_branch: list[str]
    """Target branch for the merge request"""
    source_branch: list[str]
    """Source branch for the merge request"""
    user_notes_count: list[int]
    """Number of user notes"""
    upvotes: list[int]
    """Number of upvotes"""
    downvotes: list[int]
    """Number of downvotes"""
    assignees: list[list[Any]]
    """Users assigned to the merge request"""
    reviewers: list[list[Any]]
    """Users assigned as reviewers"""
    source_project_id: list[int]
    """ID of the source project"""
    target_project_id: list[int]
    """ID of the target project"""
    labels: list[list[Any]]
    """Labels assigned to the merge request"""
    work_in_progress: list[bool]
    """Whether the merge request is a work in progress"""
    merge_when_pipeline_succeeds: list[bool]
    """Whether to merge when pipeline succeeds"""
    merge_status: list[str]
    """Merge status of the merge request"""
    sha: list[str]
    """SHA of the head commit"""
    merge_commit_sha: list[str]
    """SHA of the merge commit"""
    squash_commit_sha: list[str]
    """SHA of the squash commit"""
    discussion_locked: list[bool]
    """Whether discussion is locked"""
    should_remove_source_branch: list[bool]
    """Whether source branch should be removed"""
    force_remove_source_branch: list[bool]
    """Whether to force remove source branch"""
    reference: list[str]
    """Short reference for the merge request"""
    references: list[dict[str, Any]]
    """Merge request references"""
    web_url: list[str]
    """Web URL of the merge request"""
    time_stats: list[dict[str, Any]]
    """Time tracking statistics"""
    squash: list[bool]
    """Whether to squash commits on merge"""
    task_completion_status: list[dict[str, Any]]
    """Task completion status"""
    has_conflicts: list[bool]
    """Whether the merge request has conflicts"""
    blocking_discussions_resolved: list[bool]
    """Whether blocking discussions are resolved"""
    author: list[dict[str, Any]]
    """Author of the merge request"""
    author_id: list[int]
    """ID of the author"""
    assignee: list[dict[str, Any]]
    """Primary assignee of the merge request"""
    assignee_id: list[int]
    """ID of the primary assignee"""
    closed_by: list[dict[str, Any]]
    """User who closed the merge request"""
    closed_by_id: list[int]
    """ID of the user who closed it"""
    milestone: list[dict[str, Any]]
    """Milestone the merge request belongs to"""
    milestone_id: list[int]
    """ID of the milestone"""
    merged_by: list[dict[str, Any]]
    """User who merged the merge request"""
    merged_by_id: list[int]
    """ID of the user who merged it"""
    draft: list[bool]
    """Whether the merge request is a draft"""
    detailed_merge_status: list[str]
    """Detailed merge status"""
    merge_user: list[dict[str, Any]]
    """User who performed the merge"""


class MergeRequestsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the merge request"""
    iid: Any
    """Internal ID of the merge request within the project"""
    project_id: Any
    """ID of the project"""
    title: Any
    """Title of the merge request"""
    description: Any
    """Description of the merge request"""
    state: Any
    """State of the merge request"""
    created_at: Any
    """Timestamp when the merge request was created"""
    updated_at: Any
    """Timestamp when the merge request was last updated"""
    merged_at: Any
    """Timestamp when the merge request was merged"""
    closed_at: Any
    """Timestamp when the merge request was closed"""
    target_branch: Any
    """Target branch for the merge request"""
    source_branch: Any
    """Source branch for the merge request"""
    user_notes_count: Any
    """Number of user notes"""
    upvotes: Any
    """Number of upvotes"""
    downvotes: Any
    """Number of downvotes"""
    assignees: Any
    """Users assigned to the merge request"""
    reviewers: Any
    """Users assigned as reviewers"""
    source_project_id: Any
    """ID of the source project"""
    target_project_id: Any
    """ID of the target project"""
    labels: Any
    """Labels assigned to the merge request"""
    work_in_progress: Any
    """Whether the merge request is a work in progress"""
    merge_when_pipeline_succeeds: Any
    """Whether to merge when pipeline succeeds"""
    merge_status: Any
    """Merge status of the merge request"""
    sha: Any
    """SHA of the head commit"""
    merge_commit_sha: Any
    """SHA of the merge commit"""
    squash_commit_sha: Any
    """SHA of the squash commit"""
    discussion_locked: Any
    """Whether discussion is locked"""
    should_remove_source_branch: Any
    """Whether source branch should be removed"""
    force_remove_source_branch: Any
    """Whether to force remove source branch"""
    reference: Any
    """Short reference for the merge request"""
    references: Any
    """Merge request references"""
    web_url: Any
    """Web URL of the merge request"""
    time_stats: Any
    """Time tracking statistics"""
    squash: Any
    """Whether to squash commits on merge"""
    task_completion_status: Any
    """Task completion status"""
    has_conflicts: Any
    """Whether the merge request has conflicts"""
    blocking_discussions_resolved: Any
    """Whether blocking discussions are resolved"""
    author: Any
    """Author of the merge request"""
    author_id: Any
    """ID of the author"""
    assignee: Any
    """Primary assignee of the merge request"""
    assignee_id: Any
    """ID of the primary assignee"""
    closed_by: Any
    """User who closed the merge request"""
    closed_by_id: Any
    """ID of the user who closed it"""
    milestone: Any
    """Milestone the merge request belongs to"""
    milestone_id: Any
    """ID of the milestone"""
    merged_by: Any
    """User who merged the merge request"""
    merged_by_id: Any
    """ID of the user who merged it"""
    draft: Any
    """Whether the merge request is a draft"""
    detailed_merge_status: Any
    """Detailed merge status"""
    merge_user: Any
    """User who performed the merge"""


class MergeRequestsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the merge request"""
    iid: str
    """Internal ID of the merge request within the project"""
    project_id: str
    """ID of the project"""
    title: str
    """Title of the merge request"""
    description: str
    """Description of the merge request"""
    state: str
    """State of the merge request"""
    created_at: str
    """Timestamp when the merge request was created"""
    updated_at: str
    """Timestamp when the merge request was last updated"""
    merged_at: str
    """Timestamp when the merge request was merged"""
    closed_at: str
    """Timestamp when the merge request was closed"""
    target_branch: str
    """Target branch for the merge request"""
    source_branch: str
    """Source branch for the merge request"""
    user_notes_count: str
    """Number of user notes"""
    upvotes: str
    """Number of upvotes"""
    downvotes: str
    """Number of downvotes"""
    assignees: str
    """Users assigned to the merge request"""
    reviewers: str
    """Users assigned as reviewers"""
    source_project_id: str
    """ID of the source project"""
    target_project_id: str
    """ID of the target project"""
    labels: str
    """Labels assigned to the merge request"""
    work_in_progress: str
    """Whether the merge request is a work in progress"""
    merge_when_pipeline_succeeds: str
    """Whether to merge when pipeline succeeds"""
    merge_status: str
    """Merge status of the merge request"""
    sha: str
    """SHA of the head commit"""
    merge_commit_sha: str
    """SHA of the merge commit"""
    squash_commit_sha: str
    """SHA of the squash commit"""
    discussion_locked: str
    """Whether discussion is locked"""
    should_remove_source_branch: str
    """Whether source branch should be removed"""
    force_remove_source_branch: str
    """Whether to force remove source branch"""
    reference: str
    """Short reference for the merge request"""
    references: str
    """Merge request references"""
    web_url: str
    """Web URL of the merge request"""
    time_stats: str
    """Time tracking statistics"""
    squash: str
    """Whether to squash commits on merge"""
    task_completion_status: str
    """Task completion status"""
    has_conflicts: str
    """Whether the merge request has conflicts"""
    blocking_discussions_resolved: str
    """Whether blocking discussions are resolved"""
    author: str
    """Author of the merge request"""
    author_id: str
    """ID of the author"""
    assignee: str
    """Primary assignee of the merge request"""
    assignee_id: str
    """ID of the primary assignee"""
    closed_by: str
    """User who closed the merge request"""
    closed_by_id: str
    """ID of the user who closed it"""
    milestone: str
    """Milestone the merge request belongs to"""
    milestone_id: str
    """ID of the milestone"""
    merged_by: str
    """User who merged the merge request"""
    merged_by_id: str
    """ID of the user who merged it"""
    draft: str
    """Whether the merge request is a draft"""
    detailed_merge_status: str
    """Detailed merge status"""
    merge_user: str
    """User who performed the merge"""


class MergeRequestsSortFilter(TypedDict, total=False):
    """Available fields for sorting merge_requests search results."""
    id: AirbyteSortOrder
    """ID of the merge request"""
    iid: AirbyteSortOrder
    """Internal ID of the merge request within the project"""
    project_id: AirbyteSortOrder
    """ID of the project"""
    title: AirbyteSortOrder
    """Title of the merge request"""
    description: AirbyteSortOrder
    """Description of the merge request"""
    state: AirbyteSortOrder
    """State of the merge request"""
    created_at: AirbyteSortOrder
    """Timestamp when the merge request was created"""
    updated_at: AirbyteSortOrder
    """Timestamp when the merge request was last updated"""
    merged_at: AirbyteSortOrder
    """Timestamp when the merge request was merged"""
    closed_at: AirbyteSortOrder
    """Timestamp when the merge request was closed"""
    target_branch: AirbyteSortOrder
    """Target branch for the merge request"""
    source_branch: AirbyteSortOrder
    """Source branch for the merge request"""
    user_notes_count: AirbyteSortOrder
    """Number of user notes"""
    upvotes: AirbyteSortOrder
    """Number of upvotes"""
    downvotes: AirbyteSortOrder
    """Number of downvotes"""
    assignees: AirbyteSortOrder
    """Users assigned to the merge request"""
    reviewers: AirbyteSortOrder
    """Users assigned as reviewers"""
    source_project_id: AirbyteSortOrder
    """ID of the source project"""
    target_project_id: AirbyteSortOrder
    """ID of the target project"""
    labels: AirbyteSortOrder
    """Labels assigned to the merge request"""
    work_in_progress: AirbyteSortOrder
    """Whether the merge request is a work in progress"""
    merge_when_pipeline_succeeds: AirbyteSortOrder
    """Whether to merge when pipeline succeeds"""
    merge_status: AirbyteSortOrder
    """Merge status of the merge request"""
    sha: AirbyteSortOrder
    """SHA of the head commit"""
    merge_commit_sha: AirbyteSortOrder
    """SHA of the merge commit"""
    squash_commit_sha: AirbyteSortOrder
    """SHA of the squash commit"""
    discussion_locked: AirbyteSortOrder
    """Whether discussion is locked"""
    should_remove_source_branch: AirbyteSortOrder
    """Whether source branch should be removed"""
    force_remove_source_branch: AirbyteSortOrder
    """Whether to force remove source branch"""
    reference: AirbyteSortOrder
    """Short reference for the merge request"""
    references: AirbyteSortOrder
    """Merge request references"""
    web_url: AirbyteSortOrder
    """Web URL of the merge request"""
    time_stats: AirbyteSortOrder
    """Time tracking statistics"""
    squash: AirbyteSortOrder
    """Whether to squash commits on merge"""
    task_completion_status: AirbyteSortOrder
    """Task completion status"""
    has_conflicts: AirbyteSortOrder
    """Whether the merge request has conflicts"""
    blocking_discussions_resolved: AirbyteSortOrder
    """Whether blocking discussions are resolved"""
    author: AirbyteSortOrder
    """Author of the merge request"""
    author_id: AirbyteSortOrder
    """ID of the author"""
    assignee: AirbyteSortOrder
    """Primary assignee of the merge request"""
    assignee_id: AirbyteSortOrder
    """ID of the primary assignee"""
    closed_by: AirbyteSortOrder
    """User who closed the merge request"""
    closed_by_id: AirbyteSortOrder
    """ID of the user who closed it"""
    milestone: AirbyteSortOrder
    """Milestone the merge request belongs to"""
    milestone_id: AirbyteSortOrder
    """ID of the milestone"""
    merged_by: AirbyteSortOrder
    """User who merged the merge request"""
    merged_by_id: AirbyteSortOrder
    """ID of the user who merged it"""
    draft: AirbyteSortOrder
    """Whether the merge request is a draft"""
    detailed_merge_status: AirbyteSortOrder
    """Detailed merge status"""
    merge_user: AirbyteSortOrder
    """User who performed the merge"""


# Entity-specific condition types for merge_requests
class MergeRequestsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MergeRequestsSearchFilter


class MergeRequestsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MergeRequestsSearchFilter


class MergeRequestsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MergeRequestsSearchFilter


class MergeRequestsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MergeRequestsSearchFilter


class MergeRequestsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MergeRequestsSearchFilter


class MergeRequestsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MergeRequestsSearchFilter


class MergeRequestsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MergeRequestsStringFilter


class MergeRequestsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MergeRequestsStringFilter


class MergeRequestsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MergeRequestsStringFilter


class MergeRequestsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MergeRequestsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MergeRequestsInCondition = TypedDict("MergeRequestsInCondition", {"in": MergeRequestsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MergeRequestsNotCondition = TypedDict("MergeRequestsNotCondition", {"not": "MergeRequestsCondition"}, total=False)
"""Negates the nested condition."""

MergeRequestsAndCondition = TypedDict("MergeRequestsAndCondition", {"and": "list[MergeRequestsCondition]"}, total=False)
"""True if all nested conditions are true."""

MergeRequestsOrCondition = TypedDict("MergeRequestsOrCondition", {"or": "list[MergeRequestsCondition]"}, total=False)
"""True if any nested condition is true."""

MergeRequestsAnyCondition = TypedDict("MergeRequestsAnyCondition", {"any": MergeRequestsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all merge_requests condition types
MergeRequestsCondition = (
    MergeRequestsEqCondition
    | MergeRequestsNeqCondition
    | MergeRequestsGtCondition
    | MergeRequestsGteCondition
    | MergeRequestsLtCondition
    | MergeRequestsLteCondition
    | MergeRequestsInCondition
    | MergeRequestsLikeCondition
    | MergeRequestsFuzzyCondition
    | MergeRequestsKeywordCondition
    | MergeRequestsContainsCondition
    | MergeRequestsNotCondition
    | MergeRequestsAndCondition
    | MergeRequestsOrCondition
    | MergeRequestsAnyCondition
)


class MergeRequestsSearchQuery(TypedDict, total=False):
    """Search query for merge_requests entity."""
    filter: MergeRequestsCondition
    sort: list[MergeRequestsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    id: int | None
    """ID of the user"""
    name: str | None
    """Full name of the user"""
    username: str | None
    """Username of the user"""
    state: str | None
    """State of the user account"""
    avatar_url: str | None
    """URL of the user avatar"""
    web_url: str | None
    """Web URL of the user profile"""
    locked: bool | None
    """Whether the user account is locked"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the user"""
    name: list[str]
    """Full name of the user"""
    username: list[str]
    """Username of the user"""
    state: list[str]
    """State of the user account"""
    avatar_url: list[str]
    """URL of the user avatar"""
    web_url: list[str]
    """Web URL of the user profile"""
    locked: list[bool]
    """Whether the user account is locked"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the user"""
    name: Any
    """Full name of the user"""
    username: Any
    """Username of the user"""
    state: Any
    """State of the user account"""
    avatar_url: Any
    """URL of the user avatar"""
    web_url: Any
    """Web URL of the user profile"""
    locked: Any
    """Whether the user account is locked"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the user"""
    name: str
    """Full name of the user"""
    username: str
    """Username of the user"""
    state: str
    """State of the user account"""
    avatar_url: str
    """URL of the user avatar"""
    web_url: str
    """Web URL of the user profile"""
    locked: str
    """Whether the user account is locked"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    id: AirbyteSortOrder
    """ID of the user"""
    name: AirbyteSortOrder
    """Full name of the user"""
    username: AirbyteSortOrder
    """Username of the user"""
    state: AirbyteSortOrder
    """State of the user account"""
    avatar_url: AirbyteSortOrder
    """URL of the user avatar"""
    web_url: AirbyteSortOrder
    """Web URL of the user profile"""
    locked: AirbyteSortOrder
    """Whether the user account is locked"""


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


# ===== COMMITS SEARCH TYPES =====

class CommitsSearchFilter(TypedDict, total=False):
    """Available fields for filtering commits search queries."""
    project_id: int | None
    """ID of the project the commit belongs to"""
    id: str | None
    """SHA of the commit"""
    short_id: str | None
    """Short SHA of the commit"""
    created_at: str | None
    """Timestamp when the commit was created"""
    parent_ids: list[Any] | None
    """SHAs of parent commits"""
    title: str | None
    """Title of the commit"""
    message: str | None
    """Full commit message"""
    author_name: str | None
    """Name of the commit author"""
    author_email: str | None
    """Email of the commit author"""
    authored_date: str | None
    """Date the commit was authored"""
    committer_name: str | None
    """Name of the committer"""
    committer_email: str | None
    """Email of the committer"""
    committed_date: str | None
    """Date the commit was committed"""
    trailers: dict[str, Any] | None
    """Git trailers for the commit"""
    web_url: str | None
    """Web URL of the commit"""
    stats: dict[str, Any] | None
    """Commit statistics"""


class CommitsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    project_id: list[int]
    """ID of the project the commit belongs to"""
    id: list[str]
    """SHA of the commit"""
    short_id: list[str]
    """Short SHA of the commit"""
    created_at: list[str]
    """Timestamp when the commit was created"""
    parent_ids: list[list[Any]]
    """SHAs of parent commits"""
    title: list[str]
    """Title of the commit"""
    message: list[str]
    """Full commit message"""
    author_name: list[str]
    """Name of the commit author"""
    author_email: list[str]
    """Email of the commit author"""
    authored_date: list[str]
    """Date the commit was authored"""
    committer_name: list[str]
    """Name of the committer"""
    committer_email: list[str]
    """Email of the committer"""
    committed_date: list[str]
    """Date the commit was committed"""
    trailers: list[dict[str, Any]]
    """Git trailers for the commit"""
    web_url: list[str]
    """Web URL of the commit"""
    stats: list[dict[str, Any]]
    """Commit statistics"""


class CommitsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    project_id: Any
    """ID of the project the commit belongs to"""
    id: Any
    """SHA of the commit"""
    short_id: Any
    """Short SHA of the commit"""
    created_at: Any
    """Timestamp when the commit was created"""
    parent_ids: Any
    """SHAs of parent commits"""
    title: Any
    """Title of the commit"""
    message: Any
    """Full commit message"""
    author_name: Any
    """Name of the commit author"""
    author_email: Any
    """Email of the commit author"""
    authored_date: Any
    """Date the commit was authored"""
    committer_name: Any
    """Name of the committer"""
    committer_email: Any
    """Email of the committer"""
    committed_date: Any
    """Date the commit was committed"""
    trailers: Any
    """Git trailers for the commit"""
    web_url: Any
    """Web URL of the commit"""
    stats: Any
    """Commit statistics"""


class CommitsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    project_id: str
    """ID of the project the commit belongs to"""
    id: str
    """SHA of the commit"""
    short_id: str
    """Short SHA of the commit"""
    created_at: str
    """Timestamp when the commit was created"""
    parent_ids: str
    """SHAs of parent commits"""
    title: str
    """Title of the commit"""
    message: str
    """Full commit message"""
    author_name: str
    """Name of the commit author"""
    author_email: str
    """Email of the commit author"""
    authored_date: str
    """Date the commit was authored"""
    committer_name: str
    """Name of the committer"""
    committer_email: str
    """Email of the committer"""
    committed_date: str
    """Date the commit was committed"""
    trailers: str
    """Git trailers for the commit"""
    web_url: str
    """Web URL of the commit"""
    stats: str
    """Commit statistics"""


class CommitsSortFilter(TypedDict, total=False):
    """Available fields for sorting commits search results."""
    project_id: AirbyteSortOrder
    """ID of the project the commit belongs to"""
    id: AirbyteSortOrder
    """SHA of the commit"""
    short_id: AirbyteSortOrder
    """Short SHA of the commit"""
    created_at: AirbyteSortOrder
    """Timestamp when the commit was created"""
    parent_ids: AirbyteSortOrder
    """SHAs of parent commits"""
    title: AirbyteSortOrder
    """Title of the commit"""
    message: AirbyteSortOrder
    """Full commit message"""
    author_name: AirbyteSortOrder
    """Name of the commit author"""
    author_email: AirbyteSortOrder
    """Email of the commit author"""
    authored_date: AirbyteSortOrder
    """Date the commit was authored"""
    committer_name: AirbyteSortOrder
    """Name of the committer"""
    committer_email: AirbyteSortOrder
    """Email of the committer"""
    committed_date: AirbyteSortOrder
    """Date the commit was committed"""
    trailers: AirbyteSortOrder
    """Git trailers for the commit"""
    web_url: AirbyteSortOrder
    """Web URL of the commit"""
    stats: AirbyteSortOrder
    """Commit statistics"""


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


# ===== GROUPS SEARCH TYPES =====

class GroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering groups search queries."""
    id: int | None
    """ID of the group"""
    web_url: str | None
    """Web URL of the group"""
    name: str | None
    """Name of the group"""
    path: str | None
    """URL path of the group"""
    description: str | None
    """Description of the group"""
    visibility: str | None
    """Visibility level of the group"""
    share_with_group_lock: bool | None
    """Whether sharing with other groups is locked"""
    require_two_factor_authentication: bool | None
    """Whether two-factor authentication is required"""
    two_factor_grace_period: int | None
    """Grace period for two-factor authentication"""
    project_creation_level: str | None
    """Level required to create projects"""
    auto_devops_enabled: bool | None
    """Whether Auto DevOps is enabled"""
    subgroup_creation_level: str | None
    """Level required to create subgroups"""
    emails_disabled: bool | None
    """Whether emails are disabled"""
    emails_enabled: bool | None
    """Whether emails are enabled"""
    mentions_disabled: bool | None
    """Whether mentions are disabled"""
    lfs_enabled: bool | None
    """Whether Git LFS is enabled"""
    default_branch_protection: int | None
    """Default branch protection level"""
    avatar_url: str | None
    """URL of the group avatar"""
    request_access_enabled: bool | None
    """Whether access requests are enabled"""
    full_name: str | None
    """Full name of the group"""
    full_path: str | None
    """Full path of the group"""
    created_at: str | None
    """Timestamp when the group was created"""
    parent_id: int | None
    """ID of the parent group"""
    shared_with_groups: list[Any] | None
    """Groups this group is shared with"""
    projects: list[Any] | None
    """Projects in the group"""


class GroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the group"""
    web_url: list[str]
    """Web URL of the group"""
    name: list[str]
    """Name of the group"""
    path: list[str]
    """URL path of the group"""
    description: list[str]
    """Description of the group"""
    visibility: list[str]
    """Visibility level of the group"""
    share_with_group_lock: list[bool]
    """Whether sharing with other groups is locked"""
    require_two_factor_authentication: list[bool]
    """Whether two-factor authentication is required"""
    two_factor_grace_period: list[int]
    """Grace period for two-factor authentication"""
    project_creation_level: list[str]
    """Level required to create projects"""
    auto_devops_enabled: list[bool]
    """Whether Auto DevOps is enabled"""
    subgroup_creation_level: list[str]
    """Level required to create subgroups"""
    emails_disabled: list[bool]
    """Whether emails are disabled"""
    emails_enabled: list[bool]
    """Whether emails are enabled"""
    mentions_disabled: list[bool]
    """Whether mentions are disabled"""
    lfs_enabled: list[bool]
    """Whether Git LFS is enabled"""
    default_branch_protection: list[int]
    """Default branch protection level"""
    avatar_url: list[str]
    """URL of the group avatar"""
    request_access_enabled: list[bool]
    """Whether access requests are enabled"""
    full_name: list[str]
    """Full name of the group"""
    full_path: list[str]
    """Full path of the group"""
    created_at: list[str]
    """Timestamp when the group was created"""
    parent_id: list[int]
    """ID of the parent group"""
    shared_with_groups: list[list[Any]]
    """Groups this group is shared with"""
    projects: list[list[Any]]
    """Projects in the group"""


class GroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the group"""
    web_url: Any
    """Web URL of the group"""
    name: Any
    """Name of the group"""
    path: Any
    """URL path of the group"""
    description: Any
    """Description of the group"""
    visibility: Any
    """Visibility level of the group"""
    share_with_group_lock: Any
    """Whether sharing with other groups is locked"""
    require_two_factor_authentication: Any
    """Whether two-factor authentication is required"""
    two_factor_grace_period: Any
    """Grace period for two-factor authentication"""
    project_creation_level: Any
    """Level required to create projects"""
    auto_devops_enabled: Any
    """Whether Auto DevOps is enabled"""
    subgroup_creation_level: Any
    """Level required to create subgroups"""
    emails_disabled: Any
    """Whether emails are disabled"""
    emails_enabled: Any
    """Whether emails are enabled"""
    mentions_disabled: Any
    """Whether mentions are disabled"""
    lfs_enabled: Any
    """Whether Git LFS is enabled"""
    default_branch_protection: Any
    """Default branch protection level"""
    avatar_url: Any
    """URL of the group avatar"""
    request_access_enabled: Any
    """Whether access requests are enabled"""
    full_name: Any
    """Full name of the group"""
    full_path: Any
    """Full path of the group"""
    created_at: Any
    """Timestamp when the group was created"""
    parent_id: Any
    """ID of the parent group"""
    shared_with_groups: Any
    """Groups this group is shared with"""
    projects: Any
    """Projects in the group"""


class GroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the group"""
    web_url: str
    """Web URL of the group"""
    name: str
    """Name of the group"""
    path: str
    """URL path of the group"""
    description: str
    """Description of the group"""
    visibility: str
    """Visibility level of the group"""
    share_with_group_lock: str
    """Whether sharing with other groups is locked"""
    require_two_factor_authentication: str
    """Whether two-factor authentication is required"""
    two_factor_grace_period: str
    """Grace period for two-factor authentication"""
    project_creation_level: str
    """Level required to create projects"""
    auto_devops_enabled: str
    """Whether Auto DevOps is enabled"""
    subgroup_creation_level: str
    """Level required to create subgroups"""
    emails_disabled: str
    """Whether emails are disabled"""
    emails_enabled: str
    """Whether emails are enabled"""
    mentions_disabled: str
    """Whether mentions are disabled"""
    lfs_enabled: str
    """Whether Git LFS is enabled"""
    default_branch_protection: str
    """Default branch protection level"""
    avatar_url: str
    """URL of the group avatar"""
    request_access_enabled: str
    """Whether access requests are enabled"""
    full_name: str
    """Full name of the group"""
    full_path: str
    """Full path of the group"""
    created_at: str
    """Timestamp when the group was created"""
    parent_id: str
    """ID of the parent group"""
    shared_with_groups: str
    """Groups this group is shared with"""
    projects: str
    """Projects in the group"""


class GroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting groups search results."""
    id: AirbyteSortOrder
    """ID of the group"""
    web_url: AirbyteSortOrder
    """Web URL of the group"""
    name: AirbyteSortOrder
    """Name of the group"""
    path: AirbyteSortOrder
    """URL path of the group"""
    description: AirbyteSortOrder
    """Description of the group"""
    visibility: AirbyteSortOrder
    """Visibility level of the group"""
    share_with_group_lock: AirbyteSortOrder
    """Whether sharing with other groups is locked"""
    require_two_factor_authentication: AirbyteSortOrder
    """Whether two-factor authentication is required"""
    two_factor_grace_period: AirbyteSortOrder
    """Grace period for two-factor authentication"""
    project_creation_level: AirbyteSortOrder
    """Level required to create projects"""
    auto_devops_enabled: AirbyteSortOrder
    """Whether Auto DevOps is enabled"""
    subgroup_creation_level: AirbyteSortOrder
    """Level required to create subgroups"""
    emails_disabled: AirbyteSortOrder
    """Whether emails are disabled"""
    emails_enabled: AirbyteSortOrder
    """Whether emails are enabled"""
    mentions_disabled: AirbyteSortOrder
    """Whether mentions are disabled"""
    lfs_enabled: AirbyteSortOrder
    """Whether Git LFS is enabled"""
    default_branch_protection: AirbyteSortOrder
    """Default branch protection level"""
    avatar_url: AirbyteSortOrder
    """URL of the group avatar"""
    request_access_enabled: AirbyteSortOrder
    """Whether access requests are enabled"""
    full_name: AirbyteSortOrder
    """Full name of the group"""
    full_path: AirbyteSortOrder
    """Full path of the group"""
    created_at: AirbyteSortOrder
    """Timestamp when the group was created"""
    parent_id: AirbyteSortOrder
    """ID of the parent group"""
    shared_with_groups: AirbyteSortOrder
    """Groups this group is shared with"""
    projects: AirbyteSortOrder
    """Projects in the group"""


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


# ===== BRANCHES SEARCH TYPES =====

class BranchesSearchFilter(TypedDict, total=False):
    """Available fields for filtering branches search queries."""
    project_id: int | None
    """ID of the project the branch belongs to"""
    name: str | None
    """Name of the branch"""
    merged: bool | None
    """Whether the branch is merged"""
    protected: bool | None
    """Whether the branch is protected"""
    developers_can_push: bool | None
    """Whether developers can push to the branch"""
    developers_can_merge: bool | None
    """Whether developers can merge into the branch"""
    can_push: bool | None
    """Whether the current user can push"""
    default: bool | None
    """Whether this is the default branch"""
    web_url: str | None
    """Web URL of the branch"""
    commit_id: str | None
    """SHA of the head commit"""
    commit: dict[str, Any] | None
    """Head commit details"""


class BranchesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    project_id: list[int]
    """ID of the project the branch belongs to"""
    name: list[str]
    """Name of the branch"""
    merged: list[bool]
    """Whether the branch is merged"""
    protected: list[bool]
    """Whether the branch is protected"""
    developers_can_push: list[bool]
    """Whether developers can push to the branch"""
    developers_can_merge: list[bool]
    """Whether developers can merge into the branch"""
    can_push: list[bool]
    """Whether the current user can push"""
    default: list[bool]
    """Whether this is the default branch"""
    web_url: list[str]
    """Web URL of the branch"""
    commit_id: list[str]
    """SHA of the head commit"""
    commit: list[dict[str, Any]]
    """Head commit details"""


class BranchesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    project_id: Any
    """ID of the project the branch belongs to"""
    name: Any
    """Name of the branch"""
    merged: Any
    """Whether the branch is merged"""
    protected: Any
    """Whether the branch is protected"""
    developers_can_push: Any
    """Whether developers can push to the branch"""
    developers_can_merge: Any
    """Whether developers can merge into the branch"""
    can_push: Any
    """Whether the current user can push"""
    default: Any
    """Whether this is the default branch"""
    web_url: Any
    """Web URL of the branch"""
    commit_id: Any
    """SHA of the head commit"""
    commit: Any
    """Head commit details"""


class BranchesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    project_id: str
    """ID of the project the branch belongs to"""
    name: str
    """Name of the branch"""
    merged: str
    """Whether the branch is merged"""
    protected: str
    """Whether the branch is protected"""
    developers_can_push: str
    """Whether developers can push to the branch"""
    developers_can_merge: str
    """Whether developers can merge into the branch"""
    can_push: str
    """Whether the current user can push"""
    default: str
    """Whether this is the default branch"""
    web_url: str
    """Web URL of the branch"""
    commit_id: str
    """SHA of the head commit"""
    commit: str
    """Head commit details"""


class BranchesSortFilter(TypedDict, total=False):
    """Available fields for sorting branches search results."""
    project_id: AirbyteSortOrder
    """ID of the project the branch belongs to"""
    name: AirbyteSortOrder
    """Name of the branch"""
    merged: AirbyteSortOrder
    """Whether the branch is merged"""
    protected: AirbyteSortOrder
    """Whether the branch is protected"""
    developers_can_push: AirbyteSortOrder
    """Whether developers can push to the branch"""
    developers_can_merge: AirbyteSortOrder
    """Whether developers can merge into the branch"""
    can_push: AirbyteSortOrder
    """Whether the current user can push"""
    default: AirbyteSortOrder
    """Whether this is the default branch"""
    web_url: AirbyteSortOrder
    """Web URL of the branch"""
    commit_id: AirbyteSortOrder
    """SHA of the head commit"""
    commit: AirbyteSortOrder
    """Head commit details"""


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


# ===== PIPELINES SEARCH TYPES =====

class PipelinesSearchFilter(TypedDict, total=False):
    """Available fields for filtering pipelines search queries."""
    id: int | None
    """ID of the pipeline"""
    iid: int | None
    """Internal ID of the pipeline within the project"""
    project_id: int | None
    """ID of the project"""
    sha: str | None
    """SHA of the commit that triggered the pipeline"""
    source: str | None
    """Source that triggered the pipeline"""
    ref: str | None
    """Branch or tag that triggered the pipeline"""
    status: str | None
    """Status of the pipeline"""
    created_at: str | None
    """Timestamp when the pipeline was created"""
    updated_at: str | None
    """Timestamp when the pipeline was last updated"""
    web_url: str | None
    """Web URL of the pipeline"""
    name: str | None
    """Name of the pipeline"""


class PipelinesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the pipeline"""
    iid: list[int]
    """Internal ID of the pipeline within the project"""
    project_id: list[int]
    """ID of the project"""
    sha: list[str]
    """SHA of the commit that triggered the pipeline"""
    source: list[str]
    """Source that triggered the pipeline"""
    ref: list[str]
    """Branch or tag that triggered the pipeline"""
    status: list[str]
    """Status of the pipeline"""
    created_at: list[str]
    """Timestamp when the pipeline was created"""
    updated_at: list[str]
    """Timestamp when the pipeline was last updated"""
    web_url: list[str]
    """Web URL of the pipeline"""
    name: list[str]
    """Name of the pipeline"""


class PipelinesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the pipeline"""
    iid: Any
    """Internal ID of the pipeline within the project"""
    project_id: Any
    """ID of the project"""
    sha: Any
    """SHA of the commit that triggered the pipeline"""
    source: Any
    """Source that triggered the pipeline"""
    ref: Any
    """Branch or tag that triggered the pipeline"""
    status: Any
    """Status of the pipeline"""
    created_at: Any
    """Timestamp when the pipeline was created"""
    updated_at: Any
    """Timestamp when the pipeline was last updated"""
    web_url: Any
    """Web URL of the pipeline"""
    name: Any
    """Name of the pipeline"""


class PipelinesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the pipeline"""
    iid: str
    """Internal ID of the pipeline within the project"""
    project_id: str
    """ID of the project"""
    sha: str
    """SHA of the commit that triggered the pipeline"""
    source: str
    """Source that triggered the pipeline"""
    ref: str
    """Branch or tag that triggered the pipeline"""
    status: str
    """Status of the pipeline"""
    created_at: str
    """Timestamp when the pipeline was created"""
    updated_at: str
    """Timestamp when the pipeline was last updated"""
    web_url: str
    """Web URL of the pipeline"""
    name: str
    """Name of the pipeline"""


class PipelinesSortFilter(TypedDict, total=False):
    """Available fields for sorting pipelines search results."""
    id: AirbyteSortOrder
    """ID of the pipeline"""
    iid: AirbyteSortOrder
    """Internal ID of the pipeline within the project"""
    project_id: AirbyteSortOrder
    """ID of the project"""
    sha: AirbyteSortOrder
    """SHA of the commit that triggered the pipeline"""
    source: AirbyteSortOrder
    """Source that triggered the pipeline"""
    ref: AirbyteSortOrder
    """Branch or tag that triggered the pipeline"""
    status: AirbyteSortOrder
    """Status of the pipeline"""
    created_at: AirbyteSortOrder
    """Timestamp when the pipeline was created"""
    updated_at: AirbyteSortOrder
    """Timestamp when the pipeline was last updated"""
    web_url: AirbyteSortOrder
    """Web URL of the pipeline"""
    name: AirbyteSortOrder
    """Name of the pipeline"""


# Entity-specific condition types for pipelines
class PipelinesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PipelinesSearchFilter


class PipelinesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PipelinesSearchFilter


class PipelinesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PipelinesSearchFilter


class PipelinesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PipelinesSearchFilter


class PipelinesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PipelinesSearchFilter


class PipelinesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PipelinesSearchFilter


class PipelinesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PipelinesStringFilter


class PipelinesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PipelinesStringFilter


class PipelinesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PipelinesStringFilter


class PipelinesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PipelinesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PipelinesInCondition = TypedDict("PipelinesInCondition", {"in": PipelinesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PipelinesNotCondition = TypedDict("PipelinesNotCondition", {"not": "PipelinesCondition"}, total=False)
"""Negates the nested condition."""

PipelinesAndCondition = TypedDict("PipelinesAndCondition", {"and": "list[PipelinesCondition]"}, total=False)
"""True if all nested conditions are true."""

PipelinesOrCondition = TypedDict("PipelinesOrCondition", {"or": "list[PipelinesCondition]"}, total=False)
"""True if any nested condition is true."""

PipelinesAnyCondition = TypedDict("PipelinesAnyCondition", {"any": PipelinesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pipelines condition types
PipelinesCondition = (
    PipelinesEqCondition
    | PipelinesNeqCondition
    | PipelinesGtCondition
    | PipelinesGteCondition
    | PipelinesLtCondition
    | PipelinesLteCondition
    | PipelinesInCondition
    | PipelinesLikeCondition
    | PipelinesFuzzyCondition
    | PipelinesKeywordCondition
    | PipelinesContainsCondition
    | PipelinesNotCondition
    | PipelinesAndCondition
    | PipelinesOrCondition
    | PipelinesAnyCondition
)


class PipelinesSearchQuery(TypedDict, total=False):
    """Search query for pipelines entity."""
    filter: PipelinesCondition
    sort: list[PipelinesSortFilter]


# ===== GROUP_MEMBERS SEARCH TYPES =====

class GroupMembersSearchFilter(TypedDict, total=False):
    """Available fields for filtering group_members search queries."""
    group_id: int | None
    """ID of the group"""
    id: int | None
    """ID of the member"""
    name: str | None
    """Full name of the member"""
    username: str | None
    """Username of the member"""
    state: str | None
    """State of the member account"""
    membership_state: str | None
    """State of the membership"""
    avatar_url: str | None
    """URL of the member avatar"""
    web_url: str | None
    """Web URL of the member profile"""
    access_level: int | None
    """Access level of the member"""
    created_at: str | None
    """Timestamp when the member was added"""
    expires_at: str | None
    """Expiration date of the membership"""
    created_by: dict[str, Any] | None
    """User who added the member"""
    locked: bool | None
    """Whether the member account is locked"""


class GroupMembersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    group_id: list[int]
    """ID of the group"""
    id: list[int]
    """ID of the member"""
    name: list[str]
    """Full name of the member"""
    username: list[str]
    """Username of the member"""
    state: list[str]
    """State of the member account"""
    membership_state: list[str]
    """State of the membership"""
    avatar_url: list[str]
    """URL of the member avatar"""
    web_url: list[str]
    """Web URL of the member profile"""
    access_level: list[int]
    """Access level of the member"""
    created_at: list[str]
    """Timestamp when the member was added"""
    expires_at: list[str]
    """Expiration date of the membership"""
    created_by: list[dict[str, Any]]
    """User who added the member"""
    locked: list[bool]
    """Whether the member account is locked"""


class GroupMembersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    group_id: Any
    """ID of the group"""
    id: Any
    """ID of the member"""
    name: Any
    """Full name of the member"""
    username: Any
    """Username of the member"""
    state: Any
    """State of the member account"""
    membership_state: Any
    """State of the membership"""
    avatar_url: Any
    """URL of the member avatar"""
    web_url: Any
    """Web URL of the member profile"""
    access_level: Any
    """Access level of the member"""
    created_at: Any
    """Timestamp when the member was added"""
    expires_at: Any
    """Expiration date of the membership"""
    created_by: Any
    """User who added the member"""
    locked: Any
    """Whether the member account is locked"""


class GroupMembersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    group_id: str
    """ID of the group"""
    id: str
    """ID of the member"""
    name: str
    """Full name of the member"""
    username: str
    """Username of the member"""
    state: str
    """State of the member account"""
    membership_state: str
    """State of the membership"""
    avatar_url: str
    """URL of the member avatar"""
    web_url: str
    """Web URL of the member profile"""
    access_level: str
    """Access level of the member"""
    created_at: str
    """Timestamp when the member was added"""
    expires_at: str
    """Expiration date of the membership"""
    created_by: str
    """User who added the member"""
    locked: str
    """Whether the member account is locked"""


class GroupMembersSortFilter(TypedDict, total=False):
    """Available fields for sorting group_members search results."""
    group_id: AirbyteSortOrder
    """ID of the group"""
    id: AirbyteSortOrder
    """ID of the member"""
    name: AirbyteSortOrder
    """Full name of the member"""
    username: AirbyteSortOrder
    """Username of the member"""
    state: AirbyteSortOrder
    """State of the member account"""
    membership_state: AirbyteSortOrder
    """State of the membership"""
    avatar_url: AirbyteSortOrder
    """URL of the member avatar"""
    web_url: AirbyteSortOrder
    """Web URL of the member profile"""
    access_level: AirbyteSortOrder
    """Access level of the member"""
    created_at: AirbyteSortOrder
    """Timestamp when the member was added"""
    expires_at: AirbyteSortOrder
    """Expiration date of the membership"""
    created_by: AirbyteSortOrder
    """User who added the member"""
    locked: AirbyteSortOrder
    """Whether the member account is locked"""


# Entity-specific condition types for group_members
class GroupMembersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GroupMembersSearchFilter


class GroupMembersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GroupMembersSearchFilter


class GroupMembersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GroupMembersSearchFilter


class GroupMembersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GroupMembersSearchFilter


class GroupMembersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GroupMembersSearchFilter


class GroupMembersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GroupMembersSearchFilter


class GroupMembersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GroupMembersStringFilter


class GroupMembersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GroupMembersStringFilter


class GroupMembersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GroupMembersStringFilter


class GroupMembersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GroupMembersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GroupMembersInCondition = TypedDict("GroupMembersInCondition", {"in": GroupMembersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GroupMembersNotCondition = TypedDict("GroupMembersNotCondition", {"not": "GroupMembersCondition"}, total=False)
"""Negates the nested condition."""

GroupMembersAndCondition = TypedDict("GroupMembersAndCondition", {"and": "list[GroupMembersCondition]"}, total=False)
"""True if all nested conditions are true."""

GroupMembersOrCondition = TypedDict("GroupMembersOrCondition", {"or": "list[GroupMembersCondition]"}, total=False)
"""True if any nested condition is true."""

GroupMembersAnyCondition = TypedDict("GroupMembersAnyCondition", {"any": GroupMembersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all group_members condition types
GroupMembersCondition = (
    GroupMembersEqCondition
    | GroupMembersNeqCondition
    | GroupMembersGtCondition
    | GroupMembersGteCondition
    | GroupMembersLtCondition
    | GroupMembersLteCondition
    | GroupMembersInCondition
    | GroupMembersLikeCondition
    | GroupMembersFuzzyCondition
    | GroupMembersKeywordCondition
    | GroupMembersContainsCondition
    | GroupMembersNotCondition
    | GroupMembersAndCondition
    | GroupMembersOrCondition
    | GroupMembersAnyCondition
)


class GroupMembersSearchQuery(TypedDict, total=False):
    """Search query for group_members entity."""
    filter: GroupMembersCondition
    sort: list[GroupMembersSortFilter]


# ===== PROJECT_MEMBERS SEARCH TYPES =====

class ProjectMembersSearchFilter(TypedDict, total=False):
    """Available fields for filtering project_members search queries."""
    project_id: int | None
    """ID of the project"""
    id: int | None
    """ID of the member"""
    name: str | None
    """Full name of the member"""
    username: str | None
    """Username of the member"""
    state: str | None
    """State of the member account"""
    membership_state: str | None
    """State of the membership"""
    avatar_url: str | None
    """URL of the member avatar"""
    web_url: str | None
    """Web URL of the member profile"""
    access_level: int | None
    """Access level of the member"""
    created_at: str | None
    """Timestamp when the member was added"""
    expires_at: str | None
    """Expiration date of the membership"""
    created_by: dict[str, Any] | None
    """User who added the member"""
    locked: bool | None
    """Whether the member account is locked"""


class ProjectMembersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    project_id: list[int]
    """ID of the project"""
    id: list[int]
    """ID of the member"""
    name: list[str]
    """Full name of the member"""
    username: list[str]
    """Username of the member"""
    state: list[str]
    """State of the member account"""
    membership_state: list[str]
    """State of the membership"""
    avatar_url: list[str]
    """URL of the member avatar"""
    web_url: list[str]
    """Web URL of the member profile"""
    access_level: list[int]
    """Access level of the member"""
    created_at: list[str]
    """Timestamp when the member was added"""
    expires_at: list[str]
    """Expiration date of the membership"""
    created_by: list[dict[str, Any]]
    """User who added the member"""
    locked: list[bool]
    """Whether the member account is locked"""


class ProjectMembersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    project_id: Any
    """ID of the project"""
    id: Any
    """ID of the member"""
    name: Any
    """Full name of the member"""
    username: Any
    """Username of the member"""
    state: Any
    """State of the member account"""
    membership_state: Any
    """State of the membership"""
    avatar_url: Any
    """URL of the member avatar"""
    web_url: Any
    """Web URL of the member profile"""
    access_level: Any
    """Access level of the member"""
    created_at: Any
    """Timestamp when the member was added"""
    expires_at: Any
    """Expiration date of the membership"""
    created_by: Any
    """User who added the member"""
    locked: Any
    """Whether the member account is locked"""


class ProjectMembersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    project_id: str
    """ID of the project"""
    id: str
    """ID of the member"""
    name: str
    """Full name of the member"""
    username: str
    """Username of the member"""
    state: str
    """State of the member account"""
    membership_state: str
    """State of the membership"""
    avatar_url: str
    """URL of the member avatar"""
    web_url: str
    """Web URL of the member profile"""
    access_level: str
    """Access level of the member"""
    created_at: str
    """Timestamp when the member was added"""
    expires_at: str
    """Expiration date of the membership"""
    created_by: str
    """User who added the member"""
    locked: str
    """Whether the member account is locked"""


class ProjectMembersSortFilter(TypedDict, total=False):
    """Available fields for sorting project_members search results."""
    project_id: AirbyteSortOrder
    """ID of the project"""
    id: AirbyteSortOrder
    """ID of the member"""
    name: AirbyteSortOrder
    """Full name of the member"""
    username: AirbyteSortOrder
    """Username of the member"""
    state: AirbyteSortOrder
    """State of the member account"""
    membership_state: AirbyteSortOrder
    """State of the membership"""
    avatar_url: AirbyteSortOrder
    """URL of the member avatar"""
    web_url: AirbyteSortOrder
    """Web URL of the member profile"""
    access_level: AirbyteSortOrder
    """Access level of the member"""
    created_at: AirbyteSortOrder
    """Timestamp when the member was added"""
    expires_at: AirbyteSortOrder
    """Expiration date of the membership"""
    created_by: AirbyteSortOrder
    """User who added the member"""
    locked: AirbyteSortOrder
    """Whether the member account is locked"""


# Entity-specific condition types for project_members
class ProjectMembersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectMembersSearchFilter


class ProjectMembersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectMembersSearchFilter


class ProjectMembersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectMembersSearchFilter


class ProjectMembersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectMembersSearchFilter


class ProjectMembersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectMembersSearchFilter


class ProjectMembersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectMembersSearchFilter


class ProjectMembersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectMembersStringFilter


class ProjectMembersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectMembersStringFilter


class ProjectMembersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectMembersStringFilter


class ProjectMembersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectMembersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectMembersInCondition = TypedDict("ProjectMembersInCondition", {"in": ProjectMembersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectMembersNotCondition = TypedDict("ProjectMembersNotCondition", {"not": "ProjectMembersCondition"}, total=False)
"""Negates the nested condition."""

ProjectMembersAndCondition = TypedDict("ProjectMembersAndCondition", {"and": "list[ProjectMembersCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectMembersOrCondition = TypedDict("ProjectMembersOrCondition", {"or": "list[ProjectMembersCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectMembersAnyCondition = TypedDict("ProjectMembersAnyCondition", {"any": ProjectMembersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all project_members condition types
ProjectMembersCondition = (
    ProjectMembersEqCondition
    | ProjectMembersNeqCondition
    | ProjectMembersGtCondition
    | ProjectMembersGteCondition
    | ProjectMembersLtCondition
    | ProjectMembersLteCondition
    | ProjectMembersInCondition
    | ProjectMembersLikeCondition
    | ProjectMembersFuzzyCondition
    | ProjectMembersKeywordCondition
    | ProjectMembersContainsCondition
    | ProjectMembersNotCondition
    | ProjectMembersAndCondition
    | ProjectMembersOrCondition
    | ProjectMembersAnyCondition
)


class ProjectMembersSearchQuery(TypedDict, total=False):
    """Search query for project_members entity."""
    filter: ProjectMembersCondition
    sort: list[ProjectMembersSortFilter]


# ===== RELEASES SEARCH TYPES =====

class ReleasesSearchFilter(TypedDict, total=False):
    """Available fields for filtering releases search queries."""
    name: str | None
    """Name of the release"""
    tag_name: str | None
    """Tag name associated with the release"""
    description: str | None
    """Description of the release"""
    created_at: str | None
    """Timestamp when the release was created"""
    released_at: str | None
    """Timestamp when the release was published"""
    upcoming_release: bool | None
    """Whether this is an upcoming release"""
    milestones: list[Any] | None
    """Milestones associated with the release"""
    commit_path: str | None
    """Path to the release commit"""
    tag_path: str | None
    """Path to the release tag"""
    assets: dict[str, Any] | None
    """Assets attached to the release"""
    evidences: list[Any] | None
    """Evidences collected for the release"""
    links: dict[str, Any] | None
    """Related resource links"""
    author: dict[str, Any] | None
    """Author of the release"""
    author_id: int | None
    """ID of the author"""
    commit: dict[str, Any] | None
    """Commit associated with the release"""
    commit_id: str | None
    """SHA of the associated commit"""
    project_id: int | None
    """ID of the project"""


class ReleasesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Name of the release"""
    tag_name: list[str]
    """Tag name associated with the release"""
    description: list[str]
    """Description of the release"""
    created_at: list[str]
    """Timestamp when the release was created"""
    released_at: list[str]
    """Timestamp when the release was published"""
    upcoming_release: list[bool]
    """Whether this is an upcoming release"""
    milestones: list[list[Any]]
    """Milestones associated with the release"""
    commit_path: list[str]
    """Path to the release commit"""
    tag_path: list[str]
    """Path to the release tag"""
    assets: list[dict[str, Any]]
    """Assets attached to the release"""
    evidences: list[list[Any]]
    """Evidences collected for the release"""
    links: list[dict[str, Any]]
    """Related resource links"""
    author: list[dict[str, Any]]
    """Author of the release"""
    author_id: list[int]
    """ID of the author"""
    commit: list[dict[str, Any]]
    """Commit associated with the release"""
    commit_id: list[str]
    """SHA of the associated commit"""
    project_id: list[int]
    """ID of the project"""


class ReleasesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Name of the release"""
    tag_name: Any
    """Tag name associated with the release"""
    description: Any
    """Description of the release"""
    created_at: Any
    """Timestamp when the release was created"""
    released_at: Any
    """Timestamp when the release was published"""
    upcoming_release: Any
    """Whether this is an upcoming release"""
    milestones: Any
    """Milestones associated with the release"""
    commit_path: Any
    """Path to the release commit"""
    tag_path: Any
    """Path to the release tag"""
    assets: Any
    """Assets attached to the release"""
    evidences: Any
    """Evidences collected for the release"""
    links: Any
    """Related resource links"""
    author: Any
    """Author of the release"""
    author_id: Any
    """ID of the author"""
    commit: Any
    """Commit associated with the release"""
    commit_id: Any
    """SHA of the associated commit"""
    project_id: Any
    """ID of the project"""


class ReleasesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Name of the release"""
    tag_name: str
    """Tag name associated with the release"""
    description: str
    """Description of the release"""
    created_at: str
    """Timestamp when the release was created"""
    released_at: str
    """Timestamp when the release was published"""
    upcoming_release: str
    """Whether this is an upcoming release"""
    milestones: str
    """Milestones associated with the release"""
    commit_path: str
    """Path to the release commit"""
    tag_path: str
    """Path to the release tag"""
    assets: str
    """Assets attached to the release"""
    evidences: str
    """Evidences collected for the release"""
    links: str
    """Related resource links"""
    author: str
    """Author of the release"""
    author_id: str
    """ID of the author"""
    commit: str
    """Commit associated with the release"""
    commit_id: str
    """SHA of the associated commit"""
    project_id: str
    """ID of the project"""


class ReleasesSortFilter(TypedDict, total=False):
    """Available fields for sorting releases search results."""
    name: AirbyteSortOrder
    """Name of the release"""
    tag_name: AirbyteSortOrder
    """Tag name associated with the release"""
    description: AirbyteSortOrder
    """Description of the release"""
    created_at: AirbyteSortOrder
    """Timestamp when the release was created"""
    released_at: AirbyteSortOrder
    """Timestamp when the release was published"""
    upcoming_release: AirbyteSortOrder
    """Whether this is an upcoming release"""
    milestones: AirbyteSortOrder
    """Milestones associated with the release"""
    commit_path: AirbyteSortOrder
    """Path to the release commit"""
    tag_path: AirbyteSortOrder
    """Path to the release tag"""
    assets: AirbyteSortOrder
    """Assets attached to the release"""
    evidences: AirbyteSortOrder
    """Evidences collected for the release"""
    links: AirbyteSortOrder
    """Related resource links"""
    author: AirbyteSortOrder
    """Author of the release"""
    author_id: AirbyteSortOrder
    """ID of the author"""
    commit: AirbyteSortOrder
    """Commit associated with the release"""
    commit_id: AirbyteSortOrder
    """SHA of the associated commit"""
    project_id: AirbyteSortOrder
    """ID of the project"""


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


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    name: str | None
    """Name of the tag"""
    message: str | None
    """Annotation message of the tag"""
    target: str | None
    """SHA the tag points to"""
    release: dict[str, Any] | None
    """Release associated with the tag"""
    protected: bool | None
    """Whether the tag is protected"""
    commit: dict[str, Any] | None
    """Commit the tag points to"""
    commit_id: str | None
    """SHA of the tagged commit"""
    project_id: int | None
    """ID of the project"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Name of the tag"""
    message: list[str]
    """Annotation message of the tag"""
    target: list[str]
    """SHA the tag points to"""
    release: list[dict[str, Any]]
    """Release associated with the tag"""
    protected: list[bool]
    """Whether the tag is protected"""
    commit: list[dict[str, Any]]
    """Commit the tag points to"""
    commit_id: list[str]
    """SHA of the tagged commit"""
    project_id: list[int]
    """ID of the project"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Name of the tag"""
    message: Any
    """Annotation message of the tag"""
    target: Any
    """SHA the tag points to"""
    release: Any
    """Release associated with the tag"""
    protected: Any
    """Whether the tag is protected"""
    commit: Any
    """Commit the tag points to"""
    commit_id: Any
    """SHA of the tagged commit"""
    project_id: Any
    """ID of the project"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Name of the tag"""
    message: str
    """Annotation message of the tag"""
    target: str
    """SHA the tag points to"""
    release: str
    """Release associated with the tag"""
    protected: str
    """Whether the tag is protected"""
    commit: str
    """Commit the tag points to"""
    commit_id: str
    """SHA of the tagged commit"""
    project_id: str
    """ID of the project"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    name: AirbyteSortOrder
    """Name of the tag"""
    message: AirbyteSortOrder
    """Annotation message of the tag"""
    target: AirbyteSortOrder
    """SHA the tag points to"""
    release: AirbyteSortOrder
    """Release associated with the tag"""
    protected: AirbyteSortOrder
    """Whether the tag is protected"""
    commit: AirbyteSortOrder
    """Commit the tag points to"""
    commit_id: AirbyteSortOrder
    """SHA of the tagged commit"""
    project_id: AirbyteSortOrder
    """ID of the project"""


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


# ===== GROUP_MILESTONES SEARCH TYPES =====

class GroupMilestonesSearchFilter(TypedDict, total=False):
    """Available fields for filtering group_milestones search queries."""
    id: int | None
    """ID of the milestone"""
    iid: int | None
    """Internal ID of the milestone within the group"""
    group_id: int | None
    """ID of the group"""
    title: str | None
    """Title of the milestone"""
    description: str | None
    """Description of the milestone"""
    state: str | None
    """State of the milestone"""
    created_at: str | None
    """Timestamp when the milestone was created"""
    updated_at: str | None
    """Timestamp when the milestone was last updated"""
    due_date: str | None
    """Due date of the milestone"""
    start_date: str | None
    """Start date of the milestone"""
    expired: bool | None
    """Whether the milestone is expired"""
    web_url: str | None
    """Web URL of the milestone"""


class GroupMilestonesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the milestone"""
    iid: list[int]
    """Internal ID of the milestone within the group"""
    group_id: list[int]
    """ID of the group"""
    title: list[str]
    """Title of the milestone"""
    description: list[str]
    """Description of the milestone"""
    state: list[str]
    """State of the milestone"""
    created_at: list[str]
    """Timestamp when the milestone was created"""
    updated_at: list[str]
    """Timestamp when the milestone was last updated"""
    due_date: list[str]
    """Due date of the milestone"""
    start_date: list[str]
    """Start date of the milestone"""
    expired: list[bool]
    """Whether the milestone is expired"""
    web_url: list[str]
    """Web URL of the milestone"""


class GroupMilestonesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the milestone"""
    iid: Any
    """Internal ID of the milestone within the group"""
    group_id: Any
    """ID of the group"""
    title: Any
    """Title of the milestone"""
    description: Any
    """Description of the milestone"""
    state: Any
    """State of the milestone"""
    created_at: Any
    """Timestamp when the milestone was created"""
    updated_at: Any
    """Timestamp when the milestone was last updated"""
    due_date: Any
    """Due date of the milestone"""
    start_date: Any
    """Start date of the milestone"""
    expired: Any
    """Whether the milestone is expired"""
    web_url: Any
    """Web URL of the milestone"""


class GroupMilestonesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the milestone"""
    iid: str
    """Internal ID of the milestone within the group"""
    group_id: str
    """ID of the group"""
    title: str
    """Title of the milestone"""
    description: str
    """Description of the milestone"""
    state: str
    """State of the milestone"""
    created_at: str
    """Timestamp when the milestone was created"""
    updated_at: str
    """Timestamp when the milestone was last updated"""
    due_date: str
    """Due date of the milestone"""
    start_date: str
    """Start date of the milestone"""
    expired: str
    """Whether the milestone is expired"""
    web_url: str
    """Web URL of the milestone"""


class GroupMilestonesSortFilter(TypedDict, total=False):
    """Available fields for sorting group_milestones search results."""
    id: AirbyteSortOrder
    """ID of the milestone"""
    iid: AirbyteSortOrder
    """Internal ID of the milestone within the group"""
    group_id: AirbyteSortOrder
    """ID of the group"""
    title: AirbyteSortOrder
    """Title of the milestone"""
    description: AirbyteSortOrder
    """Description of the milestone"""
    state: AirbyteSortOrder
    """State of the milestone"""
    created_at: AirbyteSortOrder
    """Timestamp when the milestone was created"""
    updated_at: AirbyteSortOrder
    """Timestamp when the milestone was last updated"""
    due_date: AirbyteSortOrder
    """Due date of the milestone"""
    start_date: AirbyteSortOrder
    """Start date of the milestone"""
    expired: AirbyteSortOrder
    """Whether the milestone is expired"""
    web_url: AirbyteSortOrder
    """Web URL of the milestone"""


# Entity-specific condition types for group_milestones
class GroupMilestonesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GroupMilestonesSearchFilter


class GroupMilestonesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GroupMilestonesSearchFilter


class GroupMilestonesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GroupMilestonesSearchFilter


class GroupMilestonesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GroupMilestonesSearchFilter


class GroupMilestonesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GroupMilestonesSearchFilter


class GroupMilestonesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GroupMilestonesSearchFilter


class GroupMilestonesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GroupMilestonesStringFilter


class GroupMilestonesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GroupMilestonesStringFilter


class GroupMilestonesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GroupMilestonesStringFilter


class GroupMilestonesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GroupMilestonesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GroupMilestonesInCondition = TypedDict("GroupMilestonesInCondition", {"in": GroupMilestonesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GroupMilestonesNotCondition = TypedDict("GroupMilestonesNotCondition", {"not": "GroupMilestonesCondition"}, total=False)
"""Negates the nested condition."""

GroupMilestonesAndCondition = TypedDict("GroupMilestonesAndCondition", {"and": "list[GroupMilestonesCondition]"}, total=False)
"""True if all nested conditions are true."""

GroupMilestonesOrCondition = TypedDict("GroupMilestonesOrCondition", {"or": "list[GroupMilestonesCondition]"}, total=False)
"""True if any nested condition is true."""

GroupMilestonesAnyCondition = TypedDict("GroupMilestonesAnyCondition", {"any": GroupMilestonesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all group_milestones condition types
GroupMilestonesCondition = (
    GroupMilestonesEqCondition
    | GroupMilestonesNeqCondition
    | GroupMilestonesGtCondition
    | GroupMilestonesGteCondition
    | GroupMilestonesLtCondition
    | GroupMilestonesLteCondition
    | GroupMilestonesInCondition
    | GroupMilestonesLikeCondition
    | GroupMilestonesFuzzyCondition
    | GroupMilestonesKeywordCondition
    | GroupMilestonesContainsCondition
    | GroupMilestonesNotCondition
    | GroupMilestonesAndCondition
    | GroupMilestonesOrCondition
    | GroupMilestonesAnyCondition
)


class GroupMilestonesSearchQuery(TypedDict, total=False):
    """Search query for group_milestones entity."""
    filter: GroupMilestonesCondition
    sort: list[GroupMilestonesSortFilter]


# ===== PROJECT_MILESTONES SEARCH TYPES =====

class ProjectMilestonesSearchFilter(TypedDict, total=False):
    """Available fields for filtering project_milestones search queries."""
    id: int | None
    """ID of the milestone"""
    iid: int | None
    """Internal ID of the milestone within the project"""
    project_id: int | None
    """ID of the project"""
    title: str | None
    """Title of the milestone"""
    description: str | None
    """Description of the milestone"""
    state: str | None
    """State of the milestone"""
    created_at: str | None
    """Timestamp when the milestone was created"""
    updated_at: str | None
    """Timestamp when the milestone was last updated"""
    due_date: str | None
    """Due date of the milestone"""
    start_date: str | None
    """Start date of the milestone"""
    expired: bool | None
    """Whether the milestone is expired"""
    web_url: str | None
    """Web URL of the milestone"""


class ProjectMilestonesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """ID of the milestone"""
    iid: list[int]
    """Internal ID of the milestone within the project"""
    project_id: list[int]
    """ID of the project"""
    title: list[str]
    """Title of the milestone"""
    description: list[str]
    """Description of the milestone"""
    state: list[str]
    """State of the milestone"""
    created_at: list[str]
    """Timestamp when the milestone was created"""
    updated_at: list[str]
    """Timestamp when the milestone was last updated"""
    due_date: list[str]
    """Due date of the milestone"""
    start_date: list[str]
    """Start date of the milestone"""
    expired: list[bool]
    """Whether the milestone is expired"""
    web_url: list[str]
    """Web URL of the milestone"""


class ProjectMilestonesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """ID of the milestone"""
    iid: Any
    """Internal ID of the milestone within the project"""
    project_id: Any
    """ID of the project"""
    title: Any
    """Title of the milestone"""
    description: Any
    """Description of the milestone"""
    state: Any
    """State of the milestone"""
    created_at: Any
    """Timestamp when the milestone was created"""
    updated_at: Any
    """Timestamp when the milestone was last updated"""
    due_date: Any
    """Due date of the milestone"""
    start_date: Any
    """Start date of the milestone"""
    expired: Any
    """Whether the milestone is expired"""
    web_url: Any
    """Web URL of the milestone"""


class ProjectMilestonesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """ID of the milestone"""
    iid: str
    """Internal ID of the milestone within the project"""
    project_id: str
    """ID of the project"""
    title: str
    """Title of the milestone"""
    description: str
    """Description of the milestone"""
    state: str
    """State of the milestone"""
    created_at: str
    """Timestamp when the milestone was created"""
    updated_at: str
    """Timestamp when the milestone was last updated"""
    due_date: str
    """Due date of the milestone"""
    start_date: str
    """Start date of the milestone"""
    expired: str
    """Whether the milestone is expired"""
    web_url: str
    """Web URL of the milestone"""


class ProjectMilestonesSortFilter(TypedDict, total=False):
    """Available fields for sorting project_milestones search results."""
    id: AirbyteSortOrder
    """ID of the milestone"""
    iid: AirbyteSortOrder
    """Internal ID of the milestone within the project"""
    project_id: AirbyteSortOrder
    """ID of the project"""
    title: AirbyteSortOrder
    """Title of the milestone"""
    description: AirbyteSortOrder
    """Description of the milestone"""
    state: AirbyteSortOrder
    """State of the milestone"""
    created_at: AirbyteSortOrder
    """Timestamp when the milestone was created"""
    updated_at: AirbyteSortOrder
    """Timestamp when the milestone was last updated"""
    due_date: AirbyteSortOrder
    """Due date of the milestone"""
    start_date: AirbyteSortOrder
    """Start date of the milestone"""
    expired: AirbyteSortOrder
    """Whether the milestone is expired"""
    web_url: AirbyteSortOrder
    """Web URL of the milestone"""


# Entity-specific condition types for project_milestones
class ProjectMilestonesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectMilestonesSearchFilter


class ProjectMilestonesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectMilestonesSearchFilter


class ProjectMilestonesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectMilestonesSearchFilter


class ProjectMilestonesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectMilestonesSearchFilter


class ProjectMilestonesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectMilestonesSearchFilter


class ProjectMilestonesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectMilestonesSearchFilter


class ProjectMilestonesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectMilestonesStringFilter


class ProjectMilestonesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectMilestonesStringFilter


class ProjectMilestonesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectMilestonesStringFilter


class ProjectMilestonesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectMilestonesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectMilestonesInCondition = TypedDict("ProjectMilestonesInCondition", {"in": ProjectMilestonesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectMilestonesNotCondition = TypedDict("ProjectMilestonesNotCondition", {"not": "ProjectMilestonesCondition"}, total=False)
"""Negates the nested condition."""

ProjectMilestonesAndCondition = TypedDict("ProjectMilestonesAndCondition", {"and": "list[ProjectMilestonesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectMilestonesOrCondition = TypedDict("ProjectMilestonesOrCondition", {"or": "list[ProjectMilestonesCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectMilestonesAnyCondition = TypedDict("ProjectMilestonesAnyCondition", {"any": ProjectMilestonesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all project_milestones condition types
ProjectMilestonesCondition = (
    ProjectMilestonesEqCondition
    | ProjectMilestonesNeqCondition
    | ProjectMilestonesGtCondition
    | ProjectMilestonesGteCondition
    | ProjectMilestonesLtCondition
    | ProjectMilestonesLteCondition
    | ProjectMilestonesInCondition
    | ProjectMilestonesLikeCondition
    | ProjectMilestonesFuzzyCondition
    | ProjectMilestonesKeywordCondition
    | ProjectMilestonesContainsCondition
    | ProjectMilestonesNotCondition
    | ProjectMilestonesAndCondition
    | ProjectMilestonesOrCondition
    | ProjectMilestonesAnyCondition
)


class ProjectMilestonesSearchQuery(TypedDict, total=False):
    """Search query for project_milestones entity."""
    filter: ProjectMilestonesCondition
    sort: list[ProjectMilestonesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
