# Phase 0 Discovery — CiteLatch MCP

**State:** `IN_PROGRESS / BLOCKED_FOR_INTEGRATION` — pemeriksaan read-only awal dilakukan 2026-10-28. Bagian template di bawah dipertahankan sebagai checklist; hasil observasi aktual ada di bagian 8 dan mengesampingkan nilai template yang belum diisi.

**Date opened:** 2026-10-28 (Asia/Jakarta)
**Operator / AI agent:** Codex desktop, sesi lokal workspace D:\MCP-MENDELEY
**Scope:** Read-only discovery and feasibility research, not automatic editing.

## 1. Runtime environment (record after observation)

| Item | Observed value | Status / evidence |
|---|---|---|
| Host OS and build | Unknown | `NOT_TESTED` |
| Local Codex CLI/IDE/cloud and version | Unknown | `NOT_TESTED` |
| Microsoft Word desktop version/build/bitness | Unknown | `NOT_TESTED` |
| Mendeley Cite add-in version | Unknown | `NOT_TESTED` |
| Mendeley Cite logged in? | Unknown | `NOT_TESTED` |
| Library synced and available? | Unknown | `NOT_TESTED` |
| Mendeley MCP repo/commit/entrypoint | Unknown | `NOT_TESTED` |
| Word MCP repo/commit/entrypoint | Unknown | `NOT_TESTED` |
| Python / .NET versions | Unknown | `NOT_TESTED` |
| Windows UI Automation accessibility | Unknown | `NOT_TESTED` |

**Privacy:** Never record passwords, client secrets, access tokens, private PDF content, private document text, user addresses, or screenshots containing personal data.

## 2. Documentary evidence register

Record sources that were personally inspected during Phase 0, using exact URL/version/access date. **Links mentioned in `README.md` are research starting points, not tested claims.**

| ID | Claim under examination | Source URL/version/date | What source actually confirms | Confidence |
|---|---|---|---|---|
| E01 | Does Mendeley Cite expose a documented insertion/write API? | Not yet reviewed | None | `UNKNOWN` |
| E02 | Can official add-in create/edit a citation on this setup? | Not yet reviewed | None | `UNKNOWN` |
| E03 | Does a Mendeley library MCP work read-only on this setup? | Not yet reviewed | None | `UNKNOWN` |
| E04 | Does Word MCP support safe document inspection here? | Not yet reviewed | None | `UNKNOWN` |
| E05 | Can Windows UI Automation reliably identify relevant Mendeley Cite controls? | Not yet reviewed | None | `UNKNOWN` |
| E06 | Can an OOXML-built citation be edited by modern Mendeley Cite? | Not yet reviewed | None | `UNKNOWN` |

## 3. Read-only discovery checklist

- [ ] Verify operating system and which instance executes Codex.
- [ ] Check Word desktop and Mendeley Cite installed versions without changing their configuration.
- [ ] Review official Mendeley API docs **separately** from Mendeley Cite add-in docs.
- [ ] Review community MCP repositories and exact installation/tool signatures (may change over time).
- [ ] Prepare a synthetic document with a clearly marked citation anchor; no private document yet.
- [ ] With approval and safe test credentials, test Mendeley lookup for a known existing user-library record.
- [ ] With approval and disposable test document, test Word adapter read-only inspection.
- [ ] Determine whether UI controls are accessible; do not start clicking/typing without approval.
- [ ] Document supported/unsupported citation formats, version gaps and concurrency behavior.
- [ ] Recommend POC path and stop/go criteria; request next-phase permission.

## 4. Approach comparison (hypotheses — unverified)

| Candidate | Possible advantage | Uncertainty / primary risk | Result |
|---|---|---|---|
| Official supported insertion API | Strongest compatibility, if it exists | Public supported API **not confirmed** | `UNVERIFIED` |
| Visible Word + Mendeley Cite UI Automation | Uses official citation authoring interface | Accessibility selectors, login, window focus, UI/version fragility | `UNVERIFIED` |
| OOXML citation structure manipulation | Might avoid UI if fully compatible | Undocumented format/version and inability to edit via official add-in | `RESEARCH_ONLY` |

## 5. Smallest practical POC (requires explicit authorization)

1. Create one **disposable** Word document, with one synthetic paragraph and anchor; never use original article.
2. Locate one **real reference already in the user's Mendeley library**, with user approval; record only minimum metadata in private local evidence.
3. Insert citation by an authorized mechanism; label result `ATTEMPTED`, not `VERIFIED`.
4. Save, close Word and reopen; select the citation using the **official Mendeley Cite pane** and confirm it can be edited.
5. Change citation style via Mendeley Cite, verify actual change and restore if necessary.
6. Confirm bibliography can be generated/updated by Mendeley Cite for the reference.
7. Ensure the source Word document is unchanged; report failure transparently if any check fails.

