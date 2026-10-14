---
title: Rekayasa Sistem Introduksi Sampel ICP-MS (Pompa Peristaltik, Nebulizer Pneumatik, dan Cyclonic Spray Chamber)
domain: analytical_chemistry
technique: icp-ms
tags:
  - analytical-chemistry
  - instrumentation
  - first-principles
  - sample-introduction
  - nebulizer
  - spray-chamber
  - fluid-dynamics
date: 2026-09-19
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-learning-roadmap]]"
  - "[[mekanika-quadrupole-rf-dc]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
  - "[[icp-ms-tuning-qc-dan-lab-sparring]]"
---

# Rekayasa Sistem Introduksi Sampel ICP-MS (Pompa Peristaltik, Nebulizer, dan Spray Chamber)

> **One-Sentence Core Phenomenon:**  
> Sistem introduksi sampel adalah gerbang konversi materi yang menaklukkan disparitas viskositas larutan melalui perpindahan volume positif, mencabik cairan menjadi kabut aerosol via geseran gas Argon pneumatik, dan menyaring droplet mikro ($< 2 - 5\ \mu\text{m}$) menggunakan pusaran inersia sentrifugal siklonik demi menjaga integritas termal plasma.

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena Fisika / Mekanika yang Terjadi | Parameter Kritis & Batas Operasional |
| :--- | :--- | :--- | :--- |
| **Layer 0**<br>*(SOP Lab & Operasional)* | Botol Sampel $\to$ Pompa $\to$ Nebulizer $\to$ Drain | Aliran stabil $\sim 0.3 - 0.4\text{ mL/min}$, pembuangan $> 95\%$ cairan ke botol limbah, batas TDS larutan $< 0.2\%$, pembersihan berkala kapiler nosel. | Uptake delay $\sim 30 - 45\text{ s}$, toleransi TDS $< 2.000\text{ ppm}$, pencucian mingguan via Eluo cleaner, pelepasan klem selang saat idle. |
| **Layer -1**<br>*(Mekanika Komponen)* | Rollers Pompa, Capillary Quartz, Cyclonic Chamber, Peltier Cooler | Oklusi $100\%$ selang polimer, penyemprotan gas Ar $20 - 30\text{ psi}$ paralel nosel, pusaran tornado tangensial, pendinginan termoelektrik cangkang spray chamber ke $+2^\circ\text{C}$. | ID kapiler nebulizer $50 - 100\ \mu\text{m}$, laju gas carrier $\sim 1\text{ L/min}$, volume ruang buffer $50 - 100\text{ mL}$, suhu Peltier $+2^\circ\text{C} \pm 0.5^\circ\text{C}$. |
| **Layer -2**<br>*(Fisika & Termodinamika)* | Dinamika Fluida & Kesetimbangan Fase | Aliran laminar Poiseuille vs Positive Displacement ($Q = V_{\text{pocket}} \cdot N \cdot \text{RPM}$), instabilitas Kelvin-Helmholtz (shear gas-liquid), gaya inersia sentrifugal Stokes ($F_c \propto r^3$), termodinamika penguapan Clausius-Clapeyron ($P_{\text{vap}}$). | $\Delta H_{\text{vap}}$ air ($40.7\text{ kJ/mol}$), cut-off aerodinamik droplet $< 2 - 5\ \mu\text{m}$, tekanan uap air $23.8\text{ Torr}$ ($25^\circ\text{C}$) $\to 5.3\text{ Torr}$ ($+2^\circ\text{C}$). |

---

## 2. Pompa Peristaltik: Mengapa Mampu Mengalahkan Viskositas?

### A. Kelemahan Hisapan Alami (*Self-Aspiration / Venturi*)
Jika cairan disedot murni mengandalkan perbedaan tekanan statis gas Argon ($\Delta P$) di ujung nebulizer, laju alir fluida tunduk pada **Hukum Poiseuille**:
$$Q = \frac{\pi \cdot \Delta P \cdot r^4}{8 \cdot \eta \cdot L}$$

* **Ketergantungan Viskositas ($\eta$):** Laju alir volumetrik ($Q$) berbanding terbalik dengan viskositas dinamik fluida.
* **Bias Analitik:** Larutan baku kalibrasi yang encer ($1\%\ \text{HNO}_3$) akan terhisap kencang, sedangkan sampel nyata berkadar garam/organik tinggi (seperti ekstrak sarang walet atau urin) terhisap jauh lebih lambat. Instrumen akan mengalami bias negatif (*underestimation*) parah karena massa analit per detik yang disuplai ke plasma anjlok.

### B. Mekanika Perpindahan Positif (*Positive Displacement*)
Pompa peristaltik memecahkan masalah ini dengan prinsip penjeratan volume mekanis (*volumetric trapping*), bekerja persis seperti **jari yang mengurut pasta gigi keluar dari wadahnya**:

