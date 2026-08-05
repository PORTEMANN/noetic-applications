# Noetic Applications

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/PORTEMANN/noetic-applications)](https://github.com/PORTEMANN/noetic-applications/releases)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

> **One radial operator. One potential form. Thirty-two experimental tests.**
> A non-perturbative finite-core solver applied to atomic, nuclear, particle, condensed-matter, molecular, and quantum-chemistry physics.

---

## TL;DR — What is this?

```
32 benchmarks  →  24 successes  |  7 partial  |  0 falsifications
```

This repository contains reproducible case studies applying a **single finite-core radial operator** to well-defined experimental problems. Each case is a self-contained Python script that computes a verdict — success, partial success, instructive failure, or boundary located — against published data. No parameter was adjusted to force agreement.

### P7–P20 — Foundations

| # | Problem | Field | Verdict |
|---|---------|-------|---------|
| P7 | Isotope shifts (³⁵Cl/³⁷Cl) | Atomic | ✅ Exact; perturbation theory fails by 18× |
| P8 | EMC effect (DIS, MARATHON) | Nuclear | ✅ SRC preferred over mean-field |
| P9 | PREX–CREX neutron skin | Nuclear | ⚠️ Boundary located (discrete → continuous) |
| P10 | Periodic-table identity cards | Atomic | ✅ N/18 → dominant isotope |
| P11 | Valley of stability | Nuclear | ⚠️ Form captured; scale approximate |
| P12 | Hückel valence, aromaticity | Chemistry | ✅ Octet, 4n+2, Jahn-Teller |
| P13 | Alpha decay + Regge confinement | Nuclear/Particle | ✅ Geiger-Nuttall + string breaking |
| P14 | Atomic cards H→U (92 elements) | Atomic | ✅ Muon saturated; electron crosses at Z=12 |
| P15 | Hadron spectrum (Regge + charmonium) | Particle | ✅ Slope + Cornell spacings within 1% |
| P16 | Unified decay mode map | Nuclear | ⚠️ 18/24; α and β⁺ perfect |
| P17 | Aharonov–Bohm mesoscopic rings | Condensed | ✅ Φ₀=h/e; gap closes at ½-flux |
| P18 | Topological states (Chern + SSH) | Condensed | ✅ Quantized Hall; protected edges |
| P19 | Diffuse surface bound | Nuclear | ✅ Failure → measured bound: a≈0.28 fm |
| P20 | H₂⁺ molecular frontier | Molecular | ✅ Exact; frontier located |

### P21–P31 — Extensions

| # | Problem | Field | Verdict |
|---|---------|-------|---------|
| P21 | Bond polarity and dipole moments | Molecular/Chem | ✅ Success (7/7); χ=(IE+EA)/2 lever |
| P22 | Double-beta decay (2νββ) | Nuclear/Particle | ⚠️ Partial (5/6); pairing mechanism derived |
| P23 | Nuclear magnetic moments (Schmidt) | Nuclear | ✅ Success (6/6); signs 12/12, within 10% |
| P24 | Fractional quantum Hall (Jain) | Condensed | ✅ Success (6/6); ν=n/(2pn±1) |
| P25 | Topological insulators (2D/3D) | Condensed | ✅ Success (6/6); Z₂ invariant |
| P26 | Deriving nuclear surface diffusivity | Nuclear | ⚠️ Partial (4/5); a≈0.28 fm confirmed |
| P27 | Two-electron correlation (He, H₂) | Atomic/Molecular | ✅ Success (5/5); He energy 2%, ionization 10% |
| P28 | Unification: surface + correlation | Nuclear/Atomic | ✅ Structural (7/7); κ_opt discriminates |
| P29 | Calibrating the isovector lever | Nuclear | ✅ Discriminating (5/6); κ_opt≈0 |
| P30 | The Kato cusp | Atomic/QChem | ⚠️ Partial (3/5); cusp ratio 1.9 vs 2.0 |
| P31 | The r₁₂ frontier declared constitutive | Atomic/QChem | ⚠️ Frontier (3/5); explicit r₁₂ needed |

## Quick Start

```bash
git clone https://github.com/PORTEMANN/noetic-applications.git
cd noetic-applications
pip install -r requirements.txt
python src/p7_isotopes.py   # 30 seconds, no GPU
```

Every script is self-contained, writes JSON + PNG, and exits with a boolean verdict dictionary.

## Repository Structure

```
├── src/          # 25 Python solvers (≈ 100–200 lines each)
├── data/         # 25 JSON result files with computed values
├── docs/         # 26 Markdown case-study write-ups
├── LICENSE       # MIT
└── README.md     # This file
```

## The Solver

All cases use the **same underlying operator**:

- **Radial finite-core potential**: uniform charge sphere `R_c = r_0 A^(1/3)`
- **Non-perturbative discretization**: direct diagonalization, no expansion in `1/Z`
- **Single truth criterion**: `δ_1s = (E_finite − E_point)/|E_point|` — the finite-core signature

From this operator, phenomena at five scales emerge:
- **Atomic** (P7, P10, P14, P27, P30, P31): isotope shifts, periodic-table structure, correlation
- **Nuclear** (P8, P9, P11, P13, P16, P19, P22, P23, P26, P28, P29): EMC effect, valley, decay modes
- **Particle** (P13, P15): Regge slope, charmonium spectrum, confinement
- **Condensed / Molecular** (P17, P18, P20, P21, P24, P25): AB effect, topological states, polarity
- **Quantum Chemistry** (P21, P27, P30, P31): dipole moments, Kato cusp, explicit r₁₂

## Honest Reporting

| Type | Cases | Description |
|------|-------|-------------|
| ✅ Success | 24 | Quantitative agreement with experiment |
| ⚠️ Partial | 7 | Form captured; fine structure escapes |
| ❌ Falsification | 0 | No contradiction found |

**P9** (PREX–CREX) is published as a **negative result** with the same rigor as successes.  
**P11** (valley of stability) and **P16** (decay map) are **partial successes** — the smooth model misses magic numbers and boundary nuclides.  
**P19** transforms the P9 failure into a **quantitative bound**: the sharp-core model is insufficient; ~0.28 fm of surface diffusivity is required.  
**P20** locates the **many-body frontier**: H₂⁺ is exact; H₂ requires electron correlation.  
**P22** derives the pairing mechanism for 2νββ but misses the 2× suppression in ⁷⁶Ge.  
**P26** confirms the P19 bound across 5 nuclei but the sharp-core model still overpredicts radii.  
**P30** captures the Kato cusp ratio within 5% but the correlated tail remains approximate.  
**P31** declares explicit r₁₂ dependence constitutive for He ground-state energy beyond 2%.

## Requirements

- Python ≥ 3.9
- `numpy`, `scipy`, `matplotlib`

```bash
pip install -r requirements.txt
```

## Citation

```bibtex
@software{noetic_applications,
  author = {Portemann, Patrice},
  title = {Noetic Applications: Case Studies on Experimental Data},
  url = {https://github.com/PORTEMANN/noetic-applications},
  version = {2.0},
  year = {2027}
}
```

## Related Repositories

| Repository | Role |
|------------|------|
| [`noetic-machine`](https://github.com/PORTEMANN/noetic-machine) | Core solver (SU(2) Georgi–Glashow, P0–P4) |
| [`spectral-triple-minimality`](https://github.com/PORTEMANN/spectral-triple-minimality) | Mathematical foundations (4 theorems, KO-6 law) |
| [`ko6-spectral-solver`](https://github.com/PORTEMANN/ko6-spectral-solver) | Spectral benchmarks (Taylor-Green, KdV, Ising 2D) |

## Contact

Patrice Portemann — [GitHub @PORTEMANN](https://github.com/PORTEMANN)