**GO:** All required `ACCEPTANCE_TESTS.md` native-citation checks pass with genuine local evidence.

**NO-GO:** The output is just text/Word-native citation or cannot be edited by Mendeley Cite after reopen; report `FEASIBILITY_BLOCKED` and do not claim full automation.

## 6. Observations and outcomes (fill only when performed)

- **Experiments run:** None.
- **Actual results:** None.
- **Blockers:** Environment details and approval for test accounts/UI automation not confirmed.
- **Documents changed:** None.
- **User permission for next phase:** Not yet obtained.
- **Suggested next action:** Verify environment; propose read-only assessment before authorized one-citation POC.

## 7. Evidence recording template

```text
Experiment ID:
Local date/time:
OS + Word + add-in versions:
Test document (synthetic only):
Reference ID (redact if shared):
Action & permission scope:
Expected outcome:
Actual observable result:
Evidence (redacted path / non-private capture):
PASS / FAIL / BLOCKED:
Notes & rollback:
```

## 8. Hasil discovery awal — 2026-10-28

### Lingkup dan izin

Pengguna meminta mencoba setelah pembacaan paket proyek. Pelaksanaan dibatasi pada discovery read-only dan pencatatan laporan ini. Tidak ada instalasi, login, akses dokumen privat, perubahan library, peluncuran Word/COM, atau UI Automation. File laporan ini saja diperbarui; implementasi belum dimulai.

### Bukti lokal

| Pemeriksaan | Hasil aktual | Batas kesimpulan |
|---|---|---|
| OS registry | ProductName `Windows 10 Home Single Language`; DisplayVersion `25H2`; CurrentBuild `26200`; EditionID `CoreSingleLanguage` | Nama registry dan build perlu direkonsiliasi; jangan menetapkan label Windows hanya dari ProductName |
| Runtime OS | `10.0.26200.0`, OS 64-bit | Diobservasi lewat .NET Environment |
| CIM OS | Akses tidak tersedia | Caption OS tidak berhasil diverifikasi; tidak meminta eskalasi |
| Office ClickToRun | `HomeStudent2021Retail,OneNoteFreeRetail`; version `16.0.20527.20088`; platform `x64` | Data instalasi, bukan uji kompatibilitas |
| WINWORD.EXE | ProductVersion dan FileVersion `16.0.20527.20088` | Binary ditemukan di lokasi Office16 standar, belum dijalankan |
| Proses | WINWORD: 0; nama proses mengandung Mendeley: 0 | Tidak membuktikan add-in belum terpasang atau akun logout |
| Python | `3.13.12` | Perintah versi berhasil |
| Node.js | `v24.14.1` | Perintah versi berhasil |
| dotnet dan uv | Tidak ditemukan pada PATH | Bukan bukti tidak terpasang di seluruh mesin |
| Word document connector | `list_document_sessions(surface=word)` berhasil; executors kosong | Tidak ada sesi Word terhubung; berbeda dari WordMcp komunitas |
| Mendeley MCP / WordMcp komunitas | Tidak ada tool khusus kedua server dalam katalog tool sesi ini | Instalasi/config global tidak diperiksa; integrasi belum diuji |
| Mendeley Cite versi/login/sync | `NOT_TESTED` | Memerlukan pemeriksaan add-in resmi |
| Dokumen uji dan lookup record nyata | `NOT_RUN` | Tidak ada dokumen .docx di workspace dan koneksi library tidak tersedia |

Paket tambahan kini tersedia: kebijakan keamanan, README, decisions, manifest contoh, dan skill lokal telah dibaca. Manifest contoh berisi dummy; tidak digunakan sebagai referensi nyata.

### Sumber dokumentasi yang diperiksa

Diakses 2026-10-28. Halaman upstream yang berubah bukan pin dependency; belum ada package/commit lokal yang diuji.

