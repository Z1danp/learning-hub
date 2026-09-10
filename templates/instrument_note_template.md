---
title: {{TITLE}}
domain: {{DOMAIN}} # analytical_chemistry
technique: icp-ms # icp-ms | gc-ms | hplc | aas
tags:
  - instrument
  - first-principles
  - analytical-chemistry
date: {{DATE}}
status: in-progress # in-progress | reviewed | mastered
related:
  - "[[analytical-chemistry-roadmap]]"
---

# {{TITLE}}

> **One-Sentence Core Phenomenon:**  
> *(Tuliskan prinsip fisika/kimia utama instrumen ini dalam 1 kalimat padat)*

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
- **Spesies Pengganggu**: *(contoh: $^{40}\text{Ar}^{16}\text{O}^+$ pada $^{56}\text{Fe}^+$, atau $^{40}\text{Ar}^{35}\text{Cl}^+$ pada $^{75}\text{As}^+$)*
- **Mekanisme Eliminasi**: *(KED mode dengan gas He / Reaction Cell dengan gas reaksi $H_2, O_2, NH_3$)*

### B. Interferensi Non-Spektral (Efek Matriks & Fisik)
- **Gejala**: *(Penurunan sinyal internal standard, pendinginan plasma oleh pelarut organik)*
- **Mitigasi**: *(Pengenceran, matrix matching, metode penambahan standar / MSA)*

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
*(Bagian ini untuk mencatat hasil diskusi `@mentor` atau `@falsify`)*
- [ ] Konsep fundamental yang sudah divalidasi
- [ ] Pertanyaan terbuka / misteri data lab hari ini
- [ ] Tautan konsep: [[icp-ms-core]] | [[quadrupole-mass-filter]] | [[qa-qc-validation]]
