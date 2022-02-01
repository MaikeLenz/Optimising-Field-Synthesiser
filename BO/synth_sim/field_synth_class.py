import numpy as np
import matplotlib.pyplot as plt
from bayes_opt import BayesianOptimization
from scipy import integrate

#defines the Element base class, Wavepacket class for individual channels, and the synthesiser class.


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
    def __init__(self, t0=0.0, wavel=1000, fwhm=10.0, amp=1.0, CEP=0.0, freq=None):
        #define initial parameters
        self._t0 = t0 #in fs
        if freq != None:
            self._wavelength = (299.792458)/(freq) #in nm
        else:
            self._wavelength = wavel #in nm
        self._fwhm_duration = fwhm #in fs
        self._amplitude = amp #relative
        self._CEP = CEP 

    def Update(self, Synth, channel_index):
        #this is used to update the channel parameters, e.g. after the optimisation.
        self._wavelength=list(Synth._param_list[0])[channel_index-1]
        self._fwhm_duration=list(Synth._param_list[1])[channel_index-1]
        self._amplitude=list(Synth._param_list[2])[channel_index-1]
        self._CEP=list(Synth._param_list[3])[channel_index-1]
        delays=list(Synth._param_list[4])
        if delays[channel_index-1] == min(delays):
            self._t0=list(Synth._param_list[4])[channel_index-1]
        else:
            self._t0=list(Synth._param_list[4])[channel_index-1] + min(delays)

    def Energy(self,t):
        """
        returns the amount of energy in this channel, arbitrary units
        """
        I=np.array([])
        for time in t:
            I=np.append(I,(self.E_field_value(time))**2)
        return integrate.simps(I,t)

   
    def __str__(self):
        return "t0={}, freq={}, fwhm={}, amp={}, CEP={}".format(self._t0, self._wavelength, self._fwhm_duration, self._amplitude, self._CEP)

    def E_field_value(self, t):
        """
        calculates electric field of a cosinusoidal gaussian wavepacket at time t in fs; centered around zero
        """
        carrier_freq=(299.792458)/(self._wavelength)
        sigma=self._fwhm_duration/(2.0*np.sqrt(2.0*np.log(2.0))) #fwhm to std of gaussian
        gauss = np.exp(-0.5*((t-self._t0)/sigma)**2.0)
        cos = np.cos(carrier_freq*(t-self._t0)+self._CEP) #CEP is phase of cosine relative to gaussian
        return self._amplitude*gauss*cos