- https://www.mendeley.com/reference-management/mendeley-cite — halaman resmi menjelaskan insertion referensi/bibliografi melalui add-in Word. Ini tidak membuktikan kemampuan otomatisasi di mesin ini.
- https://dev.mendeley.com/methods/ — dokumentasi endpoint Mendeley API diperiksa, termasuk pencarian frasa `Mendeley Cite` yang tidak menghasilkan temuan. API publik untuk mengendalikan insertion add-in tetap `UNVERIFIED`; tidak ditemukannya frasa bukan bukti API tersebut mustahil ada.
- https://github.com/pallaprolus/mendeley-mcp — README upstream mendokumentasikan kemampuan library dan operasi mutasi. Belum diinstal/diautentikasi/diuji. MVP harus membatasi penggunaan ke lookup read-only; sumber ini bukan insertion API Mendeley Cite.
- https://github.com/trsdn/mcp-server-word — README upstream menyebut Windows, Word desktop 2016+, .NET 9 SDK/runtime, package `WordMcp.McpServer`, executable `mcp-word`. Dokumentasi menegaskan akses dokumen eksklusif dan Word berjalan tersembunyi. Dukungan lokal belum diuji; prerequisite dotnet belum tersedia pada PATH.

### Pilihan feasibility dan risiko

| Mekanisme | Penilaian awal | Stop/go |
|---|---|---|
| API insertion resmi | Belum terkonfirmasi dari sumber yang diperiksa | Jangan implementasikan method rekaan |
| Visible Word + Mendeley Cite | Kandidat POC karena memakai editor resmi; accessibility belum diuji | Perlu izin UI dan selektor terbaca; hentikan bila state tidak dapat diverifikasi |
| OOXML | Research only; belum ada before/after sample yang dianalisis | Tag/teks tidak membuktikan editability; tidak layak jadi fallback |

Word-native CITATION, legacy Mendeley Desktop, dan modern Mendeley Cite tetap diperlakukan sebagai format berbeda. Keberadaan Word desktop tidak membuktikan Mendeley Cite siap.

### Blocker dan langkah berikutnya

1. Hubungkan dan uji Mendeley MCP read-only sehingga satu record library nyata dapat dikembalikan dengan provenance. Jangan menambah sumber atau menyimpan credential di repo.
2. Siapkan adapter Word yang disetujui. Bila memilih WordMcp upstream, verifikasi runtime .NET yang sesuai dahulu; instalasi memerlukan izin tersendiri.
3. Konfirmasi add-in modern terpasang/login serta library sync; versi dan aksesibilitas masih belum diketahui.
4. Setelah izin eksplisit untuk Word UI dan pembuatan dokumen uji, buat disposable synthetic doc; pilih satu record library, sisipkan melalui Mendeley Cite resmi, lalu save/close/reopen, edit lewat pane, ganti style, dan uji bibliography. WordMcp harus melepas dokumen sebelum sesi Word terlihat.

**Gate Phase 0:** belum lulus: satu library lookup dan satu pembacaan dokumen sintetis belum terjadi. **Insertion:** `FEASIBILITY_BLOCKED`, belum dicoba. T08–T11 tidak dijalankan dan tidak dinyatakan PASS. Tidak ada output sitasi aktif yang dihasilkan.

## 9. Pemeriksaan Word UI yang diizinkan — 2026-10-28

Catatan lanjutan setup connector tersedia di bagian 10 di bawah.

- Pengguna memberikan izin mencoba otomatisasi Word dan POC pada dokumen terpisah melalui balasan `okehh cobak` setelah permintaan izin eksplisit. Izin ini tidak mencakup instalasi, perubahan library, atau penulisan dokumen asli.
- Computer Use `@oai/sky` berhasil memilih jendela Word dan mengaktifkannya. Snapshot sebelum aktivasi sempat memperlihatkan aplikasi foreground lain; tidak ada input dikirim sampai Word terverifikasi.
- Ribbon Word menampilkan **dua integrasi berbeda**: legacy `Mendeley Cite-O-Matic` dan modern `Mendeley Cite`. Tombol modern dibuka; plugin lama tidak digunakan.
- Panel modern berhasil menampilkan collection picker. Memilih `All References` menampilkan entri library dengan judul dan penulis. Tidak muncul permintaan login. Ini membuktikan akses tampilan library pada saat observasi, bukan verifikasi status sinkronisasi lengkap.
- Teks accessibility Word tersedia, tetapi tree accessibility panel add-in tidak tersedia pada snapshot yang diambil. Navigasi panel menggunakan koordinat dari screenshot terbaru yang diverifikasi; tanpa klik buta.
- Tidak ada tombol Insert citation yang diklik. Tidak ada pengetikan, penyimpanan, atau perubahan isi dokumen. Tidak ada screenshot privat disimpan ke repository.
- Identitas Mendeley document ID dan metadata lengkap belum dapat diperoleh melalui tool library read-only; katalog tool sesi tetap tidak menyediakan Mendeley MCP. Melihat judul di panel belum memenuhi verifikasi ID/provenance yang diwajibkan proyek. Tidak menebak DOI/tahun atau menganggap sumber mendukung klaim dari judul.
- **Hasil:** Word UI dan panel library dapat dinavigasi; insertion tetap `FEASIBILITY_BLOCKED` sampai satu record ID nyata terverifikasi dan dipetakan. POC editability/save-close-reopen/style/bibliography belum dijalankan. Langkah berikutnya adalah menyediakan koneksi Mendeley MCP read-only, bukan menyisipkan referensi tanpa identitas terverifikasi.

