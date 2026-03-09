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
import hashlib
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
    "Available Operations",
    "Type Definitions",
    "Documentation",
]

REPO_ROOT = Path(__file__).resolve().parent.parent
CONNECTORS_DIR = REPO_ROOT / "connectors"
DEFAULT_SKILLS_DIR = REPO_ROOT / "skills" / "airbyte-agent-connectors"
DEFAULT_REFS_DIR = DEFAULT_SKILLS_DIR / "references"

GITHUB_BASE = "https://github.com/airbytehq/airbyte-ai-connectors"


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
    return warnings


def parse_readme(path: Path) -> dict:
    """Parse a connector README.md and return structured data."""
    content = path.read_text(encoding="utf-8")
    sections = _extract_sections(content)

    # Title: first H1
    title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.parent.name.title()

    # Description: first paragraph after title
    lines_after_title = content.split("\n", 1)[1] if "\n" in content else ""
    description = _first_paragraph(lines_after_title)

    # Package version from bold text
    pkg_version_match = re.search(
        r"\*\*Package Version:\*\*\s*(\S+)", content
    )
    pkg_version = pkg_version_match.group(1) if pkg_version_match else None

    # Install command
    install_block = _extract_code_block(sections.get("Installation", ""))

    # Usage code
    usage_block = _extract_code_block(sections.get("Usage", ""))

    # Operations — extract ### subsections
    ops_body = sections.get("Available Operations", "")
    operations = _extract_subsections(ops_body, level=3)

    # Build operations table: list of (entity, action, description)
    ops_table: list[tuple[str, str, str]] = []
    for entity_heading, entity_body in operations.items():
        entity_name = entity_heading.replace(" Operations", "")
        for item in _extract_bullet_list(entity_body):
            # Pattern: `method_name()` - description
            m = re.match(r"`([^`]+)`\s*[-\u2013\u2014]\s*(.*)", item)
            if m:
                ops_table.append((entity_name, m.group(1), m.group(2)))

    # Auth info — extract from Usage code block
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
        "operations": operations,
        "ops_table": ops_table,
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

    # Detect auth methods from #### headings
    methods: list[dict] = []
    for section_name, section_body in sections.items():
        subsections = _extract_subsections(section_body, level=4)
        if subsections:
            for method_name, method_body in subsections.items():
                methods.append({
                    "name": method_name,
                    "body": method_body.strip(),
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
        # Fallback: regex extraction
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
    display_name = readme["title"]
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

    # --- Build output ---
    lines: list[str] = []

    # Header
    lines.append(f"<!-- AUTO-GENERATED from connectors/{name}/ -- do not edit manually -->")
    lines.append(f"<!-- Source format: {FORMAT_VERSION} | Generated: {date_str} -->")
    lines.append("")
    lines.append(f"# {display_name}")
    lines.append("")
    lines.append(f"# Package: {pkg_name} v{version}")
    lines.append("")
    lines.append(description)
    lines.append("")

    # Key metadata
    lines.append("**Key metadata:**")
    lines.append("")
    lines.append(f"- **Package:** `{pkg_name}` v{version}")
    lines.append(f"- **Auth:** {auth_summary}")
    lines.append(f"- **Docs:** [Official API docs]({github_link})")
    lines.append(f"- **Status:** {docs_status}")
    lines.append("")

    # Quick Start
    lines.append("## Quick Start")
    lines.append("")
    if readme["install_block"]:
        lines.append("### Installation")
        lines.append("")
        lines.append(readme["install_block"])
        lines.append("")
    if readme["usage_block"]:
        lines.append("### Usage")
        lines.append("")
        lines.append(readme["usage_block"])
        lines.append("")

    # Operations table
    if readme["ops_table"]:
        lines.append("## Entities and Actions")
        lines.append("")
        lines.append("| Entity | Action | Description |")
        lines.append("|--------|--------|-------------|")
        for entity, action, desc in readme["ops_table"]:
            lines.append(f"| {entity} | `{action}` | {desc} |")
        lines.append("")

    # Authentication section
    if auth["exists"] and auth["methods"]:
        lines.append("## Authentication")
        lines.append("")
        for method in auth["methods"]:
            lines.append(f"### {method['name']}")
            lines.append("")
            lines.append(method["body"])
            lines.append("")
    elif readme["auth_class"]:
        lines.append("## Authentication")
        lines.append("")
        lines.append(f"Auth class: `{readme['auth_class']}`")
        lines.append("")
        if readme["auth_fields"]:
            lines.append("Required fields:")
            lines.append("")
            for field in readme["auth_fields"]:
                lines.append(f"- `{field}`")
            lines.append("")

    # API Reference (from REFERENCE.md)
    if reference["exists"] and reference["entities"]:
        lines.append("## API Reference")
        lines.append("")
        for entity in reference["entities"]:
            lines.append(f"### {entity['name']}")
            lines.append("")
            for action in entity["actions"]:
                lines.append(f"#### {action['name']}")
                lines.append("")
                if action["parameter_tables"]:
                    for table in action["parameter_tables"]:
                        lines.append(table)
                        lines.append("")
                if action["code_examples"]:
                    for code in action["code_examples"]:
                        lines.append(code)
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
        status = meta["docs_status"]
        lines.append(f"| {link} | {pkg} | {auth} | {entities} | {status} |")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# SKILL.md slimming
# ---------------------------------------------------------------------------

SKILL_MD_TEMPLATE = """\
# Airbyte Agent Connectors

Comprehensive reference for all Airbyte AI connectors -- type-safe Python
packages for integrating SaaS APIs into AI applications.

## Overview

{count} connectors available -- see the
[Connector Index](references/connector-index.md) for the full list with
auth types, key entities, and documentation status.

## Popular Connectors

| Connector | Package | Description |
|-----------|---------|-------------|
{popular_rows}

> For the full table, see [references/connector-index.md](references/connector-index.md).

## Quick Start (any connector)

```bash
# Install a connector
uv pip install airbyte-ai-<name>
```

```python
from airbyte_ai_<name> import <Name>Connector
from airbyte_ai_<name>.models import <Name>AuthConfig

connector = <Name>Connector(auth_config=<Name>AuthConfig(...))
```

## Reference Documentation

- [Connector Index](references/connector-index.md) -- full table of all connectors
- Per-connector references: [references/connectors/](references/connectors/)

Each per-connector reference includes:

- Package name and version
- Authentication details
- Available entities and actions
- Quick-start code snippets
- Links to full GitHub documentation

## How References Are Generated

Reference docs are auto-generated by `scripts/generate_skill_references.py`.
Run `python scripts/generate_skill_references.py --all` to regenerate all
references, or `--connector <name>` for a specific connector.

See the [generator README](../../scripts/README-generate-skill-references.md)
for full usage instructions.
"""


def generate_skill_md(connector_metadata: list[dict]) -> str:
    """Generate a slim SKILL.md with summary + links."""
    # Pick up to 5 popular connectors (by name recognition)
    popular_names = ["stripe", "hubspot", "github", "gong", "asana"]
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
        rows.append(f"| {link} | `{meta['pkg_name']}` | See reference |")

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
    if args.dry_run and not args.output_dir:
        output_dir = Path(tempfile.mkdtemp(prefix="skill-dryrun-"))
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
