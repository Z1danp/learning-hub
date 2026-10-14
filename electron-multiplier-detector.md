---
title: Detektor Pengganda Elektron ICP-MS (Discrete Dynode Electron Multiplier, Dual-Mode Detection, dan Dead Time)
domain: analytical_chemistry
technique: icp-ms
tags:
  - analytical-chemistry
  - instrumentation
  - first-principles
  - electron-multiplier
  - discrete-dynode
  - pulse-counting
  - analog-mode
  - dead-time
  - icap-q
date: 2026-10-01
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-learning-roadmap]]"
  - "[[mekanika-quadrupole-rf-dc]]"
  - "[[ion-optics-and-space-charge]]"
  - "[[interface-cones-and-vacuum-mechanics]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
  - "[[icp-ms-tuning-qc-dan-lab-sparring]]"
---

# Detektor Pengganda Elektron ICP-MS (Discrete Dynode & Dual-Mode Detection)

> **One-Sentence Core Phenomenon:**  
> Detektor pengganda elektron diskrit (*discrete dynode electron multiplier*) adalah transduser kuantum-ke-elektronik yang mengatasi batas derau termal sirkuit dengan melipatgandakan tumbukan kation tunggal menjadi semburan puluhan juta elektron ($10^7 - 10^8\ e^-$) via emisi elektron sekunder bertingkat, serta menjembatani rentang konsentrasi dari $0{,}1\text{ ppt}$ hingga $> 100\text{ ppm}$ secara simultan melalui sadapan ganda *Pulse Counting* (anoda akhir) dan *Analog Mode* (dynode tengah).

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena Fisika / Mekanika yang Terjadi | Parameter Kritis & Batas Operasional |
| :--- | :--- | :--- | :--- |
| **Layer 0**<br>*(SOP Lab & Operasional)* | Software Pengendali (Qtegra), Kurva Kalibrasi Multi-orde, Cross-Calibration | Kalibrasi silang berkala kanal pulse-ke-analog, pengaturan tegangan tinggi detektor (*detector HV tuning*), evaluasi linearitas kurva ($R^2 \ge 0.995$) dari ppt ke ppm, pemantauan usia pakai (*detector aging*). | Rentang linear pulse ($0 - 10^6\text{ cps}$), rentang linear analog ($10^4 - 10^9\text{ cps}$), tegangan operasional detektor $-1.500\text{ V s.d. } -2.500\text{ V}$, dead time $\tau \approx 30 - 50\text{ ns}$. |
| **Layer -1**<br>*(Mekanika Komponen)* | Rantai Keping Dynode ($16 - 24$ tahap), Resistor Divider, Midpoint Tapping, Preamplifier Cepat, Diskriminator Digital | Kation dipercepat tegangan awal $-2.400\text{ V}$, elektron sekunder meloncat antar-dynode mengikuti tangga potensial $\Delta V \approx +100 - 150\text{ V}$, sadapan arus kontinu analog di dynode ke-8, pengumpulan pulsa arus diskrit di anoda akhir, pemotongan derau oleh *discriminator threshold*. | Faktor multiplikasi tahap ($\delta \approx 2 - 4$), gain total $G = \delta^n \approx 10^7 - 10^8$, kapasitas arus linier analog hingga miliampere, konstanta waktu preamplifier $\sim \text{nanodetik}$. |
| **Layer -2**<br>*(Fisika Kuantum & Statistik)* | Emisi Elektron Sekunder & Teori Probabilitas Deteksi | Transfer energi kinetik kation ke elektron valensi kisi logam, mengatasi fungsi kerja permukaan (*work function* $\Phi$), penguatan eksponensial kaskade ($G = \delta^n$), batas derau termal Johnson-Nyquist ($I_{\text{ion}} \sim 10^{-18}\text{ A} \ll I_{\text{noise}}$), tumpang tindih pulsa (*pulse pile-up*) dan statistik Poisson kedatangan partikel. | Muatan elementer $e = 1.602 \times 10^{-19}\text{ C}$, persamaan koreksi dead time ($N = N_0 / (1 - N_0 \tau)$), sebaran energi elektron sekunder ($1 - 5\text{ eV}$). |

---

## 2. Paradoks Fisika: Arus Sub-Attoampere vs. Derau Termal

Tantangan mendasar deteksi kation analit bermassa pada konsentrasi ultra-trace ($0{,}1\text{ ppt} = 0{,}0001\text{ ppb}$):

