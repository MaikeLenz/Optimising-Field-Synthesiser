import numpy as np
import julia
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

def theoretical_width(radius, flength, pressure, λ0, τfwhm, energy, gas, transmission_fraction):
    """
    Returns theoretical calculation for SPM angular frequency width that comes from Luna simulation.
    Assumes Ne gas for now
    Still a factor of 10 out!!
    """

    c = 299792458 # m/s
    L = flength # m
    ω0 = 2*np.pi*c/λ0 # λ0 in m, ω0 in /s
    τ = τfwhm/(2*np.sqrt(2*np.log(2))) # τfwhm in s, τ in s
    power = energy/(np.sqrt(np.pi)*τ) # energy in J, power in J/s
    W0 = 0.64*radius # W0 in m, radius in m
    I0 = power/(np.pi*(W0**2))*transmission_fraction # I0 in J/s/m^2 

    # Get data for n2 from Luna
    Main.ω = ω0
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = pressure

    Main.eval('N0, n0, n2 = Tools.getN0n0n2(ω, gas; P=pressure, T=PhysData.roomtemp)')
    n2 = Main.n2 # n2 in m^2/W (probably)

    #get n2 from paper: https://link.springer.com/article/10.1007/s00340-013-5354-0
    #n2=(9.30 ± 0.25) × 10−21 cm2/W bar
    #n2=9.3e-21*pressure/10000 #convert to m^2/W

    #n2 for Argon:
    #(1.11 ± 0.05) × 10−19 cm2/W bar
    n2=1.11e-19*pressure/10000


    return 2*np.sqrt(2)*np.exp(-0.5)*ω0*n2*I0*L/(c*τ)

def theoretical_width_exp(radius, flength, energy, pressure, gas, dλ_rms, λ0):
    """
    Returns calculation for SPM angular frequency width from experimental parameters
    """
    c = 299792458 # m/s
    beta = (2*np.sqrt(2)*np.exp(-0.5)*(np.pi**-0.5)*(c**2))/((0.64**2)*(0.44**2))

    ω0 = 2*np.pi*c/λ0
    Main.ω = ω0
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = pressure
    Main.eval('N0, n0, n2 = Tools.getN0n0n2(ω, gas; P=pressure, T=PhysData.roomtemp)')
    n2 = Main.n2

    return (beta*n2*energy*flength*(dλ_rms**2))/((λ0**5)*(radius**2))

def theoretical_width_exp_error(radius, flength, energy, pressure, gas, dλ_rms, λ0, Δradius=0, Δflength=0, Δn2=0, Δenergy=0, Δdλ_rms=0, Δλ0=0):
    """
    Returns absolute error for calculation for SPM angular frequency width from experimental parameters, in units /s
    """
    c = 299792458 # m/s
    beta = (2*np.sqrt(2)*np.exp(-0.5)*(np.pi**-0.5)*(c**2))/((0.64**2)*(0.44**2))

    ω0 = 2*np.pi*c/λ0
    Main.ω = ω0
    Main.gas_str = gas
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = pressure
    Main.eval('N0, n0, n2 = Tools.getN0n0n2(ω, gas; P=pressure, T=PhysData.roomtemp)')
    n2 = Main.n2

    n2_err = (((beta*energy*flength*(dλ_rms**2))/((λ0**5)*(radius**2)))**2) * (Δn2**2)
    energy_err = (((beta*n2*flength*(dλ_rms**2))/((λ0**5)*(radius**2)))**2) * (Δenergy**2)
    flength_err = (((beta*n2*energy*(dλ_rms**2))/((λ0**5)*(radius**2)))**2) * (Δflength**2)
    dλ_rms_err = (((beta*n2*energy*flength*2*dλ_rms)/((λ0**5)*(radius**2)))**2) * (Δdλ_rms**2)
    λ0_err = (((5*beta*n2*energy*flength*(dλ_rms**2))/((λ0**6)*(radius**2)))**2) * (Δλ0**2)
    radius_err = (((2*beta*n2*energy*flength*(dλ_rms**2))/((λ0**5)*(radius**3)))**2) * (Δradius**2)

    #spm_width = theoretical_width_exp(radius, flength, energy, pressure, gas, dλ_rms, λ0)

    return np.sqrt(n2_err + energy_err + flength_err + dλ_rms_err + λ0_err + radius_err)