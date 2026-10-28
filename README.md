# CiteLatch MCP

Proof of concept integrasi library Mendeley dengan sitasi aktif Microsoft Word.

## Status aktual — 28 Oktober 2026

**POC teknis satu sitasi berhasil diamati pada satu lingkungan Windows. Validasi
manual pemilik proyek masih pending.** Belum ada server Citation Bridge MCP milik
CiteLatch atau adapter insertion reusable yang siap produksi.

- Lookup record asli melalui koneksi Mendeley yang diautentikasi.
- Penyisipan melalui panel resmi Mendeley Cite pada dokumen sintetis terpisah.
- Layar Edit citation mengenali sitasi setelah dokumen ditutup/dibuka ulang dua kali.
  Proses Word keseluruhan tidak dihentikan.
- Perubahan APA 7 → Vancouver → APA 7 serta bibliografi melalui add-in berhasil.
- Hash artikel asli tidak berubah.

Lihat [hasil pengujian dan keterbatasan](harness/test-results.md). Temuan ini bukan
jaminan kompatibilitas semua versi atau dokumen. Batch, idempotency, crash recovery,
dan dukungan ilmiah sumber terhadap klaim artikel belum diuji.

## Komponen yang tersedia

| Komponen | Status |
|---|---|
| Spesifikasi, arsitektur, acceptance tests | Tersedia |
| Library connector komunitas mendeley-mcp | Dependency eksternal, diuji lokal |
| Helper OAuth loopback/state validation | harness/login_mendeley.py |
| Contoh allowlist empat tool metadata | harness/mendeley-readonly.config.toml |
| Insertion UI | Eksperimen oleh agent; belum implementasi adapter |
| Citation Bridge MCP khusus CiteLatch | Belum diimplementasikan |

## Persiapan POC lokal

