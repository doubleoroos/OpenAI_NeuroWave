# OpenAI_NeuroWave
What if AI didn’t need a keyboard, a screen, or even a computer but could interface directly with the biological signals of the human body?
# NeuroWave — Quickstart

See Devpost for full details.

## Elevator Pitch
**NeuroWave turns the human body into the interface, translating measurable biological signals into AI-driven insight, no computer required.**

## How We Used gpt-oss
- Input: Evidence JSON (`max_R`, `portal window`, `frequency`, `dt`).
- Model: `openai/gpt-oss-120b` via Hugging Face Router.
- Output: Deterministic analysis + next-parameter suggestion (JSON).

## Built With
Python, NumPy, Matplotlib, OpenAI gpt-oss-120b, Hugging Face Router API, JSON, Three.js, Local GPU Deployment, GitHub

## Quick Start
```bash
pip install -r requirements.txt
export HF_TOKEN=hf_your_token_here
bash demo/run_demo.sh           # online (HF Router)
# or fully offline (no token needed):
bash demo/run_demo_offline.sh

## CI/CD Workflow & Artifact Example

This repository uses a GitHub Actions workflow to automatically run a Python script and upload artifacts (such as plots) for every push or pull request to the `main` branch.

### Automated workflow

- The workflow installs dependencies from `requirements.txt`.
- It runs `main.py` (which generates a simple plot of a sine wave).
- It uploads the results (`R_plot.png` and the `output/` folder) as artifacts with every build.

Artifacts can be found in the Actions tab after a successful workflow run.

### Run the script locally

To run the script yourself:

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the script:
    ```bash
    python main.py
    ```
3. You will find `R_plot.png` in the root directory and in the `output/` folder.

---

*See `.github/workflows/ci.yml` for workflow details.*
