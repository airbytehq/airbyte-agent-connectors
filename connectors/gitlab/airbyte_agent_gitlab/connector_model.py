"""
Connector model for gitlab.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from ._vendored.connector_sdk.types import (
    Action,
    AuthConfig,
    AuthOption,
    AuthType,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)
from ._vendored.connector_sdk.schema.security import (
    AirbyteAuthConfig,
    AuthConfigFieldSpec,
)
from ._vendored.connector_sdk.schema.extensions import (
    EntityRelationshipConfig,
)
from uuid import (
    UUID,
)

GitlabConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('5e6175e5-68e1-4c17-bff9-56103bbb0d80'),
    name='gitlab',
    version='1.0.3',
    base_url='https://{api_url}/api/v4',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='gitlabPAT',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AirbyteAuthConfig(
                    title='Personal Access Token',
                    type='object',
                    required=['access_token'],
                    properties={
                        'access_token': AuthConfigFieldSpec(
                            title='Private Token',
                            description='Log into your GitLab account and generate a personal access token.',
                        ),
                    },
                    auth_mapping={'token': '${access_token}'},
                    replication_auth_key_mapping={'credentials.access_token': 'access_token'},
                    replication_auth_key_constants={'credentials.auth_type': 'access_token'},
                ),
            ),
            AuthOption(
                scheme_name='gitlabOAuth',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://gitlab.com/oauth/token',
                },
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth2.0',
                    type='object',
                    required=[
                        'client_id',
                        'client_secret',
                        'refresh_token',
                        'access_token',
                    ],
                    properties={
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='The API ID of the GitLab developer application.',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='The API Secret of the GitLab developer application.',
                        ),
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='Access Token for making authenticated requests.',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='The key to refresh the expired access token.',
                        ),
                    },
                    auth_mapping={
                        'access_token': '${access_token}',
                        'refresh_token': '${refresh_token}',
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                    },
                    replication_auth_key_mapping={
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                        'credentials.refresh_token': 'refresh_token',
                        'credentials.access_token': 'access_token',
                    },
                    replication_auth_key_constants={'credentials.auth_type': 'oauth2.0', 'credentials.token_expiry_date': ''},
                ),
                untested=True,
            ),
        ],
    ),
    entities=[
        EntityDefinition(
            name='projects',
            stream_name='projects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects',
                    action=Action.LIST,
                    description='Get a list of all visible projects across GitLab for the authenticated user.',
                    query_params=[
                        'page',
                        'per_page',
                        'membership',
                        'owned',
                        'search',
                        'order_by',
                        'sort',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'membership': {'type': 'boolean', 'required': False},
                        'owned': {'type': 'boolean', 'required': False},
                        'search': {'type': 'string', 'required': False},
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab project',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Project ID'},
                                'name': {'type': 'string', 'description': 'Project name'},
                                'name_with_namespace': {'type': 'string', 'description': 'Project name with namespace'},
                                'path': {'type': 'string', 'description': 'Project path'},
                                'path_with_namespace': {'type': 'string', 'description': 'Full path with namespace'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Project description',
                                },
                                'default_branch': {
                                    'type': ['null', 'string'],
                                    'description': 'Default branch name',
                                },
                                'visibility': {'type': 'string', 'description': 'Project visibility level'},
                                'web_url': {'type': 'string', 'description': 'Web URL of the project'},
                                'ssh_url_to_repo': {'type': 'string', 'description': 'SSH URL'},
                                'http_url_to_repo': {'type': 'string', 'description': 'HTTP URL for cloning'},
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'last_activity_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Last activity timestamp',
                                },
                                'namespace': {'type': 'object', 'description': 'Namespace of the project'},
                                'archived': {'type': 'boolean', 'description': 'Whether the project is archived'},
                                'forks_count': {'type': 'integer', 'description': 'Number of forks'},
                                'star_count': {'type': 'integer', 'description': 'Number of stars'},
                                'open_issues_count': {'type': 'integer', 'description': 'Number of open issues'},
                                'topics': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Project topics',
                                },
                                'avatar_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Avatar URL',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Last update timestamp',
                                },
                                'description_html': {
                                    'type': ['null', 'string'],
                                    'description': 'HTML-rendered project description',
                                },
                                'tag_list': {
                                    'type': ['null', 'array'],
                                    'description': 'Deprecated: use topics instead',
                                },
                                'readme_url': {
                                    'type': ['null', 'string'],
                                    'description': 'URL to the project README',
                                },
                                '_links': {
                                    'type': ['null', 'object'],
                                    'description': 'Related links',
                                },
                                'container_registry_image_prefix': {
                                    'type': ['null', 'string'],
                                    'description': 'Container registry image prefix',
                                },
                                'empty_repo': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the repository is empty',
                                },
                                'packages_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether packages are enabled',
                                },
                                'marked_for_deletion_at': {
                                    'type': ['null', 'string'],
                                    'description': 'Timestamp when marked for deletion',
                                },
                                'marked_for_deletion_on': {
                                    'type': ['null', 'string'],
                                    'description': 'Date when marked for deletion',
                                },
                                'container_registry_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether container registry is enabled',
                                },
                                'container_expiration_policy': {
                                    'type': ['null', 'object'],
                                    'description': 'Container expiration policy',
                                },
                                'repository_object_format': {
                                    'type': ['null', 'string'],
                                    'description': 'Repository object format',
                                },
                                'issues_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether issues are enabled',
                                },
                                'merge_requests_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether merge requests are enabled',
                                },
                                'wiki_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether wiki is enabled',
                                },
                                'jobs_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether CI jobs are enabled',
                                },
                                'snippets_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether snippets are enabled',
                                },
                                'service_desk_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether service desk is enabled',
                                },
                                'service_desk_address': {
                                    'type': ['null', 'string'],
                                    'description': 'Service desk email address',
                                },
                                'can_create_merge_request_in': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether MRs can be created',
                                },
                                'resolve_outdated_diff_discussions': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether to resolve outdated diff discussions',
                                },
                                'lfs_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether Git LFS is enabled',
                                },
                                'shared_runners_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether shared runners are enabled',
                                },
                                'group_runners_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether group runners are enabled',
                                },
                                'creator_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the project creator',
                                },
                                'import_url': {
                                    'type': ['null', 'string'],
                                    'description': 'URL used for project import',
                                },
                                'import_type': {
                                    'type': ['null', 'string'],
                                    'description': 'Type of project import',
                                },
                                'import_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Project import status',
                                },
                                'import_error': {
                                    'type': ['null', 'string'],
                                    'description': 'Project import error message',
                                },
                                'emails_disabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether emails are disabled',
                                },
                                'emails_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether emails are enabled',
                                },
                                'show_diff_preview_in_email': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether diff previews are shown in emails',
                                },
                                'auto_devops_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether Auto DevOps is enabled',
                                },
                                'auto_devops_deploy_strategy': {
                                    'type': ['null', 'string'],
                                    'description': 'Auto DevOps deploy strategy',
                                },
                                'request_access_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether request access is enabled',
                                },
                                'merge_method': {
                                    'type': ['null', 'string'],
                                    'description': 'Merge method (merge, rebase_merge, ff)',
                                },
                                'squash_option': {
                                    'type': ['null', 'string'],
                                    'description': 'Squash option setting',
                                },
                                'enforce_auth_checks_on_uploads': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Enforce auth checks on uploads',
                                },
                                'shared_with_groups': {
                                    'type': ['null', 'array'],
                                    'description': 'Groups the project is shared with',
                                },
                                'only_allow_merge_if_pipeline_succeeds': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Only merge if pipeline succeeds',
                                },
                                'allow_merge_on_skipped_pipeline': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Allow merge on skipped pipeline',
                                },
                                'only_allow_merge_if_all_discussions_are_resolved': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Only merge if all discussions resolved',
                                },
                                'remove_source_branch_after_merge': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Remove source branch after merge',
                                },
                                'printing_merge_request_link_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Print MR link enabled',
                                },
                                'build_timeout': {
                                    'type': ['null', 'integer'],
                                    'description': 'Build timeout in seconds',
                                },
                                'auto_cancel_pending_pipelines': {
                                    'type': ['null', 'string'],
                                    'description': 'Auto-cancel pending pipelines setting',
                                },
                                'build_git_strategy': {
                                    'type': ['null', 'string'],
                                    'description': 'Git strategy for builds',
                                },
                                'public_jobs': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether CI jobs are public',
                                },
                                'restrict_user_defined_variables': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Restrict user-defined CI variables',
                                },
                                'keep_latest_artifact': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Keep latest build artifact',
                                },
                                'runner_token_expiration_interval': {
                                    'type': ['null', 'string'],
                                    'description': 'Runner token expiration interval',
                                },
                                'resource_group_default_process_mode': {
                                    'type': ['null', 'string'],
                                    'description': 'Default process mode for resource groups',
                                },
                                'ci_config_path': {
                                    'type': ['null', 'string'],
                                    'description': 'CI configuration file path',
                                },
                                'ci_default_git_depth': {
                                    'type': ['null', 'integer'],
                                    'description': 'Default git depth for CI',
                                },
                                'ci_delete_pipelines_in_seconds': {
                                    'type': ['null', 'integer'],
                                    'description': 'Delete pipelines after seconds',
                                },
                                'ci_forward_deployment_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Forward deployment enabled',
                                },
                                'ci_forward_deployment_rollback_allowed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Forward deployment rollback allowed',
                                },
                                'ci_job_token_scope_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'CI job token scope enabled',
                                },
                                'ci_separated_caches': {
                                    'type': ['null', 'boolean'],
                                    'description': 'CI separated caches',
                                },
                                'ci_allow_fork_pipelines_to_run_in_parent_project': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Allow fork pipelines in parent project',
                                },
                                'ci_id_token_sub_claim_components': {
                                    'type': ['null', 'array'],
                                    'description': 'CI ID token sub claim components',
                                },
                                'ci_pipeline_variables_minimum_override_role': {
                                    'type': ['null', 'string'],
                                    'description': 'Minimum role to override CI variables',
                                },
                                'ci_push_repository_for_job_token_allowed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Push repository for job token allowed',
                                },
                                'ci_display_pipeline_variables': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Display pipeline variables',
                                },
                                'protect_merge_request_pipelines': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Protect merge request pipelines',
                                },
                                'suggestion_commit_message': {
                                    'type': ['null', 'string'],
                                    'description': 'Commit message for suggestions',
                                },
                                'merge_commit_template': {
                                    'type': ['null', 'string'],
                                    'description': 'Template for merge commits',
                                },
                                'squash_commit_template': {
                                    'type': ['null', 'string'],
                                    'description': 'Template for squash commits',
                                },
                                'issue_branch_template': {
                                    'type': ['null', 'string'],
                                    'description': 'Template for issue branches',
                                },
                                'merge_request_title_regex': {
                                    'type': ['null', 'string'],
                                    'description': 'Regex for MR titles',
                                },
                                'merge_request_title_regex_description': {
                                    'type': ['null', 'string'],
                                    'description': 'Description for MR title regex',
                                },
                                'warn_about_potentially_unwanted_characters': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Warn about unwanted characters',
                                },
                                'autoclose_referenced_issues': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Auto-close referenced issues',
                                },
                                'max_artifacts_size': {
                                    'type': ['null', 'integer'],
                                    'description': 'Maximum artifacts size',
                                },
                                'external_authorization_classification_label': {
                                    'type': ['null', 'string'],
                                    'description': 'External authorization label',
                                },
                                'requirements_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether requirements are enabled',
                                },
                                'requirements_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Requirements access level',
                                },
                                'security_and_compliance_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether security and compliance is enabled',
                                },
                                'security_and_compliance_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Security and compliance access level',
                                },
                                'compliance_frameworks': {
                                    'type': ['null', 'array'],
                                    'description': 'Compliance frameworks',
                                },
                                'web_based_commit_signing_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Web-based commit signing enabled',
                                },
                                'permissions': {
                                    'type': ['null', 'object'],
                                    'description': 'Project permissions',
                                },
                                'issues_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Issues access level',
                                },
                                'repository_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Repository access level',
                                },
                                'merge_requests_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Merge requests access level',
                                },
                                'forking_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Forking access level',
                                },
                                'wiki_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Wiki access level',
                                },
                                'builds_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Builds access level',
                                },
                                'snippets_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Snippets access level',
                                },
                                'pages_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Pages access level',
                                },
                                'analytics_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Analytics access level',
                                },
                                'container_registry_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Container registry access level',
                                },
                                'releases_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Releases access level',
                                },
                                'environments_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Environments access level',
                                },
                                'feature_flags_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Feature flags access level',
                                },
                                'infrastructure_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Infrastructure access level',
                                },
                                'monitor_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Monitor access level',
                                },
                                'model_experiments_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Model experiments access level',
                                },
                                'model_registry_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Model registry access level',
                                },
                                'package_registry_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Package registry access level',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'projects',
                            'x-airbyte-stream-name': 'projects',
                        },
                    },
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{id}',
                    action=Action.GET,
                    description='Get a specific project by ID.',
                    query_params=['statistics'],
                    query_params_schema={
                        'statistics': {'type': 'boolean', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab project',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Project ID'},
                            'name': {'type': 'string', 'description': 'Project name'},
                            'name_with_namespace': {'type': 'string', 'description': 'Project name with namespace'},
                            'path': {'type': 'string', 'description': 'Project path'},
                            'path_with_namespace': {'type': 'string', 'description': 'Full path with namespace'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Project description',
                            },
                            'default_branch': {
                                'type': ['null', 'string'],
                                'description': 'Default branch name',
                            },
                            'visibility': {'type': 'string', 'description': 'Project visibility level'},
                            'web_url': {'type': 'string', 'description': 'Web URL of the project'},
                            'ssh_url_to_repo': {'type': 'string', 'description': 'SSH URL'},
                            'http_url_to_repo': {'type': 'string', 'description': 'HTTP URL for cloning'},
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'last_activity_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last activity timestamp',
                            },
                            'namespace': {'type': 'object', 'description': 'Namespace of the project'},
                            'archived': {'type': 'boolean', 'description': 'Whether the project is archived'},
                            'forks_count': {'type': 'integer', 'description': 'Number of forks'},
                            'star_count': {'type': 'integer', 'description': 'Number of stars'},
                            'open_issues_count': {'type': 'integer', 'description': 'Number of open issues'},
                            'topics': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Project topics',
                            },
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': 'Avatar URL',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'description_html': {
                                'type': ['null', 'string'],
                                'description': 'HTML-rendered project description',
                            },
                            'tag_list': {
                                'type': ['null', 'array'],
                                'description': 'Deprecated: use topics instead',
                            },
                            'readme_url': {
                                'type': ['null', 'string'],
                                'description': 'URL to the project README',
                            },
                            '_links': {
                                'type': ['null', 'object'],
                                'description': 'Related links',
                            },
                            'container_registry_image_prefix': {
                                'type': ['null', 'string'],
                                'description': 'Container registry image prefix',
                            },
                            'empty_repo': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the repository is empty',
                            },
                            'packages_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether packages are enabled',
                            },
                            'marked_for_deletion_at': {
                                'type': ['null', 'string'],
                                'description': 'Timestamp when marked for deletion',
                            },
                            'marked_for_deletion_on': {
                                'type': ['null', 'string'],
                                'description': 'Date when marked for deletion',
                            },
                            'container_registry_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether container registry is enabled',
                            },
                            'container_expiration_policy': {
                                'type': ['null', 'object'],
                                'description': 'Container expiration policy',
                            },
                            'repository_object_format': {
                                'type': ['null', 'string'],
                                'description': 'Repository object format',
                            },
                            'issues_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether issues are enabled',
                            },
                            'merge_requests_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether merge requests are enabled',
                            },
                            'wiki_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether wiki is enabled',
                            },
                            'jobs_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether CI jobs are enabled',
                            },
                            'snippets_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether snippets are enabled',
                            },
                            'service_desk_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether service desk is enabled',
                            },
                            'service_desk_address': {
                                'type': ['null', 'string'],
                                'description': 'Service desk email address',
                            },
                            'can_create_merge_request_in': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether MRs can be created',
                            },
                            'resolve_outdated_diff_discussions': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether to resolve outdated diff discussions',
                            },
                            'lfs_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether Git LFS is enabled',
                            },
                            'shared_runners_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether shared runners are enabled',
                            },
                            'group_runners_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether group runners are enabled',
                            },
                            'creator_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the project creator',
                            },
                            'import_url': {
                                'type': ['null', 'string'],
                                'description': 'URL used for project import',
                            },
                            'import_type': {
                                'type': ['null', 'string'],
                                'description': 'Type of project import',
                            },
                            'import_status': {
                                'type': ['null', 'string'],
                                'description': 'Project import status',
                            },
                            'import_error': {
                                'type': ['null', 'string'],
                                'description': 'Project import error message',
                            },
                            'emails_disabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether emails are disabled',
                            },
                            'emails_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether emails are enabled',
                            },
                            'show_diff_preview_in_email': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether diff previews are shown in emails',
                            },
                            'auto_devops_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether Auto DevOps is enabled',
                            },
                            'auto_devops_deploy_strategy': {
                                'type': ['null', 'string'],
                                'description': 'Auto DevOps deploy strategy',
                            },
                            'request_access_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether request access is enabled',
                            },
                            'merge_method': {
                                'type': ['null', 'string'],
                                'description': 'Merge method (merge, rebase_merge, ff)',
                            },
                            'squash_option': {
                                'type': ['null', 'string'],
                                'description': 'Squash option setting',
                            },
                            'enforce_auth_checks_on_uploads': {
                                'type': ['null', 'boolean'],
                                'description': 'Enforce auth checks on uploads',
                            },
                            'shared_with_groups': {
                                'type': ['null', 'array'],
                                'description': 'Groups the project is shared with',
                            },
                            'only_allow_merge_if_pipeline_succeeds': {
                                'type': ['null', 'boolean'],
                                'description': 'Only merge if pipeline succeeds',
                            },
                            'allow_merge_on_skipped_pipeline': {
                                'type': ['null', 'boolean'],
                                'description': 'Allow merge on skipped pipeline',
                            },
                            'only_allow_merge_if_all_discussions_are_resolved': {
                                'type': ['null', 'boolean'],
                                'description': 'Only merge if all discussions resolved',
                            },
                            'remove_source_branch_after_merge': {
                                'type': ['null', 'boolean'],
                                'description': 'Remove source branch after merge',
                            },
                            'printing_merge_request_link_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Print MR link enabled',
                            },
                            'build_timeout': {
                                'type': ['null', 'integer'],
                                'description': 'Build timeout in seconds',
                            },
                            'auto_cancel_pending_pipelines': {
                                'type': ['null', 'string'],
                                'description': 'Auto-cancel pending pipelines setting',
                            },
                            'build_git_strategy': {
                                'type': ['null', 'string'],
                                'description': 'Git strategy for builds',
                            },
                            'public_jobs': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether CI jobs are public',
                            },
                            'restrict_user_defined_variables': {
                                'type': ['null', 'boolean'],
                                'description': 'Restrict user-defined CI variables',
                            },
                            'keep_latest_artifact': {
                                'type': ['null', 'boolean'],
                                'description': 'Keep latest build artifact',
                            },
                            'runner_token_expiration_interval': {
                                'type': ['null', 'string'],
                                'description': 'Runner token expiration interval',
                            },
                            'resource_group_default_process_mode': {
                                'type': ['null', 'string'],
                                'description': 'Default process mode for resource groups',
                            },
                            'ci_config_path': {
                                'type': ['null', 'string'],
                                'description': 'CI configuration file path',
                            },
                            'ci_default_git_depth': {
                                'type': ['null', 'integer'],
                                'description': 'Default git depth for CI',
                            },
                            'ci_delete_pipelines_in_seconds': {
                                'type': ['null', 'integer'],
                                'description': 'Delete pipelines after seconds',
                            },
                            'ci_forward_deployment_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Forward deployment enabled',
                            },
                            'ci_forward_deployment_rollback_allowed': {
                                'type': ['null', 'boolean'],
                                'description': 'Forward deployment rollback allowed',
                            },
                            'ci_job_token_scope_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'CI job token scope enabled',
                            },
                            'ci_separated_caches': {
                                'type': ['null', 'boolean'],
                                'description': 'CI separated caches',
                            },
                            'ci_allow_fork_pipelines_to_run_in_parent_project': {
                                'type': ['null', 'boolean'],
                                'description': 'Allow fork pipelines in parent project',
                            },
                            'ci_id_token_sub_claim_components': {
                                'type': ['null', 'array'],
                                'description': 'CI ID token sub claim components',
                            },
                            'ci_pipeline_variables_minimum_override_role': {
                                'type': ['null', 'string'],
                                'description': 'Minimum role to override CI variables',
                            },
                            'ci_push_repository_for_job_token_allowed': {
                                'type': ['null', 'boolean'],
                                'description': 'Push repository for job token allowed',
                            },
                            'ci_display_pipeline_variables': {
                                'type': ['null', 'boolean'],
                                'description': 'Display pipeline variables',
                            },
                            'protect_merge_request_pipelines': {
                                'type': ['null', 'boolean'],
                                'description': 'Protect merge request pipelines',
                            },
                            'suggestion_commit_message': {
                                'type': ['null', 'string'],
                                'description': 'Commit message for suggestions',
                            },
                            'merge_commit_template': {
                                'type': ['null', 'string'],
                                'description': 'Template for merge commits',
                            },
                            'squash_commit_template': {
                                'type': ['null', 'string'],
                                'description': 'Template for squash commits',
                            },
                            'issue_branch_template': {
                                'type': ['null', 'string'],
                                'description': 'Template for issue branches',
                            },
                            'merge_request_title_regex': {
                                'type': ['null', 'string'],
                                'description': 'Regex for MR titles',
                            },
                            'merge_request_title_regex_description': {
                                'type': ['null', 'string'],
                                'description': 'Description for MR title regex',
                            },
                            'warn_about_potentially_unwanted_characters': {
                                'type': ['null', 'boolean'],
                                'description': 'Warn about unwanted characters',
                            },
                            'autoclose_referenced_issues': {
                                'type': ['null', 'boolean'],
                                'description': 'Auto-close referenced issues',
                            },
                            'max_artifacts_size': {
                                'type': ['null', 'integer'],
                                'description': 'Maximum artifacts size',
                            },
                            'external_authorization_classification_label': {
                                'type': ['null', 'string'],
                                'description': 'External authorization label',
                            },
                            'requirements_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether requirements are enabled',
                            },
                            'requirements_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Requirements access level',
                            },
                            'security_and_compliance_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether security and compliance is enabled',
                            },
                            'security_and_compliance_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Security and compliance access level',
                            },
                            'compliance_frameworks': {
                                'type': ['null', 'array'],
                                'description': 'Compliance frameworks',
                            },
                            'web_based_commit_signing_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Web-based commit signing enabled',
                            },
                            'permissions': {
                                'type': ['null', 'object'],
                                'description': 'Project permissions',
                            },
                            'issues_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Issues access level',
                            },
                            'repository_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Repository access level',
                            },
                            'merge_requests_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Merge requests access level',
                            },
                            'forking_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Forking access level',
                            },
                            'wiki_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Wiki access level',
                            },
                            'builds_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Builds access level',
                            },
                            'snippets_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Snippets access level',
                            },
                            'pages_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Pages access level',
                            },
                            'analytics_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Analytics access level',
                            },
                            'container_registry_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Container registry access level',
                            },
                            'releases_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Releases access level',
                            },
                            'environments_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Environments access level',
                            },
                            'feature_flags_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Feature flags access level',
                            },
                            'infrastructure_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Infrastructure access level',
                            },
                            'monitor_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Monitor access level',
                            },
                            'model_experiments_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Model experiments access level',
                            },
                            'model_registry_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Model registry access level',
                            },
                            'package_registry_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Package registry access level',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'projects',
                        'x-airbyte-stream-name': 'projects',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab project',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Project ID'},
                    'name': {'type': 'string', 'description': 'Project name'},
                    'name_with_namespace': {'type': 'string', 'description': 'Project name with namespace'},
                    'path': {'type': 'string', 'description': 'Project path'},
                    'path_with_namespace': {'type': 'string', 'description': 'Full path with namespace'},
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Project description',
                    },
                    'default_branch': {
                        'type': ['null', 'string'],
                        'description': 'Default branch name',
                    },
                    'visibility': {'type': 'string', 'description': 'Project visibility level'},
                    'web_url': {'type': 'string', 'description': 'Web URL of the project'},
                    'ssh_url_to_repo': {'type': 'string', 'description': 'SSH URL'},
                    'http_url_to_repo': {'type': 'string', 'description': 'HTTP URL for cloning'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'last_activity_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last activity timestamp',
                    },
                    'namespace': {'type': 'object', 'description': 'Namespace of the project'},
                    'archived': {'type': 'boolean', 'description': 'Whether the project is archived'},
                    'forks_count': {'type': 'integer', 'description': 'Number of forks'},
                    'star_count': {'type': 'integer', 'description': 'Number of stars'},
                    'open_issues_count': {'type': 'integer', 'description': 'Number of open issues'},
                    'topics': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Project topics',
                    },
                    'avatar_url': {
                        'type': ['null', 'string'],
                        'description': 'Avatar URL',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'description_html': {
                        'type': ['null', 'string'],
                        'description': 'HTML-rendered project description',
                    },
                    'tag_list': {
                        'type': ['null', 'array'],
                        'description': 'Deprecated: use topics instead',
                    },
                    'readme_url': {
                        'type': ['null', 'string'],
                        'description': 'URL to the project README',
                    },
                    '_links': {
                        'type': ['null', 'object'],
                        'description': 'Related links',
                    },
                    'container_registry_image_prefix': {
                        'type': ['null', 'string'],
                        'description': 'Container registry image prefix',
                    },
                    'empty_repo': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the repository is empty',
                    },
                    'packages_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether packages are enabled',
                    },
                    'marked_for_deletion_at': {
                        'type': ['null', 'string'],
                        'description': 'Timestamp when marked for deletion',
                    },
                    'marked_for_deletion_on': {
                        'type': ['null', 'string'],
                        'description': 'Date when marked for deletion',
                    },
                    'container_registry_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether container registry is enabled',
                    },
                    'container_expiration_policy': {
                        'type': ['null', 'object'],
                        'description': 'Container expiration policy',
                    },
                    'repository_object_format': {
                        'type': ['null', 'string'],
                        'description': 'Repository object format',
                    },
                    'issues_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether issues are enabled',
                    },
                    'merge_requests_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether merge requests are enabled',
                    },
                    'wiki_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether wiki is enabled',
                    },
                    'jobs_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether CI jobs are enabled',
                    },
                    'snippets_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether snippets are enabled',
                    },
                    'service_desk_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether service desk is enabled',
                    },
                    'service_desk_address': {
                        'type': ['null', 'string'],
                        'description': 'Service desk email address',
                    },
                    'can_create_merge_request_in': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether MRs can be created',
                    },
                    'resolve_outdated_diff_discussions': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to resolve outdated diff discussions',
                    },
                    'lfs_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether Git LFS is enabled',
                    },
                    'shared_runners_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether shared runners are enabled',
                    },
                    'group_runners_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether group runners are enabled',
                    },
                    'creator_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the project creator',
                    },
                    'import_url': {
                        'type': ['null', 'string'],
                        'description': 'URL used for project import',
                    },
                    'import_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of project import',
                    },
                    'import_status': {
                        'type': ['null', 'string'],
                        'description': 'Project import status',
                    },
                    'import_error': {
                        'type': ['null', 'string'],
                        'description': 'Project import error message',
                    },
                    'emails_disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether emails are disabled',
                    },
                    'emails_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether emails are enabled',
                    },
                    'show_diff_preview_in_email': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether diff previews are shown in emails',
                    },
                    'auto_devops_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether Auto DevOps is enabled',
                    },
                    'auto_devops_deploy_strategy': {
                        'type': ['null', 'string'],
                        'description': 'Auto DevOps deploy strategy',
                    },
                    'request_access_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether request access is enabled',
                    },
                    'merge_method': {
                        'type': ['null', 'string'],
                        'description': 'Merge method (merge, rebase_merge, ff)',
                    },
                    'squash_option': {
                        'type': ['null', 'string'],
                        'description': 'Squash option setting',
                    },
                    'enforce_auth_checks_on_uploads': {
                        'type': ['null', 'boolean'],
                        'description': 'Enforce auth checks on uploads',
                    },
                    'shared_with_groups': {
                        'type': ['null', 'array'],
                        'description': 'Groups the project is shared with',
                    },
                    'only_allow_merge_if_pipeline_succeeds': {
                        'type': ['null', 'boolean'],
                        'description': 'Only merge if pipeline succeeds',
                    },
                    'allow_merge_on_skipped_pipeline': {
                        'type': ['null', 'boolean'],
                        'description': 'Allow merge on skipped pipeline',
                    },
                    'only_allow_merge_if_all_discussions_are_resolved': {
                        'type': ['null', 'boolean'],
                        'description': 'Only merge if all discussions resolved',
                    },
                    'remove_source_branch_after_merge': {
                        'type': ['null', 'boolean'],
                        'description': 'Remove source branch after merge',
                    },
                    'printing_merge_request_link_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Print MR link enabled',
                    },
                    'build_timeout': {
                        'type': ['null', 'integer'],
                        'description': 'Build timeout in seconds',
                    },
                    'auto_cancel_pending_pipelines': {
                        'type': ['null', 'string'],
                        'description': 'Auto-cancel pending pipelines setting',
                    },
                    'build_git_strategy': {
                        'type': ['null', 'string'],
                        'description': 'Git strategy for builds',
                    },
                    'public_jobs': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether CI jobs are public',
                    },
                    'restrict_user_defined_variables': {
                        'type': ['null', 'boolean'],
                        'description': 'Restrict user-defined CI variables',
                    },
                    'keep_latest_artifact': {
                        'type': ['null', 'boolean'],
                        'description': 'Keep latest build artifact',
                    },
                    'runner_token_expiration_interval': {
                        'type': ['null', 'string'],
                        'description': 'Runner token expiration interval',
                    },
                    'resource_group_default_process_mode': {
                        'type': ['null', 'string'],
                        'description': 'Default process mode for resource groups',
                    },
                    'ci_config_path': {
                        'type': ['null', 'string'],
                        'description': 'CI configuration file path',
                    },
                    'ci_default_git_depth': {
                        'type': ['null', 'integer'],
                        'description': 'Default git depth for CI',
                    },
                    'ci_delete_pipelines_in_seconds': {
                        'type': ['null', 'integer'],
                        'description': 'Delete pipelines after seconds',
                    },
                    'ci_forward_deployment_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Forward deployment enabled',
                    },
                    'ci_forward_deployment_rollback_allowed': {
                        'type': ['null', 'boolean'],
                        'description': 'Forward deployment rollback allowed',
                    },
                    'ci_job_token_scope_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'CI job token scope enabled',
                    },
                    'ci_separated_caches': {
                        'type': ['null', 'boolean'],
                        'description': 'CI separated caches',
                    },
                    'ci_allow_fork_pipelines_to_run_in_parent_project': {
                        'type': ['null', 'boolean'],
                        'description': 'Allow fork pipelines in parent project',
                    },
                    'ci_id_token_sub_claim_components': {
                        'type': ['null', 'array'],
                        'description': 'CI ID token sub claim components',
                    },
                    'ci_pipeline_variables_minimum_override_role': {
                        'type': ['null', 'string'],
                        'description': 'Minimum role to override CI variables',
                    },
                    'ci_push_repository_for_job_token_allowed': {
                        'type': ['null', 'boolean'],
                        'description': 'Push repository for job token allowed',
                    },
                    'ci_display_pipeline_variables': {
                        'type': ['null', 'boolean'],
                        'description': 'Display pipeline variables',
                    },
                    'protect_merge_request_pipelines': {
                        'type': ['null', 'boolean'],
                        'description': 'Protect merge request pipelines',
                    },
                    'suggestion_commit_message': {
                        'type': ['null', 'string'],
                        'description': 'Commit message for suggestions',
                    },
                    'merge_commit_template': {
                        'type': ['null', 'string'],
                        'description': 'Template for merge commits',
                    },
                    'squash_commit_template': {
                        'type': ['null', 'string'],
                        'description': 'Template for squash commits',
                    },
                    'issue_branch_template': {
                        'type': ['null', 'string'],
                        'description': 'Template for issue branches',
                    },
                    'merge_request_title_regex': {
                        'type': ['null', 'string'],
                        'description': 'Regex for MR titles',
                    },
                    'merge_request_title_regex_description': {
                        'type': ['null', 'string'],
                        'description': 'Description for MR title regex',
                    },
                    'warn_about_potentially_unwanted_characters': {
                        'type': ['null', 'boolean'],
                        'description': 'Warn about unwanted characters',
                    },
                    'autoclose_referenced_issues': {
                        'type': ['null', 'boolean'],
                        'description': 'Auto-close referenced issues',
                    },
                    'max_artifacts_size': {
                        'type': ['null', 'integer'],
                        'description': 'Maximum artifacts size',
                    },
                    'external_authorization_classification_label': {
                        'type': ['null', 'string'],
                        'description': 'External authorization label',
                    },
                    'requirements_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether requirements are enabled',
                    },
                    'requirements_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Requirements access level',
                    },
                    'security_and_compliance_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether security and compliance is enabled',
                    },
                    'security_and_compliance_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Security and compliance access level',
                    },
                    'compliance_frameworks': {
                        'type': ['null', 'array'],
                        'description': 'Compliance frameworks',
                    },
                    'web_based_commit_signing_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Web-based commit signing enabled',
                    },
                    'permissions': {
                        'type': ['null', 'object'],
                        'description': 'Project permissions',
                    },
                    'issues_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Issues access level',
                    },
                    'repository_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Repository access level',
                    },
                    'merge_requests_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Merge requests access level',
                    },
                    'forking_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Forking access level',
                    },
                    'wiki_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Wiki access level',
                    },
                    'builds_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Builds access level',
                    },
                    'snippets_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Snippets access level',
                    },
                    'pages_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Pages access level',
                    },
                    'analytics_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Analytics access level',
                    },
                    'container_registry_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Container registry access level',
                    },
                    'releases_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Releases access level',
                    },
                    'environments_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Environments access level',
                    },
                    'feature_flags_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Feature flags access level',
                    },
                    'infrastructure_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Infrastructure access level',
                    },
                    'monitor_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Monitor access level',
                    },
                    'model_experiments_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Model experiments access level',
                    },
                    'model_registry_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Model registry access level',
                    },
                    'package_registry_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Package registry access level',
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'projects',
                'x-airbyte-stream-name': 'projects',
            },
        ),
        EntityDefinition(
            name='issues',
            stream_name='issues',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/issues',
                    action=Action.LIST,
                    description="Get a list of a project's issues.",
                    query_params=[
                        'page',
                        'per_page',
                        'state',
                        'scope',
                        'order_by',
                        'sort',
                        'created_after',
                        'created_before',
                        'updated_after',
                        'updated_before',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'state': {'type': 'string', 'required': False},
                        'scope': {'type': 'string', 'required': False},
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                        'created_before': {'type': 'string', 'required': False},
                        'updated_after': {'type': 'string', 'required': False},
                        'updated_before': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab issue',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Issue ID (globally unique)'},
                                'iid': {'type': 'integer', 'description': 'Issue internal ID (unique within project)'},
                                'project_id': {'type': 'integer', 'description': 'Project ID'},
                                'title': {'type': 'string', 'description': 'Issue title'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Issue description',
                                },
                                'state': {'type': 'string', 'description': 'Issue state (opened/closed)'},
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Last update timestamp',
                                },
                                'closed_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Closed timestamp',
                                },
                                'labels': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Labels',
                                },
                                'milestone': {
                                    'type': ['null', 'object'],
                                    'description': 'Milestone info',
                                },
                                'author': {'type': 'object', 'description': 'Issue author'},
                                'assignee': {
                                    'type': ['null', 'object'],
                                    'description': 'Assignee',
                                },
                                'assignees': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Assignees list',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'due_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Due date',
                                },
                                'confidential': {'type': 'boolean', 'description': 'Whether the issue is confidential'},
                                'weight': {
                                    'type': ['null', 'integer'],
                                    'description': 'Issue weight',
                                },
                                'user_notes_count': {'type': 'integer', 'description': 'Number of notes'},
                                'upvotes': {'type': 'integer', 'description': 'Number of upvotes'},
                                'downvotes': {'type': 'integer', 'description': 'Number of downvotes'},
                                'closed_by': {
                                    'type': ['null', 'object'],
                                    'description': 'User who closed the issue',
                                },
                                'time_stats': {
                                    'type': ['null', 'object'],
                                    'description': 'Time tracking statistics',
                                },
                                'task_completion_status': {
                                    'type': ['null', 'object'],
                                    'description': 'Task completion status',
                                },
                                'references': {
                                    'type': ['null', 'object'],
                                    'description': 'Issue references',
                                },
                                '_links': {
                                    'type': ['null', 'object'],
                                    'description': 'Related links',
                                },
                                'discussion_locked': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether discussion is locked',
                                },
                                'merge_requests_count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of related merge requests',
                                },
                                'blocking_issues_count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of blocking issues',
                                },
                                'severity': {
                                    'type': ['null', 'string'],
                                    'description': 'Issue severity level',
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Issue type',
                                },
                                'issue_type': {
                                    'type': ['null', 'string'],
                                    'description': 'Issue type (deprecated)',
                                },
                                'has_tasks': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the issue has tasks',
                                },
                                'task_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Task status text',
                                },
                                'moved_to_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of issue this was moved to',
                                },
                                'service_desk_reply_to': {
                                    'type': ['null', 'string'],
                                    'description': 'Service desk reply-to address',
                                },
                                'epic_iid': {
                                    'type': ['null', 'integer'],
                                    'description': 'IID of the parent epic',
                                },
                                'epic': {
                                    'type': ['null', 'object'],
                                    'description': 'Parent epic details',
                                },
                                'iteration': {
                                    'type': ['null', 'object'],
                                    'description': 'Associated iteration',
                                },
                                'health_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Health status of the issue',
                                },
                                'start_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Start date',
                                },
                                'imported': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the issue was imported',
                                },
                                'imported_from': {
                                    'type': ['null', 'string'],
                                    'description': 'Source of import',
                                },
                                'subscribed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether current user is subscribed',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'issues',
                            'x-airbyte-stream-name': 'issues',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/issues/{issue_iid}',
                    action=Action.GET,
                    description='Get a single project issue.',
                    path_params=['project_id', 'issue_iid'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'issue_iid': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab issue',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Issue ID (globally unique)'},
                            'iid': {'type': 'integer', 'description': 'Issue internal ID (unique within project)'},
                            'project_id': {'type': 'integer', 'description': 'Project ID'},
                            'title': {'type': 'string', 'description': 'Issue title'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Issue description',
                            },
                            'state': {'type': 'string', 'description': 'Issue state (opened/closed)'},
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'closed_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Closed timestamp',
                            },
                            'labels': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Labels',
                            },
                            'milestone': {
                                'type': ['null', 'object'],
                                'description': 'Milestone info',
                            },
                            'author': {'type': 'object', 'description': 'Issue author'},
                            'assignee': {
                                'type': ['null', 'object'],
                                'description': 'Assignee',
                            },
                            'assignees': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Assignees list',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'due_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Due date',
                            },
                            'confidential': {'type': 'boolean', 'description': 'Whether the issue is confidential'},
                            'weight': {
                                'type': ['null', 'integer'],
                                'description': 'Issue weight',
                            },
                            'user_notes_count': {'type': 'integer', 'description': 'Number of notes'},
                            'upvotes': {'type': 'integer', 'description': 'Number of upvotes'},
                            'downvotes': {'type': 'integer', 'description': 'Number of downvotes'},
                            'closed_by': {
                                'type': ['null', 'object'],
                                'description': 'User who closed the issue',
                            },
                            'time_stats': {
                                'type': ['null', 'object'],
                                'description': 'Time tracking statistics',
                            },
                            'task_completion_status': {
                                'type': ['null', 'object'],
                                'description': 'Task completion status',
                            },
                            'references': {
                                'type': ['null', 'object'],
                                'description': 'Issue references',
                            },
                            '_links': {
                                'type': ['null', 'object'],
                                'description': 'Related links',
                            },
                            'discussion_locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether discussion is locked',
                            },
                            'merge_requests_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of related merge requests',
                            },
                            'blocking_issues_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of blocking issues',
                            },
                            'severity': {
                                'type': ['null', 'string'],
                                'description': 'Issue severity level',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Issue type',
                            },
                            'issue_type': {
                                'type': ['null', 'string'],
                                'description': 'Issue type (deprecated)',
                            },
                            'has_tasks': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the issue has tasks',
                            },
                            'task_status': {
                                'type': ['null', 'string'],
                                'description': 'Task status text',
                            },
                            'moved_to_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of issue this was moved to',
                            },
                            'service_desk_reply_to': {
                                'type': ['null', 'string'],
                                'description': 'Service desk reply-to address',
                            },
                            'epic_iid': {
                                'type': ['null', 'integer'],
                                'description': 'IID of the parent epic',
                            },
                            'epic': {
                                'type': ['null', 'object'],
                                'description': 'Parent epic details',
                            },
                            'iteration': {
                                'type': ['null', 'object'],
                                'description': 'Associated iteration',
                            },
                            'health_status': {
                                'type': ['null', 'string'],
                                'description': 'Health status of the issue',
                            },
                            'start_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Start date',
                            },
                            'imported': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the issue was imported',
                            },
                            'imported_from': {
                                'type': ['null', 'string'],
                                'description': 'Source of import',
                            },
                            'subscribed': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether current user is subscribed',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'issues',
                        'x-airbyte-stream-name': 'issues',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab issue',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Issue ID (globally unique)'},
                    'iid': {'type': 'integer', 'description': 'Issue internal ID (unique within project)'},
                    'project_id': {'type': 'integer', 'description': 'Project ID'},
                    'title': {'type': 'string', 'description': 'Issue title'},
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Issue description',
                    },
                    'state': {'type': 'string', 'description': 'Issue state (opened/closed)'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'closed_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Closed timestamp',
                    },
                    'labels': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Labels',
                    },
                    'milestone': {
                        'type': ['null', 'object'],
                        'description': 'Milestone info',
                    },
                    'author': {'type': 'object', 'description': 'Issue author'},
                    'assignee': {
                        'type': ['null', 'object'],
                        'description': 'Assignee',
                    },
                    'assignees': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Assignees list',
                    },
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'due_date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Due date',
                    },
                    'confidential': {'type': 'boolean', 'description': 'Whether the issue is confidential'},
                    'weight': {
                        'type': ['null', 'integer'],
                        'description': 'Issue weight',
                    },
                    'user_notes_count': {'type': 'integer', 'description': 'Number of notes'},
                    'upvotes': {'type': 'integer', 'description': 'Number of upvotes'},
                    'downvotes': {'type': 'integer', 'description': 'Number of downvotes'},
                    'closed_by': {
                        'type': ['null', 'object'],
                        'description': 'User who closed the issue',
                    },
                    'time_stats': {
                        'type': ['null', 'object'],
                        'description': 'Time tracking statistics',
                    },
                    'task_completion_status': {
                        'type': ['null', 'object'],
                        'description': 'Task completion status',
                    },
                    'references': {
                        'type': ['null', 'object'],
                        'description': 'Issue references',
                    },
                    '_links': {
                        'type': ['null', 'object'],
                        'description': 'Related links',
                    },
                    'discussion_locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether discussion is locked',
                    },
                    'merge_requests_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of related merge requests',
                    },
                    'blocking_issues_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of blocking issues',
                    },
                    'severity': {
                        'type': ['null', 'string'],
                        'description': 'Issue severity level',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Issue type',
                    },
                    'issue_type': {
                        'type': ['null', 'string'],
                        'description': 'Issue type (deprecated)',
                    },
                    'has_tasks': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the issue has tasks',
                    },
                    'task_status': {
                        'type': ['null', 'string'],
                        'description': 'Task status text',
                    },
                    'moved_to_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of issue this was moved to',
                    },
                    'service_desk_reply_to': {
                        'type': ['null', 'string'],
                        'description': 'Service desk reply-to address',
                    },
                    'epic_iid': {
                        'type': ['null', 'integer'],
                        'description': 'IID of the parent epic',
                    },
                    'epic': {
                        'type': ['null', 'object'],
                        'description': 'Parent epic details',
                    },
                    'iteration': {
                        'type': ['null', 'object'],
                        'description': 'Associated iteration',
                    },
                    'health_status': {
                        'type': ['null', 'string'],
                        'description': 'Health status of the issue',
                    },
                    'start_date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Start date',
                    },
                    'imported': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the issue was imported',
                    },
                    'imported_from': {
                        'type': ['null', 'string'],
                        'description': 'Source of import',
                    },
                    'subscribed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether current user is subscribed',
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'issues',
                'x-airbyte-stream-name': 'issues',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='issues',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='merge_requests',
            stream_name='merge_requests',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/merge_requests',
                    action=Action.LIST,
                    description='Get all merge requests for a project.',
                    query_params=[
                        'page',
                        'per_page',
                        'state',
                        'scope',
                        'order_by',
                        'sort',
                        'created_after',
                        'created_before',
                        'updated_after',
                        'updated_before',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'state': {'type': 'string', 'required': False},
                        'scope': {'type': 'string', 'required': False},
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                        'created_before': {'type': 'string', 'required': False},
                        'updated_after': {'type': 'string', 'required': False},
                        'updated_before': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab merge request',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Merge request ID (globally unique)'},
                                'iid': {'type': 'integer', 'description': 'Merge request internal ID'},
                                'project_id': {'type': 'integer', 'description': 'Project ID'},
                                'title': {'type': 'string', 'description': 'Merge request title'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Merge request description',
                                },
                                'state': {'type': 'string', 'description': 'Merge request state'},
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Last update timestamp',
                                },
                                'merged_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Merged timestamp',
                                },
                                'closed_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Closed timestamp',
                                },
                                'source_branch': {'type': 'string', 'description': 'Source branch'},
                                'target_branch': {'type': 'string', 'description': 'Target branch'},
                                'author': {'type': 'object', 'description': 'Author'},
                                'assignee': {
                                    'type': ['null', 'object'],
                                    'description': 'Assignee',
                                },
                                'assignees': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Assignees list',
                                },
                                'labels': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Labels',
                                },
                                'milestone': {
                                    'type': ['null', 'object'],
                                    'description': 'Milestone info',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'merge_status': {'type': 'string', 'description': 'Merge status'},
                                'draft': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether MR is a draft',
                                },
                                'user_notes_count': {'type': 'integer', 'description': 'Number of user notes'},
                                'upvotes': {'type': 'integer', 'description': 'Number of upvotes'},
                                'downvotes': {'type': 'integer', 'description': 'Number of downvotes'},
                                'sha': {
                                    'type': ['null', 'string'],
                                    'description': 'SHA of the head commit',
                                },
                                'merged_by': {
                                    'type': ['null', 'object'],
                                    'description': 'User who merged the MR',
                                },
                                'merge_user': {
                                    'type': ['null', 'object'],
                                    'description': 'User who performed the merge',
                                },
                                'closed_by': {
                                    'type': ['null', 'object'],
                                    'description': 'User who closed the MR',
                                },
                                'reviewers': {
                                    'type': ['null', 'array'],
                                    'description': 'Assigned reviewers',
                                },
                                'source_project_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Source project ID',
                                },
                                'target_project_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Target project ID',
                                },
                                'work_in_progress': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether MR is work in progress',
                                },
                                'merge_when_pipeline_succeeds': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Merge when pipeline succeeds',
                                },
                                'detailed_merge_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Detailed merge status',
                                },
                                'merge_after': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Scheduled merge time',
                                },
                                'merge_commit_sha': {
                                    'type': ['null', 'string'],
                                    'description': 'Merge commit SHA',
                                },
                                'squash_commit_sha': {
                                    'type': ['null', 'string'],
                                    'description': 'Squash commit SHA',
                                },
                                'discussion_locked': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether discussion is locked',
                                },
                                'should_remove_source_branch': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether source branch should be removed',
                                },
                                'force_remove_source_branch': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether source branch removal is forced',
                                },
                                'prepared_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'When MR was prepared',
                                },
                                'reference': {
                                    'type': ['null', 'string'],
                                    'description': 'MR reference string',
                                },
                                'references': {
                                    'type': ['null', 'object'],
                                    'description': 'MR reference details',
                                },
                                'time_stats': {
                                    'type': ['null', 'object'],
                                    'description': 'Time tracking statistics',
                                },
                                'squash': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether squash is enabled',
                                },
                                'squash_on_merge': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether to squash on merge',
                                },
                                'task_completion_status': {
                                    'type': ['null', 'object'],
                                    'description': 'Task completion status',
                                },
                                'has_conflicts': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether MR has conflicts',
                                },
                                'blocking_discussions_resolved': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether blocking discussions are resolved',
                                },
                                'approvals_before_merge': {
                                    'type': ['null', 'integer'],
                                    'description': 'Required approvals before merge',
                                },
                                'imported': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether MR was imported',
                                },
                                'imported_from': {
                                    'type': ['null', 'string'],
                                    'description': 'Source of import',
                                },
                                'subscribed': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether current user is subscribed',
                                },
                                'changes_count': {
                                    'type': ['null', 'string'],
                                    'description': 'Number of changes',
                                },
                                'latest_build_started_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'When latest build started',
                                },
                                'latest_build_finished_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'When latest build finished',
                                },
                                'first_deployed_to_production_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'First deployed to production',
                                },
                                'pipeline': {
                                    'type': ['null', 'object'],
                                    'description': 'Associated pipeline',
                                },
                                'head_pipeline': {
                                    'type': ['null', 'object'],
                                    'description': 'Head pipeline',
                                },
                                'diff_refs': {
                                    'type': ['null', 'object'],
                                    'description': 'Diff references',
                                },
                                'merge_error': {
                                    'type': ['null', 'string'],
                                    'description': 'Merge error message',
                                },
                                'first_contribution': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether this is a first contribution',
                                },
                                'user': {
                                    'type': ['null', 'object'],
                                    'description': 'Current user merge/approval info',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'merge_requests',
                            'x-airbyte-stream-name': 'merge_requests',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/merge_requests/{merge_request_iid}',
                    action=Action.GET,
                    description='Get information about a single merge request.',
                    path_params=['project_id', 'merge_request_iid'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'merge_request_iid': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab merge request',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Merge request ID (globally unique)'},
                            'iid': {'type': 'integer', 'description': 'Merge request internal ID'},
                            'project_id': {'type': 'integer', 'description': 'Project ID'},
                            'title': {'type': 'string', 'description': 'Merge request title'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Merge request description',
                            },
                            'state': {'type': 'string', 'description': 'Merge request state'},
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'merged_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Merged timestamp',
                            },
                            'closed_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Closed timestamp',
                            },
                            'source_branch': {'type': 'string', 'description': 'Source branch'},
                            'target_branch': {'type': 'string', 'description': 'Target branch'},
                            'author': {'type': 'object', 'description': 'Author'},
                            'assignee': {
                                'type': ['null', 'object'],
                                'description': 'Assignee',
                            },
                            'assignees': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Assignees list',
                            },
                            'labels': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Labels',
                            },
                            'milestone': {
                                'type': ['null', 'object'],
                                'description': 'Milestone info',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'merge_status': {'type': 'string', 'description': 'Merge status'},
                            'draft': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether MR is a draft',
                            },
                            'user_notes_count': {'type': 'integer', 'description': 'Number of user notes'},
                            'upvotes': {'type': 'integer', 'description': 'Number of upvotes'},
                            'downvotes': {'type': 'integer', 'description': 'Number of downvotes'},
                            'sha': {
                                'type': ['null', 'string'],
                                'description': 'SHA of the head commit',
                            },
                            'merged_by': {
                                'type': ['null', 'object'],
                                'description': 'User who merged the MR',
                            },
                            'merge_user': {
                                'type': ['null', 'object'],
                                'description': 'User who performed the merge',
                            },
                            'closed_by': {
                                'type': ['null', 'object'],
                                'description': 'User who closed the MR',
                            },
                            'reviewers': {
                                'type': ['null', 'array'],
                                'description': 'Assigned reviewers',
                            },
                            'source_project_id': {
                                'type': ['null', 'integer'],
                                'description': 'Source project ID',
                            },
                            'target_project_id': {
                                'type': ['null', 'integer'],
                                'description': 'Target project ID',
                            },
                            'work_in_progress': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether MR is work in progress',
                            },
                            'merge_when_pipeline_succeeds': {
                                'type': ['null', 'boolean'],
                                'description': 'Merge when pipeline succeeds',
                            },
                            'detailed_merge_status': {
                                'type': ['null', 'string'],
                                'description': 'Detailed merge status',
                            },
                            'merge_after': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Scheduled merge time',
                            },
                            'merge_commit_sha': {
                                'type': ['null', 'string'],
                                'description': 'Merge commit SHA',
                            },
                            'squash_commit_sha': {
                                'type': ['null', 'string'],
                                'description': 'Squash commit SHA',
                            },
                            'discussion_locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether discussion is locked',
                            },
                            'should_remove_source_branch': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether source branch should be removed',
                            },
                            'force_remove_source_branch': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether source branch removal is forced',
                            },
                            'prepared_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When MR was prepared',
                            },
                            'reference': {
                                'type': ['null', 'string'],
                                'description': 'MR reference string',
                            },
                            'references': {
                                'type': ['null', 'object'],
                                'description': 'MR reference details',
                            },
                            'time_stats': {
                                'type': ['null', 'object'],
                                'description': 'Time tracking statistics',
                            },
                            'squash': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether squash is enabled',
                            },
                            'squash_on_merge': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether to squash on merge',
                            },
                            'task_completion_status': {
                                'type': ['null', 'object'],
                                'description': 'Task completion status',
                            },
                            'has_conflicts': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether MR has conflicts',
                            },
                            'blocking_discussions_resolved': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether blocking discussions are resolved',
                            },
                            'approvals_before_merge': {
                                'type': ['null', 'integer'],
                                'description': 'Required approvals before merge',
                            },
                            'imported': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether MR was imported',
                            },
                            'imported_from': {
                                'type': ['null', 'string'],
                                'description': 'Source of import',
                            },
                            'subscribed': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether current user is subscribed',
                            },
                            'changes_count': {
                                'type': ['null', 'string'],
                                'description': 'Number of changes',
                            },
                            'latest_build_started_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When latest build started',
                            },
                            'latest_build_finished_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When latest build finished',
                            },
                            'first_deployed_to_production_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'First deployed to production',
                            },
                            'pipeline': {
                                'type': ['null', 'object'],
                                'description': 'Associated pipeline',
                            },
                            'head_pipeline': {
                                'type': ['null', 'object'],
                                'description': 'Head pipeline',
                            },
                            'diff_refs': {
                                'type': ['null', 'object'],
                                'description': 'Diff references',
                            },
                            'merge_error': {
                                'type': ['null', 'string'],
                                'description': 'Merge error message',
                            },
                            'first_contribution': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether this is a first contribution',
                            },
                            'user': {
                                'type': ['null', 'object'],
                                'description': 'Current user merge/approval info',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'merge_requests',
                        'x-airbyte-stream-name': 'merge_requests',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab merge request',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Merge request ID (globally unique)'},
                    'iid': {'type': 'integer', 'description': 'Merge request internal ID'},
                    'project_id': {'type': 'integer', 'description': 'Project ID'},
                    'title': {'type': 'string', 'description': 'Merge request title'},
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Merge request description',
                    },
                    'state': {'type': 'string', 'description': 'Merge request state'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'merged_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Merged timestamp',
                    },
                    'closed_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Closed timestamp',
                    },
                    'source_branch': {'type': 'string', 'description': 'Source branch'},
                    'target_branch': {'type': 'string', 'description': 'Target branch'},
                    'author': {'type': 'object', 'description': 'Author'},
                    'assignee': {
                        'type': ['null', 'object'],
                        'description': 'Assignee',
                    },
                    'assignees': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Assignees list',
                    },
                    'labels': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Labels',
                    },
                    'milestone': {
                        'type': ['null', 'object'],
                        'description': 'Milestone info',
                    },
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'merge_status': {'type': 'string', 'description': 'Merge status'},
                    'draft': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether MR is a draft',
                    },
                    'user_notes_count': {'type': 'integer', 'description': 'Number of user notes'},
                    'upvotes': {'type': 'integer', 'description': 'Number of upvotes'},
                    'downvotes': {'type': 'integer', 'description': 'Number of downvotes'},
                    'sha': {
                        'type': ['null', 'string'],
                        'description': 'SHA of the head commit',
                    },
                    'merged_by': {
                        'type': ['null', 'object'],
                        'description': 'User who merged the MR',
                    },
                    'merge_user': {
                        'type': ['null', 'object'],
                        'description': 'User who performed the merge',
                    },
                    'closed_by': {
                        'type': ['null', 'object'],
                        'description': 'User who closed the MR',
                    },
                    'reviewers': {
                        'type': ['null', 'array'],
                        'description': 'Assigned reviewers',
                    },
                    'source_project_id': {
                        'type': ['null', 'integer'],
                        'description': 'Source project ID',
                    },
                    'target_project_id': {
                        'type': ['null', 'integer'],
                        'description': 'Target project ID',
                    },
                    'work_in_progress': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether MR is work in progress',
                    },
                    'merge_when_pipeline_succeeds': {
                        'type': ['null', 'boolean'],
                        'description': 'Merge when pipeline succeeds',
                    },
                    'detailed_merge_status': {
                        'type': ['null', 'string'],
                        'description': 'Detailed merge status',
                    },
                    'merge_after': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Scheduled merge time',
                    },
                    'merge_commit_sha': {
                        'type': ['null', 'string'],
                        'description': 'Merge commit SHA',
                    },
                    'squash_commit_sha': {
                        'type': ['null', 'string'],
                        'description': 'Squash commit SHA',
                    },
                    'discussion_locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether discussion is locked',
                    },
                    'should_remove_source_branch': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether source branch should be removed',
                    },
                    'force_remove_source_branch': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether source branch removal is forced',
                    },
                    'prepared_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When MR was prepared',
                    },
                    'reference': {
                        'type': ['null', 'string'],
                        'description': 'MR reference string',
                    },
                    'references': {
                        'type': ['null', 'object'],
                        'description': 'MR reference details',
                    },
                    'time_stats': {
                        'type': ['null', 'object'],
                        'description': 'Time tracking statistics',
                    },
                    'squash': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether squash is enabled',
                    },
                    'squash_on_merge': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to squash on merge',
                    },
                    'task_completion_status': {
                        'type': ['null', 'object'],
                        'description': 'Task completion status',
                    },
                    'has_conflicts': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether MR has conflicts',
                    },
                    'blocking_discussions_resolved': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether blocking discussions are resolved',
                    },
                    'approvals_before_merge': {
                        'type': ['null', 'integer'],
                        'description': 'Required approvals before merge',
                    },
                    'imported': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether MR was imported',
                    },
                    'imported_from': {
                        'type': ['null', 'string'],
                        'description': 'Source of import',
                    },
                    'subscribed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether current user is subscribed',
                    },
                    'changes_count': {
                        'type': ['null', 'string'],
                        'description': 'Number of changes',
                    },
                    'latest_build_started_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When latest build started',
                    },
                    'latest_build_finished_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When latest build finished',
                    },
                    'first_deployed_to_production_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'First deployed to production',
                    },
                    'pipeline': {
                        'type': ['null', 'object'],
                        'description': 'Associated pipeline',
                    },
                    'head_pipeline': {
                        'type': ['null', 'object'],
                        'description': 'Head pipeline',
                    },
                    'diff_refs': {
                        'type': ['null', 'object'],
                        'description': 'Diff references',
                    },
                    'merge_error': {
                        'type': ['null', 'string'],
                        'description': 'Merge error message',
                    },
                    'first_contribution': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a first contribution',
                    },
                    'user': {
                        'type': ['null', 'object'],
                        'description': 'Current user merge/approval info',
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'merge_requests',
                'x-airbyte-stream-name': 'merge_requests',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='merge_requests',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='users',
            stream_name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/users',
                    action=Action.LIST,
                    description='Get a list of users.',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'active',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'search': {'type': 'string', 'required': False},
                        'active': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab user',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'User ID'},
                                'username': {'type': 'string', 'description': 'Username'},
                                'name': {'type': 'string', 'description': 'Full name'},
                                'state': {'type': 'string', 'description': 'User state'},
                                'avatar_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Avatar URL',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'locked': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the user account is locked',
                                },
                                'public_email': {
                                    'type': ['null', 'string'],
                                    'description': "User's public email address",
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'users',
                            'x-airbyte-stream-name': 'users',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/users/{id}',
                    action=Action.GET,
                    description='Get a single user by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab user',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'User ID'},
                            'username': {'type': 'string', 'description': 'Username'},
                            'name': {'type': 'string', 'description': 'Full name'},
                            'state': {'type': 'string', 'description': 'User state'},
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': 'Avatar URL',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the user account is locked',
                            },
                            'public_email': {
                                'type': ['null', 'string'],
                                'description': "User's public email address",
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'users',
                        'x-airbyte-stream-name': 'users',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab user',
                'properties': {
                    'id': {'type': 'integer', 'description': 'User ID'},
                    'username': {'type': 'string', 'description': 'Username'},
                    'name': {'type': 'string', 'description': 'Full name'},
                    'state': {'type': 'string', 'description': 'User state'},
                    'avatar_url': {
                        'type': ['null', 'string'],
                        'description': 'Avatar URL',
                    },
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'locked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the user account is locked',
                    },
                    'public_email': {
                        'type': ['null', 'string'],
                        'description': "User's public email address",
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
            },
        ),
        EntityDefinition(
            name='commits',
            stream_name='commits',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/repository/commits',
                    action=Action.LIST,
                    description='Get a list of repository commits in a project.',
                    query_params=[
                        'page',
                        'per_page',
                        'ref_name',
                        'since',
                        'until',
                        'with_stats',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'ref_name': {'type': 'string', 'required': False},
                        'since': {'type': 'string', 'required': False},
                        'until': {'type': 'string', 'required': False},
                        'with_stats': {'type': 'boolean', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab commit',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Commit SHA'},
                                'short_id': {'type': 'string', 'description': 'Short commit SHA'},
                                'title': {'type': 'string', 'description': 'Commit title'},
                                'message': {'type': 'string', 'description': 'Commit message'},
                                'author_name': {'type': 'string', 'description': 'Author name'},
                                'author_email': {'type': 'string', 'description': 'Author email'},
                                'authored_date': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Authored date',
                                },
                                'committer_name': {'type': 'string', 'description': 'Committer name'},
                                'committer_email': {'type': 'string', 'description': 'Committer email'},
                                'committed_date': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Committed date',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Created at timestamp',
                                },
                                'parent_ids': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Parent commit SHAs',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'stats': {
                                    'type': ['null', 'object'],
                                    'description': 'Commit stats',
                                    'properties': {
                                        'additions': {'type': 'integer', 'description': 'Lines added'},
                                        'deletions': {'type': 'integer', 'description': 'Lines deleted'},
                                        'total': {'type': 'integer', 'description': 'Total changes'},
                                    },
                                },
                                'trailers': {
                                    'type': ['null', 'object'],
                                    'description': 'Git trailers parsed from the commit message',
                                },
                                'extended_trailers': {
                                    'type': ['null', 'object'],
                                    'description': 'Extended git trailers with support for multi-value keys',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'commits',
                            'x-airbyte-stream-name': 'commits',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/repository/commits/{sha}',
                    action=Action.GET,
                    description='Get a specific commit identified by the commit hash or name of a branch or tag.',
                    query_params=['stats'],
                    query_params_schema={
                        'stats': {'type': 'boolean', 'required': False},
                    },
                    path_params=['project_id', 'sha'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'sha': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab commit',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Commit SHA'},
                            'short_id': {'type': 'string', 'description': 'Short commit SHA'},
                            'title': {'type': 'string', 'description': 'Commit title'},
                            'message': {'type': 'string', 'description': 'Commit message'},
                            'author_name': {'type': 'string', 'description': 'Author name'},
                            'author_email': {'type': 'string', 'description': 'Author email'},
                            'authored_date': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Authored date',
                            },
                            'committer_name': {'type': 'string', 'description': 'Committer name'},
                            'committer_email': {'type': 'string', 'description': 'Committer email'},
                            'committed_date': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Committed date',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Created at timestamp',
                            },
                            'parent_ids': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Parent commit SHAs',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'stats': {
                                'type': ['null', 'object'],
                                'description': 'Commit stats',
                                'properties': {
                                    'additions': {'type': 'integer', 'description': 'Lines added'},
                                    'deletions': {'type': 'integer', 'description': 'Lines deleted'},
                                    'total': {'type': 'integer', 'description': 'Total changes'},
                                },
                            },
                            'trailers': {
                                'type': ['null', 'object'],
                                'description': 'Git trailers parsed from the commit message',
                            },
                            'extended_trailers': {
                                'type': ['null', 'object'],
                                'description': 'Extended git trailers with support for multi-value keys',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'commits',
                        'x-airbyte-stream-name': 'commits',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab commit',
                'properties': {
                    'id': {'type': 'string', 'description': 'Commit SHA'},
                    'short_id': {'type': 'string', 'description': 'Short commit SHA'},
                    'title': {'type': 'string', 'description': 'Commit title'},
                    'message': {'type': 'string', 'description': 'Commit message'},
                    'author_name': {'type': 'string', 'description': 'Author name'},
                    'author_email': {'type': 'string', 'description': 'Author email'},
                    'authored_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Authored date',
                    },
                    'committer_name': {'type': 'string', 'description': 'Committer name'},
                    'committer_email': {'type': 'string', 'description': 'Committer email'},
                    'committed_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Committed date',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Created at timestamp',
                    },
                    'parent_ids': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Parent commit SHAs',
                    },
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'stats': {
                        'type': ['null', 'object'],
                        'description': 'Commit stats',
                        'properties': {
                            'additions': {'type': 'integer', 'description': 'Lines added'},
                            'deletions': {'type': 'integer', 'description': 'Lines deleted'},
                            'total': {'type': 'integer', 'description': 'Total changes'},
                        },
                    },
                    'trailers': {
                        'type': ['null', 'object'],
                        'description': 'Git trailers parsed from the commit message',
                    },
                    'extended_trailers': {
                        'type': ['null', 'object'],
                        'description': 'Extended git trailers with support for multi-value keys',
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'commits',
                'x-airbyte-stream-name': 'commits',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='commits',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='groups',
            stream_name='groups',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/groups',
                    action=Action.LIST,
                    description='Get a list of visible groups for the authenticated user.',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'owned',
                        'order_by',
                        'sort',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'search': {'type': 'string', 'required': False},
                        'owned': {'type': 'boolean', 'required': False},
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab group',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Group ID'},
                                'name': {'type': 'string', 'description': 'Group name'},
                                'path': {'type': 'string', 'description': 'Group path'},
                                'full_name': {'type': 'string', 'description': 'Full group name'},
                                'full_path': {'type': 'string', 'description': 'Full group path'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Group description',
                                },
                                'visibility': {'type': 'string', 'description': 'Visibility level'},
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'avatar_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Avatar URL',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'parent_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the parent group',
                                },
                                'organization_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the organization',
                                },
                                'default_branch': {
                                    'type': ['null', 'string'],
                                    'description': 'Default branch of the group',
                                },
                                'default_branch_protection': {
                                    'type': ['null', 'integer'],
                                    'description': 'Default branch protection level',
                                },
                                'default_branch_protection_defaults': {
                                    'type': ['null', 'object'],
                                    'description': 'Default branch protection settings',
                                },
                                'share_with_group_lock': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether sharing with other groups is locked',
                                },
                                'require_two_factor_authentication': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether 2FA is required',
                                },
                                'two_factor_grace_period': {
                                    'type': ['null', 'integer'],
                                    'description': 'Grace period for enabling 2FA',
                                },
                                'project_creation_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Project creation permission level',
                                },
                                'auto_devops_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether Auto DevOps is enabled',
                                },
                                'subgroup_creation_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Subgroup creation permission level',
                                },
                                'emails_disabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether emails are disabled',
                                },
                                'emails_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether emails are enabled',
                                },
                                'mentions_disabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether mentions are disabled',
                                },
                                'lfs_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether Git LFS is enabled',
                                },
                                'request_access_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether request access is enabled',
                                },
                                'shared_runners_setting': {
                                    'type': ['null', 'string'],
                                    'description': 'Shared runners setting',
                                },
                                'ldap_cn': {
                                    'type': ['null', 'string'],
                                    'description': 'LDAP CN for the group',
                                },
                                'ldap_access': {
                                    'type': ['null', 'string'],
                                    'description': 'LDAP access level',
                                },
                                'wiki_access_level': {
                                    'type': ['null', 'string'],
                                    'description': 'Wiki access level',
                                },
                                'marked_for_deletion_on': {
                                    'type': ['null', 'string'],
                                    'description': 'Date marked for deletion',
                                },
                                'archived': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the group is archived',
                                },
                                'math_rendering_limits_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether math rendering limits are enabled',
                                },
                                'lock_math_rendering_limits_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether math rendering limits are locked',
                                },
                                'max_artifacts_size': {
                                    'type': ['null', 'integer'],
                                    'description': 'Maximum artifacts size in MB',
                                },
                                'show_diff_preview_in_email': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether diff previews are shown in emails',
                                },
                                'web_based_commit_signing_enabled': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether web-based commit signing is enabled',
                                },
                                'duo_namespace_access_rules': {
                                    'type': ['null', 'array'],
                                    'description': 'Duo namespace access rules',
                                },
                                'shared_with_groups': {
                                    'type': ['null', 'array'],
                                    'description': 'Groups that this group is shared with',
                                },
                                'runners_token': {
                                    'type': ['null', 'string'],
                                    'description': 'Runner registration token',
                                },
                                'enabled_git_access_protocol': {
                                    'type': ['null', 'string'],
                                    'description': 'Enabled Git access protocol',
                                },
                                'prevent_sharing_groups_outside_hierarchy': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Prevent sharing groups outside hierarchy',
                                },
                                'projects': {
                                    'type': ['null', 'array'],
                                    'description': 'Projects in the group',
                                },
                                'shared_projects': {
                                    'type': ['null', 'array'],
                                    'description': 'Projects shared with the group',
                                },
                                'shared_runners_minutes_limit': {
                                    'type': ['null', 'integer'],
                                    'description': 'Shared runners minutes limit',
                                },
                                'extra_shared_runners_minutes_limit': {
                                    'type': ['null', 'integer'],
                                    'description': 'Extra shared runners minutes limit',
                                },
                                'prevent_forking_outside_group': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Prevent forking outside the group',
                                },
                                'membership_lock': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether membership is locked',
                                },
                                'ip_restriction_ranges': {
                                    'type': ['null', 'string'],
                                    'description': 'IP restriction ranges',
                                },
                                'service_access_tokens_expiration_enforced': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Service access tokens expiration enforced',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'groups',
                            'x-airbyte-stream-name': 'groups',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/groups/{id}',
                    action=Action.GET,
                    description='Get all details of a group.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab group',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Group ID'},
                            'name': {'type': 'string', 'description': 'Group name'},
                            'path': {'type': 'string', 'description': 'Group path'},
                            'full_name': {'type': 'string', 'description': 'Full group name'},
                            'full_path': {'type': 'string', 'description': 'Full group path'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Group description',
                            },
                            'visibility': {'type': 'string', 'description': 'Visibility level'},
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': 'Avatar URL',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'parent_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the parent group',
                            },
                            'organization_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the organization',
                            },
                            'default_branch': {
                                'type': ['null', 'string'],
                                'description': 'Default branch of the group',
                            },
                            'default_branch_protection': {
                                'type': ['null', 'integer'],
                                'description': 'Default branch protection level',
                            },
                            'default_branch_protection_defaults': {
                                'type': ['null', 'object'],
                                'description': 'Default branch protection settings',
                            },
                            'share_with_group_lock': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether sharing with other groups is locked',
                            },
                            'require_two_factor_authentication': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether 2FA is required',
                            },
                            'two_factor_grace_period': {
                                'type': ['null', 'integer'],
                                'description': 'Grace period for enabling 2FA',
                            },
                            'project_creation_level': {
                                'type': ['null', 'string'],
                                'description': 'Project creation permission level',
                            },
                            'auto_devops_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether Auto DevOps is enabled',
                            },
                            'subgroup_creation_level': {
                                'type': ['null', 'string'],
                                'description': 'Subgroup creation permission level',
                            },
                            'emails_disabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether emails are disabled',
                            },
                            'emails_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether emails are enabled',
                            },
                            'mentions_disabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether mentions are disabled',
                            },
                            'lfs_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether Git LFS is enabled',
                            },
                            'request_access_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether request access is enabled',
                            },
                            'shared_runners_setting': {
                                'type': ['null', 'string'],
                                'description': 'Shared runners setting',
                            },
                            'ldap_cn': {
                                'type': ['null', 'string'],
                                'description': 'LDAP CN for the group',
                            },
                            'ldap_access': {
                                'type': ['null', 'string'],
                                'description': 'LDAP access level',
                            },
                            'wiki_access_level': {
                                'type': ['null', 'string'],
                                'description': 'Wiki access level',
                            },
                            'marked_for_deletion_on': {
                                'type': ['null', 'string'],
                                'description': 'Date marked for deletion',
                            },
                            'archived': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the group is archived',
                            },
                            'math_rendering_limits_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether math rendering limits are enabled',
                            },
                            'lock_math_rendering_limits_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether math rendering limits are locked',
                            },
                            'max_artifacts_size': {
                                'type': ['null', 'integer'],
                                'description': 'Maximum artifacts size in MB',
                            },
                            'show_diff_preview_in_email': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether diff previews are shown in emails',
                            },
                            'web_based_commit_signing_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether web-based commit signing is enabled',
                            },
                            'duo_namespace_access_rules': {
                                'type': ['null', 'array'],
                                'description': 'Duo namespace access rules',
                            },
                            'shared_with_groups': {
                                'type': ['null', 'array'],
                                'description': 'Groups that this group is shared with',
                            },
                            'runners_token': {
                                'type': ['null', 'string'],
                                'description': 'Runner registration token',
                            },
                            'enabled_git_access_protocol': {
                                'type': ['null', 'string'],
                                'description': 'Enabled Git access protocol',
                            },
                            'prevent_sharing_groups_outside_hierarchy': {
                                'type': ['null', 'boolean'],
                                'description': 'Prevent sharing groups outside hierarchy',
                            },
                            'projects': {
                                'type': ['null', 'array'],
                                'description': 'Projects in the group',
                            },
                            'shared_projects': {
                                'type': ['null', 'array'],
                                'description': 'Projects shared with the group',
                            },
                            'shared_runners_minutes_limit': {
                                'type': ['null', 'integer'],
                                'description': 'Shared runners minutes limit',
                            },
                            'extra_shared_runners_minutes_limit': {
                                'type': ['null', 'integer'],
                                'description': 'Extra shared runners minutes limit',
                            },
                            'prevent_forking_outside_group': {
                                'type': ['null', 'boolean'],
                                'description': 'Prevent forking outside the group',
                            },
                            'membership_lock': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether membership is locked',
                            },
                            'ip_restriction_ranges': {
                                'type': ['null', 'string'],
                                'description': 'IP restriction ranges',
                            },
                            'service_access_tokens_expiration_enforced': {
                                'type': ['null', 'boolean'],
                                'description': 'Service access tokens expiration enforced',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'groups',
                        'x-airbyte-stream-name': 'groups',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab group',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Group ID'},
                    'name': {'type': 'string', 'description': 'Group name'},
                    'path': {'type': 'string', 'description': 'Group path'},
                    'full_name': {'type': 'string', 'description': 'Full group name'},
                    'full_path': {'type': 'string', 'description': 'Full group path'},
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Group description',
                    },
                    'visibility': {'type': 'string', 'description': 'Visibility level'},
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'avatar_url': {
                        'type': ['null', 'string'],
                        'description': 'Avatar URL',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'parent_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the parent group',
                    },
                    'organization_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the organization',
                    },
                    'default_branch': {
                        'type': ['null', 'string'],
                        'description': 'Default branch of the group',
                    },
                    'default_branch_protection': {
                        'type': ['null', 'integer'],
                        'description': 'Default branch protection level',
                    },
                    'default_branch_protection_defaults': {
                        'type': ['null', 'object'],
                        'description': 'Default branch protection settings',
                    },
                    'share_with_group_lock': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether sharing with other groups is locked',
                    },
                    'require_two_factor_authentication': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether 2FA is required',
                    },
                    'two_factor_grace_period': {
                        'type': ['null', 'integer'],
                        'description': 'Grace period for enabling 2FA',
                    },
                    'project_creation_level': {
                        'type': ['null', 'string'],
                        'description': 'Project creation permission level',
                    },
                    'auto_devops_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether Auto DevOps is enabled',
                    },
                    'subgroup_creation_level': {
                        'type': ['null', 'string'],
                        'description': 'Subgroup creation permission level',
                    },
                    'emails_disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether emails are disabled',
                    },
                    'emails_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether emails are enabled',
                    },
                    'mentions_disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether mentions are disabled',
                    },
                    'lfs_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether Git LFS is enabled',
                    },
                    'request_access_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether request access is enabled',
                    },
                    'shared_runners_setting': {
                        'type': ['null', 'string'],
                        'description': 'Shared runners setting',
                    },
                    'ldap_cn': {
                        'type': ['null', 'string'],
                        'description': 'LDAP CN for the group',
                    },
                    'ldap_access': {
                        'type': ['null', 'string'],
                        'description': 'LDAP access level',
                    },
                    'wiki_access_level': {
                        'type': ['null', 'string'],
                        'description': 'Wiki access level',
                    },
                    'marked_for_deletion_on': {
                        'type': ['null', 'string'],
                        'description': 'Date marked for deletion',
                    },
                    'archived': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the group is archived',
                    },
                    'math_rendering_limits_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether math rendering limits are enabled',
                    },
                    'lock_math_rendering_limits_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether math rendering limits are locked',
                    },
                    'max_artifacts_size': {
                        'type': ['null', 'integer'],
                        'description': 'Maximum artifacts size in MB',
                    },
                    'show_diff_preview_in_email': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether diff previews are shown in emails',
                    },
                    'web_based_commit_signing_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether web-based commit signing is enabled',
                    },
                    'duo_namespace_access_rules': {
                        'type': ['null', 'array'],
                        'description': 'Duo namespace access rules',
                    },
                    'shared_with_groups': {
                        'type': ['null', 'array'],
                        'description': 'Groups that this group is shared with',
                    },
                    'runners_token': {
                        'type': ['null', 'string'],
                        'description': 'Runner registration token',
                    },
                    'enabled_git_access_protocol': {
                        'type': ['null', 'string'],
                        'description': 'Enabled Git access protocol',
                    },
                    'prevent_sharing_groups_outside_hierarchy': {
                        'type': ['null', 'boolean'],
                        'description': 'Prevent sharing groups outside hierarchy',
                    },
                    'projects': {
                        'type': ['null', 'array'],
                        'description': 'Projects in the group',
                    },
                    'shared_projects': {
                        'type': ['null', 'array'],
                        'description': 'Projects shared with the group',
                    },
                    'shared_runners_minutes_limit': {
                        'type': ['null', 'integer'],
                        'description': 'Shared runners minutes limit',
                    },
                    'extra_shared_runners_minutes_limit': {
                        'type': ['null', 'integer'],
                        'description': 'Extra shared runners minutes limit',
                    },
                    'prevent_forking_outside_group': {
                        'type': ['null', 'boolean'],
                        'description': 'Prevent forking outside the group',
                    },
                    'membership_lock': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether membership is locked',
                    },
                    'ip_restriction_ranges': {
                        'type': ['null', 'string'],
                        'description': 'IP restriction ranges',
                    },
                    'service_access_tokens_expiration_enforced': {
                        'type': ['null', 'boolean'],
                        'description': 'Service access tokens expiration enforced',
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'groups',
                'x-airbyte-stream-name': 'groups',
            },
        ),
        EntityDefinition(
            name='branches',
            stream_name='branches',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/repository/branches',
                    action=Action.LIST,
                    description='Get a list of repository branches from a project.',
                    query_params=['page', 'per_page', 'search'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'search': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab branch',
                            'properties': {
                                'name': {'type': 'string', 'description': 'Branch name'},
                                'merged': {'type': 'boolean', 'description': 'Whether the branch has been merged'},
                                'protected': {'type': 'boolean', 'description': 'Whether the branch is protected'},
                                'default': {'type': 'boolean', 'description': 'Whether this is the default branch'},
                                'developers_can_push': {'type': 'boolean', 'description': 'Whether developers can push'},
                                'developers_can_merge': {'type': 'boolean', 'description': 'Whether developers can merge'},
                                'can_push': {'type': 'boolean', 'description': 'Whether the current user can push'},
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'commit': {
                                    'type': ['null', 'object'],
                                    'description': 'Latest commit on this branch',
                                },
                            },
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'branches',
                            'x-airbyte-stream-name': 'branches',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/repository/branches/{branch}',
                    action=Action.GET,
                    description='Get a single project repository branch.',
                    path_params=['project_id', 'branch'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'branch': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab branch',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Branch name'},
                            'merged': {'type': 'boolean', 'description': 'Whether the branch has been merged'},
                            'protected': {'type': 'boolean', 'description': 'Whether the branch is protected'},
                            'default': {'type': 'boolean', 'description': 'Whether this is the default branch'},
                            'developers_can_push': {'type': 'boolean', 'description': 'Whether developers can push'},
                            'developers_can_merge': {'type': 'boolean', 'description': 'Whether developers can merge'},
                            'can_push': {'type': 'boolean', 'description': 'Whether the current user can push'},
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'commit': {
                                'type': ['null', 'object'],
                                'description': 'Latest commit on this branch',
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'branches',
                        'x-airbyte-stream-name': 'branches',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab branch',
                'properties': {
                    'name': {'type': 'string', 'description': 'Branch name'},
                    'merged': {'type': 'boolean', 'description': 'Whether the branch has been merged'},
                    'protected': {'type': 'boolean', 'description': 'Whether the branch is protected'},
                    'default': {'type': 'boolean', 'description': 'Whether this is the default branch'},
                    'developers_can_push': {'type': 'boolean', 'description': 'Whether developers can push'},
                    'developers_can_merge': {'type': 'boolean', 'description': 'Whether developers can merge'},
                    'can_push': {'type': 'boolean', 'description': 'Whether the current user can push'},
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'commit': {
                        'type': ['null', 'object'],
                        'description': 'Latest commit on this branch',
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'branches',
                'x-airbyte-stream-name': 'branches',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='branches',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='pipelines',
            stream_name='pipelines',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/pipelines',
                    action=Action.LIST,
                    description='List pipelines in a project.',
                    query_params=[
                        'page',
                        'per_page',
                        'status',
                        'ref',
                        'order_by',
                        'sort',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'status': {'type': 'string', 'required': False},
                        'ref': {'type': 'string', 'required': False},
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab CI/CD pipeline',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Pipeline ID'},
                                'iid': {'type': 'integer', 'description': 'Pipeline internal ID'},
                                'project_id': {'type': 'integer', 'description': 'Project ID'},
                                'status': {'type': 'string', 'description': 'Pipeline status'},
                                'ref': {'type': 'string', 'description': 'Branch or tag reference'},
                                'sha': {'type': 'string', 'description': 'Commit SHA'},
                                'source': {'type': 'string', 'description': 'Pipeline source'},
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Last update timestamp',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Pipeline name',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'pipelines',
                            'x-airbyte-stream-name': 'pipelines',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/pipelines/{pipeline_id}',
                    action=Action.GET,
                    description='Get one pipeline of a project.',
                    path_params=['project_id', 'pipeline_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'pipeline_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab CI/CD pipeline',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Pipeline ID'},
                            'iid': {'type': 'integer', 'description': 'Pipeline internal ID'},
                            'project_id': {'type': 'integer', 'description': 'Project ID'},
                            'status': {'type': 'string', 'description': 'Pipeline status'},
                            'ref': {'type': 'string', 'description': 'Branch or tag reference'},
                            'sha': {'type': 'string', 'description': 'Commit SHA'},
                            'source': {'type': 'string', 'description': 'Pipeline source'},
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Pipeline name',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'pipelines',
                        'x-airbyte-stream-name': 'pipelines',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab CI/CD pipeline',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Pipeline ID'},
                    'iid': {'type': 'integer', 'description': 'Pipeline internal ID'},
                    'project_id': {'type': 'integer', 'description': 'Project ID'},
                    'status': {'type': 'string', 'description': 'Pipeline status'},
                    'ref': {'type': 'string', 'description': 'Branch or tag reference'},
                    'sha': {'type': 'string', 'description': 'Commit SHA'},
                    'source': {'type': 'string', 'description': 'Pipeline source'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'web_url': {'type': 'string', 'description': 'Web URL'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Pipeline name',
                    },
                },
                'required': ['id'],
                'additionalProperties': True,
                'x-airbyte-entity-name': 'pipelines',
                'x-airbyte-stream-name': 'pipelines',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='pipelines',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='group_members',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/groups/{group_id}/members',
                    action=Action.LIST,
                    description='Gets a list of group members viewable by the authenticated user.',
                    query_params=['page', 'per_page', 'query'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'query': {'type': 'string', 'required': False},
                    },
                    path_params=['group_id'],
                    path_params_schema={
                        'group_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab group or project member',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'User ID'},
                                'username': {'type': 'string', 'description': 'Username'},
                                'name': {'type': 'string', 'description': 'Full name'},
                                'state': {'type': 'string', 'description': 'User state'},
                                'avatar_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Avatar URL',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'access_level': {'type': 'integer', 'description': 'Access level (10=Guest, 20=Reporter, 30=Developer, 40=Maintainer, 50=Owner)'},
                                'expires_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Membership expiration date',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the membership was created',
                                },
                                'locked': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the member account is locked',
                                },
                                'membership_state': {
                                    'type': ['null', 'string'],
                                    'description': 'State of the membership',
                                },
                                'public_email': {
                                    'type': ['null', 'string'],
                                    'description': "Member's public email address",
                                },
                                'created_by': {
                                    'type': ['null', 'object'],
                                    'description': 'User who created this membership',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/groups/{group_id}/members/{user_id}',
                    action=Action.GET,
                    description='Get a member of a group.',
                    path_params=['group_id', 'user_id'],
                    path_params_schema={
                        'group_id': {'type': 'string', 'required': True},
                        'user_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab group or project member',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'User ID'},
                            'username': {'type': 'string', 'description': 'Username'},
                            'name': {'type': 'string', 'description': 'Full name'},
                            'state': {'type': 'string', 'description': 'User state'},
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': 'Avatar URL',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'access_level': {'type': 'integer', 'description': 'Access level (10=Guest, 20=Reporter, 30=Developer, 40=Maintainer, 50=Owner)'},
                            'expires_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Membership expiration date',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the membership was created',
                            },
                            'locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the member account is locked',
                            },
                            'membership_state': {
                                'type': ['null', 'string'],
                                'description': 'State of the membership',
                            },
                            'public_email': {
                                'type': ['null', 'string'],
                                'description': "Member's public email address",
                            },
                            'created_by': {
                                'type': ['null', 'object'],
                                'description': 'User who created this membership',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                    },
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='group_members',
                    target_entity='groups',
                    foreign_key='group_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='project_members',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/members',
                    action=Action.LIST,
                    description='Gets a list of project members viewable by the authenticated user.',
                    query_params=['page', 'per_page', 'query'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'query': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab group or project member',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'User ID'},
                                'username': {'type': 'string', 'description': 'Username'},
                                'name': {'type': 'string', 'description': 'Full name'},
                                'state': {'type': 'string', 'description': 'User state'},
                                'avatar_url': {
                                    'type': ['null', 'string'],
                                    'description': 'Avatar URL',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'access_level': {'type': 'integer', 'description': 'Access level (10=Guest, 20=Reporter, 30=Developer, 40=Maintainer, 50=Owner)'},
                                'expires_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Membership expiration date',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the membership was created',
                                },
                                'locked': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the member account is locked',
                                },
                                'membership_state': {
                                    'type': ['null', 'string'],
                                    'description': 'State of the membership',
                                },
                                'public_email': {
                                    'type': ['null', 'string'],
                                    'description': "Member's public email address",
                                },
                                'created_by': {
                                    'type': ['null', 'object'],
                                    'description': 'User who created this membership',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/members/{user_id}',
                    action=Action.GET,
                    description='Get a member of a project.',
                    path_params=['project_id', 'user_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'user_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab group or project member',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'User ID'},
                            'username': {'type': 'string', 'description': 'Username'},
                            'name': {'type': 'string', 'description': 'Full name'},
                            'state': {'type': 'string', 'description': 'User state'},
                            'avatar_url': {
                                'type': ['null', 'string'],
                                'description': 'Avatar URL',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'access_level': {'type': 'integer', 'description': 'Access level (10=Guest, 20=Reporter, 30=Developer, 40=Maintainer, 50=Owner)'},
                            'expires_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Membership expiration date',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the membership was created',
                            },
                            'locked': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the member account is locked',
                            },
                            'membership_state': {
                                'type': ['null', 'string'],
                                'description': 'State of the membership',
                            },
                            'public_email': {
                                'type': ['null', 'string'],
                                'description': "Member's public email address",
                            },
                            'created_by': {
                                'type': ['null', 'object'],
                                'description': 'User who created this membership',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                    },
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='project_members',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='releases',
            stream_name='releases',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/releases',
                    action=Action.LIST,
                    description='Paginated list of releases for a given project, sorted by released_at.',
                    query_params=[
                        'page',
                        'per_page',
                        'order_by',
                        'sort',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab release',
                            'properties': {
                                'name': {'type': 'string', 'description': 'Release name'},
                                'tag_name': {'type': 'string', 'description': 'Tag name'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Release description',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'released_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Release timestamp',
                                },
                                'author': {'type': 'object', 'description': 'Author'},
                                'commit': {'type': 'object', 'description': 'Commit info'},
                                'upcoming_release': {'type': 'boolean', 'description': 'Whether this is upcoming'},
                                '_links': {'type': 'object', 'description': 'Related links'},
                                'assets': {
                                    'type': ['null', 'object'],
                                    'description': 'Release assets (sources and links)',
                                },
                                'milestones': {
                                    'type': ['null', 'array'],
                                    'description': 'Milestones associated with the release',
                                },
                                'evidences': {
                                    'type': ['null', 'array'],
                                    'description': 'Release evidences',
                                },
                                'commit_path': {
                                    'type': ['null', 'string'],
                                    'description': 'Path to the commit',
                                },
                                'tag_path': {
                                    'type': ['null', 'string'],
                                    'description': 'Path to the tag',
                                },
                            },
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'releases',
                            'x-airbyte-stream-name': 'releases',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/releases/{tag_name}',
                    action=Action.GET,
                    description='Get a release for the given tag.',
                    path_params=['project_id', 'tag_name'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'tag_name': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab release',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Release name'},
                            'tag_name': {'type': 'string', 'description': 'Tag name'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Release description',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'released_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Release timestamp',
                            },
                            'author': {'type': 'object', 'description': 'Author'},
                            'commit': {'type': 'object', 'description': 'Commit info'},
                            'upcoming_release': {'type': 'boolean', 'description': 'Whether this is upcoming'},
                            '_links': {'type': 'object', 'description': 'Related links'},
                            'assets': {
                                'type': ['null', 'object'],
                                'description': 'Release assets (sources and links)',
                            },
                            'milestones': {
                                'type': ['null', 'array'],
                                'description': 'Milestones associated with the release',
                            },
                            'evidences': {
                                'type': ['null', 'array'],
                                'description': 'Release evidences',
                            },
                            'commit_path': {
                                'type': ['null', 'string'],
                                'description': 'Path to the commit',
                            },
                            'tag_path': {
                                'type': ['null', 'string'],
                                'description': 'Path to the tag',
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'releases',
                        'x-airbyte-stream-name': 'releases',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab release',
                'properties': {
                    'name': {'type': 'string', 'description': 'Release name'},
                    'tag_name': {'type': 'string', 'description': 'Tag name'},
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Release description',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'released_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Release timestamp',
                    },
                    'author': {'type': 'object', 'description': 'Author'},
                    'commit': {'type': 'object', 'description': 'Commit info'},
                    'upcoming_release': {'type': 'boolean', 'description': 'Whether this is upcoming'},
                    '_links': {'type': 'object', 'description': 'Related links'},
                    'assets': {
                        'type': ['null', 'object'],
                        'description': 'Release assets (sources and links)',
                    },
                    'milestones': {
                        'type': ['null', 'array'],
                        'description': 'Milestones associated with the release',
                    },
                    'evidences': {
                        'type': ['null', 'array'],
                        'description': 'Release evidences',
                    },
                    'commit_path': {
                        'type': ['null', 'string'],
                        'description': 'Path to the commit',
                    },
                    'tag_path': {
                        'type': ['null', 'string'],
                        'description': 'Path to the tag',
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'releases',
                'x-airbyte-stream-name': 'releases',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='releases',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='tags',
            stream_name='tags',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/repository/tags',
                    action=Action.LIST,
                    description='Get a list of repository tags from a project, sorted by update date and time in descending order.',
                    query_params=[
                        'page',
                        'per_page',
                        'search',
                        'order_by',
                        'sort',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'search': {'type': 'string', 'required': False},
                        'order_by': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab repository tag',
                            'properties': {
                                'name': {'type': 'string', 'description': 'Tag name'},
                                'message': {
                                    'type': ['null', 'string'],
                                    'description': 'Tag message',
                                },
                                'target': {'type': 'string', 'description': 'Commit SHA the tag points to'},
                                'commit': {'type': 'object', 'description': 'Commit info'},
                                'release': {
                                    'type': ['null', 'object'],
                                    'description': 'Associated release info',
                                },
                                'protected': {'type': 'boolean', 'description': 'Whether the tag is protected'},
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Tag creation timestamp',
                                },
                            },
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'tags',
                            'x-airbyte-stream-name': 'tags',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/repository/tags/{tag_name}',
                    action=Action.GET,
                    description='Get a specific repository tag determined by its name.',
                    path_params=['project_id', 'tag_name'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'tag_name': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab repository tag',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Tag name'},
                            'message': {
                                'type': ['null', 'string'],
                                'description': 'Tag message',
                            },
                            'target': {'type': 'string', 'description': 'Commit SHA the tag points to'},
                            'commit': {'type': 'object', 'description': 'Commit info'},
                            'release': {
                                'type': ['null', 'object'],
                                'description': 'Associated release info',
                            },
                            'protected': {'type': 'boolean', 'description': 'Whether the tag is protected'},
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Tag creation timestamp',
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'tags',
                        'x-airbyte-stream-name': 'tags',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'GitLab repository tag',
                'properties': {
                    'name': {'type': 'string', 'description': 'Tag name'},
                    'message': {
                        'type': ['null', 'string'],
                        'description': 'Tag message',
                    },
                    'target': {'type': 'string', 'description': 'Commit SHA the tag points to'},
                    'commit': {'type': 'object', 'description': 'Commit info'},
                    'release': {
                        'type': ['null', 'object'],
                        'description': 'Associated release info',
                    },
                    'protected': {'type': 'boolean', 'description': 'Whether the tag is protected'},
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Tag creation timestamp',
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'tags',
                'x-airbyte-stream-name': 'tags',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tags',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='group_milestones',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/groups/{group_id}/milestones',
                    action=Action.LIST,
                    description='Returns a list of group milestones.',
                    query_params=[
                        'page',
                        'per_page',
                        'state',
                        'search',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'state': {'type': 'string', 'required': False},
                        'search': {'type': 'string', 'required': False},
                    },
                    path_params=['group_id'],
                    path_params_schema={
                        'group_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab milestone',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Milestone ID'},
                                'iid': {'type': 'integer', 'description': 'Internal ID'},
                                'title': {'type': 'string', 'description': 'Milestone title'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Milestone description',
                                },
                                'state': {'type': 'string', 'description': 'Milestone state (active/closed)'},
                                'due_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Due date',
                                },
                                'start_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Start date',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Last update timestamp',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'expired': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the milestone has expired',
                                },
                                'group_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the group (for group milestones)',
                                },
                                'project_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the project (for project milestones)',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/groups/{group_id}/milestones/{milestone_id}',
                    action=Action.GET,
                    description='Get a single group milestone.',
                    path_params=['group_id', 'milestone_id'],
                    path_params_schema={
                        'group_id': {'type': 'string', 'required': True},
                        'milestone_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab milestone',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Milestone ID'},
                            'iid': {'type': 'integer', 'description': 'Internal ID'},
                            'title': {'type': 'string', 'description': 'Milestone title'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Milestone description',
                            },
                            'state': {'type': 'string', 'description': 'Milestone state (active/closed)'},
                            'due_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Due date',
                            },
                            'start_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Start date',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'expired': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the milestone has expired',
                            },
                            'group_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the group (for group milestones)',
                            },
                            'project_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the project (for project milestones)',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                    },
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='group_milestones',
                    target_entity='groups',
                    foreign_key='group_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='project_milestones',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/milestones',
                    action=Action.LIST,
                    description='Returns a list of project milestones.',
                    query_params=[
                        'page',
                        'per_page',
                        'state',
                        'search',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'state': {'type': 'string', 'required': False},
                        'search': {'type': 'string', 'required': False},
                    },
                    path_params=['project_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'GitLab milestone',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Milestone ID'},
                                'iid': {'type': 'integer', 'description': 'Internal ID'},
                                'title': {'type': 'string', 'description': 'Milestone title'},
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Milestone description',
                                },
                                'state': {'type': 'string', 'description': 'Milestone state (active/closed)'},
                                'due_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Due date',
                                },
                                'start_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Start date',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Creation timestamp',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'Last update timestamp',
                                },
                                'web_url': {'type': 'string', 'description': 'Web URL'},
                                'expired': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the milestone has expired',
                                },
                                'group_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the group (for group milestones)',
                                },
                                'project_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the project (for project milestones)',
                                },
                            },
                            'required': ['id'],
                            'additionalProperties': True,
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_id}/milestones/{milestone_id}',
                    action=Action.GET,
                    description='Get a single project milestone.',
                    path_params=['project_id', 'milestone_id'],
                    path_params_schema={
                        'project_id': {'type': 'string', 'required': True},
                        'milestone_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GitLab milestone',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Milestone ID'},
                            'iid': {'type': 'integer', 'description': 'Internal ID'},
                            'title': {'type': 'string', 'description': 'Milestone title'},
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Milestone description',
                            },
                            'state': {'type': 'string', 'description': 'Milestone state (active/closed)'},
                            'due_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Due date',
                            },
                            'start_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Start date',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Creation timestamp',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'web_url': {'type': 'string', 'description': 'Web URL'},
                            'expired': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the milestone has expired',
                            },
                            'group_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the group (for group milestones)',
                            },
                            'project_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the project (for project milestones)',
                            },
                        },
                        'required': ['id'],
                        'additionalProperties': True,
                    },
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='project_milestones',
                    target_entity='projects',
                    foreign_key='project_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    search_field_paths={
        'projects': [
            'id',
            'description',
            'description_html',
            'name',
            'name_with_namespace',
            'path',
            'path_with_namespace',
            'created_at',
            'updated_at',
            'default_branch',
            'tag_list',
            'tag_list[]',
            'topics',
            'topics[]',
            'ssh_url_to_repo',
            'http_url_to_repo',
            'web_url',
            'readme_url',
            'avatar_url',
            'forks_count',
            'star_count',
            'last_activity_at',
            'namespace',
            'container_registry_image_prefix',
            '_links',
            'packages_enabled',
            'empty_repo',
            'archived',
            'visibility',
            'resolve_outdated_diff_discussions',
            'container_registry_enabled',
            'container_expiration_policy',
            'issues_enabled',
            'merge_requests_enabled',
            'wiki_enabled',
            'jobs_enabled',
            'snippets_enabled',
            'service_desk_enabled',
            'service_desk_address',
            'can_create_merge_request_in',
            'issues_access_level',
            'repository_access_level',
            'merge_requests_access_level',
            'forking_access_level',
            'wiki_access_level',
            'builds_access_level',
            'snippets_access_level',
            'pages_access_level',
            'operations_access_level',
            'analytics_access_level',
            'emails_disabled',
            'shared_runners_enabled',
            'lfs_enabled',
            'creator_id',
            'import_status',
            'open_issues_count',
            'ci_default_git_depth',
            'ci_forward_deployment_enabled',
            'public_jobs',
            'build_timeout',
            'auto_cancel_pending_pipelines',
            'ci_config_path',
            'shared_with_groups',
            'shared_with_groups[]',
            'only_allow_merge_if_pipeline_succeeds',
            'allow_merge_on_skipped_pipeline',
            'restrict_user_defined_variables',
            'request_access_enabled',
            'only_allow_merge_if_all_discussions_are_resolved',
            'remove_source_branch_after_merge',
            'printing_merge_request_link_enabled',
            'merge_method',
            'statistics',
            'auto_devops_enabled',
            'auto_devops_deploy_strategy',
            'autoclose_referenced_issues',
            'external_authorization_classification_label',
            'requirements_enabled',
            'security_and_compliance_enabled',
            'compliance_frameworks',
            'compliance_frameworks[]',
            'permissions',
            'keep_latest_artifact',
        ],
        'issues': [
            'id',
            'iid',
            'project_id',
            'title',
            'description',
            'state',
            'created_at',
            'updated_at',
            'closed_at',
            'labels',
            'labels[]',
            'assignees',
            'assignees[]',
            'type',
            'user_notes_count',
            'merge_requests_count',
            'upvotes',
            'downvotes',
            'due_date',
            'confidential',
            'discussion_locked',
            'issue_type',
            'web_url',
            'time_stats',
            'task_completion_status',
            'blocking_issues_count',
            'has_tasks',
            '_links',
            'references',
            'author',
            'author_id',
            'assignee',
            'assignee_id',
            'closed_by',
            'closed_by_id',
            'milestone',
            'milestone_id',
            'weight',
            'severity',
        ],
        'merge_requests': [
            'id',
            'iid',
            'project_id',
            'title',
            'description',
            'state',
            'created_at',
            'updated_at',
            'merged_at',
            'closed_at',
            'target_branch',
            'source_branch',
            'user_notes_count',
            'upvotes',
            'downvotes',
            'assignees',
            'assignees[]',
            'reviewers',
            'reviewers[]',
            'source_project_id',
            'target_project_id',
            'labels',
            'labels[]',
            'work_in_progress',
            'merge_when_pipeline_succeeds',
            'merge_status',
            'sha',
            'merge_commit_sha',
            'squash_commit_sha',
            'discussion_locked',
            'should_remove_source_branch',
            'force_remove_source_branch',
            'reference',
            'references',
            'web_url',
            'time_stats',
            'squash',
            'task_completion_status',
            'has_conflicts',
            'blocking_discussions_resolved',
            'author',
            'author_id',
            'assignee',
            'assignee_id',
            'closed_by',
            'closed_by_id',
            'milestone',
            'milestone_id',
            'merged_by',
            'merged_by_id',
            'draft',
            'detailed_merge_status',
            'merge_user',
        ],
        'users': [
            'id',
            'name',
            'username',
            'state',
            'avatar_url',
            'web_url',
            'locked',
        ],
        'commits': [
            'project_id',
            'id',
            'short_id',
            'created_at',
            'parent_ids',
            'parent_ids[]',
            'title',
            'message',
            'author_name',
            'author_email',
            'authored_date',
            'committer_name',
            'committer_email',
            'committed_date',
            'trailers',
            'web_url',
            'stats',
        ],
        'groups': [
            'id',
            'web_url',
            'name',
            'path',
            'description',
            'visibility',
            'share_with_group_lock',
            'require_two_factor_authentication',
            'two_factor_grace_period',
            'project_creation_level',
            'auto_devops_enabled',
            'subgroup_creation_level',
            'emails_disabled',
            'emails_enabled',
            'mentions_disabled',
            'lfs_enabled',
            'default_branch_protection',
            'avatar_url',
            'request_access_enabled',
            'full_name',
            'full_path',
            'created_at',
            'parent_id',
            'shared_with_groups',
            'shared_with_groups[]',
            'projects',
            'projects[]',
        ],
        'branches': [
            'project_id',
            'name',
            'merged',
            'protected',
            'developers_can_push',
            'developers_can_merge',
            'can_push',
            'default',
            'web_url',
            'commit_id',
            'commit',
        ],
        'pipelines': [
            'id',
            'iid',
            'project_id',
            'sha',
            'source',
            'ref',
            'status',
            'created_at',
            'updated_at',
            'web_url',
            'name',
        ],
        'group_members': [
            'group_id',
            'id',
            'name',
            'username',
            'state',
            'membership_state',
            'avatar_url',
            'web_url',
            'access_level',
            'created_at',
            'expires_at',
            'created_by',
            'locked',
        ],
        'project_members': [
            'project_id',
            'id',
            'name',
            'username',
            'state',
            'membership_state',
            'avatar_url',
            'web_url',
            'access_level',
            'created_at',
            'expires_at',
            'created_by',
            'locked',
        ],
        'releases': [
            'name',
            'tag_name',
            'description',
            'created_at',
            'released_at',
            'upcoming_release',
            'milestones',
            'milestones[]',
            'commit_path',
            'tag_path',
            'assets',
            'evidences',
            'evidences[]',
            '_links',
            'author',
            'author_id',
            'commit',
            'commit_id',
            'project_id',
        ],
        'tags': [
            'name',
            'message',
            'target',
            'release',
            'protected',
            'commit',
            'commit_id',
            'project_id',
        ],
        'group_milestones': [
            'id',
            'iid',
            'group_id',
            'title',
            'description',
            'state',
            'created_at',
            'updated_at',
            'due_date',
            'start_date',
            'expired',
            'web_url',
        ],
        'project_milestones': [
            'id',
            'iid',
            'project_id',
            'title',
            'description',
            'state',
            'created_at',
            'updated_at',
            'due_date',
            'start_date',
            'expired',
            'web_url',
        ],
    },
    server_variable_defaults={'api_url': 'gitlab.com'},
)