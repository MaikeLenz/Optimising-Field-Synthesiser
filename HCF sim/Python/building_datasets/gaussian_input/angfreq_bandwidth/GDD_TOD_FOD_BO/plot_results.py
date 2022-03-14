import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

f, axs = plt.subplots(1,3)

df_GDD_TOD = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\GDD_TOD_FOD_BO\\Ne_GDD_TOD.csv")
GDDs = df_GDD_TOD.iloc[:,0].values
TODs = df_GDD_TOD.iloc[:,1].values
widths_GDD_TOD = df_GDD_TOD.iloc[:,2].values
num_points = 20
widths_GDD_TOD_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_GDD_TOD_shaped[i] = widths_GDD_TOD[i*20:20+i*20]

#plt.figure()
im1 = axs[0].imshow(widths_GDD_TOD_shaped, extent=(np.amin(GDDs), np.amax(GDDs),np.amin(TODs), np.amax(TODs)), aspect = 'auto', origin="lower", vmin=2.9e14, vmax=3.4e14)
axs[0].set_xlabel("GDD, fs^2")
axs[0].set_ylabel("TOD, fs^3")
#cbar = plt.colorbar()
#cbar.ax.set_ylabel('Angular Frequency Bandwidth, /s', rotation=270, labelpad=15)

df_GDD_FOD = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\GDD_TOD_FOD_BO\\NE_GDD_FOD.csv")
GDDs = df_GDD_FOD.iloc[:,0].values
FODs = df_GDD_FOD.iloc[:,1].values
widths_GDD_FOD = df_GDD_FOD.iloc[:,2].values
num_points = 20
widths_GDD_FOD_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_GDD_FOD_shaped[i] = widths_GDD_FOD[i*20:20+i*20]

#plt.figure()
im2 = axs[1].imshow(widths_GDD_FOD_shaped, extent=(np.amin(GDDs), np.amax(GDDs) ,np.amin(FODs), np.amax(FODs)), aspect = 'auto', origin="lower", vmin=2.9e14, vmax=3.4e14)
axs[1].set_xlabel("GDD, fs^2")
axs[1].set_ylabel("FOD, fs^4")
#cbar = plt.colorbar()
#cbar.ax.set_ylabel('Angular Frequency Bandwidth, /s', rotation=270, labelpad=15)

df_TOD_FOD = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\GDD_TOD_FOD_BO\\Ne_TOD_FOD.csv")
TODs = df_TOD_FOD.iloc[:,0].values
FODs = df_TOD_FOD.iloc[:,1].values
widths_TOD_FOD = df_TOD_FOD.iloc[:,2].values
num_points = 20
widths_TOD_FOD_shaped = np.zeros((num_points,num_points))
for i in range(num_points):
    widths_TOD_FOD_shaped[i] = widths_TOD_FOD[i*20:20+i*20]

#plt.figure()
im3 = axs[2].imshow(widths_TOD_FOD_shaped, extent=(np.amin(TODs), np.amax(TODs),np.amin(FODs), np.amax(FODs)), aspect = 'auto', origin="lower", vmin=2.9e14, vmax=3.4e14)
axs[2].set_xlabel("TOD, fs^3")
axs[2].set_ylabel("FOD, fs^4")

cbar = f.colorbar(im3, orientation='vertical')
cbar.ax.set_ylabel('Angular Frequency Bandwidth, /s', rotation=270, labelpad=15)
plt.suptitle('Simulated 2D Parameter Scans', fontsize=24)

plt.show()

"""
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_pressure_vs_rms_width.csv")
pressures = df.iloc[:,0].values
energies = df.iloc[:,1].values
widths = df.iloc[:,2].values
"""
