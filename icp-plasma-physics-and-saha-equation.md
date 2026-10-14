---
title: Fisika Plasma ICP, Induksi Frekuensi Radio, dan Persamaan Saha-Eggert
domain: analytical_chemistry
technique: icp-ms
tags:
  - analytical-chemistry
  - instrumentation
  - first-principles
  - icp-torch
  - plasma-physics
  - rf-induction
  - thermodynamics
date: 2026-09-19
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-learning-roadmap]]"
  - "[[sample-introduction-and-nebulization]]"
  - "[[mekanika-quadrupole-rf-dc]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
---

# Fisika Plasma ICP, Induksi Frekuensi Radio, dan Persamaan Saha-Eggert

> **One-Sentence Core Phenomenon:**  
> Plasma ICP adalah fluida gas Argon terionisasi bertekanan atmosfer yang dibentuk oleh disipasi daya induksi RF frekuensi tinggi via Efek Kulit (*Skin Effect*) menjadi cincin toroid berlubang ($8.000 - 10.000\text{ K}$), di mana semprotan gas pembawa melubangi terowongan aksial tengah agar analit mengalami desolvasi, atomisasi, dan ionisasi tumbukan dalam waktu tinggal $\approx 1 - 2\text{ ms}$.

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena Fisika / Mekanika yang Terjadi | Parameter Kritis & Batas Operasional |
| :--- | :--- | :--- | :--- |
| **Layer 0**<br>*(SOP Lab & Operasional)* | ICP Torch, Koil RF, Gas Mass Flow Controllers | Penyaluran 3 aliran Argon (total $\sim 15 - 18\text{ L/min}$), penyalaan plasma via percikan Piezo/Tesla, autotune daya RF ($1.000 - 1.500\text{ W}$), monitoring rasio $\text{CeO}^+/\text{Ce}^+ \le 2\%$ dan $\text{Ba}^{2+}/\text{Ba}^+ \le 3\%$. | Frekuensi RF $27.12\text{ MHz}$ atau $40.68\text{ MHz}$, laju alir gas carrier $0.95 - 1.05\text{ L/min}$, jarak torch ke cone $10 - 15\text{ mm}$. |
| **Layer -1**<br>*(Mekanika Komponen)* | 3 Tabung Kuarsa Konsentris, Koil Tembaga Berpendingin Air | Aliran tangensial gas luar membentuk selimut pelindung heliks di dinding kuarsa, koil tembaga menginduksi medan magnetik aksial, pipa injektor ($ID \approx 1.5 - 2.5\text{ mm}$) melubangi terowongan donat plasma. | Debit gas luar $12 - 17\text{ L/min}$, auxiliary gas $\sim 1\text{ L/min}$, titik leleh kuarsa $\approx 1.700^\circ\text{C}$, waktu tinggal analit $\sim 1 - 2\text{ ms}$. |
| **Layer -2**<br>*(Elektrodinamika & Termodinamika)* | Persamaan Maxwell, Efek Kulit (*Skin Effect*), Kesetimbangan Saha | Hukum Faraday ($\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$), arus eddy lingkar luar dengan kedalaman kulit $\delta = \sqrt{\frac{1}{\pi f \mu \sigma}}$, tumbukan elektron inelastis, transfer muatan $Ar^+$ ($15.76\text{ eV}$), kesetimbangan ionisasi Saha-Eggert. | Suhu cincin luar $8.000 - 10.000\text{ K}$, suhu kanal tengah $5.000 - 7.000\text{ K}$, densitas elektron $n_e \sim 10^{14} - 10^{15}\text{ cm}^{-3}$, energi ikat $\text{Ce-O}$ ($8.6\text{ eV}$) vs $IE_1(\text{CeO})$ ($5.2\text{ eV}$). |

---

## 2. Anatomi Tiga Tabung Kuarsa & Tiga Aliran Gas Argon

