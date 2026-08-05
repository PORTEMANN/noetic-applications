# P31 — The r₁₂ Frontier Declared Constitutive

**Field:** Atomic / Quantum Chemistry / Foundations  
**Verdict:** ⚠️ Frontier Declared Constitutive (3/5 formal, 0/3 rules)

## Problem

Final test announced in P30: three entirely derived range constraints, zero parameter, tested on the kinematic factor u(r₁₂) = ½ r₁₂ e^(−βr₁₂) (Kato cusp imposed, factorization imposed at large distance).

## Three rules tested

| Rule (0 parameter) | β | E_min (Ha) | vs split-ζ −2.8347 |
|--------------------|---|-----------|-------------------|
| R1 — orbital scale: β = (a+b)/2 | 1.65 | −2.790 | worse by 0.045 |
| R2 — orthogonality: ⟨u′ cos θ₁₂⟩ = 0 | 2.53 | −2.821 | worse by 0.013 |
| R3 — density: ⟨r₁²⟩_ΨJ = ⟨r₁²⟩_Φ | 0.71 | −2.742 | worse by 0.092 |
| **β free** (diagnostic, grid edge) | ≥ 4 | −2.842 | **does not even reach** |
| Split-ζ alone (same integrator) | — | −2.835 | reference |
| Exact (Pekeris) | — | −2.9037 | |

## Reading

The three rules are physically distinct and all honest — and **orthogonality nearly touches the truth.** R2 (canceling the factor's leakage into the one-body sector) selects β = 2.53, close to the free edge, and loses only 0.013 Ha against split-ζ: it is the best, and its logic is that of the method. R3 (preserving density) imposes too soft a factor, R1 (orbital scale) too wide. The free diagnostic decides: energy wants the factor *extinguished* (β → ∞, J → 1). In this family, energy always prefers radial correlation alone.

## The failure is structural, not parametric

P30 had localized the problem in range; P31 closes it: even free, range does not save the family. The reason is visible in the local identity: the gain of 1/r₁₂ at contact is paid by the kinetic term u′² and by the crossing u′ cos θ₁₂ (a+b); at one term, these three contributions cannot simultaneously be good — the angular flexibility of a Hylleraas expansion (Σ c_nlm s^n t^l u^m) is needed, whose coefficients are *free parameters*. The method refuses this price.

**Consequence, published as bound not defeat:** the calculation's map has an exact frontier — everything discrete, kinematic and one-body is derivable (24 successes); the correlated continuous two-body response is not without form freedom. The failures P22 (Q_ββ magnitudes), P23 (quenching), P24 (gaps), P26/P29 (skins, shell) and P30–P31 all converge on this now-measured wall.

## Verdict

| Criterion | Result |
|-----------|--------|
| Contact derivable (cusp selected by energy, P30) | ✅ |
| Range not derivable | ✅ (published) |
| No single-term factor adds angular to radial | ✅ (published) |
| Three derived range rules tested | ✅ |
| Bound not crossed | ❌ (documented as constitutive frontier) |

## Document chain

- Script: `p31_portee.py`
- Data: `p31_portee.json`
- Figure: `p31_portee.png`
- Linked to: P27 (correlation), P28 (unification), P30 (cusp)
