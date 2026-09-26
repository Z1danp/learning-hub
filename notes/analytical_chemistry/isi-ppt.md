## Chapter 1: Why ICP-MS
- Komparasi Flame AAS vs GF-AAS vs ICP-OES vs ICP-MS
- Deteksi foton optik (emisi/absorpsi) vs perhitungan ion massa diskrit
- First Principles of ICP-MS  or saha eq

## Chapter 2: Anatomi & First Principles Instrumen
- Aerosol ke Detektor: sample intro -->  plasma ionisasi --> interface cone --> ion lens --> cell --> mass filter --> detektor
- Ionisasi dan tantangan interface
	- - _Plasma Argon (∼6.000–8.000 K∼6.000–8.000 K)_: Kenapa hampir semua unsur terionisasi menjadi M+M+ (derajat ionisasi Saha).
	- _Interface Cone (Sampling & Skimmer)_: Transisi ekstrem dari tekanan atmosfer (1 atm1 atm) ke vakum tinggi (10−5−10−6 mbar10−5−10−6 mbar). _Mengapa ini bagian paling sensitif terhadap matriks kotor?_
- Pemisahan massa dan deteksi
	- Quadrupole: Kombinasi tegangan DC dan RF  mathiue eq (U + V cos $\omega$t) sebagai filter stabilitas lintasan ion
	- Electron multiplier: Pulse counting mode untuk sensivitas hingga hitungan ion tunggal
## Chapter 3: Interferensi Analysis
- **Spektral vs Non-Spektral Interferens**
	- - Mengapa ICP-MS bisa "tertipu"? Isobarik (unsur beda, massa sama) vs Poliatomik (kombinasi plasma gas + matriks).
	- Contoh nyata di lab: 40Ar35Cl+40Ar35Cl+ menimpa 75As75As (terutama jika ada sisa garam/klorida), atau 40Ar16O+40Ar16O+ menimpa 56Fe56Fe.
- Collision/Reaction cell: mekanisme KED
	- - Bedah mekanisme: Mengapa gas Helium inert bisa memotong sinyal poliatomik?
	- _First-principles_: Ukuran penampang tumbukan (_collision cross-section_) poliatomik lebih besar dibanding analit monoatomik →→ kehilangan energi kinetik lebih banyak →→ ditahan oleh _energy barrier_ di pintu keluar sel.
## Chapter 4: Preparasi Sample
- Penjelasan terkait preparasi sampel
- Penjelasan macam-macam teknik destruksi
- Hal yang harus diperhatikan
	- TDS
		- - Batasan TDS <0.2%<0.2% (<2000 ppm<2000 ppm) — mengapa tidak boleh seperti ICP-OES/AAS yang tahan TDS tinggi?
		- Pemilihan asam: Keunggulan mutlak HNO3HNO3​ vs bahaya HClHCl (interferensi Cl), H2SO4H2​SO4​ (viskositas & deposit belerang), atau HFHF (harus inert kit).
	- Matriks Sarang Bulu Walet
		- - Karakteristik sampel: Matriks organik & protein tinggi.
		- SOP Digesti Microwave (MARS6): Kenapa butuh HNO3​ dan suhu tinggi (∼190∘C∼190∘C)?
		- Bahaya sisa karbon organik (_residual carbon_) terhadap instrumen.
## Chapter 5: Operasional, QC, dan Maintenance
- Daily Startup & Tuning Criteria (Qtegra Workflow)
	- Makna larutan tuning (Li, Co, In, Ba, Ce, ULi, Co, In, Ba, Ce, U):
	    - Mengapa rasio oksida CeO+/Ce+ harus <2%?
	    - Mengapa ion muatan ganda Ba2+/Ba+ harus <3%?
	- Macam-macam potensial ionisasi 2 unsur pada eV Ar (?)
- QC ISO/IEC 17025
	- - Peran vital **Internal Standard (IS)** (misal Sc, Y, In, BiSc, Y, In, Bi): Bagaimana IS mengoreksi _instrument drift_ dan variasi fisik aerosol.
	- Blank, Calibration verification (CCV/QC standard), CRM, dan Spike Recovery.
- Keausan tubing peristaltik (fluktuasi sinyal / presisi buruk)
- Kebersihan sample/skimmer cone (kapan harus sonikasi/dibersihkan)
