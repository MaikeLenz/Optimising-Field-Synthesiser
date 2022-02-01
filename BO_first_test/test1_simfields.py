import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

#list = [carrier_frequencies, fwhm_pulse_durations, field_amplitudes, CEPs, time_delays]

def E(t, carrier_freq, fwhm_duration, amp, CEP):
    sigma=fwhm_duration/(2.0*np.sqrt(2.0*np.log(2.0))) #fwhm to std of gaussian
    gauss = np.exp(-0.5*(t/sigma)**2.0)
    cos = np.cos(carrier_freq*t-CEP) #CEP is phase of cosine relative to gaussian
    return amp*gauss*cos

def sim_field_synth(t, N, list):
    #simulates field synthesis for arbitrary number of fields.
    #N=no.fields
    #first pulse centered at zero
    E_tot=0
    for i in range(N):
        delay1=(0,)+list[4] #delay of 1st pulse is zero
        #print(delay1)
        #print(type(delay1))
        E_i = E(t-delay1[i],list[0][i],list[1][i], list[2][i], list[3][i])
        #E_i = E(1,1,1,1,1)
        E_tot+=E_i
    return E_tot

pbounds_synth={}

list=[(633.0,635.0, 637.0),(10.0,10.0, 16.0),(1.0,3.0, 0.5),(0.0,1.0, 1.0),(10.0, 20.0)]
t=np.linspace(-20.0, 80.0, 500)
E_tot = []
for i in range(len(t)):
    #E_tot= sim_field_synth(t[i],2, list)
    E_i= sim_field_synth(t[i],2, list)
    E_tot.append(E_i)
plt.plot(t, np.array(E_tot))
plt.xlabel("time, t")
plt.ylabel("Electric field, a.u.")
plt.show()

"""
optimizer = BayesianOptimization(
    f=sim_field_synth,
    pbounds=pbounds_synth,
    verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

optimizer.maximize(
    init_points=100,
    n_iter= 100,
)


print(optimizer.max)
"""
