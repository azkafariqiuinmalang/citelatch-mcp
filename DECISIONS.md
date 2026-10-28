# DECISIONS.md — CiteLatch MCP Decision Log

**Document status:** Initial baseline. **Updated:** 2026-10-28.

This file records **architecture/product decisions**, not evidence that a capability works. Decisions marked *provisional* must be revisited if discovery or experiments contradict them. Add new entries rather than silently rewriting historical decisions.

## DEC-001 — Reuse Codex as the AI agent

- **Date:** 2026-10-28
- **Status:** Accepted (project direction)
- **Decision:** Develop a specialized MCP server for citation integration, consumed by Codex or a compatible agent. Do not build a new general LLM-based writing agent.
- **Alternatives:** Standalone AI writing application; full custom agent.
- **Reason:** The user's need is to bind existing Word citations to real Mendeley Cite citations, not to generate academic articles.
- **Evidence:** User-approved product direction in `PROJECT_CONTEXT.md`; **not** an implementation test.
- **Revisit if:** MCP constraints make the desired workflow infeasible.

## DEC-002 — Source of truth for reference identity

- **Date:** 2026-10-28
- **Status:** Accepted (safety requirement)
- **Decision:** Reference identity must be resolved to an existing user's Mendeley library record, with provenance. The LLM must never fabricate bibliographic data or substitute loosely related sources.
- **Alternatives:** LLM-generated author-year strings; unrestricted catalog searches.
- **Reason:** Reduce hallucinated/wrong citations and support human review for ambiguity.
- **Evidence:** User problem statement and `SECURITY_AND_CITATION_POLICY.md`.
- **Revisit if:** User explicitly authorizes new-library imports in a future scope expansion.

## DEC-003 — Definition of native, active citation

- **Date:** 2026-10-28
- **Status:** Accepted (acceptance gate)
- **Decision:** A citation counts as **active** only if the official Mendeley Cite add-in can recognize and edit it after Word save/close/reopen. Style changes and bibliography refresh must work for the final full workflow.
- **Alternatives:** Plain text, built-in Word `CITATION` fields, legacy Mendeley Desktop fields.
- **Reason:** Visible author-year text alone does not meet the user's goal.
- **Evidence:** `ACCEPTANCE_TESTS.md`; no working POC yet.
- **Revisit if:** User later changes the product goal.

## DEC-004 — Active insertion mechanism

- **Date:** 2026-10-28
- **Status:** **OPEN — no technical decision made**
- **Candidates:** (A) supported first-party insertion API if documented; (B) visible Word + Mendeley Cite UI Automation; (C) research-only OOXML approach.
- **Decision needed:** After `harness/discovery.md` captures versions, documented capabilities, and one-citation feasibility evidence.
- **Safeguard:** Never treat undocumented OOXML structures as a supported public API; never claim the feature passes until the official add-in can edit the result.

## DEC-005 — Data safety and operating assumptions

- **Date:** 2026-10-28
- **Status:** Provisional design defaults
- **Decision:** Single-user Windows desktop POC, read-only discovery by default, consent before any user-facing automation, new output file rather than overwrite, redact credentials and document contents from logs.
- **Alternatives:** Cloud-hosted service, silent bulk editing, in-place edits.
- **Reason:** Limit destructive effects and UI automation complexity during feasibility testing.
- **Evidence:** `PROJECT_CONTEXT.md` and `SECURITY_AND_CITATION_POLICY.md`.
- **Revisit if:** User confirms a different environment or workflow.

## DEC-006 — Isolated Mendeley connector setup

- **Date:** 2026-10-28
- **Status:** Setup complete; live authentication unverified
- **Decision:** Install `mendeley-mcp==0.8.0` in project `.venv`; prepare four metadata tools in a config template, not active configuration. Reuse upstream OAuth with a version-pinned wrapper requiring Windows keyring, loopback callback and state validation.
- **Reason/evidence:** User requested continuation. Installation and pip check passed. Inspected upstream binds callback to all interfaces and does not validate state in callback handler. Five local callback checks and config/tool-name checks passed; live OAuth not tested.
- **Alternatives:** Global install or unrestricted connector.
- **Rollback:** Remove added MCP section if activated; revoke authorization through Mendeley if desired. Review wrapper on package upgrades. Token scope is broad; tool allowlist is not OAuth scope restriction.

## Entry template

## DEC-007 — One-citation UI POC outcome

- **Date:** 2026-10-28
- **Status:** Technical observation accepted; human manual validation pending
- **Decision:** Visible Word + modern Mendeley Cite is a feasible candidate for
  further controlled work on this exact setup. No production adapter selected.
- **Evidence:** `harness/test-results.md`; synthetic output survived two document
  reopen cycles, official Edit citation recognition, APA/Vancouver style changes,
  and bibliography rerender. Original hash unchanged.
- **Alternatives:** Public insertion API unverified; OOXML injection not used.
- **Risk:** UI timing/handles and dialogs required recovery; no batch guarantee.
- **Rollback:** Retain baseline; discard test output if manual validation fails.
  No original document or library record needs restoration.


```markdown
## DEC-XXX — Short decision title
- **Date:** YYYY-MM-DD
- **Status:** Proposed / Accepted / Superseded / Rejected / Open
- **Decision:** ...
- **Alternatives:** ...
- **Reason:** ...
- **Evidence:** Test output, documentation URL/version, or user instruction
- **Rollback / revisit trigger:** ...
- **Approved by:** ...
```

> Log a decision only after evidence or user confirmation. Do not write "tested", "supported", or "done" without the corresponding real-world result.
