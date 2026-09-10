# 🔐 Backend Authentication (BE-Auth) — Deep Architecture & Mental Model

Dokumentasi ini disusun untuk membedah seluruh sistem autentikasi backend pada `projects/expense-tracker/apps/server/src/features/auth` dan `middlewares/auth.middleware.ts`. 

Tujuannya bukan sekadar menjelaskan baris kode secara pasif, melainkan memberikan **peta mental *first-principles***: mengapa kode ini dirancang seperti ini, apa mekanika di balik layarnya (dari layer HTTP hingga kriptografi), serta **titik-titik kritis (*edge cases*)** untuk melatih daya analisis dan berpikir kritismu.

---

## 🧭 Peta Alur Arsitektur (End-to-End Flow)

Sistem autentikasi ini menggunakan arsitektur **Stateless Token-Based Authentication** yang disalurkan melalui **HTTP-Only Cookies**.

```mermaid
sequenceDiagram
    autonumber
    actor Client as Client (React / Browser)
    participant Server as Express Server
    participant Zod as Zod Schema (Validation)
    participant DB as Neon PostgreSQL (Drizzle)
    participant Crypto as Bcrypt & JWT Engine

    %% REGISTER FLOW
    rect rgb(240, 248, 255)
    note right of Client: 1. Alur Registrasi Akun Baru
    Client->>Server: POST /api/v1/auth/register (name, email, password)
    Server->>Zod: safeParse(req.body)
    alt Validasi Gagal
        Zod-->>Server: Error format issues
        Server-->>Client: 422 Unprocessable Entity
    else Validasi Berhasil
        Server->>DB: SELECT user WHERE email = input.email
        alt Email Sudah Ada
            DB-->>Server: existingUser found
            Server-->>Client: 409 Conflict ("Email already registered")
        else Email Tersedia
            Server->>Crypto: bcrypt.hash(password, 10)
            Crypto-->>Server: passwordHash ($2b$10$...)
            Server->>DB: INSERT INTO users ... RETURNING id, name, email
            DB-->>Server: newUser (id: UUID)
            Server->>Crypto: jwt.sign({ userId }, JWT_SECRET, 7d)
            Crypto-->>Server: token string
            Server-->>Client: 201 Created + Set-Cookie: token=...; HttpOnly; SameSite=Strict
        end
    end
    end

    %% LOGIN FLOW
    rect rgb(245, 255, 245)
    note right of Client: 2. Alur Login Pengguna
    Client->>Server: POST /api/v1/auth/login (email, password)
    Server->>Zod: safeParse(req.body)
    Server->>DB: SELECT user WHERE email = input.email
    alt User Tidak Ditemukan
        Server-->>Client: 401 Unauthorized ("Invalid email or password")
    else User Ditemukan
        Server->>Crypto: bcrypt.compare(password, user.password_hash)
        alt Password Salah
            Crypto-->>Server: false
            Server-->>Client: 401 Unauthorized ("Invalid email or password")
        else Password Cocok
            Crypto-->>Server: true
            Server->>Crypto: jwt.sign({ userId: user.id }, JWT_SECRET, 7d)
            Server-->>Client: 200 OK + Set-Cookie: token=...; HttpOnly; SameSite=Strict
        end
    end
    end

    %% PROTECTED ROUTE FLOW
    rect rgb(255, 250, 240)
    note right of Client: 3. Pengawalan Rute Terproteksi (/me, /accounts, dll)
    Client->>Server: GET /api/v1/auth/me (Cookie: token=...)
    Server->>Server: authMiddleware(req, res, next)
    alt Cookie Tidak Ditemukan
        Server-->>Client: 401 Unauthorized
    else Cookie Ada
        Server->>Crypto: jwt.verify(token, JWT_SECRET)
        alt Signature Palsu / Kadaluarsa
            Server-->>Client: 401 Unauthorized ("Invalid or token expired")
        else Token Valid
            Server->>Server: req.userId = payload.userId
            Server->>Server: next() -> Handler Eksekusi Bisnis
            Server-->>Client: 200 OK (Data user terverifikasi)
        end
    end
    end
```

---

## 🔬 Dekonstruksi Submarine (The 3 Layers)

