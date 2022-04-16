import numpy as np
import sys
import matplotlib.pyplot as plt
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *
from theoretical_width import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
filepath = 'C:\\Users\\iammo\\Documents\\'

# Define fixed params
Main.gas_str = "He"
Main.eval("gas = Symbol(gas_str)")
λ0 = 800e-9
Main.λ0 = λ0
τfwhm = 30e-15

# Define optimum
grating_pair_displacement_in = 5.332105846540716e-05
energy_in = 0.001230333949166748
pressure_in = 3.9785416645362317
radius_in = 0.00015130627656604896
flength_in = 7.930822176101953
Main.energy = energy_in
Main.pressure = pressure_in
Main.radius = radius_in
Main.flength = flength_in

domega = 2*np.pi*0.44/τfwhm
c=299792458
omega = np.linspace(2*np.pi*c/λ0 - 5*domega/2, 2*np.pi*c/λ0 + 5*domega/2, 1000)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                

# Plot the optimum found
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ1, Iλ1 = Processing.getIω(duv, :λ, flength)")
λ1 = Main.λ1
Iλ1 = Main.Iλ1
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
ω2 = Main.ω2
Eω2 = Main.ω2
λ2 = 2*np.pi*c/ω2

om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, ω2, lambda0)

f, axs = plt.subplots()
axs.plot(λ1*(10**9), Iλ1, label='Optimum after 1000 iterations', color='black')
axs.set_xlabel('Wavelength (nm)')
axs.set_ylabel('Intensity (a.u.)')
#axs.legend(fontsize=16)

axs2 = plt.twinx(axs)
axs2.plot(λ2*(10**9), phase, '--', color='black')
axs2.set_ylabel('Phase')

# Plot the optimum after the random search
grating_pair_displacement_in = -0.00021955600793559482
energy_in = 0.0014888610889064948
pressure_in = 4.3064704974458765
radius_in = 9.64517029599389e-05
flength_in = 7.50683997836041
Main.energy = energy_in
Main.pressure = pressure_in
Main.radius = radius_in
Main.flength = flength_in

domega = 2*np.pi*0.44/τfwhm
c=299792458
omega = np.linspace(2*np.pi*c/λ0 - 5*domega/2, 2*np.pi*c/λ0 + 5*domega/2, 1000)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ1, Iλ1 = Processing.getIω(duv, :λ, flength)")
λ1 = Main.λ1
Iλ1 = Main.Iλ1
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
ω2 = Main.ω2
Eω2 = Main.ω2
λ2 = 2*np.pi*c/ω2

om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, ω2, lambda0)

axs.plot(λ1*(10**9), Iλ1, label='Optimum after random search', color='tab:red')
axs.legend(fontsize=16)

axs2 = plt.twinx(axs)
axs2.plot(λ2*(10**9), phase, '--', color='tab:red')

plt.show()