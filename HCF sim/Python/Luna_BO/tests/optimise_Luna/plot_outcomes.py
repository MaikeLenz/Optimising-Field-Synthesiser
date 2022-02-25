import pandas as pd
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

filepath = 'C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\'

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

# Read optimal params
df_0 = pd.read_csv(filepath+"random_init_0_niter_0.csv")
width_0 = df_0.iloc[:,2][0]
df_100 = pd.read_csv(filepath+"init_100_niter_100.csv")
width_100 = df_100.iloc[:,2][0]
#axs_Ne_powers[2,1].plot(df.iloc[:,0], df.iloc[:,1], label='Simulation with Experimental input')

# Pass into Luna
# Random pulse
Main.radius = df_0.iloc[:,5][0]
Main.flength = df_0.iloc[:,6][0]
Main.gas_str = df_0.iloc[:,9][0]
Main.eval("gas = Symbol(gas_str)")
Main.pressure = df_0.iloc[:,4][0]
Main.λ0 = df_0.iloc[:,8][0]
Main.τfwhm = df_0.iloc[:,7][0]
Main.energy = df_0.iloc[:,3][0]

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ_0 = Main.λ
Iλ_0 = Main.Iλ  
t_0 = Main.t
Et_allz_0 = Main.Et # array of Et at all z 
Et_0 = Et_allz_0[:,-1] # last item in each element is pulse shape at the end
Et0_0=Et_allz_0[:,0] #first item in each element is pulse shape at the start

# Optimised pulse
Main.radius = df_100.iloc[:,5][0]
Main.flength = df_100.iloc[:,6][0]
Main.gas_str = df_100.iloc[:,9][0]
Main.eval("gas = Symbol(gas_str)")
Main.pressure = df_100.iloc[:,4][0]
Main.λ0 = df_100.iloc[:,8][0]
Main.τfwhm = df_100.iloc[:,7][0]
Main.energy = df_100.iloc[:,3][0]

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
λ_100 = Main.λ
Iλ_100 = Main.Iλ  
t_100 = Main.t
Et_allz_100 = Main.Et # array of Et at all z 
Et_100 = Et_allz_100[:,-1] # last item in each element is pulse shape at the end
Et0_100=Et_allz_100[:,0] #first item in each element is pulse shape at the start

# Plot results
"""
plt.figure()
plt.plot(t_0, Et0_0)
plt.xlabel('Time, s')
plt.ylabel('Electric Field')
plt.title('Random Pulse Input')

plt.figure()
plt.plot(t_0, Et_0)
plt.xlabel('Time, s')
plt.ylabel('Electric Field')
plt.title('Random Pulse Output')

plt.figure()
plt.plot(t_100, Et0_100)
plt.xlabel('Time, s')
plt.ylabel('Electric Field')
plt.title('Optimised Input Pulse')

plt.figure()
plt.plot(t_100, Et_100)
plt.xlabel('Time, s')
plt.ylabel('Electric Field')
plt.title('Optimised Output Pulse')

plt.figure()
plt.plot(λ_0, Iλ_0, label = str(width_0*(10**9))+ 'nm')
plt.xlabel('Wavelength, nm')
plt.ylabel('Intensity')
plt.title('Random Output Pulse')
plt.legend()

plt.figure()
plt.plot(λ_100, Iλ_100, label = str(width_100*(10**9))+ 'nm')
plt.xlabel('Wavelength, nm')
plt.ylabel('Intensity')
plt.title('Optimised Output Pulse')
plt.legend()

plt.show()
"""

plt.figure()
plt.plot(λ_0*(10**9), Iλ_0, label = 'Random, Δλ = ' + str(round(width_0*(10**9))) + 'nm', color='tab:blue')
plt.plot(λ_100*(10**9), Iλ_100, label = 'Optimised, Δλ = ' + str(round(width_100*(10**9))) + 'nm', color='tab:orange')
plt.xlabel('Wavelength, nm', fontsize=22)
plt.ylabel('Intensity', fontsize=24)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.title('Optimised Output Pulse')
plt.xlim((200,2000))
plt.legend(fontsize=26)

"""
#creating indicative bar to show rms width
λ_0 = λ_0*(10**9)
λ_100 = λ_100*(10**9)
width_0=rms_width(λ_0, Iλ_0)
print(width_0)
centre=moment(λ_0, Iλ_0,1)/moment(λ_0, Iλ_0,0)
height=moment(λ_0, Iλ_0,1)/moment(λ_0, Iλ_0,0)
width_plot=np.array([centre-0.5*width_0,centre+0.5*width_0])
bar_height=np.array([height,height])
plt.plot(width_plot,bar_height, color='tab:purple')

width_100=rms_width(λ_100, Iλ_100)
print(width_100)
centre=moment(λ_100, Iλ_100,1)/moment(λ_100, Iλ_100,0)
height=moment(λ_100, Iλ_100,1)/moment(λ_100, Iλ_100,0)
width_plot=np.array([centre-0.5*width_100,centre+0.5*width_100])
bar_height=np.array([height,height])
plt.plot(width_plot,bar_height, color='tab:orange')
"""

plt.show()