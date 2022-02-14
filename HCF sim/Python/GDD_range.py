"""
Finds the range of GDD values that are to be considered for BO
"""
#imports
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from rms_width import *
c = 299792458 # m/s

#def efield_time_domain(t, amp, om0, dom, t0, gdd, cep):

def GDD_range(max_duration, starting_value=10,t,t0,wavel,domega, CEP):
    GDD=np.abs(starting_value) #need to do this w/positive GDD
    E_real = efield_time_domain(t=t, amp=1, om0=2*np.pi*c/wavel, dom=domega, t0=t0, gdd=GDD, cep=CEP)
    width=rms_width(t,E_real)#width is rms width of E with t
    if width >max_duration:
        while width>max_duration:
            GDD-=1
            E_real = efield_time_domain(t=t, amp=1, om0=2*np.pi*c/wavel, dom=domega, t0=t0, gdd=GDD, cep=CEP)
            width=rms_width(t,E_real)#width is rms width of E with t
        return GDD
    elif width<max_duration:
        while width<max_duration:
            GDD+=1
            E_real = efield_time_domain(t=t, amp=1, om0=2*np.pi*c/wavel, dom=domega, t0=t0, gdd=GDD, cep=CEP)
            width=rms_width(t,E_real)#width is rms width of E with t
        return GDD




