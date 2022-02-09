import julia
import matplotlib.pyplot as plt
import sys
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from theoretical_width import theoretical_width

from julia import Main

Main.using("Luna")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
from rms_width import *
# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhms = np.linspace(5e-15,60e-15,100) # array of FWHM durations of the pump pulse
energy=0.5e-3

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = λ0
Main.energy = energy
widths=np.array([])

for i in τfwhms:
    print(i)
    Main.τfwhm = i

    # Calculations
    # setting pressure to (0,pressure) means a gradient from zero up until given value
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

    #now extract datasets
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    #Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    wavel = Main.λ
    I = Main.Iλ
    width=rms_width(wavel,I)
    widths=np.append(widths,width)
"""
plt.scatter(τfwhms/10**(-15),widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel("Pulse duration, fs")
plt.show()
"""
plt.scatter(τfwhms/10**(-15),widths, marker="+", label='Luna')

theor_widths = []
for i in range(len(τfwhms)):
    theor_widths.append(theoretical_width(radius, flength, pressure, λ0, τfwhms[i], energy))
plt.scatter(τfwhms/10**(-15),theor_widths, marker="+", label='Theoretical')
plt.ylabel("angular frequency width, /s")
plt.xlabel('Pulse duration, fs')
plt.legend()
plt.show()