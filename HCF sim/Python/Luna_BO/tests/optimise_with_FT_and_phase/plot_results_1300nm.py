import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
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

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\Optimise_with_Fourier_Transforms\\')
from envelopes import *

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
filepath = 'C:\\Users\\iammo\\Documents\\'
##################################################################################
# Define fixed params
Main.gas_str = "He"
Main.eval("gas = Symbol(gas_str)")
λ0 = 800e-9
Main.λ0 = λ0
τfwhm = 30e-15
##################################################################################
# Plot the optimum found
grating_pair_displacement_in = 2.804851414292173e-06
energy_in = 0.001302412924828062
pressure_in = 4.826106823831891
radius_in = 0.0001869238808711249
flength_in = 5.255003046515194
Main.energy = energy_in
Main.pressure = pressure_in
Main.radius = radius_in
Main.flength = flength_in

domega = 2*np.pi*0.44/τfwhm
c=299792458
omega = np.linspace(2*np.pi*c/λ0 - 5*domega/2, 2*np.pi*c/λ0 + 5*domega/2, 1000)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                
Main.duv = Main.eval('duv2 = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')
λ1 = Main.λ
Iλ1 = Main.Iλ
ω2 = Main.ω
Eω2 = Main.Eω
λ2 = 2*np.pi*c/ω2

om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, Eω2, lambda0)

f, axs = plt.subplots(1,2)
axs[0].plot(λ1*(10**9), Iλ1, label='Optimum after 1000 iterations', color='black')
axs[0].set_xlabel('Wavelength (nm)')
axs[0].set_ylabel('Intensity (a.u.)')

filter = []
for i in range(len(λ2)):
    filter.append(np.exp(-((λ2[i]-1300e-9)/(1300e-9*0.2))**4))
#filter = superGauss(λ22, 1300e-9, 1300e-9*0.2)
Eom_smooth = []
for i in range(len(Eω2)):
    Eom_smooth.append(Eω2[i]*filter[i])

axs2 = plt.twinx(axs[1])
axs[1].plot(λ2*(10**9), np.abs(Eom_smooth)**2, color='black')
axs[1].set_xlabel('Wavelength (nm)')
axs[1].set_ylabel('Intensity (a.u.)')

header = ['Angular Frequency', 'Real Electric Field', 'Imaginary Electric Field']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_with_FT_and_phase\\spectrum_data\\1300nm_optimum.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    writer.writerow(header)
    for i in range(len(ω2)):
        writer.writerow([ω2[i], Eω2[i].real, Eω2[i].imag])
##################################################################################
# Get pulse in time-domain
# Slice phase to only select part within pulse
thresh = 0.1
rows = np.where(np.abs(Eom_smooth)**2 > max(np.abs(Eom_smooth)**2)*thresh)[0]

min_index = rows[0]
max_index = rows[-1]
phase_slice = phase[min_index-25:max_index+25]
om_slice = ω2[min_index-25:max_index+25]
lambda_slice = 2*np.pi*c/om_slice
axs2.plot(lambda_slice*(10**9), phase_slice, '--', color='black')
axs2.set_ylabel('Phase')

# Fit a quadratic to the phase and remove this
def quad(x, a, b, c):
    return a*(x**2) + b*x + c
quad_popt, _ = curve_fit(quad, om_slice, phase_slice, p0=[1,1,0])
phase_to_remove = quad(om_slice, *quad_popt)
new_phase = np.zeros(len(ω2))
old_phase = np.zeros(len(ω2))
for i in range(len(phase_to_remove)):
    new_phase[i+min_index-25] += phase_slice[i] - phase_to_remove[i]
    old_phase += phase_slice[i]

# Add the phase back to the intensity profile
Eom_complex = []
for i in range(len(ω2)):
    Eom_complex.append(np.abs(Eom_smooth[i])*np.exp(-1j*new_phase[i]))
