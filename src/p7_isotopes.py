# P7 — Isotope Shifts in Chlorine
# Same Z, different A -> same point Coulomb, different finite core.
# The isotope shift is the PURE signature of the finite core (the point
# charge is identical for all isotopes). Chlorine 35/37.
# Finite charge = uniform sphere, R_c = r_0 A^(1/3).
# Verdict: isotope shift DeltaE_1s(37-35), and what the non-perturbative
# solver brings beyond perturbation theory.

import os, json
import numpy as np
from scipy.linalg import eigh_tridiagonal

ALPHA = 1.0 / 137.036
A0 = 137.036
MU = 207.0
R0FM = 1.2
CONV = 3.04 / 0.84
Z = 17
ISOTOPES = [("Cl35", 35), ("Cl36", 36), ("Cl37", 37), ("Cl40", 40)]


def Rc(A):
    return R0FM * A ** (1.0 / 3.0) * CONV


def Vfin(r, Rc_):
    out = np.empty_like(r)
    m = r >= Rc_
    out[m] = -Z * ALPHA / r[m]
    ri = r[~m]
    out[~m] = -Z * ALPHA / Rc_ * (1.5 - 0.5 * (ri / Rc_) ** 2)
    return out


def e1s(Rc_, m):
    a0z = A0 / (m * Z)
    RMAX = 60 * a0z
    NR = 40000
    r = np.linspace(RMAX / NR, RMAX, NR)
    dr = r[1] - r[0]
    diag = 1.0 / (m * dr**2) + Vfin(r, Rc_)
    off = -1.0 / (2 * m * dr**2) * np.ones(NR - 1)
    ev, _ = eigh_tridiagonal(diag, off, select="i", select_range=(0, 0))
    return float(ev[0]), a0z, dr


def delta_th(Rc_, m):
    # Perturbation theory: deltaE_size = (2/5) Z^4 alpha^4 m^3 R_c^2  (uniform sphere)
    return (2.0 / 5.0) * Z**4 * ALPHA**4 * m**3 * Rc_**2


res = {"Z": Z, "R0FM": R0FM, "CONV": CONV, "isotopes": {}}
for m, lab in [(1.0, "electronic"), (MU, "muonic")]:
    E = {}
    for name, A in ISOTOPES:
        e, a0z, dr = e1s(Rc(A), m)
        E[A] = e
        res["isotopes"].setdefault(name, {"A": A, "R_c": Rc(A)})[lab] = {
            "E1s": e,
            "a0": a0z,
        }
    # Isotope shift (the core alone moves)
    for a1, a2 in [(35, 37), (35, 36), (36, 37), (35, 40)]:
        shift = E[a2] - E[a1]
        shift_th = delta_th(Rc(a2), m) - delta_th(Rc(a1), m)
        key = f"shift_{a2}-{a1}_{lab}"
        res[key] = {
            "numerical": shift,
            "perturbation_theory": shift_th,
            "ratio": shift / shift_th if shift_th else None,
            "relative_to_E1s": shift / abs(E[a1]),
        }
        print(
            f"[P7 {lab:12}] shift {a2}-{a1} : num={shift:+.4e}  th={shift_th:+.4e}  "
            f"ratio={shift/shift_th:.3f}  rel={shift/abs(E[a1]):+.2e}",
            flush=True,
        )
    # Reference point Coulomb (Z=17): identical for all isotopes
    Ec = -Z * Z * ALPHA**2 * m / 2
    print(
        f"[P7 {lab:12}] E1s point Coulomb (Z=17) = {Ec:.6e}  (identical 35/36/37/40)",
        flush=True,
    )

out_path = os.path.join(os.path.dirname(__file__), "..", "data", "p7_isotopes.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(res, f, indent=1)
print("[P7] saved", flush=True)
