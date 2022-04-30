import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['axes.labelsize'] = 20


#filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
#####################################################################################################################

lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=np.array(columns[0])
intens1_2=np.array(columns[1])
intens1_1=np.array(columns[2])
intens1_0=np.array(columns[3])
intens0_9=np.array(columns[4])
intens0_8=np.array(columns[5])
intens0_7=np.array(columns[6])
intens0_6=np.array(columns[7])
intens0_5=np.array(columns[8])
intens0_4=np.array(columns[9])
intens0_3=np.array(columns[10])






# Create plots
fig_Ar_powers, axs_Ar_powers = plt.subplots(5,2)

#fig_Ar_powers.suptitle('Argon Power Scan', size=24)
plt.setp(axs_Ar_powers, xlim=(310,1250))
#plt.setp(axs_Ar_powers, ylim=(0,3.8e3))
#plt.setp(axs_Ar_powers[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ar_powers[:, 0], ylabel='Intensity (a.u.)')
#fig_Ar_powers.supxlabel('Wavelength (nm)', size=18)
#fig_Ar_powers.supylabel('Intensity (a.u.)', size=18)

axs_Ar_powers[4,0].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ar_powers[4,1].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ar_powers[2,0].set_ylabel('Normalised Intensity', size=20)
axs_Ar_powers[2,1].set_ylabel('Normalised Intensity', size=20)


