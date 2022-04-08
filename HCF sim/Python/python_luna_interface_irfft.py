
import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
import cmath
from scipy.signal import detrend

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
from get_phase import *
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")


# Arguments
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
gas = "Ar"
pressure = (0,1) # gas pressure in bar, corresponds to 66% of 3.5 atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy = 1.2e-3 # energy in the pump pulse, 0.5mJ

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
# setting pressure to (0,pressure) means a gradient from zero up until given value
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')


## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables

omega=Main.ω
Eomega = Main.Eω

phase=get_phase(omega,Eomega,λ0)


#Fourier Transform
t,Et=f_to_t_irfft(omega,Eomega)
#plotting

fig,ax = plt.subplots()
# make a plot
ax.plot(omega,np.abs(Eomega)**2, label="Intensity")
# set x-axis label
ax.set_xlabel("Angular frequency,/s",fontsize=14)
# set y-axis label
ax.set_ylabel("Intensity, a.u.",fontsize=14)
#plt.legend()
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
#ax2.plot(omegaE,phase2,color="g",label="Phase")
ax2.plot(omega,phase,color="r",label="Phase")

ax2.set_ylabel("Phase, rad.",fontsize=14)
plt.show()
plt.legend()
plt.figure()
plt.plot(t,Et)
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()
plt.show()