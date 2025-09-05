# OpenAI_NeuroWave
What if AI didn’t need a keyboard, a screen, or even a computer but could interface directly with the biological signals of the human body?
# NeuroWave — Quickstart

See Devpost for full details.

## Elevator Pitch
**NeuroWave turns the human body into the interface — translating measurable biological signals into AI-driven insight, no computer required.**

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
