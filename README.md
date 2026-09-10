# 🧠 Agentic AI First-Principles Learning Hub

Selamat datang di **Personal Learning Studio & Coding Gym** untuk menguasai **Modern Web Development**, **Analytical Chemistry & Instrumentation (ICP-MS, GC-MS, dll.)**, serta **Cheminformatics** berbasis metode *First-Principles Discovery Learning* (Metode Sokrates & Teknik Feynman).

---

## 🏛️ Filosofi Belajar

1. **Source of Truth yang Ketat (`references/`)**:
   - Simpan dokumentasi resmi, paper ilmiah, standar metode (EPA, ISO, ASTM, AOAC), buku teks, dan SOP instrumen lab di folder `references/`. Agen membacanya untuk menjamin akurasi materi dan mencegah halusinasi.
2. **First-Principles Inquiry (`@mentor` / Socratic Sparring)**:
   - Agen tidak langsung memberi jawaban atau boilerplate kode instan. Anda ditantang merumuskan hipotesis dan mental model dari batasan (*constraints*) masalah nyata.
3. **Hands-on Experimentation & Coding Gym (`labs/`)**:
   - Uji pemikiran di kode nyata. Selesaikan latihan berbasis TDD (Test-Driven Development) menggunakan Python atau TypeScript sampai test suite berwarna **HIJAU (Pass)**.
4. **Writing is Thinking (`notes/`)**:
   - Kristalisasikan pemahaman menjadi catatan berjejaring di Obsidian menggunakan format Markdown dan `[[wikilinks]]`. Panggil `@review` agar agen membedah *blind spot* atau miskonsepsi.
5. **Anti-Passive Documentation & Falsifikasi (`project-docs/`)**:
   - Dokumentasi bukan sekadar cermin kode atau ringkasan pasif. Fitur nyata didekonstruksi lewat 3 lapis abstraksi (*Submarine Method*) dan diuji kritis lewat *Falsification Lab* agar terhindar dari ilusi kompetensi (*illusion of competence*).

---

## 📁 Struktur Direktori

```text
agentic-learning-hub/
├── projects/          # Symlink / shortcut ke proyek nyata (e.g., projects/expense-tracker)
├── project-docs/      # Living documentation, backlog milestone, dan arsitektur fitur
├── references/        # Standar analitik (EPA, ISO), instrument manual, paper, & cheat sheets
├── notes/             # Second-brain vault format Markdown (Obsidian-ready)
│   ├── analytical_chemistry/ # Instrumen lab (ICP-MS, GC-MS, HPLC, AAS, QA/QC)
│   ├── cheminformatics/      # SMILES parser, molekul, QSAR, deskriptor kimia
│   ├── webdev/               # Backend, frontend, arsitektur, database
│   └── hybrid_apps/          # Cross-platform & fullstack client-server
├── labs/              # Coding gym & TDD sandboxes
│   ├── analytical_chemistry/ # Otomasi kurva kalibrasi, validasi QA/QC, LOD/LOQ, interferensi
│   ├── cheminformatics/      # Algoritma komputasi kimia & cheminformatics (Python)
│   └── webdev/               # Logika concurrency, queue, caching, streaming (TypeScript)
├── templates/         # Template catatan instrumen lab, catatan konsep, dan lab runner
├── scripts/runner.py  # CLI helper untuk generate note, scaffolding lab, dan menjalankan test
└── pyproject.toml     # Dependensi Python (numpy, pandas, scipy, matplotlib, pytest)
```

---

## ⚡ Daftar Trigger & Perintah Cepat

*Catatan: Anda dapat mengetik perintah ini dengan atau tanpa awalan `@` (misal: `mentor:` atau `@mentor`).*

