import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
from scipy.optimize import curve_fit

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\")
#from ErrorCorrectionFunction_integrate import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\')
from envelopes import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main
Main.using("Luna")


# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy = 0.5e-3 # energy in the pump pulse, 0.5mJ

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

# Calculations
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')

om = Main.ω
Eom = Main.Eω

# First get phase of pulse in freq domain
om0 = moment(om,np.abs(Eom)**2,1)/moment(om,np.abs(Eom)**2,0) # Determine central frequency

plt.plot(om, np.abs(Eom)**2, label='Intensity')
plt.plot(om0, 0, 'o', label='Omega0')
plt.legend()

c=299792458
lambda0 = (2*np.pi*c)/om0
phase = get_phase(om, Eom, lambda0)

# Smooth electric field using super Gaussian filter
λ=(2*np.pi*c)/om
filter = superGauss(λ, 300e-9, 300e-9*0.1)
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
Eom_complex = []
for i in range(len(om)):
    Eom_complex.append(np.abs(Eom_smooth[i])*np.exp(1j*new_phase[i]))

# Now Fourier transform
Et = np.fft.ifft(Eom_complex)
dom = om[2] - om[1]
df = dom/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))
popt,_ = curve_fit(gauss_envelope,t,np.abs(Et)**2, p0=[max(np.abs(Et)**2),2e-14,t[np.argmax(np.abs(Et)**2)]])
print(popt[0])

f, ax = plt.subplots()
ax.plot(om, phase, '--', label='Phase Output from Luna')
ax.plot(om, new_phase, '--', label='Phase After')
ax.plot(om_slice, phase_to_remove, '--', label='Phase Fit')
ax.set_xlabel('Omega')
ax.set_ylabel('Phase')
ax.legend()

ax2 = plt.twinx(ax)
ax2.plot(om, np.abs(Eom_smooth)**2)
ax2.set_ylabel('Intensity')

plt.figure()
plt.plot(t, Et)
plt.xlabel('Time')
plt.ylabel('Electric Field')

plt.show()