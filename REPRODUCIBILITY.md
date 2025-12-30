# Reproducibility guide

## What you need
- Python 3.10+ recommended
- Jupyter Notebook or JupyterLab
- Public magnetogram data (NOAA / NSO-GONG) or your own local frames

## Quick start (pip)
1) Create and activate a virtual environment:
- macOS/Linux:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
- Windows:
  - `python -m venv .venv`
  - `.venv\Scripts\activate`

2) Install dependencies:
- `pip install -r requirements.txt`

3) Launch Jupyter:
- `jupyter lab`
  (or `jupyter notebook`)

4) Open and run:
- `DLSFH_Entropy_Diagnostic_NOAA.ipynb` (Run All)

## Expected outputs (canonical notebook)
When executed successfully, the notebook should generate:
- Node overlay / partition visualization (20-node DLSFH layout)
- Node-wise entropy values and ψ⋆s = exp(-S)
- Fragmentation map (ψ⋆s < ψcrit)
- Entropy ring detection result (adjacency-based)
- Composite risk score Rflare

## Notes on data inputs
- If the notebook pulls data from remote sources, ensure you have network access.
- If running offline, place magnetogram frames in the notebook’s expected input path and update the input configuration cell accordingly.

## Sensitivity checks
For parameter robustness:
- Run `DLSFH_PhysicsEntropy_Enhanced.ipynb`
- Use the parameter cells to vary:
  - ψcrit
  - minimum ring size
  - entropy histogram binning

## Troubleshooting
- If you see missing-package errors: re-run `pip install -r requirements.txt`
- If plots are blank: confirm notebook kernel is the same environment where packages were installed
- If files are not found: verify the configured input path and filenames
