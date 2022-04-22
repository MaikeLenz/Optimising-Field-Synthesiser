import sys
import matplotlib.pyplot as plt
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.style.use('classic')

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
energies_in = np.array([1.2e-3,1.1e-3,1.0e-3,0.9e-3,0.8e-3,0.7e-3,0.6e-3,0.5e-3,0.4e-3,0.3e-3]) # energy in the pump pulse, 1.2mJ

from scipy import integrate
energies_in_int=[]
for i in intensities:
    energies_in_int.append(integrate.simps(i,wavel_nm))

print(energies_in_int)

omega=2*np.pi*c/(wavel_nm*10**-9)

#################################################################################
#get experimental output files
lines2=[]
columns2=[[],[],[],[],[],[],[],[],[],[],[],[]]

with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\Argon_0.8bar_PowerScan\\PowerScan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines2.append(myline)

c = 299792458 # m/s

data2=lines2[22:] #gets rid of all the stuff at the top
for i in data2:
    cut2=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut2):
        columns2[j].append(float(value))

outwavel_nm=np.array(columns2[0])
outintens1_29=np.array(columns2[1])
outintens1_2=np.array(columns2[2])
outintens1_1=np.array(columns2[3])
outintens1_0=np.array(columns2[4])
outintens0_9=np.array(columns2[5])
outintens0_8=np.array(columns2[6])
outintens0_7=np.array(columns2[7])
outintens0_6=np.array(columns2[8])
outintens0_5=np.array(columns2[9])
outintens0_4=np.array(columns2[10])
outintens0_3=np.array(columns2[11])

outintensities = [outintens1_2,outintens1_1,outintens1_0,outintens0_9,outintens0_8,outintens0_7,outintens0_6,outintens0_5,outintens0_4,outintens0_3]

exp_energies_out_int=[]
for i in outintensities:
    exp_energies_out_int.append(integrate.simps(i,outwavel_nm))
exp_energies_out_int=np.array(exp_energies_out_int)
energies_in_int=np.array(energies_in_int)


#from powermeter readings
exp_energies_out=np.array([485e-6,455e-6,450e-6,435e-6,400e-6,375e-6,340e-6,300e-6,250e-6,190e-6])
transmission_exp=exp_energies_out_int/energies_in_int
transmission_actual=exp_energies_out/energies_in
##################################################################################
#simulate output spectra

sim_energies_out_int=[]
sim_energies_in_int=[]

scaling = 0.56

for i in range(len(energies_in)):
    wavel = (moment(wavel_nm,intensities[i],1)/moment(wavel_nm,intensities[i],0))*10**-9

    #print(omega)
    ϕω=np.zeros(len(intens1_2))
    Main.energy = energies_in[i]
    Main.ω = omega[::-1]
    Main.Iω = intensities[i][::-1]*scaling
    Main.phase = ϕω
    Main.λ0 = wavel

    # Define experimental params
    radius = 175e-6 # HCF core radius
    flength = 1.05 # HCF length
    gas = "Ar"
    pressure = (0,0.8) # gas pressure in bar, corresponds to 66% of 3.5 atm
    Main.radius = radius
    Main.flength = flength
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = pressure

    #Pass data to Luna
    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

    #########################################################################################
    #find simulated output 
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    Main.eval("λ2, Iλ2 = Processing.getIω(duv, :λ, 0)")
    λ = Main.λ
    Iλ = Main.Iλ
    λ2 = Main.λ2
    Iλ2 = Main.Iλ2
    
    sim_energies_out_int.append(integrate.simps(Iλ[:,0],λ))
    sim_energies_in_int.append(integrate.simps(Iλ2[:,0],λ2)/scaling)

sim_energies_out_int=np.array(sim_energies_out_int)
sim_energies_in_int=np.array(sim_energies_in_int)

transmission_sim=sim_energies_out_int/sim_energies_in_int


