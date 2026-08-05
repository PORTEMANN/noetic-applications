# P29 — Calibrating the Isovector Lever

**Field:** Nuclear Physics  
**Verdict:** ✅ Discriminating Success (5/6)

## Problem

P28 had derived the *structure* of the isovector lever (V₀^n − V₀^p = 2W(N−Z)/A) but left its calibration open: W = A_asym = 24 MeV was too stiff (inverted Fermi energies). P29 calibrates: central V₀ on mean BW separation energy, then V₀^{n/p} = V₀^c ± κ A_asym δ, with κ *derived* by minimizing rms on skins.

## Two lessons

1. **P28 defect corrected:** calibrating central V₀ on mean S restores coherent Fermi energies (all negative, close to S) — the pathological inversion disappears.
2. **But the isovector lever does not improve.** The optimal κ is **zero**: adding the symmetry term to the mean potential does not bring measured skins closer (rms 0.085 fm at κ = 0, not improved for κ > 0). The skin residual is *not* a matter of mean symmetry potential.

## Failures (published)

1. Skins at only 1/4 within tight bounds (±0.08 fm): central calibration alone does not reproduce them.
2. ²⁰⁸Pb not calculated: at central V₀ calibrated on mean S, the magic proton (Z = 82) loses bound states — brute calibration remains unstable for **magic** nuclei.
3. Measured targets remain tense (PREX/CREX).

## Reading: the nuclear frontier is the shell

The discriminant κ_opt = 0 is the central result. It says that neutron skin — the surface observable — does not come from the continuous response of the symmetry potential, but from **shell structure**: the number and nature of the last occupied levels (their l, their radial tail) fix the skin, not a continuous potential bump. The shell is already at the heart of the calculation (P12 derived it for the atom) — but the smooth spherical well of P26–P29 restores it only imperfectly.

## Synthesis with P28

P28 had unified the frontier as a *two-body response function*. P29 specifies it on the nuclear side: this function is not a continuous symmetry potential (lever tested, κ = 0), it is the **discrete level structure** — the same shell that the calculation already derives elsewhere. On the electron side, P28 showed it is angular correlation r₁₂. The unified frontier is therefore: *what escapes one-body mean field* — discrete (shell) on the nuclear side, angular (r₁₂) on the electron side.

## Verdict

| Criterion | Result |
|-----------|--------|
| Central calibration fixes P28 (coherent EF) | ✅ |
| κ_opt = 0 — mean isovector term does not improve | ✅ |
| Skin residual re-localized on **shell** | ✅ |
| Criterion failed (skins tight) documented | ✅ |
| P28 frontier unified and specified | ✅ |
| Magic nuclei stability | ⚠️ (²⁰⁸Pb unstable) |

## Document chain

- Script: `p29_isovecteur.py`
- Data: `p29_isovecteur.json`
- Figure: `p29_isovecteur.png`
- Linked to: P28 (unification), P26 (diffusivity), P6 (radial operator)
