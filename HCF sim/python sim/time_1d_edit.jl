using Luna
import Luna: Grid, Maths, PhysData, Processing
import Luna.PhysData: wlfreq, c, ε_0
import Luna.Output: AbstractOutput
import Luna.Processing: makegrid, getIω, getEω, getEt, nearest_z
import PyPlot: ColorMap, plt, pygui, Figure

function get_modes(output)
    t = output["simulation_type"]["transform"]
    !startswith(t, "TransModal") && return false, nothing
    lines = split(t, "\n")
    modeline = findfirst(li -> startswith(li, "  modes:"), lines)
    endline = findnext(li -> !startswith(li, " "^4), lines, modeline+1)
    mlines = lines[modeline+1 : endline-1]
    labels = [match(r"{([^,]*),", li).captures[1] for li in mlines]
    angles = parse.(Float64, [match(r"ϕ=([0-9]+.[0-9]+)π", li).captures[1] for li in mlines])
    if !all(angles .== 0)
        for i in eachindex(labels)
            if startswith(labels[i], "HE")
                if angles[i] == 0
                    θs = "y"
                elseif angles[i] == 0.5
                    θs = "x"
                else
                    θs = "$(angles[i])π"
                end
                labels[i] *= " ($θs)"
            end
        end
    end
    return true, labels
end

function power_unit(Pt, y=:Pt)
    units = ["kW", "MW", "GW", "TW", "PW"]
    Pmax = maximum(Pt)
    oom = clamp(floor(Int, log10(Pmax)/3), 1, 5) # maximum unit is PW
    powerfac = 1/10^(oom*3)
    if y == :Et
        sqrt(powerfac), "$(units[oom])\$^{1/2}\$"
    else
        return powerfac, units[oom]
    end
end    

function time_1D_edit_func(output, zslice=maximum(output["z"]);
        y=:Pt, modes=nothing,
        oversampling=4, trange=(-50e-15, 50e-15), bandpass=nothing,
        FTL=false, propagate=nothing, label="label",title="title",
        kwargs...)
    t, Et, zactual = getEt(output, zslice,
                trange=trange, oversampling=oversampling, bandpass=bandpass,
                FTL=FTL, propagate=propagate)
    if y == :Pt
        yt = abs2.(Et)
    elseif y == :Et
        yt = real(Et)
    elseif y == :Esq
        yt = real(Et).^2
    else
        error("unknown time plot variable $y")
    end
    multimode, modestrs = get_modes(output)
    if multimode
        if modes == :sum
            y == :Pt || error("Modal sum can only be plotted for power!")
            yt = dropdims(sum(yt, dims=2), dims=2)
            modestrs = join(modestrs, "+")
            nmodes = 1
        else
            isnothing(modes) && (modes = 1:length(modestrs))
            yt = yt[:, modes, :]
            modestrs = modestrs[modes]
            nmodes = length(modes)
        end
    end

    yfac, unit = power_unit(abs2.(Et), y)

    #sfig = plt.figure()
    if multimode && nmodes > 1
        _plot_slice_mm(plt.gca(), t*1e15, yfac*yt, zactual, modestrs; kwargs...)
    else
        #zs = [@sprintf("%.2f cm", zi*100) for zi in zactual]
        #label = multimode ? zs.*" ($modestrs)" : zs
        for iz in eachindex(zactual)
            plt.plot(t*1e15, yfac*yt[:, iz]; label=label, kwargs...)
        end
    end
    plt.title(title)
    plt.legend(frameon=false)
    #add_fwhm_legends(plt.gca(), "fs")
    plt.xlabel("Time (fs)")
    #plt.xlim(1e15.*trange)
    ylab = y == :Et ?  "Field ($unit)" : "Power ($unit)"
    plt.ylabel(ylab)
    #y == :Et || plt.ylim(ymin=0)
    #sfig.set_size_inches(8.5, 5)
    #sfig.tight_layout()
    #sfig
end

function run_sim(param, val)
    def = Dict("radius" => radius_0, 
                "pressure" => pressure_0, 
                "λ0" => λ0_0, 
                "τfwhm" => τfwhm_0, 
                "energy" => energy_0, 
                "flength" => flength_0)
    
    def[param] = val

    #for (key,val) in def
    #    println(key," = ", val)
    #end


    duv = prop_capillary(def["radius"], def["flength"], gas, def["pressure"]; 
                        λ0 = def["λ0"], τfwhm = def["τfwhm"], energy = def["energy"],
                        modes=4, trange=400e-15, λlims=(150e-9, 4e-6))

    return duv
end