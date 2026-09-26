# Big Picture Valid-Ex
Pada project webdev kali ini, aku ingin membuat web app untuk mengolah data hasil instrumentasi yang bersifat secara kuantitatif spesifik di penggunaan kurva kalibrasi untuk menentukan konsentrasi suatu senyawa di berbagai instrumentasi dan rentang konsentrasi yang mengikuti standar ISO 17025. 

Web ini tuh ngolah datanya sangat universal instrumentasi yang mana ada 3 jenis data yaitu:
1. Titik kalibrasi (x: konsentrasi standar, y: satuan alatnya (cps/s atau mungkin luas area pada GCMS/HPLC))
2. Sampel (x: output dari hasil perhitungan dengan persamaan regresi kurva kalibrasi, y: hasil pembacaan dari instrumen yang satuannya sesuai dengan titik kalibrasi)
3. Quality Control: Blank, Spike, Duplo, Larutan Kontrol (biasanya larutan standar tengah-tengah akan dicek sekali setiap beberapa sampel selesai analis (contoh 1x/20 sampel))

## Fitur
### Generate Kurva Kalibrasi
Setiap analis memasukkan titik kalibrasi, web ini akan mengolah data deret standar tersebut dengan pendekatan OLS, agar hasilnya reproducible dengan regresi yang ada di Excel, dan output kurva kalibrasi ini juga bisa dipakai untuk menghitung konsentrasi sampel dan data QC serta membuat LoD dan LoQ

### Filtering Status & Aturan Pelaporan Metrologi
Setelah mendapatkan nilai konsentrasi larutan bersih dengan menggunakan persamaan $$C_{\text{net}} = C_{\text{sample}} - C_{\text{blank}}$$, sistem akan mengevaluasi status deteksi berdasarkan batas deteksi instrumen:
1. Jika $C_{\text{net}} < \text{LOD}$: Laporkan sebagai `"Not Detected"` / `"ND"`.
2. Jika $\text{LOD} \le C_{\text{net}} < \text{LOQ}$: Laporkan sebagai `"< LOQ"` (dengan nilai batas kuantifikasi metode: $\text{LOQ}_{\text{metode}} = \frac{\text{LOQ} \times V \times dF}{W \times 1000}$).
3. Jika $C_{\text{net}} \ge \text{LOQ}$: Laporkan angka numerik hasil perhitungan persamaan di atas (misal: `6.22 mg/kg`).
Terus juga ada QC Kriteria cek dimana:
- r kurva > 0.995
- Calibration standard recovery: 100 $\pm$ 10%
- Sample & QC spike recovery: 60-115 %
- RPD $\leq$ 25%

### Sample Quantifications
Jika sampel berada diatas LoD, konsentrasi pembacaan instrumen dikonversi menjadi dalam bentuk padatan mg/kg dengan persamaan sebagai berikut:
$$\text{Conc (mg/kg)} = \frac{(C_{\text{sample}} - C_{\text{blank}})_{\text{mg/L}} \times V_{(\text{mL})} \times 10^{-3} \times \text{DF}}{W_{(\text{g})} \times 10^{-3}}$$

untuk sampel dengan kondisi $\text{LOD} \le C_{\text{net}} < \text{LOQ}$ , diberi flag/label analit terdeteksi akan tetapi tidak bisa dikuantifikasi karena tidak bisa dipastikan secara statistik

### Spreadsheet-like parser
Fitur ini akan memisahkan bagian kurva kalibrasi, analisis sampel, dan QC, jadi pertamanya tuh, kita pilih logam yang ingin dianalisis, setelah itu masing-masing kita masukkan nilai x dan y sesuai dengan 3 jenis data diatas. Nah, jujur aku bingung untuk parser ini mendingan analis sendiri yang masukin manual tinggal copas dari excel mentah (jadi table di web ini pasteable untuk cell excel), atau kita parsing excel dari dengan cara kita membuat konvensi gitu, misalnya untuk larutan standar label umumnya apa (misal label umum 'baku mix'), terus juga label buat QC kaya blanko, spike, duplo. Jadinya nanti kita pake method find stringnya gitu, yang mana kan nanti bisa disimpan untuk informasi-informasi tersebut dan akan digunakan kembali untuk kalkulasinya

## Tech Stack
### Backend
- **Server**: Express
- **Kalkulasi**: Python
- **DB**: POSTGRES
- **ORM**: Drizzle

### Frontend
- **Vite React**

### Type Safety
- **Typescript**
- **Pydantic**

### Testing
- **Vitest**
- **Pytest**

### API
- **RESTFul**
- **OPEN API Format**