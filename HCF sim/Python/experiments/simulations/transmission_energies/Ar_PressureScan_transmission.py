import sys
from matplotlib.cbook import ls_mapper
import matplotlib.pyplot as plt
import julia
import numpy as np
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\input_spectra\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\input_spectra\\")
from find_I0 import *

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
intens1_1=np.array(columns[2])
energy_in = 1.1e-3


from scipy import integrate
#energy_in_int=integrate.simps(intens1_1,wavel_nm)

omega=2*np.pi*c/(wavel_nm*10**-9)

#################################################################################
#get experimental output files
lines2=[]
columns2=[[],[],[],[],[],[],[],[]]

with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\Argon_1.1Win_PressureScan\\PressureScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines2.append(myline)

c = 299792458 # m/s

data2=lines2[22:] #gets rid of all the stuff at the top
for i in data2:
    cut2=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut2):
        columns2[j].append(float(value))

outwavel_nm=np.array(columns2[0])
press0_2=np.array(columns2[1])
press0_4=np.array(columns2[2])
press0_6=np.array(columns2[3])
press0_8=np.array(columns2[4])
press1_0=np.array(columns2[5])
press1_2=np.array(columns2[6])
press1_4=np.array(columns2[7])

pressure_spectra = [press0_2,press0_4,press0_6,press0_8,press1_0,press1_2,press1_4]
pressures=[0.2,0.4,0.6,0.8,1.0,1.2,1.4]
"""
exp_energies_out_int=[]
for i in pressure_spectra:
    exp_energies_out_int.append(integrate.simps(i,outwavel_nm))
exp_energies_out_int=np.array(exp_energies_out_int)
"""
#from powermeter readings
exp_energies_out=np.array([625e-6,590e-6,540e-6,475e-6,450e-6,420e-6,400e-6])
#transmission_exp=exp_energies_out_int/energy_in_int
transmission_actual=exp_energies_out/energy_in
##################################################################################
#simulate output spectra
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

sim_energies_out_int=[]
sim_energies_in_int=[]
wavel = (moment(wavel_nm,intens1_1,1)/moment(wavel_nm,intens1_1,0))*10**-9

for i in range(len(pressures)):
    ϕω=np.zeros(len(intens1_1))
    Main.energy = energy_in
    Main.ω = omega[::-1]
    Main.Iω = intens1_1[::-1]
    Main.phase = ϕω
    Main.λ0 = wavel

    # Define experimental params
    radius = 175e-6 # HCF core radius
    flength = 1.05 # HCF length
    gas = "Ar"
    Main.radius = radius
    Main.flength = flength
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = (0,pressures[i])

    #Pass data to Luna
    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

    #########################################################################################
    #find simulated output 
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    Main.eval("λ2, Iλ2 = Processing.getIω(duv, :λ, 0)")

    #energy(grid, Eω; bandpass=nothing)
    #Main.eval("ω, Eω = Processing.getEω(pulse)")
    #Main.eval('energy=energy(duv,duv["Eω"])')
    #Main.eval("transm=transmission(radius, λ0, flength; kind=:HE, n=1, m=1)")
    λ = Main.λ
    Iλ = Main.Iλ
    λ2 = Main.λ2
    Iλ2 = Main.Iλ2
    
    #energy_i=Main.energy
    #energy_i=energies_in[i]*Main.transm
    sim_energies_out_int.append(integrate.simps(Iλ[:,0],λ))
    sim_energies_in_int.append(integrate.simps(Iλ2[:,0],λ2))

sim_energies_out_int=np.array(sim_energies_out_int)
sim_energies_in_int=np.array(sim_energies_in_int)

transmission_sim=sim_energies_out_int/sim_energies_in_int
scaling = transmission_actual[0]/transmission_sim[0]

transmission_sim_scaled=transmission_sim*scaling

delta_lambda=rms_width(wavel_nm,intens1_1)
I0=str(round(find_I0(intens1_1,wavel_nm*10**-9,delta_lambda*10**-9,energy_in,0.5*175e-6)*10**-13,1))+"e13"

fig = plt.figure()
ax1 = fig.add_subplot(111)

#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax1.plot(np.array(pressures), transmission_actual,label="experiment, I0="+I0+"W/cm^2",marker="+",ls="None")
ax1.plot(np.array(pressures),transmission_sim_scaled,label="simulation, scaled down to %s"%(round(scaling,2)),marker="+",ls="None")
ax1.set_xlim(0.1,1.5)
ax1.set_xlabel("Pressure, Bar")
ax1.set_ylabel("Transmission")
plt.legend()
"""
ax2 = ax1.twiny()
ax2.set_xlabel("Input Intensity (I0), W/cm^2")
ax2.set_xlim(0.9,3.7)
ax2.set_xticks(list(energy_in))
ax2.set_xticklabels(I0)
"""
plt.show()

