---
name: md2gdoc
description: Convert a markdown file to a styled Google Doc using any template. Auto-generates template structure from a Google Doc URL, fits content into the template sections, handles table borders, code block backgrounds, heading styles, and uploads to Google Drive. Invoked with /md2gdoc.
---

# Markdown to Google Doc Skill

Convert markdown files to professionally styled Google Docs using customizable templates. The skill auto-generates a template skeleton from any Google Doc URL, fits user content into the template's section structure, and applies proper styling.

## Prerequisites

- `pandoc` must be installed: `brew install pandoc`
- **Python venv** must be set up (one-time):

```bash
SKILL_DIR="$HOME/.claude/skills/md2gdoc"
python3.13 -m venv "${SKILL_DIR}/.venv"
"${SKILL_DIR}/.venv/bin/pip" install -r "${SKILL_DIR}/requirements.txt"
```

- **`.env` file** must exist at `~/.claude/skills/md2gdoc/.env` with Google OAuth credentials (copy from `.env.example`)

## Base directory

```
~/.claude/skills/md2gdoc/
  SKILL.md
  requirements.txt           # Python deps (python-docx, airbyte-agent-google-drive)
  .env                       # Google OAuth credentials (not committed)
  .env.example               # Template for .env
  .venv/                     # Python 3.13 virtual environment
  scripts/
    gdrive_auth.py           # shared Google Drive auth helper
    preprocess_markdown.py   # strips preamble + converts ASCII art tables
    generate_template.py     # auto-generates skeleton from a .docx
    fit_to_template.py       # maps user content into any template structure
    postprocess_docx.py      # python-docx post-processor
    gdrive_utils.py          # upload-docx, get-doc-url, get-access-token, set-pageless
  templates/                 # populated on first use (cached per template)
    <template-name>/
      reference.docx         # pandoc style reference
      skeleton.md            # auto-generated template with {{PLACEHOLDER}} tokens
```

## Instructions

When the user invokes this skill, follow these steps:

### Step 0: Parse user input

The user provides:
1. **A markdown file path** (required) - local path to the `.md` file
2. **A template** (optional): one of:
   - A Google Doc URL to use as template (e.g., `https://docs.google.com/document/d/.../edit`)
   - A cached template name (e.g., `my-tech-spec`)
   - Nothing — prompt the user to provide a Google Doc URL or choose a cached template
3. **A Google Drive folder** (optional) - where to upload (defaults to root `/`)

Before running the pipeline, use **AskUserQuestion** to confirm/collect:
- **Title**: auto-detected from the first H1 heading in the user's markdown. Ask the user to confirm or override.
- **Status**: defaults to "Draft". Ask the user to confirm or choose another status.
- **Template**: If not specified, list cached templates from `~/.claude/skills/md2gdoc/templates/` and ask the user to choose one or provide a new Google Doc URL.

The following are auto-filled with smart defaults (no need to ask):
- **Author**: from `git config user.name`
- **Created / Last Updated**: today's date

### Step 0.5: Template setup

Check if the template exists in the cache:

```bash
SKILL_DIR="$HOME/.claude/skills/md2gdoc"
TEMPLATE_NAME="<name>"
TEMPLATE_DIR="${SKILL_DIR}/templates/${TEMPLATE_NAME}"

if [ -f "${TEMPLATE_DIR}/skeleton.md" ] && [ -f "${TEMPLATE_DIR}/reference.docx" ]; then
    echo "Template '${TEMPLATE_NAME}' found in cache"
fi
```

**If template needs generation** (user provided a Google Doc URL):

1. Extract the file ID from the URL (the part between `/d/` and `/edit`)
2. Run the generator:

```bash
"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/generate_template.py" \
  "<FILE_ID>" \
  "<TEMPLATE_NAME>" \
  --download
```

3. Report the generated skeleton structure to the user (headings found, placeholders created) for confirmation before proceeding.

**If template is already cached**: proceed directly to Step 1.

### Step 1: Pre-process the markdown

```bash
SKILL_DIR="$HOME/.claude/skills/md2gdoc"
TEMP_DIR="/tmp/md2gdoc/work"
mkdir -p "$TEMP_DIR"

"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/preprocess_markdown.py" \
  "$INPUT_MD" \
  "${TEMP_DIR}/${BASENAME}_clean.md"
```

The pre-processor does two things:
1. **Strips non-content preamble** — removes text before the first markdown heading (e.g. local repo paths, personal notes)
2. **Converts ASCII art tables** — box-drawing character tables (`┌─┬─┐`, `│`, `├─┼─┤`) inside code fences are converted to standard markdown tables (`| col | col |`). Other code blocks (YAML, bash, text) are preserved as-is.

### Step 2: Fit content to the template

