# 🧠 Agentic AI First-Principles Learning Hub

Selamat datang di **Personal Learning Studio & Coding Gym** untuk menguasai **Modern Web Development** dan **Cheminformatics** berbasis metode *First-Principles Discovery Learning* (Metode Sokrates & Teknik Feynman).

---

## 🏛️ Filosofi Belajar

1. **Buku & Paper adalah Source of Truth (`references/`)**:
   - Taruh buku teks (.pdf), paper, dan dokumentasi resmi di folder `references/`. Agen membacanya untuk menjamin akurasi materi dan mencegah halusinasi.
2. **First-Principles Inquiry (`@mentor` / Socratic Mode)**:
   - Agen tidak langsung memberi jawaban/definisi, melainkan menantangmu merumuskan teori dari batasan (*constraints*) masalah nyata.
3. **Hands-on Experimentation (`labs/`)**:
   - Uji pemikiranmu di kode nyata. Selesaikan latihan berbasis TDD sampai unit test berwarna **HIJAU (Pass)**.
4. **Writing is Thinking (`notes/`)**:
   - Tulis kesimpulan konsep dengan bahasamu sendiri (Feynman Formulation).
   - Panggil `@review` agar agen mengecek *blind spot* atau miskonsepsi.
5. **Anti-Passive Documentation & Falsifikasi (`project-docs/`)**:
   - Dokumentasi bukan sekadar cermin kode. Fitur riil didekonstruksi lewat 3 lapis abstraksi dan diuji kritis lewat *Falsification Lab* agar kamu terhindar dari ilusi kompetensi (*illusion of competence*).

---

## 📁 Struktur Direktori

- **`projects/`**: Junction / shortcut ke repositori riil yang sedang dibangun (e.g. `projects/expense-tracker`).
- **`project-docs/`**: Living documentation, backlog milestone, dan dekonstruksi arsitektur fitur (`project-docs/<nama-proyek>/AI Generated/Documentations/`).
- **`references/`**: Dokumen referensi, buku PDF, & cheat sheets (Source of Truth).
- **`notes/`**: Catatan pemahaman mandiri format Markdown (Obsidian-ready).
  - `notes/cheminformatics/`
  - `notes/webdev/`
  - `notes/hybrid_apps/`
- **`labs/`**: Bengkel eksperimen & coding gym (Python, TypeScript, Fullstack Chem Apps).
- **`templates/`**: Template catatan dan scaffold lab.
- **`scripts/runner.py`**: CLI helper ringan untuk membuat catatan, lab, dan menjalankan test.

---

## ⚡ Daftar Trigger & Perintah Cepat

*Catatan: Anda dapat mengetik perintah ini dengan atau tanpa tanda `@` (misal: `mentor:` atau `@mentor`).*

| Perintah | Deskripsi & Contoh |
| :--- | :--- |
| **`doc: <target>`** | **Feature Documentation Architect**: Menghasilkan dokumentasi fitur komprehensif (Alur Mermaid, 3-Layer Submarine, Bedah File, Falsification Lab, dan Matriks Trade-off).<br>*Contoh: `doc: projects/expense-tracker/apps/server/src/features/auth`* |
| **`extract: <file/fitur>`** | **Reverse Abstraction Extractor**: Membongkar kode proyek menjadi konsep CS fundamental (Layer 0, -1, -2).<br>*Contoh: `extract: projects/expense-tracker/apps/server/src/features/auth/auth.controller.ts`* |
| **`mentor: <topik>`** | Memulai dialog Sokrates untuk menemukan konsep dari first principles.<br>*Contoh: `mentor: Mengapa JWT stateless sulit di-revoke secara instan?`* |
| **`lab: <domain> <topik>`** | Menyiapkan arena eksperimen kode baru berbasis TDD di `labs/`.<br>*Contoh: `lab: webdev 03_token_bucket_rate_limiter`* |
| **`hint: <level 1 \| 2 \| 3>`** | Meminta petunjuk bertingkat jika buntu saat ngoding di lab. |
| **`falsify: <teori>`** | Meminta agen menguji hipotesis / logikamu dengan *edge cases* & skenario ekstrem. |
| **`review: <path_catatan>`** | Meminta review kritis atas catatan yang kamu tulis di `notes/`.<br>*Contoh: `review: notes/webdev/jwt-vs-cookie-mental-model.md`* |

---

## ⚓ Deep Just-In-Time (The Submarine Method)

1. **Bangun Proyek (Top-Down)**: Kerjakan fitur riil Anda di `projects/<nama-proyek>/`.
2. **Dokumentasi & Dekonstruksi**: Gunakan `doc: <target>` untuk memetakan arsitektur, invariant keamanan, dan arena falsifikasi di `project-docs/`.
3. **Ekstrak & Selami (Bottom-Up)**: Saat menemukan konsep yang belum dipahami, gunakan `extract: <file>` untuk memetakan lapis abstraksinya.
4. **Aturan 2-Layer**: Hanya boleh mendalami maksimal **2 lapis abstraksi** di bawah layer masalah agar tidak terjebak *rabbit hole*.
5. **Isolasi di Lab**: Buat test suite di `labs/` untuk menguji pemahaman secara hands-on.
6. **Sintesis di Obsidian**: Dokumentasikan kesimpulan di `notes/` dengan wikilinks (`[[konsep]]`).

## 🛠️ CLI Helper Commands

Jalankan perintah ini di terminal:

```powershell
# 1. Jalankan test lab Python
py scripts/runner.py test labs/cheminformatics/01_reinventing_smiles_parser/test_lab.py

# 2. Jalankan test lab TypeScript / Node.js
py scripts/runner.py test labs/webdev/01_concurrency_queue/lab.test.ts

# 3. Buat kerangka catatan baru
py scripts/runner.py new-note cheminformatics "Molecular Descriptors and QSAR"

# 4. Buat folder lab baru
py scripts/runner.py new-lab webdev "02_websocket_streaming"
```
