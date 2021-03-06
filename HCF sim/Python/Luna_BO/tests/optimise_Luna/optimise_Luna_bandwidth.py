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
from bossfunction_Luna import *
from bossfunction_Luna_debugging import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["grating_pair_displacement","energy","pressure"]

init_points = 50
n_iter = 1000
FWHM = (22e-15)*1.25
wavel = 790e-9
gas = 'Ar'


radius_init = 175e-6
flength_init = 1.05
pressure_init = 0.66
energy_init = 1.1e-3
#radius_init = randint(50, 500)*(10**-6)
#flength_init = randint(1, 30)*0.1
#pressure_init = randint(1, 10)
#energy_init= randint(1, 10)*(10**-4)

#values: radius,flength,gas_str,pressure,λ0,energy,FWHM,grating_pair_displacemen

initial_values_HCF=[radius_init, flength_init, gas, pressure_init, wavel, energy_init,FWHM,0]

opt_dict, res = Luna_BO_debug(params, initial_values_HCF, function=max_freq_bandwidth, init_points=init_points, n_iter=n_iter, ImperialLab=True)
width = opt_dict['target']
energy = opt_dict['params']['energy']
pressure = opt_dict['params']['pressure']
grating = opt_dict['params']['grating_pair_displacement']

# Save the data
header = ['init_points', 'n_iter', 'width, nm', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas', 'grating pair displacement, m']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna_data\\optimise_lab__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\exp_input_Ar_freq_bandwidth_optimise_lab__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the dataS
    writer.writerow([init_points, n_iter, width, energy, pressure, radius_init, flength_init, FWHM, wavel, gas,grating])

#{'target': 2223933819847598.2, 'params': {'energy': 0.0011730020668117554, 'grating_pair_displacement': 1.3687440750850062e-05, 'pressure': 0.9896159222064448}}