delta_lambda=rms_width(wavel_nm,intens1_2)
I0=[]
for i in range(len(energies_in)):
    I0.append(str(round(find_I0(intensities[i],wavel_nm*10**-9,delta_lambda*10**-9,energies_in[i],175e-6)*10**-13,1)))

fig=plt.figure()
ax1 = fig.add_subplot(221)

#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax1.plot(energies_in*1000, transmission_actual,label="Experiment",marker="o",c="cyan",ls="None" ,markersize=15)
ax1.plot(energies_in*1000,transmission_sim,label="Luna, Input Energy times %s"%(round(scaling,2)),marker="^",ls="None" ,markersize=15,   c="m")
ax1.errorbar(energies_in*1000, transmission_actual, xerr = 0.1*energies_in*1000,yerr=0.2*transmission_actual, ls="None" ,markersize=15,c="grey")
plt.legend(fontsize=16)
ax1.set_xticks(list(energies_in*1000))
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
ax1.set_xlim(0.2,1.3)
ax1.set_ylim(0.,1.0)

ax1.set_xlabel("Input Energy, mJ",fontsize=20)
ax1.set_ylabel("Transmission",fontsize=20)

ax2 = ax1.twiny()
ax2.set_xlabel("Input Intensity (I$\mathrm{_{0}}$), $\mathrm{10^{13} W/cm^2}$",fontsize=20)
ax2.set_xlim(0.2,1.3)
plt.xticks(fontsize=16)
ax2.set_xticks(list(energies_in*1000))
#ax2.set_title("Argon Power Scan",fontsize=22)
plt.text(0.5, 1.25, "Argon Power Scan",
         horizontalalignment='center',
         fontsize=22,
         transform = ax2.transAxes,
         fontweight="bold")
ax2.set_xticklabels(I0)
#plt.grid()

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

#from powermeter readings
exp_energies_out=np.array([625e-6,590e-6,540e-6,475e-6,450e-6,420e-6,400e-6])
#transmission_exp=exp_energies_out_int/energy_in_int
transmission_actual=exp_energies_out/energy_in
##################################################################################
#simulate output spectra

sim_energies_out_int=[]
sim_energies_in_int=[]
wavel = (moment(wavel_nm,intens1_1,1)/moment(wavel_nm,intens1_1,0))*10**-9
scaling=0.62

for i in range(len(pressures)):
    ϕω=np.zeros(len(intens1_1))
    Main.energy = energy_in*scaling
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
    λ = Main.λ
    Iλ = Main.Iλ
    λ2 = Main.λ2
    Iλ2 = Main.Iλ2
    sim_energies_out_int.append(integrate.simps(Iλ[:,0],λ))
    sim_energies_in_int.append(integrate.simps(Iλ2[:,0],λ2)/scaling)

sim_energies_out_int=np.array(sim_energies_out_int)
sim_energies_in_int=np.array(sim_energies_in_int)

transmission_sim=sim_energies_out_int/sim_energies_in_int

delta_lambda=rms_width(wavel_nm,intens1_1)
I0=str(round(find_I0(intens1_1,wavel_nm*10**-9,delta_lambda*10**-9,energy_in,0.5*175e-6)*10**-13,1))


ax1 = fig.add_subplot(223)
fig.patch.set_facecolor('white')

#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax1.plot(np.array(pressures), transmission_actual,label=r"Experiment, I$\mathrm{_0}$="+I0+"e13W/$\mathrm{cm^2}$",marker="o",c="cyan",ls="None" ,markersize=15 )
ax1.plot(np.array(pressures),transmission_sim,label="Luna, Input Energy times %s"%(round(scaling,2)),marker="^",ls="None" ,markersize=15,   c="m")
ax1.errorbar(np.array(pressures), transmission_actual, xerr = 0.1*np.array(pressures),yerr=0.2*transmission_actual, ls="None" ,markersize=15,c="grey")
ax1.set_xlim(0.1,1.5)
ax1.set_ylim(0.,1.0)

