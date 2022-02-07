import julia
import matplotlib.pyplot as plt

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

from rms_width import *
# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressures =  np.linspace(1.,15.,20)# gas pressure in bar, corresponds to 66% of final pressure in atm
λ0 = 800e-9 # central wavelength of the pump pulse
energies = np.linspace(0.1e-3,2.0e-3,20) # array of energies in the pump pulse
τfwhm = 30e-15 # FWHM durations of the pump pulse

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.τfwhm = τfwhm
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = λ0
widths=np.zeros((len(energies),len(pressures)))

for i in range(len(energies)):
    Main.energy = energies[i]
    print(energies[i])
    for j in range(len(pressures)):
        print(pressures[j])
        Main.pressure = pressures[j]
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
        widths[i][j]=width

plt.imshow(widths, extent=(np.amin(pressures)*10**15, np.amax(pressures)*10**15,np.amin(energies)*10**3, np.amax(energies)*10**3), aspect = 'auto', origin="lower")
plt.xlabel("Pressure, bar")
plt.ylabel("Pulse energy, mJ")
#legend
cbar = plt.colorbar()
cbar.ax.set_ylabel('angular frequency bandwidth', rotation=270, labelpad=15)
plt.show()
