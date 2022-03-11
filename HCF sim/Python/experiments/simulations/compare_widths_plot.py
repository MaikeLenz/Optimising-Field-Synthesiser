import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
from theoretical_width import *

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
#####################################################################################################################
# Read experimental data
Ar_PowerScan_widths = []
Ne_PowerScan_widths = []
Ar_PressureScan_widths = []
Ne_PressureScan_widths = []
Ne_GDDScan_widths = []
Ne_GDDScan_fine_widths = []

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

# Neon GDD Scan (both normal and fine scans combined)
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
I = [I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, I13, I14, I15]
Ne_GDDs = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75]
I2 = [I6_0, I6_4, I6_8, I7_2, I7_6, I8_0, I8_4, I8_8, I9_2, I9_6, I10_0, I10_4, I10_8, I11_2, I11_6, I12_0]
Ne_GDDs_fine = [0.30, 0.32, 0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.52, 0.54, 0.56, 0.58, 0.60]

for i in range(len(I)):
    Ne_GDDScan_widths.append(rms_width(wavel_nm, I[i]))
for i in range(len(I2)):
    Ne_GDDScan_fine_widths.append(rms_width(wavel_nm, I2[i]))



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
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.3")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.4")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.5")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.6")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.7")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.8")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_0.9")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_1.0")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_1.1")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PowerScan_1.2")
Ar_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.3")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.4")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.5")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.6")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.7")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.8")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_0.9")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_1.0")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_1.1")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PowerScan_1.2")
Ne_sim_gauss_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_0.2")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_0.4")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_0.6")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_0.8")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_1.0")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_1.2")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ar_PressureScan_1.4")
Ar_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_1.0")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_1.2")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_1.4")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_1.6")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_1.8")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_2.0")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_2.2")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_2.4")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_2.6")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_2.8")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_3.0")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_3.2")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_3.4")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\gaussian_input\\Ne_PressureScan_3.6")
Ne_sim_gauss_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))


# Experimental input pulse simulations
# Argon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.3")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.4")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.5")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.6")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.7")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.8")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_0.9")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.0")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.1")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PowerScan_1.2")
Ar_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon power scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.3")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.4")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.5")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.6")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.7")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.8")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_0.9")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.0")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.1")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PowerScan_1.2")
Ne_sim_pulse_PowerScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Argon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.2")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.4")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.6")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_0.8")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.0")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.2")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ar_PressureScan_1.4")
Ar_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

# Neon pressure scan
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.0")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.2")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.4")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.6")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_1.8")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.0")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.2")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.4")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.6")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_2.8")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.0")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.2")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.4")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))
df = pd.read_csv(filepath+"simulations\\data\\pressure_gradient\\pulse_input\\Ne_PressureScan_3.6")
Ne_sim_pulse_PressureScan_widths.append(rms_width(df.iloc[:,0], df.iloc[:,1]))

#####################################################################################################################
# Calculate theoretical widths
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length

# Read input data
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv")
powers = df.iloc[:,0]
energies = powers/1000
λ0s = df.iloc[:,1]
domegas = df.iloc[:,2]

def ang_freq_to_τ_FWHM(FWHM):
    freq_FWHM = FWHM/(2*np.pi)
    return 0.44/freq_FWHM
def ang_freq_to_wavel_width(width, wavel):
    c = 299792458 
    freq_width = width/(2*np.pi)
    return freq_width*(wavel**2)/c

# Argon power scan
Ar_power_theor_widths = []
pressure = 0.8*0.66
for i in range(len(energies)):
    ang_freq_width = theoretical_width(radius, flength, pressure, λ0s[i], ang_freq_to_τ_FWHM(domegas[i]), energies[i], 'Ar', 0.56)
    Ar_power_theor_widths.append(ang_freq_to_wavel_width(ang_freq_width, λ0s[i])*(10**9))
Ar_power_theor_widths = np.array(Ar_power_theor_widths)
# Neon power scan
Ne_power_theor_widths = []
pressure = 3*0.66
for i in range(len(energies)):
    ang_freq_width = theoretical_width(radius, flength, pressure, λ0s[i], ang_freq_to_τ_FWHM(domegas[i]), energies[i], 'Ne', 0.69)
    Ne_power_theor_widths.append(ang_freq_to_wavel_width(ang_freq_width, λ0s[i])*(10**9))
