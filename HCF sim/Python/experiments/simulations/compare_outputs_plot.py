import sys
import matplotlib.pyplot as plt
import pandas as pd

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
#####################################################################################################################
# Create plots
fig_Ar_powers, axs_Ar_powers = plt.subplots(3,4)
fig_Ar_powers.suptitle('Argon Power Scan', size=24)
plt.setp(axs_Ar_powers, xlim=(0,1500))
plt.setp(axs_Ar_powers[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ar_powers[:, 0], ylabel='Intensity')

fig_Ne_powers, axs_Ne_powers = plt.subplots(3,4)
fig_Ne_powers.suptitle('Neon Power Scan', size=24)
plt.setp(axs_Ne_powers, xlim=(0,1400))
plt.setp(axs_Ne_powers[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ne_powers[:, 0], ylabel='Intensity')

fig_Ar_pressures, axs_Ar_pressures = plt.subplots(2,4)
fig_Ar_pressures.suptitle('Argon Pressure Scan', size=24)
plt.setp(axs_Ar_pressures, xlim=(0,1600))
plt.setp(axs_Ar_pressures[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ar_pressures[:, 0], ylabel='Intensity')

fig_Ne_pressures, axs_Ne_pressures = plt.subplots(4,4)
fig_Ne_pressures.suptitle('Neon Pressure Scan', size=24)
plt.setp(axs_Ne_pressures, xlim=(0,1250))
plt.setp(axs_Ne_pressures[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_Ne_pressures[:, 0], ylabel='Intensity')

#####################################################################################################################
# Read simulation data
Ar_sim_powers = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
Ne_sim_powers = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
Ar_sim_pressures = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
Ne_sim_pressures = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6]

# Gaussian input simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.3")
axs_Ar_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.4")
axs_Ar_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.5")
axs_Ar_powers[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.6")
axs_Ar_powers[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.7")
axs_Ar_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.8")
axs_Ar_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.9")
axs_Ar_powers[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_1.0")
axs_Ar_powers[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_1.1")
axs_Ar_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_1.2")
axs_Ar_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.3")
axs_Ne_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.4")
axs_Ne_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.5")
axs_Ne_powers[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.6")
axs_Ne_powers[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.7")
axs_Ne_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.8")
axs_Ne_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.9")
axs_Ne_powers[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_1.0")
axs_Ne_powers[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_1.1")
axs_Ne_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_1.2")
axs_Ne_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.2")
axs_Ar_pressures[1,2].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.4")
axs_Ar_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.6")
axs_Ar_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.8")
axs_Ar_pressures[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_1.0")
axs_Ar_pressures[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_1.2")
axs_Ar_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_1.4")
axs_Ar_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.0")
axs_Ne_pressures[3,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Gaussian input')
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.2")
axs_Ne_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.4")
axs_Ne_pressures[2,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.6")
axs_Ne_pressures[2,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.8")
axs_Ne_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.0")
axs_Ne_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.2")
axs_Ne_pressures[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.4")
axs_Ne_pressures[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.6")
axs_Ne_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.8")
axs_Ne_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.0")
axs_Ne_pressures[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.2")
axs_Ne_pressures[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.4")
axs_Ne_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.6")
axs_Ne_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1])

#####################################################################################################################
# Pulse input simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.3")
axs_Ar_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Pulse input')
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.4")
axs_Ar_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.5")
axs_Ar_powers[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.6")
axs_Ar_powers[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.7")
axs_Ar_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.8")
axs_Ar_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.9")
axs_Ar_powers[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_1.0")
axs_Ar_powers[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_1.1")
axs_Ar_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_1.2")
axs_Ar_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.3")
axs_Ne_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Pulse input')
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.4")
axs_Ne_powers[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.5")
axs_Ne_powers[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.6")
axs_Ne_powers[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.7")
axs_Ne_powers[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.8")
axs_Ne_powers[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.9")
axs_Ne_powers[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_1.0")
axs_Ne_powers[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_1.1")
axs_Ne_powers[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_1.2")
axs_Ne_powers[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.2")
axs_Ar_pressures[1,2].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Pulse input')
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.4")
axs_Ar_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.6")
axs_Ar_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.8")
axs_Ar_pressures[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_1.0")
axs_Ar_pressures[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_1.2")
axs_Ar_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_1.4")
axs_Ar_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1])

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.0")
axs_Ne_pressures[3,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Pulse input')
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.2")
axs_Ne_pressures[3,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.4")
axs_Ne_pressures[2,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.6")
axs_Ne_pressures[2,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.8")
axs_Ne_pressures[2,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.0")
axs_Ne_pressures[2,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.2")
axs_Ne_pressures[1,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.4")
axs_Ne_pressures[1,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.6")
axs_Ne_pressures[1,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.8")
axs_Ne_pressures[1,0].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.0")
axs_Ne_pressures[0,3].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.2")
axs_Ne_pressures[0,2].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.4")
axs_Ne_pressures[0,1].plot(df.iloc[:,0], df.iloc[:,1])
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.6")
axs_Ne_pressures[0,0].plot(df.iloc[:,0], df.iloc[:,1])
#####################################################################################################################
# Read experimental data
Ar_PowerScan_widths = []
Ne_PowerScan_widths = []
Ar_PressureScan_widths = []
Ne_PressureScan_widths = []

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
axs_Ar_powers[0,1].plot(wavel_nm, I1_1, color='black')
axs_Ar_powers[0,2].plot(wavel_nm, I1_0, color='black')
axs_Ar_powers[0,3].plot(wavel_nm, I0_9, color='black')
axs_Ar_powers[1,0].plot(wavel_nm, I0_8, color='black')
axs_Ar_powers[1,1].plot(wavel_nm, I0_7, color='black')
axs_Ar_powers[1,2].plot(wavel_nm, I0_6, color='black')
axs_Ar_powers[1,3].plot(wavel_nm, I0_5, color='black')
axs_Ar_powers[2,0].plot(wavel_nm, I0_4, color='black')
axs_Ar_powers[2,1].plot(wavel_nm, I0_3, color='black', label='Experimental data')


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
axs_Ne_powers[0,1].plot(wavel_nm, I1_1, color='black')
axs_Ne_powers[0,2].plot(wavel_nm, I1_0, color='black')
axs_Ne_powers[0,3].plot(wavel_nm, I0_9, color='black')
axs_Ne_powers[1,0].plot(wavel_nm, I0_8, color='black')
axs_Ne_powers[1,1].plot(wavel_nm, I0_7, color='black')
axs_Ne_powers[1,2].plot(wavel_nm, I0_6, color='black')
axs_Ne_powers[1,3].plot(wavel_nm, I0_5, color='black')
axs_Ne_powers[2,0].plot(wavel_nm, I0_4, color='black')
axs_Ne_powers[2,1].plot(wavel_nm, I0_3, color='black', label='Experimental data')

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
axs_Ar_pressures[0,1].plot(wavel_nm, I1_2, color='black')
axs_Ar_pressures[0,2].plot(wavel_nm, I1_0, color='black')
axs_Ar_pressures[0,3].plot(wavel_nm, I0_8, color='black')
axs_Ar_pressures[1,0].plot(wavel_nm, I0_6, color='black')
axs_Ar_pressures[1,1].plot(wavel_nm, I0_4, color='black')
axs_Ar_pressures[1,2].plot(wavel_nm, I0_2, color='black', label='Experimental data')

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
axs_Ne_pressures[0,1].plot(wavel_nm, I3_4, color='black')
axs_Ne_pressures[0,2].plot(wavel_nm, I3_2, color='black')
axs_Ne_pressures[0,3].plot(wavel_nm, I3_0, color='black')
axs_Ne_pressures[1,0].plot(wavel_nm, I2_8, color='black')
axs_Ne_pressures[1,1].plot(wavel_nm, I2_6, color='black')
axs_Ne_pressures[1,2].plot(wavel_nm, I2_4, color='black')
axs_Ne_pressures[1,3].plot(wavel_nm, I2_2, color='black')
axs_Ne_pressures[2,0].plot(wavel_nm, I2_0, color='black')
axs_Ne_pressures[2,1].plot(wavel_nm, I1_8, color='black')
axs_Ne_pressures[2,2].plot(wavel_nm, I1_6, color='black')
axs_Ne_pressures[2,3].plot(wavel_nm, I1_4, color='black')
axs_Ne_pressures[3,0].plot(wavel_nm, I1_2, color='black')
axs_Ne_pressures[3,1].plot(wavel_nm, I1_0, color='black', label='Experimental data')
#####################################################################################################################
# Format plots
fig_Ar_powers.delaxes(axs_Ar_powers[2,2])
fig_Ar_powers.delaxes(axs_Ar_powers[2,3])
fig_Ne_powers.delaxes(axs_Ne_powers[2,2])
fig_Ne_powers.delaxes(axs_Ne_powers[2,3])
fig_Ar_pressures.delaxes(axs_Ar_pressures[1,3])
fig_Ne_pressures.delaxes(axs_Ne_pressures[3,2])
fig_Ne_pressures.delaxes(axs_Ne_pressures[3,3])

axs_Ar_powers[2,1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
axs_Ne_powers[2,1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
axs_Ar_pressures[1,2].legend(loc='center left', bbox_to_anchor=(1, 0.5))
axs_Ne_pressures[3,1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()