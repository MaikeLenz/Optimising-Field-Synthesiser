import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *
#from theoretical_width import *

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

"""
df_init = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\Optimise_Lab\\saved_optimum\\Optimal_Params_init.csv")
iteration = df_init.iloc[:,0]
target_width = df_init.iloc[:,1] # \m
energy = df_init.iloc[:,2] # J
pressure = df_init.iloc[:,3] # bar
grating_pos = df_init.iloc[:,4] # m

plt.plot(iteration, target_width, 'x')
plt.xlabel('Evaluation Number')
plt.ylabel('RMS Width, \m')
plt.title('Initial Random Search')

best_init = max(target_width)
mean_init = np.mean(target_width)
print('Best initial random point = {} \m'.format(best_init))
print('Mean initial random point = {} \m'.format(mean_init))
"""

df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\Optimal_Params_points_probed.csv")
iteration = df_iter.iloc[:,0]
target_width_iter = df_iter.iloc[:,1] # \m
energy = df_iter.iloc[:,2] # J
pressure = df_iter.iloc[:,3] # bar
grating_pos = df_iter.iloc[:,4] # m

plt.figure()
plt.plot(iteration, target_width_iter, 'x')
plt.xlabel('Number of Iterations')
plt.ylabel('RMS Width, \s')
plt.title('Optimum Found After a Given Number of Iterations')

df_optimum = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\Optimal_Params_optimums.csv")
optimum = df_optimum.iloc[:,0]
target_width_opt = df_optimum.iloc[:,1] # \m
energy = df_optimum.iloc[:,2] # J
pressure = df_optimum.iloc[:,3] # bar
grating_pos = df_optimum.iloc[:,4] # m

plt.plot(iteration[50:], target_width_opt)

plt.show()

"""
# Plot spectrum at each optimum
filepath = 'C:\\Users\\iammo\\Documents\\'
df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\Optimal_Params_optimums.csv")
energy = df_iter.iloc[:,2] # J
pressure = df_iter.iloc[:,3] # bar
grating_pos = df_iter.iloc[:,4]

#optimum_iters = [0, 13, 100, 302]
optimum_iters = [0, 1499]

Main.radius = 175e-6
Main.flength = 1.05
Main.gas_str = "Ne"
Main.eval("gas = Symbol(gas_str)")
Main.??0 = 800e-9
Main.??fwhm = 30e-15

lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

c = 299792458 # m/s
data=lines[22:] #gets rid of all the stuff at the top
data=data[int(len(data)/2):]
for i in data:
    cut=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut):
        columns[j].append(float(value))

wavel_nm = np.array(columns[0])
intens = np.array(columns[3])
omega_list=2*np.pi*c/(wavel_nm*10**-9)
Main.?? = omega_list[::-1]
Main.I?? = intens[::-1]

results = []
for i in optimum_iters:
    grating_pair_displacement_in = grating_pos[i]
    energy_in = energy[i]
    Main.energy = energy_in
    pressure_in = pressure[i]
    Main.pressure = pressure_in

    GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
    phase = []
    for j in range(len(omega_list)):
        phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.??0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
    Main.phase = phase

    Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')

    Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')
    ?? = Main.??
    I?? = Main.I??
    t = Main.t
    Et_allz = Main.Et # array of Et at all z 
    Et = Et_allz[:,-1] # last item in each element is pulse shape at the end

    f = c/??
    results.append(rms_width(f, I??))

    plt.figure()
    plt.plot(f,I??)
    plt.xlabel('Frequency (/s)')
    #plt.plot(??*10**9,I??)
    #plt.xlabel("Wavelength (nm)")
    plt.ylabel("Spectral energy density (J/m)")
    plt.title(i)
    plt.figure()
    plt.plot(t,Et)
    plt.xlabel("Time (s)")
    plt.ylabel("Electric Field (a.u.)")
    plt.title(i)
print(results)
print('Optimum is {} times larger than no iterations'.format(results[1]/results[0]))
plt.show()
"""
# Plot on same graph with SPM optimum
filepath = 'C:\\Users\\iammo\\Documents\\'
df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\Optimal_Params_optimums.csv")
energy = df_iter.iloc[:,2] # J
pressure = df_iter.iloc[:,3] # bar
grating_pos = df_iter.iloc[:,4]

Main.radius = 175e-6
Main.flength = 1.05
Main.gas_str = "Ar"
Main.eval("gas = Symbol(gas_str)")
Main.??0 = 800e-9
Main.??fwhm = 30e-15

lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open (filepath+'Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

c = 299792458 # m/s
data=lines[22:] #gets rid of all the stuff at the top
data=data[int(len(data)/2):]
for i in data:
    cut=i.split("\t") #delimiter is \t
    for j ,value in enumerate(cut):
        columns[j].append(float(value))

results = []

wavel_nm = np.array(columns[0])
intens = np.array(columns[3])
omega_list=2*np.pi*c/(wavel_nm*10**-9)
Main.?? = omega_list[::-1]
Main.I?? = intens[::-1]

"""
grating_pair_displacement_in = grating_pos[0]
energy_in = energy[0]
Main.energy = energy_in
pressure_in = pressure[0]
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.??0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase
Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
?? = Main.??
I?? = Main.I??
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
f = c/??
results.append(rms_width(f, I??))
plt.figure(1)
#plt.plot(??*(10**9),I??, label='Optimum after 50 random points')
plt.xlabel('Wavelength (nm)')
plt.ylabel("Spectral energy density (J/m)")
plt.figure(2)
plt.plot(t,Et)
plt.xlabel("Time (s)")
plt.ylabel("Electric Field (a.u.)")
plt.title('Optimum after Random Search')
"""
Main.?? = omega_list[::-1]
Main.I?? = intens[::-1]
grating_pair_displacement_in = grating_pos[999]
energy_in = energy[999]
Main.energy = energy_in
pressure_in = pressure[999]
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.??0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase
Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
?? = Main.??
I?? = Main.I??
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
f = c/??
results.append(rms_width(f, I??))
print('RMS width of optimum = {}'.format(rms_width(f, I??)))
plt.figure(1)
#plt.plot(??*(10**9),I??, label='Optimum after 1000 iterations')
plt.plot(f,I??, label='Optimum after 1000 iterations', color='black')
plt.xlabel('Angular Frequency (/s)')
plt.ylabel('Intensity (a.u.)')
plt.figure(3)
plt.plot(t,Et)
plt.xlabel("Time (s)")
plt.ylabel("Electric Field (a.u.)")
plt.title('Optimum after Iterations')


#print(results)
#print('Optimum is {} times larger than no iterations'.format(results[1]/results[0]))

# Calculate SPM Optimum
wavel_nm = np.array(columns[0])
intens = np.array(columns[3])
omega_list=2*np.pi*c/(wavel_nm*10**-9)
Main.?? = omega_list[::-1]
Main.I?? = intens[::-1]

grating_pair_displacement_in = 0
energy_in = 1.5e-3
Main.energy = energy_in
pressure_in = 1.5
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.??0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase
Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
?? = Main.??
I?? = Main.I??
t = Main.t
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
f = c/??
plt.figure(1)
#plt.plot(??*(10**9),I??, label='SPM Optimum')
plt.plot(f,I??, '--', color='tab:red', label='SPM prediction')
plt.legend(fontsize=16)

#print('Theoretical SPM Width = {}'.format(theoretical_width(Main.radius, Main.flength, pressure_in, Main.??0, Main.??fwhm, energy_in, Main.gas_str)))
print('RMS Width of SPM prediction = {}'.format(rms_width(f, I??)))
plt.show()