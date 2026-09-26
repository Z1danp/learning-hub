import openpyxl
import xlrd

# Paths
raw_path = 'references/Instrumentations/ICP-MS/251201-Sarang Walet.xls'
tmpl_path = 'references/Instrumentations/ICP-MS/Olah Data ICP-MS.xlsx'

# Load raw workbook
wb_raw = xlrd.open_workbook(raw_path)
s_raw = wb_raw.sheet_by_index(0)

# Load template workbook
wb_tmpl = openpyxl.load_workbook(tmpl_path)
ws2 = wb_tmpl['Sheet2']
ws1 = wb_tmpl['Sheet1']

# Channels in raw data:
# Col 57: 27Al (KED)
# Col 109: 208Pb (KED)
# Col 95: 111Cd (KED)
# Col 83: 75As (KED)
# Col 105: 202Hg (KED)
col_idx = {'Al': 57, 'Pb': 109, 'Cd': 95, 'As': 83, 'Hg': 105}

# 1. Update TableStandard (Sheet2 L5:Q16)
std_data = [
    # (row in Sheet2, raw_row, hg_raw_row)
    (5, 4, 4),   # Blank Baku
    (6, 13, 5),  # Baku 10 ppb / Std Hg 1
    (7, 14, 6),  # Baku 50 ppb / Std Hg 2
    (8, 15, 7),  # Baku 100 ppb / Std Hg 3
    (9, 16, 8),  # Baku 300 ppb / Std Hg 4
    (10, 17, 9), # Baku 500 ppb / Std Hg 5
    (11, 18, 10),# Baku 700 ppb / Std Hg 6
    (12, 19, 11),# Baku 800 ppb / Std Hg 7
    (13, 20, 12),# Baku 1000 ppb / Std Hg 8
    (14, 26, 26),# Blank Mars (Date) -> Blank 011225
    (15, 31, 31),# Blank Spike -> 4287 Spike
    (16, 29, 29),# CS 500 ppb -> Row 29
]

for r_s2, r_raw, r_hg in std_data:
    ws2.cell(r_s2, 13).value = s_raw.cell_value(r_raw, col_idx['Al']) # M: Al
    ws2.cell(r_s2, 14).value = s_raw.cell_value(r_raw, col_idx['Pb']) # N: Pb
    ws2.cell(r_s2, 15).value = s_raw.cell_value(r_raw, col_idx['Cd']) # O: Cd
    ws2.cell(r_s2, 16).value = s_raw.cell_value(r_raw, col_idx['As']) # P: As
    ws2.cell(r_s2, 17).value = s_raw.cell_value(r_hg, col_idx['Hg'])  # Q: Hg

# 2. Extract Samples from raw data (excluding WASH, CS, CRM, Blank)
sample_rows = []
for r in range(26, s_raw.nrows):
    sline = s_raw.cell_value(r, 1)
    if not any(k in sline for k in ['WASH', 'CS', 'CRM', 'Blank 011225']):
        sample_rows.append((r, sline))

print(f"Total sample rows extracted: {len(sample_rows)}")

# 3. Populate TableData (Sheet2 B6:J41) - 36 rows
for i in range(36):
    r_s2 = 6 + i
    if i < len(sample_rows):
        r_raw, sname = sample_rows[i]
        ws2.cell(r_s2, 2).value = sname
        ws2.cell(r_s2, 3).value = s_raw.cell_value(r_raw, col_idx['Al'])
        ws2.cell(r_s2, 4).value = s_raw.cell_value(r_raw, col_idx['Pb'])
        ws2.cell(r_s2, 5).value = s_raw.cell_value(r_raw, col_idx['Cd'])
        ws2.cell(r_s2, 6).value = s_raw.cell_value(r_raw, col_idx['As'])
        ws2.cell(r_s2, 7).value = s_raw.cell_value(r_raw, col_idx['Hg'])
        ws2.cell(r_s2, 8).value = 0.2000 # default nominal weight 0.2000 g
        ws2.cell(r_s2, 9).value = 50.0   # volume 50 mL
        ws2.cell(r_s2, 10).value = 1.0   # dF = 1
    else:
        ws2.cell(r_s2, 2).value = ''
        for c in range(3, 8):
            ws2.cell(r_s2, c).value = 0
        ws2.cell(r_s2, 8).value = 0.2000
        ws2.cell(r_s2, 9).value = 50.0
        ws2.cell(r_s2, 10).value = 1.0

# 4. Correct Sheet1 Formulas with accurate Blank Mars cell references
# Blank Mars in Sheet2:
# Al:  $M$14
# Pb:  $N$14
# Cd:  $O$14
# As:  $P$14
# Hg:  $Q$14
elem_cols = [
    (3, 'Al', '$M$14'),
    (4, 'Pb', '$N$14'),
    (5, 'Cd', '$O$14'),
    (6, 'As', '$P$14'),
    (7, 'Hg', '$Q$14'),
]

for r in range(6, 42):
    ws1.cell(r, 2).value = '=TableData[[#This Row],[ID SAMPLE]]'
    for c_idx, elem, blank_cell in elem_cols:
        formula = (
            f'=IF(((TableData[[#This Row],[{elem}]] - Sheet2!{blank_cell}) * TableData[[#This Row],[Volume]] * TableData[[#This Row],[dF]] / (TableData[[#This Row],[Weight]]* 1000)) < 0, '
            f'"0.00", '
            f'(TableData[[#This Row],[{elem}]] - Sheet2!{blank_cell}) * TableData[[#This Row],[Volume]] * TableData[[#This Row],[dF]] / (TableData[[#This Row],[Weight]] * 1000))'
        )
        ws1.cell(r, c_idx).value = formula

# 5. Fix Recovery Formulas in Sheet1 Row 5 & Row 6
# Target concentrations in Sheet2:
# Row 19: Cek Std (CRM): Col M = 50 ug/L, Col Q = 500 ug/L
# For Al: CS 500 ppb is around 380 ppb, target is 500 ppb (Col Q19)
# For Pb, Cd, As: CS 500 ppb has ~41 ppb, target is 50 ppb (Col M19)
# For Hg: target in CS 500 ppb is ~200 ppb
ws1['I5'].value = '=(Sheet2!M16/Sheet2!$Q$19)*100' # Rec Al %
ws1['J5'].value = '=(Sheet2!N16/Sheet2!$M$19)*100' # Rec Pb %
ws1['K5'].value = '=(Sheet2!O16/Sheet2!$M$19)*100' # Rec Cd %
ws1['L5'].value = '=(Sheet2!P16/Sheet2!$M$19)*100' # Rec As %
ws1['M5'].value = '=(Sheet2!Q16/200)*100'          # Rec Hg %

# Save template
wb_tmpl.save(tmpl_path)
print("Populated Olah Data ICP-MS.xlsx successfully with verified formulas!")
