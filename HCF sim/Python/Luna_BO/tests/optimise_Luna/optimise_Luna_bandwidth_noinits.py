import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
import csv
from numpy.random import *
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna_debugging import *

#################################################################################################################
#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["energy", "pressure", "grating_pair_displacement"]

init_points = 0
n_iter = 50
func=threshold
wavel = 800e-9
gas = 'Ar'

FWHM_init = 22e-15
radius_init = 175e-6
flength_init = 1.05
pressure_init = 3*0.66
energy_init = 0.5e-3
#radius_init = randint(50, 500)*(10**-6)
#flength_init = randint(1, 30)*0.1
#pressure_init = randint(1, 10)
#energy_init= randint(1, 10)*(10**-4)

# This part is optional - run first with just initial points for comparison
#values:  radius, flength, gas, pressure, wavelength, GDD, energy
initial_values_HCF=[radius_init, flength_init, gas, pressure_init, wavel, energy_init,FWHM_init, 0]

# Run optimisation
opt_dict,res = Luna_BO_debug(params, initial_values_HCF, function=func,init_points=init_points, n_iter=n_iter)
max_width_sum = opt_dict['target']
energy = opt_dict['params']['energy']
pressure = opt_dict['params']['pressure']
grating_pair_displacement = opt_dict['params']['grating_pair_displacement']
#τfwhm = opt_dict['params']['FWHM']

# Save the data
header = ['init_points', 'n_iter', 'peak power', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas', 'grating_pair_displacement, m']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_1200e-9wavelwindow_varyfwhm__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'a', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\'+"width"+'__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    # write the header
    #writer.writerow(header)

    # write the dataS
    writer.writerow([init_points, n_iter, max_width_sum, energy, pressure, radius_init, flength_init, FWHM_init, wavel, gas, grating_pair_displacement])


#final values for 1200nm (both 50 inits)
#100 iters: {'target': 3.4476846631037324e-11, 'params': {'energy': 0.0014419722696427826, 'flength': 5.245634714473661, 'grating_pair_displacement': 0.00038611804084966866, 'pressure': 6.622451813042336, 'radius': 0.00015892780922243437}}
#150 iters: {'target': 3.447764986674295e-11, 'params': {'energy': 0.0008787363275865865, 'flength': 0.9050858313980417, 'grating_pair_displacement': -0.00044008231048778837, 'pressure': 2.092091101666636, 'radius': 7.004834534514277e-05}}

#cool spectrum:
#{'target': 1.5112993991075554e-12, 'params': {'energy': 0.0010386545142497632, 'flength': 2.5620983339660492, 'grating_pair_displacement': 5.8689828445751676e-05, 'pressure': 0.9211608157857013, 'radius': 0.00013914567008819546}}