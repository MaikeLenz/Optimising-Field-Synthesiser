
import julia
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from Luna_subtarget import *
from compressor_grating_to_values import *

Main.using("Luna")
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\He_longwavel\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"\\peak_power_1.3e-06_wavelwindow__init_50_niter_1000.csv")

energy=df_0.iloc[0][3]
pressure=df_0.iloc[0][4]
radius=df_0.iloc[0][5]
flength=df_0.iloc[0][6]
FWHM=df_0.iloc[0][7]
wavel=df_0.iloc[0][8]
gas=df_0.iloc[0][9]
grating_pair_displacement=df_0.iloc[0][10]

#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.??0 = wavel
Main.??fwhm = FWHM
Main.energy = energy

print(pressure,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 1000)

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

E, ???? = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
I?? = np.abs(E)**2


Main.?? = omega
Main.I?? = I??  
Main.phase = ???? 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
    
# Get values
t_opt = Main.t
Et_allz_opt = Main.Et # array of Et at all z 
Et_opt = Et_allz_opt[:,-1] # last item in each element is pulse shape at the end
Et0=Et_allz_opt[:,0] #first item in each element is pulse shape at the start

??_opt = Main.??
I??_opt = Main.I??
I??_opt=I??_opt.reshape(len(I??_opt),)
omega_opt=Main.??
Iomega_opt=Main.I??
Iomega_opt=Iomega_opt.reshape((-1,))[0:500]
omega_opt=omega_opt[0:500]


#plotting
plt.figure()
#plt.plot(??,I??,label="SPM Prediction")

plt.plot(??_opt,I??_opt,label="Optimised")
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")
plt.legend()
plt.figure()
#plt.plot(omega,Iomega,label="SPM Prediction")

#plt.plot(width_plot,bar_height, label="rms width")
plt.plot(omega_opt,Iomega_opt,label="Optimised")
plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.figure()
#plt.plot(t,Et,label="SPM Prediction")

plt.plot(t_opt,Et_opt,label="Optimised")
#plt.plot(t,Et0,label="z=0m")
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()
plt.show()