## 10. Persiapan connector — 2026-10-28

**Latest POC outcome:** see `harness/test-results.md`. A separate synthetic
document now demonstrates one official Mendeley Cite insertion, two document
close/reopen cycles with Edit citation recognition, APA/Vancouver style changes,
and bibliography insertion/rerender. Original hash unchanged. Human manual
validation remains pending; earlier blocked statuses below are historical.

### Update aktivasi setelah izin pengguna `OKEHH GASS`

- `.codex/config.toml` dibuat khusus proyek tanpa secret, dengan empat tool metadata dalam enabled_tools. Tidak ada konfigurasi Mendeley sebelumnya pada file proyek; konfigurasi global tidak diubah.
- `codex mcp get mendeley --json`: enabled=true, disabled_reason=null, command dan allowlist sesuai. Warning akses direktori temp/PATH alias muncul tetapi pembacaan config berhasil (exit 0).
- MCP stdio nyata: initialize PASS, server mendeley 0.8.0; list_tools memuat empat nama yang diizinkan; call_tool search library `bawang merah` limit 1 HTTP 200, is_error=false, content dan structured_content tersedia. Tidak ada operasi tulis/PDF.
- Katalog tool chat saat ini masih tidak memuat Mendeley. Subprocess uji berhasil; runtime chat perlu reload koneksi sebelum tool tersedia di chat.
- Berikutnya: restart koneksi MCP melalui Settings atau buka ulang aplikasi bila perlu, verifikasi tool chat, review exact mapping, lalu POC dokumen terpisah. Pembacaan dokumen sintetis dan validasi sitasi aktif tetap belum dilakukan. Dokumen asli tidak diubah.
- Rollback: hapus hanya section mcp_servers.mendeley yang baru ditambahkan.

**Update setelah login pengguna:** keberadaan login, Windows keyring, dan kelengkapan credential terverifikasi tanpa menampilkan nilainya. Akses keyring dari eksekusi terbatas ditolak OS; pemeriksaan berizin berhasil. Pencarian read-only `bawang merah` melalui client paket terpasang menghasilkan HTTP 200, satu record dengan ID tersedia. Tidak ada PDF diunduh atau library diubah. Ini uji API client langsung, belum handshake MCP stdio atau aktivasi koneksi Codex. Sitasi aktif tetap belum diuji. Screenshot pengguna menunjukkan callback sukses; nilai authorization code/state tidak disalin ke laporan.

- Pencarian plugin Mendeley mengembalikan daftar kosong.
- `.venv` dibuat dan `mendeley-mcp==0.8.0` dipasang lokal; SDK MCP `2.3.0`. Tidak ada instalasi global atau mutasi library. Network/venv terbatas gagal; pengulangan dengan persetujuan sistem berhasil.
- `pip check`: PASS. Backend keyring `keyring.backends.Windows.WinVaultKeyring` tersedia; penyimpanan credential live belum diuji.
- Source OAuth upstream bind semua interface dan tidak memvalidasi state di callback. `harness/login_mendeley.py` membatasi loopback, state/path validation, timeout, Windows keyring wajib, dan redaksi kegagalan token exchange. Wrapper belum diuji live.
- Lima pemeriksaan callback state/path: PASS. TOML config, executable path dan empat nama tool upstream: PASS. Uji asyncio awal timeout pada socketpair internal lingkungan terbatas; pengulangan berizin PASS. Tidak ada request API library dalam pengujian ini.
- `harness/mendeley-readonly.config.toml` masih template, belum aktif. Allowlist empat tool metadata; OAuth scope tetap `all`, bukan token read-only.
- Panduan: `harness/MENDELEY_SETUP.md`. Pengguna harus mendaftarkan app API dan menyelesaikan login/consent sendiri. Tidak meminta secret di chat.
- **Blocker:** OAuth, aktivasi MCP, handshake stdio dan lookup record nyata belum dilakukan. Gate sitasi aktif belum lulus; dokumen asli tidak diubah.