plt.setp(axs_Ar_powers[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[2,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[2,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[3,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_powers[3,1].get_xticklabels(), visible=False)

axs_Ar_powers[0,0].set_yticks([0.5,1])
axs_Ar_powers[0,1].set_yticks([0.5,1])
axs_Ar_powers[1,0].set_yticks([0.5,1])
axs_Ar_powers[1,1].set_yticks([0.5,1])
axs_Ar_powers[2,0].set_yticks([0.5,1])
axs_Ar_powers[2,1].set_yticks([0.5,1])
axs_Ar_powers[3,0].set_yticks([0.5,1])
axs_Ar_powers[3,1].set_yticks([0.5,1])
axs_Ar_powers[4,0].set_yticks([0,0.5,1])
axs_Ar_powers[4,1].set_yticks([0,0.5,1])

fig_Ne_powers, axs_Ne_powers = plt.subplots(5,2)
#fig_Ne_powers.suptitle('Neon Power Scan', size=24)
plt.setp(axs_Ne_powers, xlim=(350,1200))
#plt.setp(axs_Ne_powers, ylim=(0,6.8e3))
#plt.setp(axs_Ne_powers[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ne_powers[:, 0], ylabel='Intensity (a.u.)')
#fig_Ne_powers.supxlabel('Wavelength (nm)', size=18)
#fig_Ne_powers.supylabel('Intensity (a.u.)', size=18)

axs_Ne_powers[4,0].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ne_powers[4,1].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ne_powers[2,0].set_ylabel('Normalised Intensity', size=20)
axs_Ne_powers[2,1].set_ylabel('Normalised Intensity', size=20)


plt.setp(axs_Ne_powers[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[2,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[2,1].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[3,0].get_xticklabels(), visible=False)
plt.setp(axs_Ne_powers[3,1].get_xticklabels(), visible=False)

axs_Ne_powers[0,0].set_yticks([0.5,1])
axs_Ne_powers[0,1].set_yticks([0.5,1])
axs_Ne_powers[1,0].set_yticks([0.5,1])
axs_Ne_powers[1,1].set_yticks([0.5,1])
axs_Ne_powers[2,0].set_yticks([0.5,1])
axs_Ne_powers[2,1].set_yticks([0.5,1])
axs_Ne_powers[3,0].set_yticks([0.5,1])
axs_Ne_powers[3,1].set_yticks([0.5,1])
axs_Ne_powers[4,0].set_yticks([0,0.5,1])
axs_Ne_powers[4,1].set_yticks([0,0.5,1])


fig_Ar_pressures, axs_Ar_pressures = plt.subplots(4,2)
#fig_Ar_pressures.suptitle('Argon Pressure Scan', size=24)
plt.setp(axs_Ar_pressures, xlim=(310,1420))
#plt.setp(axs_Ar_pressures, ylim=(0,9.7e3))
#plt.setp(axs_Ar_pressures[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ar_pressures[:, 0], ylabel='Intensity (a.u.)')
#fig_Ar_pressures.supxlabel('Wavelength (nm)', size=18)
#fig_Ar_pressures.supylabel('Intensity (a.u.)', size=18)

axs_Ar_pressures[3,0].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ar_pressures[2,1].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ar_pressures[1,0].set_ylabel('Normalised Intensity', size=20)
axs_Ar_pressures[1,1].set_ylabel('Normalised Intensity', size=20)


plt.setp(axs_Ar_pressures[0,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[0,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[1,0].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[1,1].get_xticklabels(), visible=False)
plt.setp(axs_Ar_pressures[2,0].get_xticklabels(), visible=False)

axs_Ar_pressures[0,0].set_yticks([0.5,1])
axs_Ar_pressures[0,1].set_yticks([0.5,1])
axs_Ar_pressures[1,0].set_yticks([0.5,1])
axs_Ar_pressures[1,1].set_yticks([0.5,1])
axs_Ar_pressures[2,0].set_yticks([0.5,1])
axs_Ar_pressures[2,1].set_yticks([0,0.5,1])
axs_Ar_pressures[3,0].set_yticks([0,0.5,1])


fig_Ne_pressures, axs_Ne_pressures = plt.subplots(7,2)
#fig_Ne_pressures.suptitle('Neon Pressure Scan', size=24)
plt.setp(axs_Ne_pressures, xlim=(350,1050))
#plt.setp(axs_Ne_pressures, ylim=(0,1.15e4))
#plt.setp(axs_Ne_pressures[-1, :], xlabel='Wavelength (nm)')
#plt.setp(axs_Ne_pressures[:, 0], ylabel='Intensity (a.u.)')
#fig_Ne_pressures.supxlabel('Wavelength (nm)', size=18)
#fig_Ne_pressures.supylabel('Intensity (a.u.)', size=18)

axs_Ne_pressures[6,0].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ne_pressures[6,1].set_xlabel("Wavelength (nm)",fontsize=20)
axs_Ne_pressures[3,0].set_ylabel('Normalised Intensity', size=20)
axs_Ne_pressures[3,1].set_ylabel('Normalised Intensity', size=20)


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

axs_Ne_pressures[0,0].set_yticks([0.5,1])
axs_Ne_pressures[0,1].set_yticks([0.5,1])
axs_Ne_pressures[1,0].set_yticks([0.5,1])
axs_Ne_pressures[1,1].set_yticks([0.5,1])
axs_Ne_pressures[2,0].set_yticks([0.5,1])
axs_Ne_pressures[2,1].set_yticks([0.5,1])
axs_Ne_pressures[3,0].set_yticks([0.5,1])
axs_Ne_pressures[3,1].set_yticks([0.5,1])
axs_Ne_pressures[4,0].set_yticks([0.5,1])
axs_Ne_pressures[4,1].set_yticks([0.5,1])
axs_Ne_pressures[5,0].set_yticks([0.5,1])
axs_Ne_pressures[5,1].set_yticks([0.5,1])
axs_Ne_pressures[6,0].set_yticks([0,0.5,1])
axs_Ne_pressures[6,1].set_yticks([0,0.5,1])


fig_Ne_GDDs, axs_Ne_GDDs = plt.subplots(3,5)
#fig_Ne_GDDs.suptitle('Neon GDD Scan', size=24)
#plt.setp(axs_Ne_GDDs, xlim=(0,1250))
plt.setp(axs_Ne_GDDs[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ne_GDDs[:, 0], ylabel='Intensity, a.u.')

fig_Ne_GDDs_fine, axs_Ne_GDDs_fine = plt.subplots(4,4)
#fig_Ne_GDDs_fine.suptitle('Neon GDD Scan', size=24)
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

#####################################################################################################################
# Pulse input simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.3")
amp1=max(df.iloc[:,1])
axs_Ar_powers[4,1].plot(df.iloc[:,0], df.iloc[:,1]/amp1, '--', color='m')
axs_Ar_powers[4,1].fill_between(wavel_nm,intens0_3/max(intens0_3),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.4")
amp2=max(df.iloc[:,1])
axs_Ar_powers[3,1].plot(df.iloc[:,0], df.iloc[:,1]/amp2, '--', color='m')
axs_Ar_powers[3,1].fill_between(wavel_nm,intens0_4/max(intens0_4),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.5")
amp3=max(df.iloc[:,1])
axs_Ar_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1]/amp3, '--', color='m')
axs_Ar_powers[2,1].fill_between(wavel_nm,intens0_5/max(intens0_5),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.6")
amp4=max(df.iloc[:,1])
axs_Ar_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1]/amp4, '--', color='m')
axs_Ar_powers[1,1].fill_between(wavel_nm,intens0_6/max(intens0_6),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.7")
amp5=max(df.iloc[:,1])
axs_Ar_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1]/amp5, '--', color='m')
axs_Ar_powers[0,1].fill_between(wavel_nm,intens0_7/max(intens0_7),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.8")
amp6=max(df.iloc[:,1])
axs_Ar_powers[4,0].plot(df.iloc[:,0], df.iloc[:,1]/amp6, '--', color='m')
axs_Ar_powers[4,0].fill_between(wavel_nm,intens0_8/max(intens0_8),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.9")
amp7=max(df.iloc[:,1])
axs_Ar_powers[3,0].plot(df.iloc[:,0], df.iloc[:,1]/amp7, '--', color='m')
axs_Ar_powers[3,0].fill_between(wavel_nm,intens0_9/max(intens0_9),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.0")
amp8=max(df.iloc[:,1])
axs_Ar_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1]/amp8, '--', color='m')
axs_Ar_powers[2,0].fill_between(wavel_nm,intens1_0/max(intens1_0),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.1")
amp9=max(df.iloc[:,1])
axs_Ar_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1]/amp9, '--', color='m')
axs_Ar_powers[1,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.2")
amp10=max(df.iloc[:,1])
axs_Ar_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1]/amp10, '--', color='m', label='Luna')
axs_Ar_powers[0,0].fill_between(wavel_nm,intens1_2/max(intens1_2),color="lightgray")


# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.3")
ampNeP1=max(df.iloc[:,1])
axs_Ne_powers[4,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP1, '--', color='m')
axs_Ne_powers[4,1].fill_between(wavel_nm,intens0_3/max(intens0_3),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.4")
ampNeP2=max(df.iloc[:,1])
axs_Ne_powers[3,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP2, '--', color='m')
axs_Ne_powers[3,1].fill_between(wavel_nm,intens0_4/max(intens0_4),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.5")
ampNeP3=max(df.iloc[:,1])
axs_Ne_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP3, '--', color='m')
axs_Ne_powers[2,1].fill_between(wavel_nm,intens0_5/max(intens0_5),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.6")
ampNeP4=max(df.iloc[:,1])
axs_Ne_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP4, '--', color='m')
axs_Ne_powers[1,1].fill_between(wavel_nm,intens0_6/max(intens0_6),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.7")
ampNeP5=max(df.iloc[:,1])
axs_Ne_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP5, '--', color='m')
axs_Ne_powers[0,1].fill_between(wavel_nm,intens0_7/max(intens0_7),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.8")
ampNeP6=max(df.iloc[:,1])
axs_Ne_powers[4,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP6, '--', color='m')
axs_Ne_powers[4,0].fill_between(wavel_nm,intens0_8/max(intens0_8),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.9")
ampNeP7=max(df.iloc[:,1])
axs_Ne_powers[3,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP7, '--', color='m')
axs_Ne_powers[3,0].fill_between(wavel_nm,intens0_9/max(intens0_9),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.0")
ampNeP8=max(df.iloc[:,1])
axs_Ne_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP8, '--', color='m')
axs_Ne_powers[2,0].fill_between(wavel_nm,intens1_0/max(intens1_0),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.1")
ampNeP9=max(df.iloc[:,1])
axs_Ne_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP9, '--', color='m')
axs_Ne_powers[1,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.2")
ampNeP10=max(df.iloc[:,1])
axs_Ne_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNeP10, '--', color='m', label='Luna')
axs_Ne_powers[0,0].fill_between(wavel_nm,intens1_2/max(intens1_2),color="lightgray")

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.2")
ampP1=max(df.iloc[:,1])
axs_Ar_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1]/ampP1, '--', color='m')
axs_Ar_pressures[2,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.4")
ampP2=max(df.iloc[:,1])
axs_Ar_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1]/ampP2, '--', color='m')
axs_Ar_pressures[1,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.6")
ampP3=max(df.iloc[:,1])
axs_Ar_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1]/ampP3, '--', color='m')
axs_Ar_pressures[0,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.8")
ampP4=max(df.iloc[:,1])
axs_Ar_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1]/ampP4, '--', color='m')
axs_Ar_pressures[3,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.0")
ampP5=max(df.iloc[:,1])
axs_Ar_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1]/ampP5, '--', color='m')
axs_Ar_pressures[2,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.2")
ampP6=max(df.iloc[:,1])
axs_Ar_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1]/ampP6, '--', color='m')
axs_Ar_pressures[1,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.4")
ampP7=max(df.iloc[:,1])
axs_Ar_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1]/ampP7, '--', color='m', label='Luna')
axs_Ar_pressures[0,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.0")
ampNePr1=max(df.iloc[:,1])
axs_Ne_pressures[6,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr1, '--', color='m')
axs_Ne_pressures[6,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.2")
ampNePr2=max(df.iloc[:,1])
axs_Ne_pressures[5,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr2, '--', color='m')
axs_Ne_pressures[5,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.4")
ampNePr3=max(df.iloc[:,1])
axs_Ne_pressures[4,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr3, '--', color='m')
axs_Ne_pressures[4,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.6")
ampNePr4=max(df.iloc[:,1])
axs_Ne_pressures[3,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr4, '--', color='m')
axs_Ne_pressures[3,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.8")
ampNePr5=max(df.iloc[:,1])
axs_Ne_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr5, '--', color='m')
axs_Ne_pressures[2,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.0")
ampNePr6=max(df.iloc[:,1])
axs_Ne_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr6, '--', color='m')
axs_Ne_pressures[1,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.2")
ampNePr7=max(df.iloc[:,1])
axs_Ne_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr7, '--', color='m')
axs_Ne_pressures[0,1].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.4")
ampNePr8=max(df.iloc[:,1])
axs_Ne_pressures[6,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr8, '--', color='m')
axs_Ne_pressures[6,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.6")
ampNePr9=max(df.iloc[:,1])
axs_Ne_pressures[5,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr9, '--', color='m')
axs_Ne_pressures[5,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.8")
ampNePr10=max(df.iloc[:,1])
axs_Ne_pressures[4,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr10, '--', color='m')
axs_Ne_pressures[4,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.0")
ampNePr11=max(df.iloc[:,1])
axs_Ne_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr11, '--', color='m')
axs_Ne_pressures[3,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.2")
ampNePr12=max(df.iloc[:,1])
axs_Ne_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr12, '--', color='m')
axs_Ne_pressures[2,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.4")
ampNePr13=max(df.iloc[:,1])
axs_Ne_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr13, '--', color='m')
axs_Ne_pressures[1,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.6")
ampNePr14=max(df.iloc[:,1])
axs_Ne_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1]/ampNePr14, '--', color='m', label='Luna')
axs_Ne_pressures[0,0].fill_between(wavel_nm,intens1_1/max(intens1_1),color="lightgray")
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

wavel_nm=np.array(columns[0])
I1_29=np.array(columns[1])
I1_2=np.array(columns[2])
I1_1=np.array(columns[3])
I1_0=np.array(columns[4])
I0_9=np.array(columns[5])
I0_8=np.array(columns[6])
I0_7=np.array(columns[7])
I0_6=np.array(columns[8])
I0_5=np.array(columns[9])
I0_4=np.array(columns[10])
I0_3=np.array(columns[11])

# Plot experimental data
"""
axs_Ar_powers[0,0].plot(wavel_nm, amp10*I1_2/max(I1_2), color='black', label="Experiment")
axs_Ar_powers[1,0].plot(wavel_nm, amp9*I1_1/max(I1_1), color='black')
axs_Ar_powers[2,0].plot(wavel_nm, amp8*I1_0/max(I1_0), color='black')
axs_Ar_powers[3,0].plot(wavel_nm, amp7*I0_9/max(I0_9), color='black')
axs_Ar_powers[4,0].plot(wavel_nm, amp6*I0_8/max(I0_8), color='black')
axs_Ar_powers[0,1].plot(wavel_nm, amp5*I0_7/max(I0_7), color='black')
axs_Ar_powers[1,1].plot(wavel_nm, amp4*I0_6/max(I0_6), color='black')
axs_Ar_powers[2,1].plot(wavel_nm, amp3*I0_5/max(I0_5), color='black')
axs_Ar_powers[3,1].plot(wavel_nm, amp2*I0_4/max(I0_4), color='black')
axs_Ar_powers[4,1].plot(wavel_nm, amp1*I0_3/max(I0_3), color='black')
"""
axs_Ar_powers[0,0].plot(wavel_nm, I1_2/amp10, color='black', label="Experiment")
axs_Ar_powers[1,0].plot(wavel_nm, I1_1/amp9, color='black')
axs_Ar_powers[2,0].plot(wavel_nm, I1_0/amp8, color='black')
axs_Ar_powers[3,0].plot(wavel_nm, I0_9/amp7, color='black')
axs_Ar_powers[4,0].plot(wavel_nm, I0_8/amp6, color='black')
axs_Ar_powers[0,1].plot(wavel_nm, I0_7/amp5, color='black')
axs_Ar_powers[1,1].plot(wavel_nm, I0_6/amp4, color='black')
axs_Ar_powers[2,1].plot(wavel_nm, I0_5/amp3, color='black')
axs_Ar_powers[3,1].plot(wavel_nm, I0_4/amp2, color='black')
axs_Ar_powers[4,1].plot(wavel_nm, I0_3/amp1, color='black')
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

wavel_nm=np.array(columns[0])
I1_24=np.array(columns[1])
I1_1=np.array(columns[2])
I1_0=np.array(columns[3])
I0_9=np.array(columns[4])
I0_8=np.array(columns[5])
I0_7=np.array(columns[6])
I0_6=np.array(columns[7])
I0_5=np.array(columns[8])
I0_4=np.array(columns[9])
I0_3=np.array(columns[10])
I1_2=np.array(columns[11])

axs_Ne_powers[0,0].plot(wavel_nm, I1_2/ampNeP10, color='black', label='Experiment')
axs_Ne_powers[1,0].plot(wavel_nm, I1_1/ampNeP9, color='black')
axs_Ne_powers[2,0].plot(wavel_nm, I1_0/ampNeP8, color='black')
axs_Ne_powers[3,0].plot(wavel_nm, I0_9/ampNeP7, color='black')
axs_Ne_powers[4,0].plot(wavel_nm, I0_8/ampNeP6, color='black')
axs_Ne_powers[0,1].plot(wavel_nm, I0_7/ampNeP5, color='black')
axs_Ne_powers[1,1].plot(wavel_nm, I0_6/ampNeP4, color='black')
axs_Ne_powers[2,1].plot(wavel_nm, I0_5/ampNeP3, color='black')
axs_Ne_powers[3,1].plot(wavel_nm, I0_4/ampNeP2, color='black')
axs_Ne_powers[4,1].plot(wavel_nm, I0_3/ampNeP1, color='black')

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

wavel_nm=np.array(columns[0])
I0_2=np.array(columns[1])
I0_4=np.array(columns[2])
I0_6=np.array(columns[3])
I0_8=np.array(columns[4])
I1_0=np.array(columns[5])
I1_2=np.array(columns[6])
I1_4=np.array(columns[7])

axs_Ar_pressures[0,0].plot(wavel_nm, I1_4/ampP7, color='black', label='Experiment')
axs_Ar_pressures[1,0].plot(wavel_nm, I1_2/ampP6, color='black')
axs_Ar_pressures[2,0].plot(wavel_nm, I1_0/ampP5, color='black')
axs_Ar_pressures[3,0].plot(wavel_nm, I0_8/ampP4, color='black')
axs_Ar_pressures[0,1].plot(wavel_nm, I0_6/ampP3, color='black')
axs_Ar_pressures[1,1].plot(wavel_nm, I0_4/ampP2, color='black')
axs_Ar_pressures[2,1].plot(wavel_nm, I0_2/ampP1, color='black')

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

wavel_nm=np.array(columns[0])
I3_6=np.array(columns[1])
I3_4=np.array(columns[2])
I3_2=np.array(columns[3])
I3_0=np.array(columns[4])
I2_8=np.array(columns[5])
I2_6=np.array(columns[6])
I2_4=np.array(columns[7])
I2_2=np.array(columns[8])
I2_0=np.array(columns[9])
I1_8=np.array(columns[10])
I1_6=np.array(columns[11])
I1_4=np.array(columns[12])
I1_2=np.array(columns[13])
I1_0=np.array(columns[14])

axs_Ne_pressures[0,0].plot(wavel_nm, I3_6/ampNePr14, color='black', label='Experiment')
axs_Ne_pressures[1,0].plot(wavel_nm, I3_4/ampNePr13, color='black')
axs_Ne_pressures[2,0].plot(wavel_nm, I3_2/ampNePr12, color='black')
axs_Ne_pressures[3,0].plot(wavel_nm, I3_0/ampNePr11, color='black')
axs_Ne_pressures[4,0].plot(wavel_nm, I2_8/ampNePr10, color='black')
axs_Ne_pressures[5,0].plot(wavel_nm, I2_6/ampNePr9, color='black')
axs_Ne_pressures[6,0].plot(wavel_nm, I2_4/ampNePr8, color='black')
axs_Ne_pressures[0,1].plot(wavel_nm, I2_2/ampNePr7, color='black')
axs_Ne_pressures[1,1].plot(wavel_nm, I2_0/ampNePr6, color='black')
axs_Ne_pressures[2,1].plot(wavel_nm, I1_8/ampNePr5, color='black')
axs_Ne_pressures[3,1].plot(wavel_nm, I1_6/ampNePr4, color='black')
axs_Ne_pressures[4,1].plot(wavel_nm, I1_4/ampNePr3, color='black')
axs_Ne_pressures[5,1].plot(wavel_nm, I1_2/ampNePr2, color='black')
axs_Ne_pressures[6,1].plot(wavel_nm, I1_0/ampNePr1, color='black')

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

wavel_nm=np.array(columns[0])
I1=np.array(columns[1])
I2=np.array(columns[2])
I3=np.array(columns[3])
I4=np.array(columns[4])
I5=np.array(columns[5])
I6=np.array(columns[6])
I7=np.array(columns[7])
I8=np.array(columns[8])
I9=np.array(columns[9])
I10=np.array(columns[10])
I11=np.array(columns[11])
I12=np.array(columns[12])
I13=np.array(columns[13])
I14=np.array(columns[14])
I15=np.array(columns[15])

# Plot experimental data
axs_Ne_GDDs[0,0].plot(wavel_nm, I1, color='black', label='Experiment')
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
axs_Ne_GDDs[2,4].plot(wavel_nm, I15, color='black')

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

wavel_nm=np.array(columns[0])
I6_0=np.array(columns[1])
I6_4=np.array(columns[2])
I6_8=np.array(columns[3])
I7_2=np.array(columns[4])
I7_6=np.array(columns[5])
I8_0=np.array(columns[6])
I8_4=np.array(columns[7])
I8_8=np.array(columns[8])
I9_2=np.array(columns[9])
I9_6=np.array(columns[10])
I10_0=np.array(columns[11])
I10_4=np.array(columns[12])
I10_8=np.array(columns[13])
I11_2=np.array(columns[14])
I11_6=np.array(columns[15])
I12_0=np.array(columns[16])

# Plot experimental data
axs_Ne_GDDs_fine[0,0].plot(wavel_nm, I6_0, color='black', label='Experiment')
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
axs_Ne_GDDs_fine[3,3].plot(wavel_nm, I12_0, color='black')

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
"""
axs_Ar_powers[4,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
axs_Ne_powers[4,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
axs_Ar_pressures[3,0].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
axs_Ne_pressures[6,1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
"""
axs_Ar_powers[0,0].legend(loc=(0,1.05), fontsize=20)
axs_Ne_powers[0,0].legend(loc=(0,1.05), fontsize=20)
axs_Ar_pressures[0,0].legend(loc=(0,1.05), fontsize=20)
axs_Ne_pressures[0,0].legend(loc=(0,1.05), fontsize=20)

ax2_Ar_powers00 = axs_Ar_powers[0,0].twinx()
ax2_Ar_powers00.legend(title='1.2W', loc='upper right', title_fontsize=20)
ax2_Ar_powers00.get_yaxis().set_visible(False)
ax2_Ar_powers01 = axs_Ar_powers[1,0].twinx()
ax2_Ar_powers01.legend(title='1.1W', loc='upper right', title_fontsize=20)
ax2_Ar_powers01.get_yaxis().set_visible(False)
ax2_Ar_powers10 = axs_Ar_powers[2,0].twinx()
ax2_Ar_powers10.legend(title='1.0W', loc='upper right', title_fontsize=20)
ax2_Ar_powers10.get_yaxis().set_visible(False)
ax2_Ar_powers11 = axs_Ar_powers[3,0].twinx()
ax2_Ar_powers11.legend(title='0.9W', loc='upper right', title_fontsize=20)
ax2_Ar_powers11.get_yaxis().set_visible(False)
ax2_Ar_powers20 = axs_Ar_powers[4,0].twinx()
ax2_Ar_powers20.legend(title='0.8W', loc='upper right', title_fontsize=20)
ax2_Ar_powers20.get_yaxis().set_visible(False)
ax2_Ar_powers21 = axs_Ar_powers[0,1].twinx()
ax2_Ar_powers21.legend(title='0.7W', loc='upper right', title_fontsize=20)
ax2_Ar_powers21.get_yaxis().set_visible(False)
ax2_Ar_powers30 = axs_Ar_powers[1,1].twinx()
ax2_Ar_powers30.legend(title='0.6W', loc='upper right', title_fontsize=20)
ax2_Ar_powers30.get_yaxis().set_visible(False)
ax2_Ar_powers31 = axs_Ar_powers[2,1].twinx()
ax2_Ar_powers31.legend(title='0.5W', loc='upper right', title_fontsize=20)
ax2_Ar_powers31.get_yaxis().set_visible(False)
ax2_Ar_powers40 = axs_Ar_powers[3,1].twinx()
ax2_Ar_powers40.legend(title='0.4W', loc='upper right', title_fontsize=20)
ax2_Ar_powers40.get_yaxis().set_visible(False)
ax2_Ar_powers41 = axs_Ar_powers[4,1].twinx()
ax2_Ar_powers41.legend(title='0.3W', loc='upper right', title_fontsize=20)
ax2_Ar_powers41.get_yaxis().set_visible(False)

ax2_Ne_powers00 = axs_Ne_powers[0,0].twinx()
ax2_Ne_powers00.legend(title='1.2W', loc='upper right', title_fontsize=20)
ax2_Ne_powers00.get_yaxis().set_visible(False)
ax2_Ne_powers01 = axs_Ne_powers[1,0].twinx()
ax2_Ne_powers01.legend(title='1.1W', loc='upper right', title_fontsize=20)
ax2_Ne_powers01.get_yaxis().set_visible(False)
ax2_Ne_powers10 = axs_Ne_powers[2,0].twinx()
ax2_Ne_powers10.legend(title='1.0W', loc='upper right', title_fontsize=20)
ax2_Ne_powers10.get_yaxis().set_visible(False)
ax2_Ne_powers11 = axs_Ne_powers[3,0].twinx()
ax2_Ne_powers11.legend(title='0.9W', loc='upper right', title_fontsize=20)
ax2_Ne_powers11.get_yaxis().set_visible(False)
ax2_Ne_powers20 = axs_Ne_powers[4,0].twinx()
ax2_Ne_powers20.legend(title='0.8W', loc='upper right', title_fontsize=20)
ax2_Ne_powers20.get_yaxis().set_visible(False)
ax2_Ne_powers21 = axs_Ne_powers[0,1].twinx()
ax2_Ne_powers21.legend(title='0.7W', loc='upper right', title_fontsize=20)
ax2_Ne_powers21.get_yaxis().set_visible(False)
ax2_Ne_powers30 = axs_Ne_powers[1,1].twinx()
ax2_Ne_powers30.legend(title='0.6W', loc='upper right', title_fontsize=20)
ax2_Ne_powers30.get_yaxis().set_visible(False)
ax2_Ne_powers31 = axs_Ne_powers[2,1].twinx()
ax2_Ne_powers31.legend(title='0.5W', loc='upper right', title_fontsize=20)
ax2_Ne_powers31.get_yaxis().set_visible(False)
ax2_Ne_powers40 = axs_Ne_powers[3,1].twinx()
ax2_Ne_powers40.legend(title='0.4W', loc='upper right', title_fontsize=20)
ax2_Ne_powers40.get_yaxis().set_visible(False)
ax2_Ne_powers41 = axs_Ne_powers[4,1].twinx()
ax2_Ne_powers41.legend(title='0.3W', loc='upper right', title_fontsize=20)
ax2_Ne_powers41.get_yaxis().set_visible(False)

ax2_Ar_pressures00 = axs_Ar_pressures[0,0].twinx()
ax2_Ar_pressures00.legend(title='1.4bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures00.get_yaxis().set_visible(False)
ax2_Ar_pressures01 = axs_Ar_pressures[1,0].twinx()
ax2_Ar_pressures01.legend(title='1.2bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures01.get_yaxis().set_visible(False)
ax2_Ar_pressures10 = axs_Ar_pressures[2,0].twinx()
ax2_Ar_pressures10.legend(title='1.0bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures10.get_yaxis().set_visible(False)
ax2_Ar_pressures11 = axs_Ar_pressures[3,0].twinx()
ax2_Ar_pressures11.legend(title='0.8bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures11.get_yaxis().set_visible(False)
ax2_Ar_pressures20 = axs_Ar_pressures[0,1].twinx()
ax2_Ar_pressures20.legend(title='0.6bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures20.get_yaxis().set_visible(False)
ax2_Ar_pressures21 = axs_Ar_pressures[1,1].twinx()
ax2_Ar_pressures21.legend(title='0.4bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures21.get_yaxis().set_visible(False)
ax2_Ar_pressures30 = axs_Ar_pressures[2,1].twinx()
ax2_Ar_pressures30.legend(title='0.2bar', loc='upper right', title_fontsize=20)
ax2_Ar_pressures30.get_yaxis().set_visible(False)

ax2_Ne_pressures00 = axs_Ne_pressures[0,0].twinx()
ax2_Ne_pressures00.legend(title='3.6bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures00.get_yaxis().set_visible(False)
ax2_Ne_pressures01 = axs_Ne_pressures[1,0].twinx()
ax2_Ne_pressures01.legend(title='3.4bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures01.get_yaxis().set_visible(False)
ax2_Ne_pressures10 = axs_Ne_pressures[2,0].twinx()
ax2_Ne_pressures10.legend(title='3.2bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures10.get_yaxis().set_visible(False)
ax2_Ne_pressures11 = axs_Ne_pressures[3,0].twinx()
ax2_Ne_pressures11.legend(title='3.0bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures11.get_yaxis().set_visible(False)
ax2_Ne_pressures20 = axs_Ne_pressures[4,0].twinx()
ax2_Ne_pressures20.legend(title='2.8bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures20.get_yaxis().set_visible(False)
ax2_Ne_pressures21 = axs_Ne_pressures[5,0].twinx()
ax2_Ne_pressures21.legend(title='2.6bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures21.get_yaxis().set_visible(False)
ax2_Ne_pressures30 = axs_Ne_pressures[6,0].twinx()
ax2_Ne_pressures30.legend(title='2.4bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures30.get_yaxis().set_visible(False)
ax2_Ne_pressures31 = axs_Ne_pressures[0,1].twinx()
ax2_Ne_pressures31.legend(title='2.2bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures31.get_yaxis().set_visible(False)
ax2_Ne_pressures40 = axs_Ne_pressures[1,1].twinx()
ax2_Ne_pressures40.legend(title='2.0bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures40.get_yaxis().set_visible(False)
ax2_Ne_pressures41 = axs_Ne_pressures[2,1].twinx()
ax2_Ne_pressures41.legend(title='1.8bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures41.get_yaxis().set_visible(False)
ax2_Ne_pressures50 = axs_Ne_pressures[3,1].twinx()
ax2_Ne_pressures50.legend(title='1.6bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures50.get_yaxis().set_visible(False)
ax2_Ne_pressures51 = axs_Ne_pressures[4,1].twinx()
ax2_Ne_pressures51.legend(title='1.4bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures51.get_yaxis().set_visible(False)
ax2_Ne_pressures60 = axs_Ne_pressures[5,1].twinx()
ax2_Ne_pressures60.legend(title='1.2bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures60.get_yaxis().set_visible(False)
ax2_Ne_pressures61 = axs_Ne_pressures[6,1].twinx()
ax2_Ne_pressures61.legend(title='1.0bar', loc='upper right', title_fontsize=20)
ax2_Ne_pressures61.get_yaxis().set_visible(False)

plt.show()