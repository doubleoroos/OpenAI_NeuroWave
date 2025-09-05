# OpenAI_NeuroWave

What if AI didn’t need a keyboard, a screen, or even a computer, but could interface directly with the biological signals of the human body?

## NeuroWave — Quickstart

See our [Devpost page](https://devpost.com/software/neurowave-biological-signal-ai-without-a-computer?ref_content=user-portfolio&ref_feature=in_progress) for full details.

## Elevator Pitch

**NeuroWave turns the human body into the interface, translating biological signals into AI-powered insight—no computer required.**

---

## How We Used gpt-oss

- **Input:** Evidence JSON (`max_R`, `portal window`, `frequency`, `dt`)
- **Model:** `openai/gpt-oss-120b` via Hugging Face Router
- **Output:** Deterministic analysis + next-parameter suggestion (JSON)

## Built With

Python, NumPy, Matplotlib, OpenAI gpt-oss-120b, Hugging Face Router API, JSON, Three.js, Local GPU Deployment, GitHub

---

## 📂 Project Structure

```
.
├── demo/
├── output/
├── main.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 📈 Visuals

<!-- Add a screenshot, diagram, or gif here to showcase results or setup -->
<!--
![Sample plot](output/R_plot.png)
-->

---

## 🚀 Quick Start

To quickly get started with NeuroWave:

```bash
pip install -r requirements.txt
export HF_TOKEN=hf_your_token_here
bash demo/run_demo.sh           # Online (HF Router)
# Or fully offline (no token needed):
bash demo/run_demo_offline.sh
```

---

## ⚙️ CI/CD Workflow & Artifacts

This repository uses a GitHub Actions workflow to automatically run a Python script and upload artifacts (such as plots) for every push or pull request to the `main` branch.

### Automated workflow

- Installs dependencies from `requirements.txt`
- Runs `main.py` (which generates a simple plot of a sine wave)
- Uploads the results (`R_plot.png` and the `output/` folder) as artifacts

Artifacts can be found in the Actions tab after a successful workflow run.

### Run the script locally

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

---

## 🤝 Contributing

To update the README.md or contribute:

```bash
git add README.md
git commit -m "Update README.md"
git push
```

---

## 📬 Contact & Support

- See [Devpost](https://devpost.com/software/neurowave-biological-signal-ai-without-a-computer?ref_content=user-portfolio&ref_feature=in_progress) for more info
- Ask questions or get support via [GitHub Issues](https://github.com/doubleoroos/OpenAI_NeuroWave/issues)

---

## 🪪 License

Distributed under the MIT License. See `LICENSE` for details.