Memerlukan Windows, Word desktop, Mendeley Cite modern, Python, dan akun Mendeley.
Jalankan dari folder checkout di PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-poc.txt
.\.venv\Scripts\python.exe .\harness\login_mendeley.py
```

Daftarkan aplikasi API dan selesaikan login sendiri sesuai
[panduan setup](harness/MENDELEY_SETUP.md). Sesuaikan path pada contoh konfigurasi
dengan lokasi checkout. Jangan simpan token di konfigurasi atau repository.
Allowlist membatasi tool agent; token OAuth sendiri memiliki scope lebih luas.
Setup ini belum menyediakan perintah konversi dokumen otomatis.

Dokumen pengguna, PDF privat, token, konfigurasi lokal, serta output uji tidak
disertakan di repository. CiteLatch bukan produk resmi Microsoft, Elsevier, atau
OpenAI. Koneksi library menggunakan dependency komunitas
[pallaprolus/mendeley-mcp](https://github.com/pallaprolus/mendeley-mcp).

## Paket spesifikasi awal (historis)

Bagian berikut dipertahankan sebagai handoff awal. Status aktual berada di atas
dan pada laporan pengujian; label pra-feasibility di bawah bersifat historis.

> **Status:** Project specification / planning. **Belum ada implementasi, MCP baru, atau integrasi sitasi aktif yang dibuktikan.**
> **Versi context pack:** 0.2.0 — 28 Oktober 2026 (spesifikasi produk masih tahap pra-feasibility)
> **Bahasa:** Indonesia; nama API dan istilah teknis dalam bahasa Inggris.

## Tujuan dalam satu kalimat
CiteLatch MCP adalah **MCP Server khusus untuk membantu AI Agent (terutama Codex) menghubungkan sitasi dari artikel Word yang sudah ada ke referensi asli di library Mendeley, lalu menyisipkannya sebagai sitasi aktif yang dikelola Mendeley Cite**, tanpa menulis ulang isi artikel.

**Yang tidak diinginkan:** agent hanya mengetik `(Nama, Tahun)` lalu mengaku itu sitasi aktif. **Yang diinginkan:** hasil nyata bisa dipilih/diedit kembali melalui **Mendeley Cite** dan bibliography dapat diperbarui dari add-in tersebut.

## Mulai dari sini
1. Baca `PROJECT_CONTEXT.md` (sumber kebenaran kebutuhan dan ruang lingkup).
2. Baca `AGENTS.md` (aturan kerja Codex yang harus dipatuhi).
3. Baca `PRD.md` + `ARCHITECTURE.md` (perilaku produk dan rencana komponen).
4. Baca `IMPLEMENTATION_PLAN.md` + `ACCEPTANCE_TESTS.md` (rencana fase & bukti kelulusan).
5. Baca `SECURITY_AND_CITATION_POLICY.md`, `OPEN_QUESTIONS.md`, dan `DECISIONS.md`.
6. Lihat `harness/discovery.md` untuk template hasil discovery (belum berisi hasil nyata).
7. Untuk prompt langsung ke agent, pakai `START_HERE_PROMPT.md`.

## Isi paket

| File | Fungsi |
|---|---|
| `PROJECT_CONTEXT.md` | Latar belakang, masalah nyata, tujuan dan scope |
| `AGENTS.md` | Instruksi tetap untuk AI coding agent |
| `PRD.md` | Fitur, user stories, prioritas, non-goals |
| `ARCHITECTURE.md` | Arsitektur, tanggung jawab MCP, rancangan tools & status |
| `IMPLEMENTATION_PLAN.md` | Tahapan implementasi berbasis bukti, stop/go gates |
| `ACCEPTANCE_TESTS.md` | Skenario uji termasuk sitasi aktif & kompatibilitas Word |
| `SECURITY_AND_CITATION_POLICY.md` | Keamanan data, pengaman naskah, anti-fabrikasi |
| `OPEN_QUESTIONS.md` | Asumsi yang masih perlu dikonfirmasi |
| `DECISIONS.md` | Catatan keputusan proyek; pilihan teknis yang belum terbukti ditandai terbuka |
| `harness/discovery.md` | Template log Phase 0, status **NOT_STARTED** |
| `START_HERE_PROMPT.md` | Prompt siap salin untuk Codex |
| `.agents/skills/citelatch-citation/SKILL.md` | Rancangan skill operasional untuk fase mendatang |
| `examples/citation-job.example.json` | Contoh manifest **dummy**, bukan data publikasi riil |

## Prinsip arsitektur
- **Codex = agent/orchestrator yang sudah ada**, tidak membangun LLM/agent baru.
- **Mendeley MCP yang tersedia** = membaca/mencari referensi, bukan menyisipkan sitasi aktif.
- **Word MCP yang tersedia** = membaca/menandai dokumen, dengan keterbatasan sesi Word sendiri.
- **Citation Bridge MCP (dibangun)** = merutekan pemetaan, consent, insertion, verification dan hasil.
- **Mendeley Cite resmi** = sistem final yang harus mengenali sitasi hasil penyisipan.

## Status kemampuan (jangan dicampur)
- **Terdokumentasi:** Mendeley Cite dapat memasukkan/mengedit sitasi dan bibliografi di Word; Mendeley API mengekspos metadata library melalui OAuth; server komunitas untuk Mendeley dan Word tersedia.
- **Belum terbukti:** API publik terdukung untuk menyuruh Mendeley Cite memasukkan sitasi; kestabilan Windows UI Automation pada panel Mendeley Cite; apakah manipulasi struktur `.docx` dapat menghasilkan sitasi yang tetap dikenali Mendeley Cite.
- **Target riset:** buktikan satu sitasi aktif end-to-end pada versi Word/Mendeley Cite pengguna terlebih dahulu.

## Referensi awal untuk audit teknis (cek versi, jangan menganggap kompatibilitas dijamin)
- Mendeley Cite resmi: https://www.mendeley.com/reference-management/mendeley-cite
- Mendeley Support: https://www.elsevier.support/mendeley/answer/what-does-mendeley-cite-do
- Mendeley API: https://dev.mendeley.com/methods
- Mendeley OAuth: https://dev.mendeley.com/reference/topics/authorization_overview.html
- Mendeley MCP komunitas: https://github.com/pallaprolus/mendeley-mcp
- Word MCP komunitas: https://github.com/trsdn/mcp-server-word
- Studi kompatibilitas format (community research, **bukan** API resmi): https://github.com/rustam-bioinfo/mendeley-cite-to-desktop
- Codex project guidance: https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex

## Cara pakai

Persiapan connector lokal: lihat [harness/MENDELEY_SETUP.md](harness/MENDELEY_SETUP.md).
Paket terpasang di `.venv`; OAuth, koneksi aktif dan lookup library belum terverifikasi.
Ekstrak folder ini sebagai root repo baru, buka folder di Codex lokal pada **Windows** (asumsi sementara), dan kirim isi `START_HERE_PROMPT.md`. Di perintah awal, minta **discovery dan feasibility POC dulu**, bukan coding seluruh fitur sekaligus.

**Catatan identitas:** `CiteLatch MCP` adalah nama kerja, belum diverifikasi sebagai merek atau paket yang bebas konflik.

## Verifikasi isi paket ZIP sebelum menjalankan Codex

Ekstrak ZIP lengkap, **bukan hanya `AGENTS.md` atau `PROJECT_CONTEXT.md`**. Pastikan **folder kerja Codex adalah folder yang berisi `AGENTS.md` dan `PROJECT_CONTEXT.md`** (bukan folder parent/Downloads). Paket lengkap memiliki struktur seperti ini:

```text
citelatch-mcp/
├── README.md
├── AGENTS.md
├── PROJECT_CONTEXT.md
├── PRD.md
├── ARCHITECTURE.md
├── IMPLEMENTATION_PLAN.md
├── ACCEPTANCE_TESTS.md
├── SECURITY_AND_CITATION_POLICY.md
├── OPEN_QUESTIONS.md
├── DECISIONS.md
├── START_HERE_PROMPT.md
├── examples/
│   └── citation-job.example.json
├── harness/
│   └── discovery.md
└── .agents/skills/citelatch-citation/SKILL.md
```

Periksa `README.md`, `SECURITY_AND_CITATION_POLICY.md`, `DECISIONS.md`, `examples/citation-job.example.json`, dan `harness/discovery.md` benar-benar terlihat di **workspace agent**. `harness/discovery.md` adalah template dan sengaja belum memuat hasil tes. Jika belum terlihat, buka ulang folder root yang benar di editor/terminal atau salin kelima file dari paket tambahan.

**Paket hanya dokumentasi/handoff**, bukan server MCP siap jalan. Tidak ada bukti integrasi aktif berhasil sampai pengujian dilakukan pada Word dan Mendeley Cite di mesin target.
