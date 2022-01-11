# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:48:49 2021

@author: iammo
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Post masses in g
masses=np.array([148,78,55,484,1300,270,430,140,45,50,1295,1740,2120])
g = 9.81

#resistances in Kohms
resistance_1 = np.array([2,3.5,4.5,0.8,0.4,1,1.2,2,11,6,0.6,0.4,0.35])

forces = np.array([])
for i in masses:
    forces=np.append(forces,i*g*(1/1000))

plt.plot(forces, 1000*resistance_1, 'x')


def exp(x, A):
    return A/x

popt, pcov = curve_fit(exp, forces, 1000*resistance_1, p0=[2000])

force_range = np.arange(0.2, 22, 0.1)
plt.plot(force_range, exp(force_range, popt[0]), label="R=%s/F" %(int(round(popt[0],0))))
#plt.plot(force_range, exp(force_range, 2000))

plt.xlabel('Force (N)')
plt.ylabel('Resistance (Ohms)')
plt.title('Calibration Curve for our Force Transducer')
plt.legend()
plt.grid()
print(popt)
print(pcov)

# Use curve to calibrate our measurements
# Need to do inverse of exponential

def inverse_exp(y, A, a):
    return -(1/a)*np.log(y/A)

R1 = ((6.83+6.28)/2)*1000
R2 = ((5.08+4.39)/2)*1000
R3 = ((8.28+9.02)/2)*1000
R4 = ((18.31+18.87)/2)*1000

print('Calibrated Forces (N):')
print(R1,exp(R1, popt[0]))
print(R2,exp(R2, popt[0]))
print(R3,exp(R3, popt[0]))
print(R4,exp(R4, popt[0]))


plt.show()