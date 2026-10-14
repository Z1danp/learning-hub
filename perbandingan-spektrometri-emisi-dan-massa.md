---
title: Perbandingan Spektrometri Emisi dan Massa (ICP-OES vs ICP-MS vs GC-MS)
domain: analytical_chemistry
technique: spectroscopy-and-mass-spectrometry
tags:
  - analytical-chemistry
  - first-principles
  - icp-oes
  - icp-ms
  - gc-ms
date: 2026-09-13
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
  - "[[mekanika-quadrupole-rf-dc]]"
---

# Perbandingan Spektrometri Emisi dan Massa (ICP-OES vs ICP-MS vs GC-MS)

> **One-Sentence Core Phenomenon:**  
> Pilihan instrumen ditentukan oleh wujud entitas yang diukur (foton optik vs partikel bermassa) dan ambang batas energi eksitasi/ionisasi yang sanggup disediakan oleh sumber daya instrumen tersebut.

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Domain Fisika / Operasional | ICP-OES | ICP-MS | GC-MS |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 0** (Surface / Data Output) | Pembacaan Analis & Software | Intensitas puncak spektrum optik ($I$) pada panjang gelombang $\lambda$ | *Counts per second* (CPS) partikel pada rasio $m/z$ tertentu | Kromatogram puncak waktu retensi ($t_R$) + spektrum fragmentasi massa |
| **Layer -1** (Instrument Mechanics) | Sumber Eksitasi & Pemilah | Obor plasma Ar (1 atm) $\to$ Polikromator optik (kisi Echelle) | Obor plasma Ar (1 atm) $\to$ Interface vakum $\to$ Filter Quadrupole | Injektor GC $\to$ Kolom kapiler $\to$ Ruang ionisasi vakum (EI 70 eV) |
| **Layer -2** (Atomic Physics & Physical Chemistry) | Mekanika Kuantum & Termodinamika | **Distribusi Boltzmann**: Eksitasi elektronik termal via tumbukan inelastis ($T_{exc} \sim 6.500\text{ K}$) | **Kesetimbangan Saha**: Ionisasi termal terbatas oleh potensial ionisasi Argon ($IP_{Ar} = 15.76\text{ eV}$) | **Tembakan Kinetik Elektron Keras**: Impak elektron $70\text{ eV}$ merobek ikatan kovalen molekuler di ruang hampa |

---

## 2. Eksitasi Boltzmann dalam ICP-OES

Eksitasi dalam plasma ICP-OES dikendalikan oleh **Distribusi Boltzmann**, dengan asumsi kesetimbangan termodinamika lokal parsial (*p-LTE*):

$$N_j = N \cdot \frac{g_j}{Z(T)} \exp\left( - \frac{E_j}{k_B T_{exc}} \right)$$

Intensitas emisi radiasi spontan yang tertangkap detektor optik ($I_{ji}$):
$$I_{ji} = \left( \frac{h \cdot c \cdot l}{\lambda_{ji}} \right) A_{ji} \cdot N \frac{g_j}{Z(T)} \exp\left( - \frac{E_j}{k_B T_{exc}} \right)$$

### Mengapa Logam Lebih Sensitif Dibanding Non-Logam di ICP-OES?
* **Atom Logam (Na, Ca, Mg, Fe):** Memiliki elektron valensi longgar dengan energi eksitasi rendah ($E_j \sim 2 - 4\text{ eV}$). Pada suhu plasma $k_B T \approx 0.56\text{ eV}$, faktor Boltzmann $\exp(-E_j / k_B T)$ bernilai melimpah ($\sim 10^{-2}$ s.d. $10^{-3}$), menghasilkan pancaran emisi yang sangat benderang.
* **Atom Non-Logam (C, P, S, Cl, F):** Memiliki energi eksitasi tingkat pertama yang sangat tinggi ($E_j > 7 - 14\text{ eV}$). Faktor Boltzmann anjlok jutaan kali lipat ($\sim 10^{-8}$), sehingga intensitas emisinya sangat redup.

### Hambatan Wilayah *Vacuum Ultra-Violet* (VUV)
Berdasarkan hubungan energi-panjang gelombang:
$$\lambda = \frac{h \cdot c}{\Delta E}$$
Transisi berenergi tinggi pada non-logam memancarkan foton pada panjang gelombang sangat pendek ($< 190\text{ nm}$):
* Belerang ($S$): $180.731\text{ nm}$
* Fosfor ($P$): $177.495\text{ nm}$
* Karbon ($C$): $193.027\text{ nm}$

> [!WARNING]
> **Kendala Atmosfer:** Oksigen ($O_2$) dan uap air di udara menyerap radiasi UV di bawah $190\text{ nm}$ secara masif (*Schumann-Runge bands*).  
> **Solusi Hardware ICP-OES:** Kotak optik (polikromator) tidak boleh berisi udara biasa, melainkan harus dibilas terus-menerus (*purged*) dengan gas **Nitrogen ($N_2$) atau Argon ($Ar$)** ultra-murni ($99.999\%$), atau dipompa dalam kondisi vakum rendah (*rough vacuum* $\sim 10^{-2}\text{ mbar}$).

