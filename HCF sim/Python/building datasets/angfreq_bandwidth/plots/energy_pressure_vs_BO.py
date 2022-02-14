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

df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_pressure_vs_rms_width.csv")
pressures = df.iloc[:,0].values
energies = df.iloc[:,1].values
widths = df.iloc[:,2].values

"""
# Run BO
params=["pressure", "energy"]

#values:  radius, flength, gas, pressure, wavelength, GDD, energy
initial_values_HCF=[125e-6, 1, "Ne", 2.340607, 800e-9, 0, 0.5e-3]
τfwhm = 30e-15 # FWHM durations of the pump pulse

Luna_BO(params, initial_values_HCF, Gaussian=True, FWHM=τfwhm, function=max_bandwidth, init_points=100, n_iter=100)
"""
# Then plot point found by BO onto the figure
# After init_points=10, n_iter=0: (Random search)
width0 = 1.8086054432613795e-07
energy0 = 0.00010021731215295529
pressure0 = 5.232656016845757

# After init_points=10, n_iter=5:
width5 = 1.808605497098563e-07
energy5 =  0.00037883619255251475
pressure5 = 2.292740326763169

# After init_points=10, n_iter=10:
width10 = 1.8086056478246469e-07
energy10 = 0.0004538944016175747
pressure10 = 5.837850178602668

# After init_points=10, n_iter=100:
width100 = 1.8086056183140002e-07
energy100 = 0.001039414750035517
pressure100 = 2.2776823585771977

# After init_points=100, n_iter=100:
width100_rep = 1.8086057420846162e-07
energy100_rep = 0.0013934507706072274
pressure100_rep = 12.303031785957677

num_points = 20
widths_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_shaped[i] = widths[i*20:20+i*20]

# Plot data
plt.imshow(widths_shaped, extent=(np.amin(pressures), np.amax(pressures),np.amin(energies), np.amax(energies)), aspect = 'auto', origin="lower")
plt.xlabel("Pressure, bar")
plt.ylabel("Pulse energy, mJ")
#legend
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.scatter(pressure0, energy0*(10**3), s=100, marker='o', label='n_init = 10, n_iter = 0')
plt.scatter(pressure5, energy5*(10**3), s=100, marker='o', label='n_init = 10, n_iter = 5')
plt.scatter(pressure10, energy10*(10**3), s=100, marker='o', label='n_init = 10, n_iter = 10')
plt.scatter(pressure100, energy100*(10**3), s=100, marker='o', label='n_init = 10, n_iter = 100')
plt.scatter(pressure100_rep, energy100_rep*(10**3), s=100, marker='o', label='n_init = 100, n_iter = 100')
plt.legend()

plt.show()
