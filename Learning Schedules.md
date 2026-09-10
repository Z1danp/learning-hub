---
title: Deliberate Practice & Building Schedule
created: 2026-09-06
tags:
  - schedule
  - habit
  - first-principles
  - productivity
related:
  - "[[First Principles coding]]"
  - "[[cs-abstraction-roadmap]]"
  - "[[backlog-fitur]]"
---

# 📅 Deliberate Practice & Building Schedule
> **Filosofi Utama:** Pisahkan waktu **Membangun (Top-Down)** dengan waktu **Mendalami (Bottom-Up)** untuk meminimalkan *context-switching fatigue* dan menjaga momentum proyek.

Terkait dengan: [[First Principles coding]] | [[cs-abstraction-roadmap]] | [[backlog-fitur]]  
Jangkar Proyek: `projects/expense-tracker`

---

## 🛠️ Weekdays: The Builder Sprint

### 🔹 Senin – Kamis (2 Jam / Malam)
*Fokus: 100% Membangun Fitur Proyek (`projects/expense-tracker`)*

* **00 – 10 menit | Alignment & Scope**:
  - Buka [[backlog-fitur|backlog fitur]] proyek, ambil **1 micro-task teratas** (maksimal estimasi 60–90 menit).
* **10 – 105 menit (95 menit) | Deep Work Coding**:
  - Fokus murni ngoding fitur (slicing UI, route Express, query DB).
  - ⛔ *Aturan Emas:* Jika menemukan konsep membingungkan, **jangan buka tab riset/rabbit hole**. Tulis sekilas di catatan cepat, lalu lanjutkan fitur sampai jalan.
* **105 – 120 menit (15 menit) | Quick Capture & Bookmark**:
  - Catat 1–2 pertanyaan fundamental yang tadi sempat muncul ke `notes/wishlist.md`.
  - Tinggalkan catatan baris kode tempat Anda berhenti untuk dilanjutkan besok malam.

---

### 🔹 Jumat: The Clean Slate & Extraction Night (2 Jam)
*Fokus: Merapikan Kode (Wrapping Up) & Menentukan Sasaran Belajar Akhir Pekan*

* **Jam ke-1 (60 menit) | Clean Slate (Bungkus & Rapikan)**:
  - Hilangkan sisa-sisa error linter / red squiggly lines TypeScript.
  - Hapus `console.log` kotor.
  - Jalankan test / build sanity check (`npm run typecheck`).
  - Lakukan `git commit` yang rapi agar otak masuk weekend dengan tenang (*Zeigarnik Effect Relief*).
* **Jam ke-2 (60 menit) | Reverse Extraction (Kurasi Topik)**:
  - Jalankan perintah: `extract: projects/expense-tracker/<file-fitur-minggu-ini>`.
  - Pilih **1 konsep CS fundamental** terbaik dari hasil ekstraksi untuk dijadikan target lab hari Sabtu.
  - *(Penting: Jangan belajar teori berat di Jumat malam; cukup tentukan targetnya, lalu tutup laptop).*

---

## 🔬 Weekend: The Deep Dive Lab & Synthesis

### 🔹 Sabtu: The Socratic Lab Day (4 Jam)
*Fokus: Menyelami Lapisan Mesin & Menguji Logika (Bottom-Up Drill)*

* **Blok 1 (1.5 Jam) | Socratic Sparring**:
  - Jalankan `mentor: <konsep-pilihan-jumat>`.
  - Rumuskan hipotesis, jawab pertanyaan pemandu agen, temukan *invariants* dan batasannya.
* **Blok 2 (2.0 Jam) | Hands-on Coding Gym (TDD)**:
  - Buat arena lab: `lab: webdev <nama_lab>`.
  - Tulis implementasi logika dari nol sampai test suite **Merah** berubah menjadi **Hijau**.
* **Blok 3 (30 Menit) | Stress-Testing & Falsifikasi**:
  - Panggil `falsify: <teorimu>` untuk menguji edge cases, race conditions, dan potensi memory leak.

---

### 🔹 Minggu: The Synthesis & Polish Day (4 Jam)
*Fokus: Mengkristalisasi Pemikiran & Menerapkannya Kembali ke Proyek*

* **Blok 1 (2.0 Jam) | Writing is Thinking (Feynman Synthesis)**:
  - Tuliskan mental model yang sudah terbukti di `notes/webdev/` menggunakan bahasa sendiri.
  - Tambahkan analogi dunia nyata dan tautan `[[wikilinks]]`.
  - Panggil `review: <path_catatan>` untuk mengecek blind spot atau miskonsepsi.
* **Blok 2 (2.0 Jam) | Closing the Loop (Refactor Proyek)**:
  - Buka kembali `projects/expense-tracker`.
  - Perbaiki (*refactor*) modul yang bersangkutan dengan standar pemahaman baru yang lebih kokoh, aman, dan efisien.

---

## ⚖️ Trade-offs & Rules of Thumb

> [!WARNING]
> ### 4 Jebakan & Mitigasinya:
> 1. **Velocity Trade-off (Kecepatan Fitur vs Teori)**:
>    - *Risiko:* Proyek terasa lebih lambat dibanding langsung copypaste kode AI.
>    - *Mitigasi:* Ingat hukum kualitas: 1 fitur yang Anda pahami luar-dalam jauh lebih berharga daripada 10 fitur rapuh buatan AI yang Anda tidak tahu cara debug-nya.
> 2. **Weekend Energy Drain (Kelelahan di Akhir Pekan)**:
>    - *Risiko:* Hari Sabtu/Minggu ada acara mendadak atau badan terlalu lelah untuk 4 jam belajar.
>    - *Mitigasi (Minimum Viable Routine / MVR):* Jika weekend darurat/lelah, pangkas menjadi **1 jam saja** (baca ulang catatan atau selesaikan 1 test lab kecil). Momentum tidak boleh putus total.
> 3. **The Over-Engineering Trap di Hari Minggu**:
>    - *Risiko:* Godaan menulis ulang (*rewrite*) seluruh arsitektur proyek karena baru belajar konsep keren.
>    - *Mitigasi:* Batasi refactor hari Minggu hanya pada **1 file/fungsi** yang relevan dengan lab Sabtu.
> 4. **The 2-Layer Rule Invariant**:
>    - *Aturan Mutlak:* Jangan pernah menyelam lebih dari 2 lapis abstraksi di bawah layer kode aktif dalam satu sesi. Catat rasa penasaran layer -3 ke `notes/wishlist.md`.