# P16 — Unified Decay Mode Map

## Problem
Predict the dominant decay mode for each nuclide (A, Z): stable, β⁻, β⁺, α, or fission. Lever: Bethe–Weizsäcker binding energy (P11) + Gamow α lifetime (P13) + fissility parameter.

## Method
Single decision tree:
1. Fissility x = Z²/(47A) ≥ 0.70 and Z ≥ 100 → fission
2. A ≥ 140 and Qα > 0 → α
3. Qβ⁻ ≤ 0 and Qβ⁺ ≤ 0 → stable
4. Qβ⁻ > Qβ⁺ → β⁻, else β⁺

## Results (24 reference nuclides)

| Mode | Score |
|------|-------|
| α | 6/6 (all identified) |
| β⁺ | 3/3 (all identified) |
| Stable | 6/9 (3 magic numbers missed) |
| β⁻ | 3/6 (3 quasi-boundary cases) |
| **Global** | **18/24 (75%)** |

The map captures the global structure (valley, α band, fission threshold) but misses fine boundaries where discrete models fail.

## Verdict
⚠️ **Partial success** — structure captured, fine boundaries escape.

## Files
- `src/p16_modes.py` — solver
- `data/p16_modes.json` — 24 nuclides + AZ grid