1. **Jumlah Ion:** Laju kedatangan kation analit dari quadrupole pada kadar trace hanya sekitar **$10$ ion per detik** ($10\text{ cps}$).
2. **Besaran Arus Fisik:**  
   Muatan satu kation tunggal adalah $e = 1{,}602 \times 10^{-19}\text{ Coulomb}$. Maka arus listrik total yang dihantarkan:
   $$I = \frac{\Delta Q}{\Delta t} = 10 \times 1{,}602 \times 10^{-19}\text{ C/s} \approx \mathbf{1{,}6 \times 10^{-18}\text{ Ampere (1,6 atto-ampere)}}$$
3. **Keterbatasan Sirkuit Konvensional (Batas Johnson-Nyquist):**  
   Arus sebesar $1{,}6\text{ aA}$ mustahil diukur oleh ammeter biasa karena fluktuasi termal acak elektron di dalam kabel tembaga (*thermal noise*):
   $$I_{\text{noise}} = \sqrt{\frac{4 k_B T \Delta f}{R}} \gg 10^{-15}\text{ A}$$
   Sinyal arus analit akan lenyap tertelan oleh derau sirkuit elektronik.

**Solusi Fisika:** Kation analit harus dilipatgandakan di dalam ruang vakum secara mekanik-kuantum **sebelum** menyentuh kabel rangkaian pengukur.

---

## 3. Mekanika Penggandaan Kaskade (*Secondary Electron Emission*)

Detektor modern menggunakan **Discrete Dynode Electron Multiplier** (rangkaian pelat logam berurutan berbahan paduan $Be-Cu$ atau lapisan film aktif dengan fungsi kerja rendah).

```
   Kation M⁺ (dari Quadrupole)
        │
        ▼
   [ Dynode 1 ] (-2.400 V)  ──► Tumbukan membebaskan 3 elektron sekunder (δ = 3)
        │
        ▼  (Ditarik oleh beda potensial ΔV = +150 V)
   [ Dynode 2 ] (-2.250 V)  ──► 3 elektron menabrak ──► membebaskan 9 elektron (3²)
        │
        ▼
   [ Dynode 3 ] (-2.100 V)  ──► 9 elektron menabrak ──► membebaskan 27 elektron (3³)
        │
       ...
        ▼
   [ Anoda Akhir ] (0 V Ground) ──► TSUNAMI ELEKTRON: G = δⁿ ≈ 3¹⁶ ≈ 43.000.000 e⁻!
```

### A. Emisi Elektron Sekunder di Dynode Pertama
- Kation analit dipercepat menuju *Dynode 1* oleh medan tegangan tinggi negatif (**$-2.000\text{ V s.d. } -2.500\text{ V}$**).
- Kation menabrak kisi atom logam dengan energi kinetik tinggi ($> 2\text{ keV}$). Energi ini ditransfer ke elektron-elektron valensi logam. Jika energi transfer melampaui fungsi kerja permukaan (*work function*), sejumlah elektron sekunder terlontar keluar ($\delta \approx 2 - 4$ elektron per tumbukan ion).

### B. Tangga Potensial Seri (*Voltage Divider Ladder*)
- Agar elektron sekunder tidak kembali ke dynode asal, dynode disusun seri dengan pembagi tegangan resistor.
- Tiap dynode berikutnya memiliki potensial yang **semakin positif** sebesar $\Delta V \approx +100\text{ s.d. } +150\text{ V}$:
  $$\text{Dynode 1 } (-2.400\text{ V}) \to \text{Dynode 2 } (-2.250\text{ V}) \to \dots \to \text{Anoda } (0\text{ V})$$
- Elektron bermuatan negatif secara alami melompat dan dipercepat menabrak dynode berikutnya, memicu penggandaan berantai secara eksponensial.

### C. Persamaan Penguatan Total (*Gain*, $G$)
Jika koefisien emisi elektron rata-rata per keping adalah $\delta$ dan jumlah keping adalah $n$ (biasanya $16 - 24$ dynode):
$$G = \delta^n$$
Untuk $\delta = 3$ dan $n = 16$:
$$G = 3^{16} \approx \mathbf{4{,}3 \times 10^7\text{ elektron}}$$
Satu kation tunggal menghasilkan paket arus berupa **puluhan juta elektron** dalam waktu $\sim 2 - 5\text{ nanodetik}$, memunculkan pulsa tegangan tajam ($\sim \text{milivolt}$) yang mudah dicacah oleh sirkuit digital *preamplifier*.

---

## 4. Arsitektur Sadapan Ganda Simultan (*Simultaneous Dual-Mode Detection*)

ICP-MS harus mampu mengukur konsentrasi trace ($0{,}1\text{ ppt} \to 10\text{ cps}$) sekaligus konsentrasi makro ($100\text{ ppm} \to 10^9\text{ cps}$) dalam satu sampel.

