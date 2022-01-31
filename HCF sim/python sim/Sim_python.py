
import julia
#from julia.api import Julia


julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin")

from julia import Main

Main.using("Luna")

# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy = 0.5e-3 # energy in the pump pulse, 0.5mJ

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

# Calculations
# setting pressure to (0,pressure) means a gradient from zero up until given value
#Main.duv = Main.eval('prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, modes=4, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.duv = Main.eval('output=prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval('dumps = duv["dumps"]')
dumps = Main.dumps

Main.eval("t, Et, zactual = Processing.getEt(dumps)")
#Main.eval('t, Et, zactual = Processing.getEt(output["Eω"])')

## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 

# These print out t, Et and zactual at the moment, which fills the terminal. The first step is to mute this printing (perhaps a kwarg in eval?)

#Main.eval("t[0:10]")

t = Main.t
Et = Main.Et
zactual = Main.zactual


print(Main)
print(t[0:10])
print(Et[0:10])
print(zactual[0:10])