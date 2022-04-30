import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['axes.labelsize'] = 20

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *
from rms_width import *
from theoretical_width import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
#filepath = 'C:\\Users\\iammo\\Documents\\'
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\"
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

wavel_nm_raw = np.array(columns[0])
wavel_nm=[]
for i in wavel_nm_raw:
    wavel_nm.append(i)
wavel_nm=np.array(wavel_nm)
intens = np.array(columns[2])
omega_list=2*np.pi*c/(wavel_nm*10**-9)
Main.ω = omega_list[::-1]
Main.Iω = intens[::-1]

# Plot the optimum found

Main.energy = 0.0011730020668117554
Main.pressure = 0.9896159222064448
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=(1.3687440750850062e-05)*1000)
phase_in = []
for j in range(len(omega_list)):
    phase_in.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase_in

Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω1, Iω1 = Processing.getIω(duv, :ω, flength)")
ω1 = Main.ω1
Iω1 = Main.Iω1
Iω1=Iω1.reshape((-1,))
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
ω2 = Main.ω2
Eω2 = Main.ω2

om0 = moment(ω2,np.abs(Eω2)**2,1)/moment(ω2,np.abs(Eω2)**2,0) # Determine central frequency
lambda0 = (2*np.pi*c)/om0
phase = get_phase(ω2, ω2, lambda0)
thresh = 0.1
rows = np.where(np.abs(Eω2)**2 > max(np.abs(Eω2)**2)*thresh)[0]
min_index = rows[0]
max_index = rows[-1]
phase_slice = phase[min_index-25:max_index+25]
om_slice = ω2[min_index-25:max_index+25]


width=rms_width(ω1,Iω1)
centre=moment(ω1,Iω1,1)/moment(ω1,Iω1,0)
height=moment(Iω1,ω1,1)/moment(Iω1,ω1,0)
width_plot=np.array([centre-0.5*width,centre+0.5*width])
bar_height=np.array([height,height])

plt.figure(2)
plt.plot(om_slice, phase_slice, label="Optimised", color='black')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Phase')

print('(2) RMS width of optimum = {}'.format(rms_width(ω1, Iω1)))
plt.figure(1)
#plt.plot(width_plot,bar_height,color="black",lw=2.5)
plt.plot(ω1, Iω1, label='Optimum, width %s $\mathrm{x} 10^{13} \mathrm{rad/s}$'%(round(width*10**(-13),1)), color='black')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Intensity (a. u.)')
##########################################################################################################################
# Plot the SPM optimum
grating_pair_displacement_in = 0
energy_in = 1.2e-3
pressure_in = 0.66*1.5

Main.energy = energy_in
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase_in_spm = []
for j in range(len(omega_list)):
    phase_in_spm.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase_in_spm

Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("ω1, Iω1 = Processing.getIω(duv, :ω, flength)")
ω1_spm = Main.ω1
Iω1_spm = Main.Iω1
Iω1_spm=Iω1_spm.reshape((-1,))

Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
ω2_spm = Main.ω2
Eω2_spm = Main.ω2

om0_spm = moment(ω2_spm,np.abs(Eω2_spm)**2,1)/moment(ω2_spm,np.abs(Eω2_spm)**2,0) # Determine central frequency
lambda0_spm = (2*np.pi*c)/om0_spm
phase_spm = get_phase(ω2_spm, Eω2_spm, lambda0_spm)
thresh = 0.1
rows = np.where(np.abs(Eω2_spm)**2 > max(np.abs(Eω2_spm)**2)*thresh)[0]
min_index = rows[0]
max_index = rows[-1]
phase_slice_spm = phase_spm[min_index-25:max_index+25]
om_slice_spm = ω2_spm[min_index-25:max_index+25]


width_spm=rms_width(ω1_spm,Iω1_spm)
centre_spm=moment(ω1_spm,Iω1_spm,1)/moment(ω1_spm,Iω1_spm,0)
height_spm=moment(Iω1_spm,ω1_spm,1)/moment(Iω1_spm,ω1_spm,0)
width_plot_spm=np.array([centre_spm-0.5*width_spm,centre_spm+0.5*width_spm])
bar_height_spm=np.array([height_spm,height_spm])

plt.figure(2)
plt.plot(om_slice_spm, phase_slice_spm, '--', label='SPM prediction', color='m')
plt.legend(fontsize=18)
print('RMS width of SPM optimum = {}'.format(rms_width(ω1_spm, Iω1_spm)))
plt.figure(1)
#plt.plot(width_plot_spm,bar_height_spm,"--",color="m",lw=2.5)
plt.plot(ω1_spm,Iω1_spm, '--', label='SPM prediction, width %s $\mathrm{x} 10^{13} \mathrm{rad/s}$'%(round(width_spm*10**(-13),1)), color='m')
plt.fill_between((2*np.pi*c)/(wavel_nm*10**(-9)),max(Iω1_spm)*intens/max(intens),color="lightgray")
print("ratio=",width/width_spm)
print("ratioE=",rms_width(ω2,np.abs(Eω2)**2)/rms_width(ω2_spm,np.abs(Eω2_spm)**2))
plt.legend(fontsize=18)


#analysis in time domain

def quad(x, a, b, c):
    return a*(x**2) + b*x + c

quad_popt, _ = curve_fit(quad, om_slice, phase_slice, p0=[1,1,0])
phase_to_remove = quad(om_slice, *quad_popt)
new_phase = np.zeros(len(ω2))

for i in range(len(phase_to_remove)):
    new_phase[i+min_index-25] += phase_slice[i] - phase_to_remove[i]

# Add the phase back to the intensity profile
Eom_complex0 = [] # raw data
Eom_complex1 = [] # quad phase removed
Eom_complex2 = [] # phase zeroed
for i in range(len(ω2)):
    Eom_complex0.append(np.abs(Eω2[i])*np.exp(1j*phase[i]))
    Eom_complex1.append(np.abs(Eω2[i])*np.exp(1j*new_phase[i]))
    Eom_complex2.append(np.abs(Eω2[i])*np.exp(1j*0))

# Now Fourier transform
Et0 = np.fft.fftshift(np.fft.ifft(Eom_complex0))
f_step = (ω2[1]-ω2[0])/(2*np.pi)
t0 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex0), d=f_step))

Et1 = np.fft.fftshift(np.fft.ifft(Eom_complex1))
f_step = (ω2[1]-ω2[0])/(2*np.pi)
t1 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex1), d=f_step))

Et2 = np.fft.fftshift(np.fft.ifft(Eom_complex2))
f_step = (ω2[1]-ω2[0])/(2*np.pi)
t2 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex2), d=f_step))
plt.figure()
plt.plot(t0*1e15, np.abs(Et0)**2, label="raw data")
plt.title(filepath)
plt.plot(t1*1e15, np.abs(Et1)**2, label="quad phase subtracted")
plt.plot(t2*1e15, np.abs(Et2)**2, label="zeroed phase")
plt.title(filepath)
plt.xlabel("time (fs)")
plt.ylabel("Intensity (arb.units)")
plt.legend()
plt.show()