ax1.set_xticks(list(pressures))
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
ax1.set_xlabel("Pressure, Bar",fontsize=20)
ax1.set_ylabel("Transmission",fontsize=20)
ax1.set_title("Argon Pressure Scan",fontsize=22,fontweight="bold")
plt.legend(fontsize=16)
#plt.grid()

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
energies_in = np.array([1.2e-3,1.1e-3,1.0e-3,0.9e-3,0.8e-3,0.7e-3,0.6e-3,0.5e-3,0.4e-3,0.3e-3]) # energy in the pump pulse, 1.2mJ

from scipy import integrate

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


#from powermeter readings
exp_energies_out=np.array([780e-6,720e-6,650e-6,590e-6,525e-6,465e-6,390e-6,330e-6,265e-6,190e-6])
#transmission_exp=exp_energies_out_int/energies_in_int
transmission_actual=exp_energies_out/energies_in
##################################################################################
#simulate output spectra

sim_energies_out_int=[]
sim_energies_in_int=[]

scaling=0.695

for i in range(len(energies_in)):
    wavel = (moment(wavel_nm,intensities[i],1)/moment(wavel_nm,intensities[i],0))*10**-9

    #print(omega)
    ϕω=np.zeros(len(intens1_2))
    Main.energy = energies_in[i]*scaling
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

    #Pass data to Luna
    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

    #########################################################################################
    #find simulated output 
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    Main.eval("λ2, Iλ2 = Processing.getIω(duv, :λ, 0)")

    λ = Main.λ
    Iλ = Main.Iλ
    λ2 = Main.λ2
    Iλ2 = Main.Iλ2
    
    sim_energies_out_int.append(integrate.simps(Iλ[:,0],λ))
    sim_energies_in_int.append(integrate.simps(Iλ2[:,0],λ2)/scaling)

sim_energies_out_int=np.array(sim_energies_out_int)
sim_energies_in_int=np.array(sim_energies_in_int)

transmission_sim=sim_energies_out_int/sim_energies_in_int

delta_lambda=rms_width(wavel_nm,intens1_2)
I0=[]
for i in range(len(energies_in)):
    I0.append(str(round(find_I0(intensities[i],wavel_nm*10**-9,delta_lambda*10**-9,energies_in[i],0.5*175e-6)*10**-13,1)))


ax1 = fig.add_subplot(222)

#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax1.plot(energies_in*1000, transmission_actual,label="Experiment",marker="o",c="cyan",ls="None" ,markersize=15 )
ax1.plot(energies_in*1000,transmission_sim,label="Luna, Input Energy times %s"%(round(scaling,2)),marker="^",ls="None" ,markersize=15,   c="m")
ax1.errorbar(energies_in*1000, transmission_actual, xerr = 0.1*energies_in*1000,yerr=0.2*transmission_actual, ls="None" ,markersize=15,c="grey")

ax1.set_xlim(0.2,1.3)
ax1.set_ylim(0.,1.0)

ax1.set_xticks(list(energies_in*1000))
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
ax1.set_xlabel("Input Energy, mJ",fontsize=20)
ax1.set_ylabel("Transmission",fontsize=20)
plt.legend(fontsize=16,loc="lower right")
ax2 = ax1.twiny()
ax2.set_xlabel(r"Input Intensity (I$\mathrm{_{0}}$), $\mathrm{10^{13}W/cm^2}$",fontsize=20)
ax2.set_xlim(0.2,1.3)
ax2.set_xticks(list(energies_in*1000))
plt.xticks(fontsize=16)
ax2.set_xticklabels(I0)
#ax2.set_title("Neon Power Scan",fontsize=22)
plt.text(0.5, 1.25, "Neon Power Scan",
         horizontalalignment='center',
         fontsize=22,
         transform = ax2.transAxes,
         fontweight="bold")
