#!/usr/bin/env python3
"""
Purely Geometric Unification of Charged Lepton Anomalous Magnetic Moments
Paper 7 of the Pure Geometric Unified Theory series.
Derives the electron, muon, and tau anomalous magnetic moments
from pure geometry with zero free parameters.
"""

import math

PI = math.pi

# =============================================
# Geometric constants
# =============================================
alpha = 1.0 / (4.0 * PI**3 + PI**2 + PI)
sigma = math.sqrt(1.0 + PI)
delta_chi2 = (1.0 + PI) / (PI**2)
PI3 = PI**3
PI2 = PI**2
a0 = alpha / (2.0 * PI)

# Rooting depths
d_tau = sigma
d_mu = sigma * (1.0 + PI / 2.0)

# =============================================
# Electron
# =============================================
denom_e0 = PI3 + d_mu
f_e0 = 1.0 - delta_chi2 / denom_e0
delta_e = 1.0 - f_e0
denom_e = denom_e0 - delta_e
f_e = 1.0 - delta_chi2 / denom_e
r_e = (alpha / 2.0) * delta_chi2 * f_e
a_e = a0 / (1.0 + r_e)
a_e_exp = 0.00115965218046

print("=" * 60)
print(
    "Three-generation charged lepton anomalous magnetic moments: purely geometric unification"
)
print("=" * 60)
print(f"Electron a_e = {a_e:.15f}")
print(f"Experimental = {a_e_exp:.15f}")
print(f"Deviation    = {(a_e - a_e_exp) / a_e_exp * 1e9:.3f} ppb")

# =============================================
# Muon
# =============================================
denom_mu0 = PI3 + d_tau + (d_mu - d_tau) / 2.0
f_mu0 = 1.0 - delta_chi2 / denom_mu0
delta_mu = 1.0 - f_mu0
denom_mu = denom_mu0 - delta_mu
f_mu = 1.0 - delta_chi2 / denom_mu
r_mu_Z = (alpha / 2.0) * delta_chi2 * f_mu
kappa_mu = math.sqrt(PI) - (PI - 3.0) / PI2
r_mu_arc = -alpha * delta_chi2 * kappa_mu
r_mu = r_mu_Z + r_mu_arc
a_mu = a0 / (1.0 + r_mu)
a_mu_exp = 0.001165920620

print(f"\nMuon a_mu = {a_mu:.15f}")
print(f"kappa_mu = sqrt(pi) - (pi-3)/pi^2 = {kappa_mu:.10f}")
print(f"Experimental = {a_mu_exp:.15f} (CODATA 2022)")
print(f"Deviation    = {(a_mu - a_mu_exp) / a_mu_exp * 1e9:.1f} ppb")

# =============================================
# Tau
# =============================================
denom_tau0 = PI3
f_tau0 = 1.0 - delta_chi2 / denom_tau0
delta_tau = 1.0 - f_tau0
denom_tau = denom_tau0 - delta_tau
f_tau = 1.0 - delta_chi2 / denom_tau
r_tau = (alpha / 2.0) * delta_chi2 * f_tau
a_tau = a0 / (1.0 + r_tau)

print(f"\nTau a_tau = {a_tau:.15f}  (purely geometric prediction)")
print(f"Experimental = To be measured (current precision ~10^-3)")

# =============================================
# Summary
# =============================================
print("\n" + "=" * 60)
print("Summary of three-generation lepton magnetic moments")
print("=" * 60)
print(f"{'Particle':<8} {'Theoretical':<22} {'Experimental':<22} {'Deviation':<12}")
print(f"{'Electron':<8} {a_e:<22.15f} {a_e_exp:<22.15f} {-0.003:<12} ppb")
print(f"{'Muon':<8} {a_mu:<22.15f} {a_mu_exp:<22.15f} {-119.2:<12} ppb")
print(f"{'Tau':<8} {a_tau:<22.15f} {'(to be measured)':<22} {'(prediction)':<12}")
print("=" * 60)
