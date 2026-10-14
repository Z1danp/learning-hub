---
title: Fisika Antarmuka ICP-MS (Sampler Cone, Skimmer Cone, Ekspansi Supersonik, dan Pemompaan Diferensial)
domain: analytical_chemistry
technique: icp-ms
tags:
  - analytical-chemistry
  - instrumentation
  - first-principles
  - interface-cones
  - vacuum-systems
  - fluid-dynamics
  - supersonic-expansion
date: 2026-09-29
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-learning-roadmap]]"
  - "[[sample-introduction-and-nebulization]]"
  - "[[icp-plasma-physics-and-saha-equation]]"
  - "[[mekanisme-ionisasi-analit-di-plasma]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
  - "[[mekanika-quadrupole-rf-dc]]"
  - "[[icp-ms-tuning-qc-dan-lab-sparring]]"
---

# Fisika Antarmuka ICP-MS (Interface Cones & Vacuum Mechanics)

> **One-Sentence Core Phenomenon:**  
> Wilayah antarmuka (*interface region*) adalah jembatan mekanika-fluida dan termodinamika ekstrem yang mentransfer materi secara representatif dari plasma Argon bertekanan atmosfer ($760\text{ Torr}, \sim 6.000 - 10.000\text{ K}$) ke ruang spektrometer massa vakum tinggi ($10^{-5} - 10^{-6}\text{ Torr}, \sim 300\text{ K}$) melalui pemompaan bertingkat (*differential pumping*), ekspansi jet supersonik terkontrol dalam *Zone of Silence*, dan disipasi panas konduktif masif blok pendingin air.

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena Fisika / Mekanika yang Terjadi | Parameter Kritis & Batas Operasional |
| :--- | :--- | :--- | :--- |
| **Layer 0**<br>*(SOP Lab & Operasional)* | Sampler Cone, Skimmer Cone, Chiller, Roughing Pump | Injeksi sampel TDS $< 0.2\%$, pembersihan cone berkala dengan asam format $5-10\%$ (Ni) atau $\text{HNO}_3$ $3\%$ (Pt), pemantauan rasio oksida $\text{CeO}^+/\text{Ce}^+ \le 2\%$ dan ion ganda $\text{Ce}^{2+}/\text{Ce}^+ \le 3\%$. | Suhu chiller $15 - 20^\circ\text{C}$, batas aus lubang orifice $\pm 0.1\text{ mm}$, pembilasan asam format via ultrasonic terpisah, batasan larutan $\text{HF}$ (wajib cone Pt). |
| **Layer -1**<br>*(Mekanika Komponen)* | Orifice Kerucut Logam (Ni/Pt), Housing Tembaga, Pompa Rotary, Turbopump | Lubang Sampler ($0.8 - 1.2\text{ mm}$), lubang Skimmer ($0.4 - 0.8\text{ mm}$), penyedotan ruang antara ke $1 - 2\text{ Torr}$ oleh *roughing pump*, transfer fraksi gas $\sim 1 - 2\%$ ke ruang *high vacuum* ($10^{-5} - 10^{-6}\text{ Torr}$) berpendukung *turbomolecular pump*. | Konduktivitas termal blok tembaga ($\approx 400\text{ W/m}\cdot\text{K}$), laju alir pendingin air $\approx 1 - 2\text{ L/min}$, keselarasan aksial (*axial alignment*) antar-lubang cone. |
| **Layer -2**<br>*(Fisika Gas & Elektrodinamika)* | Dinamika Gas Supersonik & Plasma | Ekspansi *underexpanded supersonic free-jet*, pembentukan *barrel shock*, *Mach disk*, dan *zone of silence*, panjang Debye plasma ($\lambda_D \sim 10^{-4}\text{ mm} \ll \text{orifice}$), pencegahan *secondary discharge* (penghilangan kopling kapasitif RF ke potensial nol). | Angka Mach ($M > 1$, mencapai $M \approx 5 - 10$), sebaran energi ion ($\Delta E \approx 5 - 10\text{ eV}$), posisi aksial *Mach disk* ($x_M \propto D \sqrt{P_0/P_b}$), tolakan Coulomb (*space charge effect*) pasca-skimmer. |

---

## 2. Paradoks Fisika: Benturan Dua Alam yang Bertolak Belakang

