#!/usr/bin/env python3
"""Generate all figures for the case studies."""

import os
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def fig_p7():
    """P7 — Isotope shifts: numerical vs perturbation theory."""
    data = json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "p7_isotopes.json")))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    for ax, lab, title in zip(axes, ["electronic", "muonic"], ["Electronic", "Muonic"]):
        shifts = []
        labels = []
        for key, val in data.items():
            if key.startswith("shift_") and key.endswith(f"_{lab}"):
                pair = key.replace("shift_", "").replace(f"_{lab}", "")
                shifts.append(val["numerical"])
                labels.append(pair)
        x = np.arange(len(labels))
        ax.bar(x - 0.2, shifts, 0.4, label="numerical", color="steelblue")
        ax.bar(x + 0.2, [data[k]["perturbation_theory"] for k in data if k.startswith("shift_") and k.endswith(f"_{lab}")], 0.4, label="perturbation", color="coral")
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha="right")
        ax.set_ylabel("Shift (a.u.)")
        ax.set_title(f"P7 — {title} isotope shifts")
        ax.legend()
        ax.set_yscale("symlog")

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "p7_isotopes.png")
    plt.savefig(path, dpi=150)
    print(f"[fig] {path}")
    plt.close()


def fig_p8():
    """P8 — EMC effect: mean-field vs SRC modification."""
    data = json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "p8_emc.json")))
    fig, ax = plt.subplots(figsize=(7, 5))

    mf = data["mean_field"]
    src = data["src"]

    ax.plot([d["rho"] for d in mf], [d["modif_rel"] for d in mf], "o-", label="Mean-field", color="steelblue")
    ax.plot([d["d_over_Rc"] for d in src], [d["modif_rel"] for d in src], "s-", label="SRC (pair)", color="coral")
    ax.axhline(4.3, color="coral", ls="--", alpha=0.5, label="SRC saturation")
    ax.set_xlabel("Control parameter  (rho/rho0  or  d/Rc)")
    ax.set_ylabel("Relative modification of ground state")
    ax.set_title("P8 — EMC effect: mean-field vs SRC")
    ax.legend()
    ax.set_xscale("log")
    ax.set_yscale("log")
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "p8_emc.png")
    plt.savefig(path, dpi=150)
    print(f"[fig] {path}")
    plt.close()


def fig_p9():
    """P9 — PREX–CREX: neutron skin vs experiment."""
    data = json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "p9_prex.json")))
    fig, ax = plt.subplots(figsize=(6, 4))

    triplet = data["TRIPLET"]
    names = [d["name"] for d in triplet]
    skins = [d["skin_fm"] for d in triplet]
    exp = [0.121, 0.13, 0.283]  # CREX, RIKEN approx, PREX-II

    x = np.arange(len(names))
    ax.bar(x - 0.2, skins, 0.4, label="Solver (v4)", color="steelblue")
    ax.bar(x + 0.2, exp, 0.4, label="Experiment", color="coral")
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.set_ylabel("Neutron skin Δr_np (fm)")
    ax.set_title("P9 — PREX–CREX: solver vs data")
    ax.legend()
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "p9_prex.png")
    plt.savefig(path, dpi=150)
    print(f"[fig] {path}")
    plt.close()


if __name__ == "__main__":
    fig_p7()
    fig_p8()
    fig_p9()
    print("All figures generated.")
