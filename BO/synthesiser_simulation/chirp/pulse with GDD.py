# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:55:57 2019

@author: jt
"""

import numpy as np
import matplotlib.pylab as plt

def efield_time_domain(t, amp, om0, dom, t0, gdd, cep):
    """ returns time domain e_efield (real)
    t is time axis
    amp is pulse amplitude
    om0 is centre frequency
    dom is bandwidth
    t0 is time offset
    gdd is group delay dispersion (in units of time^2)
    cep is carrier envelop phase
    """
    
    q = ( np.log(4)/dom **2 + 0.5 * 1j * gdd )**0.5
    return np.real(amp * np.log(4)**0.5 * np.exp(-0.25*(t-t0)**2/q**2) * np.exp(1j*om0*(t-t0) + 1j*cep)/(dom*q))

c = 300 # nm/fs
lam0 = 800 # nm
tau = 4 # fs, for TL pulse

amp = 1
om0 = 2 * np.pi * c/lam0 # centre frequency
dom = 2 * np.pi * 0.441/tau # bandwidth of TL Gaussian pulse with fwhm = tau
t0 = 0
cep = 0

t = np.linspace(-20, 20, 1000)

gdd = 0
eft = efield_time_domain(t, amp, om0, dom, t0, gdd, cep)
plt.plot(t, eft, label="GDD=0")



gdd = 20
eft = efield_time_domain(t, amp, om0, dom, t0, gdd, cep)
plt.plot(t, eft, label="GDD="+str(gdd))
plt.legend()
plt.show()


