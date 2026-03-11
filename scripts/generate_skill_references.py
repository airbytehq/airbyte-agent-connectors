#!/usr/bin/env python3
"""Auto-generate per-connector reference docs and a connector index for skills/.

Usage:
    # Generate everything:
    python scripts/generate_skill_references.py --all

    # Generate specific connector(s) and rebuild index:
    python scripts/generate_skill_references.py --connector stripe gong

    # Dry run (writes to temp dir, prints summary):
    python scripts/generate_skill_references.py --all --dry-run

    # Output to custom directory (for tests):
    python scripts/generate_skill_references.py --all --output-dir /tmp/skill-preview

    # Validate (check no drift):
    python scripts/generate_skill_references.py --check
"""

from __future__ import annotations

import argparse
import difflib
import logging
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# tomllib is available in Python 3.11+; fall back to tomli for older versions
try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:
        tomllib = None  # type: ignore[assignment]

logger = logging.getLogger("generate_skill_references")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

FORMAT_VERSION = "v1"

# Sections we expect in the current auto-generated README format.
# The generator adapts to whichever sections are present but warns when
# the canonical set changes.
EXPECTED_README_SECTIONS = [
    "Installation",
    "Usage",
    "Full documentation",
    "Version information",
]

# Optional sections that produce warnings (not errors) when missing.
OPTIONAL_README_SECTIONS = [
    "Example questions",
    "Unsupported questions",
]

REPO_ROOT = Path(__file__).resolve().parent.parent
CONNECTORS_DIR = REPO_ROOT / "connectors"
DEFAULT_SKILLS_DIR = REPO_ROOT / "skills" / "airbyte-agent-connectors"
DEFAULT_REFS_DIR = DEFAULT_SKILLS_DIR / "references"

GITHUB_BASE = "https://github.com/airbytehq/airbyte-agent-connectors"

# Brand-correct display names for connectors whose README H1 uses
# directory-cased names (e.g. "Google-Analytics-Data-Api") instead of
# proper product names.
_BRAND_NAMES: dict[str, str] = {
    "amazon-ads": "Amazon Ads",
    "amazon-seller-partner": "Amazon Seller Partner",
    "facebook-marketing": "Facebook Marketing",
    "github": "GitHub",
    "gitlab": "GitLab",
    "google-ads": "Google Ads",
    "google-analytics-data-api": "Google Analytics Data API",
    "google-drive": "Google Drive",
    "google-search-console": "Google Search Console",
    "hubspot": "HubSpot",
    "incident-io": "incident.io",
    "linkedin-ads": "LinkedIn Ads",
    "paypal-transaction": "PayPal Transaction",
    "sendgrid": "SendGrid",
    "shopify": "Shopify",
    "snapchat-marketing": "Snapchat Marketing",
    "tiktok-marketing": "TikTok Marketing",
    "woocommerce": "WooCommerce",
    "zendesk-chat": "Zendesk Chat",
    "zendesk-support": "Zendesk Support",
    "zendesk-talk": "Zendesk Talk",
}


def _brand_display_name(dir_name: str, readme_title: str) -> str:
    """Return a brand-correct display name for a connector.

    Uses the explicit mapping first, then falls back to the README H1 title.
    If the README H1 is obviously directory-cased (contains hyphens), apply
    title-casing with common acronym handling.
    """
    if dir_name in _BRAND_NAMES:
        return _BRAND_NAMES[dir_name]
    # If the README title contains hyphens it was likely auto-generated from
    # the directory name.  Fall back to a cleaned-up version.
    if "-" in readme_title:
        return readme_title.replace("-", " ").title()
    return readme_title


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def _heading_level(line: str) -> int | None:
    """Return the heading level (1-6) if *line* is an ATX heading, else None."""
    m = re.match(r"^(#{1,6})\s", line)
    return len(m.group(1)) if m else None


def _extract_sections(content: str) -> dict[str, str]:
    """Split markdown *content* into {heading_text: body} for ## headings."""
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in content.splitlines(keepends=True):
        lvl = _heading_level(line)
        if lvl == 2:
            if current is not None:
                sections[current] = "".join(buf)
            current = line.lstrip("#").strip()
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "".join(buf)
    return sections


def _extract_subsections(body: str, level: int = 3) -> dict[str, str]:
    """Split *body* into subsections at the given heading *level*."""
    prefix = "#" * level
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in body.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith(prefix + " ") and not stripped.startswith(prefix + "#"):
            if current is not None:
                sections[current] = "".join(buf)
            current = stripped.lstrip("#").strip()
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "".join(buf)
    return sections


def _first_paragraph(text: str) -> str:
    """Return the first non-empty paragraph from *text*."""
    for para in re.split(r"\n{2,}", text.strip()):
        para = para.strip()
        if para and not para.startswith("#"):
            return para
    return ""


def _extract_code_block(text: str) -> str:
    """Return the first fenced code block found in *text*, including fences."""
    m = re.search(r"(```[^\n]*\n.*?```)", text, re.DOTALL)
    return m.group(1) if m else ""


