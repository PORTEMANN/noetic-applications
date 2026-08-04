#!/usr/bin/env python3
# P13 -- Stability as form of the potential
# Slope 1: alpha radioactivity (finite barrier, Gamow tunnel effect)
# Slope 2: confinement (infinite barrier, flux tube, Regge)
import os, json
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
# natural constants (MeV, fm, s) -- hard-coded for clarity
HC = 197.3269804              # hbar.c in MeV.fm
C_LIGHT = 2.99792458e23       # c in fm/s
E2 = 1.4399645                # e^2/(4 pi eps0) in MeV.fm
R0 = 1.2                        # fm, anchor P6/P9/P11
M_AMU = 931.494                 # MeV/c^2
M_ALPHA = 3727.379              # MeV/c^2
ZALPHA = 2.0                    # alpha particle charge

# ---------------------------------------------------------------- slope 1
# alpha-emitting nuclei: (name, A_daughter, Z_daughter, E_alpha MeV, T1/2 measured in s)
ALPHA = [
    ("212Po",208,82,8.784, 2.99e-7),
    ("218Po",214,82,6.115, 0.186),
    ("216Po",212,82,6.906, 0.145),
    ("214Po",210,82,7.833, 1.64e-4),
    ("226Ra",222,86,4.784, 1.60e3*3.156e7),
    ("228Th",224,88,5.423, 1.912*3.156e7),
    ("230Th",226,88,4.687, 7.54e4*3.156e7),
    ("232Th",228,88,4.083, 1.40e10*3.156e7),
    ("235U",231,90,4.679, 7.04e8*3.156e7),
    ("238U",234,90,4.270, 4.468e9*3.156e7),
    ("241Pu",237,92,5.150, 14.3*3.156e7),
    ("244Cm",240,94,5.805, 18.1*3.156e7),
    ("252Cf",248,96,6.118, 2.645*3.156e7),
    ("148Gd",144,62,3.183, 70.9*3.156e7),
    ("151Eu",147,63,1.964, 4.62e18*3.156e7),
]

def gamow(A_d, Z_d, E):
    """Gamow factor G and T1/2: T = exp(-2G), T1/2 = ln2*Rc/(v*T)."""
    Rc = R0*A_d**(1/3.0)
    b = Z_d*ZALPHA*E2/E                     # outer turning point
    if b <= Rc: return Rc, b, 0.0, 0.0, 0.0
    mu = (M_ALPHA*M_AMU*A_d)/(M_ALPHA+M_AMU*A_d)   # reduced mass
    # closed WKB Coulomb integral: G = sqrt(2 mu V0 b) * [acos(sqrt x)-sqrt(x(1-x))] / hbar
    x = Rc/b
    arg = np.arccos(np.sqrt(x)) - np.sqrt(x*(1-x))
    V0 = Z_d*ZALPHA*E2                      # Z1 Z2 e^2 product (MeV.fm)
    G = np.sqrt(2*mu*V0*b)/HC*arg
    v = np.sqrt(2.0*E/M_ALPHA)*C_LIGHT    # alpha velocity in nucleus (fm/s)
    f = v/(2*Rc)                          # collision frequency (s^-1)
    # logarithmic space: log10(T1/2) direct, without ever computing exp(2G)
    log10_t12 = (np.log(np.log(2)) - np.log(f) + 2*G)/np.log(10)
    t12 = 10**log10_t12 if log10_t12 < 300 else np.inf
    return Rc, b, G, t12, log10_t12

rows=[]; xs=[]; ycalc=[]; ymes=[]
for nom,Ad,Zd,E,t in ALPHA:
    Rc,b,G,t12,l10 = gamow(Ad,Zd,E)
    x = Zd/np.sqrt(E)                  # Geiger-Nuttall variable
    lm=float(np.log10(t))
    rows.append(dict(nom=nom,A=Ad,Z=Zd,E=E,Rc=round(Rc,3),b=round(b,2),
                     G=round(G,4),t12_calc_s=float(f"{t12:.3e}"),
                     t12_mes_s=float(f"{t:.3e}"),
                     log10_calc=float(l10),log10_mes=lm,
                     ecart_log=float(l10-lm)))
    xs.append(x); ycalc.append(l10); ymes.append(lm)

