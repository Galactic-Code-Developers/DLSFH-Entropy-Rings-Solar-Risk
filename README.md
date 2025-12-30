# DLSFH Entropy & Coherence Diagnostics for Solar Flare and CME Risk

[![GitHub Repository](https://img.shields.io/badge/GitHub-dlsfh--entropy--rings--solar--risk-black?logo=github)](https://github.com/geopayme/AstroPhysics)
[![Zenodo DOI](https://img.shields.io/badge/Zenodo-DOI%20pending-blue?logo=zenodo)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/geopayme/AstroPhysics/blob/main/DLSFH_Entropy_Diagnostic_NOAA.ipynb
)

This repository accompanies the paper:

**_Entropy Rings and Fragmented Suns: A New Approach to Flare and CME Risk Detection_**  
Antonios Valamontes, Kapodistrian Academy of Science

It contains the computational materials required for **transparent, auditable reproduction** of the paper’s diagnostic framework: a 20-node DLSFH partition of solar magnetograms, localized Shannon entropy estimation, coherence amplitude $\psi^\star_s = \exp(-S)$, SGCV fragmentation detection, entropy-ring identification via the DLSFH adjacency graph, and the composite flare/CME risk score $\(R_{\mathrm{flare}}\)$.

The repository supports **method verification, qualitative robustness assessment, and exploratory interpretation**. It is not an operational forecasting system.

---

## Contents

### Notebooks (source of truth)

In this repository, **“source of truth”** denotes the authoritative computational implementations from which the figures, diagnostics, and numerical results reported in the paper are generated.

#### Core reproducibility and analysis

1. `DLSFH_Entropy_Diagnostic_NOAA.ipynb`  
   **Canonical end-to-end pipeline**: magnetogram partitioning, entropy extraction, coherence computation, fragmentation detection, entropy-ring identification, and risk scoring.

2. `DLSFH_Entropy_AutoAnalysis_Patched.ipynb`  
   Automated batch-style execution of the entropy–coherence pipeline with patched robustness handling. Used for repeated frame analysis and consistency checks.

3. `Complete_DLSFH_Dual_Overlay_Test.ipynb`  
   Validation notebook demonstrating geometric alignment between DLSFH node placement and NOAA active-region overlays.

#### Sensitivity, robustness, and interpretation

4. `DLSFH_PhysicsEntropy_Enhanced.ipynb`  
   Sensitivity and robustness exploration (coherence threshold variation, entropy binning effects, node-level trend stability).

5. `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL.ipynb`  
   Exploratory and interpretive analysis motivated by the DLSFH/SGCV framework. Not required to reproduce operational diagnostics.

---

## Execution order

Recommended execution order depends on intent:

### Reproduce the paper’s core results
1. `DLSFH_Entropy_Diagnostic_NOAA.ipynb`

### Validate geometry and overlays
2. `Complete_DLSFH_Dual_Overlay_Test.ipynb`

### Automated or repeated analyses
3. `DLSFH_Entropy_AutoAnalysis_Patched.ipynb`

### Sensitivity and robustness
4. `DLSFH_PhysicsEntropy_Enhanced.ipynb`

### Exploratory theoretical interpretation (optional)
5. `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL.ipynb`

See `RUN_ORDER.md` for concise guidance.

---

## Environment requirements

- Python 3.10+  
- Jupyter Notebook or JupyterLab  
- Standard scientific Python stack

Environment specifications:
- `requirements.txt` (pip)
- `environment.yml` (conda, optional)

Step-by-step instructions and expected outputs are documented in `REPRODUCIBILITY.md`.

---

## Data sources

All analyses rely on **publicly available solar magnetogram data**, including NOAA and NSO/GONG products. No proprietary datasets are required.

---

## Citation and archiving

Formal citation metadata and archival information are provided in:

- `CITATION.cff`
- `zenodo.json`

A versioned Zenodo DOI is minted upon release to ensure long-term traceability.

---

## License

See `LICENSE`.

---

## Contact

Antonios Valamontes  
Kapodistrian Academy of Science  
Email: avalamontes@Kapodistrian.edu.gr