```bash
SKILL_DIR="$HOME/.claude/skills/md2gdoc"
TEMPLATE_DIR="${SKILL_DIR}/templates/${TEMPLATE_NAME}"
TEMP_DIR="/tmp/md2gdoc/work"

"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/fit_to_template.py" \
  "${TEMP_DIR}/${BASENAME}_clean.md" \
  "${TEMPLATE_DIR}/skeleton.md" \
  "${TEMP_DIR}/${BASENAME}_templated.md" \
  --title "User-confirmed title" \
  --status "User-confirmed status"
```

This step maps the user's markdown sections into the template structure:

**Section mapping** (auto-derived from skeleton headings):
- Keywords are generated from each skeleton heading text (full text, sub-phrases, significant words)
- User headings are matched via case-insensitive substring match against these keywords
- Only H1/H2 headings are used for section matching; H3+ stay as sub-sections within their parent

**Behavior**:
- The first H1 heading is treated as the document title (used for metadata, not mapped)
- Unmapped sections are appended at a logical insertion point in the template (after the main content section)
- When multiple sections map to the same placeholder, subsequent headings are preserved as H3 sub-headings
- All template sections are always present, even if empty
- Code blocks are properly handled (headings inside code fences are ignored)

**Low mapping rate**: If fewer than 50% of template sections are mapped, the user's document structure likely doesn't align well with the template. In this case:
1. Show the user which sections mapped and which didn't
2. Ask if they want to proceed as-is (unmapped content gets appended) or manually specify which of their sections should map to which template placeholders
3. If the user provides manual mappings, edit the templated markdown accordingly before proceeding to Step 3

**Custom metadata**: Use `--meta KEY VALUE` to pass arbitrary metadata that matches any `{{PLACEHOLDER}}` in the skeleton.

### Step 3: Convert markdown to docx with pandoc

```bash
REFERENCE_DOC="${TEMPLATE_DIR}/reference.docx"

pandoc "${TEMP_DIR}/${BASENAME}_templated.md" \
  --reference-doc="$REFERENCE_DOC" \
  --wrap=none \
  -o "${TEMP_DIR}/${BASENAME}_pandoc.docx"
```

The `--reference-doc` flag pulls base styles (fonts, heading sizes, spacing) from the template.

### Step 4: Post-process the docx with python-docx

```bash
"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/postprocess_docx.py" \
  "${TEMP_DIR}/${BASENAME}_pandoc.docx" \
  "${TEMP_DIR}/${BASENAME}.docx"
```

