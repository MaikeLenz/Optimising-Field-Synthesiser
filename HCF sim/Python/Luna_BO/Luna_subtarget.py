import julia
#from julia.api import Julia
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

import numpy as np 
#from scipy.integrate import simps
from scipy import integrate

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

def max_wavel_bandwidth(t,Et,λ,Iλ):
    return 10**9*rms_width(λ,Iλ)

def max_freq_bandwidth(t,Et,λ,Iλ):
    c = 299792458
    f = c/λ
    return rms_width(f,Iλ)

def max_peak_power(t,Et,λ,Iλ):
    I=[]
    for i in Et:
        I.append(np.abs(i)**2)
    return max(I)
def min_duration_FT(om,Eom):
    """
    Fourier transforms to time domain to minimise duration
    """
    t,Et=f_to_t(om/(2*np.pi),Eom)
    It=np.abs(Et)**2
    return -rms_width(t,It)

def min_thresh_duration_FT(om,Eom):
    """
    Fourier transforms to time domain to minimise duration
    """
    t,Et=f_to_t(om/(2*np.pi),Eom)
    It=np.abs(Et)**2
    return -threshold(t,It,t,It)

def max_peak_power_FT(om,Eom):
    """
    Fourier transforms Eomega to Et and maximised amplitude there
    """
    t,Et=f_to_t(om/(2*np.pi),Eom)
    return max(np.abs(Et)**2)

def peak_power_window(t,Et,λ,Iλ):
    """
    defined in the bossfunction
    """
    return True

def min_duration(t,Et,λ,Iλ):
    """
    return the negative of the time rms width
    """
    I=[]
    for i in Et:
        I.append(np.abs(i)**2)
    return -rms_width(t,I)


def max_intens_integral(λ,Iλ,bounds):
    """
    integrates spectral intensity between wavelength bounds
    """
    λ_truncated1 = λ[bounds[0] <λ]
    λ_truncated=λ_truncated1[λ_truncated1< bounds[1]]
    Iλ_truncated1 = Iλ[bounds[0] <λ]
    Iλ_truncated=Iλ_truncated1[λ_truncated1< bounds[1]]
    return integrate.simps(Iλ_truncated,λ_truncated)

def threshold(t,Et,x,y):
    """
    Find points where signal reaches certain level above noise and find the distance between them
    """
    thresh=0.1
    rows = np.where(y > max(y)*thresh)[0]
    if len(rows) <= 1:
        print("Set a lower threshold")
        min_index = rows[0]
        max_index = min_index
    else:
        min_index = rows[0]
        max_index = rows[-1]
    return x[max_index]-x[min_index]

def norm_and_int(t,Et,x, y):
    """
    Normalises the pulse so that the maximum is 1, and then integrates
    """
    maximum = max(y)
    norm = []
    for i in y:
        norm.append(i/maximum)
    return integrate.simps(norm, x)

def combo(t,Et,λ,Iλ):
    return -min_duration(t,Et,λ,Iλ)+max_freq_bandwidth(t,Et,λ,Iλ)+max_peak_power(t,Et,λ,Iλ)+max_wavel_bandwidth(t,Et,λ,Iλ)+threshold(t,Et,λ,Iλ)

def combo2(t,Et,λ,Iλ):
    return max_freq_bandwidth(t,Et,λ,Iλ)+max_wavel_bandwidth(t,Et,λ,Iλ)+threshold(t,Et,λ,Iλ)

def thresh_and_rms(t,Et,λ,Iλ):
    return max_wavel_bandwidth(t,Et,λ,Iλ)+threshold(t,Et,λ,Iλ)

def max_peak_power_300nm(t,Et,λ,Iλ):
    # First smooth using super Gaussian filter
    def superGauss(x,x0,sigma):
        return np.exp(-((x-x0)/sigma)**4)
    filter = superGauss(λ, 300e-9, 300e-9*0.1)

    Iλ_smooth = []
    for i in range(len(Iλ)):
        Iλ_smooth.append(Iλ[i]*filter[i])

    # Now Fourier transform
    c = 299792458
    f = []
    for i in range(len(λ)):
        f.append(c/λ[i])
    t_filtered, I_filtered = f_to_t(f[::-1], Iλ_smooth[::-1])
    
    # Now find peak power in time-domain
    return max(I_filtered)

def max_peak_power_1300nm(t,Et,λ,Iλ):
    # First smooth using super Gaussian filter
    def superGauss(x,x0,sigma):
        return np.exp(-((x-x0)/sigma)**4)
    filter = superGauss(λ, 1300e-9, 1300e-9*0.2)

    Iλ_smooth = []
    for i in range(len(Iλ)):
        Iλ_smooth.append(Iλ[i]*filter[i])

    # Now Fourier transform
    c = 299792458
    f = []
    for i in range(len(λ)):
        f.append(c/λ[i])
    t_filtered, I_filtered = f_to_t(f[::-1], Iλ_smooth[::-1])
    
    # Now find peak power in time-domain
    return max(I_filtered)