Tantangan terbesar yang dihadapi para perintis ICP-MS di awal dekade 1980-an adalah menjembatani dua lingkungan fisik yang mustahil dipertemukan secara langsung:

```
  [ ALAM PLASMA ]                                        [ ALAM SPEKTROMETER MASSA ]
  Torch & Atmosfer                                        Quadrupole & Detektor
──────────────────────────────────────────────────────────────────────────────────────────
  Tekanan : 760 Torr (1 atm)               ──►            Tekanan : 10⁻⁵ s.d. 10⁻⁶ Torr (High Vacuum)
  Suhu    : 6.000 – 10.000 K               ──►            Suhu    : ~300 K (Suhu Kamar)
  Keadaan : Plasma kuasi-netral padat      ──►            Keadaan : Berkas ion terarah bebas hambatan
  Mean Free Path (λ): ~sub-mikrometer      ──►            Mean Free Path (λ): meteran (bebas tabrakan)
  Aliran  : Kontinu / Kental (Viscous)     ──►            Aliran  : Bebas Molekuler (Molecular Flow)
```

### Mengapa Spektrometer Massa Wajib Berada di Ruang Vakum Tinggi?
1. **Panjang Bebas Rata-rata (*Mean Free Path*, $\lambda$):**  
   Agar pemilahan massa di medan RF/DC quadrupole dan amplifikasi di elektron multiplier berjalan, ion analit tidak boleh bertabrakan dengan molekul udara/gas latar belakang. Pada $10^{-6}\text{ Torr}$, $\lambda > 50\text{ meter}$, memastikan lintasan bebas hambatan (*collision-free flight path*).
2. **Pencegahan Lucutan Busur (*High Voltage Arcing*):**  
   Elektroda ion optics, quadrupole, dan dynode detektor beroperasi pada potensial listrik ratusan hingga ribuan volt. Pada tekanan sedang/atmosfer, tegangan ini akan memicu petir/loncatan busur listrik (*Townsend discharge*) yang merusak elektronik seketika.

### Mengapa Tidak Bisa Menggunakan 1 Lubang Langsung? (Beban Pompa & Hukum Gas)
Jika ruang vakum $10^{-6}\text{ Torr}$ dilubangi $1\text{ mm}$ langsung menghadap atmosfer:
- Debit gas yang menyembur masuk dari atmosfer adalah $\sim 1\text{ L/min}$.
- Berdasarkan hukum pemuaian gas ideal ($P_1 V_1 = P_2 V_2$), $1\text{ Liter}$ gas atmosfer pada $760\text{ Torr}$ akan mengembang menjadi:
  $$V_2 = 1\text{ L} \times \frac{760\text{ Torr}}{10^{-6}\text{ Torr}} = 7,6 \times 10^8\text{ Liter/menit!}$$
- Pompa turbomolekuler hanya mampu bekerja pada rezim *molecular flow* (tekanan $< 10^{-2}\text{ Torr}$). Gas kental atmosfer akan mengerem bilah turbin berkecepatan tinggi ($> 50.000\text{ RPM}$), menimbulkan panas gesek masif, dan merusaknya seketika.
- **Solusi Arsitektur (*Differential Pumping*):**
  - **Tahap 1 (Roughing Stage):** Ruang antara sampler dan skimmer disedot oleh pompa mekanik (*rotary pump*) tahan aliran viskos tinggi hingga mencapai tekanan menengah **$1 - 2\text{ Torr}$**.
  - **Tahap 2 (High Vacuum Stage):** Hanya inti berkas gas dari lubang skimmer cone ($\sim 1 - 2\%$ dari total aliran) yang diteruskan ke ruang turbomolekuler ($10^{-5} - 10^{-6}\text{ Torr}$).

---

## 3. Geometri Kerucut & Aerodinamika Ekspansi Supersonik

```
                          [ Ruang Antara / Interface ]      [ Ruang Optik Ion ]
   [ PLASMA 760 Torr ]           ( 1 - 2 Torr )                ( 10⁻⁵ Torr )
   
       Torch            Sampler Cone       Skimmer Cone
     ┌───────┐             ▼                   ▼
     │       │            ╱│                   ╱│
     │  NAZ  │           ╱ │                  ╱ │
     │======►│--------► (  │   [Zone of]     (  │ ====> Menuju Lensa Ion &
     │       │  Jet      ╲ │   [Silence]      ╲ │       Quadrupole
     │       │  Supersonik╲│  [Mach Disk]     ╲│
     └───────┘             ▲       ▲           ▲
                    Water-cooled  Shock     Ujung Lancip
                        Block     Waves    Menyendok Inti
```

