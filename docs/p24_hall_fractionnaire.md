# P24 — Fractional Quantum Hall Effect (Jain Sequence)

**Field:** Condensed Matter Physics  
**Verdict:** ✅ Success (6/6)

## Problem

Can the Jain sequence ν = n/(2pn ± 1) — and its conjugate 1 − ν — be derived from two ingredients already locked: the flux quantum Φ₀ = h/e (P17) and the integer Chern number σ = Ce²/h (P18)?

## Derivation

In the lowest Landau level, the only scale is l_B and dynamics is frozen. Attach 2p flux quanta to each electron. The composite fermion sees reduced field:

B* = B − 2p n Φ₀  →  ν* = ν/(1 − 2pν)

Requiring the integer Chern number from P18 for composite fermions, ν* = n, gives without any new parameter:

**ν = n/(2pn ± 1)** and its particle-hole conjugate 1 − ν.

## Results

| Observed fraction | Jain assignment | In sequence |
|-------------------|-----------------|-------------|
| 1/3, 2/5, 3/7, 4/9, 5/11 | n/(2n+1), p=1 | ✓ |
| 2/3, 3/5, 4/7, 5/9 | conjugates 1−ν | ✓ |
| 1/5, 2/7 | n/(4n+1), p=2 | ✓ |
| **Coverage** | | **11/11** |

**Gap hierarchy** along branch n/(2n+1): 1/3 : 0.10 → 2/5 : 0.033 → 3/7 : 0.013 — monotonically decreasing with denominator, as required by B* = B/(2n+1).

## Key theorems from the bench

1. **Statistics constrain flux parity:** exchanging two particles around q flux quanta adds phase e^(iπq). Preserving fermion statistics requires q *even*, hence denominator 2pn ± 1 is necessarily *odd*.
2. **ν = 1/2 is gapless:** B* = 0 → composite fermion Fermi sea, no plateau. No even denominator is producible.
3. **Without attachment (p = 0):** only integers are derived — no fractions.

## Failures (localized)

1. **Gap magnitudes:** direction (Δ decreases with q) is derived, but measured slope (~q⁻²·⁴) requires composite fermion mass — a two-body response.
2. **ν = 5/2 plateau:** observed, but has *even* denominator — outside the mechanism, requires composite fermion pairing.

## Verdict

| Criterion | Result |
|-----------|--------|
| Statistics ⇒ q even | ✅ |
| Jain sequence derived, no parameter | ✅ |
| Coverage 11/11 observed | ✅ |
| Gap hierarchy direction | ✅ |
| ν = 1/2 gapless discriminant | ✅ |
| Lever without attachment negative | ✅ |

## Document chain

- Script: `p24_jain.py`
- Data: `p24_jain.json`
- Figure: `p24_jain.png`
- Linked to: P17 (flux quantum), P18 (Chern integer), P28 (two-body response)
