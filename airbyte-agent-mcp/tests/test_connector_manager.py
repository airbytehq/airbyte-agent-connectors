"""Test connector manager."""

import base64
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from airbyte_agent_mcp._vendored.connector_sdk.executor.models import ExecutionConfig, ExecutionResult

from airbyte_agent_mcp.connector_manager import ConnectorManager
from airbyte_agent_mcp.models import Config, ConnectorConfig, ConnectorType
from airbyte_agent_mcp.secret_manager import SecretsManager


@pytest.fixture
def mock_secrets_manager():
    """Create a mock secrets manager."""
    backend = MagicMock()
    backend.get_secret.return_value = "test_secret_value"
    return SecretsManager(backend)


@pytest.fixture
def simple_config():
    """Create a simple test configuration."""
    return Config(
        connectors=[
            ConnectorConfig(
                id="test_yaml",
                type=ConnectorType.LOCAL,
                path="/tmp/test_connector.yaml",
                secrets={"token": "TEST_KEY"},
            )
        ]
    )


@pytest.mark.asyncio
async def test_execute_connector_not_found(mock_secrets_manager, simple_config):
    """Test error when connector not found."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    with pytest.raises(ValueError, match="Connector not found: nonexistent"):
        await manager.execute(connector_id="nonexistent", entity="customers", action="list")


@pytest.mark.asyncio
async def test_execute_success(mock_secrets_manager, simple_config):
    """Test successful execution of a connector operation."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    mock_connector = AsyncMock()
    mock_data = {"data": [{"id": "cust_123", "email": "test@example.com"}]}
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=True, data=mock_data))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        result = await manager.execute(connector_id="test_yaml", entity="customers", action="list", params={"limit": 10})

        assert result == mock_data
        mock_connector.execute.assert_called_once_with(ExecutionConfig(entity="customers", action="list", params={"limit": 10}))


@pytest.mark.asyncio
async def test_execute_with_secrets(simple_config):
    """Test that secrets are resolved and passed to connector."""
    backend = MagicMock()
    backend.get_secret.return_value = "secret_api_key_value"
    secrets_manager = SecretsManager(backend)

    manager = ConnectorManager(simple_config, secrets_manager)

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=True, data={"success": True}))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor") as MockConnectorExecutor:
        MockConnectorExecutor.return_value = mock_connector

        await manager.execute(connector_id="test_yaml", entity="customers", action="list")

        MockConnectorExecutor.assert_called_once_with(
            config_path="/tmp/test_connector.yaml",
            auth_config={"token": "secret_api_key_value"},
            auth_scheme=None,
            config_values={},
            execution_context="mcp",
        )

        mock_connector.execute.assert_called_once_with(ExecutionConfig(entity="customers", action="list", params={}))


@pytest.mark.asyncio
async def test_execute_without_params(mock_secrets_manager, simple_config):
    """Test execution with no params defaults to empty dict."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=True, data={"data": []}))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        await manager.execute(connector_id="test_yaml", entity="customers", action="list")

        # Verify execute was called with empty dict
        mock_connector.execute.assert_called_once_with(ExecutionConfig(entity="customers", action="list", params={}))


@pytest.mark.asyncio
async def test_describe_connector_with_query_params():
    """Test describe_connector returns query params with full metadata."""
    connector_yaml = """
openapi: 3.1.0
info:
  title: Test Connector
  version: 1.0.0
  x-airbyte-connector-name: test
  x-airbyte-connector-id: 00000000-0000-0000-0000-000000000099
  x-airbyte-external-documentation-urls:
    - type: other
      title: Airbyte Documentation
      url: https://docs.airbyte.com/
servers:
  - url: https://api.test.com
paths:
  /v1/widgets:
    get:
      summary: List all widgets
      description: Returns a list of widgets
      operationId: widgets_List
      x-airbyte-entity: widgets
      x-airbyte-action: list
      tags:
        - Widgets
      parameters:
        - name: limit
          in: query
          description: A limit on the number of objects to be returned
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
      responses:
        "200":
          description: Success
          content:
            application/json:
              schema:
                type: object
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(connector_yaml)
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        manager = ConnectorManager(config, secrets_manager)

        entities = await manager.describe_connector("test")

        assert len(entities) == 1
        assert entities[0]["entity_name"] == "widgets"
        assert entities[0]["available_actions"] == ["list"]
        assert entities[0]["description"] == "Returns a list of widgets"
        assert "parameters" in entities[0]
        assert "list" in entities[0]["parameters"]

        # Check full parameter metadata
        params = entities[0]["parameters"]["list"]
        assert len(params) == 1
        assert params[0]["name"] == "limit"
        assert params[0]["in"] == "query"
        assert params[0]["required"] is False
        assert params[0]["type"] == "integer"
        assert params[0]["description"] == "A limit on the number of objects to be returned"

    finally:
        Path(yaml_path).unlink()


