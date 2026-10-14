---
title: Mekanika Quadrupole Mass Filter (RF, DC, Inersia, dan Resonansi Parametrik)
domain: analytical_chemistry
technique: mass-spectrometry
tags:
  - analytical-chemistry
  - physics
  - first-principles
  - quadrupole
  - ion-mechanics
date: 2026-09-13
status: reviewed
related:
  - "[[prinsip-dasar-icp-ms]]"
  - "[[icp-ms-interferensi-dan-qcell-ked]]"
  - "[[perbandingan-spektrometri-emisi-dan-massa]]"
---

# Mekanika Quadrupole Mass Filter (RF, DC, Inersia, dan Resonansi Parametrik)

> **One-Sentence Core Phenomenon:**  
> Pemilahan massa pada quadrupole dicapai bukan melalui penyaringan fisik pori, melainkan melalui manipulasi kestabilan lintasan osilasi elektro-dinamik di mana inersia ion diadu melawan medan bolak-balik RF dan medan statis DC.

---

## 1. Submarine Deconstruction (3 Abstraction Layers)

| Layer | Komponen / Fase | Fenomena Fisika yang Terjadi | Parameter Kritis |
| :--- | :--- | :--- | :--- |
| **Layer 0** (Data Output) | Spektogram Massa | Puncak hitungan ion per detik (*Counts Per Second* / CPS) pada resolusi satuan ($m/z \pm 0.35\text{ Da}$) | *Peak hopping*, *dwell time* ($\sim 10 - 50\text{ ms}$) |
| **Layer -1** (Instrument Mechanics) | Batang Quadrupole (4 Rods) | Batang paralel dialiri tegangan superposisi $[+ (U + V \cos \omega t)]$ dan $[- (U + V \cos \omega t)]$ | Frekuensi radio ($\omega \sim 1 - 3\text{ MHz}$), rasio $U/V \approx 0.168$, vakum $10^{-6}\text{ mbar}$ |
| **Layer -2** (Electrodynamics & Quantum Physics) | Persamaan Mathieu & Lautan Fermi | Persamaan diferensial gerak $\frac{d^2 u}{d\xi^2} + (a_u - 2q_u \cos 2\xi)u = 0$, resonansi parametrik, transfer muatan femtodetik | Parameter kestabilan $(a, q)$, kelembaman inersia ($m$), densitas elektron konduksi logam ($10^{23}\text{ e}^-/\text{cm}^3$) |

---

## 2. Lingkungan Vakum Tinggi vs Kedahsyatan Gaya Listrik

Di dalam ruang quadrupole ($10^{-6}\text{ mbar}$):
1. **Tidak Ada Arus Angin:** Pompa vakum (*turbomolecular pump*) tidak menyedot seperti *vacuum cleaner* rumah tangga karena hampir tidak ada molekul udara bebas (*mean free path* mencapai bermeter-meter). Tidak ada gaya seret aerodinamis yang menghanyutkan ion.
2. **Keperkasaan Gaya Elektrostatik:** Selama partikel berwujud ion bermuatan ($M^+$), gaya Lorentz ($F = q \cdot E$) **jutaan kali lebih kuat** dari gravitasi atau fluktuasi mekanis. Ion 100% patuh pada ayunan medan listrik batang quadrupole.
3. **Reduksi Seketika di Lautan Elektron Batang (*Fermi Sea*):**
   * Batang logam (stainless steel/molibdenum) adalah lautan padat berisi $\sim 10^{23}$ elektron konduksi bebas.
   * Meskipun batang diberi tegangan positif $+100\text{ V}$, kekurangan elektron di permukaannya hanyalah $\sim 10^{10}$ elektron (ibarat mengambil seember air dari samudera).
   * Begitu ion positif menyentuh batang logam, elektron dari logam langsung melompat (*quantum tunneling*) dalam skala waktu **femtodetik ($10^{-15}\text{ s}$)**:
     $$M^+ + e^-_{(\text{logam})} \longrightarrow M^0\text{ (Atom Netral)}$$
   * Seketika muatannya menjadi nol, atom netral tidak lagi terpengaruh medan listrik, terpental lepas, dan disedot habis oleh turbopump.

---

## 3. Inersia dalam Belokan Gang Sempit

Inersia (Hukum Newton I) adalah **kemalasan suatu benda untuk mengubah arah dan keadaan geraknya**. Ukuran dari inersia adalah **Massa ($m$)**.

Dalam gerak belok, jari-jari kelengkungan lintasan dirumuskan sebagai:
$$R = \frac{m \cdot v^2}{F}$$

```
[ Ion Ringan: Pejalan Kaki ]        [ Ion Berat: Truk Tronton ]
       Inersia Sangat Kecil                 Inersia Raksasa
- Radius putar (R) sangat tajam     - Radius putar (R) sangat lebar ("makan jalan")
- Manuver belok seketika            - Sangat lamban merespons setir belokan
```

Di dalam lorong quadrupole yang sempit (lebar beberapa milimeter):
* **Ion Ringan (Pejalan Kaki):** Mampu berbelok patah seketika mengikuti tarikan listrik $\rightarrow$ sangat rentan terlempar menabrak pembatas lorong.
* **Ion Berat (Truk Tronton):** Membutuhkan ancang-ancang busur belokan yang terlalu panjang $\rightarrow$ tidak sanggup bergoyang mengikuti getaran setir yang berganti arah jutaan kali per detik.

---

## 4. Perkawinan Tegangan RF (Dinamis) dan DC (Statis)

