"""
Compare different measurements of the width for the GDD scan data
"""
import sys
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import math as math
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
#from theoretical_width import *
from width_methods import *
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

#filepath = "C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
#####################################################################################################################
# Read experimental data
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
I = [I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, I13, I14, I15]

#####################################################################################################################
# Apply width measurement methods

# RMS width
RMS_widths = []
for i in range(len(I)):
    RMS_widths.append(rms_width(wavel_nm, I[i]))

# Normalise and integrate
norm_and_int_widths = []
for i in range(len(I)):
    norm_and_int_widths.append(norm_and_int(wavel_nm, I[i]))

superGauss_widths = []
# Fit a Super Gaussian
for i in range(len(I)):
    popt, pcov = curve_fit(superGauss, wavel_nm, I[i], p0=[4000, 800, 20])
    superGauss_widths.append(popt[2])
    """
    plt.figure()
    plt.plot(wavel_nm, I[i])
    plt.plot(wavel_nm, superGauss(wavel_nm, *popt))
    """

# Determine from threshold
thresh_widths=[]
for i in range(len(I)):
    thresh_widths.append(threshold(wavel_nm, np.array(I[i])))

#####################################################################################################################
# Pulse in time-domain
# First convert to frequencies
c = 299792458
freq = []
for i in range(len(wavel_nm)):
    freq.append(c/(wavel_nm[i]*(10**-9)))

# Fourier transform to time-domain
ts = np.zeros((len(I), math.ceil(len(I[0])/2)))
Its = np.zeros((len(I), math.ceil(len(I[0])/2)))
for i in range(len(I)):
    t, It = f_to_t(freq, I[i])
    #plt.figure()
    #plt.plot(t, It)
    ts[i] = t
    Its[i] = It
#plt.show()

# Determine width of pulse in time-domain
# RMS width
time_RMS_widths = []
for i in range(len(I)):
    time_RMS_widths.append(rms_width(ts[i], np.abs(Its[i])))

# Normalise and integrate
time_norm_and_int_widths = []
for i in range(len(I)):
    time_norm_and_int_widths.append(norm_and_int(ts[i], np.abs(Its[i])))

# Determine from threshold
time_thresh_widths=[]
for i in range(len(I)):
    time_thresh_widths.append(threshold(ts[i], np.abs(Its[i])))

#####################################################################################################################
# Plot results
positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

f, axs = plt.subplots(2,2)
plt.setp(axs[-1, :], xlabel='Compressor Grating Position, mm')
plt.setp(axs[:, 0], ylabel='Width, nm')
plt.suptitle('Wavelength-Domain Widths')

axs[0,0].plot(positions, RMS_widths)
axs[0,0].set_title('RMS Width')
axs[0,1].plot(positions, norm_and_int_widths)
axs[0,1].set_title('Normalised & Integrated')
axs[1,0].plot(positions, superGauss_widths)
axs[1,0].set_title('Super Gaussian Fit')
axs[1,1].plot(positions, thresh_widths)
axs[1,1].set_title('Threshold')

f2, axs2 = plt.subplots(2,2)
plt.setp(axs2[-1, :], xlabel='Compressor Grating Position, mm')
plt.setp(axs2[:, 0], ylabel='Width, s')
plt.suptitle('Time-Domain Widths')

axs2[0,0].plot(positions, time_RMS_widths)
axs2[0,0].set_title('RMS Width')
axs2[0,1].plot(positions, time_norm_and_int_widths)
axs2[0,1].set_title('Normalised & Integrated')
axs2[1,1].plot(positions, time_thresh_widths)
axs2[1,1].set_title('Threshold')
plt.show()