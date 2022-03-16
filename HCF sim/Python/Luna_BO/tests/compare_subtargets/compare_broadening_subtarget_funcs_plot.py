import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
import csv
import sys
import pandas as pd

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from Luna_subtarget import *
from compressor_grating_to_values import *



filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets"
# Read optimal params
df_0 = pd.read_csv(filepath+"vary_energy_pressure_grating.csv")

target_wavel=df_0.iloc[1,0]
energy_wavel=df_0.iloc[1,1]
pressure_wavel=df_0.iloc[1,2]
grating_pair_displacement_wavel=df_0.iloc[1,3]
target_freq=df_0.iloc[1,4]
energy_freq=df_0.iloc[1,5]
pressure_freq=df_0.iloc[1,6]
grating_pair_displacement_freq=df_0.iloc[1,7]
target_Pt=df_0.iloc[1,8]
energy_Pt=df_0.iloc[1,9]
pressure_Pt=df_0.iloc[1,10]
grating_pair_displacement_Pt=df_0.iloc[1,11]
target_dt=df_0.iloc[1,12]
energy_dt=df_0.iloc[1,13]
pressure_dt=df_0.iloc[1,14]
grating_pair_displacement_dt=df_0.iloc[1,15]
radius=df_0.iloc[1,16]
flength=df_0.iloc[1,17]
duration=df_0.iloc[1,18]
wavel=df_0.iloc[1,19]
gas=df_0.iloc[1,20]


#############################################################################################################################################
#max wavel bandwidth
#path_file='C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\'
#path_file='C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\compare_subtargets\\'

domega=2*np.pi*0.44/duration
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)
GDD,TOD=compressor_grating_values(grating_pair_displacement_mm=1000*grating_pair_displacement_wavel, wavel_m=wavel)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.energy = energy_wavel
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.λ0 = wavel
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure_wavel

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')

λ_wavel = Main.λ
Iλ_wavel = Main.Iλ
t_wavel = Main.t
omega_wavel=Main.ω
Iomega_wavel=Main.Iω
Iomega_wavel=Iomega_wavel.reshape((-1,))[0:500]
omega_wavel=omega_wavel[0:500]

Et_allz_wavel=Main.Et #array of Et at all z 
Et_wavel=Et_allz_wavel[:,-1] #last item in each element is pulse shape at the end
Et0_wavel=Et_allz_wavel[:,0]


##############################################################################################################################

GDD,TOD=compressor_grating_values(grating_pair_displacement_mm=1000*grating_pair_displacement_freq, wavel_m=wavel)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.energy = energy_freq
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.pressure = pressure_freq

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')

λ_freq = Main.λ
Iλ_freq = Main.Iλ
t_freq = Main.t
omega_freq=Main.ω
Iomega_freq=Main.Iω
Iomega_freq=Iomega_freq.reshape((-1,))[0:500]
omega_freq=omega_freq[0:500]

Et_allz_freq=Main.Et #array of Et at all z 
Et_freq=Et_allz_freq[:,-1] #last item in each element is pulse shape at the end
Et0_freq=Et_allz_freq[:,0]

#################################################################################################################################################

GDD,TOD=compressor_grating_values(grating_pair_displacement_mm=1000*grating_pair_displacement_Pt, wavel_m=wavel)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.energy = energy_Pt
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.pressure = pressure_Pt

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')

λ_Pt = Main.λ
Iλ_Pt = Main.Iλ
t_Pt = Main.t
omega_Pt=Main.ω
Iomega_Pt=Main.Iω
Iomega_Pt=Iomega_Pt.reshape((-1,))[0:500]
omega_Pt=omega_Pt[0:500]

Et_allz_Pt=Main.Et #array of Et at all z 
Et_Pt=Et_allz_Pt[:,-1] #last item in each element is pulse shape at the end
Et0_Pt=Et_allz_Pt[:,0]

#########################################################################################################################################################

GDD,TOD=compressor_grating_values(grating_pair_displacement_mm=1000*grating_pair_displacement_dt, wavel_m=wavel)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.energy = energy_dt
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.λ0 = wavel
Main.pressure = pressure_dt

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')

λ_dt = Main.λ
Iλ_dt = Main.Iλ
t_dt = Main.t
omega_dt=Main.ω
Iomega_dt=Main.Iω
Iomega_dt=Iomega_dt.reshape((-1,))[0:500]
omega_dt=omega_dt[0:500]

Et_allz_dt=Main.Et #array of Et at all z 
Et_dt=Et_allz_dt[:,-1] #last item in each element is pulse shape at the end
Et0_dt=Et_allz_dt[:,0]

###################################################################################################################################
#plot
# Save the data
fig=plt.figure()
ax1 = fig.add_subplot(311)
ax1.set_title("Frequency",fontsize=20)
plt.yticks(fontsize=14)

plt.xticks(fontsize=14)
#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax1.plot(omega_wavel,Iomega_wavel,label="Max Wavelength Bandwidth")
ax1.plot(omega_freq,Iomega_freq,label="Max Frequency Bandwidth")
ax1.plot(omega_Pt,Iomega_Pt,label="Max Peak Power")
ax1.plot(omega_dt,Iomega_dt,label="Minimum Duration")

ax1.set_xlabel("Angular Frequency, $\mathrm{s^{-1}}$",fontsize=16)
ax1.set_ylabel("Spectral Energy Density, a.u.",fontsize=16)
plt.legend(fontsize=14,loc="lower right")

ax2 = fig.add_subplot(312)
ax2.set_title("Wavelength",fontsize=20)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax2.plot(10**9*λ_wavel,Iλ_wavel,label="Max Wavelength Bandwidth")
ax2.plot(10**9*λ_freq,Iλ_freq,label="Max Frequency Bandwidth")
ax2.plot(10**9*λ_Pt,Iλ_Pt,label="Max Peak Power")
ax2.plot(10**9*λ_dt,Iλ_dt,label="Minimum Duration")

ax2.set_xlabel("Wavelength, nm",fontsize=16)
ax2.set_ylabel("Spectral Energy Density, a.u.",fontsize=16)
plt.legend(fontsize=14,loc="lower right")

ax3 = fig.add_subplot(313)
ax3.set_title("Wavelength",fontsize=20)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax3.plot(10**15*t_wavel,Et_wavel,label="Max Wavelength Bandwidth")
ax3.plot(10**15*t_freq,Et_freq,label="Max Frequency Bandwidth")
ax3.plot(10**15*t_Pt,Et_Pt,label="Max Peak Power")
ax3.plot(10**15*t_dt,Et_dt,label="Minimum Duration")

ax3.set_xlabel("Time, fs",fontsize=16)
ax3.set_ylabel("Spectral Energy Density, a.u.",fontsize=16)
plt.legend(fontsize=14,loc="lower right")

plt.show()