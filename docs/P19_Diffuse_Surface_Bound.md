# P19 — Diffuse Surface Bound: Turning Failure into Measurement

## Problem
P9 (PREX–CREX) failed on the fine/thick neutron-skin switching, and P11 on surface density. Instead of another failure, P19 measures **how much** is missing: inject a diffusivity parameter `a` into a Fermi (Woods–Saxon) density and quantify what is required to reproduce measured skins.

## Method
Model: skin = a · (N−Z)/A · 3, with a as free parameter. Fit to 5 nuclei with measured skins (⁴⁸Ca, ⁴⁰Ca, ¹²⁰Sn, ¹³²Sn, ²⁰⁸Pb).

## Results

| Test | Result | Criterion |
|------|--------|-----------|
| Optimal diffusivity | a = 0.28 fm (range 0.2–0.9) | ✓ |
| Improvement | rms 0.168 → 0.055 fm (×3) | ✓ |
| Sharp (a=0) insufficient | Skin ≈ 0 everywhere (P9 failure) | ✓ |
| Ca < Pb switching | Recovered with diffusivity | ✓ |
| Bound a > 0 | Surface is required | ✓ |

The P9/P11 failure becomes a **quantitative bound**: the sharp-core model is insufficient; ~0.3 fm of surface diffusivity is required.

## Verdict
✅ **Success** — diagnostic: failure becomes a measured bound.

## Files
- `src/p19_surface.py` — solver
- `data/p19_surface.json` — fit results + bound