```
             Arah Putaran Roda Rotor --->
             
     [Roller 1]                      [Roller 2]
        ( O )                           ( O )
  =======|================================|=======  <- Selang Elastis (Santoprene/PVC)
  -------|--------------------------------|-------
       (Jepit rapat)    [ KANTONG CAIRAN ]    (Jepit rapat)
                         Volume Tetap (V)
  ================================================  <- Plat Penyangga (Platen/Bridge)
```

1. **Oklusi Total ($100\%$):** Roller menekan selang elastis hingga gepeng rapat, mengunci cairan di belakangnya agar tidak bisa mengalir balik.
2. **Kantong Geometris Tetap:** Volume di antara dua roller ($V_{\text{kantong}}$) bernilai konstan:
   $$V_{\text{kantong}} = \text{Luas Penampang Selang} \times \text{Jarak Antar-Roller}$$
3. **Persamaan Laju Alir:**
   $$Q = V_{\text{kantong}} \times N_{\text{roller}} \times \text{RPM}$$

*Variabel viskositas ($\eta$) tereliminasi dari persamaan.* Selama torsi motor pompa mampu memutar rotor, volume cairan yang dihantarkan per satuan waktu akan konstan terlepas dari apakah cairan itu encer atau kental.

### C. Trade-Off Mekanis & Batas Operasional
* **Aliran Berdenyut (*Pulsating Flow*):** Transisi saat roller melepaskan jepitan menimbulkan fluktuasi tekanan berkala yang dapat merusak presisi (%RSD) jika tidak diredam oleh spray chamber.
* **Kelelahan Material (*Tubing Fatigue*):** Selang yang terus-menerus digilas roller akan kehilangan elastisitas balik (*elastic rebound*). Jika selang gepeng permanen, $V_{\text{kantong}}$ menyusut dan laju alir melayang (*drift*).
  > **Aturan Lab:** Selalu kendorkan tuas penjepit (*cam release*) saat instrumen dimatikan agar selang tidak aus dan tidak gepeng permanen ([[IK-BRIN-LKIMIA-6.4-09, hal. 23]]).

---

## 3. Nebulizer Pneumatik: Fisika Pencacahan Cairan Menjadi Kabut

Tipe paling umum pada analisis trace adalah **Concentric Glass Nebulizer** (misal tipe *MicroMist*).

```
   Gas Argon Tekanan Tinggi (20-30 psi)  ===============>  [ Semprotan Aerosol ]
                                                           /  (Disrupsi Geser)
   Sampel Cair (dari Pompa) ---------[ Kapiler 50-100 µm ]--
                                                           \
   Gas Argon Tekanan Tinggi (20-30 psi)  ===============>  [ Semprotan Aerosol ]
```

1. **Gaya Geser Pneumatik (*Pneumatic Shear*):** Cairan dialirkan lambat lewat kapiler kaca pusat ($ID \approx 50 - 100\ \mu\text{m}$). Gas Argon melesat kencang di celah cincin luar dengan kecepatan mendekati sonik.
2. **Instabilitas Gelombang Fluida:** Perbedaan kecepatan ekstrem antara gas dan cairan memicu instabilitas *Kelvin-Helmholtz*, menarik kolom cairan menjadi filamen/lembaran tipis yang kemudian putus menjadi jutaan butiran droplet mikroskopis (*aerosol*).

### Dua Batas Fisis & Kimia Kritis Nebulizer:
1. **Fenomena *Salting Out* & Penyumbatan Garam (TDS $> 0.2\%$):**
   Gas Argon murni bertekanan tinggi bersifat mutlak kering (RH $0\%$). Ketika gas kering ini bergesekan dengan film cairan di ujung nosel bertekanan rendah, terjadi **penguapan kilat pelarut (*flash desolvation*)**. Jika larutan mengandung garam terlarut tinggi, penguapan pelarut lokal menyebabkan konsentrasi garam melampaui $K_{sp}$, memicu presipitasi kerak kristal garam di bibir nosel (*salting out*). Nosel tersumbat dan aliran tercekik.
2. **Erosi Kimia Asam Hidrofluorat ($\text{HF}$):**
   Sampel mineral/batuan silikat memerlukan asam $\text{HF}$ untuk dekomposisi. Namun, kuarsa/kaca terbuat dari silika:
   $$\text{SiO}_{2(s)} + 4\text{HF}_{(aq)} \longrightarrow \text{SiF}_{4(g)} \uparrow + 2\text{H}_2\text{O}_{(l)}$$
   $\text{HF}$ mengikis habis geometri kapiler $50\ \mu\text{m}$ nebulizer kaca, menghancurkan dinamika semprotan, serta membanjiri detektor dengan interferensi Silikon ($^{28}\text{Si}$).
   * **Solusi Mutlak:** Wajib beralih ke *Inert HF-Resistant Kit* berbahan polimer fluorokarbon inert seperti **PFA (*Perfluoroalkoxy*)** atau **PTFE (*Teflon*)** dengan injektor torch safir/platina.
