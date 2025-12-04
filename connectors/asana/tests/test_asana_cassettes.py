"""
Auto-generated cassette tests for Asana connector.

These tests are generated from cassette YAML files and test the connector
against recorded API responses.
"""

import pytest
from unittest.mock import AsyncMock, patch

from airbyte_ai_asana import AsanaConnector


@pytest.mark.asyncio
async def test_projects_get():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'gid': '1201485355022853', 'archived': False, 'color': 'hot-pink', 'completed': False, 'completed_at': None, 'created_at': '2021-12-10T06:05:00.412Z', 'current_status': None, 'current_status_update': None, 'custom_fields': [], 'custom_field_settings': [{'gid': '1203605485550450', 'custom_field': {'gid': '1203605485550446', 'enum_options': [{'gid': '1203605485550447', 'color': 'green', 'enabled': True, 'name': 'Low', 'resource_type': 'enum_option'}, {'gid': '1203605485550448', 'color': 'yellow', 'enabled': True, 'name': 'Medium', 'resource_type': 'enum_option'}, {'gid': '1203605485550449', 'color': 'red', 'enabled': True, 'name': 'High', 'resource_type': 'enum_option'}], 'name': 'Priority', 'resource_subtype': 'enum', 'resource_type': 'custom_field', 'type': 'enum', 'privacy_setting': 'public_with_guests', 'default_access_level': 'admin', 'is_formula_field': False}, 'is_important': True, 'parent': {'gid': '1201485355022853', 'name': 'Illustrations', 'resource_type': 'project'}, 'project': {'gid': '1201485355022853', 'name': 'Illustrations', 'resource_type': 'project'}, 'resource_type': 'custom_field_setting'}], 'default_access_level': 'editor', 'default_view': 'board', 'due_on': None, 'due_date': None, 'followers': [{'gid': '1200344886012993', 'name': 'John Lafleur', 'resource_type': 'user'}, {'gid': '912270837847830', 'name': 'Adrien Duermael', 'resource_type': 'user'}, {'gid': '1202256332970684', 'name': 'Laylee Asgari', 'resource_type': 'user'}, {'gid': '1205902752148546', 'name': 'Nora Kako', 'resource_type': 'user'}, {'gid': '1210024517224647', 'name': 'Charles Giardina', 'resource_type': 'user'}], 'members': [{'gid': '1200344886012993', 'name': 'John Lafleur', 'resource_type': 'user'}, {'gid': '912270837847830', 'name': 'Adrien Duermael', 'resource_type': 'user'}, {'gid': '1202256332970684', 'name': 'Laylee Asgari', 'resource_type': 'user'}, {'gid': '1205902752148546', 'name': 'Nora Kako', 'resource_type': 'user'}, {'gid': '1210024517224647', 'name': 'Charles Giardina', 'resource_type': 'user'}, {'gid': '1210585428323573', 'name': 'Anusha Thalnerkar', 'resource_type': 'user'}], 'minimum_access_level_for_customization': 'editor', 'minimum_access_level_for_sharing': 'editor', 'modified_at': '2025-11-11T00:00:44.562Z', 'name': 'Illustrations', 'notes': '', 'owner': {'gid': '1200344886012993', 'name': 'John Lafleur', 'resource_type': 'user'}, 'permalink_url': 'https://app.asana.com/1/1199152354181012/project/1201485355022853', 'privacy_setting': 'public_to_workspace', 'public': True, 'resource_type': 'project', 'start_on': None, 'team': {'gid': '1201485355022849', 'name': 'Design', 'resource_type': 'team'}, 'workspace': {'gid': '1199152354181012', 'name': 'Airbyte, Inc', 'resource_type': 'workspace'}}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.projects.get(project_gid="1201485355022853")

    assert result == mock_response