Untuk menjaga tabung kaca kuarsa (titik leleh $\approx 1.700^\circ\text{C}$) tidak meleleh oleh nyala plasma bersuhu $10.000\text{ K}$, instrumen menggunakan desain 3 tabung konsentris:

```
   ================== Dinding Tabung Kuarsa Luar (Outer Tube) ==================
   ---> Aliran 1: Plasma / Coolant Gas (~12 - 17 L/min, semprotan tangensial heliks)
   ------------------ Tabung Tengah (Middle Tube) -----------------------------
   ---> Aliran 2: Auxiliary Gas (~0.75 - 1.5 L/min)
   ===========[ Pipa Injektor Pusat (Sample Injector ID 1.5 - 2.5 mm) ]=========
   ===> Aliran 3: Carrier / Nebulizer Gas + Aerosol Sampel (~0.9 - 1.1 L/min)
   ============================================================================
```

### 1. Aliran Gas Luar (*Plasma / Coolant Gas*, $12 - 17\text{ L/min}$)
* **Inlet Miring / Tangensial:** Gas diinjeksikan menyinggung dinding tabung luar sehingga membentuk **pusaran spiral heliks (*tangential swirl*)**.
* **Perisai Fluida Dingin (*Laminar Boundary Layer*):** Gaya sentrifugal dari pusaran menekan lapisan gas Argon dingin menempel ketat di sepanjang dinding dalam tabung kuarsa luar. Lapisan pelindung ini mendinginkan kaca secara konvektif sehingga kuarsa hanya menerima panas radiasi dan tidak pernah bersentuhan langsung dengan nyala plasma.

### 2. Aliran Gas Tengah (*Auxiliary Gas*, $\sim 1\text{ L/min}$)
* Mengalir di antara tabung tengah dan tabung injektor.
* Berfungsi mengangkat dasar nyala plasma (*plasma base*) beberapa milimeter di depan ujung pipa injektor kuarsa agar ujung nosel injektor tidak meleleh akibat panas balik.

### 3. Aliran Gas Pusat (*Carrier / Nebulizer Gas*, $\sim 1\text{ L/min}$)
* Membawa kabut droplet aerosol ($< 2 - 5\ \mu\text{m}$) dari spray chamber.
* Bergerak dengan kecepatan linier tinggi untuk **melubangi / menembus pusat cincin donat plasma (*central channel*)**.

---

## 3. Fisika Pembangkitan Plasma: Frekuensi Radio & Efek Kulit (*Skin Effect*)

Bagaimana gas Argon netral yang bersifat isolator dapat berubah menjadi plasma super panas konduktif?

```
                    Koil Induksi RF (Arus Bolak-balik 27 / 40 MHz)
                           ( O )          ( O )          ( O )
                    ─────────────────────────────────────────────
                     [ Lapisan Kulit Luar: Arus Eddy Raksasa ] -> 10.000 K
                     ---------------------------------------------
                     [ KANAL TENGAH: Medan Batal, Sejuk ]      ->  6.000 K
                     ---------------------------------------------
                     [ Lapisan Kulit Luar: Arus Eddy Raksasa ] -> 10.000 K
                    ─────────────────────────────────────────────
                           ( O )          ( O )          ( O )
```

1. **Pemicu Awal (*Ignition*):** Percikan tegangan tinggi dari kumparan Tesla atau Piezo menyuntikkan elektron awal (*seed electrons*) ke aliran gas Argon.
2. **Induksi Elektromagnetik (Hukum Faraday):**  
   Koil tembaga dialiri arus bolak-balik RF ($27.12\text{ MHz}$ atau $40.68\text{ MHz}$, daya $\approx 1.000 - 1.400\text{ W}$). Arus frekuensi tinggi ini menciptakan medan magnet bolak-balik aksial intens yang menginduksi medan listrik melingkar di dalam gas:
   $$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$
