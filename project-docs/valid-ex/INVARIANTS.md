# 🛡️ System Invariants: valid-ex

> **Invariants** are non-negotiable rules that MUST hold true across all layers of the system.  
> Neither user code nor AI-generated code is permitted to violate these rules.

---

## 1. Domain & Metrological Invariants (ISO/IEC 17025 & EURACHEM)
- **Invariant D1 (Calibration Minimum Points)**: A linear calibration curve must contain at least 5 non-zero concentration levels (or minimum 3 for screening) plus a blank.
- **Invariant D2 (No Unchecked Extrapolation)**: Sample quantification outside the calibrated dynamic range ($x < \text{LOQ}$ or $x > x_{\max}$) must trigger an explicit regulatory flag/warning.
- **Invariant D3 (Audit Trail Transparency)**: All exported Excel spreadsheets must contain live, native formula strings (e.g. `=SLOPE()`, `=STEYX()`), never static hardcoded numbers for calculated cells.

---

## 2. Technical & Computational Invariants (Layer -1 & Layer -2)
- **Invariant T1 (Memory Bound / No In-Memory Buffering)**: Incoming file uploads $> 10 \text{ MB}$ must be streamed to temporary disk storage; they must NEVER be buffered entirely into Node.js V8 RAM.
- **Invariant T2 (Orphaned File Reaper)**: Every temporary file created during upload must either be deleted immediately upon connection abort (`req.on('aborted')`) or reaped by a TTL cleaner when age $> 2 \text{ hours}$.
- **Invariant T3 (Transactional Data Persistence)**: Calibration data and calculated parameters must be written within an ACID database transaction. Partial saves are strictly forbidden.
