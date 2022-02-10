import pandas as pd
from matplotlib import pyplot as plt

df_duration = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\duration_vs_rms_width.csv")
df_energy = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_vs_rms_width.csv")
df_flength = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\flength_vs_rms_width.csv")
df_pressure = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\pressure_vs_rms_width.csv")
df_radius = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\radius_vs_rms_width.csv")
df_wavelength = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\wavelength_vs_rms_width.csv")

f = plt.figure(constrained_layout=True)
layout=[2,3]
gs = f.add_gridspec(layout[0],layout[1])


f_ax1 = f.add_subplot(gs[0,0])
f_ax2 = f.add_subplot(gs[0,1])
f_ax3 = f.add_subplot(gs[0,2])
f_ax4 = f.add_subplot(gs[1,0])
f_ax5 = f.add_subplot(gs[1,1])
f_ax6 = f.add_subplot(gs[1,2])

ymin = 0
ymax = 3.5e16
f_ax1.set_ylim([ymin, ymax])
f_ax2.set_ylim([ymin, ymax])
f_ax3.set_ylim([ymin, ymax])
f_ax4.set_ylim([ymin, ymax])
f_ax5.set_ylim([ymin, ymax])
f_ax6.set_ylim([ymin, ymax])


f_ax1.plot(df_duration.iloc[:,0], df_duration.iloc[:,1], label='Luna')
f_ax1.plot(df_duration.iloc[:,0], df_duration.iloc[:,2], label='Theoretical')
f_ax1.set_xlabel('Pulse duration, fs')

f_ax2.plot(df_energy.iloc[:,0], df_energy.iloc[:,1], label='Luna')
f_ax2.plot(df_energy.iloc[:,0], df_energy.iloc[:,2], label='Theoretical')
f_ax2.set_xlabel('Pulse energy, mJ')

f_ax3.plot(df_flength.iloc[:,0], df_flength.iloc[:,1], label='Luna')
f_ax3.plot(df_flength.iloc[:,0], df_flength.iloc[:,2], label='Theoretical')
f_ax3.set_xlabel('Fibre Length, m')

f_ax4.plot(df_pressure.iloc[:,0], df_pressure.iloc[:,1], label='Luna')
f_ax4.plot(df_pressure.iloc[:,0], df_pressure.iloc[:,2], label='Theoretical')
f_ax4.set_xlabel('Pressure, bar')

f_ax5.plot(df_radius.iloc[:,0], df_radius.iloc[:,1], label='Luna')
f_ax5.plot(df_radius.iloc[:,0], df_radius.iloc[:,2], label='Theoretical')
f_ax5.set_xlabel('Core radius, um')

f_ax6.plot(df_wavelength.iloc[:,0], df_wavelength.iloc[:,1], label='Luna')
f_ax6.plot(df_wavelength.iloc[:,0], df_wavelength.iloc[:,2], label='Theoretical')
f_ax6.set_xlabel('Wavelength, nm')
plt.legend()


plt.suptitle("Parameter vs Bandwidth for Luna Simulation")
plt.show()