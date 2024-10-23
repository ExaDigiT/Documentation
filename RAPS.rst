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


Raps input data format
----------

Raps requires a certain amount of data on a series of jobs in order to function.  


This requires a list of jobs, where each job has the following information (as a job_dict structure descrived below):

- **Number of nodes** : used by the job (integer)
- **Name** : job name (string)
- **Cpu_trace** : either a trace in the granularity of a trace quanta, or a single value , either in the range [0,N_CPUs]
- **Gpu_trace**  : same as cpu_trace, either a list/np.ndarray of floats or a single float, either in the range  [0,N_GPUs]
- **Wall_time** : job duration in seconds (integer)
- **State** : completion state at the end of the job (String)
- **Scheduled_nodes** : list of nodes assigned to the job or None (by node index) (String)
- **Time_offset** : the submit time, or when the job enters the queue
- **job_id** :  (integer or string)
- **priority** : priority of the job (integer)

To read data from your cluster in Raps, you need to declare your cluster and associate a dataloader with it. Dataloader will format the data from your cluster in raps format.

The power utilization is computed from the **cpu_trace** and **gpu_trace** and each value in the trace is a percentage between 0 and N_CPUs / 0 and N_GPUs receptively.

If the trace (CPU and GPU) provides a single value, constant utilization is assumed for the duration of the job.

Given these trace values the power is computed given:

**raps/config/frontier/power.json** (Needs to be created to for your system, while enabling your system with the --system cli parameter)

This means that you need to look up the configuration of your system and adjust these values.

Everything but CPU and GPU is considered constant at the moment.
  
.. code-block:: shell-session

   def job_dict(nodes_required, name, cpu_trace, gpu_trace, wall_time, \
             end_state, scheduled_nodes, time_offset, job_id, priority=0):
       """ Return job info dictionary """
       return {
           'nodes_required': nodes_required,
           'name': name,
           'cpu_trace': cpu_trace,
           'gpu_trace': gpu_trace,
           'wall_time': wall_time,
           'end_state': end_state,
           'requested_nodes': scheduled_nodes,
           'submit_time': time_offset,
           'id': job_id,
           'priority': priority
       }


Developpers
-----------

Brewer Wesley, Maiterth Mathias, Bouknight Sedrick, Hines Jesse, Webb Tyler
