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
from bossfunction_Luna_pressures import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["pressure"]

#values:  radius, flength, gas, pressure, wavelength, energy, τfwhm, grating_pair_separation
gas="Ar"
pressure_init=(0,1,1)
radius_init=175e-6
flength_init=1.05
wavel=800e-9
energy_init=1.2e-3
fwhm_init=30e-15
grating_pair_displacement_init=0
initial_values_HCF=[radius_init, flength_init, gas, pressure_init, wavel, energy_init, fwhm_init, grating_pair_displacement_init]
inits=50
iters=1000
result,iterations=Luna_BO_press(params, initial_values_HCF, function=max_peak_power_FT, init_points=inits, n_iter=iters)

#for i, res in enumerate(iterations):
#    print("Iteration {}: \n\t{}".format(i, res))

target = result['target']
#energy = result['params']['energy']
pressure = [0]
for i in range(len(pressure_init)-1):
    pressure.append(result['params']['pressure%s'%i])
#grating_pair_displacement = result['params']['grating_pair_displacement']
# Save the data
header = ['init_points', 'n_iter', 'peak power', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas', 'grating_pair_displacement, m']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_1200e-9wavelwindow_varyfwhm__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'a', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\1.2mJmaxpeakpower_FT_'+gas+str(len(pressure_init))+"pressure_points"+'__init_' + str(inits) + '_niter_' + str(iters) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow([inits, iters, target, energy_init, pressure, radius_init, flength_init, fwhm_init, wavel, gas, grating_pair_displacement_init])
   
#{'target': 4.763738527790547e-07, 'params': {'pressure0': 9.80348248225596, 'pressure1': 9.49469506106953, 'pressure2': 8.704360800010729, 'pressure3': 9.498192503181018, 'pressure4': 9.535506335276617, 'pressure5': 9.79785956770131, 'pressure6': 9.415345993352524, 'pressure7': 8.454469323276149, 'pressure8': 9.05251263927737}}