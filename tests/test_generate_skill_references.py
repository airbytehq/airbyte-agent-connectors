"""Tests for scripts/generate_skill_references.py.

Run with:  python -m pytest tests/test_generate_skill_references.py -v
"""

from __future__ import annotations

from pathlib import Path

import pytest

# conftest.py handles sys.path setup for scripts/ importability.
REPO_ROOT = Path(__file__).resolve().parent.parent

from generate_skill_references import (
    FORMAT_VERSION,
    _brand_display_name,
    _extract_bullet_list,
    _extract_code_block,
    _extract_sections,
    _extract_subsections,
    _sanitize_filename,
    _strip_details_blocks,
    check_drift,
    discover_connectors,
    generate_all,
    generate_connector_index,
    generate_connector_reference,
    generate_skill_md,
    parse_auth,
    parse_pyproject,
    parse_readme,
    parse_reference,
    validate_readme_structure,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

# New format README matching actual connector README structure.
SAMPLE_README = """\
# Stripe

The Stripe agent connector is a Python package for AI agents.

## Example questions

- List customers created in the last 7 days
- Show me details for a recent customer

## Unsupported questions

- Create a new customer profile in Stripe
- Delete a customer record

## Installation

```bash
uv pip install airbyte-agent-stripe
```

## Usage

### Open source

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = StripeConnector(
    auth_config=StripeAuthConfig(
        api_key="<Your Stripe API Key>"
    )
)
```

### Hosted

```python
from airbyte_agent_stripe import StripeConnector, AirbyteAuthConfig

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>"
    )
)
```

## Full documentation

### Entities and actions

| Entity | Actions |
|--------|--------|
| Customers | [List](REFERENCE.md#list), [Get](REFERENCE.md#get) |
| Invoices | [List](REFERENCE.md#list-1) |

### Stripe API docs

For more information, visit the [Stripe API documentation](https://docs.stripe.com/api).

## Version information

**Package version:** 0.5.0
"""

SAMPLE_README_MISSING_SECTION = """\
# Airbyte Test AI Connector

Some description.

## Usage

```python
pass
```

## Full documentation

### Entities and actions

| Entity | Actions |
|--------|--------|
| Foo | [Do](REFERENCE.md#do) |
"""

SAMPLE_PYPROJECT = """\
[project]
name = "airbyte-agent-stripe"
version = "0.5.0"
description = "Airbyte Stripe Connector for AI platforms"
"""

SAMPLE_AUTH_MD = """\
# Authentication

## Auth Methods

#### OAuth

OAuth 2.0 flow with refresh tokens.

| Field | Required | Description |
|-------|----------|-------------|
| client_id | Yes | OAuth client ID |
| client_secret | Yes | OAuth client secret |

#### Token

Simple API token authentication.

| Field | Required | Description |
|-------|----------|-------------|
| token | Yes | API access token |
"""

SAMPLE_REFERENCE_MD = """\
# API Reference

## Customers

### list_customers

List all customers.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | int | No | Max results |
| offset | int | No | Pagination offset |

```python
result = connector.list_customers(limit=10)
```

<details>
<summary>Response Schema</summary>

```json
{"type": "object", "properties": {"id": {"type": "string"}}}
```

</details>

### get_customer

Get a single customer.

```python
result = connector.get_customer(id="cus_123")
```
"""


def _create_connector_fixture(
    tmp_path: Path,
    name: str = "stripe",
    *,
    readme: str = SAMPLE_README,
    pyproject: str = SAMPLE_PYPROJECT,
    auth_md: str | None = None,
    reference_md: str | None = None,
) -> Path:
    """Create a fake connector directory with source files."""
    connector_dir = tmp_path / "connectors" / name
    connector_dir.mkdir(parents=True, exist_ok=True)
    (connector_dir / "README.md").write_text(readme)
    (connector_dir / "pyproject.toml").write_text(pyproject)
    if auth_md is not None:
        (connector_dir / "AUTH.md").write_text(auth_md)
    if reference_md is not None:
        (connector_dir / "REFERENCE.md").write_text(reference_md)
    return connector_dir


# ---------------------------------------------------------------------------
# Unit tests — parsers
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "content,expected_title",
    [
        pytest.param(SAMPLE_README, "Stripe", id="standard_title"),
        pytest.param("# My Connector\n\nDesc.", "My Connector", id="simple_title"),
    ],
)
def test_parse_readme_extracts_title(tmp_path: Path, content: str, expected_title: str):
    readme = tmp_path / "README.md"
    readme.write_text(content)
    result = parse_readme(readme)
    assert result["title"] == expected_title


