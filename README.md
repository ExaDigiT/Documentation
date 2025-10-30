# ExaDigiT: The Exascale Digital Twin Framework

ExaDigiT is an open, modular ecosystem for modeling, simulating, and visualizing large-scale supercomputing facilities.

---

## 🔧 Structure

### 🧊 Cooling
Modelica-based and CSM-driven models for facility-level thermal management.
- [cooling-autocsm](../Cooling/cooling-autocsm)
- [cooling-datacenter-frontier](../Cooling/cooling-datacenter-frontier)
- [cooling-datacenter-summit](../Cooling/cooling-datacenter-summit)
- [cooling-fmu-library](../Cooling/cooling-fmu-library)
- [cooling-csm-power9](../Cooling/cooling-csm-power9)

### ⚙️ Simulation
RAPS-based workload and power modeling tools.
- [sim-raps](../Simulation/sim-raps)
- [sim-dashboard](../Simulation/sim-dashboard)
- [sim-server](../Simulation/sim-server)

### 🕶 Visualization
AR/VR and visual analytics modules for immersive digital twins.
- [viz-ue5-digitaltwin](../Visualization/viz-ue5-digitaltwin)
- [viz-omniverse](../Visualization/viz-omniverse)
- [viz-avp-configurator](../Visualization/viz-avp-configurator)
- [viz-usd-datacenterbuilder](../Visualization/viz-usd-datacenterbuilder)

### 📘 Documentation
- [docs-exadigit](../Documentation/docs-exadigit)

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