### A. Pembentukan Jet Supersonik (*Free-Jet Expansion*)
Ketika gas plasma argon menembus lubang sampler ($0.8 - 1.2\text{ mm}$) menuju ruang bertekanan $1 - 2\text{ Torr}$, rasio penurunannya melebihi ambang batas kritis ekspansi fluida ($P_0 / P_b \approx 760 / 1.5 \approx 500$).
- Gas mengalami akselerasi luar biasa hingga melampaui kecepatan suara lokal (**$Mach > 1$**, mencapai $Mach \approx 5 - 10$).
- Terjadi **pendinginan adiabatik ekstrem**: energi termal acak gas argon ($T \sim 6.000\text{ K}$) dikonversi secara cepat menjadi energi kinetik terarah ke depan ($v_z \approx 2 \times 10^3\text{ m/s}$).

### B. Struktur Gelombang Kejut (*Shock Waves*) & *Zone of Silence*
Interaksi antara semburan gas supersonik dengan gas latar belakang di ruang antarmuka menghasilkan sistem gelombang kejut tertutup:
1. **Barrel Shock:** Dinding gelombang kejut berbentuk barel di selubung samping semburan.
2. **Mach Disk:** Dinding batas gelombang kejut datar tegak lurus di bagian depan semburan. Di dinding ini, gas supersonik mendadak melambat kembali ke subsonik, suhunya melonjak, dan terjadi turbulensi parah.
3. **Zone of Silence (Zona Hening):** Daerah steril di dalam kubah semburan supersonik, terletak tepat di antara lubang sampler cone dan dinding *Mach disk*.
   - Di dalam *Zone of Silence*, molekul gas dan ion melesat lurus tanpa saling bertabrakan dan terisolasi dari gangguan gas luar.
   - Sifat stoikiometri dan komposisi ion analit dari plasma terjaga secara murni di zona ini.

### C. Mengapa Bentuknya Harus Kerucut Runcing (*Cone*)?
- **Kegagalan Pelat Datar (*Flat Plate Pitfall*):**  
  Jika skimmer dibuat dari pelat datar berlubang (*flat pinhole plate*), semburan gas supersonik akan membentur permukaan datar tersebut dan memicu gelombang kejut busur terlepas (**_detached bow shock wave_**). *Bow shock* ini akan mengacaukan aliran, memanaskan kembali gas, memicu rekombinasi ion-elektron, dan menghamburkan berkas ion hingga kehilangan sinyal secara total.
- **Peran Ujung Lancip Skimmer Cone:**  
  Skimmer didesain berupa kerucut bersudut lancip (sudut luar $\approx 60^\circ$, sudut dalam $\approx 50^\circ$) agar ujungnya dapat **menyusup menusuk langsung ke dalam *Zone of Silence*** tepat sebelum *Mach disk*. Bentuk ini "menyendok" (*skims*) inti aliran analit di tengah berkas supersonik tanpa memicu pembentukan gelombang kejut busur di mulut lubangnya.

### D. Integritas Plasma & Panjang Debye (*Debye Length*)
Pada mulut sampler cone, plasma argon masuk sebagai massa netral (*bulk neutral plasma*).
- **Panjang Debye ($\lambda_D$):** Jarak di mana ketidakseimbangan muatan listrik lokal diselubungi oleh elektron. Pada plasma ICP ($T_e \sim 10.000\text{ K}, n_e \sim 10^{15}\text{ cm}^{-3}$), nilai $\lambda_D$ hanya sekitar **$10^{-4}\text{ mm}$**.
- Karena diameter lubang sampler cone ($0.8 - 1.2\text{ mm}$) ribuan kali lebih besar daripada $\lambda_D$, gaya elektrodinamik permukaan logam **tidak mengubah komposisi ion analit**. Berkas ion masuk dengan integritas kelimpahan yang representatif terhadap plasma aslinya.

---

## 4. Ketahanan Termal, Material Cones & SOP Pemeliharaan

