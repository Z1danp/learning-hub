---
title: Optik Ion ICP-MS (Space-Charge Effect, Defleksi Elektrostatik 90°, dan Eliminasi Latar Belakang)
domain: analytical_chemistry
technique: icp-ms
tags:
  - analytical-chemistry
  - instrumentation
  - first-principles
  - ion-optics
  - space-charge-effect
  - electrostatic-deflection
  - background-suppression
  - icap-q
date: 2026-09-29
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-learning-roadmap]]"
  - "[[interface-cones-and-vacuum-mechanics]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
  - "[[mekanika-quadrupole-rf-dc]]"
  - "[[icp-ms-tuning-qc-dan-lab-sparring]]"
---

# Optik Ion ICP-MS (Space-Charge Effect & Electrostatic Deflection)

> **One-Sentence Core Phenomenon:**  
> Sistem optik ion adalah susunan lensa elektrostatis dinamis yang mengekstraksi dan membelokkan kation analit $90^\circ$ ke penganalisis massa guna melenyapkan derau foton dan partikel netral ke *beam dump*, sekaligus mengompensasi ledakan tolakan Coulomb antarkation (*space-charge effect*) melalui modulasi tegangan lentur dinamis (*dynamic voltage ramping*).

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena Fisika / Mekanika yang Terjadi | Parameter Kritis & Batas Operasional |
| :--- | :--- | :--- | :--- |
| **Layer 0**<br>*(SOP Lab & Operasional)* | Tuning Solution (Li, In, U), Software Qtegra / Autotune, Internal Standard (ISTD) | Optimasi sensitivitas tiga massa ($^7\text{Li} > 30.000$, $^{115}\text{In} > 132.000$, $^{238}\text{U} > 150.000\text{ cps}$), verifikasi *background noise* $< 1\text{ cps}$ pada $m/z$ kosong, pencocokan massa ISTD untuk koreksi supresi matriks berat. | Konsentrasi larutan tuning $1\text{ ppb}$, toleransi RSD sinyal harian $< 2\%$, rentang penerimaan recovery ISTD $70\% - 130\%$. |
| **Layer -1**<br>*(Mekanika Komponen)* | Lensa Ekstraksi (*Extraction Lens*), RAPID Deflector Lens (Thermo iCAP Q) / Hollow Ion Mirror, Penangkap Partikel (*Beam Dump*) | Ekstraksi kation pasca-skimmer ke ruang vakum $10^{-3} - 10^{-4}\text{ Torr}$, pembuangan foton dan partikel netral secara lurus ke *beam dump*, pembelokan ortogonal $90^\circ$ kation positif menuju QCell/Flatapole, pemindaian tegangan lensa sinkron dengan scan quadrupole (*on-the-fly ramping*). | Voltase deflektor $\pm 5 - 200\text{ V}$, dimensi bukaan lensa lapang bebas deposit kotoran, tekanan ruang optik dijaga turbopump primer. |
| **Layer -2**<br>*(Fisika Medan & Elektrodinamika)* | Dinamika Partikel Bermuatan & Medan Elektrostatik | Difusi elektron kilat ($v_{th} \propto \sqrt{T/m_e}$), disintegrasi netralitas plasma $\to$ berkas murni kation positif, tolakan Coulombik radial ($F \propto q_1 q_2 / r^2$), inersia Newton ($a = F/m$), kesetimbangan gaya sentripetal belokan melingkar ($R = \frac{2E_k}{qE} \propto \frac{m}{qE}$), ketidakberlakuan gaya Lorentz pada partikel tak bermuatan ($q = 0 \implies \vec{F} = 0$). | Energi kinetik aksial ($E_k \approx 0.15\text{ eV}$ untuk Li vs $5.0\text{ eV}$ untuk U), kecepatan gas pendorong supersonik $v_z \approx 2.000\text{ m/s}$, radius kelengkungan lintasan deflektor ($R$). |

---

## 2. Dinamika Pasca-Skimmer: Hilangnya Kuasi-Netralitas Plasma