Eom_Lunaphase = []
for i in range(len(ω2)):
    Eom_Lunaphase.append(np.abs(Eom_smooth[i])*np.exp(-1j*old_phase[i]))

# Now Fourier transform
Et = np.fft.fftshift(np.fft.ifft(Eom_complex))
f_step = (omega[1]-omega[0])/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex), d=f_step))

Et_zerophase = np.fft.fftshift(np.fft.ifft(Eom_smooth))
f_step = (omega[1]-omega[0])/(2*np.pi)
t_zerophase = np.fft.fftshift(np.fft.fftfreq(len(Eom_smooth), d=f_step))

Et_Lunaphase = np.fft.fftshift(np.fft.ifft(Eom_Lunaphase))
f_step = (omega[1]-omega[0])/(2*np.pi)
t_Lunaphase = np.fft.fftshift(np.fft.fftfreq(len(Eom_Lunaphase), d=f_step))

f2, axst = plt.subplots()
axst.plot(t, np.abs(Et)**2, color='black', label='Optimum after 1000 iterations')
axst.set_xlabel('Time (s)')
axst.set_ylabel('Intensity (a.u.)')
axst.set_title('Pulse in Time-Domain with Quadratic Phase Subtracted')

f22, axst2 = plt.subplots()
axst2.plot(t_zerophase, np.abs(Et_zerophase)**2, color='black', label='Optimum after 1000 iterations')
axst2.set_xlabel('Time (s)')
axst2.set_ylabel('Intensity (a.u.)')
axst2.set_title('Transform Limited Pulse in Time-Domain')

f23, axst3 = plt.subplots()
axst3.plot(t_Lunaphase, np.abs(Et_Lunaphase)**2, color='black', label='Optimum after 1000 iterations')
axst3.set_xlabel('Time (s)')
axst3.set_ylabel('Intensity (a.u.)')
axst3.set_title('Pulse in Time-Domain before Chirped Mirrors')

duration_opt_phasesubtracted = rms_width(t, np.abs(Et)**2)
duration_opt_zerophase = rms_width(t_zerophase, np.abs(Et_zerophase)**2)
duration_opt_Lunaphase = rms_width(t_Lunaphase, np.abs(Et_Lunaphase)**2)

##################################################################################
# Plot the optimum after the random search
grating_pair_displacement_in = 5.8689828445751676e-05
energy_in = 0.0011704675101784023
pressure_in = 1.30858765630998
radius_in = 0.00013914567008819546
flength_in = 4.231317543434557
Main.energy = energy_in
Main.pressure = pressure_in
Main.radius = radius_in
Main.flength = flength_in

domega = 2*np.pi*0.44/τfwhm
c=299792458
omega = np.linspace(2*np.pi*c/λ0 - 5*domega/2, 2*np.pi*c/λ0 + 5*domega/2, 1000)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
Iω = np.abs(E)**2

Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω 
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                
Main.duv = Main.eval('duv2 = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')
λ1 = Main.λ
Iλ1 = Main.Iλ
ω2 = Main.ω
Eω2 = Main.Eω
λ2 = 2*np.pi*c/ω2

om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, Eω2, lambda0)

axs[0].plot(λ1*(10**9), Iλ1, label='Optimum after random search', color='tab:red')
axs[0].legend(fontsize=16)

filter = []
for i in range(len(λ2)):
    filter.append(np.exp(-((λ2[i]-1300e-9)/(1300e-9*0.2))**4))
#filter = superGauss(λ22, 1300e-9, 1300e-9*0.2)
Eom_smooth = []
for i in range(len(Eω2)):
    Eom_smooth.append(Eω2[i]*filter[i])

axs[1].plot(λ2*(10**9), np.abs(Eom_smooth)**2, color='tab:red')

