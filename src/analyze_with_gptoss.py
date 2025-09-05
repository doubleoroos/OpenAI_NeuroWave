#!/usr/bin/env python3
import os, json, argparse, sys

def offline_analysis(ev):
    start = ev.get("start_idx")
    end = ev.get("end_idx")
    dt = ev.get("dt", 0.02)
    duration = None if (start is None or end is None) else (end - start) * dt
    out = {
        "analysis": {
            "max_R": round(float(ev.get("R_max", 0.0)), 3),
            "portal_window": None if duration is None else [round(start*dt,3), round(end*dt,3)],
            "optimal_frequency": 2.4 if float(ev.get("R_max",0)) >= 0.6 else 0.6,
            "confidence": 0.9 if float(ev.get("R_max",0)) >= 0.6 else 0.6
        },
        "recommendation": "Increase coupling K by 0.05 and retest" if float(ev.get("R_max",0)) < 0.6 else "Sweep gamma by +0.05"
    }
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--model", default="openai/gpt-oss-120b:fireworks-ai")
    ap.add_argument("--router", default="https://router.huggingface.co/v1")
    ap.add_argument("--out", default="demo/demo_evidence.json")
    ap.add_argument("--offline", action="store_true", help="Skip API; produce deterministic analysis from evidence.")
    args = ap.parse_args()

    with open(args.evidence) as f:
        ev = json.load(f)

    if args.offline:
        out = offline_analysis(ev)
        with open(args.out, "w") as f: json.dump(out, f, indent=2)
        print(f"[offline] Wrote {args.out}")
        return

    try:
        from openai import OpenAI
    except Exception as e:
        print("ERROR: openai package not available. Try: pip install openai", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr); sys.exit(1)

    api_key = os.environ.get("HF_TOKEN")
    if not api_key:
        print("ERROR: HF_TOKEN is not set. Export your Hugging Face token.", file=sys.stderr); sys.exit(1)

    client = OpenAI(base_url=args.router, api_key=api_key)
    sys_prompt = "You are a scientific data analyst. Output JSON only. No extra text."
    user = json.dumps({"evidence": ev, "task":"summarize and suggest next parameters (frequency, K, gamma)."})
    try:
        resp = client.chat.completions.create(
            model=args.model,
            messages=[{"role":"system","content":sys_prompt},{"role":"user","content":user}],
            response_format={"type":"json_object"}
        )
    except Exception as e:
        print("ERROR calling HF Router / OpenAI-compatible endpoint.", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        print("Tip: run with --offline to bypass API for testing.", file=sys.stderr); sys.exit(1)

    out = resp.choices[0].message.content
    try:
        parsed = json.loads(out)
    except Exception:
        parsed = out
    with open(args.out, "w") as f:
        if isinstance(parsed, str): f.write(parsed)
        else: json.dump(parsed, f, indent=2)
    print(f"Wrote {args.out}")

if __name__=="__main__":
    main()

