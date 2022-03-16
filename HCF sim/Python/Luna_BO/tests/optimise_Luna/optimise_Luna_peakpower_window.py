import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
import csv
from numpy.random import *
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main

import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna_debugging import *

#################################################################################################################
#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["energy", "pressure", "radius", "flength","grating_pair_displacement", "FWHM"]

init_points = 10
n_iter = 50
wavel = 800e-9
gas = 'Ne'
GDD = 0

FWHM_init = 25e-15
radius_init = 175e-6
flength_init = 1
pressure_init = 3*0.66
energy_init = 0.5e-3
#radius_init = randint(50, 500)*(10**-6)
#flength_init = randint(1, 30)*0.1
#pressure_init = randint(1, 10)
#energy_init= randint(1, 10)*(10**-4)

# This part is optional - run first with just initial points for comparison
#values:  radius, flength, gas, pressure, wavelength, GDD, energy
initial_values_HCF=[radius_init, flength_init, gas, pressure_init, wavel, energy_init,FWHM_init, 0]
goal_wavel=300e-9
wavel_bounds=(0.9*goal_wavel,1.1*goal_wavel)
opt_dict,res = Luna_BO_debug(params, initial_values_HCF, function=max_intens_integral, wavel_bounds=wavel_bounds,init_points=init_points, n_iter=1)
max_intens_intergral = opt_dict['target']
energy = opt_dict['params']['energy']
pressure = opt_dict['params']['pressure']
radius = opt_dict['params']['radius']
flength = opt_dict['params']['flength']
grating_pair_displacement = opt_dict['params']['grating_pair_displacement']
τfwhm = opt_dict['params']['FWHM']

# Save the data
header = ['init_points', 'n_iter', 'peak power', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas', 'grating_pair_displacement, m']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_300e-9wavelwindow_varyfwhm__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
#with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_1000e-9wavelwindow__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the dataS
    writer.writerow([init_points, 0, max_intens_integral, energy, pressure, radius, flength, τfwhm, wavel, gas, grating_pair_displacement])

# Run optimisation
opt_dict,res = Luna_BO_debug(params, initial_values_HCF, function=max_intens_integral, wavel_bounds=wavel_bounds,init_points=init_points, n_iter=n_iter)
max_intens_intergral = opt_dict['target']
energy = opt_dict['params']['energy']
pressure = opt_dict['params']['pressure']
radius = opt_dict['params']['radius']
flength = opt_dict['params']['flength']
grating_pair_displacement = opt_dict['params']['grating_pair_displacement']
τfwhm = opt_dict['params']['FWHM']

# Save the data
header = ['init_points', 'n_iter', 'peak power', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas', 'grating_pair_displacement, m']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_300e-9wavelwindow_varyfwhm__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'a', encoding='UTF8', newline='') as f:
#with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_1000e-9wavelwindow__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    # write the header
    #writer.writerow(header)

    # write the dataS
    writer.writerow([init_points, n_iter, max_intens_integral, energy, pressure, radius, flength, τfwhm, wavel, gas, grating_pair_displacement])


#final values for 1200nm (both 50 inits)
#100 iters: {'target': 3.4476846631037324e-11, 'params': {'energy': 0.0014419722696427826, 'flength': 5.245634714473661, 'grating_pair_displacement': 0.00038611804084966866, 'pressure': 6.622451813042336, 'radius': 0.00015892780922243437}}
#150 iters: {'target': 3.447764986674295e-11, 'params': {'energy': 0.0008787363275865865, 'flength': 0.9050858313980417, 'grating_pair_displacement': -0.00044008231048778837, 'pressure': 2.092091101666636, 'radius': 7.004834534514277e-05}}