@pytest.mark.asyncio
async def test_projects_list_limit_5():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': [{'gid': '1201485355022853', 'name': 'Illustrations', 'resource_type': 'project'}, {'gid': '1201642069664056', 'name': 'Call for Speakers for Events', 'resource_type': 'project'}, {'gid': '1201840564953313', 'name': 'Developer Experience', 'resource_type': 'project'}, {'gid': '1201856001387054', 'name': 'Speaking Engagements ', 'resource_type': 'project'}, {'gid': '1202192547291132', 'name': 'Design - Marketing', 'resource_type': 'project'}], 'next_page': {'offset': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IlswLDEyMDUwODMzODQyMzAyMjNdIiwiaWF0IjoxNzYzNjgwMTg2LCJleHAiOjE3NjM2ODEwODZ9.pHu8OtznOxZXQ6w1oSTiej6tJUIxlKzETNrE-NtNXI4', 'path': '/projects?workspace=1199152354181012&limit=5&offset=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IlswLDEyMDUwODMzODQyMzAyMjNdIiwiaWF0IjoxNzYzNjgwMTg2LCJleHAiOjE3NjM2ODEwODZ9.pHu8OtznOxZXQ6w1oSTiej6tJUIxlKzETNrE-NtNXI4', 'uri': 'https://app.asana.com/api/1.0/projects?workspace=1199152354181012&limit=5&offset=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IlswLDEyMDUwODMzODQyMzAyMjNdIiwiaWF0IjoxNzYzNjgwMTg2LCJleHAiOjE3NjM2ODEwODZ9.pHu8OtznOxZXQ6w1oSTiej6tJUIxlKzETNrE-NtNXI4'}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.projects.list(workspace="1199152354181012", limit=5)

    assert result == mock_response

@pytest.mark.asyncio
async def test_tasks_get():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'gid': '1210025338168162', 'actual_time_minutes': None, 'assignee': {'gid': '912270837847830', 'name': 'Adrien Duermael', 'resource_type': 'user'}, 'assignee_status': 'inbox', 'completed': False, 'completed_at': None, 'created_at': '2025-04-18T17:23:53.402Z', 'custom_fields': [{'gid': '1203605485550446', 'enabled': True, 'enum_options': [{'gid': '1203605485550447', 'color': 'green', 'enabled': True, 'name': 'Low', 'resource_type': 'enum_option'}, {'gid': '1203605485550448', 'color': 'yellow', 'enabled': True, 'name': 'Medium', 'resource_type': 'enum_option'}, {'gid': '1203605485550449', 'color': 'red', 'enabled': True, 'name': 'High', 'resource_type': 'enum_option'}], 'enum_value': None, 'name': 'Priority', 'description': '', 'created_by': {'gid': '1200344886012993', 'name': 'John Lafleur', 'resource_type': 'user'}, 'display_value': None, 'resource_subtype': 'enum', 'resource_type': 'custom_field', 'is_formula_field': False, 'is_value_read_only': False, 'type': 'enum'}], 'due_at': None, 'due_on': '2025-05-02', 'followers': [{'gid': '1210024517224647', 'name': 'Charles Giardina', 'resource_type': 'user'}, {'gid': '912270837847830', 'name': 'Adrien Duermael', 'resource_type': 'user'}], 'hearted': False, 'hearts': [], 'liked': False, 'likes': [], 'memberships': [{'project': {'gid': '1201485355022853', 'name': 'Illustrations', 'resource_type': 'project'}, 'section': {'gid': '1201496992494975', 'name': 'Backlog', 'resource_type': 'section'}}], 'modified_at': '2025-06-25T17:12:01.463Z', 'name': 'Octavia emoji for new value', 'notes': "We added a new value for the engineering team and we would like to create an emoji in slack for it just like we have for the other values.  Here's a link to a doc about the value: https://docs.google.com/document/d/1MTf68-Exr0pNqmBOF3pU2HlOF1apHMHSSoN1oqbUbb0/edit?tab=t.0#heading=h.cluqjpcsb1hr It's about striving to grow and fulfill our full potential.\n\nMy default would be to do an octavia version of the default lifting weight emoji. 🏋️ I am not super opinionated on what it looks like.  If that's too hard or you have a better idea, please run with it.\n\nLet me know if you have any questions.", 'num_hearts': 0, 'num_likes': 0, 'parent': None, 'permalink_url': 'https://app.asana.com/1/1199152354181012/project/1201485355022853/task/1210025338168162', 'projects': [{'gid': '1201485355022853', 'name': 'Illustrations', 'resource_type': 'project'}], 'resource_type': 'task', 'start_at': None, 'start_on': None, 'tags': [], 'resource_subtype': 'default_task', 'workspace': {'gid': '1199152354181012', 'name': 'Airbyte, Inc', 'resource_type': 'workspace'}}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.tasks.get(task_gid="1210025338168162")

    assert result == mock_response

