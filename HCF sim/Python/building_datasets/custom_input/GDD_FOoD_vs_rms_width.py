import julia
import matplotlib.pyplot as plt
import csv  
import sys

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
c = 299792458 # m/s

# Define custom pulse in frequency domain
energy = 0.5e-3
wavel = 800e-9
τfwhm = 30e-15 # FWHM duration of the pump pulse
domega = (0.44/τfwhm)*2*np.pi
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)
GDDs = np.linspace(-300*(10**-30), 700*(10**-30), 20) #GDD in s^2
FoODs = np.linspace(-66000*(10**-60), 112000*(10**-60), 20) #FoOD in s^4
Main.energy = energy
Main.λ0 = wavel

# Define experimental params
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure

widths=np.zeros((len(GDDs),len(FoODs)))
for i in range(len(GDDs)):
    for j in range(len(FoODs)):
        print(i)
        print(j)
        E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=GDDs[i], TOD=0, FoOD=FoODs[j])
        Iω = np.abs(E**2)
        Main.ω = omega
        Main.Iω = Iω  
        Main.phase = ϕω

        # Calculations
        # setting pressure to (0,pressure) means a gradient from zero up until given value
        Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
        
        #now extract datasets
        Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
        Main.eval('t, Et = Processing.getEt(duv)')

        ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
        # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
        # subsequently would be the inputs the the BO 
        #assign python variables
        ω = Main.ω
        Iω = Main.Iω
        width=rms_width(ω,Iω)
        widths[i][j]=width

plt.imshow(widths, extent=(np.amin(GDDs)*10**30, np.amax(GDDs)*10**30,np.amin(FoODs)*10**60, np.amax(FoODs)*10**60), aspect = 'auto', origin="lower")
plt.xlabel("GDD, fs^2")
plt.ylabel("FoOD, fs^4")
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)
plt.show()


# Save the data
header = ['GDD, fs^2', 'FoOD, fs^4', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\custom_input\\data\\GDD_and_FoOD_vs_rms_width.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    for i in range(len(GDDs)):
        for j in range(len(FoODs)):
            writer.writerow([GDDs[i]*10**30, FoODs[j]*10**60, widths[i][j]])