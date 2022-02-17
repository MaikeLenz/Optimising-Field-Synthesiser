import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import csv  
#####################################################################################################################
# Read data
#path to txt file
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open ('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=columns[0]
intens1_2=columns[1]
intens1_1=columns[2]
intens1_0=columns[3]
intens0_9=columns[4]
intens0_8=columns[5]
intens0_7=columns[6]
intens0_6=columns[7]
intens0_5=columns[8]
intens0_4=columns[9]
intens0_3=columns[10]
"""
plt.plot(wavel_nm,intens1_2,label="1200mW")
plt.plot(wavel_nm,intens1_1,label="1100mW")
plt.plot(wavel_nm,intens1_0,label="1000mW")
plt.plot(wavel_nm,intens0_9,label="900mW")
plt.plot(wavel_nm,intens0_8,label="800mW")
plt.plot(wavel_nm,intens0_7,label="700mW")
plt.plot(wavel_nm,intens0_6,label="600mW")
plt.plot(wavel_nm,intens0_5,label="500mW")
plt.plot(wavel_nm,intens0_4,label="400mW")
plt.plot(wavel_nm,intens0_3,label="300mW")
plt.legend()
plt.xlabel("Wavelength, nm")
plt.ylabel("Intensity")
plt.show()
"""
#####################################################################################################################
# Convert axis from wavelength to frequency
def wavel_to_freq(wavel):
    c = 299792458
    return 2*np.pi*c/wavel
def freq_to_wavel(freq):
    c = 299792458
    return 2*np.pi*c/freq

omega = []
for i in range(len(wavel_nm)):
    omega.append(wavel_to_freq(wavel_nm[i]*(10**-9)))
#####################################################################################################################
# Fit Gaussians to the data to determine central wavelength and width
def Gauss(x, A, u, FWHM):
    o = FWHM/(2*np.sqrt(2*np.log(2)))
    return A*np.exp(-((x-u)**2)/(2*o**2))

popt1_2, pcov1_2 = curve_fit(Gauss, omega, intens1_2, p0=[4500, 2.4e15, 0.2e15])
popt1_1, pcov1_1 = curve_fit(Gauss, omega, intens1_1, p0=[4500, 2.4e15, 0.2e15])
popt1_0, pcov1_0 = curve_fit(Gauss, omega, intens1_0, p0=[4500, 2.4e15, 0.2e15])
popt0_9, pcov0_9 = curve_fit(Gauss, omega, intens0_9, p0=[4500, 2.4e15, 0.2e15])
popt0_8, pcov0_8 = curve_fit(Gauss, omega, intens0_8, p0=[4500, 2.4e15, 0.2e15])
popt0_7, pcov0_7 = curve_fit(Gauss, omega, intens0_7, p0=[4500, 2.4e15, 0.2e15])
popt0_6, pcov0_6 = curve_fit(Gauss, omega, intens0_6, p0=[4500, 2.4e15, 0.2e15])
popt0_5, pcov0_5 = curve_fit(Gauss, omega, intens0_5, p0=[4500, 2.4e15, 0.2e15])
popt0_4, pcov0_4 = curve_fit(Gauss, omega, intens0_4, p0=[4500, 2.4e15, 0.2e15])
popt0_3, pcov0_3 = curve_fit(Gauss, omega, intens0_3, p0=[4500, 2.4e15, 0.2e15])

"""
plt.plot(omega, intens1_2)
plt.plot(omega, Gauss(omega, *popt1_2))
plt.show()
plt.plot(omega, intens1_1)
plt.plot(omega, Gauss(omega, *popt1_1))
plt.show()
plt.plot(omega, intens1_0)
plt.plot(omega, Gauss(omega, *popt1_0))
plt.show()
plt.plot(omega, intens0_9)
plt.plot(omega, Gauss(omega, *popt0_9))
plt.show()
plt.plot(omega, intens0_8)
plt.plot(omega, Gauss(omega, *popt0_8))
plt.show()
plt.plot(omega, intens0_7)
plt.plot(omega, Gauss(omega, *popt0_7))
plt.show()
plt.plot(omega, intens0_6)
plt.plot(omega, Gauss(omega, *popt0_6))
plt.show()
plt.plot(omega, intens0_5)
plt.plot(omega, Gauss(omega, *popt0_5))
plt.show()
plt.plot(omega, intens0_4)
plt.plot(omega, Gauss(omega, *popt0_4))
plt.show()
plt.plot(omega, intens0_3)
plt.plot(omega, Gauss(omega, *popt0_3))
plt.show()
"""

central_freqs = [popt1_2[1], popt1_1[1], popt1_0[1], popt0_9[1], popt0_8[1], popt0_7[1], popt0_6[1], popt0_5[1], popt0_4[1], popt0_3[1]]
FWHM_freqs = [popt1_2[2], popt1_1[2], popt1_0[2], popt0_9[2], popt0_8[2], popt0_7[2], popt0_6[2], popt0_5[2], popt0_4[2], popt0_3[2]]

central_wavels = []
for i in range(len(central_freqs)):
    central_wavels.append(freq_to_wavel(central_freqs[i]))

powers = [1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]

#####################################################################################################################
# Save the extracted params
header = ['Power, W', 'Central wavelength, m', 'FWHM frequency, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the dataS
    for i in range(len(central_wavels)):
        writer.writerow([powers[i], central_wavels[i], FWHM_freqs[i]])
