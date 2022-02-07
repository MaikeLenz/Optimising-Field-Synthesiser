import julia
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('text', usetex = True)
matplotlib.rc('font', **{'family':"sans-serif"})
params = {'text.latex.preamble': [r'\usepackage{siunitx}', 
    r'\usepackage{sfmath}', r'\sisetup{detect-family = true}',
    r'\usepackage{amsmath}']}   
plt.rcParams.update(params)

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

from rms_width import *
# Arguments
radius = np.linspace(50e-6,500e-6,2) # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of final pressure in atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy=0.5e-3

# Assign arguments to Main namespace
Main.flength = flength
Main.pressure = pressure

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.τfwhm = τfwhm
Main.λ0 = λ0
Main.energy = energy
widths=np.array([])

for i in radius:
    print(i)
    Main.radius = i
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

plt.scatter(radius*10**6,widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel("Core radius, $\si{\um}$")
plt.show()