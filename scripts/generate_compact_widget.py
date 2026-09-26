import json

samples_data = [
  {"id": "4287 Simplo", "al": 37.1533, "pb": 1.1625, "cd": 0.0315, "as_val": 0.0568, "hg": 1.8650, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4287 Duplo", "al": 38.5309, "pb": 1.4984, "cd": 0.0540, "as_val": 0.0568, "hg": 1.7007, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4287 Spike", "al": 407.1681, "pb": 39.1657, "cd": 34.0912, "as_val": 34.9988, "hg": 174.2146, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4254", "al": 26.7386, "pb": 1.3186, "cd": 0.0315, "as_val": 0.0929, "hg": 0.8785, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4255", "al": 44.2764, "pb": 0.9419, "cd": 0.0196, "as_val": 0.0877, "hg": 0.7363, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4256", "al": 33.1890, "pb": 1.0427, "cd": 0.0094, "as_val": 0.0413, "hg": 0.7450, "weight": 0.2000, "volume": 50.0, "df": 1.0},
  {"id": "4257", "al": 34.8016, "pb": 1.4984, "cd": 0.0196, "as_val": 0.0465, "hg": 1.7871, "weight": 0.2000, "volume": 50.0, "df": 1.0},
]

blank_mars = {
  "al": 12.2601,
  "pb": 1.1818,
  "cd": 0.0112,
  "as_val": 0.0516,
  "hg": 0.5063
}

compact_html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-3">
  <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-xl p-4 shadow-sm space-y-3">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-[var(--border)] pb-2.5">
      <div>
        <div class="flex items-center gap-1.5">
          <span class="text-sm">🧪</span>
          <span class="font-bold text-xs">Simulator Cepat Olah Data ICP-MS</span>
          <span class="text-[10px] px-1.5 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20 font-mono">Walet 251201</span>
        </div>
      </div>
      <div id="quick-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
        Status: Valid (> Blank)
      </div>
    </div>

    <!-- Controls Row -->
    <div class="grid grid-cols-2 gap-2 text-xs">
      <div>
        <label class="block text-[10px] text-[var(--muted-foreground)] font-semibold mb-1">Pilih Sampel:</label>
        <select id="quick-sample" onchange="updateCalc()" class="w-full bg-[var(--background)] border border-[var(--border)] rounded px-2 py-1 text-xs">
          {''.join(f'<option value="{i}">{s["id"]}</option>' for i, s in enumerate(samples_data))}
        </select>
      </div>
      <div>
        <label class="block text-[10px] text-[var(--muted-foreground)] font-semibold mb-1">Pilih Unsur:</label>
        <div class="grid grid-cols-5 gap-1">
          <button onclick="setElem('al')" id="qbtn-al" class="qbtn active py-0.5 rounded border border-blue-500 bg-blue-500/20 text-blue-400 font-bold text-[10px]">Al</button>
          <button onclick="setElem('pb')" id="qbtn-pb" class="qbtn py-0.5 rounded border border-[var(--border)] bg-[var(--background)] font-bold text-[10px]">Pb</button>
          <button onclick="setElem('cd')" id="qbtn-cd" class="qbtn py-0.5 rounded border border-[var(--border)] bg-[var(--background)] font-bold text-[10px]">Cd</button>
          <button onclick="setElem('as_val')" id="qbtn-as_val" class="qbtn py-0.5 rounded border border-[var(--border)] bg-[var(--background)] font-bold text-[10px]">As</button>
          <button onclick="setElem('hg')" id="qbtn-hg" class="qbtn py-0.5 rounded border border-[var(--border)] bg-[var(--background)] font-bold text-[10px]">Hg</button>
        </div>
      </div>
    </div>

    <!-- Live Equation Display -->
    <div class="bg-[var(--background)] p-2.5 rounded-lg border border-[var(--border)] space-y-1.5 font-mono text-[11px]">
      <div class="flex justify-between text-[10px] text-[var(--muted-foreground)]">
        <span>C_sampel: <b id="val-craw" class="text-blue-400">37.15 ppb</b></span>
        <span>C_blank: <b id="val-cblank" class="text-amber-400">12.26 ppb</b></span>
        <span>W: <b>0.20 g</b></span>
        <span>V: <b>50 mL</b></span>
      </div>
      <div class="text-[10px] text-[var(--muted-foreground)] pt-0.5">
        Langkah 1 (Koreksi): <span id="val-cnet" class="text-emerald-400 font-bold">37.15 - 12.26 = 24.89 ppb</span>
      </div>
      <div class="text-[10px] text-[var(--muted-foreground)]">
        Langkah 2: <span class="text-[var(--foreground)]">(24.89 × 50 mL × 1) / (0.2000 g × 1000)</span>
      </div>
    </div>

    <!-- Final Result -->
    <div class="flex items-center justify-between bg-blue-500/10 border border-blue-500/20 px-3 py-2 rounded-lg">
      <span class="text-xs font-semibold text-[var(--muted-foreground)]">Kadar Akhir Sarang Walet:</span>
      <div class="flex items-baseline gap-1.5">
        <span id="val-res" class="text-xl font-extrabold text-blue-400">6.2233</span>
        <span class="text-xs font-bold text-[var(--muted-foreground)]">mg/kg (ppm)</span>
      </div>
    </div>
  </div>

  <script>
    const samples = {json.dumps(samples_data)};
    const blank = {json.dumps(blank_mars)};
    let activeElem = 'al';

    function setElem(e) {{
      activeElem = e;
      document.querySelectorAll('.qbtn').forEach(b => {{
        b.className = 'qbtn py-0.5 rounded border border-[var(--border)] bg-[var(--background)] font-bold text-[10px]';
      }});
      document.getElementById('qbtn-' + e).className = 'qbtn active py-0.5 rounded border border-blue-500 bg-blue-500/20 text-blue-400 font-bold text-[10px]';
      updateCalc();
    }}

    function updateCalc() {{
      const idx = document.getElementById('quick-sample').value;
      const s = samples[idx];
      const rawC = s[activeElem];
      const blankC = blank[activeElem];
      const netC = rawC - blankC;
      let finalRes = (netC * s.volume * s.df) / (s.weight * 1000);

      document.getElementById('val-craw').textContent = rawC.toFixed(2) + ' ppb';
      document.getElementById('val-cblank').textContent = blankC.toFixed(2) + ' ppb';
      document.getElementById('val-cnet').textContent = `${{rawC.toFixed(2)}} - ${{blankC.toFixed(2)}} = ${{netC.toFixed(2)}} ppb`;

      const badge = document.getElementById('quick-badge');
      if (finalRes < 0) {{
        document.getElementById('val-res').textContent = '0.00';
        badge.textContent = 'Status: < Blank (0.00)';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/10 text-amber-400 border border-amber-500/20';
      }} else {{
        document.getElementById('val-res').textContent = finalRes.toFixed(4);
        badge.textContent = 'Status: Valid (> Blank)';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20';
      }}
    }}

    window.onload = updateCalc;
  </script>
</body>
</html>
'''

with open('/home/zidan/.gemini/antigravity/brain/0fb34663-a1d6-46d0-bfbb-3e4c755722e9/compact_calculator.html', 'w', encoding='utf-8') as f:
    f.write(compact_html)

print("Generated compact calculator successfully!")
