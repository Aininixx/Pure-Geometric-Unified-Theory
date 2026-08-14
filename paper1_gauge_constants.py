"""
附录C 完整数值验算
维度坍缩、永恒旋转与信息守恒：耦合常数的几何起源

本代码覆盖：
  1. 三重投影与裸耦合常数
  2. 波包锐化参数（Δπ_max, π_eff, r²）
  3. M_Z 能标的有效耦合预言（电磁、弱、强）
  4. C.6.7bis 反推一致性检验
  5. C.6.12 反算验证表（E₀ 几何锁定）
  6. C.6.13 弱耦合与强耦合跑动独立预言
"""

import math
import numpy as np

# ============================================================
# 0. 基本几何常数
# ============================================================
PI = math.pi

# 波包宽度：降维喷涂编码成本
sigma = math.sqrt(1.0 + PI)

# 三重投影信息容量
I_3sphere = 4.0 * PI**3  # 三维球面 4π^3
I_2brane = PI**2  # 二维母线 π^2
I_1line = PI  # 一维线段 π
I_total_bare = I_3sphere + I_2brane + I_1line  # 4π^3 + π^2 + π

print("=" * 78)
print("附录C：耦合常数的几何起源——完整数值验算")
print("=" * 78)
print(f"π        = {PI:.15f}")
print(f"σ        = sqrt(1+π) = {sigma:.12f}")
print(f"三维球面 4π^3 = {I_3sphere:.12f}")
print(f"二维母线 π^2  = {I_2brane:.12f}")
print(f"一维线段 π    = {I_1line:.12f}")
print(f"光子总禁锢边界 4π^3+π^2+π = {I_total_bare:.12f}")

# ============================================================
# 1. 裸耦合常数
# ============================================================
alpha_bare = 1.0 / I_total_bare
alpha_W_bare = 1.0 / (PI**3)
alpha_s_bare = 1.0 / PI
sin2_thetaW_bare = (PI**3) / I_total_bare

print()
print("【C.5】裸耦合常数（低能几何值）")
print("-" * 78)
print(f"α      裸值 = 1/(4π³+π²+π) = 1/{I_total_bare:.12f} = {alpha_bare:.15f}")
print(f"        实验值 ≈ 1/137.035999084")
print(f"        α^{-1} 偏差 = {1/alpha_bare - 137.035999084:+.6e}")
print()
print(f"α_W    裸值 = 1/π³ = 1/{PI**3:.12f} = {alpha_W_bare:.15f}")
print(f"        α_W^{-1} = {1/alpha_W_bare:.12f} ≈ 1/31.006")
print()
print(f"α_s    裸值 = 1/π = {alpha_s_bare:.15f}")
print(f"        α_s^{-1} = {1/alpha_s_bare:.12f} ≈ π = {PI:.12f}")
print()
print(f"sin²θ_W 裸值 = π³/(4π³+π²+π) = {sin2_thetaW_bare:.12f}")
print(f"        实验低能提取值约 0.238（受非微扰污染）")

# ============================================================
# 2. 波包锐化参数
# ============================================================
Delta_pi_max = 1.0 / sigma - sigma**2 / PI**2
pi_eff = PI + Delta_pi_max
r2 = (PI / pi_eff) ** 2

print()
print("【C.6.5-C.6.6】波包锐化与压缩因子")
print("-" * 78)
print(f"Δπ_max = 1/σ - σ²/π²")
print(f"       = {1/sigma:.12f} - {sigma**2/PI**2:.12f}")
print(f"       = {Delta_pi_max:.12f}")
print(f"π_eff  = π + Δπ_max = {pi_eff:.12f}")
print(f"r²     = (π/π_eff)² = {r2:.12f}")

# ============================================================
# 3. M_Z 能标有效耦合预言
# ============================================================
# 几何锁定参数
Lambda1 = 0.2675  # GeV，π线段溶解中心
delta1 = 0.02  # GeV，过渡宽度
E_pi2 = 246.22  # GeV，电弱标度
E0 = E_pi2 / (1.0 / sigma**2 + sigma * PI)  # 几何锁定， ≈37.11 GeV

print()
print("【C.6.12】几何锁定参数")
print("-" * 78)
print(f"Λ₁   = {Lambda1} GeV")
print(f"δ₁   = {delta1} GeV")
print(
    f"E₀   = v / (1/σ² + σπ) = {E_pi2} / ({1/sigma**2:.6f} + {sigma*PI:.6f}) = {E0:.6f} GeV"
)