Begitu semburan gas plasma menembus lubang runcing *skimmer cone* ($0.4 - 0.8\text{ mm}$), tekanan lingkungan anjlok dari $\sim 1\text{ Torr}$ ke ruang optik ion bertekanan **$10^{-3} - 10^{-4}\text{ Torr}$** yang disedot oleh pompa turbomolekuler.

```
   [ DI DALAM INTERFACE ]                     [ DI DALAM RUANG OPTIK ION ]
       (Tekanan ~1 Torr)                         (Tekanan 10⁻³ - 10⁻⁴ Torr)
─────────────────────────────────          ──────────────────────────────────────────
   Plasma Kuasi-Netral:                       Elektron Buyar & Difusi Kilat:
   • Kation M⁺, Ar⁺                           • Elektron melesat ke dinding luar
   • Elektron e⁻                              • Tersisa: BERKAS MURNI KATION POSITIF!
   (Muatan seimbang: Σq ≈ 0)                  (Ledakan Tolakan Coulomb: F = k·q₁q₂/r²)
```

### Mengapa Elektron Mendadak Berdifusi Keluar Jalur?
1. **Disparitas Massa Ekstrem:** Massa elektron ($m_e \approx 9.1 \times 10^{-31}\text{ kg}$) sekitar **$73.000\times$ lebih ringan** daripada kation Argon ($m_{Ar} \approx 6.6 \times 10^{-26}\text{ kg}$).
2. **Kecepatan Termal Acak ($v_{th}$):**  
   Berdasarkan distribusi Maxwell-Boltzmann:
   $$v_{th} = \sqrt{\frac{3 k_B T}{m}}$$
   Karena massanya sangat kerdil, kecepatan gerak acak termal elektron ribuan kali lebih cepat daripada kation.
