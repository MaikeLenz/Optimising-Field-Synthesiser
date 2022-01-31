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


#Plotting.prop_2D(duv, :λ; modes=:sum, trange=(-20e-15, 20e-15), λrange=(150e-9, 1000e-9),
#                 dBmin=-30)

"""
#nothing is plotted
# plot the total time-dependent power at the end of the propagation:
Plotting.time_1D(duv; modes=:sum)
# plot the UV dispersive wave in the fundamental mode only
Plotting.time_1D(duv; modes=1, bandpass=(220e-9, 270e-9))
# plot the spectrogram of the pulse at the exit with a white background
Plotting.spectrogram(duv, flength; trange=(-20e-15, 30e-15), λrange=(150e-9, 1000e-9),
                     N=256, fw=3e-15, cmap=Plotting.cmap_white("viridis"))
"""

# retrieve the spectral energy density at the output
λ, Iλ = Processing.getIω(duv, :λ, flength)
#λ2, Eλ = Processing.getEt(duv, :λ, flength)
# plot the result
plt.figure()
plt.plot(λ*1e9, Iλ*1e-3, label="intensity")
#plt.plot(λ2*1e9, Eλ*1e-3, label="Et")
plt.xlim(200, 950)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral energy density (μJ/nm)")
plt.legend()
plt.ylim(ymin=0)
plt.show()