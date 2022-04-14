import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

df_duration = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\duration_vs_rms_width.csv")
df_energy = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\energy_vs_rms_width.csv")
df_flength = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\flength_vs_rms_width.csv")
df_pressure = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\pressure_vs_rms_width.csv")
df_radius = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\radius_vs_rms_width.csv")
df_wavelength = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\wavelength_vs_rms_width.csv")

f = plt.figure(constrained_layout=True)
layout=[2,3]
gs = f.add_gridspec(layout[0],layout[1])

f_ax1 = f.add_subplot(gs[0,0])
f_ax2 = f.add_subplot(gs[0,1])
f_ax3 = f.add_subplot(gs[0,2])
f_ax4 = f.add_subplot(gs[1,0])
f_ax5 = f.add_subplot(gs[1,1])
f_ax6 = f.add_subplot(gs[1,2])

f_ax1.set_ylabel('RMS Width (/s)', fontsize=16)
f_ax4.set_ylabel('RMS Width (/s)', fontsize=16)

ymin = 0
ymax = 1e16
f_ax1.set_ylim([ymin, ymax])
f_ax2.set_ylim([ymin, ymax])
f_ax3.set_ylim([ymin, ymax])
f_ax4.set_ylim([ymin, ymax])
f_ax5.set_ylim([ymin, ymax])
f_ax6.set_ylim([ymin, ymax])

f_ax1.xaxis.set_tick_params(labelsize=12)
f_ax1.yaxis.set_tick_params(labelsize=12)
f_ax2.xaxis.set_tick_params(labelsize=12)
f_ax2.yaxis.set_tick_params(labelsize=12)
f_ax3.xaxis.set_tick_params(labelsize=12)
f_ax3.yaxis.set_tick_params(labelsize=12)
f_ax4.xaxis.set_tick_params(labelsize=12)
f_ax4.yaxis.set_tick_params(labelsize=12)
f_ax5.xaxis.set_tick_params(labelsize=12)
f_ax5.yaxis.set_tick_params(labelsize=12)
f_ax6.xaxis.set_tick_params(labelsize=12)
f_ax6.yaxis.set_tick_params(labelsize=12)


f_ax1.plot(df_duration.iloc[:,0][8:], df_duration.iloc[:,1][8:], '+', label='Luna')
f_ax1.plot(df_duration.iloc[:,0][8:], df_duration.iloc[:,2][8:], '+', label='Theoretical')
f_ax1.set_xlabel('Pulse Duration (fs)', fontsize=16)

f_ax2.plot(df_energy.iloc[:,0], df_energy.iloc[:,1], '+', label='Luna')
f_ax2.plot(df_energy.iloc[:,0], df_energy.iloc[:,2], '+', label='Theoretical')
f_ax2.set_xlabel('Pulse Energy (mJ)', fontsize=16)

f_ax3.plot(df_flength.iloc[:,0][:50], df_flength.iloc[:,1][:50], '+', label='Luna')
f_ax3.plot(df_flength.iloc[:,0][:50], df_flength.iloc[:,2][:50], '+', label='Theoretical')
f_ax3.set_xlabel('Fibre Length (m)', fontsize=16)

f_ax4.plot(df_pressure.iloc[:,0], df_pressure.iloc[:,1], '+', label='Luna')
f_ax4.plot(df_pressure.iloc[:,0], df_pressure.iloc[:,2], '+', label='Theoretical')
f_ax4.set_xlabel('Pressure (bar)', fontsize=16)

f_ax5.plot(df_radius.iloc[:,0], df_radius.iloc[:,1], '+', label='Luna')
f_ax5.plot(df_radius.iloc[:,0], df_radius.iloc[:,2], '+', label='Theoretical')
f_ax5.set_xlabel('Fibre Radius (μm)', fontsize=16)

f_ax6.plot(df_wavelength.iloc[:,0], df_wavelength.iloc[:,1], '+', label='Luna Simulation')
f_ax6.plot(df_wavelength.iloc[:,0], df_wavelength.iloc[:,2], '+', label='Theoretical')
f_ax6.set_xlabel('Central Wavelength (nm)', fontsize=16)
f_ax1.legend(fontsize=16)

print(len(df_duration.iloc[:,0]))
print(len(df_flength.iloc[:,0]))

#plt.suptitle("Parameters vs Bandwidth for the Luna Simulation", fontsize=24)
plt.show()