| Perintah | Deskripsi & Contoh Penggunaan |
| :--- | :--- |
| **`mentor: <topik>`** | **Socratic Research Mentor**: Memulai dialog Sokrates untuk menemukan konsep fundamental dari batasannya.<br>• *Analitik: `mentor: Mengapa interferensi ArCl mengacaukan pembacaan As-75 di ICP-MS?`*<br>• *WebDev: `mentor: Mengapa JWT stateless sulit di-revoke secara instan?`* |
| **`falsify: <teori>`** | **Stress-Testing Hipotesis**: Menguji pemikiran / hasil analisismu dengan skenario ekstrem, edge cases, atau interferensi tersembunyi.<br>• *Analitik: `falsify: Internal standard sinyalnya drop 40% karena pompa selang aus.`*<br>• *WebDev: `falsify: Mutex ini aman dari race condition saat cluster dinaikkan 3 node.`* |
| **`doc: <target>`** | **Feature Documentation Architect**: Menghasilkan dokumentasi komprehensif (Alur Mermaid, 3-Layer Submarine, Bedah File, Falsification Lab, dan Trade-off Matrix).<br>• *Contoh: `doc: projects/expense-tracker/apps/server/src/features/auth`* |
| **`extract: <file/fitur>`** | **Reverse Abstraction Extractor**: Membongkar kode atau metode instrumen menjadi Layer 0, -1, dan -2.<br>• *Contoh: `extract: projects/expense-tracker/apps/server/src/features/auth/auth.controller.ts`* |
| **`lab: <domain> <topik>`** | **TDD Lab Generator**: Menyiapkan arena eksperimen kode/data baru dengan test suite Merah (failing).<br>• *Analitik: `lab: analytical_chemistry calibration_validator`*<br>• *WebDev: `lab: webdev 03_token_bucket_rate_limiter`* |
| **`hint: <level 1 \| 2 \| 3>`** | Meminta petunjuk bertingkat secara terukur jika buntu saat menyelesaikan lab. |
| **`review: <path_catatan>`** | Meminta *peer-review* kritis atas catatan Obsidian yang telah kamu tulis.<br>• *Contoh: `review: notes/analytical_chemistry/prinsip-dasar-icp-ms.md`* |

---

## ⚓ The Submarine Method (Aturan 2-Layer)

Jangan pernah menyelam lebih dari 2 lapis abstraksi di bawah layer operasional aktif dalam satu sesi agar terhindar dari kelelahan kognitif (*rabbit hole*):

### A. Pada Domain Kimia Analitik & Instrumentasi:
* **Layer 0 (SOP & Operasional Lab)**: Preparasi sampel (digest asam $HNO_3$), setting autosampler, pembuatan deret standar, pembacaan konsentrasi ppb di software instrumen.
* **Layer -1 (Instrument Mechanics & Physics)**: Dinamika aerosol nebulizer, suhu ionisasi plasma argon ($6.000 - 10.000\text{ K}$), vakum antarmuka (*interface cones*), *Kinetic Energy Discrimination* (KED) di collision cell, filter massa kuadrupol ($m/z$), detektor *electron multiplier*.
* **Layer -2 (Atomic Physics & Physical Chemistry)**: Persamaan ionisasi Saha, penampang tabrakan ion poliatomik, *space-charge effect* (tolakan ion berat vs ringan), kestabilan Mathieu ($a, q$).
* **Layer -3**: 🛑 *Berhenti & catat ke `notes/wishlist.md` jika penasaran ke tingkat kuark / subatomik.*

### B. Pada Domain Software Engineering & WebDev:
* **Layer 0**: Framework API / Surface Code (`express`, `react`, query ORM).
* **Layer -1**: Runtime & Language CS Mechanics (Event Loop, Closures, Garbage Collector, Memory Heap).
* **Layer -2**: OS Protocols, Network & Database Storage (TCP/IP, HTTP/2, B-Tree Index, ACID Transactions).
* **Layer -3**: 🛑 *Berhenti & catat ke `notes/wishlist.md` jika penasaran ke tingkat gerbang logika silikon.*

---

## 🛠️ Panduan CLI Helper (`scripts/runner.py`)

Gunakan script helper untuk mempercepat alur kerja:

```powershell
# 1. Buat catatan baru (otomatis menggunakan template yang sesuai)
py scripts/runner.py new-note analytical_chemistry "Interferensi Poliatomik dan Mode KED"
py scripts/runner.py new-note webdev "Concurrency Model di Node JS"

# 2. Buat arena lab TDD baru
py scripts/runner.py new-lab analytical_chemistry weighted_linear_regression
py scripts/runner.py new-lab webdev token_bucket_limiter

# 3. Jalankan unit test lab
py scripts/runner.py test labs/analytical_chemistry/calibration_validator/test_lab.py
py scripts/runner.py test labs/webdev/01_concurrency_queue/lab.test.ts
```
