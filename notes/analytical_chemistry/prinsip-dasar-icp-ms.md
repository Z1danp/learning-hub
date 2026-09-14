---
title: Prinsip Dasar ICP MS
domain: analytical_chemistry # analytical_chemistry
technique: icp-ms # icp-ms | gc-ms | hplc | aas
tags:
  - instrument
  - first-principles
  - analytical-chemistry
date: 2026-09-10
status: in-progress # in-progress | reviewed | mastered
related:
  - "[[icp-ms-learning-roadmap]]"
---

# Prinsip Dasar ICP MS

> **One-Sentence Core Phenomenon:**  
> ICP-MS mengonversi analit cair menjadi ion positif monoatomik via plasma Argon bersuhu ekstrem (~6.000–10.000 K), mendiskriminasi interferensi poliatomik secara fisik melalui sel kolisi/reaksi, dan memilah massa berdasarkan rasio $m/z$ dalam osilasi medan dinamis RF dan statis DC Quadrupole.

---

## 1. Submarine Deconstruction (Alur Fisika Instrumen)

| Layer | Komponen / Fase | Fenomena yang Terjadi | Parameter Kritis |
| :--- | :--- | :--- | :--- |
| **Layer 0** (SOP / Operasional) | Preparasi & Injeksi | Digest asam ($HNO_3$), pompa peristaltik, autosampler | Kecepatan pompa, kebersihan vial, TDS $< 0.2\%$ |
| **Layer -1** (Instrument Mechanics) | Ionisasi & Transmisi | Nebulizer $\to$ Spray Chamber $\to$ Torch Plasma $\to$ Cones $\to$ Lensa $\to$ Quadrupole $\to$ Detektor | Laju alir gas nebulizer ($Ar$), daya RF (W), voltase lensa, vakum |
| **Layer -2** (Atomic/Physical Chem) | Fisika Atomik & Dinamika Ion | Atomisasi thermal, ionisasi plasma ($Ar^+ = 15.76\text{ eV}$), *space-charge effect*, kestabilan Mathieu ($m/z$) | Energi ionisasi pertama, penampang tabrakan ion (*cross-section*) |

---

## 2. Interferensi & Strategi Mitigasi

### A. Interferensi Spektral (Isobarik, Poliatomik, Doubly Charged)
- **Spesies Pengganggu**: $^{40}\text{Ar}^{16}\text{O}^+$ pada $^{56}\text{Fe}^+$, $^{40}\text{Ar}^{35}\text{Cl}^+$ pada $^{75}\text{As}^+$, $^{136}\text{Ba}^{2+}$ pada $^{68}\text{Zn}^+$. Detail mendalam: [[icp-ms-interferensi-dan-qcell-ked]].
- **Mekanisme Eliminasi**:
  - He-KED Mode dengan barier potensial energi kinetik (memanfaatkan ukuran penampang lintang $\sigma_{coll}$ poliatomik yang lebih bongsor).
  - Reaction Cell Mode dengan *mass-shift* kimia fase gas ($O_2, H_2, NH_3$).

### B. Interferensi Non-Spektral (Efek Matriks & Fisik)
- **Gejala**: Penurunan sinyal internal standard, pendinginan plasma oleh asam berlebih atau pelarut organik, penyumbatan cone oleh garam terlarut (TDS $> 0.2\%$).
- **Mitigasi**: Pengenceran (*dilution*), *matrix matching*, metode penambahan standar (*standard addition* / MSA).

---

## 3. Protokol QA/QC & Kriteria Keberterimaan

- **Kurva Kalibrasi**: Koefisien determinasi ($R^2 \ge 0.995$), evaluasi residual.
- **Internal Standard (IS)**: Toleransi rentang intensitas ($70\% - 130\%$ dari *calibration blank*).
- **Quality Control (QC)**:
  - Calibration Blank / Method Blank: $< \text{MDL}$
  - Initial / Continuing Calibration Verification (ICV / CCV): Recovery $90\% - 110\%$
  - Matrix Spike (MS / MSD): Recovery $75\% - 125\%$, RPD $\le 20\%$
- **Sensitivitas & Deteksi**:
  $$\text{LOD} = 3 \times \frac{\sigma_{\text{blank}}}{m}, \quad \text{LOQ} = 10 \times \frac{\sigma_{\text{blank}}}{m}$$

---

## 4. Troubleshooting & Falsification Lab (Analisis Gangguan)

| Gejala Gangguan | Hipotesis Penyebab (Root Cause) | Uji Diagnostik / Solusi |
| :--- | :--- | :--- |
| Sensitivitas drop drastis | Orifice *skimmer/sample cone* kotor/tersumbat | Cek tekanan vakum & inspeksi fisik ujung cone |
| Sinyal internal standard melayang (*drifting*) | Nebulizer tersumbat sebagian / peristaltic tube aus | Ganti selang pompa peristaltik, cuci nebulizer |
| Oksida ratio tinggi ($CeO^+/Ce^+ > 2\%$) | Aliran gas carrier nebulizer terlalu tinggi / plasma dingin | Tune ulang laju alir gas argon atau naikkan daya RF |

---

## 5. Sparring Notes & Catatan Mentor
*(Hasil dekonstruksi first-principles bersama mentor):*
- [x] **Disparitas Eksitasi & Ionisasi**: [[perbandingan-spektrometri-emisi-dan-massa]] (Eksitasi Boltzmann ICP-OES vs Ionisasi Saha ICP-MS vs Tembakan Kinetik GC-MS 70 eV).
- [x] **Dinamika Sel Kolisi & Flatapole**: [[icp-ms-interferensi-dan-qcell-ked]] (Dimensi spasial poliatomik vs monoatomik, trade-off STD vs KED, dan LMCO dinamis).
- [x] **Mekanika Gerak Quadrupole**: [[mekanika-quadrupole-rf-dc]] (Inersia belokan, osilasi RF vs tarikan DC, resonansi parametrik pada sumbu DC positif).
