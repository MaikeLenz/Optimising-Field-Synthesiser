import julia
import matplotlib.pyplot as plt
#plt.rcParams['text.usetex'] = True

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

from rms_width import *
# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of final pressure in atm
λ0s = np.linspace(500e-9,1000e-9,100) # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy=0.5e-3

# Assign arguments to Main namespace
Main.flength = flength
Main.pressure = pressure
Main.radius = radius
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.τfwhm = τfwhm
Main.energy = energy
widths=np.array([])

for i in λ0s:
    print(i)
    Main.λ0 = i
    # Calculations
    # setting pressure to (0,pressure) means a gradient from zero up until given value
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

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
    widths=np.append(widths,width)

plt.scatter(λ0s*10**9,widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel('Wavelength, nm')
plt.show()