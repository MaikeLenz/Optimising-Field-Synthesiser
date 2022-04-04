import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
import cmath
from scipy.signal import detrend

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")


# Arguments
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
gas = "Ar"
pressure1 = (0,1) # gas pressure in bar, corresponds to 66% of 3.5 atm
pressure2= (1,0)
pressure3=(0.66,0.66)
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy = 1.2e-3 # energy in the pump pulse, 0.5mJ

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure1
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

# Calculations
# setting pressure to (0,pressure) means a gradient from zero up until given value
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval('ω1, Eω = Processing.getEω(duv)')


## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
Eω_allz=Main.Eω #array of Et at all z 
Eω=Eω_allz[:,-1] #last item in each element is pulse shape at the end
Eω0=Eω_allz[:,0]
omegaE=Main.ω1
phase_wrapped = np.angle(Eω)
phase = detrend(np.unwrap(phase_wrapped))
####################################################################################################################################
Main.pressure = pressure2

# Calculations
# setting pressure to (0,pressure) means a gradient from zero up until given value
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval('ω1, Eω = Processing.getEω(duv)')


## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
Eω_allz2=Main.Eω #array of Et at all z 
Eω2=Eω_allz2[:,-1] #last item in each element is pulse shape at the end
Eω02=Eω_allz2[:,0]
omegaE2=Main.ω1
phase_wrapped2 = np.angle(Eω2)
phase2 = detrend(np.unwrap(phase_wrapped2))
####################################################################################################################################
Main.pressure = pressure3

# Calculations
# setting pressure to (0,pressure) means a gradient from zero up until given value
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval('ω1, Eω = Processing.getEω(duv)')


## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
Eω_allz3=Main.Eω #array of Et at all z 
Eω3=Eω_allz3[:,-1] #last item in each element is pulse shape at the end
Eω03=Eω_allz3[:,0]
omegaE3=Main.ω1
phase_wrapped3 = np.angle(Eω3)
phase3 = detrend(np.unwrap(phase_wrapped3))


#plotting

fig,ax = plt.subplots()
# make a plot
ax.plot(omegaE,np.abs(Eω)**2, label="Intensity - (0,P)")
ax.plot(omegaE2,np.abs(Eω2)**2, label="Intensity - (P,0)")
ax.plot(omegaE3,np.abs(Eω3)**2, label="Intensity - 2/3 P")

# set x-axis label
ax.set_xlabel("Angular frequency,/s",fontsize=14)
# set y-axis label
ax.set_ylabel("Intensity, a.u.",fontsize=14)
#plt.legend()
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
#ax2.plot(omegaE,phase2,color="g",label="Phase")
ax2.plot(omegaE,phase,label="(0,P)")
ax2.plot(omegaE2,phase2,label="(P,0)")
ax2.plot(omegaE3,phase3,label="2/3 P")


ax2.set_ylabel("Phase, rad.",fontsize=14)
plt.legend(fontsize=14)

plt.show()