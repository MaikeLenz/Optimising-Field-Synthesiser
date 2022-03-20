import sys
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from pulse_with_GDD import *
from angfreq_to_time import *
import numpy as np
import matplotlib.pyplot as plt
import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using('Luna')

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

c = 3e8
wavel0 = 800e-9
fwhm = 30e-15
domega = 2*np.pi*0.44/fwhm
omega = np.linspace(2*np.pi*c/wavel0 - domega/2, 2*np.pi*c/wavel0 + domega/2, 100)
GDD = 100e-30
TOD = 1000e-45

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.pressure = 3
Main.energy = 1e-3
Main.radius = 200e-6
Main.flength = 1
Main.gas_str = 'Ne'
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = wavel0

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval('t, Et = Processing.getEt(duv)')
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
Et0=Et_allz[:,0] #first item in each element is pulse shape at the start

f, axs = plt.subplots(1,2)
axs[0].plot(omega, Iω)
axs[0].set_xlabel('Angular frequency (/s)')
axs[0].set_ylabel('Intensity (a.u.)')

axs[1].plot(t*(10**15), Et0)
axs[1].set_xlabel('Time (fs)')
axs[1].set_ylabel('Electric field (a.u.)')
plt.show()