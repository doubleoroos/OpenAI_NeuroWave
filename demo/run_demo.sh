#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."
mkdir -p demo
python src/simulate_signals.py --out demo/demo_R_series.csv --portal_out demo/portal_window.json
python src/analyze_with_gptoss.py --evidence demo/portal_window.json --out demo/demo_evidence.json
python src/visualize_coherence.py --csv demo/demo_R_series.csv --portal demo/portal_window.json --out demo/R_plot.png
echo "Done. Outputs in ./demo"

