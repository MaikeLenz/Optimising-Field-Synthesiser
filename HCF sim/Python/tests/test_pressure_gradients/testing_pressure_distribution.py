import julia
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('tableau-colorblind10')
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 14

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

radius = 175e-6
flength = 1
gas = "Ne"
P=5
pressure1 = (0,P)
pressure2=(P,0)
pressure3=(2/3)*P
λ0 = 800e-9
τfwhm = 30e-15
energy = 2.5e-3

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure1
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
#Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
#Main.eval('t, Et = Processing.getEt(duv)')

λ = Main.λ
Iλ = Main.Iλ
#t = Main.t
#Et_allz=Main.Et #array of Et at all z 
#Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
#Et0=Et_allz[:,0] #first item in each element is pulse shape at the start

plt.plot(10**9*λ, Iλ, linewidth=2.0, label="0 to %s bar"%P)

#########################################################################################################################################
# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure2
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
#Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
#Main.eval('t, Et = Processing.getEt(duv)')

λ = Main.λ
Iλ = Main.Iλ
#t = Main.t
#Et_allz=Main.Et #array of Et at all z 
#Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
#Et0=Et_allz[:,0] #first item in each element is pulse shape at the start

plt.plot(10**9*λ, Iλ,label="%s to 0 bar"%P)

########################################################################################################
# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure3
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
#Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
#Main.eval('t, Et = Processing.getEt(duv)')

λ = Main.λ
Iλ = Main.Iλ
#t = Main.t
#Et_allz=Main.Et #array of Et at all z 
#Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
#Et0=Et_allz[:,0] #first item in each element is pulse shape at the start

plt.plot(10**9*λ, Iλ, '--', label="%s bar"%(round((2/3)*P,2)))

plt.xlabel("Wavelength, nm")
plt.ylabel("Intensity, a.u.")
plt.legend(fontsize=14)
plt.show()