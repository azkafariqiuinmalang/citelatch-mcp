# Mendeley MCP setup — local metadata lookup

Status update 2026-10-28: installed; saved OAuth credentials, live library lookup,
and MCP stdio initialize/list_tools/search verified. Project config is enabled and
recognized by Codex CLI. Current chat tool catalog still needs a connection reload.
The later one-citation UI experiment is documented in test-results.md; human
manual signoff remains pending. Steps below describe setup on a new checkout;
do not duplicate a configuration that already exists.

Installed in `D:\MCP-MENDELEY\.venv`: mendeley-mcp 0.8.0.
This is a community library connector, not a Mendeley Cite insertion API.

## User action: API application and OAuth

1. Open https://dev.mendeley.com/myapps.html and sign in yourself.
2. Register an application using Authorization Code (not Legacy), with redirect
   URL exactly `http://localhost:8585/callback`. Use a descriptive name such as
   CiteLatch Local POC. Follow the portal's required fields; do not invent data.
3. Keep the Client ID and Client Secret private. Do not paste them into chat,
   config files, screenshots, or source control.
4. Open PowerShell yourself and run:

   ```powershell
   Set-Location -LiteralPath 'D:\MCP-MENDELEY'
   .\.venv\Scripts\python.exe .\harness\login_mendeley.py
   ```

5. Enter credentials at the interactive prompts. Secret input is hidden.
   Complete the official browser login and consent yourself.
   If consent is declined, stop; do not bypass authentication.

The helper reuses upstream OAuth while restricting the callback to 127.0.0.1,
checking the state parameter, requiring Windows keyring, setting a five-minute
callback timeout, and redacting token-exchange failures. It has local checks,
and saved credentials plus live library lookup were subsequently verified locally.
The upstream success page means the callback
was received; wait for terminal confirmation that token exchange/storage finished.
Do not use `mendeley-auth show-env`: it prints secrets.

Mendeley Authorization Code uses broad user API authorization. The Codex tool
allowlist restricts tools exposed to the agent; it does not make the OAuth token
itself read-only. Only metadata lookup is authorized for this project.

## Connect to Codex after login

The exact configuration section is in `mendeley-readonly.config.toml` beside this
document. Merge that section into your existing MCP configuration without
replacing unrelated settings. The original test workspace already activated this
project configuration; new checkouts must configure their own executable path.
Codex supports project-scoped `.codex/config.toml` for trusted projects and
user-scoped configuration. Restart the MCP connection after configuration.

Only four tools should be exposed: search library, get document, list documents,
and list folders. Do not enable add/update/delete, global catalog, or PDF tools.
Ask the agent to verify one library record after connection. A tool listing or
installed package alone does not establish successful authentication.

## Sources checked 2026-10-28

- https://github.com/pallaprolus/mendeley-mcp
- https://dev.mendeley.com/reference/topics/authorization_overview.html
- https://learn.chatgpt.com/docs/extend/mcp

Rollback: remove only the added MCP section to disconnect. Revoke the application's
authorization through Mendeley's account controls if desired. Never delete or
overwrite the user's Word document; no Word insertion is part of this setup.
