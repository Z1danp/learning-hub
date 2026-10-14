---
title: Interferensi Spektral dan Teknologi QCell KED pada ICP-MS
domain: analytical_chemistry
technique: icp-ms
tags:
  - analytical-chemistry
  - first-principles
  - icp-ms
  - collision-cell
  - interference
  - icap-q
date: 2026-09-13
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[perbandingan-spektrometri-emisi-dan-massa]]"
  - "[[mekanika-quadrupole-rf-dc]]"
---

# Interferensi Spektral dan Teknologi QCell KED pada ICP-MS

> **One-Sentence Core Phenomenon:**  
> Kuantifikasi akurat pada ICP-MS menuntut diskriminasi fisik terhadap ion poliatomik kembar ($m/z$ identik) menggunakan perbedaan penampang lintang tumbukan (*collision cross-section*) dan modulasi potensial sel Flatapole.

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena yang Terjadi | Parameter Kritis |
| :--- | :--- | :--- | :--- |
| **Layer 0** (SOP / Software) | Pemilihan Mode di Qtegra | Pemilihan mode `STD`, `KED`, atau `STD & KED` | Kurva kalibrasi, batas deteksi (LOD), konsentrasi analit |
| **Layer -1** (Instrument Hardware) | Flatapole QCell & Gas Kolisi | Injeksi gas Helium ($He$), tumbukan dengan ion poliatomik, filter tegangan *potential barrier* | Laju alir gas He ($\sim 4 - 5\text{ mL/min}$), voltase bias KED ($V$) |
| **Layer -2** (Atomic & Nuclear Physics) | Dimensi Geometri Ruang & Inersia | Penampang lintang tumbukan ($\sigma_{coll}$), jarak bebas rata-rata ($\lambda_{mfp}$), hukum rasio muatan ($m/z$) | Panjang ikatan kovalen diatomik ($r_e$), parameter kestabilan Mathieu ($q$) |

---

## 2. Hakikat Rasio Massa terhadap Muatan ($m/z$)

Spektrometer massa tidak pernah mengukur massa murni ($m$), melainkan rasio **$m/z$** karena defleksi gerak partikel bermuatan dalam medan elektromagnetik dikendalikan oleh:
$$a = \frac{F}{m} = \frac{(z \cdot e) \cdot E}{m} = e \cdot E \cdot \left(\frac{z}{m}\right) \implies \text{Radius Belokan} \propto \frac{m}{z}$$

```
[ Mobil Ringan: 68 kg ]  ──► Ditarik 1 Tali (Muatan +1) ──► Membelok dengan radius R
[ Truk Berat: 136 kg ]   ──► Ditarik 2 Tali (Muatan +2) ──► MEMBELOK SAMA TAJAMNYA (Radius R)!
```

### Fenomena Spesi *Doubly-Charged* ($M^{2+}$)
Jika suatu atom kehilangan dua elektron di plasma, nilai $z = 2$, sehingga massa terbaca di spektrum menjadi **setengah dari massa aslinya**:
* **$^{136}\text{Ba}^{2+}$:** $m/z = 136 / 2 = \mathbf{68} \longrightarrow$ menimpa analit Seng **$^{68}\text{Zn}^+$** ($m/z = 68/1 = 68$).
* **$^{46}\text{Ti}^{2+}$:** $m/z = 46 / 2 = \mathbf{23} \longrightarrow$ menimpa analit Natrium **$^{23}\text{Na}^+$** ($m/z = 23/1 = 23$).

---

### 3. Bahaya Latar Belakang: Interferensi Poliatomik

Pelarut ($H_2O$), asam digesti ($HNO_3, HCl$), dan gas plasma ($Ar$) bergabung membentuk ion molekuler pengganggu yang massanya persis sama dengan analit:

| Elemen Analit Target ($m/z$) | Pengganggu Poliatomik | Sumber Utama Matriks |
| :--- | :--- | :--- |
| **$^{56}\text{Fe}^+$** ($56$) | $^{40}\text{Ar}^{16}\text{O}^+$ | Plasma Argon + Pelarut Air |
| **$^{52}\text{Cr}^+$** ($52$) | $^{40}\text{Ar}^{12}\text{C}^+$ | Plasma Argon + Matriks Organik/Karbon |
| **$^{75}\text{As}^+$** ($75$) | $^{40}\text{Ar}^{35}\text{Cl}^+$ | Plasma Argon + Asam Klorida ($HCl$) |
| **$^{51}\text{V}^+$** ($51$) | $^{35}\text{Cl}^{16}\text{O}^+$ | Asam Klorida ($HCl$) + Air |
| **$^{39}\text{K}^+$** ($39$) | $^{38}\text{Ar}^{1}\text{H}^+$ | Plasma Argon + Pelarut Air |

> [!CAUTION]
> **Dampak pada Kuantifikasi:** Tanpa eliminasi, sinyal poliatomik menghasilkan **positif palsu (*false positive*)** pada blanko, dan derau tembakan (*Poisson shot noise* $\sigma \propto \sqrt{N}$) akan melipatgandakan nilai deviasi standar blanko sehingga merusak batas deteksi (LOD).

---

## 4. Dimensi Geometri Spasial: Monoatomik vs Poliatomik

Mengapa molekul poliatomik dapat disingkirkan secara fisik oleh gas Helium padahal massanya sama dengan analit?

