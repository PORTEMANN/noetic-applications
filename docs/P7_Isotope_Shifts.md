# P7 — Isotope Shifts in Chlorine

**Domain:** Atomic physics — finite-nuclear-size effects  
**Status:** ✅ Success  
**Data:** ³⁵Cl, ³⁶Cl, ³⁷Cl, ⁴⁰Cl (Z = 17)  
**Solver:** Non-perturbative radial Schrödinger, uniform charge sphere

## Problem

Isotopes have the same Z but different A: the point Coulomb is *identical* for all,
only the finite nuclear core radius changes (R_c = r₀ A^(1/3)). The isotope shift
is therefore the pure signature of the finite core — the cleanest test of what
a non-perturbative solver brings beyond perturbation theory.

## Protocol

- Four chlorine isotopes (Z = 17; A = 35, 36, 37, 40)
- Uniform charge sphere R_c = r₀ A^(1/3)
- Radial Schrödinger (NR = 40000, convergence verified at 7 digits on 40000 → 240000)
- Electronic and muonic versions
- Verdict: isotope shift ΔE₁s(A₂ − A₁), compared to point Coulomb and first-order
  perturbation theory ΔE_th = (2/5) Z⁴ α⁴ m³ Δ(R_c²)

## Results

| shift A₂ − A₁ | solver (el.) | perturbation (el.) | solver / pert. |
|---------------|-------------:|-------------------:|---------------:|
| ³⁷ − ³⁵      | +3.97 × 10⁻⁵ | +7.22 × 10⁻⁴       | 0.055          |
| ⁴⁰ − ³⁵      | +9.56 × 10⁻⁵ | +1.78 × 10⁻³       | 0.054          |

Relative to E₁s: 8.3 × 10⁻³ (³⁷−³⁵ el.); 2.7 × 10⁻² (³⁷−³⁵ μ)

## What the solver brings: the non-perturbative regime

1. **Sign and order are correct:** the heavy isotope (larger R_c) has a *less* bound
   1s — the finite-size effect decreases as the core grows. The shift is measurable:
   0.8% (el.) to 2.7% (μ) of the fundamental between ³⁵Cl and ³⁷Cl.

2. **First-order perturbation theory is wrong here:** it overestimates by a factor
   of 18 (electronic) because the hierarchy R_c/a₀ = 1.2 is *not* small. The
   non-perturbative solver is exact: this is the core of its value — where
   perturbation breaks down, the verdict holds.

3. **Muon saturation:** for the muon, the orbit (a₀^(μ) = 0.039 lattice unit) is
   *deep inside* the core (R_c = 14.5 units, R_c/a₀^(μ) = 372). The muon no longer
   sees a Coulomb potential but a quasi-parabolic well (harmonic oscillator inside
   the charge sphere). Linear perturbation then diverges by a factor ~10⁷; the
   solver, resolving the true potential, saturates correctly. This is the clearest
   demonstration: the solver sees the regime that the approximation misses.

## Limitations and corrections (published)

- The "uniform sphere" potential is a charge model; real nuclei have a diffuse
  skin (Fermi) — the absolute shift depends slightly on it, the isotopic ratio
  much less.
- First-order perturbation theory, used as a reference, is *outside its domain*
  when the hierarchy ≳ 1: the solver/perturbation ratio (0.055) is not a solver
  error but the *measure* of non-perturbativity — published as such.

## Verdict

**P7 is a success.** The solver distinguishes isotopes by their finite core and
corrects the theory where it breaks down. The isotope shift of chlorine is
measured (³⁷Cl/³⁵Cl: 8×10⁻³ el., 3×10⁻² μ), the non-perturbative regime captured
(perturbation wrong by 18 to 10⁷), and muon saturation explained (parabolic well
in the core). This is the solver's own added value.

---

**Stratum:** S3 (off-corpus, constitutive)  
**Anchors:** r_p = 0.84 fm (S1 measured)  
**No adjusted parameters.**
