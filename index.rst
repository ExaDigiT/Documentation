.. ExaDigiT documentation master file, created by
   sphinx-quickstart on Wed Apr 24 22:19:44 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. figure:: ExaDigiTUE5/pictures/FrontierDigitalTwin.JPG
   :align: center
   :width: 100%
   :alt: Frontier digital twin view

   
ExaDigiT documentation
====================================

ExaDigiT is a digital twin of supercomputers and their thermal infrastructures. It offers insights into operational strategies, "what-if" scenarios, as well as elucidates complex, cross-disciplinary transient behaviors. It also serves as a design tool for future system prototyping.
It combines telemetry and simulations, providing a virtual representation of physical systems. It supports planning, construction, and operations, offering value in decision-making, predictive maintenance, and system efficiency. In design stages, it can evaluate energy efficiency, virtually prototype cooling systems, and model network performance. During operations, ExaDigiT aids in predictive maintenance and operational optimization.

ExaDigiT is built on an open software stack (Modelica, SST Macro, Unreal Engine) with an aim to foster community-driven development, we have formed a partnership with national supercomputer centers (ORNL, LLNL, LANL (USA), PAWSEY (Australia), LUMI (Finland), CINES (France) , CINECA (Italy), ...) around the world to develop an open framework for modeling supercomputers.

ExaDigiT architecture overview:
---------------------------------------

.. figure:: ExaDigiTUE5/pictures/ExadigitComponents.JPG
   :align: center
   :width: 100%
   :alt: ExaDigiT components and their interactions




         
ExaDigiT uses four primary components:
---------------------------------------


    - **RAPS**: Resource Allocator and Power Simulator (https://code.ornl.gov/exadigit/raps) to model workloads, energy usage, and energy conversion losses.

    - **Cooling Model with Modelica FMU** (AutoCSM https://code.ornl.gov/exadigit/AutoCSM, LBNL https://github.com/lbl-srg/modelica-buildingsL, TRANSFORM https://github.com/ORNL-Modelica/TRANSFORM-Library) transient thermo-fluid simulation to model the cooling system from the cooling tower to the cold plate.

    - A network digital twin to simulate network power and congestion.

    - **ExaDigiTUE5**: A visual analytics module (https://code.ornl.gov/exadigit/exadigitue5) using Unreal Engine 5 for augmented reality and a web-based dashboard for experiments.



The schema above shows the architectural overview of the various components of ExaDigiT. There are three main modules that
we develop:  RAPS,  a cooling model, and  visual
analytics capabilities. The RAPS module can replay workloads
from telemetry, reschedule them, or simulate synthetic work-
loads on the supercomputer to analyze the resulting energy
consumption; further details are provided in Section III-B. The
cooling model simulates thermo-fluid dynamics and control
of the Central Energy Plant (CEP), which itself includes
three components:  a thermo-fluid model for predicting
temperatures (T ), pressures (Π), and flow rates (Q);  a
control system model for predicting the staging of cooling
towers, hot/cold water pumps, and heat exchangers; and 
a sub-module for predicting the system PUE. Both RAPS and
the cooling model can be interfaced either via a terminal
console, the web-based dashboard, or the ExadigitUE5 augmented reality
environment for visual insights.
         
.. toctree::
   :maxdepth: 1
   :hidden:

   RAPS
   coolingModel
   NetworkDT
   ExaDigiTUE5


