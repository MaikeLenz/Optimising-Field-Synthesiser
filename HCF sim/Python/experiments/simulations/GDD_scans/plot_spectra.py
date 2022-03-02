import matplotlib.pyplot as plt
import pandas as pd

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"

"""
# Plotting in subplots
# First plot experimental spectra
fig_exp, axs_exp = plt.subplots(3,5)
fig_exp.suptitle('Experimental GDD Scan', size=24)
#plt.setp(axs_exp, xlim=(0,1250))
plt.setp(axs_exp[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_exp[:, 0], ylabel='Intensity')

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
axs_exp[0,0].plot(wavel_nm, I1, color='black')
axs_exp[0,1].plot(wavel_nm, I2, color='black')
axs_exp[0,2].plot(wavel_nm, I3, color='black')
axs_exp[0,3].plot(wavel_nm, I4, color='black')
axs_exp[0,4].plot(wavel_nm, I5, color='black')
axs_exp[1,0].plot(wavel_nm, I6, color='black')
axs_exp[1,1].plot(wavel_nm, I7, color='black')
axs_exp[1,2].plot(wavel_nm, I8, color='black')
axs_exp[1,3].plot(wavel_nm, I9, color='black')
axs_exp[1,4].plot(wavel_nm, I10, color='black')
axs_exp[2,0].plot(wavel_nm, I11, color='black')
axs_exp[2,1].plot(wavel_nm, I12, color='black')
axs_exp[2,2].plot(wavel_nm, I13, color='black')
axs_exp[2,3].plot(wavel_nm, I14, color='black')
axs_exp[2,4].plot(wavel_nm, I15, color='black')

# Now plot simulated data

fig_sim, axs_sim = plt.subplots(3,5)
fig_sim.suptitle('Simulated GDD Scan', size=24)
plt.setp(axs_sim, xlim=(650,1000))
plt.setp(axs_sim[-1, :], xlabel='Wavelength, nm')
plt.setp(axs_sim[:, 0], ylabel='Intensity')

df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.0984_TOD2.15_pos-0.4.csv")
axs_sim[0,0].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.101_TOD2.2_pos-0.35.csv")
axs_sim[0,1].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.103_TOD2.25_pos-0.3.csv")
axs_sim[0,2].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.105_TOD2.3_pos-0.25.csv")
axs_sim[0,3].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.108_TOD2.35_pos-0.2.csv")
axs_sim[0,4].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.11_TOD2.4_pos-0.15.csv")
axs_sim[1,0].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.112_TOD2.45_pos-0.1.csv")
axs_sim[1,1].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.115_TOD2.5_pos-0.05.csv")
axs_sim[1,2].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.117_TOD2.55_pos0.csv")
axs_sim[1,3].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.12_TOD2.6_pos0.05.csv")
axs_sim[1,4].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.122_TOD2.66_pos0.1.csv")
axs_sim[2,0].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.124_TOD2.71_pos0.15.csv")
axs_sim[2,1].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.127_TOD2.76_pos0.2.csv")
axs_sim[2,2].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.129_TOD2.81_pos0.25.csv")
axs_sim[2,3].plot(df.iloc[:,0], df.iloc[:,1], color='black')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.131_TOD2.86_pos0.3.csv")
axs_sim[2,4].plot(df.iloc[:,0], df.iloc[:,1], color='black')

plt.show()
"""
# Plotting on same plot
fig, axs = plt.subplots(3,5)
fig.suptitle('GDD Scan Experimental vs Simulated', size=24)
plt.setp(axs, xlim=(500,900))
plt.setp(axs[-1, :], xlabel='Wavelength, nm')
plt.setp(axs[:, 0], ylabel='Intensity')

# Plot simulated data

df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.0984_TOD2.15_pos-0.4.csv")
axs[0,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.101_TOD2.2_pos-0.35.csv")
axs[0,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.103_TOD2.25_pos-0.3.csv")
axs[0,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.105_TOD2.3_pos-0.25.csv")
axs[0,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.108_TOD2.35_pos-0.2.csv")
axs[0,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.11_TOD2.4_pos-0.15.csv")
axs[1,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.112_TOD2.45_pos-0.1.csv")
axs[1,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.115_TOD2.5_pos-0.05.csv")
axs[1,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.117_TOD2.55_pos0.csv")
axs[1,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.12_TOD2.6_pos0.05.csv")
axs[1,4].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.122_TOD2.66_pos0.1.csv")
axs[2,0].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.124_TOD2.71_pos0.15.csv")
axs[2,1].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.127_TOD2.76_pos0.2.csv")
axs[2,2].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.129_TOD2.81_pos0.25.csv")
axs[2,3].plot(df.iloc[:,0], df.iloc[:,1]/10, color='tab:orange')
df = pd.read_csv(filepath+"simulations\\GDD_scans\\data\\real_range\\GDD-0.131_TOD2.86_pos0.3.csv")
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