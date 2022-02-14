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


# Run BO
params=["pressure", "energy"]

#values:  radius, flength, gas, pressure, wavelength, GDD, energy
initial_values_HCF=[125e-6, 1, "Ne", 2.340607, 800e-9, 0, 0.5e-3]

Luna_BO(params, initial_values_HCF, function=max_bandwidth, init_points=10, n_iter=100)

# Then plot point found by BO onto the figure
# After init_points=10, n_iter=0: (Random search)
width0 = 8.82001549724403e-07
energy0 = 0.00010021731215295529
pressure0 = 5.232656016845757

# After init_points=10, n_iter=5:
width5 = 8.820269893611299e-07
energy5 =  0.0018277151208271087
pressure5 = 8.820792709866982

# After init_points=10, n_iter=10:
width10 = 8.819891998207039e-07
energy10 = 0.001288983323577848
pressure10 = 14.997829386205092

# After init_points=10, n_iter=100:
width100 = 8.819891998207039e-07
energy100 = 0.001288983323577848
pressure100 = 14.997829386205092


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

plt.scatter(pressure0, energy0*(10**3), s=100, c='tab:purple', marker='o', label='0')
plt.scatter(pressure5, energy5*(10**3), s=100, c='tab:blue', marker='o', label='5')
plt.scatter(pressure10, energy10*(10**3), s=100, c='tab:green', marker='o', label='10')
plt.scatter(pressure100, energy100*(10**3), s=100, c='tab:red', marker='o', label='100')
plt.legend()

plt.show()