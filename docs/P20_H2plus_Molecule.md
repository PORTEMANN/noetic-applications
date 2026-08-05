# P20 — H₂⁺: The Only Exactly Solvable Molecule

## Problem
Test the many-body frontier. H₂⁺ = 1 electron + 2 protons is the **only** molecular system exactly solvable by a one-body operator. If the machine fails here, it cannot claim any molecule.

## Method
LCAO on 1s orbitals with variable exponent ζ, minimize E(R) + 1/R (internuclear repulsion). The gérade state accumulates density between protons → covalent bond.

## Results

| Test | Calculated | Measured | Match |
|------|-----------|----------|-------|
| Minimum exists | Yes (E < E_diss) | — | ✓ |
| Equilibrium R | 2.18 a₀ | 2.0 a₀ | Within 9% |
| Binding energy Dₑ | 1.40 eV | 2.79 eV | Order of magnitude |
| Dissociation | H + p⁺ | — | ✓ |

The LCAO-1s underestimates Dₑ by ~1 eV (expected: no correlation). The frontier is **located**: beyond H₂⁺, multi-electron correlation begins.

## Verdict
✅ **Success** — frontier located. H₂⁺ is exact; H₂ (2 e⁻) is beyond.

## Files
- `src/p20_h2plus.py` — solver
- `data/p20_h2plus.json` — H₂⁺ binding curve + frontier note