```
[ Ion Monoatomik: 56Fe+ ]          [ Ion Poliatomik Dimer: 40Ar-16O+ ]
         ╭─────╮                         ╭─────╮     ╭─────╮
        │   +   │                       │  Ar   ├───┤   O   │
         ╰─────╯                         ╰─────╯     ╰─────╯
      1 Pusat Inti                         2 Pusat Inti + Panjang Ikatan
   Bentuk: Bola Simetris                 Bentuk: Lonjong (Dumbbell)
   Diameter: ~2.5 Å                      Panjang Rentang: ~4.5 - 5.0 Å
```

1. **Jumlah Inti Atom:** $^{56}\text{Fe}^+$ hanya memiliki 1 pusat inti bola padat ($d \approx 2.5\text{ Å}$). Sebaliknya, $[^{40}\text{Ar}^{16}\text{O}]^+$ memiliki **2 pusat inti** yang dipisahkan oleh ikatan kimia ($d \approx 4.5 - 5.0\text{ Å}$).
2. **Penampang Lintang Tumbukan (*Collision Cross-Section*, $\sigma_{coll}$):** Luas area efektif molekul poliatomik **$2 - 3\times$ lebih besar** dibanding monoatomik.
3. **Jarak Bebas Rata-rata ($\lambda_{mfp} = \frac{1}{n \cdot \sigma}$):** Karena $\sigma$ lebih besar, poliatomik menabrak atom Helium jauh lebih sering ($10 - 15\times$ tabrakan) dibanding ion monoatomik ($3 - 5\times$ tabrakan) di sepanjang lorong sel.

---

## 5. Rekayasa QCell Flatapole (Thermo Scientific iCAP Q)

```
[ Berkas Ion Masuk ] ──► [ Flatapole QCell berisi Gas Helium ] ──► [ Energy Barrier ] ──► [ Quadrupole ]
  - Fe+ (Monoatomik)       Sedikit bertumbukan -> E-kinetik tinggi       Lolos (Transmisi 20-50%)
  - ArO+ (Poliatomik)      Sering bertumbukan -> E-kinetik drop         Tertolak & Dibuang
```

### A. Mekanisme He-KED (*Kinetic Energy Discrimination*)
* Poliatomik kehilangan energi kinetik secara masif akibat frekuensi tumbukan tinggi.
* Di pintu keluar sel, dipasang elektroda voltase positif penghalang (**Potential Energy Barrier**).
* Ion poliatomik yang energinya sudah terkuras tidak sanggup mendaki *barrier* ini dan tertahan, sedangkan ion analit ($Fe^+$) yang masih lincah melenggang bebas ke quadrupole.

### B. Mode STD vs Mode KED (*The Trade-off*)
* **Mode STD (Tanpa Gas):** Transmisi ion $\approx 100\%$ (Sensitivitas puncak). Digunakan untuk unsur di zona massa bersih tanpa poliatomik ($m/z > 100$ seperti $^{208}\text{Pb}, ^{209}\text{Bi}, ^{238}\text{U}$) serta unsur sangat ringan ($^{7}\text{Li}, ^{9}\text{Be}$) yang rentan terhambur oleh Helium.
* **Mode KED (Dengan Gas Helium):** Sensitivitas analit turun $50\% - 80\%$ (karena sebagian ion monoatomik juga mengalami tabrakan acak), tetapi sinyal pengganggu poliatomik anjlok hingga **$99.999\%$**. Rasio sinyal terhadap derau ($S/N$) meningkat ribuan kali lipat.
* **Mengapa Hasil Konsentrasi Sampel Antara STD dan KED Terlihat Mirip?**  
  Karena penurunan transmisi dialami oleh larutan standar kalibrasi DAN larutan sampel secara bersamaan. Efek pemotongan intensitas ternormalisasi oleh kemiringan (*slope*) kurva kalibrasi.

### C. Tiga Keunggulan Desain *Flatapole* (Bilah Pelat Datar)
1. **Collisional Focusing:** Medan RF dari pelat datar mencekik berkas ion tepat ke tengah sumbu pipa sel, memadatkan berkas ion sebelum ditembakkan ke quadrupole.
2. **Dynamic Low-Mass Cut-Off (LMCO Dinamis):**
   * Berdasarkan parameter Mathieu $q \propto \frac{V_{RF}}{m}$.
   * Ketika mengukur $^{56}\text{Fe}$, flatapole menaikkan $V_{RF}$ untuk membuang semua prekursor ringan ($m/z < 39$) ke dinding agar tidak membentuk poliatomik baru di dalam sel.
   * Nilai *cut-off* ini bergeser secara dinamis mengikuti elemen target (misal saat membaca $^{23}\text{Na}$, ambang potong otomatis turun ke $m/z < 12$).
3. **Volume Mikro & Fast Gas Switching:** Rongga sel mini memungkinkan pergantian mode dari STD ke KED hanya dalam waktu $5 - 10\text{ detik}$, memungkinkan mode kombinasi otomatis `STD & KED` dalam satu siklus sampel.

---

## 6. Tautan Konsep Terkait
- Lanjut ke mekanika osilasi dan resonansi: [[mekanika-quadrupole-rf-dc]]
- Kembali ke perbandingan spektrometri: [[perbandingan-spektrometri-emisi-dan-massa]]
- Dokumen SOP & Troubleshooting: [[prinsip-dasar-icp-ms]]
