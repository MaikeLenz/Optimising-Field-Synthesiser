import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *
from theoretical_width import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\')
from envelopes import *

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
filepath = 'C:\\Users\\iammo\\Documents\\'
##################################################################################
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_with_FT_and_phase\\300nm_optimum_data_angfreq.csv")
ω2 = df.iloc[:,0]
Eω2_real = df.iloc[:,1]
Eω2_imag = df.iloc[:,2]
Eω2 = Eω2_real + Eω2_imag
c = 299792458
λ2 = 2*np.pi*c/ω2
df2 = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_with_FT_and_phase\\300nm_optimum_data_wavel.csv")
λ1 = df.iloc[:,0]
Iλ1 = df.iloc[:,1]

om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, Eω2, lambda0)

f, axs = plt.subplots(1,2)
axs[0].plot(λ1*(10**9), Iλ1, label='Optimum after 1000 iterations', color='black')
axs[0].set_xlabel('Wavelength (nm)')
axs[0].set_ylabel('Intensity (a.u.)')

filter = []
for i in range(len(λ2)):
    filter.append(np.exp(-((λ2[i]-300e-9)/(300e-9*0.1))**4))
Eom_smooth = []
for i in range(len(Eω2)):
    Eom_smooth.append(Eω2[i]*filter[i])

axs2 = plt.twinx(axs[1])
axs[1].plot(λ2*(10**9), np.abs(Eom_smooth)**2, color='black')
axs[1].set_xlabel('Wavelength (nm)')
axs[1].set_ylabel('Intensity (a.u.)')
##################################################################################
# Get pulse in time-domain
# Slice phase to only select part within pulse
thresh = 0.1
rows = np.where(np.abs(Eom_smooth)**2 > max(np.abs(Eom_smooth)**2)*thresh)[0]

min_index = rows[0]
max_index = rows[-1]
phase_slice = phase[min_index-25:max_index+25]
om_slice = ω2[min_index-25:max_index+25]
lambda_slice = 2*np.pi*c/om_slice
axs2.plot(lambda_slice*(10**9), phase_slice, '--', color='black')
axs2.set_ylabel('Phase')

# Fit a quadratic to the phase and remove this
def quad(x, a, b, c):
    return a*(x**2) + b*x + c
quad_popt, _ = curve_fit(quad, om_slice, phase_slice, p0=[1,1,0])
phase_to_remove = quad(om_slice, *quad_popt)
new_phase = np.zeros(len(ω2))
for i in range(len(phase_to_remove)):
    new_phase[i+min_index-25] += phase_slice[i] - phase_to_remove[i]

# Add the phase back to the intensity profile
Eom_complex = []
for i in range(len(ω2)):
    Eom_complex.append(np.abs(Eom_smooth[i])*np.exp(-1j*new_phase[i]))

# Now Fourier transform
Et = np.fft.ifft(Eom_smooth) # Finding FT of pulse with whole phase spectrum
Et = np.fft.ifft(Eom_complex) # Finding FT of pulse with quadratic phase removed
dom = ω2[2] - ω2[1]
df = dom/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))
f2, axst = plt.subplots()
axst.plot(t, np.abs(Et)**2, color='black', label='Optimum after 1000 iterations')
axst.set_xlabel('Time (s)')
axst.set_ylabel('Intensity (a.u.)')

plt.show()