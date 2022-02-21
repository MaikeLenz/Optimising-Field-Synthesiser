import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import julia
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main
Main.using("Luna")

#####################################################################################################################
# Read input pulses
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
#with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
with open ('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

c = 299792458 # m/s
#print(lines[:22])
data=lines[22:] #gets rid of all the stuff at the top
data=data[int(len(data)/2):]
for i in data:
    cut=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut):
        columns[j].append(float(value))

wavel_nm = np.array(columns[0])
intens1_2 = np.array(columns[1])
intens1_1 = np.array(columns[2])
intens1_0 = np.array(columns[3])
intens0_9 = np.array(columns[4])
intens0_8 = np.array(columns[5])
intens0_7 = np.array(columns[6])
intens0_6 = np.array(columns[7])
intens0_5 = np.array(columns[8])
intens0_4 = np.array(columns[9])
intens0_3 = np.array(columns[10])

#####################################################################################################################
# Define fixed params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
Main.radius = radius
Main.flength = flength
c = 299792458 
omega=2*np.pi*c/(wavel_nm*10**-9)

#####################################################################################################################
"""
# Argon 0.8bar power scan
gas = "Ar"
pressure = 0.8
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure
energies = [1.2e-3, 1.1e-3, 1.0e-3, 0.9e-3, 0.8e-3, 0.7e-3, 0.6e-3, 0.5e-3, 0.4e-3, 0.3e-3]
powers = energies*(10**3)
intens = [intens1_2, intens1_1, intens1_0, intens0_9, intens0_8, intens0_7, intens0_6, intens0_5, intens0_4, intens0_3]

for i in range(len(energies)):
    wavel = (moment(wavel_nm,intens[i],1)/moment(wavel_nm,intens[i],0))*10**-9
    ϕω=np.zeros(len(intens[i]))
    Main.energy = energies[i]
    Main.ω = omega[::-1]
    Main.Iω = intens[i][::-1]
    Main.phase = ϕω
    Main.λ0 = wavel
    
    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pulse_input\\Ar_PowerScan_'+str(powers[i]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()
"""
#####################################################################################################################
"""
# Neon 3bar power scan
gas = "Ne"
pressure = 3
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure
energies = [1.2e-3, 1.1e-3, 1.0e-3, 0.9e-3, 0.8e-3, 0.7e-3, 0.6e-3, 0.5e-3, 0.4e-3, 0.3e-3]
powers = energies*(10**3)
intens = [intens1_2, intens1_1, intens1_0, intens0_9, intens0_8, intens0_7, intens0_6, intens0_5, intens0_4, intens0_3]

for i in range(len(energies)):
    wavel = (moment(wavel_nm,intens[i],1)/moment(wavel_nm,intens[i],0))*10**-9
    ϕω=np.zeros(len(intens[i]))
    Main.energy = energies[i]
    Main.ω = omega[::-1]
    Main.Iω = intens[i][::-1]
    Main.phase = ϕω
    Main.λ0 = wavel

    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pulse_input\\Ne_PowerScan_'+str(powers[i]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()
"""
#####################################################################################################################
"""
# Argon 1.1W pressure scan
gas = "Ar"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressures = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]

# Define custom pulse in the frequency domain
energy = 1.1e-3 
wavel = (moment(wavel_nm,intens1_1,1)/moment(wavel_nm,intens1_1,0))*10**-9
ϕω=np.zeros(len(intens1_1))
Main.energy = energy
Main.ω = omega[::-1]
Main.Iω = intens1_1[::-1]
Main.phase = ϕω
Main.λ0 = wavel
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

for i in range(len(pressures)):
    Main.pressure = pressures[i]

    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pulse_input\\Ar_PressureScan_'+str(pressures[i]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()
"""
#####################################################################################################################
"""
# Neon 1.1W pressure scan
gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressures = [3.6, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]

# Define custom pulse in the frequency domain
energy = 1.1e-3 
wavel = (moment(wavel_nm,intens1_1,1)/moment(wavel_nm,intens1_1,0))*10**-9
ϕω=np.zeros(len(intens1_1))
Main.energy = energy
Main.ω = omega[::-1]
Main.Iω = intens1_1[::-1]
Main.phase = ϕω
Main.λ0 = wavel
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

for i in range(len(pressures)):
    Main.pressure = pressures[i]

    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pulse_input\\Ne_PressureScan_'+str(pressures[i]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()
"""