def _extract_bullet_list(text: str) -> list[str]:
    """Return a list of bullet-point strings from *text*."""
    items: list[str] = []
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]\s+(.+)", line)
        if m:
            items.append(m.group(1).strip())
    return items


def _strip_details_blocks(text: str) -> str:
    """Remove <details>...</details> blocks from *text*."""
    return re.sub(r"<details>.*?</details>", "", text, flags=re.DOTALL).strip()


def _sanitize_filename(name: str) -> str:
    """Sanitize *name* for use as a filename component."""
    return re.sub(r"[^a-z0-9_-]", "-", name.lower()).strip("-")


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------


def validate_readme_structure(content: str, connector_name: str) -> list[str]:
    """Check that *content* contains all expected ## sections.

    Returns a list of warning messages for missing sections.
    Raises ``ValueError`` if *Installation* or *Usage* are missing
    (these are critical).
    """
    sections = _extract_sections(content)
    present = set(sections.keys())
    warnings: list[str] = []
    for section in EXPECTED_README_SECTIONS:
        if section not in present:
            msg = (
                f"{connector_name}/README.md missing expected section "
                f"'## {section}'. Source doc format may have changed."
            )
            # Installation and Usage are critical
            if section in ("Installation", "Usage"):
                raise ValueError(msg)
            warnings.append(msg)
    for section in OPTIONAL_README_SECTIONS:
        if section not in present:
            msg = (
                f"{connector_name}/README.md missing optional section "
                f"'## {section}'."
            )
            warnings.append(msg)
    return warnings


