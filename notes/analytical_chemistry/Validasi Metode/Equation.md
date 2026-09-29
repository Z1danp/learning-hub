# ⚗️ Validasi Metode: Persamaan Matematis, LOD/LOQ, & Evaluasi Data ICP-OES

- **Domain**: [[analytical-chemistry]] | [[validasi-metode]]
- **Instrumen**: [[perbandingan-spektrometri-emisi-dan-massa|ICP-OES]] (Inductively Coupled Plasma Optical Emission Spectrometry) [[icp-ms-core]]
- **Standar Rujukan**: ISO/IEC 17025, EURACHEM / CITAC Guide CG4, ICH Q2(R2)
- **Project Terkait**: `projects/valid-ex`

---

## 1. Fondasi Stokastik: Subjek Uji LOD & LOQ adalah "Blanko"

Dalam validasi metode spektrometri, penentuan batas deteksi pada hakikatnya adalah sebuah **Uji Hipotesis Nol (*Null Hypothesis / $H_0$*)**:
- **$H_0$**: *"Tabung sampel tidak mengandung analit logam (hanya derau/noise pelarut blanko)."*
- **Sinyal Blanko**: Fluktuasi desis plasma dan detektor optik berpusat pada rata-rata $\mu_0$ dengan simpangan baku $\sigma$, membentuk **Distribusi Normal Gaussian $\mathcal{N}(\mu_0, \sigma^2)$**.

```text
               Frekuensi Muncul
                      ▲
                      │          ┌───┐   <- Rata-rata Blanko (μ₀)
                      │        ┌─┘   └─┐
                      │       ┌┘       └┐
                      │     ┌─┘         └─┐
                      │   ┌─┘             └─┐
                      │ ┌─┘                 └─┐
                      └─┴─────────────────────┴──────► Nilai Sinyal (c/s)
                       -3σ        μ₀        +3σ (LOD)      +10σ (LOQ)
```

---

## 2. Limit of Detection (LOD): Batas Kualitatif ($3\sigma$)

### A. Mengapa Konstantanya 3? (Kaiser, 1947)
Berdasarkan sifat kurva lonceng Gaussian (uji satu arah / *one-tailed*):
- Peluang derau acak blanko melonjak melampaui $\mu_0 + 1\sigma$: **15.9%** (terlalu sering).
- Peluang derau acak blanko melonjak melampaui $\mu_0 + 2\sigma$: **2.28%**.
- Peluang derau acak blanko melonjak melampaui $\mu_0 + 3\sigma$: **0.13%** (Tingkat kepercayaan $99.87\%$).

> **Makna Fisis**: Jika sinyal sampel $\ge 3\sigma$, probabilitas bahwa sinyal itu hanyalah "kebetulan noise blanko" kurang dari $0.13\%$. Kita menolak $H_0$ dan menyimpulkan secara kualitatif: **Logam terbukti ADA (Detected).**

### B. Mengapa Belum Boleh Kuantitatif pada LOD?
Pada titik $3\sigma$, proporsi simpangan baku ($\sigma$) terhadap tinggi sinyal bersih ($3\sigma$) adalah:
$$\%RSD = \frac{\sigma}{3\sigma} \times 100\% = \frac{1}{3} \times 100\% \approx \mathbf{33.3\%}$$
Galat ketidakpastian sebesar $\pm 33.3\%$ terlalu besar dan tidak dapat diterima untuk pelaporan hasil uji kuantitatif resmi.

---

## 3. Limit of Quantitation (LOQ): Batas Kuantitatif ($10\sigma$)

### A. Mengapa Konstantanya 10? (Currie, 1968)
LOQ mendefinisikan batas konsentrasi terendah di mana analit tidak hanya terdeteksi, tetapi **dapat diukur dengan presisi yang dapat diterima secara analitik**.

Standar analitik menuntut batas keraguan relatif (%RSD) maksimal sebesar **10%**:
$$\%RSD = \frac{\sigma}{k \cdot \sigma} \times 100\% \le 10\% \implies \frac{1}{k} \le 0.1 \implies \mathbf{k \ge 10}$$

