# Open Questions, Defaults & Decision Log

Dokumen ini mencegah Codex menganggap preferensi yang belum diputuskan sebagai fakta. **Pertanyaan berikut tidak menghalangi penulisan konteks/riset read-only; hanya ditanyakan saat benar-benar menentukan setup/implementasi.**

| ID | Pertanyaan untuk pemilik proyek | Default sementara | Mengapa penting |
|---|---|---|---|
| Q01 | OS utama Windows 10 atau 11? | Windows 10/11 | COM + UI Automation |
| Q02 | Word versi berapa: Microsoft 365 / 2019 / 2021 / 2024? | Desktop Word 2016+ | Dukungan WordMcp dan add-in |
| Q03 | Sudah pakai **Mendeley Cite add-in**, bukan Cite-O-Matic lama? | Diasumsikan Mendeley Cite | Format field berbeda |
| Q04 | Mendeley Reference Manager/cloud library sudah sync dan Cite login? | Belum dipastikan | Library lookup vs add-in insertion |
| Q05 | Codex yang digunakan CLI lokal, IDE plugin, atau cloud? | CLI lokal Windows | Akses Word desktop interaktif |
| Q06 | Source selection hanya library pribadi, atau boleh katalog global bila tidak ada? | **Hanya library pribadi** | Hindari sumber tak disetujui |
| Q07 | Default jika sitasi teks tidak ditemukan/ambigu? | Tandai untuk review, jangan auto-insert | Keamanan akademik |
| Q08 | Dokumen memiliki sitasi teks biasa, Mendeley aktif lama, atau campuran? | Uji dengan teks biasa dulu | Strategi scanning dan migrasi |
| Q09 | Apakah isi artikel sama sekali dilarang berubah? | Ya, kecuali objek sitasi/bibliografi yang disetujui | Non-goal utama |
| Q10 | Apakah boleh mengoperasikan Word UI otomatis? | Hanya setelah persetujuan | Dialog/fokus dan reliabilitas |
| Q11 | Gaya sitasi utama (APA 7, Vancouver, lainnya)? | Mengikuti style Mendeley Cite yang dipilih user | Tidak hard-code style di agent |
| Q12 | Apakah perlu mendukung multi-reference `(A, 2022; B, 2023)` dalam versi pertama? | Bukan MVP pertama | Kompleksitas cluster |
| Q13 | Persetujuan mapping per sitasi atau satu batch? | Review per sitasi untuk MVP | Mencegah salah pasang |
| Q14 | Nama `CiteLatch MCP` mau dipakai sebagai working name final? | Working name | Cek naming/licensing sebelum rilis |

## Decision protocol
Saat pilihan disepakati, pindahkan hasil ke `PROJECT_CONTEXT.md`/`ARCHITECTURE.md` dan log keputusan:

```text
DEC-XXX | YYYY-MM-DD | Decision | Alternatives | Rationale | Evidence | Rollback
```

## Top 4 questions for the owner before a real Windows POC
1. Windows 10/11 dan versi Word desktop?
2. Mendeley Cite versi modern sudah terpasang/login? Mendeley library sudah sinkron?
3. Codex lokal di Windows atau menjalankan coding di lingkungan cloud?
4. Boleh memakai UI Automation untuk mengklik Mendeley Cite saat Word terlihat, dengan review sebelum menulis output?
