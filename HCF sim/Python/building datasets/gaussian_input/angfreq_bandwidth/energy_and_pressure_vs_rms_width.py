import julia
import matplotlib.pyplot as plt
import csv  
import sys

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\")
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *
from rms_width import *
from theoretical_width import theoretical_width

# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressures =  np.linspace(1,15,20)# gas pressure in bar, corresponds to 66% of final pressure in atm
λ0 = 800e-9 # central wavelength of the pump pulse
energies = np.linspace(0.1e-3,2e-3,20) # array of energies in the pump pulse
τfwhm = 30e-15 # FWHM durations of the pump pulse

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.τfwhm = τfwhm
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = λ0
widths=np.zeros((len(energies),len(pressures)))

print('Assigned values, starting search')
for i in range(len(energies)):
    Main.energy = energies[i]
    print(energies[i])
    for j in range(len(pressures)):
        print(pressures[j])
        Main.pressure = pressures[j]
        # Calculations
        # setting pressure to (0,pressure) means a gradient from zero up until given value

        # Run the optimisation using Gaussian input pulse
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
        
        """
        # New: run using custom pulse - cannot find the correct range to prevent CSpine errors
        c = 299792458 # m/s
        domega = 2e15
        omega = np.linspace(2*np.pi*c/λ0 - domega/2, 2*np.pi*c/λ0 + domega/2, 100)

        E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
        Iω = np.abs(E**2)

        Main.ω = omega
        Main.Iω = Iω  
        Main.phase = ϕω 
        # Pass data to Luna
        Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
        """

        #now extract datasets
        Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
        #Main.eval('t, Et = Processing.getEt(duv)')

        ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
        # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
        # subsequently would be the inputs the the BO 
        #assign python variables
        ω = Main.ω
        Iω = Main.Iω
        width=rms_width(ω,Iω)
        widths[i][j]=width

plt.imshow(widths, extent=(np.amin(pressures), np.amax(pressures),np.amin(energies)*10**3, np.amax(energies)*10**3), aspect = 'auto', origin="lower")
plt.xlabel("Pressure, bar")
plt.ylabel("Pulse energy, mJ")
#legend
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)
plt.show()

"""
# Calculate theoretical widths
theor_widths = np.zeros((len(energies),len(pressures)))
for i in range(len(energies)):
    for j in range(len(pressures)):
        theor_widths[i][j] = theoretical_width(radius, flength, pressures[j], λ0, τfwhm, energies[i])
"""

"""
# Save the data
header = ['Pressure, bar', 'Pulse energy, mJ', 'Simulated Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\energy_and_pressure_vs_rms_width_custom_pulse.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(energies)):
        for j in range(len(pressures)):
            writer.writerow([pressures[j], energies[i]*(10**3), widths[i][j]])
"""