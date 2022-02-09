import numpy as np
import julia
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

def theoretical_width(radius, flength, pressure, λ0, τfwhm, energy):
    """
    Returns theoretical calculation for SPM frequency width that comes from Luna simulation.
    Assumes Ne gas for now
    Still a factor of 10 out!!
    """

    c = 299792458 # m/s
    L = flength # m
    ω0 = 2*np.pi*c/λ0 # λ0 in m, ω0 in /s
    τ = τfwhm/(2*np.sqrt(np.log(2))) # τfwhm in s, τ in s
    power = energy/(np.sqrt(np.pi)*τ) # energy in J, power in J/s
    W0 = 0.64*radius # W0 in m, radius in m
    I0 = power/(np.pi*(W0**2)) # I0 in J/s/m^2 

    # Get data for n2 from Luna
    Main.ω = ω0
    gas = "Ne"
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = pressure
    Main.eval('N0, n0, n2 = Tools.getN0n0n2(ω, gas; P=pressure, T=PhysData.roomtemp)')
    n2 = Main.n2 # n2 in m^2/W (probably)

    return 2*np.sqrt(2)*np.exp(-0.5)*ω0*n2*I0*L/(c*τ)