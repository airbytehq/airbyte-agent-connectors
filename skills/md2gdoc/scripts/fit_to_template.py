"""
Fit user markdown content into a template skeleton.

Parses the user's markdown, maps sections to template placeholders via
fuzzy heading matching (derived dynamically from the skeleton), fills
metadata with smart defaults, and renders the final templated markdown.

Usage:
    python3 fit_to_template.py <input.md> <skeleton.md> <output.md> \
        [--author "Name"] [--title "Title"] [--status "Status"] \
        [--meta KEY VALUE ...]
"""

import argparse
import re
import subprocess
from datetime import date
from pathlib import Path
from typing import Optional


STOP_WORDS = {
    "and", "or", "the", "a", "an", "in", "of", "for", "to",
    "with", "on", "at", "by", "is", "are", "be", "can", "more",
    "than", "one", "there",
}


# ---------------------------------------------------------------------------
# Dynamic section mapping from skeleton
# ---------------------------------------------------------------------------

def derive_section_map(skeleton_text: str) -> dict:
    """Parse skeleton.md to build a section map dynamically.

    Scans for heading lines (# ...) followed by {{PLACEHOLDER}} tokens.
    Generates keyword lists from the heading text itself.

    Returns:
        dict mapping placeholder_name -> list of keyword strings
    """
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
    placeholder_re = re.compile(r"\{\{([A-Z_0-9]+)\}\}")

    section_map = {}
    lines = skeleton_text.splitlines()

    for i, line in enumerate(lines):
        heading_match = heading_re.match(line)
        if heading_match:
            heading_text = heading_match.group(2).strip()

            # Look ahead for the {{PLACEHOLDER}} on the next non-empty line
            for j in range(i + 1, min(i + 4, len(lines))):
                ph_match = placeholder_re.search(lines[j])
                if ph_match:
                    placeholder = ph_match.group(1)
                    keywords = generate_keywords(heading_text)
                    section_map[placeholder] = keywords
                    break

    return section_map


def generate_keywords(heading_text: str) -> list:
    """Generate match keywords from heading text.

    'Data Protection Considerations' produces:
        ['data protection considerations',
         'data protection',
         'protection considerations',
         'protection',
         'considerations']
    """
    lower = heading_text.lower().strip()
    # Remove non-alphanumeric chars for cleaner matching
    cleaned = re.sub(r"[^a-z0-9\s]", "", lower).strip()
    words = cleaned.split()
    keywords = [cleaned]  # Always include full text

    # Add sub-phrases (sliding window of 3 and 2 words)
    for window in [3, 2]:
        for start in range(len(words) - window + 1):
            phrase = " ".join(words[start:start + window])
            if phrase != cleaned and phrase not in keywords:
                keywords.append(phrase)

    # Add individual significant words (skip stop words and short words)
    for word in words:
        if word not in STOP_WORDS and len(word) > 2 and word not in keywords:
            keywords.append(word)

    return keywords


def find_unmapped_insertion_point(skeleton_text: str) -> str:
    """Find the best heading to insert unmapped content before.

    Strategy:
    1. Find the first H2 after a main content section (solution/design/proposal)
    2. Fallback: before the last H1
    3. Final fallback: empty string (append at end)

    Returns the full heading line to insert before, or empty string.
    """
    heading_re = re.compile(r"^(#{1,2})\s+(.+)$", re.MULTILINE)
    headings = [(m.group(0), len(m.group(1)), m.group(2).strip())
                for m in heading_re.finditer(skeleton_text)]

    # Find a main content section
    main_idx = None
    main_keywords = ["solution", "proposal", "design", "implementation",
                     "approach", "content", "body"]
    for i, (full, level, text) in enumerate(headings):
        if level == 2:
            lower = text.lower()
            if any(kw in lower for kw in main_keywords):
                main_idx = i
                break

    if main_idx is not None:
        # Find the next sibling H2 (or H1) after main content
        for i in range(main_idx + 1, len(headings)):
            full, level, text = headings[i]
            if level <= 2:
                return full

    # Fallback: before the last H1
    h1s = [(full, text) for full, level, text in headings if level == 1]
    if len(h1s) > 1:
        return h1s[-1][0]

    return ""  # append at end


# ---------------------------------------------------------------------------
# Markdown parser
# ---------------------------------------------------------------------------

def _mask_code_blocks(md_text: str):
    """
    Replace code block contents with placeholders so that headings inside
    code fences (e.g. YAML comments starting with #) are not parsed.

    Returns (masked_text, replacements_dict).
    """
    code_re = re.compile(r"(```[^\n]*\n)(.*?)(```)", re.DOTALL)
    replacements = {}
    counter = [0]

    def _replace(m):
        key = f"__CODE_BLOCK_{counter[0]}__"
        counter[0] += 1
        replacements[key] = m.group(0)
        return key

    masked = code_re.sub(_replace, md_text)
    return masked, replacements


def _restore_code_blocks(text: str, replacements: dict) -> str:
    """Restore code block placeholders back to original content."""
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text


