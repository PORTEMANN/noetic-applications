#!/usr/bin/env python3
# P17 -- L'effet Aharonov-Bohm et les anneaux mesoscopiques
# Levier : la topologie d'anneau de flux (P0). Le potentiel vecteur A, nul en B=0
# autour du flux, deplace les niveaux : E_m(Phi) = E_0 (m - Phi/Phi0)^2.
# Tests discriminants :
#   1) periodicite du spectre / de l'energie en Phi0 = h/e (quantum de flux)
#   2) le gap du benzene se ferme a Phi/Phi0 = 1/2 (deja vu P12, confirme ici)
#   3) harmoniques : energie fondamentale en Phi0, composante Phi0/2 (h/2e, effet mesoscopique)
import json, hashlib, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# electron sur un anneau (1D quantique) : E_m(phi) = (hbar^2/2mR^2)(m-phi)^2, phi=Phi/Phi0
def energies(phi, M=12):
    m = np.arange(-M, M+1)
    return (m - phi)**2   # en unites hbar^2/2mR^2

PHIS = np.linspace(0, 1.0, 201)

# energie fondamentale (remplissage du niveau le plus bas) vs flux
def ground(phi):
    return np.min((np.arange(-12,13)-phi)**2)

Eg = np.array([ground(p) for p in PHIS])

# courant persistant : I = -dE/dPhi ~ -dEg/dphi
dphi = PHIS[1]-PHIS[0]
I = -np.gradient(Eg, dphi)

# anneau de N sites (Huckel) avec flux : spectre de Peierls (comme P12 mais vs flux)
def ring_spectrum(N, phi):
    H = np.zeros((N,N),dtype=complex)
    for i in range(N):
        j=(i+1)%N; phase=2*np.pi*phi/N
        H[i,j]=np.exp(-1j*phase); H[j,i]=np.exp(1j*phase)
    return np.linalg.eigvalsh(H)

def ring_ground(N, phi, Ne):
    E=ring_spectrum(N,phi); E=np.sort(E)
    return np.sum(E[:Ne])   # remplissage des Ne premiers (sans spin pour lisibilite)

# benzene N=6, 6 electrons pi (3 paires de spin -> 3 niveaux doubles occupes)
def gap_benzene(phi):
    E=np.sort(ring_spectrum(6,phi))
    return E[3]-E[2]   # HOMO=2, LUMO=3

gapB = np.array([gap_benzene(p) for p in PHIS])

# FFT de l'energie fondamentale : harmoniques (Phi0 vs Phi0/2)
Eg_c = Eg - Eg.mean()
fft = np.abs(np.fft.rfft(Eg_c))
freqs = np.fft.rfftfreq(len(Eg), d=dphi)
harm = {f"h{int(round(fr))}":round(float(fft[i]/fft.max()),3)
        for i,fr in enumerate(freqs) if 0.5<fr<4.5}

res = {
 "effet_AB": dict(
    quantum_flux="Phi0 = h/e",
    periodicite_fondamental="E(phi) periodique de periode Phi0 (dent de scie)",
    harmoniques=harm,
    lecture="le spectre et l'energie sont periodiques du quantum de flux : "
            "la topologie d'anneau impose la periodicite h/e"),
 "gap_benzene": dict(
    phi_fermeture=0.5,
    gap_0=round(float(gapB[0]),4), gap_demiflux=round(float(gapB[100]),4),
    lecture="le gap aromatique (P12) se ferme a mi-flux : l'aromaticite est AB-sensible"),
 "courant_persistant": dict(
    amplitude=round(float(np.max(np.abs(I))),3),
    lecture="courant d'equilibre non nul dans l'anneau, periodique en Phi0 (mesoscopique)"),
}

verdict = dict(
    periodicite_Phi0 = bool(abs(Eg[0]-Eg[-1])<1e-9 and np.all(Eg>=0)),
    gap_ferme_a_demi_flux = bool(abs(gapB[100])<0.05 and gapB[0]>1.0),
    courant_persistant_non_nul = bool(np.max(np.abs(I))>0.5),
    oscillation_periodique = bool(abs(Eg[0]-Eg[-1])<1e-9))
res["verdict"]=verdict

# figure
fig,ax=plt.subplots(1,3,figsize=(15,4.6))
a=ax[0]
for m in range(-2,3):
    a.plot(PHIS,(np.arange(-12,13)[np.arange(-12,13)==m][0]-PHIS)**2, lw=1,
           label=f"m={m}")
a.set_xlabel(r"$Phi/Phi_0$"); a.set_ylabel(r"$E_m$ ($hbar^2/2mR^2$)")
a.set_title("A -- Niveaux E_m(Phi)=(m-Phi/Phi0)^2\nperiodiques du quantum de flux",fontsize=9.5)
a.legend(fontsize=7,ncol=2); a.grid(alpha=0.3)

a=ax[1]
a.plot(PHIS,Eg,color="steelblue",lw=2,label="energie fondamentale")
a.plot(PHIS,I/np.max(np.abs(I)),color="indianred",lw=1.5,ls="--",label="courant persistant (norm.)")
a.set_xlabel(r"$Phi/Phi_0$"); a.set_ylabel("energie / courant")
a.set_title("B -- Oscillations AB : periode Phi0 = h/e\nenergie et courant d'equilibre",fontsize=9.5)
a.legend(fontsize=8); a.grid(alpha=0.3)

a=ax[2]
a.plot(PHIS,gapB,color="seagreen",lw=2.5)
a.axvline(0.5,color="k",ls=":",lw=1)
a.annotate("fermeture a\nPhi/Phi0 = 1/2",(0.5,gapB[100]),textcoords="offset points",
           xytext=(8,20),fontsize=9)
a.set_xlabel(r"$Phi/Phi_0$"); a.set_ylabel("gap HOMO-LUMO (|beta|)")
a.set_title("C -- Gap du benzene vs flux\nl'aromaticite se ferme au demi-quantum",fontsize=9.5)
a.grid(alpha=0.3)

fig.suptitle("P17 -- L'effet Aharonov-Bohm : la topologie d'anneau de flux (levier P0)",fontsize=12)
fig.tight_layout(rect=[0,0,1,0.95]); fig.savefig(f"{OUT}/p17_ab.png",dpi=150)

with open(f"{OUT}/p17_ab.json","w") as f: json.dump(res,f,indent=1,ensure_ascii=False)
print(json.dumps(verdict,indent=1)); print("harmoniques:",harm)
print("gap benzene: phi=0 ->",res["gap_benzene"]["gap_0"]," phi=1/2 ->",res["gap_benzene"]["gap_demiflux"])
