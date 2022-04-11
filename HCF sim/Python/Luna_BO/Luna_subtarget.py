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

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
from get_phase import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\")
from envelopes import *

from scipy.optimize import curve_fit

import numpy as np 
#from scipy.integrate import simps
from scipy import integrate

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

def max_wavel_bandwidth(λ,Iλ):
    return 10**9*rms_width(λ,Iλ)

def max_freq_bandwidth(λ,Iλ):
    c = 299792458
    f = c/λ
    return rms_width(f,Iλ)

def min_duration_FT(om,Eom):
    """
    Fourier transforms to time domain to minimise duration
    """
    Et = np.fft.ifft(Eom)
    dom = om[2] - om[1]
    df = dom/(2*np.pi)
    t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))
    return -rms_width(t,np.abs(Et)**2)

def min_thresh_duration_FT(om,Eom):
    """
    Fourier transforms to time domain to minimise duration
    """
    Et = np.fft.ifft(Eom)
    dom = om[2] - om[1]
    df = dom/(2*np.pi)
    t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))
    return -threshold(t,np.abs(Et)**2)

def max_peak_power_FT(om,Eom):
    """
    Fourier transforms Eomega to Et and maximised amplitude there
    """
    Et = np.fft.ifft(Eom)
    dom = om[2] - om[1]
    df = dom/(2*np.pi)
    t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))

    popt,_=curve_fit(gauss_envelope,t,np.abs(Et)**2, p0=[max(np.abs(Et)**2),2e-14,t[np.argmax(np.abs(Et)**2)]])
    #plt.plot(t,np.abs(Et)**2)
    #plt.plot(t,gauss_envelope(t,*popt))
    #plt.show()
    return popt[0]

def peak_power_window(λ,Iλ):
    """
    defined in the bossfunction
    """
    return True

def max_intens_integral(λ,Iλ,bounds):
    """
    integrates spectral intensity between wavelength bounds
    """
    λ_truncated1 = λ[bounds[0] <λ]
    λ_truncated=λ_truncated1[λ_truncated1< bounds[1]]
    Iλ_truncated1 = Iλ[bounds[0] <λ]
    Iλ_truncated=Iλ_truncated1[λ_truncated1< bounds[1]]
    return integrate.simps(Iλ_truncated,λ_truncated)

def threshold(x,y,x2=None,y2=None):
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

def norm_and_int(x, y):
    """
    Normalises the pulse so that the maximum is 1, and then integrates
    """
    maximum = max(y)
    norm = []
    for i in y:
        norm.append(i/maximum)
    return integrate.simps(norm, x)

def max_peak_power_300nm(om,Eom):
    # First smooth using super Gaussian filter
    c=299792458
    λ=(2*np.pi*c)/om
    filter = superGauss(λ, 300e-9, 300e-9*0.1)
    plt.plot(om,np.abs(Eom)**2)
    Eom_smooth = []
    for i in range(len(Eom)):
        Eom_smooth.append(Eom[i]*filter[i])
    plt.plot(om, np.abs(Eom_smooth)**2)
    plt.show()
    # Now Fourier transform
    """
    f = []
    for i in range(len(λ)):
        f.append(c/λ[i])
    t_filtered, I_filtered = f_to_t(f[::-1], Iλ_smooth[::-1])
    """
    Et = np.fft.ifft(Eom_smooth)
    return max(np.abs(Et)**2)

def max_peak_power_300nm_envelope(om,Eom):
    # First smooth using super Gaussian filter
    c=299792458
    λ=(2*np.pi*c)/om
    filter = superGauss(λ, 300e-9, 300e-9*0.1)
    plt.plot(om,np.abs(Eom)**2)
    Eom_smooth = []
    for i in range(len(Eom)):
        Eom_smooth.append(Eom[i]*filter[i])
    plt.plot(om, np.abs(Eom_smooth)**2)
    plt.show()
    # Now Fourier transform
    """
    f = []
    for i in range(len(λ)):
        f.append(c/λ[i])
    t_filtered, I_filtered = f_to_t(f[::-1], Iλ_smooth[::-1])
    """
    Et = np.fft.ifft(Eom_smooth)
    dom = om[2] - om[1]
    df = dom/(2*np.pi)
    t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))
    popt,_=curve_fit(gauss_envelope,t,np.abs(Et)**2, p0=[max(np.abs(Et)**2),2e-14,t[np.argmax(np.abs(Et)**2)]])

    return popt[0]

def max_peak_power_1300nm(λ,Iλ):
    # First smooth using super Gaussian filter
    
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