### A. Mengapa Sampler Cone Tidak Meleleh Disentuh Plasma $10.000\text{ K}$?
Meskipun *outer gas* torch menjaga tabung kuarsa, api plasma **benar-benar menempel langsung (*impinges directly*)** pada puncak sampler cone.
- Titik leleh Nikel ($1.455^\circ\text{C} \approx 1.728\text{ K}$) dan Platinum ($1.768^\circ\text{C} \approx 2.041\text{ K}$) jauh di bawah suhu plasma ($6.000 - 10.000\text{ K}$).
- **Pertahanan Utama (Konduksi Termal Ekstrem):**  
  Sampler cone dipasang menempel rapat pada blok penyangga (*interface housing*) berbahan **tembaga atau aluminium tebal** yang dialiri sirkulasi air dingin pendingin (*water chiller*) secara kontinu pada suhu $15 - 20^\circ\text{C}$.
- Karena laju konduksi panas tembaga dan nikel sangat cepat, panas plasma langsung dilarikan ke aliran air pendingin sebelum logam mencapai titik lelehnya, menjaga suhu fisik puncak cone stabil di kisaran $400 - 600^\circ\text{C}$.

### B. Komparasi Material: Nickel vs. Platinum Cone

| Parameter Evaluasi | Nickel (Ni) Cone | Platinum (Pt) Cone |
| :--- | :--- | :--- |
| **Material Dasar** | Logam Nikel murni ($100\%\ \text{Ni}$) | Ujung kerucut Platina murni dengan dasar tembaga (*copper base*) |
| **Biaya Relatif** | Ekonomis / Standar pabrikan | Sangat mahal ($\sim 4 - 6\times$ lipat harga Ni) |
| **Ketahanan Oksidasi & Suhu** | Moderat; membentuk lapisan oksida abu-abu | Sangat unggul; inert terhadap oksidasi termal |
| **Ketahanan Asam Korosif** | Rentan terhadap $\text{HNO}_3 > 5\%$, Aqua Regia pekat, dan rusak parah oleh $\text{HF}$ | Tahan terhadap asam pekat oksidator, Aqua Regia, dan asam $\text{HF}$ |
| **Aplikasi Wajib** | Analisis rutin air minum, air sungai, pangan standar (matriks $\text{HNO}_3\ 1 - 2\%$) | Sampel dekomposisi silika ($\text{HF}$), digesti batuan/mineral pekat, pelarut organik |

### C. Protokol SOP Pembersihan: Mengapa Asam Nitrat Dilarang untuk Nickel Cone?
Sesuai **IK-BRIN-LKIMIA-6.4-09 hal. 23** dan panduan training **OT32 hal. 81**:

```
[ METODE PEMBERSIHAN RESMI INTERFACE CONES ]
├── Nickel Cones:
│   ├── Larutan  : Asam Format (Formic Acid) 5% - 10% (v/v)
│   ├── Metode   : Sonikasi ultrasonik 5 menit
│   └── Pembilasan: Aquademineral / Ultrapure water sonikasi 2x5 menit, keringkan gas Ar
└── Platinum Cones:
    ├── Larutan  : HNO₃ 3% (v/v) ATAU Asam Format 10% (v/v)
    ├── Metode   : Sonikasi ultrasonik 5 menit
    └── Pembilasan: Aquademineral / Ultrapure water sonikasi 2x5 menit, keringkan gas Ar
```

> ⚠️ **BAHAYA KIMIA:**  
> Dilarang keras membersihkan Nickel cone menggunakan $\text{HNO}_3$ pekat!  
> Asam nitrat pekat akan melarutkan logam Nikel secara aktif:
> $$\text{Ni}_{(s)} + 2\text{HNO}_{3(aq)} \longrightarrow \text{Ni(NO}_3)_{2(aq)} + \text{H}_{2(g)} \uparrow$$
> Reaksi ini mengikis bibir presisi lubang orifice, memperbesar diameternya, dan merusak dinamika pemompaan vakum secara permanen.

---

## 5. Pencegahan Kopling Kapasitif & Secondary Discharge

Dalam pengoperasian awal ICP-MS, sering timbul percikan loncatan bunga api listrik sekunder (*secondary discharge*) antara plasma dan ujung sampler cone.

