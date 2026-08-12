#!/usr/bin/env python3
"""
Purely Geometric Origin of Gauge Coupling Constants
Paper 1 of the Pure Geometric Unified Theory series.
Calculates all geometric constants and gauge couplings from first principles.
Zero free parameters.
"""

import math

PI = math.pi

# ------------------------------------------------------------
# 0. Fundamental geometric constants
# ------------------------------------------------------------

# Coding sphere radius (radians)
R = PI

# Wave packet width (coding cost of dimensional reduction spray)
sigma = math.sqrt(1.0 + PI)

# Angular spread squared
delta_chi2 = (1.0 + PI) / (PI**2)

# ------------------------------------------------------------
# 1. Triple projections (information capacities in bits)
# ------------------------------------------------------------

# 1st eternal rotation: full 3D sphere surface
projection_3D = 4.0 * PI**3  # electromagnetic U(1) boundary

# 2nd eternal rotation: broken 2D arc (half circumference)
projection_2D = PI**2  # weak SU(2) cage

# 3rd eternal rotation: 1D line segment
projection_1D = PI  # strong SU(3) confining string

# ------------------------------------------------------------
# 2. Gauge coupling constants (bare values)
# ------------------------------------------------------------

# Fine-structure constant (electromagnetic U(1))
alpha = 1.0 / (4.0 * PI**3 + PI**2 + PI)

# Weak coupling (SU(2))
alpha_W = 1.0 / (PI**3)

# Strong coupling bare (SU(3))
alpha_s_bare = 1.0 / (PI**2)

# ------------------------------------------------------------
# 3. Weinberg angle (bare)
# ------------------------------------------------------------

sin2_thetaW_bare = (PI**3) / (4.0 * PI**3 + PI**2 + PI)

# ------------------------------------------------------------
# 4. Output all results
# ------------------------------------------------------------

print("=" * 60)
print("Purely Geometric Origin of Gauge Coupling Constants")
print("=" * 60)
print(f"Coding sphere radius R    = {R:.15f} rad")
print(f"Wave packet width σ       = {sigma:.10f}")
print(f"Angular spread (Δχ)²      = {delta_chi2:.10f}")
print("-" * 60)
print("Triple Projections (information capacities):")
print(f"  1st rotation (3D sphere) : {projection_3D:.6f} bits")
print(f"  2nd rotation (2D arc)    : {projection_2D:.6f} bits")
print(f"  3rd rotation (1D segment): {projection_1D:.6f} bits")
print("-" * 60)
print("Gauge Coupling Constants (bare):")
print(f"  α (U(1) EM)   = {alpha:.15f}")
print(f"  1/α           = {1.0/alpha:.10f}")
print(f"  α_W (SU(2))   = {alpha_W:.10f}  (~ 1/{1.0/alpha_W:.1f})")
print(f"  α_s bare (SU(3)) = {alpha_s_bare:.6f}")
print("-" * 60)
print("Weinberg Angle (bare):")
print(f"  sin²θ_W(bare) = {sin2_thetaW_bare:.6f}")
print(f"  θ_W(bare)     = {math.degrees(math.asin(math.sqrt(sin2_thetaW_bare))):.3f}°")
print("-" * 60)
print("Comparison with experiment:")
print(f"  α (CODATA 2018)        = 1/137.035999084")
print(f"  α (this theory, bare)  = 1/{1.0/alpha:.10f}")
print(f"  α_W (exp, mZ scale)     ~ 1/30")
print(f"  α_s (exp, mZ scale)    ~ 0.118")
print(f"  sin²θ_W (exp, mZ scale) ~ 0.23122")
print("=" * 60)
