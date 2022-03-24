import julia
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16
"""
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
"""
def P_gradient(z, P0, PL, L):
    """
    Defines pressure gradient for incompressible viscous fluid
    """
    return np.sqrt((P0**2) + (z/L)*((PL**2) - (P0**2)))
def P_average(Z, P):
    """
    Finds average pressure from a pressure gradient
    """
    norm_len = Z[-1] - Z[0]
    P_integrated = []
    for i in range(len(Z)-1):
        P0 = P[i]
        PL = P[i+1]
        L = Z[i+1] - Z[i]
        z = np.arange(0,-Z[i] +Z[i+1], L/100)
        Pz = P_gradient(z, P0, PL, L)
        P_integrated.append(integrate.simps(Pz, z))
    P_av = (np.sum(P_integrated)/norm_len)/(len(Z)-1)
    return P_av


def P_distribution(Z,P):
    P_integrand=np.array([])
    for i in range(len(Z)-1):
        P0 = P[i]
        PL = P[i+1]
        L = Z[i+1] - Z[i]
        z = np.arange(0,-Z[i] +Z[i+1], L/100)
        if PL<P0:
            Pz = P_gradient(z, PL, P0, L)[::-1]
        else:
            Pz = P_gradient(z, P0, PL, L)
        P_integrand=np.append(P_integrand,Pz)
    z=np.linspace(Z[0],Z[-1],len(P_integrand))
    return z,P_integrand


def P_avg(Z,P):
    """
    integrate over whole fibre to find average pressure
    """
    norm_len = Z[-1] - Z[0]
    P_integrand=np.array([])
    for i in range(len(Z)-1):
        P0 = P[i]
        PL = P[i+1]
        L = Z[i+1] - Z[i]
        z = np.arange(0,-Z[i] +Z[i+1], L/100)
        if PL<P0:
            Pz = P_gradient(z, PL, P0, L)[::-1]
        else:
            Pz = P_gradient(z, P0, PL, L)
        P_integrand=np.append(P_integrand,Pz)
    z=np.linspace(Z[0],Z[-1],len(P_integrand))
    P_integrated = integrate.simps(P_integrand, z)
    return P_integrated/norm_len


def P_average_manual(Z, P):
    P_integrated = []
    for i in range(len(Z)-1):
        P0 = P[i]
        PL = P[i+1]
        #L = Z[i+1] - Z[i]
        P_integrated.append((2/3)*((PL**2)**(3/2) - (P0**3))/((PL**2) - (P0**2)))
    P_av = np.sum(P_integrated)/(len(Z)-1)
    return P_av
"""
def P_average_manual2(Z,P):
    P_integrated = []
    for i in range(len(Z)-1):
        P0 = P[i]
        PL = P[i+1]
        #L = Z[i+1] - Z[i]
        P_integrated.append((P0/(1+PL**2/P0**2))*((2/3)*((2+PL**2/P0**2)**(3/2)-1)))
    P_av = np.sum(P_integrated)/(len(Z)-1)
    return P_av
"""
"""
P1 = 10
P2 = 5
P3 = 50
flength = 1.05
#print(P_average((0,flength/2,flength),(P1,P2,P3)))
#print(np.mean([P1,P2,P3]))
print(P_average((0,flength/2,flength),(P1,P2,P3)))
#print(np.mean([P1,P2,P3]))
print(P_average_manual((0,flength/2,flength),(P1,P2,P3)))
#print(P_average_manual2((0,flength/2,flength),(P1,P2,P3)))
print(P_avg((0,flength/2,flength),(P1,P2,P3)))

P1=0
P2=3
print(P_average((0,flength),(P1,P2)))
print(0.66*P2)
print(P_average_manual((0,flength),(P1,P2)))
#print(P_average_manual2((0,flength),(P1,P2)))
print(P_avg((0,flength),(P1,P2)))
"""
"""
radius = 175e-6
flength = 1.05
gas = "Ar"
λ0 = 800e-9
τfwhm = 30e-15
energy = 1.2e-3

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

P = 1
pressure1 = ((0,flength), (0,P))
pressure2 = ((0,flength), (0.66*P,0.66*P))
pressure3 = ((0,flength), (P,0))
"""
"""
pressure4_unnormalised = ((0,flength/2,flength), (0,3/2,3))
pressure4_array = []
for i in range(len(pressure4_unnormalised[1])):
    pressure4_array.append(pressure4_unnormalised[1][i]*0.66*3/P_average(pressure4_unnormalised[0], pressure4_unnormalised[1]))
pressure4 = ((0,flength/2,flength), (pressure4_array[0],pressure4_array[1],pressure4_array[2]))
print(P_average(pressure4[0], pressure4[1]))
"""
"""
Main.pressure = pressure1
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
plt.plot(λ*(10**9), Iλ, label='(0,P)')

Main.pressure = pressure2
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
plt.plot(λ*(10**9), Iλ, label='2/3*P')

Main.pressure = pressure3
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
plt.plot(λ*(10**9), Iλ, label='(P,0)')
"""
"""
Main.pressure = pressure4
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
Main.eval('t, Et = Processing.getEt(duv)')
λ = Main.λ
Iλ = Main.Iλ
plt.plot(λ, Iλ, label='(0,P/2,P)')
"""
"""
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (a.u.)')
plt.legend(fontsize=16)
plt.show()
"""
"""
z=np.linspace(0,10,100)
P1=P_gradient(z,1,2,10)
P2=P_gradient(z,0,1,10)+1
plt.plot(z,P1,label="P1")
plt.plot(z,P2,label="P2")
plt.legend()
plt.show()
"""