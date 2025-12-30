# DLSFH Entropy & Coherence Diagnostics for Solar Flare and CME Risk

[![GitHub Repository](https://img.shields.io/badge/GitHub-dlsfh--entropy--rings--solar--risk-black?logo=github)](https://github.com/geopayme/AstroPhysics)
[![Zenodo DOI](https://img.shields.io/badge/Zenodo-DOI%20pending-blue?logo=zenodo)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/geopayme/AstroPhysics/blob/main/DLSFH_Entropy_Diagnostic_NOAA.ipynb
)

This release package accompanies the paper:

**_Entropy Rings and Fragmented Suns: A New Approach to Flare and CME Risk Detection_**  
Antonios Valamontes, Kapodistrian Academy of Science

It contains the computational materials required for **transparent, auditable reproduction** of the paper’s diagnostic framework: a 20-node DLSFH partition of solar magnetograms, localized Shannon entropy estimation, coherence amplitude $\psi^\star_s = \exp(-S)$, SGCV fragmentation detection, entropy-ring identification via the DLSFH adjacency graph, and the composite flare/CME risk score \(R_{\mathrm{flare}}\).

The repository is intended to support **method verification and qualitative robustness assessment**, not operational deployment.

---

## Contents

### Notebooks (source of truth)

### Notebooks (source of truth)

In this repository, “source of truth” denotes the authoritative computational implementations from which the figures, diagnostics, and numerical results reported in the paper are generated. All analyses shown in the manuscript can be reproduced directly by executing these notebooks; derived figures or summaries should be treated as secondary to the notebook outputs.

The canonical analysis notebooks are hosted in the associated GitHub repository:

1. `DLSFH_Entropy_Diagnostic_NOAA.ipynb` — **Primary reproducibility pipeline**  
2. `DLSFH_PhysicsEntropy_Enhanced.ipynb` — **Sensitivity / robustness exploration**  
3. `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL_5.ipynb` — **Extended physics interpretation (exploratory)**

Because this ZIP is designed to be portable, it includes a **manifest** and a **fetch script** to retrieve the latest notebook copies from GitHub when internet access is available:

- `manifest/notebooks.json`  
- `tools/fetch_notebooks.py`

---

## Execution order

- **Reproduce the paper’s core results:** `DLSFH_Entropy_Diagnostic_NOAA.ipynb`  
- **Sensitivity & robustness:** `DLSFH_PhysicsEntropy_Enhanced.ipynb`  
- **Exploratory theory (optional):** `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL_5.ipynb`

See `RUN_ORDER.md` for details.

---

## Environment requirements

- Python 3.10+  
- Jupyter Notebook or JupyterLa
