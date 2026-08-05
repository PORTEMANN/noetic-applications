# P17 — Aharonov–Bohm Effect and Mesoscopic Rings

## Problem
Exploit the topological ring-flux lever (P0) on mesoscopic systems. Discriminating tests:
1. Periodicity of spectrum in Φ₀ = h/e
2. Benzene gap closes at Φ/Φ₀ = 1/2 (P12 confirmed)
3. Persistent current, h/e oscillations

## Method
- **1D ring**: E_m(Φ) = (ℏ²/2mR²)(m − Φ/Φ₀)²
- **Hückel ring (Peierls)**: hopping phases exp(±2πiΦ/NΦ₀)
- **Benzene N=6**: HOMO-LUMO gap vs flux

## Results

| Test | Result | Criterion |
|------|--------|-----------|
| Periodicity | E(0) = E(Φ₀), dent de scie | ✓ |
| Gap closure | 2|β| → 0 at Φ/Φ₀ = 1/2 | ✓ |
| Persistent current | Non-zero, sawtooth | ✓ |
| h/e oscillations | Fundamental h₁ = 1.0, harmonics h₂, h₃, h₄ | ✓ |

## Verdict
✅ **Success**

## Files
- `src/p17_ab.py` — solver
- `data/p17_ab.json` — AB spectrum, persistent current, benzene gap
