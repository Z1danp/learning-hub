# 🛡️ Sparring Record: Auth Schema Architecture & Invariants

- **Project**: `projects/valid-ex`
- **Topic**: Single-Table Auth Architecture (Local Email/Password + Google OAuth)
- **Decision**: **Opsi 1 (Pragmatic Single-Table dengan DB Check Constraint)**
- **Target DB**: Neon Serverless PostgreSQL via Drizzle ORM

---

## 1. Context & Dilemma

Aplikasi Valid-Ex membutuhkan dua pintu masuk autentikasi:
1. **Registrasi Manual**: Email + Password.
2. **Google OAuth**: Single Sign-On (SSO) via Google identity provider.

### Dilemma
Apakah membuat kolom `password_hash` menjadi `NULL` cukup aman untuk akun OAuth?

---

## 2. Identified Vulnerabilities (Murphy's Law Red-Team)

1. **Bypass Null Password**:
   Jika request login manual mengirim `{ email: "...", password: null }` atau string kosong, tanpa pengecekan ketat `if (!user.passwordHash)`, bcrypt bisa mengalami error atau bypass logika pada implementasi naif.
2. **Account Takeover / Collision Attack**:
   Pengguna mendaftar dengan Google (`user@lab.com`), kemudian pihak ketiga mendaftar manual dengan email yang sama (`user@lab.com`) dan password sembarang. Jika tidak divalidasi, data akun berisiko tertimpa atau dibajak.

---

## 3. Decided Architectural Invariant (Option 1)

Menggunakan **satu tabel `users`** yang dipagari oleh **PostgreSQL Check Constraint**:

```typescript
// Drizzle ORM Schema
import { pgTable, uuid, varchar, text, timestamp, check } from 'drizzle-orm/pg-core';
import { sql } from 'drizzle-orm';

export const users = pgTable('users', {
  id: uuid('id').defaultRandom().primaryKey(),
  email: varchar('email', { length: 255 }).notNull().unique(),
  name: varchar('name', { length: 255 }).notNull(),
  avatarUrl: text('avatar_url'),
  passwordHash: text('password_hash'),
  authProvider: varchar('auth_provider', { length: 50 }).notNull().default('local'),
  googleId: varchar('google_id', { length: 255 }).unique(),
  createdAt: timestamp('created_at', { withTimezone: true }).defaultNow().notNull(),
  updatedAt: timestamp('updated_at', { withTimezone: true }).defaultNow().notNull(),
}, (table) => [
  check('check_password_for_local_auth', sql`
    (${table.authProvider} = 'local' AND ${table.passwordHash} IS NOT NULL) OR
    (${table.authProvider} != 'local')
  `)
]);
```

### Business Rules di Express Gateway:
- Jika login manual (`/api/auth/login`) dipanggil untuk akun dengan `authProvider !== 'local'`, tolak dengan HTTP 400: *"Akun ini terdaftar via Google. Silakan login menggunakan Google."*
- Jika pengguna mencoba mendaftar manual dengan email yang sudah ada via Google, tolak dengan HTTP 409 Conflict: *"Email sudah terdaftar menggunakan Google OAuth."*