Untuk memahami kode secara mendalam, kita membedahnya ke dalam 3 lapisan abstraksi:

```
┌────────────────────────────────────────────────────────┐
│ Layer  0: Express Router, Zod SafeParse, Drizzle ORM   │ (Surface Code)
├────────────────────────────────────────────────────────┤
│ Layer -1: Bcrypt Hashing, Event Loop, JWT Verification │ (Runtime & CS)
├────────────────────────────────────────────────────────┤
│ Layer -2: HTTP Cookies (HttpOnly/SameSite), DB Indexes │ (Protocol & OS)
└────────────────────────────────────────────────────────┘
```

### 1. Layer 0: Surface & Framework APIs
* **Zod Runtime Type Contract**: `registerSchema.safeParse(req.body)`. TypeScript hanya memeriksa tipe saat *compile-time*, sedangkan Zod memvalidasi payload saat *runtime* sebelum data menyentuh database.
* **Drizzle ORM Querying**: Menggunakan method chaining type-safe `db.select().from(users).where(eq(users.email, email))`. Menghasilkan prepared statement SQL yang kebal terhadap *SQL Injection*.
* **Express Request Lifecycle**: Pemanfaatan `next()` di middleware sebagai *gatekeeper* agar handler bisnis hanya memproses request yang sudah terjamin identitasnya.

### 2. Layer -1: Runtime & Mekanika Komputasi (Node.js & Kriptografi)
* **Bcrypt Work Factor (Salt Rounds = 10)**:
  Bcrypt sengaja dirancang **lambat secara komputasi** (*adaptive cost function*). Algoritma ini berjalan sebanyak $2^{10} = 1.024$ iterasi hashing menggunakan Blowfish cipher. Tujuannya adalah memitigasi serangan *brute-force* dan *hardware-accelerated cracking* (GPU/ASIC).
* **Asinkron (`await bcrypt.hash`) vs Event Loop**:
  Bcrypt memanfaatkan `libuv threadpool` di balik layar Node.js. Menggunakan versi *async* memastikan komputasi hashing yang berat tidak memblokir (*non-blocking*) *main thread* event loop Express.
* **Mekanika JWT (JSON Web Token)**:
  JWT terdiri dari 3 bagian: `Base64Url(Header).Base64Url(Payload).Signature`.
  $$\text{Signature} = \text{HMAC-SHA256}(\text{Header} + "." + \text{Payload}, \text{JWT\_SECRET})$$
  Server tidak perlu menyimpan sesi di database/RAM (*stateless*). Server cukup memverifikasi matematis apakah `Signature` valid menggunakan rahasia `JWT_SECRET`.

### 3. Layer -2: Protokol Jaringan & Keamanan Browser (HTTP Headers)
* **Penyimpanan Token: HttpOnly Cookie vs LocalStorage**:
  * **Masalah LocalStorage**: Kode JavaScript apapun (termasuk script jahat dari library pihak ketiga atau serangan XSS) bisa membaca `localStorage.getItem('token')`.
  * **Solusi HttpOnly Cookie**: Browser melarang JavaScript mengakses `document.cookie`. Cookie otomatis dilampirkan oleh browser di header request HTTP setiap kali memanggil origin server.
* **Flag Keamanan Cookie**:
  * `httpOnly: true`: Mencegah pencurian token lewat XSS.
  * `secure: process.env.NODE_ENV === 'production'`: Hanya mengirimkan cookie jika koneksi menggunakan protokol terenkripsi HTTPS (mencegah *Man-In-The-Middle attack* pada jaringan publik).
  * `sameSite: 'strict'`: Melindungi dari serangan CSRF (*Cross-Site Request Forgery*). Browser menolak mengirim cookie jika request dipicu dari domain luar.

---

## 📂 Bedah File & Tanggung Jawab Desain

### 1. `apps/server/src/types/express.d.ts` (TypeScript Declaration Merging)
```typescript
import 'express';

declare global {
    namespace Express {
        interface Request {
            userId?: string
        }
    }
}
```
* **Maksud & Tujuan**: Secara default, objek `req` bawaan Express tidak memiliki properti `userId`. Melalui *declaration merging*, kita memperluas interface `Express.Request` agar TypeScript mengizinkan `req.userId` diakses secara type-safe di seluruh controller setelah diverifikasi middleware.

