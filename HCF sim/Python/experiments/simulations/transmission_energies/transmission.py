import sys
import matplotlib.pyplot as plt
import julia
import numpy as np
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

################################################################################################
#import data
#path to txt file
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]

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
intens1_1=np.array(columns[2])
intens1_0=np.array(columns[3])
intens0_9=np.array(columns[4])
intens0_8=np.array(columns[5])
intens0_7=np.array(columns[6])
intens0_6=np.array(columns[7])
intens0_5=np.array(columns[8])
intens0_4=np.array(columns[9])
intens0_3=np.array(columns[10])

#list of input spectra
intensities = [intens1_2,intens1_1,intens1_0,intens0_9,intens0_8,intens0_7,intens0_6,intens0_5,intens0_4,intens0_3]

omega=2*np.pi*c/(wavel_nm*10**-9)

####################################################################################################
#calculate input energies by integrating intensities
from scipy import integrate
energy_in=[]
for i in intensities:
    energy_in_i = integrate.simps(i, wavel_nm)
    energy_in.append(energy_in_i)

print(energy_in)

#################################################################################
#get experimental output files
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
outintens1_1=np.array(columns2[2])
outintens1_0=np.array(columns2[3])
outintens0_9=np.array(columns2[4])
outintens0_8=np.array(columns2[5])
outintens0_7=np.array(columns2[6])
outintens0_6=np.array(columns2[7])
outintens0_5=np.array(columns2[8])
outintens0_4=np.array(columns2[9])
outintens0_3=np.array(columns2[10])
outintens1_2=np.array(columns2[11])

outintensities = [outintens1_2,outintens1_1,outintens1_0,outintens0_9,outintens0_8,outintens0_7,outintens0_6,outintens0_5,outintens0_4,outintens0_3]

#################################################################################
#find output energies

exp_energy_out=[]
for i in outintensities:
    energy_out_i = integrate.simps(i, outwavel_nm)
    exp_energy_out.append(energy_out_i)

print(exp_energy_out)

"""
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
ϕω=np.zeros(len(intens1_2))
Main.energy = energy
Main.ω = omega[::-1]
Main.Iω = intens1_2[::-1]
Main.phase = ϕω
Main.λ0 = wavel

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
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
λ = Main.λ
Iλ = Main.Iλ
#plotting
plt.figure()
plt.plot(λ*10**9,Iλ,label="simulation")
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")
plt.plot(outwavel_nm,outintens1_2, label="experiment")
plt.legend()
plt.show()

"""