3. **Akibat Fisik:** Pada tekanan rendah di mana tumbukan antarmolekul melonggar drastis, elektron berhamburan dan berdifusi ke segala arah menjauhi sumbu berkas, menabrak dinding logam instrumen.
4. **Hasil Akhir:** Keseimbangan muatan runtuh. Berkas gas di sepanjang sumbu tengah instrumen bermutasi menjadi **berkas murni kation bermuatan positif padat** ($Ar^+, M^+$) ([Robert Thomas, Bab 6, hal. 41–42](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners,%20Second%20Edition%20(Practical%20Spectroscopy)%20(2008,%20CRC%20Press)%20-%20libgen.li.pdf#page=67)).

---

## 3. Fisika Efek Muatan Ruang (*The Space-Charge Effect*)

Ketika berkas partikel berubah menjadi $100\%$ kation positif tanpa ada perisai elektron netral, berlaku **Hukum Tolakan Coulomb**:
$$F_{\text{Coulomb}} = \frac{1}{4\pi \varepsilon_0} \frac{q_1 q_2}{r^2}$$

Kation-kation yang berdesakan rapat saling menolak satu sama lain ke arah radial (ke luar dari garis sumbu aksial). Ini memicu ledakan pemuaian berkas ion (*beam defocusing/blooming*).

```
                            [ Garis Sumbu Aksial ]
                                      │
               Ion Berat (²³⁸U⁺)      │      Ion Ringan (⁷Li⁺)
             ● Inersia Besar          │    ○ Inersia Kerdil
             ● Ek = 5.0 eV            │    ○ Ek = 0.15 eV
             ● Tetap Melaju Lurus     │    ○ Terpental Jauh ke Samping
                     │                │            ↗
                     │                │          ↗ (Terlempar ke Luar Sumbu)
                     ▼                │        ○
                     ●                │
                     │                │
```

### Mengapa Ion Ringan Terlempar, Sedangkan Ion Berat Lolos Lurus?
1. **Hukum II Newton ($a = F/m$):**  
   Setiap kation di tepi berkas merasakan gaya tolak Coulomb radial ($F$) yang kurang lebih setara. Namun percepatan lemparannya ($a_{\text{radial}}$) berbanding terbalik dengan massa ion ($m$):
   $$a_{\text{radial}} = \frac{F_{\text{Coulomb}}}{m}$$
   - Massa $^{238}\text{U}^+$ bernilai $238\text{ amu}$.
   - Massa $^7\text{Li}^+$ bernilai $7\text{ amu}$ ($\sim 34\times$ lebih ringan dari U).
   - Akibatnya, kation Lithium mengalami percepatan lemparan ke luar sumbu **$34\times$ lebih dahsyat** daripada Uranium.
2. **Keseragaman Kecepatan Aksial & Disparitas Energi Kinetik:**  
   Seluruh atom dan ion dihembuskan keluar dari mulut skimmer cone oleh ekspansi jet gas argon supersonik pada kecepatan dorong terminal yang hampir sama:
   $$v_z \approx 2.000\text{ m/s}$$
   Karena energi kinetik aksial maju adalah $E_k = \frac{1}{2} m v_z^2$, energi dorong ke depan berbanding lurus dengan massanya:
   $$E_k(^{238}\text{U}^+) \approx \mathbf{5{,}0\text{ eV}} \quad \gg \quad E_k(^7\text{Li}^+) \approx \mathbf{0{,}15\text{ eV}}$$
   - **Ion Berat ($^{238}\text{U}^+$):** Memiliki inersia momentum masif layaknya **bola boling**. Ia melesat mantap menembus pusat sumbu optik.
   - **Ion Ringan ($^7\text{Li}^+$):** Memiliki inersia lemah layaknya **bola pingpong**. Begitu bertabrakan Coulomb dengan ion-ion berat matriks di sekitarnya, ia langsung terpental keluar dari jangkauan lensa.

### Implikasi Analitik Nyata: Supresi Matriks Berat (*Heavy Matrix Suppression*)
Jika sebuah sampel memiliki konsentrasi tinggi unsur berat (seperti timbal $Pb$, barium $Ba$, talium $Tl$, atau uranium $U$), densitas muatan ion berat di pusat sumbu akan **mendesak analit ringan ($Li, Be, B$) keluar lintasan secara brutal**.
- **Aturan Mitigasi SOP:** Wajib menggunakan **Internal Standard (ISTD)** yang massanya setara (*mass-matched ISTD*). 
  Mengoreksi sinyal $^7\text{Li}$ menggunakan ISTD $^{209}\text{Bi}$ adalah kesalahan fatal metrologi, karena Lithium akan tertekan hebat oleh *space-charge effect*, sedangkan Bismuth sama sekali tidak terpengaruh! Gunakan $^6\text{Li}$ atau $^{45}\text{Sc}$ untuk analit ringan, dan $^{115}\text{In}$ atau $^{209}\text{Bi}$ untuk analit berat.

---

## 4. Pemilahan Foton & Netral: Arsitektur Belokan 90° (RAPID Lens)

Selain kation analit, lubang skimmer cone menyemburkan "penumpang gelap" berbahaya langsung dari plasma:
1. **Foton UV & Cahaya Tampak:** Radiasi elektromagnetik intensitas tinggi dari bola plasma $10.000\text{ K}$.
2. **Partikel Netral:** Atom gas Argon ($Ar^0$), molekul air pelarut belum pecah, dan partikel garam mikro netral.

Jika foton atau partikel netral ini meluncur lurus menabrak detektor (*Electron Multiplier*), mereka akan melepaskan elektron sekunder palsu, mendongkrak derau latar (*background noise*) dari $< 1\text{ cps}$ menjadi ribuan cps!

```
                  [ LURUS: DIBUANG KE TEMPAT SAMPAH ]
                  Foton (Cahaya) & Partikel Netral (q = 0)
                                      ▲
                                      │  (F = q·E = 0, kebal medan listrik)
                                      │
   [ DARI SKIMMER CONE ] ─────────────┼──────────────────┐
   Berkas Campuran:                   │                  │
   • Kation M⁺ (q > 0)                │ RAPID LENS       │ Dinding Peredam
   • Foton Cahaya (q = 0)             │ (Medan Listrik   │ (Beam Dump /
   • Partikel Netral (q = 0)          │  Belokkan 90°)   │  Penyedotan Vakum)
                                      │                  │
                                      ▼                  ▼
                             [ DIBELOKKAN 90° ]
                             HANYA Kation M⁺ (q > 0)
                                      │
                                      ▼
                             Menuju QCell Flatapole ──► Quadrupole ──► Detektor
```

### Gaya Lorentz: Mengapa Foton dan Netral Pasti Lolos Lurus?
Komponen deflektor pada ICP-MS (seperti **RAPID Lens** pada Thermo Scientific iCAP Q atau *Hollow Ion Mirror*) bekerja murni menggunakan **Medan Elektrostatik ($\vec{E}$)**.

Berdasarkan formulasi **Gaya Lorentz**:
$$\vec{F} = q \cdot (\vec{E} + \vec{v} \times \vec{B})$$

1. **Untuk Foton & Netral ($q = 0$):**
   $$\vec{F} = 0 \cdot \vec{E} = 0$$
   Partikel netral dan foton **sama sekali tidak merasakan gaya listrik**. Mereka kebal terhadap elektroda deflektor dan terus melesat lurus ke depan, menabrak dinding penangkap (*beam dump*), lalu diserap dan dibuang oleh pompa vakum.
2. **Untuk Kation Analit ($q = +1$):**
   $$\vec{F} = +e \cdot \vec{E}$$
   Kation merasakan tarikan elektroda negatif dan tolakan elektroda positif, membelokkan lintasannya secara presisi sebesar **$90^\circ$ ke samping** menuju sel reaksi dan penganalisis massa.
3. **Hasil Metrologis:** Latar belakang derau instrumen jatuh bebas hingga **$< 1\text{ cps}$** (memenuhi kriteria spesifikasi [IK-BRIN iCAP Q, hal. 23](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/IK-BRIN-LKIMIA-6.4-09%20Pengoperasian%20ICP-MS%20iCAP%20Q_rev%2002%20final.pdf#page=23)).

---

## 5. Dinamika Belokan Elektrostatik & *Dynamic Lens Ramping*

Agar kation analit bermuatan $q$ dan bermassa $m$ berhasil berbelok $90^\circ$ tanpa menabrak dinding elektroda deflektor, gaya elektrostatik harus bertindak sebagai **gaya sentripetal**:
$$F_{\text{sentripetal}} = F_{\text{elektrostatik}}$$
$$\frac{m v^2}{R} = q E \implies R = \frac{m v^2}{q E} = \frac{2 E_k}{q E}$$

Karena kecepatan dorong aksial semua ion seragam ($v \approx 2.000\text{ m/s}$), maka radius kelengkungan belokan ($R$) berbanding lurus dengan massa ion:
$$R \propto \frac{m}{q E}$$

```
                                [ Elektroda Luar ]
                               ───────────────────
                                        ▲
                                       /  (Under-Bending / Bablas)
                                      /     ²³⁸U⁺ (Ek = 5.0 eV)
                                     /
   [ MASUK DARI SKIMMER ] ─────────►●══════════► [ BELOKAN SEMPURNA 90° ]
                                     \             (Target: Menuju Quadrupole)
                                      \
                                       \  ⁷Li⁺ (Ek = 0.15 eV)
                                        ▼   (Over-Bending / Menukik)
                               ───────────────────
                                [ Elektroda Dalam ]
```

### Dua Mode Kegagalan Jika Voltase Disetel Statis:
1. **Under-Bending (Overshoot pada Massa Berat):**  
   Jika voltase listrik $E$ disetel rendah (hanya cukup membelokkan Lithium), energi kinetik Uranium ($5.0\text{ eV}$) terlalu besar untuk dibelokkan tajam. Radius belokannya terlalu lebar ($R \gg R_{\text{desain}}$), sehingga ion Uranium **bablas menabrak dinding luar atau terbuang ke *beam dump***.
2. **Over-Bending (Undershoot pada Massa Ringan):**  
   Jika voltase listrik $E$ dinaikkan tinggi agar mampu membelokkan Uranium, medan listrik menjadi teramat kuat bagi Lithium ($0.15\text{ eV}$). Radius belokan Lithium menjadi teramat kecil ($R \ll R_{\text{desain}}$), membanting ion Lithium menukik tajam ke elektroda dalam sebelum sempat mencapai pintu masuk quadrupole.

### Solusi Rekayasa Komersial: *Dynamic Lens Ramping on-the-fly*
Instrumen modern tidak menggunakan satu nilai voltase statis. Komputer pengendali instrumen menjalankan **Dynamic Lens Voltage Ramping**:
- Tegangan elektroda deflektor **dimodulasi secara dinamis (*on the fly*)** sinkron dengan pemindaian massa quadrupole ($m/z$).
- Saat quadrupole mengukur $^7\text{Li}$, voltase diturunkan ke titik optimum rendah.
- Saat quadrupole beralih mengukur $^{238}\text{U}$, voltase dinaikkan seketika ke titik optimum tinggi ([Robert Thomas, hal. 44](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners,%20Second%20Edition%20(Practical%20Spectroscopy)%20(2008,%20CRC%20Press)%20-%20libgen.li.pdf#page=70)).

> 🔬 **Landasan Fisis Larutan Tuning Harian:**  
> Inilah alasan mutlak mengapa larutan *Daily Tuning* ([IK-BRIN iCAP Q, hal. 23](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/IK-BRIN-LKIMIA-6.4-09%20Pengoperasian%20ICP-MS%20iCAP%20Q_rev%2002%20final.pdf#page=23)) wajib mengandung:
> - **$^7\text{Li}$ ($7\text{ amu}$)**: Kalibrasi respon voltase lensa rentang rendah (*low-mass*).
> - **$^{115}\text{In}$ ($115\text{ amu}$)**: Kalibrasi respon voltase lensa rentang menengah (*mid-mass*).
> - **$^{238}\text{U}$ ($238\text{ amu}$)**: Kalibrasi respon voltase lensa rentang tinggi (*high-mass*).
>
> Algoritma Autotune memetakan kurva tegangan ketiga titik jangkar ini untuk menjamin efisiensi transmisi ion yang datar dan seragam di sepanjang spektrum massa.

---

## 6. Rujukan Primer & Landasan Verifikasi (Ground Truth Citations)

1. **Robert Thomas**, *Practical Guide to ICP-MS: A Tutorial for Beginners*, 2nd Edition (2008), CRC Press:
   - *Chapter 6: "Ion-Focusing System"* (hal. 39–47 / PDF hal. 65–73): Mekanisme difusi elektron, repulsi Coulomb *space-charge effect*, eliminasi foton via pembelokan $90^\circ$ (*ion mirror*), dan *dynamic lens voltage ramping*.
2. **Douglas A. Skoog, F. James Holler, Stanley R. Crouch**, *Principles of Instrumental Analysis*, 7th Edition (2018), Cengage Learning:
   - *Chapter 11C-1: "Instruments for ICPMS"* (hal. 263 / PDF hal. 285): Pemisahan ion positif dari elektron dan spesi molekuler oleh voltase negatif lensa ekstraksi.
3. **Badan Riset dan Inovasi Nasional (BRIN)**, *Instruksi Kerja Pengoperasian ICP-MS Thermo Fisher Scientific iCAP Q*, No. Dok: `IK-BRIN-LKIMIA-6.4-09` Rev 01 (2026):
   - *Bagian 12.4.2 (hal. 23)*: Batas keberterimaan sinyal elemen larutan tuning harian ($^7\text{Li}, ^{115}\text{In}, ^{238}\text{U}$) dan batas derau latar belakang (*background noise* $< 1\text{ cps}$ pada $m/z$ kosong).
4. **Thermo Fisher Scientific Inc.**, *Technical Note: The RAPID Lens (Right Angle Positive Ion Deflection) Technology for the iCAP Q ICP-MS Series*:
   - Arsitektur defleksi ortogonal $90^\circ$ bebas perawatan untuk pembuangan total partikel netral dan foton ke *beam dump*.