---

### 2. `apps/server/src/features/auth/auth.schema.ts` (Validasi Input Fail-Fast)
```typescript
import { email, z } from 'zod';

export const registerSchema = z.object({
  name: z.string({ message: 'Name is required' }).min(2, 'Name at least 2 characters').max(255),
  email: z.email({ message: 'Email is required' }),
  password: z.string({ message: 'Password is required' }).min(8, 'Password at least 8 characters'),
});
```
* **Maksud & Tujuan**: Menerapkan prinsip *fail-fast*. Jika format data salah (misal password kurang dari 8 karakter atau bukan email valid), request langsung ditolak di boundary controller sebelum membuang resource komputasi query database atau hashing bcrypt.

---

### 3. `apps/server/src/features/auth/auth.controller.ts` (Orkestrasi Logika Bisnis)

#### A. Helper `jwtGenerator`
```typescript
const jwtGenerator = (userId: string) => {
  const jwtSecret = process.env.JWT_SECRET;
  if (!jwtSecret) {
    throw new Error('JWT_SECRET is not configured in .env');
  }
  return jwt.sign({ userId }, jwtSecret, { expiresIn: '7d' });
};
```
* **Maksud & Tujuan**: Sentralisasi pembuatan token. Membawa payload seminimal mungkin (`userId` saja), menghindari penyimpanan informasi sensitif atau data yang sering berubah (seperti role/nama) di dalam token.

#### B. Handler `register`
1. **Validasi Skema**: Memeriksa kelayakan input. Jika gagal, memformat issues menjadi format standar `ValidationErrorResponse` (HTTP 422).
2. **Cek Duplikasi Email**: Melakukan query pengecekan keberadaan user. Jika ditemukan, lempar HTTP 409 Conflict.
3. **Hashing Password**: Mengubah plaintext menjadi hash salted dengan cost factor 10.
4. **Insert Database & Returning**: Menyimpan data user baru ke PostgreSQL, mengembalikan field non-sensitif (tanpa `password_hash`).
5. **Issue Cookie & Response**: Membuat JWT, memasukkannya ke HttpOnly cookie, dan mengembalikan HTTP 201 Created.

#### C. Handler `login`
1. **Validasi Format Input**: Memastikan email dan password dikirimkan sesuai format.
2. **Pencarian Identitas**: Mengambil baris record berdasarkan email.
3. **Komparasi Kriptografis (`bcrypt.compare`)**: Menghindari *Timing Attacks* (komparasi waktu konstan).
4. **Penerbitan Sesi**: Memasang cookie token baru berdurasi 7 hari dan mengembalikan profil pengguna (HTTP 200 OK).

---

### 4. `apps/server/src/middlewares/auth.middleware.ts` (Penjaga Pintu Masuk / Guard)
```typescript
export const authMiddleware = (req: Request, res: Response<ApiErrorResponse>, next: NextFunction) => {
  const token = req.cookies?.token;
  if (!token) {
    return res.status(401).json({ success: false, message: 'Unauthorized' });
  }

  try {
    const jwtSecret = process.env.JWT_SECRET;
    if (!jwtSecret) {
      return res.status(500).json({ success: false, message: 'Internal server error' });
    }
    const decode = jwt.verify(token, jwtSecret);

    // Type-guarding runtime payload
    if (typeof decode === 'string' || !decode || typeof decode.userId !== 'string') {
      return res.status(401).json({ success: false, message: 'Invalid or token expired' });
    }

    req.userId = decode.userId;
    next();
  } catch (error) {
    return res.status(401).json({ success: false, message: 'Invalid or token expired' });
  }
};
```
* **Maksud & Tujuan**:
  * Mengisolasi logika verifikasi token agar tidak perlu diulang-ulang di setiap route/controller.
  * Mencegah payload palsu dengan *type-guarding* runtime (`typeof decode.userId === 'string'`).
  * Menyuntikkan `req.userId` sebagai konteks autentikasi untuk handler downstream.

---

## 🧠 Arena Berpikir Kritis & Bahan Uji (Falsification Lab)

