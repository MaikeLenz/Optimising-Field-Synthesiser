import sys
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from SPM_plus_GDD_broadening import *

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

t = np.linspace(-50e-15, 50e-15, 1000)
radius = 175e-6
flength = 1.05
pressure = 2
λ0 = 800e-9
τfwhm = 30e-15
energy = 1e-3
gas = 'Ne'
GDD = 400e-30

total_phase_pos, phase_GDD_pos, phase_SPM_pos = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD, t0=0, cep=0, transmission_fraction=1)
total_phase_neg, phase_GDD_neg, phase_SPM_neg = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, -GDD, t0=0, cep=0, transmission_fraction=1)
total_phase_zero, phase_GDD_zero, phase_SPM_zero = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, 0, t0=0, cep=0, transmission_fraction=1)

omega_pos = omega_SPM_plus_GDD(t, total_phase_pos)
omega_neg = omega_SPM_plus_GDD(t, total_phase_neg)
omega_zero = omega_SPM_plus_GDD(t, total_phase_zero)

domega_pos = max(omega_pos) - min(omega_pos)
domega_neg = max(omega_neg) - min(omega_neg)
domega_zero = max(omega_zero) - min(omega_zero)

print('Positive GDD = {}'.format(domega_pos))
print('Negative GDD = {}'.format(domega_neg))
print('Zero GDD = {}'.format(domega_zero))

plt.figure()
plt.plot(t, total_phase_pos, label='Positive GDD')
plt.plot(t, total_phase_neg, label='Negative GDD')
plt.plot(t, total_phase_zero, label='Zero GDD')
plt.legend()

plt.figure()
plt.plot(t, omega_pos, label='Positive GDD')
plt.plot(t, omega_neg, label='Negative GDD')
plt.plot(t, omega_zero, label='Zero GDD')
plt.legend()


GDD_range = np.linspace(-1000e-30, 1000e-30, 10000)
domegas = []
domega_for_zero_GDD = width_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, 0, t0=0, cep=0, transmission_fraction=1)
for i in range(len(GDD_range)):
    domegas.append(width_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD_range[i], t0=0, cep=0, transmission_fraction=1) - domega_for_zero_GDD)
print(domega_for_zero_GDD)
print(domegas[0])

plt.figure()
plt.plot(GDD_range*(10**30), domegas)
plt.xlabel('GDD, fs$\mathrm{^2}$')
plt.ylabel('Change in Width, s$\mathrm{^{-1}}$')
plt.title('Additional Contribution to the Theoretical Width from GDD', fontsize=24)
plt.show()