@pytest.mark.asyncio
async def test_tasks_list_limit_5():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': [{'gid': '1210025338168162', 'name': 'Octavia emoji for new value', 'resource_type': 'task', 'resource_subtype': 'default_task'}, {'gid': '1201537794816218', 'name': "List of mascots for Octavia's world", 'resource_type': 'task', 'resource_subtype': 'default_task'}, {'gid': '1201502702358429', 'name': 'Comic one-page comic with Airbyte with some data engineering stories', 'resource_type': 'task', 'resource_subtype': 'default_task'}, {'gid': '1201485355022870', 'name': 'Octavia in Paris (for the Paris meetup)', 'resource_type': 'task', 'resource_subtype': 'default_task'}, {'gid': '1201485355022874', 'name': 'Octavia at a conference (branding the conference as Airbyte)', 'resource_type': 'task', 'resource_subtype': 'default_task'}], 'next_page': {'offset': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IltcIlZcIiwxMjAxNDk2OTkyNDk0OTc1LFwiSTAwNDRRUTRFTjNKXCIsMTIwMjA2MDA1MzIzMDI1NF0iLCJpYXQiOjE3NjM2ODAyNTMsImV4cCI6MTc2MzY4MTE1M30.xfu0s99Hb0cSawgUelR20ruFLCLOsnYREocSj2MMRqo', 'path': '/projects/1201485355022853/tasks?limit=5&offset=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IltcIlZcIiwxMjAxNDk2OTkyNDk0OTc1LFwiSTAwNDRRUTRFTjNKXCIsMTIwMjA2MDA1MzIzMDI1NF0iLCJpYXQiOjE3NjM2ODAyNTMsImV4cCI6MTc2MzY4MTE1M30.xfu0s99Hb0cSawgUelR20ruFLCLOsnYREocSj2MMRqo', 'uri': 'https://app.asana.com/api/1.0/projects/1201485355022853/tasks?limit=5&offset=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IltcIlZcIiwxMjAxNDk2OTkyNDk0OTc1LFwiSTAwNDRRUTRFTjNKXCIsMTIwMjA2MDA1MzIzMDI1NF0iLCJpYXQiOjE3NjM2ODAyNTMsImV4cCI6MTc2MzY4MTE1M30.xfu0s99Hb0cSawgUelR20ruFLCLOsnYREocSj2MMRqo'}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.tasks.list(project_gid="1201485355022853", limit=5)

    assert result == mock_response

