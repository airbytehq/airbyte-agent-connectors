"""
Pydantic models for gitlab connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration - multiple options available

class GitlabPersonalAccessTokenAuthConfig(BaseModel):
    """Personal Access Token"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Log into your GitLab account and generate a personal access token."""

class GitlabOauth20AuthConfig(BaseModel):
    """OAuth2.0"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The API ID of the GitLab developer application."""
    client_secret: str
    """The API Secret of the GitLab developer application."""
    access_token: str
    """Access Token for making authenticated requests."""
    refresh_token: str
    """The key to refresh the expired access token."""

GitlabAuthConfig = GitlabPersonalAccessTokenAuthConfig | GitlabOauth20AuthConfig

# Replication configuration

class GitlabReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from GitLab."""

    model_config = ConfigDict(extra="forbid")

    start_date: Optional[str] = None
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data. If not set, all data will be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Project(BaseModel):
    """GitLab project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    name_with_namespace: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    path_with_namespace: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    default_branch: Union[str | None, Any] = Field(default=None)
    visibility: Union[str, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    ssh_url_to_repo: Union[str, Any] = Field(default=None)
    http_url_to_repo: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    last_activity_at: Union[str, Any] = Field(default=None)
    namespace: Union[dict[str, Any], Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    forks_count: Union[int, Any] = Field(default=None)
    star_count: Union[int, Any] = Field(default=None)
    open_issues_count: Union[int, Any] = Field(default=None)
    topics: Union[list[str], Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    description_html: Union[str | None, Any] = Field(default=None)
    tag_list: Union[list[Any] | None, Any] = Field(default=None)
    readme_url: Union[str | None, Any] = Field(default=None)
    links: Union[dict[str, Any] | None, Any] = Field(default=None, alias="_links")
    container_registry_image_prefix: Union[str | None, Any] = Field(default=None)
    empty_repo: Union[bool | None, Any] = Field(default=None)
    packages_enabled: Union[bool | None, Any] = Field(default=None)
    marked_for_deletion_at: Union[str | None, Any] = Field(default=None)
    marked_for_deletion_on: Union[str | None, Any] = Field(default=None)
    container_registry_enabled: Union[bool | None, Any] = Field(default=None)
    container_expiration_policy: Union[dict[str, Any] | None, Any] = Field(default=None)
    repository_object_format: Union[str | None, Any] = Field(default=None)
    issues_enabled: Union[bool | None, Any] = Field(default=None)
    merge_requests_enabled: Union[bool | None, Any] = Field(default=None)
    wiki_enabled: Union[bool | None, Any] = Field(default=None)
    jobs_enabled: Union[bool | None, Any] = Field(default=None)
    snippets_enabled: Union[bool | None, Any] = Field(default=None)
    service_desk_enabled: Union[bool | None, Any] = Field(default=None)
    service_desk_address: Union[str | None, Any] = Field(default=None)
    can_create_merge_request_in: Union[bool | None, Any] = Field(default=None)
    resolve_outdated_diff_discussions: Union[bool | None, Any] = Field(default=None)
    lfs_enabled: Union[bool | None, Any] = Field(default=None)
    shared_runners_enabled: Union[bool | None, Any] = Field(default=None)
    group_runners_enabled: Union[bool | None, Any] = Field(default=None)
    creator_id: Union[int | None, Any] = Field(default=None)
    import_url: Union[str | None, Any] = Field(default=None)
    import_type: Union[str | None, Any] = Field(default=None)
    import_status: Union[str | None, Any] = Field(default=None)
    import_error: Union[str | None, Any] = Field(default=None)
    emails_disabled: Union[bool | None, Any] = Field(default=None)
    emails_enabled: Union[bool | None, Any] = Field(default=None)
    show_diff_preview_in_email: Union[bool | None, Any] = Field(default=None)
    auto_devops_enabled: Union[bool | None, Any] = Field(default=None)
    auto_devops_deploy_strategy: Union[str | None, Any] = Field(default=None)
    request_access_enabled: Union[bool | None, Any] = Field(default=None)
    merge_method: Union[str | None, Any] = Field(default=None)
    squash_option: Union[str | None, Any] = Field(default=None)
    enforce_auth_checks_on_uploads: Union[bool | None, Any] = Field(default=None)
    shared_with_groups: Union[list[Any] | None, Any] = Field(default=None)
    only_allow_merge_if_pipeline_succeeds: Union[bool | None, Any] = Field(default=None)
    allow_merge_on_skipped_pipeline: Union[bool | None, Any] = Field(default=None)
    only_allow_merge_if_all_discussions_are_resolved: Union[bool | None, Any] = Field(default=None)
    remove_source_branch_after_merge: Union[bool | None, Any] = Field(default=None)
    printing_merge_request_link_enabled: Union[bool | None, Any] = Field(default=None)
    build_timeout: Union[int | None, Any] = Field(default=None)
    auto_cancel_pending_pipelines: Union[str | None, Any] = Field(default=None)
    build_git_strategy: Union[str | None, Any] = Field(default=None)
    public_jobs: Union[bool | None, Any] = Field(default=None)
    restrict_user_defined_variables: Union[bool | None, Any] = Field(default=None)
    keep_latest_artifact: Union[bool | None, Any] = Field(default=None)
    runner_token_expiration_interval: Union[str | None, Any] = Field(default=None)
    resource_group_default_process_mode: Union[str | None, Any] = Field(default=None)
    ci_config_path: Union[str | None, Any] = Field(default=None)
    ci_default_git_depth: Union[int | None, Any] = Field(default=None)
    ci_delete_pipelines_in_seconds: Union[int | None, Any] = Field(default=None)
    ci_forward_deployment_enabled: Union[bool | None, Any] = Field(default=None)
    ci_forward_deployment_rollback_allowed: Union[bool | None, Any] = Field(default=None)
    ci_job_token_scope_enabled: Union[bool | None, Any] = Field(default=None)
    ci_separated_caches: Union[bool | None, Any] = Field(default=None)
    ci_allow_fork_pipelines_to_run_in_parent_project: Union[bool | None, Any] = Field(default=None)
    ci_id_token_sub_claim_components: Union[list[Any] | None, Any] = Field(default=None)
    ci_pipeline_variables_minimum_override_role: Union[str | None, Any] = Field(default=None)
    ci_push_repository_for_job_token_allowed: Union[bool | None, Any] = Field(default=None)
    ci_display_pipeline_variables: Union[bool | None, Any] = Field(default=None)
    protect_merge_request_pipelines: Union[bool | None, Any] = Field(default=None)
    suggestion_commit_message: Union[str | None, Any] = Field(default=None)
    merge_commit_template: Union[str | None, Any] = Field(default=None)
    squash_commit_template: Union[str | None, Any] = Field(default=None)
    issue_branch_template: Union[str | None, Any] = Field(default=None)
    merge_request_title_regex: Union[str | None, Any] = Field(default=None)
    merge_request_title_regex_description: Union[str | None, Any] = Field(default=None)
    warn_about_potentially_unwanted_characters: Union[bool | None, Any] = Field(default=None)
    autoclose_referenced_issues: Union[bool | None, Any] = Field(default=None)
    max_artifacts_size: Union[int | None, Any] = Field(default=None)
    external_authorization_classification_label: Union[str | None, Any] = Field(default=None)
    requirements_enabled: Union[bool | None, Any] = Field(default=None)
    requirements_access_level: Union[str | None, Any] = Field(default=None)
    security_and_compliance_enabled: Union[bool | None, Any] = Field(default=None)
    security_and_compliance_access_level: Union[str | None, Any] = Field(default=None)
    compliance_frameworks: Union[list[Any] | None, Any] = Field(default=None)
    web_based_commit_signing_enabled: Union[bool | None, Any] = Field(default=None)
    permissions: Union[dict[str, Any] | None, Any] = Field(default=None)
    issues_access_level: Union[str | None, Any] = Field(default=None)
    repository_access_level: Union[str | None, Any] = Field(default=None)
    merge_requests_access_level: Union[str | None, Any] = Field(default=None)
    forking_access_level: Union[str | None, Any] = Field(default=None)
    wiki_access_level: Union[str | None, Any] = Field(default=None)
    builds_access_level: Union[str | None, Any] = Field(default=None)
    snippets_access_level: Union[str | None, Any] = Field(default=None)
    pages_access_level: Union[str | None, Any] = Field(default=None)
    analytics_access_level: Union[str | None, Any] = Field(default=None)
    container_registry_access_level: Union[str | None, Any] = Field(default=None)
    releases_access_level: Union[str | None, Any] = Field(default=None)
    environments_access_level: Union[str | None, Any] = Field(default=None)
    feature_flags_access_level: Union[str | None, Any] = Field(default=None)
    infrastructure_access_level: Union[str | None, Any] = Field(default=None)
    monitor_access_level: Union[str | None, Any] = Field(default=None)
    model_experiments_access_level: Union[str | None, Any] = Field(default=None)
    model_registry_access_level: Union[str | None, Any] = Field(default=None)
    package_registry_access_level: Union[str | None, Any] = Field(default=None)

class Issue(BaseModel):
    """GitLab issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    iid: Union[int, Any] = Field(default=None)
    project_id: Union[int, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    labels: Union[list[str], Any] = Field(default=None)
    milestone: Union[dict[str, Any] | None, Any] = Field(default=None)
    author: Union[dict[str, Any], Any] = Field(default=None)
    assignee: Union[dict[str, Any] | None, Any] = Field(default=None)
    assignees: Union[list[dict[str, Any]], Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    confidential: Union[bool, Any] = Field(default=None)
    weight: Union[int | None, Any] = Field(default=None)
    user_notes_count: Union[int, Any] = Field(default=None)
    upvotes: Union[int, Any] = Field(default=None)
    downvotes: Union[int, Any] = Field(default=None)
    closed_by: Union[dict[str, Any] | None, Any] = Field(default=None)
    time_stats: Union[dict[str, Any] | None, Any] = Field(default=None)
    task_completion_status: Union[dict[str, Any] | None, Any] = Field(default=None)
    references: Union[dict[str, Any] | None, Any] = Field(default=None)
    links: Union[dict[str, Any] | None, Any] = Field(default=None, alias="_links")
    discussion_locked: Union[bool | None, Any] = Field(default=None)
    merge_requests_count: Union[int | None, Any] = Field(default=None)
    blocking_issues_count: Union[int | None, Any] = Field(default=None)
    severity: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    issue_type: Union[str | None, Any] = Field(default=None)
    has_tasks: Union[bool | None, Any] = Field(default=None)
    task_status: Union[str | None, Any] = Field(default=None)
    moved_to_id: Union[int | None, Any] = Field(default=None)
    service_desk_reply_to: Union[str | None, Any] = Field(default=None)
    epic_iid: Union[int | None, Any] = Field(default=None)
    epic: Union[dict[str, Any] | None, Any] = Field(default=None)
    iteration: Union[dict[str, Any] | None, Any] = Field(default=None)
    health_status: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    imported: Union[bool | None, Any] = Field(default=None)
    imported_from: Union[str | None, Any] = Field(default=None)
    subscribed: Union[bool | None, Any] = Field(default=None)

class MergeRequest(BaseModel):
    """GitLab merge request"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    iid: Union[int, Any] = Field(default=None)
    project_id: Union[int, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    merged_at: Union[str | None, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    source_branch: Union[str, Any] = Field(default=None)
    target_branch: Union[str, Any] = Field(default=None)
    author: Union[dict[str, Any], Any] = Field(default=None)
    assignee: Union[dict[str, Any] | None, Any] = Field(default=None)
    assignees: Union[list[dict[str, Any]], Any] = Field(default=None)
    labels: Union[list[str], Any] = Field(default=None)
    milestone: Union[dict[str, Any] | None, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    merge_status: Union[str, Any] = Field(default=None)
    draft: Union[bool | None, Any] = Field(default=None)
    user_notes_count: Union[int, Any] = Field(default=None)
    upvotes: Union[int, Any] = Field(default=None)
    downvotes: Union[int, Any] = Field(default=None)
    sha: Union[str | None, Any] = Field(default=None)
    merged_by: Union[dict[str, Any] | None, Any] = Field(default=None)
    merge_user: Union[dict[str, Any] | None, Any] = Field(default=None)
    closed_by: Union[dict[str, Any] | None, Any] = Field(default=None)
    reviewers: Union[list[Any] | None, Any] = Field(default=None)
    source_project_id: Union[int | None, Any] = Field(default=None)
    target_project_id: Union[int | None, Any] = Field(default=None)
    work_in_progress: Union[bool | None, Any] = Field(default=None)
    merge_when_pipeline_succeeds: Union[bool | None, Any] = Field(default=None)
    detailed_merge_status: Union[str | None, Any] = Field(default=None)
    merge_after: Union[str | None, Any] = Field(default=None)
    merge_commit_sha: Union[str | None, Any] = Field(default=None)
    squash_commit_sha: Union[str | None, Any] = Field(default=None)
    discussion_locked: Union[bool | None, Any] = Field(default=None)
    should_remove_source_branch: Union[bool | None, Any] = Field(default=None)
    force_remove_source_branch: Union[bool | None, Any] = Field(default=None)
    prepared_at: Union[str | None, Any] = Field(default=None)
    reference: Union[str | None, Any] = Field(default=None)
    references: Union[dict[str, Any] | None, Any] = Field(default=None)
    time_stats: Union[dict[str, Any] | None, Any] = Field(default=None)
    squash: Union[bool | None, Any] = Field(default=None)
    squash_on_merge: Union[bool | None, Any] = Field(default=None)
    task_completion_status: Union[dict[str, Any] | None, Any] = Field(default=None)
    has_conflicts: Union[bool | None, Any] = Field(default=None)
    blocking_discussions_resolved: Union[bool | None, Any] = Field(default=None)
    approvals_before_merge: Union[int | None, Any] = Field(default=None)
    imported: Union[bool | None, Any] = Field(default=None)
    imported_from: Union[str | None, Any] = Field(default=None)
    subscribed: Union[bool | None, Any] = Field(default=None)
    changes_count: Union[str | None, Any] = Field(default=None)
    latest_build_started_at: Union[str | None, Any] = Field(default=None)
    latest_build_finished_at: Union[str | None, Any] = Field(default=None)
    first_deployed_to_production_at: Union[str | None, Any] = Field(default=None)
    pipeline: Union[dict[str, Any] | None, Any] = Field(default=None)
    head_pipeline: Union[dict[str, Any] | None, Any] = Field(default=None)
    diff_refs: Union[dict[str, Any] | None, Any] = Field(default=None)
    merge_error: Union[str | None, Any] = Field(default=None)
    first_contribution: Union[bool | None, Any] = Field(default=None)
    user: Union[dict[str, Any] | None, Any] = Field(default=None)

class User(BaseModel):
    """GitLab user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    username: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    locked: Union[bool | None, Any] = Field(default=None)
    public_email: Union[str | None, Any] = Field(default=None)

class CommitStats(BaseModel):
    """Commit stats"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    additions: Union[int, Any] = Field(default=None, description="Lines added")
    """Lines added"""
    deletions: Union[int, Any] = Field(default=None, description="Lines deleted")
    """Lines deleted"""
    total: Union[int, Any] = Field(default=None, description="Total changes")
    """Total changes"""

class Commit(BaseModel):
    """GitLab commit"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    short_id: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    message: Union[str, Any] = Field(default=None)
    author_name: Union[str, Any] = Field(default=None)
    author_email: Union[str, Any] = Field(default=None)
    authored_date: Union[str, Any] = Field(default=None)
    committer_name: Union[str, Any] = Field(default=None)
    committer_email: Union[str, Any] = Field(default=None)
    committed_date: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    parent_ids: Union[list[str], Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    stats: Union[CommitStats | None, Any] = Field(default=None)
    trailers: Union[dict[str, Any] | None, Any] = Field(default=None)
    extended_trailers: Union[dict[str, Any] | None, Any] = Field(default=None)

class Group(BaseModel):
    """GitLab group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    full_name: Union[str, Any] = Field(default=None)
    full_path: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    visibility: Union[str, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    organization_id: Union[int | None, Any] = Field(default=None)
    default_branch: Union[str | None, Any] = Field(default=None)
    default_branch_protection: Union[int | None, Any] = Field(default=None)
    default_branch_protection_defaults: Union[dict[str, Any] | None, Any] = Field(default=None)
    share_with_group_lock: Union[bool | None, Any] = Field(default=None)
    require_two_factor_authentication: Union[bool | None, Any] = Field(default=None)
    two_factor_grace_period: Union[int | None, Any] = Field(default=None)
    project_creation_level: Union[str | None, Any] = Field(default=None)
    auto_devops_enabled: Union[bool | None, Any] = Field(default=None)
    subgroup_creation_level: Union[str | None, Any] = Field(default=None)
    emails_disabled: Union[bool | None, Any] = Field(default=None)
    emails_enabled: Union[bool | None, Any] = Field(default=None)
    mentions_disabled: Union[bool | None, Any] = Field(default=None)
    lfs_enabled: Union[bool | None, Any] = Field(default=None)
    request_access_enabled: Union[bool | None, Any] = Field(default=None)
    shared_runners_setting: Union[str | None, Any] = Field(default=None)
    ldap_cn: Union[str | None, Any] = Field(default=None)
    ldap_access: Union[str | None, Any] = Field(default=None)
    wiki_access_level: Union[str | None, Any] = Field(default=None)
    marked_for_deletion_on: Union[str | None, Any] = Field(default=None)
    archived: Union[bool | None, Any] = Field(default=None)
    math_rendering_limits_enabled: Union[bool | None, Any] = Field(default=None)
    lock_math_rendering_limits_enabled: Union[bool | None, Any] = Field(default=None)
    max_artifacts_size: Union[int | None, Any] = Field(default=None)
    show_diff_preview_in_email: Union[bool | None, Any] = Field(default=None)
    web_based_commit_signing_enabled: Union[bool | None, Any] = Field(default=None)
    duo_namespace_access_rules: Union[list[Any] | None, Any] = Field(default=None)
    shared_with_groups: Union[list[Any] | None, Any] = Field(default=None)
    runners_token: Union[str | None, Any] = Field(default=None)
    enabled_git_access_protocol: Union[str | None, Any] = Field(default=None)
    prevent_sharing_groups_outside_hierarchy: Union[bool | None, Any] = Field(default=None)
    projects: Union[list[Any] | None, Any] = Field(default=None)
    shared_projects: Union[list[Any] | None, Any] = Field(default=None)
    shared_runners_minutes_limit: Union[int | None, Any] = Field(default=None)
    extra_shared_runners_minutes_limit: Union[int | None, Any] = Field(default=None)
    prevent_forking_outside_group: Union[bool | None, Any] = Field(default=None)
    membership_lock: Union[bool | None, Any] = Field(default=None)
    ip_restriction_ranges: Union[str | None, Any] = Field(default=None)
    service_access_tokens_expiration_enforced: Union[bool | None, Any] = Field(default=None)

class Branch(BaseModel):
    """GitLab branch"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    merged: Union[bool, Any] = Field(default=None)
    protected: Union[bool, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    developers_can_push: Union[bool, Any] = Field(default=None)
    developers_can_merge: Union[bool, Any] = Field(default=None)
    can_push: Union[bool, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    commit: Union[dict[str, Any] | None, Any] = Field(default=None)

class Pipeline(BaseModel):
    """GitLab CI/CD pipeline"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    iid: Union[int, Any] = Field(default=None)
    project_id: Union[int, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    ref: Union[str, Any] = Field(default=None)
    sha: Union[str, Any] = Field(default=None)
    source: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class Member(BaseModel):
    """GitLab group or project member"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    username: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    access_level: Union[int, Any] = Field(default=None)
    expires_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    locked: Union[bool | None, Any] = Field(default=None)
    membership_state: Union[str | None, Any] = Field(default=None)
    public_email: Union[str | None, Any] = Field(default=None)
    created_by: Union[dict[str, Any] | None, Any] = Field(default=None)

class Release(BaseModel):
    """GitLab release"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    tag_name: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    released_at: Union[str, Any] = Field(default=None)
    author: Union[dict[str, Any], Any] = Field(default=None)
    commit: Union[dict[str, Any], Any] = Field(default=None)
    upcoming_release: Union[bool, Any] = Field(default=None)
    links: Union[dict[str, Any], Any] = Field(default=None, alias="_links")
    assets: Union[dict[str, Any] | None, Any] = Field(default=None)
    milestones: Union[list[Any] | None, Any] = Field(default=None)
    evidences: Union[list[Any] | None, Any] = Field(default=None)
    commit_path: Union[str | None, Any] = Field(default=None)
    tag_path: Union[str | None, Any] = Field(default=None)

class Tag(BaseModel):
    """GitLab repository tag"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    message: Union[str | None, Any] = Field(default=None)
    target: Union[str, Any] = Field(default=None)
    commit: Union[dict[str, Any], Any] = Field(default=None)
    release: Union[dict[str, Any] | None, Any] = Field(default=None)
    protected: Union[bool, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)

class Milestone(BaseModel):
    """GitLab milestone"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    iid: Union[int, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    web_url: Union[str, Any] = Field(default=None)
    expired: Union[bool | None, Any] = Field(default=None)
    group_id: Union[int | None, Any] = Field(default=None)
    project_id: Union[int | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class GitlabCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class GitlabExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GitlabExecuteResultWithMeta(GitlabExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the project"""
    description: str | None = None
    """Description of the project"""
    description_html: str | None = None
    """HTML-rendered description of the project"""
    name: str | None = None
    """Name of the project"""
    name_with_namespace: str | None = None
    """Full name including namespace"""
    path: str | None = None
    """URL path of the project"""
    path_with_namespace: str | None = None
    """Full path including namespace"""
    created_at: str | None = None
    """Timestamp when the project was created"""
    updated_at: str | None = None
    """Timestamp when the project was last updated"""
    default_branch: str | None = None
    """Default branch of the project"""
    tag_list: list[Any] | None = None
    """List of tags for the project"""
    topics: list[Any] | None = None
    """List of topics for the project"""
    ssh_url_to_repo: str | None = None
    """SSH URL to the repository"""
    http_url_to_repo: str | None = None
    """HTTP URL to the repository"""
    web_url: str | None = None
    """Web URL of the project"""
    readme_url: str | None = None
    """URL to the project README"""
    avatar_url: str | None = None
    """URL of the project avatar"""
    forks_count: int | None = None
    """Number of forks"""
    star_count: int | None = None
    """Number of stars"""
    last_activity_at: str | None = None
    """Timestamp of last activity"""
    namespace: dict[str, Any] | None = None
    """Namespace the project belongs to"""
    container_registry_image_prefix: str | None = None
    """Prefix for container registry images"""
    links: dict[str, Any] | None = None
    """Related resource links"""
    packages_enabled: bool | None = None
    """Whether packages are enabled"""
    empty_repo: bool | None = None
    """Whether the repository is empty"""
    archived: bool | None = None
    """Whether the project is archived"""
    visibility: str | None = None
    """Visibility level of the project"""
    resolve_outdated_diff_discussions: bool | None = None
    """Whether outdated diff discussions are auto-resolved"""
    container_registry_enabled: bool | None = None
    """Whether container registry is enabled"""
    container_expiration_policy: dict[str, Any] | None = None
    """Container expiration policy settings"""
    issues_enabled: bool | None = None
    """Whether issues are enabled"""
    merge_requests_enabled: bool | None = None
    """Whether merge requests are enabled"""
    wiki_enabled: bool | None = None
    """Whether wiki is enabled"""
    jobs_enabled: bool | None = None
    """Whether jobs are enabled"""
    snippets_enabled: bool | None = None
    """Whether snippets are enabled"""
    service_desk_enabled: bool | None = None
    """Whether service desk is enabled"""
    service_desk_address: str | None = None
    """Email address for the service desk"""
    can_create_merge_request_in: bool | None = None
    """Whether user can create merge requests"""
    issues_access_level: str | None = None
    """Access level for issues"""
    repository_access_level: str | None = None
    """Access level for the repository"""
    merge_requests_access_level: str | None = None
    """Access level for merge requests"""
    forking_access_level: str | None = None
    """Access level for forking"""
    wiki_access_level: str | None = None
    """Access level for the wiki"""
    builds_access_level: str | None = None
    """Access level for builds"""
    snippets_access_level: str | None = None
    """Access level for snippets"""
    pages_access_level: str | None = None
    """Access level for pages"""
    operations_access_level: str | None = None
    """Access level for operations"""
    analytics_access_level: str | None = None
    """Access level for analytics"""
    emails_disabled: bool | None = None
    """Whether emails are disabled"""
    shared_runners_enabled: bool | None = None
    """Whether shared runners are enabled"""
    lfs_enabled: bool | None = None
    """Whether Git LFS is enabled"""
    creator_id: int | None = None
    """ID of the project creator"""
    import_status: str | None = None
    """Import status of the project"""
    open_issues_count: int | None = None
    """Number of open issues"""
    ci_default_git_depth: int | None = None
    """Default git depth for CI pipelines"""
    ci_forward_deployment_enabled: bool | None = None
    """Whether CI forward deployment is enabled"""
    public_jobs: bool | None = None
    """Whether jobs are public"""
    build_timeout: int | None = None
    """Build timeout in seconds"""
    auto_cancel_pending_pipelines: str | None = None
    """Auto-cancel pending pipelines setting"""
    ci_config_path: str | None = None
    """Path to the CI configuration file"""
    shared_with_groups: list[Any] | None = None
    """Groups the project is shared with"""
    only_allow_merge_if_pipeline_succeeds: bool | None = None
    """Whether merge requires pipeline success"""
    allow_merge_on_skipped_pipeline: bool | None = None
    """Whether merge is allowed on skipped pipeline"""
    restrict_user_defined_variables: bool | None = None
    """Whether user-defined variables are restricted"""
    request_access_enabled: bool | None = None
    """Whether access requests are enabled"""
    only_allow_merge_if_all_discussions_are_resolved: bool | None = None
    """Whether merge requires all discussions resolved"""
    remove_source_branch_after_merge: bool | None = None
    """Whether source branch is removed after merge"""
    printing_merge_request_link_enabled: bool | None = None
    """Whether MR link printing is enabled"""
    merge_method: str | None = None
    """Merge method used for the project"""
    statistics: dict[str, Any] | None = None
    """Project statistics"""
    auto_devops_enabled: bool | None = None
    """Whether Auto DevOps is enabled"""
    auto_devops_deploy_strategy: str | None = None
    """Auto DevOps deployment strategy"""
    autoclose_referenced_issues: bool | None = None
    """Whether referenced issues are auto-closed"""
    external_authorization_classification_label: str | None = None
    """External authorization classification label"""
    requirements_enabled: bool | None = None
    """Whether requirements are enabled"""
    security_and_compliance_enabled: bool | None = None
    """Whether security and compliance is enabled"""
    compliance_frameworks: list[Any] | None = None
    """Compliance frameworks for the project"""
    permissions: dict[str, Any] | None = None
    """User permissions for the project"""
    keep_latest_artifact: bool | None = None
    """Whether the latest artifact is kept"""


class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the issue"""
    iid: int | None = None
    """Internal ID of the issue within the project"""
    project_id: int | None = None
    """ID of the project the issue belongs to"""
    title: str | None = None
    """Title of the issue"""
    description: str | None = None
    """Description of the issue"""
    state: str | None = None
    """State of the issue"""
    created_at: str | None = None
    """Timestamp when the issue was created"""
    updated_at: str | None = None
    """Timestamp when the issue was last updated"""
    closed_at: str | None = None
    """Timestamp when the issue was closed"""
    labels: list[Any] | None = None
    """Labels assigned to the issue"""
    assignees: list[Any] | None = None
    """Users assigned to the issue"""
    type_: str | None = None
    """Type of the issue"""
    user_notes_count: int | None = None
    """Number of user notes on the issue"""
    merge_requests_count: int | None = None
    """Number of related merge requests"""
    upvotes: int | None = None
    """Number of upvotes"""
    downvotes: int | None = None
    """Number of downvotes"""
    due_date: str | None = None
    """Due date for the issue"""
    confidential: bool | None = None
    """Whether the issue is confidential"""
    discussion_locked: bool | None = None
    """Whether discussion is locked"""
    issue_type: str | None = None
    """Type classification of the issue"""
    web_url: str | None = None
    """Web URL of the issue"""
    time_stats: dict[str, Any] | None = None
    """Time tracking statistics"""
    task_completion_status: dict[str, Any] | None = None
    """Task completion status"""
    blocking_issues_count: int | None = None
    """Number of blocking issues"""
    has_tasks: bool | None = None
    """Whether the issue has tasks"""
    links: dict[str, Any] | None = None
    """Related resource links"""
    references: dict[str, Any] | None = None
    """Issue references"""
    author: dict[str, Any] | None = None
    """Author of the issue"""
    author_id: int | None = None
    """ID of the author"""
    assignee: dict[str, Any] | None = None
    """Primary assignee of the issue"""
    assignee_id: int | None = None
    """ID of the primary assignee"""
    closed_by: dict[str, Any] | None = None
    """User who closed the issue"""
    closed_by_id: int | None = None
    """ID of the user who closed the issue"""
    milestone: dict[str, Any] | None = None
    """Milestone the issue belongs to"""
    milestone_id: int | None = None
    """ID of the milestone"""
    weight: int | None = None
    """Weight of the issue"""
    severity: str | None = None
    """Severity level of the issue"""


class MergeRequestsSearchData(BaseModel):
    """Search result data for merge_requests entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the merge request"""
    iid: int | None = None
    """Internal ID of the merge request within the project"""
    project_id: int | None = None
    """ID of the project"""
    title: str | None = None
    """Title of the merge request"""
    description: str | None = None
    """Description of the merge request"""
    state: str | None = None
    """State of the merge request"""
    created_at: str | None = None
    """Timestamp when the merge request was created"""
    updated_at: str | None = None
    """Timestamp when the merge request was last updated"""
    merged_at: str | None = None
    """Timestamp when the merge request was merged"""
    closed_at: str | None = None
    """Timestamp when the merge request was closed"""
    target_branch: str | None = None
    """Target branch for the merge request"""
    source_branch: str | None = None
    """Source branch for the merge request"""
    user_notes_count: int | None = None
    """Number of user notes"""
    upvotes: int | None = None
    """Number of upvotes"""
    downvotes: int | None = None
    """Number of downvotes"""
    assignees: list[Any] | None = None
    """Users assigned to the merge request"""
    reviewers: list[Any] | None = None
    """Users assigned as reviewers"""
    source_project_id: int | None = None
    """ID of the source project"""
    target_project_id: int | None = None
    """ID of the target project"""
    labels: list[Any] | None = None
    """Labels assigned to the merge request"""
    work_in_progress: bool | None = None
    """Whether the merge request is a work in progress"""
    merge_when_pipeline_succeeds: bool | None = None
    """Whether to merge when pipeline succeeds"""
    merge_status: str | None = None
    """Merge status of the merge request"""
    sha: str | None = None
    """SHA of the head commit"""
    merge_commit_sha: str | None = None
    """SHA of the merge commit"""
    squash_commit_sha: str | None = None
    """SHA of the squash commit"""
    discussion_locked: bool | None = None
    """Whether discussion is locked"""
    should_remove_source_branch: bool | None = None
    """Whether source branch should be removed"""
    force_remove_source_branch: bool | None = None
    """Whether to force remove source branch"""
    reference: str | None = None
    """Short reference for the merge request"""
    references: dict[str, Any] | None = None
    """Merge request references"""
    web_url: str | None = None
    """Web URL of the merge request"""
    time_stats: dict[str, Any] | None = None
    """Time tracking statistics"""
    squash: bool | None = None
    """Whether to squash commits on merge"""
    task_completion_status: dict[str, Any] | None = None
    """Task completion status"""
    has_conflicts: bool | None = None
    """Whether the merge request has conflicts"""
    blocking_discussions_resolved: bool | None = None
    """Whether blocking discussions are resolved"""
    author: dict[str, Any] | None = None
    """Author of the merge request"""
    author_id: int | None = None
    """ID of the author"""
    assignee: dict[str, Any] | None = None
    """Primary assignee of the merge request"""
    assignee_id: int | None = None
    """ID of the primary assignee"""
    closed_by: dict[str, Any] | None = None
    """User who closed the merge request"""
    closed_by_id: int | None = None
    """ID of the user who closed it"""
    milestone: dict[str, Any] | None = None
    """Milestone the merge request belongs to"""
    milestone_id: int | None = None
    """ID of the milestone"""
    merged_by: dict[str, Any] | None = None
    """User who merged the merge request"""
    merged_by_id: int | None = None
    """ID of the user who merged it"""
    draft: bool | None = None
    """Whether the merge request is a draft"""
    detailed_merge_status: str | None = None
    """Detailed merge status"""
    merge_user: dict[str, Any] | None = None
    """User who performed the merge"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the user"""
    name: str | None = None
    """Full name of the user"""
    username: str | None = None
    """Username of the user"""
    state: str | None = None
    """State of the user account"""
    avatar_url: str | None = None
    """URL of the user avatar"""
    web_url: str | None = None
    """Web URL of the user profile"""
    locked: bool | None = None
    """Whether the user account is locked"""


class CommitsSearchData(BaseModel):
    """Search result data for commits entity."""
    model_config = ConfigDict(extra="allow")

    project_id: int | None = None
    """ID of the project the commit belongs to"""
    id: str | None = None
    """SHA of the commit"""
    short_id: str | None = None
    """Short SHA of the commit"""
    created_at: str | None = None
    """Timestamp when the commit was created"""
    parent_ids: list[Any] | None = None
    """SHAs of parent commits"""
    title: str | None = None
    """Title of the commit"""
    message: str | None = None
    """Full commit message"""
    author_name: str | None = None
    """Name of the commit author"""
    author_email: str | None = None
    """Email of the commit author"""
    authored_date: str | None = None
    """Date the commit was authored"""
    committer_name: str | None = None
    """Name of the committer"""
    committer_email: str | None = None
    """Email of the committer"""
    committed_date: str | None = None
    """Date the commit was committed"""
    trailers: dict[str, Any] | None = None
    """Git trailers for the commit"""
    web_url: str | None = None
    """Web URL of the commit"""
    stats: dict[str, Any] | None = None
    """Commit statistics"""


class GroupsSearchData(BaseModel):
    """Search result data for groups entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the group"""
    web_url: str | None = None
    """Web URL of the group"""
    name: str | None = None
    """Name of the group"""
    path: str | None = None
    """URL path of the group"""
    description: str | None = None
    """Description of the group"""
    visibility: str | None = None
    """Visibility level of the group"""
    share_with_group_lock: bool | None = None
    """Whether sharing with other groups is locked"""
    require_two_factor_authentication: bool | None = None
    """Whether two-factor authentication is required"""
    two_factor_grace_period: int | None = None
    """Grace period for two-factor authentication"""
    project_creation_level: str | None = None
    """Level required to create projects"""
    auto_devops_enabled: bool | None = None
    """Whether Auto DevOps is enabled"""
    subgroup_creation_level: str | None = None
    """Level required to create subgroups"""
    emails_disabled: bool | None = None
    """Whether emails are disabled"""
    emails_enabled: bool | None = None
    """Whether emails are enabled"""
    mentions_disabled: bool | None = None
    """Whether mentions are disabled"""
    lfs_enabled: bool | None = None
    """Whether Git LFS is enabled"""
    default_branch_protection: int | None = None
    """Default branch protection level"""
    avatar_url: str | None = None
    """URL of the group avatar"""
    request_access_enabled: bool | None = None
    """Whether access requests are enabled"""
    full_name: str | None = None
    """Full name of the group"""
    full_path: str | None = None
    """Full path of the group"""
    created_at: str | None = None
    """Timestamp when the group was created"""
    parent_id: int | None = None
    """ID of the parent group"""
    shared_with_groups: list[Any] | None = None
    """Groups this group is shared with"""
    projects: list[Any] | None = None
    """Projects in the group"""


class BranchesSearchData(BaseModel):
    """Search result data for branches entity."""
    model_config = ConfigDict(extra="allow")

    project_id: int | None = None
    """ID of the project the branch belongs to"""
    name: str | None = None
    """Name of the branch"""
    merged: bool | None = None
    """Whether the branch is merged"""
    protected: bool | None = None
    """Whether the branch is protected"""
    developers_can_push: bool | None = None
    """Whether developers can push to the branch"""
    developers_can_merge: bool | None = None
    """Whether developers can merge into the branch"""
    can_push: bool | None = None
    """Whether the current user can push"""
    default: bool | None = None
    """Whether this is the default branch"""
    web_url: str | None = None
    """Web URL of the branch"""
    commit_id: str | None = None
    """SHA of the head commit"""
    commit: dict[str, Any] | None = None
    """Head commit details"""


class PipelinesSearchData(BaseModel):
    """Search result data for pipelines entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the pipeline"""
    iid: int | None = None
    """Internal ID of the pipeline within the project"""
    project_id: int | None = None
    """ID of the project"""
    sha: str | None = None
    """SHA of the commit that triggered the pipeline"""
    source: str | None = None
    """Source that triggered the pipeline"""
    ref: str | None = None
    """Branch or tag that triggered the pipeline"""
    status: str | None = None
    """Status of the pipeline"""
    created_at: str | None = None
    """Timestamp when the pipeline was created"""
    updated_at: str | None = None
    """Timestamp when the pipeline was last updated"""
    web_url: str | None = None
    """Web URL of the pipeline"""
    name: str | None = None
    """Name of the pipeline"""


class GroupMembersSearchData(BaseModel):
    """Search result data for group_members entity."""
    model_config = ConfigDict(extra="allow")

    group_id: int | None = None
    """ID of the group"""
    id: int | None = None
    """ID of the member"""
    name: str | None = None
    """Full name of the member"""
    username: str | None = None
    """Username of the member"""
    state: str | None = None
    """State of the member account"""
    membership_state: str | None = None
    """State of the membership"""
    avatar_url: str | None = None
    """URL of the member avatar"""
    web_url: str | None = None
    """Web URL of the member profile"""
    access_level: int | None = None
    """Access level of the member"""
    created_at: str | None = None
    """Timestamp when the member was added"""
    expires_at: str | None = None
    """Expiration date of the membership"""
    created_by: dict[str, Any] | None = None
    """User who added the member"""
    locked: bool | None = None
    """Whether the member account is locked"""


class ProjectMembersSearchData(BaseModel):
    """Search result data for project_members entity."""
    model_config = ConfigDict(extra="allow")

    project_id: int | None = None
    """ID of the project"""
    id: int | None = None
    """ID of the member"""
    name: str | None = None
    """Full name of the member"""
    username: str | None = None
    """Username of the member"""
    state: str | None = None
    """State of the member account"""
    membership_state: str | None = None
    """State of the membership"""
    avatar_url: str | None = None
    """URL of the member avatar"""
    web_url: str | None = None
    """Web URL of the member profile"""
    access_level: int | None = None
    """Access level of the member"""
    created_at: str | None = None
    """Timestamp when the member was added"""
    expires_at: str | None = None
    """Expiration date of the membership"""
    created_by: dict[str, Any] | None = None
    """User who added the member"""
    locked: bool | None = None
    """Whether the member account is locked"""


class ReleasesSearchData(BaseModel):
    """Search result data for releases entity."""
    model_config = ConfigDict(extra="allow")

    name: str | None = None
    """Name of the release"""
    tag_name: str | None = None
    """Tag name associated with the release"""
    description: str | None = None
    """Description of the release"""
    created_at: str | None = None
    """Timestamp when the release was created"""
    released_at: str | None = None
    """Timestamp when the release was published"""
    upcoming_release: bool | None = None
    """Whether this is an upcoming release"""
    milestones: list[Any] | None = None
    """Milestones associated with the release"""
    commit_path: str | None = None
    """Path to the release commit"""
    tag_path: str | None = None
    """Path to the release tag"""
    assets: dict[str, Any] | None = None
    """Assets attached to the release"""
    evidences: list[Any] | None = None
    """Evidences collected for the release"""
    links: dict[str, Any] | None = None
    """Related resource links"""
    author: dict[str, Any] | None = None
    """Author of the release"""
    author_id: int | None = None
    """ID of the author"""
    commit: dict[str, Any] | None = None
    """Commit associated with the release"""
    commit_id: str | None = None
    """SHA of the associated commit"""
    project_id: int | None = None
    """ID of the project"""


class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")

    name: str | None = None
    """Name of the tag"""
    message: str | None = None
    """Annotation message of the tag"""
    target: str | None = None
    """SHA the tag points to"""
    release: dict[str, Any] | None = None
    """Release associated with the tag"""
    protected: bool | None = None
    """Whether the tag is protected"""
    commit: dict[str, Any] | None = None
    """Commit the tag points to"""
    commit_id: str | None = None
    """SHA of the tagged commit"""
    project_id: int | None = None
    """ID of the project"""


class GroupMilestonesSearchData(BaseModel):
    """Search result data for group_milestones entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the milestone"""
    iid: int | None = None
    """Internal ID of the milestone within the group"""
    group_id: int | None = None
    """ID of the group"""
    title: str | None = None
    """Title of the milestone"""
    description: str | None = None
    """Description of the milestone"""
    state: str | None = None
    """State of the milestone"""
    created_at: str | None = None
    """Timestamp when the milestone was created"""
    updated_at: str | None = None
    """Timestamp when the milestone was last updated"""
    due_date: str | None = None
    """Due date of the milestone"""
    start_date: str | None = None
    """Start date of the milestone"""
    expired: bool | None = None
    """Whether the milestone is expired"""
    web_url: str | None = None
    """Web URL of the milestone"""


class ProjectMilestonesSearchData(BaseModel):
    """Search result data for project_milestones entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """ID of the milestone"""
    iid: int | None = None
    """Internal ID of the milestone within the project"""
    project_id: int | None = None
    """ID of the project"""
    title: str | None = None
    """Title of the milestone"""
    description: str | None = None
    """Description of the milestone"""
    state: str | None = None
    """State of the milestone"""
    created_at: str | None = None
    """Timestamp when the milestone was created"""
    updated_at: str | None = None
    """Timestamp when the milestone was last updated"""
    due_date: str | None = None
    """Due date of the milestone"""
    start_date: str | None = None
    """Start date of the milestone"""
    expired: bool | None = None
    """Whether the milestone is expired"""
    web_url: str | None = None
    """Web URL of the milestone"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

MergeRequestsSearchResult = AirbyteSearchResult[MergeRequestsSearchData]
"""Search result type for merge_requests entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

CommitsSearchResult = AirbyteSearchResult[CommitsSearchData]
"""Search result type for commits entity."""

GroupsSearchResult = AirbyteSearchResult[GroupsSearchData]
"""Search result type for groups entity."""

BranchesSearchResult = AirbyteSearchResult[BranchesSearchData]
"""Search result type for branches entity."""

PipelinesSearchResult = AirbyteSearchResult[PipelinesSearchData]
"""Search result type for pipelines entity."""

GroupMembersSearchResult = AirbyteSearchResult[GroupMembersSearchData]
"""Search result type for group_members entity."""

ProjectMembersSearchResult = AirbyteSearchResult[ProjectMembersSearchData]
"""Search result type for project_members entity."""

ReleasesSearchResult = AirbyteSearchResult[ReleasesSearchData]
"""Search result type for releases entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

GroupMilestonesSearchResult = AirbyteSearchResult[GroupMilestonesSearchData]
"""Search result type for group_milestones entity."""

ProjectMilestonesSearchResult = AirbyteSearchResult[ProjectMilestonesSearchData]
"""Search result type for project_milestones entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ProjectsListResult = GitlabExecuteResult[list[Project]]
"""Result type for projects.list operation."""

IssuesListResult = GitlabExecuteResult[list[Issue]]
"""Result type for issues.list operation."""

MergeRequestsListResult = GitlabExecuteResult[list[MergeRequest]]
"""Result type for merge_requests.list operation."""

UsersListResult = GitlabExecuteResult[list[User]]
"""Result type for users.list operation."""

CommitsListResult = GitlabExecuteResult[list[Commit]]
"""Result type for commits.list operation."""

GroupsListResult = GitlabExecuteResult[list[Group]]
"""Result type for groups.list operation."""

BranchesListResult = GitlabExecuteResult[list[Branch]]
"""Result type for branches.list operation."""

PipelinesListResult = GitlabExecuteResult[list[Pipeline]]
"""Result type for pipelines.list operation."""

GroupMembersListResult = GitlabExecuteResult[list[Member]]
"""Result type for group_members.list operation."""

ProjectMembersListResult = GitlabExecuteResult[list[Member]]
"""Result type for project_members.list operation."""

ReleasesListResult = GitlabExecuteResult[list[Release]]
"""Result type for releases.list operation."""

TagsListResult = GitlabExecuteResult[list[Tag]]
"""Result type for tags.list operation."""

GroupMilestonesListResult = GitlabExecuteResult[list[Milestone]]
"""Result type for group_milestones.list operation."""

ProjectMilestonesListResult = GitlabExecuteResult[list[Milestone]]
"""Result type for project_milestones.list operation."""

