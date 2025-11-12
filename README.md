# ExaDigiT: The Exascale Digital Twin Framework

ExaDigiT is an open, modular ecosystem for modeling, simulating, and visualizing large-scale supercomputing facilities.

---

## Structure

### 🧊 Cooling
Modelica-based and CSM-driven models for facility-level thermal management.
- [cooling-autocsm](../AutoCSM)
- [cooling-frontier](../datacenterCoolingModel)
- [cooling-power9-csm](../POWER9CSM)
- [cooling-fmu-library](../fmu-models)
- [cooling-summit-archive](../summitcoolingmodel)

### ⚙️ Simulation
RAPS-based workload and power modeling tools.
- [sim-raps](../raps)
- [sim-dashboard](../simulation-dashboard)
- [sim-server](../simulationserver)

### 🕶 Visualization
AR/VR and visual analytics modules for immersive digital twins.
- [viz-exadigitUE5](../exadigitue5)
- [viz-omniverse](../exadigit-ov)
- [viz-datacenterexplorer-ue-plugin](../DatacenterExplorer)

### 🔧 Tools
- [tools-atlas-system-configurator](../atlas)
- [tools-avp-configurator](../avp-configurator)
- [tools-usd-datacenter-builder](../usddcbuilder)

---

## 🧩 Overview

ExaDigiT integrates real telemetry data, simulation models, and visualization tools to enable:
- Energy-efficient supercomputer operation
- Predictive maintenance
- AR/VR-enabled exploration of power, cooling, and workloads

For more information, contact: **Wes Brewer (ORNL)** or visit [code.ornl.gov/exadigit](https://code.ornl.gov/exadigit).

-----------------------------------------

# Documentation

This is the ExaDigiT documentation source. The documentation is deployed at
[https://exadigit.readthedocs.io/](https://exadigit.readthedocs.io/).

## Setup Python dependencies
pip install -r requirements.txt

## Build documentation
make html

## Open in browser
open build/html/index.html
