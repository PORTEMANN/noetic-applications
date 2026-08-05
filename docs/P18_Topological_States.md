# P18 — Topological States of Matter

## Problem
Extend the topological lever (P0) to electronic bands: quantum Hall insulator and Su–Schrieffer–Heeger (SSH) topological insulator. Same lever — topology of a fiber bundle over the Brillouin zone.

## Method

**Quantum Hall (versant A):** Hofstadter spectrum for flux α = 1/3 per plaquette. Compute Chern numbers by Berry curvature integration.

**SSH (versant B):** Dimerized chain with intra-cell hopping t₁ and inter-cell t₂. Topological phase (t₂ > t₁) hosts protected zero-modes at edges; trivial phase (t₁ > t₂) does not.

## Results

| Test | Result | Criterion |
|------|--------|-----------|
| Chern numbers | 1.02, −1.98, 0.97 | Integers (±0.15) ✓ |
| Sequence | (1, −2, 1) | Matches theory ✓ |
| Sum of Chern | 0.01 ≈ 0 | Torus topology ✓ |
| SSH topological | 2 zero-modes | Protected edges ✓ |
| SSH trivial | 0 zero-modes | No edges ✓ |

## Verdict
✅ **Success**

## Files
- `src/p18_topo.py` — solver
- `data/p18_topo.json` — Chern numbers + SSH zero-modes