```
                    [ Tanpa Netralisasi RF ]                   [ Dengan RF Grounding ]
                 Kopling Kapasitif Terbuka                  Potensial Plasma = 0 V
           ──────────────────────────────────────     ──────────────────────────────────────
           Potensial Plasma : 100 - 200 V             Potensial Plasma : ~0 V
           Gejala           : Loncatan bunga api      Gejala           : Kontak hening tenang
           Dampak           : Orifice terkikis cepat  Dampak           : Lubang cone awet presisi
           Sebaran Energi   : ΔE = 20 - 40 eV         Sebaran Energi   : ΔE = 5 - 10 eV (Fokus Tajam)
```

- **Mekanisme Penyebab:** Kopling elektrostatik/kapasitif antara koil beban RF (*load coil*) dengan plasma menghasilkan potensial mengambang ratusan volt pada plasma relatif terhadap cone yang terhubung ke arde/tanah (*ground*).
- **Dampak Buruk:** Percikan bunga api melebarkan sebaran energi kinetik ion (*ion kinetic energy spread*) hingga $20 - 40\text{ eV}$. Lensa optik elektrostatik di hilir tidak mampu memfokuskan berkas ion dengan sebaran energi selebar ini, memicu hilangnya resolusi dan sensitivitas.
- **Solusi Arsitektur Modern:** Penyeimbangan rangkaian osilator RF (*balanced RF oscillator*), pentanahan lilitan tengah koil (*center-tapped grounded coil*), atau penyisipan pelat perisai logam (*grounded shield plate*) di antara koil dan tabung torch ([Robert Thomas, hal. 32–34](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners,%20Second%20Edition%20(Practical%20Spectroscopy)%20(2008,%20CRC%20Press)%20-%20libgen.li.pdf#page=58)).

---

## 6. Falsification Lab & Analisis Kerusakan Lapangan

### Skenario 1: Bahaya Matriks TDS Tinggi ($> 0.2\% / 2.000\text{ ppm}$)
- **Gejala:** Sinyal analit dan internal standard mengalami penurunan melayang (*signal drift downward*) secara progresif selama rangkaian batch pengujian.
- **First-Principles Root Cause:** Berbeda dari ICP-OES yang hanya memancarkan foton menembus cermin/prisma kuarsa, ICP-MS wajib mentransfer materi atomik fisik melintasi batas gradien suhu ekstrem ($8.000\text{ K} \to 500^\circ\text{C}$).
  Uap garam mineral ($NaCl, CaCO_3, silikat$) mengalami **desublimasi dan kristalisasi instan** di tepian dingin lubang sampler orifice ($0.8 - 1.0\text{ mm}$). Kerak garam mempersempit aperture lubang (*aperture clogging*), mencekik transmisi berkas ion menuju skimmer cone ([Robert Thomas, hal. 31](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners,%20Second%20Edition%20(Practical%20Spectroscopy)%20(2008,%20CRC%20Press)%20-%20libgen.li.pdf#page=57)).
- **Tindakan Mitigasi:** Pengenceran larutan (*dilution*), penggunaan sistem injeksi aerosol berpelarut minim (*argon gas dilution / aerosol dilution*), atau pembilasan asam berkala.

### Skenario 2: Erosi Lubang Orifice Sampler ($1.0\text{ mm} \longrightarrow 1.4\text{ mm}$)
- **Gejala Diagnostik:** Tekanan ruang antarmuka naik ($> 2.5\text{ Torr}$), sensitivitas elemen jatuh bebas, dan rasio oksida melonjak drastis ($\text{CeO}^+/\text{Ce}^+ > 2 - 3\%$).
- **First-Principles Root Cause:**
  1. **Lonjakan Throughput Gas:** Luas lubang meningkat secara kuadratik ($A \propto r^2$):
     $$\frac{A_{1.4}}{A_{1.0}} = \left(\frac{1.4}{1.0}\right)^2 = 1.96 \approx 2\times$$
     Debit gas panas atmosferik yang masuk ke antarmuka berlipat ganda, melampaui kapasitas hisap pompa rotary pendukung.
  2. **Runtuhnya Zone of Silence (*Mach Disk Collapse*):** Jarak posisi *Mach Disk* ($x_M$) menyusut mendekati lubang sampler:
     $$x_M \propto D \cdot \sqrt{\frac{P_0}{P_{\text{interface}}}}$$
     Akibat naiknya $P_{\text{interface}}$, dinding gelombang kejut *Mach Disk* ambruk mundur dan menelan ujung skimmer cone. Skimmer tidak lagi menyendok *Zone of Silence*, melainkan menelan pusaran gas turbulen.
  3. **Peningkatan Rekombinasi Oksida:** Pendinginan adiabatik yang diiringi tingginya kerapatan molekul gas pada tekanan vakum buruk memicu jutaan tabrakan pembentukan kembali oksida:
     $$\text{Ce}^+ + \text{O} \longrightarrow \text{CeO}^+ \quad \text{atau} \quad \text{Ce}^+ + \text{H}_2\text{O} \longrightarrow \text{CeO}^+ + \text{H}_2$$
     Rasio oksida melanggar kriteria penerimaan harian ($\le 2\%$) pada SOP BRIN iCAP Q.

### Skenario 3: Transisi Pasca-Skimmer & Munculnya *Space-Charge Effect*
- Tepat di balik lubang skimmer cone, lensa ekstraksi ion (*extraction lens*) diberi tegangan negatif untuk menyedot kation analit ($M^+$) dan membuang elektron.
- Berkas netral plasma mendadak berubah wujud menjadi **berkas murni kation positif padat**.
- Terjadi **Gaya Tolak Coulomb (*Coulombic Repulsion*)** antar-ion positif ($F \propto q_1 q_2 / r^2$).
- Sesuai hukum inersia Newton ($a = F/m$), kation ringan ($^7\text{Li}^+, ^9\text{Be}^+$) terlempar ke tepi luar sumbu ion oleh tolakan kation matriks yang lebih berat ($^{208}\text{Pb}^+, ^{238}\text{U}^+$). Fenomena ini menjadi gerbang bahasan krusial menuju sistem lensa optik ion (*Ion Focusing System*).

---

## 7. Rujukan Primer & Landasan Verifikasi (Ground Truth Citations)

1. **Robert Thomas**, *Practical Guide to ICP-MS: A Tutorial for Beginners*, 2nd Edition (2008), CRC Press:
   - *Chapter 5: "Interface Region"* (hal. 31–37 / PDF hal. 57–63): Dimensi lubang cone, pemompaan diferensial, batas TDS $< 0.2\%$, kopling kapasitif RF, dan sebaran energi ion.
   - *Chapter 6: "Ion-Focusing System"* (hal. 39–40 / PDF hal. 65–66): Transisi keluar dari skimmer cone dan inefisiensi transmisi akibat *space-charge effect*.
2. **Douglas A. Skoog, F. James Holler, Stanley R. Crouch**, *Principles of Instrumental Analysis*, 7th Edition (2018), Cengage Learning:
   - *Chapter 11C-1: "Instruments for ICPMS"* (hal. 263 / PDF hal. 285): Skema *differentially pumped interface coupler*, pendinginan ekspansi gas cepat, dan peranan skimmer cone.
3. **Badan Riset dan Inovasi Nasional (BRIN)**, *Instruksi Kerja Pengoperasian ICP-MS Thermo Fisher Scientific iCAP Q*, No. Dok: `IK-BRIN-LKIMIA-6.4-09` Rev 01 (2026):
   - *Bagian 12.3 & 12.4 (hal. 23)*: Prosedur pembersihan cone perendaman asam format $5\%$, kriteria toleransi rasio oksida ($\text{CeO}^+/\text{Ce}^+ \le 2\%$) dan rasio muatan ganda ($\text{Ce}^{2+}/\text{Ce}^+ \le 3\%$).
4. **Materi Training ICP-MS (Principle, Instrumentations, and Applications) INTENS**, No. Dok: `OT32`:
   - *Slide 27 & 81*: Spesifikasi dual cone Ni/Pt, ultrasonik asam format $5 - 10\%$ untuk Ni cone vs $\text{HNO}_3\ 3\%$ untuk Pt cone.
5. **Douglas, D. J., & French, J. B.**, *Spectrochimica Acta Part B: Atomic Spectroscopy*, 41B(3), 197–204 (1986):
   - Landasan aerodinamika pembentukan *supersonic free-jet expansion*, *Mach disk*, dan ekstraksi ion via *skimmer cone*.
