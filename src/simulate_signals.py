#!/usr/bin/env python3
import argparse, json
import numpy as np, pandas as pd

def coherence(theta):
    z = np.exp(1j*theta).mean()
    return float(np.abs(z))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--N", type=int, default=144)
    ap.add_argument("--freqs", type=float, nargs="+", default=[0.6, 2.4])
    ap.add_argument("--gamma", type=float, default=0.9)
    ap.add_argument("--steps", type=int, default=1200)
    ap.add_argument("--dt", type=float, default=0.02)
    ap.add_argument("--noise", type=float, default=0.015)
    ap.add_argument("--out", type=str, default="demo/demo_R_series.csv")
    ap.add_argument("--portal_out", type=str, default="demo/portal_window.json")
    ap.add_argument("--threshold", type=float, default=0.6)
    ap.add_argument("--min_duration", type=int, default=30)
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    omega0 = 2*np.pi*args.freqs[0]
    omega = omega0 + 0.08 * rng.standard_normal(args.N)
    theta = rng.uniform(-np.pi, np.pi, size=args.N)
    R_series = np.empty(args.steps, dtype=float)
    t_series = np.arange(args.steps) * args.dt

    def driver_phase(t, freqs):
        sig = np.mean(np.sin(2*np.pi*np.asarray(freqs)*t))
        sig = np.clip(sig, -0.999999, 0.999999)
        return np.arctan2(sig, np.sqrt(1 - sig*sig))

    for n in range(args.steps):
        t = n * args.dt
        phi_c = driver_phase(t, args.freqs)
        drive = np.sin(phi_c - theta)
        eta = args.noise * rng.standard_normal(args.N)
        dtheta = omega + args.gamma * drive + eta
        theta = (theta + args.dt * dtheta + np.pi) % (2*np.pi) - np.pi
        R_series[n] = coherence(theta)

    pd.DataFrame({"t": t_series, "R": R_series}).to_csv(args.out, index=False)

    thr, min_len = args.threshold, args.min_duration
    above = R_series >= thr
    start, portal = None, None
    for i, f in enumerate(above):
        if f and start is None: start = i
        if not f and start is not None:
            if i - start >= min_len: portal=(start,i-1); break
            start=None
    if portal is None and start is not None and len(R_series)-start>=min_len:
        portal=(start,len(R_series)-1)
    out_portal = {"start_idx": None if portal is None else int(portal[0]),
                  "end_idx": None if portal is None else int(portal[1]),
                  "R_max": float(R_series.max()), "dt": args.dt}
    with open(args.portal_out, "w") as f: json.dump(out_portal, f, indent=2)
    print(f"Wrote {args.out} and {args.portal_out}")

if __name__ == "__main__":
    main()

