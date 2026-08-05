# Noetic Applications — Case Studies on Experimental Data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Noetic Machine](https://img.shields.io/badge/noetic--machine-v1.0-blue)](https://github.com/PORTEMANN/noetic-machine)

> Applications of the Noetic non-perturbative solver to real experimental data:
> isotope shifts, EMC effect, PREX–CREX neutron-skin puzzle, periodic-table structure,
> valley of stability, chemical valence, alpha decay / quark confinement,
> hadron spectrum, topological states, and molecular frontier.

## Overview

This repository contains case studies applying the **Noetic Machine** (a non-perturbative
finite-core solver) to well-defined problems in atomic, nuclear, particle, and condensed-matter physics.
Each case includes:
- A documented problem statement with experimental anchors
- Python implementation (`src/`)
- Raw numerical results (`data/`)
- A verdict: success, partial success, instructive failure, or boundary located

## Case Studies

| # | Domain | Data | Result | Status |
|---|--------|------|--------|--------|
| **P7** | Atomic physics | ³⁵Cl/³⁷Cl isotope shift | Non-perturbative exact; perturbation theory fails by 18× | ✅ Success |
| **P8** | Nuclear physics | EMC effect (DIS, MARATHON) | SRC preferred over mean-field by form of modification | ✅ Success |
| **P9** | Nuclear physics | PREX-II, CREX, RIKEN ¹³²Sn | Good magnitude, wrong fine/thick switching; boundary located | ⚠️ Instructive failure |
| **P10** | Atomic physics | ANU audit (88 elements) | N/18 points to dominant isotopes; core hierarchy validated | ✅ Measured success |
| **P11** | Nuclear physics | Valley of stability anchors | Form captured (trough, beta-line); absolute scale approximate | ⚠️ Partial success |
| **P12** | Quantum chemistry | Benzene, CBD, valence table | Octet, Hückel 4n+2, aromaticity derived from degeneracy | ✅ Success |
| **P13** | Nuclear / particle | Alpha emitters, Regge slope | Geiger-Nuttall slope + hierarchy; confinement Regge match | ✅ Success |
| **P14** | Atomic physics | Periodic table H→U (92 elements) | Identity cards; electron boundary at Z=12; muon saturated | ✅ Success |
| **P15** | Particle physics | Regge trajectories, charmonium | Universal slope 1/(2πσ); Cornell spacings within 1% | ✅ Success |
| **P16** | Nuclear physics | Decay mode map (24 nuclides) | 18/24 correct; α and β⁺ perfect; boundary cases escape | ⚠️ Partial success |
| **P17** | Mesoscopic physics | Aharonov–Bohm rings | Periodicity Φ₀=h/e; gap closure at ½-flux; persistent current | ✅ Success |
| **P18** | Condensed matter | Quantum Hall, SSH chain | Chern (1,−2,1); protected edge zero-modes | ✅ Success |
| **P19** | Nuclear physics | Neutron skin (5 nuclei) | Diffuse surface bound: a ≈ 0.28 fm required | ✅ Success (diagnostic) |
| **P20** | Molecular physics | H₂⁺ (1 e⁻, 2 p⁺) | Exact LCAO; R_eq=2.18 a₀; D_e=1.40 eV; frontier located | ✅ Success |

### P7 — Isotope Shifts in Chlorine
The isotope shift is the pure signature of the finite nuclear core: same Z, different A,
same point Coulomb, different core radius. The solver computes the 1s shift exactly
for electronic and muonic versions of Cl-35/36/37/40. Perturbation theory is wrong
by a factor of 18 (electronic) to 10⁷ (muonic saturation regime).

### P8 — EMC Effect: Mean-Field vs SRC
The European Muon Collaboration effect (1983) remains unexplained. Two hypotheses:
mean-field (all nucleons modified by density) vs Short-Range Correlations (only
paired nucleons modified). The solver distinguishes them by computing the *form*
of the modification: linear in density vs saturating at pair contact. The SRC
signature matches three experimental facts: EMC–SRC correlation, saturation at
heavy nuclei, and isospin dependence (MARATHON).

### P9 — PREX–CREX Neutron-Skin Puzzle
A negative result published with the same care as a success. Three failed attempts
(v1–v3) documented, then v4 (shell model with spin-orbit) captures the right
magnitude but inverts the fine/thick switching. The boundary is located: discrete
shell models cannot capture the continuous surface density diffusion that makes
²⁰⁸Pb thick-skinned.

### P10 — ANU Bridge: Periodic Table Identity Cards
The ANU audit (1918) provides quantum-counted values for 88 elements. The solver
shows that `N/18` points to the *dominant isotope* rather than the weighted average,
resolving the worst deviations as isotopic structure. Each element receives a
"core identity card": `Rc = r0 A^(1/3)` and hierarchy `Rc/a0`.

### P11 — Valley of Stability
The Bethe-Weizsäcker mass formula is derived from finite-core geometry: Coulomb
`ac` from `r0`, surface `as` from `Rc ~ A^(1/3)`, symmetry `aa` and pairing `ap`
from core-scale isovector and pair structure. The form (trough, beta-stability line,
curvature) is captured without fit; absolute scale is approximate (RMS 0.25 MeV).
Magic numbers remain outside the smooth model.

### P12 — Chemistry and Valence
The octet rule (`2(2l+1)`), valence counting (`min(n, 8−n)`), and Hückel aromaticity
(`4n+2`) are derived from degeneracy structure. The Möbius control inverts the rule
to `4n`, proving its topological origin. Benzene vs cyclobutadiene, Jahn-Teller
distortion, and Aharonov-Bohm flux all match experiment.

