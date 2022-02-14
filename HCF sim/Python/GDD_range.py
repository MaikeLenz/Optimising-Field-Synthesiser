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

def GDD_range(max_duration, starting_value=10,wavel,domega,omega, CEP, TOD):
    GDD=np.abs(starting_value)
    E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=CEP, GDD=GDD, TOD=TOD)
    E_abs=np.abs(E)
    width=rms_width(omega,E_abs)
    if width >max_duration:
        while width>max_duration:
            GDD-=1
            E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
            E_abs=np.abs(E)
            width=rms_width(omega,E_abs)
        return GDD
    elif width<max_duration:
        while width<max_duration:
            GDD+=1
            E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
            E_abs=np.abs(E)
            width=rms_width(omega,E_abs)





