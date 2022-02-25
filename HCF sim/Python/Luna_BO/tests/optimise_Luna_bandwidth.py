import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
import csv
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
from bossfunction_Luna import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["energy", "pressure", "radius", "flength"]

init_points = 1
n_iter = 0
FWHM = 30e-15
wavel = 800e-9
gas = 'Ne'
GDD = 0

#values:  radius, flength, gas, pressure, wavelength, GDD, energy
initial_values_HCF=[125e-6, 1, gas, 2, wavel, GDD, 0.5e-3]

opt_dict = Luna_BO(params, initial_values_HCF, function=max_bandwidth, init_points=init_points, n_iter=n_iter, FWHM=FWHM)
width = opt_dict['target']
energy = opt_dict['params']['energy']
pressure = opt_dict['params']['pressure']
radius = opt_dict['params']['radius']
flength = opt_dict['params']['flength']

# Save the data
header = ['init_points', 'n_iter', 'width, nm', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna_data\\init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the dataS
    writer.writerow([init_points, n_iter, width, energy, pressure, radius, flength, FWHM, wavel, gas])