#!/usr/bin/env python3
import argparse, pandas as pd, json
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--portal", required=True)
    ap.add_argument("--out", default="demo/R_plot.png")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    with open(args.portal) as f:
        portal = json.load(f)

    t = df["t"].values
    R = df["R"].values

    plt.figure()
    plt.plot(t, R)
    if portal.get("start_idx") is not None:
        i0, i1 = portal["start_idx"], portal["end_idx"]
        plt.axvspan(t[i0], t[i1], alpha=0.15)
    plt.xlabel("time (s)"); plt.ylabel("R (coherence)")
    plt.title("Coherence over time"); plt.savefig(args.out, dpi=180, bbox_inches="tight")
    print(f"Wrote {args.out}")

if __name__=="__main__": main()

