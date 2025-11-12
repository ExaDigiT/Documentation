# ExaDigiT: the exascale digital twin framework

ExaDigiT is an open, modular ecosystem for modeling, simulating, and visualizing large-scale supercomputing facilities.

---

## structure

### 🧊 cooling
modelica-based and csm-driven models for facility-level thermal management.
- [cooling-autocsm](https://code.ornl.gov/exadigit/autocsm)
- [cooling-frontier](https://code.ornl.gov/exadigit/datacentercoolingmodel)
- [cooling-power9-csm](https://code.ornl.gov/exadigit/power9csm)
- [cooling-fmu-library](https://code.ornl.gov/exadigit/fmu-models)
- [cooling-summit-archive](https://code.ornl.gov/exadigit/summitcoolingmodel)

### ⚙️ simulation
raps-based workload and power modeling tools.
- [sim-raps](https://code.ornl.gov/exadigit/raps)
- [sim-dashboard](https://code.ornl.gov/exadigit/simulation-dashboard)
- [sim-server](https://code.ornl.gov/exadigit/simulationserver)

### 🕶 visualization
ar/vr and visual analytics modules for immersive digital twins.
- [viz-exadigitue5](https://code.ornl.gov/exadigit/exadigitue5)
- [viz-omniverse](https://code.ornl.gov/exadigit/exadigit-ov)
- [viz-datacenterexplorer-ue-plugin](https://code.ornl.gov/exadigit/datacenterexplorer)

### 🔧 tools
- [tools-atlas-system-configurator](https://code.ornl.gov/exadigit/atlas)
- [tools-avp-configurator](https://code.ornl.gov/exadigit/avp-configurator)
- [tools-usd-datacenter-builder](https://code.ornl.gov/exadigit/usddcbuilder)

---

## 🧩 overview

exadigit integrates real telemetry data, simulation models, and visualization tools to enable:
- energy-efficient supercomputer operation
- predictive maintenance
- ar/vr-enabled exploration of power, cooling, and workloads

for more information, contact: **Wes Brewer** at [brewerwh@ornl.gov](mailto:brewerwh@ornl.gov)

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
