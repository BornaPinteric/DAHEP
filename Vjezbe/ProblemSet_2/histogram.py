import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def transform(pt, eta, phi):
    px = pt * np.cos(phi)
    py = pt * np.sin(phi)
    pz = pt * np.sinh(eta)
    E = pt * np.cosh(eta)
    return E, px, py, pz

def inv_mass(pt, eta, phi):
    px = pt * np.cos(phi)
    py = pt * np.sin(phi)
    pz = pt * np.sinh(eta)
    E = pt * np.cosh(eta)

    E_sum = ak.sum(E, axis=1)
    px_sum = ak.sum(px, axis=1)
    py_sum = ak.sum(py, axis=1)
    pz_sum = ak.sum(pz, axis=1)

    m2 = E_sum**2 - px_sum**2 - py_sum**2 - pz_sum**2

    return np.sqrt(m2)

def plot_mass_hist(mass, title, bins=50):
    plt.figure(figsize=(8, 6))

    plt.hist(mass, bins=bins, histtype="step", linewidth=1.5)

    plt.xlabel("m [MeV]")
    plt.ylabel("# of hits")
    plt.title(title)
    title = title.replace(" ", "_")

    plt.grid(alpha=0.3)
    plt.tight_layout()

    output_path = Path(__file__).resolve().parent / f"{title}.png"
    plt.savefig(output_path, dpi=300)

    plt.close()

    print(f"Histogram saved to: {output_path}")

file = uproot.open("ggH125_ZZ4lAnalysis.root")

tree = file["ZZTree/candTree"]

data = tree.arrays(["LepPt", "LepEta", "LepPhi"], library="ak")

pt = data["LepPt"]
eta = data["LepEta"]
phi = data["LepPhi"]

N_events = len(pt)

mass_H = ak.to_numpy(inv_mass(pt, eta, phi))
mass_Z1 = ak.to_numpy(inv_mass(pt[:, 0:2], eta[:, 0:2], phi[:, 0:2]))

plot_mass_hist(mass_H, "Mase H bozona")
plot_mass_hist(mass_Z1, "Mase prvog Z bozona")