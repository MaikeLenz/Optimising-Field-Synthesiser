
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
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"\\new_data\\Ar.csv")

energy=float(df_0.iloc[0][3])
pressure=float(df_0.iloc[0][4])
radius=float(df_0.iloc[0][5])
flength=float(df_0.iloc[0][6])
FWHM=float(df_0.iloc[0][7])
wavel=float(df_0.iloc[0][8])
gas=df_0.iloc[0][9]
grating_pair_displacement=float(df_0.iloc[0][10])

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
omega = np.linspace(2*np.pi*c/wavel -5* domega/2, 2*np.pi*c/wavel + 5*domega/2, 1000)

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
 
# Get values


omega_opt=Main.??
Iomega_opt=Main.I??
Iomega_opt=Iomega_opt.reshape((-1,))
omega_opt=omega_opt

#######################################################################################################
#now calculate spm prediction

Main.energy=1.1e-3
Main.pressure=1*0.66
"""
# Calculations
# setting pressure to (0,pressure) means a gradient from zero up until given value
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, ??fwhm, energy, trange=400e-15, ??lims=(150e-9, 4e-6))')

#now extract datasets
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")
Main.eval('t, Et = Processing.getEt(duv)')

## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 
#assign python variables
?? = Main.??
I?? = Main.I??
t = Main.t
omega=Main.??
Iomega=Main.I??
Iomega=Iomega.reshape((-1,))[0:500]
omega=omega[0:500]

Et_allz=Main.Et #array of Et at all z 
Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
Et0=Et_allz[:,0] #first item in each element is pulse shape at the start
#note Et is complex

"""
#print(rms_width(??,I??))
domega = 2*np.pi*0.44/FWHM
omega = np.linspace(2*np.pi*c/wavel - 5*domega/2, 2*np.pi*c/wavel + 5*domega/2, 1000)
GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=0*1000)

E, ???? = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
I?? = np.abs(E)**2


Main.?? = omega
Main.I?? = I??  
Main.phase = ???? 
# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(??, I??, phase; energy, ??0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; ??0, pulses=pulse, trange=400e-15, ??lims=(150e-9, 4e-6))')
Main.eval("??, I?? = Processing.getI??(duv, :??, flength)")


omega2=Main.??
Iomega2=Main.I??
Iomega2=Iomega2.reshape((-1,))
omega2=omega2


#plotting

plt.figure()
#plt.plot(omega,Iomega,label="SPM Prediction")
plt.plot(omega2,Iomega2,label="SPM Prediction, width %s"%(rms_width(omega2,Iomega2)))

#plt.plot(width_plot,bar_height, label="rms width")
plt.plot(omega_opt,Iomega_opt,label="Optimised, width %s"%(rms_width(omega_opt,Iomega_opt)))
plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.show()
#{'target': 454.33147357060653, 'params': {'energy': 0.0010992847619322667, 'grating_pair_displacement': 3.937495614034377e-06, 'pressure': 0.6592512482937603}}
#{'target': 454.33147357060653, 'params': {'energy': 0.0010992847619322667, 'grating_pair_displacement': 3.937495614034377e-06, 'pressure': 0.6592512482937603}}