import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
from scipy.signal import detrend

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
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
Main.eval("ω, Eω = Processing.getEω(duv)")

omega1=Main.ω
Eomega1=Main.Eω
Eomega1=Eomega1[:,-1]
#phase1 = np.angle(Eomega1)
#phase1 = np.unwrap(phase1)
phase1 = detrend(np.unwrap(np.angle(Eomega1)))

ax1.plot(omega1[:600], phase1[:600], '--', label='Phase after')
ax2.plot(omega1[:600], np.abs(Eomega1[:600])**2, label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ne, 1.2mJ, 0.66*3bar')
plt.show()