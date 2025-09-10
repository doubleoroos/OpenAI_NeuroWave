import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Kuramoto-style oscillator demo
# -----------------------------

# Parameters
N = 50              # number of oscillators
timesteps = 500
dt = 0.05
K = 1.0             # internal coupling
gamma = 0.4         # crystal coupling strength
phi_c = 0.0         # crystal driver phase

# Natural frequencies
omega = np.random.normal(0, 0.2, N)

# Initialize phases
theta = np.random.uniform(0, 2*np.pi, N)

R_values = []

# Simulation loop
for t in range(timesteps):
    dtheta = omega + (K/N) * np.sum(np.sin(theta - theta[:, None]), axis=1) \
             + gamma * np.sin(phi_c - theta)
    theta += dtheta * dt

    # Coherence order parameter
    R = np.abs(np.mean(np.exp(1j * theta)))
    R_values.append(R)

# -----------------------------
# Plot results
# -----------------------------
plt.figure(figsize=(6,4))
plt.plot(R_values, label="Coherence R(t)")
plt.axhline(0.7, color='r', linestyle='--', label="Threshold R* = 0.7")
plt.xlabel("Time steps")
plt.ylabel("Coherence R")
plt.title("Kuramoto demo: Portal threshold")
plt.legend()
plt.tight_layout()
plt.show()
