# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:48:49 2021

@author: iammo
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Post masses in g
mass_L = 522.51
mass_M = 194.66
mass_S = 145.80
g = 9.81

resistance_200k = [42, 30, 55, 70, 170]
resistance_ohms = []
for i in resistance_200k:
    resistance_ohms.append(i*200*1000)

masses = [mass_L+mass_M, mass_L+mass_M+mass_S, mass_L+mass_S, mass_L, mass_M+mass_S]
forces = []
for i in masses:
    forces.append(i*g*(1/1000))

plt.plot(forces, resistance_ohms, 'x')

def exp(x, A, a):
    return A*np.exp(-a*x)

popt, pcov = curve_fit(exp, forces, resistance_ohms, p0=[10, 0.001])

force_range = np.arange(3, 9, 0.1)
plt.plot(force_range, exp(force_range, popt[0], popt[1]))
plt.xlabel('Force (N)')
plt.ylabel('Resistance (Ohms)')
plt.title('Calibration Curve for our Force Transducer')

print(popt)
print(pcov)

# Use curve to calibrate our measurements
# Need to do inverse of exponential
def inverse_exp(y, A, a):
    return -(1/a)*np.log(y/A)

R1 = ((6.83+6.28)/2)*20*1000
R2 = ((5.08+4.39)/2)*20*1000
R3 = ((8.28+9.02)/2)*20*1000
R4 = ((18.31+18.87)/2)*20*1000

print('Calibrated Forces (N):')
print(inverse_exp(R1, popt[0], popt[1]))
print(inverse_exp(R2, popt[0], popt[1]))
print(inverse_exp(R3, popt[0], popt[1]))
print(inverse_exp(R4, popt[0], popt[1]))