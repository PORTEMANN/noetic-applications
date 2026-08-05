# P30 — The Kato Cusp

**Field:** Atomic / Quantum Chemistry  
**Verdict:** ⚠️ Partial Success (3/5)

## Problem

Is the two-body response derivable? First test: impose the Kato cusp as a *kinematic constraint* (value 1/2 derived from 1/r₁₂ divergence, zero free parameter) in a saturating factor u(r) = c r/(1+r).

## Results

| Configuration | E (Ha) | % of HF→exact gap |
|---------------|--------|-------------------|
| HF (1-body bound) | −2.8477 | 0 |
| Split-ζ P27 (MC) | −2.8485 | 51.5 |
| Jastrow smooth P28 (c_opt = 0) | — | 44.3 |
| Cusp saturated c = 1/2, Φ HF fixed | −2.793 | ~57 |
| Cusp saturated, (a,b) re-optimized | −2.793 (1.73, 1.73) | 197* |
| Exact (Pekeris) | −2.9037 | 100 |

*Percentage misleading: the comparison point is the *best* bound (−2.8485), which the result does not cross.

## Key finding

The cusp works at *fixed* Φ, and *reverses* at free Φ: when (a,b) are free, the two-body factor *replaces* radial correlation instead of adding to it. The global minimum prefers (1.73, 1.73), symmetric, without inner-outer screening. Angular and radial correlations are not additive in a fixed-range trial function: they compete.

## Failures (documented)

1. **Bound not improved:** −2.793 > −2.8485 (P27) — variational criterion C1 fails.
2. **Lever inverted:** at optimized (a,b), c_opt = 0 — consequence of (1), not independent signal.
3. **Cause:** saturating factor range fixed at 1 a₀; imposing cusp 1/2 *at all distances* over-correlates the pair at large separation, where the true correlation factor vanishes.

## Reading

The cusp is necessary but not sufficient; the kinematic constraint fixes only contact, not range. Freeing range would cure energy but reintroduce an adjusted parameter — exactly the betrayal the method refuses. The result is not confused, it is clear: **the cusp is derivable, the range is not; no single-term factor adds angular to radial.**

## Verdict

| Criterion | Result |
|-----------|--------|
| Control validated | ✅ |
| Capture > 55% at fixed Φ | ✅ |
| Zero parameter | ✅ |
| P27 bound crossed | ❌ |
| Lever inverted at free Φ | ❌ |

## Document chain

- Script: `p30_cusp.py`
- Data: `p30_cusp.json`
- Figure: `p30_cusp.png`
- Linked to: P27 (correlation), P28 (unification)
