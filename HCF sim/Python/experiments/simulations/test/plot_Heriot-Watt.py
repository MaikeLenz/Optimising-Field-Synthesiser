import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['axes.labelsize'] = 20

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *
from theoretical_width import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *
import pandas as pd
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_with_FT_and_phase\\spectrum_data\\200nm_optimum.csv"

df_0 = pd.read_csv(filepath,skipinitialspace=True)
omega=df_0.iloc[:,0]
Eomega_real=df_0.iloc[:,1]
Eomega_imag=df_0.iloc[:,2]
 
Eom = Eomega_real + 1j*Eomega_imag
om=[]
for i in omega:
    om.append(i)
om=np.array(om)

# First get phase of pulse in freq domain
om0 = moment(om,np.abs(Eom)**2,1)/moment(om,np.abs(Eom)**2,0) # Determine central frequency
c=299792458
lambda0 = (2*np.pi*c)/om0
print(lambda0)
phase = get_phase(om, Eom, lambda0)

# Smooth electric field using super Gaussian filter
λ=(2*np.pi*c)/om



filter = []
for i in range(len(λ)):
    filter.append(np.exp(-((λ[i]-300e-9)/(300e-9*0.1))**4))

Eom_smooth = []
for i in range(len(Eom)):
    Eom_smooth.append(Eom[i]*filter[i])

# Slice phase to only select part within pulse
thresh = 0.1
rows = np.where(np.abs(Eom_smooth)**2 > max(np.abs(Eom_smooth)**2)*thresh)[0]
min_index = rows[0]
max_index = rows[-1]

phase_slice = phase[min_index-25:max_index+25]
om_slice = om[min_index-25:max_index+25]

# Fit a quadratic to the phase and remove this
def quad(x, a, b, c):
    return a*(x**2) + b*x + c
quad_popt, _ = curve_fit(quad, om_slice, phase_slice, p0=[1,1,0])
phase_to_remove = quad(om_slice, *quad_popt)
new_phase = np.zeros(len(om))

for i in range(len(phase_to_remove)):
    new_phase[i+min_index-25] += phase_slice[i] - phase_to_remove[i]

# Add the phase back to the intensity profile
Eom_complex0 = [] # raw data
Eom_complex1 = [] # quad phase removed
Eom_complex2 = [] # phase zeroed
for i in range(len(om)):
    Eom_complex0.append(np.abs(Eom_smooth[i])*np.exp(-1j*phase[i]))
    Eom_complex1.append(np.abs(Eom_smooth[i])*np.exp(-1j*new_phase[i]))
    Eom_complex2.append(np.abs(Eom_smooth[i])*np.exp(-1j*0))

# Now Fourier transform
Et0 = np.fft.fftshift(np.fft.ifft(Eom_complex0))
f_step = (omega[1]-omega[0])/(2*np.pi)
t0 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex0), d=f_step))

Et1 = np.fft.fftshift(np.fft.ifft(Eom_complex1))
f_step = (omega[1]-omega[0])/(2*np.pi)
t1 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex1), d=f_step))

Et2 = np.fft.fftshift(np.fft.ifft(Eom_complex2))
f_step = (omega[1]-omega[0])/(2*np.pi)
t2 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex2), d=f_step))

plt.plot(t1*1e15, np.abs(Et1)**2, label="quad phase subtracted")
plt.plot(t2*1e15, np.abs(Et2)**2, label="zeroed phase")
plt.title(filepath)
plt.xlabel("time (fs)")
plt.ylabel("Intensity (arb.units)")
plt.legend()
plt.show()