def parse_sections(md_text: str):
    """
    Split markdown into top-level sections (H1/H2 boundaries only).

    H3+ headings are kept as content within their parent H1/H2 section.
    Headings inside code fences are ignored.

    Returns a list of dicts:
        {"level": int, "title": str, "content": str}

    Content before the first heading is returned with level=0 and title="".
    """
    # Mask code blocks to avoid parsing # comments as headings
    masked_text, code_replacements = _mask_code_blocks(md_text)

    heading_re = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
    sections = []
    last_end = 0

    for match in heading_re.finditer(masked_text):
        level = len(match.group(1))
        title = match.group(2).strip()
        preceding = masked_text[last_end:match.start()].strip()

        if level <= 2:
            # New top-level section — flush preceding content to last section
            if preceding:
                if sections:
                    sections[-1]["content"] += "\n\n" + preceding
                else:
                    sections.append({"level": 0, "title": "", "content": preceding})

            sections.append({"level": level, "title": title, "content": ""})
        else:
            # H3+ — include as content within the current section
            if preceding:
                if sections:
                    sections[-1]["content"] += "\n\n" + preceding
                else:
                    sections.append({"level": 0, "title": "", "content": preceding})

            sub_heading = "#" * level + " " + title
            if sections:
                sections[-1]["content"] += "\n\n" + sub_heading
            else:
                sections.append({"level": 0, "title": "", "content": sub_heading})

        last_end = match.end()

    # Trailing content after last heading
    if last_end < len(masked_text):
        trailing = masked_text[last_end:].strip()
        if trailing:
            if sections:
                sections[-1]["content"] += "\n\n" + trailing if sections[-1]["content"] else trailing
            else:
                sections.append({"level": 0, "title": "", "content": trailing})

    # Restore code blocks in all section content
    for s in sections:
        s["content"] = _restore_code_blocks(s["content"], code_replacements)
        s["title"] = _restore_code_blocks(s["title"], code_replacements)

    return sections


def match_section(title: str, section_map: dict) -> Optional[str]:
    """Return the template placeholder name for a heading, or None."""
    lower = title.lower().strip()
    for placeholder, keywords in section_map.items():
        for kw in keywords:
            if kw in lower:
                return placeholder
    return None


# ---------------------------------------------------------------------------
# Metadata helpers
# ---------------------------------------------------------------------------

def git_user_name() -> str:
    try:
        result = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True, text=True, timeout=5,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def extract_frontmatter(md_text: str):
    """
    If the markdown starts with YAML frontmatter (---), extract it and return
    (frontmatter_dict, remaining_text). Otherwise return ({}, md_text).
    """
    fm_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    m = fm_re.match(md_text)
    if not m:
        return {}, md_text

    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip().lower()] = val.strip().strip('"').strip("'")
    return fm, md_text[m.end():]


def extract_first_h1(sections) -> str:
    """Return the title of the first H1 heading, or empty string."""
    for s in sections:
        if s["level"] == 1 and s["title"]:
            return s["title"]
    return ""


def extract_skeleton_metadata_placeholders(skeleton_text: str) -> list:
    """Find all {{PLACEHOLDER}} tokens in the metadata area (before first heading).

    Returns list of placeholder names found in the metadata area.
    """
    first_heading = re.search(r"^#{1,6}\s+", skeleton_text, re.MULTILINE)
    if first_heading:
        metadata_area = skeleton_text[:first_heading.start()]
    else:
        metadata_area = skeleton_text

    return re.findall(r"\{\{([A-Z_0-9]+)\}\}", metadata_area)


# ---------------------------------------------------------------------------
# Content mapping
# ---------------------------------------------------------------------------

def map_content(sections, section_map: dict, preamble_content: str = ""):
    """
    Map parsed sections to template placeholders.

    The first H1 heading is treated as the document title and skipped
    (its content is merged into the first content placeholder or preamble).

    Returns:
        mapped: dict[placeholder] -> list of content strings
        unmapped: list of sections that didn't match any placeholder
    """
    mapped = {k: [] for k in section_map}
    unmapped = []

    # Find the first content placeholder (for preamble content)
    first_content_key = next(iter(section_map), None)

    # Any preamble content (before first heading) goes to the first section
    if preamble_content.strip() and first_content_key:
        mapped[first_content_key].append(preamble_content.strip())

    first_h1_seen = False
    for section in sections:
        if section["level"] == 0:
            continue  # already handled as preamble

        # Skip the first H1 — it's the document title. Its content (if any)
        # gets pushed to the first content section so it's not lost.
        if section["level"] == 1 and not first_h1_seen:
            first_h1_seen = True
            if section["content"].strip() and first_content_key:
                mapped[first_content_key].append(section["content"].strip())
            continue

        placeholder = match_section(section["title"], section_map)

        section_text = section["content"] if section["content"] else ""

        if placeholder:
            # When multiple sections map to the same placeholder, preserve
            # subsequent headings as sub-headings so content stays organized.
            if mapped[placeholder]:
                # This placeholder already has content — add heading as H3
                heading = f"### {section['title']}"
                section_text = heading + ("\n\n" + section_text if section_text else "")
            mapped[placeholder].append(section_text)
        else:
            # Keep the heading for unmapped sections
            heading_prefix = "#" * section["level"]
            full_text = f"{heading_prefix} {section['title']}"
            if section_text:
                full_text += "\n\n" + section_text
            unmapped.append(full_text)

    return mapped, unmapped


