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


def efield_freq_domain(t, amp, om0, dom, t0, gdd, cep):
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
    E=amp * np.log(4)**0.5 * np.exp(-0.25*(t-t0)**2/q**2) * np.exp(1j*om0*(t-t0) + 1j*cep)/(dom*q)
    E_omega=np.fft.ifft(E)
    omega=np.fft.fftfreq(len(t),d=(t[1]-t[0]))
    return omega,np.real(E_omega)

def E_field_freq(omega, t0=0.0, wavel=1000, fwhm=10.0, amp=1.0, CEP=0.0, GDD=0):
    E0 = amp
    E_transform_limited = E0 * np.exp(-2 * np.log(2) * (omega-omega0)**2/domega**2)
    return E_transform_limited * np.exp(phi * 1J) 

c = 3*(10**(8))
omega0 = 2 * np. pi * c/wavel # rad/fs
domega = 2 # for example, rad/fs
omega = np.linspace(omega0-domega/2, omega0+domega/2, 1000)

CEP  = np.pi/2 # for example, rad
GD = 0 # GD relates to absolute arrival times, so not physically important
GDD = 100 # for example, fs**2
TOD = 0 # maybe later, fs**3

def get_phi(omega, omega0, CEP, GDD, TOD):
    return CEP + GD * (omega-omega0) + (1/2) * GDD * (omega-omega0)**2 + (1/6) * TOD * (omega-omega0)**3 
phi = get_phi(omega, omega0, CEP, GDD, TOD)