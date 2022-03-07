import julia
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv  
import sys

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
#from theoretical_width import theoretical_width

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from theoretical_width import *
from theoretical_GDD_duration import *


julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')

from rms_width import *
c = 299792458 # m/s
n=5
gdd_step=200e-30 #in fs^2
gdd_mid=0
GDDs=[gdd_mid-4*gdd_step,gdd_mid-3*gdd_step,gdd_mid-2*gdd_step,gdd_mid-gdd_step,gdd_mid,gdd_mid+gdd_step,gdd_mid+2*gdd_step,gdd_mid+3*gdd_step,gdd_mid+4*gdd_step]

# Define fixed params
c = 299792458 
wavel=800e-9
energy=0.5e-3

gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure = (0,3)
Main.pressure = pressure
radius=175e-6
Main.radius=radius
flength=1.05
Main.flength=flength
Main.λ0 = wavel
Main.energy=energy

def fwhm_to_sigma(fwhm, power=2):
    return fwhm / (2 * (2 * np.log(2))**(1 / power))

def Gauss(x,x0,sigma,power=2):
    return np.exp(-1/2 * ((x-x0)/sigma)**power)

fwhm_duration=30e-15#30fs fwhm duration input pulse
t=np.linspace(-100e-15,100e-15,1000)
t0=0
zero_GDD_shape=Gauss(t,t0,fwhm_to_sigma(fwhm_duration))

Et_in=[]
Iom_out=[]
om_out=[]
Et_out=[]
t_out=[]
dom=2*np.pi*0.441/fwhm_duration

omega=np.linspace(2*np.pi*c/wavel - dom/2, 2*np.pi*c/wavel + dom/2, 1000)

#Et_in[2][0]=zero_GDD_shape
#print(Et_in)

for i in range(len(GDDs)):
    Et = efield_time_domain(t, 1, 2*np.pi*c/wavel, dom, t0, GDDs[i], 0)
    E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=dom, amp=1, CEP=0, GDD=GDDs[i], TOD=0)
    Et_in.append(np.abs(Et))
    Iω = np.abs(E**2)
    Main.ω = omega
    Main.Iω = Iω  
    Main.phase = ϕω

    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    
    #now extract datasets
    Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ω = Main.ω
    Iω = Main.Iω
    Iω=Iω.reshape((-1,))[0:500]
    ω=ω[0:500]
    Iom_out.append(Iω)
    om_out.append(ω)

    t_i=Main.t
    Et_i=Main.Et
    Et_i=Et_i[:,-1]
    Et_out.append(Et_i)
    t_out.append(t_i)
   

rms_widths=[]
SPM_widths=[]
GDD_width=[]
for i in range(len(Et_out)):
    rms_widths.append(rms_width(Et_out))
    SPM_widths.append(theoretical_width(radius, flength, pressure, wavel, fwhm_duration, energy))
    GDD_width.append(GDD_duration(GDDs[i],fwhm_duration))

plt.plot(GDDs*10**30,rms_widths,label="RMS Width")
plt.plot(GDDs*10**30, GDD_width,label="Theoretical GDD Broadening")
plt.plot(GDDs*10**30,SPM_widths,label="Theoretical SPM Broadening")
plt.xlabel("GDD, fs$\mathrm{^2}$",fontsize=14)
plt.ylabel("Width",fontsize=14)
plt.legend(fontsize=16)
plt.title("Width Comparison", fontsize=20)
plt.show()