3. **Pantangan Mekanik:**
   *Dilarang keras membersihkan lubang kapiler kaca dengan kawat atau jarum logam!* Goresan mikro pada kaca tipis akan memecahkan bibir kapiler (*chipping*). Pembersihan wajib menggunakan **Eluo Nebulizer Cleaner** dengan metode semprot balik (*hydraulic back-flush*).

---

## 4. Cyclonic Spray Chamber & Pendingin Peltier ($+2^\circ\text{C}$)

Mengapa sistem membuang $> 95\%$ cairan dan hanya mengizinkan $\approx 1 - 2\%$ droplet masuk ke plasma?

```
                     [ Menuju Injektor Plasma Torch ]
                                  ^
                                  |  (Droplet Halus < 2-5 µm)
                               +-----+
                               |     |  <- Vortex Core
                 +-------------+     +-------------+
                 |                                 |
                 |     PUSARAN SIKLONIK            |
                 |       (VORTEX TORNADO)          |
  Aerosol dari   |                                 |
  Nebulizer ===> ) (Inersia Sentrifugal Lempar      |
  (Tangensial)   |  Droplet Kasar > 5 µm ke Dinding)
                 |                                 |
                 +----------------+----------------+
                                  |
                                  v
                        [ Saluran Pembuangan / Drain ]
```

### A. Mekanisme Pemilahan Ukuran Droplet (Gaya Sentrifugal vs Stokes Drag)
Di dalam tabung *cyclonic spray chamber*, aerosol ditembakkan miring/tangensial ke dinding silinder sehingga membentuk pusaran tornado (*cyclonic vortex*):
* **Gaya Sentrifugal:** $F_c = m \cdot \frac{v^2}{r} \propto r_{\text{droplet}}^3$. Gaya yang melempar partikel ke dinding kaca berbanding lurus dengan **pangkat tiga jari-jari droplet**!
* **Gaya Hambatan Gesek Gas (*Drag Force*):** $F_d \propto r_{\text{droplet}}$.

**Hasil Separasi:**
* **Droplet Kasar ($> 2 - 5\ \mu\text{m}$):** Inersia massanya terlalu besar. Gaya sentrifugal mendominasi dan melemparkannya menabrak dinding kaca (*impaction*), menyatu menjadi aliran cairan, lalu dibuang ke selang *drain*.
* **Droplet Halus ($< 2 - 5\ \mu\text{m}$):** Inersia sentrifugalnya sangat kecil. Droplet patuh pada aliran gas, terperangkap di mata pusaran pusat (*vortex core*), lalu naik vertikal menuju cerobong injektor plasma.

### B. Fungsi Peredam Denyut (*Pulse Dampening*)
Spray chamber memiliki volume internal $\approx 50 - 100\text{ mL}$. Ruang ini bertindak sebagai **kapasitor/akumulator pneumatik**. Gelombang denyutan cairan akibat roller pompa peristaltik terdistribusi dan terbaur secara merata di dalam pusaran ruang spray chamber, sehingga kabut mikro yang keluar menuju torch mengalir dengan stabilitas emisi yang sangat tenang (%RSD $< 1\%$).

### C. Termodinamika Pendingin Peltier ($+2^\circ\text{C}$)
Tabung cyclonic spray chamber dibungkus oleh cangkang logam termoelektrik **Peltier Cooler** yang suhunya dikunci dingin stabil pada **$+2^\circ\text{C}$**:

1. **Penekanan Tekanan Uap Air ($P_{\text{vap}}$):**
   Berdasarkan persamaan *Clausius-Clapeyron*:
   * Pada suhu ruang lab ($25^\circ\text{C}$): $P_{\text{H}_2\text{O}} \approx 23.8\text{ Torr}$.
   * Pada suhu pendingin ($+2^\circ\text{C}$): $P_{\text{H}_2\text{O}} \approx 5.3\text{ Torr}$.
   * **Hasil:** Beban molekul uap air yang melayang ke plasma **terpangkas hampir $80\%$**! Uap air berlebih terkondensasi menjadi air cair di dinding kaca dan terbuang ke drain.
