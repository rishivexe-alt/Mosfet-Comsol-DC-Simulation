# DC Characteristics of an n-Channel MOSFET
### Two-dimensional device simulation with COMSOL Multiphysics® 6.2 (Semiconductor Module)

![COMSOL](https://img.shields.io/badge/COMSOL-6.2-blue)
![Module](https://img.shields.io/badge/Module-Semiconductor-informational)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Type-Simulation%20study-orange)

A finite-element study of a 2D n-channel silicon MOSFET (Fermi–Dirac statistics, Jain–Roulston
band-gap narrowing, SRH recombination). The project extracts the **threshold voltage**, the
**linear / non-linear / saturation** output characteristics, visualises **channel formation and
pinch-off**, and derives **small-signal parameters** (gm, gd, rd).

📄 **Full report:** [`report/MOSFET_report.pdf`](report/MOSFET_report.pdf) (20 pages, also as [`.docx`](report/MOSFET_report.docx))

<p align="center">
  <img src="figures/08_electron_conc_and_potential.png" width="850" alt="Electron concentration and potential at Vg = 4 V for Vd = 5, 1, 0 V">
</p>

---

## Headline results

| Quantity | Result |
|---|---|
| Threshold voltage (simulated, Vd = 10 mV) | **≈ 1.2 V** |
| Threshold voltage (analytical, reference model) | 1.18 V |
| Saturation current, Vg = 2 / 3 / 4 V | ≈ 25 / 137–142 / 347–369 µA |
| Square-law constant K = 2·I<sub>D,sat</sub>/(V<sub>G</sub>−V<sub>T</sub>)² | ≈ 84 µA/V² (within ~7 %) |
| Output conductance, non-linear region (Vg = 4 V) | 91.7 µS (r<sub>d</sub> ≈ 10.9 kΩ) |
| Output conductance, saturation (Vg = 4 V) | ≈ 7 µS (r<sub>d</sub> ≈ 135 kΩ) |
| Saturation transconductance g<sub>m</sub> | ≈ 227 µS |
| Intrinsic gain g<sub>m</sub>/g<sub>d</sub> | ≈ 30 |

> **Note:** the model is 2D, so currents are per unit out-of-plane depth. Compare absolute µA values
> qualitatively, and trends quantitatively.

<table>
<tr>
<td><img src="figures/06_transfer_id_vs_vg.png" alt="Transfer characteristic"><br><sub><b>Transfer curve</b> (Vd = 10 mV): V<sub>T</sub> ≈ 1.2 V</sub></td>
<td><img src="figures/07_output_id_vs_vd.png" alt="Output characteristics"><br><sub><b>Output curves</b> at Vg = 2, 3, 4 V</sub></td>
</tr>
</table>

## Key findings

1. **Threshold voltage** from the simulated transfer curve (≈ 1.2 V) agrees with linear extrapolation
   (≈ 1.18 V) and the analytical estimate (1.18 V).
2. **Three operating regions** are reproduced for every gate voltage; saturation current scales
   approximately with (V<sub>G</sub> − V<sub>T</sub>)².
3. **Pinch-off:** at V<sub>D</sub> = 5 V the inversion layer is markedly thinner at the drain end. This is
   the physical origin of current saturation. At V<sub>D</sub> = 0 V the channel is uniform.
4. **Short-channel signatures:** saturation begins earlier than V<sub>G</sub>−V<sub>T</sub> at high V<sub>G</sub>
   and the saturation current keeps rising slightly with V<sub>D</sub> (finite r<sub>d</sub>).

## Device and model

<p align="center"><img src="figures/01_device_geometry_terminals.png" width="600" alt="Device geometry"></p>

| Item | Value |
|---|---|
| Domain | 3 µm × 0.7 µm p-type Si, N<sub>a</sub> = 10¹⁷ cm⁻³ |
| Source / drain | n⁺ Gaussian box implants, peak N<sub>d</sub> = 10²⁰ cm⁻³, d<sub>j</sub> = (0.2, 0.25) µm |
| Gate | x = 0.7–2.3 µm (1.6 µm), 30 nm insulator, ε<sub>r</sub> = 4.5 |
| Contacts | Source and base grounded; drain V<sub>d</sub>; gate V<sub>g</sub> |
| Physics | Fermi–Dirac, Jain–Roulston BGN, SRH recombination |
| Mesh | Edge mesh 0.08 µm + mapped boundary-layer mesh (growth rate 1.05) |
| Study 1 | V<sub>d</sub> = 10 mV, V<sub>g</sub> = 0–4 V (transfer curve) |
| Study 2 | V<sub>d</sub> = 0–5 V at V<sub>g</sub> = 2, 3, 4 V (output curves) |

<table>
<tr>
<td><img src="figures/04_doping_signed_Nd-Na.png" alt="Signed doping"><br><sub>Signed doping N<sub>d</sub>−N<sub>a</sub></sub></td>
<td><img src="figures/05_doping_net_pn_log.png" alt="Net doping p/n"><br><sub>Net doping, p-type (red) / n-type (blue), log scale</sub></td>
</tr>
</table>

Full parameter list: [`data/simulation_parameters.csv`](data/simulation_parameters.csv).
Step-by-step rebuild instructions: [`docs/reproduce_in_comsol.md`](docs/reproduce_in_comsol.md).

## Repository structure

```
.
├── README.md
├── LICENSE
├── CITATION.cff
├── report/                 Full report (PDF + DOCX)
├── figures/                Publication-style figures used in the report
├── comsol_screenshots/     Raw COMSOL GUI screenshots (settings + results)
├── data/                   key_results.csv, simulation_parameters.csv
├── docs/                   reproduce_in_comsol.md
├── model/                  Place mosfet.mph here (see model/README.md)
└── scripts/
    └── verify_calculations.py
```

## Verify the derived numbers

`scripts/verify_calculations.py` recomputes ψ<sub>B</sub>, the extrapolated V<sub>T</sub>, K, g<sub>d</sub>, r<sub>d</sub>,
g<sub>m</sub> and gain from the values read off the COMSOL curves and checks they match the report.
No dependencies beyond the Python standard library.

```bash
python scripts/verify_calculations.py
```

## Limitations

* 2D model: currents are per unit depth.
* Edge mesh (0.08 µm) is coarser than the COMSOL reference (0.03 µm); no mesh-convergence study yet.
* Several values were read graphically (≈ ±3–5 %).
* Simplified gate stack (no interface traps, fixed charge, quantum effects or leakage); default
  mobility; no temperature dependence.

## Roadmap

- [ ] Mesh-convergence study (0.08 µm vs 0.03 µm)
- [ ] Export raw I–V data and compute slopes/knees numerically
- [ ] Sub-threshold analysis on a log scale (swing, on/off ratio)
- [ ] Sweep gate length, oxide thickness, doping, junction depth (DIBL, channel-length modulation)
- [ ] High-k dielectrics and alternative channel materials
- [ ] AC small-signal and transient analysis; temperature and interface-trap models

## References

1. S. M. Sze and K. K. Ng, *Physics of Semiconductor Devices*, 3rd ed., Wiley, 2007.
2. COMSOL AB, *DC Characteristics of a MOS Transistor (MOSFET)*, Application Library model
   `Semiconductor_Module/Transistors/mosfet`, COMSOL Multiphysics® 6.2.
3. COMSOL AB, *Semiconductor Module User's Guide*, COMSOL Multiphysics® 6.2.
4. Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI Devices*, 3rd ed., Cambridge Univ. Press, 2021.
5. S. C. Jain and D. J. Roulston, *Solid-State Electronics* **34**(5), 453–465, 1991.
6. W. Shockley and W. T. Read, *Physical Review* **87**(5), 835–842, 1952.

## Acknowledgement and licence

This work follows the structure of COMSOL's Application Library example, with modified geometry
parameters and mesh settings, and my own analysis. COMSOL Multiphysics® is a registered trademark of
COMSOL AB, which is not affiliated with this repository. Report text, figures and scripts are released
under the [MIT License](LICENSE).

**Author:** Rishi P
