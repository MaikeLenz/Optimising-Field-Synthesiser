import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna import *

"""
Won't work until we add duration into BO
"""
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_duration_vs_rms_width.csv")
τfwhms = df.iloc[:,0]
energies = df.iloc[:,1]
widths = df.iloc[:,2]

# Plot data
plt.imshow(widths, extent=(np.amin(τfwhms)*10**15, np.amax(τfwhms)*10**15,np.amin(energies)*10**3, np.amax(energies)*10**3), aspect = 'auto', origin="lower")
plt.xlabel("Pulse duration, fs")
plt.ylabel("Pulse energy, mJ")
#legend
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

# Run BO
params=[ "τfwhm", "energy"]

#values:  radius, flength, gas, pressure, wavelength, GDD, energy
initial_values_HCF=[125e-6, 1, "Ne", 2.340607, 800e-9, 0, 0.1e-3]

Luna_BO(params, initial_values_HCF, function=max_bandwidth, init_points=1, n_iter=1)

# Then plot point found by BO onto the figure
