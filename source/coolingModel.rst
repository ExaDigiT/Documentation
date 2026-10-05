Cooling Model
===================================

The datacenter cooling model is a thermo-fluid modeling framework developed using open-source Modelica libraries and the
commercial Dymola IDE. It is used to model cooling systems like that of the Frontier supercomputer at Oak
Ridge National Laboratory. This framework can be extended to other liquid-cooled systems
and is part of ExaDigiT, an open-source framework for developing comprehensive digital twins
of liquid-cooled supercomputers.

The models are generated with the AutoCSM workflow, where the Dymola Python interface is used to create a
Functional Mock-up Unit (FMU) from templated models, driven by a JSON input specification file. The exported
FMU can be run standalone, with default values or time-series inputs, or coupled to RAPS, which supplies the
heat load of each CDU at every time step (see `Use with RAPS`_).

The example models live in the POWER9CSM repository (https://github.com/ExaDigiT/POWER9CSM), which uses the
AutoCSM framework (https://github.com/ExaDigiT/AutoCSM) and the TRANSFORM library.

Prerequisites
-------------

- Python with ``fmpy``, ``numpy``, ``pandas`` and ``matplotlib``
- Dymola IDE, only needed to generate a new FMU or to edit the models; pre-generated FMUs can be run without it
- Modelica libraries, included as git submodules of POWER9CSM:

  - ORNL `TRANSFORM Library <https://github.com/ORNL-Modelica/TRANSFORM-Library>`_
  - ORNL `AutoCSM <https://github.com/ExaDigiT/AutoCSM>`_

Installation
------------

.. code-block:: shell-session

   $ git clone --recurse-submodules https://github.com/ExaDigiT/POWER9CSM
   $ cd POWER9CSM

The submodules may need to be switched from https to ssh URLs depending on your access.

Repository contents:

- ``json``: input specifications (``marconi100.json``, ``lassen.json``, ``summit.json``)
- ``POWER9Datacenter``: Modelica library following the AutoCSM templated approach
- ``fmus``: pre-generated, license-free FMUs of the example systems (Marconi100, Lassen, Summit)
- ``data``: example time series for testing the models

Quickstart
----------

To run an example without Dymola, use one of the FMUs in ``fmus``. To create the FMUs yourself:

.. code-block:: shell-session

   $ python run_autocsm.py    # generates setup.mos, Simulator.mo and Simulator.fmu in the output folder (e.g. temp)
   $ python run_fmu.py        # simulates the FMU; plots, results and logs go to the output folder

A one day (86400 s) simulation takes about two minutes for Marconi100 and Lassen. Summit takes about two minutes for 2000 seconds.

To explore or modify a model, open Dymola and run the generated ``setup.mos`` on the ``Simulation`` tab, or load the libraries manually. To model a different system, create or modify an input specification in ``json``. The Dymola flags below are set automatically by AutoCSM; for interactive work they improve performance when pasted into the Dymola command line:

.. code-block:: console

  Advanced.Define.GlobalOptimizations = 2;
  Advanced.Translation.SparseActivate = true;
  Advanced.Translation.SparseActivateIntegrator = true;
  Advanced.Translation.SparseActivateSystems = true;
  Advanced.Translation.ODEJacobianForDiscrete = true;

Use with RAPS
-------------

RAPS loads the FMU with FMPy and steps it together with the power simulation. At each cooling step RAPS provides:

- the heat load of each CDU, which is the CDU power multiplied by ``cooling_efficiency`` and divided by ``racks_per_cdu``, and
- the outdoor temperature input of the FMU (``temperature_keys``): the ``wet_bulb_temp`` default of the system config, or, when replaying telemetry with weather enabled, the hourly air temperature from Open-Meteo for the site (``zip_code`` and ``country_code`` of the system).

The FMU returns rack and facility temperatures, pressures and flow rates, the pump and cooling tower power, and RAPS calculates the PUE. The ``cooling`` section of the system config (see :doc:`RAPS`) tells RAPS which FMU to load and how its variables map to RAPS output.

To get the example FMUs into RAPS, run ``make fetch-example-fmus`` in the RAPS repository. It downloads the ``fmus`` folder of POWER9CSM to ``models/POWER9CSM/fmus``. The Frontier FMU is not part of POWER9CSM; the Frontier system config expects it in the ``fmu-models`` repository (``make fetch-fmu-models``, which needs ORNL access). Then enable cooling with ``-c``:

.. code-block:: shell-session

   $ raps run --system marconi100 -c

Contributors
------------

Vineet Kumar, Michael Scott Greenwood, Wesley Brewer, Wesley Williams, Nathan Parkison, David Grant, Oak Ridge National Laboratory.
