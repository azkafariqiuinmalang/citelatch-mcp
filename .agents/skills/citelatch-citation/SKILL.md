---
name: citelatch-citation
description: Workflow for safely mapping existing Microsoft Word citations to verified Mendeley library records and, only after feasibility is proven, inserting native editable Mendeley Cite citations.
---

# CiteLatch Citation Workflow (Draft)

> This is an instruction skill. It does **not** implement MCP tools or confer ability to control Mendeley Cite. Use only available, verified tools.

## When to use
The user has an existing `.docx` document with textual citations and asks to connect, convert, validate, or refresh those citations through Mendeley Cite.

## Workflow
1. Read `PROJECT_CONTEXT.md`, `AGENTS.md`, `SECURITY_AND_CITATION_POLICY.md`.
2. Inspect document read-only, distinguishing plain text, Word-native citation fields, and modern Mendeley Cite controls. Flag uncertain formats.
3. Find candidate matching records **in Mendeley library**. Preserve original reference IDs, DOI, title, author, year and source of evidence.
4. Mark matches as `matched`, `ambiguous` or `not_found`; no fabricated references. Seek user review for ambiguity.
5. Generate dry-run manifest and proposed changes. Do not touch original.
6. Only with approval and proven insertion adapter: insert on working copy with unique idempotency key.
7. Confirm official Mendeley Cite editability after save/close/reopen; test style change & bibliography if requested.
8. If insertion unavailable, report `FEASIBILITY_BLOCKED`. **Never silently downgrade to plain text.**
9. Return output path plus per-citation evidence and limitations.

## Forbidden shortcuts
- Treating a formatted author-year string as active citation.
- Treating Word's built-in CITATION field as Mendeley Cite.
- Looking up paper identity solely from LLM knowledge.
- Hiding incomplete validations or overwriting original document.
