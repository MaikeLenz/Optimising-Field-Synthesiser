import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\')

from rms_width import *

#construct gaussian spectral intensity distribution
def gauss(w,A,u,o):
    return A*np.exp(-((w-u)**2)/o**2)

omega=np.linspace(100,200,1000)
I=gauss(omega,1,150,1)

print(rms_width(omega,I))
#for a gaussian, the rms width should be the fwhm divided by sqrt(2)
#for a range of gaussian widths, scatter plot the rms width and see if the gradient matches

fwhms=np.linspace(0.1,10,100)
rms_widths=np.array([])
for i in fwhms:
    I = gauss(omega,1,150,i)
    width=rms_width(omega,I)
    rms_widths=np.append(rms_widths,width)

def func(x,a,b):
    return a*x+b

popt,_=curve_fit(func, fwhms, rms_widths)
plt.scatter(fwhms,rms_widths)
plt.xlabel("FWHM gaussian")
plt.ylabel("rms width")
plt.plot(fwhms, func(fwhms,*popt))
print(popt)
print("expect the gradient ",1/np.sqrt(2))
plt.show()