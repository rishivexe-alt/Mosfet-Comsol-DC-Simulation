# DC Characteristics of an n-Channel MOSFET

### Two-Dimensional Semiconductor Device Simulation Using COMSOL Multiphysics® 6.2

<p align="center">

**COMSOL Multiphysics® 6.2** · **Semiconductor Module** · **Finite-Element Simulation** · **Device Physics**

</p>

<p align="center">
  <img src="figures/08_electron_conc_and_potential.png"
       width="850"
       alt="Electron concentration and potential distribution in the simulated MOSFET">
</p>

<p align="center">
  <b>2D MOSFET simulation showing carrier concentration and electrostatic potential under different drain-bias conditions.</b>
</p>

---

## About This Project

Transistors are the fundamental active devices behind modern electronics. They enable **switching, amplification, signal processing, memory, sensing, and computation**, forming the basis of everything from microcontrollers and communication systems to CPUs, GPUs, and embedded hardware.

Among the different transistor families, the **MOSFET (Metal–Oxide–Semiconductor Field-Effect Transistor)** is one of the most important devices in modern semiconductor technology. Its ability to control current through an electric field makes it highly suitable for both digital switching and analog amplification.

This project investigates the **DC characteristics of a two-dimensional n-channel MOSFET** using COMSOL Multiphysics® 6.2 and the Semiconductor Module. Rather than treating the device as a simple circuit element, the study examines how **doping, electric potential, carrier concentration, gate bias, drain bias, channel formation, and pinch-off** interact to produce the observed electrical characteristics.

The simulation extracts the **threshold voltage**, evaluates the **transfer and output characteristics**, visualizes **channel formation and pinch-off**, and derives important **small-signal parameters** such as transconductance, output conductance, output resistance, and intrinsic gain.

---

# 1. Understanding the Transistor

A **transistor** is a semiconductor device used primarily to control the flow of electrical current.

At a fundamental level, a transistor provides a way for a relatively small electrical signal to control a larger current or voltage. This makes transistors useful in two fundamental roles:

- **Switching** — turning current flow ON and OFF
- **Amplification** — controlling current to produce a larger signal response

A transistor operates through the controlled movement of charge carriers inside a semiconductor. The device structure, doping profile, electric fields, and applied voltages determine how those carriers move.

In modern electronics, billions of transistors can be integrated onto a single semiconductor chip. Understanding transistor physics therefore provides the foundation for understanding **digital logic, processors, memory, analog circuits, embedded systems, and integrated circuits**.

---

# 2. From Transistor to MOSFET

A **MOSFET** is a field-effect transistor in which the current flowing between the **source** and **drain** terminals is controlled primarily by the electric field produced by the **gate**.

A typical MOSFET has four terminals:

| Terminal | Function |
|---|---|
| **Gate (G)** | Controls the channel through an electric field |
| **Drain (D)** | Collects carriers flowing through the channel |
| **Source (S)** | Provides carriers to the channel |
| **Body / Bulk (B)** | Semiconductor region surrounding the channel |

The defining feature of the MOSFET is the insulated gate structure. The gate is separated from the semiconductor by an insulating layer, allowing the gate voltage to control the semiconductor surface without requiring significant steady-state gate current.

For an **n-channel MOSFET**, applying a sufficiently positive gate voltage attracts electrons toward the semiconductor surface and creates an **inversion channel** between source and drain.

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/N-Kanal-MOSFET%20(Schema).svg"
       width="650"
       alt="Conceptual cross-section of an n-channel MOSFET">
</p>

<p align="center">
  <sub>Conceptual n-channel MOSFET structure. Source: Wikimedia Commons, CC BY-SA.</sub>
</p>

> The conceptual illustration above is used to introduce MOSFET structure. The device investigated in this repository is the independently configured 2D COMSOL simulation shown in the project figures below.

---

# 3. How an n-Channel MOSFET Works

The operation of an n-channel MOSFET can be understood through the gate voltage.

### V<sub>G</sub> below threshold

When the gate voltage is insufficient to create a strong inversion layer, a continuous conducting channel does not form between the source and drain.

### V<sub>G</sub> above threshold

As the gate voltage increases beyond the threshold voltage, electrons are attracted toward the semiconductor surface and an inversion channel develops.

The resulting channel provides a path for current between the source and drain.

### Increasing V<sub>D</sub>

As the drain voltage increases, the potential along the channel is no longer uniform. The inversion layer gradually becomes thinner toward the drain.

At sufficiently high drain voltage, the channel approaches **pinch-off** near the drain. Beyond this condition, the drain current becomes much less sensitive to drain voltage, producing the characteristic saturation behavior.

This project investigates these physical effects directly through the simulated **carrier concentration and electrostatic potential distributions** rather than relying only on circuit-level equations.

---

# 4. Why MOSFET Characterization Matters

MOSFET characterization is important because the electrical behavior of the device determines how effectively it can function in real circuits.

Important parameters include:

### Threshold Voltage — V<sub>T</sub>

The threshold voltage represents the approximate gate voltage required to establish strong inversion and enable significant channel conduction.

It affects:

- Switching behavior
- Logic voltage levels
- Power consumption
- Biasing
- Device operating point

### Transconductance — g<sub>m</sub>

Transconductance describes how strongly the drain current responds to changes in gate voltage.

A higher g<sub>m</sub> generally corresponds to stronger gate control over drain current and is particularly important in amplifier design.

### Output Conductance — g<sub>d</sub>

Output conductance describes the dependence of drain current on drain voltage in a particular operating region.

It provides insight into non-ideal saturation behavior.

### Output Resistance — r<sub>d</sub>

Output resistance is approximately the inverse of output conductance:

r<sub>d</sub> ≈ 1 / g<sub>d</sub>

It is an important parameter for understanding the voltage gain and output behavior of transistor-based circuits.

### Intrinsic Gain

The ratio

g<sub>m</sub> / g<sub>d</sub>

provides an indication of the transistor's intrinsic voltage-gain capability.

---

# 5. Project Objective

The objective of this project is to perform a detailed **two-dimensional semiconductor device simulation of an n-channel MOSFET** and connect the physical device behavior to its electrical characteristics.

The study focuses on:

- Modeling the MOSFET device structure
- Defining realistic semiconductor doping regions
- Solving the semiconductor electrostatic and carrier-transport problem
- Investigating threshold-voltage behavior
- Obtaining transfer characteristics
- Obtaining drain-current versus drain-voltage characteristics
- Identifying linear, non-linear, and saturation regions
- Visualizing channel formation
- Studying pinch-off near the drain
- Extracting g<sub>m</sub>, g<sub>d</sub>, and r<sub>d</sub>
- Estimating intrinsic gain
- Independently verifying derived quantities using Python

---

# 6. My Approach

I approached this project by focusing on **understanding the physical reason behind each simulated result rather than simply reproducing a curve**.

The workflow was structured around the relationship:

```text
Device Structure
       ↓
Material Properties
       ↓
Doping Profiles
       ↓
Electrical Boundary Conditions
       ↓
Mesh Configuration
       ↓
Semiconductor Physics
       ↓
DC Simulation
       ↓
Carrier Concentration & Potential
       ↓
I–V Characteristics
       ↓
Parameter Extraction
       ↓
Independent Verification