# 计算 M_Z 处的 Δπ(m_Z) 和 r²(m_Z)
mZ = 91.1876  # GeV

Delta_pi_mZ = Delta_pi_max * (1.0 - math.exp(-mZ / E0))
r2_mZ = (PI / (PI + Delta_pi_mZ)) ** 2

print()
print(f"【C.6.7】M_Z 能标的有效耦合预言 (E₀={E0:.4f} GeV)")
print("-" * 78)
print(f"Δπ(m_Z) = Δπ_max × (1 - e^(-m_Z/E₀))")
print(f"        = {Delta_pi_max:.12f} × (1 - e^(-{mZ}/{E0:.4f}))")
print(f"        = {Delta_pi_mZ:.12f}")
print(f"r²(m_Z) = (π/(π+Δπ(m_Z)))² = {r2_mZ:.12f}")
print()

# 电磁耦合
I_bare_mZ = I_3sphere + I_2brane  # 4π³ + π²
alpha_inv_mZ = I_bare_mZ * r2_mZ

print(f"【有效电磁耦合】")
print(f"  I_bare(m_Z) = 4π³+π² = {I_bare_mZ:.12f}")
print(
    f"  α⁻¹(m_Z) = I_bare × r²(m_Z) = {I_bare_mZ:.12f} × {r2_mZ:.12f} = {alpha_inv_mZ:.12f}"
)
print(f"  实验值 127.95，偏差 = {alpha_inv_mZ - 127.95:+.6f}")
print()

# 弱耦合
alpha_W_inv_mZ = PI**3 * r2_mZ
print(f"【有效弱耦合】")
print(
    f"  α_W⁻¹(m_Z) = π³ × r²(m_Z) = {PI**3:.12f} × {r2_mZ:.12f} = {alpha_W_inv_mZ:.12f}"
)
print(f"  实验值 29.59±0.02，偏差 = {alpha_W_inv_mZ - 29.59:+.6f}")
print()

# 强耦合
alpha_s_inv_mZ = (PI**2 - 1.0) * r2_mZ
alpha_s_mZ = 1.0 / alpha_s_inv_mZ
print(f"【有效强耦合】")
print(
    f"  α_s⁻¹(m_Z) = (π²-1) × r²(m_Z) = {PI**2-1:.12f} × {r2_mZ:.12f} = {alpha_s_inv_mZ:.12f}"
)
print(f"  α_s(m_Z) = 1/{alpha_s_inv_mZ:.12f} = {alpha_s_mZ:.12f}")
print(f"  PDG实验值 0.1180，偏差 = {(alpha_s_mZ-0.1180)/0.1180*100:+.3f}%")
print()

# 温伯格角
sin2_thetaW_mZ = PI**3 / I_bare_mZ
print(f"【有效温伯格角】")
print(
    f"  sin²θ_W(m_Z) = π³/(4π³+π²) = {PI**3:.12f}/{I_bare_mZ:.12f} = {sin2_thetaW_mZ:.12f}"
)
print(f"  实验值 0.23122，偏差 = {sin2_thetaW_mZ - 0.23122:+.6f}")
print()

# ============================================================
# 4. C.6.7bis 反推一致性检验
# ============================================================
print()
print("【C.6.7bis】公共压缩因子的独立反推检验")
print("-" * 78)

alpha_W_exp_mZ = 1.0 / 29.7
r2_infer = 1.0 / (PI**3 * alpha_W_exp_mZ)

print(f"由 α_W^(exp)(M_Z) ≈ 1/29.7 反推：")
print(f"  r²_infer = 1/(π³·α_W^(exp))")
print(f"          = 1/({PI**3:.12f} × {alpha_W_exp_mZ:.12f})")
print(f"          = {r2_infer:.12f}")
print(f"  C.6.12 给出的 r²(m_Z) = {r2_mZ:.12f}")
print(f"  二者偏差 = {abs(r2_infer - r2_mZ)/r2_mZ*100:.3f}%")
print()

# 用 r2_infer 预测电磁耦合
alpha_inv_mZ_infer = I_bare_mZ * r2_infer
print(f"用 r²_infer 预测 α⁻¹(m_Z)：")
print(f"  α⁻¹ = (4π³+π²)·r²_infer")
print(f"       = {I_bare_mZ:.12f} × {r2_infer:.12f}")
print(f"       = {alpha_inv_mZ_infer:.12f}")
print(f"  实验值 127.95，偏差 = {abs(alpha_inv_mZ_infer-127.95)/127.95*100:.3f}%")
print()