xs=np.array(xs); ycalc=np.array(ycalc); ymes=np.array(ymes)
rms = float(np.sqrt(np.mean((ycalc-ymes)**2)))
med = float(np.median(ycalc-ymes))
# Geiger-Nuttall slope fitted on calculation (physical slope, not fitted to measurement)
pente_calc = float(np.polyfit(xs,ycalc,1)[0])
pente_mes  = float(np.polyfit(xs,ymes,1)[0])

res = {"constantes":{"hc_MeVfm":HC,"e2_MeVfm":E2,"r0_fm":R0,"m_alpha_MeV":M_ALPHA},
       "versant1_alpha":{"noyaux":rows,"rms_log10":rms,"decalage_median_log10":med,
                         "pente_calc":pente_calc,"pente_mes":pente_mes,
                         "ordres_de_grandeur_couvert":float(max(ymes)-min(ymes)),
                         "note":"absolute offset (preformation prefactor) is logged; "
                                "test is on slope and hierarchy"}}

# ---------------------------------------------------------------- slope 2
SIGMA = 0.18       # GeV^2, measured string tension
M_MESON = 0.775    # GeV, rho (lightest bound state of u-d string)
res["versant2_confinement"]={}

# 1) string breaking
r_casse = 2*M_MESON/SIGMA           # fm
sigma_GeVfm = SIGMA/0.197327        # GeV/fm
r_casse = 2*M_MESON/sigma_GeVfm
res["versant2_confinement"]["cassure"]=dict(
    sigma_GeV2=SIGMA, sigma_GeVfm=round(sigma_GeVfm,4),
    energie_cassure_GeV=round(2*M_MESON,3), distance_fm=round(r_casse,3),
    interpretation="string breaks when sigma*r reaches two-meson mass -> 2 mesons, no free quark")

# 2) Regge trajectories: spectrum of linear potential V = sigma r (s-wave, spin in J)
# model: M^2 = 2 pi sigma (n + J) + C -> slope 2 pi sigma
# radial spectrum of ultra-relativistic confined quark: E_n = sigma * x_n, x_n = zeros of Ai
ai_zeros = [2.3381,4.0879,5.5206,6.7867]  # -Ai zeros for linear well
# canonical Regge slope
alpha_p = 1/(2*np.pi*SIGMA)   # GeV^-2
res["versant2_confinement"]["regge"]=dict(
    pente_calculee_GeV_2=round(alpha_p,4), pente_mesuree_GeV_2=0.9,
    zeros_Ai=ai_zeros,
    interpretation="M^2 linear in J, slope 1/(2 pi sigma); "
            "with sigma=0.18 GeV^2 -> 0.884 GeV^-2, vs 0.9 measured")

# 3) linear well spectrum (radial masses, normalisation)
res["versant2_confinement"]["spectre_lineaire"]=dict(
    M2_n=[round(2*np.pi*SIGMA*(n+1),3) for n in range(4)],
    interpretation="M_n^2 = 2 pi sigma n (relativistic string)")

# ------------------------------------------------------------------ verdict
verdict = dict(
    geiger_nuttall_pente = bool(abs(pente_calc-pente_mes)/abs(pente_mes) < 0.15),
    hierarchie_20_ordres = bool((max(ymes)-min(ymes)) > 15),
    cassure_corde_calculee = bool(1.0 < r_casse < 2.0),
    regge_pente = bool(abs(alpha_p-0.9)/0.9 < 0.15))
res["verdict"]=verdict

out_path = os.path.join(OUT, "p13_stabilite.json")
os.makedirs(OUT, exist_ok=True)
with open(out_path, "w") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)

print(json.dumps(verdict, indent=1))
print(f"GN: {len(rows)} nuclei, {res['versant1_alpha']['ordres_de_grandeur_couvert']:.1f} orders, "
      f"slope calc {pente_calc:.2f} vs mes {pente_mes:.2f}, rms {rms:.2f} log")
print(f"break: {r_casse:.2f} fm | Regge: {alpha_p:.3f} vs 0.9")
print("worst deviations (log10):")
for r in sorted(rows,key=lambda z:-abs(z["ecart_log"]))[:4]:
    print(f"  {r['nom']:6s} E={r['E']:.3f}  calc {r['log10_calc']:7.2f}  mes {r['log10_mes']:7.2f}  ecart {r['ecart_log']:+.2f}")
print("[P13] saved to", out_path)
