import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from Luna_subtarget import *
from compressor_grating_to_values import *

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\")
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\investigate_phase\\')
from get_phase import *

Main.using("Luna")

filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\new_data\\exp_input_Ar_freq_bandwidth_optimise_lab__init_50_niter_1000.csv"
import pandas as pd
df_0 = pd.read_csv(filepath)

energy=float(df_0.iloc[0][3])
pressure=float(df_0.iloc[0][4])
radius=float(df_0.iloc[0][5])
flength=float(df_0.iloc[0][6])
FWHM=float(df_0.iloc[0][7])
wavel=float(df_0.iloc[0][8])
gas=df_0.iloc[0][9]
grating_pair_displacement=float(df_0.iloc[0][10])

#import input spectra
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
#####################################################################################################################

lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]
with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=np.array(columns[0])
intens1_2=np.array(columns[1])

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = energy

print(pressure,energy,grating_pair_displacement)
c = 299792458 # m/s
omega_list=2*np.pi*c/(wavel_nm*10**-9)
Main.ω = omega_list[::-1]
Main.Iω = intens1_2[::-1]

# Plot the optimum found

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=(grating_pair_displacement)*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω = grid.ω")
Main.eval('Eω = duv["Eω"][:,end]')
Eom=Main.Eω
om=Main.ω


#now get SPM optimum
# Assign arguments to Main namespace
Main.pressure = 0.66*1.5
Main.energy = 1.2e-3

omega_list=2*np.pi*c/(wavel_nm*10**-9)
Main.ω = omega_list[::-1]
Main.Iω = intens1_2[::-1]

# Plot the optimum found

GDD=0
TOD=0
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("grid = Processing.makegrid(duv)")
Main.eval("ω2 = grid.ω")
Main.eval('Eω2 = duv["Eω"][:,end]')
Eom_spm=Main.Eω2
om_spm=Main.ω2


#plt bot on frequency axis
print(rms_width(om,np.abs(Eom)**2))
print(rms_width(om_spm,np.abs(Eom_spm)**2))
plt.figure()
plt.plot(om,np.abs(Eom)**2,label="Optimised",color="black")
plt.plot(om_spm,np.abs(Eom_spm)**2,label="SPM Prediction",linestyle="--",color="tab:red")
plt.xlabel("Angular frequency, rad/s",fontsize=20)
plt.ylabel("Intensity, a.u.",fontsize=20)
plt.legend(fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)



#analysis in time domain
om0 = moment(om,np.abs(Eom)**2,1)/moment(om,np.abs(Eom)**2,0) # Determine central frequency
c=299792458
lambda0 = (2*np.pi*c)/om0
phase=get_phase(om,Eom,lambda0)
thresh = 0.1
rows = np.where(np.abs(Eom)**2 > max(np.abs(Eom)**2)*thresh)[0]
min_index = rows[0]
max_index = rows[-1]

phase_slice = phase[min_index-25:max_index+25]
om_slice = om[min_index-25:max_index+25]

def quad(x, a, b, c):
    return a*(x**2) + b*x + c
quad_popt, _ = curve_fit(quad, om_slice, phase_slice, p0=[1,1,0])
phase_to_remove = quad(om_slice, *quad_popt)
new_phase = np.zeros(len(om))

for i in range(len(phase_to_remove)):
    new_phase[i+min_index-25] += phase_slice[i] - phase_to_remove[i]

# Add the phase back to the intensity profile
Eom_complex0 = [] # raw data
Eom_complex1 = [] # quad phase removed
Eom_complex2 = [] # phase zeroed
for i in range(len(om)):
    Eom_complex0.append(np.abs(Eom[i])*np.exp(-1j*phase[i]))
    Eom_complex1.append(np.abs(Eom[i])*np.exp(-1j*new_phase[i]))
    Eom_complex2.append(np.abs(Eom[i])*np.exp(-1j*0))

# Now Fourier transform
Et0 = np.fft.fftshift(np.fft.ifft(Eom_complex0))
f_step = (om[1]-om[0])/(2*np.pi)
t0 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex0), d=f_step))

Et1 = np.fft.fftshift(np.fft.ifft(Eom_complex1))
f_step = (om[1]-om[0])/(2*np.pi)
t1 = np.fft.fftshift(np.fft.fftfreq(len(Eom_complex1), d=f_step))

Et2 = np.fft.fftshift(np.fft.ifft(Eom_complex2))
f_step = (om[1]-om[0])/(2*np.pi)
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