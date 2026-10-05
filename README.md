# ExaDigiT: the exascale digital twin framework

ExaDigiT is an open, modular ecosystem for modeling, simulating, and visualizing large-scale supercomputing facilities.
The framework integrates real telemetry data, simulation models, and visualization tools to enable:
- energy-efficient supercomputer operation
- predictive maintenance
- ar/vr-enabled exploration of power, cooling, and workloads

For more information, contact: **Wes Brewer** at [brewerwh@ornl.gov](mailto:brewerwh@ornl.gov)

---

## Structure

### 🧊 cooling
modelica-based and csm-driven models for facility-level thermal management.
- [cooling-autocsm](https://github.com/ExaDigiT/AutoCSM)
- [cooling-frontier](https://github.com/ExaDigiT/datacenterCoolingModel)
- [cooling-power9-csm](https://github.com/ExaDigiT/POWER9CSM)

### ⚙️ simulation
raps-based workload and power modeling tools.
- [sim-raps](https://github.com/ExaDigiT/RAPS)
- [sim-dashboard](https://github.com/ExaDigiT/SimulationDashboard)
- [sim-server](https://github.com/ExaDigiT/SimulationServer)

### 🕶 visualization
ar/vr and visual analytics modules for immersive digital twins.
- [viz-exadigitue5](https://github.com/ExaDigiT/exadigitue5)
- [viz-omniverse](https://github.com/ExaDigiT/exadigit-ov)
- [viz-datacenterexplorer-ue-plugin](https://github.com/ExaDigiT/DatacenterExplorer)

### 🔧 tools
- [tools-usd-datacenter-builder](https://github.com/ExaDigiT/usd-dc-builder)

-----------------------------------------

# Instructions for building Sphinx-based documentation

This is the ExaDigiT documentation source. The documentation is deployed at
[https://exadigit.readthedocs.io/](https://exadigit.readthedocs.io/).

## Setup Python dependencies

    pip install -r requirements.txt

## Build documentation

    make html

## Open in browser

    open build/html/index.html
