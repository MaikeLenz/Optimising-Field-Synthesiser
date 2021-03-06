import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import julia
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main
Main.using("Luna")

#####################################################################################################################
# Read input pulse params
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv")
powers = df.iloc[:,0]
energies = powers/1000
λ0s = df.iloc[:,1]
domegas = df.iloc[:,2]
correction_to_tau = 1.25

#####################################################################################################################
# Define fixed params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
Main.radius = radius
Main.flength = flength
c = 299792458 
omega = np.linspace(2*np.pi*c/λ0s[0] - 5*domegas[0]/2, 2*np.pi*c/λ0s[0] + 5*domegas[0]/2, 100)

#####################################################################################################################
# Argon 0.8bar power scan
gas = "Ar"
pressure = (0,0.8)
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure

for i in range(len(energies)):
    E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0s[i], domega=domegas[i]/correction_to_tau, amp=1, CEP=0, GDD=0, TOD=0)
    Iω = np.abs(E)**2
    Main.ω = omega
    Main.Iω = Iω  
    Main.phase = ϕω
    Main.energy = energies[i]
    Main.λ0 = λ0s[i]

    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PowerScan_'+str(powers[i]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()

#####################################################################################################################

# Neon 3bar power scan
gas = "Ne"
pressure = (0,3)
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure

for i in range(len(energies)):
    E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0s[i], domega=domegas[i]/correction_to_tau, amp=1, CEP=0, GDD=0, TOD=0)
    Iω = np.abs(E**2)
    Main.ω = omega
    Main.Iω = Iω  
    Main.phase = ϕω
    Main.energy = energies[i]
    Main.λ0 = λ0s[i]

    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PowerScan_'+str(powers[i]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()
#####################################################################################################################

# Argon 1.1W pressure scan
gas = "Ar"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressures = [(0,0.2), (0,0.4), (0,0.6), (0,0.8), (0,1.0), (0,1.2), (0,1.4)]

E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0s[1], domega=domegas[1]/correction_to_tau, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E**2)
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.energy = energies[1]
Main.λ0 = λ0s[1]
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

for i in range(len(pressures)):
    Main.pressure = pressures[i]

    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ar_PressureScan_'+str(pressures[i][1]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()

#####################################################################################################################

# Neon 1.1W pressure scan
gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressures = [(0,3.6), (0,3.4), (0,3.2), (0,3.0), (0,2.8), (0,2.6), (0,2.4), (0,2.2), (0,2.0), (0,1.8), (0,1.6), (0,1.4), (0,1.2), (0,1.0)]

E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0s[1], domega=domegas[1]/correction_to_tau, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E**2)
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.energy = energies[1]
Main.λ0 = λ0s[1]
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')

for i in range(len(pressures)):
    Main.pressure = pressures[i]

    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    λ = Main.λ
    Iλ = Main.Iλ

    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\pressure_gradient\\gaussian_input_larger_omega_range\\Ne_PressureScan_'+str(pressures[i][1]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j][0]])
    
    plt.plot(λ, Iλ, label=str(i))
plt.legend()
plt.show()