Ne_power_theor_widths = np.array(Ne_power_theor_widths)
# Argon pressure scan
Ar_pressures = [1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2]
Ar_pressure_theor_widths = []
energy = energies[1]
λ0 = λ0s[1]
domega = domegas[1]
for i in range(len(Ar_pressures)):
    ang_freq_width = theoretical_width(radius, flength, Ar_pressures[i]*0.66, λ0, ang_freq_to_τ_FWHM(domega), energy, 'Ar', 0.62)
    Ar_pressure_theor_widths.append(ang_freq_to_wavel_width(ang_freq_width, λ0)*(10**9))
Ar_pressure_theor_widths = np.array(Ar_pressure_theor_widths)
# Neon pressure scan
Ne_pressures = [3.6, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]
Ne_pressure_theor_widths = []
energy = energies[1]
λ0 = λ0s[1]
domega = domegas[1]
for i in range(len(Ne_pressures)):
    ang_freq_width = theoretical_width(radius, flength, Ne_pressures[i]*0.66, λ0, ang_freq_to_τ_FWHM(domega), energy, 'Ne', 0.71)
    Ne_pressure_theor_widths.append(ang_freq_to_wavel_width(ang_freq_width, λ0)*(10**9))
Ne_pressure_theor_widths = np.array(Ne_pressure_theor_widths)


#####################################################################################################################
#SPM errors

#Ne pressure scan
Ne_press_errs=[]
energy=energies[1]
gas = "Ne"
λ0 = λ0s[1]
dλ_rms= ang_freq_to_wavel_width(domegas[1],λ0)/(4*np.sqrt(np.log(2)))
Δradius= 0
Δflength= 0
Δn2= 0.25e-21/10000
Δenergy= 0.1*energy
Δdλ_rms= 0.01*dλ_rms
Δλ0=0.1*λ0
for i in range(len(Ne_pressures)):
    pressure=Ne_pressures[i]
    #Ne_press_errs.append(theoretical_width_exp_error(radius, flength, energy, pressure, gas, dλ_rms, λ0, Δradius, Δflength, Δn2, Δenergy, Δdλ_rms, Δλ0))
    Ne_press_errs.append(0.32*Ne_pressure_theor_widths[i])
Ne_press_errs = np.array(Ne_press_errs)

#Ne power scan
Ne_pow_errs=[]
gas = "Ne"
Δradius= 0
Δflength= 0
Δn2= 0.25e-21/10000
pressure=3*0.66
for i in range(len(energies)):
    energy=energies[i]
    λ0=λ0s[i]
    dλ_rms= ang_freq_to_wavel_width(domegas[i],λ0)/(4*np.sqrt(np.log(2)))
    Δdλ_rms= 0.01*dλ_rms
    Δλ0=0.1*λ0
    Δenergy= 0.1*energy
    #Ne_pow_errs.append(theoretical_width_exp_error(radius, flength, energy, pressure, gas, dλ_rms, λ0, Δradius, Δflength, Δn2, Δenergy, Δdλ_rms, Δλ0))
    Ne_pow_errs.append(0.32*Ne_power_theor_widths[i])

Ne_pow_errs = np.array(Ne_pow_errs)

#Ar pressure scan
Ar_press_errs=[]
energy=energies[1]
gas = "Ar"
λ0 = λ0s[1]
dλ_rms= ang_freq_to_wavel_width(domegas[1],λ0)/(4*np.sqrt(np.log(2)))
Δradius= 0
Δflength= 0
Δn2= 0.05e-19/10000
Δenergy= 0.1*energy
Δdλ_rms= 0.01*dλ_rms
Δλ0=0.1*λ0
for i in range(len(Ar_pressures)):
    pressure=Ar_pressures[i]
    #Ar_press_errs.append(theoretical_width_exp_error(radius, flength, energy, pressure, gas, dλ_rms, λ0, Δradius, Δflength, Δn2, Δenergy, Δdλ_rms, Δλ0))
    Ar_press_errs.append(0.32*Ar_pressure_theor_widths[i])

Ar_press_errs = np.array(Ar_press_errs)

#Ar power scan
Ar_pow_errs=[]
gas = "Ar"
Δradius= 0
Δflength= 0
Δn2= 0.05e-19/10000
pressure= 0.8*0.66
for i in range(len(energies)):
    energy=energies[i]
    λ0=λ0s[i]
    dλ_rms= ang_freq_to_wavel_width(domegas[i],λ0)/(4*np.sqrt(np.log(2)))
    Δdλ_rms= 0.01*dλ_rms
    Δλ0=0.1*λ0
    Δenergy= 0.1*energy
    #Ar_pow_errs.append(theoretical_width_exp_error(radius, flength, energy, pressure, gas, dλ_rms, λ0, Δradius, Δflength, Δn2, Δenergy, Δdλ_rms, Δλ0))
    Ar_pow_errs.append(0.32*Ar_power_theor_widths[i])