@pytest.mark.asyncio
async def test_describe_connector_with_path_params():
    """Test describe_connector returns path params as always required."""
    connector_yaml = """
openapi: 3.1.0
info:
  title: Test Connector
  version: 1.0.0
  x-airbyte-connector-name: test
  x-airbyte-connector-id: 00000000-0000-0000-0000-000000000099
  x-airbyte-external-documentation-urls:
    - type: other
      title: Airbyte Documentation
      url: https://docs.airbyte.com/
servers:
  - url: https://api.test.com
paths:
  /v1/widgets/{widget_id}:
    get:
      summary: Get a widget
      description: Returns a single widget by ID
      operationId: widgets_Get
      x-airbyte-entity: widgets
      x-airbyte-action: get
      parameters:
        - name: widget_id
          in: path
          required: true
          description: The widget identifier
          schema:
            type: string
      responses:
        "200":
          description: Success
          content:
            application/json:
              schema:
                type: object
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(connector_yaml)
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        manager = ConnectorManager(config, secrets_manager)

        entities = await manager.describe_connector("test")

        assert len(entities) == 1
        params = entities[0]["parameters"]["get"]
        assert len(params) == 1
        assert params[0]["name"] == "widget_id"
        assert params[0]["in"] == "path"
        assert params[0]["required"] is True  # Path params are always required
        assert params[0]["type"] == "string"
        assert params[0]["description"] == "The widget identifier"

    finally:
        Path(yaml_path).unlink()


@pytest.mark.asyncio
async def test_describe_connector_with_body_fields():
    """Test describe_connector returns body fields with required status from schema."""
    connector_yaml = """
openapi: 3.1.0
info:
  title: Test Connector
  version: 1.0.0
  x-airbyte-connector-name: test
  x-airbyte-connector-id: 00000000-0000-0000-0000-000000000099
  x-airbyte-external-documentation-urls:
    - type: other
      title: Airbyte Documentation
      url: https://docs.airbyte.com/
servers:
  - url: https://api.test.com
paths:
  /v1/widgets:
    post:
      summary: Create a widget
      description: Creates a new widget
      operationId: widgets_Create
      x-airbyte-entity: widgets
      x-airbyte-action: create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: The widget name
                color:
                  type: string
                  description: Optional widget color
      responses:
        "201":
          description: Created
          content:
            application/json:
              schema:
                type: object
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(connector_yaml)
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        manager = ConnectorManager(config, secrets_manager)

        entities = await manager.describe_connector("test")

        assert len(entities) == 1
        params = entities[0]["parameters"]["create"]
        assert len(params) == 2

        # Find params by name
        name_param = next(p for p in params if p["name"] == "name")
        color_param = next(p for p in params if p["name"] == "color")

        # name is required per schema
        assert name_param["in"] == "body"
        assert name_param["required"] is True
        assert name_param["type"] == "string"
        assert name_param["description"] == "The widget name"

        # color is optional
        assert color_param["in"] == "body"
        assert color_param["required"] is False
        assert color_param["type"] == "string"
        assert color_param["description"] == "Optional widget color"

    finally:
        Path(yaml_path).unlink()


@pytest.mark.asyncio
async def test_describe_connector_with_multiple_actions():
    """Test describe_connector handles multiple actions on same entity."""
    connector_yaml = """
openapi: 3.1.0
info:
  title: Test Connector
  version: 1.0.0
  x-airbyte-connector-name: test
  x-airbyte-connector-id: 00000000-0000-0000-0000-000000000099
  x-airbyte-external-documentation-urls:
    - type: other
      title: Airbyte Documentation
      url: https://docs.airbyte.com/
servers:
  - url: https://api.test.com
paths:
  /v1/widgets:
    get:
      summary: List widgets
      description: Returns all widgets
      operationId: widgets_List
      x-airbyte-entity: widgets
      x-airbyte-action: list
      parameters:
        - name: limit
          in: query
          required: true
          description: Max items to return
          schema:
            type: integer
      responses:
        "200":
          description: Success
  /v1/widgets/{id}:
    get:
      summary: Get widget
      description: Returns one widget
      operationId: widgets_Get
      x-airbyte-entity: widgets
      x-airbyte-action: get
      parameters:
        - name: id
          in: path
          required: true
          description: Widget ID
          schema:
            type: string
      responses:
        "200":
          description: Success
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(connector_yaml)
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        manager = ConnectorManager(config, secrets_manager)

        entities = await manager.describe_connector("test")

        assert len(entities) == 1
        assert set(entities[0]["available_actions"]) == {"list", "get"}

        # Check list action has query param
        list_params = entities[0]["parameters"]["list"]
        assert len(list_params) == 1
        assert list_params[0]["name"] == "limit"
        assert list_params[0]["in"] == "query"
        assert list_params[0]["required"] is True  # Explicitly marked required in spec

        # Check get action has path param
        get_params = entities[0]["parameters"]["get"]
        assert len(get_params) == 1
        assert get_params[0]["name"] == "id"
        assert get_params[0]["in"] == "path"
        assert get_params[0]["required"] is True

    finally:
        Path(yaml_path).unlink()


@pytest.mark.asyncio
async def test_describe_connector_no_parameters():
    """Test describe_connector handles entity with no parameters."""
    connector_yaml = """