3. **Pemanasan Ohmik / Joule:** Elektron bebas dipercepat oleh medan listrik melingkar, bertumbukan secara inelastis dengan atom Argon ($IE_1 = 15.76\text{ eV}$), melepaskan lebih banyak elektron dalam reaksi berantai (*avalanche ionization*).
4. **Efek Kulit (*Skin Effect*) Pembentuk Cincin Donat:**  
   Karena plasma adalah fluida berkonduktivitas listrik tinggi ($\sigma$), arus induksi frekuensi tinggi tunduk pada persamaan kedalaman penetrasi kulit:
   $$\delta = \sqrt{\frac{1}{\pi \cdot f \cdot \mu \cdot \sigma}}$$
   Pada frekuensi $27 - 40\text{ MHz}$, arus eddy **hanya terkonsentrasi di lapisan luar silinder plasma**. Bagian tengah silinder mengalami pelemahan medan magnetik induksi.
   * **Hasil Morfologi:** Plasma membentuk **cincin donat berongga (*toroidal shape*)**. Dinding luar donat membara pada $8.000 - 10.000\text{ K}$, sementara terowongan sumbu tengah berongga dan bersuhu lebih sejuk ($\sim 5.000 - 6.000\text{ K}$).

---

## 4. Dinamika 4 Zona Reaksi Aksial di Kanal Tengah

Semprotan *carrier gas* meluncur menembus lubang donat membawa materi analit selama waktu tinggal yang sangat singkat ($\approx 1 - 2\text{ ms}$). Di sepanjang lorong ini terjadi 4 transformasi fase dan energi:

```
[ Injektor ] ===> [ 1. Desolvasi ] ===> [ 2. Vaporisasi ] ===> [ 3. Atomisasi ] ===> [ 4. Ionisasi ] ===> [ Mulut Sampler Cone ]
                 Droplet Cair           Garam Kering Padat     Gas Molekuler          Atom Bebas (M⁰)       Ion Positif M⁺
                 Menguap Kilat          Menyublim              Ikatan Kimia Putus     Lepas Elektron        Disedot ke Vakum
```

1. **Zona Desolvasi (*Desolvation Zone*):**  
   Droplet air basah menerima panas radiasi dari dinding donat. Pelarut air menguap kilat, meninggalkan mikro-kristal garam kering padat.
2. **Zona Vaporisasi (*Vaporization Zone*):**  
   Partikel garam kering meleleh dan menyublim menjadi gas fase molekuler (misal molekul netral $\text{NaCl}_{(g)}$ atau $\text{CeO}_{(g)}$).
3. **Zona Atomisasi (*Atomization Zone*):**  
   Energi termal memutuskan ikatan kimia kovalen/ionik molekul gas, memecahnya menjadi atom-atom netral bebas ($M^0$).
4. **Zona Ionisasi (*Ionization Zone*):**  
   Atom netral analit melepaskan elektron valensi dan berubah menjadi ion positif monoatomik ($M^+$) tepat di depan corong ekstraksi *Sampler Cone*.

---

## 5. Mekanisme Ionisasi di Kanal Tengah

Ionisasi analit di dalam plasma bukan sekadar efek radiasi termal pasif, melainkan didominasi oleh **tumbukan partikel energi tinggi**:

### A. Tumbukan Elektron Inelastis (*Electron Impact Ionization*)
Elektron cepat dari ekor distribusi menabrak atom analit bebas:
$$M^0 + e^-_{\text{cepat}} \longrightarrow M^+ + 2e^-_{\text{lambat}} \quad (\text{Syarat: } E_k \ge IE_1(M))$$

### B. Transfer Muatan dengan Kation Argon (*Charge Transfer Ionization*)
Argon memiliki energi ionisasi pertama yang sangat tinggi: **$IE_1(\text{Ar}) = 15.76\text{ eV}$**.  
Tumbukan langsung antara atom netral logam dan ion $Ar^+$ memicu transfer muatan spontan:
$$M^0 + Ar^+ \longrightarrow M^+ + Ar^0 + \Delta E \quad (\text{Syarat: } IE_1(M) < 15.76\text{ eV})$$

