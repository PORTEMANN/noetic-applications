# P8 — EMC Effect: Is the bound nucleon a deformed core?
# The nucleon = finite core of charge (R_c = r_0 A_n^(1/3)). Its "effective partons"
# are bound states INSIDE the core (well of the charge sphere). The structure-function
# analogue = distribution of these states (proportional to binding energies / effective
# well depth). The EMC modification = change of this spectrum when the core is bound
# to an environment.
#
# Two regimes (discriminant test):
#   (a) MEAN-FIELD: the core is immersed in a mean field of density rho
#       (uniform extra well, depth V_mf ~ rho). Modification of ALL nucleons,
#       ~ density, isotropic, saturates at heavy nuclei.
#   (b) SRC: the core is bound to ONE neighbour at short distance d (pair).
#       Well of two overlapping spheres. Modification only of paired nucleons,
#       ~ 1/d, isospin-dependent (np dominant), active from A=3.
# Verdict: which form reproduces the measured EMC slope and its dependence (A, isospin)?

import os, json
import numpy as np
from scipy.linalg import eigh_tridiagonal

ALPHA = 1.0 / 137.036
A0 = 137.036
CONV = 3.04 / 0.84
# The nucleon = core of charge Z_n=1, radius Rc_n = r_p (proton) -> 3.04 lattice units.
# "effective partons" = bound states of the core: internal well of the charge sphere.
Z_N = 1
RC_N = 3.04


def Vsphere(r, Rc_, Zc):
    out = np.empty_like(r)
    m = r >= Rc_
    out[m] = -Zc * ALPHA / r[m]
    ri = r[~m]
    out[~m] = -Zc * ALPHA / Rc_ * (1.5 - 0.5 * (ri / Rc_) ** 2)
    return out


def spectrum_partons(Veff, m=1.0, NR=20000, RMAX=None):
    """Spectrum of bound states (effective partons) in well Veff."""
    if RMAX is None:
        RMAX = 60 * A0
    r = np.linspace(RMAX / NR, RMAX, NR)
    dr = r[1] - r[0]
    diag = 1.0 / (m * dr**2) + Veff
    off = -1.0 / (2 * m * dr**2) * np.ones(NR - 1)
    ev, _ = eigh_tridiagonal(diag, off, select="i", select_range=(0, 5))
    return ev


# --- FREE core (reference) ---
r = np.linspace(60 * A0 / 20000, 60 * A0, 20000)
V_libre = Vsphere(r, RC_N, Z_N)
E_libre = spectrum_partons(V_libre)
prof_libre = -E_libre[0]  # binding depth of ground state (proxy mean "x")
print(
    f"[P8] free core: parton ground = {E_libre[0]:.6e}  (depth={prof_libre:.6e})",
    flush=True,
)

# --- (a) MEAN-FIELD: mean field of density rho -> uniform well V_mf ---
# V_mf proportional to nuclear density; sweep rho in units of rho0.
res_mf = []
for rho in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
    V_mf = -rho * 0.05 * Z_N * ALPHA / RC_N  # mean well ~ density, core scale
    V = Vsphere(r, RC_N, Z_N) + V_mf
    E = spectrum_partons(V)
    modif = (E[0] - E_libre[0]) / E_libre[0] if E_libre[0] != 0 else 0
    res_mf.append({"rho": rho, "E0": float(E[0]), "modif_rel": float(modif)})
    print(f"[P8 MF ] rho={rho:4.2f} : E0={E[0]:+.6e}  modif={modif:+.4f}", flush=True)

# --- (b) SRC: short-distance pair at distance d -> two overlapping spheres ---
# The nucleon is bound to ONE neighbour at distance d (in units of core radius).
res_src = []
for d_over_Rc in [100, 20, 8, 4, 3, 2.5, 2.2, 2.0]:
    d = d_over_Rc * RC_N
    # Potential of the other sphere seen from the first (z axis): cylindrical
    # average approximation -> add the neighbour's well centred at r=d.
    rr = np.abs(r - d)
    rr = np.maximum(rr, r[0])
    Vpair = Vsphere(rr, RC_N, Z_N)
    V = Vsphere(r, RC_N, Z_N) + Vpair
    E = spectrum_partons(V)
    modif = (E[0] - E_libre[0]) / E_libre[0] if E_libre[0] != 0 else 0
    res_src.append(
        {"d_over_Rc": d_over_Rc, "E0": float(E[0]), "modif_rel": float(modif)}
    )
    print(
        f"[P8 SRC] d/Rc={d_over_Rc:5.1f} : E0={E[0]:+.6e}  modif={modif:+.4f}",
        flush=True,
    )

out_path = os.path.join(os.path.dirname(__file__), "..", "data", "p8_emc.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(
        {
            "Z_N": Z_N,
            "RC_N": RC_N,
            "E_libre": E_libre.tolist(),
            "mean_field": res_mf,
            "src": res_src,
        },
        f,
        indent=1,
    )
print("[P8] saved", flush=True)