#plt.grid()


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
columns2=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\Neon_1.1Win_PressureScan\\pressure_scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines2.append(myline)

c = 299792458 # m/s

data2=lines2[22:] #gets rid of all the stuff at the top
for i in data2:
    cut2=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut2):
        columns2[j].append(float(value))

outwavel_nm=np.array(columns2[0])
press3_6=np.array(columns2[1])
press3_4=np.array(columns2[2])
press3_2=np.array(columns2[3])
press3_0=np.array(columns2[4])
press2_8=np.array(columns2[5])
press2_6=np.array(columns2[6])
press2_4=np.array(columns2[7])
press2_2=np.array(columns2[8])
press2_0=np.array(columns2[9])
press1_8=np.array(columns2[10])
press1_6=np.array(columns2[11])
press1_4=np.array(columns2[12])
press1_2=np.array(columns2[13])
press1_0=np.array(columns2[14])

pressure_spectra = [press3_6,press3_4,press3_2,press3_0,press2_8,press2_6,press2_4,press2_2,press2_0,press1_8,press1_6,press1_4,press1_2,press1_0]
pressures=[3.6,3.4,3.2,3.0,2.8,2.6,2.4,2.2,2.0,1.8,1.6,1.4,1.2,1.0]

#from powermeter readings
exp_energies_out=np.array([710e-6,710e-6,720e-6,724e-6,740e-6,740e-6,735e-6,740e-6,750e-6,740e-6,735e-6,740e-6,740e-6,740e-6])
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
scaling=0.71

for i in range(len(pressures)):
    ϕω=np.zeros(len(intens1_1))
    Main.energy = energy_in*scaling
    Main.ω = omega[::-1]
    Main.Iω = intens1_1[::-1]
    Main.phase = ϕω
    Main.λ0 = wavel

    # Define experimental params
    radius = 175e-6 # HCF core radius
    flength = 1.05 # HCF length
    gas = "Ne"
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

    λ = Main.λ
    Iλ = Main.Iλ
    λ2 = Main.λ2
    Iλ2 = Main.Iλ2
    
    sim_energies_out_int.append(integrate.simps(Iλ[:,0],λ))
    sim_energies_in_int.append(integrate.simps(Iλ2[:,0],λ2)/scaling)

sim_energies_out_int=np.array(sim_energies_out_int)
sim_energies_in_int=np.array(sim_energies_in_int)

transmission_sim=sim_energies_out_int/sim_energies_in_int

delta_lambda=rms_width(wavel_nm,intens1_1)
I0=str(round(find_I0(intens1_1,wavel_nm*10**-9,delta_lambda*10**-9,energy_in,0.5*175e-6)*10**-13,1))

ax1 = fig.add_subplot(224)
ax1.set_title("Neon Pressure Scan",fontsize=22,fontweight="bold")
plt.yticks(fontsize=16)
ax1.set_xticks(list(pressures))
plt.xticks(fontsize=16)
#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
ax1.plot(np.array(pressures), transmission_actual,label=r"Experiment, I$\mathrm{_{0}}$="+I0+"e13$\mathrm{W/cm^2}$",marker="o",c="cyan",ls="None" ,markersize=15 )
ax1.plot(np.array(pressures),transmission_sim,label="Luna, Input Energy times %s"%(round(scaling,2)),marker="^",ls="None" ,markersize=15,   c="m")
ax1.errorbar(np.array(pressures), transmission_actual, xerr = 0.1*np.array(pressures),yerr=0.2*transmission_actual, ls="None" ,markersize=15,c="grey")
ax1.set_xlim(0.9,3.7)
ax1.set_ylim(0.,1.0)
ax1.set_xlabel("Pressure, Bar",fontsize=20)
ax1.set_ylabel("Transmission",fontsize=20)
plt.legend(fontsize=16,loc="lower right")
#plt.grid()

plt.show()

