# Implementation Plan — Proof before features

**Rule:** Jangan melanjutkan ke tahap berikutnya tanpa exit criteria fase sebelumnya. Semua perkiraan effort hanya setelah environment discovery; tidak ada janji berhasil sebelum POC.

## Phase 0 — Environment & feasibility discovery (READ-ONLY)
**Tasks**
- Identifikasi Windows edition, Word desktop version, Office architecture, Mendeley Cite add-in version & login, Mendeley cloud sync, Python/.NET/Codex availability.
- Periksa dokumentasi terbaru proyek `pallaprolus/mendeley-mcp` dan `trsdn/mcp-server-word`; hindari asumsi nama executable/tool yang kedaluwarsa.
- Uji akses read-only Mendeley MCP; WordMcp pada **dokumen sintetik**.
- Tinjau mekanisme insersi native: supported Mendeley Cite API vs UI Automation vs OOXML research; record source and limitations.
- Buat matriks risiko, compatibility list, `harness/discovery.md`.
**Exit:** sekurangnya dapat menemukan satu referensi di Mendeley dan membaca satu dokumen uji. Jika akun/tools belum siap, status `blocked`, berikan langkah setup aman.

## Phase 1 — Deterministic document citation inspection
**Tasks**
- Deteksi sitasi plain text author-year secara konservatif; preserve document structure.
- Tandai existing Mendeley Cite controls dan bentuk lain (Word native, old Mendeley) bila bisa; hindari double-conversion.
- Deteksi sitasi dalam footnotes/tables dan tracked changes sebagai warnings, bukan auto-modify.
- Kembangkan fixtures sintetik dan unit tests.
**Exit:** laporan sitasi lokasi/teks, tidak ada perubahan pada file asli.

## Phase 2 — Library lookup & mapping (read-only)
**Tasks**
- Implement adapter search Mendeley ID via existing MCP/API.
- Strategi match DOI > normalized title+authors+year > manual review.
- Modelkan multi-citation clusters dan `no_match`, `ambiguous`, `matched`.
- Tampilkan dry-run mapping dengan alasan dan audit.
**Exit:** satu sitasi uji dipasangkan ke reference ID nyata tanpa menebak identitas.

## Phase 3 — **Critical Gate: one native active citation POC**
**Tasks**
- Buat disposable `.docx` dari fixture, backup dan log.
- Dengan WordMcp tertutup, gunakan opsi insertion yang telah disetujui untuk menambahkan **satu** sitasi melalui Mendeley Cite resmi (atau metode lain yang terbukti kompatibel).
- Save → close → reopen. Klik/edit sitasi **di Mendeley Cite**, ubah style, simpan dan reopen lagi.
- Buat catatan versi Office/add-in, interaksi, kegagalan dan bukti.
**GO:** sitasi edit-able dan style berubah dari Mendeley Cite. **NO-GO:** hanya tampak `(Author, Year)`, UI tak dapat diotomasi, atau sitasi jadi corrupt. Stop dan lakukan technical decision review. Jangan mengklaim fiturnya sudah selesai.

## Phase 4 — Citation Bridge MCP service
**Prereq:** POC Phase 3 GO.
**Tasks**
- MCP server stdio, tool schemas dari `ARCHITECTURE.md`, guardrails & consent.
- File working-copy, hashes, journal, retry/idempotency, structured result.
- Adapter insertion dipisah dari library/Word; serialize Word access.
- Tests: mocks, timeout, stale doc, wrong ID, ambiguous, duplicate insert, crash recovery.
**Exit:** Codex dapat minta insert dan mendapat hasil sukses/gagal yang jujur dalam test fixture.

## Phase 5 — Bibliography, batch, usability
**Prereq:** 1 citation E2E and MCP tool integration PASS.
**Tasks**
- Two citations; multi-citation cluster; insert/update bibliography through add-in.
- Change APA ↔ Vancouver via Mendeley Cite dan verifikasi rerender.
- Support review queue, selective approval, output-only save, documentation.
**Exit:** acceptance criteria P1 pass on versions supported and failure cases documented.

## Phase 6 — Polish / distribution (optional)
- Packaging/installer, compatibility guide, release CI unit tests, manual Windows E2E protocol.
- No public release claim until native editability and file-safety tests are consistently proven.

## Tracking template
For each phase maintain: `goal`, `environment`, `decision`, `source`, `implementation`, `tests_run`, `actual_results`, `blockers`, `user_approval`, `next_step`.

## First coding-agent assignment
**Do Phase 0 only**. Return a discovery summary, feasibility options, a smallest POC proposal, and the blockers to resolve. Do not install software or modify private files without permission.
