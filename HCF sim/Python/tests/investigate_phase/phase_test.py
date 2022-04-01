import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
from scipy.signal import detrend
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

"""
c = 299792458 # m/s
wavel = 800e-9
fwhm = 30e-15
domega = 2*np.pi*0.441/fwhm
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
gas = "Ar"
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = wavel

energy = 1.2e-3
pressure = 0.66*1
Main.pressure = pressure
Main.energy = energy

omega = np.linspace(2*np.pi*c/wavel - 50*domega/2, 2*np.pi*c/wavel + 50*domega/2, 100)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E)**2
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(omega, ϕω, '--', label='Phase before')
ax2.plot(omega, Iω, label='Intensity before')
ax1.set_xlabel('Angular Frequency')
ax1.set_ylabel('Phase')
ax2.set_ylabel('Intensity')

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("ω, Eω = Processing.getEω(duv)")

omega1=Main.ω
Eomega1=Main.Eω
Eomega1=Eomega1[:,-1]
#phase1 = np.angle(Eomega1)
#phase1 = np.unwrap(phase1)
phase1 = detrend(np.unwrap(np.angle(Eomega1)))

ax1.plot(omega1[:600], phase1[:600], '--', label='Phase after')
ax2.plot(omega1[:600], (np.abs(Eomega1[:600])**2)*(10**17), label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ar, 1.2mJ, 0.66*1bar')
#plt.show()

# Try another energy and pressure
energy = 2e-3
pressure = 0.66*10
Main.pressure = pressure
Main.energy = energy

omega = np.linspace(2*np.pi*c/wavel - 50*domega/2, 2*np.pi*c/wavel + 50*domega/2, 100)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E)**2
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(omega, ϕω, '--', label='Phase before')
ax2.plot(omega, Iω, label='Intensity before')
ax1.set_xlabel('Angular Frequency')
ax1.set_ylabel('Phase')
ax2.set_ylabel('Intensity')

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("ω, Eω = Processing.getEω(duv)")

omega1=Main.ω
Eomega1=Main.Eω
Eomega1=Eomega1[:,-1]
#phase1 = np.angle(Eomega1)
#phase1 = np.unwrap(phase1)
phase1 = detrend(np.unwrap(np.angle(Eomega1)))

ax1.plot(omega1[:600], phase1[:600], '--', label='Phase after')
ax2.plot(omega1[:600], (np.abs(Eomega1[:600])**2)*(10**17), label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ar, 2mJ, 0.66*10bar')
#plt.show()

# Another energy and pressure
energy = 0.4e-3
pressure = 0.66*0.2
Main.pressure = pressure
Main.energy = energy

omega = np.linspace(2*np.pi*c/wavel - 50*domega/2, 2*np.pi*c/wavel + 50*domega/2, 100)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E)**2
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(omega, ϕω, '--', label='Phase before')
ax2.plot(omega, Iω, label='Intensity before')
ax1.set_xlabel('Angular Frequency')
ax1.set_ylabel('Phase')
ax2.set_ylabel('Intensity')

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("ω, Eω = Processing.getEω(duv)")

omega1=Main.ω
Eomega1=Main.Eω
Eomega1=Eomega1[:,-1]
#phase1 = np.angle(Eomega1)
#phase1 = np.unwrap(phase1)
phase1 = detrend(np.unwrap(np.angle(Eomega1)))

ax1.plot(omega1[:600], phase1[:600], '--', label='Phase after')
ax2.plot(omega1[:600], (np.abs(Eomega1[:600])**2)*(10**17), label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ar, 0.4mJ, 0.66*0.2bar')
plt.show()
"""
"""
# Try using Luna Gaussian pulse instead
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
ax2.plot(omega1[:600], (np.abs(Eomega1[:600])**2)*(10**17), label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ne, 1.2mJ, 0.66*3bar')
plt.show()
"""
# Try an inital pulse with GDD
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

energy = 1.2e-3
pressure = 0.66*3
Main.pressure = pressure
Main.energy = energy

omega = np.linspace(2*np.pi*c/wavel - 50*domega/2, 2*np.pi*c/wavel + 50*domega/2, 100)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=500e-30, TOD=0)
Iω = np.abs(E)**2
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(omega, ϕω, '--', label='Phase before')
ax2.plot(omega, Iω, label='Intensity before')
ax1.set_xlabel('Angular Frequency')
ax1.set_ylabel('Phase')
ax2.set_ylabel('Intensity')

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("ω, Eω = Processing.getEω(duv)")

omega1=Main.ω
Eomega1=Main.Eω
Eomega1=Eomega1[:,-1]
#phase1 = np.angle(Eomega1)
#phase1 = np.unwrap(phase1)
phase1 = detrend(np.unwrap(np.angle(Eomega1)))

ax1.plot(omega1[:600], phase1[:600], '--', label='Phase after')
ax2.plot(omega1[:600], (np.abs(Eomega1[:600])**2)*(10**17), label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ne, 1.2mJ, 0.66*3bar, 500fs^2 GDD')
plt.show()