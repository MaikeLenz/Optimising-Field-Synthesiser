
import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from Luna_subtarget import *
from compressor_grating_to_values import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

Main.using("Luna")
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"\\new_data\\Ar_peakpower_FT_optimise_lab__init_50_niter_1000.csv")

energy=float(df_0.iloc[0][3])
pressure=float(df_0.iloc[0][4])
radius=float(df_0.iloc[0][5])
flength=float(df_0.iloc[0][6])
FWHM=float(df_0.iloc[0][7])
wavel=float(df_0.iloc[0][8])
gas=df_0.iloc[0][9]
grating_pair_displacement=float(df_0.iloc[0][10])

#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = energy

print(pressure,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
omega = np.linspace(2*np.pi*c/wavel -5* domega/2, 2*np.pi*c/wavel + 5*domega/2, 1000)

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2


Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')


omega=Main.ω
Eomega=Main.Eω

phase=get_phase(omega,Eomega)
#omega=omega[210:340]
#phase=phase[210:340]
#Eomega=Eomega[210:340]

Et = np.fft.ifft(Eomega)
dom = omega[2] - omega[1]
df = dom/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Et), d=df))
########################################################################   
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = 0.66*1.5
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = 1.2e-3

print(pressure,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
om = np.linspace(2*np.pi*c/wavel -5* domega/2, 2*np.pi*c/wavel + 5*domega/2, 1000)

GDD, TOD = 0,0

E, ϕω = E_field_freq(om, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2


Main.ω = om
Main.Iω = Iω  
Main.phase = ϕω 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')


omega2=Main.ω
Eomega2=Main.Eω

phase2=get_phase(omega2,Eomega2)
#omega2=omega2[210:340]
#phase2=phase2[210:340]
#Eomega2=Eomega2[210:340]

Et2 = np.fft.ifft(Eomega2)
dom2 = omega2[2] - omega2[1]
df2 = dom2/(2*np.pi)
t2 = np.fft.fftshift(np.fft.fftfreq(len(Et2), d=df2))
    
############################################################
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.set_xlabel('Angular Frequency')
ax1.set_ylabel('Phase')
ax2.set_ylabel('Intensity')
ax1.plot(omega, phase, '--', label='Phase after')
ax2.plot(omega, np.abs(Eomega)**2, label='Intensity after')
ax1.plot(omega2, phase2, '--', label='SPM, Phase after')
ax2.plot(omega2, np.abs(Eomega2)**2, label='SPM, Intensity after')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.figure()
plt.plot(t,np.abs(Et)**2, label="Optimised")
plt.plot(t2,np.abs(Et2)**2, label="SPM Optimum")

plt.show()
