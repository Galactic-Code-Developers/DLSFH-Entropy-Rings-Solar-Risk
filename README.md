# DLSFH Entropy & Coherence Diagnostics for Solar Flare and CME Risk

This release package accompanies the paper:

**_Entropy Rings and Fragmented Suns: A New Approach to Flare and CME Risk Detection_**  
Antonios Valamontes, Kapodistrian Academy of Science

It contains the computational notebooks and metadata required for **transparent, auditable reproduction** of the paper’s diagnostics: a 20-node DLSFH partition, localized Shannon entropy, coherence amplitude \(\psi_s^\star=\exp(-S)\), fragmentation detection, entropy-ring detection via the adjacency graph, and the composite risk score \(R_{\mathrm{flare}}\).

## Contents

### Notebooks (source of truth)
The canonical notebooks live in the GitHub repository:

1. `DLSFH_Entropy_Diagnostic_NOAA.ipynb` — **Primary reproducibility pipeline**  
2. `DLSFH_PhysicsEntropy_Enhanced.ipynb` — **Sensitivity/robustness exploration**  
3. `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL_5.ipynb` — **Extended physics interpretation (exploratory)**

Because this ZIP is intended to be portable, it includes a **manifest** and a **fetch script** to pull the latest notebook copies from GitHub when you have internet access.

- `manifest/notebooks.json`
- `tools/fetch_notebooks.py`

## Quick start

1. Create a fresh environment (example):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Fetch notebooks from GitHub:
   ```bash
   python tools/fetch_notebooks.py
   ```

3. Open and run:
   - `notebooks/DLSFH_Entropy_Diagnostic_NOAA.ipynb`

## Zenodo archiving workflow (recommended)

1. Create a GitHub Release (e.g., `v1.0.0`).
2. Connect the repository to Zenodo (GitHub → Zenodo integration).
3. Trigger an archive by publishing the release.
4. Add the resulting DOI to:
   - `zenodo.json` (this package)
   - the paper’s Reproducibility section

## Citation

See:
- `CITATION.cff`
- `zenodo.json`

## License

See `LICENSE`.

## Contact

Antonios Valamontes  
Kapodistrian Academy of Science  
Email: avalamontes@Kapodistrian.edu.gr
