# generate_skill_references.py

Auto-generates per-connector reference docs and a connector index for
`skills/airbyte-agent-connectors/`.

## Prerequisites

- Python 3.11+ (uses `tomllib` from stdlib)
- No external dependencies required

## Usage

```bash
# Generate everything
python scripts/generate_skill_references.py --all

# Generate specific connector(s) and rebuild index
python scripts/generate_skill_references.py --connector stripe gong

# Dry run (writes to temp dir, prints summary)
python scripts/generate_skill_references.py --all --dry-run

# Output to custom directory
python scripts/generate_skill_references.py --all --output-dir /tmp/skill-preview

# Validate no drift between generated and committed files
python scripts/generate_skill_references.py --check

# Verbose logging
python scripts/generate_skill_references.py --all -v
```

## Running Tests

```bash
python -m pytest tests/test_generate_skill_references.py -v
```

Tests use `tmp_path` fixtures and never touch the repo's `skills/` directory.

## What It Generates

```
skills/airbyte-agent-connectors/
  SKILL.md                              # Slim summary (<= 500 lines)
  references/
    connector-index.md                  # Full table of all connectors
    connectors/
      stripe.md                         # Per-connector reference
      hubspot.md
      ...
```

## How It Works

1. Scans `connectors/*/pyproject.toml` to discover connectors.
2. Parses each connector's `README.md` (required), `AUTH.md`, and
   `REFERENCE.md` (optional).
3. Generates a structured reference file per connector.
4. Rebuilds the full connector index on every run.
5. Generates a slim `SKILL.md` linking to the index.

## CI Integration

### Phase 1 (Manual)

Run locally, review outputs, commit to repo.

### Phase 2 (Automated)

The `.github/workflows/generate-skills.yml` workflow:
- Triggers on changes to connector doc files on `main`.
- Regenerates all references.
- Opens a PR via `peter-evans/create-pull-request` if files changed.
- Requires a `GITHUB_TOKEN` with `contents: write` and
  `pull-requests: write` permissions (default for GitHub Actions).

### Option B (Post-Publish)

Run the generator as a step in the publish workflow after packages are
published, so versions in references stay in sync.

## What to Watch for in Review

- **Format drift**: If connector READMEs change their section structure,
  the generator will raise `ValueError` for missing critical sections
  (Installation, Usage) or log warnings for optional ones.
- **Large files**: `<details>` blocks from REFERENCE.md are stripped.
  Check that parameter tables and SDK examples survive.
- **Version accuracy**: Versions come from `pyproject.toml`. If running
  locally, the version may not match the latest published version.

## Risks and Mitigation

See [RISKS.md](RISKS.md) in this directory.
