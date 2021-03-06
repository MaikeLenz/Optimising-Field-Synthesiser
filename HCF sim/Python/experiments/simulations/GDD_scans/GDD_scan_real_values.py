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
# GDD in ps^2, TOD in fs^3, (GDD, TOD) - incorrect
#GDDs_and_TODs = [(-0.0984, 2.15e5), (-0.101, 2.20e5), (-0.103, 2.25e5), (-0.105, 2.30e5), (-0.108, 2.35e5), (-0.110, 2.40e5), (-0.112, 2.45e5), (-0.115, 2.50e5), (-0.117, 2.55e5), (-0.120, 2.60e5), (-0.122, 2.66e5), (-0.124, 2.71e5), (-0.127, 2.76e5), (-0.129, 2.81e5), (-0.131, 2.86e5)]
# GDD in fs^2, TOD in fs^3, (GDD, TOD) - correct
GDDs_and_TODs = [(1870, -4.09e3), (1640, -3.58e3), (1410, -3.06e3), (1170, -2.55e3), (937, -2.04e3), (703, -1.53e3), (469, -1.02e3), (234, -511), (0,0), (-234, 511), (-469, 1.02e3), (-703,1.53e3), (-937,2.04e3), (-1170,2.55e3), (-1410,3.06e3)]
# Grating positions in mm
grating_pos = [-0.40, -0.35, -0.30, -0.25, -0.20, -0.15, -0.10, -0.05, 0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]

# Read input pulse params
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv")
powers = df.iloc[:,0]
energies = powers/1000
??0s = df.iloc[:,1]
domegas = df.iloc[:,2]

# Define fixed params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
Main.radius = radius
Main.flength = flength
c = 299792458 
omega = np.linspace(2*np.pi*c/??0s[0] - domegas[0]/2, 2*np.pi*c/??0s[0] + domegas[0]/2, 100)
gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure = (0,3)
Main.pressure = pressure

freq_widths=np.array([])
for i in range(len(GDDs_and_TODs)):
    GDD = (GDDs_and_TODs[i][0] - GDDs_and_TODs[8][0])*(10**-30) #fs^2 to s^2
    TOD = (GDDs_and_TODs[i][1] - GDDs_and_TODs[8][1])*(10**-45) #fs^3 to s^3
    print(i)

    # Add additional width of 15fs 
    tau = (2*np.pi*0.44)/(domegas[1])
    new_tau = tau + 15e-15
    domega = (2*np.pi*0.44)/(new_tau)
    print(tau)
    print(new_tau)

    E, ???? = E_field_freq(omega, GD=0.0, wavel=??0s[1], domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
    I?? = np.abs(E)**2
    Main.?? = omega
    Main.I?? = I??  
    Main.phase = ????
    Main.energy = energies[1]
    Main.??0 = ??0s[1]

    Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
    
    #now extract datasets
    Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
    Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    ?? = Main.??
    I?? = Main.I??[:,0]
    ?? = Main.??
    I?? = Main.I??[:,0]
    width=rms_width(??,I??)
    freq_widths=np.append(freq_widths,width)

    # Save the data
    header = ['Wavelength, nm', 'Intensity']
    with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD' +str(GDDs_and_TODs[i][0]) + '_TOD' + str(round(GDDs_and_TODs[i][1]*(10**-5), 2)) + '_pos' + str(grating_pos[i]) + '.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)

        # write the dataS
        for j in range(len(??)):
            writer.writerow([??[j]*(10**9), I??[j]])

wavel_widths = np.array([])
for i in range(len(freq_widths)):
    wavel_widths = np.append(wavel_widths, freq_widths[i]*(??0s[1]**2)/c)

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
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\GDD_scans\\data\\real_range_plus_100fs_input_duration\\GDD_TOD_Scan_Widths.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the dataS
    for i in range(len(GDDs_and_TODs)):
        writer.writerow([grating_pos[i], GDDs_and_TODs[i][0], GDDs_and_TODs[i][1], wavel_widths[i]*(10**9)])