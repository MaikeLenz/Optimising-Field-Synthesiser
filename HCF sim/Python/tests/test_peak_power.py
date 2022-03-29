import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from compressor_grating_to_values import *

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

"""
λ = np.linspace(100e-9, 1000e-9, 1000)
def Gauss(x, x0, sigma):
    return np.exp(-((x-x0)/sigma)**2)
Iλ = Gauss(λ, 800e-9, 100e-9)
plt.plot(λ, Iλ)
"""
# Load some data from a scan for testing
filepath = 'C:\\Users\\iammo\\Documents\\'
df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\good_data\\300nm_many_iters\\Optimal_Params_optimums.csv")
energy = df_iter.iloc[:,2] # J
pressure = df_iter.iloc[:,3] # bar
grating_pos = df_iter.iloc[:,6]

Main.radius = 175e-6
Main.flength = 1.05
Main.gas_str = "Ne"
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = 800e-9
Main.τfwhm = 30e-15

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
Main.ω = omega_list[::-1]
Main.Iω = intens[::-1]

results = []
grating_pair_displacement_in = grating_pos[999]
energy_in = energy[999]
Main.energy = energy_in
pressure_in = pressure[999]
Main.pressure = pressure_in
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement_in*1000)
phase = []
for j in range(len(omega_list)):
    phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/Main.λ0, CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
Main.phase = phase

Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
t = Main.t
"""
Et_allz = Main.Et # array of Et at all z 
Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
f, Ef = t_to_f(t, Et)
c = 299792458
λ = c/f
"""
plt.plot(λ, Iλ, label='Before smoothing')
#plt.plot(λ, Ef, label='Before smoothing')

# First smooth using super Gaussian filter
def superGauss(x,x0,sigma):
    return np.exp(-((x-x0)/sigma)**4)
filter = superGauss(λ, 800e-9, 800e-9*0.1)

Iλ_smooth = []
for i in range(len(Iλ)):
    Iλ_smooth.append(Iλ[i]*filter[i])
plt.plot(λ, Iλ_smooth, label='After smoothing')

"""
Ef_smooth = []
for i in range(len(Ef)):
    Ef_smooth.append(Ef[i]*filter[i])
plt.plot(λ, Ef_smooth, label='After smoothing')
"""
plt.legend()
# Now Fourier transform
c = 299792458
f = []
for i in range(len(λ)):
    f.append(c/λ[i])

t_filtered, I_filtered = f_to_t(f[::-1], Iλ_smooth[::-1])
#t_filtered, I_filtered = f_to_t(λ, Ef_smooth)
plt.figure()
plt.plot(t_filtered, I_filtered)
# Now find peak power in time-domain
plt.show()
print(max(I_filtered))