### C. Ionisasi Penning via Argon Metastabil (*Penning Ionization*)
Atom Argon metastabil $Ar^*$ menyimpan energi eksitasi $11.55\text{ eV}$ dan $11.72\text{ eV}$:
$$M^0 + Ar^* \longrightarrow M^+ + Ar^0 + e^- \quad (\text{Syarat: } IE_1(M) < \sim 11.5\text{ eV})$$

*(Dekonstruksi matematis dan korelasi tuning instrumen dibahas lengkap di [[mekanisme-ionisasi-analit-di-plasma]])*

### D. Kesetimbangan Termodinamika Saha-Eggert
Di bawah kesetimbangan termal lokal (*Local Thermodynamic Equilibrium* / LTE), perbandingan populasi ion terhadap atom netral dirumuskan oleh **Persamaan Saha-Eggert**:
$$\frac{n_i \cdot n_e}{n_a} = \frac{2 g_i}{g_a} \left(\frac{2\pi m_e k T}{h^2}\right)^{3/2} \exp\left(-\frac{E_i}{k T}\right)$$

* Karena suhu kanal tengah $T \approx 6.500 - 7.500\text{ K}$ dan densitas elektron tinggi ($n_e \approx 10^{14}\text{ cm}^{-3}$), unsur dengan $E_i < 8\text{ eV}$ (seperti $\text{Na, Mg, Fe, Pb, Cu}$) memiliki derajat ionisasi **$> 90 - 99\%$**.
* Unsur dengan $E_i > 10\text{ eV}$ (seperti $\text{As, Se, Hg, Cl}$) memiliki derajat ionisasi jauh lebih rendah ($< 30 - 50\%$).

---

## 6. Paradoks Oksida: Jalur Utama vs Jalur Parasitik

### Mengapa Ion Oksida ($\text{CeO}^+$) Bisa Terbentuk?
* **Energi Disosiasi Ikatan (*Bond Dissociation Energy* / BDE):**  
  $\text{BDE}(\text{Ce-O}) \approx \mathbf{8.6\text{ eV}}$ (energi yang sangat besar untuk memutus ikatan atom).
* **Energi Ionisasi Pertama Molekul Oksida ($IE_1$):**  
  $IE_1(\text{CeO} \to \text{CeO}^+ + e^-) \approx \mathbf{5.2\text{ eV}}$ (hanya mencabut satu elektron valensi molekul).

$$IE_1(\text{CeO})\ [5.2\text{ eV}] \ll \text{BDE}(\text{Ce-O})\ [8.6\text{ eV}]$$

```
                            [ Gas Molekul CeO ]
                                     │
             ┌───────────────────────┴───────────────────────┐
             ▼ (JALUR UTAMA: Plasma Cukup Panas)             ▼ (JALUR PARASITIK: Plasma Dingin / Gas Kencang)
       Atomisasi Tuntas                                 Ionisasi Dini Molekul Oksida
       Ikatan Ce-O Putus (BDE = 8.6 eV)                 Lepas 1 Elektron (IE = 5.2 eV)
             │                                               │
             ▼                                               ▼
       [ Atom Bebas Ce⁰ ]                               [ Ion Poliatomik CeO⁺ ]
             │                                               │
             ▼ (Ionisasi Utama)                              ▼ (Kebablasan ke Cone)
       [ ION TARGET Ce⁺ ]                               Mengganggu Spektrometer Massa
```

Jika gas pembawa terlalu kencang ($1.5\text{ L/min}$), pendinginan evaporatif dan desolvasi yang lambat menyebabkan temperatur lokal kanal tengah anjlok. Energi plasma tidak cukup untuk memutus ikatan $\text{Ce-O}$ ($8.6\text{ eV}$), tetapi cukup untuk mencabut satu elektron ($5.2\text{ eV}$). Analit terjebak di jalur parasitik sebagai ion oksida poliatomik $\text{CeO}^+$!

---

## 7. Falsification Lab & Matriks Troubleshooting Tuning Plasma

