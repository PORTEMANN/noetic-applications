# P26 — Deriving Nuclear Surface Diffusivity

**Field:** Nuclear Physics  
**Verdict:** ⚠️ Partial Success (4/5)

## Problem

P19 had quantified the P9/P11 failure: the sharp model gives zero skin; one must inject a ≈ 0.3 fm of surface diffusivity. P26 asks: can this diffusivity be *derived* from existing levers, without any shape parameter?

## Method (zero shape parameter)

For each nucleus (⁴⁰,⁴⁸Ca, ¹²⁰,¹³²Sn, ²⁰⁸Pb): spherical finite well of radius R = r₀A¹/³ (r₀ = 1.2 fm); depth V₀ calibrated on separation energy S from Bethe–Weizsäcker (P16 coefficients); spectrum solved by radial operator P6; filling of bound states (2(2l+1)); n/p densities summed; diffusivity measured *without fit* by a = t₉₀₋₁₀/4.394.

Two variants: sharp edge, and edge *folded* by finite nucleon size (σ = R_p/√3 = 0.485 fm).

## Results

| Nucleus | a sharp (fm) | a folded (fm) | Skin derived (fm) | Skin measured (fm) |
|---------|-------------|---------------|-------------------|-------------------|
| ⁴⁰Ca | 0.315 | 0.345 | −0.054 | 0.05 |
| ⁴⁸Ca | 0.283 | 0.322 | +0.210 | 0.121 |
| ¹²⁰Sn | 0.612 | 0.421 | +0.060 | 0.12 |
| ¹³²Sn | 0.306 | 0.348 | +0.233 | 0.17 |
| ²⁰⁸Pb | 0.242 | 0.294 | +0.149 | 0.283 |

**For ²⁰⁸Pb:** a_derived = 0.294 fm — within 0.7% of the a_opt = 0.296 fm that P19 had to adjust. **P19 is closed.**

## Failures (published)

1. **Skins at only 2/5** (±0.08 fm): ²⁰⁸Pb underestimated, ⁴⁸Ca overestimated. The missing lever is the **isovector potential asymmetry** — candidate P28/P29.
2. **First run correction:** initial conclusion of a ≈ 0.12 fm via flawed Fermi fit was overturned by robust t₉₀₋₁₀ measurement.
3. **Targets themselves are tense** (PREX-II 0.283 vs CREX 0.121): the calculation falls on the mean-field consensus (~0.15–0.20 fm).

## Verdict

| Criterion | Result |
|-----------|--------|
| Derived profiles for 5 nuclei | ✅ |
| Folded a within P19 envelope (0.20–0.45) | ✅ |
| Sharp diffusivity non-zero | ✅ |
| Skins beating sharp baseline (0.094 < 0.168) | ✅ |
| Skins within ±0.08 fm (2/5) | ❌ (documented) |

## Document chain

- Script: `p26_diffusivite.py`
- Data: `p26_diffusivite.json`
- Figure: `p26_diffusivite.png`
- Linked to: P19 (surface bound), P16 (BW coefficients), P6 (radial operator)
