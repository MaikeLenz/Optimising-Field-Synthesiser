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

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')

from rms_width import *
c = 299792458 # m/s
n=5
gdd_step=50e-30 #in fs^2
gdd_mid=-200e-30
GDDs=[gdd_mid-2*gdd_step,gdd_mid-gdd_step,gdd_mid,gdd_mid+gdd_step,gdd_mid+2*gdd_step]
#GDDs=np.array([-200e-30,-100e-30,0,100e-30,200e-30])
print(GDDs)
# Define fixed params
c = 299792458 
wavel=800e-9
energy=1e-3

gas = "Ar"
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
t=np.linspace(-150e-15,150e-15,1000)
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
    Et_in.append(Et.real)
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
        axes[i].set_xlim(2.1,2.6)
        axes[i].set_ylabel("I, a.u.",fontsize=12)
        axes[i].set_xlabel("$\mathrm{\omega}$, 10$\mathrm{^{15}}$s$\mathrm{^{-1}}$",fontsize=12)
#ax3.plot(t,zero_GDD_shape)

plt.show()




