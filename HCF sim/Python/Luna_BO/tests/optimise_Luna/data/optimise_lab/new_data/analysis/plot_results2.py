import numpy as np
import sys
import matplotlib.pyplot as plt
import csv
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *
#from theoretical_width import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
filepath = 'C:\\Users\\iammo\\Documents\\'
#filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\"
# Define fixed params
Main.radius = 175e-6
Main.flength = 1.05
Main.gas_str = "Ar"
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = 800e-9
Main.τfwhm = 2.75e-14

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
Main.ω = omega_list[::-1]
Main.Iω = intens[::-1]

# Plot the optimum found
energy_in = 0.0011730020668117554
pressure_in = 0.9896159222064448
grating_pair_displacement_in = 1.3687440750850062e-05

Main.energy = energy_in
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase

Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω1, Iω1 = Processing.getIω(duv, :ω, flength)")
ω1 = Main.ω1
Iω1 = Main.Iω1
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
ω2 = Main.ω2
Eω2 = Main.ω2
"""
header = ['Angular Frequency', 'Real Electric Field', 'Imaginary Electric Field']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\new_data\\analysis\\spectrum_data\\optimum.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    writer.writerow(header)
    for i in range(len(ω2)):
        writer.writerow([ω2[i], Eω2[i].real, Eω2[i].imag])
"""
om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, Eω2, lambda0)
thresh = 0.1
rows = np.where(np.abs(Eω2)**2 > max(np.abs(Eω2)**2)*thresh)[0]
min_index = rows[0]
max_index = rows[-1]
phase_slice = phase[min_index-25:max_index+25]
om_slice = ω2[min_index-25:max_index+25]

plt.figure(2)
plt.plot(om_slice, phase_slice, label='Optimum after 1000 iterations', color='black')
plt.xlabel('Angular Frequency (/s)')
plt.ylabel('Phase')

print('(2) RMS width of optimum = {}'.format(rms_width(ω1, Iω1)))
plt.figure(1)
plt.plot(ω1, Iω1, label='Optimum after 1000 iterations', color='black')
plt.xlabel('Angular Frequency (/s)')
plt.ylabel('Intensity (a.u.)')

Et = np.fft.fftshift(np.fft.ifft(Eω2))
f_step = (ω2[1]-ω2[0])/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Eω2), d=f_step))
plt.figure(3)
plt.plot(t, np.abs(Et)**2, label='Optimum after 1000 iterations', color='black')
plt.xlabel('Time (s)')
plt.ylabel('Intensity (a.u.)')

# Plot the SPM optimum
grating_pair_displacement_in = 0
energy_in = 1.2e-3
pressure_in = 0.66*1.5

Main.energy = energy_in
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase

Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω1, Iω1 = Processing.getIω(duv, :ω, flength)")
ω1 = Main.ω1
Iω1 = Main.Iω1
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
ω2 = Main.ω2
Eω2 = Main.ω2
"""
header = ['Angular Frequency', 'Real Electric Field', 'Imaginary Electric Field']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\new_data\\analysis\\spectrum_data\\init.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    writer.writerow(header)
    for i in range(len(ω2)):
        writer.writerow([ω2[i], Eω2[i].real, Eω2[i].imag])
"""
om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, Eω2, lambda0)
thresh = 0.1
rows = np.where(np.abs(Eω2)**2 > max(np.abs(Eω2)**2)*thresh)[0]
min_index = rows[0]
max_index = rows[-1]
phase_slice = phase[min_index-25:max_index+25]
om_slice = ω2[min_index-25:max_index+25]

plt.figure(2)
plt.plot(om_slice, phase_slice, '--', label='SPM prediction', color='tab:red')
plt.legend(fontsize=16)
print('RMS width of SPM optimum = {}'.format(rms_width(ω1, Iω1)))
plt.figure(1)
plt.plot(ω1,Iω1, '--', label='SPM prediction', color='tab:red')
plt.legend(fontsize=16)

Et = np.fft.fftshift(np.fft.ifft(Eω2))
f_step = (ω2[1]-ω2[0])/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Eω2), d=f_step))
plt.figure(3)
plt.plot(t, np.abs(Et)**2, '--', label='SPM prediction', color='tab:red')
plt.legend(fontsize=16)

plt.show()