CoolingModel
===================================

The Datacenter Cooling model is a thermo-fluid modeling framework developed using open-source Modelica libraries and the 
commercial Dymola IDE. It is used to models the cooling system like the Frontier supercomputer at Oak 
Ridge National Laboratory. This framework can be extended to other liquid-cooled systems 
and is part of ExaDigit—an open-source framework for developing comprehensive digital twins 
of liquid-cooled supercomputers. The model is dependent on the AutoCSM workflow wherein the 
Dymola Python interface is used to create a Functional MockUp Interface (FMU) of templated 
models from the cooling library using a JSON-based input specification file. The exported 
FMU can be run with either default values of required inputs or time-series values.  Please note that the system load data is calculated using the heat load from the 
central energy plant data.


Prerequisite
------------

- Dymola IDE
- Modelica Libraries
  - ORNL [TRANSFORM Library](https://github.com/ORNL-Modelica/TRANSFORM-Library)
  - ORNL [AutoCSM Library](https://code.ornl.gov/exadigit/AutoCSM)
  - LBNL [Buildings Library](https://github.com/lbl-srg/modelica-buildings)

Installation
------------

  - Clone the repository ``` git clone https://code.ornl.gov/exadigit/datacenterCoolingModel ```
  - Open `setup.mos` in a text editor and update the library locations (if needed).


Quickstart
----------

  - Recommended Dymola Flags (Note these are automatically set via AutoCSM)
  - Copy paste to Dymola command line for performance improvement in editor
  ```
  Advanced.Define.GlobalOptimizations = 2;
  Advanced.Translation.SparseActivate = true;
  Advanced.Translation.SparseActivateIntegrator = true;
  Advanced.Translation.SparseActivateSystems = true;
  Advanced.Translation.ODEJacobianForDiscrete = true;
  ```
  
  - Open Dymola
  - On the `Simulation` tab, run the script `setup.mos` or load the libraries manually
  - Export the FMU: python run_auto_csm.py
  - Run the FMU: python run_fmu.py


Contributors
------------

Vineet Kumar, Oak Ridge National Laboratory.

Michael Scott Greenwood, Oak Ridge National Laboratory.

Wesley Brewer, Oak Ridge National Laboratory.

Wesley Williams, Oak Ridge National Laboratory.

Nathan Parkison, Oak Ridge National Laboratory.

David Grant, Oak Ridge National Laboratory.