class Synthesiser(Element):
    """
    synthesises N amount of Wavepackets
    """
    def __init__(self, fields, delays):
        """
        generates list of tuples with parameter values, takes list of Wavepacket objects as input
        """
        self._pulse_list=fields #a list of the wavepacket objects that make up the synthesiser
        #list of tuples that holds the channel parameters = [carrier_frequencies, fwhm_pulse_durations, field_amplitudes, CEPs, time_delays]
        #create tuples that contain one parameter for each channel
        wavel=() 
        fwhm=()
        amp=()
        CEP=()
        for i in self._pulse_list: #append to the tuples
            wavel= wavel+(i._wavelength,)
            fwhm=fwhm+(i._fwhm_duration,)
            amp=amp+(i._amplitude,)
            CEP=CEP+(i._CEP,)
        if len(delays) != len(self._pulse_list)-1:
            raise "Error: Synthesiser not created successfully, dimension of delays doesn't match number of fields."
        delay1=(0,)+delays #delay of 1st pulse is zero
        list=[wavel,fwhm,amp,CEP,delay1] #list of tuples that hold the channel parameters
        self._param_list=list

    def E_field_value(self,t):
        """
        returns total electric field at time t, fs.
        """
        E_tot=0
        for i in range(len(self._pulse_list)):
            #iterate through channels and add the E field from each one
            wavel = self._param_list[0][i]
            freq=(299.792458)/(wavel)
            fwhm_duration = self._param_list[1][i]
            amp = self._param_list[2][i]
            CEP = self._param_list[3][i]
            delay = self._param_list[4][i]

            sigma=fwhm_duration/(2.0*np.sqrt(2.0*np.log(2.0))) #fwhm to std of gaussian
            gauss = np.exp(-0.5*((t-delay)/sigma)**2.0)
            cos = np.cos(freq*(t-delay)+CEP) #CEP is phase of cosine relative to gaussian
            E_tot += amp*gauss*cos
        return E_tot

    def Update(self, channel_index, wavel=None, fwhm=None, amp=None, CEP=None, delay=None):
        """
        Updates the parameter list attribute. Call this in the optimisation.
        have to convert tuples to lists and then back since tuples are immutable.
        Note: leaves original field objects as they were, only changes synthesiser object. To update channels, need to call their individual Update method
        """
        #goes through arguments and changes each one in th elist of tuples with channel paraneters
        if wavel != None:
            l0=list(self._param_list[0])
            l0[channel_index-1] = wavel
            self._param_list[0]=tuple(l0)
        if fwhm != None:
            l1=list(self._param_list[1])
            l1[channel_index-1] = fwhm
            self._param_list[1]=tuple(l1)
        if amp != None:
            l2=list(self._param_list[2])
            l2[channel_index-1] = amp
            self._param_list[2]=tuple(l2)
        if CEP != None:
            l3=list(self._param_list[3])
            l3[channel_index-1] = CEP
            self._param_list[3]=tuple(l3)
        if delay != None:
            l4= list(self._param_list[4])
            l4[channel_index-1] = delay
            self._param_list[4]=tuple(l4)

    def create_dict(self):
        """
        returns a dictionary of the parameters in the synthesiser and their values
        """
        param_dict = {}
        for i in range(len(self._param_list[0])):
            param_dict['wavel' + str(i+1)] = self._param_list[0][i]
        for i in range(len(self._param_list[1])):
            param_dict['fwhm' + str(i+1)] = self._param_list[1][i]
        for i in range(len(self._param_list[2])):
            param_dict['amp' + str(i+1)] = self._param_list[2][i]
        for i in range(len(self._param_list[3])):
            param_dict['CEP' + str(i+1)] = self._param_list[3][i]
        for i in range(len(self._param_list[4])):
            param_dict['delay' + str(i+1)] = self._param_list[4][i]
        return param_dict
   
    def no_of_channels(self):
        """
        returns the number of channels in the synthesiser
        """
        return len(self._pulse_list)

    def Energy_distr(self,t):
        """
        returns array with fraction of energy in each channel
        """
        energies=np.array([])
        for i in self._pulse_list:
            energies=np.append(energies,i.Energy(t))
        return energies / np.sum(energies)


#testing        
"""

t0=-10.0 #start time of first pulse in sequence
Field1=(Wavepacket(t0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0))
Field2=(Wavepacket(t0, wavel=800.0, fwhm=10.0, amp=1.0, CEP=np.pi))
Field3=(Wavepacket(t0, wavel=1300.0, fwhm=10.0, amp=1.0, CEP=np.pi))
Field4=(Wavepacket(t0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=np.pi))
pulses=[Field1,Field2,Field3, Field4]
delays=(10.0,20.0,50.0) #has to be tuple! each relative delay is measured from 1st pulse

Synth=(Synthesiser(pulses, delays))
#print(Synth.pulse_list)

plt.figure()
t=np.linspace(-20.0, 80.0, 5000)
E_tot = []
for i in range(len(t)):
    #create list of total electric field value at every t
    E_i= Synth.E_field_value(t[i])
    #E_i= Field2.E_field_value(t[i])
    E_tot.append(E_i)



plt.plot(t, np.array(E_tot))
plt.xlabel("time, t")
plt.ylabel("Electric field, a.u.")

Synth.Update(2,delay=40.0, amp=4.0)
plt.figure()
t=np.linspace(-20.0, 80.0, 1000)
E_tot = []
for i in range(len(t)):
    #create list of total electric field value at every t
    E_i= Synth.E_field_value(t[i])
    #E_i= Field2.E_field_value(t[i])
    E_tot.append(E_i)



plt.plot(t, np.array(E_tot))
plt.xlabel("time, t")
plt.ylabel("Electric field, a.u.")
plt.show()

"""
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
