---
title: Database Migrations
domain: webdev
tags:
  - webdev
  - database
  - migrations
  - architecture
  - zero-downtime
related:
  - "[[production-grade-anatomy]]"
  - "[[First Principles coding]]"
---

# 🗄️ Database Migrations

Sebuah prosedur bagaimana caranya kita mengubah suatu desain data tanpa mengganggu stabilitas suatu sistem, dimana database tersebut sudah digunakan oleh banyak pengguna.

## Kenapa perlu migrasi
Database ini bersifat **stateful** –punya memori yang merupakan penghuni dari suatu sistem. Sehingga, ketika terjadi perubahan schema, kita perlu memikirkan cara bagaimana kita renovasi ulang database kita tanpa mengganggu penghuni yang ada di dalamnya.

## How to do that?
1. **Schema as code**: Perubahan skema ditulis secara bertahap eksplisit dalam codebase. Example
	```plain
	migrations/
  ├── 001_create_users_table.sql
  ├── 002_add_phone_number_to_users.sql
  └── 003_create_orders_table.sql
	```
2. **Table Metadata**: Sebuah table khusus –seperti logbook, untuk mencatat perubahan skema yang sudah dieksekusi di database
3. **Otomatisasi**: tool migrasi (like drizzle) akan menjalankan file-file yang belum tercatat di metadata

## Implementation: Expand and Contract Technique
**Study Case**: Aku ingin merubah kolom `name` menjadi `full_name` pada database yang sudah live productions

### What's suppose to do
1. **Buat 2 versi server**
	V1: untuk server lama yang masih menggunakan kolom `name`
	V2: untuk server baru yang menggunakan kolom `full_name` dan tetap ada `name`
2. **Kolom baru wajib nullable! Hear me out**
	soalnya di V1 ini blom ada kodingan untuk gunain kolom `full_name`, jadinya kolom baru  perlu nullable dulu, karena dari load balancer nanti beberapa user akan dibagi ke 2 server
3. **Mulai migrasi data lama ke kolom baru**:
	1. Salin data `name` ke kolom baru `full_name`
	2. Mulai deploy server V2
	3. Setelah dipastikan semua data di `name` sudah ada di `full_name`, server V1 dimatikan sepenuhnya
4. **Bersihkan data lama (Contract)**
	setelah dipastikan semua kode tidak ada yang menggunakan kolom `name`, kolom tersebut boleh didrop di database

---

## 🔗 Catatan Terkait
- [[production-grade-anatomy]] — Pondasi database, persistensi data, dan arsitektur zero-downtime.
- [[First Principles coding]] — Prinsip memecah sistem hingga ke batas invarian fundamental.