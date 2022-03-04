import matplotlib.pyplot as plt
import pandas as pd

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"

# Plotting on same plot
fig, axs = plt.subplots(3,5)
fig.suptitle('GDD Scan Experimental vs Simulated', size=24)
plt.setp(axs, xlim=(450,1000))
plt.setp(axs[-1, :], xlabel='Wavelength, nm')
plt.setp(axs[:, 0], ylabel='Intensity')

# Plot simulated data
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD1870_TOD-0.04_pos-0.4.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD1640_TOD-0.04_pos-0.35.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD1410_TOD-0.03_pos-0.3.csv")
axs[0,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD1170_TOD-0.03_pos-0.25.csv")
axs[0,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD937_TOD-0.02_pos-0.2.csv")
axs[0,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD703_TOD-0.02_pos-0.15.csv")
axs[1,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD469_TOD-0.01_pos-0.1.csv")
axs[1,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD234_TOD-0.01_pos-0.05.csv")
axs[1,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\GDD0_TOD0.0_pos0.csv")
axs[1,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-234_TOD0.01_pos0.05.csv")
axs[1,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-469_TOD0.01_pos0.1.csv")
axs[2,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-703_TOD0.02_pos0.15.csv")
axs[2,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-937_TOD0.02_pos0.2.csv")
axs[2,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-1170_TOD0.03_pos0.25.csv")
axs[2,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-1410_TOD0.03_pos0.3.csv")
axs[2,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange', label='Simulated')
"""
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD1870_TOD-0.04_pos-0.4.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD1640_TOD-0.04_pos-0.35.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD1410_TOD-0.03_pos-0.3.csv")
axs[0,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD1170_TOD-0.03_pos-0.25.csv")
axs[0,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD937_TOD-0.02_pos-0.2.csv")
axs[0,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD703_TOD-0.02_pos-0.15.csv")
axs[1,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD469_TOD-0.01_pos-0.1.csv")
axs[1,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD234_TOD-0.01_pos-0.05.csv")
axs[1,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\GDD0_TOD0.0_pos0.csv")
axs[1,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD-234_TOD0.01_pos0.05.csv")
axs[1,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD-469_TOD0.01_pos0.1.csv")
axs[2,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD-703_TOD0.02_pos0.15.csv")
axs[2,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD-937_TOD0.02_pos0.2.csv")
axs[2,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD-1170_TOD0.03_pos0.25.csv")
axs[2,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_15fs_input_duration\\GDD-1410_TOD0.03_pos0.3.csv")
axs[2,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange', label='Simulated')
"""
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD1870_TOD-0.04_pos-0.4.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD1640_TOD-0.04_pos-0.35.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD1410_TOD-0.03_pos-0.3.csv")
axs[0,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD1170_TOD-0.03_pos-0.25.csv")
axs[0,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD937_TOD-0.02_pos-0.2.csv")
axs[0,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD703_TOD-0.02_pos-0.15.csv")
axs[1,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD469_TOD-0.01_pos-0.1.csv")
axs[1,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD234_TOD-0.01_pos-0.05.csv")
axs[1,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\GDD0_TOD0.0_pos0.csv")
axs[1,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD-234_TOD0.01_pos0.05.csv")
axs[1,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD-469_TOD0.01_pos0.1.csv")
axs[2,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD-703_TOD0.02_pos0.15.csv")
axs[2,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD-937_TOD0.02_pos0.2.csv")
axs[2,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD-1170_TOD0.03_pos0.25.csv")
axs[2,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD-1410_TOD0.03_pos0.3.csv")
axs[2,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange', label='Simulated')
"""
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1870_TOD-0.04_pos-0.4.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1640_TOD-0.04_pos-0.35.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1410_TOD-0.03_pos-0.3.csv")
axs[0,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD1170_TOD-0.03_pos-0.25.csv")
axs[0,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD937_TOD-0.02_pos-0.2.csv")
axs[0,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD703_TOD-0.02_pos-0.15.csv")
axs[1,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD469_TOD-0.01_pos-0.1.csv")
axs[1,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD234_TOD-0.01_pos-0.05.csv")
axs[1,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\GDD0_TOD0.0_pos0.csv")
axs[1,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-234_TOD0.01_pos0.05.csv")
axs[1,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-469_TOD0.01_pos0.1.csv")
axs[2,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-703_TOD0.02_pos0.15.csv")
axs[2,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-937_TOD0.02_pos0.2.csv")
axs[2,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-1170_TOD0.03_pos0.25.csv")
axs[2,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD-1410_TOD0.03_pos0.3.csv")
axs[2,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange', label='Simulated')

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
axs[0,0].plot(wavel_nm, I1, color='black')
axs[0,1].plot(wavel_nm, I2, color='black')
axs[0,2].plot(wavel_nm, I3, color='black')
axs[0,3].plot(wavel_nm, I4, color='black')
axs[0,4].plot(wavel_nm, I5, color='black')
axs[1,0].plot(wavel_nm, I6, color='black')
axs[1,1].plot(wavel_nm, I7, color='black')
axs[1,2].plot(wavel_nm, I8, color='black')
axs[1,3].plot(wavel_nm, I9, color='black')
axs[1,4].plot(wavel_nm, I10, color='black')
axs[2,0].plot(wavel_nm, I11, color='black')
axs[2,1].plot(wavel_nm, I12, color='black')
axs[2,2].plot(wavel_nm, I13, color='black')
axs[2,3].plot(wavel_nm, I14, color='black')
axs[2,4].plot(wavel_nm, I15, color='black', label='Experimental')

axs[2,4].legend()

plt.show()