### P13 — Stability as Form of the Potential
Alpha radioactivity (finite barrier) and quark confinement (infinite barrier) are
unified in the finite-core potential framework. The Geiger-Nuttall slope (1.60 vs
1.57 measured) and 30-order hierarchy are reproduced without fit. String breaking
(1.70 fm) and Regge slope (0.884 vs 0.9 GeV⁻²) match QCD phenomenology.

### P14 — Atomic Identity Cards: H → U
Extend the finite-core identity cards to the complete periodic table (92 elements).
The electron probe crosses the boundary Rc/a₁s = 1 at Z = 12 (Mg); the muon probe
is saturated everywhere. Each element receives a core identity card with δ₁s,
regime classification, and hierarchy.

### P15 — Hadron Spectrum: Regge + Charmonium
Test the universal Regge slope M² = 2πσ(2n + L) against ρ-meson radial and orbital
trajectories. The two trajectories bracket the theoretical slope 1/(2πσ) = 0.884 GeV⁻².
For charmonium, the Cornell potential (−k/r + σr) reproduces level spacings within 1%
(S−P: 426 vs 429 MeV; 2S−1S: 588 vs 589 MeV).

### P16 — Unified Decay Mode Map
Predict the dominant decay mode for each nuclide using a single decision tree:
Bethe–Weizsäcker binding + Gamow α lifetime + fissility parameter. Score: 18/24
reference nuclides. α and β⁺ are perfect; boundary cases (magic numbers, quasi-stable)
escape the smooth model.

### P17 — Aharonov–Bohm Effect and Mesoscopic Rings
The topological ring-flux lever imposes periodicity Φ₀ = h/e on the spectrum.
The benzene aromatic gap closes at half-flux (confirming P12). Persistent current
and h/e oscillations are reproduced.

### P18 — Topological States of Matter
Quantum Hall: Hofstadter spectrum for flux 1/3, Chern numbers (1, −2, 1) quantizing
the Hall conductance. SSH: dimerized chain with protected edge zero-modes in the
topological phase (t₂ > t₁), none in the trivial phase.

### P19 — Diffuse Surface Bound
Transform the P9/P11 failure into a quantitative bound. A Fermi (Woods–Saxon)
density with diffusivity parameter `a` is fitted to 5 measured neutron skins.
The sharp-core model (a = 0) is insufficient; a ≈ 0.28 fm of surface diffusivity
is required. The failure becomes a measured bound.

### P20 — H₂⁺: The Only Exactly Solvable Molecule
H₂⁺ = 1 electron + 2 protons is the only molecular system solvable by a one-body
operator. LCAO-1s gives R_eq = 2.18 a₀ and D_e = 1.40 eV (order of magnitude).
The frontier is located: beyond H₂⁺, multi-electron correlation begins.

## Epistemic Stratification

All results are classified according to three strata:

- **S1 (Minimality)** — Measured anchors from spectral-triple minimality:
  `c/cs = 120`, `κR² = cs`, substrate benchmarks. These are inputs, not derived.
- **S2 (Preliminary notions)** — Historical data source (atomic mass audit, quantum
  18-ANU). Source material, held outside the proof device.
- **S3 (Off-corpus)** — Constitutive structure of the solver: Georgi–Glashow SU(2)+Higgs,
  functional C(ρ), Bogomolny bound, Dirac theorem. Chosen, not derived, and mapped
  by P0–P4 in the core repository.

## Repository Structure

```
noetic-applications/
├── docs/              # Case-study write-ups (Markdown)
├── src/               # Python solvers
├── data/              # Numerical results (JSON)
├── figures/           # Generated plots (PNG)
├── LICENSE            # MIT
├── README.md          # This file
└── requirements.txt   # Dependencies
```

## Quick Start

```bash
pip install -r requirements.txt
python src/p7_isotopes.py    # Chlorine isotope shifts
python src/p8_emc.py         # EMC mean-field vs SRC
python src/p9_prex.py        # PREX–CREX neutron skin (v4)
python src/p10_pont.py       # ANU bridge / periodic table
python src/p11_vallee.py     # Valley of stability
python src/p12_chimie.py     # Chemistry and valence
python src/p13_stabilite.py  # Stability: alpha decay + confinement
python src/p14_table.py      # Atomic identity cards H→U
python src/p15_hadrons.py    # Hadron spectrum: Regge + charmonium
python src/p16_modes.py      # Unified decay mode map
python src/p17_ab.py         # Aharonov–Bohm effect
python src/p18_topo.py       # Topological states
python src/p19_surface.py    # Diffuse surface bound
python src/p20_h2plus.py     # H₂⁺ molecular frontier
```

## Honest Reporting
P9 is published as a **negative result** with the same care as successes.
P11 and P16 are **partial successes** — form captured, fine boundaries escape.
P19 is a **diagnostic success** — failure transformed into a quantitative bound.
P20 locates the **many-body frontier** beyond which correlation is required.
No parameter was adjusted to force agreement.

## Dependencies
- `noetic-machine` (the core solver)
- `numpy`, `matplotlib`, `scipy`

## Citation
If you use these case studies, please cite the core repository:

```bibtex
@software{noetic_machine,
  author = {Portemann, Patrice},
  title = {Noetic Machine: A Non-Perturbative Finite-Core Solver},
  url = {https://github.com/PORTEMANN/noetic-machine},
  year = {2027}
}
```

## Contact
Patrice Portemann — [GitHub @PORTEMANN](https://github.com/PORTEMANN)