The post-processor fixes issues that pandoc/Google Docs import doesn't handle:
- **Table full width**: Stretches all tables to 100% page width (pandoc defaults to auto-sized narrow tables)
- **Table borders**: Adds solid black borders to all table cells
- **Header row shading**: Gray background (#D9D9D9) + bold text on first row
- **Table cell font**: Arial 10pt for all cells
- **Code blocks**: Gray background (#F3F3F3), Roboto Mono 9pt, dark gray text (#37474F), indentation
- **Heading hierarchy**: H1=20pt black, H2=16pt black, H3=14pt #434343, H4=12pt #666666, H5/H6=11pt bold #666666
- **Paragraph spacing**: Body text 8pt after + 1.15 line height, list items 2pt after + 1.15 line height, code blocks 8pt before/after group

### Step 5: Upload to Google Drive and get the URL

Upload the .docx to Google Drive using the connector. The file is automatically converted to a native Google Doc on upload. The script prints the Google Docs edit URL to stdout.

```bash
"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/gdrive_utils.py" upload-docx "${TEMP_DIR}/${BASENAME}.docx" "${GDRIVE_FOLDER}"
```

If `GDRIVE_FOLDER` is empty or `/`, omit the folder argument to upload to the Drive root:

```bash
"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/gdrive_utils.py" upload-docx "${TEMP_DIR}/${BASENAME}.docx"
```

Capture the output as `DOC_URL` and extract the `FILE_ID` from the URL path (the segment between `/d/` and `/edit`).

Return the URL to the user.

**Note:** The folder path is slash-separated (e.g., `"Tech Specs/Q1 2026"`) and each segment is resolved by name. The upload uses the Drive v3 multipart upload API with conversion to native Google Docs format.

### Step 6: Switch to Pageless mode

Switch the Google Doc to Pageless mode for a clean white background (removes the default page border/tint).

**Option A — Google Docs API (preferred, requires Docs API enabled):**

If the GCP project behind the `.env` OAuth credentials has the Google Docs API enabled (not just Drive API), use the helper script:

```bash
"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/gdrive_utils.py" set-pageless "${FILE_ID}"
```

If the script exits with code 2, the Docs API is not enabled for this OAuth project — fall back to Option B or C.

**Note:** The GCP project behind the `.env` OAuth credentials must have both the Drive API and Docs API enabled for this option to work.

**Option B — Chrome MCP tools (fallback):**

If the Claude in Chrome MCP tools are available, open the Google Doc URL and click through:

1. Navigate to the Google Doc URL
2. Click **File** menu
3. Click **Page setup**
4. Click the **Pageless** tab
5. Click **OK**

**Option C — Manual:**

If neither option is available, tell the user they can switch to Pageless mode via **File → Page setup → Pageless** for a cleaner look.

### Step 7: Evaluate the output

If the Claude in Chrome MCP tools are available, open the Google Doc URL and run through the quality checklist below. If the plugin is not connected, inform the user that installing the [Claude in Chrome extension](https://claude.ai/chrome) is recommended for automated QA evaluation, and provide the Google Doc URL so they can review manually.

| Check | What to verify |
|-------|---------------|
| **Metadata block** | Author, Created date, Last Updated date, and Status are present and correct |
| **Heading hierarchy** | H1 → H2 → H3 structure follows the template |
| **Table borders** | All tables have visible black borders and gray header rows |
| **Code blocks** | Gray background, monospace font, readable text |
| **Content completeness** | No user content was dropped — compare section count against the pre-processed markdown |
| **No artifacts** | No leftover `{{PLACEHOLDER}}` tokens, no `__CODE_BLOCK_N__` markers |
| **Section ordering** | Template sections appear in the correct order, unmapped content sits at the insertion point |

Report each check as **pass** / **warn** / **fail**. If any check fails, suggest whether the fix is:
- **Automated** — a bug in the pipeline scripts that should be fixed
- **Manual** — something the user should adjust in the Google Doc directly (e.g., images, custom formatting)

## Template management

### Listing cached templates

```bash
ls ~/.claude/skills/md2gdoc/templates/
```

### Creating a template from a Google Doc

Provide a Google Doc URL when invoking the skill, or run the generator directly:

```bash
SKILL_DIR="$HOME/.claude/skills/md2gdoc"
"${SKILL_DIR}/.venv/bin/python3" "${SKILL_DIR}/scripts/generate_template.py" \
  "<GOOGLE_DOC_FILE_ID>" \
  "my-template" \
  --download
```

### How auto-generation works

The generator parses the .docx to extract:
1. **Metadata fields**: Lines before the first heading that match `Key: Value` patterns (e.g., `Author:`, `Status:`)
2. **Heading structure**: All headings (H1-H6) with their hierarchy levels

For each heading, it creates a `{{PLACEHOLDER}}` token using UPPER_SNAKE_CASE of the heading text (e.g., "Data Protection Considerations" → `{{DATA_PROTECTION_CONSIDERATIONS}}`).

The skeleton is then used by `fit_to_template.py` to match user content to template sections via fuzzy keyword matching derived from the heading text.

## Pipeline summary

```
┌──────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐     ┌─────────────┐
│ Markdown     │────▶│ Fit to       │────▶│ pandoc          │────▶│ python-docx      │────▶│ Drive API   │
│ (pre-process │     │ template     │     │ --reference-doc │     │ post-processor   │     │ upload +    │
│  ASCII tables│     │ (section map │     │ (base styles)   │     │ (borders, code   │     │ convert to  │
│  → md tables)│     │  + metadata) │     │                 │     │  blocks, heads)  │     │ Google Doc  │
└──────────────┘     └──────────────┘     └─────────────────┘     └──────────────────┘     └─────────────┘
```

## Styling reference

| Element | Style |
|---------|-------|
| Body text | Arial 11pt, black |
| H1 | Arial 20pt, black |
| H2 | Arial 16pt, black |
| H3 | Arial 14pt, #434343 |
| H4 | Arial 12pt, #666666 |
| Bold | Arial 11pt, bold |
| Tables | Black borders, gray header row (#D9D9D9), Arial 10pt |
| Code blocks | Roboto Mono 9pt, #37474F text, #F3F3F3 background |
| Page | max-width 468pt, 72pt padding |

## Known limitations

1. **No syntax highlighting** in code blocks - Google Docs doesn't support it natively; code renders as uniform dark gray monospace
2. **H5/H6 headings** render small - these are uncommon in tech specs; consider using H3/H4 instead
3. **Images** in markdown are not handled - add them manually in Google Docs after upload
4. **No Title block** - the template has a Title style (26pt) but pandoc doesn't generate it from `# H1`; if the user wants a proper title, they should add metadata at the top of their markdown
5. **Template generation** depends on the .docx having consistent heading styles. Documents with custom styles or non-standard heading names may need manual skeleton adjustment.

## Example usage

**User:** `/md2gdoc /path/to/my-spec.md`

**Claude:** Asks which template to use (or use cached), confirms title and status, then runs the full pipeline and returns the Google Doc URL.

**User:** `/md2gdoc /path/to/my-spec.md "Tech Specs/Q1 2026"`

**Claude:** Uploads to the specified Google Drive folder.

**User:** `/md2gdoc /path/to/my-spec.md --template https://docs.google.com/document/d/1ABC.../edit`

**Claude:** Downloads the Google Doc as a template, generates the skeleton, caches it, then converts the markdown.
