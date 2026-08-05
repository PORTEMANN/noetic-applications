# P28 — Unification: Surface + Correlation

**Field:** Nuclear / Atomic / Molecular Physics  
**Verdict:** ✅ Structural Success (7/7)

## Problem

P26 and P27 had each located a frontier and named a missing lever (isovector nuclear potential, electronic r₁₂ correlation). P28 asks: are these two gaps **one and the same**?

## The invariant core

Between Hartree (independent) and split-ζ (in-out), the **one-body densities of He are quasi-invariant** (max deviation 8.9%). The calculation therefore has an **invariant core**: one-body orbitals and densities, stable when correlation is added. What correlation adds is *not there*.

## Electron side: the wall is angular response

- **Strictly zero angular correlation** for spherical orbitals: the θ₁₂ distribution of Hartree and split-ζ are identical. The r₁₂ wall is *exactly* the two-body angular response.
- **Smooth Jastrow factor does not lift it:** optimum at c = 0 (44.3% < 51.5% of split-ζ alone). The residual wall requires **Kato cusp** / explicit angular dependence — a two-body coordinate outside the current operator.

## Nucleus side: isovector structure exists, calibration open

The isovector potential derived from Bethe–Weizsäcker (V₀^n − V₀^p = 2W(N−Z)/A) has the correct *structure* — it separates n/p potentials — but W = A_asym = 24 MeV is **too stiff**: Fermi energies invert. The potential responds to ~A_asym/2 and V₀ central must be calibrated on mean S. **Calibration of the isovector lever remains open** — candidate P29.

## Unified reading

The invariant core (one-body orbitals + densities) is the same on both sides. The single gap is the **two-body response function**. On the electron side it is angular correlation r₁₂ (Kato cusp); on the nuclear side it is the isovector potential response. In both cases it is how *one particle feels another* beyond mean field — the part that a one-body operator, by construction, does not contain.

**The frontier is unified.**

## Verdict

| Criterion | Result |
|-----------|--------|
| Invariant core confirmed (1-body densities, 8.9%) | ✅ |
| r₁₂ wall localized as angular response (0.0% for spherical) | ✅ |
| Smooth Jastrow insufficient | ✅ |
| Isovector structure derived | ✅ |
| Calibration open (published) | ✅ |
| P26/P27 frontiers unified | ✅ |
| P19/P11 boundary re-localized | ✅ |

## Document chain

- Script: `p28_unification.py`
- Data: `p28_unification.json`
- Figure: `p28_unification.png`
- Linked to: P26 (diffusivity), P27 (correlation), P16 (BW coefficients)