def test_parse_readme_extracts_example_questions(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert len(result["example_questions"]) == 2
    assert "List customers" in result["example_questions"][0]


def test_parse_readme_extracts_unsupported_questions(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert len(result["unsupported_questions"]) == 2
    assert "Create" in result["unsupported_questions"][0]


def test_parse_readme_extracts_description(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert "Stripe agent connector" in result["description"]


def test_parse_readme_extracts_install_block(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert "uv pip install airbyte-agent-stripe" in result["install_block"]


def test_parse_readme_extracts_usage_block(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert "StripeConnector" in result["usage_block"]
    # OSS and Hosted subsections should be extracted
    assert "StripeAuthConfig" in (result["oss_usage"] or "")
    assert "AirbyteAuthConfig" in (result["hosted_usage"] or "")


def test_parse_readme_extracts_operations(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert len(result["ops_table"]) == 2
    entities = [e for e, _, _ in result["ops_table"]]
    assert "Customers" in entities
    assert "Invoices" in entities


def test_parse_readme_extracts_auth_class(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(SAMPLE_README)
    result = parse_readme(readme)
    assert result["auth_class"] == "StripeAuthConfig"
    assert "api_key" in result["auth_fields"]


@pytest.mark.parametrize(
    "pyproject_content,expected_name,expected_version",
    [
        pytest.param(
            SAMPLE_PYPROJECT,
            "airbyte-agent-stripe",
            "0.5.0",
            id="standard_pyproject",
        ),
        pytest.param(
            '[project]\nname = "airbyte-agent-gong"\nversion = "0.19.0"\n',
            "airbyte-agent-gong",
            "0.19.0",
            id="gong_pyproject",
        ),
    ],
)
def test_parse_pyproject(
    tmp_path: Path,
    pyproject_content: str,
    expected_name: str,
    expected_version: str,
):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(pyproject_content)
    result = parse_pyproject(pyproject)
    assert result["name"] == expected_name
    assert result["version"] == expected_version


def test_parse_auth_with_auth_md(tmp_path: Path):
    auth_path = tmp_path / "AUTH.md"
    auth_path.write_text(SAMPLE_AUTH_MD)
    result = parse_auth(auth_path)
    assert result["exists"] is True
    assert len(result["methods"]) >= 1


def test_parse_auth_filters_unavailable_methods(tmp_path: Path):
    """Methods marked 'isn't available' should be filtered out."""
    auth_content = """\
# Authentication

## Open source execution

#### OAuth

OAuth 2.0 flow.

| Field | Required |
|-------|----------|
| client_id | Yes |

#### Token

This authentication method isn't available for this connector.

## Hosted

#### OAuth

OAuth 2.0 flow (hosted).

#### Execution

This authentication method isn't available for this connector.
"""
    auth_path = tmp_path / "AUTH.md"
    auth_path.write_text(auth_content)
    result = parse_auth(auth_path)
    assert result["exists"] is True
    method_names = [m["name"] for m in result["methods"]]
    assert "OAuth" in method_names
    assert "Token" not in method_names  # filtered: isn't available
    assert "Execution" not in method_names  # filtered: hosting-specific
    # OAuth appears under both OSS and Hosted; should be deduplicated
    assert method_names.count("OAuth") == 1
    assert "Bring your own OAuth flow" not in method_names  # hosting-specific


def test_parse_auth_missing_file(tmp_path: Path):
    auth_path = tmp_path / "AUTH.md"
    result = parse_auth(auth_path)
    assert result["exists"] is False
    assert result["methods"] == []


def test_parse_reference_strips_response_schemas(tmp_path: Path):
    ref_path = tmp_path / "REFERENCE.md"
    ref_path.write_text(SAMPLE_REFERENCE_MD)
    result = parse_reference(ref_path)
    assert result["exists"] is True
    # <details> blocks should be stripped
    assert "<details>" not in result["raw_content"]


def test_parse_reference_preserves_parameter_tables(tmp_path: Path):
    ref_path = tmp_path / "REFERENCE.md"
    ref_path.write_text(SAMPLE_REFERENCE_MD)
    result = parse_reference(ref_path)
    assert result["exists"] is True
    # At least one entity with actions containing parameter tables
    found_table = False
    for entity in result["entities"]:
        for action in entity["actions"]:
            if action["parameter_tables"]:
                found_table = True
    assert found_table, "Parameter tables should be preserved"


def test_parse_reference_missing_file(tmp_path: Path):
    ref_path = tmp_path / "REFERENCE.md"
    result = parse_reference(ref_path)
    assert result["exists"] is False


# ---------------------------------------------------------------------------
# Unit tests — validation
# ---------------------------------------------------------------------------


def test_validate_readme_structure_passes_standard():
    warnings = validate_readme_structure(SAMPLE_README, "stripe")
    # Should pass without errors; may have warnings for missing optional sections
    assert isinstance(warnings, list)
    # All required sections present, so no ValueError raised
    for w in warnings:
        assert "missing expected section" not in w


def test_validate_readme_warns_on_missing_optional_section():
    """Missing optional section should produce a warning, not an error."""
    # Build a README with all required sections but without optional ones
    content = (
        "# Test\n\n"
        "Description.\n\n"
        "## Installation\n\n```bash\npip install test\n```\n\n"
        "## Usage\n\n```python\nimport test\n```\n\n"
        "## Full documentation\n\n"
        "### Entities and actions\n\n"
        "| Entity | Actions |\n|--------|--------|\n| A | B |\n\n"
        "## Version information\n\n**Package version:** 0.1.0\n"
    )
    warnings = validate_readme_structure(content, "test")
    # Should have warnings for missing Example questions / Unsupported questions
    assert any("Example questions" in w for w in warnings)


def test_format_validation_catches_changed_structure():
    """README missing Installation should raise ValueError."""
    content = "# Test\n\n## Usage\n\ncode\n"
    with pytest.raises(ValueError, match="missing expected section.*Installation"):
        validate_readme_structure(content, "test-connector")


def test_validate_readme_raises_on_missing_critical_section():
    """Missing Installation (critical) should raise ValueError."""
    content = SAMPLE_README_MISSING_SECTION
    with pytest.raises(ValueError, match="missing expected section.*Installation"):
        validate_readme_structure(content, "test")


# ---------------------------------------------------------------------------
# Unit tests — helpers
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text,expected_count",
    [
        pytest.param("- item1\n- item2\n- item3", 3, id="three_items"),
        pytest.param("* a\n* b", 2, id="asterisk_bullets"),
        pytest.param("no bullets here", 0, id="no_bullets"),
    ],
)
def test_extract_bullet_list(text: str, expected_count: int):
    result = _extract_bullet_list(text)
    assert len(result) == expected_count


@pytest.mark.parametrize(
    "text,expected",
    [
        pytest.param(
            "some\n```python\ncode\n```\nmore",
            "```python\ncode\n```",
            id="python_block",
        ),
        pytest.param("no code here", "", id="no_code_block"),
    ],
)
def test_extract_code_block(text: str, expected: str):
    result = _extract_code_block(text)
    assert result == expected


@pytest.mark.parametrize(
    "text,expected_empty",
    [
        pytest.param(
            "before <details>hidden</details> after",
            True,
            id="removes_details",
        ),
        pytest.param("no details here", False, id="no_details"),
    ],
)
def test_strip_details_blocks(text: str, expected_empty: bool):
    result = _strip_details_blocks(text)
    if expected_empty:
        assert "<details>" not in result
    else:
        assert result == text


@pytest.mark.parametrize(
    "name,expected",
    [
        pytest.param("stripe", "stripe", id="simple"),
        pytest.param("zendesk-support", "zendesk-support", id="hyphenated"),
        pytest.param("My Connector!", "my-connector", id="special_chars"),
    ],
)
def test_sanitize_filename(name: str, expected: str):
    result = _sanitize_filename(name)
    assert result == expected


# ---------------------------------------------------------------------------
# Unit tests — missing AUTH.md generates stub
# ---------------------------------------------------------------------------


def test_missing_auth_md_generates_stub(tmp_path: Path):
    """When AUTH.md is absent, the generated reference should still include
    auth info extracted from the README Usage section."""
    connector_dir = _create_connector_fixture(
        tmp_path, "stripe", auth_md=None
    )
    content, metadata = generate_connector_reference(
        connector_dir, generation_date="2025-01-01"
    )
    assert "## Authentication" in content
    assert "StripeAuthConfig" in content
    assert metadata["docs_status"] == "docs pending"


# ---------------------------------------------------------------------------
# Unit tests — connector reference generation
# ---------------------------------------------------------------------------


def test_generate_connector_reference_header(tmp_path: Path):
    connector_dir = _create_connector_fixture(tmp_path, "stripe")
    content, metadata = generate_connector_reference(
        connector_dir, generation_date="2025-01-01"
    )
    assert "<!-- AUTO-GENERATED from connectors/stripe/" in content
    assert f"Source format: {FORMAT_VERSION}" in content
    assert "`airbyte-agent-stripe` v0.5.0" in content


def test_generate_connector_reference_has_ops_table(tmp_path: Path):
    connector_dir = _create_connector_fixture(tmp_path, "stripe")
    content, _ = generate_connector_reference(
        connector_dir, generation_date="2025-01-01"
    )
    assert "## Entities and Actions" in content
    assert "| Customers |" in content


def test_generate_connector_reference_with_auth_and_reference(tmp_path: Path):
    connector_dir = _create_connector_fixture(
        tmp_path,
        "stripe",
        auth_md=SAMPLE_AUTH_MD,
        reference_md=SAMPLE_REFERENCE_MD,
    )
    content, metadata = generate_connector_reference(
        connector_dir, generation_date="2025-01-01"
    )
    assert "## Authentication" in content
    assert "## API Reference" in content
    assert metadata["docs_status"] == "complete"


# ---------------------------------------------------------------------------
# Unit tests — connector index
# ---------------------------------------------------------------------------


def test_generate_connector_index():
    metadata = [
        {
            "name": "stripe",
            "safe_name": "stripe",
            "display_name": "Airbyte Stripe AI Connector",
            "pkg_name": "airbyte-ai-stripe",
            "version": "0.5.0",
            "auth_summary": "Token",
            "key_entities": "Customers",
            "docs_status": "docs pending",
            "github_link": "https://example.com",
        },
    ]
    result = generate_connector_index(metadata, generation_date="2025-01-01")
    assert "# Connector Index" in result
    assert "1 connectors available" in result
    assert "| [Airbyte Stripe AI Connector]" in result
    assert "docs pending" in result


# ---------------------------------------------------------------------------
# Unit tests — SKILL.md generation
# ---------------------------------------------------------------------------


def test_generate_skill_md_line_count():
    metadata = [
        {
            "name": f"connector-{i}",
            "safe_name": f"connector-{i}",
            "display_name": f"Connector {i}",
            "pkg_name": f"airbyte-ai-connector-{i}",
            "version": "1.0.0",
            "auth_summary": "Token",
            "key_entities": "Entity",
            "docs_status": "complete",
            "github_link": "https://example.com",
        }
        for i in range(60)
    ]
    result = generate_skill_md(metadata)
    line_count = len(result.splitlines())
    assert line_count <= 500, f"SKILL.md is {line_count} lines, expected <= 500"


def test_generate_skill_md_has_operational_content():
    """SKILL.md must contain operational guidance, not just an index."""
    metadata = [
        {
            "name": "stripe",
            "safe_name": "stripe",
            "display_name": "Stripe",
            "pkg_name": "airbyte-agent-stripe",
            "version": "0.5.0",
            "auth_summary": "Token",
            "key_entities": "Customers",
            "docs_status": "complete",
            "github_link": "https://example.com",
        },
    ]
    result = generate_skill_md(metadata)
    # Must have YAML frontmatter with only name and description
    assert result.startswith("---")
    assert "name: airbyte-agent-connectors" in result
    assert "description:" in result
    # Frontmatter must NOT contain non-standard fields (Claude Code spec)
    # Extract frontmatter block (between first and second ---)
    fm_end = result.index("---", 3)
    frontmatter = result[:fm_end]
    assert "license:" not in frontmatter
    assert "compatibility:" not in frontmatter
    assert "metadata:" not in frontmatter
    assert "author:" not in frontmatter
    assert "version:" not in frontmatter
    assert "repo:" not in frontmatter
    assert "mcp-server:" not in frontmatter
    # Must have operational sections
    assert "## Mode Detection" in result
    assert "Platform Mode" in result
    assert "OSS Mode" in result
    assert "## Entity-Action API Pattern" in result
    assert "## Authentication Quick Reference" in result
    assert "## Security Best Practices" in result
    # Must have pagination example
    assert "fetch_all" in result
    # Must have Skill Metadata section in body (not frontmatter) with all 6 bullets
    assert "## Skill Metadata" in result
    assert "**Author:** Airbyte" in result
    assert "**Version:** 1.2.0" in result
    assert "**License:** Elastic-2.0" in result
    assert "**Compatibility:** Requires Python 3.11+" in result
    assert "**Repository:** https://github.com/airbytehq/airbyte-agent-connectors" in result
    assert "**MCP Server:** airbyte-agent-mcp" in result
    # Must have Reference Documentation table with all 8 links
    assert "## Reference Documentation" in result
    assert "references/getting-started.md" in result
    assert "references/platform-setup.md" in result
    assert "references/oss-setup.md" in result
    assert "references/entity-action-api.md" in result
    assert "references/authentication.md" in result
    assert "references/programmatic-setup.md" in result
    assert "references/mcp-integration.md" in result
    assert "references/troubleshooting.md" in result


def test_brand_display_name():
    """_brand_display_name should return brand-correct names."""
    assert _brand_display_name("google-analytics-data-api", "Google-Analytics-Data-Api") == "Google Analytics Data API"
    assert _brand_display_name("tiktok-marketing", "Tiktok-Marketing") == "TikTok Marketing"
    assert _brand_display_name("paypal-transaction", "Paypal-Transaction") == "PayPal Transaction"
    # Names not in map: fall back to README title if no hyphens
    assert _brand_display_name("stripe", "Stripe") == "Stripe"
    # Hyphenated fallback: title-case
    assert _brand_display_name("some-connector", "some-connector") == "Some Connector"


# ---------------------------------------------------------------------------
# End-to-end tests
# ---------------------------------------------------------------------------


def test_end_to_end_writes_to_output_dir(tmp_path: Path):
    """Run generate_all into a temp dir and verify file structure."""
    # Create two connectors
    _create_connector_fixture(tmp_path, "stripe")
    _create_connector_fixture(
        tmp_path,
        "gong",
        readme=(
            "# Gong\n\n"
            "The Gong agent connector.\n\n"
            "## Installation\n\n```bash\nuv pip install airbyte-agent-gong\n```\n\n"
            "## Usage\n\n```python\n"
            "from airbyte_agent_gong import GongConnector\n"
            "from airbyte_agent_gong.models import GongAuthConfig\n"
            "connector = GongConnector(auth_config=GongAuthConfig(access_key=\"...\"))\n"
            "```\n\n"
            "## Full documentation\n\n"
            "### Entities and actions\n\n"
            "| Entity | Actions |\n"
            "|--------|--------|\n"
            "| Users | [List](REFERENCE.md#list) |\n\n"
            "## Version information\n\n"
            "**Package version:** 0.19.0\n"
        ),
        pyproject='[project]\nname = "airbyte-agent-gong"\nversion = "0.19.0"\n',
    )

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    connectors_dir = tmp_path / "connectors"
    all_metadata, warnings = generate_all(
        connectors_dir,
        output_dir,
        generation_date="2025-01-01",
    )

    assert len(all_metadata) == 2

    # Check per-connector references exist
    refs_dir = output_dir / "references" / "connectors"
    assert (refs_dir / "stripe.md").exists()
    assert (refs_dir / "gong.md").exists()

    # Check index exists
    index_path = output_dir / "references" / "connector-index.md"
    assert index_path.exists()
    index_content = index_path.read_text()
    assert "2 connectors available" in index_content

    # Check SKILL.md exists and is <= 500 lines
    skill_path = output_dir / "SKILL.md"
    assert skill_path.exists()
    skill_lines = len(skill_path.read_text().splitlines())
    assert skill_lines <= 500


def test_end_to_end_check_no_drift(tmp_path: Path):
    """After generating, --check should report no drift."""
    _create_connector_fixture(tmp_path, "stripe")
    connectors_dir = tmp_path / "connectors"
    output_dir = tmp_path / "skills"
    output_dir.mkdir()

    generate_all(
        connectors_dir,
        output_dir,
        generation_date="2025-01-01",
    )

    has_drift, diffs = check_drift(
        connectors_dir,
        output_dir,
        generation_date="2025-01-01",
    )

    assert not has_drift, f"Unexpected drift:\n{''.join(diffs)}"


def test_end_to_end_check_detects_drift(tmp_path: Path):
    """Modifying a generated file should cause --check to detect drift."""
    _create_connector_fixture(tmp_path, "stripe")
    connectors_dir = tmp_path / "connectors"
    output_dir = tmp_path / "skills"
    output_dir.mkdir()

    generate_all(
        connectors_dir,
        output_dir,
        generation_date="2025-01-01",
    )

    # Modify a generated file
    ref_file = output_dir / "references" / "connectors" / "stripe.md"
    ref_file.write_text("# Modified content\n")

    has_drift, diffs = check_drift(
        connectors_dir,
        output_dir,
        generation_date="2025-01-01",
    )

    assert has_drift


def test_end_to_end_skips_connector_without_readme(tmp_path: Path):
    """Connectors without README.md should be skipped with a warning."""
    connector_dir = tmp_path / "connectors" / "noreadme"
    connector_dir.mkdir(parents=True)
    (connector_dir / "pyproject.toml").write_text(
        '[project]\nname = "airbyte-ai-noreadme"\nversion = "0.1.0"\n'
    )

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    connectors_dir = tmp_path / "connectors"
    all_metadata, warnings = generate_all(
        connectors_dir,
        output_dir,
        generation_date="2025-01-01",
    )

    assert len(all_metadata) == 0
    assert any("noreadme" in w and "README.md not found" in w for w in warnings)


def test_end_to_end_specific_connectors(tmp_path: Path):
    """Generating specific connectors still rebuilds the full index."""
    _create_connector_fixture(tmp_path, "stripe")
    _create_connector_fixture(
        tmp_path,
        "gong",
        readme=(
            "# Gong\n\nThe Gong agent connector.\n\n"
            "## Installation\n\n```bash\nuv pip install airbyte-agent-gong\n```\n\n"
            "## Usage\n\n```python\nfrom airbyte_agent_gong import GongConnector\n```\n\n"
            "## Full documentation\n\n"
            "### Entities and actions\n\n"
            "| Entity | Actions |\n"
            "|--------|--------|\n"
            "| Users | [List](REFERENCE.md#list) |\n\n"
            "## Version information\n\n"
            "**Package version:** 0.19.0\n"
        ),
        pyproject='[project]\nname = "airbyte-agent-gong"\nversion = "0.19.0"\n',
    )

    output_dir = tmp_path / "output"
    output_dir.mkdir()
    connectors_dir = tmp_path / "connectors"

    # Generate only stripe
    all_metadata, _ = generate_all(
        connectors_dir,
        output_dir,
        connector_names=["stripe"],
        generation_date="2025-01-01",
    )

    # Only stripe reference file should exist
    refs_dir = output_dir / "references" / "connectors"
    assert (refs_dir / "stripe.md").exists()
    assert not (refs_dir / "gong.md").exists()

    # But index should list both
    index_content = (output_dir / "references" / "connector-index.md").read_text()
    assert "2 connectors available" in index_content
    assert "gong" in index_content.lower()
