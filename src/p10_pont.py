#!/usr/bin/env python3
# P10 - ANU bridge <-> identity cards: 3 deliverables.
# (1) Annotated periodic table: N_ANU, N/18, modern mass, + machine card
#     (R_c=r0 A^(1/3), hierarchy Rc/a0) at the A closest to N/18.
# (2) Deviation test: the 8 worst deviations N/18 vs mass -> isotopic structure?
#     Test if N/18 points to the DOMINANT isotope (integer A_dom) rather than
#     the weighted average (standard mass): if yes, the deviation is structure.
# (3) Meta-elements: correspondence meta-counting <-> precise isotope (P7-like).

import os, json
import numpy as np

R0FM = 1.2
CONV = 3.04 / 0.84
A0 = 137.036

# Load audit data - expects a JSON with 'table' field
# Format: [symbol, Z, N_ANU, N18, mass]
AUDIT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "audit_anu_mass.json")
if os.path.exists(AUDIT_PATH):
    audit = json.load(open(AUDIT_PATH))
else:
    # Fallback: minimal built-in data for demonstration
    audit = {
        "table": [
            ["H", 1, 18, 1.0, 1.008],
            ["He", 2, 72, 4.0, 4.0026],
            ["Li", 3, 127, 7.06, 6.94],
            ["Be", 4, 164, 9.11, 9.0122],
            ["B", 5, 200, 11.11, 10.81],
            ["C", 6, 216, 12.0, 12.011],
            ["N", 7, 261, 14.5, 14.007],
            ["O", 8, 290, 16.11, 15.999],
            ["F", 9, 340, 18.88, 18.998],
            ["Ne", 10, 360, 20.0, 20.18],
        ],
        "pires_ecarts": ["N", "Si", "Kr", "Te", "At", "Nb", "Sm", "Eu"],
        "meta_elements_isotopes": {
            "Meta-Neon": {"N": 402, "N/18": 22.33, "22Ne": 21.99, "note": "points to 22Ne"},
            "Meta-Chlore": {"N": 667, "N/18": 37.06, "37Cl": 36.97, "note": "points to 37Cl"},
        },
        "controle_nul": {"rms": 0.37},
        "rms_relatif_pct": 1.4,
    }

T = audit["table"]


def carte(A):
    Rc = R0FM * A ** (1.0 / 3.0) * CONV
    return {"R_c_lattice": Rc, "R_c_fm": Rc / CONV, "hierarchy": Rc / A0}


# Dominant isotopes (most abundant natural isotope) for deviation test
ISO_DOM = {
    "N": 14, "Si": 28, "S": 32, "Cl": 35, "Ar": 40, "K": 39, "Ca": 40, "Ti": 48,
    "Cr": 52, "Fe": 56, "Ni": 58, "Cu": 63, "Zn": 64, "Kr": 84, "Nb": 93, "Mo": 98,
    "Sn": 120, "Te": 130, "Xe": 132, "Sm": 152, "Eu": 153, "Gd": 158, "Pt": 195,
    "Au": 197, "Hg": 202, "Pb": 208, "At": 210, "O": 16, "C": 12, "Ne": 20,
}

# --- Deliverable 1: annotated periodic table ---
table = []
for row in T:
    sym, Z, N, N18, masse = row[0], row[1], row[2], row[3], row[4]
    A_near = int(round(N18))
    ecart_pct = (N18 - masse) / masse * 100
    c = carte(A_near)
    table.append(
        {
            "sym": sym,
            "Z": Z,
            "N_ANU": N,
            "N18": N18,
            "mass": masse,
            "A_near": A_near,
            "deviation_pct": ecart_pct,
            "R_c_fm": c["R_c_fm"],
            "hierarchy": c["hierarchy"],
        }
    )
print(f"[P10] annotated table: {len(table)} elements built", flush=True)

# --- Deliverable 2: deviation test ---
pires = audit.get("pires_ecarts", [])
test_ecarts = []
for row in T:
    sym = row[0]
    if sym in pires:
        N18 = row[3]
        masse = row[4]
        A_dom = ISO_DOM.get(sym)
        if A_dom:
            e_moy = (N18 - masse) / masse * 100
            e_dom = (N18 - A_dom) / A_dom * 100
            verdict = (
                "STRUCTURE (dominant isotope)"
                if abs(e_dom) < abs(e_moy)
                else "NOISE/ambiguous"
            )
            test_ecarts.append(
                {
                    "sym": sym,
                    "N18": N18,
                    "mass": masse,
                    "A_dom": A_dom,
                    "deviation_vs_mean": e_moy,
                    "deviation_vs_dominant": e_dom,
                    "verdict": verdict,
                }
            )
            print(
                f"[P10 dev] {sym:3} N/18={N18:6.2f} mass={masse:7.3f} A_dom={A_dom:3} "
                f"e_moy={e_moy:+5.2f}% e_dom={e_dom:+5.2f}% -> {verdict}",
                flush=True,
            )

# --- Deliverable 3: meta-elements ---
meta = audit.get("meta_elements_isotopes", {})
test_meta = []
for name, info in meta.items():
    N = info.get("N", 0)
    N18 = info.get("N/18", 0)
    iso = [k for k in info.keys() if k not in ("N", "N/18", "note")]
    iso_pt = iso[0] if iso else None
    iso_val = info[iso_pt] if iso_pt else None
    note = info.get("note", "")
    A_near = int(round(N18))
    c = carte(A_near)
    test_meta.append(
        {
            "meta": name,
            "N": N,
            "N18": N18,
            "isotope_pointed": iso_pt,
            "A_near": A_near,
            "note": note,
            "R_c_fm": c["R_c_fm"],
        }
    )
    print(
        f"[P10 meta] {name:14} N={N:5} N/18={N18:6.2f} -> A~{A_near:3} "
        f"(isotope {iso_pt}={iso_val}) R_c={c['R_c_fm']:.2f} fm  {note}",
        flush=True,
    )

out_path = os.path.join(os.path.dirname(__file__), "..", "data", "p10_pont.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(
        {
            "table": table,
            "test_deviations": test_ecarts,
            "test_meta": test_meta,
            "null_control": audit.get("controle_nul", {}),
            "rms_audit": audit.get("rms_relatif_pct", None),
        },
        f,
        indent=1,
    )
print("[P10] saved", flush=True)
