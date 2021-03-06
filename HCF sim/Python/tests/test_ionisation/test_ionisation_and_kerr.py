
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

c = 299792458 # m/s
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
wavel = 800e-9
fwhm = 30e-15
domega = 2*np.pi*0.441/fwhm
Main.radius = radius
Main.flength = flength
Main.λ0 = wavel

omega = np.linspace(2*np.pi*c/wavel - 5*domega/2, 2*np.pi*c/wavel + 5*domega/2, 100)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E)**2
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω

wavel_array = 2*np.pi*c/omega
initial_width = rms_width(wavel_array, Iω)
print(initial_width*(10**9))

"""
# Neon test
gas = "Ne"
energy = 3e-3
#energy = 1.5e-3
pressure = (0, 3.5)
Main.energy = energy
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

f, axs = plt.subplots(1,2)
axs[0].plot(λ*(10**9), Iλ, label='With all effects')
axs[0].set_xlabel("Wavelength (nm)")
axs[0].set_ylabel("Spectral energy density (J/m)")
axs[0].set_title('Neon, 3mJ, 3.5bar', size=24)
print('Neon width with all = {}'.format(rms_width(λ*(10**9), Iλ)))

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6), plasma=false)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

axs[0].plot(λ*(10**9), Iλ, '--',label='Without ionisation')
print('Neon width without ionisation = {}'.format(rms_width(λ*(10**9), Iλ)))

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6), kerr=false)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

axs[0].plot(λ*(10**9), Iλ, ':', label='Without Kerr effect')
#axs[0].legend(fontsize=16, loc='upper right')
print('Neon width without Kerr = {}'.format(rms_width(λ*(10**9), Iλ)))


# Argon test
gas = "Ar"
energy = 1.5e-3
pressure = (0, 1.5)
Main.energy = energy
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

axs[1].plot(λ*(10**9), Iλ, label='With all effects')
axs[1].set_xlabel("Wavelength (nm)")
#plt.ylabel("Spectral energy density (J/m)")
axs[1].set_title('Argon, 1.5mJ, 1.5bar', size=24)
print('Argon width with all = {}'.format(rms_width(λ*(10**9), Iλ)))

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6), plasma=false)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

axs[1].plot(λ*(10**9), Iλ, '--', label='Without ionisation')
print('Argon width without ionisation = {}'.format(rms_width(λ*(10**9), Iλ)))

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6), kerr=false)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

axs[1].plot(λ*(10**9), Iλ, ':', label='Without Kerr effect')
#axs[1].legend(fontsize=16, loc='upper right')
axs[1].legend(fontsize=16, bbox_to_anchor=(1.04,1), loc="upper left")
print('Argon width without Kerr = {}'.format(rms_width(λ*(10**9), Iλ)))
plt.show()
"""
# Argon test blueshift
gas = "Ar"
energy = 1.5e-3
pressure = (0, 5)
Main.energy = energy
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

plt.figure()
plt.plot(λ*(10**9), Iλ, label='With all effects')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral energy density (J/m)")
plt.title('Argon, 1.5mJ, 5bar', size=24)
print('Argon width with all = {}'.format(rms_width(λ*(10**9), Iλ)))

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6), plasma=false)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ = Main.λ
Iλ = Main.Iλ

plt.plot(λ*(10**9), Iλ, '--', label='Without ionisation')
print('Argon width without ionisation = {}'.format(rms_width(λ*(10**9), Iλ)))

plt.legend(fontsize=16, loc="upper right")
plt.show()