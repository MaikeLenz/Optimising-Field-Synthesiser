
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

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\test_pressure_gradients\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\test_pressure_gradients\\')
from compare_pressures import *

Main.using("Luna")
filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\pressure_distributions\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"Ar9pressure_points__init_50_niter_1000.csv")

energy=df_0.iloc[0][3]
radius=df_0.iloc[0][5]
flength=df_0.iloc[0][6]
FWHM=df_0.iloc[0][7]
wavel=df_0.iloc[0][8]
gas=df_0.iloc[0][9]
grating_pair_displacement=df_0.iloc[0][10]
pressures_str=df_0.iloc[0][4]

pressures=pressures_str.strip('][').split(', ')
print(pressures)
pressure_list=[[],[]]
for i in range(len(pressures)):
        #iterate through and append the corresponding z and p value
        #z:
        pressure_list[0].append(i*flength/(len(pressures)-1))
        
        #p:
        pressure_list[1].append(float(pressures[i]))
pressure_list_rev=pressure_list.copy()
pressure_list_rev[1]=pressure_list_rev[1][::-1]
pressure=tuple(tuple(sub) for sub in pressure_list)
pressure_rev=tuple(tuple(sub) for sub in pressure_list_rev)
print(pressure,pressure_rev)
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

###########################################################################################################################################################################
# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Pmax=1.5
Main.pressure = P_avg(pressure[0],pressure[1])
Main.??0 = wavel
Main.??fwhm = FWHM
Main.energy = energy

#print(pressure,energy,grating_pair_displacement)
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
t_opt2 = Main.t
Et_allz_opt2 = Main.Et # array of Et at all z 
Et_opt2 = Et_allz_opt2[:,-1] # last item in each element is pulse shape at the end
Et02=Et_allz_opt2[:,0] #first item in each element is pulse shape at the start

??_opt2 = Main.??
I??_opt2 = Main.I??
I??_opt2=I??_opt2.reshape(len(I??_opt2),)
omega_opt2=Main.??
Iomega_opt2=Main.I??
Iomega_opt2=Iomega_opt2.reshape((-1,))[0:500]
omega_opt2=omega_opt2[0:500]

####################################################################################################################################################

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
"""
if gas=="Ne":
    Main.pressure = 0.66*3
elif gas=="Ar":
    Main.pressure = 0.66*1.5
"""
#Main.pressure=max(pressure[1])
#print(max(pressure[1]))
Main.pressure=pressure_rev
Main.??0 = wavel
Main.??fwhm = FWHM
Main.energy = energy

#print(pressure_rev,energy,grating_pair_displacement)
domega = 2*np.pi*0.44/FWHM
c=299792458
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 1000)

GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=0)

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
t_opt3 = Main.t
Et_allz_opt3 = Main.Et # array of Et at all z 
Et_opt3 = Et_allz_opt3[:,-1] # last item in each element is pulse shape at the end
Et03=Et_allz_opt3[:,0] #first item in each element is pulse shape at the start

??_opt3 = Main.??
I??_opt3 = Main.I??
I??_opt3=I??_opt3.reshape(len(I??_opt3),)
omega_opt3=Main.??
Iomega_opt3=Main.I??
Iomega_opt3=Iomega_opt3.reshape((-1,))[0:500]
omega_opt3=omega_opt3[0:500]


print("Optimised")
print(rms_width(??_opt,I??_opt),max(abs(Et_opt)))
print("Max pressure")
print(rms_width(??_opt3,I??_opt3),max(abs(Et_opt3)))


#plotting
plt.figure()
#plt.plot(??,I??,label="SPM Prediction")

plt.plot(??_opt,I??_opt,label="Optimised")
#plt.plot(??_opt2,I??_opt2,label="Constant Pressure")
#plt.plot(??_opt3,I??_opt3,label="SPM Prediction")
plt.plot(??_opt3,I??_opt3,label="Reverse Pressure Distribution")

plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")
plt.legend()
plt.figure()
#plt.plot(omega,Iomega,label="SPM Prediction")

#plt.plot(width_plot,bar_height, label="rms width")
plt.plot(omega_opt,Iomega_opt,label="Optimised")
#plt.plot(omega_opt2,Iomega_opt2,label="Constant Pressure")
#plt.plot(omega_opt3,Iomega_opt3,label="SPM Prediction")
plt.plot(omega_opt3,Iomega_opt3,label="Reverse Pressure Distribution")

plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.figure()
#plt.plot(t,Et,label="SPM Prediction")


from scipy.integrate import simps
integral_opt=simps(np.abs(Et_opt),t_opt)
integral_max=simps(np.abs(Et_opt3),t_opt3)
print("optimised integral %s"%integral_opt)
print("max pressure integral %s"%integral_max)
plt.plot(t_opt,Et_opt,label="Optimised")
#plt.plot(t_opt2,Et_opt2,label="Constant Pressure")
#plt.plot(t_opt3,Et_opt3,label="SPM Prediction")
plt.plot(t_opt3,Et_opt3,label="Reverse Pressure Distribution")

#plt.plot(t,Et0,label="z=0m")
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()

##########################################################################################
#plot pressure distribution

plt.figure()
z,Pz=P_distribution(pressure[0],pressure[1])
plt.scatter(pressure[0],pressure[1])
plt.plot(z,Pz)
plt.xlabel("Position along the Fibre, m")
plt.ylabel("Pressure, bar")


plt.show()