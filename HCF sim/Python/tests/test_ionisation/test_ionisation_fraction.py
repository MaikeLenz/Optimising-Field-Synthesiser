
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

Main.λ0=790e-9
gas = "Ar"
energy = 1.2e-3
Main.energy = energy
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure_Ar=4
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

lam = 2*np.pi*c/omega

# Neon test
energy = 1.2e-3
Main.energy = energy

Main.pressure = pressure_Ar
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval('t, Et = Processing.getEt(duv, 0)')
t=Main.t
Et=Main.Et
Main.Emax=max(Et)
Main.eval('ionrate=Ionisation.ionrate_fun!_PPTcached(gas, λ0)')
Main.eval('frac=Ionisation.ionfrac(ionrate, Et, 1e-14)')
#Main.eval('phi=Ionisation.φ(ionrate)')
Main.eval('keldysh=Ionisation.keldysh(gas,Et)')
#phi=Main.phi
keldysh=Main.keldysh
#print(phi,keldysh)
print(keldysh)
ionfrac=Main.frac
plt.plot(t,np.abs(ionfrac))
plt.figure()
plt.plot(t,Et)
plt.show()