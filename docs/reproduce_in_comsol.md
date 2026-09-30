# Reproducing the model in COMSOL Multiphysics 6.2

Requires the **Semiconductor Module**. All lengths in µm.

| Step | Stage | Actions |
|---|---|---|
| 1 | Model Wizard | New > Model Wizard > 2D > Semiconductor (semi) > Study > Stationary |
| 2 | Global parameters | `Vd = 10[mV]`, `Vg = 2[V]` |
| 3 | Geometry | Rectangle 3 × 0.7; closed polygon (vertices below); Mesh Control Edges; remove boundary 4 of the "fin" |
| 4 | Material | Add *Si – Silicon* |
| 5 | Semiconductor | Fermi–Dirac statistics; Analytic Doping Models 1–3 (below) |
| 6 | Boundaries | Metal Contact on B3 (source, 0 V), B7 (drain, `Vd`), B2 (base, 0 V); Thin Insulator Gate on B5 (`Vg`, ε = 4.5, 30 nm) |
| 7 | Recombination / BGN | Trap-Assisted Recombination on all domains; Jain–Roulston band-gap narrowing |
| 8 | Mesh | User-controlled: edge mesh (0.08 µm) on B3–B7, mapped mesh with distribution, free triangular |
| 9 | Plot | Signed dopant concentration `semi.Nd - semi.Na` |
| 10 | Study 1 | `Vd = 0.01 V`; `Vg = range(0,0.2,1.4), 2, 3, 4`; plot `semi.IO_2` vs Vg |
| 11 | Study 2 | Sweep `Vd` 0–5 V at `Vg = 2, 3, 4 V`; plot `semi.IO_2` vs Vd |
| 12 | Post-processing | Electron concentration and potential at Vd = 5, 1, 0 V (Vg = 4 V) |

## Polygon vertices (closed curve)

| Vertex | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| x (µm) | 0 | 0 | 0.5 | 0.7 | 2.3 | 2.5 | 3 | 3 |
| y (µm) | 0.67 | 0.7 | 0.7 | 0.7 | 0.7 | 0.7 | 0.7 | 0.67 |

## Analytic Doping Models (all domains)

| Feature | Role | Settings |
|---|---|---|
| Model 1 | Uniform p-type background | `NA0 = 1e17[1/cm^3]` |
| Model 2 | n+ source (Box, Gaussian) | `r0 = (0, 0.6)`, `W = 0.6`, `D = 0.1`, `ND0 = 1e20[1/cm^3]`, `dj = (0.2, 0.25)`, `Nb = Acceptor concentration (semi/adm1)` |
| Model 3 | n+ drain (Box, Gaussian) | as Model 2 with `r0 = (2.4, 0.6)` |

## Boundary map

| Boundary | Location | Condition |
|---|---|---|
| 1, 8 | Left / right walls | Insulation |
| 2 | Bottom | Metal contact, 0 V (base) |
| 3 | x = 0–0.5 µm | Metal contact, 0 V (source) |
| 4, 6 | Gaps | Insulation |
| 5 | x = 0.7–2.3 µm | Thin Insulator Gate, `V0 = Vg` |
| 7 | x = 2.5–3 µm | Metal contact, `V0 = Vd` (drain) |

## Exporting data for further analysis

To make the results fully reproducible, export the curves from COMSOL
(*Results > Export > Plot* or *Derived Values > Evaluate*) as
`data/id_vs_vg.csv` and `data/id_vs_vd.csv`, then compute slopes and knees
numerically instead of reading them off the plots.
