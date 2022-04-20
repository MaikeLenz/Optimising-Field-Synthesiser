import matplotlib.pyplot as plt
import pandas as pd
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

#filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"

import numpy as np

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
intens1_1=np.array(columns[2])



# Plotting on same plot
fig, axs = plt.subplots(4,2)
#fig.suptitle('GDD Scan Experimental vs Simulated', size=24)
#fig.suptitle('Neon Compressor Grating Position Scan', size=24)
plt.setp(axs, xlim=(450,1050))
#plt.setp(axs[-1, :], xlabel='Wavelength, nm')
#plt.setp(axs[:, 0], ylabel='Intensity, a.u.')
fig.supxlabel('Wavelength (nm)', size=18)
fig.supylabel('Intensity (a.u.)', size=18)
plt.setp(axs[0,0].get_xticklabels(), visible=False)
plt.setp(axs[0,1].get_xticklabels(), visible=False)
plt.setp(axs[1,0].get_xticklabels(), visible=False)
plt.setp(axs[1,1].get_xticklabels(), visible=False)
plt.setp(axs[2,0].get_xticklabels(), visible=False)
plt.setp(axs[2,1].get_xticklabels(), visible=False)

axs[0,0].set_yticks([])
axs[0,1].set_yticks([])
axs[1,0].set_yticks([])
axs[1,1].set_yticks([])
axs[2,0].set_yticks([])
axs[2,1].set_yticks([])
axs[3,0].set_yticks([])
axs[3,1].set_yticks([])
# Plot simulated data
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1870_TOD-0.04_pos-0.4.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10)
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1640_TOD-0.04_pos-0.35.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10)
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1410_TOD-0.03_pos-0.3.csv")
axs[0,2].plot(df.iloc[:,0], df.iloc[:,1]/10)
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1170_TOD-0.03_pos-0.25.csv")
axs[0,3].plot(df.iloc[:,0], df.iloc[:,1]/10)
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD937_TOD-0.02_pos-0.2.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m', label='Luna')
#axs[0,0].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD703_TOD-0.02_pos-0.15.csv")
axs[1,0].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[1,0].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD469_TOD-0.01_pos-0.1.csv")
axs[2,0].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[2,0].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD234_TOD-0.01_pos-0.05.csv")
axs[3,0].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[3,0].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\GDD0_TOD0.0_pos0.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[0,1].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-234_TOD0.01_pos0.05.csv")
axs[1,1].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[1,1].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-469_TOD0.01_pos0.1.csv")
axs[2,1].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[2,1].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-703_TOD0.02_pos0.15.csv")
axs[3,1].plot(df.iloc[:,0], df.iloc[:,1]/10, '--', color='m')
#axs[3,1].fill_between(wavel_nm,max(df.iloc[:,1])*intens1_1/(10*max(intens1_1)),color="lightgray")
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-937_TOD0.02_pos0.2.csv")
axs[2,2].plot(df.iloc[:,0], df.iloc[:,1]/10)
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-1170_TOD0.03_pos0.25.csv")
axs[2,3].plot(df.iloc[:,0], df.iloc[:,1]/10)
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-1410_TOD0.03_pos0.3.csv")
axs[2,4].plot(df.iloc[:,0], df.iloc[:,1]/10, label='Luna Simulation')
"""

# Plot experimental spectra
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'HCF_scans\\Neon_3bar_1.1W_GDDScan\\GDDScan.txt', 'rt') as myfile: 
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
"""
axs[0,0].plot(wavel_nm, I1)
axs[0,1].plot(wavel_nm, I2)
axs[0,2].plot(wavel_nm, I3)
axs[0,3].plot(wavel_nm, I4)
"""
axs[0,0].plot(wavel_nm, I5, color='black', label='Experiment')
axs[1,0].plot(wavel_nm, I6, color='black')
axs[2,0].plot(wavel_nm, I7, color='black')
axs[3,0].plot(wavel_nm, I8, color='black')
axs[0,1].plot(wavel_nm, I9, color='black')
axs[1,1].plot(wavel_nm, I10, color='black')
axs[2,1].plot(wavel_nm, I11, color='black')
axs[3,1].plot(wavel_nm, I12, color='black')
"""
axs[2,2].plot(wavel_nm, I13)
axs[2,3].plot(wavel_nm, I14)
axs[2,4].plot(wavel_nm, I15, label='Experimental Data')
"""
axs[0,0].legend(loc=(0,1.05), fontsize=18)

ax2_00 = axs[0,0].twinx()
ax2_00.legend(title='-0.20mm', loc='upper right', title_fontsize=16)
ax2_00.get_yaxis().set_visible(False)
ax2_10 = axs[1,0].twinx()
ax2_10.legend(title='-0.15mm', loc='upper right', title_fontsize=16)
ax2_10.get_yaxis().set_visible(False)
ax2_20 = axs[2,0].twinx()
ax2_20.legend(title='-0.10mm', loc='upper right', title_fontsize=16)
ax2_20.get_yaxis().set_visible(False)
ax2_30 = axs[3,0].twinx()
ax2_30.legend(title='-0.05mm', loc='upper right', title_fontsize=16)
ax2_30.get_yaxis().set_visible(False)
ax2_01 = axs[0,1].twinx()
ax2_01.legend(title='0.00mm', loc='upper right', title_fontsize=16)
ax2_01.get_yaxis().set_visible(False)
ax2_11 = axs[1,1].twinx()
ax2_11.legend(title='0.05mm', loc='upper right', title_fontsize=16)
ax2_11.get_yaxis().set_visible(False)
ax2_21 = axs[2,1].twinx()
ax2_21.legend(title='0.10mm', loc='upper right', title_fontsize=16)
ax2_21.get_yaxis().set_visible(False)
ax2_31 = axs[3,1].twinx()
ax2_31.legend(title='0.15mm', loc='upper right', title_fontsize=16)
ax2_31.get_yaxis().set_visible(False)

plt.show()