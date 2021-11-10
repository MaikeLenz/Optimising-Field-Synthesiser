# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:50:26 2021

@author: iammo
"""

import numpy as np
import matplotlib.pyplot as plt

def errorCorrection(t, E1, E2):
    diff = []
    if len(E1) != len(E2):
        print('Error- E1 is a different length to E2')
    for i in range(len(E1)):
        diff.append((E1[i] - E2[i])**2)
    h = t[1] - t[0]
    return (0.5*h*((diff[0]+diff[-1]) + 2*np.sum(diff[1:-1])))**0.5

#%%
# Testing errorCorrection
def Gauss(x, A, u, o):
    return A*np.exp(-((x-u)**2)/(2*(o**2)))

t = np.arange(0, 50, 0.1)
E1 = Gauss(t, 1, 25, 5)

# Test function against itself
plt.figure()
plt.plot(t, E1)
print(errorCorrection(t, E1, E1)) # Should be zero

# Test against function shifted in time (delayed)
E2 = Gauss(t+5, 1, 25, 5)
plt.figure()
plt.plot(t, E1)
plt.plot(t, E2)
print(errorCorrection(t, E1, E2))

# Shift more in time- should be a larger error
E2 = Gauss(t+10, 1, 25, 5)
plt.figure()
plt.plot(t, E1)
plt.plot(t, E2)
print(errorCorrection(t, E1, E2))

# Change amplitude and width
E2 = Gauss(t, 5, 25, 5)
plt.figure()
plt.plot(t, E1)
plt.plot(t, E2)
print(errorCorrection(t, E1, E2))
E3 = Gauss(t, 1, 25, 10)
plt.plot(t, E3)
print(errorCorrection(t, E1, E3))