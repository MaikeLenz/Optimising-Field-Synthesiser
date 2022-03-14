import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import sys
import csv
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna import *

from julia import Main

Main.using("Luna")
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\")
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *

# Arguments
c = 299792458 # m/s
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
#gas = "Ar"
τfwhm = 30e-15 # FWHM durations of the pump pulse
λ0 = 800e-9 # central wavelength of the pump pulse
gas = "Ne"
pressure = 0.66*3
energy = 1e-3

domega = (0.44/τfwhm)*2*np.pi
omega = np.linspace(2*np.pi*c/λ0 - domega/2, 2*np.pi*c/λ0 + domega/2, 100)

GDDs = np.linspace(-700*(10**-30), 700*(10**-30), 20)
TODs = np.linspace(-46000*(10**-45), 46000*(10**-45), 20)
FODs = np.linspace(-112000*(10**-60), 112000*(10**-60), 20)

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.τfwhm = τfwhm
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = λ0
Main.pressure = pressure
Main.energy = energy
widths_GDD_TOD = np.zeros((len(GDDs),len(TODs)))
widths_GDD_FOD = np.zeros((len(GDDs),len(FODs)))
widths_TOD_FOD = np.zeros((len(TODs),len(FODs)))

print('Assigned values')
print('GDD vs TOD')
for i in range(len(GDDs)):
    print(GDDs[i])
    for j in range(len(TODs)):
        print(TODs[j])

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDDs[i], TOD=TODs[j], FOoD=0)
        Iω = np.abs(E**2)
        Main.ω = omega
        Main.Iω = Iω  
        Main.phase = ϕω

        Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
        
        Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
        Main.eval('t, Et = Processing.getEt(duv)')
        ω = Main.ω
        Iω = Main.Iω
        width=rms_width(ω,Iω)
        widths_GDD_TOD[i][j]=width
print('GDD vs FOD')
for i in range(len(GDDs)):
    print(GDDs[i])
    for j in range(len(FODs)):
        print(FODs[j])

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDDs[i], TOD=0, FOoD=FODs[j])
        Iω = np.abs(E**2)
        Main.ω = omega
        Main.Iω = Iω  
        Main.phase = ϕω

        Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
        
        Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
        Main.eval('t, Et = Processing.getEt(duv)')
        ω = Main.ω
        Iω = Main.Iω
        width=rms_width(ω,Iω)
        widths_GDD_FOD[i][j]=width
print('TOD vs FOD')
for i in range(len(TODs)):
    print(TODs[i])
    for j in range(len(FODs)):
        print(FODs[j])

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=0, TOD=TODs[i], FOoD=FODs[j])
        Iω = np.abs(E**2)
        Main.ω = omega
        Main.Iω = Iω  
        Main.phase = ϕω

        Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
        
        Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
        Main.eval('t, Et = Processing.getEt(duv)')
        ω = Main.ω
        Iω = Main.Iω
        width=rms_width(ω,Iω)
        widths_TOD_FOD[i][j]=width


# Save the data
header = ['GDD, fs^2', 'TOD, fs^3', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\GDD_TOD_FOD_BO\\Ne_GDD_TOD.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(GDDs)):
        for j in range(len(TODs)):
            writer.writerow([GDDs[i]*(10**30), TODs[j]*(10**45), widths_GDD_TOD[i][j]])
header = ['GDD, fs^2', 'FOD, fs^4', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\GDD_TOD_FOD_BO\\Ne_GDD_FOD.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(GDDs)):
        for j in range(len(FODs)):
            writer.writerow([GDDs[i]*(10**30), FODs[j]*(10**60), widths_GDD_FOD[i][j]])
header = ['TOD, fs^3', 'FOD, fs^4', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\GDD_TOD_FOD_BO\\Ne_TOD_FOD.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(TODs)):
        for j in range(len(FODs)):
            writer.writerow([TODs[i]*(10**45), FODs[j]*(10**60), widths_TOD_FOD[i][j]])

plt.figure()
plt.imshow(widths_GDD_TOD, extent=(np.amin(GDDs)*(10**30), np.amax(GDDs)*(10**30),np.amin(TODs)*(10**45), np.amax(TODs)*(10**45)), aspect = 'auto', origin="lower")
plt.xlabel("GDD, fs^2")
plt.ylabel("TOD, fs^3")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.figure()
plt.imshow(widths_GDD_FOD, extent=(np.amin(GDDs)*(10**30), np.amax(GDDs)*(10**30),np.amin(FODs)*(10**60), np.amax(FODs)*(10**60)), aspect = 'auto', origin="lower")
plt.xlabel("GDD, fs^2")
plt.ylabel("FOD, fs^4")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.figure()
plt.imshow(widths_TOD_FOD, extent=(np.amin(TODs)*(10**45), np.amax(TODs)*(10**45),np.amin(FODs)*(10**60), np.amax(FODs)*(10**60)), aspect = 'auto', origin="lower")
plt.xlabel("TOD, fs^3")
plt.ylabel("FOD, fs^4")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.show()

"""
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_pressure_vs_rms_width.csv")
pressures = df.iloc[:,0].values
energies = df.iloc[:,1].values
widths = df.iloc[:,2].values
"""