Gunakan daftar ini untuk menguji dan mengasah pemahaman kritismu terhadap kode yang telah dibuat:

### 🥊 Tantangan 1: Race Condition pada Registrasi (Check-Then-Act Flaw)
* **Kondisi Kode Saat Ini**:
  ```typescript
  const [existingUser] = await db.select().from(users).where(eq(users.email, email));
  if (existingUser) return res.status(409)...
  // ... kemudian insert
  await db.insert(users)...
  ```
* **Pertanyaan Kritis**:
  *Apa yang terjadi jika ada 2 request registrasi dengan email persis sama masuk bersamaan dalam rentang selisih 2 milidetik?*
* **Realita Lapisan Database**:
  Kedua request akan sama-sama membaca `existingUser = undefined`, lalu keduanya lanjut melakukan `db.insert(...)`. Di sini database PostgreSQL kamu akan menolak request kedua karena *Unique Constraint* (`email: varchar().unique()`). Namun karena controller tidak menangani error duplikasi constraint secara spesifik di blok `catch`, request kedua akan jatuh ke `500 Internal Server Error`, bukan `409 Conflict`.
* **Uji Hipotesis**: Bagaimana cara menangani *unique violation error code* PostgreSQL (kode `23505`) di blok `catch` atau menggunakan klausa `INSERT ... ON CONFLICT DO NOTHING`?

---

### 🥊 Tantangan 2: Dilema Stateless JWT Revocation (The Invalidation Problem)
* **Kondisi Kode Saat Ini**:
  Token JWT berlaku valid selama 7 hari (`expiresIn: '7d'`).
* **Pertanyaan Kritis**:
  *Jika akun seorang user diretas hari ini, atau user mengganti password-nya, bagaimana cara server membatalkan (*revoke*) token lama yang masih beredar sebelum masa 7 hari habis?*
* **Realita Arsitektur**:
  Karena JWT bersifat *stateless* (server tidak mengecek DB setiap ada request di middleware), server **tidak bisa** membatalkan token tersebut secara sepihak kecuali kamu menerapkan:
  1. *Token Blacklist* di memory cache (Redis) dengan TTL sesuai sisa expiry.
  2. Atau memperpendek umur Access Token (misal: 15 menit) dan menyertakan Refresh Token tersimpan di DB.

---

### 🥊 Tantangan 3: Rute Logout & Session Termination
* **Kondisi Kode Saat Ini**:
  Di `auth.routes.ts`, rute yang ada baru `/register`, `/login`, dan `/me`.
* **Pertanyaan Kritis**:
  *Bagaimana cara mengimplementasikan endpoint `/logout` dengan arsitektur HttpOnly cookie saat ini?*
* **Konsep Solusi**:
  Karena browser melarang JavaScript menghapus HttpOnly cookie secara langsung via `document.cookie = ''`, server harus merespons dengan header `Set-Cookie` yang menginstruksikan penghapusan:
  ```typescript
  res.clearCookie('token', {
    httpOnly: true,
    sameSite: 'strict',
    secure: process.env.NODE_ENV === 'production',
  });
  ```

---

## 📋 Ringkasan Keputusan Desain (Design Trade-offs)

| Aspek Desain | Pilihan yang Diambil | Alternatif Lain | Alasan / Trade-off |
| :--- | :--- | :--- | :--- |
| **Penyimpanan Sesi** | Stateless JWT | Session ID di Redis/DB | Lebih ringan tanpa overhead lookup DB tiap request, tetapi lebih sulit melakukan pembatalan sesi instan. |
| **Transport Token** | HttpOnly Cookie | Bearer Authorization Header | Kebal terhadap pencurian token via serangan XSS; membutuhkan konfigurasi CORS `credentials: true`. |
| **Password Hashing** | Bcrypt (Cost 10) | Argon2id / PBKDF2 / SHA-256 | Bcrypt adalah standar industri battle-tested dengan proteksi brute force yang terukur; SHA-256 murni terlalu cepat dan rentan terhadap rainbow tables. |
| **Validasi Input** | Zod Schema Runtime | Manual checking / Interface saja | Menjamin runtime data sesuai tipe dan memberikan pesan validasi terstruktur (HTTP 422). |
