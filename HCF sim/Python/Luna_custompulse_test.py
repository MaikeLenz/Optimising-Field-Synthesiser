
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

# Define custom pulse in frequency domain
#energy = 0.5e-3 # energy in the pump pulse, 0.5mJ
energy = 1.2e-3
c = 299792458 # m/s
wavel = 800e-9
fwhm = 30e-15
domega = 2*np.pi*0.441/fwhm
#domega = 2e15
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E)**2

Main.energy = energy
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.λ0 = wavel

# Define experimental params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
gas = "Ne"
#pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
pressure = 0.66*3
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("ω1, Eω = Processing.getEω(duv)")

## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
λ = Main.λ
Iλ = Main.Iλ
t = Main.t
omega=Main.ω
Iomega=Main.Iω
Iomega=Iomega.reshape((-1,))[0:500]
omega=omega[0:500]
omega1=Main.ω1
Eomega1=Main.Eω
Eomega1=Eomega1[:,-1]

Et_allz=Main.Et #array of Et at all z 
Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
Et0=Et_allz[:,0] #first item in each element is pulse shape at the start
#note Et is complex

#plotting
plt.figure()
plt.plot(λ,Iλ)
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")
"""
plt.figure()
plt.plot(omega,Iomega)
#plt.plot(width_plot,bar_height, label="rms width")
plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.figure()
plt.plot(t,Et,label="z=1m")
plt.plot(t,Et0,label="z=0")
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()
plt.show()
"""
plt.figure()
plt.plot(omega1, Eomega1)
plt.xlabel("Angular Frequency")
plt.ylabel("Electric Field")
plt.show()

# Save data
header = ['Angular frequency (rad/s)', 'Real Electric Field (a.u.)', 'Imaginary Electric Field (a.u.)']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Test_Data2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(omega1)):
        writer.writerow([omega1[i], Eomega1[i].real, Eomega1[i].imag])
        