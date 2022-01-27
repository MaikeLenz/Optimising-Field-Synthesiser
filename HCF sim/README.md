# DWG-Optimisation
This project started work towards optimising parameters of the Luna prop_capillary method.

Current Progress: 
<br />
- Interactive comparison plots for a single mode of the signal. The peak gives some indication of how effective 
the paremeters are at minimising peak wavelength.
Default values are assigned for all but 1 parameter, which is varied about its default value.

- We have also been able to run the simulation via a python script, allowing for plotting and optimisation in python.


## Files to Run:
### DUV_comparison_plots.jl
Interactive plotting tool. Allows comparison of how different parameters vary the single mode of the signal.
### Sim_python
Runs the Luna prop_capillary julia method in python natively.
### RDWemission_DUV.jl
An original Luna example file, used to run an example simulation and plot the data in various ways.


<br />

## Additional files 
### API_example.py
An example of how the Julia-Python API works to act as reference for future progress.
### Playground.jl
A simple julia file, used in the API_example.py file to illustrate how julia functions defined in a script can be run in Python
### time_1d_edit.jl
The Luna function time_1d was edited to allow for multiple plots to be made on the same figure. Additional 
functions used in DUV_comparison_plots.jl were also defined in the file.
### plotparams.py
Attractive matplotlib.pyplot parameters for plotting in Python.

## Plots
There are 2 folders containing plots:
### LunaPlots
The output files from the RDWemission_DUV.jl file.
### ComparisonPlots
The output files from the DUV_comparison_plots.jl file. In these instances, the options are set as "all" (ie plot all parameters), and "0.2" (ie maximum difference from default value is 0.2).
