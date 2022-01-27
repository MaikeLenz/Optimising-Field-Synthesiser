
import julia
#from julia.api import Julia


julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin")

from julia import Main

Main.using("Luna")

# Arguments
radius = 125e-6 # HCF core radius
flength = 3 # HCF length
gas = "Ar"
pressure = 80e-3 # gas pressure in bar
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 10e-15 # FWHM duration of the pump pulse
energy = 60e-6 # energy in the pump pulse

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
Main.duv = Main.eval('prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, modes=4, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval('dumps = duv["dumps"]')
dumps = Main.dumps

#Main.eval("t, Et, zactual = Processing.getEt(duv)")
#%%
Main.eval("t, Et = Processing.getEt(duv)")

## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
# Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
# subsequently would be the inputs the the BO 

# These print out t, Et and zactual at the moment, which fills the terminal. The first step is to mute this printing (perhaps a kwarg in eval?)

Main.eval("t[0:10]")

t = Main.t
Et = Main.Et
zactual = Main.zactual

print(t[0:10])
print(Et[0:10])
print(zactual[0:10])