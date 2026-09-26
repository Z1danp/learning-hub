## Spec & Invariant First
Sebelum memulai membuat suatu website, perlu dibuat suatu invariants, yaitu aturan mutlak yang tidak boleh dilanggar dalam kondisi apapun. Selain itu perlu dibuatkan dokumentasi dalam bentuk **living architecture decisions (ADR)** dan **type contracts / schemas**

## Red Team / Hackers

The methods:
1. Aku merancang suatu draf skema atau logicnya
2. Aku menginstruksikan AI untuk menguji draf aku dengan skeptis. (mungkin aku perlu mempelajari beberapa pengujian basics di setiap tahapan untuk membuat sesuatu), as example:
	> Ini rancangan alur transaksi yang saya buat. Posisikan dirimu sebagai senior security & database architect. Identifikasi 5 skenario konkurensi, race condition, atau edge-case kegagalan jaringan dimana rancangan ini akan korup atau gagal di level Layer -1 dan Layer -2
## Context Engineering yang Terstruktur (Machine-Readable Context)
- Simpan konteks sistem dalam dokumen deklaratif di workspaces (ex: `ARCHITECTURE.md`, `INVARIANTS.md`)
- Gunakan aturan tipe data yang ketat (*strict typescript* atau *Pydantic*) sebagai "pagar kawat  berduri". Jika AI menghasilkan kode yang melanggar tipe atau kontrak, *type checker* di IDE akan langsung menggagalkan sebelum aku sempat melihat.
---

# What Should I Have Learn To Understand This Framework

- [x] Living Architecture Decisions (ADR)
- [x] Basics unit testing, like apa saja possibility yang mungkin terjadi dalam traffic website (4 Vektor Kekacauan & Defense in Depth)
- [x] How to create declarative document (CONTEXT, INVARIANTS, SCHEMAS, ADR)
- [x] How to align context with AI (Machine-Readable Context & Single Source of Truth)
*(Catatan lengkap hasil pembelajaran dirangkum di [[notes/webdev/spec-invariants-dan-ai-alignment.md]])*

Kayanya ku perlu rearangge folder ini lagi. Rencananya ada notes untuk pemikiran aku sendiri, dan ada notes hasil generates AI. Nah, jadinya cara kerjanya tuh, aku buat input di notes pemikiran, argumen panjang or pertanyaan, apapun itu yang dihasilkan dari otak aku, kemudian aku ingin mengetes hasil pemikiran aku ke AI, agar aku bisa tahu apa saja trade-off dari decisions yang akan aku pilih nanti. Untuk sekarang aku bingung bagaimana cara mengelola folder dan bisa align dengan AI ini soalnya ini menurut aku second brains ini masih berantakan.

Oiyaa, aku juga pengen kayaa blue-print dari sebuah apps ini dikelompokkan sesuai dengan projectsnya, jadinya aku bisa gampang nunjukkin konteksnya ke AI, tapi tidak mengganggu untuk folder belajar aku seperti yang sedang aku pelajari sekarang ini yaitu ICP-MS. Jadinya tuh ada notes istilah, hasil pemikiran aku, sama dokumen deklaratif atau apapun itu untuk menunjukkan konteksnya ke AI. Soalnya aku juga pake dual-boot jadi, setidaknya AI tau konteks yang sedang aku kerjakan