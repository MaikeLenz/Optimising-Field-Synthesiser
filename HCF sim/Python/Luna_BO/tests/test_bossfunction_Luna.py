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
from bossfunction_Luna import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

params=["energy", "pressure", "grating_pair_displacement"]

#values:  radius, flength, gas, pressure, wavelength, energy, τfwhm, grating_pair_separation
gas="Ne"
initial_values_HCF=[175e-6, 1.05, gas, 2, 800e-9, 0.5e-3, 30e-15, 0]

result,iterations=Luna_BO(params, initial_values_HCF, function=max_bandwidth, ImperialLab=True, init_points=100, n_iter=100, wavel_bounds=(1300e-9, 1500e-9))

#for i, res in enumerate(iterations):
#    print("Iteration {}: \n\t{}".format(i, res))


header = ['Iteration', "target width, \m", "energy, J","pressure, bar","grating pair displacement, m"]
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\Optimise_Lab\\'+gas+"_Exp_Input.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i, res in enumerate(iterations):
        writer.writerow([i,res["target"],res["params"]["energy"],res["params"]["pressure"],res["params"]["grating_pair_displacement"]])
        
