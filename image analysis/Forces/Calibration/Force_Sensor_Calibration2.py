# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:48:49 2021

@author: iammo
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Post masses in g
masses=np.array([144.65,110.29,95.05,23.71,66.59,89.16])
g = 9.81

#resistances in Kohms
resistance_1 = np.array([5.3,13.4,6.0,14.2,7.7,10.9])
resistance_2 = np.array([4.5,16.6,5.5,19.9,7.5,6.8])
resistance_3 = np.array([4.4,9.0,5.9,12.6,7.6,9.7])
mean_resistance =np.array([])
for i in range(len(resistance_1)):
    mean_resistance=np.append(mean_resistance,(resistance_1[i]+resistance_2[i]+resistance_3[i])/3)
forces = np.array([])
for i in masses:
    forces=np.append(forces,i*g*(1/1000))

plt.plot(forces, 1000*mean_resistance, 'x')

"""
def exp(x, A, a):
    return A*np.exp(-a*x)

popt, pcov = curve_fit(exp, forces, resistance_ohms, p0=[10, 0.001])

force_range = np.arange(3, 9, 0.1)
plt.plot(force_range, exp(force_range, popt[0], popt[1]))
"""
plt.xlabel('Force (N)')
plt.ylabel('Resistance (Ohms)')
plt.title('Calibration Curve for our Force Transducer')

#print(popt)
#print(pcov)

# Use curve to calibrate our measurements
# Need to do inverse of exponential
"""
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
"""

plt.show()