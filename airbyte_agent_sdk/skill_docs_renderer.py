"""Render hosted skill docs into text for agent tools."""

from __future__ import annotations

import json
from typing import Any


def render_skill_docs(docs: dict[str, Any]) -> str:
    metadata = docs.get("metadata") or {}
    lines = [
        f"# {metadata.get('title', docs.get('id', 'Skill docs'))}",
        f"Skill ID: {metadata.get('id', '')}",
        f"Kind: {metadata.get('kind', '')}",
    ]
    summary = metadata.get("summary")
    if summary:
        lines.append(f"Summary: {summary}")
    warnings = metadata.get("warnings") or []
    if warnings:
        lines.append("")
        lines.append("Warnings:")
        lines.extend(f"- {warning}" for warning in warnings)

    section_id = docs.get("section_id")
    content = docs.get("content") or []
    if content and not section_id:
        for block in content:
            lines.extend(_render_block(block))

    outline = docs.get("outline") or []
    if outline and (section_id or not content or not _content_has_outline(content)):
        lines.append("")
        lines.append("## Outline")
        for section in outline:
            outline_section_id = section.get("id", "")
            title = section.get("title", outline_section_id)
            summary = section.get("summary")
            suffix = f" - {summary}" if summary else ""
            lines.append(f"- `{outline_section_id}` {title}{suffix}")

    if section_id:
        lines.append("")
        lines.append(f"## Section `{section_id}`")
        for block in content:
            lines.extend(_render_block(block))

    return "\n".join(lines).strip()


def _content_has_outline(content: list[Any]) -> bool:
    for block in content:
        if isinstance(block, dict) and block.get("type") == "heading" and block.get("text") == "Outline":
            return True
    return False


def _render_block(block: Any) -> list[str]:
    if not isinstance(block, dict):
        return [json.dumps(block, sort_keys=True, default=str)]
    block_type = block.get("type")
    try:
        if block_type == "heading":
            level = int(block.get("level") or 2)
            level = min(max(level, 1), 6)
            return ["", f"{'#' * level} {block.get('text', '')}"]
        if block_type == "paragraph":
            return ["", str(block.get("text", ""))]
        if block_type == "list":
            return ["", *[f"- {item}" for item in block.get("items") or []]]
        if block_type == "code":
            language = block.get("language") or ""
            code = block.get("code") or ""
            return ["", f"```{language}", str(code), "```"]
        if block_type == "table":
            return _render_table(block)
    except Exception:
        return [json.dumps(block, sort_keys=True, default=str)]
    return [json.dumps(block, sort_keys=True, default=str)]


def _render_table(block: dict[str, Any]) -> list[str]:
    headers = [_escape_table_cell(header) for header in block.get("headers") or []]
    rows = [[_escape_table_cell(cell) for cell in row] for row in block.get("rows") or []]
    if not headers:
        return [json.dumps(block, sort_keys=True, default=str)]
    rendered = ["", "| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        padded = [*row, *("" for _ in range(max(0, len(headers) - len(row))))]
        rendered.append("| " + " | ".join(padded[: len(headers)]) + " |")
    return rendered


def _escape_table_cell(value: Any) -> str:
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ")
