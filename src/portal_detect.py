#!/usr/bin/env python3
import json, argparse, pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--threshold", type=float, default=0.6)
    ap.add_argument("--min_duration", type=int, default=30)
    ap.add_argument("--dt", type=float, default=None)
    ap.add_argument("--out", default="portal_window.json")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    R = df["R"].values
    dt = args.dt if args.dt is not None else float(df["t"].iloc[1]-df["t"].iloc[0])
    above = R >= args.threshold
    start, portal = None, None
    for i, f in enumerate(above):
        if f and start is None: start=i
        if not f and start is not None:
            if i-start>=args.min_duration: portal=(start,i-1); break
            start=None
    if portal is None and start is not None and len(R)-start>=args.min_duration:
        portal=(start,len(R)-1)
    out = {"start_idx": None if portal is None else int(portal[0]),
           "end_idx": None if portal is None else int(portal[1]),
           "R_max": float(R.max()), "dt": dt}
    with open(args.out, "w") as f: json.dump(out, f, indent=2)
    print(f"Wrote {args.out}")

if __name__=="__main__": main()