@pytest.mark.asyncio
async def test_users_get():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'gid': '1200344886012993', 'email': 'john@airbyte.io', 'name': 'John Lafleur', 'photo': {'image_21x21': 'https://asanausercontent.com/us1/assets/1199152354181012/profile_photos/1204255119328610/1200344886012993.1200344886041359.tDfeerEoN2LpCHDiZlgo_21x21.png?e=1764285010&v=0&t=2uceKxsVwpQrcemCLmbdZfokUWOnh01kekq_qfUkpKM', 'image_27x27': 'https://asanausercontent.com/us1/assets/1199152354181012/profile_photos/1204255119328610/1200344886012993.1200344886041359.tDfeerEoN2LpCHDiZlgo_27x27.png?e=1764285010&v=0&t=jWGlsGOzzorp4n882XpVoHPGZ6zTpHv_94SgBgpw-Oo', 'image_36x36': 'https://asanausercontent.com/us1/assets/1199152354181012/profile_photos/1204255119328610/1200344886012993.1200344886041359.tDfeerEoN2LpCHDiZlgo_36x36.png?e=1764285010&v=0&t=GMwLcvqsbTHp3U0ZFm5szmIzlXfZH9PaERGBn5Qfat4', 'image_60x60': 'https://asanausercontent.com/us1/assets/1199152354181012/profile_photos/1204255119328610/1200344886012993.1200344886041359.tDfeerEoN2LpCHDiZlgo_60x60.png?e=1764285010&v=0&t=AcDaxIhXU6bEiAraCA9AKoCcele7tv3MInUW2GDtyCI', 'image_128x128': 'https://asanausercontent.com/us1/assets/1199152354181012/profile_photos/1204255119328610/1200344886012993.1200344886041359.tDfeerEoN2LpCHDiZlgo_128x128.png?e=1764285010&v=0&t=XWnqpy9PS_fef8_x-ehXi93hxubs0Ojs4v1RhmFIzC8'}, 'resource_type': 'user', 'workspaces': [{'gid': '1199152354181012', 'name': 'Airbyte, Inc', 'resource_type': 'workspace'}]}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.users.get(user_gid="1200344886012993")

    assert result == mock_response

@pytest.mark.asyncio
async def test_users_list_limit_5():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': [{'gid': '1200344886012993', 'name': 'John Lafleur', 'resource_type': 'user'}, {'gid': '1200272792717222', 'name': 'Integration Test User', 'resource_type': 'user'}, {'gid': '912270837847830', 'name': 'Adrien Duermael', 'resource_type': 'user'}, {'gid': '1201617089911900', 'name': 'Chris Rose', 'resource_type': 'user'}, {'gid': '1201882454438380', 'name': 'Glenn Rossman', 'resource_type': 'user'}], 'next_page': {'offset': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IlsxMjAyMDQxNjA5ODI1MDY5XSIsImlhdCI6MTc2MzY4MDE4NywiZXhwIjoxNzYzNjgxMDg3fQ.S29I4ecOwTg70ZQh_qjQx-BA8qKm7-Cnf833z2o03gI', 'path': '/users?workspace=1199152354181012&limit=5&offset=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IlsxMjAyMDQxNjA5ODI1MDY5XSIsImlhdCI6MTc2MzY4MDE4NywiZXhwIjoxNzYzNjgxMDg3fQ.S29I4ecOwTg70ZQh_qjQx-BA8qKm7-Cnf833z2o03gI', 'uri': 'https://app.asana.com/api/1.0/users?workspace=1199152354181012&limit=5&offset=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib3JkZXJfcmFuayI6IlsxMjAyMDQxNjA5ODI1MDY5XSIsImlhdCI6MTc2MzY4MDE4NywiZXhwIjoxNzYzNjgxMDg3fQ.S29I4ecOwTg70ZQh_qjQx-BA8qKm7-Cnf833z2o03gI'}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.users.list(workspace="1199152354181012", limit=5)

    assert result == mock_response

@pytest.mark.asyncio
async def test_workspaces_get():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': {'gid': '1199152354181012', 'resource_type': 'workspace', 'name': 'Airbyte, Inc', 'email_domains': ['airbyte.io'], 'is_organization': True}}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.workspaces.get(workspace_gid="1199152354181012")

    assert result == mock_response

@pytest.mark.asyncio
async def test_workspaces_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'data': [{'gid': '1199152354181012', 'resource_type': 'workspace', 'name': 'Airbyte, Inc'}]}

    connector = AsanaConnector(auth_config={"token": "test_key"})

    with patch(
        "airbyte_ai_asana._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.workspaces.list()

    assert result == mock_response
