import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

f, axs = plt.subplots(1,3)

df_E_P = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\energy_pressure_GDD_BO\\Ne_energy_pressure.csv")
energies = df_E_P.iloc[:,0].values
pressures = df_E_P.iloc[:,1].values
widths_E_P = df_E_P.iloc[:,2].values
num_points = 20
widths_E_P_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_E_P_shaped[i] = widths_E_P[i*20:20+i*20]

#plt.figure()
axs[0].imshow(widths_E_P_shaped, extent=(np.amin(pressures), np.amax(pressures),np.amin(energies), np.amax(energies)), aspect = 'auto', origin="lower", vmin=0, vmax=5e14)
axs[0].set_xlabel("Pressure, bar")
axs[0].set_ylabel("Pulse energy, mJ")
#cbar = plt.colorbar()
#cbar.ax.set_ylabel('Angular Frequency Bandwidth, /s', rotation=270, labelpad=15)

df_E_G = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\energy_pressure_GDD_BO\\Ne_energy_grating.csv")
energies = df_E_G.iloc[:,0].values
grating_positions = df_E_G.iloc[:,1].values
widths_E_G = df_E_G.iloc[:,2].values
num_points = 20
widths_E_G_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_E_G_shaped[i] = widths_E_G[i*20:20+i*20]

#plt.figure()
axs[1].imshow(widths_E_G_shaped, extent=(np.amin(energies), np.amax(energies) ,np.amin(grating_positions)*(10**3), np.amax(grating_positions)*(10**3)), aspect = 'auto', origin="lower", vmin=0, vmax=5e14)
axs[1].set_xlabel("Pulse energy, mJ")
axs[1].set_ylabel("Compressor Grating Position, mm")
#cbar = plt.colorbar()
#cbar.ax.set_ylabel('Angular Frequency Bandwidth, /s', rotation=270, labelpad=15)

df_P_G = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\energy_pressure_GDD_BO\\Ne_pressure_grating.csv")
pressures = df_P_G.iloc[:,0].values
grating_positions = df_P_G.iloc[:,1].values
widths_P_G = df_P_G.iloc[:,2].values
num_points = 20
widths_P_G_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_P_G_shaped[i] = widths_P_G[i*20:20+i*20]

#plt.figure()
im = axs[2].imshow(widths_P_G_shaped, extent=(np.amin(pressures), np.amax(pressures),np.amin(grating_positions)*(10**3), np.amax(grating_positions)*(10**3)), aspect = 'auto', origin="lower", vmin=0, vmax=5e14)
axs[2].set_xlabel("Pressure, bar")
axs[2].set_ylabel("Compressor Grating Position, mm")

cbar = f.colorbar(im, orientation='vertical')
cbar.ax.set_ylabel('Angular Frequency Bandwidth, /s', rotation=270, labelpad=15)
plt.suptitle('Simulated 2D Parameter Scans', fontsize=24)

plt.show()

"""
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_pressure_vs_rms_width.csv")
pressures = df.iloc[:,0].values
energies = df.iloc[:,1].values
widths = df.iloc[:,2].values
"""
