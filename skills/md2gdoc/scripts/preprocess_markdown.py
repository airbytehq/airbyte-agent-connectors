#!/usr/bin/env python3
"""Pre-process a markdown file for conversion to Google Docs.

Performs two transformations:
1. Strips non-content preamble (text before first markdown heading).
2. Converts ASCII art tables (box-drawing characters) inside code fences
   to standard markdown table syntax. Other code blocks are preserved.

Usage:
    python3 preprocess_markdown.py <input.md> <output.md>

Compatible with Python 3.9+.
"""

import os
import re
import sys
from typing import List, Optional, Tuple


# Box-drawing characters that identify an ASCII art table
BOX_CHARS = set("┌├└│─┬┼┴┐┤┘╔╠╚║═╦╬╩╗╣╝")


def strip_preamble(text: str) -> Tuple[str, bool]:
    """Remove all text before the first markdown heading (# ...).

    Returns:
        A tuple of (cleaned_text, was_stripped).
    """
    # Match the first line that starts with one or more '#' followed by a space
    match = re.search(r"^(#{1,6}\s)", text, re.MULTILINE)
    if match and match.start() > 0:
        return text[match.start():], True
    return text, False


def _has_box_drawing(text: str) -> bool:
    """Return True if text contains box-drawing characters."""
    return any(ch in BOX_CHARS for ch in text)


def _parse_ascii_table(block: str) -> Optional[List[List[str]]]:
    """Parse an ASCII art table block into rows of cells.

    Returns None if the block cannot be parsed as a table.
    Each inner list is a row of cell values (stripped).
    """
    lines = block.strip().splitlines()
    rows = []  # type: List[List[str]]

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Separator lines start with box-drawing corner/T characters
        first_char = stripped[0]
        if first_char in "┌├└╔╠╚":
            # This is a separator line -- skip it
            continue

        # Data lines start/end with vertical bars
        if first_char in "│║":
            # Split on the vertical bar character used
            bar = first_char
            # Remove leading and trailing bar
            inner = stripped
            if inner.startswith(bar):
                inner = inner[1:]
            if inner.endswith(bar) or inner.endswith("│") or inner.endswith("║"):
                inner = inner[:-1]

            # Split on any vertical bar character
            cells = re.split(r"[│║]", inner)
            cells = [c.strip() for c in cells]
            rows.append(cells)
        else:
            # Unexpected line format -- not a parseable table
            return None

    if len(rows) < 1:
        return None

    return rows


def _escape_pipe(value: str) -> str:
    """Escape pipe characters in cell content."""
    return value.replace("|", "\\|")


def _rows_to_markdown_table(rows: List[List[str]]) -> str:
    """Convert parsed rows into a markdown table string.

    The first row is treated as the header.
    """
    if not rows:
        return ""

    # Normalize column count to the max across all rows
    num_cols = max(len(r) for r in rows)
    normalized = []
    for r in rows:
        # Pad short rows, truncate long ones
        padded = r[:num_cols] + [""] * max(0, num_cols - len(r))
        normalized.append([_escape_pipe(c) for c in padded])

    lines = []

    # Header row
    header = normalized[0]
    lines.append("| " + " | ".join(header) + " |")

    # Separator row
    lines.append("| " + " | ".join(["---"] * num_cols) + " |")

    # Data rows
    for row in normalized[1:]:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def convert_ascii_tables(text: str) -> Tuple[str, int]:
    """Find fenced code blocks containing ASCII art tables and convert them.

    Uses a line-by-line state machine to handle code fences with inconsistent
    indentation between opening and closing markers.

    Returns:
        A tuple of (transformed_text, number_of_tables_converted).
    """
    tables_converted = 0
    lines = text.split("\n")
    result_lines = []  # type: List[str]

    # Regex to detect a fence line: optional whitespace + ``` + optional lang
    fence_open_re = re.compile(r"^(\s*)```(\S*)\s*$")
    fence_close_re = re.compile(r"^\s*```\s*$")

    i = 0
    while i < len(lines):
        open_match = fence_open_re.match(lines[i])
        if open_match:
            # Found an opening fence
            open_line_idx = i
            body_lines = []  # type: List[str]
            i += 1
            # Collect lines until closing fence
            while i < len(lines):
                if fence_close_re.match(lines[i]) and i > open_line_idx:
                    break
                body_lines.append(lines[i])
                i += 1

            close_line_idx = i
            body_text = "\n".join(body_lines)

            if _has_box_drawing(body_text):
                rows = _parse_ascii_table(body_text)
                if rows is not None:
                    md_table = _rows_to_markdown_table(rows)
                    tables_converted += 1
                    # Replace the entire fenced block with the markdown table
                    result_lines.extend(md_table.split("\n"))
                    # Skip past the closing fence
                    i = close_line_idx + 1
                    continue

            # Not converted -- preserve the fenced block as-is
            result_lines.append(lines[open_line_idx])
            result_lines.extend(body_lines)
            if close_line_idx < len(lines):
                result_lines.append(lines[close_line_idx])
            i = close_line_idx + 1
        else:
            result_lines.append(lines[i])
            i += 1

    return "\n".join(result_lines), tables_converted


def preprocess(input_path: str, output_path: str) -> None:
    """Run full preprocessing pipeline on a markdown file."""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: strip preamble
    content, preamble_stripped = strip_preamble(content)

    # Step 2: convert ASCII art tables
    content, tables_converted = convert_ascii_tables(content)

    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Print summary
    if preamble_stripped:
        print("Preamble: stripped (removed text before first heading)")
    else:
        print("Preamble: none detected (file already starts with heading)")

    print(f"ASCII art tables converted: {tables_converted}")
    print(f"Output written to: {output_path}")


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.md> <output.md>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isfile(input_path):
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    preprocess(input_path, output_path)


if __name__ == "__main__":
    main()