Jika 1 miliar ion ($10^9\text{ cps}$) digandakan penuh $10^7\times$, arus keluaran mencapai miliampere ($> 1\text{ mA}$), yang akan **membakar lapisan aktif dynode (*burnout*)** dan merusak instrumen.

```
   Ion M⁺ Masuk
        │
        ▼
   [ Dynode 1 - 7 ]  (Penggandaan Awal)
        │
        ├──────────────────────────► [ KANAL ANALOG (DC CURRENT) ]
        │                            Disadap dari Midpoint Dynode (Dynode ~8)
        ▼                            • Penguatan moderat ~10³ - 10⁴× (Aman dari Burnout)
   [ Dynode 8 - 16 ]                 • Mengukur konsentrasi tinggi: 10⁴ - 10⁹ cps
        │                            • Membaca arus kontinu proporsional
        ▼
   [ Anoda Akhir ] ────────────────► [ KANAL PULSE COUNTING (DIGITAL) ]
                                     Disadap dari Kolektor Akhir (Dynode ~16-24)
                                     • Penguatan penuh ~10⁷ - 10⁸×
                                     • Mengukur konsentrasi trace: 0 - 10⁶ cps
                                     • Menghitung pulsa diskrit (1 pulsa = 1 ion)
```

### A. Kanal Pulse Counting (Digital)
- **Titik Sadapan:** Anoda pengumpul akhir.
- **Prinsip Kerja:** Setiap pulsa voltase yang melampaui nilai ambang batas (*threshold discriminator*) dihitung sebagai 1 kejadian kedatangan ion.
- **Rentang Kerja:** **$0$ hingga $\sim 10^6\text{ cps}$** ($0{,}1\text{ ppt} - \text{sub-ppb}$).
- **Batas Kritis (*Dead Time Limitation*):** Di atas $10^6\text{ cps}$, pulsa saling bertumpuk (*pulse pile-up*), menyebabkan kejenuhan hitungan.

### B. Kanal Analog (Arus Kontinu)
- **Titik Sadapan:** **Dynode Tengah (*Midpoint Dynode*, misal dynode ke-8)**.
- **Prinsip Kerja:** Di dynode tengah, elektron baru digandakan sekitar $10^3 - 10^4\times$. Arus yang mengalir masih dalam orde mikroampere sehingga tidak merusak sistem. Arus kontinu ini diukur langsung oleh penguat DC (*linear DC amplifier*).
- **Rentang Kerja:** **$10^4$ hingga $\mathbf{10^9\text{ cps}}$** (puluhan ppb hingga $> 100\text{ ppm}$).

### C. Jembatan Kalibrasi Silang (*Cross-Calibration*)
- Pada daerah tumpang tindih (**$10^4 - 10^6\text{ cps}$**), kedua kanal aktif membaca sinyal secara simultan.
- Perangkat lunak instrumen (misal Qtegra) membandingkan rasio arus analog terhadap jumlah cacahan pulsa digital untuk menentukan faktor konversi yang presisi:
  $$\text{Faktor Konversi} = \frac{\text{Cacahan Pulse (cps)}}{\text{Arus Analog (\mu A)}}$$
