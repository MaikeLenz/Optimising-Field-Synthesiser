# -*- coding: utf-8 -*-
from sympy import E
from pulse_with_GDD import *

import numpy as np
import matplotlib.pylab as plt

"""
c = 300 # nm/fs
lam0 = 800 # nm
tau = 4 # fs, for TL pulse

amp = 1
om0 = 2 * np.pi * c/lam0 # centre frequency
print(om0)
dom = 2 * np.pi * 0.441/tau # bandwidth of TL Gaussian pulse with fwhm = tau
t0 = 0
cep = 0

t = np.linspace(-20, 20, 1000)

gdd = 0
#eft = efield_time_domain(t, amp, om0, dom, t0, gdd, cep)
#plt.plot(t, eft, label="GDD=0")
omega,E_omega=efield_freq_domain(t, amp, om0, dom, t0, gdd, cep)
plt.plot(omega, E_omega, label="GDD=0")

gdd = 20
#eft = efield_time_domain(t, amp, om0, dom, t0, gdd, cep)
omega,E_omega=efield_freq_domain(t, amp, om0, dom, t0, gdd, cep)
plt.plot(omega, E_omega, label="GDD="+str(gdd))

#plt.plot(t, eft, label="GDD="+str(gdd))
plt.legend()
plt.show()
"""

t=np.linspace(0,100,10000)
f=10
Et=np.sin(f*t)
spacing=t[1]-t[0]
E_omega=np.fft.fft(Et)
omega=np.fft.fftfreq(len(t),d=(t[1]-t[0]))

plt.figure()
plt.plot(t,Et)
plt.figure()
plt.plot(omega,E_omega)
plt.show()


