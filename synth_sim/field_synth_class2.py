import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization

#list = [carrier_frequencies, fwhm_pulse_durations, field_amplitudes, CEPs, time_delays]


class Element:
    """
    abstract class 
    Base class for synthesised pulses
    """
    def __init__(self):
        self
        
class Wavepacket(Element):
    """
    Class of Elements which are fields
    """
    def __init__(self, t0=0.0, freq=633.0, fwhm=10.0, amp=1.0, CEP=0.0):
        self._t0 = t0
        self._carrier_freq = freq
        self._fwhm_duration = fwhm
        self._amplitude = amp
        self._CEP = CEP

        
    def __str__(self):
        return "t0={}, freq={}, fwhm={}, amp={}, CEP={}".format(self._t0, self._carrier_freq, self._fwhm_duration, self._amplitude, self._CEP)

    def E_field_value(self, t):
        """
        calculates electric field of a cosinusoidal gaussian wavepacket at time t in fs; centered around zero
        """
        sigma=self._fwhm_duration/(2.0*np.sqrt(2.0*np.log(2.0))) #fwhm to std of gaussian
        gauss = np.exp(-0.5*((t-self._t0)/sigma)**2.0)
        cos = np.cos(self._carrier_freq*(t-self._t0)-self._CEP) #CEP is phase of cosine relative to gaussian
        #print(amp*gauss*cos)
        return self._amplitude*gauss*cos

class Synthesiser(Element):
    """
    synthesises N amount of Wavepackets
    """
    def __init__(self, **attrs):
        self.__dict__.update(**attrs)

    def __getattr__(self, attr):
        return self.__dict__.get(attr, None)

    def generate(self, delays):
        """
        generates list of tuples with parameter values, takes list of Wavepacket objects as input
        """
        #list = [carrier_frequencies, fwhm_pulse_durations, field_amplitudes, CEPs, time_delays] list of tuples
        freq=()
        fwhm=()
        amp=()
        CEP=()
        for i in range(len(self.__dict__)):
            pulse_list=[]
        for i in self.pulse_list:
            #print(i._carrier_freq)
            freq= freq+(i._carrier_freq,)
            fwhm=fwhm+(i._fwhm_duration,)
            amp=amp+(i._amplitude,)
            CEP=CEP+(i._CEP,)
        delay1=(0,)+delays #delay of 1st pulse is zero
        list=[freq,fwhm,amp,CEP,delay1]
        #print(list)
        return list


    def E_field_value(self, delays):
        """
        returns total electric field at time t, fs.
        """
        list=self.generate(delays)
        E_tot=0
        for i in range(len(self.pulse_list)):
            E_i = self.pulse_list[i].E_field_value(t-list[4][i])
            E_tot+=E_i
        return E_tot
    
t0=-10.0 #start time of first pulse in sequence
Field1=(Wavepacket(t0, freq=633.0, fwhm=10.0, amp=1.0, CEP=0.0))
Field2=(Wavepacket(t0, freq=635.0, fwhm=10.0, amp=1.0, CEP=np.pi))
Field3=(Wavepacket(t0, freq=637.0, fwhm=10.0, amp=1.0, CEP=np.pi))
pulses=[Field1,Field2,Field3]
Synth=(Synthesiser(Field1,Field2,Field3))
delays=(10.0,20.0,) #has to be tuple! each relative delay is measured from 1st pulse
Synth.generate(delays)
#print(Synth.pulse_list)


t=np.linspace(-20.0, 20.0, 500)
E_tot = []
for i in range(len(t)):
    #create list of total electric field value at every t
    E_i= Synth.E_field_value(delays,t[i])
    #E_i= Field2.E_field_value(t[i])
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