def _parse_entity_actions_table(text: str) -> list[tuple[str, str]]:
    """Parse a ``| Entity | Actions |`` markdown table.

    Returns a list of (entity_name, actions_string) tuples where
    *actions_string* is the raw markdown cell content (may contain links).
    """
    rows: list[tuple[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Entity"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # split on | gives ["", cell1, cell2, ..., ""]  for a row like | A | B |
        if len(cells) >= 3:
            entity = cells[1].strip()
            actions = cells[2].strip()
            if entity and entity != "Entity":
                rows.append((entity, actions))
    return rows


def parse_readme(path: Path) -> dict:
    """Parse a connector README.md and return structured data."""
    content = path.read_text(encoding="utf-8")
    sections = _extract_sections(content)

    # Title: first H1
    title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.parent.name.title()

    # Description: first non-empty paragraph after the title line and any
    # single-paragraph intro that follows immediately.
    lines_after_title = content.split("\n", 1)[1] if "\n" in content else ""
    description = _first_paragraph(lines_after_title)

    # Package version from "Version information" section
    version_section = sections.get("Version information", "")
    pkg_version_match = re.search(
        r"\*\*Package version:\*\*\s*(\S+)", version_section
    )
    if not pkg_version_match:
        # Legacy format fallback
        pkg_version_match = re.search(
            r"\*\*Package Version:\*\*\s*(\S+)", content
        )
    pkg_version = pkg_version_match.group(1) if pkg_version_match else None

    # Install command
    install_block = _extract_code_block(sections.get("Installation", ""))

    # Usage section — extract OSS and Hosted subsections
    usage_body = sections.get("Usage", "")
    usage_subsections = _extract_subsections(usage_body, level=3)
    oss_usage = _extract_code_block(usage_subsections.get("Open source", ""))
    hosted_usage = _extract_code_block(usage_subsections.get("Hosted", ""))
    # Fallback: if no subsections, grab first code block from Usage
    usage_block = oss_usage or _extract_code_block(usage_body)

    # Example questions
    example_questions = _extract_bullet_list(
        sections.get("Example questions", "")
    )

    # Unsupported questions
    unsupported_questions = _extract_bullet_list(
        sections.get("Unsupported questions", "")
    )

    # Operations — new format uses "## Full documentation" with
    # "### Entities and actions" containing a | Entity | Actions | table.
    full_docs = sections.get("Full documentation", "")
    full_docs_subsections = _extract_subsections(full_docs, level=3)
    entities_body = full_docs_subsections.get("Entities and actions", "")
    entity_actions_table = _parse_entity_actions_table(entities_body)

    # Legacy fallback: "## Available Operations" with ### subsections
    ops_table: list[tuple[str, str, str]] = []
    if entity_actions_table:
        for entity_name, actions_str in entity_actions_table:
            # Extract action names from markdown links like [List](...), [Get](...)
            action_names = re.findall(r"\[([^\]]+)\]", actions_str)
            if action_names:
                ops_table.append((entity_name, ", ".join(action_names), ""))
            else:
                ops_table.append((entity_name, actions_str, ""))
    else:
        # Legacy format: "## Available Operations" with ### subsections
        ops_body = sections.get("Available Operations", "")
        operations = _extract_subsections(ops_body, level=3)
        for entity_heading, entity_body in operations.items():
            entity_name = entity_heading.replace(" Operations", "")
            for item in _extract_bullet_list(entity_body):
                m = re.match(r"`([^`]+)`\s*[-\u2013\u2014]\s*(.*)", item)
                if m:
                    ops_table.append((entity_name, m.group(1), m.group(2)))

    # API docs link — from "### {Name} API docs" subsection
    api_docs_link = ""
    for sub_name, sub_body in full_docs_subsections.items():
        if sub_name.endswith("API docs"):
            link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", sub_body)
            if link_match:
                api_docs_link = link_match.group(2)
            break

    # Auth info — extract from Usage code block (OSS mode)
    auth_match = re.search(r"(\w+AuthConfig)\(([^)]*)\)", usage_block)
    auth_class = auth_match.group(1) if auth_match else None
    auth_params_raw = auth_match.group(2) if auth_match else ""
    auth_fields = re.findall(r'(\w+)=', auth_params_raw)

    return {
        "title": title,
        "description": description,
        "pkg_version": pkg_version,
        "install_block": install_block,
        "usage_block": usage_block,
        "oss_usage": oss_usage,
        "hosted_usage": hosted_usage,
        "example_questions": example_questions,
        "unsupported_questions": unsupported_questions,
        "ops_table": ops_table,
        "entity_actions_table": entity_actions_table,
        "api_docs_link": api_docs_link,
        "auth_class": auth_class,
        "auth_fields": auth_fields,
        "raw_content": content,
        "sections": sections,
    }


def parse_auth(path: Path) -> dict:
    """Parse an AUTH.md file and return structured auth data."""
    if not path.exists():
        return {"exists": False, "methods": [], "raw_content": ""}

    content = path.read_text(encoding="utf-8")
    content = _strip_details_blocks(content)
    sections = _extract_sections(content)

    # Detect auth methods from #### headings, but filter out:
    #  1. Methods explicitly marked as unavailable ("isn't available")
    #  2. Hosting-specific method names that aren't auth types
    #     ("Execution" = how to call the connector after auth,
    #      "Bring your own OAuth flow" = a hosting mode, not an auth type)
    #  3. Duplicates (same method appears under OSS + Hosted headings)
    _HOSTING_METHOD_NAMES = {"Execution", "Bring your own OAuth flow"}
    seen_names: set[str] = set()
    methods: list[dict] = []
    for section_name, section_body in sections.items():
        subsections = _extract_subsections(section_body, level=4)
        if subsections:
            for method_name, method_body in subsections.items():
                body_stripped = method_body.strip()
                # Skip methods that declare themselves unavailable
                if "isn't available" in body_stripped:
                    continue
                # Skip hosting-specific sections (not auth types)
                if method_name in _HOSTING_METHOD_NAMES:
                    continue
                # Deduplicate (same method may appear under OSS + Hosted)
                if method_name in seen_names:
                    continue
                seen_names.add(method_name)
                methods.append({
                    "name": method_name,
                    "body": body_stripped,
                })
        elif "auth" in section_name.lower():
            methods.append({
                "name": section_name,
                "body": section_body.strip(),
            })

    return {
        "exists": True,
        "methods": methods,
        "raw_content": content,
        "sections": sections,
    }


def parse_reference(path: Path) -> dict:
    """Parse a REFERENCE.md file and return structured entity/action data."""
    if not path.exists():
        return {"exists": False, "entities": [], "raw_content": ""}

    content = path.read_text(encoding="utf-8")
    # Strip <details> blocks (response schemas)
    content = _strip_details_blocks(content)
    sections = _extract_sections(content)

    entities: list[dict] = []
    for section_name, section_body in sections.items():
        actions = _extract_subsections(section_body, level=3)
        entity_actions: list[dict] = []
        for action_name, action_body in actions.items():
            # Keep SDK code examples, skip duplicate curl examples
            code_blocks = re.findall(r"(```(?:python|py)[^\n]*\n.*?```)", action_body, re.DOTALL)
            # Extract parameter tables (markdown tables)
            tables = re.findall(r"(\|.+\|(?:\n\|.+\|)+)", action_body)
            entity_actions.append({
                "name": action_name,
                "code_examples": code_blocks,
                "parameter_tables": tables,
                "body": action_body.strip(),
            })
        if entity_actions:
            entities.append({
                "name": section_name,
                "actions": entity_actions,
            })

    return {
        "exists": True,
        "entities": entities,
        "raw_content": content,
        "sections": sections,
    }


def parse_pyproject(path: Path) -> dict:
    """Parse a pyproject.toml and return project metadata."""
    if tomllib is None:
        # Fallback: regex extraction — only handles simple single-line
        # key = "value" patterns. Sufficient for SDK-generated pyproject.toml
        # files but will not handle multiline strings or inline tables.
        content = path.read_text(encoding="utf-8")
        name_m = re.search(r'^name\s*=\s*"([^"]+)"', content, re.MULTILINE)
        ver_m = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
        desc_m = re.search(r'^description\s*=\s*"([^"]+)"', content, re.MULTILINE)
        return {
            "name": name_m.group(1) if name_m else "",
            "version": ver_m.group(1) if ver_m else "0.0.0",
            "description": desc_m.group(1) if desc_m else "",
        }

    data = tomllib.loads(path.read_text(encoding="utf-8"))
    project = data.get("project", {})
    return {
        "name": project.get("name", ""),
        "version": project.get("version", "0.0.0"),
        "description": project.get("description", ""),
    }


# ---------------------------------------------------------------------------
# Connector discovery
# ---------------------------------------------------------------------------


def discover_connectors(connectors_dir: Path) -> list[dict]:
    """Scan *connectors_dir* for connector subdirectories with pyproject.toml.

    Returns a sorted list of connector metadata dicts.
    """
    connectors: list[dict] = []
    if not connectors_dir.is_dir():
        logger.warning("Connectors directory not found: %s", connectors_dir)
        return connectors

    for child in sorted(connectors_dir.iterdir()):
        pyproject = child / "pyproject.toml"
        if child.is_dir() and pyproject.exists():
            connectors.append({
                "dir_name": child.name,
                "path": child,
                "pyproject_path": pyproject,
            })
    return connectors


# ---------------------------------------------------------------------------
# Per-connector reference generator
# ---------------------------------------------------------------------------


def generate_connector_reference(
    connector_dir: Path,
    *,
    generation_date: str | None = None,
) -> tuple[str, dict]:
    """Generate a reference markdown file for one connector.

    Returns (markdown_content, metadata_dict).
    """
    name = connector_dir.name
    safe_name = _sanitize_filename(name)
    date_str = generation_date or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    readme_path = connector_dir / "README.md"
    auth_path = connector_dir / "AUTH.md"
    ref_path = connector_dir / "REFERENCE.md"
    pyproject_path = connector_dir / "pyproject.toml"

    if not readme_path.exists():
        raise FileNotFoundError(f"{name}/README.md not found")

    # Parse all sources
    readme = parse_readme(readme_path)
    auth = parse_auth(auth_path)
    reference = parse_reference(ref_path)

    if not pyproject_path.exists():
        raise FileNotFoundError(f"{name}/pyproject.toml not found")
    pyproject = parse_pyproject(pyproject_path)

    pkg_name = pyproject["name"]
    version = pyproject["version"]
    display_name = _brand_display_name(name, readme["title"])
    description = readme["description"]

    # Auth summary
    if auth["exists"] and auth["methods"]:
        auth_summary = ", ".join(m["name"] for m in auth["methods"])
    elif readme["auth_fields"]:
        auth_summary = f"{readme['auth_class'] or 'Token'} ({', '.join(readme['auth_fields'])})"
    else:
        auth_summary = "See Usage section"

    # Docs status
    has_auth = auth["exists"]
    has_ref = reference["exists"]
    docs_status = "complete" if has_auth and has_ref else "docs pending"

    github_link = f"{GITHUB_BASE}/tree/main/connectors/{name}"

    # API docs link
    api_docs_link = readme.get("api_docs_link", "")

    # --- Build output ---
    lines: list[str] = []

    # Header
    lines.append(f"<!-- AUTO-GENERATED from connectors/{name}/ -- do not edit manually -->")
    lines.append(f"<!-- Source format: {FORMAT_VERSION} | Generated: {date_str} -->")
    lines.append("")
    lines.append(f"# {display_name}")
    lines.append("")
    lines.append(description)
    lines.append("")

    # Key metadata
    docs_link = api_docs_link or github_link
    lines.append("**Key metadata:**")
    lines.append("")
    lines.append(f"- **Package:** `{pkg_name}` v{version}")
    lines.append(f"- **Auth:** {auth_summary}")
    lines.append(f"- **Docs:** [Official API docs]({docs_link})")
    lines.append(f"- **Status:** {docs_status}")
    lines.append("")

    # Example prompts
    if readme.get("example_questions"):
        lines.append("## Example Prompts")
        lines.append("")
        for q in readme["example_questions"]:
            lines.append(f"- {q}")
        lines.append("")

    # Unsupported
    if readme.get("unsupported_questions"):
        lines.append("## Unsupported")
        lines.append("")
        for q in readme["unsupported_questions"]:
            lines.append(f"- {q}")
        lines.append("")

    # Quick Start
    lines.append("## Quick Start")
    lines.append("")
    if readme["install_block"]:
        lines.append("### Installation")
        lines.append("")
        lines.append(readme["install_block"])
        lines.append("")

    # OSS and Hosted usage
    if readme.get("oss_usage"):
        lines.append("### OSS Mode")
        lines.append("")
        lines.append(readme["oss_usage"])
        lines.append("")
    if readme.get("hosted_usage"):
        lines.append("### Hosted Mode")
        lines.append("")
        lines.append(readme["hosted_usage"])
        lines.append("")
    elif readme["usage_block"] and not readme.get("oss_usage"):
        # Fallback for legacy format
        lines.append("### Usage")
        lines.append("")
        lines.append(readme["usage_block"])
        lines.append("")

    # Operations table
    if readme["ops_table"]:
        lines.append("## Entities and Actions")
        lines.append("")
        lines.append("| Entity | Actions |")
        lines.append("|--------|---------|")
        for entity, actions, _desc in readme["ops_table"]:
            lines.append(f"| {entity} | {actions} |")
        lines.append("")

    # Authentication section
    if auth["exists"] and auth["methods"]:
        lines.append("## Authentication")
        lines.append("")
        auth_link = f"{GITHUB_BASE}/blob/main/connectors/{name}/AUTH.md"
        lines.append(f"For all authentication options, see the connector's [authentication documentation]({auth_link}).")
        lines.append("")
    elif readme["auth_class"]:
        lines.append("## Authentication")
        lines.append("")
        lines.append(f"Auth class: `{readme['auth_class']}`")
        lines.append("")
        if readme["auth_fields"]:
            lines.append("Detected auth fields (from usage example):")
            lines.append("")
            for field in readme["auth_fields"]:
                lines.append(f"- `{field}`")
            lines.append("")

    # API Reference — link to REFERENCE.md instead of inlining
    if reference["exists"]:
        lines.append("## API Reference")
        lines.append("")
        ref_link = f"{GITHUB_BASE}/blob/main/connectors/{name}/REFERENCE.md"
        lines.append(f"For the full API reference with parameters and examples, see the connector's [reference documentation]({ref_link}).")
        lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append(f"*[Full docs on GitHub]({github_link})*")
    lines.append("")

    content = "\n".join(lines)

    metadata = {
        "name": name,
        "safe_name": safe_name,
        "display_name": display_name,
        "pkg_name": pkg_name,
        "version": version,
        "auth_summary": auth_summary,
        "docs_status": docs_status,
        "key_entities": ", ".join(
            dict.fromkeys(entity for entity, _, _ in readme["ops_table"])
        ) if readme["ops_table"] else "",
        "github_link": github_link,
    }

    return content, metadata


# ---------------------------------------------------------------------------
# Connector index generator
# ---------------------------------------------------------------------------


def generate_connector_index(
    connector_metadata: list[dict],
    *,
    generation_date: str | None = None,
) -> str:
    """Generate the connector-index.md content from a list of metadata dicts."""
    date_str = generation_date or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines: list[str] = []
    lines.append("<!-- AUTO-GENERATED -- do not edit manually -->")
    lines.append(f"<!-- Source format: {FORMAT_VERSION} | Generated: {date_str} -->")
    lines.append("")
    lines.append("# Connector Index")
    lines.append("")
    lines.append(
        f"{len(connector_metadata)} connectors available. "
        "Each entry links to its full reference doc."
    )
    lines.append("")
    lines.append("| Name | Package | Auth | Key Entities | Status |")
    lines.append("|------|---------|------|--------------|--------|")

    for meta in sorted(connector_metadata, key=lambda m: m["name"]):
        link = f"[{meta['display_name']}](connectors/{meta['safe_name']}.md)"
        pkg = f"`{meta['pkg_name']}`"
        auth = meta["auth_summary"]
        entities = meta["key_entities"] or "--"
        # Truncate long entity lists for readable table rows
        if len(entities) > 60:
            entities = entities[:57] + "..."
        status = meta["docs_status"]
        lines.append(f"| {link} | {pkg} | {auth} | {entities} | {status} |")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# SKILL.md slimming
# ---------------------------------------------------------------------------

SKILL_MD_TEMPLATE = """\
---
name: airbyte-agent-connectors
description: |
  Sets up and operates Airbyte Agent Connectors -- strongly typed Python packages
  for accessing {count}+ third-party APIs (Salesforce, HubSpot, GitHub, Slack, Stripe,
  Jira, and more) through a unified entity-action interface. Use when the user wants
  to connect to a SaaS API, set up an Airbyte connector, integrate third-party data
  into an AI agent, or configure MCP tools for Claude. Covers Platform Mode (Airbyte
  Cloud) and OSS Mode (local SDK).
---

# Airbyte Agent Connectors

Airbyte Agent Connectors let AI agents call third-party APIs through strongly typed, well-documented tools. Each connector is a standalone Python package.

> **Terminology:** **Platform Mode** = Airbyte Cloud at app.airbyte.ai (managed credentials, UI visibility). **OSS Mode** = local Python SDK (self-managed credentials, no cloud dependency). **Definition ID** = UUID that identifies a connector type in the Airbyte API (used in `definition_id` fields, not `connector_type` or `connector_definition_id`).

> **Important:** This skill provides documentation and setup guidance. When helping users set up connectors, follow the documented workflows below. Do NOT attempt to import Python modules, verify package installations, or run code to check configurations -- simply guide users through the steps using the code examples provided.

## Mode Detection

**First, determine which mode the user needs:**

### Platform Mode (Airbyte Cloud)
Use when:
- Environment has `AIRBYTE_CLIENT_ID` + `AIRBYTE_CLIENT_SECRET`
- User wants connectors visible in the Airbyte UI at app.airbyte.ai
- User needs managed credential storage, entity cache, or multi-tenant deployments

### OSS Mode (Open Source / Local SDK)
Use when:
- User wants to run connectors directly without platform integration
- User is doing quick development or prototyping
- User wants Claude Code/Desktop integration via MCP only

> **Ask if unclear:** "Are you using Airbyte Platform (app.airbyte.ai) or open source connectors?"

---

## Supported Connectors

{count} connectors available. All connectors follow the same entity-action pattern: `connector.execute(entity, action, params)`

| Connector | Package | Auth Type | Key Entities |
|-----------|---------|-----------|--------------|
{popular_rows}

> **Full table:** See [references/connector-index.md](references/connector-index.md) for all {count} connectors with auth types, key entities, and documentation status.

**If the connector is NOT in the index:** Inform the user that this connector isn't available yet. Point them to [GitHub issues](https://github.com/airbytehq/airbyte-agent-connectors/issues).

---

## Platform Mode Quick Start

For users with Airbyte Platform credentials.

### Prerequisites

Get credentials from [app.airbyte.ai](https://app.airbyte.ai) > Settings > API Keys:
- `AIRBYTE_CLIENT_ID`
- `AIRBYTE_CLIENT_SECRET`

### Create a Connector

```python
from airbyte_agent_stripe import StripeConnector
from airbyte_agent_stripe.models import StripeAuthConfig

connector = await StripeConnector.create_hosted(
    external_user_id="user_123",
    airbyte_client_id="...",
    airbyte_client_secret="...",
    auth_config=StripeAuthConfig(api_key="sk_live_...")
)
```

### Use Existing Connector

```python
connector = StripeConnector(
    external_user_id="user_123",
    airbyte_client_id="...",
    airbyte_client_secret="...",
)
result = await connector.execute("customers", "list", {{"limit": 10}})
```

---

## OSS Mode Quick Start

### Install

```bash
# Using uv (recommended)
uv add airbyte-agent-github

# Or using pip in a virtual environment
python3 -m venv .venv && source .venv/bin/activate
pip install airbyte-agent-github
```

### Use Directly

```python
from airbyte_agent_github import GithubConnector
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

connector = GithubConnector(
    auth_config=GithubPersonalAccessTokenAuthConfig(token="ghp_your_token")
)

result = await connector.execute("issues", "list", {{
    "owner": "airbytehq",
    "repo": "airbyte",
    "states": ["OPEN"],
    "per_page": 10
}})
```

### Add to Claude via MCP

```bash
claude mcp add airbyte-agent-mcp --scope project
```

---

## Entity-Action API Pattern

All connectors use the same interface:

```python
result = await connector.execute(entity, action, params)
# result.data contains the records (list or dict depending on action)
# result.meta contains pagination info for list operations
```

### Actions

| Action | Description | `result.data` Type |
|--------|-------------|-------------------|
| `list` | Get multiple records | `list[dict]` |
| `get` | Get single record by ID | `dict` |
| `create` | Create new record | `dict` |
| `update` | Modify existing record | `dict` |
| `delete` | Remove record | `dict` |
| `api_search` | Native API search syntax | `list[dict]` |

### Quick Examples

```python
# List
await connector.execute("customers", "list", {{"limit": 10}})

# Get
await connector.execute("customers", "get", {{"id": "cus_xxx"}})

# Search
await connector.execute("repositories", "api_search", {{
    "query": "language:python stars:>1000"
}})
```

### Pagination

```python
async def fetch_all(connector, entity, params=None):
    all_records = []
    cursor = None
    params = params or {{}}

    while True:
        if cursor:
            params["after"] = cursor
        result = await connector.execute(entity, "list", params)
        all_records.extend(result.data)

        if result.meta and hasattr(result.meta, 'pagination'):
            cursor = getattr(result.meta.pagination, 'cursor', None)
            if not cursor:
                break
        else:
            break

    return all_records
```

---

## Authentication Quick Reference

### API Key Connectors

```python
# Stripe
from airbyte_agent_stripe.models import StripeAuthConfig
auth_config=StripeAuthConfig(api_key="sk_live_...")

# Gong
from airbyte_agent_gong.models import GongAccessKeyAuthenticationAuthConfig
auth_config=GongAccessKeyAuthenticationAuthConfig(
    access_key="...", access_key_secret="..."
)

# HubSpot (Private App)
from airbyte_agent_hubspot.models import HubspotPrivateAppAuthConfig
auth_config=HubspotPrivateAppAuthConfig(access_token="pat-na1-...")
```

### Personal Access Token

```python
# GitHub
from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig
auth_config=GithubPersonalAccessTokenAuthConfig(token="ghp_...")

# Slack
from airbyte_agent_slack.models import SlackAuthConfig
auth_config=SlackAuthConfig(token="xoxb-...")
```

### OAuth (requires refresh token)

```python
# Salesforce
from airbyte_agent_salesforce.models import SalesforceAuthConfig
auth_config=SalesforceAuthConfig(
    client_id="...", client_secret="...", refresh_token="..."
)
```

> **Per-connector auth details:** Each connector reference in [references/connectors/](references/connectors/) includes the specific auth class name and fields.

---

## Security Best Practices

- Never hard-code credentials in source files. Use environment variables or `.env` files.
- Use `.env` pattern: `from dotenv import load_dotenv; load_dotenv()`
- Rotate tokens regularly. Use short-lived tokens where possible.
- For production, use Platform Mode for managed credential storage.

---

## Per-Connector Reference Documentation

- [Connector Index](references/connector-index.md) -- full table of all connectors
- Per-connector references: [references/connectors/](references/connectors/)

Each per-connector reference includes: package name and version, authentication details, available entities and actions, quick-start code snippets, and links to full GitHub documentation.

## Reference Documentation

| Topic | Reference |
|-------|----------|
| Getting Started | [references/getting-started.md](references/getting-started.md) |
| Platform Setup | [references/platform-setup.md](references/platform-setup.md) |
| OSS Setup | [references/oss-setup.md](references/oss-setup.md) |
| Entity-Action API | [references/entity-action-api.md](references/entity-action-api.md) |
| Authentication | [references/authentication.md](references/authentication.md) |
| Programmatic Setup | [references/programmatic-setup.md](references/programmatic-setup.md) |
| MCP Integration | [references/mcp-integration.md](references/mcp-integration.md) |
| Troubleshooting | [references/troubleshooting.md](references/troubleshooting.md) |

## How References Are Generated

Reference docs are auto-generated by `scripts/generate_skill_references.py`.
Run `python scripts/generate_skill_references.py --all` to regenerate all
references, or `--connector <name>` for a specific connector.

---

## Skill Metadata

- **Author:** Airbyte
- **Version:** 1.2.0
- **License:** Elastic-2.0
- **Compatibility:** Requires Python 3.11+. Recommends uv for package management.
- **Repository:** https://github.com/airbytehq/airbyte-agent-connectors
- **MCP Server:** airbyte-agent-mcp

## Support

- **Slack Community**: [slack.airbyte.com](https://slack.airbyte.com/)
- **GitHub Issues**: [airbytehq/airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors/issues)
- **Documentation**: [docs.airbyte.com/ai-agents](https://docs.airbyte.com/ai-agents)
"""


def generate_skill_md(connector_metadata: list[dict]) -> str:
    """Generate SKILL.md with operational content + auto-generated connector table."""
    # Pick up to 5 popular connectors (by name recognition) for the table
    popular_names = ["stripe", "hubspot", "github", "salesforce", "gong"]
    popular: list[dict] = []
    for pname in popular_names:
        for meta in connector_metadata:
            if meta["name"] == pname:
                popular.append(meta)
                break

    # If we have fewer than 3 popular, add from the rest
    if len(popular) < 3:
        for meta in connector_metadata:
            if meta not in popular:
                popular.append(meta)
            if len(popular) >= 5:
                break

    rows: list[str] = []
    for meta in popular:
        link = f"[{meta['display_name']}](references/connectors/{meta['safe_name']}.md)"
        auth = meta["auth_summary"]
        entities = meta["key_entities"] or "--"
        if len(entities) > 40:
            entities = entities[:37] + "..."
        rows.append(f"| {link} | `{meta['pkg_name']}` | {auth} | {entities} |")

    return SKILL_MD_TEMPLATE.format(
        count=len(connector_metadata),
        popular_rows="\n".join(rows),
    )


# ---------------------------------------------------------------------------
# Core generate/check logic
# ---------------------------------------------------------------------------


def generate_all(
    connectors_dir: Path,
    output_dir: Path,
    *,
    connector_names: list[str] | None = None,
    generation_date: str | None = None,
) -> tuple[list[dict], list[str]]:
    """Generate reference docs for connectors.

    If *connector_names* is provided, only those connectors are regenerated,
    but the index is always rebuilt from *all* discovered connectors.

    Returns (all_metadata, warnings).
    """
    all_connectors = discover_connectors(connectors_dir)
    if not all_connectors:
        logger.warning("No connectors found in %s", connectors_dir)
        return [], ["No connectors found"]

    refs_dir = output_dir / "references" / "connectors"
    refs_dir.mkdir(parents=True, exist_ok=True)

    # Determine which connectors to regenerate
    if connector_names:
        target_set = set(connector_names)
    else:
        target_set = None  # all

    all_metadata: list[dict] = []
    warnings: list[str] = []

    for conn in all_connectors:
        name = conn["dir_name"]
        readme_path = conn["path"] / "README.md"

        if not readme_path.exists():
            msg = f"Skipping {name}: README.md not found"
            logger.warning(msg)
            warnings.append(msg)
            continue

        try:
            # Validate README structure
            readme_content = readme_path.read_text(encoding="utf-8")
            struct_warnings = validate_readme_structure(readme_content, name)
            warnings.extend(struct_warnings)
            for w in struct_warnings:
                logger.warning(w)

            content, metadata = generate_connector_reference(
                conn["path"],
                generation_date=generation_date,
            )
            all_metadata.append(metadata)

            # Only write if this connector is in our target set
            if target_set is None or name in target_set:
                out_path = refs_dir / f"{metadata['safe_name']}.md"
                out_path.write_text(content, encoding="utf-8")
                logger.info("Generated %s", out_path)

        except (ValueError, FileNotFoundError) as exc:
            msg = f"Error processing {name}: {exc}"
            logger.error(msg)
            warnings.append(msg)

    # Always rebuild the index from all discovered connectors
    index_content = generate_connector_index(
        all_metadata, generation_date=generation_date,
    )
    index_path = output_dir / "references" / "connector-index.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(index_content, encoding="utf-8")
    logger.info("Generated %s", index_path)

    # Generate SKILL.md
    skill_content = generate_skill_md(all_metadata)
    skill_path = output_dir / "SKILL.md"
    skill_path.write_text(skill_content, encoding="utf-8")
    logger.info("Generated %s", skill_path)

    return all_metadata, warnings


def check_drift(
    connectors_dir: Path,
    skills_dir: Path,
    *,
    generation_date: str | None = None,
) -> tuple[bool, list[str]]:
    """Compare generated content with files in *skills_dir*.

    Returns (has_drift, diff_lines).
    """
    with tempfile.TemporaryDirectory(prefix="skill-check-") as tmpdir:
        tmp_path = Path(tmpdir)
        generate_all(
            connectors_dir, tmp_path,
            generation_date=generation_date,
        )

        diffs: list[str] = []
        has_drift = False

        # Compare all files in the temp dir against skills_dir
        for tmp_file in sorted(tmp_path.rglob("*.md")):
            rel = tmp_file.relative_to(tmp_path)
            existing = skills_dir / rel

            if not existing.exists():
                diffs.append(f"NEW: {rel}")
                has_drift = True
                continue

            generated = tmp_file.read_text(encoding="utf-8").splitlines(keepends=True)
            current = existing.read_text(encoding="utf-8").splitlines(keepends=True)

            file_diff = list(difflib.unified_diff(
                current, generated,
                fromfile=f"current/{rel}",
                tofile=f"generated/{rel}",
            ))
            if file_diff:
                has_drift = True
                diffs.extend(line.rstrip() for line in file_diff)

        # Check for files in skills_dir/references that are NOT in temp
        existing_refs = skills_dir / "references" / "connectors"
        if existing_refs.is_dir():
            tmp_refs = tmp_path / "references" / "connectors"
            for existing_file in sorted(existing_refs.glob("*.md")):
                rel = existing_file.relative_to(skills_dir)
                if not (tmp_path / rel).exists():
                    diffs.append(f"REMOVED: {rel}")
                    has_drift = True

        return has_drift, diffs


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Auto-generate connector reference docs for skills/.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate references for all connectors.",
    )
    parser.add_argument(
        "--connector",
        nargs="+",
        metavar="NAME",
        help="Generate references for specific connector(s) and rebuild index.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write to a temp dir (or --output-dir) instead of skills/.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that skills/ is up to date (nonzero exit if drift).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Custom output directory (default: skills/airbyte-agent-connectors).",
    )
    parser.add_argument(
        "--connectors-dir",
        type=Path,
        default=CONNECTORS_DIR,
        help="Path to connectors/ directory (default: auto-detected from repo root).",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if args.check:
        # Determine the date to use for comparison — use a fixed date so
        # that regeneration does not trigger false drift from timestamp changes.
        # We read the existing index to extract the last generation date.
        skills_dir = args.output_dir or DEFAULT_SKILLS_DIR
        index_path = skills_dir / "references" / "connector-index.md"
        gen_date: str | None = None
        if index_path.exists():
            m = re.search(r"Generated:\s*(\d{4}-\d{2}-\d{2})", index_path.read_text())
            if m:
                gen_date = m.group(1)

        has_drift, diffs = check_drift(
            args.connectors_dir,
            skills_dir,
            generation_date=gen_date,
        )
        if has_drift:
            logger.error("Drift detected! Run the generator to update skills/.")
            for line in diffs:
                print(line)
            return 1
        logger.info("No drift detected. skills/ is up to date.")
        return 0

    if not args.all and not args.connector:
        parser.error("Specify --all, --connector NAME..., or --check.")

    # Determine output directory
    _tmpdir = None  # keep a reference so GC doesn't clean it up early
    if args.dry_run and not args.output_dir:
        _tmpdir = tempfile.TemporaryDirectory(prefix="skill-dryrun-")
        output_dir = Path(_tmpdir.name)
        logger.info("Dry-run output directory: %s", output_dir)
    elif args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = DEFAULT_SKILLS_DIR

    connector_names = args.connector if args.connector else None

    all_metadata, warnings = generate_all(
        args.connectors_dir,
        output_dir,
        connector_names=connector_names,
    )

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"Generated references for {len(all_metadata)} connector(s)")
    print(f"Output directory: {output_dir}")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    print(f"{'=' * 60}\n")

    if args.dry_run:
        print("Dry-run complete. Files written to:", output_dir)
        # List generated files
        for f in sorted(output_dir.rglob("*.md")):
            rel = f.relative_to(output_dir)
            lines_count = len(f.read_text().splitlines())
            print(f"  {rel} ({lines_count} lines)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
