# Prompt pertama untuk Codex / AI Coding Agent

Salin instruksi di bawah ini ke Codex setelah mengekstrak paket proyek sebagai folder/repository lokal.

---

Kamu bertugas membantu mengembangkan proyek **CiteLatch MCP**. **Baca dahulu** `PROJECT_CONTEXT.md`, `AGENTS.md`, `PRD.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, `ACCEPTANCE_TESTS.md`, `SECURITY_AND_CITATION_POLICY.md`, `OPEN_QUESTIONS.md`, `DECISIONS.md`, dan `README.md` sebelum memulai.

**Masalah pengguna:** artikel Microsoft Word sudah ditulis, tetapi sitasi AI biasanya hanya berupa `(Penulis, Tahun)` dalam teks dan tidak terhubung dengan referensi asli. Target CiteLatch bukan membuat AI menulis artikel, melainkan memungkinkan AI Agent mencocokkan sitasi pada artikel **yang sudah ada** ke library Mendeley, lalu menyisipkannya sebagai **sitasi aktif Mendeley Cite yang tetap dapat diedit setelah save/reopen**, dengan bibliography yang diperbarui melalui add-in.

Gunakan **Codex sebagai agent**, bukan membangun agent/LLM baru. Produk yang dikembangkan adalah **MCP Server / Citation Bridge**. Existing Mendeley MCP dan Word MCP adalah kandidat dependency yang harus diverifikasi, bukan dianggap pasti bekerja.

**TUGASMU SEKARANG HANYA PHASE 0 (read-only discovery / planning):**
1. Audit asumsi environment dan dependency yang diperlukan.
2. Identifikasi perbedaan Word-native `CITATION`, Mendeley Desktop lama, dan Mendeley Cite modern.
3. Cari dokumentasi resmi terkait insertion API. Jangan mengarang API Mendeley Cite.
4. Bandingkan pendekatan UI Automation vs OOXML research; berikan pilihan yang paling realistis beserta keterbatasannya.
5. Rancang POC terkecil: **satu sitasi pada dokumen Word dummy menjadi native editable Mendeley Cite**, dengan kriteria pengujian yang tegas.
6. Lengkapi template `harness/discovery.md` **hanya dengan hasil observasi nyata**, catat keputusan baru di `DECISIONS.md`, dan susun daftar blocker yang perlu user jawab; jangan mengakses file privat atau login tanpa izin.
7. Laporkan apa yang terbukti, apa yang hanya hipotesis, serta rencana implementasi fase berikutnya.

**DILARANG pada tahap ini:** menginstal software tanpa izin, mengubah dokumen asli, membuat sitasi plain text lalu mengaku sitasi aktif, menambah referensi Mendeley tanpa izin, menulis ulang artikel, atau mengklaim full automation sudah terwujud.

Bicaralah dalam bahasa Indonesia secara jelas, langsung, terstruktur. Jangan menambah fitur penelitian literatur/AI writing yang tidak diminta.

---

**Prompt susulan (hanya setelah Phase 0 disetujui dan environment siap):**

> Lanjutkan Phase 1-2 sesuai `IMPLEMENTATION_PLAN.md` menggunakan test fixtures dan mocks. Tunjukkan hasil unit/integration test serta manifest mapping. Jangan menulis dokumen asli atau memulai UI Automation sebelum persetujuan eksplisit.

**Pra-cek:** Pastikan semua file inti tersedia di root workspace, termasuk `examples/citation-job.example.json` dan `harness/discovery.md`. Jika ada berkas hilang, hentikan task dan minta paket lengkap alih-alih menyimpulkan file tersebut tidak pernah dibuat.
