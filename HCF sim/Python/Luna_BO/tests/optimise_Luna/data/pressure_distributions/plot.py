
import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from Luna_subtarget import *
from compressor_grating_to_values import *

Main.using("Luna")
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\pressure_distributions\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"Ar3pressure_points__init_50_niter_150.csv")

energy=df_0.iloc[0][3]
pressure=df_0.iloc[0][4]
radius=df_0.iloc[0][5]
flength=df_0.iloc[0][6]
FWHM=df_0.iloc[0][7]
wavel=df_0.iloc[0][8]
gas=df_0.iloc[0][9]
grating_pair_displacement=df_0.iloc[0][10]

#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = energy

print(pressure,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 1000)

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2


Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    
# Get values
t_opt = Main.t
Et_allz_opt = Main.Et # array of Et at all z 
Et_opt = Et_allz_opt[:,-1] # last item in each element is pulse shape at the end
Et0=Et_allz_opt[:,0] #first item in each element is pulse shape at the start

λ_opt = Main.λ
Iλ_opt = Main.Iλ
Iλ_opt=Iλ_opt.reshape(len(Iλ_opt),)
omega_opt=Main.ω
Iomega_opt=Main.Iω
Iomega_opt=Iomega_opt.reshape((-1,))[0:500]
omega_opt=omega_opt[0:500]

###########################################################################################################################################################################
# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Pmax=1.5
Main.pressure = 0.66*Pmax
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = energy

print(pressure,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 1000)

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2


Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    
# Get values
t_opt2 = Main.t
Et_allz_opt2 = Main.Et # array of Et at all z 
Et_opt2 = Et_allz_opt2[:,-1] # last item in each element is pulse shape at the end
Et02=Et_allz_opt2[:,0] #first item in each element is pulse shape at the start

λ_opt2 = Main.λ
Iλ_opt2 = Main.Iλ
Iλ_opt2=Iλ_opt2.reshape(len(Iλ_opt2),)
omega_opt2=Main.ω
Iomega_opt2=Main.Iω
Iomega_opt2=Iomega_opt2.reshape((-1,))[0:500]
omega_opt2=omega_opt2[0:500]

####################################################################################################################################################

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = 0.66*Pmax
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = 1.2e-3

print(pressure,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 1000)

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=0)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2


Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    
# Get values
t_opt3 = Main.t
Et_allz_opt3 = Main.Et # array of Et at all z 
Et_opt3 = Et_allz_opt3[:,-1] # last item in each element is pulse shape at the end
Et03=Et_allz_opt3[:,0] #first item in each element is pulse shape at the start

λ_opt3 = Main.λ
Iλ_opt3 = Main.Iλ
Iλ_opt3=Iλ_opt3.reshape(len(Iλ_opt3),)
omega_opt3=Main.ω
Iomega_opt3=Main.Iω
Iomega_opt3=Iomega_opt3.reshape((-1,))[0:500]
omega_opt3=omega_opt3[0:500]


#plotting
plt.figure()
#plt.plot(λ,Iλ,label="SPM Prediction")

plt.plot(λ_opt,Iλ_opt,label="Optimised")
plt.plot(λ_opt2,Iλ_opt2,label="Constant Pressure")
plt.plot(λ_opt3,Iλ_opt3,label="SPM Prediction")

plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")
plt.legend()
plt.figure()
#plt.plot(omega,Iomega,label="SPM Prediction")

#plt.plot(width_plot,bar_height, label="rms width")
plt.plot(omega_opt,Iomega_opt,label="Optimised")
plt.plot(omega_opt2,Iomega_opt2,label="Constant Pressure")
plt.plot(omega_opt3,Iomega_opt3,label="SPM Prediction")

plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.figure()
#plt.plot(t,Et,label="SPM Prediction")

plt.plot(t_opt,Et_opt,label="Optimised")
plt.plot(t_opt2,Et_opt2,label="Constant Pressure")
plt.plot(t_opt3,Et_opt3,label="SPM Prediction")

#plt.plot(t,Et0,label="z=0m")
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()
plt.show()