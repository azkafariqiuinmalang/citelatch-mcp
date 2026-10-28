# One-citation POC — 2026-10-28

Status: **TECHNICAL_POC_OBSERVED / HUMAN_MANUAL_SIGNOFF_PENDING**.
This is a controlled UI experiment, not a completed production feature or a new
Citation Bridge MCP implementation.

## Environment and authorization

- Word desktop x64 `16.0.20527.20088`; Mendeley Cite version announcement displayed
  `1.69.4`. Legacy Cite-O-Matic also present but not used.
- User explicitly requested `lanjut POC satu sitasi`, following authorization for
  Word automation and a separate disposable document.
- No WordMcp background session used. User's original document remained open;
  only the separate test document was edited and closed/reopened.
- Mendeley library lookup used installed authenticated community connector client,
  because the current chat still did not expose direct Mendeley tools. No library
  mutations or PDF downloads.

## Artifacts

- `outputs/poc-one-citation/before.docx`: synthetic paragraph baseline.
- `outputs/poc-one-citation/after.docx`: one active citation plus add-in bibliography.
- `outputs/poc-one-citation/citation_manifest.json`: private exact reference mapping,
  provenance, hashes and per-check observations. All are under ignored outputs/.
- Baseline SHA256: `5a525158f3f18d4eb6cee709101d3b8c879125ba1a62e52e6f02e9273eb5cfac`.
- Final saved SHA256 before second reopen:
  `536f2ed06267914f84f74c1a8b296c9f15d360323102c33765656cfbbde3c75d`.

## Observed checks

| Check | Result | Evidence |
|---|---|---|
| Read synthetic baseline | PASS | Saved package read without modification; expected text found |
| Real library identity | PASS for technical fixture | Authenticated search returned record ID, title, author and year; exact title matched in official pane |
| One native citation insertion (T08) | Observed PASS | Clicked Insert citation in modern official Mendeley Cite, not legacy/built-in Word |
| Editability after save/close/reopen (T09) | Observed PASS twice | Selected saved citation and opened official Edit citation screen, Currently citing Ayu Kusuma 2019 |
| Style change (T10) | Observed PASS | Official APA 7 -> NLM/Vancouver changed author-year to (1); switched back to APA 7 |
| Bibliography (T11) | Observed PASS | Official Insert Bibliography created one entry; return to APA rerendered the entry |
| Original file safety | PASS | Original SHA256 equals initial scan `a0d661bcf659914dde68051996ba4e0ec64b4799f4ddafd514354ade77422e13` |
| Non-citation text safety | PASS for fixture text | Baseline paragraph preserved as prefix of final paragraph |
| Duplicate count | PASS for resulting fixture | Exactly one citation control and one bibliography control in saved package |
| Human manual signoff | PENDING | User must confirm official pane editability; feature not declared done |

Package markers and embedded record identity were supplementary evidence only;
editability was observed in the official UI. No OOXML injection was performed.

## Limitations and failures

- The full WINWORD process was not terminated, because the original article was
  open. The disposable document was closed and reopened twice.
- Bibliography did not appear on the first attempt. Read-only package inspection
  confirmed absence before one retry; retry succeeded with fully visible dialog
  controls. No silent fallback or duplicate insertion was used.
- One screenshot handle became invalid and a subsequent capture showed another
  foreground app. Input stopped; target window was reselected and activated before
  continuing. This demonstrates UI fragility; no unattended/batch guarantee.
- Accessibility snapshots sometimes lagged visible focus. No raw taskpane URL,
  credential, or screenshot has been saved in this report. Screenshots were
  inspected live; there is no persisted screenshot evidence for independent audit.
- Library metadata has a suspicious ISSN resembling a date range. No metadata was
  invented or corrected. Plain-text extraction of generated bibliography also
  included a replacement glyph; visual output showed the entry. Bibliographic
  correctness beyond the returned library identity remains unverified.
- Not tested: automated idempotent retries, crash recovery, complex formatting,
  tracked changes, multiple citations, arbitrary documents, or scientific support
  for the original article's claim. No production insertion adapter implemented.

## Next action

User manually opens after.docx, selects the citation and confirms that official
Mendeley Cite can edit it. Keep the original article untouched. Only after this
signoff should the project gate be reviewed for further implementation; this
experiment does not authorize batch edits or changes to the original article.
