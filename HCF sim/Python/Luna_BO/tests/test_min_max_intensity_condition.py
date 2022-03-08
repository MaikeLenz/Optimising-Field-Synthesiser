# test new min/max intensity condition
import numpy as np

import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

E = 100e-3 # energy, J
tau = 30e-15 # duration, fs
#a = 175e-6 # fibre radius, m
gas = "Ne"
λ = 800e-9
pressure = 5

Main.λ = λ
Main.gas_str = gas
Main.pressure = pressure
Main.eval("gas = Symbol(gas_str)")

Main.eval('ω = PhysData.wlfreq(λ)')
Main.eval('_, n0, n2  = Tools.getN0n0n2(ω, gas; P=pressure)')
Main.eval('Pcrit = Tools.Pcr(ω, n0, n2)')
Pcrit = Main.Pcrit

max_power = Pcrit
min_power = 0

P = E/(np.sqrt(np.pi)*tau)

print(P)
print(min_power <= P <= max_power)
print(int(min_power <= P <= max_power))