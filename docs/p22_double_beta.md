# P22 — Double-Beta Decay (2νββ)

**Field:** Nuclear / Particle Physics  
**Verdict:** ⚠️ Partial Success (5/6)

## Problem

P16 (decay mode map) had failed on magic nuclei. P22 probes the enriched criterion: double-beta decay, which exists only where simple beta decay is blocked.

**Inputs:** same Bethe–Weizsäcker coefficients as P16 (nothing adjusted), Q_β and Q_ββ computed from BW masses.

## What is derived

- **Mechanism:** all known 2νββ emitters are even-even (9/9) — explained by pairing creating a mass parabola shift that pushes the odd-odd intermediate above the even-even initial.
- **Discriminating lever:** without the pairing term, the criterion selects nothing (0/9). Pairing is necessary — proved by internal control.
- **Signs of Q_ββ:** 9/9 positive.
- **Phase scaling:** T₁/₂ ~ Q⁻⁷·², compatible with the 2ν phase-space reference Q⁻¹¹.

## Failures (published)

1. **Magnitudes:** Q_ββ from BW are overestimated by +2.6 MeV on average; only 3/9 pass within 1.5 MeV. Largest errors at ⁴⁸Ca (doubly magic), ¹³⁰Te, ¹³⁶Xe (N = 82 region) — the same shell-model failures as P16/P29.
2. **False positives:** ¹²⁰Sn and ¹³⁸Ba (magic) are incorrectly selected.
3. **Lifetime spread:** at fixed Q, measured T₁/₂ span ~30× around the trend — this is the nuclear matrix element, the two-body response.

## Verdict

| Criterion | Result |
|-----------|--------|
| Mechanism derived | ✅ |
| Lever discriminating | ✅ |
| Signs 9/9 | ✅ |
| False positives localized (magic) | ✅ |
| Phase scaling trend | ✅ |
| Magnitudes Q_ββ sufficient | ❌ (documented) |

## Document chain

- Script: `p22_doublebeta.py`
- Data: `p22_doublebeta.json`
- Figure: `p22_doublebeta.png`
- Linked to: P16 (decay map), P19/P29 (shell boundary)
