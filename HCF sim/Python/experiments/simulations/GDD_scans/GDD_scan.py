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

GDDs = np.linspace(-10000*(10**-30), 10000*(10**-30), 100)

# Read input pulse params
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv")
powers = df.iloc[:,0]
energies = powers/1000
λ0s = df.iloc[:,1]
domegas = df.iloc[:,2]

# Define fixed params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
Main.radius = radius
Main.flength = flength
c = 299792458 
omega = np.linspace(2*np.pi*c/λ0s[0] - domegas[0]/2, 2*np.pi*c/λ0s[0] + domegas[0]/2, 100)
gas = "Ne"
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
pressure = (0,3)
Main.pressure = pressure

freq_widths=np.array([])
for i in range(len(GDDs)):
    print(i)
    E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0s[1], domega=domegas[1], amp=1, CEP=0, GDD=GDDs[i], TOD=0)
    Iω = np.abs(E**2)
    Main.ω = omega
    Main.Iω = Iω  
    Main.phase = ϕω
    Main.energy = energies[1]
    Main.λ0 = λ0s[1]

    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
    
    #now extract datasets
    Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    ω = Main.ω
    Iω = Main.Iω
    width=rms_width(ω,Iω)
    freq_widths=np.append(freq_widths,width)

wavel_widths = np.array([])
for i in range(len(freq_widths)):
    wavel_widths = np.append(wavel_widths, freq_widths[i]*(λ0s[1]**2)/c)

plt.figure()
plt.scatter(GDDs*(10**30),wavel_widths*(10**9),marker="+")
plt.ylabel("RMS width, nm")
plt.xlabel('GDD, fs^2')
plt.title('Simulated GDD Scan')
plt.show()


# Save the data
header = ['GDD, fs^2', 'Simulated RMS Width, nm']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\simulations\\data\\GDD_Scan_huge_range.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the dataS
    for i in range(len(GDDs)):
        writer.writerow([GDDs[i]*(10**30), wavel_widths[i]*(10**9)])

"""
import pandas as pd
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\custom_input\\data\\GDD_Ne_long_range_vs_rms_width.csv")

plt.plot(df.iloc[:,0],df.iloc[:,1])
plt.ylabel("angular frequency width, /s")
plt.xlabel('GDD, fs^2')
plt.show()
"""