---

## 3. Disparitas Energi Ionisasi: ICP-MS vs GC-MS

Mengapa ICP-MS praktis "buta" terhadap unsur C, H, N, O, F, Cl, sementara GC-MS sangat unggul mendeteksi senyawa dari unsur-unsur tersebut?

```
[ ICP-MS: Plasma Termal Argon ]                 [ GC-MS: Ruang Ionisasi EI ]
     Plafon Energi: 15.76 eV                          Energi Elektron: 70 eV
                │                                               │
                ▼                                               ▼
Hanya mampu mengionisasi unsur                  Sanggup merobek elektron dari ikatan
dengan IP < 15.8 eV (Efisiensi F ~0%)           kovalen molekul apa pun di alam semesta
```

### A. Di dalam ICP-MS (Dibatasi oleh Kesetimbangan Saha)
Tingkat ionisasi analit diatur oleh persamaan Saha:
$$\frac{N_+ \cdot N_e}{N_0} \propto T^{3/2} \exp\left( - \frac{\text{IP}}{k_B T} \right)$$
* Gas pembentuk plasma adalah **Argon** dengan potensial ionisasi $\text{IP} = 15.76\text{ eV}$.
* **Fluorin ($\text{IP} = 17.42\text{ eV}$):** Memiliki ambang ionisasi lebih tinggi dari gas Argon. Plasma Argon tidak sanggup mengionisasi F menjadi $F^+$. Karena ICP-MS hanya mendeteksi ion bermuatan positif, atom F netral terbuang sia-sia ke pompa vakum.
* **Klorin ($\text{IP} = 12.97\text{ eV}$):** Efisiensi ionisasi hanya $\sim 0.9\%$.
* **Bencana Derau Pelarut/Atmosfer:** Ion $^{1}\text{H}^+, ^{12}\text{C}^+, ^{14}\text{N}^+, ^{16}\text{O}^+$ melimpah ruah triliunan kali lipat dari pelarut air dan udara, menenggelamkan sinyal analit non-logam tingkat renik.

### B. Di dalam GC-MS (Ionisasi Tumbukan Elektron / EI 70 eV)
* **Pemisahan Temporal (Waktu):** Analit dipisahkan secara molekuler di dalam kolom kromatografi berdasarkan titik didih dan interaksi fasa diam. Pelarut dibuang terlebih dahulu via *solvent delay*.
* **Tembakan Kinetik $70\text{ eV}$:** Di ruang hampa tinggi, molekul kovalen non-logam ditembak langsung oleh berkas elektron berenergi **$70\text{ eV}$**.
* Karena energi ionisasi molekul organik rata-rata hanya butuh **$8 - 12\text{ eV}$**, tembakan $70\text{ eV}$ menjamin efisiensi ionisasi mendekati mutlak:
  $$M + e^-_{(70\text{ eV})} \longrightarrow M^{+\bullet} + 2e^-$$

---

## 4. Matriks Perbandingan Komparatif

| Parameter Kritis | ICP-OES | ICP-MS | GC-MS |
| :--- | :--- | :--- | :--- |
| **Entitas yang Dideteksi** | Foton emisi relaksasi elektron | Partikel ion bermuatan positif ($M^+$) | Ion molekuler ($M^{+\bullet}$) / fragmen |
| **Kebutuhan Ruang Hampa** | Tekanan atmosfer (optik *purged* $N_2/Ar$) | **Vakum Ultra-Tinggi** ($10^{-5} - 10^{-7}\text{ mbar}$) | **Vakum Tinggi** ($10^{-5} - 10^{-6}\text{ mbar}$) |
| **Tipe Informasi** | Elemental total | Elemental + Komposisi Rasio Isotop | Struktur molekuler & senyawa spesifik |
| **Limit of Detection (LOD)** | Sub-ppb s.d. ppm ($10^{-9}$) | Sub-ppt s.d. ppq ($10^{-12} - 10^{-15}$) | Sub-ppb s.d. ppm (senyawa volatil) |
| **Kelemahan Terbesar** | Interferensi tumpang-tindih spektral optik | Interferensi isobar & ion poliatomik | Terbatas pada molekul volatil / termostabil |

---

## 5. Tautan Konsep Terkait
- Lanjut ke penanganan interferensi poliatomik: [[icp-ms-interferensi-dan-qcell-ked]]
- Lanjut ke mekanika gerak ion di dalam medan listrik: [[mekanika-quadrupole-rf-dc]]
- Kembali ke indeks navigasi: [[prinsip-dasar-icp-ms]] | [[icp-ms-learning-roadmap]]
