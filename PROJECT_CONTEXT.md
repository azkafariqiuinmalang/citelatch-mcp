# PROJECT_CONTEXT.md — CiteLatch MCP

**Status:** Proposed / pre-feasibility | **Version:** 0.1.0 | **Updated:** 2026-10-28

## 1. Latar belakang masalah
Pengguna sering sudah memiliki artikel akademik / laporan praktikum dalam Microsoft Word, baik ditulis sendiri maupun disusun dengan bantuan AI. Ketika AI diminta menambahkan sitasi, output yang umum hanya berupa teks semacam `(Penulis, 2024)` yang mungkin berasal dari ingatan model, tidak selalu cocok dengan library Mendeley, dan **bukan sitasi aktif Mendeley Cite**. Akibatnya referensi sulit diverifikasi, style tidak tersinkron, dan bibliography tidak otomatis terkelola.

Pengguna **tidak meminta AI menulis ulang artikel, melakukan riset dari nol, atau membuat sistem academic research umum**. Masalah utamanya adalah *citation binding*: menghubungkan klaim/sitasi teks pada naskah yang **sudah tersedia** ke referensi nyata milik pengguna, lalu memasukkan sitasi sebagai objek sitasi yang dikenali oleh Mendeley Cite.

## 2. Visi
**CiteLatch MCP: From AI-Generated Citation Text to Real, Editable Mendeley Citations.**

MCP server yang bisa dipanggil oleh Codex atau MCP-compatible agents untuk membantu memilih, mencocokkan, menyisipkan, memverifikasi, serta memperbarui sitasi/bibliografi yang dikelola Mendeley Cite di Word.

## 3. Tujuan utama (urut prioritas)
1. Membaca **artikel Word yang sudah ada** dan menemukan sitasi teks atau lokasi yang ingin disitasi tanpa mengubah substansi naskah.
2. Menemukan **referensi nyata di library Mendeley pengguna** dan mencocokkannya ke sitasi dengan identitas terverifikasi (DOI + title + authors + year, bila tersedia).
3. Menyisipkan **sitasi aktif Mendeley Cite**, bukan teks biasa, pada posisi yang disetujui.
4. Menghasilkan / memperbarui bibliography **melalui Mendeley Cite**, agar style mengikuti pilihan Mendeley Cite.
5. Memastikan sitasi dapat diedit setelah Word ditutup dan dibuka ulang, dan menyajikan log per sitasi.
6. Menghindari perubahan isi artikel, layout, atau sitasi aktif lama yang tidak diperlukan.

## 4. Siapa yang menggunakan
- Pengguna utama: penulis laporan praktikum/karya ilmiah dengan Word dan library Mendeley.
- Eksekutor: Codex lokal sebagai agent utama.
- Sistem eksternal: Microsoft Word desktop, add-in Mendeley Cite, akun Mendeley/cloud library.
- Target awal: **single-user lokal Windows**; spesifikasi sistem sebenarnya belum dikonfirmasi.

## 5. Contoh user journey
**Input:** `laporan_fitokimia.docx` yang mengandung sitasi teks `(Rahman et al., 2024)`.

**Agent workflow:**
- Baca dokumen *tanpa* mengubahnya; inventarisasi sitasi yang belum aktif.
- Cari kandidat di **library Mendeley**; cek DOI, judul, penulis, tahun dan bila perlu isi sumber. Jika ambigu, tawarkan kandidat alih-alih menebak.
- Buat laporan pratinjau mapping sitasi → reference ID dan lokasi dalam Word.
- Setelah persetujuan, buat **salinan kerja** dokumen dan sisipkan satu sitasi uji melalui mekanisme yang terbukti menghasilkan sitasi aktif Mendeley Cite.
- Verifikasi lewat add-in, ganti style untuk menguji pembaruan, lalu buat bibliography dan simpan **output baru**.

**Output:** `.docx` berisi sitasi aktif Mendeley Cite dan laporan bukti uji/log mapping, tanpa mengubah isi artikel di luar elemen sitasi/bibliografi.

## 6. Ruang lingkup MVP
**Termasuk**
- Windows desktop + Word + Mendeley Cite (versi riil harus diobservasi).
- Artikel Word yang sudah ada; simpan output sebagai **file baru**.
- Satu (1) sitasi teks existing yang cocok dengan satu (1) entri library; lalu 2 sitasi dan bibliography sebagai tahap berikutnya.
- Read-only Mendeley lookup, match review, persetujuan sebelum penulisan.
- Verifikasi sitasi *editability* Mendeley Cite setelah dokumen dibuka kembali.
- Adapter untuk koneksi MCP; tool API yang terstruktur, status/error yang jelas.

**Tidak termasuk pada MVP**
- Menulis artikel secara otomatis, melakukan systematic review, penelitian literatur dari nol.
- Mengarang rujukan, menambah sumber baru ke library tanpa persetujuan eksplisit.
- Dukungan Zotero / EndNote atau Word Online / Mac / Linux.
- Mengatasi dokumen dengan semua jenis field/pagination/revision tanpa observasi.
- Mengklaim mengubah field Word `CITATION` menjadi sitasi Mendeley Cite (itu sistem berbeda).
- Otomatisasi seluruh jurnal / seluruh dokumen sebelum POC satu sitasi lulus.

## 7. Kriteria keberhasilan inti
**Sukses hanya bila:**
- Reference ID yang dipakai benar-benar ditemukan di library Mendeley pengguna.
- Citation object muncul dan dapat dipilih/diedit pada **Mendeley Cite resmi**, bukan hanya tampilan teks.
- Setelah save → close → reopen, sitasi tetap aktif.
- Mengganti style melalui Mendeley Cite memperbarui tampilan sitasi sesuai format dan bibliography konsisten.
- Tidak ada sitasi fiktif, placeholder bocor, kehilangan naskah, dan tidak ada perubahan tak disetujui.

## 8. Prinsip pengambilan keputusan
- **Evidence before implementation**: cari bukti kemampuan API/integrasi; uji POC lalu tetapkan arsitektur.
- **Mendeley is source of reference identity; Mendeley Cite is renderer/editor.** LLM tidak memformat sitasi final dari memorinya.
- **No silent fallback**: jika penyisipan aktif gagal, status harus `blocked`/`failed`, bukan diam-diam membuat sitasi plain text.
- **Human-in-the-loop** untuk matching ambigu dan penulisan file; output default tidak menimpa asli.
- **Minimal change**: ubah elemen sitasi/bibliografi saja; pertahankan body/layout sedapat mungkin.

## 9. Status asumsi & pertanyaan
Asumsi awal (belum dikonfirmasi): Windows 10/11, Word desktop 2016+, Mendeley Cite terpasang dan login, user memiliki library tersinkron. Semua asumsi dan perubahan keputusan harus dicatat dalam `OPEN_QUESTIONS.md` atau decision log baru.

## 10. Keadaan pengembangan
**BELUM dibangun dan BELUM diuji.** Dokumen ini adalah handoff untuk implementasi bertahap. Teknologi UI Automation dan/atau package-level OOXML hanya kandidat riset, bukan solusi yang sudah terbukti.
