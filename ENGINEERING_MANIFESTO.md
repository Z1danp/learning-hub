# 🧭 The Sovereign Engineer's Manifesto (Driver vs Navigator)

> "AI adalah akselerator sintaks dan penguji sistem, bukan pilot pemikiran arsitektural."

---

## 1. Golden Rule: Anti-Cognitive Outsourcing
- **Kamu adalah DRIVER**: Pemegang hukum kekekalan sistem (*Invariants*), logika bisnis, batasan matematika, dan pengambil keputusan.
- **AI adalah NAVIGATOR & RED TEAM**: Pembaca kendala fisik, pencari skenario kegagalan (*edge cases*), dan pengetik sintaks/tes boilerplate HANYA setelah kamu menentukan arah.
- **Waspada Ilusi Kompetensi**: Jangan memesan kode jadi. Kode yang sekadar jalan di `localhost` bukanlah bukti kamu paham arsitekturnya.

---

## 2. The 4-Step Socratic Engineering Loop (Mengatasi Paradoks Cold-Start)
Saat belum memiliki fundamental untuk fitur baru, JANGAN minta kode. Eksekusi 4 langkah ini:
1. **Injeksi Kendala Fisik (AI)**: Minta AI jelaskan apa yang terjadi di RAM (Layer -1), socket jaringan, disk I/O, atau DB (Layer -2), lalu minta 1 dilema arsitektur.
2. **Kepemilikan Hipotesis (Kamu)**: Analisis kendala tersebut, lalu rumuskan strategi dan aturan main (*invariants*).
3. **Falsifikasi & Red-Teaming (AI)**: Minta AI membantai idemu dengan skenario dunia nyata (*race condition*, *sudden crash*, koneksi lambat/putus).
4. **Scaffolding & Muscle Memory**: AI siapkan tes yang gagal (`Red`), kamu yang mengetik implementasi inti (`Green`).

---

## 3. Production-Grade Standard (Murphy's Law)
Sebuah web baru berstatus "Production-Grade" jika tahan banting terhadap:
- **Batas Memori**: Streaming payload besar vs buffering di RAM (hindari OOM).
- **Pembersihan Bersih**: Event abort pada socket + TTL-based reaper untuk file temporary.
- **Integritas State**: Transaksi ACID, idempotency key, penanganan *partial write*.
- **Observability**: Structured logging dengan Correlation ID, bukan `console.log` acak.

---

## 4. The 2-Layer Submarine Rule
- `Layer 0`: API Framework & UI (React, Express, FastAPI).
- `Layer -1`: Runtime & Memory (V8 Heap, Event Loop, Garbage Collector).
- `Layer -2`: Protokol OS & DB (TCP/IP, Socket State, Disk Inode, B-Tree).
- *Layer -3*: (Silikon/Gerbang Logika) $\rightarrow$ Catat di wishlist, jangan tenggelam terlalu jauh!

---

## ⚡ Formula Prompting Harian (Copy-Paste Ready):
> *"Aku mau bikin [FITUR]. Jangan beri kode dulu. Jelaskan kendala komputasi di Layer -1 dan Layer -2 (RAM, socket jaringan, DB) saat fitur ini berjalan, lalu berikan 1 dilema arsitektur untuk aku putuskan."*