2. **Supresi Interferensi Oksida Poliatomik ($\text{CeO}^+/\text{Ce}^+$):**
   Air adalah sumber utama radikal oksigen di dalam plasma ($H_2O \to 2H + O$). Dengan memangkas uap pelarut, kepadatan oksigen di plasma turun drastis, beban pendinginan plasma berkurang, dan pembentukan oksida refraktori dapat ditekan hingga memenuhi kriteria keberterimaan harian:
   $$\frac{^{140}\text{Ce}^{16}\text{O}^+}{^{140}\text{Ce}^+} \le 2\%$$
3. **Batas Fisis Pembekuan ($< 0^\circ\text{C}$):**
   Suhu tidak boleh diturunkan hingga $< 0^\circ\text{C}$ (misal $-5^\circ\text{C}$), karena kondensasi air di dinding kaca dan kapiler drain akan membeku menjadi lapisan es (*frost blockage*), menyumbat aliran aerosol, dan mematikan sistem secara seketika. Suhu $+2^\circ\text{C}$ adalah titik kompromi termodinamika terdingin yang paling aman di atas titik beku air.

---

## 5. Falsification Lab & Matriks Troubleshooting Meja Lab

| Gejala Gangguan di Lab | Root Cause Analisis Fisika / Kimia | Tindakan Korektif Terverifikasi |
| :--- | :--- | :--- |
| **Presisi sinyal buruk (%RSD $> 5\%$)** | Selang peristaltik kendor, aus, atau klem penekan (*bridge tensioner*) terlalu longgar sehingga timbul selip dan denyutan parah. | Kencangkan klem penekan selang atau ganti selang pompa baru; pastikan orientasi pemasangan klem tidak terbalik. |
| **Sinyal analit & ISTD drop mendadak ke nol, tekanan gas naik** | Terjadi *salting out* (kristalisasi garam) di ujung kapiler nosel nebulizer akibat injeksi sampel berkadar TDS $> 0.2\%$. | Hentikan injeksi, lakukan semprot balik (*back-flush*) menggunakan *Eluo Nebulizer Cleaner* dengan air ultra-pure / $5\%\ \text{HNO}_3$. |
| **Rasio CeO+/Ce+ melonjak tinggi ($> 3\%$) saat Daily Tuning** | Suhu Peltier cooler mati atau tidak stabil (naik ke suhu ruang $25^\circ\text{C}$), menyebabkan uap air membanjiri plasma. | Periksa sirkulasi cairan chiller pendingin eksternal dan pastikan setting temperatur Peltier di software instrumen terkunci di $+2^\circ\text{C}$. |
| **Sinyal background Silikon ($^{28}\text{Si}$) dan Boron ($^{11}\text{B}$) sangat tinggi** | Sampel mengandung asam $\text{HF}$ yang mengikis dinding kaca nebulizer dan spray chamber. | Segera bilas instrumen; ganti seluruh kit sample intro kaca dengan kit polimer PFA/PTFE inert. |

---

## 6. Referensi Terverifikasi (Ground Truth)

1. **Robert Thomas**, *Practical Guide to ICP-MS: A Tutorial for Beginners*, 2nd Edition (2008), CRC Press:
   - Chapter 3: *Sample Introduction* (hal. 13–21 / PDF hal. 40–48) [Robert Thomas (2008)](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Robert%20Thomas%20-%20Practical%20Guide%20to%20ICP-MS_%20A%20Tutorial%20for%20Beginners%2C%20Second%20Edition%20%28Practical%20Spectroscopy%29%20%282008%2C%20CRC%20Press%29%20-%20libgen.li.pdf#page=40).
2. **Douglas A. Skoog, F. James Holler, Stanley R. Crouch**, *Principles of Instrumental Analysis*, 7th Edition (2018), Cengage Learning:
   - Chapter 11C: *Inductively Coupled Plasma Mass Spectrometry* (hal. 263 / PDF hal. 286) [Skoog et al. (2018)](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/Crouch%2C%20Stanley%20R._Holler%2C%20F.%20James_Skoog%2C%20Douglas%20A%20-%20Principles%20of%20Instrumental%20Analysis%20%282018_2016%2C%20CENGAGE%20Learning%29%20-%20libgen.li.pdf#page=286).
3. **Instruksi Kerja BRIN**, *Pengoperasian Inductively Coupled Plasma Mass Spectrometry (ICP-MS) Thermo Scientific iCAP Q*, No. Dok: IK-BRIN-LKIMIA-6.4-09, Rev 02 (2026):
   - Bagian 12.2 & 12.3: Pemeliharaan Mingguan dan Bulanan Sample Introduction System (hal. 23) [IK-BRIN iCAP Q](file:///home/zidan/Projects/learning-hub/references/Instrumentations/ICP-MS/IK-BRIN-LKIMIA-6.4-09%20Pengoperasian%20ICP-MS%20iCAP%20Q_rev%2002%20final.pdf#page=23).
