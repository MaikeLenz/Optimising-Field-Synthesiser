import pandas as pd
from matplotlib import pyplot as plt
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
df_duration = pd.read_csv("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\duration_vs_rms_width.csv")
df_energy = pd.read_csv("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\energy_vs_rms_width.csv")
df_flength = pd.read_csv("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\flength_vs_rms_width.csv")
df_pressure = pd.read_csv("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\pressure_vs_rms_width.csv")
df_radius = pd.read_csv("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\radius_vs_rms_width.csv")
df_wavelength = pd.read_csv("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\data\\wavelength_vs_rms_width.csv")

f = plt.figure(constrained_layout=True)
layout=[2,3]
gs = f.add_gridspec(layout[0],layout[1])

f_ax1 = f.add_subplot(gs[0,0])
f_ax2 = f.add_subplot(gs[0,1])
f_ax3 = f.add_subplot(gs[0,2])
f_ax4 = f.add_subplot(gs[1,0])
f_ax5 = f.add_subplot(gs[1,1])
f_ax6 = f.add_subplot(gs[1,2])

f_ax1.set_ylabel('RMS Width (rad/s)', fontsize=20)
f_ax2.set_ylabel('RMS Width (rad/s)', fontsize=20)
f_ax3.set_ylabel('RMS Width (rad/s)', fontsize=20)
f_ax5.set_ylabel('RMS Width (rad/s)', fontsize=20)
f_ax6.set_ylabel('RMS Width (rad/s)', fontsize=20)
f_ax4.set_ylabel('RMS Width (rad/s)', fontsize=20)

ymin = 0
ymax = 0.8e16
f_ax1.set_ylim([ymin, ymax])
f_ax2.set_ylim([ymin, ymax])
f_ax3.set_ylim([ymin, ymax])
f_ax4.set_ylim([ymin, ymax])
f_ax5.set_ylim([ymin, ymax])
f_ax6.set_ylim([ymin, ymax])

f_ax1.xaxis.set_tick_params(labelsize=18)
f_ax1.yaxis.set_tick_params(labelsize=18)
f_ax2.xaxis.set_tick_params(labelsize=18)
f_ax2.yaxis.set_tick_params(labelsize=18)
f_ax3.xaxis.set_tick_params(labelsize=18)
f_ax3.yaxis.set_tick_params(labelsize=18)
f_ax4.xaxis.set_tick_params(labelsize=18)
f_ax4.yaxis.set_tick_params(labelsize=18)
f_ax5.xaxis.set_tick_params(labelsize=18)
f_ax5.yaxis.set_tick_params(labelsize=18)
f_ax6.xaxis.set_tick_params(labelsize=18)
f_ax6.yaxis.set_tick_params(labelsize=18)


f_ax1.plot(df_duration.iloc[:,0][8:], df_duration.iloc[:,1][8:], '--',color='m', label='Luna')
f_ax1.plot(df_duration.iloc[:,0][8:], df_duration.iloc[:,2][8:], color='black', label='SPM Theory')
f_ax1.axvline(x=30,color="lightgrey",dashes=[5,5])
f_ax1.set_xlabel('Pulse Duration (fs)', fontsize=20)

f_ax2.plot(df_energy.iloc[:,0], df_energy.iloc[:,1], '--',color='m', label='Luna')
f_ax2.plot(df_energy.iloc[:,0], df_energy.iloc[:,2], color='black', label='Theoretical')
f_ax2.axvspan(0.1, 1.2, alpha=0.5, color='lightgrey')
f_ax2.set_xlabel('Pulse Energy (mJ)', fontsize=20)

f_ax3.plot(df_flength.iloc[:,0][:50], df_flength.iloc[:,1][:50],'--', color='m', label='Luna')
f_ax3.plot(df_flength.iloc[:,0][:50], df_flength.iloc[:,2][:50], color='black', label='Theoretical')
f_ax3.axvline(x=1.05,color="lightgrey",dashes=[5,5])
f_ax3.set_xlabel('Fibre Length (m)', fontsize=20)

f_ax4.plot(df_pressure.iloc[:,0], df_pressure.iloc[:,1],'--', color='m', label='Luna')
f_ax4.plot(df_pressure.iloc[:,0], df_pressure.iloc[:,2], color='black', label='Theoretical')
f_ax4.axvspan(1, 3.5, alpha=0.5, color='lightgrey')
f_ax4.set_xlabel('Pressure (bar)', fontsize=20)

f_ax5.plot(df_radius.iloc[:,0], df_radius.iloc[:,1],'--', color='m', label='Luna')
f_ax5.plot(df_radius.iloc[:,0], df_radius.iloc[:,2], color='black', label='Theoretical')
f_ax5.axvline(x=175,color="lightgrey",dashes=[5,5])
f_ax5.set_xlabel('Fibre Core Radius (μm)', fontsize=20)

f_ax6.plot(df_wavelength.iloc[:,0], df_wavelength.iloc[:,1], '--',color='m', label='Luna Simulation')
f_ax6.plot(df_wavelength.iloc[:,0], df_wavelength.iloc[:,2],  color='black', label='Theoretical')
f_ax6.axvline(x=790,color="lightgrey",dashes=[5,5])
f_ax6.set_xlabel('Central Wavelength (nm)', fontsize=20)
f_ax1.legend(fontsize=20)

print(len(df_duration.iloc[:,0]))
print(len(df_flength.iloc[:,0]))

#plt.suptitle("Parameters vs Bandwidth for the Luna Simulation", fontsize=24)
plt.show()