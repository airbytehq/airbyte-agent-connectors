# Airbyte Github AI Connector

Type-safe Github API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.18.1

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-github
```

## Usage

```python
from airbyte_ai_github import GithubConnector
from airbyte_ai_github.models import GithubAuthConfig

# Create connector
connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Repositories Operations
- `repositories__get()` - Gets information about a specific GitHub repository using GraphQL
- `repositories__list()` - Returns a list of repositories for the specified user using GraphQL
- `repositories__search()` - Search for GitHub repositories using GitHub's powerful search syntax.
Examples: "language:python stars:>1000", "topic:machine-learning", "org:facebook is:public"


### Org_Repositories Operations
- `org_repositories__list()` - Returns a list of repositories for the specified organization using GraphQL

### Branches Operations
- `branches__list()` - Returns a list of branches for the specified repository using GraphQL
- `branches__get()` - Gets information about a specific branch using GraphQL

### Commits Operations
- `commits__list()` - Returns a list of commits for the default branch using GraphQL
- `commits__get()` - Gets information about a specific commit by SHA using GraphQL

### Releases Operations
- `releases__list()` - Returns a list of releases for the specified repository using GraphQL
- `releases__get()` - Gets information about a specific release by tag name using GraphQL

### Issues Operations
- `issues__list()` - Returns a list of issues for the specified repository using GraphQL
- `issues__get()` - Gets information about a specific issue using GraphQL
- `issues__search()` - Search for issues using GitHub's search syntax

### Pull_Requests Operations
- `pull_requests__list()` - Returns a list of pull requests for the specified repository using GraphQL
- `pull_requests__get()` - Gets information about a specific pull request using GraphQL
- `pull_requests__search()` - Search for pull requests using GitHub's search syntax

### Reviews Operations
- `reviews__list()` - Returns a list of reviews for the specified pull request using GraphQL

### Comments Operations
- `comments__list()` - Returns a list of comments for the specified issue using GraphQL
- `comments__get()` - Gets information about a specific issue comment by its GraphQL node ID.

Note: This endpoint requires a GraphQL node ID (e.g., 'IC_kwDOBZtLds6YWTMj'),
not a numeric database ID. You can obtain node IDs from the Comments_List response,
where each comment includes both 'id' (node ID) and 'databaseId' (numeric ID).


### Pr_Comments Operations
- `pr_comments__list()` - Returns a list of comments for the specified pull request using GraphQL
- `pr_comments__get()` - Gets information about a specific pull request comment by its GraphQL node ID.

Note: This endpoint requires a GraphQL node ID (e.g., 'IC_kwDOBZtLds6YWTMj'),
not a numeric database ID. You can obtain node IDs from the PRComments_List response,
where each comment includes both 'id' (node ID) and 'databaseId' (numeric ID).


### Labels Operations
- `labels__list()` - Returns a list of labels for the specified repository using GraphQL
- `labels__get()` - Gets information about a specific label by name using GraphQL

### Milestones Operations
- `milestones__list()` - Returns a list of milestones for the specified repository using GraphQL
- `milestones__get()` - Gets information about a specific milestone by number using GraphQL

### Organizations Operations
- `organizations__get()` - Gets information about a specific organization using GraphQL
- `organizations__list()` - Returns a list of organizations the user belongs to using GraphQL

### Users Operations
- `users__get()` - Gets information about a specific user using GraphQL
- `users__list()` - Returns a list of members for the specified organization using GraphQL
- `users__search()` - Search for GitHub users using search syntax

### Teams Operations
- `teams__list()` - Returns a list of teams for the specified organization using GraphQL
- `teams__get()` - Gets information about a specific team using GraphQL

### Tags Operations
- `tags__list()` - Returns a list of tags for the specified repository using GraphQL
- `tags__get()` - Gets information about a specific tag by name using GraphQL

### Stargazers Operations
- `stargazers__list()` - Returns a list of users who have starred the repository using GraphQL

### Viewer Operations
- `viewer__get()` - Gets information about the currently authenticated user.
This is useful when you don't know the username but need to access
the current user's profile, permissions, or associated resources.


### Viewer_Repositories Operations
- `viewer_repositories__list()` - Returns a list of repositories owned by the authenticated user.
Unlike Repositories_List which requires a username, this endpoint
automatically lists repositories for the current authenticated user.


## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_github.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