> **Makna Fisis**: Pada titik $10\sigma$, sinyal logam sudah 10 kali lebih kuat dari derau baseline. Rasio derau terhadap sinyal ditekan hingga $\le 10\%$, sehingga nilainya sah dilaporkan secara kuantitatif.

### B. Tiga Zona Pelaporan Laboratorium (SOP ISO 17025)

| Rentang Sinyal | Status Deteksi | Format Pelaporan Resmi di Sertifikat (CoA) |
| :--- | :--- | :--- |
| $< \text{LOD}$ | Tidak terbedakan dari derau blanko. | **"Not Detected (ND)"** / Tidak Terdeteksi |
| $\text{LOD} \le x < \text{LOQ}$ | Analit terbukti ada, presisi galat $> 10\%$. | **"$< \text{LOQ}$"** atau *"Trace"* (Dilarang lapor angka) |
| $\ge \text{LOQ}$ | Analit ada dan presisi galat terbukti $\le 10\%$. | **Angka Numerik Sah Dilaporkan** (misal: $0.25\ \text{mg/kg}$) |

---

## 4. Standar Deviasi Residual ($s_{y/x}$) & Derajat Kebebasan ($N - 2$)

### A. Mengapa Memakai Standar Deviasi Residual?
Dalam pengujian rutin, analis tidak mengukur 10 tabung blanko terpisah untuk mencari $s_{\text{blank}}$ (keterbatasan waktu dan gas argon). Sebagai gantinya, analis menggunakan seluruh titik pada **kurva kalibrasi** (misal $N = 7$ titik standar).

Jarak vertikal antara titik terukur ($y_i$) dengan garis regresi teoretis ($\hat{y}_i$) disebut **residual** ($e_i = y_i - \hat{y}_i$), yang merepresentasikan fluktuasi acak seluruh sistem pengukuran.

### B. Mengapa Pembaginya Harus $(N - 2)$? (Derajat Kebebasan / $df$)
$$s_{y/x} = \sqrt{\frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{N - 2}}$$

1. **Kasus $N = 2$ Titik**:
   Sebuah garis lurus melewati 2 titik dengan sempurna tanpa meleset sedikit pun ($SS_{\text{res}} = 0$). Kedua titik tersebut habis dikorbankan untuk mengunci 2 parameter garis:
   - **Slope ($m$)**: Mengunci sudut kemiringan (rotasi).
   - **Intercept ($c$)**: Mengunci posisi ketinggian vertikal (translasi).
   Karena parameter garis mengonsumsi 2 titik, tersisa $df = 2 - 2 = 0$ derajat kebebasan untuk menguji galat.
2. **Kasus $N \ge 3$ Titik**:
   Titik ke-3 dan seterusnya adalah data independen yang bebas meleset dari garis untuk membuktikan adanya derau alat.
   Pada kurva 7 titik standar ($N = 7$):
   $$df = 7 - 2 = 5 \text{ derajat kebebasan independen}$$

---

## 5. Konversi Sinyal Detektor ke Satuan Konsentrasi Kimia

Nilai $3 \times s_{y/x}$ masih berada dalam satuan respon detektor (**counts per second / c/s**). Untuk mengubahnya menjadi konsentrasi yang dicari analis (**ppm / mg/L**), nilai tersebut dibagi dengan **Slope ($m$)**:

$$\text{LOD (mg/L)} = \frac{3 \times s_{y/x}}{m}$$

$$\text{LOQ (mg/L)} = \frac{10 \times s_{y/x}}{m}$$

*Dimensi satuan*:
$$\frac{\text{c/s}}{\left(\frac{\text{c/s}}{\text{mg/L}}\right)} = \text{mg/L (ppm)}$$

---

## 6. Formula Perhitungan Sampel Nyata di Laboratorium (ICP-OES)

Berdasarkan template pengolahan data riil lab:

### A. Koreksi Blanko Destruksi (*Digestion Blank Subtraction*)
Setiap batch destruksi memiliki 1 bejana (*vessel*) berisi pelarut asam ($HNO_3$) tanpa sampel untuk mengoreksi kontaminasi pereaksi:
$$C_{\text{bersih}} = C_{\text{sampel}} - C_{\text{blank}} \quad (\text{mg/L})$$

