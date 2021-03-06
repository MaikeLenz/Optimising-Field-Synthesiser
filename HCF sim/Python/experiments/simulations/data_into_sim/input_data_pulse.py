import matplotlib.pyplot as plt
import numpy as np

#path to txt file
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]

import sys
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *

#get input
with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
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

wavel_nm=np.array(columns[0])
intens1_2=np.array(columns[1])

omega=2*np.pi*c/(wavel_nm*10**-9)


plt.plot(omega,intens1_2, label="I(omega), 1200mW")
plt.xlabel("Angular frequency")
plt.ylabel("Intensity")
plt.legend()
plt.figure()
plt.plot(wavel_nm,intens1_2,label="I(lambda), 1200mW")
plt.xlabel("Wavelength, nm")
plt.ylabel("Intensity")
plt.legend()
plt.show()

#get experimental output
lines2=[]
columns2=[[],[],[],[],[],[],[],[],[],[],[],[]]

with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\Neon_3bar_PowerScan\\PowerScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines2.append(myline)

c = 299792458 # m/s

data2=lines2[22:] #gets rid of all the stuff at the top
for i in data2:
    cut2=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut2):
        columns2[j].append(float(value))

outwavel_nm=np.array(columns2[0])
outintens1_2=np.array(columns2[11])

import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

# Define custom pulse in frequency domain
energy = 1.2e-3 # energy in the pump pulse, 1.2mJ
wavel = (moment(wavel_nm,intens1_2,1)/moment(wavel_nm,intens1_2,0))*10**-9
print(wavel)
#print(omega)
????=np.zeros(len(intens1_2))
Main.energy = energy
Main.?? = omega[::-1]
Main.I?? = intens1_2[::-1]
Main.phase = ????
Main.??0 = wavel

# Define experimental params
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
gas = "Ne"
pressure = (0.001,3.) # gas pressure in bar, corresponds to 66% of 3.5 atm
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")

## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
?? = Main.??
I?? = Main.I??
#plotting
plt.figure()
plt.plot(??*10**9,I??,label="simulation")
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")
plt.plot(outwavel_nm,outintens1_2, label="experiment")
plt.legend()
plt.show()


