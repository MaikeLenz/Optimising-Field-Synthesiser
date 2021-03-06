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
from width_methods import *

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

c = 299792458 # m/s
n=5
gdd_step=50e-30 #in fs^2
gdd_mid=0

GDDs=np.array([-200e-30,-200e-30,0,200e-30,200e-30])
print(GDDs)
# Define fixed params
c = 299792458 
wavel=800e-9
energy=1.5e-3

gas = "Ar"
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

def fwhm_to_sigma(fwhm, power=2):
    return fwhm / (2 * (2 * np.log(2))**(1 / power))

def Gauss(x,x0,sigma,power=2):
    return np.exp(-1/2 * ((x-x0)/sigma)**power)

fwhm_duration=30e-15#30fs fwhm duration input pulse
t=np.linspace(-150e-15,150e-15,1000)
t0=0
zero_GDD_shape=Gauss(t,t0,fwhm_to_sigma(fwhm_duration))

Et_in=[]
Iom_out=[]
om_out=[]
Et_out=[]
t_out=[]
dom=2*np.pi*0.441/fwhm_duration

omega=np.linspace(2*np.pi*c/wavel -5* dom/2, 2*np.pi*c/wavel + 5*dom/2, 1000)

#Et_in[2][0]=zero_GDD_shape
#print(Et_in)

for i in range(len(GDDs)):
    Et = efield_time_domain(t, 1, 2*np.pi*c/wavel, dom, t0, GDDs[i], 0)
    E, ???? = E_field_freq(omega, GD=0.0, wavel=wavel, domega=dom, amp=1, CEP=0, GDD=GDDs[i], TOD=0)
    Et_in.append(Et.real)
    I?? = np.abs(E**2)
    Main.?? = omega
    Main.I?? = I??  
    Main.phase = ????

    Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
    
    #now extract datasets
    Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ?? = Main.??
    I?? = Main.I??
    I??=I??.reshape((-1,))
    ??=??
    Iom_out.append(I??)
    om_out.append(??)

    t_i=Main.t
    Et_i=Main.Et
    Et_i=Et_i[:,-1]
    Et_out.append(Et_i)
    t_out.append(t_i)
   
f = plt.figure(constrained_layout=True)

ax1 = plt.subplot2grid((3,5), (0, 0))
ax2 = plt.subplot2grid((3,5), (0, 1))
ax3 = plt.subplot2grid((3,5), (0, 2))
ax4 = plt.subplot2grid((3,5), (0, 3))
ax5 = plt.subplot2grid((3,5), (0, 4))
ax6 = plt.subplot2grid((3,5), (1, 0))
ax7 = plt.subplot2grid((3,5), (1, 1))
ax8 = plt.subplot2grid((3,5), (1, 2))
ax9 = plt.subplot2grid((3,5), (1, 3))
ax10 = plt.subplot2grid((3,5), (1, 4))
ax11 = plt.subplot2grid((3,5), (2, 0))
ax12 = plt.subplot2grid((3,5), (2, 1))
ax13 = plt.subplot2grid((3,5), (2, 2))
ax14 = plt.subplot2grid((3,5), (2, 3))
ax15 = plt.subplot2grid((3,5), (2, 4))

left  = 0.1  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9     # the top of the subplots of the figure
wspace = 0.4   # the amount of width reserved for blank space between subplots
hspace = 0.47   # the amount of height reserved for white space between subplots

plt.subplots_adjust(left, bottom, right, top, wspace, hspace)


