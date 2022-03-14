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

domega = (0.44/τfwhm)*2*np.pi
omega = np.linspace(2*np.pi*c/λ0 - domega/2, 2*np.pi*c/λ0 + domega/2, 100)

pressures = np.linspace(0.01, 3.5, 20)
energies = np.linspace(0.1e-3, 1.3e-3, 20)
grating_positions = np.linspace(-0.5e-3, 0.5e-3, 20)

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.τfwhm = τfwhm
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = λ0
widths_E_P=np.zeros((len(energies),len(pressures)))
widths_E_G=np.zeros((len(energies),len(grating_positions)))
widths_P_G=np.zeros((len(pressures),len(grating_positions)))

print('Assigned values')
print('Energy vs Pressure')
for i in range(len(energies)):
    Main.energy = energies[i]
    print(energies[i])
    for j in range(len(pressures)):
        print(pressures[j])
        Main.pressure = pressures[j]
        #for k in range(len(grating_positions)):
        #    grating_pos = grating_positions[k]
            # Calculations

        #   GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pos*1000)
        GDD = 0
        TOD = 0

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
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
        widths_E_P[i][j]=width
print('Energy vs Grating Pos')
for i in range(len(energies)):
    Main.energy = energies[i]
    print(energies[i])
    for j in range(len(grating_positions)):
        print(grating_positions[j])
        pressure = 3*0.66
        Main.pressure = pressure

        grating_pos = grating_positions[j]
        GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pos*1000)

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
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
        widths_E_G[i][j]=width
print('Pressure vs Grating Pos')
for i in range(len(pressures)):
    Main.pressure = pressures[i]
    print(pressures[i])
    for j in range(len(grating_positions)):
        print(grating_positions[j])
        energy = 1e-3
        Main.energy = energy

        grating_pos = grating_positions[j]
        GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pos*1000)

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
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
        widths_P_G[i][j]=width


# Save the data
header = ['Pulse energy, mJ', 'Pressure, bar', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\energy_pressure_GDD_BO\\Ne_energy_pressure.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(energies)):
        for j in range(len(pressures)):
            writer.writerow([energies[i]*(10**3), pressures[j], widths_E_P[i][j]])
header = ['Pulse energy, mJ', 'Compressor Grating Position, m', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\energy_pressure_GDD_BO\\Ne_energy_grating.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(energies)):
        for j in range(len(grating_positions)):
            writer.writerow([energies[i]*(10**3), grating_positions[j], widths_E_G[i][j]])
header = ['Pressure, bar', 'Compressor Grating Position, m', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\gaussian_input\\angfreq_bandwidth\\energy_pressure_GDD_BO\\Ne_pressure_grating.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(pressures)):
        for j in range(len(grating_positions)):
            writer.writerow([pressures[i], grating_positions[j], widths_E_P[i][j]])

plt.figure()
plt.imshow(widths_E_P, extent=(np.amin(pressures), np.amax(pressures),np.amin(energies)*10**3, np.amax(energies)*10**3), aspect = 'auto', origin="lower")
plt.xlabel("Pressure, bar")
plt.ylabel("Pulse energy, mJ")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.figure()
plt.imshow(widths_E_G, extent=(np.amin(energies)*10**3, np.amax(energies)*10**3 ,np.amin(grating_positions), np.amax(grating_positions)), aspect = 'auto', origin="lower")
plt.xlabel("Pulse energy, mJ")
plt.ylabel("Compressor Grating Position, m")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.figure()
plt.imshow(widths_P_G, extent=(np.amin(pressures), np.amax(pressures),np.amin(grating_positions), np.amax(grating_positions)), aspect = 'auto', origin="lower")
plt.xlabel("Pressure, bar")
plt.ylabel("Compressor Grating Position, m")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)

plt.show()

"""
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_pressure_vs_rms_width.csv")
pressures = df.iloc[:,0].values
energies = df.iloc[:,1].values
widths = df.iloc[:,2].values
"""
