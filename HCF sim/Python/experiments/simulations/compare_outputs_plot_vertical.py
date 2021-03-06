import sys
import matplotlib.pyplot as plt
import pandas as pd
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
#####################################################################################################################
# Create plots
fig_Ar_powers, axs_Ar_powers = plt.subplots(5,2)
fig_Ar_powers.suptitle('Argon Power Scan', size=24)
plt.setp(axs_Ar_powers, xlim=(310,1250))
#plt.setp(axs_Ar_powers, ylim=(0,3.8e3))
#plt.setp(axs_Ar_powers[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ar_powers[:, 0], ylabel='Intensity (a.u.)')
fig_Ar_powers.supxlabel('Wavelength (nm)', size=16)
fig_Ar_powers.supylabel('Intensity (a.u.)', size=16)
plt.setp(axs_Ar_powers[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[2,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[2,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[3,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[3,1].get_xticklabels(), visible=False)

fig_Ne_powers, axs_Ne_powers = plt.subplots(5,2)
fig_Ne_powers.suptitle('Neon Power Scan', size=24)
plt.setp(axs_Ne_powers, xlim=(350,1200))
#plt.setp(axs_Ne_powers, ylim=(0,6.8e3))
#plt.setp(axs_Ne_powers[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ne_powers[:, 0], ylabel='Intensity (a.u.)')
fig_Ne_powers.supxlabel('Wavelength (nm)', size=16)
fig_Ne_powers.supylabel('Intensity (a.u.)', size=16)
plt.setp(axs_Ne_powers[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[2,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[2,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[3,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[3,1].get_xticklabels(), visible=False)

fig_Ar_pressures, axs_Ar_pressures = plt.subplots(4,2)
fig_Ar_pressures.suptitle('Argon Pressure Scan', size=24)
plt.setp(axs_Ar_pressures, xlim=(310,1420))
#plt.setp(axs_Ar_pressures, ylim=(0,9.7e3))
#plt.setp(axs_Ar_pressures[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ar_pressures[:, 0], ylabel='Intensity (a.u.)')
fig_Ar_pressures.supxlabel('Wavelength (nm)', size=16)
fig_Ar_pressures.supylabel('Intensity (a.u.)', size=16)
plt.setp(axs_Ar_pressures[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[2,0].get_xticklabels(), visible=False)

fig_Ne_pressures, axs_Ne_pressures = plt.subplots(7,2)
fig_Ne_pressures.suptitle('Neon Pressure Scan', size=24)
plt.setp(axs_Ne_pressures, xlim=(350,1050))
#plt.setp(axs_Ne_pressures, ylim=(0,1.15e4))
#plt.setp(axs_Ne_pressures[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ne_pressures[:, 0], ylabel='Intensity (a.u.)')
fig_Ne_pressures.supxlabel('Wavelength (nm)', size=16)
fig_Ne_pressures.supylabel('Intensity (a.u.)', size=16)
plt.setp(axs_Ne_pressures[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[2,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[2,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[3,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[3,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[4,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[4,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[5,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_pressures[5,1].get_xticklabels(), visible=False)

fig_Ne_GDDs, axs_Ne_GDDs = plt.subplots(3,5)
fig_Ne_GDDs.suptitle('Neon GDD Scan', size=24)
#plt.setp(axs_Ne_GDDs, xlim=(0,1250))
plt.setp(axs_Ne_GDDs[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ne_GDDs[:, 0], ylabel='Intensity, a.u.')

fig_Ne_GDDs_fine, axs_Ne_GDDs_fine = plt.subplots(4,4)
fig_Ne_GDDs_fine.suptitle('Neon GDD Scan', size=24)
#plt.setp(axs_Ne_GDDs_fine, xlim=(0,1250))
plt.setp(axs_Ne_GDDs_fine[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ne_GDDs_fine[:, 0], ylabel='Intensity, a.u.')

#####################################################################################################################
# Read simulation data
Ar_sim_powers = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
Ne_sim_powers = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
Ar_sim_pressures = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
Ne_sim_pressures = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6]
GDDs = [1*0.05, 2*0.05, 3*0.05, 4*0.05, 5*0.05, 6*0.05, 7*0.05, 8*0.05, 9*0.05, 10*0.05, 11*0.05, 12*0.05, 13*0.05, 14*0.05, 15*0.05]
GDDs_fine = [6*0.05, 6*0.05 + 0.004, 6*0.05 + 0.008, 7*0.05 + 0.002, 7*0.05 + 0.006, 8*0.05, 8*0.05 + 0.004, 8*0.05 + 0.008, 9*0.05 + 0.002, 9*0.05 + 0.006, 10*0.05, 10*0.05 +0.004, 10*0.05 + 0.008, 11*0.05 + 0.002, 11*0.05 +0.006, 12*0.05]
"""
# Gaussian input simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.3")
axs_Ar_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.4")
axs_Ar_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.5")
axs_Ar_powers[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.6")
axs_Ar_powers[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.7")
axs_Ar_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.8")
axs_Ar_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_0.9")
axs_Ar_powers[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_1.0")
axs_Ar_powers[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_1.1")
axs_Ar_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_1.2")
axs_Ar_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.3")
axs_Ne_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.4")
axs_Ne_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.5")
axs_Ne_powers[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.6")
axs_Ne_powers[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.7")
axs_Ne_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.8")
axs_Ne_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_0.9")
axs_Ne_powers[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_1.0")
axs_Ne_powers[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_1.1")
axs_Ne_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_1.2")
axs_Ne_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_0.2")
axs_Ar_pressures[1,2].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_0.4")
axs_Ar_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_0.6")
axs_Ar_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_0.8")
axs_Ar_pressures[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_1.0")
axs_Ar_pressures[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_1.2")
axs_Ar_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_1.4")
axs_Ar_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_1.0")
axs_Ne_pressures[3,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_1.2")
axs_Ne_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_1.4")
axs_Ne_pressures[2,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_1.6")
axs_Ne_pressures[2,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_1.8")
axs_Ne_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_2.0")
axs_Ne_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_2.2")
axs_Ne_pressures[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_2.4")
axs_Ne_pressures[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_2.6")
axs_Ne_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_2.8")
axs_Ne_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_3.0")
axs_Ne_pressures[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_3.2")
axs_Ne_pressures[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_3.4")
axs_Ne_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_3.6")
axs_Ne_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1])
"""
#####################################################################################################################
# Pulse input simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.3")
axs_Ar_powers[4,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red', label='Luna')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.4")
axs_Ar_powers[3,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.5")
axs_Ar_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.6")
axs_Ar_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.7")
axs_Ar_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.8")
axs_Ar_powers[4,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.9")
axs_Ar_powers[3,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.0")
axs_Ar_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.1")
axs_Ar_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.2")
axs_Ar_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.3")
axs_Ne_powers[4,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red', label='Luna')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.4")
axs_Ne_powers[3,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.5")
axs_Ne_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.6")
axs_Ne_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.7")
axs_Ne_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.8")
axs_Ne_powers[4,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.9")
axs_Ne_powers[3,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.0")
axs_Ne_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.1")
axs_Ne_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.2")
axs_Ne_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.2")
axs_Ar_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.4")
axs_Ar_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.6")
axs_Ar_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.8")
axs_Ar_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red', label='Luna')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.0")
axs_Ar_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.2")
axs_Ar_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.4")
axs_Ar_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.0")
axs_Ne_pressures[6,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red', label='Luna')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.2")
axs_Ne_pressures[5,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.4")
axs_Ne_pressures[4,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.6")
axs_Ne_pressures[3,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.8")
axs_Ne_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.0")
axs_Ne_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.2")
axs_Ne_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.4")
axs_Ne_pressures[6,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.6")
axs_Ne_pressures[5,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.8")
axs_Ne_pressures[4,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.0")
axs_Ne_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.2")
axs_Ne_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.4")
axs_Ne_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.6")
axs_Ne_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1], '--', color='tab:red')
#####################################################################################################################
# Read experimental data
Ar_powers = [1.29, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
Ne_powers = [1.24, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
Ar_pressures = [1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2]
Ne_pressures = [3.6, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]

# Argon PowerScan
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Argon_0.8bar_PowerScan\\PowerScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
I1_29=columns[1]
I1_2=columns[2]
I1_1=columns[3]
I1_0=columns[4]
I0_9=columns[5]
I0_8=columns[6]
I0_7=columns[7]
I0_6=columns[8]
I0_5=columns[9]
I0_4=columns[10]
I0_3=columns[11]

# Plot experimental data
axs_Ar_powers[0,0].plot(wavel_nm, I1_2, color='black')
axs_Ar_powers[1,0].plot(wavel_nm, I1_1, color='black')
axs_Ar_powers[2,0].plot(wavel_nm, I1_0, color='black')
axs_Ar_powers[3,0].plot(wavel_nm, I0_9, color='black')
axs_Ar_powers[4,0].plot(wavel_nm, I0_8, color='black')
axs_Ar_powers[0,1].plot(wavel_nm, I0_7, color='black')
axs_Ar_powers[1,1].plot(wavel_nm, I0_6, color='black')
axs_Ar_powers[2,1].plot(wavel_nm, I0_5, color='black')
axs_Ar_powers[3,1].plot(wavel_nm, I0_4, color='black')
axs_Ar_powers[4,1].plot(wavel_nm, I0_3, color='black', label='Experiment')


# Neon PowerScan
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Neon_3bar_PowerScan\\PowerScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
I1_24=columns[1]
I1_1=columns[2]
I1_0=columns[3]
I0_9=columns[4]
I0_8=columns[5]
I0_7=columns[6]
I0_6=columns[7]
I0_5=columns[8]
I0_4=columns[9]
I0_3=columns[10]
I1_2=columns[11]

axs_Ne_powers[0,0].plot(wavel_nm, I1_2, color='black')
axs_Ne_powers[1,0].plot(wavel_nm, I1_1, color='black')
axs_Ne_powers[2,0].plot(wavel_nm, I1_0, color='black')
axs_Ne_powers[3,0].plot(wavel_nm, I0_9, color='black')
axs_Ne_powers[4,0].plot(wavel_nm, I0_8, color='black')
axs_Ne_powers[0,1].plot(wavel_nm, I0_7, color='black')
axs_Ne_powers[1,1].plot(wavel_nm, I0_6, color='black')
axs_Ne_powers[2,1].plot(wavel_nm, I0_5, color='black')
axs_Ne_powers[3,1].plot(wavel_nm, I0_4, color='black')
axs_Ne_powers[4,1].plot(wavel_nm, I0_3, color='black', label='Experiment')

# Argon PressureScan
lines=[]
columns=[[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Argon_1.1Win_PressureScan\\PressureScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
I0_2=columns[1]
I0_4=columns[2]
I0_6=columns[3]
I0_8=columns[4]
I1_0=columns[5]
I1_2=columns[6]
I1_4=columns[7]

axs_Ar_pressures[0,0].plot(wavel_nm, I1_4, color='black')
axs_Ar_pressures[1,0].plot(wavel_nm, I1_2, color='black')
axs_Ar_pressures[2,0].plot(wavel_nm, I1_0, color='black')
axs_Ar_pressures[3,0].plot(wavel_nm, I0_8, color='black', label='Experiment')
axs_Ar_pressures[0,1].plot(wavel_nm, I0_6, color='black')
axs_Ar_pressures[1,1].plot(wavel_nm, I0_4, color='black')
axs_Ar_pressures[2,1].plot(wavel_nm, I0_2, color='black')

# Neon PressureScan
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Neon_1.1Win_PressureScan\\pressure_scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
I3_6=columns[1]
I3_4=columns[2]
I3_2=columns[3]
I3_0=columns[4]
I2_8=columns[5]
I2_6=columns[6]
I2_4=columns[7]
I2_2=columns[8]
I2_0=columns[9]
I1_8=columns[10]
I1_6=columns[11]
I1_4=columns[12]
I1_2=columns[13]
I1_0=columns[14]

axs_Ne_pressures[0,0].plot(wavel_nm, I3_6, color='black')
axs_Ne_pressures[1,0].plot(wavel_nm, I3_4, color='black')
axs_Ne_pressures[2,0].plot(wavel_nm, I3_2, color='black')
axs_Ne_pressures[3,0].plot(wavel_nm, I3_0, color='black')
axs_Ne_pressures[4,0].plot(wavel_nm, I2_8, color='black')
axs_Ne_pressures[5,0].plot(wavel_nm, I2_6, color='black')
axs_Ne_pressures[6,0].plot(wavel_nm, I2_4, color='black')
axs_Ne_pressures[0,1].plot(wavel_nm, I2_2, color='black')
axs_Ne_pressures[1,1].plot(wavel_nm, I2_0, color='black')
axs_Ne_pressures[2,1].plot(wavel_nm, I1_8, color='black')
axs_Ne_pressures[3,1].plot(wavel_nm, I1_6, color='black')
axs_Ne_pressures[4,1].plot(wavel_nm, I1_4, color='black')
axs_Ne_pressures[5,1].plot(wavel_nm, I1_2, color='black')
axs_Ne_pressures[6,1].plot(wavel_nm, I1_0, color='black', label='Experiment')

# Neon GDD Scan
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Neon_3bar_1.1W_GDDScan\\GDDScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
I1=columns[1]
I2=columns[2]
I3=columns[3]
I4=columns[4]
I5=columns[5]
I6=columns[6]
I7=columns[7]
I8=columns[8]
I9=columns[9]
I10=columns[10]
I11=columns[11]
I12=columns[12]
I13=columns[13]
I14=columns[14]
I15=columns[15]

# Plot experimental data
axs_Ne_GDDs[0,0].plot(wavel_nm, I1, color='black')
axs_Ne_GDDs[0,1].plot(wavel_nm, I2, color='black')
axs_Ne_GDDs[0,2].plot(wavel_nm, I3, color='black')
axs_Ne_GDDs[0,3].plot(wavel_nm, I4, color='black')
axs_Ne_GDDs[0,4].plot(wavel_nm, I5, color='black')
axs_Ne_GDDs[1,0].plot(wavel_nm, I6, color='black')
axs_Ne_GDDs[1,1].plot(wavel_nm, I7, color='black')
axs_Ne_GDDs[1,2].plot(wavel_nm, I8, color='black')
axs_Ne_GDDs[1,3].plot(wavel_nm, I9, color='black')
axs_Ne_GDDs[1,4].plot(wavel_nm, I10, color='black')
axs_Ne_GDDs[2,0].plot(wavel_nm, I11, color='black')
axs_Ne_GDDs[2,1].plot(wavel_nm, I12, color='black')
axs_Ne_GDDs[2,2].plot(wavel_nm, I13, color='black')
axs_Ne_GDDs[2,3].plot(wavel_nm, I14, color='black')
axs_Ne_GDDs[2,4].plot(wavel_nm, I15, color='black', label='Experiment')

# Neon GDD Fine Scan
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Neon_3bar_1.1W_GDDScan\\GDDScan_fine.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
I6_0=columns[1]
I6_4=columns[2]
I6_8=columns[3]
I7_2=columns[4]
I7_6=columns[5]
I8_0=columns[6]
I8_4=columns[7]
I8_8=columns[8]
I9_2=columns[9]
I9_6=columns[10]
I10_0=columns[11]
I10_4=columns[12]
I10_8=columns[13]
I11_2=columns[14]
I11_6=columns[15]
I12_0=columns[16]

# Plot experimental data
axs_Ne_GDDs_fine[0,0].plot(wavel_nm, I6_0, color='black')
axs_Ne_GDDs_fine[0,1].plot(wavel_nm, I6_4, color='black')
axs_Ne_GDDs_fine[0,2].plot(wavel_nm, I6_8, color='black')
axs_Ne_GDDs_fine[0,3].plot(wavel_nm, I7_2, color='black')
axs_Ne_GDDs_fine[1,0].plot(wavel_nm, I7_6, color='black')
axs_Ne_GDDs_fine[1,1].plot(wavel_nm, I8_0, color='black')
axs_Ne_GDDs_fine[1,2].plot(wavel_nm, I8_4, color='black')
axs_Ne_GDDs_fine[1,3].plot(wavel_nm, I8_8, color='black')
axs_Ne_GDDs_fine[2,0].plot(wavel_nm, I9_2, color='black')
axs_Ne_GDDs_fine[2,1].plot(wavel_nm, I9_6, color='black')
axs_Ne_GDDs_fine[2,2].plot(wavel_nm, I10_0, color='black')
axs_Ne_GDDs_fine[2,3].plot(wavel_nm, I10_4, color='black')
axs_Ne_GDDs_fine[3,0].plot(wavel_nm, I10_8, color='black')
axs_Ne_GDDs_fine[3,1].plot(wavel_nm, I11_2, color='black')
axs_Ne_GDDs_fine[3,2].plot(wavel_nm, I11_6, color='black')
axs_Ne_GDDs_fine[3,3].plot(wavel_nm, I12_0, color='black', label='Experiment')

#####################################################################################################################
# Format plots
fig_Ar_pressures.delaxes(axs_Ar_pressures[3,1])

axs_Ne_GDDs[0,0].set_title('0.05 mm')
axs_Ne_GDDs[0,1].set_title('0.10 mm')
axs_Ne_GDDs[0,2].set_title('0.15 mm')
axs_Ne_GDDs[0,3].set_title('0.20 mm')
axs_Ne_GDDs[0,4].set_title('0.25 mm')
axs_Ne_GDDs[1,0].set_title('0.30 mm')
axs_Ne_GDDs[1,1].set_title('0.35 mm')
axs_Ne_GDDs[1,2].set_title('0.40 mm')
axs_Ne_GDDs[1,3].set_title('0.45 mm')
axs_Ne_GDDs[1,4].set_title('0.50 mm')
axs_Ne_GDDs[2,0].set_title('0.55 mm')
axs_Ne_GDDs[2,1].set_title('0.60 mm')
axs_Ne_GDDs[2,2].set_title('0.65 mm')
axs_Ne_GDDs[2,3].set_title('0.70 mm')
axs_Ne_GDDs[2,4].set_title('0.75 mm')

axs_Ne_GDDs_fine[0,0].set_title('0.30 mm')
axs_Ne_GDDs_fine[0,1].set_title('0.32 mm')
axs_Ne_GDDs_fine[0,2].set_title('0.34 mm')
axs_Ne_GDDs_fine[0,3].set_title('0.36 mm')
axs_Ne_GDDs_fine[1,0].set_title('0.38 mm')
axs_Ne_GDDs_fine[1,1].set_title('0.40 mm')
axs_Ne_GDDs_fine[1,2].set_title('0.42 mm')
axs_Ne_GDDs_fine[1,3].set_title('0.44 mm')
axs_Ne_GDDs_fine[2,0].set_title('0.46 mm')
axs_Ne_GDDs_fine[2,1].set_title('0.48 mm')
axs_Ne_GDDs_fine[2,2].set_title('0.50 mm')
axs_Ne_GDDs_fine[2,3].set_title('0.52 mm')
axs_Ne_GDDs_fine[3,0].set_title('0.54 mm')
axs_Ne_GDDs_fine[3,1].set_title('0.56 mm')
axs_Ne_GDDs_fine[3,2].set_title('0.58 mm')
axs_Ne_GDDs_fine[3,3].set_title('0.60 mm')

axs_Ar_powers[4,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
axs_Ne_powers[4,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
axs_Ar_pressures[3,0].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
axs_Ne_pressures[6,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)

ax2_Ar_powers00 = axs_Ar_powers[0,0].twinx()
ax2_Ar_powers00.legend(title='1.2W', loc='upper right', title_fontsize=16)
ax2_Ar_powers00.get_yaxis().set_visible(False)
ax2_Ar_powers01 = axs_Ar_powers[1,0].twinx()
ax2_Ar_powers01.legend(title='1.1W', loc='upper right', title_fontsize=16)
ax2_Ar_powers01.get_yaxis().set_visible(False)
ax2_Ar_powers10 = axs_Ar_powers[2,0].twinx()
ax2_Ar_powers10.legend(title='1.0W', loc='upper right', title_fontsize=16)
ax2_Ar_powers10.get_yaxis().set_visible(False)
ax2_Ar_powers11 = axs_Ar_powers[3,0].twinx()
ax2_Ar_powers11.legend(title='0.9W', loc='upper right', title_fontsize=16)
ax2_Ar_powers11.get_yaxis().set_visible(False)
ax2_Ar_powers20 = axs_Ar_powers[4,0].twinx()
ax2_Ar_powers20.legend(title='0.8W', loc='upper right', title_fontsize=16)
ax2_Ar_powers20.get_yaxis().set_visible(False)
ax2_Ar_powers21 = axs_Ar_powers[0,1].twinx()
ax2_Ar_powers21.legend(title='0.7W', loc='upper right', title_fontsize=16)
ax2_Ar_powers21.get_yaxis().set_visible(False)
ax2_Ar_powers30 = axs_Ar_powers[1,1].twinx()
ax2_Ar_powers30.legend(title='0.6W', loc='upper right', title_fontsize=16)
ax2_Ar_powers30.get_yaxis().set_visible(False)
ax2_Ar_powers31 = axs_Ar_powers[2,1].twinx()
ax2_Ar_powers31.legend(title='0.5W', loc='upper right', title_fontsize=16)
ax2_Ar_powers31.get_yaxis().set_visible(False)
ax2_Ar_powers40 = axs_Ar_powers[3,1].twinx()
ax2_Ar_powers40.legend(title='0.4W', loc='upper right', title_fontsize=16)
ax2_Ar_powers40.get_yaxis().set_visible(False)
ax2_Ar_powers41 = axs_Ar_powers[4,1].twinx()
ax2_Ar_powers41.legend(title='0.3W', loc='upper right', title_fontsize=16)
ax2_Ar_powers41.get_yaxis().set_visible(False)

ax2_Ne_powers00 = axs_Ne_powers[0,0].twinx()
ax2_Ne_powers00.legend(title='1.2W', loc='upper right', title_fontsize=16)
ax2_Ne_powers00.get_yaxis().set_visible(False)
ax2_Ne_powers01 = axs_Ne_powers[1,0].twinx()
ax2_Ne_powers01.legend(title='1.1W', loc='upper right', title_fontsize=16)
ax2_Ne_powers01.get_yaxis().set_visible(False)
ax2_Ne_powers10 = axs_Ne_powers[2,0].twinx()
ax2_Ne_powers10.legend(title='1.0W', loc='upper right', title_fontsize=16)
ax2_Ne_powers10.get_yaxis().set_visible(False)
ax2_Ne_powers11 = axs_Ne_powers[3,0].twinx()
ax2_Ne_powers11.legend(title='0.9W', loc='upper right', title_fontsize=16)
ax2_Ne_powers11.get_yaxis().set_visible(False)
ax2_Ne_powers20 = axs_Ne_powers[4,0].twinx()
ax2_Ne_powers20.legend(title='0.8W', loc='upper right', title_fontsize=16)
ax2_Ne_powers20.get_yaxis().set_visible(False)
ax2_Ne_powers21 = axs_Ne_powers[0,1].twinx()
ax2_Ne_powers21.legend(title='0.7W', loc='upper right', title_fontsize=16)
ax2_Ne_powers21.get_yaxis().set_visible(False)
ax2_Ne_powers30 = axs_Ne_powers[1,1].twinx()
ax2_Ne_powers30.legend(title='0.6W', loc='upper right', title_fontsize=16)
ax2_Ne_powers30.get_yaxis().set_visible(False)
ax2_Ne_powers31 = axs_Ne_powers[2,1].twinx()
ax2_Ne_powers31.legend(title='0.5W', loc='upper right', title_fontsize=16)
ax2_Ne_powers31.get_yaxis().set_visible(False)
ax2_Ne_powers40 = axs_Ne_powers[3,1].twinx()
ax2_Ne_powers40.legend(title='0.4W', loc='upper right', title_fontsize=16)
ax2_Ne_powers40.get_yaxis().set_visible(False)
ax2_Ne_powers41 = axs_Ne_powers[4,1].twinx()
ax2_Ne_powers41.legend(title='0.3W', loc='upper right', title_fontsize=16)
ax2_Ne_powers41.get_yaxis().set_visible(False)

ax2_Ar_pressures00 = axs_Ar_pressures[0,0].twinx()
ax2_Ar_pressures00.legend(title='1.4bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures00.get_yaxis().set_visible(False)
ax2_Ar_pressures01 = axs_Ar_pressures[1,0].twinx()
ax2_Ar_pressures01.legend(title='1.2bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures01.get_yaxis().set_visible(False)
ax2_Ar_pressures10 = axs_Ar_pressures[2,0].twinx()
ax2_Ar_pressures10.legend(title='1.0bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures10.get_yaxis().set_visible(False)
ax2_Ar_pressures11 = axs_Ar_pressures[3,0].twinx()
ax2_Ar_pressures11.legend(title='0.8bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures11.get_yaxis().set_visible(False)
ax2_Ar_pressures20 = axs_Ar_pressures[0,1].twinx()
ax2_Ar_pressures20.legend(title='0.6bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures20.get_yaxis().set_visible(False)
ax2_Ar_pressures21 = axs_Ar_pressures[1,1].twinx()
ax2_Ar_pressures21.legend(title='0.4bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures21.get_yaxis().set_visible(False)
ax2_Ar_pressures30 = axs_Ar_pressures[2,1].twinx()
ax2_Ar_pressures30.legend(title='0.2bar', loc='upper right', title_fontsize=16)
ax2_Ar_pressures30.get_yaxis().set_visible(False)

ax2_Ne_pressures00 = axs_Ne_pressures[0,0].twinx()
ax2_Ne_pressures00.legend(title='3.6bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures00.get_yaxis().set_visible(False)
ax2_Ne_pressures01 = axs_Ne_pressures[1,0].twinx()
ax2_Ne_pressures01.legend(title='3.4bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures01.get_yaxis().set_visible(False)
ax2_Ne_pressures10 = axs_Ne_pressures[2,0].twinx()
ax2_Ne_pressures10.legend(title='3.2bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures10.get_yaxis().set_visible(False)
ax2_Ne_pressures11 = axs_Ne_pressures[3,0].twinx()
ax2_Ne_pressures11.legend(title='3.0bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures11.get_yaxis().set_visible(False)
ax2_Ne_pressures20 = axs_Ne_pressures[4,0].twinx()
ax2_Ne_pressures20.legend(title='2.8bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures20.get_yaxis().set_visible(False)
ax2_Ne_pressures21 = axs_Ne_pressures[5,0].twinx()
ax2_Ne_pressures21.legend(title='2.6bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures21.get_yaxis().set_visible(False)
ax2_Ne_pressures30 = axs_Ne_pressures[6,0].twinx()
ax2_Ne_pressures30.legend(title='2.4bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures30.get_yaxis().set_visible(False)
ax2_Ne_pressures31 = axs_Ne_pressures[0,1].twinx()
ax2_Ne_pressures31.legend(title='2.2bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures31.get_yaxis().set_visible(False)
ax2_Ne_pressures40 = axs_Ne_pressures[1,1].twinx()
ax2_Ne_pressures40.legend(title='2.0bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures40.get_yaxis().set_visible(False)
ax2_Ne_pressures41 = axs_Ne_pressures[2,1].twinx()
ax2_Ne_pressures41.legend(title='1.8bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures41.get_yaxis().set_visible(False)
ax2_Ne_pressures50 = axs_Ne_pressures[3,1].twinx()
ax2_Ne_pressures50.legend(title='1.6bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures50.get_yaxis().set_visible(False)
ax2_Ne_pressures51 = axs_Ne_pressures[4,1].twinx()
ax2_Ne_pressures51.legend(title='1.4bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures51.get_yaxis().set_visible(False)
ax2_Ne_pressures60 = axs_Ne_pressures[5,1].twinx()
ax2_Ne_pressures60.legend(title='1.2bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures60.get_yaxis().set_visible(False)
ax2_Ne_pressures61 = axs_Ne_pressures[6,1].twinx()
ax2_Ne_pressures61.legend(title='1.0bar', loc='upper right', title_fontsize=16)
ax2_Ne_pressures61.get_yaxis().set_visible(False)

plt.show()