| Parameter Tuning | Deviasi Pengaturan | Fenomena Fisis yang Terjadi | Gejala di Layar Spektrometer |
| :--- | :--- | :--- | :--- |
| **Carrier Gas Flow** | Terlalu Kencang ($> 1.3\text{ L/min}$) | Kecepatan aerosol terlalu tinggi, waktu tinggal $< 1\text{ ms}$, desolvasi telat, zona ionisasi terdorong melewati mulut cone (*downstream shift*). | Sinyal analit drop, rasio oksida $\mathbf{\text{CeO}^+/\text{Ce}^+ > 2\%}$ (gagal tuning), cone cepat kotor oleh deposit garam. |
| **Carrier Gas Flow** | Terlalu Lambat ($< 0.7\text{ L/min}$) | Waktu tinggal terlalu lama, zona ionisasi terjadi terlalu dekat dengan injektor, difusi radial ion ke samping, ionisasi tingkat dua berlebih. | Sinyal sensitivitas drop karena difusi, rasio ion bermuatan ganda $\mathbf{\text{Ba}^{2+}/\text{Ba}^+ > 3\%}$ (gagal tuning). |
| **RF Power** | Terlalu Rendah ($< 900\text{ W}$) | Kerapatan elektron plasma $n_e$ merosot, suhu kanal tengah dingin, energi disosiasi ikatan tidak tercapai. | Oksida melonjak drastis, analit berenergi ionisasi tinggi ($As, Se$) tidak terionisasi. |
| **RF Power** | Terlalu Tinggi ($> 1.500\text{ W}$) | Plasma membara berlebih, pembentukan ion ganda ($M^{2+}$) meningkat tajam, beban panas radiasi pada *sampler cone* meningkat drastis. | Rasio $\text{Ba}^{2+}/\text{Ba}^+$ melanggar batas, usia pakai sampler cone memendek karena erosi termal. |

---

## 8. Referensi Terverifikasi (Ground Truth)

1. **Robert Thomas**, *Practical Guide to ICP-MS: A Tutorial for Beginners*, 2nd Edition (2008), CRC Press:
   - Chapter 2: *Principles of Ion Formation* (hal. 7–10 / PDF hal. 34–37) [Robert Thomas (2008)](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners%2C%20Second%20Edition%20%28Practical%20Spectroscopy%29%20%282008%2C%20CRC%20Press%29%20-%20libgen.li.pdf#page=34).
   - Chapter 4: *Plasma Source* (hal. 23–29 / PDF hal. 50–56) [Robert Thomas (2008)](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners%2C%20Second%20Edition%20%28Practical%20Spectroscopy%29%20%282008%2C%20CRC%20Press%29%20-%20libgen.li.pdf#page=50).
2. **Douglas A. Skoog, F. James Holler, Stanley R. Crouch**, *Principles of Instrumental Analysis*, 7th Edition (2018), Cengage Learning:
   - Chapter 11C: *Inductively Coupled Plasma Mass Spectrometry* (hal. 263 / PDF hal. 286) [Skoog et al. (2018)](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Crouch%2C%20Stanley%20R._Holler%2C%20F.%20James_Skoog%2C%20Douglas%20A%20-%20Principles%20of%20Instrumental%20Analysis%20%282018_2016%2C%20CENGAGE%20Learning%29%20-%20libgen.li.pdf#page=286).
3. **Instruksi Kerja BRIN**, *Pengoperasian Inductively Coupled Plasma Mass Spectrometry (ICP-MS) Thermo Scientific iCAP Q*, No. Dok: IK-BRIN-LKIMIA-6.4-09, Rev 02 (2026):
   - Kriteria Keberterimaan Tuning Harian: Rasio CeO+/Ce+ $\le 2\%$, Rasio Ce++/Ce+ $\le 3\%$ (hal. 23) [IK-BRIN iCAP Q](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/IK-BRIN-LKIMIA-6.4-09%20Pengoperasian%20ICP-MS%20iCAP%20Q_rev%2002%20final.pdf#page=23).
