# Execution order (Entropy Rings / DLSFH notebooks)

This repository contains three notebooks. Use the order below depending on your goal.

## A. Reproduce the paper’s core diagnostic outputs (recommended)
1. `DLSFH_Entropy_Diagnostic_NOAA.ipynb`
   - End-to-end pipeline: partition → entropy → ψ⋆s → fragmentation → ring detection → Rflare
   - Produces the primary fragmentation maps, ring overlays, ψ⋆s trends, and risk score outputs.

## B. Sensitivity & robustness checks (thresholds / binning)
2. `DLSFH_PhysicsEntropy_Enhanced.ipynb`
   - Parameter sweeps (e.g., ψcrit, ring size), entropy binning effects, trend stability.

## C. Extended / exploratory theoretical interpretation (non-operational)
3. `DLSFH_PhysicsEntropy_AdvancedFinal_FINAL_5.ipynb`
   - Exploratory analysis and interpretive visualizations motivated by DLSFH/SGCV framing.
   - Not required for reproducing the operational diagnostic outputs.
