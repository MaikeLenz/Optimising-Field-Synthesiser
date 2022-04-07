import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
from scipy.signal import detrend
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *


#from BO.synthesiser_simulation.angfreq_to_time import f_to_t_irfft

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

c = 299792458 # m/s
wavel = 800e-9
fwhm = 30e-15
domega = 2*np.pi*0.441/fwhm
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
pressure = 0.66*3
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

domega = omega[2] - omega[1]
tau = np.pi/domega
phase_raw = np.angle(Eomega)
phase = np.unwrap(phase_raw - omega*tau)
phase -= phase[np.argmin(np.abs(omega - 2.4e-15))]
phase=phase*(-1)
omega=omega[210:340]
phase=phase[210:340]
Eomega=Eomega[210:340]
ax1.plot(omega, phase, '--', label='Phase after')
ax2.plot(omega, np.abs(Eomega)**2, label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ne, 1.2mJ, 0.66*3bar')

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
t,Et=f_to_t_irfft(omega/(2*np.pi),Eomega)
plt.plot(t,np.abs(Et)**2)
plt.show()