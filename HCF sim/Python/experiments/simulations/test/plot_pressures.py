import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.integrate import simps
import csv
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['axes.labelsize'] = 20

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

radius = 0.000175
flength = 1.05
gas = "Ne"
pressure = ((0, flength/10, 2*flength/10, 3*flength/10, 4*flength/10, 5*flength/10, 6*flength/10, 7*flength/10, 8*flength/10, 9*flength/10, flength), (0, 4.753198042323167, 7.482920440979423, 1.001029373356104, 3.7209931536865577, 2.3208030173540175, 1.8310473529191802, 2.676341902399038, 4.11004654338743, 4.570907268076029, 5.849350606030212))
λ0 = 800e-9
τfwhm = 2e-14
energy = 0.002

# Plot pressure distribution
plt.figure()
plt.xlabel('Distance along the Fibre (m)')
plt.ylabel('Pressure (bar)')
def P_gradient(z, P0, PL, L):
    return np.sqrt((P0**2) + (z/L)*((PL**2) - (P0**2)))
z = np.linspace(0, flength/10, 100)
P01 = P_gradient(z, pressure[1][0], pressure[1][1], flength/10)
P12 = P_gradient(z, pressure[1][1], pressure[1][2], flength/10)
P23 = P_gradient(z, pressure[1][2], pressure[1][3], flength/10)
P34 = P_gradient(z, pressure[1][3], pressure[1][4], flength/10)
P45 = P_gradient(z, pressure[1][4], pressure[1][5], flength/10)
P56 = P_gradient(z, pressure[1][5], pressure[1][6], flength/10)
P67 = P_gradient(z, pressure[1][6], pressure[1][7], flength/10)
P78 = P_gradient(z, pressure[1][7], pressure[1][8], flength/10)
P89 = P_gradient(z, pressure[1][8], pressure[1][9], flength/10)
P910 = P_gradient(z, pressure[1][9], pressure[1][10], flength/10)

plt.plot(z, P01, color='black')
plt.plot(z+flength/10, P12, color='black')
plt.plot(z+2*flength/10, P23, color='black')
plt.plot(z+3*flength/10, P34, color='black')
plt.plot(z+4*flength/10, P45, color='black')
plt.plot(z+5*flength/10, P56, color='black')
plt.plot(z+6*flength/10, P67, color='black')
plt.plot(z+7*flength/10, P78, color='black')
plt.plot(z+8*flength/10, P89, color='black')
plt.plot(z+9*flength/10, P910, color='black')
plt.plot(pressure[0], pressure[1], 'o', color='m',markersize=15)

# Find outcomes
# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
#Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
#Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
#ω = Main.ω
#Iω = Main.Iω
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')
ω = Main.ω
Eω = Main.Eω
Iω = np.abs(Eω)**2
"""
header = ['Angular Frequency', 'Real Electric Field', 'Imaginary Electric Field']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\pressure_distributions\\good data\\spectrum_data\\pressure_dist.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) 
    writer.writerow(header)
    for i in range(len(ω)):
        writer.writerow([ω[i], Eω[i].real, Eω[i].imag])
"""
def P_gradient(z, P0, PL, L):
    return np.sqrt((P0**2) + (z/L)*((PL**2) - (P0**2)))
def P_average(Z, P):
    norm_len = Z[-1] - Z[0]
    P_integrated = []
    for i in range(len(Z)-1):
        P0 = P[i]
        PL = P[i+1]
        L = Z[i+1] - Z[i]
        z = np.arange(0,-Z[i] +Z[i+1], L/100)
        Pz = P_gradient(z, P0, PL, L)
        P_integrated.append(simps(Pz, z))
    P_av = (np.sum(P_integrated)/norm_len)/(len(Z)-1)
    return P_av

#average_pressure = P_average(pressure[0], pressure[1])
average_pressure = np.mean(np.array(pressure[1]))
#print(average_pressure)
#print(np.mean(np.array(pressure[1])))
Main.pressure = average_pressure

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
#Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
#Main.eval("ω2, Iω2 = Processing.getIω(duv, :ω, flength)")
#ω2 = Main.ω2
#Iω2 = Main.Iω2
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')
ω2 = Main.ω
Eω2 = Main.Eω
Iω2 = np.abs(Eω2)**2
"""
header = ['Angular Frequency', 'Real Electric Field', 'Imaginary Electric Field']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\pressure_distributions\\good data\\spectrum_data\\pressure_average.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) 
    writer.writerow(header)
    for i in range(len(ω)):
        writer.writerow([ω[i], Eω[i].real, Eω[i].imag])
"""
print('Width with many points = {}'.format(rms_width(ω, Iω)))
print('Width with average P = {}'.format(rms_width(ω2, Iω2)))

plt.figure()
plt.plot(ω, Iω, label='Optimised Pressure Distribution, width %s rad/s'%(round(rms_width(ω, Iω)*10**(-13),1)),c="black")
plt.plot(ω2, Iω2, "--", label='Constant Average Pressure, width %s rad/s'%(round(rms_width(ω2, Iω2)*10**(-13),1)),c="m")
plt.xlabel("Angular Frequency (rad/s)",fontsize=20)
plt.ylabel("Intensity (a. u.)",fontsize=20)
plt.legend(fontsize=20)
plt.show()
