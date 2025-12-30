# DLSFH Entropy & Coherence Diagnostics for Solar Flare and CME Risk

This release package accompanies the paper:

**_Entropy Rings and Fragmented Suns: A New Approach to Flare and CME Risk Detection_**  
Antonios Valamontes, Kapodistrian Academy of Science

It contains the computational materials required for **transparent, auditable reproduction** of the paper’s diagnostic framework: a 20-node DLSFH partition of solar magnetograms, localized Shannon entropy estimation, coherence amplitude  
$\psi^\star_s = \exp(-S)$,
SGCV fragmentation detection, entropy-ring identification via the DLSFH adjacency graph, and the composite flare/CME risk score $\(R_{\mathrm{flare}}\)$.

The repository is intended to support **method verification and qualitative robustness assessment**, not operational deployment.

---

## Contents

### Notebooks (source of truth)

The canonical analysis notebooks are hosted in the associated GitHub repository:

1. `DLSFH_Entropy_Diagnostic_NOAA.ipynb` — **Primary reproducibility pipeline**  
   End-to-end implementation of the entropy–coherence diagnostic: node partitioning, entropy extraction, coherence computation, fragmentation and entropy-ring detection, and risk scoring.

2. `DLSFH_PhysicsEntropy_Enhanced.ipynb` — **Sensitivity / robustness exploration**  
   Parameter variation (e.g., coherence threshold, entropy binning) and qualitative stability checks.

3. `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL_5.ipynb` — **Extended physics interpretation (exploratory)**  
   Non-operational analyses motivated by the DLSFH/SGCV framework; not required to reproduce the core diagnostic results.

Because this ZIP is designed to be portable, it includes a **manifest** and a **fetch script** to retrieve the latest notebook copies from GitHub when internet access is available:

- `manifest/notebooks.json`  
- `tools/fetch_notebooks.py`

---

## Execution order

Recommended notebook execution order depends on intent:

- **Reproduce the paper’s core results:**  
  Run `DLSFH_Entropy_Diagnostic_NOAA.ipynb`.

- **Examine sensitivity and robustness:**  
  Then run `DLSFH_PhysicsEntropy_Enhanced.ipynb`.

- **Explore extended theoretical interpretation (optional):**  
  Run `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL_5.ipynb`.

A concise execution guide is provided in `RUN_ORDER.md`.

---

## Environment requirements

- Python 3.10+ recommended  
- Jupyter Notebook or JupyterLab  
- Standard scientific Python stack

Two environment specifications are provided:

- `requirements.txt` — pip-based installation  
- `environment.yml` — Conda-based installation (optional)

Step-by-step reproduction instructions and expected outputs are documented in `REPRODUCIBILITY.md`.

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
