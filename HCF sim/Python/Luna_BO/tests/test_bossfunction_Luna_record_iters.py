import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
import csv
import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna_record_iters import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

# Optimise our lab

params=["energy", "pressure", "grating_pair_displacement"]

#values:  radius, flength, gas, pressure, wavelength, energy, τfwhm, grating_pair_separation
#gas="Ne"
gas = "Ar"
#initial_values_HCF=[175e-6, 1.05, gas, 3, 800e-9, 1e-3, 30e-15, 0]
initial_values_HCF=[175e-6, 1.05, gas, 1, 800e-9, 1e-3, 30e-15, 0]

result,iterations=Luna_BO_record_iters(params, initial_values_HCF, function=max_freq_bandwidth, ImperialLab=True, init_points=50, n_iter=1000, save_path='C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\', plotting=True)

"""
# Optimise wavelength bands

params = ["energy", "pressure", "radius", "flength", "grating_pair_displacement"]
wavel_bounds = (300e-9 - (300e-9)*0.1, 300e-9 + (300e-9)*0.1)
#wavel_bounds = (1300e-9 - (1300e-9)*0.2, 1300e-9 + (1300e-9)*0.2)

#values:  radius, flength, gas, pressure, wavelength, energy, τfwhm, grating_pair_separation
gas = "He"
initial_values_HCF=[175e-6, 1, gas, 1.8*0.66, 800e-9, 0.075e-3, 40e-15, 0]

result,iterations=Luna_BO_record_iters(params, initial_values_HCF, function=max_intens_integral, wavel_bounds=wavel_bounds, init_points=50, n_iter=50, save_path='C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\He_40fs_300nm_1mJmax\\', plotting=True)
"""