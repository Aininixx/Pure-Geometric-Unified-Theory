#!/usr/bin/env python3
"""
Purely Geometric Recursive Summation of the Electron Anomalous Magnetic Moment
Paper 3 of the Pure Geometric Unified Theory series.
Derives the fine-structure constant and electron anomalous magnetic moment
from pure geometry with zero free parameters.
"""

import math

PI = math.pi

# Geometric constants
sigma = math.sqrt(1.0 + PI)
delta_chi2 = (1.0 + PI) / (PI**2)
alpha = 1.0 / (4.0 * PI**3 + PI**2 + PI)

# First-order dilution
d_mu = sigma * (1.0 + PI / 2.0)  # muon rooting depth
denom0 = PI**3 + d_mu  # dilution benchmark
f_s3_0 = 1.0 - delta_chi2 / denom0  # first-order dilution factor

# First-order result
r_0 = (alpha / 2.0) * delta_chi2 * f_s3_0
a_e_0 = (alpha / (2.0 * PI)) / (1.0 + r_0)

# Self-consistent second-order refinement
delta = 1.0 - f_s3_0
denom = denom0 - delta
f_s3 = 1.0 - delta_chi2 / denom

# Recursion factor and magnetic moment
r = (alpha / 2.0) * delta_chi2 * f_s3
a_e = (alpha / (2.0 * PI)) / (1.0 + r)

print("=" * 50)
print("Electron Anomalous Magnetic Moment: Geometric Recursive Summation")
print("=" * 50)
print(f"Geometric alpha   = {alpha:.15f}")
print(f"Wave packet width sigma = {sigma:.10f}")
print(f"Angular spread Deltachi^2 = {delta_chi2:.10f}")
print("-" * 50)
print(f"First-order dilution benchmark denom0 = pi^3 + d_mu = {denom0:.8f}")
print(f"First-order dilution factor f_S3^(0) = {f_s3_0:.8f}")
print(f"First-order recursion factor r_0 = {r_0:.10f}")
print(f"First-order a_e = {a_e_0:.15f}")
print(
    f"First-order deviation = {abs(a_e_0 - 0.00115965218046) / 0.00115965218046 * 1e9:.3f} ppb"
)
print("-" * 50)
print(f"Self-consistent refinement delta = 1 - f_S3^(0) = {delta:.8f}")
print(f"Second-order dilution benchmark denom = denom0 - delta = {denom:.8f}")
print(f"Second-order dilution factor f_S3 = {f_s3:.8f}")
print(f"Second-order recursion factor r = {r:.10f}")
print(f"Second-order a_e = {a_e:.15f}")
print(f"Experimental value   = 0.001159652180460")
print(
    f"Second-order deviation = {(a_e - 0.00115965218046) / 0.00115965218046 * 1e9:.3f} ppb"
)
print("=" * 50)
