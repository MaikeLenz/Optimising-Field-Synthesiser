import julia
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv  
import sys

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
#from theoretical_width import theoretical_width

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

from rms_width import *
c = 299792458 # m/s

# Values found from https://lasercalculator.com/grating-pair-dispersion-calculator/
# GDD in fs^2, TOD in fs^3, (GDD, TOD)
GDDs_and_TODs = [(1870, -4.09e3), (1640, -3.58e3), (1410, -3.06e3), (1170, -2.55e3), (937, -2.04e3), (703, -1.53e3), (469, -1.02e3), (234, -511), (0,0), (-234, 511), (-469, 1.02e3), (-703,1.53e3), (-937,2.04e3), (-1170,2.55e3), (-1410,3.06e3)]
# Grating positions in mm
grating_pos = [-0.40, -0.35, -0.30, -0.25, -0.20, -0.15, -0.10, -0.05, 0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]

# Read input pulse params
lines = []
columns = [[],[],[],[],[],[],[],[],[],[],[]]
with open ('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data = lines[22:] #gets rid of all the stuff at the top
for i in data:
    split = i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))
wavel_nm = np.array(columns[0])
intens = np.array(columns[2])

omega=2*np.pi*c/(wavel_nm*10**-9)
ω = omega[::-1]
Iω = intens[::-1]

# Define fixed params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
Main.radius = radius
Main.flength = flength
c = 299792458 
gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure = (0,3)
Main.pressure = pressure

wavel = (moment(wavel_nm,intens,1)/moment(wavel_nm,intens,0))*10**-9
Main.λ0 = wavel
omega0 = 2*np.pi*c/wavel

freq_widths=np.array([])
for i in range(len(GDDs_and_TODs)):
    GDD = (GDDs_and_TODs[i][0] - GDDs_and_TODs[8][0])*(10**-30) #fs^2 to s^2
    TOD = (GDDs_and_TODs[i][1] - GDDs_and_TODs[8][1])*(10**-45) #fs^3 to s^3
    print(i)

    ω = omega[::-1]
    Iω = intens[::-1]
    Main.ω = ω
    Main.Iω = Iω
    Main.energy = 1.1/1000

    #phase = np.zeros(len(ω))
    phase = []
    for j in range(len(ω)):
        phase.append(get_phi(omega=ω[j], omega0=omega0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
    Main.phase = phase

    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    
    #now extract datasets
    Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    ω = Main.ω
    Iω = Main.Iω[:,0]
    λ = Main.λ
    Iλ = Main.Iλ[:,0]
    width=rms_width(ω,Iω)
    freq_widths=np.append(freq_widths,width)

    # Save the data
    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD' +str(GDDs_and_TODs[i][0]) + '_TOD' + str(round(GDDs_and_TODs[i][1]*(10**-5), 2)) + '_pos' + str(grating_pos[i]) + '.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)

        # write the dataS
        for j in range(len(λ)):
            writer.writerow([λ[j]*(10**9), Iλ[j]])

wavel_widths = np.array([])
for i in range(len(freq_widths)):
    wavel_widths = np.append(wavel_widths, freq_widths[i]*(wavel**2)/c)

f, axs = plt.subplots(1, 2)
for i in range(len(GDDs_and_TODs)):
    axs[0].plot(grating_pos[i], GDDs_and_TODs[i][0], 'x', color='tab:red')
    axs[1].plot(grating_pos[i], GDDs_and_TODs[i][1], 'x', color='tab:blue')
axs[0].set_xlabel('Compressor Grating Position, mm')
axs[1].set_xlabel('Compressor Grating Position, mm')
axs[0].set_ylabel('GDD, fs^2')
axs[1].set_ylabel('TOD, fs^3')

# Save the data
header = ['Grating Position, mm', 'GDD, fs^2', 'TOD, fs^3', 'Simulated RMS Width, nm']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\GDD_scans\\data\\real_range_exp_pulse_input\\GDD_TOD_Scan_Widths.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the dataS
    for i in range(len(GDDs_and_TODs)):
        writer.writerow([grating_pos[i], GDDs_and_TODs[i][0], GDDs_and_TODs[i][1], wavel_widths[i]*(10**9)])