header = ['Angular Frequency', 'Real Electric Field', 'Imaginary Electric Field']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_with_FT_and_phase\\spectrum_data\\1300nm_init.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) # peak_power_1000e-9wavelwindow__init_50_niter_100
    writer.writerow(header)
    for i in range(len(ω2)):
        writer.writerow([ω2[i], Eω2[i].real, Eω2[i].imag])
##################################################################################
# Get pulse in time-domain
# Slice phase to only select part within pulse
thresh = 0.1
rows = np.where(np.abs(Eom_smooth)**2 > max(np.abs(Eom_smooth)**2)*thresh)[0]

min_index = rows[0]
max_index = rows[-1]
phase_slice = phase[min_index-25:max_index+25]
om_slice = ω2[min_index-25:max_index+25]
lambda_slice = 2*np.pi*c/om_slice
axs2.plot(lambda_slice*(10**9), phase_slice, '--', color='black')
axs2.set_ylabel('Phase')

# Fit a quadratic to the phase and remove this
def quad(x, a, b, c):
    return a*(x**2) + b*x + c
quad_popt, _ = curve_fit(quad, om_slice, phase_slice, p0=[1,1,0])
phase_to_remove = quad(om_slice, *quad_popt)
new_phase = np.zeros(len(ω2))
old_phase = np.zeros(len(ω2))
for i in range(len(phase_to_remove)):
    new_phase[i+min_index-25] += phase_slice[i] - phase_to_remove[i]
    old_phase += phase_slice[i]

# Add the phase back to the intensity profile
Eom_complex = []
for i in range(len(ω2)):
    Eom_complex.append(np.abs(Eom_smooth[i])*np.exp(-1j*new_phase[i]))
Eom_Lunaphase = []
for i in range(len(ω2)):
    Eom_Lunaphase.append(np.abs(Eom_smooth[i])*np.exp(-1j*old_phase[i]))

# Now Fourier transform
Et = np.fft.fftshift(np.fft.ifft(Eom_complex))
f_step = (omega[1]-omega[0])/(2*np.pi)
t = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex), d=f_step))

Et_zerophase = np.fft.fftshift(np.fft.ifft(Eom_smooth))
f_step = (omega[1]-omega[0])/(2*np.pi)
t_zerophase = np.fft.fftshift(np.fft.fftfreq(len(Eom_smooth), d=f_step))

Et_Lunaphase = np.fft.fftshift(np.fft.ifft(Eom_Lunaphase))
f_step = (omega[1]-omega[0])/(2*np.pi)
t_Lunaphase = np.fft.fftshift(np.fft.fftfreq(len(Eom_Lunaphase), d=f_step))

axst.plot(t, np.abs(Et)**2, color='tab:red', label='Optimum after random search')
axst.legend(fontsize=16)

axst2.plot(t_zerophase, np.abs(Et_zerophase)**2, color='tab:red', label='Optimum after random search')
axst2.legend(fontsize=16)

axst3.plot(t_Lunaphase, np.abs(Et_Lunaphase)**2, color='tab:red', label='Optimum after random search')
axst3.legend(fontsize=16)

duration_init_phasesubtracted = rms_width(t, np.abs(Et)**2)
duration_init_zerophase = rms_width(t_zerophase, np.abs(Et_zerophase)**2)
duration_init_Lunaphase = rms_width(t_Lunaphase, np.abs(Et_Lunaphase)**2)
##################################################################################
print('Optimised duration with phase subtracted = {}'.format(duration_opt_phasesubtracted*(10**15)))
print('Optimised duration with zero phase = {}'.format(duration_opt_zerophase*(10**15)))
print('Optimised duration with Luna phase = {}'.format(duration_opt_Lunaphase*(10**15)))
print('Random search duration with phase subtracted = {}'.format(duration_init_phasesubtracted*(10**15)))
print('Random search duration with zero phase = {}'.format(duration_init_zerophase*(10**15)))
print('Random search duration with Luna phase = {}'.format(duration_init_Lunaphase*(10**15)))

plt.show()