# ---------------------------------------------------------------------------
# Template rendering
# ---------------------------------------------------------------------------

def render_template(skeleton: str, mapped: dict, unmapped: list,
                    metadata: dict, section_map: dict) -> str:
    """Replace {{PLACEHOLDER}} tokens in the skeleton with mapped content."""
    result = skeleton

    # Replace ALL placeholders found in the skeleton with values from
    # metadata (case-insensitive key match) or section content
    all_placeholders = re.findall(r"\{\{([A-Z_0-9]+)\}\}", skeleton)
    for ph in all_placeholders:
        key = ph.lower()
        # Check metadata first
        value = metadata.get(key, "")
        # Then check mapped content
        if not value and ph in mapped:
            value = "\n\n".join(c for c in mapped[ph] if c.strip())
        result = result.replace("{{" + ph + "}}", value)

    # Append unmapped sections at the best insertion point
    if unmapped:
        unmapped_block = "\n\n".join(unmapped)
        marker = find_unmapped_insertion_point(skeleton)
        if marker and marker in result:
            result = result.replace(
                marker,
                unmapped_block + "\n\n" + marker,
            )
        else:
            result += "\n\n" + unmapped_block

    # Remove completely empty metadata lines (e.g. "**PRD:** \n")
    # but keep section headings
    lines = result.splitlines()
    cleaned = []
    for line in lines:
        meta_line = re.match(r"^\*\*[^*]+:\*\*\s*$", line)
        if meta_line:
            continue
        cleaned.append(line)
    result = "\n".join(cleaned)

    # Collapse runs of 3+ blank lines down to max 2 (one visual gap)
    result = re.sub(r"\n{3,}", "\n\n", result)

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Fit user markdown into a template structure"
    )
    parser.add_argument("input", help="Path to user's markdown file")
    parser.add_argument("skeleton", help="Path to template skeleton markdown")
    parser.add_argument("output", help="Path to write templated output")
    parser.add_argument("--author", default=None)
    parser.add_argument("--title", default=None)
    parser.add_argument("--status", default=None)
    parser.add_argument("--target-date", default=None)
    parser.add_argument("--meta", nargs=2, action="append", metavar=("KEY", "VALUE"),
                        help="Set arbitrary metadata: --meta key value")
    args = parser.parse_args()

    # Read files
    md_text = Path(args.input).read_text(encoding="utf-8")
    skeleton = Path(args.skeleton).read_text(encoding="utf-8")

    # Derive section map dynamically from the skeleton
    section_map = derive_section_map(skeleton)

    # Extract frontmatter if present
    frontmatter, md_body = extract_frontmatter(md_text)

    # Parse sections
    sections = parse_sections(md_body)

    # Build metadata with smart defaults
    today = date.today().strftime("%Y-%m-%d")
    author = args.author or frontmatter.get("author", "") or git_user_name()
    title = args.title or frontmatter.get("title", "") or extract_first_h1(sections)
    status = args.status or frontmatter.get("status", "") or "Draft"

    metadata = {
        "title": title,
        "author": author,
        "date": today,
        "target_date": args.target_date or frontmatter.get("target_date", ""),
        "created_date": today,
        "last_updated_date": today,
        "status": status,
        # Common aliases for date fields
        "created": today,
        "last_updated": today,
        "target_ratification_date": args.target_date or frontmatter.get("target_date", ""),
    }

    # Merge frontmatter values into metadata (so any skeleton placeholder can match)
    for key, val in frontmatter.items():
        if key not in metadata:
            metadata[key] = val

    # Merge --meta key value pairs
    if args.meta:
        for key, value in args.meta:
            metadata[key.lower()] = value

    # Map content
    preamble = ""
    if sections and sections[0]["level"] == 0:
        preamble = sections[0]["content"]

    mapped, unmapped = map_content(sections, section_map, preamble)

    # Render
    output_text = render_template(skeleton, mapped, unmapped, metadata, section_map)

    # Write
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(output_text, encoding="utf-8")

    # Report
    filled = sum(1 for v in mapped.values() if any(c.strip() for c in v))
    total = len(section_map)
    print(f"Template fitting complete:")
    print(f"  Sections mapped: {filled}/{total}")
    print(f"  Unmapped sections (appended): {len(unmapped)}")
    print(f"  Title: {metadata['title']}")
    print(f"  Author: {metadata['author']}")
    print(f"  Status: {metadata['status']}")
    print(f"  Output: {args.output}")


if __name__ == "__main__":
    main()