### B. Rumus Kadar Akhir Sampel ($mg/kg$)
$$\text{Hasil (mg/kg)} = \frac{(E_{\text{sampel}} - E_{\text{blank}}) \times V_{\text{labu}} \ (\text{mL}) \times dF}{W_{\text{timbang}} \ (\text{g})}$$

*Penjabaran Dimensi Satuan*:
$$\frac{\text{mg}}{\text{L}} \times \text{mL} \times \left(10^{-3}\ \frac{\text{L}}{\text{mL}}\right) \times \frac{1}{\text{g} \times \left(10^{-3}\ \frac{\text{kg}}{\text{g}}\right)} = \frac{\text{mg}}{\text{kg}}$$
*(Faktor pengali $10^{-3}$ di pembilang dan penyebut saling menghilangkan).*

> ⚠️ **Unit-Aware (Anti-Galat $1000\times$)**: rumus di atas valid bila $C$ dalam $\text{mg/L}$ (ppm). Bila $C$ dalam $\mu\text{g/L}$ (ppb), hasilnya menjadi $\frac{C \times V \times dF}{W \times 1000}$; untuk $\text{ppt}$ (ng/L) beda lagi. `@valid-ex/math` memakai tabel konversi dimensi eksplisit berbasis `solutionConcUnit`/`solidResultUnit`/`weightUnit`/`volumeUnit`, DILARANG meng-hardcode `/1000` ([[project-docs/valid-ex/INVARIANTS|Invariant D3]]).

*Logika Guardrail di Excel*:
```excel
=IF((E8-E$6)*C8*D8/(B8) < 0, "0.00", (E8-E$6)*C8*D8/(B8))
```
Jika hasil pengurangan blanko bernilai negatif (karena fluktuasi noise di bawah blanko), hasil otomatis di-nolkan (`"0.00"`).

---

## 7. Kriteria Kendali Mutu (QC Acceptance Criteria)

| Parameter Uji Mutu | Rumus / Definisi | Standar Keberterimaan Lab |
| :--- | :--- | :--- |
| **Linearitas Kurva ($r$)** | Koefisien korelasi Pearson | $r \ge 0.995$ |
| **Recovery Cek Standar (ICV/CRM)** | $\text{Rec} = \frac{C_{\text{terukur}}}{C_{\text{sebenarnya}}} \times 100\%$ | $100 \pm 10\%$ ($90\% - 110\%$) |
| **Spike Recovery Sampel** | $\text{Rec} = \frac{C_{\text{spike}} - C_{\text{unspiked}}}{C_{\text{target spike}}} \times 100\%$ | $60\% - 115\%$ |
| **Presisi Duplo (RPD)** | $\text{RPD} = \frac{\|S_1 - S_2\|}{(S_1 + S_2)/2} \times 100\%$ | $\le 25\%$ |

> **Catatan ([[project-docs/valid-ex/adr/0007-governed-qc-criteria-profiles|ADR-0007]])**: angka di tabel ini adalah **isi profil kriteria QC lab (SOP "QC CRITERIA CHECK")**, bukan konstanta universal. `valid-ex` tidak meng-hardcode-nya; kriteria disimpan sebagai profil ber-versi yang bisa punya **band per tingkat konsentrasi** (lihat AOAC Appendix F Table A5).

---

## 8. Vektor Falsifikasi & Peluang Rekayasa Perangkat Lunak (`valid-ex`)

1. **Jebakan Hardcoding di Excel**: 
   Di template manual, nilai slope $m$ diketik manual ke sel (misal `17330`), dan pembagi $N-2$ di-hardcode `(7-2)`. `valid-ex` mengganti kelemahan ini dengan formula dinamis native (`=SLOPE()`, `=COUNT()-2`, `=STEYX()`).
2. **Heteroskedastisitas**:
   Regresi OLS mengasumsikan varians konstan di semua konsentrasi. Di ICP-OES rentang lebar, galat di konsentrasi rendah seringkali terdistorsi. `valid-ex` akan memvalidasi apakah pembobotan *Weighted Least Squares ($1/x$)* diperlukan.
