# Acceptance Tests & POC Protocol

## Definisi sitasi aktif (strict)
A citation **PASS** hanya jika: (1) ditambahkan sebagai referensi Mendeley Cite modern; (2) klik/edit via pane **Mendeley Cite** resmi mengenali sumber; (3) survive save/close/reopen; (4) style switch via pane mengubah representasi sesuai expected style; (5) bibliography mengikuti reference set. Teks, Word native CITATION fields, atau OOXML tags saja **tidak cukup**.

## Test matrix
| ID | Scenario | Expected result | Level |
|---|---|---|---|
| T01 | Baca dokumen sintetik dengan `(TestAuthor, 2023)` | Temukan teks dan lokasi, tanpa tulis | Unit |
| T02 | Identifikasi sitasi existing Mendeley Cite | Tidak diperlakukan sebagai teks yang harus diganti | Integration |
| T03 | DOI exact ditemukan di Mendeley | Cocok ID dan metadata dari library | Integration |
| T04 | Dua paper author-year identik | `AMBIGUOUS_MATCH`, perlu review | Unit |
| T05 | Reference tidak ada | `NO_MATCH`, tidak dibuat-buat | Unit |
| T06 | Dokumentasi Word berisi footnote dan table | Tidak hilang dan warning bila belum supported | Integration |
| T07 | Dry-run diff | Berkas asli binary hash tidak berubah | Integration |
| T08 | Insersi satu sitasi ke dokumen uji | Recognized as active by official Mendeley Cite | Windows E2E |
| T09 | Tutup & buka ulang | Sitasi masih dapat diedit oleh pane | Windows E2E |
| T10 | Ubah style mis. APA ↔ Vancouver | Output sitasi berubah via add-in | Windows E2E |
| T11 | Insert/update bibliography | Daftar pustaka memuat sitasi dan refresh | Windows E2E |
| T12 | Retry job sama | Tidak ada duplikat sitasi | Integration / E2E |
| T13 | Dokumen berubah sejak scan | `STALE_DOCUMENT`, wajib review ulang | Unit |
| T14 | Word locked / UI dialog / timeout | Error jujur, tidak corrupt, bisa rollback | Windows E2E |
| T15 | Invalid Mendeley auth | Tidak menulis dokumen; `ADDIN_NOT_AUTHENTICATED` | E2E |
| T16 | UI insertion menghasilkan teks biasa saja | FAIL, bukan `verified` | E2E |
| T17 | Existing bibliography and tracked changes | Warning dan no destructive default | Integration |
| T18 | Audit after successful run | Berisi ID, anchor, result; tanpa token/isi privat | Integration |

## POC test setup
- Gunakan **dokumen sintetis/disposable** dengan satu paragraf, satu lokasi sitasi, dan satu paper nyata yang sudah ada di **library Mendeley milik tester**. ID/DOI tidak ditanam sebagai dummy di test integration.
- Simpan `before.docx` dan `after.docx` di folder uji lokal yang diabaikan Git.
- Catat Word/Mendeley Cite versions, browser/webview runtime, dpi/scaling, state login dan timestamp.
- Dalam uji E2E: jangan jalankan WordMcp background saat Word terlihat memegang dokumen yang sama.

## Manual verification evidence checklist
- [ ] Perintah insertion dicatat (`job_id`, `anchor_id`, `reference_id`).
- [ ] Tampilan Mendeley Cite mengenali sitasi dan referensinya ketika dipilih.
- [ ] Sitasi tetap dapat diedit setelah save/close/reopen.
- [ ] Style diganti via Mendeley Cite; tampilan di dokumen berubah dengan benar.
- [ ] Bibliography dibuat/update via Mendeley Cite dan cocok dengan referensi.
- [ ] Naskah non-sitasi tetap sama; original untouched.
- [ ] Tidak ada referensi palsu dan tidak ada placeholder.
- [ ] Jika gagal, hasil `FAILED/BLOCKED` dan file asli aman.

## Scope boundaries
Unit/integration tests boleh memakai fakes tanpa Mendeley login. Tetapi **tidak boleh** mengklaim `active citation E2E PASS` dari mock/regex/OOXML only. Ketergantungan terhadap akun dan UI eksternal menjadikan pengujian Windows E2E manual/semi-otomatis wajib.
