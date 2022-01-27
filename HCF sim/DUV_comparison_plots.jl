##################### parameters to vary user input
println("""\nDeclare which parameters to simulate for. \n
Possible inputs:
- radius
- flength
- pressure
- λ0
- τfwhm
- energy
- all (runs all parameters)

eg. "radius, pressure, tfwhm" """)

Possible_parameters = ("radius", "flength", "pressure", "λ0", "τfwhm", "energy")

num_params = 0

valid = false
while valid == false
    global input = readline()


    for i in Possible_parameters
        if occursin(i, input)
            println("\nsimulating for ", i)
            global num_params +=1
        end
    end

    if occursin("all", input)
        println("\nsimulating for all parameters")
        global num_params = 6
    end

    if num_params == 0
        println("\nNo parameters declared. Note to not use any capitcal letters")
    elseif num_params>0
        println("\n---parameters declared---")
        global valid = true
    end
end



##################### maximum variation user input

println("\nDeclare the maximum variation from the default values.
ie if set to 0.2, then parameters will be varied between 0.8 and 1.2 times the 
    default value")

nums = "1234567890.eE"
valid=false
while valid == false   
    global max_dif = readline()
    if any([!(i in nums) for i in max_dif])
        println("\nException: input must be a float")
    else
        max_dif = parse(Float64, max_dif)
        global valid=true
    end
end
println("\nMaximum Variation set as ", max_dif)

println("\n---inputs declared. Simulating starting---")

#################### Simulation

println("\n Importing Luna... \n")
using Luna
println("Luna Imported \n")

import PyPlot: plt, savefig #, pygui, Figure, ColorMap, 
include("time_1d_edit.jl")


#Default Values
radius_0 = 125e-6 # HCF core radius
flength_0 = 3 # HCF length
gas = :Ar
pressure_0 = 80e-3 # gas pressure in bar
λ0_0 = 800e-9 # central wavelength of the pump pulse
τfwhm_0 = 10e-15 # FWHM duration of the pump pulse
energy_0 = 60e-6 # energy in the pump pulse


increment = max_dif/5

parameters = Dict("radius" => [radius_0*(1-max_dif + increment*i) for i in 0:10], 
            "pressure" => [pressure_0*(1-max_dif + increment*i) for i in 0:10], 
            "λ0" => [λ0_0*(1-max_dif + increment*i) for i in 0:10], 
            "τfwhm" => [τfwhm_0*(1-max_dif + increment*i) for i in 0:10], 
            "energy" => [energy_0*(1-max_dif + increment*i) for i in 0:10], 
            "flength" => [flength_0*(1-max_dif + increment*i) for i in 0:10])


count = 1
total_iterations = 11*num_params

println("vars defined \n")


for (param, values) in parameters
    if occursin(param, input) || occursin("all", input)
        sfig = plt.figure()
        sfig.set_size_inches(10, 5)

        #plt.ylim([0,500])
        plt.xlim([-10,35])

        title = param

        println("initialising ", param, " simulations \n")

        for val in values

            println("\nInteration ", count, " of ", total_iterations, "\n")

            duv = run_sim(param, val)
                            
            time_1D_edit_func(duv; modes=1, bandpass=(220e-9, 270e-9), 
                                label=val, title=title)
            
            global count+=1



        end
        filename = "ComparisonPlots\\"*param*".png"
        savefig(filename)
    end
end