using Luna
import PyPlot: plt
import DSP: unwrap

λ0 = 800e-9
τfwhm = 30e-15
energy = 1.2e-3

a = 175e-6
flength = 1.05
gas = :Ne
pressure = 0.66*3

duv = prop_capillary(a, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))
ω, Eω = Processing.getEω(duv)


##
Plotting.time_1D(duv)

##
δω = ω[2] - ω[1] # sample spacing on the frequency axis
τ = π/δω # the centre of the time window

φraw = angle.(Eω[:, end]) # raw phase (no unwrapping or processing)
φ = unwrap(φraw - ω .* τ) # subtract the phase ramp and then unwrap
φ .-= φ[argmin(abs.(ω .- 2.4e15))] # subtract phase at central freq. (arbitrary)

plt.figure()
plt.plot(ω, abs2.(Eω[:, end]); color="k")
plt.xlim(1.5e15, 3.5e15)
plt.ylim(ymin=0)
plt.twinx()
plt.plot(ω, φ; color="r")
plt.ylim(-10, 10)
