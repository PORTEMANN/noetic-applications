# P15 — Hadron Spectrum: Regge + Charmonium

## Problem
Extend P13 (Regge slope, string breaking) to the full measured hadron spectrum. Two regimes:
- **Light quarks** (ultra-relativistic): linear Regge trajectories, universal slope
- **Heavy quarks** (non-relativistic): Cornell potential (−k/r + σr), charmonium spectrum

## Method

**Regge (versant A):** Test M² = 2πσ(2n + L) against ρ meson radial (n) and orbital (L=J) excitations.

**Charmonium (versant B):** Solve −(ℏ²/2μ)∇² − k/r + σr for mc = 1.84 GeV, k = 0.52 GeV/fm. The absolute constant V₀ cancels in level spacings.

## Results

| Test | Calculated | Measured | Match |
|------|-----------|----------|-------|
| Regge radial slope | 0.765 | 0.884 (theory) | Within 14% |
| Regge orbital slope | 0.904 | 0.884 (theory) | Within 2% |
| Both trajectories | Encadrent 0.884 | ✓ | ✓ |
| Charmonium S−P | 426 MeV | 429 MeV | 1% |
| Charmonium 2S−1S | 588 MeV | 589 MeV | 0% |
| Level order | 1S < 1P < 2S | ✓ | ✓ |

## Verdict
✅ **Success**

## Files
- `src/p15_hadrons.py` — solver
- `data/p15_hadrons.json` — Regge fits + charmonium spacings
