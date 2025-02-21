import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.interpolate import interp1d
from scipy import integrate
import os
import sys
import re
import csv

# Constants
timestamp_col = 0 # column 0
Joules_col = 24 # column 24
counters_born = 32 # column 32
quantum_duration = 20 # seconds


infile_csv = "g1152.pm_counters.log"
outfile_csv = "g1152.RAPS.csv"
node_name = re.sub(r"\.pm_counters\.log$", "", infile_csv)

Node = pd.read_csv(infile_csv, sep='[ ;]', engine="python",header=None)       
        
timestamps = Node.iloc[:,timestamp_col]  # view on column 0
Joules = Node.iloc[:,Joules_col]  # view on column 24

# keep Joules growing even when a reset occurs and create two midpoints for the corresponding interval of time
offset=0
midpoints = []     
midpoints.append(Node.iloc[0,timestamp_col] )
for i in range(2,len(timestamps)):            
    # if a reset on the pm_counter occured
    if  i >= 2 and Joules[i-2] - Joules[i-1] > offset: 
        offset += Joules[i-2]
        Node.iloc[i-1,timestamp_col] = int(Node.iloc[i-1,counters_born] / 1000000.0) # set first timestamp when counters were reset
        Node.iloc[i-1,Joules_col] = offset 
        print(f'offset = {offset} i = {i}')
    else:
        Node.iloc[i-1,Joules_col] += offset
    midpoints.append( timestamps[i-2]+0.01)  
    midpoints.append( timestamps[i-1] )
                   
Node.iloc[-1,Joules_col] += offset 
midpoints.append(Node.iloc[-1,timestamp_col] )


# Compute the derivative of Joules to obtain Watts
derivative = []
dy = Joules[1] - Joules[0]
dt = timestamps[1] - timestamps[0]
derivative.append(dy / dt)       
for i in range(1, len(timestamps)-1):
    # Check if the current time is going reverse or energy is negative
    if timestamps[i] <= timestamps[i-1] or Joules[i] < Joules[i-1]:
        derivative.append(np.nan)
        derivative.append(np.nan)
        print(f'!!!!!!!!!!!! Nan timestamps {timestamps[i]} {timestamps[i-1]} or node Joules {Node.iloc[i,Joules_col]} {Node.iloc[i-1,Joules_col]}')
    else:
        # Calculate the derivative
        dy = Joules[i] - Joules[i-1]
        dt = timestamps[i] - timestamps[i-1]
        derivative.append(dy / dt)
        derivative.append(dy / dt)
        
dy = Joules.iat[-2] - Joules.iat[-1]
dt = Node.iloc[-2,timestamp_col] - Node.iloc[-1,timestamp_col]
derivative.append(dy / dt)        

# Interpolate Watts and create a resampled derivative list of Watts every 20 seconds in thanks to range(x_start+10, x_end-10,20)
interp_func = interp1d(midpoints, derivative, kind='linear', bounds_error=False,fill_value=np.nan)
x_start = int(midpoints[0])
if x_start % quantum_duration != 0:
    x_start += (quantum_duration - x_start %quantum_duration)    
x_end = int(midpoints[-1])
if x_end % quantum_duration != 0:
    x_end += (quantum_duration - x_end %quantum_duration)        
x = []
for t in range(x_start+10, x_end-10,20):
    x.append(t)        
derivative_resampled = interp_func(x)       
for i, val in enumerate(derivative_resampled):
    if np.isnan(val):  # Check if interpolation failed (out of bounds)
        print(f'derivative nan {i}')   #derivative_resampled[i] = y[i]
        

# Create a CSV file for RAPS with Watts sampled every 20 seconds for one compute node
outfd_csv = open(outfile_csv, mode='w', newline='', encoding='utf-8') 
outwriter = csv.writer(outfd_csv)     
# In the outfile_csv, Write the selected columns for each row
for i in range(0,len(midpoints)):
    selected_columns = [midpoints[i],derivative[i]]
    outwriter.writerow(selected_columns)
outfd_csv.close()


# Plot the dataframe and capture the Axes object
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, derivative_resampled,label="derivée du cumul Joules interpolé toutes les 20 s",marker='x')
ax.plot(midpoints, derivative,label="derivée du cumul Joules ~ toutes les 60 s",marker='s')
plt.title(f"{node_name} Comparaison selon les sources de données")
plt.xlabel("Number of seconds since 1970")
plt.ylabel("Watt")
plt.legend(fontsize="small", loc="upper center", ncol=1, bbox_to_anchor=(1, 1))  # Légende

# Add a grid with both major and minor lines
ax.grid(True, which='major', linestyle='-', linewidth=0.75, alpha=0.8)  # Major grid
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.6)  # Minor grid

# Set up dynamic minor tick locators
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

# Rotate X-axis labels and dynamically update absolute labels
def update_labels(event):
    """
    Updates the X-axis labels to show absolute values dynamically when the view changes.
    """
    # Get the current view limits
    xmin, xmax = ax.get_xlim()
    
    # Update the ticks based on the current limits
    ticks = np.linspace(xmin-xmin%20, xmax+20-xmax%20, num=40)  # Adjust the number of ticks as needed
    ax.set_xticks(ticks)  # Set tick positions
    ax.set_xticklabels([f"{int(tick)}" for tick in ticks], rotation=90)  # Set absolute tick labels
    
    # Redraw the canvas
    fig.canvas.draw_idle()

# Connect the update_labels function to the xlim_changed event
ax.callbacks.connect('xlim_changed', update_labels)

# Tight layout for better display
plt.tight_layout()

# Show the plot
plt.show()
