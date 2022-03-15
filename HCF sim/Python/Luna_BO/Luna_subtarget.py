import julia
#from julia.api import Julia
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

import numpy as np 

from scipy.integrate import simpson

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

def max_bandwidth(t,Et,λ,Iλ):
    return rms_width(λ,Iλ)

def max_peak_power(t,Et,λ,Iλ):
    I=[]
    for i in Et:
        I.append(np.abs(i**2))
    return max(I)

def peak_power_window(t,Et,λ,Iλ):
    """
    defined in the bossfunction
    """
    return True


def max_intens_integral(λ,Iλ,bounds):
    λ_truncated = λ[bounds[0] <λ < bounds[1]]
    Iλ_truncated = Iλ[bounds[0] <λ < bounds[1]]
    return simpson(Iλ,λ)

