# PRD — Product Requirements Document

**Product:** CiteLatch MCP | **Stage:** Discovery → POC | **Owner:** project initiator

## Problem statement
Artikel Word siap pakai berisi sitasi tekstual yang tidak aktif atau klaim tanpa ikatan referensi. AI mampu menebak author-year tetapi tidak mengintegrasikan secara riil ke library Mendeley / Mendeley Cite. Pengguna ingin mengonversinya menjadi sitasi asli yang bisa dikendalikan style/bibliography dari add-in.

## User jobs / acceptance
- **UJ-01:** "Aku punya laporan Word yang sudah ditulis, jangan tulis ulang isinya." → Dokumen asli tidak tertimpa; perubahan non-sitasi tidak ada atau dinyatakan eksplisit.
- **UJ-02:** "Aku punya `(Penulis, Tahun)` hasil AI; cari referensinya dari library Mendeley." → Kandidat dikembalikan dengan judul/penulis/tahun/DOI/Mendeley ID + confidence dan alasan.
- **UJ-03:** "Jangan paksa sitasi jika sumbernya tidak cocok." → Ambigu/no-match menghasilkan review queue, bukan `insert`.
- **UJ-04:** "Aku ingin sitasi aktif Mendeley Cite." → Sitasi bisa diedit di pane Mendeley Cite resmi sesudah reopen.
- **UJ-05:** "Bibliografi mengikuti Mendeley Cite." → Bibliografi dibuat/di-refresh via add-in; ubah gaya melalui Mendeley Cite mengubah output sesuai style.
- **UJ-06:** "Kalau gagal, naskah aman." → Backup/recovery, per-sitasi progress, audit, no silent fallback.

## Prioritas fitur
| ID | Fitur | Prioritas | Ukuran hasil |
|---|---|---|---|
| F01 | Inspeksi dokumen Word existing (read-only) | P0 | Identifikasi sitasi teks tanpa merusak field aktif |
| F02 | Lookup referensi di Mendeley library via MCP | P0 | ID dan metadata asli, bukan hasil ingatan model |
| F03 | Candidate matching + review | P0 | Exact DOI / high-confidence title + author/year; konflik dideteksi |
| F04 | Dry-run manifest lokasi dan pasangan referensi | P0 | Tinjauan eksplisit sebelum perubahan |
| F05 | Insert **satu sitasi aktif Mendeley Cite** | P0 riset | Dibuktikan di UI resmi & reopen |
| F06 | Audit + save as + rollback | P0 | Original tetap utuh; kesalahan transparan |
| F07 | 2+ sitasi dan bibliography refresh | P1 | Konsisten setelah style switch |
| F08 | Replace existing plain-text citation idempotently | P1 | Tidak menyisipkan duplikat saat retry |
| F09 | Batch dan multi-citation clusters | P2 | Skala setelah POC terbukti |
| F10 | Menyarankan sitasi untuk klaim tanpa sumber | P2 | Hanya rekomendasi untuk user review, bukan insert default |

## Mode produk
**Mode A (prioritas MVP):** `resolve_existing_citations` → artikel memiliki sitasi teks biasa; cari dan pasangkan ke Mendeley; insert setelah approval.

**Mode B (nanti):** `suggest_missing_citations` → identifikasi klaim tanpa sitasi; cocokkan ke library; user menyetujui klaim-sumber; baru insert. **Agent tidak boleh berpura-pura suatu paper mendukung klaim hanya berdasarkan judul/abstract.**

## Input / output
**Input:** path absolut file `.docx`, mode, optional selected citation anchors, optional Mendeley folder ID, citation style tujuan (dipilih/dikonfirmasi oleh Mendeley Cite).

**Output:** `*.citelatch.docx` (jika lulus insert/validate); `citation_manifest.json`, `citation_report.md`, `error_report.json` dan backup sesuai kebijakan. Jangan otomatis menganggap file `.docx` lulus bila hanya teks yang berubah.

## Matching requirements
- Prioritaskan referensi **yang sudah ada** di Mendeley library pengguna.
- DOI exact (jika tersedia), title normalized, authors/year; toleransi variasi transliterasi/year online-first dengan penanda konflik.
- Author-year tanpa DOI bersifat **ambiguous** jika terdapat beberapa kandidat layak.
- Banyak referensi pada satu tanda kurung harus dimodelkan sebagai citation cluster, bukan dipecah salah.
- Verifikasi sumber terhadap teks claim jika user meminta *support validation*; metadata saja tidak membuktikan isi artikel.
- Jangan menambahkan referensi katalog/global ke library tanpa izin.

## Compatibility requirements
- Target awal: Word desktop Windows dengan add-in **Mendeley Cite** modern (bukan Cite-O-Matic lama).
- Existing Mendeley Cite controls harus dilestarikan; dokumen dengan legacy fields/mixed controls perlu deteksi dan perlakuan terpisah.
- Tracked Changes, komentar, footnotes, tables, hyperlinks, daftar pustaka lama, proteksi/IRM: identifikasi risikonya di discovery; jangan berasumsi aman untuk semua kasus.

## UX / kontrol
- Preview: `detected` → `matched|ambiguous|missing` → `approved` → `inserting` → `verified|failed`.
- Pengguna harus dapat melihat naskah mana, sitasi mana, referensi mana dan statusnya.
- Hanya setelah approval agent boleh menulis file output; jangan gunakan persetujuan menyeluruh untuk penambahan sumber baru atau perubahan konten.

## Non-functional
- Single-user lokal; tidak perlu layanan cloud baru (kecuali Mendeley cloud dan lisensi Word yang digunakan).
- Setiap action punya timeout, retry terbatas, idempotency key, dan error code.
- Data sensitif lokal; audit minim metadata dengan token disembunyikan.
- Support Windows UI Automation **hanya bila terbukti feasible** pada mesin pengguna.
