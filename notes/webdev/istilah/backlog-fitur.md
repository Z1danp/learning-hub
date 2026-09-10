---
title: Backlog Fitur (Feature Backlog)
domain: webdev
category: istilah
tags:
  - istilah
  - software-engineering
  - productivity
  - workflow
date: 2026-09-06
status: reviewed
related:
  - "[[Learning Schedules]]"
  - "[[First Principles coding]]"
  - "[[cs-abstraction-roadmap]]"
---

# 📋 Backlog Fitur (Feature Backlog)

> **One-Sentence Core Idea:**  
> Daftar antrean terurut (*prioritized queue*) dari seluruh fitur, perbaikan bug, dan tugas teknis yang ingin dikerjakan, diurutkan dari yang paling penting agar otak bebas dari *decision fatigue* saat mulai ngoding.

Terkait dengan: [[Learning Schedules]] | [[First Principles coding]] | [[cs-abstraction-roadmap]]  
Jangkar Proyek: `projects/expense-tracker`

---

## 1. Masalah Fundamental: Mengapa Butuh Backlog?

Otak manusia adalah **prosesor untuk memikirkan ide, bukan media penyimpanan (harddisk) untuk menampung to-do list** (*Cognitive Load Theory*).

Ketika Anda membangun proyek tanpa backlog:
1. **Decision Fatigue (Kelelahan Mengambil Keputusan)**: Setiap kali membuka laptop, Anda menghabiskan 20–30 menit hanya untuk bingung: *"Malam ini enaknya ngerjain apa ya?"*. Ini adalah pemicu utama prokrastinasi dan scrolling media sosial.
2. **Shiny Object Syndrome**: Saat sedang ngoding fitur A, tiba-tiba terpikir ide fitur B (misal: animasi keren atau dark mode). Tanpa backlog, Anda akan langsung melompat mengerjakan fitur B, meninggalkan fitur A dalam kondisi setengah jadi.
3. **Zeigarnik Effect (Kecemasan Mental)**: Pikiran terus terbebani karena takut melupakan ide-ide fitur yang berseliweran di kepala.

> **Solusi:** Keluarkan semua ide dari kepala, tuliskan ke dalam satu dokumen terpusat (*backlog*), lalu prioritaskan.

---

## 2. 🍳 Analogi Dunia Nyata: Dapur Restoran

* **Tanpa Backlog**: Pelanggan, pelayan, dan kasir berteriak secara acak meminta nasi goreng, steak, es teh, dan sup. Koki bingung mana yang harus dimasak duluan, kompor terbakar, pesanan tertunda, dan dapur berantakan.
* **Dengan Backlog**: Setiap pesanan ditulis di atas kertas tiket dan dijepit berurutan di papan antrean (*the backlog*). Koki cukup mengambil **tiket paling atas**, memasaknya hingga tuntas, lalu mengambil tiket berikutnya. Dapur tenang, fokus, dan pesanan selesai satu per satu.

---

## 3. 🎯 Skema Prioritas Praktis (Model MoSCoW Ringkas)

Untuk pengembang mandiri (*solo developer*), tidak perlu menggunakan software manajemen proyek yang rumit seperti Jira. Cukup gunakan 3 tingkatan prioritas:

### 🔴 1. Must-Have (Fokus Sekarang — Inti Aplikasi)
Fitur absolut yang menentukan apakah aplikasi bisa berfungsi sesuai tujuannya (*Minimum Viable Product / MVP*). Tanpa fitur ini, aplikasi belum layak disebut jalan.

### 🟡 2. Should-Have (Fokus Berikutnya — Peningkatan Nilai)
Fitur penting yang meningkatkan kegunaan aplikasi secara signifikan, tetapi jika belum ada di versi pertama, sistem inti tetap bisa berjalan.

### 🟢 3. Nice-to-Have (Nanti Saja — Pemanis & Optimasi)
Fitur pemanis, kosmetik, atau optimasi canggih yang bagus jika ada, tetapi **dilarang dikerjakan** sebelum poin 1 dan 2 selesai.

---

## 4. 📝 Contoh Nyata Backlog: `projects/expense-tracker`

Contoh implementasi backlog riil pada proyek Anda:

```markdown
### 🔴 Must-Have (MVP)
- [x] Setup arsitektur monorepo (client, server, shared-types)
- [x] Backend API: Register & Login dengan JWT + HTTP-Only Cookie
- [ ] Frontend UI: Form Login & Register di React 19 + Tailwind v4
- [ ] Database: Schema tabel categories & transactions di PostgreSQL via Drizzle
- [ ] Backend API: CRUD pencatatan pengeluaran (tambah, lihat, edit, hapus)
- [ ] Frontend UI: Form input transaksi + dropdown kategori

### 🟡 Should-Have
- [ ] Dashboard Ringkasan: Total pengeluaran bulan berjalan vs sisa budget
- [ ] Filter transaksi berdasarkan rentang tanggal dan kategori
- [ ] Validasi saldo: Peringatan visual jika pengeluaran melewati ambang batas (alert threshold)

### 🟢 Nice-to-Have
- [ ] Toggle Dark Mode / Light Mode
- [ ] Export data pengeluaran ke format CSV / Excel
- [ ] Grafik visualisasi pie chart pengeluaran dengan animasi Chart.js / Recharts
- [ ] Rekap pengeluaran otomatis berbasis AI
```

---

## 5. ⏱️ Penerapan dalam Jadwal Belajar 2 Jam (Weekdays)

Gunakan backlog ini sebagai panduan eksekusi harian Anda:

1. **Menit 00 – 10 (Ambil Tiket)**:
   * Buka backlog, ambil **1 tugas paling atas** dari kategori *Must-Have*.
   * Pastikan cakupan tugas realistis untuk diselesaikan dalam 60–90 menit.
2. **Menit 10 – 105 (Deep Focus)**:
   * Kerjakan tugas tersebut sampai selesai tanpa memikirkan fitur lain.
3. **Menit 105 – 120 (Tutup & Bookmark)**:
   * Beri tanda centang `[x]` pada backlog jika selesai.
   * Tinggalkan catatan baris kode untuk tugas berikutnya di hari esok.