axes=[ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12,ax13,ax14,ax15]
for i in range(len(axes)):
    if i<5:
        if i==2:
            axes[i].set_title("Input Temporal Electric Field",fontsize=16)
        axes[i].plot(t*10**15,Et_in[i], label="GDD="+str(int(GDDs[i]*10**30))+"fs$\mathrm{^2}$")
        axes[i].set_yticks([-1,-0.5,0,0.5,1])
        axes[i].set_ylabel("E, a.u.",fontsize=12)
        axes[i].set_xlabel("t, fs",fontsize=12)
        axes[i].legend(fontsize=12,loc="lower right")
       
    elif i <10:
        if i==7:
            axes[i].set_title("Output Temporal Electric Field",fontsize=16)
        axes[i].plot(t_out[i-5]*10**15,Et_out[i-5]/50000)
        axes[i].set_ylabel("E, a.u.",fontsize=12)
        axes[i].set_xlabel("t, fs",fontsize=12)
    else:
        if i==12:
            axes[i].set_title("Output Spectral Energy Density",fontsize=16)
        axes[i].plot(om_out[i-10]*10**-15,Iom_out[i-10]*10**18)
        #axes[i].set_xlim(2.1,2.6)
        axes[i].set_ylabel("I, a.u.",fontsize=12)
        axes[i].set_xlabel("$\mathrm{\omega}$, 10$\mathrm{^{15}}$s$\mathrm{^{-1}}$",fontsize=12)
#ax3.plot(t,zero_GDD_shape)

thresh_widths=[]
rms_widths=[]
#superG_widths=[]
normint_widths=[]
SPM_widths=[]

from scipy.optimize import curve_fit
for i in range(len(Et_out)):
    rms_widths.append(rms_width(om_out[i],Iom_out[i]))
    thresh_widths.append(threshold(om_out[i],Iom_out[i]))
    #popt, pcov = curve_fit(superGauss, om_out[i], Iom_out[i], p0=[6, 2*np.pi*c/800e-9, 2e14])
    #superG_widths.append(popt[2])
    normint_widths.append(norm_and_int(om_out[i],Iom_out[i]))
    GDD_width=GDD_duration(GDDs[i],fwhm_duration)
    transmission_fraction=0.6
    SPM_widths.append(theoretical_width(radius, flength, 0.66*pressure[1], wavel, GDD_width, energy, gas, transmission_fraction)/(4*np.sqrt(np.log(2))))

GDDs=np.array(GDDs)
rms_widths=np.array(rms_widths)
thresh_widths=np.array(thresh_widths)
#superG_widths=np.array(superG_widths)
SPM_widths=np.array(SPM_widths)
normint_widths=np.array(normint_widths)

scaling_rms=max(SPM_widths)/max(rms_widths)
scaling_thresh=max(SPM_widths)/max(thresh_widths)
#scaling_superG=max(SPM_widths)/max(superG_widths)
scaling_normint=max(SPM_widths)/max(normint_widths)

fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()
"""
ax1.plot(GDDs*10**30,SPM_widths,label="Theoretical SPM Broadening")
ax1.plot(GDDs*10**30,rms_widths*scaling_rms,label="RMS Width times %s"%(round(scaling_rms,2)))
ax1.plot(GDDs*10**30,thresh_widths*scaling_thresh,label="Threshold Width times %s"%(round(scaling_thresh,2)))
ax1.plot(GDDs*10**30,superG_widths*scaling_superG,label="Super Gaussian Width times %s"%(round(scaling_superG,2)))
ax1.plot(GDDs*10**30,normint_widths*scaling_normint,label="Normalised Integral times %s"%(round(scaling_normint,2)))
"""
ax1.plot(GDDs*10**30,SPM_widths,label="Theoretical SPM Broadening")
ax1.plot(GDDs*10**30,rms_widths,label="RMS Width")
ax1.plot(GDDs*10**30,thresh_widths,label="Threshold Width")
#ax1.plot(GDDs*10**30,superG_widths,label="Super Gaussian Width times %s"%(round(scaling_superG,2)))
ax1.plot(GDDs*10**30,normint_widths,label="Normalised Integral")

ax1.set_xlabel("GDD, fs$\mathrm{^2}$",fontsize=14)
ax1.set_ylabel("Widths, s$\mathrm{^{-1}}$",fontsize=14)
#ax2.set_ylabel("Theoretical GDD Broadening/ Threshold Width, s",fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=16,loc="upper right")
plt.title("Frequency Width Comparison Output Pulse", fontsize=20)
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





