# Connector qualification

Qualification is a measurable quality claim for an agent connector, computed only from artifacts already in the repo: readiness output, cassettes, the golden-questions report, the connector model, and the smoke-test config. It is separate from `x-airbyte-platform-availability`, which stays a human product decision.

The full design and the criteria tables live in [`docs/agent-connector-qualification.md`](../../../docs/agent-connector-qualification.md).

## Statuses

A connector declares its claim in `connector.yaml`:

```yaml
info:
  x-airbyte-qualification:
    status: candidate          # unverified | candidate | qualified
    criteria_version: v1
    bypassed_criteria:
      - criterion: C16
        reason: Not wired into the credentialed smoke suite yet
```

- `unverified` (or no block at all): not opted in, never blocks anything.
- `candidate` / `qualified`: the claim is re-verified by CI; a failing gate criterion fails the run unless it carries a documented bypass.

The status is a declaration of intent, not a stored verdict. `validate_connector_qualification` in [`qualification.py`](qualification.py) recomputes every criterion from the tree and returns a `QualificationResult` with per-criterion outcomes.

## Criteria

Criteria are grouped as C1..C17 (C13 was dropped as not measurable):

| Group | Criteria | Source |
| --- | --- | --- |
| A. Static definition | C1-C6 | `validate_connector_readiness` results |
| B. Auth parity | C7 | declared security schemes vs cassette coverage |
| C. Golden questions | C8-C12 | `tests/golden_questions_report.yaml` + freshness hash |
| D. Scope | C14-C15 | connector model, cassette map, smoke config |
| E. Live execution | C16-C17 | smoke-test config and live smoke results |

Each criterion is a **gate** (must pass) or a **warn** (reported only). A criterion that cannot be computed is reported as `UNEVALUATED` and never counts as passed. C17 is only evaluated when a live smoke result is plumbed in (the daily fleet workflow does this); a result that exists but cannot be parsed fails the gate.

Thresholds are named constants at the top of `qualification.py`, so the quality bar can be adjusted in one place.

## Running it

```bash
cd connector-sdk
uv run python -m airbyte_agent_sdk.cli validate qualification ../integrations/<name> [--json-output] [--report-only]
```

Exit code 1 means an opted-in connector failed a gate or its `connector.yaml` could not load. `--report-only` always exits 0 and just prints the report. The fleet runner is `integrations/scripts/run-all-qualifications.sh`.
