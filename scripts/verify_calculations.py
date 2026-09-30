#!/usr/bin/env python3
"""
Independent check of the derived quantities quoted in the report.

Every input below is a value read from the COMSOL results (see
data/key_results.csv and the report, Sections 4.2-4.5). Nothing here
re-runs the finite-element model; the script only verifies that the
hand calculations in the report are internally consistent.

Usage:  python scripts/verify_calculations.py
"""
import math

# ---- Constants -----------------------------------------------------------
kB_q = 8.617333e-5          # eV/K  (kB/q in V/K)
T = 300.0                   # K
ni = 1e10                   # cm^-3, intrinsic density used in the report
Na = 1e17                   # cm^-3, substrate doping

# ---- 1. Bulk potential and strong-inversion onset (Sec. 2.3) -------------
psi_B = kB_q * T * math.log(Na / ni)
print(f"psi_B            = {psi_B:.3f} V   (report: ~0.42 V)")
print(f"2*psi_B          = {2*psi_B:.3f} V   (report: ~0.83 V)")

# ---- 2. Threshold voltage by linear extrapolation (Sec. 4.2) -------------
# Linear part of the Id-Vg curve at Vd = 10 mV: (2 V, 1.0 uA) and (4 V, 3.5 uA)
(v1, i1), (v2, i2) = (2.0, 1.0), (4.0, 3.5)
slope = (i2 - i1) / (v2 - v1)            # uS  -> transconductance gm (linear)
VT_extrap = v1 - i1 / slope
print(f"gm (linear)      = {slope:.2f} uS  (report: ~1.25 uS)")
print(f"VT (extrapolated)= {VT_extrap:.2f} V   (from the two rounded points read off the plot;\n"
      f"                    report quotes ~1.18 V from the unrounded data; simulated VT ~ 1.2 V)")

# ---- 3. Square-law constant K = 2*Id,sat/(Vg-VT)^2 (Sec. 4.3) ------------
VT = 1.2
rows = [(2, 25.0), (3, 137.0), (4, 347.0)]   # Vg [V], Id,sat [uA] at the knee (report Table 6)
Ks = []
print("\n Vg   Vg-VT   Id,sat   K = 2Id/(Vg-VT)^2")
for vg, idsat in rows:
    ov = vg - VT
    K = 2 * idsat / ov**2
    Ks.append(K)
    print(f" {vg:>2}   {ov:>4.1f}   {idsat:>6.1f}   {K:6.1f} uA/V^2")
Kmean = sum(Ks) / len(Ks)
print(f"mean K = {Kmean:.1f} uA/V^2 ; max deviation = "
      f"{max(abs(k-Kmean)/Kmean for k in Ks)*100:.1f} %  (report: ~84, within ~7 %)")

# ---- 4. Output conductance / resistance (Sec. 4.5) -----------------------
y1, y2 = 255.09, 346.77                       # uA at Vd = 1 V and 2 V (Vg = 4 V)
gd_nonlin = (y2 - y1) / (2.0 - 1.0)           # uS
print(f"\ngd (Vd=1-2 V)    = {gd_nonlin:.2f} uS -> rd = {1e3/gd_nonlin:.1f} kOhm "
      f"(report: 91.68 uS, 10.9 kOhm)")

gd_sat = (369.0 - 347.0) / (5.0 - 2.0)        # uS
print(f"gd (Vd=2-5 V)    = {gd_sat:.1f} uS   -> rd = {1e3/gd_sat:.0f} kOhm "
      f"(report: ~7 uS, ~135 kOhm)")

# ---- 5. Saturation transconductance and intrinsic gain -------------------
gm_sat = (369.0 - 142.0) / (4.0 - 3.0)        # uS at Vd = 5 V
print(f"gm (sat)         = {gm_sat:.0f} uS  (report: ~227 uS)")
print(f"gm/gd (sat)      = {gm_sat/gd_sat:.0f}     (report: order of 30)")

# ---- 6. Long-channel saturation voltage vs observed knee -----------------
print("\nVD,sat = Vg - VT (long-channel prediction) vs observed knee:")
for vg, knee in [(2, 0.5), (3, 2.0), (4, 2.0)]:
    print(f"  Vg={vg} V: predicted {vg-VT:.1f} V, observed ~{knee:.1f} V")
