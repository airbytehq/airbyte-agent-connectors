# Risks and Mitigation

## 1. Format Drift

**Risk:** Connector SDK changes the auto-generated README structure,
breaking the parser.

**Mitigation:**
- `validate_readme_structure()` raises a clear `ValueError` naming the
  connector and missing section.
- Unit tests simulate format changes to ensure the error path works.
- Critical sections (Installation, Usage) cause hard failures; optional
  sections produce warnings.

## 2. Large REFERENCE.md Files

**Risk:** Some connectors may have thousands of lines of response schemas
in `<details>` blocks, inflating generated references.

**Mitigation:**
- `<details>` blocks are stripped entirely from REFERENCE.md content.
- Only parameter tables and SDK code examples are preserved.
- Target per-connector reference size is 100-300 lines.

## 3. CI Permissions for PR Creation

**Risk:** The `peter-evans/create-pull-request` action requires
`contents: write` and `pull-requests: write` permissions.

**Mitigation:**
- The workflow uses the default `GITHUB_TOKEN`, which has these
  permissions when configured in the workflow's `permissions` block.
- The workflow creates a PR for human review rather than committing
  directly to main.
- Branch auto-deletion is enabled to avoid stale branches.

## 4. Version Sync

**Risk:** Running the generator locally may produce references with
versions that don't match the latest published packages.

**Mitigation:**
- In CI (Phase 2), the generator runs after publish, so versions are
  always current.
- Generated files include the version source in the header comment.
- A future enhancement could compare local vs. published versions and
  warn.

## 5. Cross-Repo Sync

**Risk:** If skills are consumed from a separate public skills repo,
the connector repo's `skills/` directory must be synced.

**Mitigation:**
- Keep `skills/` in the connector repo as canonical.
- Document a subtree-push or CI sync procedure in the README.
- Do not attempt to automate cross-repo sync in the initial
  implementation.
