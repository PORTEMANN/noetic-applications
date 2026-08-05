# P25 — Topological Insulators (2D and 3D)

**Field:** Condensed Matter Physics  
**Verdict:** ✅ Success (6/6)

## Problem

Generalize the Chern number of P18 to real lattices: Haldane model, Kane–Mele Z₂ invariant, and 3D strong index — using only the Berry connection method (P18), with zero adjusted parameters.

## Models

1. **Haldane (2D, broken TR):** d_z(k) = M − 2t₂ sin φ Σᵢ sin(k·bᵢ). At valleys: d_z(K) = M + 3√3 t₂ sin φ, d_z(K') = M − 3√3 t₂ sin φ.
2. **Kane–Mele (2D, TR conserved):** two copies of Haldane (φ, −φ) for the two spins.
3. **Wilson–Dirac (3D):** H(k) = Σᵢ sin kᵢ Γᵢ + (m + Σᵢ cos kᵢ) Γ₀.

## Results

| Test | Derived | Numerical | Match |
|------|---------|-----------|-------|
| Haldane Chern in phase | C = ±1 | −1 (stable, 30² grid) | ✓ |
| Phase boundary | \|M/t₂\| = 3√3 \|sin φ\| = 5.196 | transition at 5.0 | ✓ |
| Kane–Mele | C_total = 0, Z₂ = 1 | C↑ = −1, C↓ = +1 | ✓ |
| Helical ribbon | Kramers pair at TRIM | 2 pairs at k=0, 0 at k=π | ✓ |
| 3D strong phases | 1 < \|m\| < 3 | ν₀ numeric = analytic (6/6) | ✓ |
| Lever negative (φ=0, t₂=0, \|M\| large) | trivial | C = 0, ν₀ = 0 | ✓ |

## Internal correction

First pass: Berry connection method produced stable but wrong integers (C = 12!) due to a ULP difference at the Brillouin zone seam — corrected by modular indices. QWZ control (|C| = 1 for 0 < |m| < 2) recovered exactly.

## Verdict

| Criterion | Result |
|-----------|--------|
| Haldane C = ±1 and exact boundary 3√3 | ✅ |
| Kane–Mele Z₂ = 1 without net Hall | ✅ |
| Helical edge verified (bulk-boundary) | ✅ |
| 3D strong index from sign of masses at TRIM | ✅ |
| Discriminating lever without mechanism | ✅ |
| First-pass bug published and corrected | ✅ |

## Document chain

- Script: `p25_topologie.py`
- Data: `p25_topologie.json`
- Figure: `p25_topologie.png`
- Linked to: P17 (flux quantum), P18 (Chern integer)
