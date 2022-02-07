import numpy as np
import julia
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

def theoretical_width(flength, pressure, λ0, τfwhm, energy):
    """
    Returns theoretical calculation for SPM frequency width that comes from Luna simulation.
    Assumes Ne gas for now
    """

    c = 3*(10**8)
    L = flength
    I0 = energy**2
    ω0 = 2*np.pi*c/λ0
    τ = τfwhm/np.log(2)

    Main.ω = ω0
    gas = "Ne"
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = pressure

    # Get data for n2 from Luna
    Main.eval('N0, n0, n2 = Tools.getN0n0n2(ω, gas; P=pressure, T=PhysData.roomtemp)')

    n2 = Main.n2

    """
    # Right now this is just a rough estimate for n2, need an actual function
    if pressure <= 10*(10**(-3)):
        n2 = 0 * (10**(-19))
    elif pressure > 10*(10**(-3)) and pressure <= 100*(10**(-3)):
        n2 = 0.1 * (10**(-19))
    elif pressure > 100*(10**(-3)) and pressure <= 500*(10**(-3)):
        n2 = 0.8 * (10**(-19))
    elif pressure > 500*(10**(-3)):
        n2 = 1.3 * (10**(-19))
    """

    return 2*np.sqrt(2)*np.exp(-0.5)*ω0*n2*I0*L/(c*τ)