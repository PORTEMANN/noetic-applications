# P14 — Atomic Identity Cards: H → U

## Problem
Extend the finite-core identity cards from P10 (9 elements) to the complete periodic table (H → U, 92 elements). The same finite-core radial operator validated in P6 and P10 is used for every element.

## Method
For each element (Z, A, symbol), compute the 1s energy with a finite nuclear charge distribution (uniform sphere, Rc = r₀A^(1/3)). The signature is δ₁s = (E_finite − E_point) / |E_point|.

Two probes:
- **Electron**: a₁s = a₀/Z (grows with Z, core eventually resolved)
- **Muon** (mass 207×): a₁s^μ = a₀/(207Z) (saturated everywhere)

## Results

| Test | Result | Criterion |
|------|--------|-----------|
| Complete table | 92/92 elements | ✓ |
| δ₁s monotonic | 3.8×10⁻⁴ (H) → 0.87 (U) | ✓ |
| Electron boundary Rc/a₁s = 1 | At Z = 12 (Mg) | ✓ |
| Muon saturated everywhere | Rc/a₁s^μ > 1 for all Z | ✓ |
| Hierarchy H→Pb | >10³ × 2.2×10³ on signature | ✓ |

## Verdict
✅ **Success**

## Files
- `src/p14_table.py` — solver
- `data/p14_table.json` — all 92 cards (Z, A, Rc, δ₁s, regime)
