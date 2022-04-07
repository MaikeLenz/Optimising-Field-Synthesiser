import sys
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

c = 3e8
wavel0 = 5000e-9
om0 = 2*np.pi*c/wavel0
fwhm = 30e-15
domega = 2*np.pi*0.44/fwhm
cep = np.pi/2

t = np.linspace(-100e-15, 100e-15, 1000)
E = efield_time_domain(t, 1, om0, domega, 0, 0, cep)

plt.ylim(-1,1.5)
plt.plot(t*(10**15), E, color='black')
plt.xlabel('Time (fs)')
plt.ylabel('Electric Field (a.u.)')

def Gauss(x, A, x0, sigma):
    return A*np.exp(-((x-x0)**2)/(sigma**2))

plt.plot(t*(10**15), Gauss(t*(10**15), 1, 0, fwhm*(10**15)), color='tab:red')

plt.axvline(x=0, linestyle='--', color='black')

peaks, properties = find_peaks(E)
plt.axvline(x=t[peaks[6]]*(10**15), linestyle='--', color='black')
print(peaks)

plt.show()