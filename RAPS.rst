Resource Allocator and Power Simulator (RAPS)
===========================================================

RAPS is one of the modules used by the ExaDigiT framework.
RAPS is a python code that either simulates workloads or replays historical workloads from system telemetry, and is able to predict dynamic energy consumption, as well as interact with the cooling model to predict cooling system behavior. Such a tool can be used together with reinforcement learning algorithms to provide an end-to-end optimization tool for data centers.

Installation
------------

.. code-block:: shell-session

   # Requires Python version >= 3.9
   $ git clone https://code.ornl.gov/exadigit/raps
   $ cd raps
   $ pip install -e .

Quickstart
----------
.. code-block:: shell-session

   # Download dataset (270MB) related to Marconi supercomputer
   $ wget https://zenodo.org/records/10127767/files/job_table.parquet
   $ python main.py --system marconi100 -f job_table.parquet

   
Command line flags
------------------

.. literalinclude:: RAPS.usage.txt
  :language: shell


  



Developpers
-----------

Brewer Wesley, Maiterth Mathias, Bouknight Sedrick, Hines Jesse, Webb Tyler
