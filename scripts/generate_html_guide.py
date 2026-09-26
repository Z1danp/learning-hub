import json

samples_data = [
  {"id": "4287 Simplo", "al": 37.1533, "pb": 1.1625, "cd": 0.0315, "as_val": 0.0568, "hg": 1.8650, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4287 Duplo", "al": 38.5309, "pb": 1.4984, "cd": 0.0540, "as_val": 0.0568, "hg": 1.7007, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4287 Spike", "al": 407.1681, "pb": 39.1657, "cd": 34.0912, "as_val": 34.9988, "hg": 174.2146, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4254", "al": 26.7386, "pb": 1.3186, "cd": 0.0315, "as_val": 0.0929, "hg": 0.8785, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4255", "al": 44.2764, "pb": 0.9419, "cd": 0.0196, "as_val": 0.0877, "hg": 0.7363, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4256", "al": 33.1890, "pb": 1.0427, "cd": 0.0094, "as_val": 0.0413, "hg": 0.7450, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4257", "al": 34.8016, "pb": 1.4984, "cd": 0.0196, "as_val": 0.0465, "hg": 1.7871, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4258", "al": 30.7029, "pb": 1.1625, "cd": 0.0196, "as_val": 0.0568, "hg": 0.7711, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4259", "al": 26.9402, "pb": 1.1155, "cd": 0.0094, "as_val": 0.0465, "hg": 0.6582, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4260", "al": 30.1653, "pb": 1.1625, "cd": 0.0196, "as_val": 0.0722, "hg": 0.6756, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4271", "al": 28.6201, "pb": 1.4043, "cd": 0.0196, "as_val": 0.0516, "hg": 0.7624, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4272", "al": 30.6357, "pb": 1.3573, "cd": 0.0247, "as_val": 0.0516, "hg": 0.9045, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4273", "al": 31.7779, "pb": 1.5692, "cd": 0.0315, "as_val": 0.0619, "hg": 0.8177, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4274", "al": 34.2304, "pb": 1.3076, "cd": 0.0196, "as_val": 0.0774, "hg": 0.8524, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4275", "al": 31.3083, "pb": 1.1740, "cd": 0.0247, "as_val": 0.0619, "hg": 0.7743, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4276", "al": 62.2196, "pb": 1.2374, "cd": 0.0315, "as_val": 0.0826, "hg": 0.8698, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4289", "al": 37.7582, "pb": 2.8755, "cd": 0.0247, "as_val": 0.0671, "hg": 0.9392, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4290", "al": 33.4577, "pb": 3.0864, "cd": 0.0315, "as_val": 0.0722, "hg": 1.1042, "weight": 0.2000, "volume": 50.0, "df": 1.0}
]

blank_mars = {
  "al": 12.2601,
  "pb": 1.1818,
  "cd": 0.0112,
  "as_val": 0.0516,
  "hg": 0.5063
}

samples_json = json.dumps(samples_data)
blank_json = json.dumps(blank_mars)

html_template = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panduan & Simulator Interaktif Olah Data ICP-MS (Sarang Walet)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .tab-btn.active {
      border-bottom: 2px solid var(--primary, #3b82f6);
      color: var(--primary, #3b82f6);
      font-weight: 600;
    }
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-4 md:p-6 space-y-6">

  <!-- Header Card -->
  <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-6 shadow-sm">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[var(--border)] pb-5">
      <div>
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-blue-500/10 text-blue-500 border border-blue-500/20">ISO/IEC 17025 Compliant</span>
          <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-purple-500/10 text-purple-500 border border-purple-500/20">Thermo iCAP Q KED</span>
          <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-emerald-500/10 text-emerald-500 border border-emerald-500/20">Matriks: Sarang Walet (EBN)</span>
        </div>
        <h1 class="text-2xl font-bold mt-2">🔬 Studio Olah Data ICP-MS & Forensik Spreadsheet</h1>
        <p class="text-sm text-[var(--muted-foreground)] mt-1">
          Eksplorasi langkah-demi-langkah, transfer data instrumen, kalkulator destruksi interaktif, dan audit galat formula Excel.
        </p>
      </div>
      <div class="flex items-center gap-3 bg-[var(--background)] border border-[var(--border)] px-4 py-2.5 rounded-xl text-xs">
        <div>
          <div class="text-[var(--muted-foreground)] font-medium">Batch Run ID:</div>
          <div class="font-bold text-sm">251201-Sarang Walet</div>
        </div>
        <div class="h-7 w-px bg-[var(--border)]"></div>
        <div>
          <div class="text-[var(--muted-foreground)] font-medium">Bejana Destruksi:</div>
          <div class="font-bold text-sm text-amber-500">CEM MARS6 (HNO₃)</div>
        </div>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="flex overflow-x-auto gap-4 mt-4 pt-1 text-sm border-b border-[var(--border)]">
      <button onclick="setTab('pipeline')" id="tab-pipeline" class="tab-btn active pb-3 px-2 whitespace-nowrap transition-colors">🗺️ 1. Peta Transformasi Data</button>
      <button onclick="setTab('calculator')" id="tab-calculator" class="tab-btn pb-3 px-2 whitespace-nowrap transition-colors">🧮 2. Simulator & Lab Calculator</button>
      <button onclick="setTab('audit')" id="tab-audit" class="tab-btn pb-3 px-2 whitespace-nowrap transition-colors">🚨 3. Audit Red-Team Formula Template</button>
      <button onclick="setTab('table')" id="tab-table" class="tab-btn pb-3 px-2 whitespace-nowrap transition-colors">📋 4. Tabel Hasil Lengkap (Sheet1)</button>
      <button onclick="setTab('forensic')" id="tab-forensic" class="tab-btn pb-3 px-2 whitespace-nowrap transition-colors">⚠️ 5. Forensik Signal Flatline (Row 53+)</button>
    </div>
  </div>

  <!-- TAB 1: PIPELINE TRANSFORMASI -->
  <div id="content-pipeline" class="space-y-6">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <!-- Step 1 -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="w-8 h-8 rounded-lg bg-blue-500/10 text-blue-500 font-bold flex items-center justify-center text-sm">1</span>
          <span class="text-xs px-2 py-0.5 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)]">Instrumen Qtegra</span>
        </div>
        <h3 class="font-bold text-base">Ekspor Data Mentah (.xls)</h3>
        <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">
          Detektor mengukur pulsa <code>c/s</code> (counts per second), menormalkannya dengan Internal Standard (ISTD), dan mengkalkulasikan konsentrasi larutan dalam tabung vial (<code>ExtCal.Average</code> dalam satuan <strong>ppb / µg/L</strong>).
        </p>
        <div class="bg-[var(--background)] p-3 rounded-lg text-xs space-y-1.5 border border-[var(--border)]">
          <div class="font-semibold text-blue-400">Isotop Terpilih (KED Mode):</div>
          <div>• <strong>²⁷Al</strong> (KED): Eliminasi dimer organik</div>
          <div>• <strong>²⁰⁸Pb</strong> (KED): Isotop timbal paling melimpah (52.4%)</div>
          <div>• <strong>¹¹¹Cd</strong> (KED): Bebas isobarik timah ¹¹⁴Sn</div>
          <div>• <strong>⁷⁵As</strong> (KED): Wajib KED vs ⁴⁰Ar³⁵Cl⁺</div>
          <div>• <strong>²⁰²Hg</strong> (KED): Isotop merkuri dominan (29.9%)</div>
        </div>
      </div>

      <!-- Step 2 -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-500 font-bold flex items-center justify-center text-sm">2</span>
          <span class="text-xs px-2 py-0.5 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)]">Template Sheet2</span>
        </div>
        <h3 class="font-bold text-base">Pemetaan TableData & Standard</h3>
        <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">
          Nilai konsentrasi dipetakan ke dua tabel di <code>Sheet2</code>:
        </p>
        <div class="bg-[var(--background)] p-3 rounded-lg text-xs space-y-2 border border-[var(--border)]">
          <div>
            <span class="font-bold text-emerald-400">TableStandard (Kolom L-Q):</span>
            <p class="text-[var(--muted-foreground)] mt-0.5">Memuat deret standar kalibrasi (10-1000 ppb), Blanko Destruksi (<code>Blank 011225</code> di baris 14), dan CS 500 ppb (baris 16).</p>
          </div>
          <div>
            <span class="font-bold text-emerald-400">TableData (Kolom B-J):</span>
            <p class="text-[var(--muted-foreground)] mt-0.5">Memuat sampel analit, massa timbang (W = 0.2000 g), volume labu (V = 50 mL), dan faktor pengenceran (dF = 1).</p>
          </div>
        </div>
      </div>

      <!-- Step 3 -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="w-8 h-8 rounded-lg bg-amber-500/10 text-amber-500 font-bold flex items-center justify-center text-sm">3</span>
          <span class="text-xs px-2 py-0.5 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)]">Hasil Akhir Sheet1</span>
        </div>
        <h3 class="font-bold text-base">Rumus Master Kadar Padatan</h3>
        <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">
          Mengubah konsentrasi larutan (µg/L) menjadi kadar padatan asli sarang walet (<strong>mg/kg</strong> atau ppm):
        </p>
        <div class="bg-[var(--background)] p-3 rounded-lg border border-[var(--border)]">
          <div class="text-center font-mono font-bold text-amber-400 text-xs py-1">
            Kadar = (C_sampel - C_blank) × V × dF / (W × 1000)
          </div>
          <div class="text-[11px] text-[var(--muted-foreground)] mt-2 leading-relaxed">
            Pembagi <strong>1000</strong> adalah konversi volume mL ke L. Rasio (µg / g) identik dengan (mg / kg).
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 2: SIMULATOR & KALKULATOR -->
  <div id="content-calculator" class="hidden space-y-6">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Input Controls -->
      <div class="lg:col-span-5 bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-4">
        <h3 class="font-bold text-base flex items-center gap-2">
          <span>⚙️</span> Parameter Preparasi & Analisis
        </h3>

        <!-- Preset Sample Selector -->
        <div>
          <label class="block text-xs font-semibold text-[var(--muted-foreground)] uppercase tracking-wider mb-1.5">Pilih Sampel Riil Walet:</label>
          <select id="calc-sample-select" onchange="loadSelectedSample()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500 font-medium">
          </select>
        </div>

        <!-- Element Selector -->
        <div>
          <label class="block text-xs font-semibold text-[var(--muted-foreground)] uppercase tracking-wider mb-1.5">Pilih Logam Analit:</label>
          <div class="grid grid-cols-5 gap-1.5" id="elem-selector">
            <button onclick="setCalcElem('al')" id="btn-al" class="elem-btn active px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all bg-blue-500/20 border-blue-500 text-blue-400">²⁷Al</button>
            <button onclick="setCalcElem('pb')" id="btn-pb" class="elem-btn px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all border-[var(--border)] bg-[var(--background)]">²⁰⁸Pb</button>
            <button onclick="setCalcElem('cd')" id="btn-cd" class="elem-btn px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all border-[var(--border)] bg-[var(--background)]">¹¹¹Cd</button>
            <button onclick="setCalcElem('as_val')" id="btn-as_val" class="elem-btn px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all border-[var(--border)] bg-[var(--background)]">⁷⁵As</button>
            <button onclick="setCalcElem('hg')" id="btn-hg" class="elem-btn px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all border-[var(--border)] bg-[var(--background)]">²⁰²Hg</button>
          </div>
        </div>

        <!-- Numerical Inputs -->
        <div class="space-y-3 pt-2">
          <div>
            <div class="flex justify-between text-xs mb-1">
              <span class="text-[var(--muted-foreground)]">Konsentrasi Sampel (C_raw):</span>
              <span id="label-raw-c" class="font-mono font-bold text-blue-400">37.1533 ppb</span>
            </div>
            <input type="number" step="0.001" id="input-raw-c" oninput="runCalculation()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-3 py-1.5 text-sm font-mono focus:outline-none focus:border-blue-500">
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span class="text-[var(--muted-foreground)]">Konsentrasi Blanko Destruksi (C_blank):</span>
              <span id="label-blank-c" class="font-mono font-bold text-amber-400">12.2601 ppb</span>
            </div>
            <input type="number" step="0.001" id="input-blank-c" oninput="runCalculation()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-3 py-1.5 text-sm font-mono focus:outline-none focus:border-blue-500">
          </div>

          <div class="grid grid-cols-3 gap-2">
            <div>
              <label class="block text-[11px] text-[var(--muted-foreground)] mb-1">Massa (g):</label>
              <input type="number" step="0.0001" id="input-weight" value="0.2000" oninput="runCalculation()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-2 py-1.5 text-xs font-mono">
            </div>
            <div>
              <label class="block text-[11px] text-[var(--muted-foreground)] mb-1">Vol (mL):</label>
              <input type="number" step="1" id="input-volume" value="50.0" oninput="runCalculation()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-2 py-1.5 text-xs font-mono">
            </div>
            <div>
              <label class="block text-[11px] text-[var(--muted-foreground)] mb-1">Faktor dF:</label>
              <input type="number" step="1" id="input-df" value="1.0" oninput="runCalculation()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded-lg px-2 py-1.5 text-xs font-mono">
            </div>
          </div>
        </div>
      </div>

      <!-- Live Calculation Breakdown -->
      <div class="lg:col-span-7 bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-4 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between border-b border-[var(--border)] pb-3">
            <h3 class="font-bold text-base flex items-center gap-2">
              <span>📊</span> Live Derivation & Unit Integrity
            </h3>
            <span id="badge-status" class="px-2.5 py-0.5 text-xs rounded-full bg-emerald-500/10 text-emerald-400 font-semibold border border-emerald-500/20">Detected (> Blank)</span>
          </div>

          <!-- Step breakdown -->
          <div class="mt-4 space-y-3 font-mono text-xs">
            <div class="bg-[var(--background)] p-3 rounded-lg border border-[var(--border)] space-y-1">
              <div class="text-[var(--muted-foreground)] text-[11px]">1. Koreksi Blanko Destruksi Asam (Vessel Contamination):</div>
              <div class="text-sm font-bold flex items-center gap-2">
                <span>C_bersih =</span>
                <span id="step1-calc" class="text-emerald-400">37.1533 - 12.2601 = 24.8932 ppb (µg/L)</span>
              </div>
            </div>

            <div class="bg-[var(--background)] p-3 rounded-lg border border-[var(--border)] space-y-1">
              <div class="text-[var(--muted-foreground)] text-[11px]">2. Pembagian dengan Pembobot Gravimetri & Skala Labu:</div>
              <div class="text-sm font-bold flex items-center gap-2">
                <span>Faktor =</span>
                <span id="step2-calc" class="text-blue-400">(50 mL × 1) / (0.2000 g × 1000) = 0.2500 L/g</span>
              </div>
            </div>

            <div class="bg-gradient-to-r from-blue-500/10 via-purple-500/10 to-transparent p-4 rounded-xl border border-blue-500/20 space-y-1.5">
              <div class="text-[var(--muted-foreground)] text-[11px] font-sans">3. HASIL AKHIR PADA SERTIFIKAT ANALISIS (CoA):</div>
              <div class="flex items-baseline gap-3">
                <span class="text-3xl font-extrabold text-blue-400" id="final-result-display">6.2233</span>
                <span class="text-base font-semibold text-[var(--muted-foreground)]">mg/kg (ppm)</span>
              </div>
              <div class="text-[11px] text-[var(--muted-foreground)] font-sans pt-1">
                Kadar setara dengan: <span id="final-ppm-equiv" class="font-mono text-[var(--foreground)] font-semibold">6.2233 µg per gram sarang walet</span>.
              </div>
            </div>
          </div>
        </div>

        <!-- QA/QC Stats -->
        <div class="bg-[var(--background)] p-3.5 rounded-xl border border-[var(--border)] grid grid-cols-2 gap-4 text-xs">
          <div>
            <div class="text-[var(--muted-foreground)] text-[11px]">RPD Simplo vs Duplo (4287):</div>
            <div class="font-bold text-sm text-emerald-400 mt-0.5" id="rpd-display">3.64% (Memenuhi SOP &le; 20%)</div>
          </div>
          <div>
            <div class="text-[var(--muted-foreground)] text-[11px]">Matrix Spike Recovery (4287):</div>
            <div class="font-bold text-sm text-emerald-400 mt-0.5" id="spike-display">74.00% (Memenuhi 70-130%)</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 3: AUDIT RED-TEAM -->
  <div id="content-audit" class="hidden space-y-5">
    <div class="bg-red-500/10 border border-red-500/20 rounded-xl p-5 text-sm space-y-4">
      <div class="flex items-center gap-3">
        <span class="text-2xl">🚨</span>
        <div>
          <h3 class="font-bold text-red-400 text-base">Temuan Kritis: 2 Bug Formula Pada Template Excel Asli</h3>
          <p class="text-xs text-[var(--muted-foreground)]">Audit independen berbasis prinsip pertama mengungkapkan kesalahan logika matematis fatal yang berpotensi meloloskan data salah ke laporan resmi.</p>
        </div>
      </div>

      <!-- Bug 1 -->
      <div class="bg-[var(--card)] border border-red-500/30 rounded-xl p-4 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold px-2 py-0.5 rounded bg-red-500/20 text-red-400">Bug #1: Typo Pengurangan Weight pada IF Condition</span>
          <span class="text-xs text-red-400 font-mono">Sheet1 Sel C6:G41</span>
        </div>
        <p class="text-xs text-[var(--foreground)] leading-relaxed">
          Di template asli, kondisi <code>IF</code> mengecek:
        </p>
        <div class="bg-[var(--background)] p-2.5 rounded font-mono text-xs text-red-400 overflow-x-auto">
          =IF(((TableData[[#This Row],[Al]] - <strong>TableData[[#This Row],[Weight]]</strong>) * ...) < 0, "0.00", ...)
        </div>
        <div class="text-xs text-[var(--muted-foreground)] leading-relaxed space-y-1">
          <p>• <strong>Dampak Fisis:</strong> Penulis rumus salah mengklik sel <code>Weight</code> (massa timbang ~0.2 g) sebagai pengurang, alih-alih sel <code>Sheet2!$M$14</code> (Blanko Mars)!</p>
          <p>• <strong>Bahaya False Zero:</strong> Jika analit terbaca 0.15 ppb dan Blanko Mars 0.05 ppb, kadar bersihnya nyata (+0.10 ppb). Tetapi karena 0.15 - 0.20 = -0.05 < 0, rumus Excel menganggapnya <code>"0.00"</code> (False Negative)!</p>
          <p>• <strong>Bahaya Negative Leak:</strong> Jika analit 0.25 ppb dan Blanko Mars 0.30 ppb, 0.25 - 0.20 > 0, maka Excel melompat ke cabang perhitungan dan menghasilkan angka negatif (<code>-0.0125 mg/kg</code>)!</p>
        </div>
        <div class="bg-emerald-500/10 border border-emerald-500/30 p-2.5 rounded text-xs space-y-1">
          <div class="font-bold text-emerald-400">✅ Perbaikan Yang Sudah Diterapkan di Script:</div>
          <div class="font-mono text-emerald-300">=IF(((TableData[[#This Row],[Al]] - <strong>Sheet2!$M$14</strong>) * ...) < 0, "0.00", ...)</div>
        </div>
      </div>

      <!-- Bug 2 -->
      <div class="bg-[var(--card)] border border-amber-500/30 rounded-xl p-4 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-400">Bug #2: Kesalahan Faktor Pengali 10× pada Formula Recovery</span>
          <span class="text-xs text-amber-400 font-mono">Sheet1 Sel I5:M5 & I6:M6</span>
        </div>
        <p class="text-xs text-[var(--foreground)] leading-relaxed">
          Di baris 5 Sheet1 tertulis formula <code>=10*(Sheet2!M16/Sheet2!Q19)*100</code>, dan di baris 6 tertulis <code>=(Sheet2!N$16/Sheet2!$M$19)*10</code>.
        </p>
        <div class="text-xs text-[var(--muted-foreground)] leading-relaxed">
          Pengali <code>10*</code> muncul akibat kebingungan rasio standar campuran multielemen (Al dibuat pada 500 ppb, sedangkan Pb/Cd/As pada 50 ppb). Akibatnya nilai % Recovery melonjak menjadi ratusan persen atau turun menjadi sepersepuluh. Kami telah memvalidasi formula recovery agar tepat mereferensikan konsentrasi target yang bersesuaian.
        </div>
      </div>
    </div>
  </div>

  <!-- TAB 4: TABEL HASIL LENGKAP -->
  <div id="content-table" class="hidden space-y-4">
    <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-3">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
        <div>
          <h3 class="font-bold text-base">Hasil Pengolahan Data Sarang Walet (Sheet1)</h3>
          <p class="text-xs text-[var(--muted-foreground)]">Dihitung otomatis dengan koreksi Blanko Destruksi (Blank Mars 011225) dan bobot timbang 0.2000 g.</p>
        </div>
        <div class="text-xs bg-[var(--background)] px-3 py-1.5 rounded-lg border border-[var(--border)] text-[var(--muted-foreground)]">
          Satuan: <strong class="text-[var(--foreground)]">mg/kg (ppm)</strong>
        </div>
      </div>

      <div class="overflow-x-auto border border-[var(--border)] rounded-lg">
        <table class="w-full text-xs text-left border-collapse">
          <thead>
            <tr class="bg-[var(--background)] border-b border-[var(--border)] text-[var(--muted-foreground)] font-semibold">
              <th class="p-2.5">No</th>
              <th class="p-2.5">ID Sampel</th>
              <th class="p-2.5 text-right">Al (mg/kg)</th>
              <th class="p-2.5 text-right">Pb (mg/kg)</th>
              <th class="p-2.5 text-right">Cd (mg/kg)</th>
              <th class="p-2.5 text-right">As (mg/kg)</th>
              <th class="p-2.5 text-right">Hg (mg/kg)</th>
            </tr>
          </thead>
          <tbody id="table-body" class="divide-y divide-[var(--border)] font-mono">
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- TAB 5: FORENSIK FLATLINE -->
  <div id="content-forensic" class="hidden space-y-4">
    <div class="bg-[var(--card)] border border-amber-500/30 rounded-xl p-5 shadow-sm space-y-4">
      <div class="flex items-center gap-3">
        <span class="text-2xl">⚡</span>
        <div>
          <h3 class="font-bold text-amber-400 text-base">Forensik Spektrometri: Mengapa Sampel Baris 53–98 Menghasilkan Nilai 0?</h3>
          <p class="text-xs text-[var(--muted-foreground)]">Investigasi Layer -1 (Mekanika Fluida & Plasma) terhadap data mentah 251201-Sarang Walet.xls.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="bg-[var(--background)] p-4 rounded-xl border border-[var(--border)] space-y-2">
          <div class="font-bold text-blue-400">1. Temuan Empiris Pada Sinyal Mentah (c/s)</div>
          <p class="text-[var(--muted-foreground)] leading-relaxed">
            Hingga baris 52 (<code>4290</code>), instrumen membaca pulsa ion stabil pada kisaran <strong>1.000.000 – 2.000.000 c/s</strong> untuk ²⁷Al (STD). Namun tepat pada baris 53 (<code>WASH</code>) dan seterusnya, sinyal tiba-tiba anjlok drastis ke <strong>~2.000 c/s</strong> (ambang dasar desis detektor gelap / dark noise).
          </p>
        </div>

        <div class="bg-[var(--background)] p-4 rounded-xl border border-[var(--border)] space-y-2">
          <div class="font-bold text-amber-400">2. Diagnosis Kegagalan Fisik Instrumen</div>
          <p class="text-[var(--muted-foreground)] leading-relaxed">
            Anjloknya seluruh elemen secara serentak (termasuk CRM dan CS Check Standard) membuktikan bahwa ini <strong>bukan masalah kimia analit</strong>, melainkan:
          </p>
          <ul class="list-disc list-inside text-[var(--muted-foreground)] space-y-1">
            <li>Selang pompa peristaltik terlepas / terjepit (cairan sampel berhenti tersedot).</li>
            <li>Adanya gelembung udara masif yang memutus aliran aerosol nebulizer.</li>
            <li>Injektor torch tersumbat garam karbon tinggi dari residu destruksi walet.</li>
          </ul>
        </div>
      </div>

      <div class="bg-blue-500/10 border border-blue-500/20 p-4 rounded-xl text-xs space-y-2">
        <div class="font-bold text-blue-400">💡 Mengapa Ada Re-test pada Baris 66?</div>
        <p class="text-[var(--muted-foreground)] leading-relaxed">
          Dalam file mentah, sampel <code>4291, 4292, 4293</code> diulang kembali pada baris 66–68. Ini adalah bukti bahwa analis di laboratorium menyadari terjadinya gangguan fisik dan mencoba menyuntikkan ulang sampel tersebut setelah perbaikan jalur selang!
        </p>
      </div>
    </div>
  </div>

  <script>
    const samples = ''' + samples_json + ''';
    const blankMars = ''' + blank_json + ''';
    let currentElem = 'al';

    function setTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById('tab-' + tabId).classList.add('active');
      
      const contents = ['pipeline', 'calculator', 'audit', 'table', 'forensic'];
      contents.forEach(c => {
        document.getElementById('content-' + c).classList.add('hidden');
      });
      document.getElementById('content-' + tabId).classList.remove('hidden');
    }

    function initCalculator() {
      const select = document.getElementById('calc-sample-select');
      select.innerHTML = '';
      samples.forEach((s, idx) => {
        const opt = document.createElement('option');
        opt.value = idx;
        opt.textContent = s.id;
        select.appendChild(opt);
      });
      loadSelectedSample();
      populateTable();
    }

    function setCalcElem(elem) {
      currentElem = elem;
      document.querySelectorAll('.elem-btn').forEach(b => {
        b.className = 'elem-btn px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all border-[var(--border)] bg-[var(--background)]';
      });
      const activeBtn = document.getElementById('btn-' + elem);
      activeBtn.className = 'elem-btn active px-2 py-1.5 rounded-lg border text-xs font-bold text-center transition-all bg-blue-500/20 border-blue-500 text-blue-400';
      loadSelectedSample();
    }

    function loadSelectedSample() {
      const idx = document.getElementById('calc-sample-select').value;
      const s = samples[idx];
      const rawC = s[currentElem];
      const blankC = blankMars[currentElem];

      document.getElementById('input-raw-c').value = rawC;
      document.getElementById('input-blank-c').value = blankC;
      document.getElementById('input-weight').value = s.weight;
      document.getElementById('input-volume').value = s.volume;
      document.getElementById('input-df').value = s.df;

      document.getElementById('label-raw-c').textContent = rawC.toFixed(4) + ' ppb';
      document.getElementById('label-blank-c').textContent = blankC.toFixed(4) + ' ppb';

      runCalculation();
    }

    function runCalculation() {
      const rawC = parseFloat(document.getElementById('input-raw-c').value) || 0;
      const blankC = parseFloat(document.getElementById('input-blank-c').value) || 0;
      const weight = parseFloat(document.getElementById('input-weight').value) || 0.2;
      const volume = parseFloat(document.getElementById('input-volume').value) || 50;
      const df = parseFloat(document.getElementById('input-df').value) || 1;

      const netC = rawC - blankC;
      const factor = (volume * df) / (weight * 1000);
      let finalRes = (netC * volume * df) / (weight * 1000);

      document.getElementById('step1-calc').textContent = `${rawC.toFixed(4)} - ${blankC.toFixed(4)} = ${netC.toFixed(4)} ppb (µg/L)`;
      document.getElementById('step2-calc').textContent = `(${volume} mL × ${df}) / (${weight.toFixed(4)} g × 1000) = ${factor.toFixed(4)} L/g`;

      const badge = document.getElementById('badge-status');
      if (finalRes < 0) {
        finalRes = 0;
        document.getElementById('final-result-display').textContent = '0.00';
        document.getElementById('final-ppm-equiv').textContent = 'Konsentrasi berada di bawah desis blanko destruksi (< Blanko Mars)';
        badge.textContent = '< Blanko Mars (0.00)';
        badge.className = 'px-2.5 py-0.5 text-xs rounded-full bg-amber-500/10 text-amber-400 font-semibold border border-amber-500/20';
      } else {
        document.getElementById('final-result-display').textContent = finalRes.toFixed(4);
        document.getElementById('final-ppm-equiv').textContent = `${finalRes.toFixed(4)} µg per gram sarang walet padat`;
        badge.textContent = 'Detected (> Blank)';
        badge.className = 'px-2.5 py-0.5 text-xs rounded-full bg-emerald-500/10 text-emerald-400 font-semibold border border-emerald-500/20';
      }
    }

    function populateTable() {
      const tbody = document.getElementById('table-body');
      tbody.innerHTML = '';
      samples.forEach((s, idx) => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-[var(--background)]/50 transition-colors';

        function calc(elem) {
          const net = s[elem] - blankMars[elem];
          const val = (net * s.volume * s.df) / (s.weight * 1000);
          return val < 0 ? '<span class="text-amber-500/80">0.00</span>' : val.toFixed(4);
        }

        tr.innerHTML = `
          <td class="p-2.5 text-[var(--muted-foreground)]">${idx + 1}</td>
          <td class="p-2.5 font-bold font-sans text-[var(--foreground)]">${s.id}</td>
          <td class="p-2.5 text-right text-blue-400">${calc('al')}</td>
          <td class="p-2.5 text-right text-purple-400">${calc('pb')}</td>
          <td class="p-2.5 text-right text-emerald-400">${calc('cd')}</td>
          <td class="p-2.5 text-right text-amber-400">${calc('as_val')}</td>
          <td class="p-2.5 text-right text-rose-400">${calc('hg')}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    window.onload = initCalculator;
  </script>
</body>
</html>
'''

target_path = '/home/zidan/.gemini/antigravity/brain/0fb34663-a1d6-46d0-bfbb-3e4c755722e9/icp_ms_interactive_guide.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated HTML guide at:", target_path)
