import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
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

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
#################################################################################
"""
# Plot peak power at 300nm for 10fs pulse with He

filepath = 'C:\\Users\\iammo\\Documents\\'
df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\good_data\\peak_power_300e-9wavelwindow_5fs__init_10_niter_50.csv")
energy = df_iter.iloc[:,3] # J
pressure = df_iter.iloc[:,4] # bar
radius = df_iter.iloc[:,5]
flength = df_iter.iloc[:,6]
FWHM = df_iter.iloc[:,7]
wavel = df_iter.iloc[:,8]
gas = 'Ne'
grating_pos = df_iter.iloc[:,10]
#print(df_iter)

results = []

Main.radius = radius[0]
Main.flength = flength[0]
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = wavel[0]
Main.τfwhm = FWHM[0]
Main.energy = energy[0]
Main.pressure = pressure[0]
grating_pair_displacement = grating_pos[0]

#print(Main.radius, Main.flength, Main.λ0, Main.τfwhm, Main.energy, Main.pressure, grating_pair_displacement)

domega = 2*np.pi*0.44/FWHM[0]
c=299792458#m/s
omega = np.linspace(2*np.pi*c/wavel[0] - domega/2, 2*np.pi*c/wavel[0] + domega/2, 100)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel[0], domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E**2)

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end

plt.figure()
plt.plot(λ*10**9,Iλ, label='Best After Random Search of 10 Points')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral energy density (J/m)")
plt.title('Maximising Peak Power at 300nm', fontsize=24)

Main.radius = radius[1]
Main.flength = flength[1]
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = wavel[1]
Main.τfwhm = FWHM[1]
Main.energy = energy[1]
Main.pressure = pressure[1]
grating_pair_displacement = grating_pos[1]

domega = 2*np.pi*0.44/FWHM[1]
c=299792458#m/s
omega = np.linspace(2*np.pi*c/wavel[1] - domega/2, 2*np.pi*c/wavel[1] + domega/2, 100)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel[1], domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E**2)

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end

plt.plot(λ*10**9,Iλ, label='Found Optimum')

plt.legend(fontsize=16)
plt.show()
"""
"""
energy = 0.0010386545142497632
pressure = 0.9211608157857013
radius = 0.00013914567008819546
flength = 2.5620983339660492
FWHM = 10e-15
wavel = 800e-9
gas = 'He'
grating_pos = 5.8689828445751676e-05
"""
energy = 0.0006438685563398267
pressure = 6.278805535257321
radius = 0.00014872393094115304
flength = 5.561938015261752
FWHM = 5e-15
wavel = 8e-07
gas = 'He'
grating_pos = 0.00034876718020634436
#print(df_iter)

results = []

Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = energy
Main.pressure = pressure
grating_pair_displacement = grating_pos

#print(Main.radius, Main.flength, Main.λ0, Main.τfwhm, Main.energy, Main.pressure, grating_pair_displacement)

domega = 2*np.pi*0.44/FWHM
c=299792458#m/s
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end

plt.figure()
plt.plot(λ*10**9,Iλ)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral energy density (J/m)")
plt.title('Maximising Peak Power at 300nm', fontsize=24)
plt.show()