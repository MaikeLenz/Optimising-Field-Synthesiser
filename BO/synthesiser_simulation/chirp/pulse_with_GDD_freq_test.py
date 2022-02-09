import sys
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

import numpy as np
import matplotlib.pyplot as plt

c = 299792458 # m/s
wavel = 800e-9
domega = 2
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)

E = np.abs(E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0))

print(E)

plt.plot(omega, E)
plt.xlabel('ang freq')
plt.ylabel('electric field amplitude')