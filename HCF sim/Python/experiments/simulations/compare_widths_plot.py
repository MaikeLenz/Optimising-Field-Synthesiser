import sys
import matplotlib.pyplot as plt
import pandas as pd
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
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
I = [I1_29, I1_2, I1_1, I1_0, I0_9, I0_8, I0_7, I0_6, I0_5, I0_4, I0_3]

for i in range(len(I)):
    Ar_PowerScan_widths.append(rms_width(wavel_nm, I[i]))

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
I = [I1_24, I1_2, I1_1, I1_0, I0_9, I0_8, I0_7, I0_6, I0_5, I0_4, I0_3]

for i in range(len(I)):
    Ne_PowerScan_widths.append(rms_width(wavel_nm, I[i]))

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
I = [I1_4, I1_2, I1_0, I0_8, I0_6, I0_4, I0_2]

for i in range(len(I)):
    Ar_PressureScan_widths.append(rms_width(wavel_nm, I[i]))

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
I = [I3_6, I3_4, I3_2, I3_0, I2_8, I2_6, I2_4, I2_2, I2_0, I1_8, I1_6, I1_4, I1_2, I1_0]

for i in range(len(I)):
    Ne_PressureScan_widths.append(rms_width(wavel_nm, I[i]))

#####################################################################################################################
# Read simulation data
Ar_sim_gauss_PowerScan_widths = []
Ne_sim_gauss_PowerScan_widths = []
Ar_sim_gauss_PressureScan_widths = []
Ne_sim_gauss_PressureScan_widths = []

Ar_sim_pulse_PowerScan_widths = []
Ne_sim_pulse_PowerScan_widths = []
Ar_sim_pulse_PressureScan_widths = []
Ne_sim_pulse_PressureScan_widths = []

Ar_sim_powers = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
Ne_sim_powers = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
Ar_sim_pressures = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
Ne_sim_pressures = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6]

# Gaussian input simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.3")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.4")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.5")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.6")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.7")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.8")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_0.9")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_1.0")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_1.1")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PowerScan_1.2")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.3")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.4")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.5")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.6")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.7")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.8")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_0.9")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_1.0")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_1.1")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PowerScan_1.2")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.2")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.4")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.6")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_0.8")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_1.0")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_1.2")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ar_PressureScan_1.4")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.0")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.2")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.4")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.6")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_1.8")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.0")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.2")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.4")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.6")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_2.8")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.0")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.2")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.4")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\gaussian_input\\Ne_PressureScan_3.6")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))


# Experimental input pulse simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.3")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.4")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.5")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.6")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.7")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.8")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_0.9")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_1.0")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_1.1")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PowerScan_1.2")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.3")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.4")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.5")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.6")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.7")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.8")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_0.9")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_1.0")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_1.1")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PowerScan_1.2")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.2")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.4")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.6")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_0.8")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_1.0")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_1.2")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ar_PressureScan_1.4")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.0")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.2")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.4")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.6")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_1.8")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.0")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.2")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.4")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.6")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_2.8")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.0")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.2")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.4")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pulse_input\\Ne_PressureScan_3.6")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

#####################################################################################################################
# Plot results
fig, axs = plt.subplots(2,2)
axs[0,0].plot(Ar_powers, Ar_PowerScan_widths, color='black')
axs[0,0].set_xlabel('Power, W')
axs[0,0].set_ylabel('RMS width, nm')
axs[0,1].plot(Ar_pressures, Ar_PressureScan_widths, color='black')
axs[0,1].set_xlabel('Pressure, bar')
axs[0,1].set_ylabel('RMS width, nm')
axs[1,0].plot(Ne_powers, Ne_PowerScan_widths, color='black')
axs[1,0].set_xlabel('Power, W')
axs[1,0].set_ylabel('RMS width, nm')
axs[1,1].plot(Ne_pressures, Ne_PressureScan_widths, color='black', label='Experimental data')
axs[1,1].set_xlabel('Pressure, bar')
axs[1,1].set_ylabel('RMS width, nm')

axs[0,0].plot(Ar_sim_powers, Ar_sim_gauss_PowerScan_widths)
axs[0,1].plot(Ar_sim_pressures, Ar_sim_gauss_PressureScan_widths)
axs[1,0].plot(Ne_sim_powers, Ne_sim_gauss_PowerScan_widths)
axs[1,1].plot(Ne_sim_pressures, Ne_sim_gauss_PressureScan_widths, label='Simulation with Gaussian Input')

axs[0,0].plot(Ar_sim_powers, Ar_sim_pulse_PowerScan_widths)
axs[0,1].plot(Ar_sim_pressures, Ar_sim_pulse_PressureScan_widths)
axs[1,0].plot(Ne_sim_powers, Ne_sim_pulse_PowerScan_widths)
axs[1,1].plot(Ne_sim_pressures, Ne_sim_pulse_PressureScan_widths, label='Simulation with Pulse Input')

axs[0,0].set_title('Argon Power Scan')
axs[0,1].set_title('Argon Pressure Scan')
axs[1,0].set_title('Neon Power Scan')
axs[1,1].set_title('Neon Pressure Scan')

plt.legend()
plt.show()