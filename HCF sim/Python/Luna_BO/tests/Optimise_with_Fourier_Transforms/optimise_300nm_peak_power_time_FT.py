import sys
import csv
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna_debugging import *

params=["energy", "pressure", "grating_pair_displacement", "radius", "flength"]

#values:  radius, flength, gas, pressure, wavelength, energy, τfwhm, grating_pair_separation
gas="He"
# Define experimental params
radius = 500e-6 # HCF core radius
flength = 5 # HCF length
wavel=800e-9
duration=30e-15
energy_init=1.1e-3
pressure_init=0.66*3
grating_init=0
initial_values_HCF=[radius, flength, gas,pressure_init, wavel, energy_init,duration, grating_init]


inits=5
iters=5
result,iterations=Luna_BO_debug(params, initial_values_HCF, function=max_peak_power_300nm_envelope, init_points=inits, n_iter=iters)
target = result['target']
grating=result["params"]["grating_pair_displacement"]
pressure=result["params"]["pressure"]
energy=result["params"]["energy"]
radius=result["params"]["radius"]
flength=result["params"]["flength"]

header = ['init_points', 'n_iter', 'peak power', 'energy, J', 'pressure, bar', 'radius, m', 'flength, m', 'FWHM, s', 'wavel, m', 'gas', 'grating_pair_displacement, m']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\peak_power_1200e-9wavelwindow_varyfwhm__init_' + str(init_points) + '_niter_' + str(n_iter) + '.csv', 'a', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\data\\300nm_env'+gas+'__init_' + str(inits) + '_niter_' + str(iters) + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow([inits, iters, target, energy_init, pressure, radius, flength, duration, wavel, gas, grating])
  
