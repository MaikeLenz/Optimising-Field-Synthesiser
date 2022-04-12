import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import sys
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
from get_phase import *
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

Main.using("Luna")
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\data\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\data\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"300nm_He__init_50_niter_250.csv")

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

omega1 = Main.ω
Eomega1 = Main.Eω

phase1=get_phase(omega1,Eomega1,wavel)

#######################################################################################################################
# Read optimal params
df_0 = pd.read_csv(filepath+"300nm_envHe__init_50_niter_250.csv")

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

omega2 = Main.ω
Eomega2 = Main.Eω

phase2=get_phase(omega2,Eomega2,wavel)


#######################################################################################################################
# Read optimal params
df_0 = pd.read_csv(filepath+"300nm_env_100quadraticphaseHe__init_50_niter_250.csv")

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

omega3 = Main.ω
Eomega3 = Main.Eω

phase3=get_phase(omega3,Eomega3,wavel)



######################################################################################
#plot

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.set_xlabel('Angular Frequency', fontsize=14)
ax1.set_ylabel('Phase', fontsize=14)
ax2.set_ylabel('Intensity', fontsize=14)
i1=0
i2=4000
ax1.plot(omega1[i1:i2], phase1[i1:i2], '--', label='No envelope, Phase after')
ax2.plot(omega1[i1:i2], np.abs(Eomega1[i1:i2])**2, label='No envelope')
#ax1.plot(omega2[i1:i2], phase2[i1:i2], '--', label='Envelope, Phase after')
#ax2.plot(omega2[i1:i2], np.abs(Eomega2[i1:i2])**2, label='Envelope')
ax1.plot(omega3[i1:i2], phase3[i1:i2], '--', label='Envelope, Phase after',c="tab:green")
ax2.plot(omega3[i1:i2], np.abs(Eomega3[i1:i2])**2, label='Quadratic Phase', c="tab:green")

#ax1.legend(loc='upper left', fontsize=14)
ax2.legend(loc='upper right', fontsize=14)

#######################################################################################################
plt.figure()

Et1 = np.fft.ifft(Eomega1)
dom1 = omega1[2] - omega1[1]
df1 = dom1/(2*np.pi)
t1 = np.fft.fftshift(np.fft.fftfreq(len(Et1), d=df1))

popt,_=curve_fit(gauss_envelope,t1,np.abs(Et1)**2, p0=[max(np.abs(Et1)**2),2e-14,t1[np.argmax(np.abs(Et1)**2)]])
plt.plot(t1,np.abs(Et1)**2, label="No envelope",c="tab:blue")
#plt.plot(t1,gauss_envelope(t1,*popt), c="tab:blue")

Et2 = np.fft.ifft(Eomega2)
dom2 = omega2[2] - omega2[1]
df2 = dom2/(2*np.pi)
t2 = np.fft.fftshift(np.fft.fftfreq(len(Et2), d=df2))

popt,_=curve_fit(gauss_envelope,t2,np.abs(Et2)**2, p0=[max(np.abs(Et2)**2),2e-14,t2[np.argmax(np.abs(Et2)**2)]])
#plt.plot(t2,np.abs(Et2)**2, label="Envelope",c="tab:orange")
#plt.plot(t2,gauss_envelope(t2,*popt), c="tab:orange")

Et3 = np.fft.ifft(Eomega3)
dom3 = omega3[2] - omega3[1]
df3 = dom3/(2*np.pi)
t3 = np.fft.fftshift(np.fft.fftfreq(len(Et3), d=df3))

popt,_=curve_fit(gauss_envelope,t3,np.abs(Et3)**2, p0=[max(np.abs(Et3)**2),2e-14,t3[np.argmax(np.abs(Et3)**2)]])
plt.plot(t3,np.abs(Et3)**2, label="Quadratic phase",c="tab:green")
#plt.plot(t1,gauss_envelope(t1,*popt), c="tab:blue")

plt.xlabel("time, s",fontsize=14)
plt.ylabel("Intensity, a.u.", fontsize=14)
plt.legend(fontsize=14)
plt.show()