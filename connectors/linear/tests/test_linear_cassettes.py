"""
Auto-generated cassette tests for Linear connector.

These tests are generated from cassette YAML files and test the connector
against recorded API responses.
"""

import pytest
from unittest.mock import AsyncMock, patch

from airbyte_ai_linear import LinearConnector



@pytest.mark.asyncio
async def test_issues_get_id_7673b1ad_d549_4086_94cb_a7b102e911fa():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'issue': {'id': '7673b1ad-d549-4086-94cb-a7b102e911fa', 'title': 'Connect your tools (3)', 'description': 'Integrations turn Linear into your source of truth around product development. Keep data in sync, and eliminate manual updates between tools.\n\n![connect-your-tools.png](https://uploads.linear.app/fe63b3e2-bf87-46c0-8784-cd7d639287c8/c2eae035-37e2-4754-adcb-b8305431aa1f/c92d70c7-e6d0-4fa2-a0fd-78f6e780993a)\n\n### **Key integrations**\n\n* [**Slack**](https://linear.app/settings/integrations/slack)\n  Create issues from Slack messages and sync threads\n* [**GitHub**](https://linear.app/settings/integrations/github)** / **[**GitLab**](https://linear.app/settings/integrations/gitlab)\n  Automate your pull request, commit workflows, and keep issues synced both ways\n* [**Agents**](https://linear.app/integrations/agents)\n  Deploy AI agents that work alongside you as teammates\n\n### **Browse all integrations**\n\nDiscover 150+ available connections in our [integration directory](https://linear.app/integrations) – from bug creation via support tools (Intercom, Zendesk), to issues created from design explorations (Figma).\n\n### **Linear API**\n\nIf you need something more custom, you can build directly on the Linear API (built on GraphQL). [See our Dev Docs to learn more](https://linear.app/developers).', 'state': {'name': 'Todo'}, 'priority': 0, 'assignee': None, 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T01:14:56.237Z'}}}

    connector = LinearConnector(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_linear._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.issues.get(id="7673b1ad-d549-4086-94cb-a7b102e911fa")

    assert result == mock_response


@pytest.mark.asyncio
async def test_issues_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'issues': {'nodes': [{'id': '7673b1ad-d549-4086-94cb-a7b102e911fa', 'title': 'Connect your tools (3)', 'description': 'Integrations turn Linear into your source of truth around product development. Keep data in sync, and eliminate manual updates between tools.\n\n![connect-your-tools.png](https://uploads.linear.app/fe63b3e2-bf87-46c0-8784-cd7d639287c8/c2eae035-37e2-4754-adcb-b8305431aa1f/c92d70c7-e6d0-4fa2-a0fd-78f6e780993a)\n\n### **Key integrations**\n\n* [**Slack**](https://linear.app/settings/integrations/slack)\n  Create issues from Slack messages and sync threads\n* [**GitHub**](https://linear.app/settings/integrations/github)** / **[**GitLab**](https://linear.app/settings/integrations/gitlab)\n  Automate your pull request, commit workflows, and keep issues synced both ways\n* [**Agents**](https://linear.app/integrations/agents)\n  Deploy AI agents that work alongside you as teammates\n\n### **Browse all integrations**\n\nDiscover 150+ available connections in our [integration directory](https://linear.app/integrations) – from bug creation via support tools (Intercom, Zendesk), to issues created from design explorations (Figma).\n\n### **Linear API**\n\nIf you need something more custom, you can build directly on the Linear API (built on GraphQL). [See our Dev Docs to learn more](https://linear.app/developers).', 'state': {'name': 'Todo'}, 'priority': 0, 'assignee': None, 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T01:14:56.237Z'}, {'id': '744eb0b0-218a-437c-94ec-b7a296904389', 'title': 'Import your data (4)', 'description': "Sync data between Linear and your other tools.\n\n![import-your-data.png](https://uploads.linear.app/fe63b3e2-bf87-46c0-8784-cd7d639287c8/80d7e050-dd1f-4d4f-8257-b29c16087017/65c16454-30f3-4f4a-8f25-c2428d64ff57)\n\nWhether you're exploring Linear, running a pilot, or ready for full migration, we’ve got you covered.\xa0\n\n### **Exploring Linear:**\n\n* [**Pitch Linear**](https://linear.app/switch/pitch-guide)\n  Build your business case and get organizational buy-in\n* [**Run a pilot**](https://linear.app/switch/pilot-guide)\n  Test Linear with a small team before rolling out company-wide\n\n### **Ready to migrate:**\n\n* [**Migration guide**](https://linear.app/switch/migration-guide) \n  Step-by-step process for importing data and rolling out Linear\n\n---\n\nIf you have any questions hit `?` in the bottom left > Contact us.\n\n![contactlinear (1).gif](https://uploads.linear.app/fe63b3e2-bf87-46c0-8784-cd7d639287c8/191f6985-8562-4f62-9482-a094b69c4756/0e4ff63b-3da2-4699-912b-04afb68511e8)", 'state': {'name': 'Todo'}, 'priority': 0, 'assignee': None, 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T01:15:45.578Z'}, {'id': '4c2d3408-451a-42d7-b26a-31f86af765bf', 'title': 'Set up your teams (2)', 'description': 'This workspace is a container for your organization’s work.\xa0\n\n* [Learn more about Workspaces](https://linear.app/docs/workspaces)\n  How to configure settings and workflows\xa0\n\nTeams are how you organize people and work in Linear.\n\n* [Learn about Teams](https://linear.app/docs/teams)\n  How to structure teams and configure workflows\n\nTeams are made of members with defined roles (Admin, Member, Guest).\n\n* [Learn more about Members](https://linear.app/docs/invite-members)\n  Add your team and assign roles\n\n---\n\nReady to add your team? Invite via CSV or a unique link in [settings](http://linear.app/settings/members).', 'state': {'name': 'Todo'}, 'priority': 0, 'assignee': None, 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T01:14:56.237Z'}, {'id': '18842a17-5b13-4fbb-83d7-78b3f57ca88e', 'title': 'Get familiar with Linear (1)', 'description': 'Welcome to Linear!\xa0\n\nWatch an introductory video and access a list of resources below.\n\n[LinearH264Version.mp4](https://uploads.linear.app/fe63b3e2-bf87-46c0-8784-cd7d639287c8/923e2801-e5f2-4055-9b27-1541f27e3365/44ab081a-253a-4ccf-8d3d-2547ac09b986)\n\n### **Choose your setup guide** based on your company stage:\n\n* [Small teams](https://linear.app/docs/how-to-use-linear-small-teams)\n  For early-stage startups and projects\n* [Startups & mid-size companies](https://linear.app/docs/how-to-use-linear-startups-mid-size-companies)\n  For growing teams with cross-functional needs\n* [Large & scaling companies](https://linear.app/docs/how-to-use-linear-large-scaling-companies)\n  For enterprise and high-growth teams with complex workflows\n\n### **Need help getting started?**\n\n* [Join our Slack community](https://linear.app/join-slack)\n  Connect with other Linear users and get tips\n* [Join a live ](https://lu.ma/welcome-to-linear?utm_source=docs)[onboarding](https://lu.ma/welcome-to-linear?utm_source=onboarding)[ ](https://lu.ma/welcome-to-linear?utm_source=docs)[session](https://lu.ma/welcome-to-linear?utm_source=onboarding)\n  Learn the essentials and see demos of core workflows\n\n---\n\nIf you have any questions hit `?` in the bottom left > Contact us.\n\n![contactlinear (1).gif](https://uploads.linear.app/fe63b3e2-bf87-46c0-8784-cd7d639287c8/bc9bbf62-4192-411f-88f6-c89c9150503e/4df0346e-803b-4f58-8527-4aeb30d88411)', 'state': {'name': 'Todo'}, 'priority': 0, 'assignee': None, 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T01:14:56.237Z'}], 'pageInfo': {'hasNextPage': False, 'endCursor': '18842a17-5b13-4fbb-83d7-78b3f57ca88e'}}}}

    connector = LinearConnector(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_linear._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.issues.list(first=10, after=None)

    assert result == mock_response


@pytest.mark.asyncio
async def test_projects_get_id_6b01548e_c9a3_420f_9992_ece7edeb6b28():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'project': {'id': '6b01548e-c9a3-420f-9992-ece7edeb6b28', 'name': 'My Example Project', 'description': '', 'state': 'backlog', 'startDate': None, 'targetDate': None, 'lead': None, 'createdAt': '2025-11-20T01:15:26.994Z', 'updatedAt': '2025-11-20T01:15:35.551Z'}}}

    connector = LinearConnector(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_linear._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.projects.get(id="6b01548e-c9a3-420f-9992-ece7edeb6b28")

    assert result == mock_response


@pytest.mark.asyncio
async def test_projects_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'projects': {'nodes': [{'id': '6b01548e-c9a3-420f-9992-ece7edeb6b28', 'name': 'My Example Project', 'description': '', 'state': 'backlog', 'startDate': None, 'targetDate': None, 'lead': None, 'createdAt': '2025-11-20T01:15:26.994Z', 'updatedAt': '2025-11-20T01:15:35.551Z'}], 'pageInfo': {'hasNextPage': False, 'endCursor': '6b01548e-c9a3-420f-9992-ece7edeb6b28'}}}}

    connector = LinearConnector(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_linear._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.projects.list(first=10, after=None)

    assert result == mock_response


@pytest.mark.asyncio
async def test_teams_get_id_1c5bad49_8001_4c2e_82d4_9783030d2d24():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'team': {'id': '1c5bad49-8001-4c2e-82d4-9783030d2d24', 'name': 'Airbyte Integration Testing', 'key': 'AIR', 'description': None, 'timezone': 'America/Los_Angeles', 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T18:01:17.150Z'}}}

    connector = LinearConnector(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_linear._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.teams.get(id="1c5bad49-8001-4c2e-82d4-9783030d2d24")

    assert result == mock_response


@pytest.mark.asyncio
async def test_teams_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'teams': {'nodes': [{'id': '1c5bad49-8001-4c2e-82d4-9783030d2d24', 'name': 'Airbyte Integration Testing', 'key': 'AIR', 'description': None, 'timezone': 'America/Los_Angeles', 'createdAt': '2025-11-20T01:14:56.237Z', 'updatedAt': '2025-11-20T18:01:17.150Z'}], 'pageInfo': {'hasNextPage': False, 'endCursor': '1c5bad49-8001-4c2e-82d4-9783030d2d24'}}}}

    connector = LinearConnector(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_linear._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.teams.list(first=10, after=None)

    assert result == mock_response

