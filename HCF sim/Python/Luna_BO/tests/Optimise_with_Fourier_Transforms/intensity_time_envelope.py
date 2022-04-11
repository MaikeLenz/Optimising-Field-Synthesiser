import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.optimize import curve_fit

import csv
from scipy.signal import detrend
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
from get_phase import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\")
from envelopes import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

c = 299792458 # m/s
wavel = 800e-9
fwhm = 30e-15
#domega = 2*np.pi*0.441/fwhm
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
gas = "Ne"
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = wavel
Main.τfwhm = fwhm

energy = 1.2e-3
pressure = (0,3)
Main.pressure = pressure
Main.energy = energy


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.set_xlabel('Angular Frequency')
ax1.set_ylabel('Phase')
ax2.set_ylabel('Intensity')

# Pass data to Luna
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')

omega = Main.ω
Eomega = Main.Eω

phase=get_phase(omega,Eomega,wavel)

i1=210
i2=240
ax1.plot(omega[i1,i2], phase[i1,i2], '--', label='Phase after')
ax2.plot(omega[i1,i2], np.abs(Eomega[i1,i2])**2, label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

"""
# Save data
header = ['Angular frequency (rad/s)', 'Real Electric Field (a.u.)', 'Imaginary Electric Field (a.u.)']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Test_Data_grid.csv', 'w', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Test_Data_grid_zoom.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(omega)):
        writer.writerow([omega[i], Eomega[i].real, Eomega[i].imag])
"""
plt.show()
#Fourier transform to get E(t)
Et = np.fft.ifft(Eomega)
dom = omega[2] - omega[1]
df = dom/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))

popt,_=curve_fit(gauss_envelope,t,Et, p0=[1e12,10e-15,0])
plt.plot(t,np.abs(Et)**2)
plt.plot(t,gauss_envelope(t,*popt))
plt.show()