# Noetic Applications — Case Studies on Experimental Data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Noetic Machine](https://img.shields.io/badge/noetic--machine-v1.0-blue)](https://github.com/PORTEMANN/noetic-machine)

> Applications of the Noetic non-perturbative solver to real experimental data:
> isotope shifts, EMC effect, and the PREX–CREX neutron-skin puzzle.

## Overview

This repository contains case studies applying the **Noetic Machine** (a non-perturbative
finite-core solver) to three well-defined problems in atomic and nuclear physics.
Each case includes:
- A documented problem statement with experimental anchors
- Python implementation (`src/`)
- Raw numerical results (`data/`)
- A verdict: success, instructive failure, or boundary located

## Case Studies

| # | Domain | Data | Result | Status |
|---|--------|------|--------|--------|
| **P7** | Atomic physics | ³⁵Cl/³⁷Cl isotope shift | Non-perturbative exact; perturbation theory fails by 18× | ✅ Success |
| **P8** | Nuclear physics | EMC effect (DIS, MARATHON) | SRC preferred over mean-field by form of modification | ✅ Success |
| **P9** | Nuclear physics | PREX-II, CREX, RIKEN ¹³²Sn | Good magnitude, wrong fine/thick switching; boundary located | ⚠️ Instructive failure |

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
python src/p7_isotopes.py   # Chlorine isotope shifts
python src/p8_emc.py        # EMC mean-field vs SRC
python src/p9_prex.py       # PREX–CREX neutron skin (v4)
```

## Honest Reporting

P9 is published as a **negative result** with the same care as successes.
The solver's boundary is located: discrete shell models fail to capture continuous
surface density. This is valuable knowledge. No parameter was adjusted to force
the switching.

## Dependencies

- `noetic-machine` (the core solver)
- `numpy`, `scipy`, `matplotlib`

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
