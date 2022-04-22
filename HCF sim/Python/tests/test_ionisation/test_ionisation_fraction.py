
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
gas = "Ne"
energy = 1.2e-3
Main.energy = energy
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure_Ar=1
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
energy = 3e-3
Main.energy = energy

Main.pressure = pressure_Ar
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval('t, Et = Processing.getEt(duv, 0)')
t=Main.t
Et=Main.Et
Et=Et.reshape((-1,))

print(Et.shape)
dt=t[2]-t[1]
Main.dt=dt
#Main.Emax=max(Et)
#Main.eval('ionrate=Ionisation.ionrate_fun!_ADK(gas)')
Main.eval("ionpot=PhysData.ionisation_potential(gas;unit=:SI)")
#Main.ionpot=15.6*1.6*10**(-19)
ionpot=Main.ionpot
Main.eval("ionrate=Ionisation.ionrate_fun!_ADK(ionpot)")
rate=Main.ionrate
print(rate)
print("ionpot=",ionpot)
Main.eval("thresh=Ionisation.ADK_threshold(ionpot)")
thresh=Main.thresh
print("thresh=",thresh)


def I_W_cm2(energy,duration,fibre_radius):
    w=0.64*fibre_radius*10**2 #in cm
    return energy/(duration*np.pi*w**2)

def max_E_V_m(I_W_cm2):
    return 2740*np.sqrt(I_W_cm2)

I_calc=I_W_cm2(1.2e-3,30e-15,175e-6)
print(I_calc)
E_max=max_E_V_m(I_calc)
print(max(np.abs(Et)))
print(E_max)
Main.E=E_max*Et/max(np.abs(Et))

Main.eval('frac=Ionisation.ionfrac(ionrate,E,dt)')

#Main.eval('phi=Ionisation.φ(ionrate)')
#Main.eval('keldysh=Ionisation.keldysh(gas,E)')
#phi=Main.phi
#keldysh=Main.keldysh
#print(phi,keldysh)
#print(keldysh)
ionfrac=Main.frac
plt.plot(t*10**15,np.abs(ionfrac))
#plt.plot(t,ionfrac.imag)
#plt.plot(t,ionfrac.real)
plt.ylabel("Ionisation fraction",fontsize=14)
plt.xlabel("Time, fs",fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.figure()
plt.plot(t,Et)
plt.show()