Ar_pow_errs = np.array(Ar_pow_errs)

#######################################################################################################################
# Plot results
fig, axs = plt.subplots(2,2)

left  = 0.1  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9     # the top of the subplots of the figure
wspace = 0.2   # the amount of width reserved for blank space between subplots
hspace = 0.3  # the amount of height reserved for white space between subplots

plt.subplots_adjust(left, bottom, right, top, wspace, hspace)

axs[0,0].plot(powers, Ar_power_theor_widths, color='red')
axs[0,0].fill_between(powers, Ar_power_theor_widths - Ar_pow_errs, Ar_power_theor_widths + Ar_pow_errs, alpha=0.2)
axs[0,1].plot(Ar_pressures, Ar_pressure_theor_widths, color='red')
axs[0,1].fill_between(Ar_pressures, Ar_pressure_theor_widths - Ar_press_errs, Ar_pressure_theor_widths + Ar_press_errs, alpha=0.2)
axs[1,0].plot(powers, Ne_power_theor_widths, color='red')
axs[1,0].fill_between(powers, Ne_power_theor_widths - Ne_pow_errs, Ne_power_theor_widths + Ne_pow_errs, alpha=0.2)
axs[1,1].plot(Ne_pressures, Ne_pressure_theor_widths, color='red', label='Theoretical')
axs[1,1].fill_between(Ne_pressures, Ne_pressure_theor_widths - Ne_press_errs, Ne_pressure_theor_widths + Ne_press_errs, alpha=0.2)

axs[0,0].plot(Ar_powers, Ar_PowerScan_widths,'+', color='black')
axs[0,0].set_xlabel('Power, W')
axs[0,0].set_ylabel('RMS width, nm')
axs[0,1].plot(Ar_pressures, Ar_PressureScan_widths,'+', color='black')
axs[0,1].set_xlabel('Pressure, bar')
axs[0,1].set_ylabel('RMS width, nm')
axs[1,0].plot(Ne_powers, Ne_PowerScan_widths,'+', color='black')
axs[1,0].set_xlabel('Power, W')
axs[1,0].set_ylabel('RMS width, nm')
axs[1,1].plot(Ne_pressures, Ne_PressureScan_widths,'+', color='black', label='Experimental data')
axs[1,1].set_xlabel('Pressure, bar')
axs[1,1].set_ylabel('RMS width, nm')

axs[0,0].plot(Ar_sim_powers, Ar_sim_gauss_PowerScan_widths,'+')
axs[0,1].plot(Ar_sim_pressures, Ar_sim_gauss_PressureScan_widths,'+')
axs[1,0].plot(Ne_sim_powers, Ne_sim_gauss_PowerScan_widths,'+')
axs[1,1].plot(Ne_sim_pressures, Ne_sim_gauss_PressureScan_widths,'+', label='Simulation with Gaussian Input')

axs[0,0].plot(Ar_sim_powers, Ar_sim_pulse_PowerScan_widths,'+')
axs[0,1].plot(Ar_sim_pressures, Ar_sim_pulse_PressureScan_widths,'+')
axs[1,0].plot(Ne_sim_powers, Ne_sim_pulse_PowerScan_widths,'+')
axs[1,1].plot(Ne_sim_pressures, Ne_sim_pulse_PressureScan_widths,'+', label='Simulation with Experimental Input')

axs[0,0].set_title('Argon Power Scan')
axs[0,1].set_title('Argon Pressure Scan')
axs[1,0].set_title('Neon Power Scan')
axs[1,1].set_title('Neon Pressure Scan')

plt.legend()

plt.figure()
plt.plot(Ne_GDDs, Ne_GDDScan_widths, '+', color='tab:blue', label='Rough scan')
plt.plot(Ne_GDDs_fine, Ne_GDDScan_fine_widths, '+', color='tab:red', label='Fine Scan')
plt.title('Neon GDD Scan Widths')
plt.xlabel('Compressor grating displacement, mm')
plt.ylabel('RMS width, nm')
plt.legend()

plt.show()