- **Hasil Metrologis:** Instrumen memperoleh rentang dinamis linier kontinu sebesar **9 hingga 10 orde besaran ($0{,}1\text{ ppt} - 100\text{ ppm}$)** dalam satu kali pembacaan tanpa perlu injeksi ulang ([Robert Thomas, Bab 11, hal. 98–99](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners,%20Second%20Edition%20(Practical%20Spectroscopy)%20(2008,%20CRC%20Press)%20-%20libgen.li.pdf#page=124)).

---

## 5. Fenomena Waktu Mati (*Dead Time*) & Koreksi Non-Linearitas

Dalam mode *Pulse Counting*, setiap pulsa elektron membutuhkan waktu untuk mencapai puncak, meluruh, dan mereset sirkuit diskriminator.

Periode di mana detektor "buta" dan tidak mampu mendeteksi ion berikutnya disebut **Waktu Mati (*Dead Time*, $\tau$)**, bernilai sekitar **$30 - 50\text{ nanodetik}$** ([Robert Thomas, hal. 94](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners,%20Second%20Edition%20(Practical%20Spectroscopy)%20(2008,%20CRC%20Press)%20-%20libgen.li.pdf#page=120)).

```
   Pulsa 1 Masuk      Pulsa 2 Tiba di Periode Dead Time (HILANG!)
        ▲                        ▲
       ╱ ╲                      ╱ ╲
      ╱   ╲                    ╱   ╲
     ╱     ╲                  ╱     ╲
   ─┴───────┴────────────────┴───────┴──────────────► Waktu (t)
    │◄──────►│
    Dead Time (τ ≈ 35 ns) -> Detektor Buta Sesaat
```

### Formulasi Koreksi Dead Time
Jika laju cacahan terukur adalah $N_{\text{obs}}$ (cps), laju kedatangan ion sebenarnya ($N_{\text{true}}$) dikoreksi menggunakan model *non-paralyzable*:
$$N_{\text{true}} = \frac{N_{\text{obs}}}{1 - N_{\text{obs}} \cdot \tau}$$

- Pada $N_{\text{obs}} = 10.000\text{ cps}$ dan $\tau = 35\text{ ns}$:  
  $N_{\text{obs}} \cdot \tau = 0{,}00035$ (kehilangan hanya $0{,}035\%$, hampir linier sempurna).
- Pada $N_{\text{obs}} = 1.000.000\text{ cps}$ ($10^6\text{ cps}$):  
  $N_{\text{obs}} \cdot \tau = 0{,}035$ (kehilangan cacahan mencapai $3{,}5\%$).
- Di atas $10^6\text{ cps}$, koreksi matematis mulai menyimpang tajam dan tidak andal. Inilah alasan mendasar mengapa sistem wajib mengalihkan pengukuran ke **Analog Mode** saat sinyal menembus ambang $10^6\text{ cps}$.

---

## 6. Penuaan Detektor (*Detector Aging*) & Pemeliharaan Preventif

Seiring ribuan jam operasional dan jutaan ion yang membentur pelat logam:
1. **Penipisan Lapisan Aktif (*Active Film Depletion*):** Tumbukan kation secara perlahan mengikis atom-atom lapisan aktif $Be-Cu$ pada dynode awal, menurunkan koefisien emisi $\delta$.
2. **Gejala Klinis di Laboratorium:** Nilai *Gain* menurun, puncak pulsa tegangan memendek mendekati garis ambang diskriminator, dan sensitivitas sinyal (*counts*) melayang turun perlahan selama berbulan-bulan.
3. **Tindakan Kompensasi (*High Voltage Calibration*):**  
   Melalui software instrumen (menu diagnostik Qtegra), analis menjalankan rutinitas kalibrasi voltase detektor. Tegangan tinggi detektor dinaikkan secara berkala (misal dari $-1.800\text{ V}$ menjadi $-2.100\text{ V}$) untuk memulihkan gain ke $10^7\times$.
4. **Batas Akhir Pemakaian (*End-of-Life*):** Ketika tegangan detektor sudah mencapai batas maksimum perangkat keras (biasanya $-2.500\text{ V}$ s.d. $-3.000\text{ V}$) dan gain tetap di bawah spesifikasi, modul pengganda elektron telah habis masa pakainya dan **wajib diganti dengan unit baru**.

---

## 7. Rujukan Primer & Landasan Verifikasi (Ground Truth Citations)

1. **Robert Thomas**, *Practical Guide to ICP-MS: A Tutorial for Beginners*, 2nd Edition (2008), CRC Press:
   - *Chapter 11: "Ion Detectors"* (hal. 93–100 / PDF hal. 119–126): Prinsip emisi elektron sekunder, batasan dead time ($30 - 50\text{ ns}$), perbandingan Channeltron vs Discrete Dynode, dan perpanjangan rentang dinamis via sadapan midpoint analog.
2. **E. R. Denoyer, R. J. Thomas, and L. Cousins**, *"Characterization of a Dual-Mode Discrete Dynode Electron Multiplier for ICP-MS"*, *Spectroscopy*, 12(2), 56–61 (1997) [Covered by U.S. Patent 5,463,219]:
   - Paten arsitektur sadapan dynode tengah dan kalibrasi silang (*cross-calibration*) simultan pulse-analog.
3. **Douglas A. Skoog, F. James Holler, Stanley R. Crouch**, *Principles of Instrumental Analysis*, 7th Edition (2018), Cengage Learning:
   - *Chapter 11C-1 & Chapter 20B*: Mekanisme pengganda elektron diskrit, amplifikasi kaskade $G = \delta^n$, dan transduser ion.
4. **Thermo Fisher Scientific Inc.**, *iCAP Q ICP-MS Operator Manual & Qtegra Software Help*:
   - Konfigurasi detektor dual-mode, kriteria cross-calibration otomatis, dan protokol penggantian berkala discrete dynode multiplier.
