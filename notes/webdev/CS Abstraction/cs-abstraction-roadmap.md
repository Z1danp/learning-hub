---
title: Computer Science Abstraction Roadmap
domain: webdev
tags:
  - roadmap
  - first-principles
  - computer-science
  - architecture
date: 2026-09-06
status: in-progress
related:
  - "[[First Principles coding]]"
  - "[[Learning Schedules]]"
  - "[[backlog-fitur]]"
---

# 🧭 The Computer Science Abstraction Roadmap
> **Filosofi:** Belajar Computer Science bukan menghafal sintaksis framework yang berganti tiap 3 tahun, melainkan menguasai **hukum fisika komputasi** (CPU, RAM, Disk, Network) yang tidak pernah berubah selama 50 tahun terakhir.

Terkait dengan: [[First Principles coding]] | [[Learning Schedules]] | [[backlog-fitur]]  
Subjek Praktik: `projects/expense-tracker`

---

## 🏛️ Mengapa Roadmap Ini Benar-Benar "Fundamental"?

| Yang Bersifat Tren (Fana - Berubah Tiap 2-3 Tahun) | Yang Bersifat Fundamental (Abadi - Invariant)              |
| :------------------------------------------------- | :--------------------------------------------------------- |
| Next.js App Router vs Pages Router                 | **HTTP Request-Response Lifecycle & Statelessness** (1991) |
| Redux vs Zustand vs React State                    | **Memory Allocation, Pointers, Heap vs Stack** (1960-an)   |
| Drizzle ORM vs Prisma vs TypeORM                   | **B-Tree Indexing, ACID, Disk I/O & WAL** (1970-an)        |
| Express 4 vs 5 vs Fastify                          | **Single-Threaded Event Loop & Non-Blocking I/O (epoll)**  |
| JWT library syntax di Node.js                      | **One-Way Hash Function, Salt, & HMAC Cryptography**       |

Framework hanyalah "kulit" (Layer 0). Jika Anda menguasai **5 Pilar Abstraksi CS** di bawah ini, Anda bisa mempelajari framework apa pun dalam hitungan hari, dan Anda tidak akan pernah bisa dibohongi oleh halusinasi kode AI.

---

## 🗺️ 5 Pilar Abstraksi Computer Science

```
Stage 1: Runtime & Memory  ──>  Stage 2: Storage & Indexing  ──>  Stage 3: Networks & Protocols
                                          │                                     │
                                          ▼                                     ▼
                               Stage 4: Concurrency & Locks  ──>  Stage 5: Cryptography & Security
```

---

### 🟢 Stage 1: The Execution Machine (Runtime & Memory)
*Estimasi: 8 - 10 Jam Pembelajaran Aktif*

Mengerti bagaimana sepotong kode TypeScript/JavaScript dieksekusi di RAM dan CPU oleh mesin runtime.\

* **Invarian CS Fundamental**:
  - **Call Stack vs Memory Heap**: Alokasi memori untuk tipe data primitif (di stack) vs objek/array (di heap).
  - **Pointers & References**: Mengapa mutasi objek di satu fungsi bisa merusak data di fungsi lain (*side-effects*).
  - **The Event Loop (Libuv & V8)**: Bagaimana Node.js membagi tugas antara Call Stack, Microtask Queue (`Promise`), dan Macrotask Queue (`setTimeout`).
  - **Closures & Lexical Scope**: Bagaimana fungsi mempertahankan referensi ke scope induknya di heap memory, dan bagaimana ini bisa menyebabkan *memory leak*.
* **Jangkar di `expense-tracker`**:
  - `apps/server/src/index.ts`: Middleware chain Express dan alur asinkron `async/await`.
* **Uji Verifikasi Mandiri (Active Recall)**:
  - *Dapatkah Anda menjelaskan urutan output console dari campuran `console.log`, `Promise.then`, dan `setTimeout` tanpa menjalankannya?*

---

### 🟡 Stage 2: The Storage Machine (Database & Disk I/O)
*Estimasi: 10 - 12 Jam Pembelajaran Aktif*

Mengerti bagaimana data disusun di disk magnetik/SSD dan bagaimana database relational membaca jutaan baris dalam hitungan milidetik.

* **Invarian CS Fundamental**:
  - **Sequential vs Random Disk I/O**: Mengapa membaca data yang berurutan 100x lebih cepat daripada melompat-lompat di disk.
  - **B-Tree Index Data Structure**: Struktur pohon seimbang (*balanced tree*) yang memangkas kompleksitas pencarian dari $O(N)$ menjadi $O(\log N)$.
  - **Write-Ahead Logging (WAL)**: Menulis catatan perubahan ke disk secara append-only sebelum mengubah file database utama (rahasia ketahanan crash).
  - **Query Execution Plan (`EXPLAIN ANALYZE`)**: Bagaimana database optimizer memilih antara Sequential Scan, Index Scan, atau Bitmap Heap Scan.
* **Jangkar di `expense-tracker`**:
  - `apps/server/src/db/schema.ts`: Pemilihan tipe data (`varchar`, `uuid`, `timestamp`) dan pembuatan index pada foreign keys.
