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

"""
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")
"""
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')

from rms_width import *
from width_methods import *
c = 299792458 # m/s
n=5
#gdd_step=200e-30 #in fs^2
#gdd_mid=0
#GDDs=[gdd_mid-4*gdd_step,gdd_mid-3*gdd_step,gdd_mid-2*gdd_step,gdd_mid-gdd_step,gdd_mid,gdd_mid+gdd_step,gdd_mid+2*gdd_step,gdd_mid+3*gdd_step,gdd_mid+4*gdd_step]
GDDs=np.linspace(-1000e-30,1000e-30,20)


# Define fixed params
c = 299792458 
wavel=800e-9
energy=1e-3
"""
gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure = (0,3)
Main.pressure = pressure
radius=175e-6
Main.radius=radius
flength=1.05
Main.flength=flength
Main.??0 = wavel
Main.energy=energy
"""

def fwhm_to_sigma(fwhm, power=2):
    return fwhm / (2 * (2 * np.log(2))**(1 / power))

def Gauss(x,x0,sigma,power=2):
    return np.exp(-1/2 * ((x-x0)/sigma)**power)

fwhm_duration=30e-15#30fs fwhm duration input pulse
t=np.linspace(-500e-15,500e-15,1000)
t0=0
zero_GDD_shape=Gauss(t,t0,fwhm_to_sigma(fwhm_duration))

Et_in=[]
#Iom_out=[]
#om_out=[]
#Et_out=[]
#t_out=[]
dom=2*np.pi*0.441/fwhm_duration

omega=np.linspace(2*np.pi*c/wavel - 5*dom/2, 2*np.pi*c/wavel + 5*dom/2, 1000)

#Et_in[2][0]=zero_GDD_shape
#print(Et_in)

for i in range(len(GDDs)):
    Et = efield_time_domain(t, 1, 2*np.pi*c/wavel, dom, t0, GDDs[i], 0)
    E, ???? = E_field_freq(omega, GD=0.0, wavel=wavel, domega=dom, amp=1, CEP=0, GDD=GDDs[i], TOD=0)
    Et_in.append(np.abs(Et))
    #I?? = np.abs(E**2)
    #Main.?? = omega
    #Main.I?? = I??  
    #Main.phase = ????

    #Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    #Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
    
    #now extract datasets
    #Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
    #Main.eval('t, Et = Processing.getEt(duv)')

    #?? = Main.??
    #I?? = Main.I??
    #I??=I??.reshape((-1,))[0:500]
    #??=??[0:500]
    #Iom_out.append(I??)
    #om_out.append(??)

    #t_i=Main.t
    #Et_i=Main.Et
    #Et_i=Et_i[:,-1]
    #Et_out.append(Et_i)
    #t_out.append(t_i)
   
thresh_widths=[]
rms_widths=[]
superG_widths=[]
#SPM_widths=[]
GDD_widths=[]
normint_widths=[]
from scipy.optimize import curve_fit
for i in range(len(Et_in)):
    rms_widths.append(rms_width(t,Et_in[i]))
    thresh_widths.append(threshold(t,Et_in[i]))
    popt, pcov = curve_fit(superGauss, t, Et_in[i], p0=[1, 0, 50e-15])
    superG_widths.append(popt[2])
    normint_widths.append(norm_and_int(t,Et_in[i]))
    #SPM_widths.append(theoretical_width(radius, flength, pressure, wavel, fwhm_duration, energy))
    GDD_widths.append(GDD_duration(GDDs[i],fwhm_duration))
GDDs=np.array(GDDs)
rms_widths=np.array(rms_widths)
thresh_widths=np.array(thresh_widths)
superG_widths=np.array(superG_widths)
#SPM_widths=np.array(SPM_widths)
GDD_widths=np.array(GDD_widths)
normint_widths=np.array(normint_widths)

fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()
ax1.plot(GDDs*10**30,GDD_widths*10**15,label="Theoretical GDD Broadening",color="tab:blue")
ax1.plot(GDDs*10**30,rms_widths*0.8*10**15,label="RMS Width times 0.8",color="tab:orange")
ax1.plot(GDDs*10**30,thresh_widths*0.4*10**15,label="Threshold Width times 0.4",color="tab:green")
ax1.plot(GDDs*10**30,superG_widths*10**(15)*0.7,label="Super Gaussian Width times 0.7",color="tab:red")
ax1.plot(GDDs*10**30,normint_widths*10**(15),label="Normalised Integral",color="tab:purple")


ax1.set_xlabel("GDD, fs$\mathrm{^2}$",fontsize=14)
ax1.set_ylabel("Widths, fs",fontsize=14)
#ax2.set_ylabel("Theoretical GDD Broadening/ Threshold Width, s",fontsize=14)
plt.legend(fontsize=16,loc="upper right")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Width Comparison", fontsize=20)
plt.show()
"""
plt.plot(GDDs*10**30,rms_widths,label="RMS Width")
plt.plot(GDDs*10**30, GDD_widths,label="Theoretical GDD Broadening")
#plt.plot(GDDs*10**30,SPM_widths,label="Theoretical SPM Broadening")
plt.xlabel("GDD, fs$\mathrm{^2}$",fontsize=14)
plt.ylabel("Width",fontsize=14)
plt.legend(fontsize=16)
plt.title("Width Comparison", fontsize=20)
plt.show()
"""



