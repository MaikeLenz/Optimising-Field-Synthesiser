using Luna
import PyPlot: plt

radius = 125e-6 # HCF core radius
flength = 1 # HCF length

gas = :Ne
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm

λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse


energy = 0.5e-3 # energy in the pump pulse

duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy,
                     #modes=4, trange=400e-15, λlims=(150e-9, 4e-6))
                    trange=400e-15, λlims=(150e-9, 4e-6))

#ω, Eω = Processing.getEω(duv, flength)
#grid = Grid.EnvGrid(flength, λ0, λlims=(150e-9, 4e-6), trange=400e-15)

grid = duv["grid"]
Eω = duv["Eω"]
peakpower(grid, Eω, λlims=(700e-9,800e-9))
#collect_stats(grid, Eω, peakpower)