print(f"sin²θ_W(m_Z) 仍为 {sin2_thetaW_mZ:.12f}（r² 抵消）")
print(f"  实验值 0.23122，偏差 = {abs(sin2_thetaW_mZ-0.23122)/0.23122*100:.3f}%")
print()

# ============================================================
# 5. C.6.12 反算验证表
# ============================================================
print()
print("【C.6.12】反算验证表（E₀ 几何锁定）")
print("-" * 78)

# 实验数据点
exp_data = np.array(
    [
        [0.1, 137.036],
        [1.5, 134.0],
        [2.5, 133.0],
        [3.5, 132.0],
        [59.0, 130.0],
        [91.1876, 127.95],
        [200.0, 127.0],
    ]
)


def alpha_inv_model(E, Lambda1, delta1, E0):
    """理论 α^-1(E)"""
    z = (E - Lambda1) / delta1
    # 数值稳定 sigmoid
    sigmoid = np.where(z > 50.0, 0.0, np.where(z < -50.0, 1.0, 1.0 / (1.0 + np.exp(z))))
    Delta_pi_E = Delta_pi_max * (1.0 - np.exp(-E / E0))
    r2_E = (PI / (PI + Delta_pi_E)) ** 2
    return (4 * PI**3 + PI**2 + PI * sigmoid) * r2_E


print(f"使用参数：Λ₁={Lambda1} GeV, δ₁={delta1} GeV, E₀={E0:.6f} GeV")
print()
print(f"{'E (GeV)':>10} | {'理论 α^-1':>12} | {'实验/约束 α^-1':>14} | {'偏差':>8}")
print("-" * 56)
for E_test, exp_val in exp_data:
    pred = alpha_inv_model(np.array([E_test]), Lambda1, delta1, E0)[0]
    diff = (pred - exp_val) / exp_val * 100
    print(f"{E_test:10.4f} | {pred:12.4f} | {exp_val:14.4f} | {diff:+.3f}%")
print()

# 补充几个低能外推点
print("低能外推点：")
for E_test in [0.185, 0.2675, 0.35, 1.0]:
    pred = alpha_inv_model(np.array([E_test]), Lambda1, delta1, E0)[0]
    print(f"  E = {E_test} GeV -> α^-1 = {pred:.4f}")

print()

# ============================================================
# 6. C.6.13 弱耦合与强耦合预言（数值已在上面给出）
# ============================================================
print()
print("【C.6.13】弱耦合与强耦合常数跑动的独立预言")
print("-" * 78)
print(f"Δπ(m_Z) = {Delta_pi_mZ:.12f}")
print(f"r²(m_Z) = {r2_mZ:.12f}")
print()
print(f"弱耦合预言：α_W⁻¹(m_Z) = π³·r²(m_Z) = {alpha_W_inv_mZ:.12f} ≈ 29.75")
print(f"  实验值 29.59±0.02，偏差约 {abs(alpha_W_inv_mZ-29.59)/29.59*100:.2f}%")
print()
print(f"强耦合预言：α_s⁻¹(m_Z) = (π²-1)·r²(m_Z) = {alpha_s_inv_mZ:.12f} ≈ 8.51")
print(f"  α_s(m_Z) = {alpha_s_mZ:.12f} ≈ 0.1175")
print(f"  PDG实验值 0.1180，偏差约 {(alpha_s_mZ-0.1180)/0.1180*100:.2f}%")
print()

# ============================================================
# 7. 温伯格角预言
# ============================================================
print()
print("【温伯格角预言】")
print("-" * 78)
print(f"裸值：sin²θ_W(bare) = π³/(4π³+π²+π) = {sin2_thetaW_bare:.12f}")
print(f"     ≈ 0.2263，实验低能提取值≈0.238（受非微扰污染）")
print(f"M_Z 跑动值：sin²θ_W(m_Z) = π³/(4π³+π²) = {sin2_thetaW_mZ:.12f}")
print(f"     ≈ 0.23156，实验值 0.23122，偏差 <0.15%")
print(f"高能极限：sin²θ_W → 0 当 E >> E_pi2（二维母线 π² 溶解，π³ 曲面消失）")

print("=" * 78)
print("验算完成")
print("=" * 78)
