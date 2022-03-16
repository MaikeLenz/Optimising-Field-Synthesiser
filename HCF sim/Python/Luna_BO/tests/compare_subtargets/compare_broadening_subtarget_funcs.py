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
from bossfunction_Luna_debugging import *

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

init=50
iter=150
#############################################################################################################################################
#max wavel bandwidth
path_file='C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\'
#path_file='C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\'

result_wavel,iterations_wavel=Luna_BO_debug(params, initial_values_HCF, function=max_wavel_bandwidth, init_points=init, n_iter=iter)

target_wavel=result_wavel["target"]
energy_wavel=result_wavel["params"]["energy"]
pressure_wavel=result_wavel["params"]["pressure"]
grating_pair_displacement_wavel=result_wavel["params"]["grating_pair_displacement"]


result_freq,iterations_freq=Luna_BO_debug(params, initial_values_HCF, function=max_freq_bandwidth, init_points=init, n_iter=iter)

target_freq=result_freq["target"]
energy_freq=result_freq["params"]["energy"]
pressure_freq=result_freq["params"]["pressure"]
grating_pair_displacement_freq=result_freq["params"]["grating_pair_displacement"]


result_Pt,iterations_Pt=Luna_BO_debug(params, initial_values_HCF, function=max_peak_power, init_points=init, n_iter=iter)

target_Pt=result_Pt["target"]
energy_Pt=result_Pt["params"]["energy"]
pressure_Pt=result_Pt["params"]["pressure"]
grating_pair_displacement_Pt=result_Pt["params"]["grating_pair_displacement"]


result_dt,iterations_dt=Luna_BO_debug(params, initial_values_HCF, function=min_duration, init_points=init, n_iter=iter)

target_dt=result_dt["target"]
energy_dt=result_dt["params"]["energy"]
pressure_dt=result_dt["params"]["pressure"]
grating_pair_displacement_dt=result_dt["params"]["grating_pair_displacement"]

###################################################################################################################################
#save data
# Save the data
header = ['wavel bandw target', 'wavel bandw energy, J', 'wavel bandw pressure, bar', 'wavel bandw grating displacement, m','wavel bandw target', 'wavel bandw energy, J', 'wavel bandw pressure, bar', 'wavel bandw grating displacement, m','wavel bandw target', 'wavel bandw energy, J', 'peak pressure, bar', 'peak power- grating displacement, m','duration- target', 'duration- energy, J', 'duration- pressure, bar', 'duration- grating displacement, m', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna_data\\data\\predicted_max__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\vary_energy_pressure_grating.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the dataS
    writer.writerow([target_wavel,energy_wavel,pressure_wavel, grating_pair_displacement_wavel,target_freq,energy_freq,pressure_freq, grating_pair_displacement_freq,target_Pt,energy_Pt,pressure_Pt, grating_pair_displacement_Pt,target_dt,energy_dt,pressure_dt, grating_pair_displacement_dt, radius, flength, duration, wavel, gas])