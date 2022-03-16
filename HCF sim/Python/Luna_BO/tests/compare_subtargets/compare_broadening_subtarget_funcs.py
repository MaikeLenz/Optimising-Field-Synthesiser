import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
import csv
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna_record_iters import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["energy", "pressure", "grating_pair_displacement"]

#values:  radius, flength, gas, pressure, wavelength, energy, τfwhm, grating_pair_separation
gas="Ne"
initial_values_HCF=[175e-6, 1.05, gas, 0.66*3, 800e-9, 1.1e-3, 30e-15, 0]
# Define experimental params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
wavel=800e-9
duration=30e-15
domega=2*np.pi*0.44/duration
#############################################################################################################################################
#max wavel bandwidth
path_file='C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\'
#path_file='C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\'

result_wavel,iterations_wavel=Luna_BO_record_iters(params, initial_values_HCF, function=max_wavel_bandwidth, init_points=50, n_iter=50, save_path=path_file)
energy_wavel=result_wavel["params"]["energy"]
pressure_wavel=result_wavel["params"]["pressure"]
grating_pair_displacement_wavel=result_wavel["params"]["grating_pair_displacement"]

omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)
GDD,TOD=compressor_grating_values(grating_pair_displacement_mm=1000*grating_pair_displacement_wavel, wavel_m=wavel)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.energy = energy_wavel
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.λ0 = wavel
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure_wavel

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')




result_freq,iterations_freq=Luna_BO_record_iters(params, initial_values_HCF, function=max_freq_bandwidth, init_points=50, n_iter=50, save_path=path_file)

result_Pt,iterations_Pt=Luna_BO_record_iters(params, initial_values_HCF, function=max_peak_power, init_points=50, n_iter=50, save_path=path_file)

result_dt,iterations_dt=Luna_BO_record_iters(params, initial_values_HCF, function=min_duration, init_points=1, n_iter=1, save_path=path_file)