* **Uji Verifikasi Mandiri**:
  - *Mengapa menambahkan index pada setiap kolom di database justru membuat operasi `INSERT` dan `UPDATE` menjadi lambat?*

---

### 🔵 Stage 3: The Wire Machine (Network & Protocols)
*Estimasi: 8 - 10 Jam Pembelajaran Aktif*

Mengerti apa yang terjadi di kabel fisik saat browser memanggil server Anda.

* **Invarian CS Fundamental**:
  - **TCP 3-Way Handshake & Connection Overhead**: SYN, SYN-ACK, ACK. Mengapa membuka koneksi baru itu mahal dan mengapa kita butuh *Connection Pooling*.
  - **HTTP Semantics & State Management**: Mengapa protokol HTTP itu *stateless*, dan bagaimana header `Set-Cookie` merekayasa persistensi sesi.
  - **Same-Origin Policy (SOP) & CORS**: Model keamanan browser yang mengisolasi antar website, serta cara kerja preflight request `OPTIONS`.
  - **Transport Layer Security (TLS/HTTPS)**: Negosiasi kunci asimetris (RSA/ECC) untuk menyepakati kunci simetris sementara (AES) demi kecepatan.
* **Jangkar di `expense-tracker`**:
  - `apps/server/src/index.ts`: Pengaturan `cors({ origin: 'http://localhost:5173', credentials: true })`.
  - `auth.controller.ts`: Pengiriman cookie `httpOnly`, `secure`, `sameSite: strict`.
* **Uji Verifikasi Mandiri**:
  - *Apa bedanya serangan XSS dan CSRF, dan bagaimana kombinasi `HttpOnly` + `SameSite=Strict` menangkal keduanya?*

---

### 🟣 Stage 4: The Contention Machine (Concurrency & Locks)
*Estimasi: 10 - 12 Jam Pembelajaran Aktif*

Mengerti perilaku sistem ketika banyak pengguna mengakses data yang sama pada milidetik yang sama.

* **Invarian CS Fundamental**:
  - **Race Conditions & TOCTOU (Time-of-Check to Time-of-Use)**: Celah waktu antara saat kondisi dicek dan saat aksi dieksekusi.
  - **Database Transaction Isolation Levels**: Perbedaan *Read Committed*, *Repeatable Read*, dan *Serializable*. Fenomena *Dirty Read* dan *Phantom Read*.
  - **Pessimistic vs Optimistic Locking**: Kapan mengunci baris data (`SELECT FOR UPDATE`) vs kapan menggunakan versioning token.
* **Jangkar di `expense-tracker`**:
  - Fitur pencatatan transaksi dan pengurangan saldo: Mencegah saldo berkurang dua kali jika request dikirim bersamaan.
* **Uji Verifikasi Mandiri**:
  - *Jika dua user mentransfer uang satu sama lain di saat yang persis sama, bagaimana deadlock bisa terjadi dan bagaimana cara mencegahnya?*

---

### 🔴 Stage 5: The Trust Machine (Security & Cryptography)
*Estimasi: 6 - 8 Jam Pembelajaran Aktif*

Mengerti matematika perlindungan rahasia dan verifikasi integritas data.

* **Invarian CS Fundamental**:
  - **One-Way Functions (Cryptographic Hashing)**: Sifat deterministik, resistan terhadap collision, dan efek avalanche.
  - **Adaptive Work Factor & Salt**: Mengapa algoritma seperti Bcrypt/Argon2 sengaja dibuat boros CPU/RAM untuk menangkal serangan ASIC/GPU dan Rainbow Table.
  - **Digital Signatures (HMAC / Asymmetric Signatures)**: Membuktikan data tidak diubah pihak ketiga tanpa harus menyimpan salinannya.
  - **The Stateless Revocation Paradox**: Trade-off antara skalabilitas token stateless dengan ketidakmampuan mencabut akses secara instan.
* **Jangkar di `expense-tracker`**:
  - `auth.controller.ts`: `bcrypt.hash(password, 10)` dan `jwtGenerator(newUser.id)`.
* **Uji Verifikasi Mandiri**:
  - *Mengapa kita tidak boleh mengenkripsi password dengan AES-256 (two-way), melainkan harus menggunakan One-Way Hashing dengan Salt?*

---

## ⚓ Metodologi Belajar: The Submarine Method & 2-Layer Rule

Saat mempelajari roadmap ini sambil menjalankan ritme [[Learning Schedules]]:

1. **Top-Down Hook (Jangkar Fitur)**: Ambil mikro-tugas dari [[backlog-fitur]], lalu kerjakan di proyek.
2. **Deep Drill-Down**: Saat penasaran dengan mekanismenya, gunakan:
   - `extract: <file>` untuk memetakan layer abstraksi.
   - `mentor: <topik>` untuk berdiskusi secara Sokrates.
3. **The 2-Layer Rule**: Maksimal turun 2 level di bawah layer masalah aktif. Jangan turun ke level semikonduktor/assembly kecuali itu tujuan riset Anda.
4. **Hands-on TDD Gym**: Gunakan `lab: webdev <topik>` untuk membuktikan teori sampai tes berwarna **Hijau**.
5. **Synthesis**: Tuliskan model mental Anda di `notes/webdev/` dan hubungkan dengan `[[wikilinks]]`.
