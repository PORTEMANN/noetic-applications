# P27 — Two-Electron Correlation (He, H₂)

**Field:** Atomic / Molecular Physics  
**Verdict:** ✅ Success (5/5)

## Problem

P20 located the many-body frontier beyond H₂⁺ (1 electron). P27 steps to two electrons: He (atom) and H₂ (molecule). Can a one-body operator treat correlation, or does it stop dead?

**Method:** variational Monte Carlo with common random numbers, exact local energy for exponential orbitals (no adjusted integrals; Eckart 1930 and Wang 1928 references reproduced).

## He: radial correlation is crossable

| Method | E (Ha) | vs exact | % of E_c recovered |
|--------|--------|----------|-------------------|
| Hartree (single ζ) | −2.8477 | 1.93% | 0 |
| Split-ζ in-out (MC) | −2.8766 | 0.94% | 51.5% |
| Exact (Pekeris) | −2.9037 | — | 100% |

- **Ionization:** I₁ = 23.07 eV vs 24.59 measured (6.2%).
- Split-ζ minimum at (a,b) = (1.16, 2.20), within 9×10⁻⁴ Ha of Eckart reference.

## H₂: covalent correlation is crossable

| Method | R_eq (a₀) | D_e (eV) | Dissociation |
|--------|-----------|----------|--------------|
| MO gerade double (RHF) | 1.60 | 2.75 | wrong (ionically contaminated) |
| Heitler–London (VB) | **1.40** | **3.80** | correct (E(∞) = −1.00 Ha) |
| Exact | 1.401 | 4.75 | — |

- **52.4%** of the MO→exact gap recovered.
- Wang 1928 result (D_e ≈ 3.78 eV, ζ ≈ 1.17) reproduced.

## The frontier is a gradient

1. **Mean field (Hartree):** existence, orders of magnitude, variational bound.
2. **Radial/covalent correlation:** accessible in one-body orbitals (in-out for He, VB for H₂), ~50% of E_c.
3. **Angular correlation (r₁₂):** the wall, requiring an explicitly two-body coordinate.

## Verdict

| Criterion | Result |
|-----------|--------|
| He energy within 2% | ✅ |
| Ionization within 10% | ✅ |
| In-out recovers ≥ 45% E_c | ✅ |
| H₂ MO R_eq within 15% | ✅ |
| H₂ VB recovers ≥ 50% of gap | ✅ |

## Document chain

- Script: `p27_correlation.py`
- Data: `p27_correlation.json`
- Figure: `p27_correlation.png`
- Linked to: P20 (H₂⁺), P12 (molecular frontier), P6 (radial operator)
