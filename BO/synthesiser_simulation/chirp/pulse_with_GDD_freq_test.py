import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

import numpy as np
import matplotlib.pyplot as plt

c = 299792458 # m/s
wavel = 800e-9
domega = 2e15
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)

E, phase = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=np.pi/2, GDD=10, TOD=0, FoOD=5, FiOD=9)
E = np.abs(E)

plt.plot(omega, E)
plt.xlabel('ang freq')
plt.ylabel('electric field amplitude')
plt.show()

plt.plot(omega, phase)
plt.xlabel('ang freq')
plt.ylabel('phase')
plt.show()