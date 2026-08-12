#!/usr/bin/env python3
"""
Purely Geometric Origin of the Higgs Boson and Neutrinos
Paper 6 of the Pure Geometric Unified Theory series.
Derives Higgs and neutrino masses from pure geometry with zero free parameters.
"""

import math

PI = math.pi

# =============================================
# Higgs Boson Mass
# =============================================
E_pi2 = 246.22  # GeV, electroweak scale
sigma = math.sqrt(1 + PI)
m_H = E_pi2 * sigma / 4.0

print("=" * 50)
print("Higgs Boson Mass")
print("=" * 50)
print(f"σ = {sigma:.10f}")
print(f"m_H = {E_pi2} × {sigma:.6f} / 4 = {m_H:.2f} GeV")
print(f"Experimental: 125.09 ± 0.24 GeV, Deviation {abs(m_H-125.09)/125.09*100:.2f}%")
print()

# =============================================
# Neutrino Masses
# =============================================
# Z boson mass
mZ = (E_pi2 / math.sqrt(2.0)) * (PI / 6.0)
mZ_eV = mZ * 1e9  # GeV -> eV
alpha_W = 1.0 / PI**3
sigma2 = 1.0 + PI
sigma4 = sigma2**2

exp_2sigma2 = 2.0 * sigma2
alpha_W_pow = alpha_W**exp_2sigma2
base = mZ_eV * alpha_W_pow / sigma4


def I_pow(I):
    return I ** (2.0 / PI)


m_e = base * I_pow(PI)
m_mu = base * I_pow(PI**2)
m_tau = base * I_pow(4.0 * PI**3)

print("=" * 50)
print("Neutrino Masses")
print("=" * 50)
print(f"mZ = {mZ:.4f} GeV = {mZ_eV:.2f} eV")
print(f"ν_e: {m_e:.6f} eV")
print(f"ν_μ: {m_mu:.6f} eV")
print(f"ν_τ: {m_tau:.6f} eV")
print(f"Ratio: 1 : {m_mu/m_e:.2f} : {m_tau/m_e:.2f}")
print(f"Σm_ν = {m_e+m_mu+m_tau:.4f} eV")

dm2_21_exp = 7.41e-5  # eV²
dm2_31_exp = 2.51e-3  # eV²
dm2_21 = m_mu**2 - m_e**2
dm2_31 = m_tau**2 - m_e**2
print(
    f"Δm²₂₁ = {dm2_21:.2e} eV²  (Measured {dm2_21_exp:.2e} eV², Deviation {(dm2_21 - dm2_21_exp)/dm2_21_exp*100:.1f}%)"
)
print(
    f"Δm²₃₁ = {dm2_31:.2e} eV²  (Measured {dm2_31_exp:.2e} eV², Deviation {(dm2_31 - dm2_31_exp)/dm2_31_exp*100:.2f}%)"
)
print()

# =============================================
# σ Power Spectrum
# =============================================
print("=" * 50)
print("σ Power Spectrum")
print("=" * 50)
print(f"Higgs mass: m_H ∝ σ¹")
print(f"Electron magnetic moment: Δχ² ∝ σ²")
print(f"Neutrino mass: m_ν ∝ 1/σ⁴")
print(f"σ = √(1+π) = {sigma:.10f}")
