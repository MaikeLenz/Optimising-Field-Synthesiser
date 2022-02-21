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
radius = 175e-6 # HCF core radius

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

from scipy import integrate
energies_in_int=[]
for i in intensities:
    energies_in_int.append(integrate.simps(i,wavel_nm)/(np.pi*radius**2))

print(energies_in_int)

omega=2*np.pi*c/(wavel_nm*10**-9)

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

exp_energies_out_int=[]
for i in outintensities:
    exp_energies_out_int.append(integrate.simps(i,outwavel_nm)/(np.pi*radius**2))

#from powermeter readings
exp_energies_out=np.array([780e-3,720e-3,650e-3,590e-3,525e-3,465e-3,390e-3,330e-3,265e-3,190e-3])

##################################################################################
#simulate output spectra
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

energies_in = np.array([1.2e-3,1.1e-3,1.0e-3,0.9e-3,0.8e-3,0.7e-3,0.6e-3,0.5e-3,0.4e-3,0.3e-3]) # energy in the pump pulse, 1.2mJ

sim_energies_out_int=[]

for i in range(len(energies_in)):
    wavel = (moment(wavel_nm,intensities[i],1)/moment(wavel_nm,intensities[i],0))*10**-9

    #print(omega)
    ϕω=np.zeros(len(intens1_2))
    Main.energy = energies_in[i]
    Main.ω = omega[::-1]
    Main.Iω = intensities[i][::-1]
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

    #########################################################################################
    #find simulated output 
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

    #energy(grid, Eω; bandpass=nothing)
    #Main.eval("ω, Eω = Processing.getEω(pulse)")
    #Main.eval('energy=energy(duv,duv["Eω"])')
    #Main.eval("transm=transmission(radius, λ0, flength; kind=:HE, n=1, m=1)")
    λ = Main.λ
    Iλ = Main.Iλ
    print(λ.shape,Iλ.shape)
    #energy_i=Main.energy
    #energy_i=energies_in[i]*Main.transm
    energy_i=(integrate.simps(Iλ,λ))/(np.pi*radius**2)
    sim_energies_out_int.append(energy_i)

plt.plot(energies_in_int,exp_energies_out_int,label="experimental")
plt.plot(energies_in_int,np.array(sim_energies_out_int),label="simulation")
plt.legend()
plt.xlabel("Energy in, J")
plt.ylabel("Energy out, J")
plt.show()

