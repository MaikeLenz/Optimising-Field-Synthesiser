import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from pulse_with_GDD import *
from angfreq_to_time import *

import numpy as np
import matplotlib.pyplot as plt

c = 299792458 # m/s
wavel = 800e-9
domega = 2e15
omega = np.linspace(2*np.pi*c/wavel - 5*domega/2, 2*np.pi*c/wavel + 5*domega/2, 100)

E, phase = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=np.pi/2, GDD=0, TOD=0, FoOD=0, FiOD=0)
I = np.abs(E)**2

fig, [ax1,ax3] = plt.subplots(2)
ax2 = ax1.twinx()
ax1.set_xlabel('Angular Frequency (/s)')
ax2.set_ylabel('Phase')
ax1.set_ylabel('Intensity')

ax1.plot(omega, I, label='Intensity')
ax2.plot(omega, phase, '--', label='Phase')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

t, Et = f_to_t(omega/(2*np.pi), E)
ax3.plot(t, Et)
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Electric Field')
plt.show()