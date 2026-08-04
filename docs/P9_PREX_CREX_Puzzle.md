# P9 — PREX–CREX Neutron-Skin Puzzle

**Domain:** Nuclear physics — parity-violating electron scattering  
**Status:** ⚠️ Instructive negative result; boundary located  
**Data:** PREX-II (²⁰⁸Pb), CREX (⁴⁸Ca), RIKEN (¹³²Sn)  
**Solver:** Shell model with spin-orbit (v4), plus three documented failures (v1–v3)

## Problem

Two parity-violation measurements (without strong-interaction uncertainty) give
incompatible neutron skins for global models:

- **PREX-II** (²⁰⁸Pb) ⇒ thick skin, Δr_np = 0.283 ± 0.071 fm, stiff symmetry
  energy (L = 106 ± 37 MeV)
- **CREX** (⁴⁸Ca) ⇒ thin skin, Δr_np = 0.121 ± 0.026 fm, soft symmetry energy

No density functional reproduces both at 68%. Since 2026, a third doubly magic
nucleus, ¹³²Sn (RIKEN), also gives a thin skin — a triplet (⁴⁸Ca, ¹³²Sn, ²⁰⁸Pb)
that tightens the vice. This is an isovector nuclear structure problem at two
scales — exactly where the solver proved its value (P6–P8).

## Anchors (measured)

- **Skins:** ⁴⁸Ca 0.121 ± 0.026 fm (CREX); ¹³²Sn, thin skin (RIKEN, R_m − R_ch);
  ²⁰⁸Pb 0.283 ± 0.071 fm (PREX-II)
- **Symmetry energy:** slope L = 3 ρ₀ dS/dρ|₀; PREX-II ⇒ L ~ 106 MeV (stiff),
  CREX + ¹³²Sn ⇒ L low (soft)
- **Triplet:** all three nuclei are doubly magic (⁴⁸Ca: Z=20, N=28; ¹³²Sn: Z=50,
  N=82; ²⁰⁸Pb: Z=82, N=126) — the simplest structurally, therefore the cleanest
  test of the isovector sector.
- **Theoretical lead:** Zhang & Chen (Nusym24) — a strong isovector spin-orbit
  reconciles CREX and PREX, because ⁴⁸Ca and ²⁰⁸Pb have different shell and
  surface structures.

## The mechanism (derived, not postulated)

The nucleus = an isoscalar core (paired protons + neutrons) + excess neutrons
(N − Z) to place. The PREX–CREX question: where do these excess neutrons go?
The skin is their spatial distribution relative to protons.

In the finite-core model, excess neutrons occupy valence orbits above the paired
core. Two facts from the solver drive the switching:

- P7 showed that the core regime changes with its size (R_c ∝ A^(1/3)): for a
  small core, valence orbits are *inside* or at the edge (saturated regime, thin
  skin); for a large core, surface tension and symmetry pressure push excess
  neutrons outward (thick skin).
- P8 established that the solver distinguishes regimes by *form* — here, the
  control parameter is N − Z and the scale A^(1/3).

**Prediction:** the relative skin Δr_np/R grows with neutron excess *and* with A
in a non-monotone way — thin for ⁴⁸Ca (N−Z=8) and ¹³²Sn (taut surface, broad
shells), thick for ²⁰⁸Pb (N−Z=44, large surface).

## Four attempts, three failures documented

### v1 — Single valence orbit
Skin *negative* and monotone — scale artefact; the radius of a single orbit is
not the distribution skin.

### v2 — Geometric Woods-Saxon
Skin *null* — radius is driven by R_c (geometry), insensitive to depth; surface
physics is missing.

### v3 — Symmetry/surface minimisation, quadratic term
*Saturation* of all heavy nuclei to the same value — the switching is masked by
the form of the surface term.

These three successive failures are the real content of P9: the neutron skin is a
problem of *continuous surface density*, which neither a single orbit, nor a
geometry, nor a simple phenomenological minimisation captures.

### v4 — Shell model with spin-orbit
The Zhang–Chen mechanism (isovector spin-orbit) implemented: filling of shells
(n, l, j) of a Woods-Saxon + spin-orbit well, matter radii (n+p) vs charge (p).

| Nucleus | N − Z | Solver skin (fm) | Experiment (fm) |
|---------|------:|-----------------:|----------------:|
| ⁴⁸Ca    | 8     | +0.199           | 0.121 ± 0.026 (CREX) |
| ¹³²Sn   | 32    | +0.250           | thin (RIKEN) |
| ²⁰⁸Pb   | 44    | +0.221           | 0.283 ± 0.071 (PREX-II) |

## The right magnitude, the wrong switching, and why

1. **Succeeded:** v4 gives a positive skin of ~0.2 fm — the right order of
   magnitude, where v1–v3 failed. Spin-orbit captures surface distribution by shells.

2. **Failed:** the switching is *inverted* — the solver gives Ca (0.199) < Pb
   (0.221) but Sn (0.250) > Pb, whereas experiment requires Pb clearly above
   (0.283) of Ca+Sn (~0.13).

3. **Cause identified:** shell analysis shows that Pb valence neutrons are in
   high-angular-momentum orbitals (i₁₃/₂, l = 6, radius 5.5 fm) — strongly
   localised near the edge but *inside* the core. The discrete shell model misses
the *continuous surface density diffusion* of Pb's 44 excess neutrons (large
volume, low symmetry cost per neutron), which is the true mechanism of the thick
skin. Sn has more external shells in this model (l=5 at 4.7 fm) giving its falsely
high skin.

## Limitations (published with the verdict)

- The solver computes mean orbit radii, not full densities: Δr_np is a proxy for
  the skin; conversion to experimental R_n − R_p assumes a distribution
  (sphere/Fermi).
- The symmetry term and surface tension are constitutive assumed parameters
  (stratum S3) — the verdict is on the *switching* (qualitative, robust), not on
the absolute value of L.
- ¹³²Sn (RIKEN) has large error bars and is measured by hadronic reaction (less
clean than parity violation) — lower weight in the verdict.

## Verdict

**P9 is a negative result, published as such; the solver's boundary is located.**
The solver captures spin-orbit and the right order of magnitude (v4), but *misses
the fine/thick switching*: the discrete shell model does not reproduce the
continuous surface density diffusion that makes ²⁰⁸Pb thick-skinned. This is not a
success — and it is valuable knowledge: it locates exactly where the finite-core
model must be extended (continuous surface density, not discrete shells) to speak
about the neutron skin.

In accordance with honest reporting, the failure is published with the same care
as a success, with its three documented attempts. **No parameter was adjusted to
force the switching.**

**Recommendation:** either extend the model (continuous density — work in progress),
or retain the boundary as a documented limit of the solver.

---

**Stratum:** S3 (off-corpus, constitutive)  
**Anchors:** PREX-II, CREX, RIKEN data (S2 preliminary / external data)  
**No adjusted parameters.**