openapi: 3.1.0
info:
  title: Test Connector
  version: 1.0.0
  x-airbyte-connector-name: test
  x-airbyte-connector-id: 00000000-0000-0000-0000-000000000099
  x-airbyte-external-documentation-urls:
    - type: other
      title: Airbyte Documentation
      url: https://docs.airbyte.com/
servers:
  - url: https://api.test.com
paths:
  /v1/status:
    get:
      summary: Get status
      description: Returns system status
      operationId: status_Get
      x-airbyte-entity: status
      x-airbyte-action: get
      responses:
        "200":
          description: Success
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(connector_yaml)
        yaml_path = f.name

    try:
        config = Config(connectors=[ConnectorConfig(id="test", type=ConnectorType.LOCAL, path=yaml_path)])

        backend = MagicMock()
        secrets_manager = SecretsManager(backend)
        manager = ConnectorManager(config, secrets_manager)

        entities = await manager.describe_connector("test")

        assert len(entities) == 1
        assert entities[0]["entity_name"] == "status"
        # No parameters for this action
        assert entities[0]["parameters"] == {}

    finally:
        Path(yaml_path).unlink()


async def _async_generator(chunks: list[bytes]):
    """Helper to create an async generator from a list of chunks."""
    for chunk in chunks:
        yield chunk


@pytest.mark.asyncio
async def test_execute_download_returns_base64(mock_secrets_manager, simple_config):
    """Test that download operations return base64-encoded data."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    # Create mock connector that returns an ExecutionResult with async generator in data
    mock_connector = AsyncMock()
    binary_content = b"Hello, this is binary file content!"
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=True, data=_async_generator([binary_content]), error=None))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        result = await manager.execute(connector_id="test_yaml", entity="files", action="download", params={"id": "file_123"})

        # Verify the result is base64 encoded
        assert result["encoding"] == "base64"
        assert result["size"] == len(binary_content)
        assert base64.b64decode(result["data"]) == binary_content


@pytest.mark.asyncio
async def test_execute_download_multiple_chunks(mock_secrets_manager, simple_config):
    """Test that download handles multiple chunks correctly."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    chunks = [b"chunk1", b"chunk2", b"chunk3"]
    expected_content = b"chunk1chunk2chunk3"

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=True, data=_async_generator(chunks), error=None))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        result = await manager.execute(connector_id="test_yaml", entity="files", action="download", params={"id": "file_123"})

        assert result["size"] == len(expected_content)
        assert base64.b64decode(result["data"]) == expected_content


@pytest.mark.asyncio
async def test_execute_download_exceeds_size_limit(mock_secrets_manager, simple_config):
    """Test that downloads exceeding size limit raise an error."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    # Create a chunk that's larger than 50MB limit
    large_chunk = b"x" * (51 * 1024 * 1024)  # 51MB

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=True, data=_async_generator([large_chunk]), error=None))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        with pytest.raises(Exception, match="Download exceeds maximum size limit"):
            await manager.execute(connector_id="test_yaml", entity="files", action="download", params={"id": "file_123"})


@pytest.mark.asyncio
async def test_execute_failed_result_raises_exception(mock_secrets_manager, simple_config):
    """Test that failed ExecutionResult raises an exception."""
    manager = ConnectorManager(simple_config, mock_secrets_manager)

    mock_connector = AsyncMock()
    mock_connector.execute = AsyncMock(return_value=ExecutionResult(success=False, data=None, error="API rate limit exceeded"))

    with patch("airbyte_agent_mcp.connector_manager.ConnectorExecutor", return_value=mock_connector):
        with pytest.raises(Exception, match="API rate limit exceeded"):
            await manager.execute(connector_id="test_yaml", entity="customers", action="list")