Tegangan pada 4 batang quadrupole dipisahkan menjadi dua pasang sumbu yang tegak lurus ($90^\circ$):

```
                  [ Batang Atas: DC Positif (+) + RF ]
                             ▲
                             │ 
                             │  ◄── Sumbu Y: Osilasi Resonansi Parametrik
                             │
     [ Batang Kiri: DC (-) ] ┼ [ Batang Kanan: DC (-) ]
           ▲                               ▲
           └───────────────┬───────────────┘
                           │
                 Sumbu X: Tarikan DC Statis
                             │
                             ▼
                  [ Batang Bawah: DC Positif (+) + RF ]
```

> [!NOTE]
> **Dominasi Tegangan RF:**  
> Amplitudo ayunan RF ($V \sim 600\text{ V}$) jauh melampaui tegangan statis DC ($U \sim 100\text{ V}$).  
> Batang "DC Positif" secara dinamis mengayun dari $+700\text{ V}$ hingga **$-500\text{ V}$**!

---

### Skenario 1: Mengapa Ion Berat Menabrak Batang DC Negatif?
* Ion berat (inersia raksasa) **terlalu lambat untuk merespons ayunan RF** jutaan Hertz. Ayunan bolak-balik RF efeknya saling meniadakan menjadi nol.
* **Tetapi**, ion berat tidak bisa lepas dari tarikan konstan medan **DC Negatif (-)** pada sumbu horisontal (batang kiri-kanan).
* Tanpa ada pantulan RF yang menyelamatkannya ke tengah, ion berat perlahan melayang condong ke samping dan **menabrak salah satu Batang DC Negatif**.
* *(Sumbu DC Negatif bertindak sebagai **High-Mass Filter**)*.

---

### Skenario 2: Mengapa Ion Ringan Menabrak Batang DC Positif? (Fenomena "Pompa Ayunan")

Ini adalah jawaban atas paradoks: *Jika batang atas-bawah sama-sama DC Positif, mengapa tidak saling meniadakan di tengah?*

1. **Mangkuk Potensial & Kecepatan Maksimum:**
   * Kedua batang DC(+) memang menolak ion positif ke arah tengah lorong ($y=0$).
   * Di titik tengah, gaya dorong memang nol ($F=0$), **tetapi kecepatannya MAKSIMAL ($v_{max}$)**!
   * Akibat inersia, ion tidak bisa berhenti mendadak di tengah. Ia meluncur menembus titik tengah menuju batang seberangnya (*overshoot*).
2. **Resonansi Parametrik (Pompa Ayunan):**
   * Denyutan ayunan RF bertindak seperti orang dewasa yang terus mendorong ayunan anak-anak di waktu yang tepat.
   * Karena ion sangat ringan, setiap kali ia memantul melintasi titik tengah, denyutan RF menyuntikkan energi kinetik tambahan yang gagal diredam.
   * Amplitudo lompatannya meledak secara eksponensial:
     $$\text{Pantulan 1 (sempit)} \longrightarrow \text{Pantulan 2 (lebar)} \longrightarrow \text{JEBRED! Menabrak Batang DC Positif!}$$
   * Gerakan melenting ini terjadi di sumbu vertikal, sehingga ion ringan **PASTI menabrak salah satu dari Batang DC Positif (Atas atau Bawah)**.
* *(Sumbu DC Positif bertindak sebagai **Low-Mass Filter**)*.

---

### Skenario 3: Ion dengan Massa yang PAS (*Stable Passband*)
* Pada massa analit target, inersianya berada di titik keseimbangan sempurna (*sweet spot* kestabilan Mathieu).
* Di sumbu DC(-): Inersianya cukup lincah untuk dipantulkan balik oleh RF sehingga tidak tersedot ke batang negatif.
* Di sumbu DC(+): Inersianya cukup berat untuk meredam resonansi sehingga goyangan atas-bawahnya tidak meledak.
* **Hasilnya:** Ion meliuk-liuk secara harmonis tepat di tengah lorong dan menembus keluar menuju detektor!

---

## 5. Ringkasan Matriks Nasib Partikel di Quadrupole

| Kategori Partikel | Inersia Massa | Sumbu Kegagalan | Batang yang Ditabrak | Penyebab Utama Kematian Lintasan |
| :--- | :--- | :--- | :--- | :--- |
| **Ion Jauh Lebih Ringan** ($m \ll m_{target}$) | Nyaris Nol | Acak (X & Y) | Batang mana pun | Guncangan liar RF langsung melempar ion dalam 1 siklus |
| **Ion Sedikit Lebih Ringan** ($m < m_{target}$) | Rendah | Vertikal (Y) | **Batang DC Positif (+)** | Resonansi parametrik: *overshoot* melintasi titik tengah yang meledak |
| **Ion Target Pas** ($m = m_{target}$) | **Harmonis** | **Tidak Ada** | **Lolos Bebas (Detektor)** | Amplitudo osilasi stabil dan terkungkung di lorong tengah |
| **Ion Sedikit/Jauh Lebih Berat** ($m > m_{target}$) | Raksasa | Horisontal (X) | **Batang DC Negatif (-)** | Inersia lamban tak mampu berosilasi $\to$ tersedot tarikan DC statis |

---

## 6. Tautan Konsep Terkait
- Solusi sel kolisi sebelum quadrupole: [[icp-ms-interferensi-dan-qcell-ked]]
- Dasar eksitasi plasma & optik: [[perbandingan-spektrometri-emisi-dan-massa]]
- Navigasi SOP dan Roadmap: [[prinsip-dasar-icp-ms]] | [[icp-ms-learning-roadmap]]
